# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_task_utils.lib.task_common import find_task_by_name, get_function_input


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'task_utils_update_task"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_task_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_task_utils", {})

    @function("task_utils_update_task")
    def _task_utils_update_task_function(self, event, *args, **kwargs):
        """Function: A function which takes in the ID of an existing Task and a task_utils_payload which is a JSON String of the task details to update."""

        def update_task(task):
            """
            A inner function which is used as a lambda
            The return value of this lambda is then sent to Resilient as a PUT.

            In this case we also update an outer scope variable called updated_task
             with the value of the newly modified task object before returning it
            :param task:
            :return:
            """
            task.update(json.loads(task_utils_payload))
            updated_task.update(task)
            return task

        try:
            payload = ResultPayload("task_utils_update_task", **kwargs)

            # Get the function parameters:
            incident_id = get_function_input(kwargs, "incident_id")  # number
            task_id = get_function_input(kwargs, "task_id", optional=True)  # number
            task_name = get_function_input(kwargs, "task_name", optional=True)  # text
            task_utils_payload = self.get_textarea_param(kwargs.get("task_utils_payload"))  # textarea

            if not task_name and not task_id:
                raise ValueError("Either a Task ID or a Task Name to search for must be provided.")

            log = logging.getLogger(__name__)
            log.info(kwargs.get("task_utils_payload"))

            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("task_name: %s", task_name)
            log.info("task_utils_payload: %s", task_utils_payload)

            try:
                json.loads(task_utils_payload)
            except Exception as json_exception:
                err_msg = "Could not load task_utils_payload as JSON. Error: {}", json_exception
                log.error(err_msg)
                raise TypeError(err_msg)

            res_client = self.rest_client()

            # If task name was provided try to find its ID
            if task_name:
                yield StatusMessage("task_name was provided; Searching incident {} for first matching task with name '{}'".format(incident_id, task_name))
                task_id = find_task_by_name(res_client, incident_id, task_name)

                if not task_id:
                    raise ValueError("task_name not found: %s", task_name)

            log.info("Sending new task info to res")
            updated_task = {}

            task_url = "/tasks/{}".format(task_id)
            try:
                res_client.get_put(task_url, lambda task: update_task(task))
            except Exception as update_exception:
                err_msg = "Encountered exception while trying to update task. Error: {}", update_exception
                raise ValueError(err_msg)

            yield StatusMessage("Task {} has been updated".format(task_id))

            results = payload.done(
                success=True,
                content={
                    "task_id": task_id,
                    "task": updated_task
                }
            )
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
