# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - initiate eoc scan. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.import json
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_scan_endpoints"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_scan_endpoints' of package fn_sep.

    The Function takes the following parameter:
            sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_name, sep_sha256, sep_description

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Run a Evidence of Compromise (EOC) scan on Symantec Endpoint Protection endpoints."""
        try:
            # Get the function parameters:
            sep_group_ids = getattr(fn_inputs, "sep_group_ids", None)  # text
            sep_computer_ids = getattr(fn_inputs, "sep_computer_ids", None)  # text
            sep_scan_type = self.get_select_param(getattr(fn_inputs, "sep_scan_type", None))  # select, values: "QUICK_SCAN", "FULL_SCAN"
            sep_file_path = getattr(fn_inputs, "sep_file_path", None)  # text
            sep_sha256 = getattr(fn_inputs, "sep_sha256", None)  # text
            sep_sha1 = getattr(fn_inputs, "sep_sha1", None)  # text
            sep_md5 = getattr(fn_inputs, "sep_md5", None)  # text
            sep_description = getattr(fn_inputs, "sep_description", None)  # text
            sep_scan_action = self.get_select_param(getattr(fn_inputs, "sep_scan_action", None))  # select, values: "scan", "remediate"

            self.LOG.info("sep_group_ids: %s", sep_group_ids)
            self.LOG.info("sep_computer_ids: %s", sep_computer_ids)
            self.LOG.info("sep_scan_type: %s", sep_scan_type)
            self.LOG.info("sep_file_path: %s", sep_file_path)
            self.LOG.info("sep_sha256: %s", sep_sha256)
            self.LOG.info("sep_sha1: %s", sep_sha1)
            self.LOG.info("sep_md5: %s", sep_md5)
            self.LOG.info("sep_description: %s", sep_description)
            self.LOG.info("sep_scan_action: %s", sep_scan_action)

            validate_fields(["sep_scan_type", "sep_description"], fn_inputs)

            yield self.status_message("Running Symantec SEP Scan Endpoints command...")

            sep = Sepclient(self.options)

            rtn = sep.scan_endpoints(computer_ids=sep_computer_ids,
                                     group_ids=sep_group_ids,
                                     scan_type=sep_scan_type,
                                     file_path=sep_file_path,
                                     sha256=sep_sha256,
                                     sha1=sep_sha1,
                                     md5=sep_md5,
                                     description=sep_description,
                                     scan_action=sep_scan_action)

            yield self.status_message("Returning 'Symantec SEP Scan Endpoints' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
