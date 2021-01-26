# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pipl"""

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
    Parameters required reload codegen for the fn_pipl package
    """
    return {
        "package": u"fn_pipl",
        "message_destinations": [u"fn_pipl"],
        "functions": [u"pipl_search_function"],
        "workflows": [u"example_pipl_search_function"],
        "actions": [u"Example: Create an Artifact from Pipl data", u"Example: Pipl search function"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"pipl_person_data"],
        "automatic_tasks": [],
        "scripts": [u"Create Artifact from Pipl Data"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 38.1.71

    Contents:
    - Message Destinations:
        - fn_pipl
    - Functions:
        - pipl_search_function
    - Workflows:
        - example_pipl_search_function
    - Rules:
        - Example: Create an Artifact from Pipl data
        - Example: Pipl search function
    - Data Tables:
        - pipl_person_data
    - Scripts:
        - Create Artifact from Pipl Data
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)