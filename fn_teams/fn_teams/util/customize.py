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
            u"ms_teams_archive_team"],
        "workflows": [
            u"incident_post_message_to_teams",
            u"incident_create_a_microsoft_group",
            u"incident_create_a_microsoft_team",
            u"task_create_a_microsoft_group",
            u"task_create_a_microsoft_team",
            u"task_post_message_to_teams",
            u"common_delete_a_microsoft_group",
            u"common_archive_unarchive_a_microsoft_team",
            u"common_enable_microsoft_team_for_group"],
        "actions": [
            u"MS Teams: Post Task Information to Teams",
            u"MS Teams: Post incident information to teams",
            u"MS Teams: Create Group from incident",
            u"MS Teams: Create Group from task",
            u"MS Teams: Delete Group from incident",
            u"MS Teams: Delete Group from task",
            u"MS Teams: Create Team from incident",
            u"MS Teams: Create Team from task",
            u"MS Teams: Enable Teams for an existing Group"],
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
        - ms_teams_create_group
        - ms_teams_create_team
        - ms_teams_delete_group
        - ms_teams_enable_team
        - ms_teams_post_message
    - Workflows:
        - common_archive_unarchive_a_microsoft_team
        - common_delete_a_microsoft_group
        - common_enable_microsoft_team_for_group
        - incident_create_a_microsoft_group
        - incident_create_a_microsoft_team
        - incident_post_message_to_teams
        - task_create_a_microsoft_group
        - task_create_a_microsoft_team
        - task_post_message_to_teams
    - Rules:
        - MS Teams: Create Group from incident
        - MS Teams: Create Group from task
        - MS Teams: Create Team from incident 
        - MS Teams: Create Team from task
        - MS Teams: Delete Group from incident
        - MS Teams: Delete Group from task
        - MS Teams: Enable Teams for an existing Group
        - MS Teams: Post incident information to teams
        - MS Teams: Post Task Information to Teams
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)