# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for fn_playbook_utils"""

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
    Parameters required reload codegen for the fn_playbook_utils package
    """
    return {
        "package": u"fn_playbook_utils",
        "message_destinations": [u"fn_playbook_utils"],
        "functions": [u"pb_export_playbook", u"pb_get_playbook_data", u"pb_get_playbooks", u"pb_get_workflow_content", u"pb_get_workflow_data", u"pb_import_playbook"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"workflow_usage"],
        "automatic_tasks": [],
        "scripts": [u"PB: Display playbook data", u"PB: Display workflow data"],
        "playbooks": [u"pb_get_workflowplaybook_usage_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_playbook_utils
    - Functions:
        - pb_export_playbook
        - pb_get_playbook_data
        - pb_get_playbooks
        - pb_get_workflow_content
        - pb_get_workflow_data
        - pb_import_playbook
    - Playbooks:
        - pb_get_workflowplaybook_usage_pb
    - Data Tables:
        - workflow_usage
    - Scripts:
        - PB: Display playbook data
        - PB: Display workflow data
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)