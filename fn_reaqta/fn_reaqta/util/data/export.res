{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_id",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_summary",
          "method": "not_contains",
          "type": null,
          "value": "Closed by ReaQta"
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Close Alert",
      "id": 161,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Close Alert",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "acc342e1-a1c7-4eba-aa13-9e00ea753515",
      "view_items": [],
      "workflows": [
        "reaqta_close_alert"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Artifact from Process Path",
      "id": 162,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Artifact from Process Path",
      "object_type": "reaqta_process_list",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e7b09e04-9576-422b-ad01-63d283ee018a",
      "view_items": [],
      "workflows": [
        "reaqta_create_artifact_from_process_path"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "reaqta_trigger_events.program_path",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Artifact from Trigger Event",
      "id": 163,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Artifact from Trigger Event",
      "object_type": "reaqta_trigger_events",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "c39476d7-49e6-4a6e-8bde-ee8cfc13d9c7",
      "view_items": [],
      "workflows": [
        "reaqta_create_artifact_from_trigger_event"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Attachment from Process List",
      "id": 164,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Attachment from Process List",
      "object_type": "reaqta_process_list",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "30da5104-ef54-42d3-978e-4e68b57c7e04",
      "view_items": [],
      "workflows": [
        "reaqta_attach_file_from_process_list"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "reaqta_trigger_events.program_path",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Attachment from Triggered Event",
      "id": 165,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Attachment from Triggered Event",
      "object_type": "reaqta_trigger_events",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "827e49e1-8850-4524-82cc-89e679bf9ccf",
      "view_items": [],
      "workflows": [
        "reaqta_attach_file_from_triggered_events"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "ReaQta"
        },
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Note",
      "id": 166,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Note",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "aff66bed-f73d-427b-b6c5-84c2aaafe503",
      "view_items": [],
      "workflows": [
        "reaqta_create_note"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-256 Hash"
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Create Policy from Artifact",
      "id": 160,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Policy from Artifact",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "143c8b3c-2100-4958-97ca-b19dac138480",
      "view_items": [
        {
          "content": "Policy Settings",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "401eb0a4-50bd-4108-8dd2-ee91e7920801",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c5965e9-c316-4751-816c-b43b2493ead9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4ee39c15-38ef-4289-a934-20f60ae240f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d95602fa-01a4-411f-8d29-411cd6833caf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a6b69a85-21b5-4587-905e-bbfec8552c18",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5a8d3f2a-ee44-4665-83c0-514e3b492343",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7ae5b9d2-3cd8-487e-a888-b236ea01d691",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "reaqta_create_policy_from_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ReaQta: Create Policy on Triggered Event",
      "id": 167,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Create Policy on Triggered Event",
      "object_type": "reaqta_trigger_events",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0b1897db-dcaf-4609-8891-29e2e4685323",
      "view_items": [
        {
          "content": "Policy Settings",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c5965e9-c316-4751-816c-b43b2493ead9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4ee39c15-38ef-4289-a934-20f60ae240f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d95602fa-01a4-411f-8d29-411cd6833caf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a6b69a85-21b5-4587-905e-bbfec8552c18",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5a8d3f2a-ee44-4665-83c0-514e3b492343",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7ae5b9d2-3cd8-487e-a888-b236ea01d691",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "reaqta_create_policy_on_triggered_event"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_hive",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Get Alert Information",
      "id": 168,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Get Alert Information",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "d759bf21-6d25-4bdf-9545-207628cd5ae5",
      "view_items": [],
      "workflows": [
        "reaqta_get_alert_information"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Get Processes",
      "id": 169,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Get Processes",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "90679895-3e4b-437c-9116-410f8fdba158",
      "view_items": [
        {
          "content": "c436aa5f-80a7-4683-bb22-4cd4f075870d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f4c77bb2-eeae-49b1-8195-03320541f74a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "reaqta_get_processes"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Isolate Endpoint",
      "id": 170,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Isolate Endpoint",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d8450a68-0ff2-46ab-9742-b5b8b857849d",
      "view_items": [
        {
          "content": "Confirm Endpoint Isolation?",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "reaqta_isolate_endpoint"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "reaqta_process_list.pid",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Kill Process",
      "id": 171,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Kill Process",
      "object_type": "reaqta_process_list",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "20590bab-c8c1-40ed-895c-60379a3387ac",
      "view_items": [
        {
          "content": "Confirm Process Kill?",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "reaqta_kill_process"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647546271808,
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
      "export_key": "__function/reaqta_hive",
      "hide_notification": false,
      "id": 1270,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_hive",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "reaqta_hive",
      "tooltip": "Label used to identify which ReaQta hive this alert is associated with",
      "type_id": 11,
      "uuid": "8328e505-3176-4864-b179-7da5dc9e9251",
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
      "export_key": "__function/reaqta_note",
      "hide_notification": false,
      "id": 1252,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_note",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_note",
      "tooltip": "",
      "type_id": 11,
      "uuid": "974101e4-0904-4bc8-abd1-a34f163be445",
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
      "export_key": "__function/reaqta_program_path",
      "hide_notification": false,
      "id": 1253,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_program_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_program_path",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a67fc10f-bec1-4915-b4bb-e4b6ce6a8456",
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
      "export_key": "__function/reaqta_policy_excluded_groups",
      "hide_notification": false,
      "id": 1066,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_excluded_groups",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_excluded_groups",
      "tooltip": "Comma separated list of excluded groups for this policy",
      "type_id": 11,
      "uuid": "c5e6f2d1-cb47-4801-965a-dcf86fd3fa7d",
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
      "export_key": "__function/reaqta_sha256",
      "hide_notification": false,
      "id": 1062,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_sha256",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_sha256",
      "tooltip": "Program file sh256 hash",
      "type_id": 11,
      "uuid": "c72e88df-ec5e-4078-b7d9-3b4bb422f9cb",
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
      "export_key": "__function/reaqta_is_malicious",
      "hide_notification": false,
      "id": 1254,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_is_malicious",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_is_malicious",
      "tooltip": "",
      "type_id": 11,
      "uuid": "cd0bea42-4e4f-46d0-9a68-ad1822a02014",
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
      "export_key": "__function/reaqta_incident_id",
      "hide_notification": false,
      "id": 1255,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d587ce18-7232-448f-98a7-23babb4b6e62",
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
      "export_key": "__function/reaqta_policy_description",
      "hide_notification": false,
      "id": 1064,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ecc14545-92fc-4272-8b46-b589e20ab01b",
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
      "export_key": "__function/reaqta_policy_enabled",
      "hide_notification": false,
      "id": 1067,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_enabled",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_enabled",
      "tooltip": "Enable/disable policy when created",
      "type_id": 11,
      "uuid": "f40af3ea-ba5f-4d96-8149-7e8c80cb7cc5",
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
      "export_key": "__function/reaqta_policy_title",
      "hide_notification": false,
      "id": 1063,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_title",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0d93e3ef-6249-4566-a1e2-bb8ba43277f1",
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
      "export_key": "__function/reaqta_policy_block",
      "hide_notification": false,
      "id": 1068,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_block",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_block",
      "tooltip": "Yes - Block hash, No - Create alert only",
      "type_id": 11,
      "uuid": "3658c33e-a7f6-4eef-b899-abd9f5c57446",
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
      "export_key": "__function/reaqta_starttime",
      "hide_notification": false,
      "id": 1256,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_starttime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_starttime",
      "tooltip": "",
      "type_id": 11,
      "uuid": "48ae8d4f-7cd3-49bd-b370-2bc878003aa3",
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
      "export_key": "__function/reaqta_process_pid",
      "hide_notification": false,
      "id": 1257,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_process_pid",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_process_pid",
      "tooltip": "",
      "type_id": 11,
      "uuid": "577df2a5-6b20-4828-a3a9-da6f3446dee5",
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
      "export_key": "__function/reaqta_endpoint_id",
      "hide_notification": false,
      "id": 1258,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_endpoint_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_endpoint_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
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
      "export_key": "__function/reaqta_artifact_type",
      "hide_notification": false,
      "id": 1259,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Malware Sample",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5b379be4-15dd-4f7c-b219-6c973464bf9e",
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
      "export_key": "__function/reaqta_alert_id",
      "hide_notification": false,
      "id": 1260,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_alert_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "66e6a8cc-1c5e-4f72-82cc-1a7198442c91",
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
      "export_key": "__function/reaqta_has_incident",
      "hide_notification": false,
      "id": 1261,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_has_incident",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_has_incident",
      "tooltip": "Select only processes associated with an incident",
      "type_id": 11,
      "uuid": "705674a2-6e43-49be-bcce-5235a82e3508",
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
      "export_key": "__function/reaqta_suspended",
      "hide_notification": false,
      "id": 1262,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_suspended",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_suspended",
      "tooltip": "Select only processes which are suspended",
      "type_id": 11,
      "uuid": "7066af79-2b00-4cc7-87a3-1cad073c7544",
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
      "export_key": "__function/reaqta_policy_included_groups",
      "hide_notification": false,
      "id": 1065,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_included_groups",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "reaqta_policy_included_groups",
      "tooltip": "Comma separated list of included groups for this policy",
      "type_id": 11,
      "uuid": "712d96a6-9d8f-4c50-86b5-ee97edd8ec88",
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
      "export_key": "actioninvocation/reaqta_policy_excluded_groups",
      "hide_notification": false,
      "id": 1072,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_excluded_groups",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Specify groups which will not trigger this policy",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Excluded Groups",
      "tooltip": "Comma separated list of groups to exclude in policy",
      "type_id": 6,
      "uuid": "a6b69a85-21b5-4587-905e-bbfec8552c18",
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
      "export_key": "actioninvocation/reaqta_has_incident",
      "hide_notification": false,
      "id": 1250,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_has_incident",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Has Incident",
      "tooltip": "Select only processes associated with an Alert",
      "type_id": 6,
      "uuid": "c436aa5f-80a7-4683-bb22-4cd4f075870d",
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
      "export_key": "actioninvocation/reaqta_policy_included_groups",
      "hide_notification": false,
      "id": 1071,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_included_groups",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Specify groups which will trigger this policy",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Included Groups",
      "tooltip": "Comma separated list of groups to include in policy",
      "type_id": 6,
      "uuid": "d95602fa-01a4-411f-8d29-411cd6833caf",
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
      "export_key": "actioninvocation/reaqta_suspended",
      "hide_notification": false,
      "id": 1251,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_suspended",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Suspended",
      "tooltip": "Select only processes which are suspended",
      "type_id": 6,
      "uuid": "f4c77bb2-eeae-49b1-8195-03320541f74a",
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
      "export_key": "actioninvocation/reaqta_policy_title",
      "hide_notification": false,
      "id": 1069,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Title",
      "tooltip": "",
      "type_id": 6,
      "uuid": "0c5965e9-c316-4751-816c-b43b2493ead9",
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
      "export_key": "actioninvocation/reaqta_hive",
      "hide_notification": false,
      "id": 1271,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_hive",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Hive Label",
      "tooltip": "Specify label of ReaQta configured environment or empty for default",
      "type_id": 6,
      "uuid": "401eb0a4-50bd-4108-8dd2-ee91e7920801",
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
      "export_key": "actioninvocation/reaqta_policy_description",
      "hide_notification": false,
      "id": 1070,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Description",
      "tooltip": "",
      "type_id": 6,
      "uuid": "4ee39c15-38ef-4289-a934-20f60ae240f3",
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
      "export_key": "actioninvocation/reaqta_policy_enabled",
      "hide_notification": false,
      "id": 1073,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_enabled",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Enable",
      "tooltip": "Yes - enable, No - disable",
      "type_id": 6,
      "uuid": "5a8d3f2a-ee44-4665-83c0-514e3b492343",
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
      "export_key": "actioninvocation/reaqta_policy_block_when_triggered",
      "hide_notification": false,
      "id": 1074,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_policy_block_when_triggered",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "Block when Triggered",
      "tooltip": "Yes - block file, No - create alert only",
      "type_id": 6,
      "uuid": "7ae5b9d2-3cd8-487e-a888-b236ea01d691",
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
      "export_key": "incident/reaqta_endpoint_id",
      "hide_notification": false,
      "id": 1023,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_endpoint_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Endpoint ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "83381df6-c68a-4f9b-a0d3-9b90882e470f",
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
      "export_key": "incident/reaqta_groups",
      "hide_notification": false,
      "id": 1033,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_groups",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Groups",
      "tooltip": "",
      "type_id": 0,
      "uuid": "954eef3e-3b53-46a2-93c3-58e8135bbb82",
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
      "export_key": "incident/reaqta_trigger_condition",
      "hide_notification": false,
      "id": 1075,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_trigger_condition",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Trigger Condition",
      "tooltip": "",
      "type_id": 0,
      "uuid": "bbed21b9-66fb-4701-bcdc-3901d9d0881f",
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
      "export_key": "incident/reaqta_tags",
      "hide_notification": false,
      "id": 1021,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Tags",
      "tooltip": "",
      "type_id": 0,
      "uuid": "c3cc70b5-e5a5-443b-9e31-f594adb2c79e",
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
      "export_key": "incident/reaqta_alert_link",
      "hide_notification": false,
      "id": 1022,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_alert_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Alert Link",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e39872e3-10c7-45b4-9512-086e0f34e776",
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
      "export_key": "incident/reaqta_id",
      "hide_notification": false,
      "id": 1020,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Alert ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "015cec48-c34c-4bc9-a826-3c557f014d4a",
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
      "export_key": "incident/reaqta_machine_info",
      "hide_notification": false,
      "id": 1037,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_machine_info",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Machine Info",
      "tooltip": "",
      "type_id": 0,
      "uuid": "121920cf-fee4-4b31-b48d-133b81f30d6a",
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
      "export_key": "incident/reaqta_hive",
      "hide_notification": false,
      "id": 1269,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_hive",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ReaQta Hive",
      "tooltip": "ReaQta hive reference when multiple hives are present",
      "type_id": 0,
      "uuid": "34e62fcc-49a8-4aaf-af3e-c95f9f3b0ce0",
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
      "export_key": "incident/reaqta_impact",
      "hide_notification": false,
      "id": 1268,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "reaqta_impact",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "templates": [],
      "text": "ReaQta Impact",
      "tooltip": "",
      "type_id": 0,
      "uuid": "47acded8-6c54-4963-8b44-2c7d92e719cb",
      "values": []
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
      "created_date": 1647347327940,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Attach the file associated with a running process",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Attach File",
      "export_key": "reaqta_attach_file",
      "id": 161,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531651883,
      "name": "reaqta_attach_file",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"type\": \"incident\", \"id\": 53, \"uuid\": \"469ef303-d1d5-4124-8265-3786ab2dd50b\", \"name\": \"wininit.exe\", \"content_type\": \"application/x-msdownload\", \"created\": 1645638429292, \"creator_id\": 3, \"size\": 480013, \"actions\": [{\"id\": 15, \"name\": \"Example: Attachment Hash\", \"enabled\": true}, {\"id\": 16, \"name\": \"Example: Attachment to Base64\", \"enabled\": true}, {\"id\": 20, \"name\": \"Example: Email Parsing (Attachment)\", \"enabled\": true}, {\"id\": 26, \"name\": \"Example: PDFiD\", \"enabled\": true}, {\"id\": 27, \"name\": \"Example: Resilient Search\", \"enabled\": true}, {\"id\": 32, \"name\": \"Example: Use Excel Data\", \"enabled\": false}, {\"id\": 35, \"name\": \"Example: Zip List\", \"enabled\": false}, {\"id\": 34, \"name\": \"Example: Zip Extract\", \"enabled\": false}, {\"id\": 55, \"name\": \"PB: Get workflows/playbooks by attachment name\", \"enabled\": true}, {\"id\": 90, \"name\": \"Example: Virus Total for Attachments\", \"enabled\": true}], \"task_id\": null, \"task_name\": null, \"task_custom\": null, \"task_members\": null, \"task_at_id\": null, \"vers\": 9, \"inc_id\": 2818, \"inc_name\": \"ReaQta Alert - Code Injection, Endpoint: DOMINO\", \"inc_owner\": 3}, \"raw\": null, \"inputs\": {\"reaqta_program_path\": \"C:\\\\Windows\\\\System32\\\\wininit.exe\", \"reaqta_endpoint_id\": \"825095183572926464\", \"reaqta_incident_id\": 2818}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 19785, \"timestamp\": \"2022-02-23 12:47:07\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"uuid\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"created\": {\"type\": \"integer\"}, \"creator_id\": {\"type\": \"integer\"}, \"size\": {\"type\": \"integer\"}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"task_id\": {}, \"task_name\": {}, \"task_custom\": {}, \"task_members\": {}, \"task_at_id\": {}, \"vers\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_program_path\": {\"type\": \"string\"}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "6cf8dd59-9465-49a4-8ce8-6538f6c61a4b",
      "version": 2,
      "view_items": [
        {
          "content": "d587ce18-7232-448f-98a7-23babb4b6e62",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a67fc10f-bec1-4915-b4bb-e4b6ce6a8456",
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
          "name": "ReaQta: Attach File from Process List",
          "object_type": "reaqta_process_list",
          "programmatic_name": "reaqta_attach_file_from_process_list",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 132
        },
        {
          "actions": [],
          "description": null,
          "name": "ReaQta: Attach File from Triggered Event",
          "object_type": "reaqta_trigger_events",
          "programmatic_name": "reaqta_attach_file_from_triggered_events",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 136
        }
      ]
    },
    {
      "created_date": 1647347328022,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Close a ReaQta Alert",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Close Alert",
      "export_key": "reaqta_close_alert",
      "id": 162,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531670111,
      "name": "reaqta_close_alert",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"alertId\": \"831993910053044226\", \"closed\": true}, \"raw\": null, \"inputs\": {\"reaqta_is_malicious\": false, \"reaqta_alert_id\": \"831993910053044226\", \"reaqta_note\": \"\u003cdiv class=\\\"rte\\\"\u003e\u003cdiv\u003e\u003cstrong\u003ethis is now complete\u003c/strong\u003e\u003c/div\u003e\u003c/div\u003e\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 1065, \"timestamp\": \"2022-02-18 13:54:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"alertId\": {\"type\": \"string\"}, \"closed\": {\"type\": \"boolean\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_is_malicious\": {\"type\": \"boolean\"}, \"reaqta_alert_id\": {\"type\": \"string\"}, \"reaqta_note\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "5801a66d-6b78-40dc-8ec4-f6ab0d842d7c",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66e6a8cc-1c5e-4f72-82cc-1a7198442c91",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cd0bea42-4e4f-46d0-9a68-ad1822a02014",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "974101e4-0904-4bc8-abd1-a34f163be445",
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
          "name": "ReaQta: Close Alert",
          "object_type": "incident",
          "programmatic_name": "reaqta_close_alert",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 130
        }
      ]
    },
    {
      "created_date": 1647347328093,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create an artifact from a ReaQta endpoint process file",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Create Artifact",
      "export_key": "reaqta_create_artifact",
      "id": 163,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531686842,
      "name": "reaqta_create_artifact",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"id\": 2141, \"type\": 12, \"value\": \"chrome.exe\", \"description\": \"Extracted from ReaQta\", \"attachment\": null, \"parent_id\": null, \"creator\": {\"id\": 3, \"fname\": \"Resilient\", \"lname\": \"Sysadmin\", \"display_name\": \"Resilient Sysadmin\", \"status\": \"A\", \"email\": \"a@example.com\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\"}, \"inc_id\": 2857, \"inc_name\": \"ReaQta Alert - Ransomware Behavior Detected, Endpoint: REAQTAWIN10-CSP\", \"inc_owner\": 2, \"hits\": [], \"created\": 1646339889974, \"last_modified_time\": 1646398787005, \"last_modified_by\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"pending_sources\": [], \"perms\": null, \"properties\": null, \"actions\": [], \"hash\": \"cb702049ff10bce20e09e04024c6654a78c85d54ea71de07f328f76426a42ed5\", \"relating\": true, \"creator_principal\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"related_incident_count\": null, \"pending_scan_result\": false, \"ip\": {\"source\": null, \"destination\": null}, \"global_artifact\": []}, {\"id\": 2142, \"type\": 13, \"value\": \"87d2ffd6a891119062b89decb05c89d8\", \"description\": \"Extracted from ReaQta\", \"attachment\": null, \"parent_id\": 2141, \"creator\": {\"id\": 3, \"fname\": \"Resilient\", \"lname\": \"Sysadmin\", \"display_name\": \"Resilient Sysadmin\", \"status\": \"A\", \"email\": \"a@example.com\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\"}, \"inc_id\": 2857, \"inc_name\": \"ReaQta Alert - Ransomware Behavior Detected, Endpoint: REAQTAWIN10-CSP\", \"inc_owner\": 2, \"hits\": [], \"created\": 1646339890099, \"last_modified_time\": 1646398787006, \"last_modified_by\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"pending_sources\": [], \"perms\": null, \"properties\": null, \"actions\": [], \"hash\": \"881c60fa0d9f9fd6c9a568e65f1ab1061e7de130f4c2268b600b7c092e72470d\", \"relating\": true, \"creator_principal\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"related_incident_count\": null, \"pending_scan_result\": false, \"ip\": {\"source\": null, \"destination\": null}, \"global_artifact\": []}, {\"id\": 2143, \"type\": 14, \"value\": \"4d224080d73d0e18a84e5eac43e52aba16161f23\", \"description\": \"Extracted from ReaQta\", \"attachment\": null, \"parent_id\": 2141, \"creator\": {\"id\": 3, \"fname\": \"Resilient\", \"lname\": \"Sysadmin\", \"display_name\": \"Resilient Sysadmin\", \"status\": \"A\", \"email\": \"a@example.com\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\"}, \"inc_id\": 2857, \"inc_name\": \"ReaQta Alert - Ransomware Behavior Detected, Endpoint: REAQTAWIN10-CSP\", \"inc_owner\": 2, \"hits\": [], \"created\": 1646339890117, \"last_modified_time\": 1646398787005, \"last_modified_by\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"pending_sources\": [], \"perms\": null, \"properties\": null, \"actions\": [], \"hash\": \"b8ea66ed6adba64778a93233cd636a6978bb34f9d91924c6a1480d5dfcdf71ef\", \"relating\": true, \"creator_principal\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"related_incident_count\": null, \"pending_scan_result\": false, \"ip\": {\"source\": null, \"destination\": null}, \"global_artifact\": []}, {\"id\": 2144, \"type\": 38, \"value\": \"93c68561a63428b1fe70b3d7b0e02af7c9cdcfefc1f6867ecb9ddcc05794bac9\", \"description\": \"Extracted from ReaQta\", \"attachment\": null, \"parent_id\": 2141, \"creator\": {\"id\": 3, \"fname\": \"Resilient\", \"lname\": \"Sysadmin\", \"display_name\": \"Resilient Sysadmin\", \"status\": \"A\", \"email\": \"a@example.com\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\"}, \"inc_id\": 2857, \"inc_name\": \"ReaQta Alert - Ransomware Behavior Detected, Endpoint: REAQTAWIN10-CSP\", \"inc_owner\": 2, \"hits\": [], \"created\": 1646339890136, \"last_modified_time\": 1646398787005, \"last_modified_by\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"pending_sources\": [], \"perms\": null, \"properties\": null, \"actions\": [], \"hash\": \"95b8f0eafd6b31fba895dc7e517e1fac8b10a8a27a08c1d434d2e3ae4b6638be\", \"relating\": true, \"creator_principal\": {\"id\": 3, \"type\": \"user\", \"name\": \"a@example.com\", \"display_name\": \"Resilient Sysadmin\"}, \"related_incident_count\": null, \"pending_scan_result\": false, \"ip\": {\"source\": null, \"destination\": null}, \"global_artifact\": []}], \"raw\": null, \"inputs\": {\"reaqta_artifact_type\": \"Malware Sample\", \"reaqta_program_path\": \"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"reaqta_endpoint_id\": \"833847379160465408\", \"reaqta_incident_id\": 2857}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 20461, \"timestamp\": \"2022-03-04 07:59:46\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"attachment\": {}, \"parent_id\": {\"type\": [\"integer\", \"null\"]}, \"creator\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"fname\": {\"type\": \"string\"}, \"lname\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}, \"status\": {\"type\": \"string\"}, \"email\": {\"type\": \"string\"}, \"locked\": {\"type\": \"boolean\"}, \"password_changed\": {\"type\": \"boolean\"}, \"is_external\": {\"type\": \"boolean\"}, \"ui_theme\": {\"type\": \"string\"}}}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}, \"hits\": {\"type\": \"array\"}, \"created\": {\"type\": \"integer\"}, \"last_modified_time\": {\"type\": \"integer\"}, \"last_modified_by\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"pending_sources\": {\"type\": \"array\"}, \"perms\": {}, \"properties\": {}, \"actions\": {\"type\": \"array\"}, \"hash\": {\"type\": \"string\"}, \"relating\": {\"type\": \"boolean\"}, \"creator_principal\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"related_incident_count\": {}, \"pending_scan_result\": {\"type\": \"boolean\"}, \"ip\": {\"type\": \"object\", \"properties\": {\"source\": {}, \"destination\": {}}}, \"global_artifact\": {\"type\": \"array\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_artifact_type\": {\"type\": \"string\"}, \"reaqta_program_path\": {\"type\": \"string\"}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "172eb03f-e7fd-4290-b98b-388ecedcd0e3",
      "version": 2,
      "view_items": [
        {
          "content": "d587ce18-7232-448f-98a7-23babb4b6e62",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a67fc10f-bec1-4915-b4bb-e4b6ce6a8456",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5b379be4-15dd-4f7c-b219-6c973464bf9e",
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
          "name": "ReaQta: Create Artifact from Process Path",
          "object_type": "reaqta_process_list",
          "programmatic_name": "reaqta_create_artifact_from_process_path",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 139
        },
        {
          "actions": [],
          "description": null,
          "name": "ReaQta: Create Artifact from Trigger Event",
          "object_type": "reaqta_trigger_events",
          "programmatic_name": "reaqta_create_artifact_from_trigger_event",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 129
        }
      ]
    },
    {
      "created_date": 1647347328165,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Append a note to the ReaQta notes",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Create Note",
      "export_key": "reaqta_create_note",
      "id": 164,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531705935,
      "name": "reaqta_create_note",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": \"\\\"\\\\nIBM SOAR 23/02/2022 12:44:51\\\\nthis is a note\\\"\", \"raw\": null, \"inputs\": {\"reaqta_alert_id\": \"834099413533065218\", \"reaqta_note\": \"\u003cdiv class=\\\"rte\\\"\u003e\u003cdiv\u003ethis is a note\u003c/div\u003e\u003c/div\u003e\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 1114, \"timestamp\": \"2022-02-23 12:44:51\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"string\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_alert_id\": {\"type\": \"string\"}, \"reaqta_note\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "21db5c06-30af-4619-b1ed-1c78b76f36b7",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66e6a8cc-1c5e-4f72-82cc-1a7198442c91",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "974101e4-0904-4bc8-abd1-a34f163be445",
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
          "name": "ReaQta: Create Note",
          "object_type": "note",
          "programmatic_name": "reaqta_create_note",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 131
        }
      ]
    },
    {
      "created_date": 1645535475281,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create an alert trigger based on a program\u0027s SHA256 hash",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Create Policy",
      "export_key": "reaqta_create_policy",
      "id": 123,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531729684,
      "name": "reaqta_create_policy",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"type\": 2, \"id\": \"834951840876462084\", \"versionId\": \"834951840876466181\", \"title\": \"test it policy\", \"description\": \"\", \"enabled\": true, \"deleted\": false, \"default\": false, \"matchers\": [{\"type\": 2, \"id\": \"834951840876470278\", \"hash\": \"91514e6be3f581a77daa79e2a4905dcbdf6bdcc32ee0f713599a94d453a26fc1\", \"alg\": 1}], \"actions\": [2], \"created\": \"2022-02-24T02:00:31.520Z\", \"lastModified\": \"2022-02-24T02:00:31.520Z\", \"scope\": \"group\", \"groups\": [{\"id\": \"831820214906650631\", \"name\": \"Demo\", \"enabled\": true}], \"policy_url\": \"https://rhiveam.techzone.ibm.com/policies/details/834951840876462084\"}, \"raw\": null, \"inputs\": {\"reaqta_policy_title\": \"test it policy\", \"reaqta_policy_block\": false, \"reaqta_policy_excluded_groups\": null, \"reaqta_policy_enabled\": true, \"reaqta_policy_description\": \"\", \"reaqta_sha256\": \"91514e6be3f581a77daa79e2a4905dcbdf6bdcc32ee0f713599a94d453a26fc1\", \"reaqta_policy_included_groups\": \"Demo\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 1283, \"timestamp\": \"2022-02-23 21:00:29\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"integer\"}, \"id\": {\"type\": \"string\"}, \"versionId\": {\"type\": \"string\"}, \"title\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}, \"deleted\": {\"type\": \"boolean\"}, \"default\": {\"type\": \"boolean\"}, \"matchers\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"integer\"}, \"id\": {\"type\": \"string\"}, \"hash\": {\"type\": \"string\"}, \"alg\": {\"type\": \"integer\"}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}}, \"created\": {\"type\": \"string\"}, \"lastModified\": {\"type\": \"string\"}, \"scope\": {\"type\": \"string\"}, \"groups\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"policy_url\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_policy_title\": {\"type\": \"string\"}, \"reaqta_policy_block\": {\"type\": \"boolean\"}, \"reaqta_policy_excluded_groups\": {}, \"reaqta_policy_enabled\": {\"type\": \"boolean\"}, \"reaqta_policy_description\": {\"type\": \"string\"}, \"reaqta_sha256\": {\"type\": \"string\"}, \"reaqta_policy_included_groups\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "7d727515-5a39-4213-8dee-ce9a56e8f26d",
      "version": 4,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c72e88df-ec5e-4078-b7d9-3b4bb422f9cb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0d93e3ef-6249-4566-a1e2-bb8ba43277f1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ecc14545-92fc-4272-8b46-b589e20ab01b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "712d96a6-9d8f-4c50-86b5-ee97edd8ec88",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c5e6f2d1-cb47-4801-965a-dcf86fd3fa7d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f40af3ea-ba5f-4d96-8149-7e8c80cb7cc5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3658c33e-a7f6-4eef-b899-abd9f5c57446",
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
          "name": "ReaQta: Create Policy from Artifact",
          "object_type": "artifact",
          "programmatic_name": "reaqta_create_policy_from_artifact",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 128
        },
        {
          "actions": [],
          "description": null,
          "name": "ReaQta: Create Policy on Triggered Event",
          "object_type": "reaqta_trigger_events",
          "programmatic_name": "reaqta_create_policy_on_triggered_event",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 134
        }
      ]
    },
    {
      "created_date": 1647347328263,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get all the ReaQta Alert information to populate custom fields and datatables",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Get Alert Information",
      "export_key": "reaqta_get_alert_information",
      "id": 165,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531744070,
      "name": "reaqta_get_alert_information",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"834832646071648258\", \"localId\": \"834832599212890114\", \"endpointId\": \"833847379160465408\", \"triggerCondition\": 7, \"endpoint\": {\"id\": \"833847379160465408\", \"machineId\": \"de64775b529ad34495bc51cd8b227c254d112185cfd06a92e0d5bd8a9ca19124\", \"osType\": 1, \"cpuVendor\": 1, \"arch\": 2, \"cpuDescr\": \"Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz\", \"kernel\": \"10.0\", \"os\": \"Windows 10 Pro\", \"name\": \"REAQTAWIN10-CSP\", \"domain\": \"csplab.local\", \"state\": 1, \"registrationTime\": \"2022-02-21T00:51:47.330Z\", \"agentVersion\": \"3.6.1\", \"componentsVersions\": [{\"name\": \"keeper\", \"version\": \"3.6.0\", \"build\": \"19.1627291555548.commit\"}, {\"name\": \"probos\", \"version\": \"3.5.0\", \"build\": \"3.5.0\"}, {\"name\": \"rqtsentry\", \"version\": \"3.6.1\", \"build\": \"119.1632119719010.commit\"}, {\"name\": \"rqtnetsentry\", \"version\": \"3.6.0\", \"build\": \"44.1627295520120.commit\"}, {\"name\": \"installer\", \"version\": \"3.6.1\", \"build\": \"\"}], \"isVirtualMachine\": true, \"isDomainController\": false, \"isServer\": false, \"sessionStart\": \"2022-02-21T00:51:49.215Z\", \"sessionEnd\": \"2022-02-24T01:09:59.043Z\", \"lastSeenAt\": \"2022-02-24T01:04:59.043Z\", \"disconnectionReason\": 0, \"localAddr\": \"172.16.253.37\", \"hvStatus\": 19, \"macs\": [\"00:50:56:bf:9f:16\"], \"isolated\": false, \"connected\": true, \"tags\": [\"vm\"], \"groups\": [{\"id\": \"822878129902059527\", \"name\": \"Partner Team\", \"description\": \"Partner Team Ambassador Rob Fichtel\"}], \"avInstalled\": false}, \"triggerEvents\": [{\"id\": \"834832645178261505\", \"category\": \"hive\", \"localId\": \"834832599133194241\", \"endpointId\": \"833847379160465408\", \"receivedAt\": \"2022-02-23T18:06:53.051Z\", \"happenedAt\": \"2022-02-23T18:06:42.073Z\", \"relevance\": 0, \"severity\": \"none\", \"trigger\": true, \"manuallyAdded\": false, \"process\": {\"id\": \"833847379160465408:7868:1645639602071\", \"parentId\": \"833847379160465408:872:1645639598803\", \"endpointId\": \"833847379160465408\", \"program\": {\"path\": \"c:\\\\users\\\\melody\\\\appdata\\\\local\\\\temp\\\\tryme.exe\", \"filename\": \"tryme.exe\", \"md5\": \"a3ce5c07dc7b7d58740b4407a7d3f9d2\", \"sha1\": \"9fa6c5f1cff4ca41c441e428a847a924627210cc\", \"sha256\": \"cf8c1b234ad4d72dd6a455b82bf48ff16cd794aaefb682729b0151f0e1c374dd\", \"size\": 84992, \"arch\": \"x32\", \"fsName\": \"tryme.exe\"}, \"user\": \"REAQTAWIN10-CSP\\\\Melody\", \"pid\": 7868, \"startTime\": \"2022-02-23T18:06:42.071Z\", \"ppid\": 872, \"pstartTime\": \"2022-02-23T18:06:38.803Z\", \"userSID\": \"S-1-5-21-2250471729-4061103233-1630355673-1002\", \"privilegeLevel\": \"MEDIUM\", \"noGui\": false, \"logonId\": \"0x154d314\"}, \"eventType\": 2, \"data\": {\"cmdLine\": \"C:\\\\Users\\\\Melody\\\\AppData\\\\Local\\\\Temp\\\\tryme.exe\", \"cmdLineArgs\": [\"C:\\\\Users\\\\Melody\\\\AppData\\\\Local\\\\Temp\\\\tryme.exe\"], \"_t\": \"l\"}, \"happenedAt_ts\": 1645639602000}, {\"id\": \"834832645488640001\", \"category\": \"hive\", \"localId\": \"834832599212886017\", \"endpointId\": \"833847379160465408\", \"receivedAt\": \"2022-02-23T18:06:53.125Z\", \"happenedAt\": \"2022-02-23T18:06:42.092Z\", \"relevance\": 83, \"severity\": \"medium\", \"trigger\": true, \"manuallyAdded\": false, \"process\": {\"id\": \"833847379160465408:872:1645639598803\", \"parentId\": \"833847379160465408:6580:1645471843080\", \"endpointId\": \"833847379160465408\", \"program\": {\"path\": \"c:\\\\program files\\\\microsoft office\\\\root\\\\office16\\\\winword.exe\", \"filename\": \"winword.exe\", \"md5\": \"313009918ec71770c8f2fdcd416a4485\", \"sha1\": \"5d36f6ef6d0f76aaf837c4f7e65b611acd92e0ae\", \"sha256\": \"d76c3d25eb625a8475488b14b501e775b3186ad4ff77e9c07edb4ec2ff6923d9\", \"certInfo\": {\"signer\": \"Microsoft Corporation\", \"issuer\": \"Microsoft Code Signing PCA 2011\", \"trusted\": true, \"expired\": false}, \"size\": 1638704, \"arch\": \"x64\", \"fsName\": \"winword.exe\"}, \"user\": \"REAQTAWIN10-CSP\\\\Melody\", \"pid\": 872, \"startTime\": \"2022-02-23T18:06:38.803Z\", \"ppid\": 6580, \"pstartTime\": \"2022-02-21T19:30:43.080Z\", \"userSID\": \"S-1-5-21-2250471729-4061103233-1630355673-1002\", \"privilegeLevel\": \"MEDIUM\", \"noGui\": false, \"logonId\": \"0x154d314\"}, \"eventType\": 31, \"data\": {\"behaviourType\": 1, \"_t\": \"l\"}, \"happenedAt_ts\": 1645639602000}], \"totalEventCount\": 452, \"byTypeEventCount\": [{\"type\": 11, \"count\": 140}, {\"type\": 21, \"count\": 73}, {\"type\": 10, \"count\": 59}, {\"type\": 5, \"count\": 37}, {\"type\": 12, \"count\": 34}, {\"type\": 65, \"count\": 29}, {\"type\": 8, \"count\": 28}, {\"type\": 38, \"count\": 21}, {\"type\": 2, \"count\": 8}, {\"type\": 57, \"count\": 8}, {\"type\": 37, \"count\": 6}, {\"type\": 6, \"count\": 3}, {\"type\": 3, \"count\": 2}, {\"type\": 30, \"count\": 1}, {\"type\": 31, \"count\": 1}, {\"type\": 62, \"count\": 1}, {\"type\": 89, \"count\": 1}], \"impact\": 83, \"severity\": \"medium\", \"closed\": false, \"activityState\": \"inactive\", \"terminationReason\": 1, \"receivedAt\": \"2022-02-23T18:06:53.264Z\", \"happenedAt\": \"2022-02-23T18:06:42.092Z\", \"tags\": [], \"endpointState\": {\"osType\": 1, \"cpuVendor\": 1, \"arch\": 2, \"cpuDescr\": \"Intel(R) Xeon(R) CPU E5-2450 0 @ 2.10GHz\", \"kernel\": \"10.0\", \"os\": \"Windows 10 Pro\", \"hvStatus\": 19, \"name\": \"REAQTAWIN10-CSP\", \"domain\": \"csplab.local\", \"isolated\": false, \"localAddr\": \"172.16.253.37\", \"macs\": [\"00:50:56:bf:9f:16\"], \"componentsVersions\": [{\"name\": \"keeper\", \"version\": \"3.6.0\", \"build\": \"19.1627291555548.commit\"}, {\"name\": \"probos\", \"version\": \"3.5.0\", \"build\": \"3.5.0\"}, {\"name\": \"rqtsentry\", \"version\": \"3.6.1\", \"build\": \"119.1632119719010.commit\"}, {\"name\": \"rqtnetsentry\", \"version\": \"3.6.0\", \"build\": \"44.1627295520120.commit\"}, {\"name\": \"installer\", \"version\": \"3.6.1\", \"build\": \"\"}], \"endpointVersion\": \"3.6.1\", \"tags\": [\"vm\"], \"groups\": [{\"id\": \"822878129902059527\", \"name\": \"Partner Team\", \"description\": \"Partner Team Ambassador Rob Fichtel\"}]}, \"alert_url\": \"https://rhiveam.techzone.ibm.com/alerts/834832646071648258\"}, \"raw\": null, \"inputs\": {\"reaqta_alert_id\": \"834832646071648258\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 663, \"timestamp\": \"2022-02-23 20:04:58\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"localId\": {\"type\": \"string\"}, \"endpointId\": {\"type\": \"string\"}, \"triggerCondition\": {\"type\": \"integer\"}, \"endpoint\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"machineId\": {\"type\": \"string\"}, \"osType\": {\"type\": \"integer\"}, \"cpuVendor\": {\"type\": \"integer\"}, \"arch\": {\"type\": \"integer\"}, \"cpuDescr\": {\"type\": \"string\"}, \"kernel\": {\"type\": \"string\"}, \"os\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"domain\": {\"type\": \"string\"}, \"state\": {\"type\": \"integer\"}, \"registrationTime\": {\"type\": \"string\"}, \"agentVersion\": {\"type\": \"string\"}, \"componentsVersions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"version\": {\"type\": \"string\"}, \"build\": {\"type\": \"string\"}}}}, \"isVirtualMachine\": {\"type\": \"boolean\"}, \"isDomainController\": {\"type\": \"boolean\"}, \"isServer\": {\"type\": \"boolean\"}, \"sessionStart\": {\"type\": \"string\"}, \"sessionEnd\": {\"type\": \"string\"}, \"lastSeenAt\": {\"type\": \"string\"}, \"disconnectionReason\": {\"type\": \"integer\"}, \"localAddr\": {\"type\": \"string\"}, \"hvStatus\": {\"type\": \"integer\"}, \"macs\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"isolated\": {\"type\": \"boolean\"}, \"connected\": {\"type\": \"boolean\"}, \"tags\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"groups\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}}}}, \"avInstalled\": {\"type\": \"boolean\"}}}, \"triggerEvents\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"category\": {\"type\": \"string\"}, \"localId\": {\"type\": \"string\"}, \"endpointId\": {\"type\": \"string\"}, \"receivedAt\": {\"type\": \"string\"}, \"happenedAt\": {\"type\": \"string\"}, \"relevance\": {\"type\": \"integer\"}, \"severity\": {\"type\": \"string\"}, \"trigger\": {\"type\": \"boolean\"}, \"manuallyAdded\": {\"type\": \"boolean\"}, \"process\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"parentId\": {\"type\": \"string\"}, \"endpointId\": {\"type\": \"string\"}, \"program\": {\"type\": \"object\", \"properties\": {\"path\": {\"type\": \"string\"}, \"filename\": {\"type\": \"string\"}, \"md5\": {\"type\": \"string\"}, \"sha1\": {\"type\": \"string\"}, \"sha256\": {\"type\": \"string\"}, \"size\": {\"type\": \"integer\"}, \"arch\": {\"type\": \"string\"}, \"fsName\": {\"type\": \"string\"}, \"certInfo\": {\"type\": \"object\", \"properties\": {\"signer\": {\"type\": \"string\"}, \"issuer\": {\"type\": \"string\"}, \"trusted\": {\"type\": \"boolean\"}, \"expired\": {\"type\": \"boolean\"}}}}}, \"user\": {\"type\": \"string\"}, \"pid\": {\"type\": \"integer\"}, \"startTime\": {\"type\": \"string\"}, \"ppid\": {\"type\": \"integer\"}, \"pstartTime\": {\"type\": \"string\"}, \"userSID\": {\"type\": \"string\"}, \"privilegeLevel\": {\"type\": \"string\"}, \"noGui\": {\"type\": \"boolean\"}, \"logonId\": {\"type\": \"string\"}}}, \"eventType\": {\"type\": \"integer\"}, \"data\": {\"type\": \"object\", \"properties\": {\"cmdLine\": {\"type\": \"string\"}, \"cmdLineArgs\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"_t\": {\"type\": \"string\"}, \"behaviourType\": {\"type\": \"integer\"}}}, \"happenedAt_ts\": {\"type\": \"integer\"}}}}, \"totalEventCount\": {\"type\": \"integer\"}, \"byTypeEventCount\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"integer\"}, \"count\": {\"type\": \"integer\"}}}}, \"impact\": {\"type\": \"integer\"}, \"severity\": {\"type\": \"string\"}, \"closed\": {\"type\": \"boolean\"}, \"activityState\": {\"type\": \"string\"}, \"terminationReason\": {\"type\": \"integer\"}, \"receivedAt\": {\"type\": \"string\"}, \"happenedAt\": {\"type\": \"string\"}, \"tags\": {\"type\": \"array\"}, \"endpointState\": {\"type\": \"object\", \"properties\": {\"osType\": {\"type\": \"integer\"}, \"cpuVendor\": {\"type\": \"integer\"}, \"arch\": {\"type\": \"integer\"}, \"cpuDescr\": {\"type\": \"string\"}, \"kernel\": {\"type\": \"string\"}, \"os\": {\"type\": \"string\"}, \"hvStatus\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"domain\": {\"type\": \"string\"}, \"isolated\": {\"type\": \"boolean\"}, \"localAddr\": {\"type\": \"string\"}, \"macs\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"componentsVersions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"version\": {\"type\": \"string\"}, \"build\": {\"type\": \"string\"}}}}, \"endpointVersion\": {\"type\": \"string\"}, \"tags\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"groups\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}}}}}}, \"alert_url\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_alert_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "13918f45-5268-41b0-8ff0-e6a6223ad302",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66e6a8cc-1c5e-4f72-82cc-1a7198442c91",
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
          "name": "ReaQta: Get Alert Information",
          "object_type": "incident",
          "programmatic_name": "reaqta_get_alert_information",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 138
        }
      ]
    },
    {
      "created_date": 1647347328341,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get active processes from a given endpoint",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Get Processes",
      "export_key": "reaqta_get_processes",
      "id": 166,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531756976,
      "name": "reaqta_get_processes",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"pid\": 0, \"ppid\": 0, \"processName\": \"[System Process]\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 0}, {\"pid\": 4, \"ppid\": 0, \"processName\": \"System\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645515988249}, {\"pid\": 320, \"ppid\": 4, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"smss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\smss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645515988596}, {\"pid\": 416, \"ppid\": 408, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645515999443}, {\"pid\": 520, \"ppid\": 512, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516001029}, {\"pid\": 544, \"ppid\": 408, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"wininit.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\wininit.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516001050}, {\"pid\": 576, \"ppid\": 512, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"winlogon.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\winlogon.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516001162}, {\"pid\": 660, \"ppid\": 544, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"services.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\services.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516003318}, {\"pid\": 676, \"ppid\": 544, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"lsass.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\lsass.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516004097}, {\"pid\": 760, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516007207}, {\"pid\": 812, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516008133}, {\"pid\": 912, \"ppid\": 576, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"LogonUI.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\LogonUI.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516009649}, {\"pid\": 920, \"ppid\": 576, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"dwm.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dwm.exe\", \"user\": \"Window Manager\\\\DWM-1\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516009661}, {\"pid\": 984, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516009804}, {\"pid\": 1020, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516009837}, {\"pid\": 364, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516009883}, {\"pid\": 1036, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516010782}, {\"pid\": 1084, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516010902}, {\"pid\": 1136, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516011004}, {\"pid\": 1204, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516011305}, {\"pid\": 1256, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516011553}, {\"pid\": 1776, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"spoolsv.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\spoolsv.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012637}, {\"pid\": 1988, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012827}, {\"pid\": 1996, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"Db2TAPProxyHelper.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\Windows S-TAP\\\\Bin\\\\Db2TAPProxyHelper.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012829}, {\"pid\": 2012, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"MsMpEng.exe\", \"programPath\": \"C:\\\\ProgramData\\\\Microsoft\\\\Windows Defender\\\\platform\\\\4.18.2201.10-0\\\\MsMpEng.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012848}, {\"pid\": 1128, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"db2mgmtsvc.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2mgmtsvc.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012887}, {\"pid\": 1156, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"filezilla-server.exe\", \"programPath\": \"C:\\\\Program Files\\\\FileZilla Server\\\\filezilla-server.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012890}, {\"pid\": 1376, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"snmp.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\snmp.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012954}, {\"pid\": 1592, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"gimclient.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Guardium\\\\Guardium Installation Manager\\\\GIM\\\\Current\\\\gimclient.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012988}, {\"pid\": 2052, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"resmon.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\Guardium Agent Monitor\\\\Bin\\\\resmon.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012989}, {\"pid\": 2060, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516012992}, {\"pid\": 2096, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"DbMonitor.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\Windows S-TAP\\\\Bin\\\\DbMonitor.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013028}, {\"pid\": 2128, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"vm3dservice.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\vm3dservice.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013047}, {\"pid\": 2144, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013051}, {\"pid\": 2224, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"Guardium_Stapr.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\Windows S-TAP\\\\Bin\\\\Guardium_Stapr.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013105}, {\"pid\": 2248, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nservice.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nservice.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013170}, {\"pid\": 2264, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"vmtoolsd.exe\", \"programPath\": \"C:\\\\Program Files\\\\VMware\\\\VMware Tools\\\\vmtoolsd.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013198}, {\"pid\": 2272, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"VGAuthService.exe\", \"programPath\": \"C:\\\\Program Files\\\\VMware\\\\VMware Tools\\\\VMware VGAuth\\\\VGAuthService.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013239}, {\"pid\": 2348, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"WinCollect.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\WinCollect\\\\bin\\\\WinCollect.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013326}, {\"pid\": 2380, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"lnsnmp.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\lnsnmp.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013413}, {\"pid\": 2400, \"ppid\": 2128, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"vm3dservice.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\vm3dservice.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013426}, {\"pid\": 2468, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"Db2TAPService.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\Windows S-TAP\\\\Bin\\\\Db2TAPService.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645516013580}, {\"pid\": 2544, \"ppid\": 2380, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"conhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\conhost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516013738}, {\"pid\": 2968, \"ppid\": 1592, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"perl.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Guardium\\\\Guardium Installation Manager\\\\sppNew\\\\perl\\\\bin\\\\perl.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516014689}, {\"pid\": 3044, \"ppid\": 2968, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"conhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\conhost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516014788}, {\"pid\": 3136, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516014968}, {\"pid\": 3708, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"dllhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dllhost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516016204}, {\"pid\": 3728, \"ppid\": 660, \"privilegeLevel\": \"HIGH\", \"processName\": \"db2rcmd.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2rcmd.exe\", \"user\": \"DOMINO\\\\db2admin\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516016340}, {\"pid\": 3736, \"ppid\": 660, \"privilegeLevel\": \"HIGH\", \"processName\": \"db2syscs.exe\", \"programPath\": \"C:\\\\PROGRA~1\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2syscs.exe\", \"user\": \"DOMINO\\\\db2admin\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645516016371}, {\"pid\": 3744, \"ppid\": 660, \"privilegeLevel\": \"HIGH\", \"processName\": \"db2dasrrm.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2dasrrm.exe\", \"user\": \"DOMINO\\\\db2admin\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516016410}, {\"pid\": 2188, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"msdtc.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\msdtc.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516020691}, {\"pid\": 3996, \"ppid\": 2248, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"scontroller.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\scontroller.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516021380}, {\"pid\": 3048, \"ppid\": 760, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"WmiPrvSE.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\wbem\\\\WmiPrvSE.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516021529}, {\"pid\": 4136, \"ppid\": 3996, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nserver.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nserver.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516032326}, {\"pid\": 4316, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"conhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\conhost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516032982}, {\"pid\": 4684, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"NisSrv.exe\", \"programPath\": \"C:\\\\ProgramData\\\\Microsoft\\\\Windows Defender\\\\platform\\\\4.18.2201.10-0\\\\NisSrv.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516046055}, {\"pid\": 4808, \"ppid\": 3736, \"privilegeLevel\": \"HIGH\", \"processName\": \"db2fmp64.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2fmp64.exe\", \"user\": \"DOMINO\\\\db2admin\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645516050669}, {\"pid\": 4224, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nevent.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nevent.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516081570}, {\"pid\": 4476, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nupdate.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nupdate.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516090772}, {\"pid\": 2312, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nreplica.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nreplica.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516090860}, {\"pid\": 2340, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nrouter.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nrouter.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091023}, {\"pid\": 2376, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"namgr.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\namgr.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091145}, {\"pid\": 2424, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nadminp.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nadminp.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091278}, {\"pid\": 2500, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"ncalconn.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\ncalconn.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091437}, {\"pid\": 2936, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nsched.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nsched.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091566}, {\"pid\": 1728, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nhttp.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nhttp.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091667}, {\"pid\": 4676, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nimap.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nimap.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516091995}, {\"pid\": 3808, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nldap.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nldap.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092135}, {\"pid\": 3824, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"npop3.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\npop3.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092276}, {\"pid\": 4048, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nrnrmgr.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nrnrmgr.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092427}, {\"pid\": 4940, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"ncollect.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\ncollect.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092570}, {\"pid\": 4860, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nintrcpt.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nintrcpt.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092656}, {\"pid\": 4912, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nsmtp.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nsmtp.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516092752}, {\"pid\": 4500, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"ndomidx.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\ndomidx.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516093144}, {\"pid\": 3804, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nprocmon.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nprocmon.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516095454}, {\"pid\": 4084, \"ppid\": 4136, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"nrunjava.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\nrunjava.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516095883}, {\"pid\": 5220, \"ppid\": 2376, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"namgr.exe\", \"programPath\": \"C:\\\\IBM\\\\Domino\\\\namgr.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516097200}, {\"pid\": 6088, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"BESClient.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\BigFix Enterprise\\\\BES Client\\\\BESClient.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516146836}, {\"pid\": 6140, \"ppid\": 660, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516149920}, {\"pid\": 4288, \"ppid\": 5892, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"GoogleCrashHandler.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Update\\\\1.3.36.122\\\\GoogleCrashHandler.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516168156}, {\"pid\": 3836, \"ppid\": 5892, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"GoogleCrashHandler64.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Update\\\\1.3.36.122\\\\GoogleCrashHandler64.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516168682}, {\"pid\": 6640, \"ppid\": 6632, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516251743}, {\"pid\": 6684, \"ppid\": 6632, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"winlogon.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\winlogon.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516251846}, {\"pid\": 6768, \"ppid\": 6684, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"dwm.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dwm.exe\", \"user\": \"Window Manager\\\\DWM-2\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516253142}, {\"pid\": 2448, \"ppid\": 984, \"privilegeLevel\": \"HIGH\", \"processName\": \"rdpclip.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\rdpclip.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516256532}, {\"pid\": 2608, \"ppid\": 660, \"privilegeLevel\": \"HIGH\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516257826}, {\"pid\": 3468, \"ppid\": 1136, \"privilegeLevel\": \"HIGH\", \"processName\": \"sihost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\sihost.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516257899}, {\"pid\": 4280, \"ppid\": 1136, \"privilegeLevel\": \"HIGH\", \"processName\": \"taskhostw.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\taskhostw.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516257975}, {\"pid\": 6976, \"ppid\": 6088, \"privilegeLevel\": \"HIGH\", \"processName\": \"BESClientUI.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\BigFix Enterprise\\\\BES Client\\\\BESClientUI.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516271088}, {\"pid\": 5828, \"ppid\": 760, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516294793}, {\"pid\": 7440, \"ppid\": 6684, \"privilegeLevel\": \"HIGH\", \"processName\": \"explorer.exe\", \"programPath\": \"C:\\\\Windows\\\\explorer.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516312254}, {\"pid\": 7780, \"ppid\": 760, \"privilegeLevel\": \"LOW\", \"processName\": \"ShellExperienceHost.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\ShellExperienceHost_cw5n1h2txyewy\\\\ShellExperienceHost.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": true, \"startTime\": 1645516322277}, {\"pid\": 7892, \"ppid\": 760, \"privilegeLevel\": \"LOW\", \"processName\": \"SearchUI.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\Microsoft.Windows.Cortana_cw5n1h2txyewy\\\\SearchUI.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": true, \"startTime\": 1645516322666}, {\"pid\": 7324, \"ppid\": 7440, \"privilegeLevel\": \"HIGH\", \"processName\": \"filezilla-server-gui.exe\", \"programPath\": \"C:\\\\Program Files\\\\FileZilla Server\\\\filezilla-server-gui.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516350485}, {\"pid\": 6968, \"ppid\": 7440, \"privilegeLevel\": \"HIGH\", \"processName\": \"db2systray.exe\", \"programPath\": \"C:\\\\Program Files\\\\IBM\\\\SQLLIB\\\\BIN\\\\db2systray.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516352502}, {\"pid\": 4800, \"ppid\": 6796, \"privilegeLevel\": \"HIGH\", \"processName\": \"jusched.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Common Files\\\\Java\\\\Java Update\\\\jusched.exe\", \"user\": \"DOMINO\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645516353751}], \"raw\": null, \"inputs\": {\"reaqta_has_incident\": null, \"reaqta_endpoint_id\": \"825095183572926464\", \"reaqta_suspended\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 785, \"timestamp\": \"2022-02-23 12:45:51\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"pid\": {\"type\": \"integer\"}, \"ppid\": {\"type\": \"integer\"}, \"processName\": {\"type\": \"string\"}, \"hasIncident\": {\"type\": \"boolean\"}, \"suspended\": {\"type\": \"boolean\"}, \"startTime\": {\"type\": \"integer\"}, \"privilegeLevel\": {\"type\": \"string\"}, \"programPath\": {\"type\": \"string\"}, \"user\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_has_incident\": {}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_suspended\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "f97be6f0-081a-47af-931f-5e2b101aec3a",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "705674a2-6e43-49be-bcce-5235a82e3508",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7066af79-2b00-4cc7-87a3-1cad073c7544",
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
          "name": "ReaQta: Get Processes",
          "object_type": "incident",
          "programmatic_name": "reaqta_get_processes",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 135
        }
      ]
    },
    {
      "created_date": 1647347328414,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Isolate a ReaQta controlled machine based on it\u0027s endpoint ID",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Isolate Machine",
      "export_key": "reaqta_isolate_machine",
      "id": 167,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531771035,
      "name": "reaqta_isolate_machine",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"message\": \"Endpoint offline\", \"details\": {\"endpointId\": \"820358261151629312\", \"lastSeenAt\": \"2022-02-15T18:05:09.113Z\"}}, \"raw\": null, \"inputs\": {\"reaqta_endpoint_id\": \"820358261151629312\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 498, \"timestamp\": \"2022-02-18 14:04:55\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"message\": {\"type\": \"string\"}, \"details\": {\"type\": \"object\", \"properties\": {\"endpointId\": {\"type\": \"string\"}, \"lastSeenAt\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_endpoint_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "79d595f7-b9dc-435c-87bf-e2845fddda94",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
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
          "name": "ReaQta: Isolate Endpoint",
          "object_type": "incident",
          "programmatic_name": "reaqta_isolate_endpoint",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 137
        }
      ]
    },
    {
      "created_date": 1647347328483,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Kill a process on a machine by the process PID",
        "format": "text"
      },
      "destination_handle": "fn_reaqta",
      "display_name": "ReaQta: Kill Process",
      "export_key": "reaqta_kill_process",
      "id": 168,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1647531787812,
      "name": "reaqta_kill_process",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"pid\": 4, \"startTime\": 1644961331131, \"killed\": false, \"errorCode\": -1, \"error\": \"Process not found\"}], \"raw\": null, \"inputs\": {\"reaqta_starttime\": 1644961331131, \"reaqta_endpoint_id\": \"831986736375529472\", \"reaqta_process_pid\": 4}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 953, \"timestamp\": \"2022-02-18 13:48:08\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"pid\": {\"type\": \"integer\"}, \"startTime\": {\"type\": \"integer\"}, \"killed\": {\"type\": \"boolean\"}, \"errorCode\": {\"type\": \"integer\"}, \"error\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_starttime\": {\"type\": \"integer\"}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_process_pid\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "f8f32b38-a279-4657-8419-5ce82fcdb36d",
      "version": 2,
      "view_items": [
        {
          "content": "8328e505-3176-4864-b179-7da5dc9e9251",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "57fc46a2-de15-48ea-966c-277c2e5f8cda",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "577df2a5-6b20-4828-a3a9-da6f3446dee5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48ae8d4f-7cd3-49bd-b370-2bc878003aa3",
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
          "name": "ReaQta: Kill Process",
          "object_type": "reaqta_process_list",
          "programmatic_name": "reaqta_kill_process",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 133
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 53,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647546262444,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647546262444,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "32af467b-2030-45a9-a279-1257fef3ba98"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_reaqta",
      "name": "fn_reaqta",
      "programmatic_name": "fn_reaqta",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "09518133-71e4-4cdc-bd40-0d04ec1354c6"
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
      "display_name": "ReaQta Process List",
      "export_key": "reaqta_process_list",
      "fields": {
        "has_incident": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/has_incident",
          "hide_notification": false,
          "id": 1040,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "has_incident",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Related to Alert",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "f94aa912-ab1e-4c53-8149-672be5cc546e",
          "values": [],
          "width": 70
        },
        "pid": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/pid",
          "hide_notification": false,
          "id": 1041,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "pid",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "PID",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "69e512f0-cb2d-4cae-9793-f04c71b8959e",
          "values": [],
          "width": 29
        },
        "privilege_level": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/privilege_level",
          "hide_notification": false,
          "id": 1042,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "privilege_level",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Privilege Level",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "1f072df1-cd16-4f08-8d61-97c5ca4c4eda",
          "values": [],
          "width": 74
        },
        "process_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/process_name",
          "hide_notification": false,
          "id": 1043,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "process_name",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Program Name",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "84b0484d-6ac9-47c7-9f9b-4c51c0700a59",
          "values": [],
          "width": 68
        },
        "process_path": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/process_path",
          "hide_notification": false,
          "id": 1044,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "process_path",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Process Path",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "757fdae8-3496-4c86-9818-b93fcbcfc7dd",
          "values": [],
          "width": 66
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/report_date",
          "hide_notification": false,
          "id": 1045,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "report_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report Date",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "060eb4ae-dbb1-410d-9a47-cdbdd4c8dde7",
          "values": [],
          "width": 67
        },
        "start_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/start_time",
          "hide_notification": false,
          "id": 1046,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "start_time",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Start Time",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "9c2ba4f8-ba17-4f7c-afff-15be464a0dda",
          "values": [],
          "width": 45
        },
        "status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/status",
          "hide_notification": false,
          "id": 1054,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "332e07f6-7ec3-46fe-b07a-60635b38c8be",
          "values": [],
          "width": 49
        },
        "suspended": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/suspended",
          "hide_notification": false,
          "id": 1047,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "suspended",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Process Suspended",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "2f867983-970a-4035-8569-dd632738fe9c",
          "values": [],
          "width": 85
        },
        "user": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_process_list/user",
          "hide_notification": false,
          "id": 1048,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "user",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "3c6051f4-cf12-475a-a7c4-7e47b58aae98",
          "values": [],
          "width": 42
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
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "reaqta_process_list",
      "uuid": "edbc75bc-81fe-467f-8c9f-f1d464f3554c"
    },
    {
      "actions": [],
      "display_name": "ReaQta Trigger Events",
      "export_key": "reaqta_trigger_events",
      "fields": {
        "category": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/category",
          "hide_notification": false,
          "id": 1025,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "category",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "a1582531-a236-4b08-a1c9-2c2c840f741a",
          "values": [],
          "width": 93
        },
        "happened_at": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/happened_at",
          "hide_notification": false,
          "id": 1031,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "happened_at",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Happened At",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "3b2b8e17-dbbe-4b45-920f-a601f5ebf84a",
          "values": [],
          "width": 114
        },
        "policy_match": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/policy_match",
          "hide_notification": false,
          "id": 1267,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "policy_match",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Policy Match",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "f19a95d7-6171-4ccf-a1b0-7178e6cc948d",
          "values": [],
          "width": 46
        },
        "process_pid": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/process_pid",
          "hide_notification": false,
          "id": 1026,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "process_pid",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "PID",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "13d11555-26cc-4511-b329-d8aaa7af46fc",
          "values": [],
          "width": 111
        },
        "program_path": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/program_path",
          "hide_notification": false,
          "id": 1027,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "program_path",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Program Path",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "2c662898-94ae-4ddd-8f85-bf6a106c5b42",
          "values": [],
          "width": 130
        },
        "relevance": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/relevance",
          "hide_notification": false,
          "id": 1029,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "relevance",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Relevance",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "9a7db901-6331-4229-a087-510456f8b707",
          "values": [],
          "width": 90
        },
        "severity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/severity",
          "hide_notification": false,
          "id": 1030,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "severity",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Severity",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "42ba61a7-6374-464f-980d-646bd691498b",
          "values": [],
          "width": 93
        },
        "sha256_hash": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/sha256_hash",
          "hide_notification": false,
          "id": 1061,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sha256_hash",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "SHA256 Hash",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "358fda9a-86eb-4bac-b8e5-836b75bf505b",
          "values": [],
          "width": 62
        },
        "windows_event_account": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/windows_event_account",
          "hide_notification": false,
          "id": 1263,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "windows_event_account",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Windows Event Account",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "539528fc-5872-45fb-8e90-e6ae1d79b31b",
          "values": [],
          "width": 70
        },
        "windows_event_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/windows_event_description",
          "hide_notification": false,
          "id": 1264,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "windows_event_description",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Windows Event Description",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "6467231f-af25-489d-a229-74269b2c3699",
          "values": [],
          "width": 88
        },
        "windows_event_ipport": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/windows_event_ipport",
          "hide_notification": false,
          "id": 1265,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "windows_event_ipport",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Windows Event IP/Port",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "6d32324a-fdf7-4390-8325-012b43a7a2f1",
          "values": [],
          "width": 70
        },
        "windows_event_workstation": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "reaqta_trigger_events/windows_event_workstation",
          "hide_notification": false,
          "id": 1266,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "windows_event_workstation",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Windows Event Workstation",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "9cad1857-f542-477f-b9db-b41969a458a0",
          "values": [],
          "width": 93
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
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "reaqta_trigger_events",
      "uuid": "1965902b-05da-4b63-bf98-d46e0f1ceb51"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "reaqta_get_processes",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_get_processes\" isExecutable=\"true\" name=\"ReaQta: Get Processes\"\u003e\u003cdocumentation\u003eGet the running processes on a given machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_105iv85\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17ds9m6\" name=\"ReaQta: Get Processes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f97be6f0-081a-47af-931f-5e2b101aec3a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  if isinstance(results.content, list):\\n    for process in results.content:\\n      row = incident.addRow(\\\"reaqta_process_list\\\")\\n      \\n      row[\u0027report_date\u0027] = now\\n      row[\\\"pid\\\"] = process.get(\\\"pid\\\")\\n      row[\\\"process_name\\\"] = process.get(\\\"processName\\\")\\n      row[\\\"process_path\\\"] = process.get(\\\"programPath\\\")\\n      row[\\\"privilege_level\\\"] = process.get(\\\"privilegeLevel\\\")\\n      row[\\\"user\\\"] = process.get(\\\"user\\\")\\n      row[\\\"has_incident\\\"] = process.get(\\\"hasIncident\\\")\\n      row[\\\"suspended\\\"] = process.get(\\\"suspended\\\")\\n      row[\\\"start_time\\\"] = process.get(\\\"startTime\\\")\\n  else:\\n    incident.addNote(u\\\"ReaQta Get Processes unsuccessful: {}\\\".format(results.content.get(\u0027message\u0027)))\\nelse:\\n  incident.addNote(u\\\"ReaQta Get Processes failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_has_incident = rule.properties.reaqta_has_incident\\ninputs.reaqta_suspended = rule.properties.reaqta_suspended\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_105iv85\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_05708f1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_105iv85\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17ds9m6\"/\u003e\u003cendEvent id=\"EndEvent_03c4nkr\"\u003e\u003cincoming\u003eSequenceFlow_05708f1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_05708f1\" sourceRef=\"ServiceTask_17ds9m6\" targetRef=\"EndEvent_03c4nkr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0o7mqwk\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Process List datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_052jgro\" sourceRef=\"ServiceTask_17ds9m6\" targetRef=\"TextAnnotation_0o7mqwk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17ds9m6\" id=\"ServiceTask_17ds9m6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_105iv85\" id=\"SequenceFlow_105iv85_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03c4nkr\" id=\"EndEvent_03c4nkr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"440\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"458\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05708f1\" id=\"SequenceFlow_05708f1_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"404\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0o7mqwk\" id=\"TextAnnotation_0o7mqwk_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"208\" x=\"354\" y=\"54\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_052jgro\" id=\"Association_052jgro_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Get the running processes on a given machine",
      "export_key": "reaqta_get_processes",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535584361,
      "name": "ReaQta: Get Processes",
      "object_type": "incident",
      "programmatic_name": "reaqta_get_processes",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "52eabc99-7975-498c-ab63-6103a9d9fa02",
      "workflow_id": 135
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "reaqta_isolate_endpoint",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_isolate_endpoint\" isExecutable=\"true\" name=\"ReaQta: Isolate Endpoint\"\u003e\u003cdocumentation\u003eIsolate the endpoint machine from the network\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12prgk8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0mv7hpr\" name=\"ReaQta: Isolate Machine\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"79d595f7-b9dc-435c-87bf-e2845fddda94\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success and results.content.get(\u0027success\u0027):\\n  msg = \\\"Endpoint Machine Isolated\\\"\\nelif results.reason:\\n  msg = u\\\"ReaQta Isolate Machine failed: {}\\\".format(results.reason)\\nelse:\\n  msg = u\\\"ReaQta Isolate Machine failed: {}\\\".format(results.content.get(\u0027message\u0027))\\n\\nincident.addNote(msg)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12prgk8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0cwboeb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12prgk8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0mv7hpr\"/\u003e\u003cendEvent id=\"EndEvent_0tj4xao\"\u003e\u003cincoming\u003eSequenceFlow_0cwboeb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0cwboeb\" sourceRef=\"ServiceTask_0mv7hpr\" targetRef=\"EndEvent_0tj4xao\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ponl4v\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the ReaQta process lists datatable and in a Case note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cnekdo\" sourceRef=\"ServiceTask_0mv7hpr\" targetRef=\"TextAnnotation_1ponl4v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0mv7hpr\" id=\"ServiceTask_0mv7hpr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12prgk8\" id=\"SequenceFlow_12prgk8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tj4xao\" id=\"EndEvent_0tj4xao_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"461\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"479\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cwboeb\" id=\"SequenceFlow_0cwboeb_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"418.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ponl4v\" id=\"TextAnnotation_1ponl4v_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"265\" x=\"367\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cnekdo\" id=\"Association_1cnekdo_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"143\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Isolate the endpoint machine from the network",
      "export_key": "reaqta_isolate_endpoint",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535600325,
      "name": "ReaQta: Isolate Endpoint",
      "object_type": "incident",
      "programmatic_name": "reaqta_isolate_endpoint",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "15b24205-66cf-4cde-957f-fb76e116356c",
      "workflow_id": 137
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "reaqta_attach_file_from_process_list",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_attach_file_from_process_list\" isExecutable=\"true\" name=\"ReaQta: Attach File from Process List\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Attach a file from an endpoint\u0027s process list]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1oo1nx1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1imxjev\" name=\"ReaQta: Attach File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6cf8dd59-9465-49a4-8ce8-6538f6c61a4b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(u\\\"ReaQta Attach File created: {} from program path: {}\\\".format(results.content[\u0027name\u0027], results.inputs[\u0027reaqta_program_path\u0027]))\\nelse:\\n  incident.addNote(u\\\"ReaQta Attach File failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_program_path = row[\u0027process_path\u0027].replace(\\\"\\\\\\\\\\\\\\\\\\\", \\\"\\\\\\\\\\\")\\ninputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_incident_id = incident.id\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1oo1nx1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1db59ip\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1oo1nx1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1imxjev\"/\u003e\u003cendEvent id=\"EndEvent_1p2fsdk\"\u003e\u003cincoming\u003eSequenceFlow_1db59ip\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1db59ip\" sourceRef=\"ServiceTask_1imxjev\" targetRef=\"EndEvent_1p2fsdk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0m1lp0i\"\u003e\u003ctext\u003e\u003c![CDATA[Attachment is created and results placed in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wv5eu6\" sourceRef=\"ServiceTask_1imxjev\" targetRef=\"TextAnnotation_0m1lp0i\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1imxjev\" id=\"ServiceTask_1imxjev_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1oo1nx1\" id=\"SequenceFlow_1oo1nx1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"236.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1p2fsdk\" id=\"EndEvent_1p2fsdk_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"437\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"455\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1db59ip\" id=\"SequenceFlow_1db59ip_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"406\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0m1lp0i\" id=\"TextAnnotation_0m1lp0i_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"239\" x=\"361\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wv5eu6\" id=\"Association_0wv5eu6_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "a@example.com",
      "description": "Attach a file from an endpoint\u0027s process list",
      "export_key": "reaqta_attach_file_from_process_list",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535790165,
      "name": "ReaQta: Attach File from Process List",
      "object_type": "reaqta_process_list",
      "programmatic_name": "reaqta_attach_file_from_process_list",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "04c60ae1-1d98-464c-bdc6-f2e62506a383",
      "workflow_id": 132
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "reaqta_create_artifact_from_trigger_event",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_artifact_from_trigger_event\" isExecutable=\"true\" name=\"ReaQta: Create Artifact from Trigger Event\"\u003e\u003cdocumentation\u003eCreate an artifact from a file in the  ReaQta trigger events table\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0n6hif5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0o7hngv\" name=\"ReaQta: Create Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"172eb03f-e7fd-4290-b98b-388ecedcd0e3\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.success:\\n  incident.addNote(\\\"ReaQta Create Artifact failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_incident_id = incident.id\\ninputs.reaqta_artifact_type = \\\"Malware Sample\\\"\\ninputs.reaqta_program_path = row[\u0027program_path\u0027]\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0n6hif5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1643zqe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0n6hif5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0o7hngv\"/\u003e\u003cendEvent id=\"EndEvent_1tkuto6\"\u003e\u003cincoming\u003eSequenceFlow_1643zqe\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1643zqe\" sourceRef=\"ServiceTask_0o7hngv\" targetRef=\"EndEvent_1tkuto6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0zpvb2k\"\u003e\u003ctext\u003e\u003c![CDATA[New artifact (and hashes) are created\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_069v4as\" sourceRef=\"ServiceTask_0o7hngv\" targetRef=\"TextAnnotation_0zpvb2k\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0o7hngv\" id=\"ServiceTask_0o7hngv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"267\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0n6hif5\" id=\"SequenceFlow_0n6hif5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"267\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"232.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tkuto6\" id=\"EndEvent_1tkuto6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"441\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1643zqe\" id=\"SequenceFlow_1643zqe_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"404\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0zpvb2k\" id=\"TextAnnotation_0zpvb2k_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"209\" x=\"359\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_069v4as\" id=\"Association_069v4as_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Create an artifact from a file in the  ReaQta trigger events table",
      "export_key": "reaqta_create_artifact_from_trigger_event",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535455269,
      "name": "ReaQta: Create Artifact from Trigger Event",
      "object_type": "reaqta_trigger_events",
      "programmatic_name": "reaqta_create_artifact_from_trigger_event",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "a805cee2-17ca-47cf-9ad9-2f67359462cb",
      "workflow_id": 129
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "reaqta_create_policy_from_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_policy_from_artifact\" isExecutable=\"true\" name=\"ReaQta: Create Policy from Artifact\"\u003e\u003cdocumentation\u003eCreate a blocking policy from a SHA256 hash\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1y2z2yr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0p3n8y1\" name=\"ReaQta: Create Policy\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7d727515-5a39-4213-8dee-ce9a56e8f26d\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  policies = []\\n  for policy in results.content:\\n    policies.append( \u0027\u0026lt;a href=\\\"{0}\\\" target=\\\"blank\\\"\u0026gt;{0}\u0026lt;/a\u0026gt;\u0027.format(policy.get(\\\"policy_url\\\")))\\n  incident.addNote(helper.createRichText(\\\"ReaQta Create Policies successful: {}\\\".format(\\\"\u0026lt;br\u0026gt;\\\".join(policies))))\\nelse:\\n  incident.addNote(helper.createRichText(\\\"ReaQta Create Policy failed: {}\\\".format(results.reason)))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.reaqta_sha256 = artifact.value\\ninputs.reaqta_policy_title = rule.properties.reaqta_policy_title\\ninputs.reaqta_policy_description = rule.properties.reaqta_policy_description or \u0027\u0027\\ninputs.reaqta_policy_included_groups = rule.properties.reaqta_policy_included_groups\\ninputs.reaqta_policy_excluded_groups = rule.properties.reaqta_policy_excluded_groups\\ninputs.reaqta_policy_enabled = rule.properties.reaqta_policy_enabled\\ninputs.reaqta_policy_block = rule.properties.reaqta_policy_block_when_triggered\\ninputs.reaqta_hive = rule.properties.reaqta_hive if rule.properties.reaqta_hive else incident.properties.reaqta_hive \",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1y2z2yr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1fj6wbv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1y2z2yr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0p3n8y1\"/\u003e\u003cendEvent id=\"EndEvent_1g5jw7t\"\u003e\u003cincoming\u003eSequenceFlow_1fj6wbv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1fj6wbv\" sourceRef=\"ServiceTask_0p3n8y1\" targetRef=\"EndEvent_1g5jw7t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18njsxy\"\u003e\u003ctext\u003eResults returned in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1joulbg\" sourceRef=\"ServiceTask_0p3n8y1\" targetRef=\"TextAnnotation_18njsxy\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0p3n8y1\" id=\"ServiceTask_0p3n8y1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1y2z2yr\" id=\"SequenceFlow_1y2z2yr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1g5jw7t\" id=\"EndEvent_1g5jw7t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"443\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"461\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fj6wbv\" id=\"SequenceFlow_1fj6wbv_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18njsxy\" id=\"TextAnnotation_18njsxy_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"152\" x=\"359\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1joulbg\" id=\"Association_1joulbg_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Create a blocking policy from a SHA256 hash",
      "export_key": "reaqta_create_policy_from_artifact",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647539461630,
      "name": "ReaQta: Create Policy from Artifact",
      "object_type": "artifact",
      "programmatic_name": "reaqta_create_policy_from_artifact",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "ba3ee293-497a-4d74-b4a5-86325fef2e68",
      "workflow_id": 128
    },
    {
      "actions": [],
      "content": {
        "version": 30,
        "workflow_id": "reaqta_get_alert_information",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_get_alert_information\" isExecutable=\"true\" name=\"ReaQta: Get Alert Information\"\u003e\u003cdocumentation\u003eGet alert information and populate the custom fields and datatables\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_13m34t8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1dmrak4\"\u003e\u003cincoming\u003eSequenceFlow_0auqhbv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13m34t8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1s37ruf\"/\u003e\u003cserviceTask id=\"ServiceTask_1s37ruf\" name=\"ReaQta: Get Alert Information\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"13918f45-5268-41b0-8ff0-e6a6223ad302\"\u003e{\"inputs\":{},\"post_processing_script\":\"TRIGGERCONDITION_LOOKUP = {\\n    0: \\\"Code Injection\\\",\\n    1: \\\"Process Impersonated\\\",\\n    2: \\\"Signature Forged\\\",\\n    3: \\\"Incident Correlated\\\",\\n    4: \\\"DLL Sideloaded\\\",\\n    5: \\\"Suspicious Script Executed\\\",\\n    6: \\\"Policies Triggered\\\",\\n    7: \\\"Anomalous Behaviour Detected\\\",\\n    8: \\\"Token Stolen\\\",\\n    9: \\\"Ransomware Behavior Detected\\\",\\n    10: \\\"Privilege Escalated\\\",\\n    11: \\\"External Trigger\\\",\\n    12: \\\"Detection Strategy\\\",\\n    13: \\\"Antimalware Detection\\\"\\n  }\\n\\nif not results.success:\\n  incident.addNote(\\\"ReaQta: Get Alert Information failed: {}\\\".format(results.reason))\\nelse:\\n  content = results.content\\n  alert_url = \u0027\u0026lt;a href=\\\"{0}\\\" target=\\\"blank\\\"\u0026gt;{0}\u0026lt;/a\u0026gt;\u0027.format(content.get(\\\"alert_url\\\"))\\n  incident.properties.reaqta_alert_link = helper.createRichText(alert_url)\\n  incident.properties.reaqta_endpoint_id = content.get(\\\"endpointId\\\")\\n  incident.properties.reaqta_trigger_condition = TRIGGERCONDITION_LOOKUP.get(content.get(\\\"triggerCondition\\\"))\\n  incident.properties.reaqta_impact = content.get(\\\"impact\\\")\\n  \\n  endpoint = content.get(\\\"endpoint\\\", {})\\n  incident.properties.reaqta_tags = \\\", \\\".join(endpoint.get(\\\"tags\\\", []))\\n  incident.properties.reaqta_groups = \\\", \\\".join([ group.get(\\\"name\\\") for group in endpoint.get(\\\"groups\\\", []) ])\\n  incident.properties.reaqta_machine_info = \\\"Machine Name: {}\\\\nOS: {}\\\\nDomain: {}\\\\nCPU: {}\\\"\\\\\\n                          .format(endpoint.get(\u0027name\u0027),\\n                                  endpoint.get(\u0027os\u0027),\\n                                  endpoint.get(\u0027domain\u0027),\\n                                  endpoint.get(\u0027cpuDescr\u0027))\\n                                  \\n  # populate datatable with trigger events\\n  for event in content.get(\u0027triggerEvents\u0027, []):\\n    row = incident.addRow(\u0027reaqta_trigger_events\u0027)\\n    row[\u0027happened_at\u0027] = event.get(\u0027happenedAt_ts\u0027)\\n    row[\u0027category\u0027] = event.get(\u0027category\u0027)\\n    row[\u0027relevance\u0027] = event.get(\u0027relevance\u0027)\\n    row[\u0027severity\u0027] = event.get(\u0027severity\u0027)\\n    \\n    process = event.get(\u0027process\u0027, {})\\n    program = process.get(\u0027program\u0027, {})\\n    if program:\\n      row[\u0027process_pid\u0027] = process.get(\u0027pid\u0027)\\n      row[\u0027program_path\u0027] = program.get(\u0027path\u0027)\\n      row[\u0027sha256_hash\u0027] = program.get(\u0027sha256\u0027)\\n    \\n    if event.get(\u0027category\u0027) == \\\"etw\\\" and event.get(\u0027data\u0027):\\n      data = event.get(\u0027data\u0027)\\n      row[\u0027windows_event_account\u0027] = \\\"{}\\\\\\\\{}\\\".format(data.get(\u0027etwTargetDomainName\u0027), data.get(\u0027etwTargetUserName\u0027))\\n      row[\u0027windows_event_workstation\u0027] = data.get(\u0027etwWorkstationName\u0027)\\n      row[\u0027windows_event_description\u0027] = data.get(\u0027etwEventDescription\u0027)\\n      row[\u0027windows_event_ipport\u0027] = \\\"{}/{}\\\".format(data.get(\u0027etwIpAddress\u0027), data.get(\u0027etwIpPort\u0027))\\n      \\n    if event.get(\u0027category\u0027) == \\\"policies\\\" and event.get(\u0027data\u0027):\\n      data = event.get(\u0027data\u0027)\\n      row[\u0027policy_match\u0027] = data.get(\u0027matched\u0027, [])[0][\u0027policyTitle\u0027]\\n      \\n    \\n    # create artifacts from the trigger event\\n    if program:\\n      incident.addArtifact(\\\"Malware SHA-256 Hash\\\", program.get(\u0027sha256\u0027), \\\"\\\")\\n      incident.addArtifact(\\\"File Path\\\", program.get(\u0027path\u0027), \\\"\\\")\\n      incident.addArtifact(\\\"File Name\\\", program.get(\u0027filename\u0027), \\\"\\\")\\n    if process:\\n      incident.addArtifact(\\\"User Account\\\", process.get(\u0027user\u0027), \\\"\\\")\\n    \\n  # create artifacts from endpoint\\n  endpoint_name = endpoint.get(\\\"name\\\")\\n  incident.addArtifact(\\\"IP Address\\\", endpoint.get(\\\"localAddr\\\"), \\\"Endpoint: {}\\\".format(endpoint_name))\\n  incident.addArtifact(\\\"System Name\\\", endpoint_name, \\\"\\\")\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.reaqta_alert_id = incident.properties.reaqta_id\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_13m34t8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0auqhbv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0auqhbv\" sourceRef=\"ServiceTask_1s37ruf\" targetRef=\"EndEvent_1dmrak4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mfd8d6\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in ReaQta custom fields and datatables\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1jmblpn\" sourceRef=\"ServiceTask_1s37ruf\" targetRef=\"TextAnnotation_1mfd8d6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1dmrak4\" id=\"EndEvent_1dmrak4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"410\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"428\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13m34t8\" id=\"SequenceFlow_13m34t8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"179\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1s37ruf\" id=\"ServiceTask_1s37ruf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0auqhbv\" id=\"SequenceFlow_0auqhbv_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"380\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mfd8d6\" id=\"TextAnnotation_1mfd8d6_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"163\" x=\"335\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1jmblpn\" id=\"Association_1jmblpn_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 30,
      "creator_id": "a@example.com",
      "description": "Get alert information and populate the custom fields and datatables",
      "export_key": "reaqta_get_alert_information",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535564618,
      "name": "ReaQta: Get Alert Information",
      "object_type": "incident",
      "programmatic_name": "reaqta_get_alert_information",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "92bd854f-c669-4ba4-9409-55a9dbe282d5",
      "workflow_id": 138
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "reaqta_close_alert",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_close_alert\" isExecutable=\"true\" name=\"ReaQta: Close Alert\"\u003e\u003cdocumentation\u003eClose the ReaQta Alert\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lyfm85\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xog9el\" name=\"ReaQta: Close Alert\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5801a66d-6b78-40dc-8ec4-f6ab0d842d7c\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Modify this table for custom resolution types\\nIS_MALICIOUS_LOOKUP = {\\n  7: False, # Unresolved\\n  8: False, # Duplicate\\n  9: False, # Not a Issue\\n  10: True  # Resolved\\n}\\n\\ninputs.reaqta_alert_id = incident.properties.reaqta_id\\ninputs.reaqta_note = incident.resolution_summary.content\\ninputs.reaqta_is_malicious = IS_MALICIOUS_LOOKUP.get(incident.resolution_id, False) # if resolution_id is not found, set to not malicious\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lyfm85\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_191zm33\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lyfm85\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xog9el\"/\u003e\u003cendEvent id=\"EndEvent_1a1861k\"\u003e\u003cincoming\u003eSequenceFlow_191zm33\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_191zm33\" sourceRef=\"ServiceTask_0xog9el\" targetRef=\"EndEvent_1a1861k\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0plvu3q\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0cj6l3c\" sourceRef=\"ServiceTask_0xog9el\" targetRef=\"TextAnnotation_0plvu3q\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xog9el\" id=\"ServiceTask_0xog9el_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lyfm85\" id=\"SequenceFlow_1lyfm85_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1a1861k\" id=\"EndEvent_1a1861k_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"447\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"465\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_191zm33\" id=\"SequenceFlow_191zm33_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0plvu3q\" id=\"TextAnnotation_0plvu3q_di\"\u003e\u003comgdc:Bounds height=\"37\" width=\"160\" x=\"361\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0cj6l3c\" id=\"Association_0cj6l3c_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Close the ReaQta Alert",
      "export_key": "reaqta_close_alert",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535906366,
      "name": "ReaQta: Close Alert",
      "object_type": "incident",
      "programmatic_name": "reaqta_close_alert",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "7b5db5ff-e109-451b-ad13-1581177d6e5a",
      "workflow_id": 130
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "reaqta_attach_file_from_triggered_events",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_attach_file_from_triggered_events\" isExecutable=\"true\" name=\"ReaQta: Attach File from Triggered Event\"\u003e\u003cdocumentation\u003eAttach a file from an endpoint\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1clliwp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13gu21v\" name=\"ReaQta: Attach File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6cf8dd59-9465-49a4-8ce8-6538f6c61a4b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(u\\\"ReaQta Attach File created: {} from program path: {}\\\".format(results.content[\u0027name\u0027], results.inputs[\u0027reaqta_program_path\u0027]))\\nelse:\\n  incident.addNote(u\\\"ReaQta Attach File failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_program_path = row[\u0027program_path\u0027]\\ninputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_incident_id = incident.id\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1clliwp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z60ooh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1clliwp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13gu21v\"/\u003e\u003cendEvent id=\"EndEvent_0zqfpz5\"\u003e\u003cincoming\u003eSequenceFlow_0z60ooh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0z60ooh\" sourceRef=\"ServiceTask_13gu21v\" targetRef=\"EndEvent_0zqfpz5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13pgcoq\"\u003e\u003ctext\u003e\u003c![CDATA[Attachment is created and results placed in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13bucvl\" sourceRef=\"ServiceTask_13gu21v\" targetRef=\"TextAnnotation_13pgcoq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13gu21v\" id=\"ServiceTask_13gu21v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1clliwp\" id=\"SequenceFlow_1clliwp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0zqfpz5\" id=\"EndEvent_0zqfpz5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"407.8702611625948\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"425.8702611625948\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z60ooh\" id=\"SequenceFlow_0z60ooh_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"379\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13pgcoq\" id=\"TextAnnotation_13pgcoq_di\"\u003e\u003comgdc:Bounds height=\"47\" width=\"208\" x=\"333\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13bucvl\" id=\"Association_13bucvl_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "a@example.com",
      "description": "Attach a file from an endpoint",
      "export_key": "reaqta_attach_file_from_triggered_events",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535871350,
      "name": "ReaQta: Attach File from Triggered Event",
      "object_type": "reaqta_trigger_events",
      "programmatic_name": "reaqta_attach_file_from_triggered_events",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "b2670fa3-29a7-4e68-9c1a-4586c85f3dec",
      "workflow_id": 136
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "reaqta_create_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_note\" isExecutable=\"true\" name=\"ReaQta: Create Note\"\u003e\u003cdocumentation\u003eAdd a note from SOAR to ReaQta\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1eh3gaj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0f30tsg\" name=\"ReaQta: Create Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"21db5c06-30af-4619-b1ed-1c78b76f36b7\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to ReaQta at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_alert_id = incident.properties.reaqta_id\\ninputs.reaqta_note = note.text.content\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1eh3gaj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_008dyky\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1eh3gaj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0f30tsg\"/\u003e\u003cendEvent id=\"EndEvent_1ef14zp\"\u003e\u003cincoming\u003eSequenceFlow_008dyky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_008dyky\" sourceRef=\"ServiceTask_0f30tsg\" targetRef=\"EndEvent_1ef14zp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10wf16x\"\u003e\u003ctext\u003e\u003c![CDATA[The original note is updated to reflect the synchronization\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ue37i6\" sourceRef=\"ServiceTask_0f30tsg\" targetRef=\"TextAnnotation_10wf16x\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f30tsg\" id=\"ServiceTask_0f30tsg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"265\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1eh3gaj\" id=\"SequenceFlow_1eh3gaj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"265\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"231.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ef14zp\" id=\"EndEvent_1ef14zp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"421\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_008dyky\" id=\"SequenceFlow_008dyky_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10wf16x\" id=\"TextAnnotation_10wf16x_di\"\u003e\u003comgdc:Bounds height=\"55\" width=\"173\" x=\"355\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ue37i6\" id=\"Association_1ue37i6_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Add a note from SOAR to ReaQta",
      "export_key": "reaqta_create_note",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535520547,
      "name": "ReaQta: Create Note",
      "object_type": "note",
      "programmatic_name": "reaqta_create_note",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "cbc2998f-8085-4d1c-9a44-3f3a8660b84a",
      "workflow_id": 131
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "reaqta_create_artifact_from_process_path",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_artifact_from_process_path\" isExecutable=\"true\" name=\"ReaQta: Create Artifact from Process Path\"\u003e\u003cdocumentation\u003eCreate an artifact from a ReaQta Endpoint process file\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1hlay6f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17lnyge\" name=\"ReaQta: Create Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"172eb03f-e7fd-4290-b98b-388ecedcd0e3\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.success:\\n  incident.addNote(\\\"ReaQta Create Artifact failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.reaqta_incident_id = incident.id\\ninputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_program_path = row[\u0027process_path\u0027]\\ninputs.reaqta_artifact_type = \\\"Malware Sample\\\"\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1hlay6f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1skb6wl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1hlay6f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17lnyge\"/\u003e\u003cendEvent id=\"EndEvent_0p1fbiv\"\u003e\u003cincoming\u003eSequenceFlow_1skb6wl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1skb6wl\" sourceRef=\"ServiceTask_17lnyge\" targetRef=\"EndEvent_0p1fbiv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0mihprf\"\u003e\u003ctext\u003e\u003c![CDATA[Artifact (and hashes) created\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xaclpa\" sourceRef=\"ServiceTask_17lnyge\" targetRef=\"TextAnnotation_0mihprf\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17lnyge\" id=\"ServiceTask_17lnyge_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"291\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hlay6f\" id=\"SequenceFlow_1hlay6f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"291\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"244.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0p1fbiv\" id=\"EndEvent_0p1fbiv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"477\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"450\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1skb6wl\" id=\"SequenceFlow_1skb6wl_di\"\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"477\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"389\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0mihprf\" id=\"TextAnnotation_0mihprf_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"138\" x=\"376\" y=\"89\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xaclpa\" id=\"Association_0xaclpa_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"134\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@example.com",
      "description": "Create an artifact from a ReaQta Endpoint process file",
      "export_key": "reaqta_create_artifact_from_process_path",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535441669,
      "name": "ReaQta: Create Artifact from Process Path",
      "object_type": "reaqta_process_list",
      "programmatic_name": "reaqta_create_artifact_from_process_path",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "f05a29af-b43f-4c98-8ffe-d3bbb8ae1076",
      "workflow_id": 139
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "reaqta_create_policy_on_triggered_event",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_policy_on_triggered_event\" isExecutable=\"true\" name=\"ReaQta: Create Policy on Triggered Event\"\u003e\u003cdocumentation\u003eCreate an alert trigger policy based on a file hash\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0deomhd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_07hvdj0\" name=\"ReaQta: Create Policy\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7d727515-5a39-4213-8dee-ce9a56e8f26d\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  policies = []\\n  for policy in results.content:\\n    policies.append( \u0027\u0026lt;a href=\\\"{0}\\\" target=\\\"blank\\\"\u0026gt;{0}\u0026lt;/a\u0026gt;\u0027.format(policy.get(\\\"policy_url\\\")))\\n  incident.addNote(helper.createRichText(\\\"ReaQta Create Policies successful: {}\\\".format(\\\"\u0026lt;br\u0026gt;\\\".join(policies))))\\nelse:\\n  incident.addNote(helper.createRichText(\\\"ReaQta Create Policy failed: {}\\\".format(results.reason)))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_sha256 = row[\u0027sha256_hash\u0027]\\ninputs.reaqta_policy_title = rule.properties.reaqta_policy_title\\ninputs.reaqta_policy_description = rule.properties.reaqta_policy_description or \u0027\u0027\\ninputs.reaqta_policy_included_groups = rule.properties.reaqta_policy_included_groups\\ninputs.reaqta_policy_excluded_groups = rule.properties.reaqta_policy_excluded_groups\\ninputs.reaqta_policy_enabled = rule.properties.reaqta_policy_enabled\\ninputs.reaqta_policy_block = rule.properties.reaqta_policy_block_when_triggered\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0deomhd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1bwqaqw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0deomhd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_07hvdj0\"/\u003e\u003cendEvent id=\"EndEvent_12ufvc0\"\u003e\u003cincoming\u003eSequenceFlow_1bwqaqw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1bwqaqw\" sourceRef=\"ServiceTask_07hvdj0\" targetRef=\"EndEvent_12ufvc0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0apzhcq\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned as a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1w9g2go\" sourceRef=\"ServiceTask_07hvdj0\" targetRef=\"TextAnnotation_0apzhcq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_07hvdj0\" id=\"ServiceTask_07hvdj0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0deomhd\" id=\"SequenceFlow_0deomhd_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_12ufvc0\" id=\"EndEvent_12ufvc0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"447\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"465\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bwqaqw\" id=\"SequenceFlow_1bwqaqw_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"407.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0apzhcq\" id=\"TextAnnotation_0apzhcq_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"190\" x=\"354\" y=\"75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1w9g2go\" id=\"Association_1w9g2go_di\"\u003e\u003comgdi:waypoint x=\"361\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "creator_id": "a@example.com",
      "description": "Create an alert trigger policy based on a file hash",
      "export_key": "reaqta_create_policy_on_triggered_event",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647546248911,
      "name": "ReaQta: Create Policy on Triggered Event",
      "object_type": "reaqta_trigger_events",
      "programmatic_name": "reaqta_create_policy_on_triggered_event",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "2734388a-38c0-4189-a682-0c9c688483a9",
      "workflow_id": 134
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "reaqta_kill_process",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_kill_process\" isExecutable=\"true\" name=\"ReaQta: Kill Process\"\u003e\u003cdocumentation\u003eKill a running process on an endpoint machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1184vnm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1uthi8b\"\u003e\u003cincoming\u003eSequenceFlow_097a1xa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1184vnm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0u6072u\"/\u003e\u003cserviceTask id=\"ServiceTask_0u6072u\" name=\"ReaQta: Kill Process\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f8f32b38-a279-4657-8419-5ce82fcdb36d\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  for process in results.content:\\n    row[\u0027report_date\u0027] = now\\n    if process.get(\u0027killed\u0027):\\n      row[\u0027status\u0027] = \u0027killed\u0027\\n      msg = u\\\"Process: {} ({}) killed\\\".format(row[\u0027process_name\u0027], row[\u0027pid\u0027])\\n    else:\\n      row[\u0027status\u0027] = process.get(\u0027error\u0027)\\n      msg = u\\\"Process: {} ({}) kill failed: {}\\\".format(row[\u0027process_name\u0027], row[\u0027pid\u0027], process.get(\u0027error\u0027))\\n    incident.addNote(msg)\\n    break;\\nelse:\\n  incident.addNote(u\\\"ReaQta Kill Process failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_process_pid = row[\u0027pid\u0027]\\ninputs.reaqta_starttime = row[\u0027start_time\u0027]\\ninputs.reaqta_hive = incident.properties.reaqta_hive\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1184vnm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_097a1xa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_097a1xa\" sourceRef=\"ServiceTask_0u6072u\" targetRef=\"EndEvent_1uthi8b\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04dvz23\"\u003e\u003ctext\u003e\u003c![CDATA[Results updated on datatable and in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1sw8t9y\" sourceRef=\"ServiceTask_0u6072u\" targetRef=\"TextAnnotation_04dvz23\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1uthi8b\" id=\"EndEvent_1uthi8b_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"452\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"470\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1184vnm\" id=\"SequenceFlow_1184vnm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"269\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"188.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0u6072u\" id=\"ServiceTask_0u6072u_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"269\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_097a1xa\" id=\"SequenceFlow_097a1xa_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04dvz23\" id=\"TextAnnotation_04dvz23_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"176\" x=\"357\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1sw8t9y\" id=\"Association_1sw8t9y_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "a@example.com",
      "description": "Kill a running process on an endpoint machine",
      "export_key": "reaqta_kill_process",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1647535619751,
      "name": "ReaQta: Kill Process",
      "object_type": "reaqta_process_list",
      "programmatic_name": "reaqta_kill_process",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "43b8bdd0-263d-4913-9a4f-3a020e9a693d",
      "workflow_id": 133
    }
  ],
  "workspaces": []
}
