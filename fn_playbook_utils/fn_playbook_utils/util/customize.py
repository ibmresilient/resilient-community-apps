# -*- coding: utf-8 -*-

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
        "functions": [u"pb_get_playbook_data", u"pb_get_workflow_content", u"pb_get_workflow_data"],
        "workflows": [u"pb_get_workflows_by_artifact_value_for_last_30_days", u"wf_get_workflow_data", u"wf_get_workflow_frequency", u"wf_get_workflow_usage_at_incident_close", u"wf_get_workflows_by_artifact_value", u"wf_get_workflows_by_attachment_filename", u"wf_get_workflows_by_task_name"],
        "actions": [u"PB: Get workflow/playbook frequency", u"PB: Get workflow/playbook usage", u"PB: Get workflow/playbook usage at incident close", u"PB: Get workflows/playbooks by artifact value", u"PB: Get workflows/playbooks by artifact value for last 30 days", u"PB: Get workflows/playbooks by attachment name", u"PB: Get workflows/playbooks by task name"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"workflow_usage"],
        "automatic_tasks": [],
        "scripts": [u"PB: Display playbook data", u"PB: Display workflow data"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

    Contents:
    - Message Destinations:
        - fn_playbook_utils
    - Functions:
        - pb_get_playbook_data
        - pb_get_workflow_content
        - pb_get_workflow_data
    - Workflows:
        - pb_get_workflows_by_artifact_value_for_last_30_days
        - wf_get_workflow_data
        - wf_get_workflow_frequency
        - wf_get_workflow_usage_at_incident_close
        - wf_get_workflows_by_artifact_value
        - wf_get_workflows_by_attachment_filename
        - wf_get_workflows_by_task_name
    - Rules:
        - PB: Get workflow/playbook frequency
        - PB: Get workflow/playbook usage
        - PB: Get workflow/playbook usage at incident close
        - PB: Get workflows/playbooks by artifact value
        - PB: Get workflows/playbooks by artifact value for last 30 days
        - PB: Get workflows/playbooks by attachment name
        - PB: Get workflows/playbooks by task name
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