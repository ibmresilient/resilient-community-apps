# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'have_i_been_pwned_get_breaches"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_hibp", {})

        self.PROXIES = {}
        # Get proxies
        PROXY_HTTP = self.get_config_option("hibp_proxy_http", True)
        PROXY_HTTPS = self.get_config_option("hibp_proxy_https", True)

        if PROXY_HTTP is not None:
            self.PROXIES["http"] = PROXY_HTTP

        if PROXY_HTTPS is not None:
            self.PROXIES["https"] = PROXY_HTTP

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = self.options.get(option_name)

        if not option and optional is False:
            err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this " \
                  "function".format(option_name)
            raise ValueError(err)
        else:
            return option

    @function("have_i_been_pwned_get_breaches")
    def _have_i_been_pwned_get_breaches_function(self, event, *args, **kwargs):
        """Function: Get all breaches of an email address from Have I Been Pwned."""
        try:
            yield StatusMessage("starting...")

            HAVE_I_BEEN_PWNED_BREACH_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/"
            result_payload = ResultPayload("hibp", **kwargs)

            # Get the function parameters:
            email_address = kwargs.get("email_address")  # text

            log = logging.getLogger(__name__)
            if email_address is not None:
                log.info("email_address: %s", email_address)
            else:
                raise ValueError("email_address is required to run this function")

            hibp_api_key = self.get_config_option("hibp_api_key")

            headers={
                        'User-Agent': 'Resilient HIBP/2.0',
                        'hibp-api-key': hibp_api_key
                    }

            breach_url = "{0}{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, email_address)
            breaches_response = requests.get(breach_url, headers=headers, proxies=self.PROXIES)

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
                log.warn("Have I Been Pwned returned " + str(breaches_response.status_code) + " unexpected status code")
                yield FunctionError("Have I Been Pwned returned " + str(breaches_response.status_code) + " status code")

            results = {
                "Breaches": breaches
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            yield FunctionError(e)
