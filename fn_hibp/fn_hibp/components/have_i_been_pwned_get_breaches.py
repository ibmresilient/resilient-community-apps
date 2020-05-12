# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import time
from fn_hibp.lib.common import HAVE_I_BEEN_PWNED_BREACH_URL, get_config_option, make_headers, get_proxies
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'have_i_been_pwned_get_breaches"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_hibp", {})

        self.proxies = get_proxies(self.options)

    @function("have_i_been_pwned_get_breaches")
    def _have_i_been_pwned_get_breaches_function(self, event, *args, **kwargs):
        """Function: Get all breaches of an email address from Have I Been Pwned."""
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
            headers = make_headers(hibp_api_key)

            breach_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, email_address)
            breaches_response = requests.get(breach_url, headers=headers, proxies=self.proxies)

            breaches = None
            # Good response
            if breaches_response.status_code == 200:
                breaches = breaches_response.json()
            # 404 is returned when an email was not found
            elif breaches_response.status_code == 404:
                yield StatusMessage("No breaches found on email address: {}".format(email_address))
                breaches = None
            # Rate limit was hit, wait 2 seconds and try again
            elif breaches_response.status_code == 429:
                time.sleep(2)
            else:
                msg = "Have I Been Pwned returned {} unexpected status code".format(breaches_response.status_code)
                log.warning(msg)
                yield FunctionError(msg)

            results = {
                "Breaches": breaches
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            yield FunctionError(e)
