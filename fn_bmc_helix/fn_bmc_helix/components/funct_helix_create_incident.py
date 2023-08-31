# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from json import loads
from fn_bmc_helix.lib.helix.HelixAPIClient import HelixClient
from fn_bmc_helix.lib.helix.HelixConstants import PACKAGE_NAME
from resilient_lib import validate_fields, IntegrationError, clean_html
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function, FunctionError)

FN_NAME = "helix_create_incident"
# Form name corresponding to a BMC Helix Incident
FORM_NAME = "HPD:IncidentInterface_Create"
ENTRY_NAME = "HPD:IncidentInterface"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'helix_create_incident''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    def post_incident_to_helix(self, helix_client, values):
        """POSTs a new incident to the BMC Helix AR server.
        If BMC Helix rejects the request or we get an unexpected status code,
        we send FunctionResults with success=False and return nothing.
        Otherwise, we return the BMC Helix entry information as a dict.
        :param helix_client: HelixClient object
        :param values: Values dict to send to BMC Helix
        :return: BMC Helix entry values, boolean for success, reason failed if failed
        """
        # POST an incident to BMC Helix
        try:
            helix_incident, status_code = helix_client.create_form_entry(FORM_NAME, values)
        except IntegrationError as e:
            self.LOG.error("POST request to BMC Helix resulted in an error. Ensure all required BMC Helix fields were provided.")
            return {"error": e.value}, False, "Request resulted in an error from the BMC Helix API."

        # 201 is returned for resource created
        if status_code != 201:
            # Unexpected response from BMC Helix
            return helix_incident, False, f"Expected 201 - resource created response from BMC Helix. Received {status_code}"

        self.LOG.info("Incident successfully posted to BMC Helix.")
        # Capture the Incident Number
        # Note this is a temporary number for the request to create a new entry
        # and this value will be reassigned to reflect the true value
        # by getting the newly created object from BMC Helix
        incident_number = helix_incident.get("values", {}).get("Incident Number")

        # Get the newly created form entry object
        entries, status_code = helix_client.query_form_entry(ENTRY_NAME, incident_number)
        entry = entries.get("entries", [])[0]
        # Save the incident number so we can log it. This is the ID that shows in the BMC Helix UI
        incident_number = entry.get("values", {}).get("Incident Number")
        # Save the request id so we can log it. This is the ID that shows in the BMC Helix API
        request_id = entry.get("values", {}).get("Request ID")
        # We expect only one result to be returned
        if len(entries.get("entries", [])) > 1:
            self.LOG.debug(f"Multiple form entries in BMC Helix found matching Incident Number: {incident_number}."
                      "The Request ID of the first entry will be written to the datatable.")

        self.LOG.info(f"Correlated Request ID {request_id} to Incident Number {incident_number}")

        return entry.get("values", {}), True, None

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create a new incident in BMC Helix"""
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Get and validate app configs
            app_configs = validate_fields([
                {"name": "helix_host", "placeholder": "<example.domain>"},
                {"name": "helix_user", "placeholder": "<example_user>"},
                {"name": "helix_password", "placeholder": "xxx"}],
                self.options)

            yield self.status_message("Validations complete. Starting business logic")

            # Get optional settings
            port = self.options.get("helix_port", None)

            # If verify setting in the app.config is not set then defaults to true
            verify = self.rc.get_verify()

            # Get function inputs
            helix_payload = getattr(fn_inputs, "helix_payload", "{}")
            helix_payload = loads(helix_payload)
            helix_incident_name = getattr(fn_inputs, "helix_incident_name", "")
            # SOAR incident_id
            incident_id = getattr(fn_inputs, "incident_id")
            # SOAR task id
            task_id = getattr(fn_inputs, "task_id", None)

            # Add in the additional data
            addl_data = helix_payload.pop("additional_data")
            addl_data and helix_payload.update(addl_data)

            # Required metadata field to create a resource
            helix_payload["z1D_Action"] = "CREATE"

            # Create variable task
            task = None

            if task_id:
                # Get the task data
                task = self.rest_client().get(f"/tasks/{task_id}")

                # Add task instructions to the helix_payload dict if present in the task
                if task.get("instructions"):
                    # Set the description to the task instructions
                    # Detailed description is the biggest text field we have available to us
                    # Add it to the helix_payload dict
                    helix_payload["Detailed_Decription"] = clean_html(task.get("instructions"))

            # Add the incident name to the description if one wasn't provided in the inputs
            if not helix_payload.get("Description"):
                helix_payload["Description"] = f"IBM SOAR Case {incident_id}: {helix_incident_name}"

            # Description has a max length of 100
            if len(helix_payload.get("Description", "")) > 100:
                helix_payload["Description"] = helix_payload["Description"][:100]
                self.LOG.info("Description field has a max length of 100 characters.")

            # Instantiate a HelixClient
            client = HelixClient(app_configs["helix_host"], app_configs["helix_user"],
                                 app_configs["helix_password"], self.rc, port=port, verify=verify)

            self.LOG.info(f"Incident values to POST:\n{helix_payload}")

            result, success, reason = self.post_incident_to_helix(client, helix_payload)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            if success:
                yield FunctionResult({"values": result})
            else:
                yield FunctionResult(result, success=success, reason=reason)

        except Exception as e:
            yield FunctionError(e)
