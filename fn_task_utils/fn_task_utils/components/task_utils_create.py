# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


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
            incident_id = kwargs.get("incident_id")  # number
            task_name = kwargs.get("task_name")  # text
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
                raise FunctionError(err_msg)
            else:
                log.debug("Successfully parsed task_utils_payload as valid JSON")

            yield StatusMessage("Setting up API Client")
            resilient_client = self.rest_client()

            # Replace task_json["name"] if task_name is set and task_json["name"] is not set; otherwise use default name
            # If task_json["name"] is set, do nothing, use that
            task_utils_payload["name"] = task_name if not task_utils_payload.get("name", False) and task_name else "Default Task Name"

            log.debug("New task will be saved with name %s", task_utils_payload["name"])
            yield StatusMessage("Posting to API")

            task_response = resilient_client.post('/incidents/{}/tasks'.format(incident_id), task_utils_payload)
            log.info("Response from Resilient %s", task_response)

            task_id = task_response.get('id', 'No task ID found')

            yield StatusMessage("Created task with ID: {}".format(task_id))

            results = payload.done(
                success=True,
                content={
                    "task_id": task_id,
                    "task": task_response
                }
            )
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()