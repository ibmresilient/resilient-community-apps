# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields
from fn_service_now.util.resilient_helper import CONFIG_DATA_SECTION, ResilientHelper

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'fn_snow_helper_add_task_note"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_snow_helper_add_task_note")
    def _fn_snow_helper_add_task_note_function(self, event, *args, **kwargs):
        """Function: A helper function to add a Note to a Task from a Workflow with a different parent object type"""

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["sn_res_id", "sn_note_text"], kwargs)

        # Get the function inputs:
        inputs = {
            # text (required)
            "sn_res_id": kwargs.get("sn_res_id"),
            # number (required)
            "sn_note_text": kwargs.get("sn_note_text")
        }

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        # Instantiate new SOAR API object
        res_client = self.rest_client()

        # Parse incident_id and task_id from sn_res_id
        ids = res_helper.parse_res_id(payload.inputs["sn_res_id"])

        # Create data for POST
        request_data = {
            "text": {
                "format": "html",
                "content": payload.inputs["sn_note_text"]
            }
        }

        yield StatusMessage(f"Adding Task Note to {payload.inputs['sn_res_id']}")

        # POST to SOAR API, add the Note
        task_id = ids.get("task_id")
        res_client.post(
            f"/tasks/{task_id}/comments", request_data)

        # Set results
        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
