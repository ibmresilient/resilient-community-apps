# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_watsonx_analyst"""

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
    Parameters required reload codegen for the fn_watsonx_analyst package
    """
    return {
        "package": "fn_watsonx_analyst",
        "message_destinations": ["fn_watsonx_analyst"],
        "functions": [
            "fn_watsonx_analyst_converse_via_notes",
            "fn_watsonx_analyst_scan_artifact",
            "fn_watsonx_analyst_text_generation",
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [
            "watsonx.ai Add Artifact Report to Notes",
            "watsonx.ai Respond to note",
        ],
        "playbooks": [
            "fn_watsonx_analyst_note_conversation",
            "fn_watsonx_analyst_retry_note_conversation",
            "fn_watsonx_analyst_scan_artifact",
        ],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.3.2.8

    Contents:
    - Message Destinations:
        - fn_watsonx_analyst
    - Functions:
        - fn_watsonx_analyst_converse_via_notes
        - fn_watsonx_analyst_scan_artifact
        - fn_watsonx_analyst_text_generation
    - Playbooks:
        - fn_watsonx_analyst_note_conversation
        - fn_watsonx_analyst_retry_note_conversation
        - fn_watsonx_analyst_scan_artifact
    - Scripts:
        - watsonx.ai Add Artifact Report to Notes
        - watsonx.ai Respond to note
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode="rt") as f:
        b64_data = base64.b64encode(f.read().encode("utf-8"))
        yield ImportDefinition(b64_data)
