# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging, json
from resilient_circuits import AppFunctionComponent, app_function, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils

PACKAGE_NAME =  "fn_exchange"
FN_NAME = "exchange_find_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        function_parameters = {}

        # Get the function parameters:
        function_parameters["username"]    = getattr(fn_inputs, "exchange_email", None)  # text
        function_parameters["num_emails"]  = getattr(fn_inputs, "exchange_num_emails", None) # int
        function_parameters["email_ids"]   = getattr(fn_inputs, "exchange_email_ids", None) # text
        function_parameters["folder_path"] = getattr(fn_inputs, "exchange_folder_path", None)  # text

        function_parameters["start_date"]  = getattr(fn_inputs, "exchange_start_date", None)  # datepicker
        function_parameters["end_date"]    = getattr(fn_inputs, "exchange_end_date", None)  # datepicker

        function_parameters["sender"]  = getattr(fn_inputs, "exchange_sender", None)  # text
        function_parameters["subject"] = getattr(fn_inputs, "exchange_message_subject", None) # text
        function_parameters["body"]    = getattr(fn_inputs, "exchange_message_body", None) # text
        
        function_parameters["has_attachments"]   = getattr(fn_inputs, "exchange_has_attachments", None) # boolean
        function_parameters["order_by_recency"]  = getattr(fn_inputs, "exchange_order_by_recency", None) # boolean
        function_parameters["search_subfolders"] = getattr(fn_inputs, "exchange_search_subfolders", False) # boolean

        if not function_parameters.get("folder_path"):
            function_parameters["folder_path"] = self.options.get('default_folder_path')
            self.LOG.info('No folder path was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(" ".join([parameter, ":", str(function_parameters.get(parameter))]))

        utils = exchange_utils(self.rc, self.options)

        yield StatusMessage("Finding emails")
        retrieved_emails = utils.get_emails(function_parameters)

        yield StatusMessage("Done finding emails, %d emails found" % retrieved_emails.count())
        results = utils.create_email_function_results(retrieved_emails)
        yield FunctionResult(results, success=True)

        try:
            pass
        except Exception:
            yield FunctionError()
            
            