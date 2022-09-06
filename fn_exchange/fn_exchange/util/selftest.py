# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_exchange
"""

import logging
from fn_exchange.util.exchange_utils import exchange_utils

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to confirm access to Miscrosoft Exchange API connectivity.
    """
    options = opts.get("fn_exchange", {})
    username = options.get("email")
    try:

        # Initialize utils
        utils = exchange_utils(options, opts)

        # Connect to server
        account = utils.connect_to_account(username)

        # Get mailbox info
        info = account.protocol.resolve_names([username])

        if isinstance(info, list) and info[0].email_address == username:
            return {"state": "success"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}
