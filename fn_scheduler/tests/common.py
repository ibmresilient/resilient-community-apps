# -*- coding: utf-8 -*-
"""
common files for tests
"""

def setup_mock_incident(mock_inc, end_date=None, success=True):
    # Configure the mock to return a response with an OK status code.
    if not success:
        mock_inc.return_value = { "success": success }
    else:
        mock_inc.return_value = {
            "dtm": {},
            "cm": {
                "unassigneds": [],
                "total": 0,
                "geo_counts": {}
            },
            "regulators": {
                "ids": []
            },
            "hipaa": {
                "hipaa_adverse": None,
                "hipaa_misused": None,
                "hipaa_acquired": None,
                "hipaa_additional_misuse": None,
                "hipaa_breach": None,
                "hipaa_adverse_comment": None,
                "hipaa_misused_comment": None,
                "hipaa_acquired_comment": None,
                "hipaa_additional_misuse_comment": None,
                "hipaa_breach_comment": None
            },
            "tasks": None,
            "artifacts": None,
            "name": "Integration First Steps",
            "description": "<div class=\"rte\"><div>My first integration</div></div>",
            "phase_id": 1004,
            "inc_training": False,
            "vers": 4,
            "addr": None,
            "city": None,
            "creator": {
                "id": 3,
                "fname": "Resilient",
                "lname": "Sysadmin",
                "display_name": "Resilient Sysadmin",
                "status": "A",
                "email": "a@example.com",
                "last_login": 1571253164111,
                "locked": False,
                "password_changed": False,
                "last_modified_time": 1571253164112,
                "create_date": 1562157359632,
                "is_external": False
            },
            "creator_principal": {
                "id": 3,
                "type": "user",
                "name": "a@example.com",
                "display_name": "Resilient Sysadmin"
            },
            "exposure_type_id": 1,
            "incident_type_ids": [
                20,
                21
            ],
            "reporter": None,
            "state": None,
            "country": None,
            "zip": None,
            "workspace": 1,
            "exposure": 0,
            "org_handle": 201,
            "members": [],
            "negative_pr_likely": None,
            "perms": {
                "read": True,
                "write": True,
                "comment": True,
                "assign": True,
                "close": True,
                "change_members": True,
                "attach_file": True,
                "read_attachments": True,
                "delete_attachments": True,
                "create_milestones": True,
                "list_milestones": True,
                "create_artifacts": True,
                "list_artifacts": True,
                "delete": True,
                "change_workspace": True
            },
            "confirmed": False,
            "task_changes": {
                "added": [],
                "removed": []
            },
            "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
            "data_compromised": None,
            "draft": False,
            "properties": {
                "campaign_name": None,
                "custom_number": 1234,
                "custom_datetime": 1549184706000,
                "custom_one": "new custom field Ḁ ḁ Ḃ ḃ Ḅ ḅ Ḇ ḇ Ḉ ḉ Ḋ ḋ Ḍ ḍ Ḏ ḏ Ḑ ḑ Ḓ",
                "scheduler_demo": None,
                "campaign_task_id": None,
                "messageID": None,
                "proofpoint_trap_incident_id": None,
                "campaign": None,
                "custom_bool": True,
                "campaign_id": None,
                "ansible_value": None
            },
            "resolution_id": None,
            "resolution_summary": None,
            "pii": {
                "data_compromised": None,
                "determined_date": 1546709640000,
                "harmstatus_id": 2,
                "data_encrypted": None,
                "data_contained": None,
                "impact_likely": None,
                "data_source_ids": [],
                "data_format": None,
                "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
                "exposure": 0,
                "gdpr_harm_risk": None,
                "gdpr_lawful_data_processing_categories": [],
                "alberta_health_risk_assessment": None
            },
            "gdpr": {
                "gdpr_breach_circumstances": [],
                "gdpr_breach_type": None,
                "gdpr_personal_data": None,
                "gdpr_identification": None,
                "gdpr_consequences": None,
                "gdpr_final_assessment": None,
                "gdpr_breach_type_comment": None,
                "gdpr_personal_data_comment": None,
                "gdpr_identification_comment": None,
                "gdpr_consequences_comment": None,
                "gdpr_final_assessment_comment": None,
                "gdpr_subsequent_notification": None
            },
            "regulator_risk": {},
            "inc_last_modified_date": 1571253181521,
            "comments": None,
            "actions": [
            ],
            "admin_id": None,
            "creator_id": 3,
            "crimestatus_id": 1,
            "employee_involved": None,
            "end_date": end_date,
            "exposure_dept_id": None,
            "exposure_individual_name": None,
            "exposure_vendor_id": None,
            "jurisdiction_name": None,
            "jurisdiction_reg_id": None,
            "start_date": 1546709640000,
            "inc_start": 1546709640000,
            "org_id": 201,
            "is_scenario": False,
            "hard_liability": 0,
            "nist_attack_vectors": [
                4,
                5
            ],
            "id": 2264,
            "discovered_date": 1546709640000,
            "due_date": None,
            "create_date": 1570797645045,
            "owner_id": 6,
            "severity_code": 55,
            "plan_status": "A"
        }

def setup_mock_actions(mock_rules, enabled=True, object_type=0):

    # Configure the mock to return a response with an OK status code.
    mock_rules.return_value = {
        "entities": [
            {
                "id": 24,
                "name": "Test Rule",
                "type": 0,
                "enabled": enabled,
                "object_type": object_type,
                "conditions": [
                ],
                "automations": [],
                "message_destinations": [],
                "workflows": [
                    6
                ],
                "view_items": [],
                "timeout_seconds": 86400,
                "uuid": "cd0f3596-1082-44f7-ba8d-0c214bb68a65",
                "export_key": "Automatic Campaign Close",
                "logic_type": "all",
                "tags": []
            },
             {
                 "id": 25,
                 "name": "unicode ΞΟΠΡ",
                 "type": 0,
                 "enabled": enabled,
                 "object_type": object_type,
                 "conditions": [
                 ],
                 "automations": [],
                 "message_destinations": [],
                 "workflows": [
                     6
                 ],
                 "view_items": [],
                 "timeout_seconds": 86400,
                 "uuid": "cd0f3596-1082-44f7-ba8d-0c214bb68a66",
                 "export_key": "Automatic Campaign Close",
                 "logic_type": "all",
                 "tags": []
             }
        ]
    }

def setup_evt(evt):
    evt["message"]["workflow"] = {
        "programmatic_name": "list_schedules",
        "tags": [],
        "object_type":
            { "id": 0, "name": "incident" },
        "uuid": None,
        "actions": [],
        "name": "List Schedules",
        "workflow_id": 22,
        "description": None
    }

    evt["message"]["workflow_instance"] = {
        "workflow_instance_id": 435,
        "workflow": {
            "programmatic_name": "list_schedules",
            "tags": [],
            "object_type":
                { "id": 0, "name": "incident" },
            "uuid": None,
            "actions": [],
            "name": "List Schedules",
            "workflow_id": 22,
            "description": None
        }
    }