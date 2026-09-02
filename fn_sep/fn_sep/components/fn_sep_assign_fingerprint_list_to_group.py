# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - assign fingerprint list to group. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_assign_fingerprint_list_to_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_assign_fingerprint_list_to_group' of package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id, sep_group_id

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Assign a fingerprint list to a group for lock-down."""
        try:
            # Validate the required inputs
            validate_fields(["sep_fingerprintlist_id", "sep_groupid"], fn_inputs)

            # Get the function parameters:
            sep_fingerprintlist_id = getattr(fn_inputs, "sep_fingerprintlist_id", None)  # text
            sep_groupid = getattr(fn_inputs, "sep_groupid", None)  # text

            self.LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)
            self.LOG.info("sep_groupid: %s", sep_groupid)

            yield self.status_message("Running Symantec SEP Assign Fingerprint List to Group for Lock-down action ...")

            sep = Sepclient(self.options)

            results = sep.assign_fingerprint_list_to_group(groupid=sep_groupid,
                                                           fingerprintlist_id=sep_fingerprintlist_id)

            if isinstance(results, dict) and results.get("errorCode") and int(results.get("errorCode")) == 400:
                # If this error was trapped user probably tried to get an invalid fingerprint list.
                yield self.status_message(f"""Symantec SEP Assign Fingerprint List to Group for Lock-down: Got a 400 error 
                                while attempting to assign a fingerprint list for fingerprint id '{sep_fingerprintlist_id}' because of a 
                                possible invalid or deleted fingerprintlist id.""")
            else:
                yield self.status_message(f"""Returning 'Symantec SEP Assign Fingerprint List to Group for Lock-down' results for 
                                fingerprintlist_id '{sep_fingerprintlist_id}' and groupid '{sep_groupid}'""")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
