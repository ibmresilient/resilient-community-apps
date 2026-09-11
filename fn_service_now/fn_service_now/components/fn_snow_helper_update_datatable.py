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
        self.inputs = inputs
        self.res_id = None
        self.row_id = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_snow_helper_update_datatable"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_snow_helper_update_datatable")
    def _fn_snow_helper_update_datatable_function(self, event, *args, **kwargs):
        """Function: A helper function that updates the ServiceNow Records Data Table when the status of an Incident/Task is changed."""

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["incident_id", "sn_resilient_status"], kwargs)

        # Get the function inputs:
        inputs = {
            # number (required)
            "incident_id": kwargs.get("incident_id"),
            # number (optional)
            "task_id": kwargs.get("task_id"),
            # text (required)
            "sn_resilient_status": kwargs.get("sn_resilient_status"),
        }

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        # Instantiate new SOAR API object
        res_client = self.rest_client()

        # Instantiate a reference to the ServiceNow Datatable
        res_datatable = ServiceNowRecordsDataTable(
            res_client, payload.inputs["incident_id"])

        # Get the datatable data and rows
        res_datatable.get_data()

        # Generate the res_id
        payload.res_id = res_helper.generate_res_id(
            payload.inputs["incident_id"], payload.inputs["task_id"])

        # Search for a row that contains the res_id
        row_found = res_datatable.get_row(
            "sn_records_dt_res_id", payload.res_id)

        # Get current time (*1000 as API does not accept int)
        now = int(time() * 1000)

        if row_found:

            resilient_status = res_helper.state_to_text(
                payload.inputs.get("sn_resilient_status"))

            yield StatusMessage(f"Row found for {payload.res_id}. Updating resilient_status to {resilient_status}")

            resilient_status = res_helper.convert_text_to_richtext(resilient_status, SN_STATE_COLOR_MAP.get(resilient_status, "red"))

            cells_to_update = {
                "sn_records_dt_time": now,
                "sn_records_dt_res_status": resilient_status
            }

            # Update the row
            update_row_response = res_datatable.update_row(
                row_found, cells_to_update)
            payload.row_id = update_row_response["id"]

        else:
            payload.success = False
            err_msg = "No row found for the {0} {1}"

            if payload.inputs["task_id"]:
                err_msg = err_msg.format("Task", payload.inputs["task_id"])

            else:
                err_msg = err_msg.format(
                    "Incident", payload.inputs["incident_id"])

            yield StatusMessage(err_msg)

        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
