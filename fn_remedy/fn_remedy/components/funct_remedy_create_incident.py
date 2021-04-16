# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Function implementation"""

import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError, template_functions
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError, clean_html, str_to_bool
from fn_remedy.lib.remedy.RemedyAPIClient import RemedyClient
from fn_remedy.lib.datatable.data_table import Datatable


PACKAGE_NAME = "fn_remedy"
FN_NAME = "remedy_create_incident"
TABLE_NAME = "remedy_linked_incidents_reference_table"

# fields we want Remedy to return when creating an incident
RETURN_FIELDS = ["Incident Number", "Request ID"]
# form name corresponding to a Remedy Incident
FORM_NAME = "HPD:IncidentInterface_Create"
ENTRY_NAME = "HPD:IncidentInterface"

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'remedy_create_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @staticmethod
    def parse_additional_data(remedy_payload, values):
        """Parses the additional data parameter provided in the workflow.
        Adds the additional_data key:value pairs to the values dict
        we build to send to Remedy.

        :param remedy_payload: remedy_payload kwarg passes from the workflow
        :param values: dict of values we build to send to Remedy
        :return: updated values dict
        """
        if remedy_payload.get("additional_data").get("content"):
            try:
                additional_data = json.loads(remedy_payload["additional_data"]["content"])
            except json.decoder.JSONDecodeError:
                LOG.error(
                    u"Exception when converting %s to json. Incident will be raised without additional_data."
                    "" % remedy_payload["additional_data"]["content"])
                return values
            values.update(additional_data)
        return values

    def add_dt_row(self, incident_id, task, values):
        """Adds a row to the datatable correlating the Resilient task
        to the Remedy incident.

        :param incident_id: Resilient incident ID
        :param task: task dictionary payload from Resilient
        :param values: dictionary of Remedy Incident values
        :return: Resilient's response to the datatable request
        """
        # instantiate a datatable client
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        # add the task and its associated Remedy data to the lookup table
        row = {
            # convert to mills and discard fractions of a second
            "timestamp": {"value": int(datetime.now().timestamp() * 1000)},
            "taskincident_id": {u"value": "{0}: {1}".format(task["id"], task["name"])},
            "remedy_id": {"value": values["Request ID"]},
            "status": {"value": values["Status"]},
            "extra": {"value": values["Incident Number"]}
        }
        LOG.info(u"Adding row to the remedy_linked_incidents_reference_table DataTable: {0}".format(row))
        dt_response = dt.dt_add_rows(row)
        LOG.debug(u"Response from the Resilient Datatable API:\n{0}".format(dt_response))
        return dt_response

    def post_incident_to_remedy(self, remedy_client, rp, values, incident_id, task):
        """POSTs a new incident to the Remedy AR server.
        If Remedy rejects the request or we get an unexpected status code,
        we return a ResultsPayload object with success=False.
        Otherwise, we return a ResultsPayload with success=True
        and the incident payload returned under results["content"]
        :param remedy_client: RemedyClient object
        :param rp: ResultsPayload object
        :param values: values dict to send to Remedy
        :param incident_id: Resilient incident ID
        :param task: task dict from Resilient
        :return: ResultsPayload.done
        """
        # POST an incident to Remedy
        try:
            remedy_incident, status_code = remedy_client.create_form_entry(
                FORM_NAME, values, return_values=RETURN_FIELDS)
        except IntegrationError as e:
            LOG.error("POST request to Remedy resulted in an error. Ensure all required Remedy fields were provided.")
            return rp.done(False, {"error": e.value}, reason="Request resulted in an error from the Remedy API.")

        # 201 is returned for resource created
        if status_code != 201:
            # unexpected response from Remedy
            LOG.error("Received an unexpected status code from Remedy. Expected 201, but got {0}".format(status_code))
            reason = "Expected 201 - resource created response from Remedy. Received {0}".format(status_code)
            return rp.done(False, remedy_incident)

        LOG.info("Incident successfully posted to Remedy.")
        # capture the Incident Number
        # note this is a temporary number for the request to create a new entry
        # and this value will be reassigned to reflect the true value
        # by getting the newly created object from Remedy
        incident_number = remedy_incident["values"]["Incident Number"]

        # get the newly created form entry object
        entries, status_code = remedy_client.query_form_entry(ENTRY_NAME, incident_number)
        entry = entries["entries"][0]
        # save the incident number so we can log it. this is the ID that shows in the Remedy UI
        incident_number = entry["values"]["Incident Number"]
        # save the request id so we can log it. this is the ID that shows in the Remedy API
        request_id = entry["values"]["Request ID"]
        # we expect only one result to be returned
        if len(entries["entries"]) > 1:
            LOG.debug("Multiple form entries in Remedy found matching Incident Number: {0}."
                      "The Request ID of the first entry will be written to the datatable.".format(incident_number))

        LOG.info("Correlated Request ID {0} to Incident Number {1}".format(request_id, incident_number))

        dt_response = self.add_dt_row(incident_id, task, entry["values"])

        results = rp.done(True, entry)
        # pass the task back to Resilient to use in the post-script if we were successful
        results["content"]["task"] = task
        return results

    @function(FN_NAME)
    def _remedy_create_incident_function(self, event, *args, **kwargs):
        """Function: Create a new incident in Remedy"""
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
            verify = str_to_bool(self.fn_options.get("verify", "true"))

            # get function inputs
            remedy_payload = kwargs.get("remedy_payload")
            remedy_payload = json.loads(remedy_payload.get("content"))

            # From the payload, build a values dict from only the information provided.
            # If the field was left blank, we leave it blank in order to give priority to templating.
            values = {**remedy_payload}
            del values["additional_data"]

            # add the additional data to the values dict
            values = self.parse_additional_data(remedy_payload, values)

            # required metadata field to create a resource
            values["z1D_Action"] = "CREATE"

            # resilient incident_id
            incident_id = kwargs.get("incident_id")
            # resilient task id
            task_id = kwargs.get("task_id")

            # instantiate a resilient API client
            resilientClient = self.rest_client()
            # get the incident and task data
            incident = resilientClient.get("/incidents/{0}".format(incident_id))
            task = resilientClient.get("/tasks/{0}".format(task_id))

            # add task instructions to the values dict if present in the task
            if task.get("instructions"):
                # set the description to the task instructions
                # detailed description is the biggest text field we have available to us
                desc = clean_html(task["instructions"])
                # add it to the values dict
                # remedy has a typo in their API, the below is correct
                values["Detailed_Decription"] = desc

            # add the task name to the description if one wasn't provided in the inputs
            if not values.get("Description"):
                values["Description"] = u"IBM SOAR Case {0}: {1}".format(incident_id, task["name"])
            # description has a max length of 100
            if len(values.get("Description", "")) > 100:
                values["Description"] = values["Description"][:100]

            # instantiate a RemedyClient
            client = RemedyClient(app_configs["remedy_host"], app_configs["remedy_user"],
                                  app_configs["remedy_password"], rc, port=port, verify=verify)

            LOG.info(u"Incident values to POST:\n{0}".format(values))

            results = self.post_incident_to_remedy(client, rp, values, incident_id, task)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as e:
            yield FunctionError(e)
