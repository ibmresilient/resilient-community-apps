# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import time
from fn_hibp.lib.common import HAVE_I_BEEN_PWNED_PASTES_URL, get_config_option, make_headers, get_proxies
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'have_i_been_pwned_get_pastes"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_hibp", {})

        self.proxies = get_proxies(self.options)

    @function("have_i_been_pwned_get_pastes")
    def _have_i_been_pwned_get_pastes_function(self, event, *args, **kwargs):
        """Function: Get all pastes of an email account from Have I Been Pwned."""
        try:
            yield StatusMessage("starting...")

            result_payload = ResultPayload("hibp", **kwargs)

            log = logging.getLogger(__name__)

            # Get the function parameters:
            email_address = kwargs.get("email_address")  # text
            if email_address is not None:
                log.info("email_address: %s", email_address)
            else:
                raise ValueError("email_address is required to run this function")

            hibp_api_key = get_config_option(self.options, "hibp_api_key")
            headers= make_headers(hibp_api_key)

            breach_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_PASTES_URL, email_address)
            pastes_response = requests.get(breach_url, headers=headers, proxies=self.proxies)

            pastes = None
            # Good response
            if pastes_response.status_code == 200:
                pastes = pastes_response.json()
            # 404 is returned when an email was not found
            elif pastes_response.status_code == 404:
                yield StatusMessage("No pastes found on email address: {}".format(email_address))
                pastes = None
            # Rate limit was hit, wait 2 seconds and try again
            elif pastes_response.status_code == 429:
                time.sleep(2)
            else:
                msg = "Have I Been Pwned returned {} unexpected status code".format(pastes_response.status_code)
                log.warn(msg)
                yield FunctionError(msg)

            results = {
                "Pastes": pastes
            }

            yield StatusMessage("Lookup complete")
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            yield FunctionError(e)
