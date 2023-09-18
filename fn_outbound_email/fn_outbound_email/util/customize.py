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
        "functions": [u"send_email", u"send_email2"],
        "workflows": [u"example_send_incident_email_html", u"example_send_incident_email_html2", u"example_send_incident_email_text", u"example_send_task_email_html", u"example_send_task_email_html2", u"outbound_email_reply_to_message"],
        "actions": [u"Example: Send Incident Email HTML", u"Example: Send Incident Email HTML2", u"Example: Send Incident Email Text", u"Example: Send Task Email HTML", u"Example: Send Task Email HTML2", u"Outbound Email: Reply to Message"],
        "incident_fields": [u"email_message_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"email_conversations"],
        "automatic_tasks": [],
        "scripts": [u"Save Outbound Email Results"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - email_outbound
    - Functions:
        - send_email
        - send_email2
    - Workflows:
        - example_send_incident_email_html
        - example_send_incident_email_html2
        - example_send_incident_email_text
        - example_send_task_email_html
        - example_send_task_email_html2
        - outbound_email_reply_to_message
    - Rules:
        - Example: Send Incident Email HTML
        - Example: Send Incident Email HTML2
        - Example: Send Incident Email Text
        - Example: Send Task Email HTML
        - Example: Send Task Email HTML2
        - Outbound Email: Reply to Message
    - Incident Fields:
        - email_message_id
    - Data Tables:
        - email_conversations
    - Scripts:
        - Save Outbound Email Results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)