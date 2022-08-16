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
from fn_bigfix.util.helpers import validate_opts, PACKAGE_NAME
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
        validate_opts(self)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Bigfix action status - Get status for Bigfix action id."""
        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate parameters
        validate_fields(["bigfix_action_id"], fn_inputs)

        self.LOG.info("bigfix_action_id: {}".format(fn_inputs.bigfix_action_id))

        yield self.status_message("Running Query BigFix for BigFix action id '{}' ...".format(fn_inputs.bigfix_action_id))
        bigfix_client = BigFixClient(self.opts, self.options)

        # Check status every 'retry_interval' secs up to 'retry_timeout' secs
        try:
            status = None
            (status, message) = poll_action_status(bigfix_client, fn_inputs.bigfix_action_id,
                int(self.options.get("bigfix_polling_interval")), int(self.options.get("bigfix_polling_timeout")))
        except Exception as e:
            yield self.status_message("Failed with exception '{}' while trying to poll BigFix action status.".format(type(e).__name__))

        results = {}
        if not status:
            raise FunctionError(
                "Function 'poll_action_status' returned bad status {}.".format(status))
        elif status == "OK":
            yield self.status_message("Received successful status message '{}' for BigFix action {}.".format(sub('\.$', '', message), fn_inputs.bigfix_action_id))
            results = {"status": "OK", "status_message": message}
        elif status == "Failed":
            yield self.status_message("Received error status {} for BigFix action {}.".format(message, fn_inputs.bigfix_action_id))
            results = {"status": "Failed", "status_message": message}
        elif status == "Unsupported":
            yield self.status_message("Received  unexpected status {} while retrieving status for BigFix action {}.".format(message, fn_inputs.bigfix_action_id))
        elif status == "Timedout":
            yield self.status_message("Timed out getting action status for BigFix action {}".format(fn_inputs.bigfix_action_id))

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
