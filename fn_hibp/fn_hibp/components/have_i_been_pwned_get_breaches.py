# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import time
from fn_hibp.lib.common import HAVE_I_BEEN_PWNED_BREACH_URL, Hibp
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, IntegrationError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'have_i_been_pwned_get_breaches"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_hibp", {})
        self.hibp = Hibp(self.options)

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

            breach_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, email_address)
            try:
                breach_results = self.hibp.execute_call(breach_url)
            except IntegrationError as err:
                yield FunctionError(err)

            results = {
                "Breaches": breach_results
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            yield FunctionError(e)
