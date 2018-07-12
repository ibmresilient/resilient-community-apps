# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to remediate a hit in a Bigfix environment """

# Set up:
# Destination: a Queue named "bigfix_artifact".
# Manual Action: Execute a BigFix action to remediate hit.

import logging
from fn_bigfix.util.helpers import validate_opts, validate_params
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_bigfix.lib.bigfix_client import BigFixClient
import fn_bigfix.lib.datastorage as datastore

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
        self.bigFix = BigFixClient(opts)
        self.datastore = datastore.Datastore()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)
        self.bigFix = BigFixClient(opts)
        self.datastore = datastore.Datastore()

    @function("fn_bigfix_remediation")
    def _fn_bigfix_remediation_function(self, event, *args, **kwargs):
        """Function: """
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

            yield StatusMessage("Running BigFix remediation for Artifact ...")

            # For our purposes, config_key will be the action name
            map_data = event.message
            action_name = event.name
            workflow_name = event.workflow
            map_data["action_name"] = action_name
            map_data["workflow_name"] = workflow_name
            log.debug(json.dumps(map_data, indent=2))

            yield StatusMessage("Running BigFix remediation ...")
            # Send a remediation message to BigFix

            if workflow_name == "bigfix_kill_process":
                response = self.bigFix.send_kill_process_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif workflow_name == "bigfix_stop_service":
                response = self.bigFix.send_stop_service_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif workflow_name == "bigfix_delete_registry_key":
                response = self.bigFix.send_delete_registry_key_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            elif workflow_name == "bigfix_delete_file":
                response = self.bigFix.send_delete_file_remediation_message(bigfix_artifact_value, bigfix_asset_id)
            else:
                log.info("Not supported action %s", action_name)
                raise ValueError("Incorrect value {} for 'action_name'.".format(action_name))

            if response is None:
                log.debug("Could not create BigFix Action.")
                yield FunctionError("Could not create BigFix Action")
            else:
                status_message = "BigFix Action Created Successfully."
                action_id = response
                remediation_date = datetime.datetime.today().strftime('%m-%d-%Y %H:%M:%S')
                #try:
                #    self.datastore.add_bg_action(int(response), params["row_id"], int(params["incident_id"]))
                #except Exception as e:
                #    log.exception("Could not save row in DB. Action ID {0}. Row ID {1}. Incident ID {2}"
                #                  .format(response, params["row_id"], params["incident_id"]))
                status_note = "Big Fix Integration: Action created successfully to remediate artifact value {0} " \
                                "and type {1} in asset ID {2}. BigFix Action ID {3}." \
                    .format(params["artifact_value"], params["artifact_type"], params["asset_id"], response)
                results = {"status": "OK", "status_message": status_message,  "status_note": status_note,
                           "remediation_date": remediation_date, "action_id": action_id}

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()