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
        "functions": [u"fn_symantec_dlp_update_incident"],
        "workflows": [u"sdlp_send_note_to_incident", u"sdlp_set_incident_status"],
        "actions": [u"Example: Symantec DLP - Send a note to a DLP Incident", u"Example: Symantec DLP - Update DLP when this Incident is closed "],
        "incident_fields": [u"sdlp_incident_id", u"sdlp_incident_url"],
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

    IBM Resilient Platform Version: 40.2.81

    Contents:
    - Message Destinations:
        - fn_symantec_dlp
    - Functions:
        - fn_symantec_dlp_update_incident
    - Workflows:
        - sdlp_send_note_to_incident
        - sdlp_set_incident_status
    - Rules:
        - Example: Symantec DLP - Send a note to a DLP Incident
        - Example: Symantec DLP - Update DLP when this Incident is closed 
    - Incident Fields:
        - sdlp_incident_id
        - sdlp_incident_url
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)