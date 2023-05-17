# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4368

"""Generate the Resilient customizations required for fn_teams"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_teams package
    """
    return {
        "package": u"fn_teams",
        "message_destinations": [u"fn_teams"],
        "functions": [u"ms_teams_archive_team", u"ms_teams_create_channel", u"ms_teams_create_group", u"ms_teams_create_team", u"ms_teams_delete_channel", u"ms_teams_delete_group", u"ms_teams_enable_team", u"ms_teams_post_message", u"ms_teams_read_message"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"ms_teams_archive_team_from_task_pb", u"ms_teams_archive_team_pb", u"ms_teams_create_channel_from_task_pb", u"ms_teams_create_channel_pb", u"ms_teams_create_group_from_task_pb", u"ms_teams_create_group_pb", u"ms_teams_create_team_from_task_pb", u"ms_teams_create_team_pb", u"ms_teams_delete_channel_from_task_pb", u"ms_teams_delete_channel_pb", u"ms_teams_delete_group_from_task_pb", u"ms_teams_delete_group_pb", u"ms_teams_enable_teams_for_group_from_task_pb", u"ms_teams_enable_teams_for_group_pb", u"ms_teams_post_incident_information_pb", u"ms_teams_post_task_information_pb", u"ms_teams_read_channel_messages_from_task_pb", u"ms_teams_read_channel_messages_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_teams
    - Functions:
        - ms_teams_archive_team
        - ms_teams_create_channel
        - ms_teams_create_group
        - ms_teams_create_team
        - ms_teams_delete_channel
        - ms_teams_delete_group
        - ms_teams_enable_team
        - ms_teams_post_message
        - ms_teams_read_message
    - Playbooks:
        - ms_teams_archive_team_from_task_pb
        - ms_teams_archive_team_pb
        - ms_teams_create_channel_from_task_pb
        - ms_teams_create_channel_pb
        - ms_teams_create_group_from_task_pb
        - ms_teams_create_group_pb
        - ms_teams_create_team_from_task_pb
        - ms_teams_create_team_pb
        - ms_teams_delete_channel_from_task_pb
        - ms_teams_delete_channel_pb
        - ms_teams_delete_group_from_task_pb
        - ms_teams_delete_group_pb
        - ms_teams_enable_teams_for_group_from_task_pb
        - ms_teams_enable_teams_for_group_pb
        - ms_teams_post_incident_information_pb
        - ms_teams_post_task_information_pb
        - ms_teams_read_channel_messages_from_task_pb
        - ms_teams_read_channel_messages_pb
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)