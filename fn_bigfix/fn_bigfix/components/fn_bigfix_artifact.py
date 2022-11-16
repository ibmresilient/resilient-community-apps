# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

# Set up:
# Destination: a Queue named "bigfix_artifact".
# Manual Action: Execute a REST query against a BigFix server return hits.

from datetime import datetime
from json import loads, dumps
from resilient_lib import validate_fields
from fn_bigfix.lib.bigfix_client import BigFixClient
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_bigfix.util.helpers import create_attachment, PACKAGE_NAME

FN_NAME = "fn_bigfix_artifact"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_bigfix_artifact' of package fn_bigfix.

        The Function does a BigFix query to determine BigFix endpoints with hits and takes the
        following parameters:

            bigfix_artifact_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_artifact_properties_name
            bigfix_artifact_properties_value, bigfix_incident_id, bigfix_incident_plan_status


        An example of a set of query parameter might look like the following:

                bigfix_artifact_id =  120
                bigfix_artifact_value = "HKLM\SOFTWARE\TEST\TEST\com.tst.browsercore"
                bigfix_artifact_type = "Registry Key"
                bigfix_artifact_properties_name = "TESTKEY"
                bigfix_artifact_properties_value = "TESTVAL"
                bigfix_incident_id = 2095
                bigfix_incident_plan_status = "A"

        The BigFix Query will execute a REST query against a Bigfix server and the Function returns a result
        in JSON format similar to the following.

            {'hits_count': 1,
             'endpoint_hits': [{u'computer_id': 13550086, u'failure': False, u'resp_time': 0,
                                u'query_id': 1, u'result': u'True', u'computer_name': u'DESKTOP-TUKM3HF'}]
             'query_execution_date': '07-17-2018 17:44:21'
            }
        """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function : Bigfix artifact - Get hits in BigFix for artifact."""

        # Validate parameters
        validate_fields(["bigfix_artifact_id", "bigfix_artifact_value", "bigfix_artifact_type", "bigfix_incident_id", "bigfix_incident_plan_status"], fn_inputs)

        params = {"artifact_id": fn_inputs.bigfix_artifact_id,
                  "artifact_value": fn_inputs.bigfix_artifact_value,
                  "artifact_properties_name": fn_inputs.bigfix_artifact_properties_name if hasattr(fn_inputs, 'bigfix_artifact_properties_name') else None,
                  "artifact_properties_value": fn_inputs.bigfix_artifact_properties_value if hasattr(fn_inputs, 'bigfix_artifact_properties_value') else None,
                  "artifact_type": fn_inputs.bigfix_artifact_type,
                  "incident_id": fn_inputs.bigfix_incident_id,
                  "incident_plan_status": fn_inputs.bigfix_incident_plan_status}

        self.LOG.info(str(params))

        yield self.status_message(f"Running BigFix Query for Artifact id {params['artifact_id']}, with value {params['artifact_value']} ...")
        bigfix_client = BigFixClient(self.opts, self.options)

        try:
            if params["incident_plan_status"] != 'C':
                # If incident isn't closed
                if params["artifact_type"] == "IP Address":
                    artifact_data = bigfix_client.get_bf_computer_by_ip(params["artifact_value"])
                elif params["artifact_type"] == "File Path":
                    artifact_data = bigfix_client.get_bf_computer_by_file_path(
                        params["artifact_value"])
                elif params["artifact_type"] == "Process Name":
                    artifact_data = bigfix_client.get_bf_computer_by_process_name(
                        params["artifact_value"])
                elif params["artifact_type"] == "Service":
                    artifact_data = bigfix_client.get_bf_computer_by_service_name(
                        params["artifact_value"])
                elif params["artifact_type"] == "Registry Key":
                    artifact_data = bigfix_client.get_bf_computer_by_registry_key_name_value(
                        params["artifact_value"], params["artifact_properties_name"], params["artifact_properties_value"])
                else:
                    raise ValueError(f"Unsupported artifact type {params['artifact_type']}.")
        except Exception as e:
            yield self.status_message(f"Failed with exception '{type(e).__name__}' while trying to query BigFix.")

        results = {}
        if params["incident_plan_status"] == 'C':
            yield self.status_message(f"Ignoring action, incident {params['incident_id']} is closed")
        elif not artifact_data:
            yield self.status_message(f"Could not find data about the artifact {params['artifact_value']}")
        else:
            # Get endpoints with hits from results returned from BigFix
            hits = [hit for hit in artifact_data if hit.get("failure") in [0, "False"]]
            # Get number of hits found
            hits_len = len(hits)

            if not hits_len:
                yield self.status_message(f"No hits detected for artifact id '{params['artifact_id']}' with value '{params['artifact_value']}' and of type '{params['artifact_type']}'.")
            elif hits_len > int(self.options.get("bigfix_hunt_results_limit", "200")):
                yield self.status_message("Adding artifact data as an incident attachment")
                # Define file name and content to add as an attachment
                file_name = f'query_for_artifact_{params["artifact_id"]}_{params["artifact_type"]}_{datetime.today().strftime("%Y%m%d")}.txt'
                file_content = u""
                for data in hits:
                    file_content += f'Resource ID: {data.get("computer_id")}. Resource Name: {data.get("computer_name")}. Artifact value: {params["artifact_value"]}. Artifact Type: {params["artifact_type"]} \n'
                # Create an attachment
                att_report = create_attachment(self.rest_client(), file_name, file_content, params)
                results = {"hits_over_limit": True, "att_name": att_report.get("name"), "hits_count": hits_len}
            else:
                results = {"endpoint_hits": loads(dumps(hits)),
                    "hits_count": hits_len,
                    "query_execution_date": datetime.now().strftime('%m-%d-%Y %H:%M:%S'),
                    "hits_over_limit": False}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
