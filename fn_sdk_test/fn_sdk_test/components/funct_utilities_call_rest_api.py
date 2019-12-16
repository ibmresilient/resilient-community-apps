# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_call_rest_api''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_call_rest_api")
    def _utilities_call_rest_api_function(self, event, *args, **kwargs):
        """Function: This function calls a REST web service. It supports the standard REST methods: GET, HEAD, POST, PUT, DELETE and OPTIONS.

The function parameters determine the type of call, the URL, and optionally the headers and body. The results include the text or structured (JSON) result from the web service, and additional information including the elapsed time."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_call_rest_api' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            rest_body = self.get_textarea_param(kwargs.get("rest_body"))  # textarea
            rest_verify = kwargs.get("rest_verify")  # boolean
            rest_method = self.get_select_param(kwargs.get("rest_method"))  # select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS"
            rest_headers = self.get_textarea_param(kwargs.get("rest_headers"))  # textarea
            rest_url = kwargs.get("rest_url")  # text
            rest_cookies = self.get_textarea_param(kwargs.get("rest_cookies"))  # textarea

            log = logging.getLogger(__name__)
            log.info("rest_body: %s", rest_body)
            log.info("rest_verify: %s", rest_verify)
            log.info("rest_method: %s", rest_method)
            log.info("rest_headers: %s", rest_headers)
            log.info("rest_url: %s", rest_url)
            log.info("rest_cookies: %s", rest_cookies)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_call_rest_api' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
