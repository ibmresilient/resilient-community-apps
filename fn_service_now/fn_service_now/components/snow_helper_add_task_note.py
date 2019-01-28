# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'snow_helper_add_task_note"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("snow_helper_add_task_note")
    def _snow_helper_add_task_note_function(self, event, *args, **kwargs):
        """Function: A helper function to add a Note to a Task from a Workflow with a different parent object type"""

        log = logging.getLogger(__name__)

        try:

            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "sn_res_id": res_helper.get_function_input(kwargs, "sn_res_id"),  # text (required)
                "sn_note_text": res_helper.get_function_input(kwargs, "sn_note_text")  # number (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Parse incident_id and task_id from sn_res_id
            ids = res_helper.parse_res_id(payload.inputs["sn_res_id"])

            # url for POST
            url = "/tasks/{0}/comments".format(ids.get("task_id"))

            yield StatusMessage("Creating Note Request")

            # Create data for POST
            request_data = {
                "text": {
                    "format": "html",
                    "content": payload.inputs["sn_note_text"]
                }
            }

            yield StatusMessage("Adding Note to {0}".format(payload.inputs["sn_res_id"]))

            # POST to Resilient API, add the Note
            res_client.post(url, request_data)

            # Set results
            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
