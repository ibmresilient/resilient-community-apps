{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ReaQta: Attach File from Process List",
      "id": 103,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Attach File from Process List",
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
      "conditions": [],
      "enabled": true,
      "export_key": "ReaQta: Attach File from Triggered Events",
      "id": 104,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ReaQta: Attach File from Triggered Events",
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
      "id": 105,
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
      "id": 106,
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
          "field_name": "incident.properties.reaqta_endpoint_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ReaQta: Get Processes",
      "id": 100,
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
      "id": 102,
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
      "view_items": [],
      "workflows": [
        "reaqta_isolate_endpoint"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1645451542139,
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
      "export_key": "__function/reaqta_note",
      "hide_notification": false,
      "id": 1058,
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
      "id": 1055,
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
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/reaqta_is_malicious",
      "hide_notification": false,
      "id": 1059,
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
      "id": 1056,
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
      "export_key": "__function/reaqta_starttime",
      "hide_notification": false,
      "id": 1053,
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
      "id": 1038,
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
      "id": 1039,
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
      "export_key": "__function/reaqta_alert_id",
      "hide_notification": false,
      "id": 1057,
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
      "id": 1051,
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
      "id": 1052,
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
      "export_key": "actioninvocation/reaqta_has_incident",
      "hide_notification": false,
      "id": 1049,
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
      "export_key": "actioninvocation/reaqta_suspended",
      "hide_notification": false,
      "id": 1050,
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
      "created_date": 1645134645551,
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
      "id": 119,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347045,
      "name": "reaqta_attach_file",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"type\": \"incident\", \"id\": 48, \"uuid\": \"50df0c2a-e222-4353-90f0-f4f2a2fad3f5\", \"name\": \"notepad.exe\", \"content_type\": \"application/x-msdownload\", \"created\": 1645210092202, \"creator_id\": 3, \"size\": 334262, \"actions\": [{\"id\": 15, \"name\": \"Example: Attachment Hash\", \"enabled\": true}, {\"id\": 16, \"name\": \"Example: Attachment to Base64\", \"enabled\": true}, {\"id\": 20, \"name\": \"Example: Email Parsing (Attachment)\", \"enabled\": true}, {\"id\": 26, \"name\": \"Example: PDFiD\", \"enabled\": true}, {\"id\": 27, \"name\": \"Example: Resilient Search\", \"enabled\": true}, {\"id\": 32, \"name\": \"Example: Use Excel Data\", \"enabled\": false}, {\"id\": 35, \"name\": \"Example: Zip List\", \"enabled\": false}, {\"id\": 34, \"name\": \"Example: Zip Extract\", \"enabled\": false}, {\"id\": 55, \"name\": \"PB: Get workflows/playbooks by attachment name\", \"enabled\": true}, {\"id\": 90, \"name\": \"Example: Virus Total for Attachments\", \"enabled\": true}], \"task_id\": null, \"task_name\": null, \"task_custom\": null, \"task_members\": null, \"task_at_id\": null, \"vers\": 7, \"inc_id\": 2377, \"inc_name\": \"ReaQta Alert - Hive alert Title, Endpoint: AUTISTIC1\", \"inc_owner\": 3}, \"raw\": null, \"inputs\": {\"reaqta_program_path\": \"C:\\\\Windows\\\\System32\\\\notepad.exe\", \"reaqta_endpoint_id\": \"831986736375529472\", \"reaqta_incident_id\": 2377}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 18981, \"timestamp\": \"2022-02-18 13:48:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"uuid\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"created\": {\"type\": \"integer\"}, \"creator_id\": {\"type\": \"integer\"}, \"size\": {\"type\": \"integer\"}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"task_id\": {}, \"task_name\": {}, \"task_custom\": {}, \"task_members\": {}, \"task_at_id\": {}, \"vers\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_program_path\": {\"type\": \"string\"}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "6cf8dd59-9465-49a4-8ce8-6538f6c61a4b",
      "version": 5,
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
          "workflow_id": 77
        },
        {
          "actions": [],
          "description": null,
          "name": "ReaQta: Attach File from Triggered Events",
          "object_type": "reaqta_trigger_events",
          "programmatic_name": "reaqta_attach_file_from_triggered_events",
          "tags": [
            {
              "tag_handle": "fn_reaqta",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 78
        }
      ]
    },
    {
      "created_date": 1645188369149,
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
      "id": 120,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347092,
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
          "workflow_id": 79
        }
      ]
    },
    {
      "created_date": 1645201619950,
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
      "id": 121,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347137,
      "name": "reaqta_create_note",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": \"this is a note in the hive alert\\nIBM SOAR 18/02/2022 14:04:57\\nReaQta Isolate Machine failed: Endpoint offline\", \"raw\": null, \"inputs\": {\"reaqta_alert_id\": \"830607817638412290\", \"reaqta_note\": \"ReaQta Isolate Machine failed: Endpoint offline\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 738, \"timestamp\": \"2022-02-18 14:04:58\"}}",
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
          "workflow_id": 80
        }
      ]
    },
    {
      "created_date": 1645100565943,
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
      "id": 118,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347182,
      "name": "reaqta_get_processes",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"pid\": 0, \"ppid\": 0, \"processName\": \"[System Process]\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 0}, {\"pid\": 4, \"ppid\": 0, \"processName\": \"System\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961331131}, {\"pid\": 92, \"ppid\": 4, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"Registry\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961322746}, {\"pid\": 436, \"ppid\": 4, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"smss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\smss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961331143}, {\"pid\": 556, \"ppid\": 544, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961338892}, {\"pid\": 628, \"ppid\": 544, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"wininit.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\wininit.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339001}, {\"pid\": 640, \"ppid\": 620, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339017}, {\"pid\": 724, \"ppid\": 620, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"winlogon.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\winlogon.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339380}, {\"pid\": 732, \"ppid\": 628, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"services.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\services.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961339390}, {\"pid\": 772, \"ppid\": 628, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"lsass.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\lsass.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339460}, {\"pid\": 884, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961339914}, {\"pid\": 896, \"ppid\": 724, \"privilegeLevel\": \"LOW\", \"processName\": \"fontdrvhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\fontdrvhost.exe\", \"user\": \"Font Driver Host\\\\UMFD-1\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339927}, {\"pid\": 912, \"ppid\": 628, \"privilegeLevel\": \"LOW\", \"processName\": \"fontdrvhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\fontdrvhost.exe\", \"user\": \"Font Driver Host\\\\UMFD-0\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961339946}, {\"pid\": 1000, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961340275}, {\"pid\": 472, \"ppid\": 724, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"LogonUI.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\LogonUI.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961340596}, {\"pid\": 576, \"ppid\": 724, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"dwm.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dwm.exe\", \"user\": \"Window Manager\\\\DWM-1\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961340622}, {\"pid\": 852, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961340865}, {\"pid\": 464, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961340913}, {\"pid\": 620, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961340926}, {\"pid\": 1124, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961341186}, {\"pid\": 1140, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961341257}, {\"pid\": 1356, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961341717}, {\"pid\": 1440, \"ppid\": 4, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"Memory Compression\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961342023}, {\"pid\": 1460, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961342039}, {\"pid\": 1620, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961342427}, {\"pid\": 1856, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961342810}, {\"pid\": 1884, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961342857}, {\"pid\": 1948, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961343041}, {\"pid\": 1176, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961343608}, {\"pid\": 2108, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346043}, {\"pid\": 2276, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\NETWORK SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346722}, {\"pid\": 2312, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"blnsvr.exe\", \"programPath\": \"C:\\\\Windows\\\\blnsvr.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346822}, {\"pid\": 2320, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346824}, {\"pid\": 2368, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"CSFalconService.exe\", \"programPath\": \"C:\\\\Program Files\\\\CrowdStrike\\\\CSFalconService.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346948}, {\"pid\": 2380, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961346955}, {\"pid\": 2528, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"sshd.exe\", \"programPath\": \"C:\\\\Program Files\\\\OpenSSH\\\\OpenSSH-Win64\\\\sshd.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961347484}, {\"pid\": 3000, \"ppid\": 2368, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"CSFalconContainer.exe\", \"programPath\": \"C:\\\\Program Files\\\\CrowdStrike\\\\CSFalconContainer.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961348699}, {\"pid\": 3152, \"ppid\": 884, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"WmiPrvSE.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\wbem\\\\WmiPrvSE.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961352416}, {\"pid\": 3728, \"ppid\": 2368, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"CSFalconContainer.exe\", \"programPath\": \"C:\\\\Program Files\\\\CrowdStrike\\\\CSFalconContainer.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961368738}, {\"pid\": 3748, \"ppid\": 884, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"WmiPrvSE.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\wbem\\\\WmiPrvSE.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961388853}, {\"pid\": 1900, \"ppid\": 884, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"MoUsoCoreWorker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\MoUsoCoreWorker.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961433195}, {\"pid\": 564, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1644961436735}, {\"pid\": 4824, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"SgrmBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\SgrmBroker.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961471025}, {\"pid\": 4908, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961471848}, {\"pid\": 4984, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961472709}, {\"pid\": 5032, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"SearchIndexer.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\SearchIndexer.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1644961473036}, {\"pid\": 2284, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645025103929}, {\"pid\": 3764, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645051594644}, {\"pid\": 3440, \"ppid\": 4092, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"csrss.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\csrss.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128644187}, {\"pid\": 2348, \"ppid\": 4092, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"winlogon.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\winlogon.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128644487}, {\"pid\": 540, \"ppid\": 2348, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"dwm.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dwm.exe\", \"user\": \"Window Manager\\\\DWM-2\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128645447}, {\"pid\": 1392, \"ppid\": 2348, \"privilegeLevel\": \"LOW\", \"processName\": \"fontdrvhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\fontdrvhost.exe\", \"user\": \"Font Driver Host\\\\UMFD-2\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128645487}, {\"pid\": 1816, \"ppid\": 852, \"privilegeLevel\": \"HIGH\", \"processName\": \"rdpclip.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\rdpclip.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128652638}, {\"pid\": 4676, \"ppid\": 1140, \"privilegeLevel\": \"HIGH\", \"processName\": \"sihost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\sihost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128653387}, {\"pid\": 2644, \"ppid\": 732, \"privilegeLevel\": \"HIGH\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128653498}, {\"pid\": 3864, \"ppid\": 1140, \"privilegeLevel\": \"HIGH\", \"processName\": \"taskhostw.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\taskhostw.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128654271}, {\"pid\": 4752, \"ppid\": 464, \"privilegeLevel\": \"HIGH\", \"processName\": \"ctfmon.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\ctfmon.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128655452}, {\"pid\": 4772, \"ppid\": 3772, \"privilegeLevel\": \"HIGH\", \"processName\": \"explorer.exe\", \"programPath\": \"C:\\\\Windows\\\\explorer.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128657528}, {\"pid\": 5764, \"ppid\": 732, \"privilegeLevel\": \"HIGH\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128676008}, {\"pid\": 5560, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"StartMenuExperienceHost.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\\\\StartMenuExperienceHost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128688180}, {\"pid\": 4048, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128689788}, {\"pid\": 5456, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128693320}, {\"pid\": 6084, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"SearchApp.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\Microsoft.Windows.Search_cw5n1h2txyewy\\\\SearchApp.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": true, \"startTime\": 1645128694606}, {\"pid\": 5204, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"YourPhone.exe\", \"programPath\": \"C:\\\\Program Files\\\\WindowsApps\\\\Microsoft.YourPhone_1.21121.256.0_x64__8wekyb3d8bbwe\\\\YourPhone.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": true, \"startTime\": 1645128696056}, {\"pid\": 6876, \"ppid\": 4772, \"privilegeLevel\": \"HIGH\", \"processName\": \"SecurityHealthSystray.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\SecurityHealthSystray.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128709527}, {\"pid\": 7028, \"ppid\": 4772, \"privilegeLevel\": \"HIGH\", \"processName\": \"OneDrive.exe\", \"programPath\": \"C:\\\\Users\\\\Administrator\\\\AppData\\\\Local\\\\Microsoft\\\\OneDrive\\\\OneDrive.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645128711380}, {\"pid\": 7036, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"SecurityHealthService.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\SecurityHealthService.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128711525}, {\"pid\": 7044, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"dllhost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\dllhost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128711678}, {\"pid\": 7652, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128743840}, {\"pid\": 7860, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"SearchApp.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\Microsoft.Windows.Search_cw5n1h2txyewy\\\\SearchApp.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": true, \"startTime\": 1645128752154}, {\"pid\": 2104, \"ppid\": 1140, \"privilegeLevel\": \"HIGH\", \"processName\": \"taskhostw.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\taskhostw.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128758242}, {\"pid\": 6596, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"ShellExperienceHost.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\ShellExperienceHost_cw5n1h2txyewy\\\\ShellExperienceHost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128818387}, {\"pid\": 6136, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128819903}, {\"pid\": 5944, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128863139}, {\"pid\": 7596, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"SettingSyncHost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\SettingSyncHost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645128966285}, {\"pid\": 6712, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"Microsoft.Photos.exe\", \"programPath\": \"C:\\\\Program Files\\\\WindowsApps\\\\Microsoft.Windows.Photos_2021.21090.10008.0_x64__8wekyb3d8bbwe\\\\Microsoft.Photos.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": true, \"startTime\": 1645130455541}, {\"pid\": 6556, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"RuntimeBroker.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\RuntimeBroker.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645130459641}, {\"pid\": 1416, \"ppid\": 884, \"privilegeLevel\": \"LOW\", \"processName\": \"TextInputHost.exe\", \"programPath\": \"C:\\\\Windows\\\\SystemApps\\\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\\\\TextInputHost.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645130848211}, {\"pid\": 7904, \"ppid\": 4772, \"privilegeLevel\": \"HIGH\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130852284}, {\"pid\": 7560, \"ppid\": 7904, \"privilegeLevel\": \"HIGH\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130852739}, {\"pid\": 7756, \"ppid\": 7904, \"privilegeLevel\": \"LOW\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130854153}, {\"pid\": 4544, \"ppid\": 7904, \"privilegeLevel\": \"HIGH\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130854303}, {\"pid\": 1044, \"ppid\": 7904, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130855630}, {\"pid\": 7796, \"ppid\": 7904, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130856112}, {\"pid\": 4140, \"ppid\": 7904, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645130858790}, {\"pid\": 908, \"ppid\": 7904, \"privilegeLevel\": \"UNTRUSTED\", \"processName\": \"chrome.exe\", \"programPath\": \"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645142344689}, {\"pid\": 5844, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"WUDFHost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\WUDFHost.exe\", \"user\": \"NT AUTHORITY\\\\LOCAL SERVICE\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645209720497}, {\"pid\": 2364, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645209721496}, {\"pid\": 7524, \"ppid\": 732, \"privilegeLevel\": \"SYSTEM\", \"processName\": \"svchost.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\svchost.exe\", \"user\": \"NT AUTHORITY\\\\SYSTEM\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645209724529}, {\"pid\": 6736, \"ppid\": 884, \"privilegeLevel\": \"HIGH\", \"processName\": \"smartscreen.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\smartscreen.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": true, \"suspended\": false, \"startTime\": 1645209738309}, {\"pid\": 4172, \"ppid\": 4772, \"privilegeLevel\": \"HIGH\", \"processName\": \"notepad.exe\", \"programPath\": \"C:\\\\Windows\\\\System32\\\\notepad.exe\", \"user\": \"AUTISTIC1\\\\Administrator\", \"hasIncident\": false, \"suspended\": false, \"startTime\": 1645209904609}], \"raw\": null, \"inputs\": {\"reaqta_has_incident\": null, \"reaqta_endpoint_id\": \"831986736375529472\", \"reaqta_suspended\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-reaqta\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 953, \"timestamp\": \"2022-02-18 13:47:22\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"pid\": {\"type\": \"integer\"}, \"ppid\": {\"type\": \"integer\"}, \"processName\": {\"type\": \"string\"}, \"hasIncident\": {\"type\": \"boolean\"}, \"suspended\": {\"type\": \"boolean\"}, \"startTime\": {\"type\": \"integer\"}, \"privilegeLevel\": {\"type\": \"string\"}, \"user\": {\"type\": \"string\"}, \"programPath\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"reaqta_has_incident\": {}, \"reaqta_endpoint_id\": {\"type\": \"string\"}, \"reaqta_suspended\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "f97be6f0-081a-47af-931f-5e2b101aec3a",
      "version": 3,
      "view_items": [
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
          "workflow_id": 74
        }
      ]
    },
    {
      "created_date": 1645060584312,
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
      "id": 117,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347232,
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
          "workflow_id": 76
        }
      ]
    },
    {
      "created_date": 1645060501766,
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
      "id": 116,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645213347278,
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
      "version": 4,
      "view_items": [
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
          "tags": [],
          "uuid": null,
          "workflow_id": 75
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 25,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1645451541057,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1645451541057,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "b55918cb-49c8-493d-ba5c-1e59cd0e9db9"
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
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Process PID",
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
          "order": 5,
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
        "version": 7,
        "workflow_id": "reaqta_close_alert",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_close_alert\" isExecutable=\"true\" name=\"ReaQta: Close Alert\"\u003e\u003cdocumentation\u003eClose the ReaQta Alert\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lyfm85\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xog9el\" name=\"ReaQta: Close Alert\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5801a66d-6b78-40dc-8ec4-f6ab0d842d7c\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Modify this table for custom resolution types\\nIS_MALICIOUS_LOOKUP = {\\n  7: False, # Unresolved\\n  8: False, # Duplicate\\n  9: False, # Not a Issue\\n  10: True  # Resolved\\n}\\n\\ninputs.reaqta_alert_id = incident.properties.reaqta_id\\ninputs.reaqta_note = incident.resolution_summary.content\\ninputs.reaqta_is_malicious = IS_MALICIOUS_LOOKUP.get(incident.resolution_id, False) # if resolution_id is not found, set to not malicious\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lyfm85\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_191zm33\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lyfm85\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xog9el\"/\u003e\u003cendEvent id=\"EndEvent_1a1861k\"\u003e\u003cincoming\u003eSequenceFlow_191zm33\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_191zm33\" sourceRef=\"ServiceTask_0xog9el\" targetRef=\"EndEvent_1a1861k\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0plvu3q\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0cj6l3c\" sourceRef=\"ServiceTask_0xog9el\" targetRef=\"TextAnnotation_0plvu3q\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xog9el\" id=\"ServiceTask_0xog9el_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lyfm85\" id=\"SequenceFlow_1lyfm85_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1a1861k\" id=\"EndEvent_1a1861k_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"447\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"465\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_191zm33\" id=\"SequenceFlow_191zm33_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0plvu3q\" id=\"TextAnnotation_0plvu3q_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"143\" x=\"361\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0cj6l3c\" id=\"Association_0cj6l3c_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Close the ReaQta Alert",
      "export_key": "reaqta_close_alert",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450869008,
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
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "reaqta_attach_file_from_triggered_events",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_attach_file_from_triggered_events\" isExecutable=\"true\" name=\"ReaQta: Attach File from Triggered Events\"\u003e\u003cdocumentation\u003eAttach a file from an endpoint\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1clliwp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13gu21v\" name=\"ReaQta: Attach File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6cf8dd59-9465-49a4-8ce8-6538f6c61a4b\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_program_path = row[\u0027program_path\u0027]\\ninputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_incident_id = incident.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1clliwp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z60ooh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1clliwp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13gu21v\"/\u003e\u003cendEvent id=\"EndEvent_0zqfpz5\"\u003e\u003cincoming\u003eSequenceFlow_0z60ooh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0z60ooh\" sourceRef=\"ServiceTask_13gu21v\" targetRef=\"EndEvent_0zqfpz5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13gu21v\" id=\"ServiceTask_13gu21v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1clliwp\" id=\"SequenceFlow_1clliwp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0zqfpz5\" id=\"EndEvent_0zqfpz5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"407.8702611625948\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"425.8702611625948\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z60ooh\" id=\"SequenceFlow_0z60ooh_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"379\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@example.com",
      "description": "Attach a file from an endpoint",
      "export_key": "reaqta_attach_file_from_triggered_events",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450838270,
      "name": "ReaQta: Attach File from Triggered Events",
      "object_type": "reaqta_trigger_events",
      "programmatic_name": "reaqta_attach_file_from_triggered_events",
      "tags": [
        {
          "tag_handle": "fn_reaqta",
          "value": null
        }
      ],
      "uuid": "b2670fa3-29a7-4e68-9c1a-4586c85f3dec",
      "workflow_id": 78
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "reaqta_attach_file_from_process_list",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_attach_file_from_process_list\" isExecutable=\"true\" name=\"ReaQta: Attach File from Process List\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Attach a file from an endpoint\u0027s process list]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1oo1nx1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1imxjev\" name=\"ReaQta: Attach File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6cf8dd59-9465-49a4-8ce8-6538f6c61a4b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(u\\\"ReaQta Attach File created: {} from program path: {}\\\".format(results.content[\u0027name\u0027], results.inputs[\u0027reaqta_program_path\u0027]))\\nelse:\\n  incident.addNote(u\\\"ReaQta Attach File failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_program_path = row[\u0027process_path\u0027].replace(\\\"\\\\\\\\\\\\\\\\\\\", \\\"\\\\\\\\\\\")\\ninputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_incident_id = incident.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1oo1nx1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1db59ip\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1oo1nx1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1imxjev\"/\u003e\u003cendEvent id=\"EndEvent_1p2fsdk\"\u003e\u003cincoming\u003eSequenceFlow_1db59ip\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1db59ip\" sourceRef=\"ServiceTask_1imxjev\" targetRef=\"EndEvent_1p2fsdk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0m1lp0i\"\u003e\u003ctext\u003e\u003c![CDATA[Results placed in a note and when successful, an attachment is created\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wv5eu6\" sourceRef=\"ServiceTask_1imxjev\" targetRef=\"TextAnnotation_0m1lp0i\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1imxjev\" id=\"ServiceTask_1imxjev_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1oo1nx1\" id=\"SequenceFlow_1oo1nx1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"236.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1p2fsdk\" id=\"EndEvent_1p2fsdk_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"437\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"455\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1db59ip\" id=\"SequenceFlow_1db59ip_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"406\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0m1lp0i\" id=\"TextAnnotation_0m1lp0i_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"239\" x=\"361\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wv5eu6\" id=\"Association_0wv5eu6_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@example.com",
      "description": "Attach a file from an endpoint\u0027s process list",
      "export_key": "reaqta_attach_file_from_process_list",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450818906,
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
      "workflow_id": 77
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "reaqta_create_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_create_note\" isExecutable=\"true\" name=\"ReaQta: Create Note\"\u003e\u003cdocumentation\u003eAdd a note from SOAR to ReaQta\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1eh3gaj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0f30tsg\" name=\"ReaQta: Create Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"21db5c06-30af-4619-b1ed-1c78b76f36b7\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to ReaQta at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_alert_id = incident.properties.reaqta_id\\ninputs.reaqta_note = note.text.content\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1eh3gaj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_008dyky\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1eh3gaj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0f30tsg\"/\u003e\u003cendEvent id=\"EndEvent_1ef14zp\"\u003e\u003cincoming\u003eSequenceFlow_008dyky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_008dyky\" sourceRef=\"ServiceTask_0f30tsg\" targetRef=\"EndEvent_1ef14zp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f30tsg\" id=\"ServiceTask_0f30tsg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"265\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1eh3gaj\" id=\"SequenceFlow_1eh3gaj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"265\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"231.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ef14zp\" id=\"EndEvent_1ef14zp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"421\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_008dyky\" id=\"SequenceFlow_008dyky_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Add a note from SOAR to ReaQta",
      "export_key": "reaqta_create_note",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450886788,
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
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "reaqta_isolate_endpoint",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_isolate_endpoint\" isExecutable=\"true\" name=\"ReaQta: Isolate Endpoint\"\u003e\u003cdocumentation\u003eIsolate the endpoint machine from the network\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12prgk8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0mv7hpr\" name=\"ReaQta: Isolate Machine\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"79d595f7-b9dc-435c-87bf-e2845fddda94\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success and results.content.get(\u0027success\u0027):\\n  msg = \\\"Endpoint Machine Isolated\\\"\\nelif results.reason:\\n  msg = u\\\"ReaQta Isolate Machine failed: {}\\\".format(results.reason)\\nelse:\\n  msg = u\\\"ReaQta Isolate Machine failed: {}\\\".format(results.content.get(\u0027message\u0027))\\n\\nincident.addNote(msg)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12prgk8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0cwboeb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12prgk8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0mv7hpr\"/\u003e\u003cendEvent id=\"EndEvent_0tj4xao\"\u003e\u003cincoming\u003eSequenceFlow_0cwboeb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0cwboeb\" sourceRef=\"ServiceTask_0mv7hpr\" targetRef=\"EndEvent_0tj4xao\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ponl4v\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the ReaQta process lists datatable and in a Case note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cnekdo\" sourceRef=\"ServiceTask_0mv7hpr\" targetRef=\"TextAnnotation_1ponl4v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0mv7hpr\" id=\"ServiceTask_0mv7hpr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12prgk8\" id=\"SequenceFlow_12prgk8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tj4xao\" id=\"EndEvent_0tj4xao_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"461\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"479\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cwboeb\" id=\"SequenceFlow_0cwboeb_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"418.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ponl4v\" id=\"TextAnnotation_1ponl4v_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"265\" x=\"367\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cnekdo\" id=\"Association_1cnekdo_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"143\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@example.com",
      "description": "Isolate the endpoint machine from the network",
      "export_key": "reaqta_isolate_endpoint",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450902436,
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
      "workflow_id": 76
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "reaqta_get_processes",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"reaqta_get_processes\" isExecutable=\"true\" name=\"ReaQta: Get Processes\"\u003e\u003cdocumentation\u003eGet the running processes on a given machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_105iv85\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17ds9m6\" name=\"ReaQta: Get Processes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f97be6f0-081a-47af-931f-5e2b101aec3a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  if isinstance(results.content, list):\\n    for process in results.content:\\n      row = incident.addRow(\\\"reaqta_process_list\\\")\\n      \\n      row[\u0027report_date\u0027] = now\\n      row[\\\"pid\\\"] = process.get(\\\"pid\\\")\\n      row[\\\"process_name\\\"] = process.get(\\\"processName\\\")\\n      row[\\\"process_path\\\"] = process.get(\\\"programPath\\\")\\n      row[\\\"privilege_level\\\"] = process.get(\\\"privilegeLevel\\\")\\n      row[\\\"user\\\"] = process.get(\\\"user\\\")\\n      row[\\\"has_incident\\\"] = process.get(\\\"hasIncident\\\")\\n      row[\\\"suspended\\\"] = process.get(\\\"suspended\\\")\\n      row[\\\"start_time\\\"] = process.get(\\\"startTime\\\")\\n  else:\\n    incident.addNote(u\\\"ReaQta Get Processes unsuccessful: {}\\\".format(results.content.get(\u0027message\u0027)))\\nelse:\\n  incident.addNote(u\\\"ReaQta Get Processes failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id\\ninputs.reaqta_has_incident = rule.properties.reaqta_has_incident\\ninputs.reaqta_suspended = rule.properties.reaqta_suspended\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_105iv85\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_05708f1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_105iv85\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17ds9m6\"/\u003e\u003cendEvent id=\"EndEvent_03c4nkr\"\u003e\u003cincoming\u003eSequenceFlow_05708f1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_05708f1\" sourceRef=\"ServiceTask_17ds9m6\" targetRef=\"EndEvent_03c4nkr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0o7mqwk\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Process List datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_052jgro\" sourceRef=\"ServiceTask_17ds9m6\" targetRef=\"TextAnnotation_0o7mqwk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17ds9m6\" id=\"ServiceTask_17ds9m6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_105iv85\" id=\"SequenceFlow_105iv85_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03c4nkr\" id=\"EndEvent_03c4nkr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"440\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"458\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05708f1\" id=\"SequenceFlow_05708f1_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"404\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0o7mqwk\" id=\"TextAnnotation_0o7mqwk_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"208\" x=\"354\" y=\"54\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_052jgro\" id=\"Association_052jgro_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Get the running processes on a given machine",
      "export_key": "reaqta_get_processes",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645450648745,
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
      "workflow_id": 74
    }
  ],
  "workspaces": []
}
