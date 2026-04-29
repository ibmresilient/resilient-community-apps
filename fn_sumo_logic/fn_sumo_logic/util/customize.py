# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_sumo_logic"""

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
    Parameters required reload codegen for the fn_sumo_logic package
    """
    return {
        "package": u"fn_sumo_logic",
        "message_destinations": [
            u"fn_sumo_logic"
        ],
        "functions": [
            u"sumo_logic_add_comment_to_insight",
            u"sumo_logic_add_tag_to_insight",
            u"sumo_logic_get_entity",
            u"sumo_logic_get_insight_by_id",
            u"sumo_logic_get_insights_comments",
            u"sumo_logic_get_signal_by_id",
            u"sumo_logic_update_insight_status"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"sumo_logic_insight_assignee",
            u"sumo_logic_insight_global_confidence",
            u"sumo_logic_insight_id",
            u"sumo_logic_insight_link",
            u"sumo_logic_insight_readable_id",
            u"sumo_logic_insight_resolution",
            u"sumo_logic_insight_source",
            u"sumo_logic_insight_status",
            u"sumo_logic_insight_sub_resolution",
            u"sumo_logic_insight_tags"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"sumo_logic_insight_signals_dt"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Convert JSON to rich text v1.3",
            u"Sumo Logic: Add Artifacts from Insight",
            u"Sumo Logic: Populate Signals Data Table"
        ],
        "playbooks": [
            u"sumo_logic_add_comment_to_insight",
            u"sumo_logic_add_tag_to_insight",
            u"sumo_logic_close_insight_on_case_close",
            u"sumo_logic_scan_artifact_for_hits",
            u"sumo_logic_scan_artifact_for_hits_automatic",
            u"sumo_logic_update_case",
            u"sumo_logic_update_case_on_creation",
            u"sumo_logic_update_insight_status",
            u"sumo_logic_write_entity_json_to_note",
            u"sumo_logic_write_insight_json_to_note",
            u"sumo_logic_write_signal_json_to_note"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_sumo_logic
    - Functions:
        - sumo_logic_add_comment_to_insight
        - sumo_logic_add_tag_to_insight
        - sumo_logic_get_entity
        - sumo_logic_get_insight_by_id
        - sumo_logic_get_insights_comments
        - sumo_logic_get_signal_by_id
        - sumo_logic_update_insight_status
    - Playbooks:
        - sumo_logic_add_comment_to_insight
        - sumo_logic_add_tag_to_insight
        - sumo_logic_close_insight_on_case_close
        - sumo_logic_scan_artifact_for_hits
        - sumo_logic_scan_artifact_for_hits_automatic
        - sumo_logic_update_case
        - sumo_logic_update_case_on_creation
        - sumo_logic_update_insight_status
        - sumo_logic_write_entity_json_to_note
        - sumo_logic_write_insight_json_to_note
        - sumo_logic_write_signal_json_to_note
    - Incident Fields:
        - sumo_logic_insight_assignee
        - sumo_logic_insight_global_confidence
        - sumo_logic_insight_id
        - sumo_logic_insight_link
        - sumo_logic_insight_readable_id
        - sumo_logic_insight_resolution
        - sumo_logic_insight_source
        - sumo_logic_insight_status
        - sumo_logic_insight_sub_resolution
        - sumo_logic_insight_tags
    - Data Tables:
        - sumo_logic_insight_signals_dt
    - Scripts:
        - Convert JSON to rich text v1.3
        - Sumo Logic: Add Artifacts from Insight
        - Sumo Logic: Populate Signals Data Table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)