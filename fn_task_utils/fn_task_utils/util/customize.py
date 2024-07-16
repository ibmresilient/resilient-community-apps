# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_task_utils"""

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
    Parameters required reload codegen for the fn_task_utils package
    """
    return {
        "package": u"fn_task_utils",
        "message_destinations": [u"fn_task_utils"],
        "functions": [u"task_utils_add_note", u"task_utils_update_task", u"task_utils_close_task", u"task_utils_create"],
        "workflows": [u"task_utils_mark_task_optional", u"task_utils_add_note_to_task", u"task_utils_create_custom_task", u"task_utils_close_task"],
        "actions": [u"Example: Task Utils - Create Custom Task", u"Example: Task Utils - Make this Task Optional", u"Example: Task Utils - Add Note to Task", u"Example: Task Utils - Close Task"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - fn_task_utils
    - Functions:
        - task_utils_add_note
        - task_utils_update_task
        - task_utils_close_task
        - task_utils_create
    - Workflows:
        - task_utils_mark_task_optional
        - task_utils_add_note_to_task
        - task_utils_create_custom_task
        - task_utils_close_task
    - Rules:
        - Example: Task Utils - Create Custom Task
        - Example: Task Utils - Make this Task Optional
        - Example: Task Utils - Add Note to Task
        - Example: Task Utils - Close Task
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)