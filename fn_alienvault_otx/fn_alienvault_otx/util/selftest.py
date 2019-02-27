# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_alienvault_otx
"""

import logging
from fn_alienvault_otx.util.alienvault_modules import *
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_alienvault_otx", {})

    # Getting Configuration Data
    ALIEN_VAULT_URL = options.get('av_base_url')+"/user/me"
    ALIEN_VAULT_KEY = options.get('av_api_key')

    # Api Controller Class Instance
    ApiCallController_instance = ApiCallController()

    # creating Proxy dict to send in get api call
    PROXIES = ApiCallController.format_proxy_data(options.get('proxy'))

    # Api Get Call Header
    HEADER = ApiCallController.create_header(ALIEN_VAULT_KEY)

    # initialising the Session
    _request_session = ApiCallController_instance.session()

    # Connection to Alien Vault OTX
    try:

        response = _request_session.get(ALIEN_VAULT_URL, headers=HEADER, proxies=PROXIES)

        response_data = ApiCallController.response_handle_errors(response).json()
        log.info("Successfully Established Connection to Alien Vault OTX")

        for k, v in response_data.items():
            log.info("{}:{}".format(k, v))

        # Closing Connection
        requests.session().close()
        return {"state": "Success"}
    except requests.exceptions.RetryError:
        raise RetryError()
    except Exception as e:
        log.info(" Failed Connection to Alien Vault OTX : {}".format(e))

        # Closing Connection
        requests.session().close()
        return {"state": "Failed"}
