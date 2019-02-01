# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from bs4 import BeautifulSoup
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

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_add_note_to_servicenow_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_add_note_to_servicenow_record")
    def _sn_utilities_add_note_to_servicenow_record_function(self, event, *args, **kwargs):
        """Function: A function that adds a Resilient Note to a ServiceNow record as either a 'Work Note' or 'Additional Comment'"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number
                "sn_note_text": res_helper.get_function_input(kwargs, "sn_note_text"),  # text (required)
                "sn_note_type": res_helper.get_function_input(kwargs, "sn_note_type")["name"]  # select, text (required)
            }

            # Convert rich text comment to plain text
            soup = BeautifulSoup(inputs["sn_note_text"], 'html.parser')
            soup = soup.get_text()
            inputs["sn_note_text"] = soup.replace(u'\xa0', u' ')

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the datatable
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Generate res_id using incident and task id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Get the sn_ref_id
            sn_ref_id = datatable.get_sn_ref_id(res_id)

            if not sn_ref_id:
                payload.success = False
                err_msg = "Failed to add Note. This {0} has not been created in ServiceNow yet. {0} ID: {1}"

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
                    "type": "comment",
                    "sn_note_text": payload.inputs["sn_note_text"],
                    "sn_note_type": payload.inputs["sn_note_type"]
                }

                yield StatusMessage("Adding Note to ServiceNow Record {0}".format(sn_ref_id))

                # Call POST and get response
                add_in_sn_response = res_helper.sn_POST("/add", data=json.dumps(request_data))
                payload.res_id = res_id
                payload.sn_ref_id = add_in_sn_response["sn_ref_id"]

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
