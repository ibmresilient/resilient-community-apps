# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get file content as base64. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from base64 import b64encode

from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_get_file_content_as_base64"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_file_content_as_base64' of package fn_sep.

    The Function takes the following parameter:
            sep_file_id

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Get the contents of an uploaded binary file, in base64 format."""
        try:
            # Get the function parameters:
            sep_file_id = getattr(fn_inputs, "sep_file_id", None)  # text

            self.LOG.info("sep_file_id: %s", sep_file_id)

            validate_fields(["sep_file_id"], fn_inputs)

            yield self.status_message("Running Symantec SEP Get File Content as Base64 ...")

            sep = Sepclient(self.options)

            rtn = b64encode(sep.get_file_content(file_id=sep_file_id)).decode("utf-8")

            yield self.status_message("Returning 'Symantec SEP Get File Content as Base64' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
