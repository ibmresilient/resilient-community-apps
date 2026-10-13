# -*- coding: utf-8 -*-

import logging

from resilient_lib import validate_fields, RequestsCommon
from fn_webex.lib import constants
from fn_webex.lib.cisco_authentication import WebexAuthentication


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
        This function creates and schedules a Webex meeting.

        Config Options:
        ---------------
            clientID     (<str>) : Client ID of the integration created on developer.webex.com
            elientSecret (<str>) : Client Secret of the same integration
            refreshToken (<str>) : Refresh token generated using the OAuth Utilities Tool
            scope        (<str>) : Scopes selected during integraiton creation is to be
                                    specified in a space seperated fashion

        Self Objects:
        -------------
            rc           (<rc>)          : A resilient wrapper for Requests object
            logger       (<logger>)      : A resilient wrapper for logger obhect
            resclient    (<rest_client>) : Rest client to interact with the SOAR instance

        Raises:
        -------
            (<IntegrationError>): Raises an exception when the client doesn't authenticate.
    """
    app_configs = opts.get("fn_webex", {})
    validate_fields(["webex_site_url", "webex_timezone", "client_id",
                     "client_secret", "refresh_token", "scope"], app_configs)

    required_parameters = {}
    required_parameters["rc"] = RequestsCommon(opts, app_configs)
    required_parameters["logger"] = log
    required_parameters["tokenURL"] = app_configs.get("webex_site_url") + constants.TOKEN_URL

    try :
        authenticator = WebexAuthentication(required_parameters, app_configs)
        _ = authenticator.authenticate()
        return {
            "state": "success",
            "reason": "success"}

    except InterruptedError as err:
        return {
                "state": "failure",
                "reason": str(err)}
