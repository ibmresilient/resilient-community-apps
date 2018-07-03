# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_parse_ssl_cert"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("utilities_parse_ssl_cert", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("utilities_parse_ssl_cert", {})

    @function("utilities_parse_ssl_cert")
    def _utilities_parse_ssl_cert_function(self, event, *args, **kwargs):
        """Function: Takes in an SSL Certificate.
Attempts to parse information from this certificate and save it as a note"""
        try:
            # Get the function parameters:
            certificate = kwargs.get("certificate")  # text

            log = logging.getLogger(__name__)
            log.info("certificate: %s", certificate)

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