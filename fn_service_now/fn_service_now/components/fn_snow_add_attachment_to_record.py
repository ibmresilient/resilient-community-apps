# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger

from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields

from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)
from fn_service_now.util.sn_records_dt import ServiceNowRecordsDataTable


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.res_id = None
        self.sn_ref_id = None
        self.attachment_name = None
        self.sn_attachment_sys_id = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_add_attachment_to_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_add_attachment_to_record")
    def _fn_snow_add_attachment_to_record_function(self, event, *args, **kwargs):
        """Function: Function that adds a Resilient Attachment to a ServiceNow Record."""

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["attachment_id", "incident_id"], kwargs)

        # Get the function inputs:
        inputs = {
            # number (required)
            "attachment_id": kwargs.get("attachment_id"),
            # number (required)
            "incident_id": kwargs.get("incident_id"),
            # number (optional)
            "task_id": kwargs.get("task_id")
        }

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        # Instantiate new Resilient API object
        res_client = self.rest_client()

        yield StatusMessage(f"Getting attachment data. ID: {payload.inputs['attachment_id']}")

        # Get the attachment
        attachment = res_helper.get_attachment(res_client,
                                                payload.inputs["attachment_id"],
                                                payload.inputs["incident_id"],
                                                payload.inputs["task_id"])

        # Get the datatable
        datatable = ServiceNowRecordsDataTable(
            res_client, payload.inputs["incident_id"])

        # Generate res_id using incident and task id
        res_id = res_helper.generate_res_id(
            payload.inputs["incident_id"], payload.inputs["task_id"])

        # Get the sn_ref_id from the datatable
        sn_ref_id = datatable.get_sn_ref_id(res_id)

        # Get the table name reference from the datatable
        sn_table_name = datatable.get_sn_table_name(res_id)

        if not sn_ref_id:
            payload.success = False
            err_msg = "Failed to add Attachment to ServiceNow. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

            if payload.inputs["task_id"]:
                err_msg = err_msg.format("Task", payload.inputs["task_id"])

            else:
                err_msg = err_msg.format(
                    "Incident", payload.inputs["incident_id"])

            raise ValueError(err_msg)

        else:
            # Generate the request_data
            request_data = {
                "sn_ref_id": sn_ref_id,
                "sn_table_name": res_helper.get_table_name(sn_table_name),
                "type": "attachment",
                "attachment_base64": attachment["contents"],
                "attachment_name": attachment["name"],
                "attachment_content_type": attachment["content_type"]
            }

            yield StatusMessage(f"Adding Attachment to ServiceNow Record {sn_ref_id}")

            # Call POST and get response
            add_in_sn_response = res_helper.sn_api_request("POST", "/add", data=request_data)
            payload.res_id = res_id
            payload.sn_ref_id = sn_ref_id
            payload.attachment_name = attachment["name"]
            payload.sn_attachment_sys_id = add_in_sn_response["attachment_id"]

        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
