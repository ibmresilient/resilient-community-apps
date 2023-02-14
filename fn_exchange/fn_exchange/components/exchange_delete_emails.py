# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage, FunctionResult)

from fn_exchange.lib import constants
from fn_exchange.lib.exchange_utils import exchange_interface

FN_NAME = "exchange_delete_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, constants.PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Query the server to find emails with the provided parameters and delete them. There
        are two types of deletion operation that can be performed:

            * Hard delete : Permanently delete selected emails
            * Soft delete : Move selected emails to TRASH

        FN Inputs:
        -------
            hard_delete           <bool> : Permanently delete email or move to trash

            username               <str> : Primary email account to be used
            num_emails             <int> : Limit the number of emails retrieved
            email_ids              <str> : Retrieve emails from all these senders
            folder_path            <str> : Custom folder path to find emails
            sender                 <str> : Only find emails from this specified sender
            subject                <str> : Retrieve emails with matching message subject
            body                   <str> : Retrieve emails with matching message body
            has_attachments       <bool> : Retrieve emails with attachments 
            order_by_recency      <bool> : Order retrieved emails by recency
            search_subfolders     <bool> : Specifies whether to query a mailbox's subfolder
            start_date        <datetime> : Get emails on or after this date
            end_date          <datetime> : Get emails until after this date

        Returns:
        --------
            Response <dict> : A response with the mails retrieved and their attributes
                              or the error message if the retrieval process failed
        """
        function_parameters = {}

        function_parameters["hard_delete"] = getattr(fn_inputs, "exchange_hard_delete", False)

        function_parameters["username"] = getattr(fn_inputs, "exchange_email", None)
        function_parameters["num_emails"] = getattr(fn_inputs, "exchange_num_emails", None)
        function_parameters["email_ids"]  = getattr(fn_inputs, "exchange_email_ids", None)
        function_parameters["src_folder"] = getattr(fn_inputs, "exchange_folder_path", None)
        function_parameters["sender"]  = getattr(fn_inputs, "exchange_sender", None)
        function_parameters["subject"] = getattr(fn_inputs, "exchange_message_subject", None)
        function_parameters["body"]    = getattr(fn_inputs, "exchange_message_body", None)
        function_parameters["has_attachments"] = getattr(fn_inputs, "exchange_has_attachments", None)
        function_parameters["order_by_recency"] = getattr(fn_inputs, "exchange_order_by_recency", None)
        function_parameters["search_subfolders"] = getattr(fn_inputs, "exchange_search_subfolders", None)
        function_parameters["start_date"] = getattr(fn_inputs, "exchange_start_date", None)
        function_parameters["end_date"] = getattr(fn_inputs, "exchange_end_date", None)

        if not function_parameters.get("src_folder"):
            function_parameters["src_folder"] = self.options.get('default_folder_path')
            self.LOG.info('No folder path was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(" ".join([parameter, ":", str(function_parameters.get(parameter))]))

        try:
            interface = exchange_interface(self.rc, self.options)
            yield StatusMessage("Finding emails")
            retrieved_emails = interface.get_emails(function_parameters)
            num_deleted = retrieved_emails.count()

            yield StatusMessage(f"Search email operation complete, {num_deleted} emails found")
            results = interface.create_email_function_results(retrieved_emails)

            if num_deleted == 0:
                msg = "Failed to perform operation as 0 emails were retrieved"

            elif function_parameters["hard_delete"]:
                msg = "Permanently deleted emails"
                retrieved_emails.delete()

            else:
                msg = "Moved emails to trash"
                for item in retrieved_emails:
                    item.move_to_trash()

            self.LOG.info(msg)
            yield StatusMessage(msg)

            yield StatusMessage(f"{num_deleted} emails deleted")
            yield FunctionResult(results, success=True)

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
