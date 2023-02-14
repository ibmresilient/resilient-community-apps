# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_lib import validate_fields
from resilient_circuits import (AppFunctionComponent, app_function, 
                                StatusMessage, FunctionResult)

from fn_exchange.lib import constants
from fn_exchange.lib.exchange_utils import exchange_interface


FN_NAME = "exchange_move_emails"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, constants.PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Query the server to find emails with the provided parameters and move them to a
        destination folder.

        FN Inputs:
        -------
            delete_src_folder      <bool> : True delete the source folder
            dst_folder              <str> : Destination path to move the email
            force_delete           <bool> : True deletes source folder with subfolders
                                            False stops the deletion process on detecting subfolders

            username                <str> : Primary email account to be used
            num_emails              <int> : Limit the number of emails retrieved
            email_ids               <str> : Retrieve emails from all these senders
            src_folder              <str> : Source folder to move the mails from
            sender                  <str> : Only find emails from this specified sender
            subject                 <str> : Retrieve emails with matching message subject
            body                    <str> : Retrieve emails with matching message body
            has_attachments        <bool> : Retrieve emails with attachments 
            order_by_recency       <bool> : Order retrieved emails by recency
            search_subfolders      <bool> : Specifies whether to query a mailbox's subfolder
            start_date         <datetime> : Get emails on or after this date
            end_date           <datetime> : Get emails until after this date

        Returns:
        --------
            Response <dict> : A response with the mails retrieved and their attributes
                              or the error message if the retrieval process failed
        """
        function_parameters = {}
        
        validate_fields([
            "exchange_destination_folder_path",
            "exchange_delete_source_folder"], fn_inputs)

        function_parameters["delete_src_folder"] = fn_inputs.exchange_delete_source_folder
        function_parameters["dst_folder"] = fn_inputs.exchange_destination_folder_path
        function_parameters["force_delete"] = fn_inputs.exchange_force_delete_subfolders

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

        yield StatusMessage("Finding emails")
        interface = exchange_interface(self.rc, self.options)
        results, retrieved_emails = interface.move_emails(
            function_parameters, function_parameters["delete_src_folder"])
        
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
        
        if function_parameters["delete_src_folder"]:
            yield StatusMessage(f"Deleting folder {function_parameters['src_folder']}")
            src_folder.delete()

        results["src_folder"] = function_parameters["src_folder"]
        results["dst_folder"] = function_parameters["dst_folder"]
        yield FunctionResult(results, success=True)

        try:
            pass

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
