# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""Generate the Resilient customizations required for fn_relations"""

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
        "message_destinations": [u"fn_relations"],
        "functions": [u"relations_assign_parent", u"relations_auto_close_child_incidents", u"relations_copy_task", u"relations_remove_child_relation", u"relations_sync_artifact", u"relations_sync_child_table_data", u"relations_sync_datatable_data", u"relations_sync_notes", u"relations_sync_task_notes"],
        "workflows": [u"example_relations_assign_parent", u"example_relations_auto_close_child_incidents", u"example_relations_remove_child_relation", u"example_relations_send_task_to_children", u"example_relations_sync_artifact_to_parentchild", u"example_relations_sync_datatable_data_to_parentchild", u"example_relations_sync_notes_to_parentchild", u"example_relations_sync_task_notes_to_parentchild", u"example_relations_update_child_table_data"],
        "actions": [u"Example: Relations - Assign Parent Incident", u"Example: Relations - Close Child Incidents", u"Example: Relations - Remove Child Relation", u"Example: Relations - Send Task to Children", u"Example: Relations - Sync Artifact", u"Example: Relations - Sync DataTable Data", u"Example: Relations - Sync Notes with Child", u"Example: Relations - Sync Notes with Parent", u"Example: Relations - Sync Task Note to Child", u"Example: Relations - Sync Task Notes to Parent", u"Example: Relations - Update Child Incident Parent Data Table"],
        "incident_fields": [u"relations_level", u"relations_parent_id"],
        "incident_artifact_types": [u"related_parent_incident"],
        "incident_types": [],
        "datatables": [u"dt_relations_child_incidents"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

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
    - Workflows:
        - example_relations_assign_parent
        - example_relations_auto_close_child_incidents
        - example_relations_remove_child_relation
        - example_relations_send_task_to_children
        - example_relations_sync_artifact_to_parentchild
        - example_relations_sync_datatable_data_to_parentchild
        - example_relations_sync_notes_to_parentchild
        - example_relations_sync_task_notes_to_parentchild
        - example_relations_update_child_table_data
    - Rules:
        - Example: Relations - Assign Parent Incident
        - Example: Relations - Close Child Incidents
        - Example: Relations - Remove Child Relation
        - Example: Relations - Send Task to Children
        - Example: Relations - Sync Artifact
        - Example: Relations - Sync DataTable Data
        - Example: Relations - Sync Notes with Child
        - Example: Relations - Sync Notes with Parent
        - Example: Relations - Sync Task Note to Child
        - Example: Relations - Sync Task Notes to Parent
        - Example: Relations - Update Child Incident Parent Data Table
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