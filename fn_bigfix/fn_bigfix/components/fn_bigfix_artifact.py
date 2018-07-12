# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Bigfix Query against a Bigfix server for an artifact to determine
if are hits on any of the BigFix endpoints"""

# Set up:
# Destination: a Queue named "bigfix_artifact".
# Manual Action: Execute a REST query against a BigFix server return hits.

"""Function implementation"""

import logging
from fn_bigfix.util.helpers import validate_opts, validate_params
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_bigfix.lib.bigfix_client import BigFixClient
from fn_bigfix.lib.bigfix_helpers import get_hits
import datetime
import os
import json

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_bigfix_artifact' of
        package fn_bigfix.

        The Function does a BigFix query and takes the following parameters:
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

        The BigFix Query will execute a REST call against a Bigfix server and the Function returns a result
        in JSON format similar to the following.

            {'endpoint_hits': [{u'computer_id': 13550086, u'failure': False, u'resp_time': 1000,
                                u'query_id': 1, u'result': u'True', u'computer_name': u'DESKTOP-TUKM3HF'}]
            }
        """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)
        self.bigFix = BigFixClient(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)
        self.bigFix = BigFixClient(self.options)

    @function("fn_bigfix_artifact")
    def _fn_bigfix_artifact_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Bigfix artifact - Get hits in BigFix for artifact."""
        try:
            # Get the function parameters:
            bigfix_artifact_id = kwargs.get("bigfix_artifact_id")  # number
            bigfix_artifact_value = kwargs.get("bigfix_artifact_value")  # text
            bigfix_artifact_type = kwargs.get("bigfix_artifact_type")  # text
            bigfix_artifact_properties_name = kwargs.get("bigfix_artifact_properties_name")  # text
            bigfix_artifact_properties_value = kwargs.get("bigfix_artifact_properties_value")  # text
            bigfix_incident_id = kwargs.get("bigfix_incident_id")  # number
            bigfix_incident_plan_status = kwargs.get("bigfix_incident_plan_status")  # text


            log = logging.getLogger(__name__)
            log.info("bigfix_artifact_id: %s", bigfix_artifact_id)
            log.info("bigfix_artifact_value: %s", bigfix_artifact_value)
            log.info("bigfix_artifact_type: %s", bigfix_artifact_type)
            log.info("bigfix_artifact_properties_name: %s", bigfix_artifact_properties_name)
            log.info("bigfix_artifact_properties_value: %s", bigfix_artifact_properties_value)
            log.info("bigfix_incident_id: %s", bigfix_incident_id)
            log.info("bigfix_incident_plan_status: %s", bigfix_incident_plan_status)

            params = {"artifact_id": bigfix_artifact_id, "artifact_value": bigfix_artifact_value,
                      "artifact_properties_name": bigfix_artifact_properties_name,
                      "artifact_properties_value": bigfix_artifact_properties_value,
                      "artifact_type": bigfix_artifact_type, "incident_id": bigfix_incident_id,
                      "incident_plan_status": bigfix_incident_plan_status}

            validate_params(params, "fn_bigfix_artifact")

            yield StatusMessage("Running Query BigFix for Artifact ...")

            if bigfix_incident_plan_status != 'C':
                # If incident isn't closed
                if bigfix_artifact_type == "IP Address":
                    artifact_data = self.bigFix.get_bf_computer_by_ip(bigfix_artifact_value)
                elif bigfix_artifact_type == "File Path":
                    artifact_data = self.bigFix.get_bf_computer_by_file_path(bigfix_artifact_value)
                elif bigfix_artifact_type == "Process Name":
                    artifact_data = self.bigFix.get_bf_computer_by_process_name(bigfix_artifact_value)
                elif bigfix_artifact_type == "Service":
                    artifact_data = self.bigFix.get_bf_computer_by_service_name(bigfix_artifact_value)
                elif bigfix_artifact_type == "Registry Key":
                    artifact_data = self.bigFix.get_bf_computer_by_registry_key_name_value(bigfix_artifact_value,
                                                                                           params["artifact_properties_name"],
                                                                                           params["artifact_properties_value"])
                else:
                    raise ValueError("Incorrect value for parameter parameter 'bigfix_artifact_type'.")

            if bigfix_incident_plan_status == 'C':
                yield StatusMessage("Ignoring action, incident %s is closed")
                results = {}
            elif not artifact_data:
                yield StatusMessage("Could not find data about the artifact %s")
                results = {}
            else:
                hits = get_hits(artifact_data, params)
                if len(hits) > int(self.options.get("hunt_results_limit", "200")):
                    yield StatusMessage("Adding artifact data as an incident attachment")
                    att_report = self._create_attachment(hits, params)
                    results = {"hits_over_limit": True, "att_name": att_report["name"]}
                else:
                    results = {"endpoint_hits": json.loads(json.dumps(hits))}

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def _create_attachment(self, hits, params):
        file_name = "query_for_artifact_{0}_{1}_{2}.txt"\
            .format(params["artifact_id"], params["artifact_type"], datetime.datetime.today().strftime('%Y%m%d'))
        file_content = ""

        for data in hits:
                file_content += "Resource ID: {0}. Resource Name: {1}. Artifact value: {2}. Artifact Type: {3} \n"\
                            .format(data.computer_id, data.computer_name, params["artifact_value"], params["artifact_type"])

        try:
            rest_client = self.rest_client()

            # Create the temporary file save results in json format.
            with open(file_name, 'w') as outfile:
                json.dump(file_content, outfile)

            # Post file to Resilient
            att_report = rest_client.post_attachment("/incidents/{0}/attachments".format(params["incident_id"]),
                                                     file_name,
                                                     file_name,
                                                     "text/plain",
                                                     "")
            LOG.info("New attachment added to incident %s", params["incident_id"])

            # Delete the temporary file.
            os.remove(file_name)

        except Exception as ex:
            LOG.error(ex)
            raise ex

        return att_report