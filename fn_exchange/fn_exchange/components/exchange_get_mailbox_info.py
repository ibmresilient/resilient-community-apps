# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_get_mailbox_info"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_get_mailbox_info")
    def _exchange_get_mailbox_info_function(self, event, *args, **kwargs):
        """Function: Get mailbox info from exchange"""
        try:
            # Get the function parameters:
            log = logging.getLogger(__name__)
            get_user = kwargs.get('exchange_get_email')
            log.info("exchange_get_email: %s" % get_user)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Connect to server
            username = self.options.get("email")
            yield StatusMessage("Getting mailbox info for %s" % get_user)
            account = utils.connect_to_account(username)

            # Get mailbox info
            info = account.protocol.resolve_names([get_user])
            if len(info) == 1:
                info = info[0]
                results = {
                    "name": info.name,
                    "email_address": info.email_address,
                    "routing_type": info.routing_type,
                    "mailbox_type": info.mailbox_type,
                    "success": True
                }
            else:
                results = {"success": False}
                yield StatusMessage("No mailbox found for %s" % get_user)

            yield StatusMessage("Done getting mailbox info")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()