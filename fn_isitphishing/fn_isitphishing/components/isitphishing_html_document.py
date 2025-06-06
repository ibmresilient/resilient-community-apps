# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

"""Function implementation"""

import base64
import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import get_file_attachment, get_file_attachment_name, validate_fields, RequestsCommon, ResultPayload
from fn_isitphishing.lib.isitphishing_helper import IsItPhishingHelper

PACKAGE_NAME = 'fn_isitphishing'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'isitphishing_html_document"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(PACKAGE_NAME, {})
        self._init_isitphishing()

    def _init_isitphishing(self):
        """ validate required fields for app.config """
        validate_fields(('isitphishing_api_url', 'isitphishing_id', 'isitphishing_secret'),
                        self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        self._init_isitphishing()

    @function("isitphishing_html_document")
    def _isitphishing_html_document_function(self, event, *args, **kwargs):
        """Function: isitphishing_html_document

        This function takes an incident id as a required parameter and
        task_id, attachment_id, and artifact_id as optional input which
        specifies an HTML document to be base64 encoded and sent to the

        The "results" dictionary contains the result of the API query in
        "contents" and the "inputs" parameters to the function.
        """
        try:
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

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

            client_id = self.options.get("isitphishing_id")
            client_secret = self.options.get("isitphishing_secret")
            api_endpoint_url = self.options.get("isitphishing_api_url")
            auth_url = self.options.get("authentication_url")

            # Form the URL for API request.
            api_url = f"{api_endpoint_url}/document"

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
                "Accept": "application/json"
            }

            # Build the document payload which is a base64-encoded string.
            client = self.rest_client()

            # Get the attachment data
            data = get_file_attachment(client, incident_id, artifact_id, task_id, attachment_id)
            filename = get_file_attachment_name(client, incident_id, artifact_id, task_id, attachment_id)

            # Base64 encode the document string and build payload.
            base64encoded_doc = base64.b64encode(data).decode("ascii")
            payload = {"document": base64encoded_doc}

            yield StatusMessage("Query IsItPhishing endpoint for status of document.")

            # Make API URL request
            rc = RequestsCommon(self.opts, self.options)
            response = rc.execute_call_v2("post", api_url, json=payload, headers=headers, proxies=rc.get_proxies())
            if response.status_code == 200:
                success = True
            else:
                success = False

            response_json = response.json()
            results = rp.done(success, response_json)

            # add back in the filename
            results["inputs"]["filename"] = filename

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except requests.exceptions.RequestException as err:
            yield FunctionError(err)
