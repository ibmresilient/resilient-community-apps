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
        """Function: This function implements a simple timer.  A workflow will pause fo.  The f"""
        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            utilities_time = kwargs.get("utilities_time")  # text

            log = logging.getLogger(__name__)
            log.info("utilities_time: %s", utilities_time)

            # Parse the input time string and compute the total time to sleep
            # and the workflow check interval in seconds.
            total_time_in_seconds, wf_check_interval = get_time_and_interval_time_in_seconds(utilities_time)

            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            res_client = self.rest_client()

            current_sleep_time = 0
            wf_status = get_workflow_status(res_client, wf_instance_id)

            # Loop and sleep while workflow is not terminated and
            while (current_sleep_time < total_time_in_seconds) and not wf_status.is_terminated:
                yield StatusMessage('Sleeping for {} out of {} seconds.'.format(wf_check_interval, total_time_in_seconds))

                # Sleep interval time
                time.sleep(wf_check_interval)

                # Keep track of total sleep time
                current_sleep_time = current_sleep_time + wf_check_interval

                # Check the status of the workflow
                wf_status = get_workflow_status(res_client, wf_instance_id)

            # Return the workflow status
            results = rp.done(True, wf_status)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)


def get_time_and_interval_time_in_seconds(time_string):
    """
    Parse the input time string into "time value" and "time unit".
    The input string will be in format time_value with the time unit character concatenated on the end.
    Time unit will be: 's' for seconds, 'm for minutes, 'h' for hours or 'd' for days.
    For example '30s' = 30 seconds; '20m' = 20 minutes; '2h' = 2 hours; '5d' = 5 days.
    """
    time_unit = time_string.rstrip()[-1]
    time_value = int(time_string[:-1])
    time_wf_check_interval = 0

    # Compute the total time to sleep in seconds
    if time_unit == 's':
        total_time_in_seconds = time_value
    elif time_unit == 'm':
        total_time_in_seconds = time_value * SECONDS_IN_MINUTE
    elif time_unit == 'h':
        total_time_in_seconds = time_value * SECONDS_IN_HOUR
    elif time == 'd':
        # In the case of sleeping for days check workflow every hour
        total_time_in_seconds = time_value * SECONDS_IN_DAY
    else:
        raise ValueError("Invalid utilities_time string format: should end in 's' for seconds, 'm for minutes, 'h' for hours or 'd' for days")

    # Compute time interval (in seconds) to check if the workflow terminated
    if total_time_in_seconds <= SECONDS_IN_MINUTE:
        # Less than 1 minute
        time_wf_check_interval = total_time_in_seconds / 2
    elif total_time_in_seconds <= SECONDS_IN_HOUR:
        # Less than an hour, check
        time_wf_check_interval = total_time_in_seconds / 4
    elif total_time_in_seconds <= SECONDS_IN_DAY:
        # Less than a day, check
        time_wf_check_interval = total_time_in_seconds / 10
    else:
        # More than a day, check every hour
        time_wf_check_interval = SECONDS_IN_HOUR

    return total_time_in_seconds, time_wf_check_interval
