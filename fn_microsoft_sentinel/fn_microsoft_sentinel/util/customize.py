# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_microsoft_sentinel"""

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
    Parameters required reload codegen for the fn_microsoft_sentinel package
    """
    return {
        "package": u"fn_microsoft_sentinel",
        "message_destinations": [u"fn_microsoft_sentinel"],
        "functions": [u"sentinel_add_incident_comment", u"sentinel_get_incident_comments", u"sentinel_get_incident_entities", u"sentinel_update_incident"],
        "workflows": [u"sentinel_comment_sync", u"sentinel_get_incident_comments", u"sentinel_get_incident_entities", u"sentinel_update_incident"],
        "actions": [u"Sentinel Comment Sync", u"Sentinel Get Incident Comments", u"Sentinel Get Incident Entities", u"Sentinel Incident Entity Sync", u"Sentinel Update Incident"],
        "incident_fields": [u"sentinel_incident_assigned_to", u"sentinel_incident_classification", u"sentinel_incident_classification_comment", u"sentinel_incident_classification_reason", u"sentinel_incident_id", u"sentinel_incident_labels", u"sentinel_incident_number", u"sentinel_incident_status", u"sentinel_incident_tactics", u"sentinel_incident_url", u"sentinel_profile"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"sentinel_comment_ids", u"sentinel_incident_entities"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

    Contents:
    - Message Destinations:
        - fn_microsoft_sentinel
    - Functions:
        - sentinel_add_incident_comment
        - sentinel_get_incident_comments
        - sentinel_get_incident_entities
        - sentinel_update_incident
    - Workflows:
        - sentinel_comment_sync
        - sentinel_get_incident_comments
        - sentinel_get_incident_entities
        - sentinel_update_incident
    - Rules:
        - Sentinel Comment Sync
        - Sentinel Get Incident Comments
        - Sentinel Get Incident Entities
        - Sentinel Incident Entity Sync
        - Sentinel Update Incident
    - Incident Fields:
        - sentinel_incident_assigned_to
        - sentinel_incident_classification
        - sentinel_incident_classification_comment
        - sentinel_incident_classification_reason
        - sentinel_incident_id
        - sentinel_incident_labels
        - sentinel_incident_number
        - sentinel_incident_status
        - sentinel_incident_tactics
        - sentinel_incident_url
        - sentinel_profile
    - Data Tables:
        - sentinel_comment_ids
        - sentinel_incident_entities
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)