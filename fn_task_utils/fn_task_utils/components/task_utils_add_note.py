# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, str_to_bool
from fn_task_utils.lib.task_common import find_task_by_name, get_function_input, user_info_to_note


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'task_utils_add_note"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)
        self.options = opts.get("fn_task_utils", {})
        self.add_user_info_to_note = str_to_bool(self.options.get("add_user_info_to_note", "false"))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_task_utils", {})
        self.add_user_info_to_note = str_to_bool(self.options.get("add_user_info_to_note", "false"))

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

            content = task_utils_note_body
            if self.add_user_info_to_note:
                user_info = user_info_to_note(event.message)
                if task_utils_note_type == "html":
                    content = f"<p><strong>{user_info['name']} ({user_info['email']})</strong> added a note:</p> <p>{task_utils_note_body}</p>"
                else:
                    content = f"{user_info['name']} ({user_info['email']}) added a note:\n{task_utils_note_body}"
            task_note_json = {
                "text": {
                    "format": task_utils_note_type,
                    "content": content
                }
            }

            res_client = self.rest_client()

            if task_name:
                yield StatusMessage(f"task_name was provided; Searching incident {incident_id} for first matching task with name '{task_name}'")

                task_id = find_task_by_name(res_client, incident_id, task_name)

                if not task_id:
                    raise ValueError(f"Could not find task with name {task_name}")

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
