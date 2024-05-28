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
        "functions": [u"symantec_dlp_close_dlp_case", u"symantec_dlp_get_incident_details", u"symantec_dlp_get_notes", u"symantec_dlp_send_note_to_dlp_incident", u"symantec_dlp_update_incident", u"symantec_dlp_upload_binaries"],
        "workflows": [u"sdlp_close_dlp_case", u"sdlp_get_notes", u"sdlp_resolve_incident_in_dlp", u"sdlp_send_soar_note_to_dlp", u"sdlp_update_incident", u"sdlp_update_severity_in_dlp", u"sdlp_upload_binaries", u"sdlp_write_incident_details_to_note"],
        "actions": [u"Symantec DLP: Close DLP Case", u"Symantec DLP: Get DLP Notes", u"Symantec DLP: Resolve Incident in DLP", u"Symantec DLP: Send SOAR Note to DLP", u"Symantec DLP: Update DLP Incident", u"Symantec DLP: Update Severity in DLP", u"Symantec DLP: Upload Binaries", u"Symantec DLP: Upload Binaries as Artifact", u"Symantec DLP: Write DLP Incident Details to Note"],
        "incident_fields": [u"sdlp_incident_id", u"sdlp_incident_status", u"sdlp_incident_url", u"sdlp_policy_group_id", u"sdlp_policy_group_name", u"sdlp_policy_id", u"sdlp_policy_name"],
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

    IBM SOAR Platform Version: 42.0.7058

    Contents:
    - Message Destinations:
        - fn_symantec_dlp
    - Functions:
        - symantec_dlp_close_dlp_case
        - symantec_dlp_get_incident_details
        - symantec_dlp_get_notes
        - symantec_dlp_send_note_to_dlp_incident
        - symantec_dlp_update_incident
        - symantec_dlp_upload_binaries
    - Workflows:
        - sdlp_close_dlp_case
        - sdlp_get_notes
        - sdlp_resolve_incident_in_dlp
        - sdlp_send_soar_note_to_dlp
        - sdlp_update_incident
        - sdlp_update_severity_in_dlp
        - sdlp_upload_binaries
        - sdlp_write_incident_details_to_note
    - Rules:
        - Symantec DLP: Close DLP Case
        - Symantec DLP: Get DLP Notes
        - Symantec DLP: Resolve Incident in DLP
        - Symantec DLP: Send SOAR Note to DLP
        - Symantec DLP: Update DLP Incident
        - Symantec DLP: Update Severity in DLP
        - Symantec DLP: Upload Binaries
        - Symantec DLP: Upload Binaries as Artifact
        - Symantec DLP: Write DLP Incident Details to Note
    - Incident Fields:
        - sdlp_incident_id
        - sdlp_incident_status
        - sdlp_incident_url
        - sdlp_policy_group_id
        - sdlp_policy_group_name
        - sdlp_policy_id
        - sdlp_policy_name
    - Scripts:
        - Convert JSON to rich text v1.1
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)