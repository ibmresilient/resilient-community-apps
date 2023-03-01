# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, INPUTS_MAP, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface

FN_NAME = "exchange_delete_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Query the server to find emails with the provided parameters and delete them. There
        are two types of deletion operation that can be performed:

            * Hard delete : Permanently delete selected emails
            * Soft delete : Move selected emails to TRASH

        FN Inputs:
        -------
            exchange_hard_delete       <bool> : Permanently delete email or move to trash

            exchange_email              <str> : Primary email account to be used
            exchange_num_emails         <int> : Limit the number of emails retrieved
            exchange_email_ids          <str> : Retrieve emails from all these senders
            exchange_folder_path        <str> : Custom folder path to find emails
            exchange_sender             <str> : Only find emails from this specified sender
            exchange_message_subject    <str> : Retrieve emails with matching message subject
            exchange_message_body       <str> : Retrieve emails with matching message body
            exchange_has_attachments   <bool> : Retrieve emails with attachments 
            exchange_order_by_recency  <bool> : Order retrieved emails by recency
            exchange_search_subfolders <bool> : Specifies whether to query a mailbox's subfolder
            exchange_start_date    <datetime> : Get emails on or after this date
            exchange_end_date      <datetime> : Get emails until after this date

        Returns:
        --------
            Response <dict> : A response with the mails retrieved and their attributes
                              or the error message if the retrieval process failed
        """
        rh = ResultsHandler(package_name=PACKAGE_NAME, fn_inputs=fn_inputs)
        function_parameters = {}
        for key, value in fn_inputs._asdict().items():
            function_parameters[INPUTS_MAP[key]] = value
        mail_limit = function_parameters.get("num_emails") if function_parameters.get("num_emails") else 0

        if not function_parameters.get("src_folder"):
            function_parameters["src_folder"] = self.options.get('default_folder_path')
            self.LOG.info('No folder path was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(f"{parameter} : {str(function_parameters.get(parameter))}")

        try:
            interface = exchange_interface(self.rc, self.options)
            yield StatusMessage("Finding emails")
            retrieved_emails = interface.get_emails(function_parameters)
            num_deleted = retrieved_emails.count()

            yield StatusMessage(f"Search email operation complete, {num_deleted} emails found")
            results = interface.create_email_function_results(retrieved_emails, function_parameters.get("num_emails"))

            if num_deleted == 0:
                msg = "Failed to perform operation as 0 emails were retrieved"

            elif function_parameters["hard_delete"]:
                msg = "Permanently deleted emails"
                for no, mail in enumerate(retrieved_emails, 1):
                    if no == mail_limit:
                        break
                    mail.delete()

            else:
                msg = "Moved emails to trash"
                for no, mail in enumerate(retrieved_emails, 1):
                    if no == mail_limit:
                        break
                    mail.move_to_trash()

            self.LOG.info(msg)
            yield StatusMessage(msg)

            yield StatusMessage(f"{num_deleted} emails deleted")
            yield rh.success(results)

        except Exception as err:
            yield rh.fail(reason=str(err))
