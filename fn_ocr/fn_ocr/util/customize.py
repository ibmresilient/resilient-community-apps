# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ocr"""

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
    Parameters required reload codegen for the fn_ocr package
    """
    return {
        "package": "fn_ocr",
        "message_destinations": ["fn_ocr"],
        "functions": ["fn_ocr"],
        "workflows": [
            "ocr_parse_image",
            "ocr_parse_image_attachment",
            "ocr_parse_image_base64",
        ],
        "actions": [
            "Parse Image (Artifact)",
            "Parse Image (Attachment)",
            "Parse Image (Base64)",
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

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - fn_ocr
    - Functions:
        - fn_ocr
    - Workflows:
        - ocr_parse_image
        - ocr_parse_image_attachment
        - ocr_parse_image_base64
    - Rules:
        - Parse Image (Artifact)
        - Parse Image (Attachment)
        - Parse Image (Base64)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode="rt") as f:
        b64_data = base64.b64encode(f.read().encode("utf-8"))
        yield ImportDefinition(b64_data)
