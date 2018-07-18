# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to remediate a hit on and endpoint in a Bigfix environment """

# Set up:
# Destination: a Queue named "bigfix_artifact".
# Manual Action: Execute a BigFix action to remediate hit.

import logging
from fn_bigfix.util.helpers import validate_opts, validate_params
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_bigfix.lib.bigfix_client import BigFixClient

import json
import datetime

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_bigfix_remediation' of
        package fn_bigfix.

        This Function attempts to remediate 'hits' discovered in a BigFix environment takes the following parameters:
            bigfix_asset_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_incident_id

        An example of a set of query parameter might look like the following:

                bigfix_asset_id = 12315195
                bigfix_artifact_value = /tmp/test.txt
                bigfix_artifact_type = File Path
                bigfix_incident_id = incident.id

        The BigFix Query will execute a remediation action against a Bigfix server and the Funcxtion returns a status
        result in JSON format similar to the following.

            {'status': 'OK', 'remediation_date': '07-11-2018 10:51:56',
             'remediation_status': 'BigFix Action Created Successfully.',
             'status_note': 'Big Fix Integration: Action created successfully to remediate artifact value lfsvc and
             type Service in asset ID 12315195. BigFix Action ID 75.', 'action_id': '75'
            }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @function("fn_bigfix_remediation")
    def _fn_bigfix_remediation_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Bigfix remediation - Remediate hit for endpoint in BigFix."""
        try:
            # Get the function parameters:
            bigfix_asset_id = kwargs.get("bigfix_asset_id")  # text
            bigfix_artifact_value = kwargs.get("bigfix_artifact_value")  # text
            bigfix_artifact_type = kwargs.get("bigfix_artifact_type")  # text
            bigfix_incident_id = kwargs.get("bigfix_incident_id")  # number


            log = logging.getLogger(__name__)
            log.info("bigfix_asset_id: %s", bigfix_asset_id)
            log.info("bigfix_artifact_value: %s", bigfix_artifact_value)
            log.info("bigfix_artifact_type: %s", bigfix_artifact_type)
            log.info("bigfix_incident_id: %s", bigfix_incident_id)

            params = {"asset_id": bigfix_asset_id, "artifact_value": bigfix_artifact_value,
                      "artifact_type": bigfix_artifact_type, "incident_id": bigfix_incident_id}

            validate_params(params, "fn_bigfix_remediation")

            yield StatusMessage("Running BigFix remediation for Artifact '{0}' on endpoint '{1}' ..."
                                .format(params["artifact_value"], params["asset_id"]))
            bigfix_client = BigFixClient(self.options)

            yield StatusMessage("Running BigFix remediation ...")
            # Send a remediation message to BigFix

            if params["artifact_type"]  == "Process Name":
                response = bigfix_client.send_kill_process_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif params["artifact_type"] == "Service":
                response = bigfix_client.send_stop_service_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif params["artifact_type"] == "Registry Key":
                response = bigfix_client.send_delete_registry_key_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif params["artifact_type"] == "File Path":
                response = bigfix_client.send_delete_file_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            else:
                log.error("Unsupported artifact type {}.".format(params["artifact_type"]))
                raise ValueError("Unsupported artifact type {}.".format(params["artifact_type"]))

            if response is None:
                log.debug("Could not create BigFix Action.")
                yield FunctionError("Could not create BigFix Action")
            else:
                status_message = "BigFix Action Created Successfully."
                action_id = response
                remediation_date = datetime.datetime.today().strftime('%m-%d-%Y %H:%M:%S')
                status_note = "Big Fix Integration: Action created successfully to remediate artifact value {0} " \
                                "and type {1} in asset ID {2}. BigFix Action ID {3}." \
                    .format(params["artifact_value"], params["artifact_type"], params["asset_id"], response)
                results = {"status": "OK", "status_message": status_message,
                           "remediation_date": remediation_date, "action_id": action_id}

            yield StatusMessage("done...")

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for BigFix integration.")
            yield FunctionError()