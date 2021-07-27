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
        "functions": [u"wf_get_workflow_content", u"wf_get_workflow_data"],
        "workflows": [u"wf_get_workflow_content", u"wf_get_workflow_data", u"wf_get_workflow_frequency", u"wf_get_workflow_usage_at_incident_close", u"wf_get_workflows_by_artifact_value", u"wf_get_workflows_by_attachment_filename", u"wf_get_workflows_by_task_name"],
        "actions": [u"WF: Get workflow content", u"WF: Get workflow frequency", u"WF: Get workflow usage", u"WF: Get workflow usage at incident close", u"WF: Get workflows by artifact value", u"WF: Get workflows by attachment name", u"WF: Get workflows by task name"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"workflow_usage"],
        "automatic_tasks": [],
        "scripts": []
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
        - wf_get_workflow_content
        - wf_get_workflow_data
    - Workflows:
        - wf_get_workflow_content
        - wf_get_workflow_data
        - wf_get_workflow_frequency
        - wf_get_workflow_usage_at_incident_close
        - wf_get_workflows_by_artifact_value
        - wf_get_workflows_by_attachment_filename
        - wf_get_workflows_by_task_name
    - Rules:
        - WF: Get workflow content
        - WF: Get workflow frequency
        - WF: Get workflow usage
        - WF: Get workflow usage at incident close
        - WF: Get workflows by artifact value
        - WF: Get workflows by attachment name
        - WF: Get workflows by task name
    - Data Tables:
        - workflow_usage
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)