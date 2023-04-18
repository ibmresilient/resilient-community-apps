{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "List Scheduled Jobs",
      "id": 39,
      "logic_type": "all",
      "message_destinations": [],
      "name": "List Scheduled Jobs",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5cd4cad0-f107-46a0-908c-fa64cd1c0339",
      "view_items": [
        {
          "content": "7a838713-7898-448a-890e-ebf41c7027bc",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "list_schedules"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.schedule_label",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.status",
          "method": "not_contains",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Modify a Scheduled Job",
      "id": 40,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Modify a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ffe8e980-04ed-4c94-aa80-899d898ac184",
      "view_items": [
        {
          "content": "ed50ff7e-c00f-426f-a05c-d5322ae41d78",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1773619f-c839-49db-9782-1dc5f740a2e4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8cbf075b-fba3-4633-827e-b99332d48155",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "modify_a_scheduled_rule"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Pause a Scheduled Job",
      "id": 41,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Pause a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fb04636a-0f1b-48f5-a07f-cb0f954a59f7",
      "view_items": [],
      "workflows": [
        "pause_a_scheduled_job"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Remove a Scheduled Job",
      "id": 42,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Remove a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d8417a45-27da-49df-b1fc-2aeba092b683",
      "view_items": [],
      "workflows": [
        "remove_a_schedule"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.status",
          "method": "contains",
          "type": null,
          "value": "Paused"
        }
      ],
      "enabled": true,
      "export_key": "Resume a Scheduled Job",
      "id": 43,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Resume a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f42ed3be-b4dd-44c8-afdd-831a36365cc8",
      "view_items": [],
      "workflows": [
        "resume_a_scheduled_job"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.schedule_label",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "scheduler_rules.status",
          "method": "not_contains",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Run Scheduled Job Now",
      "id": 44,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Run Scheduled Job Now",
      "object_type": "scheduler_rules",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7c4dad59-aad3-460b-b0fc-0f87d1d6229f",
      "view_items": [],
      "workflows": [
        "run_a_scheduled_job_now"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Schedule a Rule/Playbook to Run",
      "id": 45,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule/Playbook to Run",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9fbe41f6-f6cc-4cdf-aabd-314cb9f99d8f",
      "view_items": [
        {
          "content": "d5741a0f-b6ce-43a4-a158-a19989559cfe",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db501928-ffbb-4e2d-8e46-a3dab6eba44c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cac3d9af-41de-4751-b22f-1349efd5d456",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3fa20ee-307b-42a0-a039-b63807ea4063",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8cbf075b-fba3-4633-827e-b99332d48155",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f020bbc2-e230-4dbc-b5ef-1fd6577aba51",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "schedule_rule_to_run"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Schedule a Rule/Playbook to Run - Artifact",
      "id": 46,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule/Playbook to Run - Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ea9cee60-54bb-4500-af73-fe9fdae770c9",
      "view_items": [
        {
          "content": "d5741a0f-b6ce-43a4-a158-a19989559cfe",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db501928-ffbb-4e2d-8e46-a3dab6eba44c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cac3d9af-41de-4751-b22f-1349efd5d456",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3fa20ee-307b-42a0-a039-b63807ea4063",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8cbf075b-fba3-4633-827e-b99332d48155",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f020bbc2-e230-4dbc-b5ef-1fd6577aba51",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "schedule_a_rule_to_run_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Schedule a Rule/Playbook to Run - Task",
      "id": 47,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule/Playbook to Run - Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "69046ab3-db61-4feb-9f10-f09a823830f9",
      "view_items": [
        {
          "content": "d5741a0f-b6ce-43a4-a158-a19989559cfe",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db501928-ffbb-4e2d-8e46-a3dab6eba44c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cac3d9af-41de-4751-b22f-1349efd5d456",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3fa20ee-307b-42a0-a039-b63807ea4063",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8cbf075b-fba3-4633-827e-b99332d48155",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f020bbc2-e230-4dbc-b5ef-1fd6577aba51",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "schedule_a_rule_to_run__task"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1681825198788,
  "export_format_version": 2,
  "export_type": null,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/object_id",
      "hide_notification": false,
      "id": 696,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "object_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "object_id",
      "tooltip": "ID for task, artifact, attachment, etc.",
      "type_id": 11,
      "uuid": "8690362f-626a-4c93-a68e-c2fb3b746003",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_label_prefix",
      "hide_notification": false,
      "id": 697,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_label_prefix",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_label_prefix",
      "tooltip": "Label to reference created schedule",
      "type_id": 11,
      "uuid": "a5074a34-6d40-4d03-8bf0-a8ad65b31f59",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_label",
      "hide_notification": false,
      "id": 698,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_label",
      "tooltip": "Scheduled job name for identification",
      "type_id": 11,
      "uuid": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/modify_scheduler_type_value",
      "hide_notification": false,
      "id": 699,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "modify_scheduler_type_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "interval, date (yyyy/mm/dd hh:mm:ss) or cron value",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "modify_scheduler_type_value",
      "tooltip": "interval, date (yyyy/mm/dd hh:mm:ss) or cron value",
      "type_id": 11,
      "uuid": "b5ca3be1-0c84-4898-b1f6-2015eb753e1c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_rule_name",
      "hide_notification": false,
      "id": 700,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_rule_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_rule_name",
      "tooltip": "Name of rule to schedule",
      "type_id": 11,
      "uuid": "bfacefb1-5b39-4e7f-919c-84ccc54442f0",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/modify_scheduler_type",
      "hide_notification": false,
      "id": 701,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "modify_scheduler_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "modify_scheduler_type",
      "tooltip": "interval, date (yyyy/mm/dd hh:mm:ss) or cron value",
      "type_id": 11,
      "uuid": "0aeb9039-7eae-49d6-81d8-369ebb401019",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "cron",
          "properties": null,
          "uuid": "bee7db2c-6675-4d5d-8ff8-ce2ddfae603b",
          "value": 112
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "6d59cc69-8499-423e-90bf-5e482e7464a1",
          "value": 113
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "3540303a-bf3f-4d73-842b-eb9f6ed183e2",
          "value": 114
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "a9a054e3-9e75-4761-ad57-3258ae46102a",
          "value": 115
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_type",
      "hide_notification": false,
      "id": 702,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_type",
      "tooltip": "type of schedule to create",
      "type_id": 11,
      "uuid": "0e1330b2-0b91-462b-acf2-2772a02299f8",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "cron",
          "properties": null,
          "uuid": "eb8f0588-a416-4bf9-9154-665ed20bcdf9",
          "value": 116
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "422ba5d3-1f82-4199-bb51-773cfd56dedb",
          "value": 117
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "ff3beed4-6f48-43fd-b5d4-c389e76c4d2f",
          "value": 118
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "f1289cbb-b0ff-4027-a6f8-af40bb474910",
          "value": 119
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_rule_parameters",
      "hide_notification": false,
      "id": 703,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_rule_parameters",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_rule_parameters",
      "tooltip": "Optional parameters in json format for rule",
      "type_id": 11,
      "uuid": "4d308c31-9056-4d34-b977-99d58f89076c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/row_id",
      "hide_notification": false,
      "id": 704,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "row_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "row_id",
      "tooltip": "row information for datatable rules",
      "type_id": 11,
      "uuid": "5ad21089-a73c-4408-ae52-d636e154351c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 705,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Resilient Incident ID",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "IncidentID",
      "type_id": 11,
      "uuid": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_type_value",
      "hide_notification": false,
      "id": 706,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_type_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_type_value",
      "tooltip": "interval, date (yyyy/mm/dd hh:mm:ss) or cron value",
      "type_id": 11,
      "uuid": "6742aa35-eb76-4fa4-85f8-a86015cf888a",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/scheduler_is_playbook",
      "hide_notification": false,
      "id": 707,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "scheduler_is_playbook",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "scheduler_is_playbook",
      "tooltip": "true - playbook, false - rule",
      "type_id": 11,
      "uuid": "6b4b65f3-a243-48b5-8fea-e412bf2cf9f7",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_rule_parameters",
      "hide_notification": false,
      "id": 687,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_rule_parameters",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Rule Parameters",
      "tooltip": "field1=value;field2=value format of optional rule parameters",
      "type_id": 6,
      "uuid": "8cbf075b-fba3-4633-827e-b99332d48155",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_rule_name",
      "hide_notification": false,
      "id": 688,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_rule_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Rule Name",
      "tooltip": "Name of Rule to schedule",
      "type_id": 6,
      "uuid": "cac3d9af-41de-4751-b22f-1349efd5d456",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_is_playbook",
      "hide_notification": false,
      "id": 689,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_is_playbook",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Is Playbook",
      "tooltip": "Yes - Playbook, No - Rule",
      "type_id": 6,
      "uuid": "d3fa20ee-307b-42a0-a039-b63807ea4063",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_type",
      "hide_notification": false,
      "id": 690,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Type",
      "tooltip": "Type of schedule to create",
      "type_id": 6,
      "uuid": "d5741a0f-b6ce-43a4-a158-a19989559cfe",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "cron",
          "properties": null,
          "uuid": "4dc8293e-0937-4130-b1cf-b501bb0d7afe",
          "value": 102
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "2712d0fe-9a1d-4c9d-8fd0-47490c6ec11d",
          "value": 103
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "19dbfc0f-ce1d-49ea-a11b-c0de3fec5e5f",
          "value": 104
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "29774e73-d19c-4c24-b41b-8ebcf27f2c53",
          "value": 105
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_type_value",
      "hide_notification": false,
      "id": 691,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_type_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "cron (* 5 * * *); date (yyyy/mm/dd hh:mm:ss) ; interval (10m)",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Type Value",
      "tooltip": "cron (* 5 * * *); date (yyyy-mm-dd hh:mm:ss) ; interval (10m)",
      "type_id": 6,
      "uuid": "db501928-ffbb-4e2d-8e46-a3dab6eba44c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/modify_schedule_type",
      "hide_notification": false,
      "id": 692,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "modify_schedule_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Type",
      "tooltip": "",
      "type_id": 6,
      "uuid": "ed50ff7e-c00f-426f-a05c-d5322ae41d78",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "cron",
          "properties": null,
          "uuid": "7815a1cd-57de-4db9-a933-aacaf4270c33",
          "value": 106
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "0411052b-0a17-4eb2-a611-3a262e9fbc78",
          "value": 107
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "44cb090b-6edc-4f3d-bcc2-e6df42b4c3eb",
          "value": 108
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "3305bb0a-d67d-4de9-a847-a0f7b9892d2c",
          "value": 109
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/schedule_label_prefix",
      "hide_notification": false,
      "id": 693,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "schedule_label_prefix",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Label Prefix",
      "tooltip": "name of schedule for future reference",
      "type_id": 6,
      "uuid": "f020bbc2-e230-4dbc-b5ef-1fd6577aba51",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/modify_schedule_type_value",
      "hide_notification": false,
      "id": 694,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "modify_schedule_type_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "cron (* 5 * * *); date (yyyy-mm-dd hh:mm:ss) ; interval (10m)",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Schedule Type Value",
      "tooltip": "cron (* 5 * * *); date (yyyy-mm-dd hh:mm:ss) ; interval (10m)",
      "type_id": 6,
      "uuid": "1773619f-c839-49db-9782-1dc5f740a2e4",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/incidents_returned",
      "hide_notification": false,
      "id": 695,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "incidents_returned",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Incidents Returned",
      "tooltip": "",
      "type_id": 6,
      "uuid": "7a838713-7898-448a-890e-ebf41c7027bc",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "All",
          "properties": null,
          "uuid": "aadd559b-9d5f-46f9-a807-30ee758f28de",
          "value": 110
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "This incident only",
          "properties": null,
          "uuid": "43a22bb9-7079-4901-8b1c-c235e13e7375",
          "value": 111
        }
      ]
    },
    {
      "export_key": "incident/internal_customizations_field",
      "id": 0,
      "input_type": "text",
      "internal": true,
      "name": "internal_customizations_field",
      "read_only": true,
      "text": "Customizations Field (internal)",
      "type_id": 0,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa1"
    }
  ],
  "functions": [
    {
      "created_date": 1681402927400,
      "description": {
        "content": "Schedule a rule to run on a schedule. This rule will be executed for a given incident, artifact, task, etc.",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Create",
      "export_key": "create_a_scheduled_rule",
      "id": 7,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927439,
      "name": "create_a_scheduled_rule",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"version\": 1, \"id\": \"domain2-5640\", \"func\": \"fn_scheduler.components.create_a_scheduled_rule:triggered_job\", \"trigger\": null, \"executor\": \"default\", \"args\": [5640, null, null, \"domain2-5640\", \"test scheduled rule\", 212, 0, {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, null, {\"timezone\": \"America/New_York\", \"thread_max\": \"20\", \"datastore_dir\": \"/tmp/scheduler.sqlite\"}], \"kwargs\": {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, \"name\": \"triggered_job\", \"misfire_grace_time\": 1, \"coalesce\": false, \"max_instances\": 1, \"next_run_time\": \"Apr 27 2022 05:00AM\"}, \"raw\": \"{\\\"version\\\": 1, \\\"id\\\": \\\"domain2-5640\\\", \\\"func\\\": \\\"fn_scheduler.components.create_a_scheduled_rule:triggered_job\\\", \\\"trigger\\\": null, \\\"executor\\\": \\\"default\\\", \\\"args\\\": [5640, null, null, \\\"domain2-5640\\\", \\\"test scheduled rule\\\", 212, 0, {\\\"artifact_value\\\": \\\"abc.com\\\", \\\"artifact_type\\\": \\\"domain\\\"}, null, {\\\"timezone\\\": \\\"America/New_York\\\", \\\"thread_max\\\": \\\"20\\\", \\\"datastore_dir\\\": \\\"/tmp/scheduler.sqlite\\\"}], \\\"kwargs\\\": {\\\"artifact_value\\\": \\\"abc.com\\\", \\\"artifact_type\\\": \\\"domain\\\"}, \\\"name\\\": \\\"triggered_job\\\", \\\"misfire_grace_time\\\": 1, \\\"coalesce\\\": false, \\\"max_instances\\\": 1, \\\"next_run_time\\\": \\\"Apr 27 2022 05:00AM\\\"}\", \"inputs\": {\"scheduler_type_value\": \"* 5 * * *\", \"incident_id\": 5640, \"scheduler_type\": {\"id\": 2109, \"name\": \"cron\"}, \"scheduler_label_prefix\": \"domain2\", \"scheduler_rule_name\": \"test scheduled rule\", \"scheduler_rule_parameters\": \"artifact_value=abc.com;artifact_type=domain\", \"scheduler_is_playbook\": false}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 21, \"timestamp\": \"2022-04-26 08:38:13\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"integer\"}, \"id\": {\"type\": \"string\"}, \"func\": {\"type\": \"string\"}, \"trigger\": {}, \"executor\": {\"type\": \"string\"}, \"args\": {\"type\": \"array\", \"items\": {\"anyOf\": [{\"type\": [\"integer\", \"null\", \"string\"]}, {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"thread_max\": {\"type\": \"string\"}, \"datastore_dir\": {\"type\": \"string\"}}}]}}, \"kwargs\": {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}}}, \"name\": {\"type\": \"string\"}, \"misfire_grace_time\": {\"type\": \"integer\"}, \"coalesce\": {\"type\": \"boolean\"}, \"max_instances\": {\"type\": \"integer\"}, \"next_run_time\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_type_value\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"scheduler_type\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}}}, \"scheduler_label_prefix\": {\"type\": \"string\"}, \"scheduler_rule_name\": {\"type\": \"string\"}, \"scheduler_rule_parameters\": {\"type\": \"string\"}, \"scheduler_is_playbook\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "bde7b5b2-f454-4435-9103-de31d991b924",
      "version": 1,
      "view_items": [
        {
          "content": "0e1330b2-0b91-462b-acf2-2772a02299f8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6742aa35-eb76-4fa4-85f8-a86015cf888a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bfacefb1-5b39-4e7f-919c-84ccc54442f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4d308c31-9056-4d34-b977-99d58f89076c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a5074a34-6d40-4d03-8bf0-a8ad65b31f59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6b4b65f3-a243-48b5-8fea-e412bf2cf9f7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8690362f-626a-4c93-a68e-c2fb3b746003",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5ad21089-a73c-4408-ae52-d636e154351c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Schedule a Rule/Playbook to Run",
          "object_type": "incident",
          "programmatic_name": "schedule_rule_to_run",
          "tags": [],
          "uuid": null,
          "workflow_id": 31
        },
        {
          "actions": [],
          "description": null,
          "name": "Schedule a Rule/Playbook to Run - Artifact",
          "object_type": "artifact",
          "programmatic_name": "schedule_a_rule_to_run_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 32
        },
        {
          "actions": [],
          "description": null,
          "name": "Schedule a Rule/Playbook to Run - Task",
          "object_type": "task",
          "programmatic_name": "schedule_a_rule_to_run__task",
          "tags": [],
          "uuid": null,
          "workflow_id": 36
        }
      ]
    },
    {
      "created_date": 1681402927456,
      "description": {
        "content": "List the schedules presently defined",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule List",
      "export_key": "list_scheduled_rules",
      "id": 8,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927493,
      "name": "list_scheduled_rules",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": [{\"id\": \"domain2-5640\", \"args\": [5640, null, null, \"domain2-5640\", \"test scheduled rule\", 212, 0, {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, null, {\"timezone\": \"America/New_York\", \"thread_max\": \"20\", \"datastore_dir\": \"/tmp/scheduler.sqlite\"}], \"next_run_time\": \"Apr 27 2022 05:00AM\", \"type\": \"date\", \"value\": \"Apr 27 2022 01:02AM\"}], \"raw\": \"[{\\\"id\\\": \\\"domain2-5640\\\", \\\"args\\\": [5640, null, null, \\\"domain2-5640\\\", \\\"test scheduled rule\\\", 212, 0, {\\\"artifact_value\\\": \\\"abc.com\\\", \\\"artifact_type\\\": \\\"domain\\\"}, null, {\\\"timezone\\\": \\\"America/New_York\\\", \\\"thread_max\\\": \\\"20\\\", \\\"datastore_dir\\\": \\\"/tmp/scheduler.sqlite\\\"}], \\\"next_run_time\\\": \\\"Apr 27 2022 05:00AM\\\", \\\"type\\\": \\\"date\\\", \\\"value\\\": \\\"Apr 27 2022 01:02AM\\\"}]\", \"inputs\": {\"incident_id\": 0}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 5, \"timestamp\": \"2022-04-26 08:48:41\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"args\": {\"type\": \"array\", \"items\": {\"anyOf\": [{\"type\": [\"integer\", \"null\", \"string\"]}, {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"thread_max\": {\"type\": \"string\"}, \"datastore_dir\": {\"type\": \"string\"}}}]}}, \"next_run_time\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "8972a0b8-7a13-4dee-b6c1-e9ebc389b3d3",
      "version": 1,
      "view_items": [
        {
          "content": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "List Schedules",
          "object_type": "incident",
          "programmatic_name": "list_schedules",
          "tags": [],
          "uuid": null,
          "workflow_id": 35
        }
      ]
    },
    {
      "created_date": 1681402927509,
      "description": {
        "content": "Stop a schedule",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Remove",
      "export_key": "remove_a_scheduled_rule",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927545,
      "name": "remove_a_scheduled_rule",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": null, \"raw\": \"null\", \"inputs\": {\"scheduler_label\": \"domain2-5640\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 8, \"timestamp\": \"2022-04-26 09:08:20\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_label\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "7df74f5f-1b72-4357-85e3-20372e879b78",
      "version": 1,
      "view_items": [
        {
          "content": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Remove a Scheduled Rule/Playbook",
          "object_type": "scheduler_rules",
          "programmatic_name": "remove_a_schedule",
          "tags": [],
          "uuid": null,
          "workflow_id": 29
        }
      ]
    },
    {
      "created_date": 1681402927561,
      "description": {
        "content": "Run a scheduled job now",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Run Schedule Job Now",
      "export_key": "run_schedule_job_now",
      "id": 10,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927598,
      "name": "run_schedule_job_now",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {}, \"raw\": null, \"inputs\": {\"scheduler_label\": \"rulex1-5713\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 1609, \"timestamp\": \"2022-04-28 17:39:27\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_label\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "d35f9fe8-d19b-41fc-adb2-d80bc7b4e68b",
      "version": 1,
      "view_items": [
        {
          "content": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Run a Scheduled Job Now",
          "object_type": "scheduler_rules",
          "programmatic_name": "run_a_scheduled_job_now",
          "tags": [],
          "uuid": null,
          "workflow_id": 34
        }
      ]
    },
    {
      "created_date": 1681402927612,
      "description": {
        "content": "Modify an existing schedule",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Modify",
      "export_key": "scheduled_rule_modify",
      "id": 11,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927648,
      "name": "scheduled_rule_modify",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"domain2-5640\", \"args\": [5640, null, null, \"domain2-5640\", \"test scheduled rule\", 212, 0, {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, null, {\"timezone\": \"America/New_York\", \"thread_max\": \"20\", \"datastore_dir\": \"/tmp/scheduler.sqlite\"}], \"next_run_time\": \"Apr 27 2022 05:00AM\", \"type\": \"date\", \"value\": \"Apr 28 2022 04:05AM\"}, \"raw\": null, \"inputs\": {\"scheduler_type_value\": \"2022-04-28 04:05:06\", \"scheduler_label\": \"domain2-5640\", \"scheduler_type\": \"date\", \"scheduler_rule_parameters\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 23, \"timestamp\": \"2022-04-26 08:49:26\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"args\": {\"type\": \"array\", \"items\": {\"anyOf\": [{\"type\": [\"integer\", \"null\", \"string\"]}, {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"thread_max\": {\"type\": \"string\"}, \"datastore_dir\": {\"type\": \"string\"}}}]}}, \"next_run_time\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_type_value\": {\"type\": \"string\"}, \"scheduler_label\": {\"type\": \"string\"}, \"scheduler_type\": {\"type\": \"string\"}, \"scheduler_rule_parameters\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "a2014c98-26b7-4016-917a-147509a88775",
      "version": 1,
      "view_items": [
        {
          "content": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0aeb9039-7eae-49d6-81d8-369ebb401019",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b5ca3be1-0c84-4898-b1f6-2015eb753e1c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4d308c31-9056-4d34-b977-99d58f89076c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Modify a Scheduled Job",
          "object_type": "scheduler_rules",
          "programmatic_name": "modify_a_scheduled_rule",
          "tags": [],
          "uuid": null,
          "workflow_id": 28
        }
      ]
    },
    {
      "created_date": 1681402927663,
      "description": {
        "content": "Pause a scheduled rule",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Pause",
      "export_key": "scheduled_rule_pause",
      "id": 12,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927698,
      "name": "scheduled_rule_pause",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"id\": \"domain2-5640\", \"args\": [5640, null, null, \"domain2-5640\", \"test scheduled rule\", 212, 0, {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, null, {\"timezone\": \"America/New_York\", \"thread_max\": \"20\", \"datastore_dir\": \"/tmp/scheduler.sqlite\"}], \"next_run_time\": \"Apr 27 2022 05:00AM\", \"type\": \"date\", \"value\": \"Apr 28 2022 04:05AM\"}, \"raw\": \"{\\\"id\\\": \\\"domain2-5640\\\", \\\"args\\\": [5640, null, null, \\\"domain2-5640\\\", \\\"test scheduled rule\\\", 212, 0, {\\\"artifact_value\\\": \\\"abc.com\\\", \\\"artifact_type\\\": \\\"domain\\\"}, null, {\\\"timezone\\\": \\\"America/New_York\\\", \\\"thread_max\\\": \\\"20\\\", \\\"datastore_dir\\\": \\\"/tmp/scheduler.sqlite\\\"}], \\\"next_run_time\\\": \\\"Apr 27 2022 05:00AM\\\", \\\"type\\\": \\\"date\\\", \\\"value\\\": \\\"Apr 28 2022 04:05AM\\\"}\", \"inputs\": {\"scheduler_label\": \"domain2-5640\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 14, \"timestamp\": \"2022-04-26 09:07:44\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"args\": {\"type\": \"array\", \"items\": {\"anyOf\": [{\"type\": [\"integer\", \"null\", \"string\"]}, {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"thread_max\": {\"type\": \"string\"}, \"datastore_dir\": {\"type\": \"string\"}}}]}}, \"next_run_time\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_label\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "aa278752-98c2-4866-b477-0eb19fd81b34",
      "version": 1,
      "view_items": [
        {
          "content": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Pause a Scheduled Job",
          "object_type": "scheduler_rules",
          "programmatic_name": "pause_a_scheduled_job",
          "tags": [],
          "uuid": null,
          "workflow_id": 30
        }
      ]
    },
    {
      "created_date": 1681402927713,
      "description": {
        "content": "Resume a scheduled job",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Resume",
      "export_key": "scheduled_rule_resume",
      "id": 13,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681402927748,
      "name": "scheduled_rule_resume",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"id\": \"domain2-5640\", \"args\": [5640, null, null, \"domain2-5640\", \"test scheduled rule\", 212, 0, {\"artifact_value\": \"abc.com\", \"artifact_type\": \"domain\"}, null, {\"timezone\": \"America/New_York\", \"thread_max\": \"20\", \"datastore_dir\": \"/tmp/scheduler.sqlite\"}], \"next_run_time\": null, \"type\": \"date\", \"value\": \"Apr 28 2022 04:05AM\"}, \"raw\": \"{\\\"id\\\": \\\"domain2-5640\\\", \\\"args\\\": [5640, null, null, \\\"domain2-5640\\\", \\\"test scheduled rule\\\", 212, 0, {\\\"artifact_value\\\": \\\"abc.com\\\", \\\"artifact_type\\\": \\\"domain\\\"}, null, {\\\"timezone\\\": \\\"America/New_York\\\", \\\"thread_max\\\": \\\"20\\\", \\\"datastore_dir\\\": \\\"/tmp/scheduler.sqlite\\\"}], \\\"next_run_time\\\": null, \\\"type\\\": \\\"date\\\", \\\"value\\\": \\\"Apr 28 2022 04:05AM\\\"}\", \"inputs\": {\"scheduler_label\": \"domain2-5640\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-scheduler\", \"package_version\": \"1.2.0\", \"host\": \"local\", \"execution_time_ms\": 10, \"timestamp\": \"2022-04-26 09:08:01\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"args\": {\"type\": \"array\", \"items\": {\"anyOf\": [{\"type\": [\"integer\", \"null\", \"string\"]}, {\"type\": \"object\", \"properties\": {\"artifact_value\": {\"type\": \"string\"}, \"artifact_type\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"thread_max\": {\"type\": \"string\"}, \"datastore_dir\": {\"type\": \"string\"}}}]}}, \"next_run_time\": {}, \"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"scheduler_label\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "37083e99-ca31-41fb-85b5-d0ac4ed1f60b",
      "version": 1,
      "view_items": [
        {
          "content": "a8315456-7803-4a4d-a482-aeec5ca91c4e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Resume a Scheduled Job",
          "object_type": "scheduler_rules",
          "programmatic_name": "resume_a_scheduled_job",
          "tags": [],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 14,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1681825196605,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1681825196605,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ece0892e-be15-4dd3-beba-c7ce824b29ac"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_scheduler",
      "name": "fn_scheduler",
      "programmatic_name": "fn_scheduler",
      "tags": [],
      "users": [],
      "uuid": "02927d03-a71c-4662-9520-4010fa2ac284"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0\" isExecutable=\"true\" name=\"playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0vjpdlj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule List\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8972a0b8-7a13-4dee-b6c1-e9ebc389b3d3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = 0 if getattr(playbook.inputs, \\\"incidents_returned\\\", None) == \\\"All\\\" else incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_list\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vjpdlj\u003c/incoming\u003e\u003coutgoing\u003eFlow_10dlkmg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0vjpdlj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Write all jobs to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"ab17abfe-7197-4a20-8a4a-a7bd2003f9b1\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_10dlkmg\u003c/incoming\u003e\u003coutgoing\u003eFlow_06tw55x\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_10dlkmg\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_06tw55x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_06tw55x\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vjpdlj\" id=\"Flow_0vjpdlj_di\"\u003e\u003comgdi:waypoint x=\"610\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"610\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_10dlkmg\" id=\"Flow_10dlkmg_di\"\u003e\u003comgdi:waypoint x=\"610\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"610\" y=\"478\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06tw55x\" id=\"Flow_06tw55x_di\"\u003e\u003comgdi:waypoint x=\"610\" y=\"562\"/\u003e\u003comgdi:waypoint x=\"610\" y=\"664\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"516\" y=\"124\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"512\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"512\" y=\"478\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"544\" y=\"664\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681811822549,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0",
      "description": {
        "content": "List all scheduled jobs",
        "format": "text"
      },
      "display_name": "Scheduler: List Jobs",
      "export_key": "pb_scheduler_list_jobs",
      "field_type_handle": "playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: List Jobs",
        "export_key": "playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0",
        "uuid": "abf42e45-454d-4357-b446-08ceed0c1caa"
      },
      "has_logical_errors": false,
      "id": 24,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681812527240,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681812194267,
          "description": "Writes out all scheduled jobs to datatabe",
          "enabled": false,
          "export_key": "Write all jobs to DataTable",
          "id": 23,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681812194282,
          "name": "Write all jobs to DataTable",
          "object_type": "incident",
          "playbook_handle": "pb_scheduler_list_jobs",
          "programmatic_name": "pb_scheduler_list_jobs_write_all_jobs_to_datatable",
          "script_text": "from datetime import datetime\n\nresults = playbook.functions.results.output_scheduled_rule_list\nnow = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\") # \u00272023-03-24 11:28:34\u0027\nTYPE_LOOKUP = {\n  0: \u0027Incident\u0027,\n  1: \"Task\",\n  4: \"Artifact\",\n  5: \"Attachment\"}\n\nif not results[\u0027content\u0027]:\n  row = incident.addRow(\"scheduler_rules\")\n  row[\u0027reported_on\u0027] = date\n  row[\u0027schedule_label\u0027] = \"-- no scheduled rules --\"\n\nelse:\n  for job in results[\u0027content\u0027]:\n    row = incident.addRow(\"scheduler_rules\")\n    row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\n    row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\n    row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\n    row[\u0027schedule\u0027] = job[\u0027value\u0027]\n    row[\u0027reported_on\u0027] = now\n    row[\u0027status\u0027] = \u0027Active\u0027 if job[\u0027next_run_time\u0027] else \u0027Paused\u0027\n    row[\u0027next_run_time\u0027] = job[\u0027next_run_time\u0027]\n    row[\u0027rule_type\u0027] = TYPE_LOOKUP.get(job[\u0027args\u0027][6], \"Datatable\")\n\n    if job[\u0027args\u0027][8]:\n      row[\u0027rule\u0027] = \"\u003ca href=\u0027#playbooks/designer/{}\u0027\u003e{}\u003c/a\u003e\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\n    else:\n      row[\u0027rule\u0027] = \"\u003ca href=\u0027#customize?tab=actions\u0026id={}\u0027\u003e{}\u003c/a\u003e\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\n",
          "tags": [],
          "uuid": "ab17abfe-7197-4a20-8a4a-a7bd2003f9b1"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_list_jobs",
      "object_type": "incident",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_f48af589-3237-4bf3-8b34-8a35d56dfcf0",
        "id": 26,
        "name": "playbook_f48af589_3237_4bf3_8b34_8a35d56dfcf0",
        "type": "playbook",
        "uuid": "d7b79186-1876-4e51-b73c-4f4e619e870f"
      },
      "tags": [],
      "type": "default",
      "uuid": "f48af589-3237-4bf3-8b34-8a35d56dfcf0",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6\" isExecutable=\"true\" name=\"playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_148uxgp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Modify\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a2014c98-26b7-4016-917a-147509a88775\"\u003e{\"inputs\":{\"a8315456-7803-4a4d-a482-aeec5ca91c4e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"0aeb9039-7eae-49d6-81d8-369ebb401019\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"bee7db2c-6675-4d5d-8ff8-ce2ddfae603b\"}},\"b5ca3be1-0c84-4898-b1f6-2015eb753e1c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"4d308c31-9056-4d34-b977-99d58f89076c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.scheduler_label = row[\u0027schedule_label\u0027]\\ninputs.modify_scheduler_type = getattr(playbook.inputs, \\\"modify_schedule_type\\\", None)\\ninputs.modify_scheduler_type_value = getattr(playbook.inputs, \\\"modify_schedule_type_value\\\", \\\"cron\\\")\\ninputs.scheduler_rule_parameters = getattr(playbook.inputs, \\\"schedule_rule_parameters\\\", None)\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_modify\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_148uxgp\u003c/incoming\u003e\u003coutgoing\u003eFlow_14zt43o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_148uxgp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Write modified job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3729f3b4-aef9-454f-93e7-cef91cc7938a\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14zt43o\u003c/incoming\u003e\u003coutgoing\u003eFlow_0xvmy8a\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_14zt43o\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0xvmy8a\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0xvmy8a\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_148uxgp\" id=\"Flow_148uxgp_di\"\u003e\u003comgdi:waypoint x=\"680\" y=\"126\"/\u003e\u003comgdi:waypoint x=\"680\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14zt43o\" id=\"Flow_14zt43o_di\"\u003e\u003comgdi:waypoint x=\"680\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"680\" y=\"388\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xvmy8a\" id=\"Flow_0xvmy8a_di\"\u003e\u003comgdi:waypoint x=\"680\" y=\"472\"/\u003e\u003comgdi:waypoint x=\"680\" y=\"564\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"580\" y=\"74\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"582\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"582\" y=\"388\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"614\" y=\"564\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681812620433,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6",
      "description": {
        "content": "Modify existing jobs",
        "format": "text"
      },
      "display_name": "Scheduler: Modify Job",
      "export_key": "pb_scheduler_modify_job",
      "field_type_handle": "playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Modify Job",
        "export_key": "playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6",
        "uuid": "c1f2c44a-cbd3-4614-a677-2c6362ff43ea"
      },
      "has_logical_errors": false,
      "id": 25,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681812959267,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681812937606,
          "description": "Updates the dataTable with the modified job",
          "enabled": false,
          "export_key": "Write modified job to DataTable",
          "id": 24,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681812937617,
          "name": "Write modified job to DataTable",
          "object_type": "scheduler_rules",
          "playbook_handle": "pb_scheduler_modify_job",
          "programmatic_name": "pb_scheduler_modify_job_write_modified_job_to_datatable",
          "script_text": "from datetime import datetime\n\nresults = playbook.functions.results.output_scheduled_rule_modify\nnow = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\") # \u00272023-03-24 11:28:34\u0027\n\nif not results.get(\"success\"):\n  incident.addNote(\"Modify Scheduled Rule/Playbook failed: {}\".format(results.get(\"reason\")))\n\nelse:\n  job = results.get(\"content\")\n  row[\u0027reported_on\u0027] = now\n  row[\u0027schedule_type\u0027] = job.get(\u0027type\u0027)\n  row[\u0027schedule\u0027] = job.get(\u0027value\u0027)\n  incident.addNote(\"Modify Scheduled Rule/Playbook succeeded for: {}\".format(job.get(\u0027id\u0027)))\n",
          "tags": [],
          "uuid": "3729f3b4-aef9-454f-93e7-cef91cc7938a"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_modify_job",
      "object_type": "scheduler_rules",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_3da68bad-7a31-4e0d-bb23-36ddf5303fb6",
        "id": 27,
        "name": "playbook_3da68bad_7a31_4e0d_bb23_36ddf5303fb6",
        "type": "playbook",
        "uuid": "8d955bdf-35bf-4df1-99fa-b2efeb8a7b8f"
      },
      "tags": [],
      "type": "default",
      "uuid": "3da68bad-7a31-4e0d-bb23-36ddf5303fb6",
      "version": 5
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04\" isExecutable=\"true\" name=\"playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0vn1qwu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Pause\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"aa278752-98c2-4866-b477-0eb19fd81b34\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_pause\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vn1qwu\u003c/incoming\u003e\u003coutgoing\u003eFlow_0asbdjd\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0vn1qwu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Write paused job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"57b2ba73-f114-4562-99d6-bdc4f423bf74\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0asbdjd\u003c/incoming\u003e\u003coutgoing\u003eFlow_03vswz4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0asbdjd\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_03vswz4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_03vswz4\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vn1qwu\" id=\"Flow_0vn1qwu_di\"\u003e\u003comgdi:waypoint x=\"660\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"660\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0asbdjd\" id=\"Flow_0asbdjd_di\"\u003e\u003comgdi:waypoint x=\"660\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"660\" y=\"348\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_03vswz4\" id=\"Flow_03vswz4_di\"\u003e\u003comgdi:waypoint x=\"660\" y=\"432\"/\u003e\u003comgdi:waypoint x=\"660\" y=\"514\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"560\" y=\"54\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"562\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"562\" y=\"348\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"594\" y=\"514\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681813003917,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04",
      "description": {
        "content": "Pause a scheduled job",
        "format": "text"
      },
      "display_name": "Scheduler: Pause Job",
      "export_key": "pb_scheduler_pause_job",
      "field_type_handle": "playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Pause Job",
        "export_key": "playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04",
        "uuid": "c9d942ca-7634-4807-9ef8-ec7f97cae726"
      },
      "has_logical_errors": false,
      "id": 26,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681813225493,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681813196235,
          "description": "",
          "enabled": false,
          "export_key": "Write paused job to DataTable",
          "id": 25,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681813196247,
          "name": "Write paused job to DataTable",
          "object_type": "scheduler_rules",
          "playbook_handle": "pb_scheduler_pause_job",
          "programmatic_name": "pb_scheduler_pause_job_write_paused_job_to_datatable",
          "script_text": "results = playbook.functions.results.output_scheduled_rule_pause\n\nif results.get(\"success\"):\n  row[\u0027status\u0027] = \u0027Paused\u0027\nelse:\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \" (Error)\"\n",
          "tags": [],
          "uuid": "57b2ba73-f114-4562-99d6-bdc4f423bf74"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_pause_job",
      "object_type": "scheduler_rules",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_e6557d98-6d8b-4fa3-bad3-cf0e61d1ad04",
        "id": 28,
        "name": "playbook_e6557d98_6d8b_4fa3_bad3_cf0e61d1ad04",
        "type": "playbook",
        "uuid": "a6d1bd79-c52f-4382-9904-dee74edc9689"
      },
      "tags": [],
      "type": "default",
      "uuid": "e6557d98-6d8b-4fa3-bad3-cf0e61d1ad04",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983\" isExecutable=\"true\" name=\"playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_07citrq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Remove\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7df74f5f-1b72-4357-85e3-20372e879b78\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_remove\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_07citrq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1mnbasl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_07citrq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0s00p5r\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Write removed job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"0100138c-f497-4284-a202-0bc3b482d47d\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1mnbasl\u003c/incoming\u003e\u003coutgoing\u003eFlow_0s00p5r\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1mnbasl\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_0s00p5r\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_07citrq\" id=\"Flow_07citrq_di\"\u003e\u003comgdi:waypoint x=\"600\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"600\" y=\"238\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1mnbasl\" id=\"Flow_1mnbasl_di\"\u003e\u003comgdi:waypoint x=\"600\" y=\"322\"/\u003e\u003comgdi:waypoint x=\"600\" y=\"388\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0s00p5r\" id=\"Flow_0s00p5r_di\"\u003e\u003comgdi:waypoint x=\"600\" y=\"472\"/\u003e\u003comgdi:waypoint x=\"600\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"500\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"502\" y=\"238\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"534\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"502\" y=\"388\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681822648541,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983",
      "description": {
        "content": "Remove a scheduled job",
        "format": "text"
      },
      "display_name": "Scheduler: Remove Job",
      "export_key": "pb_scheduler_remove_job",
      "field_type_handle": "playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Remove Job",
        "export_key": "playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983",
        "uuid": "33d518f2-13c7-4303-a8d9-45bf17aa5e1d"
      },
      "has_logical_errors": false,
      "id": 33,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681825100368,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681825051404,
          "description": "",
          "enabled": false,
          "export_key": "Write removed job to DataTable",
          "id": 30,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681825051420,
          "name": "Write removed job to DataTable",
          "object_type": "scheduler_rules",
          "playbook_handle": "pb_scheduler_remove_job",
          "programmatic_name": "pb_scheduler_remove_job_write_removed_job_to_datatable",
          "script_text": "results = playbook.functions.results.output_scheduled_rule_remove\n\nif results.get(\"success\"):\n  row[\u0027status\u0027] = \"Deleted\"\nelse:\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \" (Error)\"\n",
          "tags": [],
          "uuid": "0100138c-f497-4284-a202-0bc3b482d47d"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_remove_job",
      "object_type": "scheduler_rules",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_cb82c8f1-c294-4a01-8a3a-12e581bca983",
        "id": 35,
        "name": "playbook_cb82c8f1_c294_4a01_8a3a_12e581bca983",
        "type": "playbook",
        "uuid": "da5a6680-c4f8-4c34-b340-8b8236da7076"
      },
      "tags": [],
      "type": "default",
      "uuid": "cb82c8f1-c294-4a01-8a3a-12e581bca983",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_16c168c0_628f_4f50_9523_ae5c0287b76d\" isExecutable=\"true\" name=\"playbook_16c168c0_628f_4f50_9523_ae5c0287b76d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0abzlni\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Resume\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"37083e99-ca31-41fb-85b5-d0ac4ed1f60b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_resume\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0abzlni\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kd0eqv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0abzlni\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Write resumed job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3eaa3c1c-74bc-4673-b9aa-39c7ab1dbb65\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0kd0eqv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1jfish5\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0kd0eqv\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1jfish5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1jfish5\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_16c168c0_628f_4f50_9523_ae5c0287b76d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0abzlni\" id=\"Flow_0abzlni_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kd0eqv\" id=\"Flow_0kd0eqv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"348\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jfish5\" id=\"Flow_1jfish5_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"432\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"348\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"474\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681813295240,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_16c168c0_628f_4f50_9523_ae5c0287b76d",
      "description": {
        "content": "Resume a Scheduled Job",
        "format": "text"
      },
      "display_name": "Scheduler: Resume Job",
      "export_key": "pb_scheduler_resume_job",
      "field_type_handle": "playbook_16c168c0_628f_4f50_9523_ae5c0287b76d",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Resume Job",
        "export_key": "playbook_16c168c0_628f_4f50_9523_ae5c0287b76d",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_16c168c0_628f_4f50_9523_ae5c0287b76d",
        "uuid": "c5f9138c-2931-434b-a536-94472173ef84"
      },
      "has_logical_errors": false,
      "id": 27,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681814394793,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681814369335,
          "description": "",
          "enabled": false,
          "export_key": "Write resumed job to DataTable",
          "id": 26,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681814369348,
          "name": "Write resumed job to DataTable",
          "object_type": "scheduler_rules",
          "playbook_handle": "pb_scheduler_resume_job",
          "programmatic_name": "pb_scheduler_resume_job_write_resumed_job_to_datatable",
          "script_text": "results = playbook.functions.results.output_scheduled_rule_resume\n\nif results.get(\"success\"):\n  row[\u0027status\u0027] = \u0027Active\u0027\nelse:\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \" (Error)\"",
          "tags": [],
          "uuid": "3eaa3c1c-74bc-4673-b9aa-39c7ab1dbb65"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_resume_job",
      "object_type": "scheduler_rules",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_16c168c0-628f-4f50-9523-ae5c0287b76d",
        "id": 29,
        "name": "playbook_16c168c0_628f_4f50_9523_ae5c0287b76d",
        "type": "playbook",
        "uuid": "1494a655-db1e-4cbb-99b5-b7dc492fc359"
      },
      "tags": [],
      "type": "default",
      "uuid": "16c168c0-628f-4f50-9523-ae5c0287b76d",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea\" isExecutable=\"true\" name=\"playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0bi2u41\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Run Schedule Job Now\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d35f9fe8-d19b-41fc-adb2-d80bc7b4e68b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.scheduler_label = row[\u0027schedule_label\u0027]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_run\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0bi2u41\u003c/incoming\u003e\u003coutgoing\u003eFlow_0b29eph\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0bi2u41\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Write executed job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"407b2ddd-e3b5-49bd-af97-4c1a0be854b4\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0b29eph\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ox2zla\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0b29eph\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1ox2zla\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1ox2zla\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bi2u41\" id=\"Flow_0bi2u41_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0b29eph\" id=\"Flow_0b29eph_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ox2zla\" id=\"Flow_1ox2zla_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"574\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"574\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681814503362,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea",
      "description": {
        "content": "Run a scheduled job immediately",
        "format": "text"
      },
      "display_name": "Scheduler: Run Job now",
      "export_key": "pb_scheduler_run_job_now",
      "field_type_handle": "playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Run Job now",
        "export_key": "playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea",
        "uuid": "c0b780eb-962a-402c-b93e-4c4f67953aed"
      },
      "has_logical_errors": false,
      "id": 28,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681814666194,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1681814635306,
          "description": "",
          "enabled": false,
          "export_key": "Write executed job to DataTable",
          "id": 27,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1681814635317,
          "name": "Write executed job to DataTable",
          "object_type": "scheduler_rules",
          "playbook_handle": "pb_scheduler_run_job_now",
          "programmatic_name": "pb_scheduler_run_job_now_write_executed_job_to_datatable",
          "script_text": "results = playbook.functions.results.output_scheduled_rule_run\n\nif not results.success:\n  incident.addNote(\"Run Scheduled Job Now failed for job {}: {}\".format(row[\u0027schedule_label\u0027], results.reason))\nelse:\n  msg = \"Run Scheduled Job Now suceeeded for job: {}, Rule/Playbook: {}\".format(row[\u0027schedule_label\u0027], row[\u0027rule\u0027].content)\n  incident.addNote(helper.createRichText(msg))",
          "tags": [],
          "uuid": "407b2ddd-e3b5-49bd-af97-4c1a0be854b4"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_run_job_now",
      "object_type": "scheduler_rules",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_19f67260-22c1-4871-9a9f-31b6889ab9ea",
        "id": 30,
        "name": "playbook_19f67260_22c1_4871_9a9f_31b6889ab9ea",
        "type": "playbook",
        "uuid": "caf10aaa-7678-463f-959f-d7f49101bb13"
      },
      "tags": [],
      "type": "default",
      "uuid": "19f67260-22c1-4871-9a9f-31b6889ab9ea",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a\" isExecutable=\"true\" name=\"playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_162tnn7\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"6742aa35-eb76-4fa4-85f8-a86015cf888a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"bfacefb1-5b39-4e7f-919c-84ccc54442f0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a5074a34-6d40-4d03-8bf0-a8ad65b31f59\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"6b4b65f3-a243-48b5-8fea-e412bf2cf9f7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}},\"4d308c31-9056-4d34-b977-99d58f89076c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"8690362f-626a-4c93-a68e-c2fb3b746003\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"5ad21089-a73c-4408-ae52-d636e154351c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.scheduler_type = getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\")\\n\\nif getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\") == \\\"date\\\":\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\").replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\")\\n\\ninputs.scheduler_rule_name = getattr(playbook.inputs, \\\"schedule_rule_name\\\", None)\\ninputs.scheduler_rule_parameters = getattr(playbook.inputs, \\\"schedule_rule_parameters\\\", None)\\ninputs.scheduler_label_prefix = getattr(playbook.inputs, \\\"schedule_label_prefix\\\", None)\\ninputs.incident_id = incident.id\\ninputs.scheduler_is_playbook = getattr(playbook.inputs, \\\"schedule_is_playbook\\\", False)\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_create\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_162tnn7\u003c/incoming\u003e\u003coutgoing\u003eFlow_00vaatr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_162tnn7\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_00vaatr\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1m4jj08\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Write scheduled job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"38d9b9df-35c7-48ec-adec-8a082f5be517\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_00vaatr\u003c/incoming\u003e\u003coutgoing\u003eFlow_1m4jj08\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1m4jj08\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_00vaatr\" id=\"Flow_00vaatr_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_162tnn7\" id=\"Flow_162tnn7_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1m4jj08\" id=\"Flow_1m4jj08_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"600\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"602\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"634\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"601.5\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681817436452,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a",
      "description": {
        "content": "Schedule a rule/playbook to run in the future for a given incident",
        "format": "text"
      },
      "display_name": "Scheduler: Schedule a Job",
      "export_key": "pb_scheduler_schedule_job",
      "field_type_handle": "playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Schedule a Job",
        "export_key": "playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a",
        "uuid": "c273dcad-1c4e-426c-8c17-d02a1bad18d6"
      },
      "has_logical_errors": false,
      "id": 30,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681819050944,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_schedule_job",
      "object_type": "incident",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_2405a12b-1f53-4ebf-b87e-d2f91866635a",
        "id": 32,
        "name": "playbook_2405a12b_1f53_4ebf_b87e_d2f91866635a",
        "type": "playbook",
        "uuid": "52119f75-23dd-44e9-b76f-bba681260441"
      },
      "tags": [],
      "type": "default",
      "uuid": "2405a12b-1f53-4ebf-b87e-d2f91866635a",
      "version": 14
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864\" isExecutable=\"true\" name=\"playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_162tnn7\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"6742aa35-eb76-4fa4-85f8-a86015cf888a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"bfacefb1-5b39-4e7f-919c-84ccc54442f0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a5074a34-6d40-4d03-8bf0-a8ad65b31f59\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"6b4b65f3-a243-48b5-8fea-e412bf2cf9f7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}},\"4d308c31-9056-4d34-b977-99d58f89076c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"8690362f-626a-4c93-a68e-c2fb3b746003\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"5ad21089-a73c-4408-ae52-d636e154351c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.object_id    = artifact.id\\ninputs.incident_id  = incident.id\\n\\ninputs.scheduler_type         = getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\")\\ninputs.scheduler_rule_name    = getattr(playbook.inputs, \\\"schedule_rule_name\\\", None)\\ninputs.scheduler_label_prefix = getattr(playbook.inputs, \\\"schedule_label_prefix\\\", None)\\ninputs.scheduler_is_playbook  = getattr(playbook.inputs, \\\"schedule_is_playbook\\\", False)\\n\\nif getattr(playbook.inputs, \\\"schedule_rule_parameters\\\", None):\\n  inputs.scheduler_rule_parameters =  getattr(playbook.inputs, \\\"schedule_rule_parameters\\\", \\\"\\\") + u\\\";artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\nelse:\\n  inputs.scheduler_rule_parameters = u\\\"artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\n\\nif getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\") == \\\"date\\\":\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\").replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\")\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_create\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_162tnn7\u003c/incoming\u003e\u003coutgoing\u003eFlow_00vaatr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_162tnn7\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_00vaatr\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0bt7vb4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Write scheduled job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"38d9b9df-35c7-48ec-adec-8a082f5be517\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_00vaatr\u003c/incoming\u003e\u003coutgoing\u003eFlow_0bt7vb4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0bt7vb4\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_00vaatr\" id=\"Flow_00vaatr_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"378\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_162tnn7\" id=\"Flow_162tnn7_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bt7vb4\" id=\"Flow_0bt7vb4_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"462\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"634\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"601.5\" y=\"378\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"600\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"602\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681818864447,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864",
      "description": {
        "content": "Schedule a rule/playbook to run in the future for a given artifact",
        "format": "text"
      },
      "display_name": "Scheduler: Schedule a Job (Artifact)",
      "export_key": "pb_scheduler_schedule_job_artifact",
      "field_type_handle": "playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Schedule a Job (Artifact)",
        "export_key": "playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864",
        "uuid": "4ec29c0d-82a9-45e1-a40c-1ecef5cb01bb"
      },
      "has_logical_errors": false,
      "id": 31,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681819827732,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_schedule_job_artifact",
      "object_type": "artifact",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_1881ad3e-e539-47e1-b6e5-6f1c84df0864",
        "id": 33,
        "name": "playbook_1881ad3e_e539_47e1_b6e5_6f1c84df0864",
        "type": "playbook",
        "uuid": "b5f1c2d2-60a2-422f-82b4-3d1af448438f"
      },
      "tags": [],
      "type": "default",
      "uuid": "1881ad3e-e539-47e1-b6e5-6f1c84df0864",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05\" isExecutable=\"true\" name=\"playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1t1whzl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"6742aa35-eb76-4fa4-85f8-a86015cf888a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"bfacefb1-5b39-4e7f-919c-84ccc54442f0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a5074a34-6d40-4d03-8bf0-a8ad65b31f59\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"6b4b65f3-a243-48b5-8fea-e412bf2cf9f7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}},\"4d308c31-9056-4d34-b977-99d58f89076c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"8690362f-626a-4c93-a68e-c2fb3b746003\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"5ad21089-a73c-4408-ae52-d636e154351c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.scheduler_type = getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\")\\n\\nif getattr(playbook.inputs, \\\"schedule_type\\\", \\\"cron\\\") == \\\"date\\\":\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\").replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = getattr(playbook.inputs, \\\"schedule_type_value\\\", \\\"\\\")\\n\\ninputs.scheduler_rule_name = getattr(playbook.inputs, \\\"schedule_rule_name\\\", None)\\ninputs.scheduler_rule_parameters = getattr(playbook.inputs, \\\"schedule_rule_parameters\\\", None)\\ninputs.scheduler_label_prefix = getattr(playbook.inputs, \\\"schedule_label_prefix\\\", None)\\ninputs.incident_id = incident.id\\ninputs.object_id = task.id\\ninputs.scheduler_is_playbook = getattr(playbook.inputs, \\\"schedule_is_playbook\\\", False)\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"output_scheduled_rule_create\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1t1whzl\u003c/incoming\u003e\u003coutgoing\u003eFlow_00vaatr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_00vaatr\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1m4jj08\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Write scheduled job to DataTable\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"38d9b9df-35c7-48ec-adec-8a082f5be517\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_00vaatr\u003c/incoming\u003e\u003coutgoing\u003eFlow_1m4jj08\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1m4jj08\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_1t1whzl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1m4jj08\" id=\"Flow_1m4jj08_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_00vaatr\" id=\"Flow_00vaatr_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1t1whzl\" id=\"Flow_1t1whzl_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"76\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"602\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"634\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"601.5\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"619\" y=\"24\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1681821328142,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05",
      "description": {
        "content": "Schedule a rule/playbook to run in the future for a given task",
        "format": "text"
      },
      "display_name": "Scheduler: Schedule a Job (Task)",
      "export_key": "pb_scheduler_schedule_job_task",
      "field_type_handle": "playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05",
      "fields_type": {
        "actions": [],
        "display_name": "Scheduler: Schedule a Job (Task)",
        "export_key": "playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05",
        "uuid": "540c9221-1b49-4f2a-94d0-30cbe1c64f86"
      },
      "has_logical_errors": false,
      "id": 32,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1681821480208,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "pb_scheduler_schedule_job_task",
      "object_type": "task",
      "status": "draft",
      "tag": {
        "display_name": "Playbook_a486c165-85d1-4d15-ac7a-e6b8352efc05",
        "id": 34,
        "name": "playbook_a486c165_85d1_4d15_ac7a_e6b8352efc05",
        "type": "playbook",
        "uuid": "236ae9a3-87bf-4d24-a16f-28e0c0c9e6bb"
      },
      "tags": [],
      "type": "default",
      "uuid": "a486c165-85d1-4d15-ac7a-e6b8352efc05",
      "version": 8
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 8304,
    "major": 47,
    "minor": 0,
    "version": "47.0.8304"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Scheduler Jobs",
      "export_key": "scheduler_rules",
      "fields": {
        "incident_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/incident_id",
          "hide_notification": false,
          "id": 678,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "incident_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Incident Id",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "9970f30f-bd88-41e2-aab5-87c480a2238e",
          "values": [],
          "width": 73
        },
        "next_run_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/next_run_time",
          "hide_notification": false,
          "id": 679,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "next_run_time",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Next Run Time",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "56c5e84c-68d1-48f1-b937-43bc9a1ec069",
          "values": [],
          "width": 37
        },
        "reported_on": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/reported_on",
          "hide_notification": false,
          "id": 680,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "reported_on",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Reported Date",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "4c46d03a-1025-496a-8560-e9b637e58fd2",
          "values": [],
          "width": 127
        },
        "rule": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/rule",
          "hide_notification": false,
          "id": 681,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "rule",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Rule/Playbook",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "e9b42f63-41a3-4782-9d2f-585fd9f2e537",
          "values": [],
          "width": 113
        },
        "rule_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/rule_type",
          "hide_notification": false,
          "id": 682,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "rule_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Rule Type",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "964a0f94-da6b-4005-8fa1-8540590e21b0",
          "values": [],
          "width": 36
        },
        "schedule": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/schedule",
          "hide_notification": false,
          "id": 683,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "schedule",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Schedule",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "45a3e54f-97e7-425f-a15f-d856c7b7b17c",
          "values": [],
          "width": 83
        },
        "schedule_label": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/schedule_label",
          "hide_notification": false,
          "id": 684,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "schedule_label",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Schedule Label",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "2d010306-40d2-4571-a3c1-a9e9c50a0b71",
          "values": [],
          "width": 93
        },
        "schedule_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/schedule_type",
          "hide_notification": false,
          "id": 685,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "schedule_type",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Schedule Type",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "9eaa03ac-6b52-4eec-b9cd-69b6dbf4b893",
          "values": [],
          "width": 71
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/status",
          "hide_notification": false,
          "id": 686,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1020,
          "uuid": "a6f4384a-78d6-4b48-bcb6-40e5cc1c4d9b",
          "values": [],
          "width": 49
        }
      },
      "for_actions": false,
      "for_custom_fields": false,
      "for_notifications": false,
      "for_workflows": false,
      "id": null,
      "parent_types": [
        "incident"
      ],
      "properties": {
        "can_create": false,
        "can_destroy": false,
        "for_who": []
      },
      "scripts": [],
      "tags": [],
      "type_id": 8,
      "type_name": "scheduler_rules",
      "uuid": "58fff2fe-6cd9-488b-81bc-2c6accb3447e"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "resume_a_scheduled_job",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"resume_a_scheduled_job\" isExecutable=\"true\" name=\"Resume a Scheduled Job\"\u003e\u003cdocumentation\u003eResume a Scheduled Job\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lgsip6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1z0kxqu\" name=\"Scheduled Rule Resume\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"37083e99-ca31-41fb-85b5-d0ac4ed1f60b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \u0027Active\u0027\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lgsip6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0su016m\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lgsip6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1z0kxqu\"/\u003e\u003cendEvent id=\"EndEvent_1157mca\"\u003e\u003cincoming\u003eSequenceFlow_0su016m\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0su016m\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"EndEvent_1157mca\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eggn77\"\u003e\u003ctext\u003eActs on a datatable row of scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15nfoj0\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"TextAnnotation_0eggn77\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_139h4an\"\u003e\u003ctext\u003eRow is updated to indicate that the scheduled rule is now active\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1k45r8j\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"TextAnnotation_139h4an\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1z0kxqu\" id=\"ServiceTask_1z0kxqu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lgsip6\" id=\"SequenceFlow_1lgsip6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"243.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1157mca\" id=\"EndEvent_1157mca_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"474\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"492\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0su016m\" id=\"SequenceFlow_0su016m_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"474\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"431.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eggn77\" id=\"TextAnnotation_0eggn77_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"139\" x=\"163\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15nfoj0\" id=\"Association_15nfoj0_di\"\u003e\u003comgdi:waypoint x=\"297\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_139h4an\" id=\"TextAnnotation_139h4an_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"187\" x=\"396\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1k45r8j\" id=\"Association_1k45r8j_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Resume a Scheduled Job",
      "export_key": "resume_a_scheduled_job",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928765,
      "name": "Resume a Scheduled Job",
      "object_type": "scheduler_rules",
      "programmatic_name": "resume_a_scheduled_job",
      "tags": [],
      "uuid": "f9ebf3f3-acd2-4450-a0c3-b12de9213e44",
      "workflow_id": 33
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "modify_a_scheduled_rule",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"modify_a_scheduled_rule\" isExecutable=\"true\" name=\"Modify a Scheduled Job\"\u003e\u003cdocumentation\u003eChange an existing scheduled job\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0yairkf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0f7ufct\" name=\"Scheduled Rule Modify\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a2014c98-26b7-4016-917a-147509a88775\"\u003e{\"inputs\":{\"0aeb9039-7eae-49d6-81d8-369ebb401019\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"bee7db2c-6675-4d5d-8ff8-ce2ddfae603b\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nif not results.success:\\n  incident.addNote(\\\"Modify Scheduled Rule/Playbook failed: {}\\\".format(results.reason))\\nelse:\\n  job = results.content\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_type\u0027] = job.get(\u0027type\u0027)\\n  row[\u0027schedule\u0027] = job.get(\u0027value\u0027)\\n  incident.addNote(\\\"Modify Scheduled Rule/Playbook succeeded for: {}\\\".format(job.get(\u0027id\u0027)))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.scheduler_label = row[\u0027schedule_label\u0027]\\ninputs.modify_scheduler_type = rule.properties.modify_schedule_type\\ninputs.modify_scheduler_type_value = rule.properties.modify_schedule_type_value\\ninputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0yairkf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vncz5s\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0yairkf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0f7ufct\"/\u003e\u003cendEvent id=\"EndEvent_0pg7gk3\"\u003e\u003cincoming\u003eSequenceFlow_0vncz5s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vncz5s\" sourceRef=\"ServiceTask_0f7ufct\" targetRef=\"EndEvent_0pg7gk3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19fb2ij\"\u003e\u003ctext\u003e\u003c![CDATA[A note is created with the current datatable row updated\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_100pgym\" sourceRef=\"ServiceTask_0f7ufct\" targetRef=\"TextAnnotation_19fb2ij\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f7ufct\" id=\"ServiceTask_0f7ufct_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"271.8091674462114\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0yairkf\" id=\"SequenceFlow_0yairkf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0pg7gk3\" id=\"EndEvent_0pg7gk3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"448.8091674462114\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"466.8091674462114\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vncz5s\" id=\"SequenceFlow_0vncz5s_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19fb2ij\" id=\"TextAnnotation_19fb2ij_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"177\" x=\"369\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_100pgym\" id=\"Association_100pgym_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"419\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Change an existing scheduled job",
      "export_key": "modify_a_scheduled_rule",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928015,
      "name": "Modify a Scheduled Job",
      "object_type": "scheduler_rules",
      "programmatic_name": "modify_a_scheduled_rule",
      "tags": [],
      "uuid": "bb6fde0b-9092-4416-ada8-5fe97d242d54",
      "workflow_id": 28
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "pause_a_scheduled_job",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"pause_a_scheduled_job\" isExecutable=\"true\" name=\"Pause a Scheduled Job\"\u003e\u003cdocumentation\u003ePause a scheduled job\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0r2ecr9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1jp2yxe\" name=\"Scheduled Rule Pause\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"aa278752-98c2-4866-b477-0eb19fd81b34\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \u0027Paused\u0027\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\\n\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0r2ecr9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ercxlc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0r2ecr9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1jp2yxe\"/\u003e\u003cendEvent id=\"EndEvent_1bza8l8\"\u003e\u003cincoming\u003eSequenceFlow_1ercxlc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ercxlc\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"EndEvent_1bza8l8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0kcja56\"\u003e\u003ctext\u003eActs on a given datatable row for scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1rfy0g0\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"TextAnnotation_0kcja56\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1sbpec1\"\u003e\u003ctext\u003eRow is updated to indicate that the rule is paused\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10i22at\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"TextAnnotation_1sbpec1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1jp2yxe\" id=\"ServiceTask_1jp2yxe_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"262\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r2ecr9\" id=\"SequenceFlow_0r2ecr9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"230\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bza8l8\" id=\"EndEvent_1bza8l8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"435\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ercxlc\" id=\"SequenceFlow_1ercxlc_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0kcja56\" id=\"TextAnnotation_0kcja56_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"140\" x=\"150\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1rfy0g0\" id=\"Association_1rfy0g0_di\"\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1sbpec1\" id=\"TextAnnotation_1sbpec1_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"182\" x=\"361\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10i22at\" id=\"Association_10i22at_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"409\" xsi:type=\"omgdc:Point\" y=\"140\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Pause a scheduled job",
      "export_key": "pause_a_scheduled_job",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928314,
      "name": "Pause a Scheduled Job",
      "object_type": "scheduler_rules",
      "programmatic_name": "pause_a_scheduled_job",
      "tags": [],
      "uuid": "b7c4e77c-b02d-47c7-9853-d8972ead8a96",
      "workflow_id": 30
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "schedule_a_rule_to_run_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"schedule_a_rule_to_run_artifact\" isExecutable=\"true\" name=\"Schedule a Rule/Playbook to Run - Artifact\"\u003e\u003cdocumentation\u003eSchedule a rule/playbook to run in the future for a given artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p0reen\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zz4wks\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nTYPE_LOOKUP = {0: \u0027Incident\u0027, 1: \\\"Task\\\", 4: \\\"Artifact\\\", 5: \\\"Attachment\\\"}\\n\\nif results.success:\\n  job = results.content\\n  row = incident.addRow(\\\"scheduler_rules\\\")\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\\n  row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\\n  row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\\n  row[\u0027schedule\u0027] = job[\u0027value\u0027]\\n  row[\u0027status\u0027] = \u0027Active\u0027\\n  row[\u0027next_run_time\u0027] = job[\u0027next_run_time\u0027]\\n  row[\u0027rule_type\u0027] = TYPE_LOOKUP.get(job[\u0027args\u0027][6], \\\"Datatable\\\")\\n  if job[\u0027args\u0027][8]:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#playbooks/designer/{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\n  else:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#customize?tab=actions\u0026amp;id={}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\nelse:\\n  incident.addNote(\\\"Schedule a Rule/Playbook failed: {}\\\".format(result.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\nif rule.properties.schedule_rule_parameters:\\n  inputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters + u\\\";artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\nelse:\\n  inputs.scheduler_rule_parameters = u\\\"artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.object_id = artifact.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p0reen\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yevgyi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p0reen\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zz4wks\"/\u003e\u003cendEvent id=\"EndEvent_0ed1ueg\"\u003e\u003cincoming\u003eSequenceFlow_1yevgyi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1yevgyi\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"EndEvent_0ed1ueg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02uz1py\"\u003e\u003ctext\u003eRule Activity Fields are used for parameter capture\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0tb4n3w\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"TextAnnotation_02uz1py\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_11c1lus\"\u003e\u003ctext\u003eSee Action Status for job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0m0ni5z\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"TextAnnotation_11c1lus\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zz4wks\" id=\"ServiceTask_0zz4wks_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p0reen\" id=\"SequenceFlow_0p0reen_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ed1ueg\" id=\"EndEvent_0ed1ueg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"430\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"448\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yevgyi\" id=\"SequenceFlow_1yevgyi_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02uz1py\" id=\"TextAnnotation_02uz1py_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"148\" x=\"166\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0tb4n3w\" id=\"Association_0tb4n3w_di\"\u003e\u003comgdi:waypoint x=\"292\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_11c1lus\" id=\"TextAnnotation_11c1lus_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"175\" x=\"376\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0m0ni5z\" id=\"Association_0m0ni5z_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Schedule a rule/playbook to run in the future for a given artifact",
      "export_key": "schedule_a_rule_to_run_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928622,
      "name": "Schedule a Rule/Playbook to Run - Artifact",
      "object_type": "artifact",
      "programmatic_name": "schedule_a_rule_to_run_artifact",
      "tags": [],
      "uuid": "7b1758d4-56d2-491e-99c3-15629da18640",
      "workflow_id": 32
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "schedule_a_rule_to_run__task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"schedule_a_rule_to_run__task\" isExecutable=\"true\" name=\"Schedule a Rule/Playbook to Run - Task\"\u003e\u003cdocumentation\u003eSchedule a rule/playbook to run in the future for a given task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tgjqn3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kdk3qk\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nTYPE_LOOKUP = {0: \u0027Incident\u0027, 1: \\\"Task\\\", 4: \\\"Artifact\\\", 5: \\\"Attachment\\\"}\\n\\nif results.success:\\n  job = results.content\\n  row = incident.addRow(\\\"scheduler_rules\\\")\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\\n  row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\\n  row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\\n  row[\u0027schedule\u0027] = job[\u0027value\u0027]\\n  row[\u0027status\u0027] = \u0027Active\u0027\\n  row[\u0027next_run_time\u0027] = job[\u0027next_run_time\u0027]\\n  row[\u0027rule_type\u0027] = TYPE_LOOKUP.get(job[\u0027args\u0027][6], \\\"Datatable\\\")\\n  if job[\u0027args\u0027][8]:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#playbooks/designer/{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\n  else:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#customize?tab=actions\u0026amp;id={}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\nelse:\\n  incident.addNote(\\\"Schedule a Rule/Playbook failed: {}\\\".format(result.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\n\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\ninputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters\\n\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.object_id = task.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tgjqn3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tvzby6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tgjqn3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kdk3qk\"/\u003e\u003cendEvent id=\"EndEvent_0r70nx4\"\u003e\u003cincoming\u003eSequenceFlow_0tvzby6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tvzby6\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"EndEvent_0r70nx4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0umoxay\"\u003e\u003ctext\u003eRule Activity Fields are used for parameter capture\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_06cxn04\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"TextAnnotation_0umoxay\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10gv7bg\"\u003e\u003ctext\u003eSee Action Status for status on job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1bt608b\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"TextAnnotation_10gv7bg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kdk3qk\" id=\"ServiceTask_0kdk3qk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tgjqn3\" id=\"SequenceFlow_1tgjqn3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0r70nx4\" id=\"EndEvent_0r70nx4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"433\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"451\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tvzby6\" id=\"SequenceFlow_0tvzby6_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"402.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0umoxay\" id=\"TextAnnotation_0umoxay_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"187\" x=\"107\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_06cxn04\" id=\"Association_06cxn04_di\"\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10gv7bg\" id=\"TextAnnotation_10gv7bg_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"212\" x=\"390\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1bt608b\" id=\"Association_1bt608b_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"462\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Schedule a rule/playbook to run in the future for a given task",
      "export_key": "schedule_a_rule_to_run__task",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402929165,
      "name": "Schedule a Rule/Playbook to Run - Task",
      "object_type": "task",
      "programmatic_name": "schedule_a_rule_to_run__task",
      "tags": [],
      "uuid": "fdcd87e5-d89c-44e7-bf0c-19d44168439b",
      "workflow_id": 36
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "schedule_rule_to_run",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"schedule_rule_to_run\" isExecutable=\"true\" name=\"Schedule a Rule/Playbook to Run\"\u003e\u003cdocumentation\u003eSchedule a rule/playbook to run in the future for a given incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12g71q0\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0liw2uh\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nTYPE_LOOKUP = {0: \u0027Incident\u0027, 1: \\\"Task\\\", 4: \\\"Artifact\\\", 5: \\\"Attachment\\\"}\\n\\nif results.success:\\n  job = results.content\\n  row = incident.addRow(\\\"scheduler_rules\\\")\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\\n  row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\\n  row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\\n  row[\u0027schedule\u0027] = job[\u0027value\u0027]\\n  row[\u0027status\u0027] = \u0027Active\u0027\\n  row[\u0027next_run_time\u0027] = job[\u0027next_run_time\u0027]\\n  row[\u0027rule_type\u0027] = TYPE_LOOKUP.get(job[\u0027args\u0027][6], \\\"Datatable\\\")\\n  if job[\u0027args\u0027][8]:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#playbooks/designer/{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\n  else:\\n    row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#customize?tab=actions\u0026amp;id={}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\nelse:\\n  incident.addNote(\\\"Schedule a Rule/Playbook failed: {}\\\".format(result.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\ninputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12g71q0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uggzdr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12g71q0\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0liw2uh\"/\u003e\u003cendEvent id=\"EndEvent_0hrx1s1\"\u003e\u003cincoming\u003eSequenceFlow_0uggzdr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0uggzdr\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"EndEvent_0hrx1s1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02f3vem\"\u003e\u003ctext\u003eRule Activity Fields are captured\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03297rc\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"TextAnnotation_02f3vem\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01qvnyn\"\u003e\u003ctext\u003eSee Action Status for result of job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1yf61pf\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"TextAnnotation_01qvnyn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0liw2uh\" id=\"ServiceTask_0liw2uh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12g71q0\" id=\"SequenceFlow_12g71q0_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hrx1s1\" id=\"EndEvent_0hrx1s1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"441\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uggzdr\" id=\"SequenceFlow_0uggzdr_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"410\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02f3vem\" id=\"TextAnnotation_02f3vem_di\"\u003e\u003comgdc:Bounds height=\"72\" width=\"209\" x=\"149\" y=\"44\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03297rc\" id=\"Association_03297rc_di\"\u003e\u003comgdi:waypoint x=\"305\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01qvnyn\" id=\"TextAnnotation_01qvnyn_di\"\u003e\u003comgdc:Bounds height=\"79\" width=\"192\" x=\"409\" y=\"40\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1yf61pf\" id=\"Association_1yf61pf_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Schedule a rule/playbook to run in the future for a given incident",
      "export_key": "schedule_rule_to_run",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928471,
      "name": "Schedule a Rule/Playbook to Run",
      "object_type": "incident",
      "programmatic_name": "schedule_rule_to_run",
      "tags": [],
      "uuid": "88f6f518-2218-482a-a232-2e755acd5e13",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "run_a_scheduled_job_now",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"run_a_scheduled_job_now\" isExecutable=\"true\" name=\"Run a Scheduled Job Now\"\u003e\u003cdocumentation\u003eRun a scheduled job immediately\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0g2ztm4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ezfgmb\" name=\"Run Schedule Job Now\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d35f9fe8-d19b-41fc-adb2-d80bc7b4e68b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.success:\\n  incident.addNote(\\\"Run Scheduled Job Now failed for job {}: {}\\\".format(row[\u0027schedule_label\u0027], results.reason))\\nelse:\\n  msg = \\\"Run Scheduled Job Now suceeeded for job: {}, Rule/Playbook: {}\\\".format(row[\u0027schedule_label\u0027], row[\u0027rule\u0027].content)\\n  incident.addNote(helper.createRichText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.scheduler_label = row[\u0027schedule_label\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0g2ztm4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0x22jsz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0g2ztm4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ezfgmb\"/\u003e\u003cendEvent id=\"EndEvent_1ljp1tu\"\u003e\u003cincoming\u003eSequenceFlow_0x22jsz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0x22jsz\" sourceRef=\"ServiceTask_1ezfgmb\" targetRef=\"EndEvent_1ljp1tu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0h9rnup\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0jdcbld\" sourceRef=\"ServiceTask_1ezfgmb\" targetRef=\"TextAnnotation_0h9rnup\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ezfgmb\" id=\"ServiceTask_1ezfgmb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"261\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0g2ztm4\" id=\"SequenceFlow_0g2ztm4_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"261\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"229.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ljp1tu\" id=\"EndEvent_1ljp1tu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"425\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"443\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0x22jsz\" id=\"SequenceFlow_0x22jsz_di\"\u003e\u003comgdi:waypoint x=\"361\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"425\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0h9rnup\" id=\"TextAnnotation_0h9rnup_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"191\" x=\"340\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0jdcbld\" id=\"Association_0jdcbld_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Run a scheduled job immediately",
      "export_key": "run_a_scheduled_job_now",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928913,
      "name": "Run a Scheduled Job Now",
      "object_type": "scheduler_rules",
      "programmatic_name": "run_a_scheduled_job_now",
      "tags": [],
      "uuid": "7724fc6b-8467-43af-b794-1218cf2499d8",
      "workflow_id": 34
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "list_schedules",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"list_schedules\" isExecutable=\"true\" name=\"List Schedules\"\u003e\u003cdocumentation\u003eList the active schedules\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_028h8nr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0vybqlf\" name=\"Scheduled Rule List\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8972a0b8-7a13-4dee-b6c1-e9ebc389b3d3\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\n\\nTYPE_LOOKUP = {0: \u0027Incident\u0027, 1: \\\"Task\\\", 4: \\\"Artifact\\\", 5: \\\"Attachment\\\"}\\n\\nif not results[\u0027content\u0027]:\\n  row = incident.addRow(\\\"scheduler_rules\\\")\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_label\u0027] = \\\"-- no scheduled rules --\\\"\\nelse:\\n  for job in results[\u0027content\u0027]:\\n    row = incident.addRow(\\\"scheduler_rules\\\")\\n    row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\\n    row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\\n    row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\\n    row[\u0027schedule\u0027] = job[\u0027value\u0027]\\n    row[\u0027reported_on\u0027] = str(Date())\\n    row[\u0027status\u0027] = \u0027Active\u0027 if job[\u0027next_run_time\u0027] else \u0027Paused\u0027\\n    row[\u0027next_run_time\u0027] = job[\u0027next_run_time\u0027]\\n    row[\u0027rule_type\u0027] = TYPE_LOOKUP.get(job[\u0027args\u0027][6], \\\"Datatable\\\")\\n    if job[\u0027args\u0027][8]:\\n      row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#playbooks/designer/{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\n    else:\\n      row[\u0027rule\u0027] = \\\"\u0026lt;a href=\u0027#customize?tab=actions\u0026amp;id={}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(job[\u0027args\u0027][5], job[\u0027args\u0027][4])\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"if rule.properties.incidents_returned == \\\"All\\\":\\n  inputs.incident_id = 0\\nelse:\\n  inputs.incident_id = incident.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_028h8nr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gkodi4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_028h8nr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0vybqlf\"/\u003e\u003cendEvent id=\"EndEvent_02uosbe\"\u003e\u003cincoming\u003eSequenceFlow_1gkodi4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1gkodi4\" sourceRef=\"ServiceTask_0vybqlf\" targetRef=\"EndEvent_02uosbe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13pcegt\"\u003e\u003ctext\u003eDatatable display of active schedules created\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vykydc\" sourceRef=\"ServiceTask_0vybqlf\" targetRef=\"TextAnnotation_13pcegt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vybqlf\" id=\"ServiceTask_0vybqlf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"291\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_028h8nr\" id=\"SequenceFlow_028h8nr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"291\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02uosbe\" id=\"EndEvent_02uosbe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"458\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"476\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gkodi4\" id=\"SequenceFlow_1gkodi4_di\"\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"458\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"424.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13pcegt\" id=\"TextAnnotation_13pcegt_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"209\" x=\"364\" y=\"55\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vykydc\" id=\"Association_1vykydc_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"123\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "List the active schedules",
      "export_key": "list_schedules",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402929056,
      "name": "List Schedules",
      "object_type": "incident",
      "programmatic_name": "list_schedules",
      "tags": [],
      "uuid": "b4252787-8b81-4059-b9b6-24eff399813a",
      "workflow_id": 35
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "remove_a_schedule",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"remove_a_schedule\" isExecutable=\"true\" name=\"Remove a Scheduled Rule/Playbook\"\u003e\u003cdocumentation\u003eRemove a running schedule\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0azazkf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1djv9iw\" name=\"Scheduled Rule Remove\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7df74f5f-1b72-4357-85e3-20372e879b78\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \\\"Deleted\\\"\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0azazkf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ioexmu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0azazkf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1djv9iw\"/\u003e\u003cendEvent id=\"EndEvent_1bh7j2l\"\u003e\u003cincoming\u003eSequenceFlow_0ioexmu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ioexmu\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"EndEvent_1bh7j2l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nypvxm\"\u003e\u003ctext\u003eSee Action Status for job removal\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0i0ze33\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"TextAnnotation_1nypvxm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12gson2\"\u003e\u003ctext\u003eActs on a datatable row of scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1tbaznb\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"TextAnnotation_12gson2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1djv9iw\" id=\"ServiceTask_1djv9iw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"266\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0azazkf\" id=\"SequenceFlow_0azazkf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"266\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"232\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bh7j2l\" id=\"EndEvent_1bh7j2l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"431\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"449\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ioexmu\" id=\"SequenceFlow_0ioexmu_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nypvxm\" id=\"TextAnnotation_1nypvxm_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"251\" x=\"366\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0i0ze33\" id=\"Association_0i0ze33_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12gson2\" id=\"TextAnnotation_12gson2_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"162\" x=\"130\" y=\"65\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1tbaznb\" id=\"Association_1tbaznb_di\"\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"229\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Remove a running schedule",
      "export_key": "remove_a_schedule",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1681402928169,
      "name": "Remove a Scheduled Rule/Playbook",
      "object_type": "scheduler_rules",
      "programmatic_name": "remove_a_schedule",
      "tags": [],
      "uuid": "cec2ea65-b129-40ac-84ab-dec15b645a39",
      "workflow_id": 29
    }
  ],
  "workspaces": []
}
