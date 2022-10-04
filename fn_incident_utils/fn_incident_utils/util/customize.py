# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_incident_utils"""

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
    Parameters required reload codegen for the fn_incident_utils package
    """
    return {
        "package": u"fn_incident_utils",
        "message_destinations": [u"fn_incident_utils"],
        "functions": [u"incident_utils_close_incident", u"incident_utils_create_incident", u"search_incidents"],
        "workflows": [u"example_close_incident", u"example_create_incident", u"example_search_incidents"],
        "actions": [u"Example: Close Incident", u"Example: Create Incident", u"Example: Search Incidents"],
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

    IBM Resilient Platform Version: 38.0.6006

    Contents:
    - Message Destinations:
        - fn_incident_utils
    - Functions:
        - incident_utils_close_incident
        - incident_utils_create_incident
        - search_incidents
    - Workflows:
        - example_close_incident
        - example_create_incident
        - example_search_incidents
    - Rules:
        - Example: Close Incident
        - Example: Create Incident
        - Example: Search Incidents
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)