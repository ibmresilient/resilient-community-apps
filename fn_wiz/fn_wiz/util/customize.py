# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_wiz"""

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
    Parameters required reload codegen for the fn_wiz package
    """
    return {
        "package": u"fn_wiz",
        "message_destinations": [
            u"fn_wiz"
        ],
        "functions": [
            u"wiz_pull_vulnerabilities",
            u"wiz_query_issue",
            u"wiz_send_soar_notes",
            u"wiz_sync_status"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"wiz_description",
            u"wiz_issue_id",
            u"wiz_issue_status"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"wiz_projects_table",
            u"wiz_vulnerabilities_table"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"wiz_populate_case",
            u"wiz_pull_vulnerabilities",
            u"wiz_pull_vulnerabilities_by_project",
            u"wiz_sync_notes_to_issue",
            u"wiz_sync_status"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_wiz
    - Functions:
        - wiz_pull_vulnerabilities
        - wiz_query_issue
        - wiz_send_soar_notes
        - wiz_sync_status
    - Playbooks:
        - wiz_populate_case
        - wiz_pull_vulnerabilities
        - wiz_pull_vulnerabilities_by_project
        - wiz_sync_notes_to_issue
        - wiz_sync_status
    - Incident Fields:
        - wiz_description
        - wiz_issue_id
        - wiz_issue_status
    - Data Tables:
        - wiz_projects_table
        - wiz_vulnerabilities_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)