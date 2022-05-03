# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_siemplify"""

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
    Parameters required reload codegen for the fn_siemplify package
    """
    return {
        "package": u"fn_siemplify",
        "message_destinations": [u"fn_siemplify"],
        "functions": [u"siemplify_add_playbook", u"siemplify_addupdate_entity_to_blocklist", u"siemplify_addupdate_entity_to_customlist", u"siemplify_close_case", u"siemplify_get_blocklist_entities", u"siemplify_get_customlist_entities", u"siemplify_remove_list_entry", u"siemplify_sync_artifact", u"siemplify_sync_attachment", u"siemplify_sync_case", u"siemplify_sync_comment", u"siemplify_sync_task"],
        "workflows": [u"siemplify_add_playbook", u"siemplify_addupdate_entity_to_blocklist", u"siemplify_addupdate_entity_to_customlist", u"siemplify_close_case", u"siemplify_get_blocklist_entities", u"siemplify_get_customlist_entities", u"siemplify_m_sync_case", u"siemplify_remove_list_entry", u"siemplify_sync_artifact", u"siemplify_sync_attachment", u"siemplify_sync_case", u"siemplify_sync_comment", u"siemplify_sync_task"],
        "actions": [u"Siemplify Add Playbook", u"Siemplify Auto Close Case", u"Siemplify Auto Sync Artifact", u"Siemplify Auto Sync Attachment", u"Siemplify Auto Sync Case", u"Siemplify Auto Sync Comment", u"Siemplify Remove Blocklist/Custom List Entity", u"Siemplify Sync Artifact", u"Siemplify Sync Case", u"Siemplify Sync Comment", u"Siemplify Sync Task", u"Siemplify: Add/Update Entity to Blocklist", u"Siemplify: Add/Update Entity to Custom List", u"Siemplify: Get Blocklist Entities", u"Siemplify: Get Custom List Entities"],
        "incident_fields": [u"siemplify_alert_id", u"siemplify_assignee", u"siemplify_case_id", u"siemplify_case_link", u"siemplify_environment", u"siemplify_is_important", u"siemplify_priority", u"siemplify_stage", u"siemplify_tags"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"siemplify_list_entries"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.2.41

    Contents:
    - Message Destinations:
        - fn_siemplify
    - Functions:
        - siemplify_add_playbook
        - siemplify_addupdate_entity_to_blocklist
        - siemplify_addupdate_entity_to_customlist
        - siemplify_close_case
        - siemplify_get_blocklist_entities
        - siemplify_get_customlist_entities
        - siemplify_remove_list_entry
        - siemplify_sync_artifact
        - siemplify_sync_attachment
        - siemplify_sync_case
        - siemplify_sync_comment
        - siemplify_sync_task
    - Workflows:
        - siemplify_add_playbook
        - siemplify_addupdate_entity_to_blocklist
        - siemplify_addupdate_entity_to_customlist
        - siemplify_close_case
        - siemplify_get_blocklist_entities
        - siemplify_get_customlist_entities
        - siemplify_m_sync_case
        - siemplify_remove_list_entry
        - siemplify_sync_artifact
        - siemplify_sync_attachment
        - siemplify_sync_case
        - siemplify_sync_comment
        - siemplify_sync_task
    - Rules:
        - Siemplify Add Playbook
        - Siemplify Auto Close Case
        - Siemplify Auto Sync Artifact
        - Siemplify Auto Sync Attachment
        - Siemplify Auto Sync Case
        - Siemplify Auto Sync Comment
        - Siemplify Remove Blocklist/Custom List Entity
        - Siemplify Sync Artifact
        - Siemplify Sync Case
        - Siemplify Sync Comment
        - Siemplify Sync Task
        - Siemplify: Add/Update Entity to Blocklist
        - Siemplify: Add/Update Entity to Custom List
        - Siemplify: Get Blocklist Entities
        - Siemplify: Get Custom List Entities
    - Incident Fields:
        - siemplify_alert_id
        - siemplify_assignee
        - siemplify_case_id
        - siemplify_case_link
        - siemplify_environment
        - siemplify_is_important
        - siemplify_priority
        - siemplify_stage
        - siemplify_tags
    - Data Tables:
        - siemplify_list_entries
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)