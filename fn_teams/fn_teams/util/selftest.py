# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_teams
"""

import logging

from urllib import parse
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
    options = opts.get("fn_teams", {})
    rc = RequestsCommon(opts, options)
    required_parameters = {
        "rc"  : rc,
        "log" : log}

    try:
        authenticator = TeamsAuthentication(required_parameters, options)
        header = authenticator.authenticate()
        authenticated = True

    except IntegrationError as err:
        log.error(err)
        return {
            "state": "failure",
            "reason": str(err)}

    if authenticated:
        rc.execute(method="get",
            url=parse.urljoin(constants.BASE_URL, constants.LIST_USERS),
            headers=header)

        return {
            "state": "success",
            "reason": "success"}
