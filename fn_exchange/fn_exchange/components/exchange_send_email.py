# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


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
            log.info("exchange_email: %s", exchange_email)
            log.info("exchange_message_subject: %s", exchange_message_subject)
            log.info("exchange_message_body: %s", exchange_message_body)
            log.info("exchange_emails: %s", exchange_emails)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()