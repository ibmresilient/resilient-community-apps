# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_phish_ai"""

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
    Parameters required reload codegen for the fn_phish_ai package
    """
    return {
        "package": u"fn_phish_ai",
        "message_destinations": [u"phish_ai_message_destination"],
        "functions": [u"phish_ai_get_report", u"phish_ai_scan_url"],
        "workflows": [u"example_phishai_scan_url"],
        "actions": [u"Example: Phish.AI URL scan"],
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
        - phish_ai_message_destination
    - Functions:
        - phish_ai_get_report
        - phish_ai_scan_url
    - Workflows:
        - example_phishai_scan_url
    - Rules:
        - Example: Phish.AI URL scan
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)