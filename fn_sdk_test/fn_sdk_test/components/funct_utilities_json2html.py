# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_json2html''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_json2html")
    def _utilities_json2html_function(self, event, *args, **kwargs):
        """Function: Produces an HTML representation of JSON data. All data is converted into tables of key / value pairs or lists.

Provide an optional parameter `json2html_keys` to limit the JSON data to display."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_json2html' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            json2html_data = kwargs.get("json2html_data")  # text
            json2html_keys = kwargs.get("json2html_keys")  # text

            log = logging.getLogger(__name__)
            log.info("json2html_data: %s", json2html_data)
            log.info("json2html_keys: %s", json2html_keys)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_json2html' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
