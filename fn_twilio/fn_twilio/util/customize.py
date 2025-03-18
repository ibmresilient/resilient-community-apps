# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_twilio"""

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
    Parameters required reload codegen for the fn_twilio package
    """
    return {
        "package": u"fn_twilio",
        "message_destinations": [
            u"fn_twilio"
        ],
        "functions": [
            u"twilio_get_responses",
            u"twilio_send_sms"
        ],
        "workflows": [
            u"example_twilio_receive_messages",
            u"example_twilio_send_sms",
            u"twilio_get_responses"
        ],
        "actions": [
            u"Example: Send Twilio SMS",
            u"Example: Twilio Receive Messages",
            u"Twilio: Get Responses"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"twilio_sms_log"
        ],
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
        - fn_twilio
    - Functions:
        - twilio_get_responses
        - twilio_send_sms
    - Workflows:
        - example_twilio_receive_messages
        - example_twilio_send_sms
        - twilio_get_responses
    - Rules:
        - Example: Send Twilio SMS
        - Example: Twilio Receive Messages
        - Twilio: Get Responses
    - Data Tables:
        - twilio_sms_log
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)