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
        "functions": [u"sentinel_update_incident", u"sentinel_get_incident_entities", u"sentinel_get_incident_comments", u"sentinel_add_incident_comment"],
        "workflows": [u"sentinel_update_incident", u"sentinel_get_incident_entities", u"sentinel_comment_sync", u"sentinel_get_incident_comments"],
        "actions": [u"Sentinel Comment Sync", u"Sentinel Get Incident Entities", u"Sentinel Update Incident", u"Sentinel Get Incident Comments", u"Sentinel Incident Entity Sync"],
        "incident_fields": [u"sentinel_incident_url", u"sentinel_incident_classification", u"sentinel_incident_classification_comment", u"sentinel_incident_id", u"sentinel_incident_labels", u"sentinel_incident_classification_reason", u"sentinel_incident_status", u"sentinel_profile", u"sentinel_incident_tactics", u"sentinel_incident_assigned_to"],
        "incident_artifact_types": [],
        "datatables": [u"sentinel_incident_entities", u"sentinel_comment_ids"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 37.2.38

    Contents:
    - Message Destinations:
        - fn_microsoft_sentinel
    - Functions:
        - sentinel_update_incident
        - sentinel_get_incident_entities
        - sentinel_get_incident_comments
        - sentinel_add_incident_comment
    - Workflows:
        - sentinel_update_incident
        - sentinel_get_incident_entities
        - sentinel_comment_sync
        - sentinel_get_incident_comments
    - Rules:
        - Sentinel Comment Sync
        - Sentinel Get Incident Entities
        - Sentinel Update Incident
        - Sentinel Get Incident Comments
        - Sentinel Incident Entity Sync
    - Incident Fields:
        - sentinel_incident_url
        - sentinel_incident_classification
        - sentinel_incident_classification_comment
        - sentinel_incident_id
        - sentinel_incident_labels
        - sentinel_incident_classification_reason
        - sentinel_incident_status
        - sentinel_profile
        - sentinel_incident_tactics
        - sentinel_incident_assigned_to
    - Data Tables:
        - sentinel_incident_entities
        - sentinel_comment_ids
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)