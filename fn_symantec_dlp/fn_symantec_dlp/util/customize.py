# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_symantec_dlp"""

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
    Parameters required reload codegen for the fn_symantec_dlp package
    """
    return {
        "package": u"fn_symantec_dlp",
        "message_destinations": [u"fn_symantec_dlp"],
        "functions": [u"symantec_dlp_get_incident_details", u"symantec_dlp_send_note_to_dlp_incident", u"symantec_dlp_update_incident_status", u"symantec_dlp_upload_binaries"],
        "workflows": [u"sdlp_send_soar_note_to_dlp", u"sdlp_update_incident_status", u"sdlp_upload_binaries", u"sdlp_write_incident_details_to_note"],
        "actions": [u"Symantec DLP: Send SOAR Note to DLP", u"Symantec DLP: Update DLP Incident Status", u"Symantec DLP: Upload Binaries", u"Symantec DLP: Upload Binaries as Artifact", u"Symantec DLP: Write DLP Incident Details to Note"],
        "incident_fields": [u"sdlp_incident_id", u"sdlp_incident_status", u"sdlp_incident_url"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.1"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 40.2.81

    Contents:
    - Message Destinations:
        - fn_symantec_dlp
    - Functions:
        - symantec_dlp_get_incident_details
        - symantec_dlp_send_note_to_dlp_incident
        - symantec_dlp_update_incident_status
        - symantec_dlp_upload_binaries
    - Workflows:
        - sdlp_send_soar_note_to_dlp
        - sdlp_update_incident_status
        - sdlp_upload_binaries
        - sdlp_write_incident_details_to_note
    - Rules:
        - Symantec DLP: Send SOAR Note to DLP
        - Symantec DLP: Update DLP Incident Status
        - Symantec DLP: Upload Binaries
        - Symantec DLP: Upload Binaries as Artifact
        - Symantec DLP: Write DLP Incident Details to Note
    - Incident Fields:
        - sdlp_incident_id
        - sdlp_incident_status
        - sdlp_incident_url
    - Scripts:
        - Convert JSON to rich text v1.1
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)