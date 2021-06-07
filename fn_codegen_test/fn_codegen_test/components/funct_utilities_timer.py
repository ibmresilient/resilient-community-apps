# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_timer"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_codegen_test", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_codegen_test", {})

    @function("utilities_timer")
    def _utilities_timer_function(self, event, *args, **kwargs):
        """Function: This function implements a timer (sleep) function that when called from a workflow will cause the workflow to pause for the specified amount of time. The function takes one of two parameters as input: `utilities_time` or `utilities_epoch`.

The utilities_time parameter is a string that specifies the total amount of time to pause. The input string is of format `time value` concatenated with a `time unit` character, where character is:
• `s` for seconds
• `m` for minutes
• `h` for hours
• `d` for days

For example: `30s` = 30 seconds; `20m` = 20 minutes; `5h` = 5 hours; `6d` = 6 days

The `utilities_epoch` parameter is the epoch time that the timer function should stop sleeping. An epoch time value is returned from the date time picker UI widget.

The timer function will break down the total amount of time to pause into smaller sleep time intervals and check in between sleep time whether the workflow has been terminated while the function is running. If the workflow has been terminated, the function will end execution."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            utilities_time = kwargs.get("utilities_time")  # text
            utilities_epoch = kwargs.get("utilities_epoch")  # datetimepicker

            log = logging.getLogger(__name__)
            log.info("utilities_time: %s", utilities_time)
            log.info("utilities_epoch: %s", utilities_epoch)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()