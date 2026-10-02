# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - move endpoint. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST update against a SYMANTEC SEPM server.import json
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_move_endpoint"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_move_endpoint' of package fn_sep.

    The Function takes the following parameter:
            sep_hardwarekey, sep_group_id

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Checks and moves a client computer to a specified group."""
        try:

            # Get the function parameters:
            sep_groupid = getattr(fn_inputs, "sep_groupid", None)  # text
            sep_hardwarekey = getattr(fn_inputs, "sep_hardwarekey", None)  # text

            self.LOG.info("sep_groupid: %s", sep_groupid)
            self.LOG.info("sep_hardwarekey: %s", sep_hardwarekey)

            validate_fields(["sep_groupid", "sep_hardwarekey"], fn_inputs)

            yield self.status_message("Running Symantec SEP Move Endpoint action...")

            sep = Sepclient(self.options)
            rtn = sep.move_endpoint(groupid=sep_groupid, hardwarekey=sep_hardwarekey)

            yield self.status_message("Returning 'Symantec SEP Move Endpoint' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
