# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


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
        try:
            payload = ResultPayload("task_utils_update_task", **kwargs)

            # Get the function parameters:
            task_id = kwargs.get("task_id")  # number
            task_utils_payload = self.get_textarea_param(kwargs.get("task_utils_payload"))  # textarea

            log = logging.getLogger(__name__)
            log.info(kwargs.get("task_utils_payload"))

            log.info("task_id: %s", task_id)
            log.info("task_utils_payload: %s", task_utils_payload)

            try:
                json.loads(task_utils_payload)
            except Exception as json_exception:
                err_msg = "Could not load task_utils_payload as JSON. Error: {}", json_exception
                log.error(err_msg)
                raise FunctionError(err_msg)

            res_client = self.rest_client()

            log.info("Sending new task info to res")
            updated_task = {}

            def update_task(task):
                task.update(json.loads(task_utils_payload))
                updated_task.update(task)

            task_url = "/tasks/{}".format(task_id)
            try:
                res_client.get_put(task_url, lambda task: update_task(task))
            except Exception as update_exception:
                err_msg = "Encountered exception while trying to update task. Error: {}", update_exception
                log.error(err_msg)
                raise FunctionError(err_msg)

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