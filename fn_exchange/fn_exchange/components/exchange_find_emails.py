# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_find_emails"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_find_emails")
    def _exchange_find_emails_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_folder_path = kwargs.get("exchange_folder_path")  # text
            exchange_sender = kwargs.get("exchange_sender")  # text
            exchange_start_date = kwargs.get("exchange_start_date")  # datepicker
            exchange_end_date = kwargs.get("exchange_end_date")  # datepicker

            log = logging.getLogger(__name__)
            # Use default connection email if one was not specified
            if exchange_email is None:
                exchange_email = self.options.get('email')
                log.info('No connection email was specified, using value from config file')
            log.info("exchange_email: %s", exchange_email)
            log.info("exchange_folder_path: %s", exchange_folder_path)
            log.info("exchange_sender: %s", exchange_sender)
            log.info("exchange_start_date: %s", exchange_start_date)
            log.info("exchange_end_date: %s", exchange_end_date)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Find emails
            yield StatusMessage("Finding emails")
            emails = utils.get_emails(exchange_email, exchange_folder_path, exchange_sender,
                                      exchange_start_date, exchange_end_date)
            yield StatusMessage("Done finding emails")

            # Populate results with query data
            results = {}
            for email in emails:
                results[email.message_id] = {}
                curr_email = results[email.message_id]
                curr_email['sender_name'] = email.sender.name
                curr_email['sender_email'] = email.sender.email_address
                curr_email['subject'] = email.subject
                curr_email['body'] = email.body

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
