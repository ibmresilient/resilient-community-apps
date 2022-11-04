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
            u"ms_teams_post_message"],
        "workflows": [
            u"incident_post_message_to_teams",
            u"incident_create_a_microsoft_group",
            u"incident_delete_a_microsoft_group",
            u"task_create_a_microsoft_group",
            u"task_post_message_to_teams",],
        "actions": [
            u"MS Teams: Post task information to teams",
            u"MS Teams: Post incident information to teams",
            u"MS Teams: Create Group from incident",
            u"MS Teams: Create Group from task",
            u"MS Teams: Delete Group from incident"],
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

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - fn_teams
    - Functions:
        - ms_teams_create_group
        - ms_teams_create_team
        - ms_teams_delete_group
        - ms_teams_post_message
    - Workflows:
        - incident_create_a_microsoft_group
        - incident_delete_a_microsoft_group
        - incident_post_message_to_teams
        - task_create_a_microsoft_group
        - task_post_message_to_teams
    - Rules:
        - MS Teams: Create Group from incident
        - MS Teams: Create Group from task
        - MS Teams: Delete Group from incident
        - MS Teams: Post incident information to teams
        - MS Teams: Post task information to teams
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)