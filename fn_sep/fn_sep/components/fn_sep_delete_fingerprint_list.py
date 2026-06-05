# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - delete fingerprint list. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.

from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_delete_fingerprint_list"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_delete_fingerprint_list' of package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Delete  a file fingerprint list."""
        try:
            # Validate the required inputs
            validate_fields(["sep_fingerprintlist_id"], fn_inputs)

            # Get the function parameters:
            sep_fingerprintlist_id = getattr(fn_inputs, "sep_fingerprintlist_id", None)  # text

            self.LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)

            yield self.status_message("Running Symantec SEP Delete Fingerprint List action ...")

            sep = Sepclient(self.options)
            results = sep.delete_fingerprint_list(fingerprintlist_id=sep_fingerprintlist_id)

            if isinstance(results, dict) and results.get("errors", []) and results.get("errors", [])[0].get("error_code") == 410:
                # If this error was trapped user probably tried to get information on invalid connector guid.
                yield self.status_message(
                    f"""Got a 410 error while attempting to delete fingerprint list fingerprint id  '{sep_fingerprintlist_id}' 
                    because of a possible deleted id.""")
            else:
                yield self.status_message(f"Returning 'Symantec SEP Delete Fingerprint List' results for fingerprint id '{sep_fingerprintlist_id}'.")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
