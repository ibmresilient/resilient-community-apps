# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_delete_emails"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_delete_emails")
    def _exchange_delete_emails_function(self, event, *args, **kwargs):
        """Function: Delete emails with the specified parameters"""
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_folder_path = kwargs.get("exchange_folder_path")  # text
            exchange_hard_delete = kwargs.get("exchange_hard_delete") # boolean
            exchange_email_ids = kwargs.get("exchange_email_ids")  # text
            exchange_sender = kwargs.get("exchange_sender")  # text
            exchange_message_subject = kwargs.get("exchange_message_subject") # text
            exchange_message_body = kwargs.get("exchange_message_body") # text
            exchange_start_date = kwargs.get("exchange_start_date")  # datepicker
            exchange_end_date = kwargs.get("exchange_end_date")  # datepicker
            exchange_has_attachments = kwargs.get("exchange_has_attachments")  # boolean
            exchange_order_by_recency = kwargs.get("exchange_order_by_recency")  # boolean
            exchange_num_emails = kwargs.get("exchange_num_emails")  # int
            exchange_search_subfolders = kwargs.get("exchange_search_subfolders") # boolean

            log = logging.getLogger(__name__)
            if exchange_folder_path is None:
                exchange_folder_path = self.options.get('default_folder_path')
                log.info('No folder path was specified, using value from config file')
            log.info("exchange_email: %s" % exchange_email)
            log.info("exchange_folder_path: %s" % exchange_folder_path)
            log.info("exchange_hard_delete: %s" % exchange_hard_delete)
            log.info("exchange_email_ids: %s" % exchange_email_ids)
            log.info("exchange_sender: %s" % exchange_sender)
            log.info("exchange_message_subject: %s" % exchange_message_subject)
            log.info("exchange_message_body: %s" % exchange_message_body)
            log.info("exchange_start_date: %s" % exchange_start_date)
            log.info("exchange_end_date: %s" % exchange_end_date)
            log.info("exchange_has_attachments: %s" % exchange_has_attachments)
            log.info("exchange_order_by_recency: %s" % exchange_order_by_recency)
            log.info("exchange_num_emails: %s" % exchange_num_emails)
            log.info("exchange_search_subfolders: %s" % exchange_search_subfolders)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Find emails
            yield StatusMessage("Finding emails")
            emails = utils.get_emails(exchange_email, exchange_folder_path, exchange_email_ids, exchange_sender,
                                      exchange_message_subject, exchange_message_body, exchange_start_date,
                                      exchange_end_date, exchange_has_attachments, exchange_order_by_recency,
                                      exchange_num_emails, exchange_search_subfolders)
            yield StatusMessage("Done finding emails")

            # Get function results
            results = utils.create_email_function_results(emails)
            num_deleted = emails.count()

            # Delete Emails
            yield StatusMessage("Deleting emails")
            if exchange_hard_delete:
                emails.delete()
            else:
                for item in emails:
                    item.move_to_trash()
            yield StatusMessage("Done deleting emails, %d emails deleted" % num_deleted)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()