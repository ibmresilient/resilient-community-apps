# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - quarantine endpoint. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.import json
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_quarantine_endpoints"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_quarantine_endpoints' of package fn_sep.

    The Function takes the following parameter:
            sep_group_ids, sep_computer_ids, sep_undo

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Quarantine/unquarantine Symantec Endpoint Protection endpoints."""
        try:
            # validate required parameters
            validate_fields(["sep_group_ids", "sep_computer_ids", "sep_hardwarekey"], fn_inputs)
            # Get the function parameters:
            sep_group_ids = getattr(fn_inputs, "sep_group_ids", None)  # text
            sep_computer_ids = getattr(fn_inputs, "sep_computer_ids", None)  # text
            sep_hardwareKeys = getattr(fn_inputs, "sep_hardwarekey", None)
            sep_undo = getattr(fn_inputs, "sep_undo", None)  # boolean

            self.LOG.info("sep_group_ids: %s", sep_group_ids)
            self.LOG.info("sep_computer_ids: %s", sep_computer_ids)
            self.LOG.info("sep_hardwarekey: %s", sep_hardwareKeys)
            self.LOG.info("sep_undo: %s", sep_undo)

            validate_fields(["sep_undo"], fn_inputs)

            yield self.status_message("Running Symantec SEP Quarantine Endpoint or group...")

            sep = Sepclient(self.options)

            rtn = sep.quarantine_endpoints(group_ids=sep_group_ids, computer_ids=sep_computer_ids, undo=sep_undo, hardware_keys=sep_hardwareKeys)

            yield self.status_message("Returning 'Symantec SEP Quarantine Endpoint' or group results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
