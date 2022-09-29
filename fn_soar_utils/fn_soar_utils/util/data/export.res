{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "Log File",
            "Other File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: SOAR Utilities (Artifact) Attachment to Base64",
      "id": 84,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities (Artifact) Attachment to Base64",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5527a676-030b-4f7f-af4d-3488b9d8313f",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_artifact_attachment_to_base64"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Artifact Hash",
      "id": 86,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Artifact Hash",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2c968a14-d4ec-4c91-b47b-f25a1da35f03",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_artifact_hash"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Attachment Hash",
      "id": 85,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Attachment Hash",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e3052b30-486a-4d70-b82d-b8cde6222517",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_attachment_hash"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Attachment to Base64",
      "id": 87,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Attachment to Base64",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "80931de0-6918-48e9-8ea1-d6d93fbeee99",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_attachment_to_base64"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Close Incident",
      "id": 88,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Close Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "60c8cfda-d72a-471b-b475-8acbb2b002d2",
      "view_items": [
        {
          "content": "d5865351-161e-4209-b015-f821b1e7a2f2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_soar_utilities_close_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Create Incident",
      "id": 89,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Create Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c2485cfc-3cc7-4eac-afb9-84bb8ac79688",
      "view_items": [
        {
          "content": "4c87e9f9-281f-483f-a5c3-03458440bbf1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_soar_utilities_create_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Get Incident Contact Info",
      "id": 91,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Get Incident Contact Info",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0124443c-cf3f-496a-9938-26dcbefdefe3",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_get_incident_contact_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Get Task Contact Info",
      "id": 92,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Get Task Contact Info",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cd6412d5-0d21-425e-9856-cff5472dca37",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_get_task_contact_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Search Incidents",
      "id": 93,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Search Incidents",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "77f1bcc9-409c-4d35-ac98-ede7f59ee024",
      "view_items": [
        {
          "content": "97743290-ddbe-4936-852f-e2ac5d1ccb9d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "886022ba-5545-4042-b882-6b8ce2fb72b6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_soar_utilities_search_incidents"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities SOAR Search",
      "id": 90,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities SOAR Search",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "12c2bbd6-50ab-4b9f-ae3f-e4c57519dd5f",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_soar_search"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: SOAR Utilities String to Attachment",
      "id": 94,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: SOAR Utilities String to Attachment",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ce4597cb-c9dd-40c8-a256-af45480eb05c",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_string_to_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/zip"
        }
      ],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Zip Extract",
      "id": 95,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Zip Extract",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "928a6a39-110e-42bb-be83-b19c48450417",
      "view_items": [
        {
          "content": "1afa8c6e-20a4-4104-b979-be49c89dff23",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "35eb4622-74b2-4502-88eb-2858bcbe6cf7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_soar_utilities_zip_extract"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/zip"
        }
      ],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Zip Extract to Artifact",
      "id": 97,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Zip Extract to Artifact",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "09431acd-b2d4-4729-a3aa-ba056e602c03",
      "view_items": [
        {
          "content": "1afa8c6e-20a4-4104-b979-be49c89dff23",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "35eb4622-74b2-4502-88eb-2858bcbe6cf7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_soar_utilities_zip_extract_to_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        },
        {
          "evaluation_id": null,
          "field_name": "attachment.content_type",
          "method": "equals",
          "type": null,
          "value": "application/zip"
        }
      ],
      "enabled": true,
      "export_key": "Example: SOAR Utilities Zip List",
      "id": 96,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: SOAR Utilities Zip List",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1e6fc03f-f073-49e4-8eda-7a3645601de6",
      "view_items": [],
      "workflows": [
        "example_soar_utilities_zip_list"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1664479429591,
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
      "export_key": "__function/soar_utils_sort_fields",
      "hide_notification": false,
      "id": 404,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_sort_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"id\", \"type\": \"asc\"}]",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_sort_fields",
      "tooltip": "json fields to order result set",
      "type_id": 11,
      "uuid": "98a5216f-6bf6-46e1-94ea-344b9d36cc84",
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
      "export_key": "__function/soar_utils_artifact_file_type",
      "hide_notification": false,
      "id": 399,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_artifact_file_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_artifact_file_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a2811c56-b510-40fd-bbbd-afafe0ddf6f0",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Attachment",
          "properties": null,
          "uuid": "beb27e7a-5081-4be4-b33c-fc28095fddb2",
          "value": 220
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Malware Sample",
          "properties": null,
          "uuid": "7c233ba5-5780-4f7e-b725-1e56de15e791",
          "value": 221
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Log File",
          "properties": null,
          "uuid": "6ca8e1a9-8bdf-4510-a1ec-ab374e37fcd6",
          "value": 222
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "X509 Certificate File",
          "properties": null,
          "uuid": "634bb908-9d41-4504-b7ac-711e3f788d0f",
          "value": 223
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RFC 822 Email Message File",
          "properties": null,
          "uuid": "33e8c8df-83ec-4af2-bd62-002397774853",
          "value": 224
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other File",
          "properties": null,
          "uuid": "af967e58-06ef-463d-86d6-227b257d2228",
          "value": 225
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 289,
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
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_slack",
          "value": null
        },
        {
          "tag_handle": "fn_urlscanio",
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
      "uuid": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
      "export_key": "__function/soar_utils_description",
      "hide_notification": false,
      "id": 396,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b5563a4f-73e5-4e11-b3eb-aa1be3c72300",
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
      "export_key": "__function/soar_utils_zipfile_password",
      "hide_notification": false,
      "id": 394,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_zipfile_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_zipfile_password",
      "tooltip": "",
      "type_id": 11,
      "uuid": "cba48e26-0b59-4984-b2ce-3be1bda58d31",
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
      "export_key": "__function/artifact_id",
      "hide_notification": false,
      "id": 290,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_slack",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
      "templates": [],
      "text": "artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 298,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
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
      "export_key": "__function/soar_utils_string_to_convert_to_attachment",
      "hide_notification": false,
      "id": 405,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_string_to_convert_to_attachment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_string_to_convert_to_attachment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "019b19a5-b165-4258-baa0-6c57cdabb3f5",
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
      "export_key": "__function/attachment_name",
      "hide_notification": false,
      "id": 344,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "attachment_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "attachment_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "03955f53-5940-49ff-a9df-0b607099657b",
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
      "export_key": "__function/soar_utils_file_path",
      "hide_notification": false,
      "id": 395,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_file_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_file_path",
      "tooltip": "",
      "type_id": 11,
      "uuid": "09debd01-5de2-462b-9e97-2e4ec5db0098",
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
      "export_key": "__function/attachment_id",
      "hide_notification": false,
      "id": 291,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_slack",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
      "templates": [],
      "text": "attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "17c3e652-6559-4935-9f95-74374ca37a7b",
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
      "export_key": "__function/soar_utils_create_fields",
      "hide_notification": false,
      "id": 402,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_create_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"name\": \"sample\", \"description\": \"sample incident\", \"discovered_date\": 1621110044000}",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_create_fields",
      "tooltip": "json fields to create an incident",
      "type_id": 11,
      "uuid": "25c64fed-b7d1-4a7a-b661-f865dff641e0",
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
      "export_key": "__function/soar_search_template",
      "hide_notification": false,
      "id": 387,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_search_template",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 4,
          "name": "attachments",
          "template": {
            "content": "\n  \"types\": [\"attachment\"],\n  \"filters\": {\n    \"incident\": [{\n        \"conditions\": [{\"field_name\": \"plan_status\", \"method\": \"in\", \"value\": [\"A\"]}]\n      }]\n  }\n}",
            "format": "text"
          },
          "uuid": "add41197-519d-4d28-9276-538dac2729b7"
        },
        {
          "id": 5,
          "name": "artifacts",
          "template": {
            "content": "{\n  \"types\": [\"artifact\"],\n  \"filters\": {\n    \"incident\": [{\n        \"conditions\": [{\"field_name\": \"plan_status\", \"method\": \"in\", \"value\": [\"A\"]}]\n      }]\n  }\n}",
            "format": "text"
          },
          "uuid": "2294757f-3763-432b-aadd-85a895fd8b9b"
        }
      ],
      "text": "soar_search_template",
      "tooltip": "",
      "type_id": 11,
      "uuid": "357b3f18-2df2-4b39-8128-af57eb91821a",
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
      "export_key": "__function/soar_utils_base64content",
      "hide_notification": false,
      "id": 400,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_base64content",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_base64content",
      "tooltip": "",
      "type_id": 11,
      "uuid": "42b4175a-96df-4e92-8be7-65ecbf500127",
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
      "export_key": "__function/soar_utils_content_type",
      "hide_notification": false,
      "id": 398,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_content_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_content_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "462e6c47-7587-4cc6-b2c6-f05ef09a8797",
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
      "export_key": "__function/soar_search_query",
      "hide_notification": false,
      "id": 386,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_search_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_search_query",
      "tooltip": "",
      "type_id": 11,
      "uuid": "4e3867ee-0cf5-4aa6-9867-079dba934dc0",
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
      "export_key": "__function/soar_utils_close_fields",
      "hide_notification": false,
      "id": 401,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_close_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_close_fields",
      "tooltip": "A JSON String of the fields required to close an Incident e.g.: {\u0027resolution_id\u0027:\u0027Resolved\u0027,\u0027resolution_summary\u0027:\u0027closing\u0027}",
      "type_id": 11,
      "uuid": "662e4f24-b241-48f6-959c-993d76feb214",
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
      "export_key": "__function/soar_utils_filter_conditions",
      "hide_notification": false,
      "id": 403,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_filter_conditions",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"name\", \"method\":\"contains\", \"value\":\"sample\"}]",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_filter_conditions",
      "tooltip": "json fields to filter incident records to return",
      "type_id": 11,
      "uuid": "6d6ae16e-8fbe-42a1-b4c1-5e34ee1b0e7c",
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
      "export_key": "__function/soar_utils_file_name",
      "hide_notification": false,
      "id": 397,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_file_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "soar_utils_file_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7d7a8353-5d6b-4890-99d1-7bfc9fd64287",
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
      "export_key": "actioninvocation/soar_utils_sort_fields",
      "hide_notification": false,
      "id": 391,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_sort_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"id\",\"type\":\"asc\"}]",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Sort Fields",
      "tooltip": "json formatted sort fields or leave empty",
      "type_id": 6,
      "uuid": "886022ba-5545-4042-b882-6b8ce2fb72b6",
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
      "export_key": "actioninvocation/soar_utils_search_fields",
      "hide_notification": false,
      "id": 390,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_search_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"create_date\",\"method\":\"gte\",\"value\":1614574800000}]",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Search Fields",
      "tooltip": "json portion of search filter values or leave empty",
      "type_id": 6,
      "uuid": "97743290-ddbe-4936-852f-e2ac5d1ccb9d",
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
      "export_key": "actioninvocation/soar_utils_close_fields",
      "hide_notification": false,
      "id": 388,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_close_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "e.g.: {\"resolution_id\":\"Resolved\",\"resolution_summary\":\"closing\"}",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Close Fields",
      "tooltip": "Enter a JSON String of the fields required to close an Incident",
      "type_id": 6,
      "uuid": "d5865351-161e-4209-b015-f821b1e7a2f2",
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
      "export_key": "actioninvocation/soar_utils_extract_file_path",
      "hide_notification": false,
      "id": 392,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_extract_file_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "path/to/file.txt",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Extract File Path",
      "tooltip": "Enter file location within zip archive",
      "type_id": 6,
      "uuid": "1afa8c6e-20a4-4104-b979-be49c89dff23",
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
      "export_key": "actioninvocation/soar_utils_zip_password",
      "hide_notification": false,
      "id": 393,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_zip_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Zip Password",
      "tooltip": "",
      "type_id": 6,
      "uuid": "35eb4622-74b2-4502-88eb-2858bcbe6cf7",
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
      "export_key": "actioninvocation/soar_utils_create_fields",
      "hide_notification": false,
      "id": 389,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "soar_utils_create_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"name\": \"sample\", \"description\": \"sample incident\", \"discovered_date\": 1621110044000}",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SOAR Utils Create Fields",
      "tooltip": "json format used by incident API call",
      "type_id": 6,
      "uuid": "4c87e9f9-281f-483f-a5c3-03458440bbf1",
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
      "created_date": 1663014620796,
      "description": {
        "content": "Calculate hashes for a file artifact. Returns `md5`, `sha1`, `sha256` and other hashes of the file content.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities Artifact Hash",
      "export_key": "soar_utils_artifact_hash",
      "id": 48,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663168426146,
      "name": "soar_utils_artifact_hash",
      "tags": [],
      "uuid": "357842c2-e4bc-4e80-b510-f0ed4675a6d5",
      "version": 3,
      "view_items": [
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
          "name": "Example: SOAR Utilities Artifact Hash",
          "object_type": "artifact",
          "programmatic_name": "example_soar_utilities_artifact_hash",
          "tags": [],
          "uuid": null,
          "workflow_id": 78
        }
      ]
    },
    {
      "created_date": 1663014698399,
      "description": {
        "content": "Calculate hashes for a file attachment. Returns `md5`, `sha1`, `sha256` and other hashes of the file content. Those hashes can then be used as artifacts or in other parts of your workflows.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Attachment Hash",
      "export_key": "soar_utils_attachment_hash",
      "id": 49,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663168435893,
      "name": "soar_utils_attachment_hash",
      "tags": [],
      "uuid": "897779c3-b7bf-4a2b-b3f5-fa43058bad16",
      "version": 3,
      "view_items": [
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
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
          "name": "Example: SOAR Utilities Attachment Hash",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_attachment_hash",
          "tags": [],
          "uuid": null,
          "workflow_id": 79
        }
      ]
    },
    {
      "created_date": 1663015069628,
      "description": {
        "content": "Reads a file attachment in the incident, and produces a base64-encoded string with the file attachment content. This content can then be used in combination with other workflow functions to create an artifact, a new file attachment, or to analyze the contents using various tools.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Attachment to Base64",
      "export_key": "soar_utils_attachment_to_base64",
      "id": 50,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663168471374,
      "name": "soar_utils_attachment_to_base64",
      "tags": [],
      "uuid": "71a8e169-ea42-4e1d-be8f-d0dbcd702908",
      "version": 3,
      "view_items": [
        {
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
          "name": "Example: SOAR Utilities (Artifact) Attachment to Base64",
          "object_type": "artifact",
          "programmatic_name": "example_soar_utilities_artifact_attachment_to_base64",
          "tags": [],
          "uuid": null,
          "workflow_id": 91
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Attachment to Base64",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_attachment_to_base64",
          "tags": [],
          "uuid": null,
          "workflow_id": 80
        }
      ]
    },
    {
      "created_date": 1663015129764,
      "description": {
        "content": "Extracts a file from a ZIP file attachment, producing a base64 string.\n\nThat string can then be used as input to subsequent functions that might write it as a file attachment, as a malware sample artifact, or in other ways.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Attachment Zip Extract",
      "export_key": "soar_utils_attachment_zip_extract",
      "id": 51,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181246565,
      "name": "soar_utils_attachment_zip_extract",
      "tags": [],
      "uuid": "023044a4-f71f-4768-87f3-aad822d53723",
      "version": 4,
      "view_items": [
        {
          "content": "09debd01-5de2-462b-9e97-2e4ec5db0098",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cba48e26-0b59-4984-b2ce-3be1bda58d31",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
          "name": "Example: SOAR Utilities Zip Extract",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_extract",
          "tags": [],
          "uuid": null,
          "workflow_id": 81
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Zip Extract to Artifact",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_extract_to_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 93
        }
      ]
    },
    {
      "created_date": 1663015175499,
      "description": {
        "content": "Reads a ZIP file and produces a list of the file paths, and a list with detailed information about each file.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Attachment Zip List",
      "export_key": "soar_utils_attachment_zip_list",
      "id": 52,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663168460317,
      "name": "soar_utils_attachment_zip_list",
      "tags": [],
      "uuid": "a111dc9b-9ea4-42a2-8590-23ca399d8387",
      "version": 3,
      "view_items": [
        {
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
          "name": "Example: SOAR Utilities Zip List",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_list",
          "tags": [],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "created_date": 1663015244117,
      "description": {
        "content": "Creates a new artifact from a Base64 string. You can  specify the artifact type and description.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Base64 to Artifact",
      "export_key": "soar_utils_base64_to_artifact",
      "id": 53,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181561759,
      "name": "soar_utils_base64_to_artifact",
      "tags": [],
      "uuid": "2710d4db-7c32-42cc-a264-1f0e66a64826",
      "version": 4,
      "view_items": [
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b5563a4f-73e5-4e11-b3eb-aa1be3c72300",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "42b4175a-96df-4e92-8be7-65ecbf500127",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "462e6c47-7587-4cc6-b2c6-f05ef09a8797",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a2811c56-b510-40fd-bbbd-afafe0ddf6f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d7a8353-5d6b-4890-99d1-7bfc9fd64287",
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
          "name": "Example: SOAR Utilities Zip Extract to Artifact",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_extract_to_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 93
        }
      ]
    },
    {
      "created_date": 1663015386425,
      "description": {
        "content": "Creates a new attachment from a base64 string.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Base64 to Attachment",
      "export_key": "soar_utils_base64_to_attachment",
      "id": 54,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181621824,
      "name": "soar_utils_base64_to_attachment",
      "tags": [],
      "uuid": "337c083e-2c30-4907-8000-0b9a4496154b",
      "version": 4,
      "view_items": [
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "42b4175a-96df-4e92-8be7-65ecbf500127",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d7a8353-5d6b-4890-99d1-7bfc9fd64287",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "462e6c47-7587-4cc6-b2c6-f05ef09a8797",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
          "name": "Example: SOAR Utilities Zip Extract",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_extract",
          "tags": [],
          "uuid": null,
          "workflow_id": 81
        }
      ]
    },
    {
      "created_date": 1663015724910,
      "description": {
        "content": "Function that takes an incident_id and a JSON String of field_name and field_value pairs to close an Incident.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Close Incident",
      "export_key": "soar_utils_close_incident",
      "id": 60,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181697711,
      "name": "soar_utils_close_incident",
      "tags": [],
      "uuid": "836a3505-3306-4eda-9703-6297fad907da",
      "version": 3,
      "view_items": [
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "662e4f24-b241-48f6-959c-993d76feb214",
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
          "name": "Example: SOAR Utilities Close Incident",
          "object_type": "incident",
          "programmatic_name": "example_soar_utilities_close_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 83
        }
      ]
    },
    {
      "created_date": 1663015657548,
      "description": {
        "content": "Create an incident from a function",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Create Incident",
      "export_key": "soar_utils_create_incident",
      "id": 59,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181785844,
      "name": "soar_utils_create_incident",
      "tags": [],
      "uuid": "c6f170f3-61f6-4a46-a397-f2b3ae095be4",
      "version": 4,
      "view_items": [
        {
          "content": "25c64fed-b7d1-4a7a-b661-f865dff641e0",
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
          "name": "Example: SOAR Utilities Create Incident",
          "object_type": "incident",
          "programmatic_name": "example_soar_utilities_create_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 84
        }
      ]
    },
    {
      "created_date": 1663015767485,
      "description": {
        "content": "Retrieves contact information of the owner and members of an incident or task.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Get Contact Info",
      "export_key": "soar_utils_get_contact_info",
      "id": 61,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663169946783,
      "name": "soar_utils_get_contact_info",
      "tags": [],
      "uuid": "7edb9444-2b81-4756-8fbe-3483cdafb9eb",
      "version": 2,
      "view_items": [
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
          "name": "Example: SOAR Utilities Get Incident Contact Info",
          "object_type": "incident",
          "programmatic_name": "example_soar_utilities_get_incident_contact_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 86
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Get Task Contact Info",
          "object_type": "task",
          "programmatic_name": "example_soar_utilities_get_task_contact_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 85
        }
      ]
    },
    {
      "created_date": 1663016122610,
      "description": {
        "content": "Search for incidents based on filter criteria. Sorting field are optional",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: Search Incidents",
      "export_key": "soar_utils_search_incidents",
      "id": 63,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663181955390,
      "name": "soar_utils_search_incidents",
      "tags": [],
      "uuid": "949d5b2c-0e50-4b89-9318-c509850c8b68",
      "version": 3,
      "view_items": [
        {
          "content": "6d6ae16e-8fbe-42a1-b4c1-5e34ee1b0e7c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "98a5216f-6bf6-46e1-94ea-344b9d36cc84",
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
          "name": "Example: SOAR Utilities Search Incidents",
          "object_type": "incident",
          "programmatic_name": "example_soar_utilities_search_incidents",
          "tags": [],
          "uuid": null,
          "workflow_id": 89
        }
      ]
    },
    {
      "created_date": 1663016042022,
      "description": {
        "content": "This function searches the SOAR platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, or incidents currently assigned to a given user, or a very wide range of other search conditions.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: SOAR Search",
      "export_key": "soar_utils_soar_search",
      "id": 62,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663168651316,
      "name": "soar_utils_soar_search",
      "tags": [],
      "uuid": "125b3261-250e-4b34-aad8-eb4b49fc262c",
      "version": 3,
      "view_items": [
        {
          "content": "357b3f18-2df2-4b39-8128-af57eb91821a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4e3867ee-0cf5-4aa6-9867-079dba934dc0",
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
          "name": "Example: SOAR Utilities SOAR Search",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_soar_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 88
        }
      ]
    },
    {
      "created_date": 1663016250470,
      "description": {
        "content": "Creates a new file (.txt) attachment in the incident or task from a string that your workflow provides as input.",
        "format": "text"
      },
      "destination_handle": "fn_soar_utils",
      "display_name": "SOAR Utilities: String to Attachment",
      "export_key": "soar_utils_string_to_attachment",
      "id": 64,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1663182127064,
      "name": "soar_utils_string_to_attachment",
      "tags": [],
      "uuid": "59d7c5d2-b9c0-4dff-a3b4-c8341913287b",
      "version": 3,
      "view_items": [
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03955f53-5940-49ff-a9df-0b607099657b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "019b19a5-b165-4258-baa0-6c57cdabb3f5",
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
          "name": "Example: SOAR Utilities String to Attachment",
          "object_type": "artifact",
          "programmatic_name": "example_soar_utilities_string_to_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 129,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1664479426058,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1664479426058,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_soar_utils",
      "name": "fn_soar_utils",
      "programmatic_name": "fn_soar_utils",
      "tags": [],
      "users": [],
      "uuid": "76ab2f5a-35fb-477d-9142-e00ce86d13f6"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_artifact_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_artifact_hash\" isExecutable=\"true\" name=\"Example: SOAR Utilities Artifact Hash\"\u003e\u003cdocumentation\u003eAn example that calculates hash from an artifact attachment\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dmwndm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1wyx46y\"\u003e\u003cincoming\u003eSequenceFlow_0wxnbxr\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1qsvrwc\" name=\"SOAR Utilities Artifact Hash\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"357842c2-e4bc-4e80-b510-f0ed4675a6d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The result contains at least these three hashes\\nif results.get(\u0027sha256\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-256 Hash\\\", results.get(\u0027sha256\u0027), u\\\"SHA-256 hash of \u0027{}\u0027\\\".format(artifact.value))\\n\\nif results.get(\u0027sha1\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-1 Hash\\\", results.get(\u0027sha1\u0027), u\\\"SHA-1 hash of \u0027{}\u0027\\\".format(artifact.value))\\n\\nif results.get(\u0027md5\u0027, None):\\n  incident.addArtifact(\\\"Malware MD5 Hash\\\", results.get(\u0027md5\u0027), u\\\"MD5 hash of \u0027{}\u0027\\\".format(artifact.value))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dmwndm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wxnbxr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dmwndm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qsvrwc\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0wxnbxr\" sourceRef=\"ServiceTask_1qsvrwc\" targetRef=\"EndEvent_1wyx46y\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wyx46y\" id=\"EndEvent_1wyx46y_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"528\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"501\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qsvrwc\" id=\"ServiceTask_1qsvrwc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"313\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dmwndm\" id=\"SequenceFlow_1dmwndm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"313\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"255.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wxnbxr\" id=\"SequenceFlow_0wxnbxr_di\"\u003e\u003comgdi:waypoint x=\"413\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"528\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"470.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example that calculates hash from an artifact attachment",
      "export_key": "example_soar_utilities_artifact_hash",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663161980965,
      "name": "Example: SOAR Utilities Artifact Hash",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_artifact_hash",
      "tags": [],
      "uuid": "e2f3e5e7-15e5-4580-8fe5-b0e56e4bb799",
      "workflow_id": 78
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_close_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_close_incident\" isExecutable=\"true\" name=\"Example: SOAR Utilities Close Incident\"\u003e\u003cdocumentation\u003eAn example workflow which takes an incident_id and optional close_fields in order to close an Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0wyjqvg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_16mtae1\"\u003e\u003cincoming\u003eSequenceFlow_1x7e4gy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wyjqvg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xmnymz\"/\u003e\u003cserviceTask id=\"ServiceTask_0xmnymz\" name=\"SOAR Utilities: Close Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"836a3505-3306-4eda-9703-6297fad907da\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = \\\"Result from Example: Close Incident on Incident {0}: \u0026lt;strong\u0026gt;{1}\u0026lt;/strong\u0026gt;\\\".format(results.inputs[\u0027incident_id\u0027], \\\\\\n\\\"success\\\" if results.success else \\\"failure.\u0026lt;br\u0026gt;Reason: {}\\\".format(results.reason))\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\niu_close_fields = rule.properties.soar_utils_close_fields.content\\ninputs.soar_utils_close_fields = u\\\"{}\\\".format(iu_close_fields)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wyjqvg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1x7e4gy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x7e4gy\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"EndEvent_16mtae1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02c13t7\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\nincident_id, close_fields]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17ut8cn\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"TextAnnotation_02c13t7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16mj7cm\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nCloses the Incident should reflect the action after the function runs. A Note is created with the function results.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_01rq8aj\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"TextAnnotation_16mj7cm\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16mtae1\" id=\"EndEvent_16mtae1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"599\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"617\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wyjqvg\" id=\"SequenceFlow_0wyjqvg_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"271\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xmnymz\" id=\"ServiceTask_0xmnymz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"344\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x7e4gy\" id=\"SequenceFlow_1x7e4gy_di\"\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"599\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"521.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02c13t7\" id=\"TextAnnotation_02c13t7_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"103\" x=\"199\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17ut8cn\" id=\"Association_17ut8cn_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16mj7cm\" id=\"TextAnnotation_16mj7cm_di\"\u003e\u003comgdc:Bounds height=\"89\" width=\"171\" x=\"506\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_01rq8aj\" id=\"Association_01rq8aj_di\"\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"521\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example workflow which takes an incident_id and optional close_fields in order to close an Incident.",
      "export_key": "example_soar_utilities_close_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663183798907,
      "name": "Example: SOAR Utilities Close Incident",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_close_incident",
      "tags": [],
      "uuid": "8a2320a9-0dba-4de1-8702-b01ad29dee73",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_attachment_to_base64\" isExecutable=\"true\" name=\"Example: SOAR Utilities Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting a file attachment to a Base64 encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ci0etf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0w7dz2z\"\u003e\u003cincoming\u003eSequenceFlow_0g2zmh9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ci0etf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_039vgvd\"/\u003e\u003cserviceTask id=\"ServiceTask_039vgvd\" name=\"SOAR Utilities: Attachment to Bas...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"71a8e169-ea42-4e1d-be8f-d0dbcd702908\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = str(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\")[1:20])\\n    \\n  incident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ci0etf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0g2zmh9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0g2zmh9\" sourceRef=\"ServiceTask_039vgvd\" targetRef=\"EndEvent_0w7dz2z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18w5qwi\"\u003e\u003ctext\u003eConvert a file attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1npiyrk\" sourceRef=\"ServiceTask_039vgvd\" targetRef=\"TextAnnotation_18w5qwi\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0w7dz2z\" id=\"EndEvent_0w7dz2z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"460\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"478\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ci0etf\" id=\"SequenceFlow_0ci0etf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_039vgvd\" id=\"ServiceTask_039vgvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0g2zmh9\" id=\"SequenceFlow_0g2zmh9_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"460\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18w5qwi\" id=\"TextAnnotation_18w5qwi_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"105\" x=\"405\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1npiyrk\" id=\"Association_1npiyrk_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example converting a file attachment to a Base64 encoded string",
      "export_key": "example_soar_utilities_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663182494007,
      "name": "Example: SOAR Utilities Attachment to Base64",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_attachment_to_base64",
      "tags": [],
      "uuid": "77797d3f-0bcb-43fc-8c13-b8d0b7815e21",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_soar_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_soar_search\" isExecutable=\"true\" name=\"Example: SOAR Utilities SOAR Search\"\u003e\u003cdocumentation\u003eAn example of searching SOAR\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0fcgpbb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_057b85i\"\u003e\u003cincoming\u003eSequenceFlow_1h1rfil\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1afc98z\" name=\"SOAR Utilities: SOAR Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"125b3261-250e-4b34-aad8-eb4b49fc262c\"\u003e{\"inputs\":{\"357b3f18-2df2-4b39-8128-af57eb91821a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n  \\\"types\\\": [\\\"attachment\\\"],\\n  \\\"filters\\\": {\\n    \\\"incident\\\": [{\\n        \\\"conditions\\\": [{\\\"field_name\\\": \\\"plan_status\\\", \\\"method\\\": \\\"in\\\", \\\"value\\\": [\\\"A\\\"]}]\\n      }]\\n  }\\n}\"}}}},\"post_processing_script\":\"# Search results include \\\"results\\\", which is a list of the search hits.\\n# There might be lots of results!\\n\\n# In this example we add a note with information about each result.\\nresult_info = []\\nfor result in results.results:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{}\\\"\u0026gt;{}\u0026lt;/a\u0026gt;\u0027.format(result[\u0027result\u0027][\u0027inc_id\u0027], result[\u0027result\u0027][\u0027inc_name\u0027])\\n  result_info.append(u\\\"\u0026lt;p\u0026gt;{} - {}\u0026lt;/p\u0026gt;\\\".format(link, result[\u0027obj_name\u0027]))\\n  \\nif len(result_info)==0:\\n  html = \\\"\u0026lt;div\u0026gt;No results\u0026lt;/div\u0026gt;\\\"\\nelse:\\n  html = u\\\"\u0026lt;div\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(\\\"\\\".join(result_info))\\n\\nincident.addNote(helper.createRichText(html))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Search for other occurrences of the same file attachment in Resilient.\\n\\n# The search template determines the type(s) of object to search, and the filter conditions.\\n# This can be used to search within a specific incident field, or to search only incidents that meet other criteria.\\n# Refer to SearchExInputDTO in the REST API documentation for additional details of this data structure.\\n\\n# The search query can be a simple string.\\ninputs.soar_search_query = attachment.name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fcgpbb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1h1rfil\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fcgpbb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1afc98z\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1h1rfil\" sourceRef=\"ServiceTask_1afc98z\" targetRef=\"EndEvent_057b85i\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_057b85i\" id=\"EndEvent_057b85i_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"542\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"560\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1afc98z\" id=\"ServiceTask_1afc98z_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"328\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fcgpbb\" id=\"SequenceFlow_0fcgpbb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"263\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1h1rfil\" id=\"SequenceFlow_1h1rfil_di\"\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"542\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"485\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example of searching SOAR",
      "export_key": "example_soar_utilities_soar_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663182955761,
      "name": "Example: SOAR Utilities SOAR Search",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_soar_search",
      "tags": [],
      "uuid": "dc3082ae-d200-4587-9b97-2f4494189913",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_search_incidents",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_search_incidents\" isExecutable=\"true\" name=\"Example: SOAR Utilities Search Incidents\"\u003e\u003cdocumentation\u003eSearch incidents based on filtering fields. Sort field are optional\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1l7fhuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_09f9rll\"\u003e\u003cincoming\u003eSequenceFlow_0blh56i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1l7fhuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0iqh4z0\"/\u003e\u003cserviceTask id=\"ServiceTask_0iqh4z0\" name=\"SOAR Utilities: Search Incidents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"949d5b2c-0e50-4b89-9318-c509850c8b68\"\u003e{\"inputs\":{},\"post_processing_script\":\"msgs = [u\\\"Filter conditions: {}\\\".format(results.inputs[\u0027soar_utils_filter_conditions\u0027])]\\nif results.success:\\n  for inc in results.content[\u0027data\u0027]:\\n    msgs.append(u\\\"id: \u0026lt;a target=\u0027blank\u0027 href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt; Name: {1}\\\".format(inc[\u0027id\u0027], inc[\u0027name\u0027]))\\n  incident.addNote(helper.createRichText(u\\\"Found {} incidents\u0026lt;br\u0026gt;{}\\\".format(results.content[\u0027recordsTotal\u0027], \u0027\u0026lt;br\u0026gt;\u0027.join(msgs))))\\n\\nelse:\\n  incident.addNote(u\\\"Search error found: {}\\\".format(results.reason))\\n  \",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_filter_conditions = rule.properties.soar_utils_search_fields.content\\ninputs.soar_utils_sort_fields = rule.properties.soar_utils_sort_fields.content\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1l7fhuk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0blh56i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0blh56i\" sourceRef=\"ServiceTask_0iqh4z0\" targetRef=\"EndEvent_09f9rll\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09f9rll\" id=\"EndEvent_09f9rll_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"535\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"553\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l7fhuk\" id=\"SequenceFlow_1l7fhuk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"301\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"249.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0iqh4z0\" id=\"ServiceTask_0iqh4z0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"301\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0blh56i\" id=\"SequenceFlow_0blh56i_di\"\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"468\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Search incidents based on filtering fields. Sort field are optional",
      "export_key": "example_soar_utilities_search_incidents",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663641848691,
      "name": "Example: SOAR Utilities Search Incidents",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_search_incidents",
      "tags": [],
      "uuid": "c65e3d60-0f50-4383-a689-33784d4f8c31",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_soar_utilities_zip_extract_to_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_extract_to_artifact\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip Extract to Artifact\"\u003e\u003cdocumentation\u003eAn example showing how to extract a file from a ZIP file attachment and create a new artifact.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rk2qdo\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1ssbfkh\"\u003e\u003cincoming\u003eSequenceFlow_14ghbpb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1rk2qdo\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1wux4mf\"/\u003e\u003cserviceTask id=\"ServiceTask_1wux4mf\" name=\"SOAR Utilities: Attachment Zip Ex...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"023044a4-f71f-4768-87f3-aad822d53723\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# The path within the zip that we want to extract\\ninputs.soar_utils_file_path = rule.properties.soar_utils_extract_file_path\\n\\n# If the zipfile is password protected, specify here\\n# inputs.zipfile_password = \\nif rule.properties.soar_utils_zip_password:\\n  inputs.soar_utils_zipfile_password = rule.properties.soar_utils_zip_password\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"extracted_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rk2qdo\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qfknru\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qfknru\" sourceRef=\"ServiceTask_1wux4mf\" targetRef=\"ServiceTask_0f92p9r\"/\u003e\u003cserviceTask id=\"ServiceTask_0f92p9r\" name=\"SOAR Utilities: Base64 to Artifac...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2710d4db-7c32-42cc-a264-1f0e66a64826\"\u003e{\"inputs\":{\"a2811c56-b510-40fd-bbbd-afafe0ddf6f0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"beb27e7a-5081-4be4-b33c-fc28095fddb2\"}}},\"pre_processing_script\":\"inputs.soar_utils_base64content = workflow.properties.extracted_file.content\\nfile_name = rule.properties.soar_utils_extract_file_path.split(\u0027/\u0027)[-1]\\n\\ninputs.incident_id = incident.id\\ninputs.soar_utils_file_name = file_name + \\\".b64\\\"\\ninputs.soar_utils_content_type = \\\"image/jpeg\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qfknru\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14ghbpb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14ghbpb\" sourceRef=\"ServiceTask_0f92p9r\" targetRef=\"EndEvent_1ssbfkh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0z05feh\"\u003e\u003ctext\u003e\u003c![CDATA[In this example we assume that the file attachment is a Word, Excel or Powerpoint document (docx, xlsx, pptx).\u00a0 These are zipfiles, and may contain a thumbnail image (\"docProps/thumbnail.jpeg\").\n\n\nThe \"zip extract\" function produces base64-encoded contents of the extracted file.\u00a0 In the \"output\", we give that a name so it can be used downstream.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13pf015\" sourceRef=\"ServiceTask_1wux4mf\" targetRef=\"TextAnnotation_0z05feh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1dy0d5v\"\u003e\u003ctext\u003eFrom the output of the first function, create a new artifact.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_162ex5g\" sourceRef=\"ServiceTask_0f92p9r\" targetRef=\"TextAnnotation_1dy0d5v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ssbfkh\" id=\"EndEvent_1ssbfkh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"548\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"566\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rk2qdo\" id=\"SequenceFlow_1rk2qdo_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1wux4mf\" id=\"ServiceTask_1wux4mf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qfknru\" id=\"SequenceFlow_0qfknru_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"379.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0z05feh\" id=\"TextAnnotation_0z05feh_di\"\u003e\u003comgdc:Bounds height=\"179\" width=\"179\" x=\"90\" y=\"-97\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13pf015\" id=\"Association_13pf015_di\"\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"232\" xsi:type=\"omgdc:Point\" y=\"82\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f92p9r\" id=\"ServiceTask_0f92p9r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"405\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14ghbpb\" id=\"SequenceFlow_14ghbpb_di\"\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"526.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1dy0d5v\" id=\"TextAnnotation_1dy0d5v_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"100\" x=\"516\" y=\"27\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_162ex5g\" id=\"Association_162ex5g_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example showing how to extract a file from a ZIP file attachment and create a new artifact.",
      "export_key": "example_soar_utilities_zip_extract_to_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663775364470,
      "name": "Example: SOAR Utilities Zip Extract to Artifact",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_extract_to_artifact",
      "tags": [],
      "uuid": "4d981842-4587-41bd-9fcd-706b90a1b9c9",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_string_to_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_string_to_attachment\" isExecutable=\"true\" name=\"Example: SOAR Utilities String to Attachment\"\u003e\u003cdocumentation\u003eAn example of creating an attachment from an input string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0depya1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1560ig6\"\u003e\u003cincoming\u003eSequenceFlow_1l95am2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0depya1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1n72a19\"/\u003e\u003cserviceTask id=\"ServiceTask_1n72a19\" name=\"SOAR Utilities: String to Attachm...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"59d7c5d2-b9c0-4dff-a3b4-c8341913287b\"\u003e{\"inputs\":{\"03955f53-5940-49ff-a9df-0b607099657b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"A Test Attachment Name\"}}},\"post_processing_script\":\"# result: {\u0027attachment_id\u0027: 28}\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the string to convert, the incident id and the attachment name\\ninputs.soar_utils_string_to_convert_to_attachment = artifact.value\\ninputs.incident_id = incident.id\\n#inputs.attachment_name = \\\"A Test Attachment Name\\\"\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0depya1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1l95am2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1l95am2\" sourceRef=\"ServiceTask_1n72a19\" targetRef=\"EndEvent_1560ig6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1560ig6\" id=\"EndEvent_1560ig6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"489\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"507\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0depya1\" id=\"SequenceFlow_0depya1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"239.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1n72a19\" id=\"ServiceTask_1n72a19_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"281\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l95am2\" id=\"SequenceFlow_1l95am2_di\"\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"489\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"435\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example of creating an attachment from an input string",
      "export_key": "example_soar_utilities_string_to_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663182926828,
      "name": "Example: SOAR Utilities String to Attachment",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_string_to_attachment",
      "tags": [],
      "uuid": "5a74758c-edf6-431c-8f28-57daeca0d5af",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_soar_utilities_attachment_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_attachment_hash\" isExecutable=\"true\" name=\"Example: SOAR Utilities Attachment Hash\"\u003e\u003cdocumentation\u003eAn example that calculates hash artifacts from an attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dooi7f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_04vzzkb\"\u003e\u003cincoming\u003eSequenceFlow_0rl0lje\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_01dxzwo\" name=\"SOAR Utilities: Attachment Hash\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"897779c3-b7bf-4a2b-b3f5-fa43058bad16\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dooi7f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0rl0lje\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dooi7f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01dxzwo\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0rl0lje\" sourceRef=\"ServiceTask_01dxzwo\" targetRef=\"EndEvent_04vzzkb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_08t8dqp\"\u003e\u003ctext\u003e\u003c![CDATA[Calculate hashes of a file attachment.\n\nThe results are added to the incident as new artifacts.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1bftw41\" sourceRef=\"ServiceTask_01dxzwo\" targetRef=\"TextAnnotation_08t8dqp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04vzzkb\" id=\"EndEvent_04vzzkb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"472\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"490\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01dxzwo\" id=\"ServiceTask_01dxzwo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_08t8dqp\" id=\"TextAnnotation_08t8dqp_di\"\u003e\u003comgdc:Bounds height=\"87\" width=\"122\" x=\"394\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1bftw41\" id=\"Association_1bftw41_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dooi7f\" id=\"SequenceFlow_1dooi7f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rl0lje\" id=\"SequenceFlow_0rl0lje_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"472\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"423\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example that calculates hash artifacts from an attachment.",
      "export_key": "example_soar_utilities_attachment_hash",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663017239283,
      "name": "Example: SOAR Utilities Attachment Hash",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_attachment_hash",
      "tags": [],
      "uuid": "d99cc4d1-db2d-4487-8c06-78eea1256980",
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_zip_list",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_list\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip List\"\u003e\u003cdocumentation\u003eAn example showing how to list the contents of a ZIP file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0kvfjgi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ogd9y3\"\u003e\u003cincoming\u003eSequenceFlow_0kvraz7\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0ahd0wo\" name=\"SOAR Utilities: Attachment Zip Li...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a111dc9b-9ea4-42a2-8590-23ca399d8387\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output contains two lists:\\n# - \\\"namelist\\\", which is just a list of the filenames (paths) within the zip file,\\n# - \\\"infolist\\\", which has full information for each file, including its name, size, and so on.\\n\\n# For this example, let\u0027s create two notes\\n\\n# One with a list of the namelist\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor filename in results.namelist:\\n  html = html + u\\\"{}\u0026lt;br\u0026gt;\\\".format(filename)\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\\n# Another with more detailed information\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor fileinfo in results.infolist:\\n  html = html + u\\\"{} ({} bytes, {} compressed) {}\u0026lt;br\u0026gt;\\\".format(fileinfo[\\\"filename\\\"], fileinfo[\\\"file_size\\\"], fileinfo[\\\"compress_size\\\"], fileinfo[\\\"comment\\\"])\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0kvfjgi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kvraz7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0kvfjgi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ahd0wo\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0kvraz7\" sourceRef=\"ServiceTask_0ahd0wo\" targetRef=\"EndEvent_0ogd9y3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0kqgg4l\"\u003e\u003ctext\u003eFunction reads the attachment (by id) then produces a list of its contents, in a structured data format.\u00a0 The post-processing script writes these results into a note on the incident.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1amd98w\" sourceRef=\"ServiceTask_0ahd0wo\" targetRef=\"TextAnnotation_0kqgg4l\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ogd9y3\" id=\"EndEvent_0ogd9y3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"691\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"709\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ahd0wo\" id=\"ServiceTask_0ahd0wo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kvfjgi\" id=\"SequenceFlow_0kvfjgi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"285.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kvraz7\" id=\"SequenceFlow_0kvraz7_di\"\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"691\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"582\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0kqgg4l\" id=\"TextAnnotation_0kqgg4l_di\"\u003e\u003comgdc:Bounds height=\"103\" width=\"230\" x=\"523\" y=\"1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1amd98w\" id=\"Association_1amd98w_di\"\u003e\u003comgdi:waypoint x=\"470\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"566\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example showing how to list the contents of a ZIP file attachment.",
      "export_key": "example_soar_utilities_zip_list",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663641148337,
      "name": "Example: SOAR Utilities Zip List",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_list",
      "tags": [],
      "uuid": "1a1ffaaa-3781-4f90-a44b-aa4700ca3d07",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "example_soar_utilities_artifact_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_artifact_attachment_to_base64\" isExecutable=\"true\" name=\"Example: SOAR Utilities (Artifact) Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting an Artifact of type File to a Base64 Encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_148uk59\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1up8nde\"\u003e\u003cincoming\u003eSequenceFlow_0c4ts4v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_148uk59\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0trmhbs\"/\u003e\u003cserviceTask id=\"ServiceTask_0trmhbs\" name=\"SOAR Utilities: Attachment to Bas...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"71a8e169-ea42-4e1d-be8f-d0dbcd702908\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = str(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\", \\\"\\\")[1:20] )\\n\\n  incident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: incident_id artifact_id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_148uk59\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c4ts4v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0c4ts4v\" sourceRef=\"ServiceTask_0trmhbs\" targetRef=\"EndEvent_1up8nde\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00fnkrh\"\u003e\u003ctext\u003eConvert a file attachment attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1p30sfl\" sourceRef=\"ServiceTask_0trmhbs\" targetRef=\"TextAnnotation_00fnkrh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1up8nde\" id=\"EndEvent_1up8nde_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"498\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"516\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_148uk59\" id=\"SequenceFlow_148uk59_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0trmhbs\" id=\"ServiceTask_0trmhbs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"290\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c4ts4v\" id=\"SequenceFlow_0c4ts4v_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"498\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"444\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00fnkrh\" id=\"TextAnnotation_00fnkrh_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"146\" x=\"426\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1p30sfl\" id=\"Association_1p30sfl_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "An example converting an Artifact of type File to a Base64 Encoded string",
      "export_key": "example_soar_utilities_artifact_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663177520321,
      "name": "Example: SOAR Utilities (Artifact) Attachment to Base64",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_artifact_attachment_to_base64",
      "tags": [],
      "uuid": "d1fee528-3870-4d5a-9b6e-a6b0a68d6951",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_soar_utilities_get_task_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_get_task_contact_info\" isExecutable=\"true\" name=\"Example: SOAR Utilities Get Task Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for a task in an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_01tqdx3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ra7rtl\"\u003e\u003cincoming\u003eSequenceFlow_0mvgj5u\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0qznvra\" name=\"SOAR Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7edb9444-2b81-4756-8fbe-3483cdafb9eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"owner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\ntask.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_01tqdx3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mvgj5u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_01tqdx3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qznvra\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0mvgj5u\" sourceRef=\"ServiceTask_0qznvra\" targetRef=\"EndEvent_0ra7rtl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ra7rtl\" id=\"EndEvent_0ra7rtl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"563\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"581\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qznvra\" id=\"ServiceTask_0qznvra_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"323\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01tqdx3\" id=\"SequenceFlow_01tqdx3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"260.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mvgj5u\" id=\"SequenceFlow_0mvgj5u_di\"\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"563\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"493\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get owner and member contact information for a task in an Incident",
      "export_key": "example_soar_utilities_get_task_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663082860864,
      "name": "Example: SOAR Utilities Get Task Contact Info",
      "object_type": "task",
      "programmatic_name": "example_soar_utilities_get_task_contact_info",
      "tags": [],
      "uuid": "b6f04e6b-32fa-4e2b-b3c9-5f9a88f23da2",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "example_soar_utilities_zip_extract",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_extract\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip Extract\"\u003e\u003cdocumentation\u003eAn example showing how to extract a file from a ZIP file attachment and create a new attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1auywqg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_03jmhgm\"\u003e\u003cincoming\u003eSequenceFlow_0q6icfq\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0rnx372\" name=\"SOAR Utilities: Attachment Zip Ex...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"023044a4-f71f-4768-87f3-aad822d53723\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# The path within the zip that we want to extract\\ninputs.soar_utils_file_path = rule.properties.soar_utils_extract_file_path\\n\\n# If the zipfile is password protected, specify here\\n# inputs.zipfile_password = \\nif rule.properties.soar_utils_zip_password:\\n  inputs.soar_utils_zipfile_password = rule.properties.soar_utils_zip_password\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"extracted_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1auywqg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1y4isbs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_171egfi\" name=\"SOAR Utilities: Base64 to Attachm...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"337c083e-2c30-4907-8000-0b9a4496154b\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_base64content = workflow.properties.extracted_file.content\\nfile_name = rule.properties.soar_utils_extract_file_path.split(\u0027/\u0027)[-1]\\n\\ninputs.incident_id = incident.id\\ninputs.soar_utils_file_name = file_name + \\\".b64\\\"\\ninputs.soar_utils_content_type = \\\"image/jpeg\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1y4isbs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q6icfq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1auywqg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rnx372\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1y4isbs\" sourceRef=\"ServiceTask_0rnx372\" targetRef=\"ServiceTask_171egfi\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0q6icfq\" sourceRef=\"ServiceTask_171egfi\" targetRef=\"EndEvent_03jmhgm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1by3ic1\"\u003e\u003ctext\u003e\u003c![CDATA[In this example we assume that the file attachment is a Word, Excel or Powerpoint document (docx, xlsx, pptx).\u00a0 These are zipfiles, and may contain a thumbnail image (\"docProps/thumbnail.jpeg\").\n\n\nThe \"zip extract\" function produces base64-encoded contents of the extracted file.\u00a0 In the \"output\", we give that a name so it can be used downstream.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0k3f371\" sourceRef=\"ServiceTask_0rnx372\" targetRef=\"TextAnnotation_1by3ic1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14sh9j5\"\u003e\u003ctext\u003eFrom the output of the first function, create a new file attachment.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0han8fp\" sourceRef=\"ServiceTask_171egfi\" targetRef=\"TextAnnotation_14sh9j5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03jmhgm\" id=\"EndEvent_03jmhgm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"735\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"753\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rnx372\" id=\"ServiceTask_0rnx372_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"293\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_171egfi\" id=\"ServiceTask_171egfi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"525\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1auywqg\" id=\"SequenceFlow_1auywqg_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"245.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1y4isbs\" id=\"SequenceFlow_1y4isbs_di\"\u003e\u003comgdi:waypoint x=\"393\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"459\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q6icfq\" id=\"SequenceFlow_0q6icfq_di\"\u003e\u003comgdi:waypoint x=\"625\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"735\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"680\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1by3ic1\" id=\"TextAnnotation_1by3ic1_di\"\u003e\u003comgdc:Bounds height=\"145\" width=\"257\" x=\"85\" y=\"-28\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0k3f371\" id=\"Association_0k3f371_di\"\u003e\u003comgdi:waypoint x=\"311\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14sh9j5\" id=\"TextAnnotation_14sh9j5_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"112\" x=\"681\" y=\"22\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0han8fp\" id=\"Association_0han8fp_di\"\u003e\u003comgdi:waypoint x=\"617\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "An example showing how to extract a file from a ZIP file attachment and create a new attachment.",
      "export_key": "example_soar_utilities_zip_extract",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663774962373,
      "name": "Example: SOAR Utilities Zip Extract",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_extract",
      "tags": [],
      "uuid": "2ddbfca8-90f8-4c92-ab31-1e65fd8ad846",
      "workflow_id": 81
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_create_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_create_incident\" isExecutable=\"true\" name=\"Example: SOAR Utilities Create Incident\"\u003e\u003cdocumentation\u003eCreate an incident based on json field data. Artifacts and notes can be created at the same time.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0el966k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0qsfyx6\"\u003e\u003cincoming\u003eSequenceFlow_1da5p43\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0el966k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gshre3\"/\u003e\u003cserviceTask id=\"ServiceTask_1gshre3\" name=\"SOAR Utilities: Create Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c6f170f3-61f6-4a46-a397-f2b3ae095be4\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{0}\\\"\u0026gt;{0}: {1}\u0026lt;/a\u0026gt;\u0027.format(results.content[\u0027id\u0027], results.content[\u0027name\u0027])\\n  incident.addNote(helper.createRichText(u\\\"Incident successfully created: {}\\\".format(link)))\\nelse:\\n  incident.addNote(u\\\"Incident creation failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_create_fields = rule.properties.soar_utils_create_fields.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0el966k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1da5p43\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1da5p43\" sourceRef=\"ServiceTask_1gshre3\" targetRef=\"EndEvent_0qsfyx6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0giavvu\"\u003e\u003ctext\u003eA note with the results is added\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h9k9bt\" sourceRef=\"ServiceTask_1gshre3\" targetRef=\"TextAnnotation_0giavvu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0qsfyx6\" id=\"EndEvent_0qsfyx6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"557\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"530\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0el966k\" id=\"SequenceFlow_0el966k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"330\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"219\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gshre3\" id=\"ServiceTask_1gshre3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"330\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1da5p43\" id=\"SequenceFlow_1da5p43_di\"\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"448.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0giavvu\" id=\"TextAnnotation_0giavvu_di\"\u003e\u003comgdc:Bounds height=\"38\" width=\"101\" x=\"454\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h9k9bt\" id=\"Association_0h9k9bt_di\"\u003e\u003comgdi:waypoint x=\"418\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"95\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Create an incident based on json field data. Artifacts and notes can be created at the same time.",
      "export_key": "example_soar_utilities_create_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663182837629,
      "name": "Example: SOAR Utilities Create Incident",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_create_incident",
      "tags": [],
      "uuid": "3afcf022-6310-4dd1-a650-988eb3eb8880",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_soar_utilities_get_incident_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_get_incident_contact_info\" isExecutable=\"true\" name=\"Example: SOAR Utilities Get Incident Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0z9atne\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_05qhqog\"\u003e\u003cincoming\u003eSequenceFlow_0kwuavs\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0z77voh\" name=\"SOAR Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7edb9444-2b81-4756-8fbe-3483cdafb9eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"# {\u0027owner\u0027: {\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}, \u0027members\u0027: []}\\n# {\u0027owner\u0027: None, \u0027members\u0027: [{\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}]}\\nowner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\nincident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0z9atne\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kwuavs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0z9atne\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0z77voh\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0kwuavs\" sourceRef=\"ServiceTask_0z77voh\" targetRef=\"EndEvent_05qhqog\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bm4wjs\"\u003e\u003ctext\u003eResults returned in an incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0y01zho\" sourceRef=\"ServiceTask_0z77voh\" targetRef=\"TextAnnotation_0bm4wjs\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05qhqog\" id=\"EndEvent_05qhqog_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"505\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0z77voh\" id=\"ServiceTask_0z77voh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"300\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z9atne\" id=\"SequenceFlow_0z9atne_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"300\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"249\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kwuavs\" id=\"SequenceFlow_0kwuavs_di\"\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bm4wjs\" id=\"TextAnnotation_0bm4wjs_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"107\" x=\"429\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0y01zho\" id=\"Association_0y01zho_di\"\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get owner and member contact information for an Incident",
      "export_key": "example_soar_utilities_get_incident_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663082964319,
      "name": "Example: SOAR Utilities Get Incident Contact Info",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_get_incident_contact_info",
      "tags": [],
      "uuid": "da40c7a7-dcb8-40d5-a6dd-954600796854",
      "workflow_id": 86
    }
  ],
  "workspaces": []
}
