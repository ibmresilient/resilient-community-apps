# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import time
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, get_workflow_status

CONFIG_DATA_SECTION = 'fn_utilities'
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_timer"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("utilities_timer")
    def _utilities_timer_function(self, event, *args, **kwargs):
        """This function implements a simple timer.  A workflow using this function will sleep for the
        specified amount of time. The input string is of format “time value” concatenated with a
        “time unit” character, where character is:
        ‘s’ for seconds
        ‘m’ for minutes
        ‘h’ for hours
        ‘d’ for days
        For example: '30s' = 30 seconds; '40m' = 40 minutes;
        The function periodically checks the status of the calling workflow and will end
        function execution if the workflow has been terminated."""
        try:
            # Initialize results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            utilities_time = kwargs.get("utilities_time")  # text

            log = logging.getLogger(__name__)
            log.info("utilities_time: %s", utilities_time)

            # Parse the input time string and compute the total time to sleep
            # and the workflow check interval in seconds.
            total_time_in_seconds = get_sleep_time_in_seconds(utilities_time)
            wf_check_interval = compute_interval_time(total_time_in_seconds)

            # Get workflow instance ID
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            res_client = self.rest_client()

            # Initialize before the while loop
            current_sleep_time = 0
            wf_status = get_workflow_status(res_client, wf_instance_id)

            # Loop and sleep till total time to sleep achieved and while workflow is not terminated
            while (current_sleep_time < total_time_in_seconds) and (total_time_in_seconds > 0) and not wf_status.is_terminated:
                yield StatusMessage('Sleeping for {} out of {} seconds.'.format(wf_check_interval, total_time_in_seconds))

                # Sleep interval time
                time.sleep(wf_check_interval)

                # Keep track of total sleep time
                current_sleep_time = current_sleep_time + wf_check_interval

                # Check the status of the workflow
                wf_status = get_workflow_status(res_client, wf_instance_id)

            yield StatusMessage('Total sleep time {} seconds complete.'.format(current_sleep_time))

            # Return the workflow status
            results = rp.done(True, wf_status.as_dict(), wf_status.reason)

            log.debug("RESULTS: %s", results)
            log.info("> Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)


def get_sleep_time_in_seconds(time_string):
    """
    Parse the input time string into "time value" and "time unit" and compute the time in seconds.
    The input string will be in format time_value with the time unit character concatenated on the end.
    Time unit will be: 's' for seconds, 'm' for minutes, 'h' for hours or 'd' for days.
    For example '30s' = 30 seconds; '20m' = 20 minutes; '2h' = 2 hours; '5d' = 5 days.
    """
    # Parse the time string
    time_unit = time_string.rstrip()[-1]
    time_value = int(time_string[:-1])

    # Compute the total time to sleep in seconds
    if time_unit == 's':
        time_in_seconds = time_value
    elif time_unit == 'm':
        time_in_seconds = time_value * SECONDS_IN_MINUTE
    elif time_unit == 'h':
        time_in_seconds = time_value * SECONDS_IN_HOUR
    elif time_unit == 'd':
        # In the case of sleeping for days check workflow every hour
        time_in_seconds = time_value * SECONDS_IN_DAY
    else:
        raise ValueError("Invalid utilities_time string format: should end in 's' for seconds, 'm for minutes, 'h' for hours or 'd' for days")

    return time_in_seconds

def compute_interval_time(time_in_seconds):
    """
    Compute time interval (in seconds) that is used to check if the workflow has been terminated.
    """
    if time_in_seconds <= SECONDS_IN_MINUTE:
        if time_in_seconds > 1:
            # Less than 1 minute, but more than 2 seconds
            time_interval = time_in_seconds / 2
        else:
            time_interval = time_in_seconds
    elif time_in_seconds <= SECONDS_IN_HOUR:
        # Less than an hour, check 4 times
        time_interval = time_in_seconds / 4
    elif time_in_seconds <= SECONDS_IN_DAY:
        # Less than a day, check 10 times
        time_interval = time_in_seconds / 10
    else:
        # More than a day, check every hour
        time_interval = SECONDS_IN_HOUR

    return time_interval
