# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Bigfix integration with Resilient circuits Functions  """
import logging
import time

# TODO: Check how should be defined this logger
LOG = logging.getLogger(__name__)

__author__ = 'Resilient'


def get_hits(artifact_data, params):
    """Get endpoints with hits from results returned from BigFix.

    :param artifact_data: Data returned from Bigfix
    :param params: Dictionary of Resilient Function parameters
    :return hits: Dictionary of endpoints with hit

    """

    LOG.debug("Filtering endpoint responses for hits.")

    hits = []
    for d in artifact_data:
        if (d["failure"] == 0 or d["failure"] == "False") and d["result"] == "True":
            hits.append(d)
    # if no hits result will be an empty list.
    if hits:
        LOG.info("Detected hits on %s endpoints." % (len(hits)))
    else:
        LOG.info("Detected no hits.")

    return hits

def poll_retry_sleep(retry_timeout, retry_interval, finished):
    """"Sleep for 'retry_interval' if 'retry_timeout' not reached.

    :param retry_timeout: Timeout value for poll status (secs)
    :param retry_interval: Poll status every 'retry' secs
    :param finished: Boolean to indicate if status received from bigfix
    """
    retry_timeout = retry_timeout - retry_interval
    if retry_timeout > 0 and not finished:
        time.sleep(retry_interval)
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
            if status_message:
                if status_message == "The action executed successfully." or "is not relevant" in status_message:
                    status = "OK"
                elif status_message == "The action failed.":
                    status = "Failed"
                elif status_message == "Evaluating relevance and action constraints." or status_message == \
                        "The action is currently running.":
                    retry_timeout = poll_retry_sleep(retry_timeout, retry_interval, finished)
                    continue
                else:
                    status = "Unsupported"
                finished = True

        except Exception as ex:
            LOG.error(ex)
            raise ex

        retry_timeout = poll_retry_sleep(retry_timeout, retry_interval, finished)

    if not finished:
        status = "Timedout"

    return (status, status_message)
