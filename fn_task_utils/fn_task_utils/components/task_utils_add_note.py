# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_task_utils.lib.task_common import find_task_by_name, get_function_input


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'task_utils_add_note"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_task_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_task_utils", {})

    @function("task_utils_add_note")
    def _task_utils_add_note_function(self, event, *args, **kwargs):
        """Function: A function which takes in the ID of an existing Task and then adds either a plain or richtext note to the Task."""
        try:
            payload = ResultPayload("task_utils_add_note", **kwargs)
            # Get the function parameters:
            incident_id = get_function_input(kwargs, "incident_id")  # number
            task_id = get_function_input(kwargs, "task_id", optional=True)  # number
            task_name = get_function_input(kwargs, "task_name", optional=True)  # text
            task_utils_note_type = self.get_select_param(kwargs.get("task_utils_note_type"))  # select, values: "text", "html"
            task_utils_note_body = get_function_input(kwargs, "task_utils_note_body", optional=True)  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("task_name: %s", task_name)
            log.info("task_utils_note_type: %s", task_utils_note_type)
            log.info("task_utils_note_body: %s", task_utils_note_body)

            if not task_name and not task_id:
                raise ValueError("Either a Task ID or a Task Name to search for must be provided.")

            task_note_json = {
                "text": {
                    "format": task_utils_note_type,
                    "content": task_utils_note_body
                }
            }

            res_client = self.rest_client()

            if task_name:
                yield StatusMessage("task_name was provided; Searching incident {} for first matching task with name '{}'".format(incident_id, task_name))

                task_id = find_task_by_name(res_client, incident_id, task_name)

                if not task_id:
                    raise ValueError(u"Could not find task with name {}".format(task_name))

            yield StatusMessage("Posting note to API")
            try:
                task_response = res_client.post('/tasks/{}/comments'.format(task_id), task_note_json)
            except Exception as add_note_exception:
                err_msg = "Encountered exception while trying to add note to task. Error: %s", add_note_exception
                raise ValueError(err_msg)

            yield StatusMessage("Completed API call")

            results = payload.done(
                success=True,
                content={
                    "task_note": task_response
                }
            )

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
