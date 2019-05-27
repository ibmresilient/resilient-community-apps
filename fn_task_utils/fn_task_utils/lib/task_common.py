# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import logging


def find_task_by_name(res_client, incident_id, task_name):
    """
    locate a task by name in an incident
    :param res_client:
    :param incident_id:
    :param task_name:
    :return: task_id or None
    """
    inc_tasks = res_client.get(
        '/incidents/{}/tasks?want_layouts=false&want_notes=false'.format(incident_id))

    for t in inc_tasks:
        if t.get('name', "").lower() == task_name.lower():
            return t['id']

    return None


def get_function_input(inputs, input_name, optional=False):
    """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""

    log = logging.getLogger(__name__)
    log.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

    the_input = inputs.get(input_name)

    if the_input is None and optional is False:
        err = "'{0}' is a mandatory function input".format(input_name)
        raise ValueError(err)
    else:
        log.debug("Got function input: %s", input_name)
        return the_input
