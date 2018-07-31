# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils
from exchangelib import Message


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_send_email"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_send_email")
    def _exchange_send_email_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_message_subject = kwargs.get("exchange_message_subject")  # text
            exchange_message_body = kwargs.get("exchange_message_body")  # text
            exchange_emails = kwargs.get("exchange_emails")  # text

            log = logging.getLogger(__name__)
            if exchange_email is None:
                exchange_email = self.options.get('email')
                log.info('No connection email was specified, using value from config file')
            log.info("exchange_email: %s", exchange_email)
            log.info("exchange_message_subject: %s", exchange_message_subject)
            log.info("exchange_message_body: %s", exchange_message_body)
            log.info("exchange_emails: %s", exchange_emails)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Get sender account
            yield StatusMessage("Connecting to account %s" % exchange_email)
            account = utils.connect_to_account(exchange_email)
            yield StatusMessage("Successfully connected to %s" % exchange_email)

            # Create email
            email = Message(
                account=account,
                folder=account.sent,
                subject=exchange_message_subject,
                body=exchange_message_body,
                to_recipients=exchange_emails.split(',')
            )

            # Send email
            yield StatusMessage("Sending email")
            email.send_and_save()
            yield StatusMessage("Email sent")

            results = {}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()