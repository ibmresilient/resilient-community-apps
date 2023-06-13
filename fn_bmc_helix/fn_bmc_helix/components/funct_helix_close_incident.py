# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from json import loads
from os.path import isfile
from datetime import datetime
from logging import getLogger
from fn_bmc_helix.lib.datatable.data_table import Datatable
from fn_bmc_helix.lib.helix.HelixAPIClient import HelixClient
from fn_bmc_helix.lib.helix.HelixConstants import PACKAGE_NAME, TABLE_NAME
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

FN_NAME = "helix_close_incident"
MAX_ROWS = 30  # Override option available in app.config as max_datatable_rows

# Form name corresponding to a Helix Incident
FORM_NAME = "HPD:IncidentInterface"
# Status values that indicate closure
CLOSED_LIST = ["Resolved", "Closed", "Cancelled"]

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'helix_close_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        # Override MAX_ROWS if provided in app.config
        self.max_rows = int(self.options.get("max_datatable_rows", MAX_ROWS))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    def close_helix_incident(self, incident_id, task, helix_client, rp, helix_payload):
        """Performs the work of closing (updating) an incident in BMC Helix and updating the
        corresponding row in the SOAR data table. If the incident is already closed,
        the status value on the incident is not changed and we only update the status
        on the SOAR side.

        :param incident_id: SOAR incident id
        :type incident_id: int
        :param task: SOAR task data
        :type task: dict
        :param helix_client: BMC Helix API client
        :type helix_client: HelixClient
        :param rp: Result payload object
        :type rp: ResultPayload
        :param helix_payload: Key value pairs to update on the BMC Helix incident
        :type helix_payload: dict
        :return: The results of the method
        :rtype: ResultPayload
        """
        skipped, closed = [], []

        rows = self.get_dt_rows(incident_id, task)
        if not rows:
            LOG.info(f'Task {task["id"]}: {task["name"]} not found in the BMC Helix datatable. Incidents in BMC Helix will be left unchanged.')
            return rp.done(False, {"skipped": skipped, "closed": closed}, "No record of escalating to BMC Helix")

        if len(rows) > 1:
            LOG.info(f"Multiple datatable rows found matching task {task['id']}: {task['name']}.\n"
                     "Any incidents matching these rows in BMC Helix will be closed.")
        # Handle multiple rows
        for row in rows:
            # Get BMC Helix UUID from the table
            request_id = row["cells"]["helix_id"]["value"]
            # Get the BMC Helix incident
            try:
                incident, _ = helix_client.get_form_entry(
                    FORM_NAME, request_id)
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
            closed, skipped = self.update_incident_values(
                helix_client, closed, skipped, incident, helix_payload)
            updated_row = {"status": "Closed", "timestamp": int(
                datetime.now().timestamp() * 1000)}
            self.update_datatable_row(row["id"], updated_row, incident_id)

        return rp.done(True, {"closed": closed, "skipped": skipped})

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

    def update_incident_values(self, helix_client, closed, skipped, incident, helix_payload):
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
            helix_payload["Status"] = "Resolved"
            helix_payload["Status_Reason"] = "No Further Action Required"
            helix_payload["Resolution"] = "Closed from IBM SOAR"
            incident, _ = helix_client.update_form_entry(
                FORM_NAME, request_id, helix_payload)
            closed.append(incident)
            LOG.info(f"Successfully closed Request ID {request_id}")
        else:
            skipped.append(incident)
            LOG.info(f"Request ID {request_id} already closed, resolved, or cancelled. Skipping this incident.")
        return closed, skipped

    def get_dt_rows(self, incident_id, task):
        """Gets rows from a SOAR datatable. Rows matching a query
        string concatenated from the task ID and name are returned

        :param incident_id: SOAR incident id
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
        rows = dt.get_rows(max_rows=self.max_rows, search_column="taskincident_id",
                           search_value=f'{str(task["id"])}: {task["name"]}')
        return rows

    @function(FN_NAME)
    def _helix_close_incident_function(self, event, *args, **kwargs):
        """Function: Close an incident ticket in BMC Helix"""
        try:
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage(f"Starting '{FN_NAME}' running in workflow '{wf_instance_id}'")

            # Get and validate app configs
            app_configs = validate_fields([
                {"name": "helix_host", "placeholder": "<example.domain>"},
                {"name": "helix_user", "placeholder": "<example_user>"},
                {"name": "helix_password", "placeholder": "xxx"}],
                self.options)

            yield StatusMessage("Validations complete. Starting business logic")

            # Get optional settings
            port = self.options.get("helix_port", None)

            # If verify setting in the app.config is not set then defaults to true
            verify = self.options.get("verify", "true")
            # Check if verify in the app.config is a path to a certificate
            if not isfile(verify):
                # If verify setting in the app.config is not equal to False then it is set to True
                verify = False if verify.lower() in ('0', 'false', 'no', 'off') else True

            # Get function inputs
            helix_payload = kwargs.get("helix_payload")
            helix_payload = loads(helix_payload)
            incident_id = kwargs.get("incident_id")
            task_id = kwargs.get("task_id")

            # Instantiate a SOAR API client
            # Get the task data
            task = self.rest_client().get(f"/tasks/{task_id}")

            # Instantiate a HelixClient
            client = HelixClient(app_configs["helix_host"], app_configs["helix_user"],
                                 app_configs["helix_password"], rc, port=port, verify=verify)

            results = self.close_helix_incident(
                incident_id, task, client, rp, helix_payload)

            yield StatusMessage(f"Finished '{FN_NAME}' that was running in workflow '{wf_instance_id}'")
            LOG.info(f"'{FN_NAME}' complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
