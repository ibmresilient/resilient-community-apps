# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Function for urlscan.io"""

import base64
import logging
import json
import time
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import write_file_attachment
from resilient_lib.components.integration_errors import IntegrationError
from io import BytesIO
from resilient_lib import RequestsCommon

CONFIG_DATA_SECTION = 'urlscanio'


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self.apikey = self.options.get("urlscanio_api_key")
        self.urlscanio_report_url = self.options.get("urlscanio_report_url")
        self.urlscanio_screenshot_url = self.options.get("urlscanio_screenshot_url")
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
            incident_id = kwargs.get("incident_id")                  # number, optional

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

            req_common = RequestsCommon(self.options, self.opts)

            urlscanio_scan_url = u"{}/scan/".format(self.urlscanio_report_url)
            urlscanio_post = req_common.execute_call_v2("POST", urlscanio_scan_url, self.timeout,
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
                urlscanio_result_url = u"{}/result/{}".format(self.urlscanio_report_url, uuid)
                try:
                    urlscanio_get = req_common.execute_call_v2("GET", urlscanio_result_url, self.timeout)
                    if urlscanio_get.status_code == 200:
                        # Report is done
                        break
                    else:
                        # Some other error condition
                        urlscanio_get.raise_for_status()
                    # requests-common will through an IntegrationError if 404 is received
                except IntegrationError as ie:
                    # 404 means the report is not yet complete
                    if ie.value[:3] == '404':
                        yield StatusMessage("Waiting for report...")
                    else:
                        # Some problem other than 404
                        raise IntegrationError

            yield StatusMessage("Report is ready")

            # get the full report json - usually a big blob
            urlscanio_report_url = u"{}/result/{}/".format(self.urlscanio_report_url, uuid)
            urlscanio_report_get = req_common.execute_call_v2("GET", urlscanio_report_url, self.timeout)
            urlscanio_report_json = urlscanio_report_get.json()
            yield StatusMessage("Downloaded report from {}".format(urlscanio_report_url))

            # Grab the PNG screenshot.  Return as a base64 string so it can be passed to another function as needed
            urlscanio_png_url = u"{}/{}.png".format(self.urlscanio_screenshot_url, uuid)
            urlscanio_png_get = req_common.execute_call_v2("GET", urlscanio_png_url, self.timeout)
            urlscanio_png_b64 = base64.b64encode(urlscanio_png_get.content)
            yield StatusMessage("Downloaded PNG screenshot from {}".format(urlscanio_png_url))

            # returns the png file base64 and also the report url
            results = {
                "png_base64content": str(urlscanio_png_b64),
                "png_url": urlscanio_png_url,
                "report_url": urlscanio_report_url,
                "report": urlscanio_report_json
            }

            # Get rest client, attachment name, and png content so we can write as an attachment
            rest_client = self.rest_client()
            attachment_name = u"urlscanio-screenshot-{}.png".format(urlscanio_url)
            datastream = BytesIO(urlscanio_png_get.content)

            # Write the file as an attachment
            write_file_attachment(rest_client, attachment_name, datastream, incident_id, None)

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
