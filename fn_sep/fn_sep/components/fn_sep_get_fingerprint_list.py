# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get fingerprint list. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_get_fingerprint_list"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_fingerprint_list' of package fn_sep.

    The Function takes the following parameter:
            sep_domainid, sep_fingerprintlist_name , sep_fingerprintlist_id

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Get the file fingerprint list for a specified name or id as a set of hash values."""
        try:

            # Get the function parameters:
            sep_domainid = getattr(fn_inputs, "sep_domainid", None)  # text
            sep_fingerprintlist_name = getattr(fn_inputs, "sep_fingerprintlist_name", None)  # text
            sep_fingerprintlist_id = getattr(fn_inputs, "sep_fingerprintlist_id", None)  # text

            self.LOG.info("sep_domainid: %s", sep_domainid)
            self.LOG.info("sep_fingerprintlist_name: %s", sep_fingerprintlist_name)
            self.LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)

            validate_fields(["sep_domainid"], fn_inputs)

            yield self.status_message("Running Symantec SEP Get File Fingerprint List query...")

            sep = Sepclient(self.options)
            rtn = sep.get_fingerprint_list(fingerprintlist_id=sep_fingerprintlist_id,
                                           fingerprintlist_name=sep_fingerprintlist_name,
                                           domainid=sep_domainid)

            if isinstance(rtn, dict) and rtn.get("errorCode") and int(rtn.get("errorCode")) == 410:
                # If this error was trapped user probably tried to get an invalid fingerprint list.
                yield self.status_message(
                    f"""Got a 410 error while attempting to get a fingerprint list for fingerprint name '{sep_fingerprintlist_name}' and 
                    domain id '{sep_domainid}' because of a possible invalid or deleted id.""")
            else:
                yield self.status_message(f"""Returning 'Symantec SEP Get File Fingerprint List' results for fingerprint name 
                                    '{sep_fingerprintlist_name}' and domain id '{sep_domainid}' .""")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
