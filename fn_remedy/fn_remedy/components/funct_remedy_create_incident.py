# -*- coding: utf-8 -*-
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError, template_functions
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError, clean_html
from fn_remedy.lib.remedy.RemedyAPIClient import RemedyClient
from fn_remedy.lib.datatable.data_table import Datatable
import json
from pathlib import Path
from datetime import datetime

PACKAGE_NAME = "fn_remedy"
FN_NAME = "remedy_create_incident"
TABLE_NAME = "remedy_linked_incidents_reference_table"

# fields we want Remedy to return when creating an incident
RETURN_FIELDS = ["Incident Number", "Request ID"]
# form name corresponding to a Remedy Incident
FORM_NAME = "HPD:IncidentInterface_Create"
# jinja template for remedy payload
TEMPLATE = Path(__file__).parent.parent.parent / "./data/templates/_remedy_incident_template.jinja2"

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
                self.fn_options
            )

            yield StatusMessage("Validations complete. Starting business logic")

            # get optional settings
            port = self.fn_options.get("port", None)
            verify = self.fn_options.get("verify", "true").lower() == "true"

            # get function inputs
            remedy_payload = kwargs.get("remedy_payload")
            remedy_payload = json.loads(remedy_payload.get("content"))

            # From the payload, build a values dict from only the information provided.
            # If the field was left blank, we leave it blank in order to give priority to templating.
            values = {}
            for key, value in remedy_payload.items():
                if (key != "additional_data" and value):
                    values[key] = value

            # get the additional data
            # this must be valid json so we can load it into a dict
            additional_data = None
            if remedy_payload.get("additional_data").get("content"):
                try:
                    additional_data = json.loads(remedy_payload["additional_data"]["content"])
                except json.decoder.JSONDecodeError:
                    LOG.error(u"Exception when converting %s to json. Incident will be raised without additional_data."
                              "" % remedy_payload["additional_data"]["content"])

            # TODO - do we even need jinja?? seems like extra steps since all we are doing is building a dict...
            # map the additional data to the jinja template
            # if additional_data:
            #     additional_data = self.map_values(TEMPLATE, values)
            #     # update values with the jinja result
            #     values.update(additional_data)

            # add the key, value pairs in additional data to the values dict
            if additional_data:
                values.update(additional_data)

            # required metadata field to create a resource
            values["z1D_Action"] = "CREATE"

            # resilient incident_id
            incident_id = kwargs.get("incident_id")
            # resilient task id
            task_id = kwargs.get("task_id")

            # instantiate a resilient API client
            # get the incident and task data
            resilientClient = self.rest_client()
            incident = resilientClient.get("/incidents/{0}".format(incident_id))
            task = resilientClient.get("/tasks/{0}".format(task_id))

            if task.get("instructions"):
                # set the short description to the task instructions
                # short description is the biggest text field we have available to us
                short_desc = clean_html(task["instructions"])
                # max length is 254
                if len(short_desc) > 254:
                    short_desc = short_desc[:254]
            else:
                short_desc = "."
            # add it to the values dict
            values["Short Description"] = short_desc

            # add the task name to the description if one wasn't provided
            if not values.get("Description"):
                values["Description"] = "CP4S Case " + str(incident_id) + ": " + task["name"]
            # description has a max length of 100
            if len(values.get("Description", "")) > 100:
                values["Description"] = values["Description"][:100]

            # instantiate a RemedyClient
            client = RemedyClient(app_configs["remedy_host"], app_configs["remedy_user"],
                                  app_configs["remedy_password"], rc, port=port, verify=verify
            )

            LOG.info(u"Incident values to POST:\n{0}".format(str(values)))

            results = []

            while not results:
                # POST an incident to Remedy
                try:
                    remedy_incident, status_code = client.create_form_entry(
                        FORM_NAME, values, return_values=RETURN_FIELDS
                    )
                except Exception as e:
                    results = rp.done(False, e, reason="Request resulted in an error from the Remedy API.")

                # 201 is returned for resource created
                if status_code != 201:
                    # unexpected response from Remedy
                    reason = "Expected 201 - resource created response from Remedy. Received {0}".format(status_code)
                    results = rp.done(False, remedy_incident)

                # capture the Incident Number and Request ID
                incident_number = remedy_incident["values"]["Incident Number"]
                request_id = remedy_incident["values"]["Request ID"]

                # instantiate a datatable client
                dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
                # add the task and its associated Remedy data to the lookup table
                row = {
                    "timestamp": {"value": int(datetime.now().timestamp() * 1000)}, # convert to mills and discard fractions of a second
                    "taskincident_id": {"value": str(task_id) + ": " + task["name"]},
                    "remedy_id": {"value": request_id},
                    "status": {"value": values["Status"]},
                    "extra": {"value": ''}
                }
                LOG.debug("Adding row to the remedy_linked_incidents_reference_table DataTable: {0}".format(row))
                dt_response = dt.dt_add_rows(row)

                results = rp.done(True, remedy_incident)

            # pass the task back to Resilient to use in the post-script if we were successful
            results["content"]["task"] = task if results["success"] else None

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as e:
            yield FunctionError(e)
