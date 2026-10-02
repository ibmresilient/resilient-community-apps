# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v52.0.0.0.927

"""Generate the SOAR customizations required for fn_vmware_cbc"""

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
    Parameters required reload codegen for the fn_vmware_cbc package
    """
    return {
        "package": u"fn_vmware_cbc",
        "message_destinations": [
            u"vmware_carbon_black_cloud"
        ],
        "functions": [
            u"vmware_cbc_get_alert_by_id",
            u"vmware_cbc_get_cbc_notes",
            u"vmware_cbc_get_device_by_id",
            u"vmware_cbc_kill_process",
            u"vmware_cbc_post_alert_workflow_data",
            u"vmware_cbc_post_device_action",
            u"vmware_cbc_post_note_to_cbc_alert",
            u"vmware_cbc_post_observations_detail_job",
            u"vmware_cbc_post_reputation_override",
            u"vmware_cbc_post_tags"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"vmware_cbc_alert_id",
            u"vmware_cbc_alert_link",
            u"vmware_cbc_alert_reason_code",
            u"vmware_cbc_alert_type",
            u"vmware_cbc_attack_tactic",
            u"vmware_cbc_determination_value",
            u"vmware_cbc_tags",
            u"vmware_cbc_threat_id",
            u"vmware_cbc_workflow_closure_reason",
            u"vmware_cbc_workflow_status"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"vmware_cbc_device_dt",
            u"vmware_cbc_observations_dt",
            u"vmware_cbc_processes_dt"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Convert JSON to rich text v1.3",
            u"VMware CBC: Populate CBC Device Row from Alert",
            u"VMware CBC: Populate CBC Device Row from Device",
            u"VMware CBC: Populate Observations Data Table"
        ],
        "playbooks": [
            u"vmware_cbc_background_scan_off",
            u"vmware_cbc_background_scan_on",
            u"vmware_cbc_bypass_off",
            u"vmware_cbc_bypass_on",
            u"vmware_cbc_close_alert_on_case_close",
            u"vmware_cbc_kill_process",
            u"vmware_cbc_override_reputation",
            u"vmware_cbc_override_reputation_artifact",
            u"vmware_cbc_post_note_to_cbc_alert",
            u"vmware_cbc_post_tags",
            u"vmware_cbc_quarantine_off",
            u"vmware_cbc_quarantine_on",
            u"vmware_cbc_refetch_device_in_row",
            u"vmware_cbc_update_alert_workflow_data",
            u"vmware_cbc_update_case",
            u"vmware_cbc_update_case_on_creation",
            u"vmware_cbc_update_device_row_from_device",
            u"vmware_cbc_update_observations_dt",
            u"vmware_cbc_write_alert_json_to_note",
            u"vmware_cbc_write_device_json_to_note",
            u"vmware_cbc_write_observations_json_to_note"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 50.0.9097

    Contents:
    - Message Destinations:
        - vmware_carbon_black_cloud
    - Functions:
        - vmware_cbc_get_alert_by_id
        - vmware_cbc_get_cbc_notes
        - vmware_cbc_get_device_by_id
        - vmware_cbc_kill_process
        - vmware_cbc_post_alert_workflow_data
        - vmware_cbc_post_device_action
        - vmware_cbc_post_note_to_cbc_alert
        - vmware_cbc_post_observations_detail_job
        - vmware_cbc_post_reputation_override
        - vmware_cbc_post_tags
    - Playbooks:
        - vmware_cbc_background_scan_off
        - vmware_cbc_background_scan_on
        - vmware_cbc_bypass_off
        - vmware_cbc_bypass_on
        - vmware_cbc_close_alert_on_case_close
        - vmware_cbc_kill_process
        - vmware_cbc_override_reputation
        - vmware_cbc_override_reputation_artifact
        - vmware_cbc_post_note_to_cbc_alert
        - vmware_cbc_post_tags
        - vmware_cbc_quarantine_off
        - vmware_cbc_quarantine_on
        - vmware_cbc_refetch_device_in_row
        - vmware_cbc_update_alert_workflow_data
        - vmware_cbc_update_case
        - vmware_cbc_update_case_on_creation
        - vmware_cbc_update_device_row_from_device
        - vmware_cbc_update_observations_dt
        - vmware_cbc_write_alert_json_to_note
        - vmware_cbc_write_device_json_to_note
        - vmware_cbc_write_observations_json_to_note
    - Incident Fields:
        - vmware_cbc_alert_id
        - vmware_cbc_alert_link
        - vmware_cbc_alert_reason_code
        - vmware_cbc_alert_type
        - vmware_cbc_attack_tactic
        - vmware_cbc_determination_value
        - vmware_cbc_tags
        - vmware_cbc_threat_id
        - vmware_cbc_workflow_closure_reason
        - vmware_cbc_workflow_status
    - Data Tables:
        - vmware_cbc_device_dt
        - vmware_cbc_observations_dt
        - vmware_cbc_processes_dt
    - Scripts:
        - Convert JSON to rich text v1.3
        - VMware CBC: Populate CBC Device Row from Alert
        - VMware CBC: Populate CBC Device Row from Device
        - VMware CBC: Populate Observations Data Table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)