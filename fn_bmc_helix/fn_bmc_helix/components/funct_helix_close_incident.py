# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from ast import literal_eval
from logging import getLogger
from fn_bmc_helix.lib.datatable.data_table import Datatable
from fn_bmc_helix.lib.helix.HelixAPIClient import HelixClient
from fn_bmc_helix.lib.helix.HelixConstants import PACKAGE_NAME, TABLE_NAME
from resilient_lib import validate_fields, IntegrationError, clean_html
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function, FunctionError)

FN_NAME = "helix_close_incident"
MAX_ROWS = 30  # Override option available in app.config as max_datatable_rows

# Form name corresponding to a Helix Incident
FORM_NAME = "HPD:IncidentInterface"
# Status values that indicate closure
CLOSED_LIST = ["Resolved", "Closed", "Cancelled"]

LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'helix_close_incident''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Override MAX_ROWS if provided in app.config
        self.max_rows = int(self.options.get("max_datatable_rows", MAX_ROWS))

    def close_helix_incident(self, incident_id, task, helix_client, helix_payload):
        """Performs the work of closing (updating) an incident in BMC Helix and updating the
        corresponding row in the SOAR data table. If the incident is already closed,
        the status value on the incident is not changed and we only update the status
        on the SOAR side.

        :param incident_id: SOAR case id
        :type incident_id: int
        :param task: SOAR task data
        :type task: dict
        :param helix_client: BMC Helix API client
        :type helix_client: HelixClient
        :param helix_payload: Key value pairs to update on the BMC Helix incident
        :type helix_payload: dict
        :return: The results of the method, boolean if successful, string of reason not successful
        :rtype: dict, boolean, string
        """
        skipped, closed = [], []
        if task:
            rows = self.get_dt_rows(incident_id, task)
            if not rows:
                LOG.info(f'Task {task["id"]}: {task["name"]} not found in the BMC Helix datatable. Incidents in BMC Helix will be left unchanged.')
                return {"skipped": skipped, "closed": closed}, False, "No record of escalating to BMC Helix"

            if len(rows) > 1:
                LOG.info(f"Multiple datatable rows found matching task {task['id']}: {task['name']}.\n"
                        "Any incidents matching these rows in BMC Helix will be closed.")
            # Handle multiple rows
            for row in rows:
                # Get BMC Helix UUID from the table
                request_id = row.get("cells", {}).get("helix_request_id")["value"]
                # Get the BMC Helix incident
                try:
                    incident, _ = helix_client.get_form_entry(FORM_NAME, request_id)
                except IntegrationError as e:
                    if e.value.find("404 Client Error: Not Found") > -1:
                        # 404 - The incident was probably deleted
                        LOG.info(f"Unable to find Request ID {request_id} in BMC Helix. It may have been deleted. Continuing to the next ID.")
                    else:
                        # Unknown error case - the helix_payload supplied might have a bad key
                        LOG.error(f"Received error response from BMC Helix when attempting to close Request ID {request_id}.\n"
                                "Check your helix_payload input to ensure it matches the HPD:IncidentInterface_Create schema.\n"
                                "Continuing to the next ID.")
                    skipped.append(incident)
                    continue  # Move on to the next row
                # Close the incident if not already closed
                closed, skipped = self.update_helix_incident_values(helix_client, closed, skipped, incident, helix_payload)
                self.update_datatable_row(row["id"], {"helix_status": "Closed"}, incident_id)

        return {"closed": closed, "skipped": skipped}, True, None

    def update_datatable_row(self, row_id, row, incident_id):
        """Updates the values of a row in a SOAR data table

        :param row_id: Target id of the data table row
        :type row_id: int
        :param row: The values to update on the row
        :type row: dict
        :param incident_id: Incident the datatable is associated with
        :type incident_id: int
        """
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        dt.update_row(row_id, row)

    def update_helix_incident_values(self, helix_client, closed, skipped, incident, helix_payload):
        """Updates the values dictionary of a BMC Helix incident to indicate the incident is closed.

        :param helix_client: BMC Helix API client
        :type helix_client: HelixClient
        :param closed: Previously closed request ID's
        :type closed: list
        :param skipped: Previously skipped request ID's
        :type skipped: list
        :param incident: BMC Helix incident
        :type incident: dict
        :param helix_payload: Values to update on the BMC Helix incident
        :type helix_payload: dict
        :return: Updated list of request ID's that have been closed or skipped
        :rtype: list, list
        """
        request_id = incident["values"]["Request ID"]
        if incident["values"]["Status"] not in CLOSED_LIST:
            if not helix_payload.get("Status"): # If status not given set to Resolved
                helix_payload["Status"] = "Resolved"
            if not helix_payload.get("Status_Reason"): # If Status_Reason not given set to No Further Action Required
                helix_payload["Status_Reason"] = "No Further Action Required"
            if not helix_payload.get("Resolution"): # If Resolution not given set to Closed from IBM SOAR
                helix_payload["Resolution"] = "Closed from IBM SOAR"
            else: # Remove html from Resolution
                helix_payload["Resolution"] = clean_html(helix_payload.get("Resolution"))
            incident, _ = helix_client.update_form_entry(FORM_NAME, request_id, helix_payload)
            closed.append(incident)
            LOG.info(f"Successfully closed Request ID {request_id}")
        else:
            skipped.append(incident)
            LOG.info(f"Request ID {request_id} already closed, resolved, or cancelled. Skipping this incident.")
        return closed, skipped

    def get_dt_rows(self, incident_id, task):
        """Gets rows from a SOAR datatable. Rows matching a query
        string concatenated from the task ID and name are returned

        :param incident_id: SOAR case id
        :type incident_id: int
        :param task: SOAR task data
        :type task: dict
        :return: Matched rows from the datatable
        :rtype: dict
        """
        # Instantiate a datatable client
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        # Query the rows
        rows = dt.get_rows(max_rows=self.max_rows, search_column="soar_task_id",
                           search_value=f'{str(task["id"])}: {task["name"]}')
        return rows

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Close an incident ticket in BMC Helix"""
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Validate app configs
            validate_fields([
                {"name": "helix_host", "placeholder": "<example.domain>"},
                {"name": "helix_user", "placeholder": "<example_user>"},
                {"name": "helix_password", "placeholder": "xxx"}],
                self.options)

            yield self.status_message("Validations complete. Starting business logic")

            # Get function inputs
            helix_payload = getattr(fn_inputs, "helix_payload", "{}")
            helix_payload = literal_eval(helix_payload)
            incident_id = getattr(fn_inputs, "incident_id")
            bmc_helix_request_id = getattr(fn_inputs, "bmc_helix_request_id", None)
            task_id = getattr(fn_inputs, "task_id", None)
            task = None

            if not task_id and not bmc_helix_request_id:
                raise ValueError("Either task_id or bmc_helix_request_id must be given.")

            # Instantiate a HelixClient
            client = HelixClient(self.options.get("helix_host"),
                                 self.options.get("helix_user"),
                                 self.options.get("helix_password"),
                                 self.rc,
                                 port=self.options.get("helix_port"),
                                 verify=self.rc.get_verify())

            if task_id: # If run from a BMC Helix linked SOAR task
                # Get the task data
                task = self.rest_client().get(f"/tasks/{task_id}")
                results, success, reason = self.close_helix_incident(incident_id, task, client, helix_payload)
            else: # If run from a BMC Helix linked SOAR case
                incident, _ = client.get_form_entry(FORM_NAME, bmc_helix_request_id)
                # Close the incident if not already closed
                closed, skipped = self.update_helix_incident_values(client, [], [], incident, helix_payload)
                results = {"closed": closed, "skipped": skipped}
                success = True
                reason = None

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results, success=success, reason=reason)
        except Exception as e:
            yield FunctionError(e)
