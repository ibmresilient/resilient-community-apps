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
        "functions": [u"ms_teams_create_group", u"teams_post_message"],
        "workflows": [u"example_post_incident_to_ms_teams", u"example_post_task_to_microsoft_teams", u"incident_create_a_teams_group"],
        "actions": [u"Example: Post a Task to Microsoft Teams", u"Example: Post an Incident to Microsoft Teams", u"MS Teams: Create Group"],
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
        - teams_post_message
    - Workflows:
        - example_post_incident_to_ms_teams
        - example_post_task_to_microsoft_teams
        - incident_create_a_teams_group
    - Rules:
        - Example: Post a Task to Microsoft Teams
        - Example: Post an Incident to Microsoft Teams
        - MS Teams: Create Group
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)