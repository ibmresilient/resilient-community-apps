# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'task_utils_close_task"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_task_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_task_utils", {})

    @function("task_utils_close_task")
    def _task_utils_close_task_function(self, event, *args, **kwargs):
        """Function: A function which will attempt to close either a System or Custom task using the REST API."""
        try:
            payload = ResultPayload("task_utils_close_task", **kwargs)
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            task_name = kwargs.get("task_name")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("task_name: %s", task_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")
            res_client = self.rest_client()

            if task_id:
                log.debug("Task ID was provided, using this to contact REST API")

            else:
                inc_tasks = res_client.get(
                    '/incidents/{}/tasks?want_layouts=false&want_notes=false'.format(incident_id))
                yield StatusMessage("Task Name was provided, searching the incident for task")

                for t in inc_tasks:
                    if t['name'] == task_name:
                        yield StatusMessage(u"Found task which matches at ID {}".format(t['id']))
                        task_id = t['id']
                        break
                if not task_id:
                    raise FunctionError(u"Could not find task with name {}".format(task_name))

                # function to update the task description

            def update_with_result(task):
                task["status"] = "C"
                task_name = task["name"]
                return task

            task_url = "/tasks/{}".format(task_id)
            res_client.get_put(task_url, lambda task: update_with_result(task))
            yield StatusMessage("Task {} has been closed".format(task_id))

            results = payload.done(
                success=True,
                content={
                    "task_id": task_id,
                    "task_name": task_name
                }
            )

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()