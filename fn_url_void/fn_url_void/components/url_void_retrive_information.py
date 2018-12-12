# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_url_void.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'url_void_retrive_information"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_url_void", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_url_void", {})

    @function("url_void_retrive_information")
    def _url_void_retrive_information_function(self, event, *args, **kwargs):
        """Function: Retrieves information of a URL from the  URL Void database."""
        try:
            yield StatusMessage("starting...")
            start_time = time.time()

            api_key = self.options.get("api_key")
            identifier = self.options.get("identifier", "api1000")

            # Get the function parameters:
            artifact_value = kwargs.get("artifact_value")  # text
            if artifact_value is None:
                raise ValueError("artifact_value is required to run this function.")

            log = logging.getLogger(__name__)
            log.info("artifact_value: %s", artifact_value)

            artifact_value = artifact_value.replace("https://", "")
            res = requests.get("https://api.urlvoid.com/{}/{}/host/{}".format(identifier, api_key, artifact_value))

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()