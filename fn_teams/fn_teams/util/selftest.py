# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_teams
"""

import logging
import pymsteams

from urllib import parse
from datetime import datetime
from resilient_lib import IntegrationError, RequestsCommon

from fn_teams.lib import constants
from fn_teams.lib.microsoft_authentication import MicrosoftAuthentication

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# channel reference for testing
SELF_TEST = "selftest"

def selftest_function(opts):
    """
    Self test function that allows for testing the configurations and
    credentials by quickly establishing a connection with the endpoint.
    Two tests are performed here. 

    TEST 1: Authentication
        This tests the ability of the application to interface with the
        endpoint and to create groups, teams and channels.

    Test 2 POST CHANNEL MESSAGE:
        This tests the ability of the application to post a message on a
        teams channel using webooks.

    Self Objects:
    -------------
        rc      <rc> : Resilient wrapper for Requests object
        log <logger> : Resilient wrapper for logger object

    Returns:
    --------
        result <dict> : Test state and reason
    """
    err_reason, authenticated = "", False
    test_pass_1, test_pass_2 = False, False


    options = opts.get("fn_teams", {})
    rc = RequestsCommon(opts, options)
    required_parameters = {
        "rc"     : rc,
        "logger" : log
        }

    ''' TEST 1: Teams Authentication (Mandatory) '''
    try:
        authenticator = MicrosoftAuthentication(required_parameters, options)
        header = authenticator.authenticate()
        AUTHENTICATED = True
        err_reason += constants.MSG_AUTHENTICATION_PASSED

    except Exception as err:
        log.error(str(err))
        err_reason += constants.MSG_AUTHENTICATION_FAILED.format(str(err))

    if AUTHENTICATED:
        try:
            rc.execute(method="get",
                url=parse.urljoin(constants.BASE_URL, constants.LIST_USERS),
                headers=header)
            err_reason += constants.MSG_LIST_USER_PASSED
            test_pass_1 = True

        except Exception as err:
            log.error(str(err))
            err_reason += constants.MSG_LIST_USER_FAILED.format(str(err))
            test_pass_1 = False


    if options.get(SELF_TEST):
        ''' TEST 2: Teams POST MESSAGE (Skipped if selftest option not found in app.conf) '''
        webhook = options.get(SELF_TEST)
        try:
            card = pymsteams.connectorcard(
                webhook, 
                http_proxy=opts['proxy_http'] if opts.get('proxy_http') else None,
                https_proxy=opts['proxy_https'] if opts.get('proxy_https') else None,
                http_timeout=60
                )

            card.title("Resilient SelfTest")
            card.text(datetime.ctime(datetime.now()))
            card.send()

            err_reason += constants.MSG_POST_MSG_PASSED
            test_pass_2 = True

        except Exception as err:
            log.error(str(err))
            err_reason += constants.MSG_POST_MSG_FAILED.format(str(err))
            test_pass_2 = False
    else:
        ''' Test2 is skipped if selftest option is not found in app.conf '''
        log.warn(constants.WARN_NO_WEBHOOKS_FOUND)
        test_pass_2 = True

    if AUTHENTICATED and test_pass_1 and test_pass_2:
        return{
            "state" : "success",
            "reason": err_reason
            }

    else:
        return {
            "state": "failure",
            "reason": err_reason
            }
