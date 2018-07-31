# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


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
            exchange_emails = kwargs.get("exchange_emails")  # text
            exchange_folder_path = kwargs.get("exchange_folder_path")  # text
            exchange_sender = kwargs.get("exchange_sender")  # text
            exchange_start_date = kwargs.get("exchange_start_date")  # datepicker
            exchange_end_date = kwargs.get("exchange_end_date")  # datepicker

            log = logging.getLogger(__name__)
            log.info("exchange_emails: %s", exchange_emails)
            log.info("exchange_folder_path: %s", exchange_folder_path)
            log.info("exchange_sender: %s", exchange_sender)
            log.info("exchange_start_date: %s", exchange_start_date)
            log.info("exchange_end_date: %s", exchange_end_date)

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