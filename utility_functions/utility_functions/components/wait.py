# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'wait"""

    @function("wait")
    def _wait_function(self, event, *args, **kwargs):
        """Function: Waits for a given number of seconds"""
        try:
            # Get the function parameters:
            seconds = kwargs.get("seconds")  # number
            if seconds is None or seconds <= 0:
                seconds = 0
                yield StatusMessage("Waiting for {} seconds...".format(seconds))
            elif seconds > 60 * 60 * 24:
                seconds = 60 * 60 * 24
                yield StatusMessage("Waiting for {} seconds (max)...".format(seconds))
            else:
                yield StatusMessage("Waiting for {} seconds...".format(seconds))
            time.sleep(seconds)

            # Produce an empty FunctionResult
            yield FunctionResult({})
        except Exception:
            yield FunctionError()