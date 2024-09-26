# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get fingerprint list. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_add_fingerprint_list"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_add_fingerprint_list' of package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Add a hash to a new fingerprint list."""
        try:
            # Validate the required inputs
            validate_fields(["sep_fingerprintlist_name", "sep_description", "sep_domainid",
                             "sep_hash_value"], fn_inputs)

            # Get the function parameters:
            sep_fingerprintlist_name = getattr(fn_inputs, "sep_fingerprintlist_name", None)  # text
            sep_description = getattr(fn_inputs, "sep_description", None)  # text
            sep_domainid = getattr(fn_inputs, "sep_domainid", None)  # text
            sep_hash_value = getattr(fn_inputs, "sep_hash_value", None)  # text

            self.LOG.info("sep_fingerprintlist_name: %s", sep_fingerprintlist_name)
            self.LOG.info("sep_description: %s", sep_description)
            self.LOG.info("sep_domainid: %s", sep_domainid)
            self.LOG.info("sep_hash_value: %s", sep_hash_value)

            yield self.status_message("Running Symantec SEP Add Fingerprint List action ...")

            sep = Sepclient(self.options)

            results = sep.add_fingerprint_list(fingerprintlist_name=sep_fingerprintlist_name,
                                               description=sep_description,
                                               domainid=sep_domainid,
                                               hash_value=sep_hash_value)

            if isinstance(results, dict) and results.get("errors") and results.get("errors", [])[0].get("error_code") == 409:
                # If this error was trapped user probably tried to re-add a hash to a fingerprint list.
                yield self.status_message(
                    f"Got a 409 error while attempting to get a fingerprint list for fingerprint name '{sep_fingerprintlist_name}' "
                    "because of a possible invalid or deleted id.")
            else:
                yield self.status_message(f"Returning 'Symantec SEP Add Fingerprint List' results for fingerprint name '{sep_fingerprintlist_name}'.")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
