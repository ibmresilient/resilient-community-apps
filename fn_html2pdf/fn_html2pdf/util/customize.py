# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_html2pdf"""

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
    Parameters required reload codegen for the fn_html2pdf package
    """
    return {
        "package": u"fn_html2pdf",
        "message_destinations": [u"fn_html2pdf"],
        "functions": [u"fn_html2pdf"],
        "workflows": [u"example_html2pdf"],
        "actions": [u"Example: HTML2PDF"],
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

    IBM Resilient Platform Version: 40.0.6554

    Contents:
    - Message Destinations:
        - fn_html2pdf
    - Functions:
        - fn_html2pdf
    - Workflows:
        - example_html2pdf
    - Rules:
        - Example: HTML2PDF
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)