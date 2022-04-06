# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Function implementation"""

import logging
import json
from datetime import datetime
from os.path import isfile

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError, str_to_bool
from fn_remedy.lib.remedy.RemedyAPIClient import RemedyClient
from fn_remedy.lib.datatable.data_table import Datatable

PACKAGE_NAME = "fn_remedy"
FN_NAME = "remedy_close_incident"
TABLE_NAME = "remedy_linked_incidents_reference_table"
MAX_ROWS = 30 # Override option available in app.config as max_datatable_rows

# Fields we want Remedy to return when creating an incident
RETURN_FIELDS = ["Incident Number", "Request ID"]
# Form name corresponding to a Remedy Incident
FORM_NAME = "HPD:IncidentInterface"
# Status values that indicate closure
CLOSED_LIST = ["Resolved", "Closed", "Cancelled"]

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'remedy_close_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})
        # Override MAX_ROWS if provided in app.config
        self.max_rows = int(self.fn_options.get("max_datatable_rows", MAX_ROWS))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    def close_remedy_incident(self, incident_id, task, remedy_client, rp, remedy_payload):
        """Performs the work of closing (updating) an incident in Remedy and updating the
        corresponding row in the SOAR data table. If the incident is already closed,
        the status value on the incident is not changed and we only update the status
        on the SOAR side.

        :param incident_id: SOAR incident id
        :type incident_id: int
        :param task: SOAR task data
        :type task: dict
        :param remedy_client: remedy API client
        :type remedy_client: RemedyClient
        :param rp: result payload object
        :type rp: ResultPayload
        :param remedy_payload: key value pairs to update on the remedy incident
        :type remedy_payload: dict
        :return: the results of the method
        :rtype: ResultPayload
        """

        skipped, closed = [], []

        rows = self.get_dt_rows(incident_id, task)
        if not rows:
            LOG.info("Task %s: %s not found in the Remedy datatable. Incidents in Remedy will be left unchanged.",
                    task["id"], task["name"])
            return rp.done(False, {"skipped": skipped, "closed": closed}, "No record of escalating to Remedy")

        if len(rows) > 1:
            LOG.info("Multiple datatable rows found matching task %s: %s.\n"
                     "Any incidents matching these rows in Remedy will be closed.", task["id"], task["name"])
        # handle multiple rows
        for row in rows:
            # get remedy UUID from the table
            request_id = row["cells"]["remedy_id"]["value"]
            # get the remedy incident
            try:
                incident, _ = remedy_client.get_form_entry(FORM_NAME, request_id)
            except IntegrationError as e:
                if e.value.find("404 Client Error: Not Found") > -1:
                    # 404 - the incident was probably deleted
                    LOG.info("Unable to find Request ID %s in Remedy. It may have been deleted. Continuing to the next ID.",
                             request_id)
                else:
                    # unknown error case - the remedy_payload supplied might have a bad key
                    LOG.error("Received error response from Remedy when attempting to close Request ID %s.\n"
                          "Check your remedy_payload input to ensure it matches the HPD:IncidentInterface_Create schema.\n"
                          "Continuing to the next ID.", request_id)
                skipped.append(incident)
                continue # move on to the next row
            # close the incident if not already closed
            closed, skipped = self.update_incident_values(remedy_client, closed, skipped, incident, remedy_payload)
            updated_row = {"status": "Closed", "timestamp": int(datetime.now().timestamp() * 1000)}
            self.update_datatable_row(row["id"], updated_row, incident_id)

        return rp.done(True, {"closed": closed, "skipped": skipped})

    def update_datatable_row(self, row_id, row, incident_id):
        """Updates the values of a row in a SOAR data table

        :param row_id: target id of the data table row
        :type row_id: int
        :param row: the values to update on the row
        :type row: dict
        :param incident_id: incident the datatable is associated with
        :type incident_id: int
        """
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        dt.update_row(row_id, row)
        return

    def update_incident_values(self, remedy_client, closed, skipped, incident, remedy_payload):
        """Updates the values dictionary of a remedy incident to indicate the incident is closed.

        :param remedy_client: remedy API client
        :type remedy_client: RemedyClient
        :param closed: previously closed request ID's
        :type closed: list
        :param skipped: previously skipped request ID's
        :type skipped: list
        :param incident: remedy incident
        :type incident: dict
        :param remedy_payload: values to update on the remedy incident
        :type remedy_payload: dict
        :return: updated list of request ID's that have been closed or skipped
        :rtype: list, list
        """
        request_id = incident["values"]["Request ID"]
        if incident["values"]["Status"] not in CLOSED_LIST:
            remedy_payload["Status"] = "Resolved"
            remedy_payload["Status_Reason"] = "No Further Action Required"
            remedy_payload["Resolution"] = "Closed from IBM SOAR"
            incident, _ = remedy_client.update_form_entry(FORM_NAME, request_id, remedy_payload)
            closed.append(incident)
            LOG.info("Successfully closed Request ID %s", request_id)
        else:
            skipped.append(incident)
            LOG.info("Request ID %s already closed, resolved, or cancelled. Skipping this incident.", request_id)
        return closed, skipped

    def get_dt_rows(self, incident_id, task):
        """Gets rows from a SOAR datatable. Rows matching a query
        string concatenated from the task ID and name are returned

        :param incident_id: SOAR incident id
        :type incident_id: int
        :param task: SOAR task data
        :type task: dict
        :return: matched rows from the datatable
        :rtype: dict
        """
        # instantiate a datatable client
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        # query the rows
        rows = dt.get_rows(max_rows=self.max_rows, search_column="taskincident_id",
                           search_value=str(task["id"]) + ": " + task["name"])
        return rows

    @function(FN_NAME)
    def _remedy_close_incident_function(self, event, *args, **kwargs):
        """Function: Close an incident ticket in Remedy"""
        try:
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting '{0}' running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            # Get and validate app configs
            app_configs = validate_fields([
                {"name": "remedy_host", "placeholder": "<example.domain>"},
                {"name": "remedy_user", "placeholder": "<example_user>"},
                {"name": "remedy_password", "placeholder": "xxx"}],
                self.fn_options)

            yield StatusMessage("Validations complete. Starting business logic")

            # get optional settings
            port = self.fn_options.get("remedy_port", None)
            verify = self.fn_options.get("verify", "true")
            if not isfile(verify):
                verify = str_to_bool(verify)

            # get function inputs
            remedy_payload = kwargs.get("remedy_payload")
            remedy_payload = json.loads(remedy_payload)
            incident_id = kwargs.get("incident_id")
            task_id = kwargs.get("task_id")

            # instantiate a SOAR API client
            # get the task data
            task = self.rest_client().get("/tasks/{0}".format(task_id))

            # instantiate a RemedyClient
            client = RemedyClient(app_configs["remedy_host"], app_configs["remedy_user"],
                                  app_configs["remedy_password"], rc, port=port, verify=verify)

            results = self.close_remedy_incident(incident_id, task, client, rp, remedy_payload)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))
            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
