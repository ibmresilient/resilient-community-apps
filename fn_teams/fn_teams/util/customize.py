# -*- coding: utf-8 -*-

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
        "functions": [
            u"ms_teams_create_group",
            u"ms_teams_delete_group",
            u"ms_teams_post_message",
            u"ms_teams_create_team",
            u"ms_teams_enable_team",
            u"ms_teams_archive_team",
            u"ms_teams_create_channel",
            u"ms_teams_delete_channel",
            u"ms_teams_read_message"],
        "workflows": [
            u"incident_post_message_to_teams",
            u"incident_create_a_microsoft_group",
            u"incident_create_a_microsoft_team",
            u"incident_delete_a_microsoft_group",
            u"incident_archive_unarchive_a_microsoft_team",
            u"incident_enable_microsoft_team_for_group",
            u"incident_create_a_teams_channel",
            u"incident_delete_a_teams_channel",
            u"incident_read_a_channels_messages",
            u"task_create_a_microsoft_group",
            u"task_create_a_microsoft_team",
            u"task_post_message_to_teams",
            u"task_delete_a_microsoft_group",
            u"task_archive_unarchive_a_microsoft_team",
            u"task_enable_microsoft_team_for_group",
            u"task_create_a_teams_channel",
            u"task_delete_a_teams_channel",
            u"task_read_a_channels_messages"],
        "actions": [
            u"MS Teams: Create Group",
            u"MS Teams: Create Group From Task",
            u"MS Teams: Delete Group",
            u"MS Teams: Delete Group From Task",
            u"MS Teams: Create Team",
            u"MS Teams: Create Team From Task",
            u"MS Teams: Archive Team",
            u"MS Teams: Archive Team From Task",
            u"MS Teams: Create Channel",
            u"MS Teams: Delete Channel",
            u"MS Teams: Create Channel From Task",
            u"MS Teams: Delete Channel From Task",
            u"MS Teams: Post Task Information",
            u"MS Teams: Post Incident Information",
            u"MS Teams: Enable Teams for Group",
            u"MS Teams: Enable Teams for Group From Task",
            u"MS Teams: Read Channel Messages",
            u"MS Teams: Read Channel Messages From task"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

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
    - Workflows:
        - incident_archive_unarchive_a_microsoft_team
        - incident_create_a_microsoft_group
        - incident_create_a_microsoft_team
        - incident_create_a_teams_channel
        - incident_delete_a_microsoft_group
        - incident_delete_a_teams_channel
        - incident_enable_microsoft_team_for_group
        - incident_post_message_to_teams
        - incident_read_a_channels_messages
        - task_archive_unarchive_a_microsoft_team
        - task_create_a_microsoft_group
        - task_create_a_microsoft_team
        - task_create_a_teams_channel
        - task_delete_a_microsoft_group
        - task_delete_a_teams_channel
        - task_enable_microsoft_team_for_group
        - task_post_message_to_teams
        - task_read_a_channels_messages
    - Rules:
        - MS Teams: Archive Team
        - MS Teams: Archive Team From Task
        - MS Teams: Create Channel
        - MS Teams: Create Channel From Task
        - MS Teams: Create Group
        - MS Teams: Create Group From Task
        - MS Teams: Create Team
        - MS Teams: Create Team From Task
        - MS Teams: Delete Channel
        - MS Teams: Delete Channel From Task
        - MS Teams: Delete Group
        - MS Teams: Delete Group From Task
        - MS Teams: Enable Teams for Group
        - MS Teams: Enable Teams for Group From Task
        - MS Teams: Post Incident Information
        - MS Teams: Post Task Information
        - MS Teams: Read Channel Messages
        - MS Teams: Read Channel Messages From task
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)