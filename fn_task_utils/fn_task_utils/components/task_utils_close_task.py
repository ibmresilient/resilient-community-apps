# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_task_utils.lib.task_common import find_task_by_name, get_function_input


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

        def close_task_status(task):
            """
            A inner function which is used as a lambda
            Get_put from the res_client gets our data and this lambda decides what to do with the data
            The return value of this lambda is then sent to Resilient as a PUT.
            :param task:
            :return task:
            """
            task["status"] = "C"
            log.debug("Changed status to closed for task with name %s" % task["name"])
            return task

        try:
            payload = ResultPayload("task_utils_close_task", **kwargs)
            # Get the function parameters:
            incident_id = get_function_input(kwargs, "incident_id")  # number
            task_id = get_function_input(kwargs, "task_id", optional=True)  # number
            task_name = get_function_input(kwargs, "task_name", optional=True)  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("task_name: %s", task_name)

            res_client = self.rest_client()

            if not task_name and not task_id:
                raise ValueError("Either a Task ID or a Task Name to search for must be provided.")

            if task_id:
                log.debug("Task ID was provided, using this to contact REST API")

            else:
                if task_name:
                    yield StatusMessage(
                        u"task_name was provided; Searching incident {} for first matching task with name '{}'".format(
                            incident_id, task_name))

                    task_id = find_task_by_name(res_client, incident_id, task_name)

                    if not task_id:
                        raise ValueError(u"Could not find task with name {}".format(task_name))

            task_url = "/tasks/{}".format(task_id)
            try:
                res_client.get_put(task_url, lambda task: close_task_status(task))
            except Exception as close_exception:
                err_msg = "Encountered exception while trying to close task. Error: {}", close_exception
                raise ValueError(err_msg)
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
