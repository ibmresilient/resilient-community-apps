# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib.components.resilient_common import validate_fields
from fn_isitPhishing.lib.isitphishing_util import get_license_key
import fn_isitPhishing.util.selftest as selftest


CONFIG_DATA_SECTION = 'fn_isitPhishing'
API_URL = 'https://ws.isitphishing.org/api/v2/url'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init_isitPhishing()

    def _init_isitPhishing(self):
        """ validate required fields for app.config """
        validate_fields(('isitphishing_name', 'isitphishing_license'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init_isitPhishing()

    @function("isitphishing_url")
    def _isitphishing_url_function(self, event, *args, **kwargs):
        """Function: Analyze a URL, a list of URLs or a document using the Vade Secure IsItPhishing Webservice API."""
        try:
            # Get the function parameters:
            isitphishing_url = kwargs.get("isitphishing_url")  # text

            log = logging.getLogger(__name__)
            log.info("isitphishing_url: %s", isitphishing_url)

            # Get the license key to access the API endpoint.
            auth_token = get_license_key(self.isitPhishing_name, self.isitPhishing_license)

            # Build the header and the data payload.
            headers = {
                "Authorization": u'Bearer {}'.format(auth_token),
                "Content-type": "application/json",
            }

            payload = {"url": isitphishing_url, "force": False, "smart": True, "timeout": 8000}

            yield StatusMessage("Query isitPhishing.org endpoint.")

            # Make URL request
            response = requests.post(API_URL, headers=headers, json=payload)

            # Check the results
            if response.status_code == 200:
                results_analysis = json.loads(response.content)
            else:
                msg = "An error occurred while retrieving the information from isitPhishing with status code: {}"
                raise ValueError(msg.format(response.status_code))

            yield StatusMessage("Send the results back: {0}.".format(results_analysis["status"]))

            # Send back the results and the input parameter.
            results = {
                "content": results_analysis,
                "inputs": {"URL": isitphishing_url}
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
