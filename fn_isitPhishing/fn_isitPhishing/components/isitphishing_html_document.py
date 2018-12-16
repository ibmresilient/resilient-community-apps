# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
import json
import base64
import requests
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib.components.resilient_common import get_file_attachment, validate_fields
from fn_isitPhishing.lib.isitphishing_util import get_license_key
import fn_isitPhishing.util.selftest as selftest

CONFIG_DATA_SECTION = 'fn_isitPhishing'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing_html_document"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init_isitPhishing()
        selftest.selftest_function(opts)

    def _init_isitPhishing(self):
        """ validate required fields for app.config """
        validate_fields(('isitphishing_api_url', 'isitphishing_name', 'isitphishing_license'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init_isitPhishing()

    @function("isitphishing_html_document")
    def _isitphishing_html_document_function(self, event, *args, **kwargs):
        """Function: isitphishing_html_document
        This function takes an incident id as a required parameter and
        task_id, attachment_id, and artifact_id as optional input which
        specifies an HTML document to be base64 encoded and sent to the
        Vade Secure API endpoint:
        https://ws.isitphishing.org/api/v2/document
        for analysis to detemine if the document contains phishing.
        The "results" dictionary contains the result of the API query in
        "contents" and the "inputs" parameters to the function.
        """
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("artifact_id: %s", artifact_id)

            # Form the URL for API request.
            API_URL = u"{0}/document".format(self.options["isitphishing_api_url"])

            # Get the license key to access the API endpoint.
            auth_token = get_license_key(self.options["isitphishing_name"], self.options["isitphishing_license"])

            # Build the header and the data payload.
            headers = {
                "Authorization": u'Bearer {}'.format(auth_token),
                "Content-type": "application/json",
                "Accept": "application/json"
            }

            # Build the document payload which is a base64-encoded string.
            client = self.rest_client()

            # Get the attachment data
            data = get_file_attachment(client, incident_id, artifact_id, task_id, attachment_id)

            # Base64 encode the document string and build payload.
            base64encoded_doc = base64.b64encode(data).decode("ascii")
            payload = {"document": base64encoded_doc}

            yield StatusMessage("Query isitPhishing endpoint for status of document.")

            # Make API URL request
            response = requests.post(API_URL, headers=headers, json=payload)

            # Check the results
            if response.status_code == 200:
                results_analysis = json.loads(response.content)
            else:
                msg = "An error occurred while retrieving the information from isitPhishing with status code: {}"
                raise ValueError(msg.format(response.status_code))

            yield StatusMessage("Send the results back: {0}.".format(results_analysis["result"]))

            # Send back the results and the input parameter.
            results = {
                "content": results_analysis,
                "inputs": {"incident_id": incident_id,
                           "task_id": task_id,
                           "attachment_id": attachment_id,
                           "artifact_id": artifact_id}
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError()

