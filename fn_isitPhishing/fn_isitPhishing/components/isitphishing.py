# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
import logging
import json
import base64
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_isitPhishing.util.selftest as selftest


CONFIG_DATA_SECTION = 'fn_isitPhishing'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            raise ValueError("{} section is not set in the config file".format(CONFIG_DATA_SECTION))

        self.isitPhishing_name = self.options.get("isitphishing_name")
        self.isitPhishing_license = self.options.get("isitphishing_license")
        self.isitPhishing_api_url = self.options.get("isitphishing_api_url")

        # Check that config parameters are defined.
        if not self.isitPhishing_name:
            raise ValueError("isitPhishing_name is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.isitPhishing_license:
            raise ValueError("isitPhishing_license is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.isitPhishing_api_url:
            raise ValueError("isitPhishing_api_url is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))

        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_isitPhishing", {})

    @function("isitphishing")
    def _isitphishing_function(self, event, *args, **kwargs):
        """Function: Analyze a URL, a list of URLs or a document using the Vade Secure IsItPhishing Webservice API."""
        try:
            # Get the function parameters:
            isitphishing_url = kwargs.get("isitphishing_url")  # text

            log = logging.getLogger(__name__)
            log.info("isitphishing_url: %s", isitphishing_url)

            yield StatusMessage("Setup the isitPhishing POST request.")

            # Compute the base64 license key. This key will be provided to you by Vade Secure,
            # and has the following format: <CUSTOMER_NAME>:<CUSTOMER_LICENSE>.
            url_key = u'{}:{}'.format(self.isitPhishing_name, self.isitPhishing_license)

            # It must be Base64-encoded. Handled different on Python 2 vs 3.
            if sys.version_info[0] == 2:
                auth_token = base64.b64encode(bytes(url_key).encode("utf-8"))
            else:
                auth_token = base64.b64encode(bytes(url_key, 'ascii')).decode('ascii')

            bearer_auth = u'Bearer {}'.format(auth_token)

            # Build the header and the data payload.
            headers = {
                "Authorization": bearer_auth,
                "Content-type": "application/json",
            }
            payload = {"url": isitphishing_url, "force": False, "smart": True, "timeout": 8000}

            yield StatusMessage("Query isitPhishing.org endpoint.")

            # Make URL request
            response = requests.post(self.isitPhishing_api_url, headers=headers, data=json.dumps(payload))

            # Check the results
            if response.status_code == 200:
                results_analysis = json.loads(response.content)
            else:
                msg = "An error occurred while retrieving the information from isitPhishing with status code: {}"
                raise ValueError(msg.format(response.status_code))

            yield StatusMessage("Send the results back.")

            # Send back the results and the input parameter.
            results = {
                "analysis": results_analysis,
                "inputs": {"URL": isitphishing_url}
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)