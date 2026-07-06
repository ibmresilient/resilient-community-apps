# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.7.0.1603

"""Generate the SOAR customizations required for fn_jira"""

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
        "message_destinations": [
            u"fn_jira"
        ],
        "functions": [
            u"jira_create_comment",
            u"jira_open_issue",
            u"jira_transition_issue"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"jira_internal_url",
            u"jira_issue_closed_on_jira",
            u"jira_issue_id",
            u"jira_issue_status",
            u"jira_issue_type",
            u"jira_linked_to_incident",
            u"jira_project_key",
            u"jira_server",
            u"jira_url"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"jira_task_references"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"example_create_jira_issue",
            u"example_create_jira_issue_task",
            u"example_jira_close_issue",
            u"example_jira_close_issue_task",
            u"example_jira_create_comment"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_jira
    - Functions:
        - jira_create_comment
        - jira_open_issue
        - jira_transition_issue
    - Playbooks:
        - example_create_jira_issue
        - example_create_jira_issue_task
        - example_jira_close_issue
        - example_jira_close_issue_task
        - example_jira_create_comment
    - Incident Fields:
        - jira_internal_url
        - jira_issue_closed_on_jira
        - jira_issue_id
        - jira_issue_status
        - jira_issue_type
        - jira_linked_to_incident
        - jira_project_key
        - jira_server
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