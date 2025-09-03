# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_email_header_validation"""

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
    Parameters required reload codegen for the fn_email_header_validation package
    """
    return {
        "package": u"fn_email_header_validation",
        "message_destinations": [
            u"fn_email_header_validation"
        ],
        "functions": [
            u"email_header_validation_using_dkimarc"
        ],
        "workflows": [
            u"example_email_header_validation_using_dkimarc_artifact",
            u"example_email_header_validation_using_dkimarc_attachment"
        ],
        "actions": [
            u"Example: Email Header Validation Using DKIM/ARC [Artifact]",
            u"Example: Email Header Validation Using DKIM/ARC [Attachment]"
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
        - fn_email_header_validation
    - Functions:
        - email_header_validation_using_dkimarc
    - Workflows:
        - example_email_header_validation_using_dkimarc_artifact
        - example_email_header_validation_using_dkimarc_attachment
    - Rules:
        - Example: Email Header Validation Using DKIM/ARC [Artifact]
        - Example: Email Header Validation Using DKIM/ARC [Attachment]
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)