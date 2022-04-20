{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "List Scheduled Rules",
      "id": 204,
      "logic_type": "all",
      "message_destinations": [],
      "name": "List Scheduled Rules",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "field_name": "scheduler_rules.status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Pause a Scheduled Job",
      "id": 205,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Pause a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "Remove a Scheduled Rule",
      "id": 206,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Remove a Scheduled Rule",
      "object_type": "scheduler_rules",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 207,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Resume a Scheduled Job",
      "object_type": "scheduler_rules",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "conditions": [],
      "enabled": true,
      "export_key": "Schedule a Rule to Run",
      "id": 208,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule to Run",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "Schedule a Rule to Run - Artifact",
      "id": 209,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule to Run - Artifact",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "Schedule a Rule to Run - Task",
      "id": 210,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Schedule a Rule to Run - Task",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
  "export_date": 1650485908570,
  "export_format_version": 2,
  "fields": [
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
      "id": 267,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        },
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        },
        {
          "tag_handle": "fn_relations",
          "value": null
        },
        {
          "tag_handle": "fn_scheduler",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
      "export_key": "__function/object_id",
      "hide_notification": false,
      "id": 1583,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1584,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1578,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "__function/scheduler_rule_name",
      "hide_notification": false,
      "id": 1579,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "templates": [],
      "text": "scheduler_rule_name",
      "tooltip": "Name of rule to schedule",
      "type_id": 11,
      "uuid": "bfacefb1-5b39-4e7f-919c-84ccc54442f0",
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
      "export_key": "__function/scheduler_type",
      "hide_notification": false,
      "id": 1580,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "value": 2109
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "422ba5d3-1f82-4199-bb51-773cfd56dedb",
          "value": 2110
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "ff3beed4-6f48-43fd-b5d4-c389e76c4d2f",
          "value": 2111
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "f1289cbb-b0ff-4027-a6f8-af40bb474910",
          "value": 2112
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
      "id": 1577,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1581,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "__function/scheduler_type_value",
      "hide_notification": false,
      "id": 1582,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1585,
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
      "id": 1573,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1574,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "id": 1586,
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
      "id": 1571,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "templates": [],
      "text": "Schedule Type",
      "tooltip": "Type of schedule to create",
      "type_id": 6,
      "uuid": "d5741a0f-b6ce-43a4-a158-a19989559cfe",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "deltax",
          "properties": null,
          "uuid": "5a12bad2-5a03-4dd1-ba66-3b22891aa08a",
          "value": 2102
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "cron",
          "properties": null,
          "uuid": "4dc8293e-0937-4130-b1cf-b501bb0d7afe",
          "value": 2103
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "interval",
          "properties": null,
          "uuid": "29774e73-d19c-4c24-b41b-8ebcf27f2c53",
          "value": 2104
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "date",
          "properties": null,
          "uuid": "2712d0fe-9a1d-4c9d-8fd0-47490c6ec11d",
          "value": 2105
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "delta",
          "properties": null,
          "uuid": "19dbfc0f-ce1d-49ea-a11b-c0de3fec5e5f",
          "value": 2106
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
      "id": 1575,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "templates": [],
      "text": "Schedule Type Value",
      "tooltip": "cron (* 5 * * *); date (yyyy/mm/dd hh:mm:ss) ; interval (10m)",
      "type_id": 6,
      "uuid": "db501928-ffbb-4e2d-8e46-a3dab6eba44c",
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
      "export_key": "actioninvocation/schedule_label_prefix",
      "hide_notification": false,
      "id": 1572,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
      "export_key": "actioninvocation/incidents_returned",
      "hide_notification": false,
      "id": 1576,
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "value": 2107
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "This incident only",
          "properties": null,
          "uuid": "43a22bb9-7079-4901-8b1c-c235e13e7375",
          "value": 2108
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
      "created_date": 1650484103365,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Schedule a rule to run on a schedule. This rule will be executed for a given incident, artifact, task, etc.",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Create",
      "export_key": "create_a_scheduled_rule",
      "id": 282,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1650484171747,
      "name": "create_a_scheduled_rule",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "bde7b5b2-f454-4435-9103-de31d991b924",
      "version": 2,
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
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "name": "Schedule a Rule to Run",
          "object_type": "incident",
          "programmatic_name": "schedule_rule_to_run",
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 174
        },
        {
          "actions": [],
          "description": null,
          "name": "Schedule a Rule to Run - Artifact",
          "object_type": "artifact",
          "programmatic_name": "schedule_a_rule_to_run_artifact",
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 177
        },
        {
          "actions": [],
          "description": null,
          "name": "Schedule a Rule to Run - Task",
          "object_type": "task",
          "programmatic_name": "schedule_a_rule_to_run__task",
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 172
        }
      ]
    },
    {
      "created_date": 1650484103477,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "List the schedules presently defined",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule List",
      "export_key": "list_scheduled_rules",
      "id": 283,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1650484103539,
      "name": "list_scheduled_rules",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "8972a0b8-7a13-4dee-b6c1-e9ebc389b3d3",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 171
        }
      ]
    },
    {
      "created_date": 1650484103563,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Stop a schedule",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Remove",
      "export_key": "remove_a_scheduled_rule",
      "id": 284,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1650484103626,
      "name": "remove_a_scheduled_rule",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "name": "Remove a Scheduled Rule",
          "object_type": "scheduler_rules",
          "programmatic_name": "remove_a_schedule",
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 176
        }
      ]
    },
    {
      "created_date": 1650484103651,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Pause a scheduled rule",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Pause",
      "export_key": "scheduled_rule_pause",
      "id": 285,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1650484103711,
      "name": "scheduled_rule_pause",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 175
        }
      ]
    },
    {
      "created_date": 1650484103735,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Resume a scheduled job",
        "format": "text"
      },
      "destination_handle": "fn_scheduler",
      "display_name": "Scheduled Rule Resume",
      "export_key": "scheduled_rule_resume",
      "id": 286,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1650484103795,
      "name": "scheduled_rule_resume",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
          "tags": [
            {
              "tag_handle": "fn_scheduler",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 173
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 70,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1650485907502,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1650485907502,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "9d0c37de-6d9d-4d5d-b9aa-ea7a4d350bc5"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_scheduler",
      "name": "fn_scheduler",
      "programmatic_name": "fn_scheduler",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "02927d03-a71c-4662-9520-4010fa2ac284"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 41,
    "major": 41,
    "minor": 2,
    "version": "41.2.41"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Scheduler Rules",
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
          "id": 1564,
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
          "type_id": 1026,
          "uuid": "9970f30f-bd88-41e2-aab5-87c480a2238e",
          "values": [],
          "width": 73
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
          "id": 1565,
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
          "type_id": 1026,
          "uuid": "4c46d03a-1025-496a-8560-e9b637e58fd2",
          "values": [],
          "width": 127
        },
        "rule": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/rule",
          "hide_notification": false,
          "id": 1566,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "rule",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Rule",
          "tooltip": "",
          "type_id": 1026,
          "uuid": "e9b42f63-41a3-4782-9d2f-585fd9f2e537",
          "values": [],
          "width": 124
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
          "id": 1567,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "schedule",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Schedule",
          "tooltip": "",
          "type_id": 1026,
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
          "id": 1568,
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
          "type_id": 1026,
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
          "id": 1569,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "schedule_type",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Schedule Type",
          "tooltip": "",
          "type_id": 1026,
          "uuid": "9eaa03ac-6b52-4eec-b9cd-69b6dbf4b893",
          "values": [],
          "width": 53
        },
        "status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "scheduler_rules/status",
          "hide_notification": false,
          "id": 1570,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1026,
          "uuid": "a6f4384a-78d6-4b48-bcb6-40e5cc1c4d9b",
          "values": [],
          "width": 34
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
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
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
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"resume_a_scheduled_job\" isExecutable=\"true\" name=\"Resume a Scheduled Job\"\u003e\u003cdocumentation\u003eResume a Scheduled Job\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lgsip6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1z0kxqu\" name=\"Scheduled Rule Resume\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"37083e99-ca31-41fb-85b5-d0ac4ed1f60b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \u0027Active\u0027\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lgsip6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0su016m\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lgsip6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1z0kxqu\"/\u003e\u003cendEvent id=\"EndEvent_1157mca\"\u003e\u003cincoming\u003eSequenceFlow_0su016m\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0su016m\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"EndEvent_1157mca\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eggn77\"\u003e\u003ctext\u003eActs on a datatable row of scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15nfoj0\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"TextAnnotation_0eggn77\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_139h4an\"\u003e\u003ctext\u003eRow is updated to indicate that the scheduled rule is now active\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1k45r8j\" sourceRef=\"ServiceTask_1z0kxqu\" targetRef=\"TextAnnotation_139h4an\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1z0kxqu\" id=\"ServiceTask_1z0kxqu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lgsip6\" id=\"SequenceFlow_1lgsip6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"243.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1157mca\" id=\"EndEvent_1157mca_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"474\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"492\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0su016m\" id=\"SequenceFlow_0su016m_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"474\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"431.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eggn77\" id=\"TextAnnotation_0eggn77_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"139\" x=\"163\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15nfoj0\" id=\"Association_15nfoj0_di\"\u003e\u003comgdi:waypoint x=\"297\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_139h4an\" id=\"TextAnnotation_139h4an_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"187\" x=\"396\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1k45r8j\" id=\"Association_1k45r8j_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Resume a Scheduled Job",
      "export_key": "resume_a_scheduled_job",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484104671,
      "name": "Resume a Scheduled Job",
      "object_type": "scheduler_rules",
      "programmatic_name": "resume_a_scheduled_job",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "f9ebf3f3-acd2-4450-a0c3-b12de9213e44",
      "workflow_id": 173
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "schedule_a_rule_to_run__task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"schedule_a_rule_to_run__task\" isExecutable=\"true\" name=\"Schedule a Rule to Run - Task\"\u003e\u003cdocumentation\u003eSchedule a rule to run in the future for a given task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tgjqn3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kdk3qk\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\n\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\ninputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters\\n\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.object_id = task.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tgjqn3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tvzby6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tgjqn3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kdk3qk\"/\u003e\u003cendEvent id=\"EndEvent_0r70nx4\"\u003e\u003cincoming\u003eSequenceFlow_0tvzby6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tvzby6\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"EndEvent_0r70nx4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0umoxay\"\u003e\u003ctext\u003eRule Activity Fields are used for parameter capture\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_06cxn04\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"TextAnnotation_0umoxay\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10gv7bg\"\u003e\u003ctext\u003eSee Action Status for status on job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1bt608b\" sourceRef=\"ServiceTask_0kdk3qk\" targetRef=\"TextAnnotation_10gv7bg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kdk3qk\" id=\"ServiceTask_0kdk3qk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tgjqn3\" id=\"SequenceFlow_1tgjqn3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0r70nx4\" id=\"EndEvent_0r70nx4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"433\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"451\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tvzby6\" id=\"SequenceFlow_0tvzby6_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"402.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0umoxay\" id=\"TextAnnotation_0umoxay_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"187\" x=\"107\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_06cxn04\" id=\"Association_06cxn04_di\"\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10gv7bg\" id=\"TextAnnotation_10gv7bg_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"212\" x=\"390\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1bt608b\" id=\"Association_1bt608b_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"462\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "a@example.com",
      "description": "Schedule a rule to run in the future for a given task",
      "export_key": "schedule_a_rule_to_run__task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484398811,
      "name": "Schedule a Rule to Run - Task",
      "object_type": "task",
      "programmatic_name": "schedule_a_rule_to_run__task",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "fdcd87e5-d89c-44e7-bf0c-19d44168439b",
      "workflow_id": 172
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "pause_a_scheduled_job",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pause_a_scheduled_job\" isExecutable=\"true\" name=\"Pause a Scheduled Job\"\u003e\u003cdocumentation\u003ePause a scheduled job\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0r2ecr9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1jp2yxe\" name=\"Scheduled Rule Pause\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"aa278752-98c2-4866-b477-0eb19fd81b34\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \u0027Paused\u0027\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\\n\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0r2ecr9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ercxlc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0r2ecr9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1jp2yxe\"/\u003e\u003cendEvent id=\"EndEvent_1bza8l8\"\u003e\u003cincoming\u003eSequenceFlow_1ercxlc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ercxlc\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"EndEvent_1bza8l8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0kcja56\"\u003e\u003ctext\u003eActs on a given datatable row for scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1rfy0g0\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"TextAnnotation_0kcja56\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1sbpec1\"\u003e\u003ctext\u003eRow is updated to indicate that the rule is paused\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10i22at\" sourceRef=\"ServiceTask_1jp2yxe\" targetRef=\"TextAnnotation_1sbpec1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1jp2yxe\" id=\"ServiceTask_1jp2yxe_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"262\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r2ecr9\" id=\"SequenceFlow_0r2ecr9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"230\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bza8l8\" id=\"EndEvent_1bza8l8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"435\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ercxlc\" id=\"SequenceFlow_1ercxlc_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0kcja56\" id=\"TextAnnotation_0kcja56_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"140\" x=\"150\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1rfy0g0\" id=\"Association_1rfy0g0_di\"\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1sbpec1\" id=\"TextAnnotation_1sbpec1_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"182\" x=\"361\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10i22at\" id=\"Association_10i22at_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"409\" xsi:type=\"omgdc:Point\" y=\"140\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Pause a scheduled job",
      "export_key": "pause_a_scheduled_job",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484105093,
      "name": "Pause a Scheduled Job",
      "object_type": "scheduler_rules",
      "programmatic_name": "pause_a_scheduled_job",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "b7c4e77c-b02d-47c7-9853-d8972ead8a96",
      "workflow_id": 175
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "list_schedules",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"list_schedules\" isExecutable=\"true\" name=\"List Schedules\"\u003e\u003cdocumentation\u003eList the active schedules\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_028h8nr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0vybqlf\" name=\"Scheduled Rule List\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8972a0b8-7a13-4dee-b6c1-e9ebc389b3d3\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nif not results[\u0027content\u0027]:\\n  row = incident.addRow(\\\"scheduler_rules\\\")\\n  row[\u0027reported_on\u0027] = str(Date())\\n  row[\u0027schedule_label\u0027] = \\\"-- no scheduled rules --\\\"\\nelse:\\n  for job in results[\u0027content\u0027]:\\n    row = incident.addRow(\\\"scheduler_rules\\\")\\n    row[\u0027schedule_label\u0027] = job[\u0027id\u0027]\\n    row[\u0027schedule_type\u0027] = job[\u0027type\u0027]\\n    row[\u0027incident_id\u0027] = job[\u0027args\u0027][0]\\n    row[\u0027rule\u0027] = job[\u0027args\u0027][4]\\n    row[\u0027schedule\u0027] = job[\u0027value\u0027]\\n    row[\u0027reported_on\u0027] = str(Date())\\n    row[\u0027status\u0027] = \u0027Active\u0027 if job[\u0027next_run_time\u0027] else \u0027Paused\u0027\\n    \",\"pre_processing_script\":\"if rule.properties.incidents_returned == \\\"All\\\":\\n  inputs.incident_id = 0\\nelse:\\n  inputs.incident_id = incident.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_028h8nr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gkodi4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_028h8nr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0vybqlf\"/\u003e\u003cendEvent id=\"EndEvent_02uosbe\"\u003e\u003cincoming\u003eSequenceFlow_1gkodi4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1gkodi4\" sourceRef=\"ServiceTask_0vybqlf\" targetRef=\"EndEvent_02uosbe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13pcegt\"\u003e\u003ctext\u003eDatatable display of active schedules created\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vykydc\" sourceRef=\"ServiceTask_0vybqlf\" targetRef=\"TextAnnotation_13pcegt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vybqlf\" id=\"ServiceTask_0vybqlf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"291\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_028h8nr\" id=\"SequenceFlow_028h8nr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"291\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02uosbe\" id=\"EndEvent_02uosbe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"458\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"476\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gkodi4\" id=\"SequenceFlow_1gkodi4_di\"\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"458\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"424.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13pcegt\" id=\"TextAnnotation_13pcegt_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"209\" x=\"364\" y=\"55\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vykydc\" id=\"Association_1vykydc_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"123\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "List the active schedules",
      "export_key": "list_schedules",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484104252,
      "name": "List Schedules",
      "object_type": "incident",
      "programmatic_name": "list_schedules",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "b4252787-8b81-4059-b9b6-24eff399813a",
      "workflow_id": 171
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "schedule_a_rule_to_run_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"schedule_a_rule_to_run_artifact\" isExecutable=\"true\" name=\"Schedule a Rule to Run - Artifact\"\u003e\u003cdocumentation\u003eSchedule a rule to run in the future for a given artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p0reen\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zz4wks\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\nif rule.properties.schedule_rule_parameters:\\n  inputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters + u\\\";artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\nelse:\\n  inputs.scheduler_rule_parameters = u\\\"artifact_type={};artifact_value={}\\\".format(artifact.type, artifact.value)\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.object_id = artifact.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p0reen\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yevgyi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p0reen\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zz4wks\"/\u003e\u003cendEvent id=\"EndEvent_0ed1ueg\"\u003e\u003cincoming\u003eSequenceFlow_1yevgyi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1yevgyi\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"EndEvent_0ed1ueg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02uz1py\"\u003e\u003ctext\u003eRule Activity Fields are used for parameter capture\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0tb4n3w\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"TextAnnotation_02uz1py\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_11c1lus\"\u003e\u003ctext\u003eSee Action Status for job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0m0ni5z\" sourceRef=\"ServiceTask_0zz4wks\" targetRef=\"TextAnnotation_11c1lus\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zz4wks\" id=\"ServiceTask_0zz4wks_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p0reen\" id=\"SequenceFlow_0p0reen_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ed1ueg\" id=\"EndEvent_0ed1ueg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"430\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"448\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yevgyi\" id=\"SequenceFlow_1yevgyi_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02uz1py\" id=\"TextAnnotation_02uz1py_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"148\" x=\"166\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0tb4n3w\" id=\"Association_0tb4n3w_di\"\u003e\u003comgdi:waypoint x=\"292\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_11c1lus\" id=\"TextAnnotation_11c1lus_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"175\" x=\"376\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0m0ni5z\" id=\"Association_0m0ni5z_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "a@example.com",
      "description": "Schedule a rule to run in the future for a given artifact",
      "export_key": "schedule_a_rule_to_run_artifact",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484382097,
      "name": "Schedule a Rule to Run - Artifact",
      "object_type": "artifact",
      "programmatic_name": "schedule_a_rule_to_run_artifact",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "7b1758d4-56d2-491e-99c3-15629da18640",
      "workflow_id": 177
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "schedule_rule_to_run",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"schedule_rule_to_run\" isExecutable=\"true\" name=\"Schedule a Rule to Run\"\u003e\u003cdocumentation\u003eSchedule a rule to run in the future for a given incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12g71q0\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0liw2uh\" name=\"Scheduled Rule Create\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bde7b5b2-f454-4435-9103-de31d991b924\"\u003e{\"inputs\":{\"0e1330b2-0b91-462b-acf2-2772a02299f8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"eb8f0588-a416-4bf9-9154-665ed20bcdf9\"}}},\"pre_processing_script\":\"inputs.scheduler_type = rule.properties.schedule_type\\nif rule.properties.schedule_type == \u0027date\u0027:\\n  # date format converted to use dashes\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value.replace(\\\"/\\\", \\\"-\\\")\\nelse:\\n  inputs.scheduler_type_value = rule.properties.schedule_type_value\\ninputs.scheduler_rule_name = rule.properties.schedule_rule_name\\ninputs.scheduler_rule_parameters = rule.properties.schedule_rule_parameters\\ninputs.scheduler_label_prefix = rule.properties.schedule_label_prefix\\ninputs.incident_id = incident.id\\ninputs.scheduler_is_playbook = rule.properties.schedule_is_playbook\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12g71q0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uggzdr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12g71q0\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0liw2uh\"/\u003e\u003cendEvent id=\"EndEvent_0hrx1s1\"\u003e\u003cincoming\u003eSequenceFlow_0uggzdr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0uggzdr\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"EndEvent_0hrx1s1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02f3vem\"\u003e\u003ctext\u003eRule Activity Fields are captured\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03297rc\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"TextAnnotation_02f3vem\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01qvnyn\"\u003e\u003ctext\u003eSee Action Status for result of job creation\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1yf61pf\" sourceRef=\"ServiceTask_0liw2uh\" targetRef=\"TextAnnotation_01qvnyn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0liw2uh\" id=\"ServiceTask_0liw2uh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12g71q0\" id=\"SequenceFlow_12g71q0_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hrx1s1\" id=\"EndEvent_0hrx1s1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"441\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uggzdr\" id=\"SequenceFlow_0uggzdr_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"410\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02f3vem\" id=\"TextAnnotation_02f3vem_di\"\u003e\u003comgdc:Bounds height=\"72\" width=\"209\" x=\"149\" y=\"44\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03297rc\" id=\"Association_03297rc_di\"\u003e\u003comgdi:waypoint x=\"305\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01qvnyn\" id=\"TextAnnotation_01qvnyn_di\"\u003e\u003comgdc:Bounds height=\"79\" width=\"192\" x=\"409\" y=\"40\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1yf61pf\" id=\"Association_1yf61pf_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "a@example.com",
      "description": "Schedule a rule to run in the future for a given incident",
      "export_key": "schedule_rule_to_run",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484364117,
      "name": "Schedule a Rule to Run",
      "object_type": "incident",
      "programmatic_name": "schedule_rule_to_run",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "88f6f518-2218-482a-a232-2e755acd5e13",
      "workflow_id": 174
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "remove_a_schedule",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"remove_a_schedule\" isExecutable=\"true\" name=\"Remove a Scheduled Rule\"\u003e\u003cdocumentation\u003eRemove a running schedule\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0azazkf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1djv9iw\" name=\"Scheduled Rule Remove\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7df74f5f-1b72-4357-85e3-20372e879b78\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  row[\u0027status\u0027] = \\\"Deleted\\\"\\nelse:\\n  row[\u0027status\u0027] = row[\u0027status\u0027] + \\\" (Error)\\\"\",\"pre_processing_script\":\"inputs.scheduler_label = row.schedule_label\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0azazkf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ioexmu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0azazkf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1djv9iw\"/\u003e\u003cendEvent id=\"EndEvent_1bh7j2l\"\u003e\u003cincoming\u003eSequenceFlow_0ioexmu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ioexmu\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"EndEvent_1bh7j2l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nypvxm\"\u003e\u003ctext\u003eSee Action Status for job removal\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0i0ze33\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"TextAnnotation_1nypvxm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12gson2\"\u003e\u003ctext\u003eActs on a datatable row of scheduled rules\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1tbaznb\" sourceRef=\"ServiceTask_1djv9iw\" targetRef=\"TextAnnotation_12gson2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1djv9iw\" id=\"ServiceTask_1djv9iw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"266\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0azazkf\" id=\"SequenceFlow_0azazkf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"266\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"232\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bh7j2l\" id=\"EndEvent_1bh7j2l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"431\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"449\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ioexmu\" id=\"SequenceFlow_0ioexmu_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nypvxm\" id=\"TextAnnotation_1nypvxm_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"251\" x=\"366\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0i0ze33\" id=\"Association_0i0ze33_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12gson2\" id=\"TextAnnotation_12gson2_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"162\" x=\"130\" y=\"65\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1tbaznb\" id=\"Association_1tbaznb_di\"\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"229\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Remove a running schedule",
      "export_key": "remove_a_schedule",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1650484105296,
      "name": "Remove a Scheduled Rule",
      "object_type": "scheduler_rules",
      "programmatic_name": "remove_a_schedule",
      "tags": [
        {
          "tag_handle": "fn_scheduler",
          "value": null
        }
      ],
      "uuid": "cec2ea65-b129-40ac-84ab-dec15b645a39",
      "workflow_id": 176
    }
  ],
  "workspaces": []
}
