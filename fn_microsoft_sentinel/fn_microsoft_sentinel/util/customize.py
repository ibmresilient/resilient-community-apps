# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_microsoft_sentinel"""

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
        "message_destinations": [
            u"fn_microsoft_sentinel"
        ],
        "functions": [
            u"sentinel_add_incident_comment",
            u"sentinel_get_incident_alerts",
            u"sentinel_get_incident_comments",
            u"sentinel_get_incident_entities",
            u"sentinel_update_incident"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"sentinel_incident_assigned_to",
            u"sentinel_incident_classification",
            u"sentinel_incident_classification_comment",
            u"sentinel_incident_classification_reason",
            u"sentinel_incident_id",
            u"sentinel_incident_labels",
            u"sentinel_incident_last_modified_time_utc",
            u"sentinel_incident_last_update",
            u"sentinel_incident_number",
            u"sentinel_incident_status",
            u"sentinel_incident_tactics",
            u"sentinel_incident_url",
            u"sentinel_label",
            u"sentinel_profile"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"sentinel_incident_alerts",
            u"sentinel_incident_entities"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"sentinel_comment_sync",
            u"sentinel_get_incident_alerts",
            u"sentinel_get_incident_comments",
            u"sentinel_get_incident_entities",
            u"sentinel_incident_sync",
            u"sentinel_update_incident"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_microsoft_sentinel
    - Functions:
        - sentinel_add_incident_comment
        - sentinel_get_incident_alerts
        - sentinel_get_incident_comments
        - sentinel_get_incident_entities
        - sentinel_update_incident
    - Playbooks:
        - sentinel_comment_sync
        - sentinel_get_incident_alerts
        - sentinel_get_incident_comments
        - sentinel_get_incident_entities
        - sentinel_incident_sync
        - sentinel_update_incident
    - Incident Fields:
        - sentinel_incident_assigned_to
        - sentinel_incident_classification
        - sentinel_incident_classification_comment
        - sentinel_incident_classification_reason
        - sentinel_incident_id
        - sentinel_incident_labels
        - sentinel_incident_last_modified_time_utc
        - sentinel_incident_number
        - sentinel_incident_status
        - sentinel_incident_tactics
        - sentinel_incident_url
        - sentinel_label
        - sentinel_profile
    - Data Tables:
        - sentinel_incident_alerts
        - sentinel_incident_entities
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)