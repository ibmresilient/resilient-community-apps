# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_lib import validate_fields
from resilient_circuits import (AppFunctionComponent, app_function, 
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, INPUTS_MAP, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface


FN_NAME = "exchange_move_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Query the server to find emails with the provided parameters and move them to a
        destination folder.

        FN Inputs:
        -------
            exchange_delete_source_folder    <bool> : True delete the source folder
            exchange_destination_folder_path  <str> : Destination path to move the email
            exchange_force_delete_subfolders <bool> : True deletes source folder with subfolders
                                                      False stops the deletion process on detecting subfolders

            exchange_email                    <str> : Primary email account to be used
            exchange_num_emails               <int> : Limit the number of emails retrieved
            exchange_email_ids                <str> : Retrieve emails from all these senders
            exchange_folder_path              <str> : Custom folder path to find emails
            exchange_sender                   <str> : Only find emails from this specified sender
            exchange_message_subject          <str> : Retrieve emails with matching message subject
            exchange_message_body             <str> : Retrieve emails with matching message body
            exchange_has_attachments         <bool> : Retrieve emails with attachments 
            exchange_order_by_recency        <bool> : Order retrieved emails by recency
            exchange_search_subfolders       <bool> : Specifies whether to query a mailbox's subfolder
            exchange_start_date          <datetime> : Get emails on or after this date
            exchange_end_date            <datetime> : Get emails until after this date

        Returns:
        --------
            Response <dict> : A response with the mails retrieved and their attributes
                              or the error message if the retrieval process failed
        """
        rh = ResultsHandler(package_name=PACKAGE_NAME, fn_inputs=fn_inputs)
        function_parameters = {}
        
        validate_fields([
            "exchange_destination_folder_path",
            "exchange_delete_source_folder",
            "exchange_force_delete_subfolders"], fn_inputs)

        delete_src_folder = fn_inputs.exchange_delete_source_folder
        function_parameters = {}
        for key, value in fn_inputs._asdict().items():
            function_parameters[INPUTS_MAP[key]] = value

        if not function_parameters.get("src_folder"):
            function_parameters["src_folder"] = self.options.get('default_folder_path')
            self.LOG.info('No folder path was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(" ".join([parameter, ":", str(function_parameters.get(parameter))]))

        yield StatusMessage("Finding emails")
        interface = exchange_interface(self.rc, self.options)
        results, retrieved_emails = interface.move_emails(
            function_parameters, delete_src_folder)
        
        src_folder = results.get("src_folder")
        dst_folder = results.get("dst_folder")

        if results.get("email_ids") == 0:
            msg = "Failed to perform operation as 0 emails were retrieved"
        else:
            for email in retrieved_emails:
                email.move(dst_folder)
            msg = f"Moved emails to {function_parameters['dst_folder']}"

        self.LOG.info(msg)
        yield StatusMessage(msg)
        yield StatusMessage(f"{len(results.get('email_ids'))} emails were moved")
        
        if delete_src_folder:
            yield StatusMessage(f"Deleting folder {function_parameters['src_folder']}")
            src_folder.delete()

        results["src_folder"] = function_parameters["src_folder"]
        results["dst_folder"] = function_parameters["dst_folder"]
        yield rh.success(results)

        try:
            pass

        except Exception as err:
            yield rh.fail(reason=str(err))
