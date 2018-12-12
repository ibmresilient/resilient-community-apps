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
from resilient_lib.components.resilient_common import get_file_attachment
import fn_isitPhishing.util.selftest as selftest

CONFIG_DATA_SECTION = 'fn_isitPhishing'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing_html_document"""

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
            raise ValueError(
                "isitPhishing_name is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.isitPhishing_license:
            raise ValueError(
                "isitPhishing_license is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.isitPhishing_api_url:
            raise ValueError(
                "isitPhishing_api_url is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))

        selftest.selftest_function(opts)


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_isitPhishing", {})

    @function("isitphishing_html_document")
    def _isitphishing_html_document_function(self, event, *args, **kwargs):
        """Function: """
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


            yield StatusMessage("Setup the isitPhishing POST request.")

            # Compute the base64 license key. This key will be provided to you by Vade Secure,
            # and has the following format: <CUSTOMER_NAME>:<CUSTOMER_LICENSE>.
            url_key = u'{0}:{1}'.format(self.isitPhishing_name, self.isitPhishing_license)

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
                "Accept": "application/json"
            }

            # Build the document payload which sase64-encoded string.
            client = self.rest_client()

            # Get the attachment data
            data = get_file_attachment(client, incident_id, artifact_id, task_id, attachment_id)

            # Base64 encode the document string.
            base64encoded_doc = base64.b64encode(data).decode("ascii")

            payload = {"document": base64encoded_doc}
            payload_string = json.dumps(payload)
            yield StatusMessage("Query isitPhishing.org endpoint.")

            api_url = "{0}{1}".format(self.isitPhishing_api_url, "/document")

            # Make URL request
            response = requests.post(api_url, headers=headers, data=payload_string)

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
                "inputs": {"incident_id": incident_id,
                           "task_id": task_id,
                           "attachment_id": attachment_id,
                           "artifact_id": artifact_id}
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError()

