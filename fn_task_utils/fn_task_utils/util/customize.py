# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_task_utils"""

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
        "message_destinations": [
            u"fn_task_utils"
        ],
        "functions": [
            u"task_utils_add_note",
            u"task_utils_close_task",
            u"task_utils_create",
            u"task_utils_update_task"
        ],
        "workflows": [
            u"task_utils_add_note_to_task",
            u"task_utils_close_task",
            u"task_utils_create_custom_task",
            u"task_utils_mark_task_optional"
        ],
        "actions": [
            u"Example: Task Utils - Add Note to Task",
            u"Example: Task Utils - Close Task",
            u"Example: Task Utils - Create Custom Task",
            u"Example: Task Utils - Make this Task Optional"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_task_utils
    - Functions:
        - task_utils_add_note
        - task_utils_close_task
        - task_utils_create
        - task_utils_update_task
    - Workflows:
        - task_utils_add_note_to_task
        - task_utils_close_task
        - task_utils_create_custom_task
        - task_utils_mark_task_optional
    - Rules:
        - Example: Task Utils - Add Note to Task
        - Example: Task Utils - Close Task
        - Example: Task Utils - Create Custom Task
        - Example: Task Utils - Make this Task Optional
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)