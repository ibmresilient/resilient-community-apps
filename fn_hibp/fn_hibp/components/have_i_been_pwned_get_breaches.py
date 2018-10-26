# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'have_i_been_pwned_get_breaches"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_hibp", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_hibp", {})

    @function("have_i_been_pwned_get_breaches")
    def _have_i_been_pwned_get_breaches_function(self, event, *args, **kwargs):
        """Function: Get all breaches of an email address from Have I Been Pwned."""
        retry = True
        while retry:
            try:
                yield StatusMessage("starting...")
                start = time.time()

                HAVE_I_BEEN_PWNED_BREACH_URL = "https://haveibeenpwned.com/api/v2/breachedaccount/"

                # Get the function parameters:
                email_address = kwargs.get("email_address")  # text

                log = logging.getLogger(__name__)
                if email_address is not None:
                    log.info("email_address: %s", email_address)
                else:
                    raise ValueError("email_address is required to run this function")

                breach_url = "{0}{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, email_address)
                breaches_response = requests.get(breach_url, headers={'User-Agent': 'Resilient HIBP'})

                breaches = None
                # Good response
                if breaches_response.status_code == 200:
                    breaches = breaches_response.json()
                    retry = False
                # 404 is returned when an email was not found
                elif breaches_response.status_code == 404:
                    yield StatusMessage("No breaches found on email address: {}".format(email_address))
                    breaches = None
                    retry = False
                # Rate limit was hit, wait 2 seconds and try again
                elif breaches_response.status_code == 429:
                    time.sleep(2)
                else:
                    log.warn("Have I Been Pwned returned unexpected status code")
                    retry = False
                    yield FunctionError("Have I Been Pwned returned unexpected status code")

                end = time.time()
                results = {
                    "Run Time": str(end - start),
                    "Inputs": kwargs,
                    "Breaches": breaches
                }

                yield StatusMessage("done...")
                # Produce a FunctionResult with the results
                yield FunctionResult(results)
            except Exception as e:
                yield FunctionError(e)
