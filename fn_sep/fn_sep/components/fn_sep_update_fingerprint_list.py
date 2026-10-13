# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - update fingerprint list. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.
from resilient_lib import validate_fields, b_to_s
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_update_fingerprint_list"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_update_fingerprint_list' of package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id, sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Updates an existing fingerprint list."""
        try:
            # Get the function parameters:
            sep_fingerprintlist_id = getattr(fn_inputs, "sep_fingerprintlist_id")  # text
            sep_fingerprintlist_name = getattr(fn_inputs, "sep_fingerprintlist_name")  # text
            sep_description = getattr(fn_inputs, "sep_description")  # text
            sep_domainid = getattr(fn_inputs, "sep_domainid")  # text
            sep_hash_value = getattr(fn_inputs, "sep_hash_value")  # text

            self.LOG.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)
            self.LOG.info("sep_fingerprintlist_name: %s", sep_fingerprintlist_name)
            self.LOG.info("sep_description: %s", sep_description)
            self.LOG.info("sep_domainid: %s", sep_domainid)
            self.LOG.info("sep_hash_value: %s", sep_hash_value)

            validate_fields(["sep_fingerprintlist_id", "sep_fingerprintlist_name", "sep_description",
                             "sep_domainid", "sep_hash_value"], fn_inputs)

            yield self.status_message("Running Symantec SEP Update Fingerprint List action ...")

            sep = Sepclient(self.options)

            rtn = sep.update_fingerprint_list(fingerprintlist_id=sep_fingerprintlist_id,
                                              fingerprintlist_name=sep_fingerprintlist_name,
                                              description=sep_description,
                                              domainid=sep_domainid,
                                              hash_value=sep_hash_value)
            if isinstance(rtn, bytes):
                rtn = b_to_s(rtn)

            yield self.status_message("Returning 'Symantec SEP Update Fingerprint List' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
