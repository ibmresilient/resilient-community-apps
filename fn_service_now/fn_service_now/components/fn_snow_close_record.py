# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from time import time
from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields
from fn_service_now.util.resilient_helper import SN_STATE_COLOR_MAP, CONFIG_DATA_SECTION, ResilientHelper
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.reason = None
        self.inputs = inputs
        self.sn_ref_id = None
        self.sn_record_state = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_snow_close_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_snow_close_record")
    def _fn_snow_close_record_function(self, event, *args, **kwargs):
        """Function: Function that uses the '/close_record' custom endpoint in ServiceNow to change the state of a ServiceNow Record and add Close Notes and a Close Code to the Record."""

        err_msg = None

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["incident_id", "sn_record_state"], kwargs)

        # Get the function inputs:
        inputs = {
            # number (required)
            "incident_id": kwargs.get("incident_id", None),
            # number (optional)
            "task_id": kwargs.get("task_id", None),
            # number (optional)
            "sn_res_id": kwargs.get("sn_res_id", None),
            # number (required)
            "sn_record_state": kwargs.get("sn_record_state", None),
            # text (optional)
            "sn_close_notes": kwargs.get("sn_close_notes", None),
            # text (optional)
            "sn_close_code": kwargs.get("sn_close_code", None),
            # text (optional)
            "sn_close_work_note": kwargs.get("sn_close_work_note", None)
        }

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        # Instantiate new SOAR API object
        res_client = self.rest_client()

        # Get the datatable and its data
        datatable = ServiceNowRecordsDataTable(
            res_client, inputs.get("incident_id", None))

        # Generate the res_id
        res_id = res_helper.generate_res_id(
            inputs.get("incident_id", None), inputs.get("task_id", None), inputs.get("sn_res_id", None))

        # Get the sn_ref_id
        sn_ref_id = datatable.get_sn_ref_id(res_id)

        # Get the table name reference from the datatable
        sn_table_name = datatable.get_sn_table_name(res_id)

        if not sn_ref_id:
            err_msg = "Failed to close this {0} in ServiceNow. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

            if inputs.get("task_id", None):
                err_msg = err_msg.format("Task", inputs.get("task_id", None))

            else:
                err_msg = err_msg.format(
                    "Incident", inputs.get("incident_id", None))

            payload.success = False
            payload.reason = err_msg
            yield StatusMessage(err_msg)

        else:
            # Generate the request_data
            request_data = {
                "sn_ref_id": sn_ref_id,
                "sn_table_name": res_helper.get_table_name(sn_table_name),
                "sn_close_code": inputs.get("sn_close_code", None),
                "sn_close_notes": inputs.get("sn_close_notes", None),
                "sn_record_state": inputs.get("sn_record_state", None),
                "sn_close_work_note": inputs.get("sn_close_work_note", None)
            }

            yield StatusMessage(f"Closing ServiceNow Record {sn_ref_id}")
            close_in_sn_response = res_helper.sn_api_request("POST", "/close_record", data=request_data)
            sn_record_state = close_in_sn_response["sn_state"]
            payload.sn_ref_id = sn_ref_id
            payload.sn_record_state = sn_record_state

            try:
                yield StatusMessage(f"Updating ServiceNow Records Data Table Status to {sn_record_state}")

                row_to_update = datatable.get_row(
                    "sn_records_dt_sn_ref_id", sn_ref_id)

                color = SN_STATE_COLOR_MAP.get(sn_record_state, "red")

                cells_to_update = {
                    "sn_records_dt_time": int(time() * 1000),
                    "sn_records_dt_snow_status": res_helper.convert_text_to_richtext(sn_record_state, color)
                }

                # Update the row
                datatable.update_row(row_to_update, cells_to_update)

            except Exception as err:
                payload.success = False
                raise ValueError(f"Failed to update ServiceNow Status in Datatable: {err}") from err

        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
