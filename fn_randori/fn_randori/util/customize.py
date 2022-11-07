# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_randori"""

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
    Parameters required reload codegen for the fn_randori package
    """
    return {
        "package": u"fn_randori",
        "message_destinations": [u"fn_randori"],
        "functions": [u"randori_clear_data_table", u"randori_get_detections_of_target", u"randori_get_target", u"randori_send_note_as_comment_to_target", u"randori_update_notes_from_randori_target", u"randori_update_target_impact_score", u"randori_update_target_status"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"randori_target_affiliation_state", u"randori_target_authority", u"randori_target_id", u"randori_target_impact_score", u"randori_target_link", u"randori_target_perspective_name", u"randori_target_status", u"randori_target_tags", u"randori_target_tech_category", u"randori_target_temptation"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"randori_detections_dt"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"randori_add_artifacts_of_detections", u"randori_add_detections_to_detections_data_table", u"randori_add_target_notes", u"randori_close_target", u"randori_create_artifacts_from_detection", u"randori_send_soar_note_to_randori_target", u"randori_update_detections_data_table", u"randori_update_target_data_in_soar", u"randori_update_target_impact_score_in_randori", u"randori_update_target_in_soar", u"randori_update_target_notes", u"randori_update_target_status_in_randori"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_randori
    - Functions:
        - randori_clear_data_table
        - randori_get_detections_of_target
        - randori_get_target
        - randori_send_note_as_comment_to_target
        - randori_update_notes_from_randori_target
        - randori_update_target_impact_score
        - randori_update_target_status
    - Playbooks:
        - randori_add_artifacts_of_detections
        - randori_add_detections_to_detections_data_table
        - randori_add_target_notes
        - randori_close_target
        - randori_create_artifacts_from_detection
        - randori_send_soar_note_to_randori_target
        - randori_update_detections_data_table
        - randori_update_target_data_in_soar
        - randori_update_target_impact_score_in_randori
        - randori_update_target_in_soar
        - randori_update_target_notes
        - randori_update_target_status_in_randori
    - Incident Fields:
        - randori_target_affiliation_state
        - randori_target_authority
        - randori_target_id
        - randori_target_impact_score
        - randori_target_link
        - randori_target_perspective_name
        - randori_target_status
        - randori_target_tags
        - randori_target_tech_category
        - randori_target_temptation
    - Data Tables:
        - randori_detections_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)