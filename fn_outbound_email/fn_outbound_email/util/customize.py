# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_outbound_email"""

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
    Parameters required reload codegen for the fn_outbound_email package
    """
    return {
        "package": u"fn_outbound_email",
        "message_destinations": [u"email_outbound"],
        "functions": [u"send_email"],
        "workflows": [u"example_send_incident_email_html", u"example_send_incident_email_text", u"example_send_task_email_html"],
        "actions": [u"Example: Send Incident Email HTML", u"Example: Send Incident Email Text", u"Example: Send Task Email HTML"],
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

    IBM Resilient Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - email_outbound
    - Functions:
        - send_email
    - Workflows:
        - example_send_incident_email_html
        - example_send_incident_email_text
        - example_send_task_email_html
    - Rules:
        - Example: Send Incident Email HTML
        - Example: Send Incident Email Text
        - Example: Send Task Email HTML
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)