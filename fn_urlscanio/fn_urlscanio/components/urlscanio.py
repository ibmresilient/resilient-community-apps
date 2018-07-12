# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Function for urlscan.io"""

import base64
import logging
import json
import requests
import time
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

CONFIG_DATA_SECTION = 'urlscanio'


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self.apikey = self.options.get("urlscanio_api_key")
        self.timeout = int(self.options.get("timeout", 600))
        if self.apikey is None:
            raise Exception("No API key found - please add urlscanio_api_key under a [urlscanio] in app.config")

    @function("urlscanio")
    def _urlscanio_function(self, event, *args, **kwargs):
        """Function: urlscanio"""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            urlscanio_url = kwargs.get("urlscanio_url")              # text
            urlscanio_public = kwargs.get("urlscanio_public")        # boolean, optional
            urlscanio_useragent = kwargs.get("urlscanio_useragent")  # text, optional
            urlscanio_referer = kwargs.get("urlscanio_referer")      # text, optional

            log.info("urlscanio_url: %s", urlscanio_url)

            # Construct the parameters to send to urlscan.io
            urlscanio_headers = {'Content-Type': 'application/json', 'API-Key': self.apikey}
            urlscanio_data = {
                "url": urlscanio_url
            }

            if urlscanio_public:
                urlscanio_data["public"] = "on"

            if urlscanio_useragent:
                urlscanio_data["customagent"] = urlscanio_useragent

            if urlscanio_referer:
                urlscanio_data["referer"] = urlscanio_referer

            urlscanio_post = requests.post('https://urlscan.io/api/v1/scan/',
                                           headers=urlscanio_headers,
                                           data=json.dumps(urlscanio_data))
            urlscanio_post.raise_for_status()

            # The post response contains a UUID that we use to check for the report
            urlscanio_post_json = urlscanio_post.json()
            log.debug(urlscanio_post_json)

            # UUID tells me my report ID so I can go grab it after
            uuid = urlscanio_post_json['uuid']
            yield StatusMessage("Submitted URL successfully as %s" % uuid)

            # Loop until the report is ready
            start_time = time.time()  # epoch seconds
            while True:
                time.sleep(10)
                if time.time() > start_time + self.timeout:
                    yield RuntimeError("Timeout: report was not ready after {} seconds".format(self.timeout))
                urlscanio_get = requests.get('https://urlscan.io/api/v1/result/{}/'.format(uuid))
                if urlscanio_get.status_code == 404:
                    # 404 means the report is not yet complete
                    yield StatusMessage("Waiting for report...")
                elif urlscanio_get.status_code == 200:
                    # Report is done
                    break
                else:
                    # Some other error condition
                    urlscanio_get.raise_for_status()

            yield StatusMessage("Report is ready")

            # get the full report json - usually a big blob
            urlscanio_report_url = 'https://urlscan.io/api/v1/result/{}/'.format(uuid)
            urlscanio_report_get = requests.get(urlscanio_report_url)
            urlscanio_report_json = urlscanio_report_get.json()
            yield StatusMessage("Downloaded report from {}".format(urlscanio_report_url))

            # Grab the PNG screenshot.  Return as a base64 string so it can be passed to another function as needed
            urlscanio_png_url = 'https://urlscan.io/screenshots/{}.png'.format(uuid)
            urlscanio_png_get = requests.get(urlscanio_png_url)
            urlscanio_png_b64 = base64.b64encode(urlscanio_png_get.content)
            yield StatusMessage("Downloaded PNG screenshot from {}".format(urlscanio_png_url))

            # returns the png file base64 and also the report url
            results = {
                "png_base64content": urlscanio_png_b64,
                "png_url": urlscanio_png_url,
                "report_url": urlscanio_report_url,
                "report": urlscanio_report_json
            }

            yield FunctionResult(results)
        except:
            yield FunctionError()
