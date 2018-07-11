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
        if self.apikey is None:
            raise Exception("No API key found - please add urlscanio_api_key under a [urlscanio] in app.config")

    @function("urlscanio")
    def _urlscanio_function(self, event, *args, **kwargs):
        """Function: """
        try:

            log = logging.getLogger(__name__)

            # Get the function parameters:
            urlscanio_url = kwargs.get("urlscanio_url")        # text
            incident_id = kwargs.get("urlscanio_incident_id")  # number

            log.info("urlscanio_url: %s", urlscanio_url)
            log.info("incident_id: %s", incident_id)

            # Setup headers and json data array to submit url from function - it may work with IP address and DNS Name too - I should probably validate that.
            urlscanio_headers = {'Content-Type': 'application/json', 'API-Key': self.apikey}
            urlscanio_data = '{"url": "%s"}' % urlscanio_url

            urlscanio_post = requests.post('https://urlscan.io/api/v1/scan/', headers=urlscanio_headers, data=urlscanio_data)

            # The JSON never seems to be properly formatted on the response so I need to load into json from text
            urlscanio_post_json = json.loads(urlscanio_post.text)

            # UUID tells me my report ID so I can go grab it after
            uuid = urlscanio_post_json['uuid']

            yield StatusMessage("Submitted URL Successfully as %s" % uuid)

            # Loop to check whether the report is ready - weirdly they respond with 404 so potentially here for issues if the site itself is is 404/down.
            urlscan_status = False
            while urlscan_status is False:
                try:
                    urlscanio_get = requests.get('https://urlscan.io/api/v1/result/{}/'.format(uuid))
                    if urlscanio_get.status_code == 404:
                        yield StatusMessage("Report is not ready yet... looping")
                        time.sleep(5)
                    elif urlscanio_get.status_code == 200:
                        yield StatusMessage("Report is ready")
                        urlscanio_status = True
                        break
                except requests.ConnectionError:
                    yield StatusMessage("Failed to Connect to URLScan")

            yield StatusMessage("Starting report download")

            # get the full report json - this is usually a big blob and we don't really use it, anything could be parsed out of it.
            urlscanio_report_get = requests.get('https://urlscan.io/api/v1/result/{}/'.format(uuid))
            urlscanio_report_json = json.loads(urlscanio_report_get.text)

            yield StatusMessage("Downloaded report from %s " % urlscanio_report_json['task']['reportURL'])

            yield StatusMessage("Getting PNG Screenshot")

            # Grab the PNG screenshot from url and return as a base64 encoding so it can be passed to another function as needed
            urlscanio_png_get = requests.get('https://urlscan.io/screenshots/{}.png'.format(uuid))
            urlscanio_png_b64 = base64.b64encode(urlscanio_png_get.content)

            yield StatusMessage("Downloaded PNG Screenshot")

            # returns the png file base64 and also the report url
            results = {
                "png_file": urlscanio_png_b64,
                "urlscanio_report_url": urlscanio_report_json['task']['reportURL']
            }

            yield FunctionResult(results)
        except:
            yield FunctionError()
