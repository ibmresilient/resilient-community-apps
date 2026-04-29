# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
""" Helper functions for Bigfix integration with SOAR Functions  """

from time import sleep
from logging import getLogger

LOG = getLogger(__name__)

def poll_retry_sleep(retry_timeout, retry_interval, finished):
    """"Sleep for 'retry_interval' if 'retry_timeout' not reached.
    :param retry_timeout: Timeout value for poll status (secs)
    :param retry_interval: Poll status every 'retry' secs
    :param finished: Boolean to indicate if status received from bigfix
    """
    retry_timeout -= retry_interval
    if retry_timeout > 0 and not finished:
        sleep(retry_interval)

    return retry_timeout

def poll_action_status(bigfix_client, bigfix_action_id, retry_interval=30, retry_timeout=600):
    """"Poll Bigfix for status of action by id.
    :param bigfix_action_id: Bigfix action id to poll status
    :param retry_interval: Poll status every 'retry' secs
    :param retry_timeout: Timeout value for poll status (secs)
    """
    finished = False
    status = None

    while retry_timeout >= 0 and not finished:
        status_message = None
        try:
            status_message = bigfix_client.get_bf_action_status(bigfix_action_id)
        except Exception as ex:
            LOG.error(ex)
            raise ex

        if status_message:
            if status_message == "The action executed successfully." or "is not relevant" in status_message:
                status = "OK"
            elif status_message == "The action failed.":
                status = "Failed"
            elif status_message in ["Evaluating relevance and action constraints.", "The action is currently running."]:
                retry_timeout = poll_retry_sleep(retry_timeout, retry_interval, finished)
                continue
            else:
                status = "Unsupported"
            finished = True

        retry_timeout = poll_retry_sleep(retry_timeout, retry_interval, finished)

    if not finished:
        status = "Timedout"

    return (status, status_message)
