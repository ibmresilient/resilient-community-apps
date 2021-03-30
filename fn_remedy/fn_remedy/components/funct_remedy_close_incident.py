# -*- coding: utf-8 -*-
"""Function implementation"""

import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError, str_to_bool
from fn_remedy.lib.remedy.RemedyAPIClient import RemedyClient
from fn_remedy.lib.datatable.data_table import Datatable

PACKAGE_NAME = "fn_remedy"
FN_NAME = "remedy_close_incident"
TABLE_NAME = "remedy_linked_incidents_reference_table"

# fields we want Remedy to return when creating an incident
RETURN_FIELDS = ["Incident Number", "Request ID"]
# form name corresponding to a Remedy Incident
FORM_NAME = "HPD:IncidentInterface_Create"
# status values that indicate closure
CLOSED_LIST = ["Resolved", "Closed", "Cancelled"]

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'remedy_close_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    def close_remedy_incident(self, incident_id, task, remedy_client, rp, remedy_payload):

        skipped, closed = [], []

        rows = self.get_dt_rows(incident_id, task)
        if not rows:
            LOG.info("Task {0}: {1} not found in the Remedy datatable. Incidents in Remedy will be left unchanged.")
            return rp.done(True, {"skipped": skipped, "closed": closed}, "No record of escalating to Remedy")

        if len(rows) > 1:
            LOG.info("Multiple datatable rows found matching task {0}: {1}.\n"
                     "Any incidents matching these rows in Remedy will be closed.".format(task["id"], task["name"]))
        # handle multiple rows
        for row in rows:
            # get remedy UUID from the table
            request_id = row["cells"]["remedy_id"]["value"]
            # get the remedy incident
            try:
                incident, status_code = remedy_client.get_form_entry(FORM_NAME, request_id)
            except IntegrationError as e:
                if e.value.find("404 Client Error: Not Found") > -1:
                    # 404 - the incident was probably deleted
                    LOG.info("Unable to find Request ID {0} in Remedy. It may have been deleted. Continuing to the next ID.")
                else:
                    # unknown error case - the remedy_payload supplied might have a bad key
                    LOG.error("Received error response from Remedy when attempting to close Request ID {0}.\n"
                          "Check your remedy_payload input to ensure it matches the HPD:IncidentInterface_Create schema.\n"
                          "Continuing to the next ID.".format(request_id))
                skipped.append(request_id)
                continue # move on to the next row
            # close the incident if not already closed
            closed, skipped = self.update_incident_values(remedy_client, closed, skipped, incident, request_id, remedy_payload)
            updated_row = {"status": "Closed", "timestamp": int(datetime.now().timestamp() * 1000)}
            self.update_datatable_row(row["id"], updated_row, incident_id)

        return rp.done(True, {"closed": closed, "skipped": skipped})

    def update_datatable_row(self, row_id, row, incident_id):
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        dt.update_row(row_id, row)
        return

    def update_incident_values(self, remedy_client, closed, skipped, incident, request_id, remedy_payload):
        if incident["values"]["Status"] not in CLOSED_LIST:
            remedy_payload["Status"] = "Closed"
            incident, _ = remedy_client.update_form_entry(FORM_NAME, request_id, remedy_payload)
            closed.append(request_id)
            LOG.info("Successfully close Request ID {0}".format(remedy_payload))
        else:
            skipped.append(request_id)
            LOG.info("Request ID {0} aready closed, resolved, or cancelled. Skipping this incident.".format(request_id))
        return closed, skipped

    def get_dt_rows(self, incident_id, task):
        # instantiate a datatable client
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        dt.get_data()
        # query the rows
        rows = dt.get_rows(max_rows=10, search_column="taskincident_id",
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
            port = self.fn_options.get("port", None)
            verify = str_to_bool(self.fn_options.get("verify", "true"))

            # get function inputs
            remedy_payload = kwargs.get("remedy_payload")
            remedy_payload = json.loads(remedy_payload.get("content"))
            incident_id = kwargs.get("incident_id")
            task_id = kwargs.get("task_id")

            # instantiate a resilient API client
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
