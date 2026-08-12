# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v52.0.0.0.927

"""Generate the SOAR customizations required for fn_cisco_amp4ep"""

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
    Parameters required reload codegen for the fn_cisco_amp4ep package
    """
    return {
        "package": u"fn_cisco_amp4ep",
        "message_destinations": [
            u"fn_cisco_amp"
        ],
        "functions": [
            u"fn_amp_computer_isolation",
            u"fn_amp_delete_file_list_files",
            u"fn_amp_get_activity",
            u"fn_amp_get_computer",
            u"fn_amp_get_computer_trajectory",
            u"fn_amp_get_computers",
            u"fn_amp_get_event_types",
            u"fn_amp_get_events",
            u"fn_amp_get_file_list_files",
            u"fn_amp_get_file_lists",
            u"fn_amp_get_groups",
            u"fn_amp_move_computer",
            u"fn_amp_set_file_list_files"
        ],
        "workflows": [
            u"wf_amp_add_artifact_from_activity",
            u"wf_amp_add_artifact_from_event",
            u"wf_amp_add_artifact_from_trajectory",
            u"wf_amp_delete_file_list_files",
            u"wf_amp_get_activity",
            u"wf_amp_get_computer_by_guid",
            u"wf_amp_get_computer_by_name",
            u"wf_amp_get_computer_refresh",
            u"wf_amp_get_computer_trajectory",
            u"wf_amp_get_computer_trajectory_by_activity",
            u"wf_amp_get_event_types",
            u"wf_amp_get_events",
            u"wf_amp_get_events_by_type",
            u"wf_amp_get_file_list_files",
            u"wf_amp_get_file_lists",
            u"wf_amp_get_group_name_by_guid",
            u"wf_amp_get_groups",
            u"wf_amp_move_computer",
            u"wf_amp_set_file_list_files"
        ],
        "actions": [
            u"Example: AMP add artifact from activity",
            u"Example: AMP add artifact from event",
            u"Example: AMP add artifact from trajectory",
            u"Example: AMP delete file from list",
            u"Example: AMP get computer (refresh)",
            u"Example: AMP get computer by connector guid",
            u"Example: AMP get computer by name",
            u"Example: AMP get computer trajectory",
            u"Example: AMP get computer trajectory by activity",
            u"Example: AMP get computers with activity",
            u"Example: AMP get event types",
            u"Example: AMP get events",
            u"Example: AMP get events by type",
            u"Example: AMP get files from list",
            u"Example: AMP get group name by guid",
            u"Example: AMP get groups",
            u"Example: AMP get SCD file lists",
            u"Example: AMP move computer",
            u"Example: AMP set file in list"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"amp_activity",
            u"amp_computer_trajectory",
            u"amp_computers",
            u"amp_event_types",
            u"amp_events",
            u"amp_file_list_files",
            u"amp_groups",
            u"amp_scd_file_lists"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"scr_amp_add_artifact_from_activity",
            u"scr_amp_add_artifact_from_event",
            u"scr_amp_add_artifact_from_trajectory"
        ],
        "playbooks": [
            u"amp_computer_isolation"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 50.0.9097

    Contents:
    - Message Destinations:
        - fn_cisco_amp
    - Functions:
        - fn_amp_computer_isolation
        - fn_amp_delete_file_list_files
        - fn_amp_get_activity
        - fn_amp_get_computer
        - fn_amp_get_computer_trajectory
        - fn_amp_get_computers
        - fn_amp_get_event_types
        - fn_amp_get_events
        - fn_amp_get_file_list_files
        - fn_amp_get_file_lists
        - fn_amp_get_groups
        - fn_amp_move_computer
        - fn_amp_set_file_list_files
    - Workflows:
        - wf_amp_add_artifact_from_activity
        - wf_amp_add_artifact_from_event
        - wf_amp_add_artifact_from_trajectory
        - wf_amp_delete_file_list_files
        - wf_amp_get_activity
        - wf_amp_get_computer_by_guid
        - wf_amp_get_computer_by_name
        - wf_amp_get_computer_refresh
        - wf_amp_get_computer_trajectory
        - wf_amp_get_computer_trajectory_by_activity
        - wf_amp_get_event_types
        - wf_amp_get_events
        - wf_amp_get_events_by_type
        - wf_amp_get_file_list_files
        - wf_amp_get_file_lists
        - wf_amp_get_group_name_by_guid
        - wf_amp_get_groups
        - wf_amp_move_computer
        - wf_amp_set_file_list_files
    - Playbooks:
        - amp_computer_isolation
    - Rules:
        - Example: AMP add artifact from activity
        - Example: AMP add artifact from event
        - Example: AMP add artifact from trajectory
        - Example: AMP delete file from list
        - Example: AMP get computer (refresh)
        - Example: AMP get computer by connector guid
        - Example: AMP get computer by name
        - Example: AMP get computer trajectory
        - Example: AMP get computer trajectory by activity
        - Example: AMP get computers with activity
        - Example: AMP get event types
        - Example: AMP get events
        - Example: AMP get events by type
        - Example: AMP get files from list
        - Example: AMP get group name by guid
        - Example: AMP get groups
        - Example: AMP get SCD file lists
        - Example: AMP move computer
        - Example: AMP set file in list
    - Data Tables:
        - amp_activity
        - amp_computer_trajectory
        - amp_computers
        - amp_event_types
        - amp_events
        - amp_file_list_files
        - amp_groups
        - amp_scd_file_lists
    - Scripts:
        - scr_amp_add_artifact_from_activity
        - scr_amp_add_artifact_from_event
        - scr_amp_add_artifact_from_trajectory
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)