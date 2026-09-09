# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.6.0.1543

"""Generate the SOAR customizations required for fn_ocm"""

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
    Parameters required reload codegen for the fn_ocm package
    """
    return {
        "package": u"fn_ocm",
        "message_destinations": [
            u"fn_ocm"
        ],
        "functions": [
            u"on_call_manager_create_comment",
            u"on_call_manager_create_event",
            u"on_call_manager_get_event",
            u"on_call_manager_get_incident",
            u"on_call_manager_list_incidents",
            u"on_call_manager_query_incidents",
            u"on_call_manager_update_incident"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"ocm_incident_assigned_owner",
            u"ocm_incident_assigned_team",
            u"ocm_incident_description",
            u"ocm_incident_display_id",
            u"ocm_incident_id",
            u"ocm_incident_last_changed_time",
            u"ocm_incident_priority",
            u"ocm_incident_state",
            u"ocm_incident_summary",
            u"ocm_tab_visible"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"on_call_manager_incidents"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"on_call_manager_create_comment",
            u"on_call_manager_create_event",
            u"on_call_manager_get_incident",
            u"on_call_manager_list_incidents",
            u"on_call_manager_query_incidents",
            u"on_call_manager_sync_incident",
            u"on_call_manager_sync_incident_datatable",
            u"on_call_manager_update_incident"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_ocm
    - Functions:
        - on_call_manager_create_comment
        - on_call_manager_create_event
        - on_call_manager_get_event
        - on_call_manager_get_incident
        - on_call_manager_list_incidents
        - on_call_manager_query_incidents
        - on_call_manager_update_incident
    - Playbooks:
        - on_call_manager_create_comment
        - on_call_manager_create_event
        - on_call_manager_get_incident
        - on_call_manager_list_incidents
        - on_call_manager_query_incidents
        - on_call_manager_sync_incident
        - on_call_manager_sync_incident_datatable
        - on_call_manager_update_incident
    - Incident Fields:
        - ocm_incident_assigned_owner
        - ocm_incident_assigned_team
        - ocm_incident_description
        - ocm_incident_display_id
        - ocm_incident_id
        - ocm_incident_last_changed_time
        - ocm_incident_priority
        - ocm_incident_state
        - ocm_incident_summary
        - ocm_tab_visible
    - Data Tables:
        - on_call_manager_incidents
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)