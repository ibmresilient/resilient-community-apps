# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_isitphishing.lib.isitphishing_helper import IsItPhishingHelper

PACKAGE_NAME = 'fn_isitphishing'

TIME_OUT = 60   # 60 seconds

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    def _init_isitphishing(self):
        """ validate required fields for app.config """
        validate_fields(('isitphishing_api_url', 'isitphishing_id', 'isitphishing_secret'),
                        self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self._init_isitphishing()

    @function("isitphishing_url")
    def _isitphishing_url_function(self, event, *args, **kwargs):
        """Function: isitphishing_url
        This function takes URL string as a required parameter.  It
        queries the Vade Secure isiphishing API to analyze the
        URL to determine if it is PHISHING or SPAM.
        The results contain the result of the query in 'contents' and the
        URL input parameter to the function.
        """
        try:
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            isitphishing_url = kwargs.get("isitphishing_url")  # text

            log = logging.getLogger(__name__)
            log.info("isitphishing_url: %s", isitphishing_url)

            client_id = self.options.get("isitphishing_id")
            client_secret = self.options.get("isitphishing_secret")
            api_endpoint_url = self.options.get("isitphishing_api_url")
            auth_url = self.options.get("authentication_url")

            # Form the URL for API request.
            api_url = f"{api_endpoint_url}/url"

            # Create IsItPhishingHelper class object
            isitphishing_helper = IsItPhishingHelper(api_url, auth_url, client_id, client_secret)

            # Get a session token
            session_token = isitphishing_helper.authenticate(client_id, client_secret)

            if isitphishing_helper and session_token:
                log.info("Successfully authenticated with IsItPhishing.org")

            # Get the license key to access the API endpoint.
            auth_token = session_token

            # Build the header and the data payload.
            headers = {
                "Authorization": f"Bearer {auth_token}",
                "Content-type": "application/json",
            }

            payload = {"url": isitphishing_url, "force": False, "smart": True, "timeout": TIME_OUT}

            yield StatusMessage(f"Query IsItPhishing.org endpoint for status of URL {isitphishing_url}.")

            # Make URL request
            rc = RequestsCommon(self.opts, self.options)
            response = rc.execute_call_v2("post", api_url, json=payload, headers=headers, proxies=rc.get_proxies())
            if response.status_code == 200:
                success = True
            else:
                success = False

            response_json = response.json()
            results = rp.done(success, response_json)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except requests.exceptions.RequestException as err:
            yield FunctionError(err)
