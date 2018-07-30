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
            if kwargs.get('exchange_email') is None:
                username = self.options.get('email')
                log.info('No connection email was specified, using value from config file')
            else:
                username = kwargs.get('exchange_email')
            get_user = kwargs.get('exchange_get_email')
            log.info("username: %s" % username)
            log.info("get_user: %s" % get_user)

            # Load opts and initialize utils
            opts = {'cert_verify': self.options.get('cert_verify') == "True",
                    'server': self.options.get('server'),
                    'username': self.options.get('username'),
                    'email:': self.options.get('email'),
                    'password': self.options.get('password'),
                    'default_folder_path': self.options.get('default_folder_path'),
                    'timezone': self.options.get('timezone')}
            utils = exchange_utils(**opts)

            # Connect to account
            yield StatusMessage("Connecting to %s ..." % username)
            account = utils.connect_to_account(username)
            yield StatusMessage("Connected")

            # Get mailbox info
            yield StatusMessage("Getting mailbox info")
            info = account.protocol.resolve_names([get_user])[0]
            yield StatusMessage("Done getting mailbox info")

            results = {
                "name": info.name,
                "email_address": info.email_address,
                "routing_type": info.routing_type,
                "mailbox_type": info.mailbox_type
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()