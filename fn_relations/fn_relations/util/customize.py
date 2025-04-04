# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.0.2.575

"""Generate the SOAR customizations required for fn_relations"""

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
    Parameters required reload codegen for the fn_relations package
    """
    return {
        "package": u"fn_relations",
        "message_destinations": [
            u"fn_relations"
        ],
        "functions": [
            u"relations_assign_parent",
            u"relations_auto_close_child_incidents",
            u"relations_copy_task",
            u"relations_remove_child_relation",
            u"relations_sync_artifact",
            u"relations_sync_child_table_data",
            u"relations_sync_datatable_data",
            u"relations_sync_notes",
            u"relations_sync_task_notes"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"relations_level",
            u"relations_parent_id"
        ],
        "incident_artifact_types": [
            u"related_parent_incident"
        ],
        "incident_types": [],
        "datatables": [
            u"dt_relations_child_incidents"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"relations_assign_parent_incident",
            u"relations_auto_close_child_incidents",
            u"relations_copy_task_to_children",
            u"relations_remove_child_relation",
            u"relations_sync_artifact",
            u"relations_sync_datatable_data",
            u"relations_sync_note_to_children",
            u"relations_sync_notes_to_parent",
            u"relations_sync_task_note_to_children",
            u"relations_sync_task_notes_to_parent",
            u"relations_update_child_table_data"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 48.2.16

    Contents:
    - Message Destinations:
        - fn_relations
    - Functions:
        - relations_assign_parent
        - relations_auto_close_child_incidents
        - relations_copy_task
        - relations_remove_child_relation
        - relations_sync_artifact
        - relations_sync_child_table_data
        - relations_sync_datatable_data
        - relations_sync_notes
        - relations_sync_task_notes
    - Playbooks:
        - relations_assign_parent_incident
        - relations_auto_close_child_incidents
        - relations_copy_task_to_children
        - relations_remove_child_relation
        - relations_sync_artifact
        - relations_sync_datatable_data
        - relations_sync_note_to_children
        - relations_sync_notes_to_parent
        - relations_sync_task_note_to_children
        - relations_sync_task_notes_to_parent
        - relations_update_child_table_data
    - Incident Fields:
        - relations_level
        - relations_parent_id
    - Custom Artifact Types:
        - related_parent_incident
    - Data Tables:
        - dt_relations_child_incidents
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)