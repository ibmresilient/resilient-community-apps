# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""


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
        if t['name'].lower() == task_name.lower():
            return t['id']

    return None