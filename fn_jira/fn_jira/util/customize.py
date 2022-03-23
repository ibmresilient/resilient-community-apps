# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_jira"""

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
    Parameters required reload codegen for the fn_jira package
    """
    return {
        "package": u"fn_jira",
        "message_destinations": [u"fn_jira"],
        "functions": [u"jira_create_comment", u"jira_open_issue", u"jira_transition_issue"],
        "workflows": [u"example_jira_open_issue_task", u"jira_create_comment", u"jira_open_issue", u"jira_transition_issue", u"jira_transition_issue_task"],
        "actions": [u"Example: Create Jira Issue", u"Example: Create Jira Issue (Task)", u"Example: Jira Close Issue", u"Example: Jira Close Issue (Task)", u"Example: Jira Create Comment", u"Example: Jira Create Comment (Task)"],
        "incident_fields": [u"jira_internal_url", u"jira_issue_id", u"jira_url"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"jira_task_references"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 42.2.41

    Contents:
    - Message Destinations:
        - fn_jira
    - Functions:
        - jira_create_comment
        - jira_open_issue
        - jira_transition_issue
    - Workflows:
        - example_jira_open_issue_task
        - jira_create_comment
        - jira_open_issue
        - jira_transition_issue
        - jira_transition_issue_task
    - Rules:
        - Example: Create Jira Issue
        - Example: Create Jira Issue (Task)
        - Example: Jira Close Issue
        - Example: Jira Close Issue (Task)
        - Example: Jira Create Comment
        - Example: Jira Create Comment (Task)
    - Incident Fields:
        - jira_internal_url
        - jira_issue_id
        - jira_url
    - Data Tables:
        - jira_task_references
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)