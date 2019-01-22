# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper
from fn_service_now.util.external_ticket_status_datatable import ExternalTicketStatusDatatable


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
    """Component that implements Resilient function 'sn_utilities_add_attachment_to_servicenow_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_add_attachment_to_servicenow_record")
    def _sn_utilities_add_attachment_to_servicenow_record_function(self, event, *args, **kwargs):
        """Function: A function that adds a Resilient Attachment to a ServiceNow Record."""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "attachment_id": res_helper.get_function_input(kwargs, "attachment_id"),  # number (required)
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True)  # number (optional)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the attachment
            attachment = res_helper.get_attachment(res_client,
                                                   payload.inputs["attachment_id"],
                                                   payload.inputs["incident_id"],
                                                   payload.inputs["task_id"])

            # Get the datatable
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Generate res_id using incident and task id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Get the sn_ref_id from the datatable
            sn_ref_id = datatable.get_sn_ref_id(res_id)

            if not sn_ref_id:
                payload.success = False
                err_msg = "Failed to add Attachment to ServiceNow. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

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
                    "type": "attachment",
                    "attachment_base64": attachment["contents"],
                    "attachment_name": attachment["name"],
                    "attachment_content_type": attachment["content_type"]
                }

                yield StatusMessage("Add Attachment to ServiceNow")

                # Call POST and get response
                add_in_sn_response = res_helper.sn_POST("/add", data=json.dumps(request_data))
                payload.res_id = res_id
                payload.sn_ref_id = sn_ref_id
                payload.attachment_name = attachment["name"]
                payload.sn_attachment_sys_id = add_in_sn_response["attachment_id"]

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
