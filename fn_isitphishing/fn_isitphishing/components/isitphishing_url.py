# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_isitphishing.lib.isitphishing_util import get_license_key


PACKAGE_NAME = 'fn_isitphishing'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    def _init_isitphishing(self):
        """ validate required fields for app.config """
        validate_fields(('isitphishing_api_url', 'isitphishing_name', 'isitphishing_license'), self.options)

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

            # Form the URL for API request.
            API_URL = u"{0}/url".format(self.options["isitphishing_api_url"])

            # Get the license key to access the API endpoint.
            auth_token = get_license_key(self.options["isitphishing_name"], self.options["isitphishing_license"])

            # Build the header and the data payload.
            headers = {
                "Authorization": u'Bearer {}'.format(auth_token),
                "Content-type": "application/json",
            }

            payload = {"url": isitphishing_url, "force": False, "smart": True, "timeout": 8000}

            yield StatusMessage("Query IsItPhishing.org endpoint for status of URL {0}.".format(isitphishing_url))

            # Make URL request
            rc = RequestsCommon(self.opts, self.options)
            response = rc.execute_call_v2("post", API_URL, json=payload, headers=headers, proxies=rc.get_proxies())
            if response.status_code == 200:
                success = True
            else:
                success = False

            response_json = response.json()
            results = rp.done(success, response_json)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
