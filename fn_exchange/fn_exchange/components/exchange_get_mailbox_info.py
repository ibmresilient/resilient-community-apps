# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (
    AppFunctionComponent, app_function, StatusMessage, FunctionResult)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME
from fn_exchange.lib.exchange_utils import exchange_interface

FN_NAME = "exchange_get_mailbox_info"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Get mailbox info from exchange"""
        try:
            # Get the function parameters:
            get_user = getattr(fn_inputs, 'exchange_get_email', None)
            self.LOG.info(f"exchange_get_email: {get_user}")

            utils = exchange_interface(self.rc, self.options)

            # Connect to server
            username = self.options.get("email")
            yield StatusMessage(f"Getting mailbox info for {get_user}")
            account = utils.connect_to_account(username)

            # Get mailbox info
            info = account.protocol.resolve_names([get_user])
            if len(info) == 1:
                info = info[0]
                results = {
                    "name": getattr(info, "name", ""),
                    "email_address" : getattr(info, "email_address", ""),
                    "routing_type"  : getattr(info, "routing_type", ""),
                    "mailbox_type"  : getattr(info, "mailbox_type", "")}
            else:
                yield FunctionResult({}, success=False, reason="Unable retrieve mailbox information")

                yield StatusMessage(f"No mailbox found for {get_user}")

            yield StatusMessage("Completed retrieving mailbox information")
            yield FunctionResult(results, success=True)

        except Exception as err:
            yield FunctionResult(results, success=False, reason=str(err))