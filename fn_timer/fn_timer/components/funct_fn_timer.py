# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import time
import datetime
import logging
from resilient_circuits import AppFunctionComponent, app_function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields, ResultPayload, get_workflow_status

PACKAGE_NAME = "fn_timer"
FN_NAME = "fn_timer"
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_timer'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _timer_function(self, fn_inputs):
        """
        Function: This function implements a timer (sleep) function that when called from a workflow will cause the workflow to pause for the specified amount of time. The function takes one of two parameters as input: `timer_time` or `timer_epoch`.
        Inputs:
            -   fn_inputs.timer_time
            -   fn_inputs.timer_epoch

        This function implements a simple timer.  A workflow using this function will sleep for the
        specified amount of time. The function takes as input timer_time or timer_epoch as input.
        The function periodically checks the status of the calling workflow and will end
        function execution if the workflow has been terminated.

        The timer_time parameter is a string is of format “time value” concatenated with a
        “time unit” character, where character is:
        ‘s’ for seconds
        ‘m’ for minutes
        ‘h’ for hours
        ‘d’ for days
        For example: '30s' = 30 seconds; '40m' = 40 minutes;

        The timer_epoch parameter is an epoch time value that specifies the time the timer should
        stop sleeping. The timer function computes the total sleep time needed.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        try:
            # Get the function parameters:
            timer_time = getattr(fn_inputs,"timer_time", None)  # text
            timer_epoch = getattr(fn_inputs, "timer_epoch", None) # datetime picker

            log = logging.getLogger(__name__)
            log.info("timer_time: %s", timer_time)
            log.info("timer_epoch: %s", timer_epoch)

            if timer_time is not None and timer_epoch is not None:
                raise ValueError("Timer function takes one parameter as input: timer_time OR timer_epoch.")

            # Get max timer to sleep from app.config setting and convert to seconds.
            max_timer = self.options.get("max_timer")

            if max_timer is None:
                # max_timer is not set in the app.config, so set a default and output a message.
                max_timer = "30d"
                yield StatusMessage("Please specify [fn_timer] max_timer in app.config. Setting default max_timer to '30d'.")

            max_timer_in_seconds = get_sleep_time_in_seconds(max_timer)

            # Compute the time to wait in seconds
            if timer_epoch is not None:
                total_time_in_seconds = get_sleep_time_from_epoch(timer_epoch)
            else:
                total_time_in_seconds = get_sleep_time_in_seconds(timer_time)

            if total_time_in_seconds > max_timer_in_seconds:
                raise ValueError(f'Requested sleep timer {total_time_in_seconds}s is greater than max_timer {max_timer_in_seconds}s set in app.config')

            # Compute the workflow check interval time based on the total time in seconds.
            wf_check_interval = compute_interval_time(total_time_in_seconds)

            # Get workflow instance ID
            wf_instance_id = self.get_fn_msg()["workflow_instance"]["workflow_instance_id"]
            res_client = self.rest_client()

            # Initialize before the while loop
            current_sleep_time = 0
            wf_status = get_workflow_status(res_client, wf_instance_id)

            # Loop and sleep till total time to sleep achieved and while workflow is not terminated
            while (current_sleep_time < total_time_in_seconds) and (total_time_in_seconds > 0) and not wf_status.is_terminated:
                yield StatusMessage('Sleeping for {}s. {}/{}s complete.'.format(wf_check_interval, current_sleep_time, total_time_in_seconds))

                # Sleep interval time
                time.sleep(wf_check_interval)

                # Keep track of total sleep time
                current_sleep_time = current_sleep_time + wf_check_interval

                # Check the status of the workflow
                wf_status = get_workflow_status(res_client, wf_instance_id)

                # This case will be True where total_time_in_seconds is odd and it is the
                # final time through the while-loop.  For example: total_time_in_seconds=5
                # will have awf_check_interval=2, the last time through the loop the sleep
                # time should be 1.
                if (current_sleep_time + wf_check_interval) > total_time_in_seconds:
                    wf_check_interval = total_time_in_seconds - current_sleep_time

            if wf_status.is_terminated:
                yield StatusMessage('Workflow was terminated.')

            yield StatusMessage('Total sleep time {} seconds complete.'.format(current_sleep_time))

            results = {"Workflow Status": wf_status.as_dict()}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))


def get_sleep_time_in_seconds(time_string):
    """
    Parse the input time string into "time value" and "time unit" and compute the time in seconds.
    The input string will be in format time_value with the time unit character concatenated on the end.
    Time unit will be: 's' for seconds, 'm' for minutes, 'h' for hours or 'd' for days.
    For example '30s' = 30 seconds; '20m' = 20 minutes; '2h' = 2 hours; '5d' = 5 days.
    """
    # Parse time string time value which should be integer.
    try:
        time_value = int(time_string[:-1])
    except:
        raise ValueError("Invalid timer_time string format: time value should be integer. For example: 5s, 10m, or 1d")

    # Get the time units from input string.
    time_unit = time_string.rstrip()[-1].lower()

    # Compute the total time to sleep in seconds
    if time_unit == 's':
        time_in_seconds = time_value
    elif time_unit == 'm':
        time_in_seconds = time_value * SECONDS_IN_MINUTE
    elif time_unit == 'h':
        time_in_seconds = time_value * SECONDS_IN_HOUR
    elif time_unit == 'd':
        time_in_seconds = time_value * SECONDS_IN_DAY
    else:
        raise ValueError("Invalid timer_time string format: should end in 's' for seconds, 'm for minutes, 'h' for hours or 'd' for days")

    return time_in_seconds

def get_sleep_time_from_epoch(end_epoch):
    """
    Given the epoch time to end the timer, compute the total number of seconds to sleep.
    """
    # Make sure timer end is not in the past.
    now_utc = datetime.datetime.utcnow()
    end_timer_utc = datetime.datetime.utcfromtimestamp(end_epoch / 1000)

    if now_utc > end_timer_utc:
        raise ValueError("Timer end date is in the past: {0}".format(end_epoch))

    # Compute total time to sleep in seconds.
    num_seconds = (end_timer_utc - now_utc).total_seconds()

    return int(num_seconds)

def compute_interval_time(time_in_seconds):
    """
    Compute time interval (in seconds) that is used to check if the workflow has been terminated.
    """
    if time_in_seconds < 0:
        raise ValueError("Invalid timer_time: can't sleep less than zero.")
    elif time_in_seconds == 0:
        return 0

    if time_in_seconds <= SECONDS_IN_MINUTE:
        if time_in_seconds > 1:
            # Less than 1 minute, but more than 2 seconds
            time_interval = time_in_seconds / 2
        else:
            time_interval = time_in_seconds
    elif time_in_seconds <= SECONDS_IN_HOUR:
        # Less than an hour
        time_interval = time_in_seconds / 4
    elif time_in_seconds <= SECONDS_IN_DAY:
        # Less than a day
        time_interval = time_in_seconds / 10
    else:
        # More than a day, check every hour
        time_interval = SECONDS_IN_HOUR

    return int(time_interval)
