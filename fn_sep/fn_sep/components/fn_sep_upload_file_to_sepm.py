# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM action - upload file to SEPM server. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.
from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_upload_file_to_sepm"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_upload_file_to_sepm' of package fn_sep.

    The Function takes the following parameter:
            sep_file_path, sep_computer_ids, sep_sha256, sep_sha1, sep_md5, sep_source

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Upload suspicious file from endpoint back to SEPM server."""
        try:

            # Get the function parameters:
            sep_file_path = getattr(fn_inputs, "sep_file_path", None)  # text
            sep_computer_ids = getattr(fn_inputs, "sep_computer_ids", None)  # text
            sep_sha256 = getattr(fn_inputs, "sep_sha256", None)  # text
            sep_sha1 = getattr(fn_inputs, "sep_sha1", None)  # text
            sep_md5 = getattr(fn_inputs, "sep_md5", None)  # text
            sep_source = getattr(fn_inputs, "sep_source", None)  # text

            self.LOG.info("sep_file_path: %s", sep_file_path)
            self.LOG.info("sep_computer_ids: %s", sep_computer_ids)
            self.LOG.info("sep_sha256: %s", sep_sha256)
            self.LOG.info("sep_sha1: %s", sep_sha1)
            self.LOG.info("sep_md5: %s", sep_md5)
            self.LOG.info("sep_source: %s", sep_source)

            validate_fields(["sep_file_path", "sep_computer_ids", "sep_source"], fn_inputs)

            yield self.status_message("Running Symantec SEP Upload File to SEPM ...")

            sep = Sepclient(self.options)

            rtn = sep.upload_file(file_path=sep_file_path,
                                  computer_ids=sep_computer_ids,
                                  sha256=sep_sha256,
                                  md5=sep_md5,
                                  sha1=sep_sha1,
                                  source=sep_source)

            yield self.status_message("Returning 'Symantec SEP Upload File to SEPM' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
