# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import base64
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_gcp.util.helper import GCPHelper

try: # Python 3 import
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib import urlopen

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'gcp_utilities_screenshot_sandboxed_webpage"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_gcp", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_gcp", {})

    @function("gcp_utilities_screenshot_sandboxed_webpage")
    def _gcp_utilities_screenshot_sandboxed_webpage_function(self, event, *args, **kwargs):
        """Function: Takes in an input of a URL and returns a screenshot of the UI for that webpage. Utilises Cloud Functions provided by Google Cloud Platform to set up an isolated headless Chrome instance to sandbox the webpage. Function triggers this Cloud Function with the URL and then returns the result."""
        try:
            yield StatusMessage("Starting")
            helper = GCPHelper(self.options)
            # Get GCP params
            HTTPS_PROXY, HTTP_PROXY,GCP_REGION,GCP_PROJECT_ID,GCP_FUNCTION_NAME = helper.setup_config()
            yield StatusMessage("Gathered config")
            # Get the function parameters:
            gcp_url = kwargs.get("gcp_url")  # text

            log = logging.getLogger(__name__)
            log.info("gcp_url: %s", gcp_url)

            if gcp_url is None:
                raise FunctionError("GCP_URL evaluates to NoneType. GCP_URL must be provided to run this function.")

            # Setup proxies parameter if exist in appconfig file
            proxies = {}

            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                base64Screenshot = None
                # Create the session and set the proxies.

                with requests.Session() as session:
                    session.proxies = proxies
                    # Prepare a user-agent and accept header instead of using requests user-agent
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        }
                    # Prepare request string
                    request_string = 'https://{}-{}.cloudfunctions.net/{}?url={}'.format(GCP_REGION,GCP_PROJECT_ID, GCP_FUNCTION_NAME, gcp_url)

                    yield StatusMessage("Sending request to Cloud Function : {}".format(request_string))
                    # Make the HTTP request through the session.
                    res = session.get(request_string, headers=headers, stream=True)

                    # Is the status code in the 2XX family?
                    if int(res.status_code / 100) == 2:
                        yield StatusMessage("Got a response back in the 200 family, parsing result")
                        # Read the stream for image data
                        base64Screenshot = base64.b64encode(res.raw.read())
                        
                    elif res.status_code == 401:
                        raise FunctionError("401 Status code returned. Retry function with updated credentials")
                    elif res.status_code == 403:
                        raise FunctionError("403 Forbidden response received by API")

                    else:
                        log.error(res.text)
                        log.error(res.reason)
                        yield StatusMessage("Request made. Status Code: {}; Reason {}".format(res.status_code, res.reason))

            except Exception as e:
                log.info(str(e))
                raise ValueError("Encountered issue when invoking the Google Cloud Function; Reason {}".format(str(e)))

            # Parse the input URL to get only the host. Full URL gives issues with Attachment names
            input_url = urlparse(gcp_url)

            results = {
                "input_url": input_url.hostname,
                "success": True if base64Screenshot else False,
                "base64Screenshot" : base64Screenshot
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()