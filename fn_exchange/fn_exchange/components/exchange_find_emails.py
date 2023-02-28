# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, INPUTS_MAP, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface

FN_NAME = "exchange_find_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Query the server to find emails with the provided parameters. This function also
        allows for limiting the number of emails retrieved, searching different folder
        paths, ordering retrieved information by recency, searching subfolders and finding
        emails between specific dates.

        FN Inputs:
        -------
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

        if not function_parameters.get("src_folder"):
            function_parameters["src_folder"] = self.options.get('default_folder_path')
            self.LOG.info('No folder path was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(f"{parameter} : {str(function_parameters.get(parameter))}")

        try:
            utils = exchange_interface(self.rc, self.options)
            yield StatusMessage("Finding emails")
            retrieved_emails = utils.get_emails(function_parameters)

            yield StatusMessage(f"{retrieved_emails.count()} emails found")
            out = (retrieved_emails, function_parameters.get("num_emails"))
            results = utils.create_email_function_results(retrieved_emails, function_parameters.get("num_emails"))
            yield StatusMessage(f"Search email operation complete, {len(results.get('emails'))} emails found")
            yield rh.success(results)

        except Exception as err:
            yield rh.fail(reason=str(err))
