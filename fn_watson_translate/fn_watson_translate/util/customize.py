# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_watson_translate"""

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
    Parameters required reload codegen for the fn_watson_translate package
    """
    return {
        "package": u"fn_watson_translate",
        "message_destinations": [u"fn_watson_queue"],
        "functions": [u"fn_watson_translate"],
        "workflows": [u"watson_translate_note"],
        "actions": [u"Example: Watson Translate Note"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
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
        - fn_watson_queue
    - Functions:
        - fn_watson_translate
    - Workflows:
        - watson_translate_note
    - Rules:
        - Example: Watson Translate Note
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)