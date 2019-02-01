# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper
from fn_service_now.util.external_ticket_status_datatable import ExternalTicketStatusDatatable


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
    """Component that implements Resilient function 'sn_utilities_update_datatable"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_update_datatable")
    def _sn_utilities_update_datatable_function(self, event, *args, **kwargs):
        """Function: Function that updates the ServiceNow Datatable when an Incident/Task is added/updated"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number (optional)
                "sn_resilient_status": res_helper.get_function_input(kwargs, "sn_resilient_status"),  # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Instansiate a reference to the ServiceNow Datatable
            res_datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Get the datatable data and rows
            res_datatable.get_data()

            # Generate the res_id
            payload.res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Search for a row that contains the res_id
            row_found = res_datatable.get_row("sn_records_dt_res_id", payload.res_id)

            # Get current time (*1000 as API does not accept int)
            now = int(time.time() * 1000)

            if row_found:

                resilient_status = res_helper.state_to_text(payload.inputs.get("sn_resilient_status"))

                yield StatusMessage("Row found for {0}. Updating resilient_status to {1}".format(
                    payload.res_id, resilient_status))

                if resilient_status == "Active":
                    resilient_status = res_helper.convert_text_to_richtext("Active", "green")

                else:
                    resilient_status = res_helper.convert_text_to_richtext("Closed", "red")

                cells_to_update = {
                    "sn_records_dt_time": now,
                    "sn_records_dt_res_status": resilient_status
                }

                # Update the row
                update_row_response = res_datatable.update_row(row_found, cells_to_update)
                payload.row_id = update_row_response["id"]

            else:
                payload.success = False
                err_msg = "No row found for the {0} {1}"

                if payload.inputs["task_id"]:
                    err_msg = err_msg.format("Task", payload.inputs["task_id"])

                else:
                    err_msg = err_msg.format("Incident", payload.inputs["incident_id"])

                yield StatusMessage(err_msg)

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
