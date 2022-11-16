# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

# Set up:
# Destination: a Queue named "bigfix_remediation".
# Manual Action: Execute a BigFix action to remediate hit.

from datetime import datetime
from resilient_lib import validate_fields
from fn_bigfix.lib.bigfix_client import BigFixClient
from fn_bigfix.util.helpers import PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "fn_bigfix_remediation"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_bigfix_remediation' of package fn_bigfix.

        This Function attempts to remediate a 'hit' discovered in a BigFix environment and takes the following
        parameters:

            bigfix_asset_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_incident_id

        An example of a set of query parameter might look like the following:

                bigfix_asset_id = 12315195
                bigfix_artifact_value = /tmp/evilfile.txt
                bigfix_artifact_type = File Path
                bigfix_incident_id = 2095

        The BigFix Query will execute a remediation action against a Bigfix server and the Function returns a status
        result in JSON format similar to the following.

            {'status': 'OK',
             'remediation_date': '07-18-2018 10:25:21',
             'status_message': 'BigFix Action Created Successfully.',
             'action_id': '119'
            }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function : Bigfix remediation - Remediate hit for endpoint in BigFix."""

        validate_fields(["bigfix_asset_id", "bigfix_artifact_value", "bigfix_artifact_type", "bigfix_incident_id"], fn_inputs)

        params = {"asset_id": fn_inputs.bigfix_asset_id, "artifact_value": fn_inputs.bigfix_artifact_value,
                    "artifact_type": fn_inputs.bigfix_artifact_type, "incident_id": fn_inputs.bigfix_incident_id}

        self.LOG.info(str(params))

        yield self.status_message(f"Running BigFix remediation for Artifact '{params['artifact_value']}' on endpoint '{params['asset_id']}' ...")
        bigfix_client = BigFixClient(self.opts, self.options)

        # Send a remediation message to BigFix
        response = None
        try:
            if params["artifact_type"]  == "Process Name":
                response = bigfix_client.send_kill_process_remediation_message(params["artifact_value"], params["asset_id"])
            elif params["artifact_type"] == "Service":
                response = bigfix_client.send_stop_service_remediation_message(params["artifact_value"], params["asset_id"])
            elif params["artifact_type"] == "Registry Key":
                if len(params["artifact_value"].split('\\')) <= 2:
                    yield self.status_message(f"Warning: Delete not allowed for root level key {params['artifact_value']}.")
                else:
                    # Test if registry key has 1 or more subkeys
                    result = bigfix_client.check_exists_subkey(params["artifact_value"], params["asset_id"])
                    # Query should return array with single result.
                    if not result or not result[0]:
                        yield self.status_message(f"Warning: Delete not allowed for key '{params['artifact_value']}'. BigFix subkey query did not return a valid result.")
                    elif (not result[0].get("failure") or result[0].get("failure") == "False") and result[0].get("result") == "True":
                        yield self.status_message(f"Warning: Delete not allowed, key '{params['artifact_value']}' has 1 or more subkeys.")
                    else:
                        response = bigfix_client.send_delete_registry_key_remediation_message(params["artifact_value"], params["asset_id"])
            elif params["artifact_type"] == "File Path":
                # Test if file path is a folder, if so disallow remediate.
                result = bigfix_client.check_is_folder(params["artifact_value"], params["asset_id"])
                # Query should return array with single result.
                if not result or not result[0]:
                    yield self.status_message(f"Warning: Delete not allowed for artifact '{params['artifact_value']}'. BigFix subkey query did not return a valid result")
                elif (not result[0].get("failure") or result[0].get("failure") == "False") and result[0].get("result") == "True":
                    yield self.status_message(f"Warning: Delete not allowed for folder artifact '{params['artifact_value']}'.")
                else:
                    response = bigfix_client.send_delete_file_remediation_message(params["artifact_value"], params["asset_id"])
            else:
                raise ValueError(f"Unsupported artifact type '{params['artifact_type']}'.")
        except Exception as e:
            yield self.status_message(f"Failed with exception '{type(e).__name__}' while trying to run a BigFix remediation.")

        if response:
            results = {"status": "OK", "status_message": "BigFix action created successfully.", "remediation_date": datetime.today().strftime('%m-%d-%Y %H:%M:%S'), "action_id": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
