# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get domains. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_get_domains"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_domains' of package fn_sep.

    The Function takes the following parameter

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Gets a list of all accessible domains."""
        try:
            yield self.status_message("Running Symantec SEP Get Domains query...")

            sep = Sepclient(self.options)
            results = sep.get_domains()
            yield self.status_message("Returning 'Get Domains' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
