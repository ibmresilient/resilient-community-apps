# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload

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
            task_id = kwargs.get("task_id")  # number
            task_utils_note_type = self.get_select_param(kwargs.get("task_utils_note_type"))  # select, values: "text", "html"
            task_utils_note_body = kwargs.get("task_utils_note_body")  # text

            log = logging.getLogger(__name__)
            log.info("task_id: %s", task_id)
            log.info("task_utils_note_type: %s", task_utils_note_type)
            log.info("task_utils_note_body: %s", task_utils_note_body)

            task_note_json = {
                "text": {
                    "format": task_utils_note_type['name'],
                    "content": task_utils_note_body
                }
            }

            res_client = self.rest_client()

            yield StatusMessage("Posting note to API")

            response = res_client.post('/tasks/{}/comments'.format(task_id), task_note_json)

            yield StatusMessage("Completed API call")

            results = payload.done(
                success=True,
                content={
                    "response": response
                }
            )

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()