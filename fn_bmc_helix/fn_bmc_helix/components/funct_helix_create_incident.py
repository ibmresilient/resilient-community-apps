# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from json import loads
from os.path import isfile
from datetime import datetime
from logging import getLogger
from fn_bmc_helix.lib.datatable.data_table import Datatable
from fn_bmc_helix.lib.helix.HelixAPIClient import HelixClient
from fn_bmc_helix.lib.helix.HelixConstants import PACKAGE_NAME, TABLE_NAME, RETURN_FIELDS
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError, clean_html
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

FN_NAME = "helix_create_incident"
# Form name corresponding to a BMC Helix Incident
FORM_NAME = "HPD:IncidentInterface_Create"
ENTRY_NAME = "HPD:IncidentInterface"

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'helix_create_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    def add_dt_row(self, incident_id, task, values):
        """Adds a row to the datatable correlating the SOAR task
        to the BMC Helix incident.

        :param incident_id: SOAR incident ID
        :param task: Task dictionary payload from SOAR
        :param values: Dictionary of BMC Helix Incident values
        :return: SOAR's response to the datatable request
        """
        # Instantiate a datatable client
        dt = Datatable(self.rest_client(), incident_id, TABLE_NAME)
        # Add the task and its associated BMC Helix data to the lookup table
        row = {
            # Convert to mills and discard fractions of a second
            "timestamp": {"value": int(datetime.now().timestamp() * 1000)},
            "taskincident_id": {"value": f'{task["id"]}: {task["name"]}'},
            "helix_id": {"value": values["Request ID"]},
            "status": {"value": values["Status"]},
            "extra": {"value": values["Incident Number"]}
        }
        LOG.info(f"Adding row to the helix_linked_incidents_reference_table DataTable: {row}")
        dt_response = dt.dt_add_rows(row)
        LOG.debug(f"Response from the SOAR Datatable API:\n{dt_response}")
        return dt_response

    def post_incident_to_helix(self, helix_client, rp, values, incident_id, task):
        """POSTs a new incident to the BMC Helix AR server.
        If BMC Helix rejects the request or we get an unexpected status code,
        we return a ResultsPayload object with success=False.
        Otherwise, we return a ResultsPayload with success=True
        and the incident payload returned under results["content"]
        :param helix_client: HelixClient object
        :param rp: ResultsPayload object
        :param values: Values dict to send to BMC Helix
        :param incident_id: SOAR incident ID
        :param task: task dict from SOAR
        :return: ResultsPayload.done
        """
        # POST an incident to BMC Helix
        try:
            helix_incident, status_code = helix_client.create_form_entry(
                FORM_NAME, values, return_values=RETURN_FIELDS)
        except IntegrationError as e:
            LOG.error(
                "POST request to BMC Helix resulted in an error. Ensure all required BMC Helix fields were provided.")
            return rp.done(False, {"error": e.value}, reason="Request resulted in an error from the BMX Helix API.")

        # 201 is returned for resource created
        if status_code != 201:
            # Unexpected response from BMC Helix
            reason = f"Expected 201 - resource created response from BMC Helix. Received {status_code}"
            LOG.error(reason)
            return rp.done(False, helix_incident, reason=reason)

        LOG.info("Incident successfully posted to BMC Helix.")
        # Capture the Incident Number
        # Note this is a temporary number for the request to create a new entry
        # and this value will be reassigned to reflect the true value
        # by getting the newly created object from BMC Helix
        incident_number = helix_incident["values"]["Incident Number"]

        # Get the newly created form entry object
        entries, status_code = helix_client.query_form_entry(ENTRY_NAME, incident_number)
        entry = entries["entries"][0]
        # Save the incident number so we can log it. This is the ID that shows in the BMC Helix UI
        incident_number = entry["values"]["Incident Number"]
        # Save the request id so we can log it. This is the ID that shows in the BMC Helix API
        request_id = entry["values"]["Request ID"]
        # We expect only one result to be returned
        if len(entries["entries"]) > 1:
            LOG.debug(f"Multiple form entries in BMC Helix found matching Incident Number: {incident_number}."
                      "The Request ID of the first entry will be written to the datatable.")

        LOG.info(f"Correlated Request ID {request_id} to Incident Number {incident_number}")

        self.add_dt_row(incident_id, task, entry["values"])

        results = rp.done(True, entry)
        # Pass the task back to SOAR to use in the post-script if we were successful
        results["content"]["task"] = task
        return results

    @function(FN_NAME)
    def _helix_create_incident_function(self, event, *args, **kwargs):
        """Function: Create a new incident in BMC Helix"""
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

            # Add in the additional data
            addl_data = helix_payload.pop("additional_data")
            addl_data and helix_payload.update(addl_data)

            # Required metadata field to create a resource
            helix_payload["z1D_Action"] = "CREATE"

            # SOAR incident_id
            incident_id = kwargs.get("incident_id")
            # SOAR task id
            task_id = kwargs.get("task_id")

            # Instantiate a SOAR API client
            resilientClient = self.rest_client()
            # Get the task data
            task = resilientClient.get(f"/tasks/{task_id}")

            # Add task instructions to the helix_payload dict if present in the task
            if task.get("instructions"):
                # Set the description to the task instructions
                # Detailed description is the biggest text field we have available to us
                desc = clean_html(task["instructions"])
                # Add it to the helix_payload dict
                # BMC Helix has a typo in their API, the below is correct
                helix_payload["Detailed_Decription"] = desc

            # Add the task name to the description if one wasn't provided in the inputs
            if not helix_payload.get("Description"):
                helix_payload["Description"] = f"IBM SOAR Case {incident_id}: {task['name']}"
            # Description has a max length of 100
            if len(helix_payload.get("Description", "")) > 100:
                helix_payload["Description"] = helix_payload["Description"][:100]

            # Instantiate a HelixClient
            client = HelixClient(app_configs["helix_host"], app_configs["helix_user"],
                                 app_configs["helix_password"], rc, port=port, verify=verify)

            LOG.info(f"Incident values to POST:\n{helix_payload}")

            results = self.post_incident_to_helix(
                client, rp, helix_payload, incident_id, task)

            yield StatusMessage(f"Finished '{FN_NAME}' that was running in workflow '{wf_instance_id}'")

            LOG.info(f"'{FN_NAME}' complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as e:
            yield FunctionError(e)
