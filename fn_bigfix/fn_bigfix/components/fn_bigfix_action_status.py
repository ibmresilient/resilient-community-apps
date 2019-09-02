# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Resilient functions component to check BigFix action status """

# Set up:
# Destination: a Queue named "bigfix_remediation".
# Manual Action: Check BigFix action status.

import logging
import re

from fn_bigfix.util.helpers import validate_opts, is_none
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_bigfix.lib.bigfix_client import BigFixClient
from fn_bigfix.lib.bigfix_helpers import poll_action_status

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_bigfix_action_status' of package fn_bigfix.

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
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bigfix", {})
        validate_opts(self)

    @function("fn_bigfix_action_status")
    def _fn_bigfix_action_status_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Bigfix action status - Get status for Bigfix action id."""
        try:
            # Get the function parameters:
            bigfix_action_id = kwargs.get("bigfix_action_id")  # number

            log = logging.getLogger(__name__)
            log.info("bigfix_action_id: %s", bigfix_action_id)

            if is_none(bigfix_action_id):
                raise ValueError("Required parameter 'bigfix_action_id' not set.")

            yield StatusMessage("Running Query BigFix for BigFix action id '{}' ...".format(bigfix_action_id))
            bigfix_client = BigFixClient(self.options)
            retry_interval = int(self.options.get("bigfix_polling_interval"))
            retry_timeout = int(self.options.get("bigfix_polling_timeout"))

            # Check status every 'retry_interval' secs up to 'retry_timeout' secs
            try:
                status = None
                (status, status_message) = poll_action_status(bigfix_client, bigfix_action_id, retry_interval, retry_timeout)
            except Exception as e:
                log.exception("Failed to poll BigFix action status.")
                yield StatusMessage("Failed with exception '{}' while trying to poll BigFix action status.".format(type(e).__name__))
                raise Exception("Failed with exception '{}' while trying to poll BigFix action status.".format(type(e).__name__))

            if not status:
                raise FunctionError("Function 'poll_action_status' returned bad status {}.".format(status))
            elif status == "OK":
                yield StatusMessage("Received successful status message '{0}' for BigFix action {1}.".format(re.sub('\.$', '', status_message), bigfix_action_id))
                results = {"status": "OK", "status_message": status_message}
            elif status == "Failed":
                yield StatusMessage("Received error status {0} for BigFix action {1}.".format(status_message, bigfix_action_id))
                results = {"status": "Failed", "status_message": status_message}
            elif status == "Unsupported":
                yield StatusMessage("Received  unexpected status {0} while retrieving status for BigFix action {1}."
                                    .format(status_message, bigfix_action_id))
                results = {}
            elif status == "Timedout":
                yield StatusMessage("Timed out getting action status for BigFix action {}".format(bigfix_action_id))
                results = {}

            yield StatusMessage("done...")

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for BigFix integration.")
            yield FunctionError()
