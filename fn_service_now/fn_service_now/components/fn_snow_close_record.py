# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.sn_ref_id = None
        self.sn_record_state = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_close_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_close_record")
    def _fn_snow_close_record_function(self, event, *args, **kwargs):
        """Function: Function that uses the '/close_record' custom endpoint in ServiceNow to change the state of a ServiceNow Record and add Close Notes and a Close Code to the Record."""

        err_msg = None

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number (optional)
                "sn_res_id": res_helper.get_function_input(kwargs, "sn_res_id", True),  # number (optional)
                "sn_record_state": res_helper.get_function_input(kwargs, "sn_record_state"),  # number (required)
                "sn_close_notes": res_helper.get_function_input(kwargs, "sn_close_notes", True),  # text (optional)
                "sn_close_code": res_helper.get_function_input(kwargs, "sn_close_code", True),  # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the datatable and its data
            datatable = ServiceNowRecordsDataTable(res_client, payload.inputs["incident_id"])

            # Generate the res_id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"], payload.inputs["sn_res_id"])

            # Get the sn_ref_id
            sn_ref_id = datatable.get_sn_ref_id(res_id)

            if not sn_ref_id:
                payload.success = False
                err_msg = "Failed to close this {0} in ServiceNow. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

                if payload.inputs["task_id"]:
                    err_msg = err_msg.format("Task", payload.inputs["task_id"])

                else:
                    err_msg = err_msg.format("Incident", payload.inputs["incident_id"])

                raise ValueError(err_msg)

            else:
                # Generate the request_data
                request_data = {
                    "sn_ref_id": sn_ref_id,
                    "sn_table_name": res_helper.SN_TABLE_NAME,
                    "sn_close_code": payload.inputs["sn_close_code"],
                    "sn_close_notes": payload.inputs["sn_close_notes"],
                    "sn_record_state": payload.inputs["sn_record_state"]
                }

                try:
                    yield StatusMessage("Closing ServiceNow Record {0}".format(sn_ref_id))
                    close_in_sn_response = res_helper.sn_api_request("POST", "/close_record", data=json.dumps(request_data))
                    payload.sn_ref_id = sn_ref_id
                    payload.sn_record_state = close_in_sn_response["sn_state"]

                except Exception as err:
                    payload.success = False
                    raise ValueError("Failed to close ServiceNow Record {0}".format(err))

                try:
                    yield StatusMessage("Updating ServiceNow Records Data Table Status to {0}".format(close_in_sn_response["sn_state"]))

                    row_to_update = datatable.get_row("sn_records_dt_sn_ref_id", sn_ref_id)

                    cells_to_update = {
                        "sn_records_dt_time": int(time.time() * 1000),
                        "sn_records_dt_snow_status": res_helper.convert_text_to_richtext(close_in_sn_response["sn_state"], "red")
                    }

                    # Update the row
                    datatable.update_row(row_to_update, cells_to_update)

                except Exception as err:
                    payload.success = False
                    raise ValueError("Failed to update ServiceNow Status in Datatable: {0}".format(err))

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
