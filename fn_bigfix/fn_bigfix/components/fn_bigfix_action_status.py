# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

# Set up:
# Destination: a Queue named "bigfix_remediation".
# Manual Action: Check BigFix action status.

from re import sub
from resilient_lib import validate_fields
from fn_bigfix.lib.bigfix_client import BigFixClient
from fn_bigfix.lib.bigfix_helpers import poll_action_status
from fn_bigfix.util.helpers import PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_bigfix_action_status"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_bigfix_action_status' of package fn_bigfix.

        This Function polls status of a BigFix action which is remediating a hit and takes the following parameter:

            bigfix_action_id

        An example of a set of query parameter might look like the following:

                bigfix_action_id = 119

        The BigFix Query will poll the status of a remediation action on a Bigfix server and the Function
        returns a status result in JSON format similar to the following.

            {'status': 'OK',
             'status_message': 'The action executed successfully.',
            }
    """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Check app.config is set correctly
        validate_fields(["bigfix_url", "bigfix_port", "bigfix_user", "bigfix_pass",
                         "bigfix_hunt_results_limit", "bigfix_polling_interval",
                         "bigfix_polling_timeout", "bigfix_endpoints_wait"], self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Bigfix action status - Get status for Bigfix action id."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate parameters
        validate_fields(["bigfix_action_id"], fn_inputs)

        self.LOG.info(f"bigfix_action_id: {fn_inputs.bigfix_action_id}")
        yield self.status_message(f"Running Query BigFix for BigFix action id '{fn_inputs.bigfix_action_id}' ...")

        # Check status every 'retry_interval' secs up to 'retry_timeout' secs
        status = None
        try:
            (status, message) = poll_action_status(BigFixClient(self.opts, self.options), fn_inputs.bigfix_action_id,
                int(self.options.get("bigfix_polling_interval")), int(self.options.get("bigfix_polling_timeout")))
        except Exception as e:
            yield self.status_message(f"Failed with exception '{type(e).__name__}' while trying to poll BigFix action status.")

        results = {}
        if not status:
            raise FunctionError(
                f"Function 'poll_action_status' returned bad status {status}.")
        elif status == "OK":
            yield self.status_message(f"Received successful status message '{sub('\.$', '', message)}' for BigFix action {fn_inputs.bigfix_action_id}.")
            results = {"status": "OK", "status_message": message}
        elif status == "Failed":
            yield self.status_message(f"Received error status {message} for BigFix action {fn_inputs.bigfix_action_id}.")
            results = {"status": "Failed", "status_message": message}
        elif status == "Unsupported":
            yield self.status_message(f"Received  unexpected status {message} while retrieving status for BigFix action {fn_inputs.bigfix_action_id}.")
        elif status == "Timedout":
            yield self.status_message(f"Timed out getting action status for BigFix action {fn_inputs.bigfix_action_id}")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
