# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_remedy"""

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
    Parameters required reload codegen for the fn_remedy package
    """
    return {
        "package": u"fn_remedy",
        "message_destinations": [u"fn_remedy"],
        "functions": [u"remedy_close_incident", u"remedy_create_incident"],
        "workflows": [u"close_a_remedy_incident_from_task", u"create_a_remedy_incident_from_task"],
        "actions": [u"Remedy Close Incident from Task", u"Remedy Create Incident from Task"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"remedy_linked_incidents_reference_table"],
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
        - fn_remedy
    - Functions:
        - remedy_close_incident
        - remedy_create_incident
    - Workflows:
        - close_a_remedy_incident_from_task
        - create_a_remedy_incident_from_task
    - Rules:
        - Remedy Close Incident from Task
        - Remedy Create Incident from Task
    - Data Tables:
        - remedy_linked_incidents_reference_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)