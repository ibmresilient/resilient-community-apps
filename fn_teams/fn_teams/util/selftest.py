# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
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
from fn_teams.lib.microsoft_messages import MessageClient

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

# channel reference for testing
SELF_TEST = "selftest"
SELF_TEST_WORKFLOWS = "selftest_workflows"
APPLICATION_PERMISSION_TEST = "application_id"
DELEGATED_PERMISSION_TEST = "refresh_token"

SELFTEST_MSG = "SOAR SelfTest"

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
        LOG <logger> : Resilient wrapper for logger object

    Returns:
    --------
        result <dict> : Test state and reason
    """
    err_reason = ""
    all_tests = True


    options = opts.get("fn_teams", {})
    rc = RequestsCommon(opts, options)

    # TEST 1: Teams Authentication: Application permissions
    LOG.info("Testing Application permissions")
    if APPLICATION_PERMISSION_TEST in options:
        authenticated = False
        try:
            authenticator = MicrosoftAuthentication(rc, options)
            header = authenticator.authenticate_application_permissions()
            authenticated = True
            err_reason += constants.MSG_APP_AUTHENTICATION_PASSED

        except IntegrationError as err:
            LOG.error(str(err))
            authenticated = False
            err_reason += constants.MSG_APP_AUTHENTICATION_FAILED.format(str(err))

        if authenticated:
            LOG.info("Testing Application scopes")
            try:
                rc.execute(method="get",
                    url=parse.urljoin(constants.BASE_URL, constants.URL_LIST_USERS),
                    headers=header)
                err_reason += constants.MSG_LIST_USER_PASSED

            except IntegrationError as err:
                LOG.error(str(err))
                err_reason += constants.MSG_LIST_USER_FAILED.format(str(err))
                all_tests &= False
    else:
        LOG.warning(constants.WARN_NO_APP_PERMISSION)

    # TEST 2: Teams Authentication: Delegated permissions
    if DELEGATED_PERMISSION_TEST in options:
        LOG.info("Testing Delegated permissions")
        refresh_token = options.get(DELEGATED_PERMISSION_TEST)
        try:
            authenticator = MicrosoftAuthentication(rc, options)
            header = authenticator.authenticate_delegated_permissions(refresh_token)
            err_reason += constants.MSG_DEL_AUTHENTICATION_PASSED

        except IntegrationError as err:
            LOG.error(str(err))
            err_reason += constants.MSG_DEL_AUTHENTICATION_FAILED.format(str(err))
            all_tests &= False
    else:
        # Test 2 is skipped if refresh_token is not found in app.conf
        LOG.warning(constants.WARN_NO_DEL_PERMISSION)

    test_pass_3, err_reason_test_3 = test_post_channel(rc, opts, options)
    err_reason += err_reason_test_3
    all_tests &= test_pass_3

    test_pass_4, err_reason_test_4 = test_post_workflows(rc, options)
    err_reason += err_reason_test_4
    all_tests &= test_pass_4

    if all_tests:
        return {
            "state" : "success",
            "reason": err_reason}

    return {
        "state": "failure",
        "reason": err_reason}

def test_post_channel(rc, opts, options):
    err_reason = ""
    test_pass = True

    if options.get(SELF_TEST):
        # TEST 3: Teams POST MESSAGE (Skipped if selftest option not found in app.conf)
        LOG.info("Testing webhooks")
        webhook = options.get(SELF_TEST)
        try:
            proxy = rc.get_proxies() if rc.get_proxies() else {}
            card = pymsteams.connectorcard(
                webhook,
                http_proxy=opts.get('proxy_http', proxy.get('http')),
                https_proxy=opts.get('proxy_http', proxy.get('https')),
                http_timeout=60)

            card.title(SELFTEST_MSG)
            card.text(datetime.ctime(datetime.now()))
            card.send()

            err_reason += constants.MSG_POST_MSG_PASSED

        except IntegrationError as err:
            LOG.error(str(err))
            err_reason += constants.MSG_POST_MSG_FAILED.format(str(err))
            test_pass = False

    return (test_pass, err_reason)

def test_post_workflows(rc, options):
    err_reason = ""
    test_pass = True

    if options.get(SELF_TEST_WORKFLOWS):
        # TEST 4: Teams POST MESSAGE WORKFLOWS (Skipped if selftest_workflows option not found in app.conf)
        LOG.info("Testing workflows")
        webhook = options.get(SELF_TEST_WORKFLOWS)
        message_client = MessageClient(rc)

        body = {
            "type": "TextBlock",
            "text": SELFTEST_MSG,
            "isVisible": True
        }

        teams_payload = return_test_adaptive_card(body)

        proxies = rc.get_proxies()

        try:
            results = message_client.post_message_workflow(
                webhook,
                teams_payload,
                proxies
            )

            if results.get("status_code") and int(results["status_code"]/100) == 2:
                err_reason = constants.MSG_POST_WORKFLOW_PASSED
            else:
                err_reason = constants.MSG_POST_WORKFLOW_FAILED.format(results["status_code"]/100)
                test_pass = False
        except Exception as err:
            test_pass = False
            err_reason = constants.MSG_POST_WORKFLOW_FAILED.format(str(err))

    return (test_pass, err_reason)

def return_test_adaptive_card(body):
    """return format for adaptive card

    :param body: body of message to send as an adaptive card
    :type body: dict
    :return: adaptive card
    :rtype: dict
    """
    return {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.4",
            "body": [body],
            "actions": []
        }
    }
