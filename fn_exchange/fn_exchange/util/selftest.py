# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_exchange
"""

import logging
from resilient_lib import RequestsCommon
from fn_exchange.lib.exchange_utils import exchange_interface
from exchangelib import Mailbox
from typing import Tuple

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Simple test to confirm access to Microsoft Exchange API connectivity.
    """
    options = opts.get("fn_exchange", {})
    username = options.get("email")
    rc = RequestsCommon(opts, options)
    
    try:
        # Initialize utils
        utils = exchange_interface(rc, options)

        # Connect to server
        account = utils.connect_to_account(username)

        # Get mailbox info
        info = account.protocol.resolve_names([username], return_full_contact_data=True)

        if isinstance(info, list) and isinstance(info[0], Tuple) and isinstance(info[0][0], Mailbox):
            return {"state": "success"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}
