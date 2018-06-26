# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_extract_ssl_cert_from_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("utilities_extract_ssl_cert", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("utilities_extract_ssl_cert", {})

    @function("utilities_extract_ssl_cert_from_url")
    def _utilities_extract_ssl_cert_from_url_function(self, event, *args, **kwargs):
        """Function: This function takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.
Inputs: A HTTPS_URL.
Outputs: Certificate file encoded in JSON."""
        try:
            # Get the function parameters:
            https_url = kwargs.get("https_url")  # text

            log = logging.getLogger(__name__)
            log.info("https_url: %s", https_url)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()