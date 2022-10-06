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
from fn_teams.lib.teams_authentication import TeamsAuthentication

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

# channel reference for testing
SELF_TEST = "selftest"

def selftest_function(opts):
    """
    Self test function that allows for testing the configurations and
    credentials by quickly establishing a connection with the endpoint.

    Self Objects:
    -------------
        rc      <rc> : Resilient wrapper for Requests object
        log <logger> : Resilient wrapper for logger object

    Returns:
    --------
        result <dict> : Test state and reason
    """
    AUTHENTICATED = False
    TEST_PASS_1 = False
    TEST_PASS_2 = False
    ERR_REASON  = ""

    options = opts.get("fn_teams", {})
    rc = RequestsCommon(opts, options)
    required_parameters = {
        "rc"     : rc,
        "logger" : log}

    try:
        authenticator = TeamsAuthentication(required_parameters, options)
        header = authenticator.authenticate()
        AUTHENTICATED = True
        ERR_REASON += constants.MSG_AUTHENTICATION_PASSED

    except Exception as err:
        log.error(str(err))
        ERR_REASON += constants.MSG_AUTHENTICATION_FAILED.format(str(err))

    if AUTHENTICATED:
        try:
            rc.execute(method="get",
                url=parse.urljoin(constants.BASE_URL, constants.LIST_USERS),
                headers=header)
            ERR_REASON += constants.MSG_LIST_USER_PASSED
            TEST_PASS_1 = True

        except Exception as err:
            log.error(str(err))
            ERR_REASON += constants.MSG_LIST_USER_FAILED.format(str(err))
            TEST_PASS_1 = False


    if options.get(SELF_TEST):
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

            ERR_REASON += constants.MSG_POST_MSG_PASSED
            TEST_PASS_2 = True

        except Exception as err:
            log.error(str(err))
            ERR_REASON += constants.MSG_POST_MSG_FAILED.format(str(err))
            TEST_PASS_2 = False
    else:
        log.warn(constants.WARN_NO_WEBHOOKS_FOUND)
        TEST_PASS_2 = True

    if AUTHENTICATED and TEST_PASS_1 and TEST_PASS_2:
        return{
            "state" : "success",
            "reason": ERR_REASON
            }

    else:
        return {
            "state": "failure",
            "reason": ERR_REASON
            }
