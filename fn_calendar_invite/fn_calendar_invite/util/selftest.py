# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_calendar_invite
"""

import logging
from resilient_lib import validate_fields
from fn_calendar_invite.lib.calendar_invite_util import send_email

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

PACKAGE_NAME= "fn_calendar_invite"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get(PACKAGE_NAME, {})

    validate_fields(['email_username', 'email_password', 'email_nickname', 'email_host', 'email_port'], app_configs)

    username = app_configs.get("email_username")
    password = app_configs.get("email_password")
    nickname = app_configs.get("email_nickname")
    host = app_configs.get("email_host")
    port = app_configs.get("email_port")

    # Build the email message string to be sent.
    sender = u"{} <{}>".format(nickname, username)
    test_message = "This is a test message from {0} selftest".format(PACKAGE_NAME)

    try:
        # Connect to SMTP server and send the test message.
        send_email(host, port, sender, username, password, username, test_message)
        return {"state": "success",
                "reason": "success"}
    except Exception as err:
        log.error(err)
        return {"state": "failure",
                "reason": err}