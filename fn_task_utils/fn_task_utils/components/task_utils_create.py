# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_task_utils.lib.task_common import get_function_input


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'task_utils_create"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_task_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_task_utils", {})

    @function("task_utils_create")
    def _task_utils_create_function(self, event, *args, **kwargs):
        """Function: A function which can be used to create a custom task using the REST API."""
        try:
            payload = ResultPayload("task_utils_create", **kwargs)
            # Get the function parameters:
            incident_id = get_function_input(kwargs, "incident_id")  # number
            task_name = get_function_input(kwargs, "task_name", optional=True)  # text
            task_utils_payload = self.get_textarea_param(kwargs.get("task_utils_payload"))  # textarea

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_name: %s", task_name)
            log.info("task_utils_payload: %s", task_utils_payload)

            try:
                task_utils_payload = json.loads(task_utils_payload)
            except Exception as json_exception:
                err_msg = "Could not load task_utils_payload as JSON. Error: {}", json_exception
                log.error(err_msg)
                raise TypeError(err_msg)
            else:
                log.debug("Successfully parsed task_utils_payload as valid JSON")

            resilient_client = self.rest_client()

            # Replace task_json["name"] if task_name is set and task_json["name"] is not set; otherwise use default name
            # If task_json["name"] is set, do nothing, use that
            task_utils_payload["name"] = task_name if not task_utils_payload.get("name", False) and task_name else "Default Task Name"

            log.debug("New task will be saved with name %s", task_utils_payload["name"])
            yield StatusMessage("Posting to API")
            try:
                task_response = resilient_client.post('/incidents/{}/tasks'.format(incident_id), task_utils_payload)
            except Exception as add_note_exception:
                err_msg = "Encountered exception while trying to create task. Error: {}", add_note_exception
                raise ValueError(err_msg)

            log.info("Response from Resilient %s", task_response)

            yield StatusMessage("Created task with ID: {}".format(task_response.get('id', 'No task ID found')))

            results = payload.done(
                success=True,
                content={
                    "task": task_response
                }
            )
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
