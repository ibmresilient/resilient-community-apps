# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_teams
"""
import logging
from urllib import parse
from datetime import datetime

import pymsteams
from resilient_lib import IntegrationError, RequestsCommon

from fn_teams.lib import constants
from fn_teams.lib.microsoft_authentication import MicrosoftAuthentication

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# channel reference for testing
SELF_TEST = "selftest"
APPLICATION_PERMISSION_TEST = "application_id"
DELEGATED_PERMISSION_TEST = "refresh_token"

def selftest_function(opts):
    """
    Self test function that allows for testing the configurations and
    credentials by quickly establishing a connection with the endpoint.
    Two tests are performed here.

    TEST 1: Authentication: Application Permission
        This tests the ability of the application to interface with the
        endpoint and to create groups, teams and channels.
    
    TEST 2: Authentication: Delegation Permission
        This tests the ability of the application to interface with the
        endpoint and to read messages.

    Test 3 POST CHANNEL MESSAGE:
        This tests the ability of the application to post a message on a
        teams channel using webhooks.

    Self Objects:
    -------------
        rc      <rc> : Resilient wrapper for Requests object
        log <logger> : Resilient wrapper for logger object

    Returns:
    --------
        result <dict> : Test state and reason
    """
    err_reason, authenticated = "", False
    test_pass_1, test_pass_2, test_pass_3 = False, False, False


    options = opts.get("fn_teams", {})
    rc = RequestsCommon(opts, options)

    # TEST 1: Teams Authentication: Application permissions
    log.info("Testing Application permissions")
    if APPLICATION_PERMISSION_TEST in options:
        try:
            authenticator = MicrosoftAuthentication(rc, options)
            header = authenticator.authenticate_application_permissions()
            authenticated = True
            err_reason += constants.MSG_APP_AUTHENTICATION_PASSED

        except IntegrationError as err:
            log.error(str(err))
            err_reason += constants.MSG_APP_AUTHENTICATION_FAILED.format(str(err))

        if authenticated:
            log.info("Testing Application scopes")
            try:
                rc.execute(method="get",
                    url=parse.urljoin(constants.BASE_URL, constants.URL_LIST_USERS),
                    headers=header)
                err_reason += constants.MSG_LIST_USER_PASSED
                test_pass_1 = True

            except IntegrationError as err:
                log.error(str(err))
                err_reason += constants.MSG_LIST_USER_FAILED.format(str(err))
                test_pass_1 = False
    else:
        log.warn(constants.WARN_NO_APP_PERMISSION)

    # TEST 2: Teams Authentication: Delegated permissions
    if DELEGATED_PERMISSION_TEST in options:
        log.info("Testing Delegated permissions")
        refresh_token = options.get(DELEGATED_PERMISSION_TEST)
        try:
            authenticator = MicrosoftAuthentication(rc, options)
            header = authenticator.authenticate_delegated_permissions(refresh_token)
            test_pass_2 = True
            err_reason += constants.MSG_DEL_AUTHENTICATION_PASSED

        except IntegrationError as err:
            log.error(str(err))
            err_reason += constants.MSG_DEL_AUTHENTICATION_FAILED.format(str(err))
    else:
        # Test 2 is skipped if refresh_token is not found in app.conf
        log.warn(constants.WARN_NO_DEL_PERMISSION)

    if options.get(SELF_TEST):
        # TEST 3: Teams POST MESSAGE (Skipped if selftest option not found in app.conf)
        log.info("Testing webhooks")
        webhook = options.get(SELF_TEST)
        try:
            proxy = rc.get_proxies() if rc.get_proxies() else {}
            card = pymsteams.connectorcard(
                webhook,
                http_proxy=opts.get('proxy_http', proxy.get('http')),
                https_proxy=opts.get('proxy_http', proxy.get('https')),
                http_timeout=60)

            card.title("SOAR SelfTest")
            card.text(datetime.ctime(datetime.now()))
            card.send()

            err_reason += constants.MSG_POST_MSG_PASSED
            test_pass_3 = True

        except IntegrationError as err:
            log.error(str(err))
            err_reason += constants.MSG_POST_MSG_FAILED.format(str(err))
            test_pass_3 = False
    else:
        # Test 3 is skipped if selftest option is not found in app.conf
        log.warn(constants.WARN_NO_WEBHOOKS_FOUND)

    if test_pass_1 or test_pass_2 or test_pass_3:
        return {
            "state" : "success",
            "reason": err_reason}

    return {
        "state": "failure",
        "reason": err_reason}
