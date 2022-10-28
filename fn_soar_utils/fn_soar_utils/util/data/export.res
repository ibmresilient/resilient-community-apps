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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
  "export_date": 1665000746061,
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
          "tag_handle": "fn_soar_utils",
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
          "tag_handle": "fn_soar_utils",
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
        },
        {
          "tag_handle": "fn_soar_utils",
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
          "tag_handle": "fn_soar_utils",
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
      "last_modified_time": 1664750815079,
      "name": "soar_utils_artifact_hash",
      "output_json_example": "{\"filename\": \"fn_timer.log\", \"content_type\": \"application/octet-stream\", \"size\": 14094, \"created\": 1663093337313, \"blake2b\": \"26c1297f39175f4b401ebf74e3e5ce49775ba7720f5cce375cabff28cd3b18511a8d9463c1c9f8c85a0cd6d9133b1e5d6486d1054946b2379e4dcafa1d91cc27\", \"md5\": \"d6815ac62179797d87d21b942ed7c96f\", \"shake_128\": \"8d64165fb1599e845faefe04040f8151589fec8fb13e09aeb6ea68e5f5b98ef5032e5233a6463785f1f613e8ba5b0fdb385754845c5f40b6d8f620496366d72709daca6b711ed9646f971e2ad76f78e83077bc8525e8b37610bc6584b96e89439672b093594b541a4c1a9b54bc9b5594d61aaaa3eee7435890cfa9035b820495\", \"shake_256\": \"356ba4b7bc9fda6ad64ed936f0d47e7b19022adfcfc236753182f13a82613c87e3b2dc206fb523952d1841837f785dd8bf137d74919253249327dec36a7b4f180a61cd29e2f2db53febac95deee3300519d4dd28ba08af297f29a5862653a314324e78e41fe2696ab25fb42aa80c63556eeb119d961157c0fb573d93953b7adc485e4cee5c3ecc5561acc5d45c2b1ccb5575a28763a877859d11c9f520d311a750314aebbd71e2459caa4d35a799aeee9f285934086f302d94f368ace46def566f6aac8884b5701914ff26f304b072931bbaeb697aa9d11a71d21767924c96ffe5793848aee50cf40d02dfe4f70f6d329cb83d380397f5f4081c1dcb39034458\", \"sha256\": \"561976be4b6e992478c13ea230e0f6a4e708e3b7befc61642dcd281bcacec975\", \"sha512\": \"f6f5835d41d48d27a1ed7101ae0e21dc3548aab452f5c5d9a634f68c09b50b3ec062f086296628f8d226566637887e5c7be815c83abe2dc8b2746e324b70ac5c\", \"sha3_224\": \"18f24955d1f242a59f550f52c7bc09d08e423552774674058511cefc\", \"sha384\": \"83a8bc932fc27c3e8f7c064a809c23aa8d737d2e1844b3c512e912fef14678f43bb0c994250a1d628b06b88075f2b441\", \"blake2s\": \"9ee3fa9f9907f3c6321a7323aaf0bee5a4aa5eb59652911d3cde20567d90f75e\", \"sha3_256\": \"756508e728338b4931e199674e65ff9ba5daa25914f75cca8d424efd7ab89f0d\", \"sha3_384\": \"6324ff6f2bfc710a0dfcb59f0c2f991e0d68f81976b1e85777bb94827ec031a22720dd4b66b12e2576bde798b74a0645\", \"sha224\": \"d859465ac0ccfadba558b6a4856f9517f3ab15ac3b338a96a815af7e\", \"sha1\": \"44b7ed9daadb3ac89ead8977d04a0537fa3125ae\", \"sha3_512\": \"d3e927678ab6e0f6f00eba36f137565ba945d311f694a40fd8d1998296d41391e7ff9b07269499346ad65bc8f9f27d79b46680b1dc5656ad9e213491c2e1523a\"}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"size\": {\"type\": \"integer\"}, \"created\": {\"type\": \"integer\"}, \"blake2b\": {\"type\": \"string\"}, \"md5\": {\"type\": \"string\"}, \"shake_128\": {\"type\": \"string\"}, \"shake_256\": {\"type\": \"string\"}, \"sha256\": {\"type\": \"string\"}, \"sha512\": {\"type\": \"string\"}, \"sha3_224\": {\"type\": \"string\"}, \"sha384\": {\"type\": \"string\"}, \"blake2s\": {\"type\": \"string\"}, \"sha3_256\": {\"type\": \"string\"}, \"sha3_384\": {\"type\": \"string\"}, \"sha224\": {\"type\": \"string\"}, \"sha1\": {\"type\": \"string\"}, \"sha3_512\": {\"type\": \"string\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "357842c2-e4bc-4e80-b510-f0ed4675a6d5",
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815121,
      "name": "soar_utils_attachment_hash",
      "output_json_example": "{\"filename\": \"fn_timer.log\", \"content_type\": \"application/octet-stream\", \"size\": 14094, \"created\": 1663177933110, \"md5\": \"d6815ac62179797d87d21b942ed7c96f\", \"sha3_256\": \"756508e728338b4931e199674e65ff9ba5daa25914f75cca8d424efd7ab89f0d\", \"shake_256\": \"356ba4b7bc9fda6ad64ed936f0d47e7b19022adfcfc236753182f13a82613c87e3b2dc206fb523952d1841837f785dd8bf137d74919253249327dec36a7b4f180a61cd29e2f2db53febac95deee3300519d4dd28ba08af297f29a5862653a314324e78e41fe2696ab25fb42aa80c63556eeb119d961157c0fb573d93953b7adc485e4cee5c3ecc5561acc5d45c2b1ccb5575a28763a877859d11c9f520d311a750314aebbd71e2459caa4d35a799aeee9f285934086f302d94f368ace46def566f6aac8884b5701914ff26f304b072931bbaeb697aa9d11a71d21767924c96ffe5793848aee50cf40d02dfe4f70f6d329cb83d380397f5f4081c1dcb39034458\", \"sha256\": \"561976be4b6e992478c13ea230e0f6a4e708e3b7befc61642dcd281bcacec975\", \"sha512\": \"f6f5835d41d48d27a1ed7101ae0e21dc3548aab452f5c5d9a634f68c09b50b3ec062f086296628f8d226566637887e5c7be815c83abe2dc8b2746e324b70ac5c\", \"sha3_512\": \"d3e927678ab6e0f6f00eba36f137565ba945d311f694a40fd8d1998296d41391e7ff9b07269499346ad65bc8f9f27d79b46680b1dc5656ad9e213491c2e1523a\", \"sha1\": \"44b7ed9daadb3ac89ead8977d04a0537fa3125ae\", \"sha3_384\": \"6324ff6f2bfc710a0dfcb59f0c2f991e0d68f81976b1e85777bb94827ec031a22720dd4b66b12e2576bde798b74a0645\", \"shake_128\": \"8d64165fb1599e845faefe04040f8151589fec8fb13e09aeb6ea68e5f5b98ef5032e5233a6463785f1f613e8ba5b0fdb385754845c5f40b6d8f620496366d72709daca6b711ed9646f971e2ad76f78e83077bc8525e8b37610bc6584b96e89439672b093594b541a4c1a9b54bc9b5594d61aaaa3eee7435890cfa9035b820495\", \"blake2s\": \"9ee3fa9f9907f3c6321a7323aaf0bee5a4aa5eb59652911d3cde20567d90f75e\", \"sha3_224\": \"18f24955d1f242a59f550f52c7bc09d08e423552774674058511cefc\", \"sha224\": \"d859465ac0ccfadba558b6a4856f9517f3ab15ac3b338a96a815af7e\", \"sha384\": \"83a8bc932fc27c3e8f7c064a809c23aa8d737d2e1844b3c512e912fef14678f43bb0c994250a1d628b06b88075f2b441\", \"blake2b\": \"26c1297f39175f4b401ebf74e3e5ce49775ba7720f5cce375cabff28cd3b18511a8d9463c1c9f8c85a0cd6d9133b1e5d6486d1054946b2379e4dcafa1d91cc27\"}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"size\": {\"type\": \"integer\"}, \"created\": {\"type\": \"integer\"}, \"md5\": {\"type\": \"string\"}, \"sha3_256\": {\"type\": \"string\"}, \"shake_256\": {\"type\": \"string\"}, \"sha256\": {\"type\": \"string\"}, \"sha512\": {\"type\": \"string\"}, \"sha3_512\": {\"type\": \"string\"}, \"sha1\": {\"type\": \"string\"}, \"sha3_384\": {\"type\": \"string\"}, \"shake_128\": {\"type\": \"string\"}, \"blake2s\": {\"type\": \"string\"}, \"sha3_224\": {\"type\": \"string\"}, \"sha224\": {\"type\": \"string\"}, \"sha384\": {\"type\": \"string\"}, \"blake2b\": {\"type\": \"string\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "897779c3-b7bf-4a2b-b3f5-fa43058bad16",
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815162,
      "name": "soar_utils_attachment_to_base64",
      "output_json_example": "{\"filename\": \"fn_timer.log\", \"content_type\": \"application/octet-stream\", \"size\": 14094, \"created\": 1663177933110, \"content\": \"Q3VycmVudCBQb2QgU3RhdHVzOgpQb2RTdGF0dXMoY29uZGl0aW9ucz1bUG9kQ29uZGl0aW9uKGxhc3RQcm9iZVRpbWU9bnVsbCwgbGFzdFRyYW5zaXRpb25UaW1lPTIwMjItMDktMDlUMTU6NTE6MjRaLCBtZXNzYWdlPW51bGwsIHJlYXNvbj1udWxsLCBzdGF0dXM9VHJ1ZSwgdHlwZT1Jbml0aWFsaXplZCwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCBQb2RDb25kaXRpb24obGFzdFByb2JlVGltZT1udWxsLCBsYXN0VHJhbnNpdGlvblRpbWU9MjAyMi0wOS0wOVQxNTo1MTozNlosIG1lc3NhZ2U9bnVsbCwgcmVhc29uPW51bGwsIHN0YXR1cz1UcnVlLCB0eXBlPVJlYWR5LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSksIFBvZENvbmRpdGlvbihsYXN0UHJvYmVUaW1lPW51bGwsIGxhc3RUcmFuc2l0aW9uVGltZT0yMDIyLTA5LTA5VDE1OjUxOjM2WiwgbWVzc2FnZT1udWxsLCByZWFzb249bnVsbCwgc3RhdHVzPVRydWUsIHR5cGU9Q29udGFpbmVyc1JlYWR5LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSksIFBvZENvbmRpdGlvbihsYXN0UHJvYmVUaW1lPW51bGwsIGxhc3RUcmFuc2l0aW9uVGltZT0yMDIyLTA5LTA5VDE1OjUxOjI0WiwgbWVzc2FnZT1udWxsLCByZWFzb249bnVsbCwgc3RhdHVzPVRydWUsIHR5cGU9UG9kU2NoZWR1bGVkLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBjb250YWluZXJTdGF0dXNlcz1bQ29udGFpbmVyU3RhdHVzKGNvbnRhaW5lcklEPWNvbnRhaW5lcmQ6Ly9lMTVkYzJmZWEzYmViMGI5MGYxZTRiMmM5ZGJhZDlkMWExZjM3MzY5ZTMzNmU2MzA2NDU1NzE3Yjc0YWJmNmIxLCBpbWFnZT1zZWMtcmVzaWxpZW50LWRvY2tlci1sb2NhbC5hcnRpZmFjdG9yeS5zd2ctZGV2b3BzLmNvbS9pYm1yZXNpbGllbnQvZm5fdGltZXI6MS4wLjEzNTg5LCBpbWFnZUlEPXNlYy1yZXNpbGllbnQtZG9ja2VyLWxvY2FsLmFydGlmYWN0b3J5LnN3Zy1kZXZvcHMuY29tL2libXJlc2lsaWVudC9mbl90aW1lckBzaGEyNTY6ZGE5ZDliOGQ0NjIwYWQ2YTNjOTUzZGU0NDc3YzExYWE0NDY1NmRhOTA0MDdkZGRkMTkyOTc5ZGU1NmY2M2FhNCwgbGFzdFN0YXRlPUNvbnRhaW5lclN0YXRlKHJ1bm5pbmc9bnVsbCwgdGVybWluYXRlZD1udWxsLCB3YWl0aW5nPW51bGwsIGFkZGl0aW9uYWxQcm9wZXJ0aWVzPXt9KSwgbmFtZT03ZDAzMDE1Ni1iOWJlLTRhMTItYmMzZS0zOTY0N2E3NmY5MDAsIHJlYWR5PXRydWUsIHJlc3RhcnRDb3VudD0wLCBzdGFydGVkPXRydWUsIHN0YXRlPUNvbnRhaW5lclN0YXRlKHJ1bm5pbmc9Q29udGFpbmVyU3RhdGVSdW5uaW5nKHN0YXJ0ZWRBdD0yMDIyLTA5LTA5VDE1OjUxOjM1WiwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCB0ZXJtaW5hdGVkPW51bGwsIHdhaXRpbmc9bnVsbCwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBlcGhlbWVyYWxDb250YWluZXJTdGF0dXNlcz1bXSwgaG9zdElQPTkuMzAuMTQxLjIxNCwgaW5pdENvbnRhaW5lclN0YXR1c2VzPVtdLCBtZXNzYWdlPW51bGwsIG5vbWluYXRlZE5vZGVOYW1lPW51bGwsIHBoYXNlPVJ1bm5pbmcsIHBvZElQPTEwLjQyLjEuMjE1LCBwb2RJUHM9W1BvZElQKGlwPTEwLjQyLjEuMjE1LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBxb3NDbGFzcz1CZXN0RWZmb3J0LCByZWFzb249bnVsbCwgc3RhcnRUaW1lPTIwMjItMDktMDlUMTU6NTE6MjRaLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSkKTG9nczoKCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpFbnZpcm9ubWVudDoKUHl0aG9uIFZlcnNpb246IDMuOS43IChkZWZhdWx0LCBTZXAgMTMgMjAyMSwgMDg6MTg6MzkpIApbR0NDIDguNS4wIDIwMjEwNTE0IChSZWQgSGF0IDguNS4wLTMpXQoKSW5zdGFsbGVkIHBhY2thZ2VzOgoKYmVhdXRpZnVsc291cDQ6IDQuMTEuMQpjYWNoZXRvb2xzOiA1LjIuMApjZXJ0aWZpOiAyMDIyLjYuMTUuMQpjZmZpOiAxLjE1LjEKY2hhcnNldC1ub3JtYWxpemVyOiAyLjEuMQpjaXJjdWl0czogMy4yLjIKY3J5cHRvZ3JhcGh5OiAzOC4wLjEKZGVjb3JhdG9yOiA1LjEuMQpEZXByZWNhdGVkOiAxLjIuMTMKZmlsZWxvY2s6IDMuOC4wCmZuLXRpbWVyOiAxLjAuMTM1ODkKaWRuYTogMy4zCmltcG9ydGxpYi1tZXRhZGF0YTogNC4xMi4wCmphcmFjby5jbGFzc2VzOiAzLjIuMgpqZWVwbmV5OiAwLjguMApKaW5qYTI6IDMuMS4yCmtleXJpbmc6IDIzLjkuMQpNYXJrdXBTYWZlOiAyLjEuMQptb3JlLWl0ZXJ0b29sczogOC4xNC4wCnBpcDogMjIuMi4yCnB5OiAxLjExLjAKcHljcGFyc2VyOiAyLjIxClB5U29ja3M6IDEuNy4xCnB5dHo6IDIwMjIuMi4xCnJlcXVlc3RzOiAyLjI4LjEKcmVxdWVzdHMtdG9vbGJlbHQ6IDAuOS4xCnJlc2lsaWVudDogNDYuMC4zNDYxCnJlc2lsaWVudC1jaXJjdWl0czogNDYuMC4zNDYxCnJlc2lsaWVudC1saWI6IDQ2LjAuMzQ2MQpyZXRyeTI6IDAuOS40ClNlY3JldFN0b3JhZ2U6IDMuMy4zCnNldHVwdG9vbHM6IDYyLjYuMApzaXg6IDEuMTYuMApzb3Vwc2lldmU6IDIuMy4yLnBvc3QxCnN0b21wZXN0OiAyLjMuMAp1cmxsaWIzOiAxLjI2LjEyCndhdGNoZG9nOiAyLjEuOQp3cmFwdDogMS4xNC4xCnppcHA6IDMuOC4xCiMjIyMjIyMjIyMjIyMjIwoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5MyBJTkZPIFthcHBdIENvbmZpZ3VyYXRpb24gZmlsZTogL2V0Yy9yZXNjaXJjdWl0cy9hcHAuY29uZmlnCjIwMjItMDktMDkgMTU6NTE6MzYsNDk0IElORk8gW2FwcF0gUmVzaWxpZW50IHNlcnZlcjogOS4zMC40NC40NQoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5NCBJTkZPIFthcHBdIFJlc2lsaWVudCBhcGkga2V5IGlkOiBhMDI4ODI4OC1hYjkxLTRlMWMtOGM5ZS1mZjcyOThhNzlhNTIKMjAyMi0wOS0wOSAxNTo1MTozNiw0OTUgSU5GTyBbYXBwXSBSZXNpbGllbnQgb3JnOiBUZXN0IE9yZ2FuaXphdGlvbgoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5NSBJTkZPIFthcHBdIExvZ2dpbmcgTGV2ZWw6IElORk8KMjAyMi0wOS0wOSAxNTo1MTozNiw0OTYgV0FSTklORyBbY28zXSBVbnZlcmlmaWVkIEhUVFBTIHJlcXVlc3RzIChjYWZpbGU9ZmFsc2UpLgoyMDIyLTA5LTA5IDE1OjUxOjM2LDU4OSBJTkZPIFtjbzNiYXNlXSBVc2luZyBvcmcgbmFtZTogVGVzdCBPcmdhbml6YXRpb24KMjAyMi0wOS0wOSAxNTo1MTozNywwMjggSU5GTyBbYXBwXSBDb21wb25lbnRzIGF1dG8tbG9hZCBkaXJlY3Rvcnk6IChub25lKQoyMDIyLTA5LTA5IDE1OjUxOjM3LDA2MiBJTkZPIFtjb21wb25lbnRfbG9hZGVyXSBMb2FkaW5nIDEgY29tcG9uZW50cwoyMDIyLTA5LTA5IDE1OjUxOjM3LDA2MyBJTkZPIFtjb21wb25lbnRfbG9hZGVyXSAnZm5fdGltZXIuY29tcG9uZW50cy5mdW5jdF9mbl90aW1lci5GdW5jdGlvbkNvbXBvbmVudCcgbG9hZGluZwoyMDIyLTA5LTA5IDE1OjUxOjM3LDIxOSBXQVJOSU5HIFthY3Rpb25zX2NvbXBvbmVudF0gVW52ZXJpZmllZCBTVE9NUCBUTFMgY2VydGlmaWNhdGUgKGNhZmlsZT1mYWxzZSkKMjAyMi0wOS0wOSAxNTo1MTozNywyMjkgSU5GTyBbc3RvbXBfY29tcG9uZW50XSBDb25uZWN0IHRvIDkuMzAuNDQuNDU6NjUwMDEKMjAyMi0wOS0wOSAxNTo1MTozNywyMzAgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdICdmbl90aW1lci5jb21wb25lbnRzLmZ1bmN0X2ZuX3RpbWVyLkZ1bmN0aW9uQ29tcG9uZW50JyBmdW5jdGlvbiAnZm5fdGltZXInIHJlZ2lzdGVyZWQgdG8gJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE1OjUxOjM3LDIzMCBJTkZPIFthcHBdIENvbXBvbmVudHMgbG9hZGVkCjIwMjItMDktMDkgMTU6NTE6MzcsMjMyIElORk8gW2FwcF0gQXBwIFN0YXJ0ZWQKMjAyMi0wOS0wOSAxNTo1MTozNywzMzUgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIFNUT01QIGF0dGVtcHRpbmcgdG8gY29ubmVjdAoyMDIyLTA5LTA5IDE1OjUxOjM3LDMzNiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENvbm5lY3QgdG8gU3RvbXAuLi4KMjAyMi0wOS0wOSAxNTo1MTozNywzMzYgSU5GTyBbY2xpZW50XSBDb25uZWN0aW5nIHRvIDkuMzAuNDQuNDU6NjUwMDEgLi4uCjIwMjItMDktMDkgMTU6NTE6MzcsMzkyIElORk8gW2NsaWVudF0gQ29ubmVjdGlvbiBlc3RhYmxpc2hlZAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NSBJTkZPIFtjbGllbnRdIENvbm5lY3RlZCB0byBzdG9tcCBicm9rZXIgW3Nlc3Npb249SUQ6dGhpc3RsZXMxLmZ5cmUuaWJtLmNvbS00NDYxMS0xNjYxNzgyNTAwODA1LTQ6ODQsIHZlcnNpb249MS4yXQoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NSBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENvbm5lY3RlZCB0byBmYWlsb3Zlcjooc3NsOi8vOS4zMC40NC40NTo2NTAwMSk/bWF4UmVjb25uZWN0QXR0ZW1wdHM9MyxzdGFydHVwTWF4UmVjb25uZWN0QXR0ZW1wdHM9MwoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENsaWVudCBIQjogMCAgU2VydmVyIEhCOiAxNTAwMAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIE5vIENsaWVudCBoZWFydGJlYXRzIHdpbGwgYmUgc2VudAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIFJlcXVlc3RlZCBoZWFydGJlYXRzIGZyb20gc2VydmVyLgoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2OCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gU1RPTVAgY29ubmVjdGVkLgoyMDIyLTA5LTA5IDE1OjUxOjM3LDU3MCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gcmVzaWxpZW50LWNpcmN1aXRzIGhhcyBzdGFydGVkIHN1Y2Nlc3NmdWxseSBhbmQgaXMgbm93IHJ1bm5pbmcuLi4KMjAyMi0wOS0wOSAxNTo1MTozNyw1NzAgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIFN1YnNjcmliZSB0byBtZXNzYWdlIGRlc3RpbmF0aW9uICdmbl90aW1lcicKMjAyMi0wOS0wOSAxNTo1MTozNyw1NzEgSU5GTyBbc3RvbXBfY29tcG9uZW50XSBTdWJzY3JpYmUgdG8gbWVzc2FnZSBkZXN0aW5hdGlvbiBhY3Rpb25zLjIwMS5mbl90aW1lcgoyMDIyLTA5LTA5IDE1OjUxOjM3LDk3NiBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gRXZlbnQ6IDxmbl90aW1lcltdIChpZD00MSwgd29ya2Zsb3c9cGxheWJvb2tfNTdmNmM1NjlfNWUxZV80ZTM4XzgwNjJfM2MzZDg2OTY1OTU3LCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE1OjQxOjMzLjg3MjAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTU6NTE6MzgsMTc5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gVmFsaWRhdGVkIGZ1bmN0aW9uIGlucHV0cwoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4MCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFN0YXJ0aW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4MCBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfdGltZTogCjIwMjItMDktMDkgMTU6NTE6MzgsMTgwIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogMTY2MjczODMwMDAwMAoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4NCBFUlJPUiBbYWN0aW9uc19jb21wb25lbnRdIFRyYWNlYmFjayAobW9zdCByZWNlbnQgY2FsbCBsYXN0KToKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9yZXNpbGllbnRfY2lyY3VpdHMvYWN0aW9uc19jb21wb25lbnQucHkiLCBsaW5lIDkwLCBpbiBfb25fdGFzawp5aWVsZCByZXN1bHQuZ2V0KCkKRmlsZSAiL3Vzci9saWI2NC9weXRob24zLjkvbXVsdGlwcm9jZXNzaW5nL3Bvb2wucHkiLCBsaW5lIDc3MSwgaW4gZ2V0CnJhaXNlIHNlbGYuX3ZhbHVlCkZpbGUgIi91c3IvbGliNjQvcHl0aG9uMy45L211bHRpcHJvY2Vzc2luZy9wb29sLnB5IiwgbGluZSAxMjUsIGluIHdvcmtlcgpyZXN1bHQgPSAoVHJ1ZSwgZnVuYygqYXJncywgKiprd2RzKSkKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9yZXNpbGllbnRfY2lyY3VpdHMvZGVjb3JhdG9ycy5weSIsIGxpbmUgMjkwLCBpbiBfaW52b2tlX2FwcF9mdW5jdGlvbgpyYWlzZSByCnJlc2lsaWVudF9jaXJjdWl0cy5hY3Rpb25fbWVzc2FnZS5GdW5jdGlvbkV4Y2VwdGlvbl86IApUcmFjZWJhY2sgKG1vc3QgcmVjZW50IGNhbGwgbGFzdCk6CkZpbGUgIi9vcHQvYXBwLXJvb3QvbGliNjQvcHl0aG9uMy45L3NpdGUtcGFja2FnZXMvZm5fdGltZXIvY29tcG9uZW50cy9mdW5jdF9mbl90aW1lci5weSIsIGxpbmUgNzQsIGluIF90aW1lcl9mdW5jdGlvbgp0b3RhbF90aW1lX2luX3NlY29uZHMgPSBnZXRfc2xlZXBfdGltZV9mcm9tX2Vwb2NoKHRpbWVyX2Vwb2NoKQpGaWxlICIvb3B0L2FwcC1yb290L2xpYjY0L3B5dGhvbjMuOS9zaXRlLXBhY2thZ2VzL2ZuX3RpbWVyL2NvbXBvbmVudHMvZnVuY3RfZm5fdGltZXIucHkiLCBsaW5lIDE2NiwgaW4gZ2V0X3NsZWVwX3RpbWVfZnJvbV9lcG9jaApyYWlzZSBWYWx1ZUVycm9yKCJUaW1lciBlbmQgZGF0ZSBpcyBpbiB0aGUgcGFzdDogezB9Ii5mb3JtYXQoZW5kX2Vwb2NoKSkKVmFsdWVFcnJvcjogVGltZXIgZW5kIGRhdGUgaXMgaW4gdGhlIHBhc3Q6IDE2NjI3MzgzMDAwMDAKCgoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4NiBFUlJPUiBbYWN0aW9uc19jb21wb25lbnRdIDx0YXNrW2Z1bmN0aW9ud29ya2VyXSAoPGZ1bmN0aW9uIGFwcF9mdW5jdGlvbi5fX2NhbGxfXy48bG9jYWxzPi5hcHBfZnVuY3Rpb25fZGVjb3JhdG9yLjxsb2NhbHM+Ll9pbnZva2VfYXBwX2Z1bmN0aW9uIGF0IDB4N2ZlYTU4MzUwZTUwPiwgPGZuX3RpbWVyW2Z1bmN0aW9ucy5mbl90aW1lcl0gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTU6NDE6MzMuODcyMDAwPiB0aW1lcl90aW1lPScnLCB0aW1lcl9lcG9jaD0xNjYyNzM4MzAwMDAwKT4gKDxjbGFzcyAncmVzaWxpZW50X2NpcmN1aXRzLmFjdGlvbl9tZXNzYWdlLkZ1bmN0aW9uRXhjZXB0aW9uXyc+KTogClRyYWNlYmFjayAobW9zdCByZWNlbnQgY2FsbCBsYXN0KToKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9mbl90aW1lci9jb21wb25lbnRzL2Z1bmN0X2ZuX3RpbWVyLnB5IiwgbGluZSA3NCwgaW4gX3RpbWVyX2Z1bmN0aW9uCnRvdGFsX3RpbWVfaW5fc2Vjb25kcyA9IGdldF9zbGVlcF90aW1lX2Zyb21fZXBvY2godGltZXJfZXBvY2gpCkZpbGUgIi9vcHQvYXBwLXJvb3QvbGliNjQvcHl0aG9uMy45L3NpdGUtcGFja2FnZXMvZm5fdGltZXIvY29tcG9uZW50cy9mdW5jdF9mbl90aW1lci5weSIsIGxpbmUgMTY2LCBpbiBnZXRfc2xlZXBfdGltZV9mcm9tX2Vwb2NoCnJhaXNlIFZhbHVlRXJyb3IoIlRpbWVyIGVuZCBkYXRlIGlzIGluIHRoZSBwYXN0OiB7MH0iLmZvcm1hdChlbmRfZXBvY2gpKQpWYWx1ZUVycm9yOiBUaW1lciBlbmQgZGF0ZSBpcyBpbiB0aGUgcGFzdDogMTY2MjczODMwMDAwMAoKMjAyMi0wOS0wOSAxNTo1MjozOSw4ODUgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIEV2ZW50OiA8Zm5fdGltZXJbXSAoaWQ9NDEsIHdvcmtmbG93PXBsYXlib29rXzU3ZjZjNTY5XzVlMWVfNGUzOF84MDYyXzNjM2Q4Njk2NTk1NywgdXNlcj1hZG1pbkBleGFtcGxlLmNvbSkgMjAyMi0wOS0wOSAxNTo1MjozOS42NTgwMDA+IENoYW5uZWw6IGZ1bmN0aW9ucy5mbl90aW1lcgoyMDIyLTA5LTA5IDE1OjUyOjQwLDA5MCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxNTo1Mjo0MCwwOTEgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxNTo1Mjo0MCwwOTEgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IAoyMDIyLTA5LTA5IDE1OjUyOjQwLDA5MiBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfZXBvY2g6IDE2NjI3Mzg5MDAwMDAKMjAyMi0wOS0wOSAxNTo1Mjo0MCwxNzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgMzRzLiAwLzEzOXMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTM6MTQsMjg0IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDM0cy4gMzQvMTM5cyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1Mzo0OCwzNjMgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgMzRzLiA2OC8xMzlzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU0OjIyLDQ1OCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzNHMuIDEwMi8xMzlzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU0OjU2LDU3OCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzcy4gMTM2LzEzOXMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTQ6NTksNjQ2IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAxMzkgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1NDo1OSw2NDkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE1OjU0OjU5LDY1MSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTU6NTc6NDEsOTk1IElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTU6NTc6NDEuNjg3MDAwPiBDaGFubmVsOiBmdW5jdGlvbnMuZm5fdGltZXIKMjAyMi0wOS0wOSAxNTo1Nzo0MiwxOTkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBWYWxpZGF0ZWQgZnVuY3Rpb24gaW5wdXRzCjIwMjItMDktMDkgMTU6NTc6NDIsMjAxIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU3RhcnRpbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTU6NTc6NDIsMjAxIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl90aW1lOiAyMHMKMjAyMi0wOS0wOSAxNTo1Nzo0MiwyMDEgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTU6NTc6NDIsMjkxIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDEwcy4gMC8yMHMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTc6NTIsMzYyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDEwcy4gMTAvMjBzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU4OjAyLDQzOSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFRvdGFsIHNsZWVwIHRpbWUgMjAgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1ODowMiw0NDIgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE1OjU4OjAyLDQ0MiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTg6MDg6MDQsODMzIElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTg6MDg6MDQuNTYyMDAwPiBDaGFubmVsOiBmdW5jdGlvbnMuZm5fdGltZXIKMjAyMi0wOS0wOSAxODowODowNSwwNDAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBWYWxpZGF0ZWQgZnVuY3Rpb24gaW5wdXRzCjIwMjItMDktMDkgMTg6MDg6MDUsMDQyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU3RhcnRpbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTg6MDg6MDUsMDQyIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl90aW1lOiA2MHMKMjAyMi0wOS0wOSAxODowODowNSwwNDQgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTg6MDg6MDUsMDQ1IFdBUk5JTkcgW2NvM10gVW52ZXJpZmllZCBIVFRQUyByZXF1ZXN0cyAoY2FmaWxlPWZhbHNlKS4KMjAyMi0wOS0wOSAxODowODowNSwxMzAgSU5GTyBbY28zYmFzZV0gVXNpbmcgb3JnIG5hbWU6IFRlc3QgT3JnYW5pemF0aW9uCjIwMjItMDktMDkgMTg6MDg6MDUsMzE1IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDMwcy4gMC82MHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDg6MzUsNDE4IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogV29ya2Zsb3cgd2FzIHRlcm1pbmF0ZWQuCjIwMjItMDktMDkgMTg6MDg6MzUsNDE5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAzMCBzZWNvbmRzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjA4OjM1LDQyMSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFJldHVybmluZyByZXN1bHRzCjIwMjItMDktMDkgMTg6MDg6MzUsNDIzIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogRmluaXNoZWQgcnVubmluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MjIgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIEV2ZW50OiA8Zm5fdGltZXJbXSAoaWQ9NDEsIHdvcmtmbG93PXRpbWVyX2luX3BhcmFsbGVsLCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE4OjA4OjM1LjE0MzAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTg6MDg6MzUsNDI1IElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz10aW1lcl9pbl9wYXJhbGxlbCwgdXNlcj1hZG1pbkBleGFtcGxlLmNvbSkgMjAyMi0wOS0wOSAxODowODozNS4xNDkwMDA+IENoYW5uZWw6IGZ1bmN0aW9ucy5mbl90aW1lcgoyMDIyLTA5LTA5IDE4OjA4OjM1LDQyOSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxODowODozNSw0MzAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MzAgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IDJtCjIwMjItMDktMDkgMTg6MDg6MzUsNDMzIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogTm9uZQoyMDIyLTA5LTA5IDE4OjA4OjM1LDQzMiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxODowODozNSw0MzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MzYgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IDNtCjIwMjItMDktMDkgMTg6MDg6MzUsNDM2IElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogTm9uZQoyMDIyLTA5LTA5IDE4OjA4OjM1LDUxNiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzMHMuIDAvMTIwcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxODowODozNSw1MjkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgNDVzLiAwLzE4MHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDk6MDUsNjMwIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogV29ya2Zsb3cgd2FzIHRlcm1pbmF0ZWQuCjIwMjItMDktMDkgMTg6MDk6MDUsNjMyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAzMCBzZWNvbmRzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjA5OjA1LDYzMyBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFJldHVybmluZyByZXN1bHRzCjIwMjItMDktMDkgMTg6MDk6MDUsNjM2IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogRmluaXNoZWQgcnVubmluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowOToyMCw2MzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBXb3JrZmxvdyB3YXMgdGVybWluYXRlZC4KMjAyMi0wOS0wOSAxODowOToyMCw2MzYgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBUb3RhbCBzbGVlcCB0aW1lIDQ1IHNlY29uZHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDk6MjAsNjM5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gUmV0dXJuaW5nIHJlc3VsdHMKMjAyMi0wOS0wOSAxODowOToyMCw2NDAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBGaW5pc2hlZCBydW5uaW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE4OjE5OjUxLDk3NCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gRXZlbnQ6IDxmbl90aW1lcltdIChpZD00MSwgd29ya2Zsb3c9cGxheWJvb2tfNTdmNmM1NjlfNWUxZV80ZTM4XzgwNjJfM2MzZDg2OTY1OTU3LCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE4OjE5OjUxLjY5NzAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTg6MTk6NTIsMTgwIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gVmFsaWRhdGVkIGZ1bmN0aW9uIGlucHV0cwoyMDIyLTA5LTA5IDE4OjE5OjUyLDE4MSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFN0YXJ0aW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE4OjE5OjUyLDE4MiBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfdGltZTogNW0KMjAyMi0wOS0wOSAxODoxOTo1MiwxODIgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTg6MTk6NTIsMTgyIFdBUk5JTkcgW2NvM10gVW52ZXJpZmllZCBIVFRQUyByZXF1ZXN0cyAoY2FmaWxlPWZhbHNlKS4KMjAyMi0wOS0wOSAxODoxOTo1MiwyODcgSU5GTyBbY28zYmFzZV0gVXNpbmcgb3JnIG5hbWU6IFRlc3QgT3JnYW5pemF0aW9uCjIwMjItMDktMDkgMTg6MTk6NTIsNDY3IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDc1cy4gMC8zMDBzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxMSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFdvcmtmbG93IHdhcyB0ZXJtaW5hdGVkLgoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxMiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFRvdGFsIHNsZWVwIHRpbWUgNzUgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxODoyMTowNyw2MTYgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxNiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXIn\"}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"size\": {\"type\": \"integer\"}, \"created\": {\"type\": \"integer\"}, \"content\": {\"type\": \"string\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "71a8e169-ea42-4e1d-be8f-d0dbcd702908",
      "version": 4,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 91
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Attachment to Base64",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_attachment_to_base64",
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815204,
      "name": "soar_utils_attachment_zip_extract",
      "output_json_example": "{\"info\": {\"filename\": \"export.res\", \"date_time\": 1661452332000, \"compress_type\": 8, \"comment\": \"\", \"create_system\": 3, \"create_version\": 20, \"extract_version\": 20, \"flag_bits\": 0, \"volume\": 0, \"internal_attr\": 0, \"external_attr\": 2175008768, \"header_offset\": 588360, \"CRC\": 1492648105, \"compress_size\": 10780, \"file_size\": 101541}, \"content\": \"eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IEFyY2hpdmUgSW5jaWRlbnQgU2xhY2sgQ2hhbm5lbCIsICJpZCI6IDM3LCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBJbmNpZGVudCBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiMTgzNTI0OGQtY2I1OC00NWM2LThiYjYtZTMwYmUyNWZlNWUzIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjdjYmJiZmRmLWYxYTAtNGUzMi05ZTVjLTYzMmExODM1ZGUxZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiYXJjaGl2ZV9zbGFja19jaGFubmVsIl19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW10sICJlbmFibGVkIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogQXJjaGl2ZSBUYXNrIFNsYWNrIENoYW5uZWwiLCAiaWQiOiAzOCwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInR5cGUiOiAxLCAidXVpZCI6ICIwY2U5OGNjZi0xOTdkLTQ1ZWQtOTU0My04YTlkNTlmMGU3NjciLCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayJdfSwgeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFt7ImV2YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC50eXBlIiwgIm1ldGhvZCI6ICJpbiIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogWyJSRkMgODIyIEVtYWlsIE1lc3NhZ2UgRmlsZSIsICJFbWFpbCBBdHRhY2htZW50IiwgIkxvZyBGaWxlIiwgIk90aGVyIEZpbGUiLCAiWDUwOSBDZXJ0aWZpY2F0ZSBGaWxlIl19XSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IEF0dGFjaG1lbnQgdG8gU2xhY2siLCAiaWQiOiAzOSwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogIjBhODU3MGJlLWM2YmEtNGYxZC04M2ExLTY3YmQ5NTY0Nzk3NSIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjNiMWE2NjI4LTVlZjAtNDk1Yy05NTVlLTEwYzNlNWY5ZjRlMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2tfX2FydGlmYWN0Il19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW3siZXZhbHVhdGlvbl9pZCI6IG51bGwsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLCAibWV0aG9kIjogIm5vdF9pbiIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogWyJSRkMgODIyIEVtYWlsIE1lc3NhZ2UgRmlsZSIsICJFbWFpbCBBdHRhY2htZW50IiwgIkxvZyBGaWxlIiwgIk90aGVyIEZpbGUiLCAiWDUwOSBDZXJ0aWZpY2F0ZSBGaWxlIl19XSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgImlkIjogNDAsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiZGZkNzNiMjItNDQzOC00NmVhLTllMDEtODg4ZWRjMDE3NGU3IiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fYXJ0aWZhY3QiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgImlkIjogNDEsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInR5cGUiOiAxLCAidXVpZCI6ICI0YmQ0NzcxMi1iYzkyLTQwNWQtOTM2Ny0zOWFmZmU1NDRiOTEiLCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAiMjRkZjNlMWMtMmMyOC00ZTdkLWFjMjgtNGZlYTBhMzg3N2EyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIzYjFhNjYyOC01ZWYwLTQ5NWMtOTU1ZS0xMGMzZTVmOWY0ZTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjdjYmJiZmRmLWYxYTAtNGUzMi05ZTVjLTYzMmExODM1ZGUxZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiYjJkZjQ0ZTItNWFlNi00M2FlLWI4NmMtOWM1ZjQ3NWY5Yzc5IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIyZjBmY2FkMy03OWYxLTQxMGItYjdmMC02YTZmYTBlZTM5NDciLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrIl19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW10sICJlbmFibGVkIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFjayIsICJpZCI6IDQyLCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogImM5MTU2MTllLWNhMTEtNGZiMS1iYTlkLWEyZDk0MzljOTJmMiIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjNiMWE2NjI4LTVlZjAtNDk1Yy05NTVlLTEwYzNlNWY5ZjRlMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiY3JlYXRlX3NsYWNrX21lc3NhZ2UiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2siLCAiaWQiOiA0MywgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgTm90ZSB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJub3RlIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiYWM1MDY2ZTctMjY0NC00OGUzLTllY2ItODVlYzJjMTZiYjZkIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImIyZGY0NGUyLTVhZTYtNDNhZS1iODZjLTljNWY0NzVmOWM3OSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiMmYwZmNhZDMtNzlmMS00MTBiLWI3ZjAtNmE2ZmEwZWUzOTQ3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJjcmVhdGVfc2xhY2tfcmVwbHkiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IFRhc2sgdG8gU2xhY2siLCAiaWQiOiA0NCwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgVGFzayB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJ0YXNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiMTU0MjIxY2QtZjFjMS00YzZjLWI0ZDItNjFmZjcwOWUyM2ZiIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImIyZGY0NGUyLTVhZTYtNDNhZS1iODZjLTljNWY0NzVmOWM3OSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiMmYwZmNhZDMtNzlmMS00MTBiLWI3ZjAtNmE2ZmEwZWUzOTQ3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fdGFzayJdfV0sICJhcHBzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImV4cG9ydF9kYXRlIjogMTY1OTU1NjcyMjcxMywgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJleHBvcnRfdHlwZSI6IG51bGwsICJmaWVsZHMiOiBbeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja190ZXh0IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxMywgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja190ZXh0IiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJlcXVpcmVkIjogImFsd2F5cyIsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogInNsYWNrX3RleHQiLCAidG9vbHRpcCI6ICJUZXh0IG1lc3NhZ2Ugb3IgYSBjb250YWluZXIgZmllbGQgdG8gcmV0YWluIEpTT04gZmllbGRzIHRvIHNlbmQgdG8gU2xhY2suIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiODVkMjBiNzctNzM0Zi00OTMwLTljNGItYjVmOGQ5OGM1ODFjIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi90YXNrX2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDI5OCwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInRhc2tfaWQiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJ0YXNrX2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiOTU4ZjA5NTMtOGI2Zi00NDcyLWI3ODYtYjlhZTQzNTFkZGZlIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19jaGFubmVsX2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxNiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19jaGFubmVsX2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiT3B0aW9uYWwiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19jaGFubmVsX2lkIiwgInRvb2x0aXAiOiAiT3B0aW9uYWwuIEV4ZWN1dGluZyB3aXRob3V0IGNoYW5uZWwgSUQgYXJjaGl2ZXMgdGhlIGNoYW5uZWwgdGhhdCB0aGlzIGlzIGFzc29jaWF0ZWQgd2l0aC4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5ODQ2ZGYzMS01Yjc2LTQyOTktYjEyYi0xN2UwYzY1NTE3OTEiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2F0dGFjaG1lbnRfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMjkxLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAiYXR0YWNobWVudF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImF0dGFjaG1lbnRfaWQiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5OTk3ZTA0Yy1iZGJlLTRmN2MtOWI4Ny0yYmMwMzkwODI2ZmUiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3NsYWNrX2NoYW5uZWwiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzEyLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2NoYW5uZWwiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19jaGFubmVsIiwgInRvb2x0aXAiOiAiTmFtZSBvZiB0aGUgZXhpc3Rpbmcgb3IgYSBuZXcgc2xhY2sgY2hhbm5lbCB1c2VkIHRvIHNlbmQgbWVzc2FnZSB0by4gQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5Y2FhZGI4Ni0zY2IxLTQ0ZjgtODFmNC00ZGEzMGU2OGExMDYiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMTQsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAic2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgInRvb2x0aXAiOiAiQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLiIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogImFlODJhMjBhLWQ2YWUtNGY3Ny05OGQ4LTEzODhkZmE0YjJmNyIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxNSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAidG9vbHRpcCI6ICJJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiY2MyMzExMjYtNGY0OS00MjM3LTk5OGItZDk1NzA2NjRkNjYyIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9hcnRpZmFjdF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAyOTAsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJhcnRpZmFjdF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImFydGlmYWN0X2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiZDYzZDE2YTEtYzViZC00MDE1LTk4NTAtMDUzMTZiMjI1NjRjIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19tcmtkd24iLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA5LCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX21ya2R3biIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogInNsYWNrX21ya2R3biIsICJ0b29sdGlwIjogIkRpc2FibGUgU2xhY2sgbWFya3VwIHBhcnNpbmcgYnkgc2V0dGluZyB0byBmYWxzZS4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICIyMzg4YmU0OS0yODNmLTRiNzctYmJlYi04NmEyZWUxZGNmMDgiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2luY2lkZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDI4OSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogImluY2lkZW50X2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJlcXVpcmVkIjogImFsd2F5cyIsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImluY2lkZW50X2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiM2YzNWYxYTktZjVkNi00NDBhLWE4MjUtNjZhMzQwYWVhZWZlIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19hc191c2VyIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxMCwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19hc191c2VyIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfYXNfdXNlciIsICJ0b29sdGlwIjogIlNldCB0byB0cnVlIGFuZCB0aGUgYXV0aGVudGljYXRlZCB1c2VyIG9mIHRoZSBTbGFjayBBcHAgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZSwgaWdub3JpbmcgYW55IHZhbHVlcyBwcm92aWRlZCBmb3Igc2xhY2tfdXNlcm5hbWUuICIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogIjQ4ZTU5M2Y0LTNjYzQtNGYzZS1hODA5LTM4ZTVmZWQ3MGYyMCIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc2xhY2tfdXNlcm5hbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzExLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX3VzZXJuYW1lIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfdXNlcm5hbWUiLCAidG9vbHRpcCI6ICJTZXQgeW91ciBTbGFjayBhcHAncyBuYW1lIHRoYXQgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZS4gTXVzdCBiZSB1c2VkIGluIGNvbmp1bmN0aW9uIHdpdGggc2xhY2tfYXNfdXNlciBzZXQgdG8gZmFsc2UsIG90aGVyd2lzZSBpZ25vcmVkLiIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogIjc0MzY1ZWQyLTYzNWEtNDQ2YS1iYTM5LTY1YjI2NGI3YWQ1NCIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vcnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA3LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAic2xhY2sudXNlckBlbWFpbC5jb20sIHNsYWNrLnVzZXIyQGVtYWlsLmNvbSwgIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayB1c2VycyBlbWFpbHMiLCAidG9vbHRpcCI6ICJDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8uIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3J1bGVfc2xhY2tfY2hhbm5lbCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMDUsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicnVsZV9zbGFja19jaGFubmVsIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiRXhpc3Rpbmcgb3IgbmV3IFNsYWNrIGNoYW5uZWwgbmFtZSIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiU2xhY2sgY2hhbm5lbCBuYW1lIiwgInRvb2x0aXAiOiAiTmFtZSBvZiB0aGUgZXhpc3RpbmcgU2xhY2sgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4gSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3J1bGVfc2xhY2tfdGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMDYsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicnVsZV9zbGFja190ZXh0IiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiUGxlYXNlIHJldmlldyBwb3N0ZWQgUmVzaWxpZW50IERhdGEiLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIkFkZGl0aW9uYWwgdGV4dCIsICJ0b29sdGlwIjogIkFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS4iLCAidHlwZV9pZCI6IDYsICJ1dWlkIjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vcnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA4LCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBpcyBjaGFubmVsIHByaXZhdGUiLCAidG9vbHRpcCI6ICJJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICIzYjFhNjYyOC01ZWYwLTQ5NWMtOTU1ZS0xMGMzZTVmOWY0ZTIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3NsYWNrX2NoYW5uZWxfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzE3LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2NoYW5uZWxfaWQiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICJPcHRpb25hbCIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiU2xhY2sgQ2hhbm5lbCBJRCIsICJ0b29sdGlwIjogIk9wdGlvbmFsLiBFeGVjdXRpbmcgd2l0aG91dCBjaGFubmVsIElEIGFyY2hpdmVzIHRoZSBjaGFubmVsIHRoYXQgdGhpcyBpcyBhc3NvY2lhdGVkIHdpdGguIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAidmFsdWVzIjogW119LCB7ImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAiaWQiOiAwLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogdHJ1ZSwgIm5hbWUiOiAiaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAicmVhZF9vbmx5IjogdHJ1ZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGV4dCI6ICJDdXN0b21pemF0aW9ucyBGaWVsZCAoaW50ZXJuYWwpIiwgInR5cGVfaWQiOiAwLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTEifV0sICJmdW5jdGlvbnMiOiBbeyJjcmVhdGVkX2RhdGUiOiAxNjU2NTI0ODA4NDk5LCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQiOiAiRnVuY3Rpb24gZXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAic2xhY2siLCAiZGlzcGxheV9uYW1lIjogIkFyY2hpdmUgU2xhY2sgQ2hhbm5lbCIsICJleHBvcnRfa2V5IjogInNsYWNrX2FyY2hpdmVfY2hhbm5lbCIsICJpZCI6IDE2LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJ0eXBlIjogInVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTg3Nzk0NTUzODgsICJuYW1lIjogInNsYWNrX2FyY2hpdmVfY2hhbm5lbCIsICJvdXRwdXRfanNvbl9leGFtcGxlIjogIntcImNoYW5uZWxcIjogXCJ0ZXN0djJcIn0iLCAib3V0cHV0X2pzb25fc2NoZW1hIjogIntcIiRzY2hlbWFcIjogXCJodHRwOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LTA2L3NjaGVtYVwiLCBcInR5cGVcIjogXCJvYmplY3RcIiwgXCJwcm9wZXJ0aWVzXCI6IHtcImNoYW5uZWxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifX19IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICI4ZjNhOWQxZC04MTgyLTRjNWItYjQyMi1jZmVlZTMzZGUwZGMiLCAidmVyc2lvbiI6IDMsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIzZjM1ZjFhOS1mNWQ2LTQ0MGEtYTgyNS02NmEzNDBhZWFlZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjk4NDZkZjMxLTViNzYtNDI5OS1iMTJiLTE3ZTBjNjU1MTc5MSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiOTU4ZjA5NTMtOGI2Zi00NDcyLWI3ODYtYjlhZTQzNTFkZGZlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogW3siYWN0aW9ucyI6IFtdLCAiZGVzY3JpcHRpb24iOiBudWxsLCAibmFtZSI6ICJFeGFtcGxlOiBBcmNoaXZlIEluY2lkZW50IFNsYWNrIENoYW5uZWwiLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM1fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9hcmNoaXZlX3NsYWNrX2NoYW5uZWxfX3Rhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzF9XX0sIHsiY3JlYXRlZF9kYXRlIjogMTY1NjUyNDgwODU4MSwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIkZ1bmN0aW9uIHVwbG9hZHMgSW5jaWRlbnQsIFRhc2sgb3IgQXJ0aWZhY3QgQXR0YWNobWVudHMgdG8gU2xhY2sgY2hhbm5lbC4iLCAiZm9ybWF0IjogInRleHQifSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJzbGFjayIsICJkaXNwbGF5X25hbWUiOiAiUG9zdCBhdHRhY2htZW50IHRvIFNsYWNrIiwgImV4cG9ydF9rZXkiOiAic2xhY2tfcG9zdF9hdHRhY2htZW50IiwgImlkIjogMTcsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJpZCI6IDEsICJuYW1lIjogImFkbWluQGV4YW1wbGUuY29tIiwgInR5cGUiOiAidXNlciJ9LCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1ODk1Mzc3Njg4NSwgIm5hbWUiOiAic2xhY2tfcG9zdF9hdHRhY2htZW50IiwgIm91dHB1dF9qc29uX2V4YW1wbGUiOiAie1wiY2hhbm5lbFwiOiBcInRlc3Rpbmd2MlwiLCBcInVybFwiOiBcImh0dHBzOi8vaWJtLXJlc2lsaWVudC10ZXN0LnNsYWNrLmNvbS9hcmNoaXZlcy9DMDNRWkdWMFlKVS9wMTY1ODMzMDY4ODI0MTEyOVwifSIsICJvdXRwdXRfanNvbl9zY2hlbWEiOiAie1wiJHNjaGVtYVwiOiBcImh0dHA6Ly9qc29uLXNjaGVtYS5vcmcvZHJhZnQtMDYvc2NoZW1hXCIsIFwidHlwZVwiOiBcIm9iamVjdFwiLCBcInByb3BlcnRpZXNcIjoge1wiY2hhbm5lbFwiOiB7XCJ0eXBlXCI6IFwic3RyaW5nXCJ9LCBcInVybFwiOiB7XCJ0eXBlXCI6IFwic3RyaW5nXCJ9fX0iLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogIjVmZWQ0ZGQ1LTljY2MtNDkyYS05MGUxLTRmMTdlNmE1YzVjOCIsICJ2ZXJzaW9uIjogMywgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjljYWFkYjg2LTNjYjEtNDRmOC04MWY0LTRkYTMwZTY4YTEwNiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiY2MyMzExMjYtNGY0OS00MjM3LTk5OGItZDk1NzA2NjRkNjYyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJhZTgyYTIwYS1kNmFlLTRmNzctOThkOC0xMzg4ZGZhNGIyZjciLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjg1ZDIwYjc3LTczNGYtNDkzMC05YzRiLWI1ZjhkOThjNTgxYyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiOTg0NmRmMzEtNWI3Ni00Mjk5LWIxMmItMTdlMGM2NTUxNzkxIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIzZjM1ZjFhOS1mNWQ2LTQ0MGEtYTgyNS02NmEzNDBhZWFlZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjk1OGYwOTUzLThiNmYtNDQ3Mi1iNzg2LWI5YWU0MzUxZGRmZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiZDYzZDE2YTEtYzViZC00MDE1LTk4NTAtMDUzMTZiMjI1NjRjIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5OTk3ZTA0Yy1iZGJlLTRmN2MtOWI4Ny0yYmMwMzkwODI2ZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3QiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzN9LCB7ImFjdGlvbnMiOiBbXSwgImRlc2NyaXB0aW9uIjogbnVsbCwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCAvIFRhc2sgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhdHRhY2htZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM0fV19LCB7ImNyZWF0ZWRfZGF0ZSI6IDE2NTY1MjQ4MDg2NjEsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICJGdW5jdGlvbiBzZW5kcyBhIG1lc3NhZ2UgZnJvbSBhbiBJbmNpZGVudCwgVGFzaywgTm90ZSBvciBhbiBBcnRpZmFjdCB0byBhIFNsYWNrIGNoYW5uZWwuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAic2xhY2siLCAiZGlzcGxheV9uYW1lIjogIlBvc3QgbWVzc2FnZSB0byBTbGFjayIsICJleHBvcnRfa2V5IjogInNsYWNrX3Bvc3RfbWVzc2FnZSIsICJpZCI6IDE4LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJ0eXBlIjogInVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTg5NDQzNTcxMjgsICJuYW1lIjogInNsYWNrX3Bvc3RfbWVzc2FnZSIsICJvdXRwdXRfanNvbl9leGFtcGxlIjogIntcImNoYW5uZWxcIjogXCJ0ZXN0aW5ndjJcIiwgXCJ1cmxcIjogXCJodHRwczovL2libS1yZXNpbGllbnQtdGVzdC5zbGFjay5jb20vYXJjaGl2ZXMvQzAzUVpHVjBZSlUvcDE2NTgzMzA3NTE3NTI4MTlcIn0iLCAib3V0cHV0X2pzb25fc2NoZW1hIjogIntcIiRzY2hlbWFcIjogXCJodHRwOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LTA2L3NjaGVtYVwiLCBcInR5cGVcIjogXCJvYmplY3RcIiwgXCJwcm9wZXJ0aWVzXCI6IHtcImNoYW5uZWxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifSwgXCJ1cmxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifX19IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzMiLCAidmVyc2lvbiI6IDMsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICI5Y2FhZGI4Ni0zY2IxLTQ0ZjgtODFmNC00ZGEzMGU2OGExMDYiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImNjMjMxMTI2LTRmNDktNDIzNy05OThiLWQ5NTcwNjY0ZDY2MiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiYWU4MmEyMGEtZDZhZS00Zjc3LTk4ZDgtMTM4OGRmYTRiMmY3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI4NWQyMGI3Ny03MzRmLTQ5MzAtOWM0Yi1iNWY4ZDk4YzU4MWMiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjIzODhiZTQ5LTI4M2YtNGI3Ny1iYmViLTg2YTJlZTFkY2YwOCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiNDhlNTkzZjQtM2NjNC00ZjNlLWE4MDktMzhlNWZlZDcwZjIwIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5ODQ2ZGYzMS01Yjc2LTQyOTktYjEyYi0xN2UwYzY1NTE3OTEiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjc0MzY1ZWQyLTYzNWEtNDQ2YS1iYTM5LTY1YjI2NGI3YWQ1NCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2YzNWYxYTktZjVkNi00NDBhLWE4MjUtNjZhMzQwYWVhZWZlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5NThmMDk1My04YjZmLTQ0NzItYjc4Ni1iOWFlNDM1MWRkZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX2FydGlmYWN0IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM3fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgSW5jaWRlbnQgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiY3JlYXRlX3NsYWNrX21lc3NhZ2UiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzJ9LCB7ImFjdGlvbnMiOiBbXSwgImRlc2NyaXB0aW9uIjogbnVsbCwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBOb3RlIHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogIm5vdGUiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiY3JlYXRlX3NsYWNrX3JlcGx5IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM4fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgVGFzayB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJ0YXNrIiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM2fV19XSwgImdlb3MiOiBudWxsLCAiZ3JvdXBzIjogbnVsbCwgImlkIjogMTE0LCAiaW5ib3VuZF9kZXN0aW5hdGlvbnMiOiBbXSwgImluYm91bmRfbWFpbGJveGVzIjogbnVsbCwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTY1OTU1NjcxODgzOCwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJlbmFibGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJoaWRkZW4iOiBmYWxzZSwgImlkIjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgInBhcmVudF9pZCI6IG51bGwsICJzeXN0ZW0iOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXBkYXRlX2RhdGUiOiAxNjU5NTU2NzE4ODM4LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAifV0sICJpbmR1c3RyaWVzIjogbnVsbCwgImxheW91dHMiOiBbXSwgImxvY2FsZSI6IG51bGwsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7ImFwaV9rZXlzIjogWyIwMjI4ZTAwZS0yYzQ3LTQzZTYtYTczNi01NTBmMTA0Yzk0ZWEiLCAiYmVmMTk4YzUtY2M1NC00Mzc3LTk1YzUtZjk4YmYyY2NjZmQ4Il0sICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJzbGFjayIsICJuYW1lIjogInNsYWNrIiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXNlcnMiOiBbXSwgInV1aWQiOiAiNjExZjEwZjctMWI3ZC00OWM1LTg2OTItM2I4MzgxNTZkNDJiIn1dLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJvdmVycmlkZXMiOiBbXSwgInBoYXNlcyI6IFtdLCAicGxheWJvb2tzIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAicm9sZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgInNlcnZlcl92ZXJzaW9uIjogeyJidWlsZF9udW1iZXIiOiA0OSwgIm1ham9yIjogNDMsICJtaW5vciI6IDEsICJ2ZXJzaW9uIjogIjQzLjEuNDkifSwgInRhZ3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwgInRpbWVmcmFtZXMiOiBudWxsLCAidHlwZXMiOiBbeyJhY3Rpb25zIjogW10sICJkaXNwbGF5X25hbWUiOiAiU2xhY2sgQ29udmVyc2F0aW9ucyIsICJleHBvcnRfa2V5IjogInNsYWNrX2NvbnZlcnNhdGlvbnNfZGIiLCAiZmllbGRzIjogeyJzbGFja19kYl9jaGFubmVsIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9jaGFubmVsIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMwMCwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl9jaGFubmVsIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAib3JkZXIiOiAyLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIlNsYWNrIGNoYW5uZWwgbmFtZSIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogMTAwMCwgInV1aWQiOiAiZGYwMTY1ZDQtNjM2Ny00OTE0LWI4MGMtYzg4NzdiMjBjMDExIiwgInZhbHVlcyI6IFtdLCAid2lkdGgiOiAxNjV9LCAic2xhY2tfZGJfY2hhbm5lbF90eXBlIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9jaGFubmVsX3R5cGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAxLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2RiX2NoYW5uZWxfdHlwZSIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgIm9yZGVyIjogMywgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBjaGFubmVsIHR5cGUiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogImNlNGM4Mzk5LTA5ZTMtNDgxYS05NzZmLWIwNzZjOTg5NjVmNyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogNjd9LCAic2xhY2tfZGJfcGVybWFsaW5rIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9wZXJtYWxpbmsiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAyLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0YXJlYSIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl9wZXJtYWxpbmsiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJvcmRlciI6IDQsICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogdHJ1ZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBVUkwiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogIjJmOTUzNjZiLWRkMzItNDAzNS04ODExLTU0OTY0NmMwYWY1YyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogNzl9LCAic2xhY2tfZGJfcmVzX2lkIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9yZXNfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAzLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2RiX3Jlc19pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgIm9yZGVyIjogMSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJSZXNpbGllbnQgSUQiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogImNlM2M5YTFlLTI4MDAtNDdkYS1hNWI5LWMzNzgyNTc5MDk0MyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogMjExfSwgInNsYWNrX2RiX3RpbWUiOiB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJzbGFja19jb252ZXJzYXRpb25zX2RiL3NsYWNrX2RiX3RpbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA0LCAiaW5wdXRfdHlwZSI6ICJkYXRldGltZXBpY2tlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl90aW1lIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAib3JkZXIiOiAwLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIlRpbWUiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogIjY1NmE3ZGFmLWI2NGEtNDU1OS05ODdkLWI3ODlkMGVjNGM0YiIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogMTIzfX0sICJmb3JfYWN0aW9ucyI6IGZhbHNlLCAiZm9yX2N1c3RvbV9maWVsZHMiOiBmYWxzZSwgImZvcl9ub3RpZmljYXRpb25zIjogZmFsc2UsICJmb3Jfd29ya2Zsb3dzIjogZmFsc2UsICJpZCI6IG51bGwsICJwYXJlbnRfdHlwZXMiOiBbImluY2lkZW50Il0sICJwcm9wZXJ0aWVzIjogeyJjYW5fY3JlYXRlIjogZmFsc2UsICJjYW5fZGVzdHJveSI6IGZhbHNlLCAiZm9yX3dobyI6IFtdfSwgInNjcmlwdHMiOiBbXSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidHlwZV9pZCI6IDgsICJ0eXBlX25hbWUiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYiIsICJ1dWlkIjogImUyMDM2YmYzLTYxZWEtNDc1Mi04ZDZmLTJiNGVhMjYyYmIxYiJ9XSwgIndvcmtmbG93cyI6IFt7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA1LCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2tfX2FydGlmYWN0IiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFja1wiPjxkb2N1bWVudGF0aW9uPlVwbG9hZCBBcnRpZmFjdCBBdHRhY2htZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wMmpzaHFmPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMGRneGFxa1wiIG5hbWU9XCJQb3N0IGF0dGFjaG1lbnQgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjVmZWQ0ZGQ1LTljY2MtNDkyYS05MGUxLTRmMTdlNmE1YzVjOFwiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJBcnRpZmFjdCBBdHRhY2htZW50IHdhcyBwb3N0ZWQgdG8gJmx0O2EgaHJlZj0ne30nJmd0O1NsYWNrIGNoYW5uZWwgI3t9Jmx0Oy9hJmd0Oy4gTWVtYmVycyBvZiB0aGlzIGNoYW5uZWwgYXJlOiBcXFxcbnt9XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLnVybCwgcmVzdWx0cy5jaGFubmVsLCB1c2VycylcXG5pbmNpZGVudC5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBBdHRhY2htZW50IGRhdGEgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBSZXF1aXJlZCBpbnB1dHMgYXJlOiB0aGUgaW5jaWRlbnQgaWQgYW5kIGF0dGFjaG1lbnQgaWRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5hcnRpZmFjdF9pZCA9IGFydGlmYWN0LmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbmlucHV0cy5zbGFja190ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDJqc2hxZjwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wcDA4YnllPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzB4dWxsMGpcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBwMDhieWU8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wMmpzaHFmXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMGRneGFxa1wiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBwMDhieWVcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wZGd4YXFrXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHh1bGwwalwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMXUwd3NtdVwiPjx0ZXh0PjwhW0NEQVRBW1Bvc3QgdGhlIEFydGlmYWN0IGF0dGFjaG1lbnQgdG8gc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50XG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xOTltODlsXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMGRneGFxa1wiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzF1MHdzbXVcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18wZGd4YXFrXCIgaWQ9XCJTZXJ2aWNlVGFza18wZGd4YXFrX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjM0MFwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMHh1bGwwalwiIGlkPVwiRW5kRXZlbnRfMHh1bGwwal9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjU3MVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1ODlcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wMmpzaHFmXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDJqc2hxZl9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNDBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI2OVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMHAwOGJ5ZVwiIGlkPVwiU2VxdWVuY2VGbG93XzBwMDhieWVfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ0MFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTcxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MDUuNVwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xdTB3c211XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xdTB3c211X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMjMzXCIgeD1cIjIyN1wiIHk9XCIzOVwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzE5OW04OWxcIiBpZD1cIkFzc29jaWF0aW9uXzE5OW04OWxfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM3OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzQ5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI2OVwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDUsICJkZXNjcmlwdGlvbiI6ICJVcGxvYWQgQXJ0aWZhY3QgQXR0YWNobWVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLiIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrX19hcnRpZmFjdCIsICJsYXN0X21vZGlmaWVkX2J5IjogImFkbWluQGV4YW1wbGUuY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTk1NTQwMDU4MTksICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3QiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogIjI3MjU0ZjIyLThlYmItNDc5MC1hNTU3LTBhODNjYjgwMjE5NiIsICJ3b3JrZmxvd19pZCI6IDMzfSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogImNyZWF0ZV9zbGFja19yZXBseSIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiY3JlYXRlX3NsYWNrX3JlcGx5XCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2tcIj48ZG9jdW1lbnRhdGlvbj5Qb3N0IGEgbWVzc2FnZSBmcm9tIHRoZSBOb3RlIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEluY2lkZW50IG9yIFRhc2sgTm90ZSB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xNGZvODFlPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMXJiMjh5cFwiIG5hbWU9XCJQb3N0IG1lc3NhZ2UgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImRlZDI4MjZjLTY1MjgtNGEyNi1iMmM4LTBjZjIxNWRjZTNjM1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJOb3RlIHdhcyBwb3N0ZWQgdG8gJmx0O2EgaHJlZj0ne30nJmd0O1NsYWNrIGNoYW5uZWwgI3t9Jmx0Oy9hJmd0Oy4gTWVtYmVycyBvZiB0aGlzIGNoYW5uZWwgYXJlOiBcXFxcbnt9XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLnVybCwgcmVzdWx0cy5jaGFubmVsLCB1c2VycylcXG5pZiBub3QgdGFzazpcXG4gIGluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcXG5lbHNlOlxcbiAgdGFzay5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBOb3RlIGRhdGEgICAgICAgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbnJ1bGVfYWRkaXRpb25hbF90ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIEluY2lkZW50IGlkIGZvciB0aGUgVVJMXFxuaW5jaWRlbnRfaWQgPSBzdHIoaW5jaWRlbnQuaWQpXFxudHlwZV9kYXRhID0gXFxcIkluY2lkZW50IE5vdGVcXFwiXFxuaWYgdGFzazpcXG4gIGluY2lkZW50X2lkICs9IFxcXCI/dGFza19pZD1cXFwiK3N0cih0YXNrLmlkKVxcbiAgdHlwZV9kYXRhID0gXFxcIlRhc2sgTm90ZVxcXCJcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSBcXG4jXFxuIyBUZXh0IGZpZWxkcyBsaWtlICdub3RlLnRleHQuY29udGVudCcsICd0YXNrLm5hbWUnIG9yICdTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZScgY2FuIGluY2x1ZGUgZG91YmxlIHF1b3Rlcy5cXG4jIFdhdGNoIG91dCBmb3IgZW1iZWRkZWQgZG91YmxlIHF1b3RlcyBpbiB0aGVzZSB0ZXh0IGZpZWxkcyBhbmQgZXNjYXBlIHdpdGggZmllbGQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIG90aGVyd2lzZSBqc29uLmxvYWRzIHdpbGwgZmFpbC5cXG5zbGFja190ZXh0ID0gdVxcXCJcXFwiXFxcInt7XFxuICBcXFwiQWRkaXRpb25hbCBUZXh0XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MH1cXFwiIH19LFxcbiAgXFxcIlJlc2lsaWVudCBVUkxcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImluY2lkZW50XFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezF9XFxcIiB9fSxcXG4gIFxcXCJUeXBlIG9mIGRhdGFcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInsyfVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgSURcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInszfVxcXCIgfX0sXFxuICBcXFwiVGFza1xcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezR9XFxcIiB9fSxcXG4gIFxcXCJOb3RlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJyaWNodGV4dFxcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns1fVxcXCIgfX1cXG59fVxcXCJcXFwiXFxcIi5mb3JtYXQoXFxuICBydWxlX2FkZGl0aW9uYWxfdGV4dC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJyksXFxuICBpbmNpZGVudF9pZCxcXG4gIHR5cGVfZGF0YSxcXG4gIHN0cihpbmNpZGVudC5pZCksXFxuICB0YXNrLm5hbWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIGlmIHRhc2sgZWxzZSBcXFwiXFxcIiwgXFxuICBub3RlLnRleHQuY29udGVudC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgaWYgbm90ZS50ZXh0IGlzIG5vdCBOb25lIGVsc2UgJycpXFxuXFxuIyBTbGFjayB1c2VybmFtZSAtIG9wdGlvbmFsIHNldHRpbmdcXG4jIFNldCB0byB0cnVlIGFuZCB0aGUgYXV0aGVudGljYXRlZCB1c2VyIG9mIHRoZSBTbGFjayBBcHAgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZSwgaWdub3JpbmcgYW55IHZhbHVlcyBwcm92aWRlZCBmb3Igc2xhY2tfdXNlcm5hbWUuIFxcbiMgU2V0IHlvdXIgYm90J3MgbmFtZSB0byBOb3RlJ3MgY3JlYXRvciB0byBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZS4gTXVzdCBiZSB1c2VkIGluIGNvbmp1bmN0aW9uIHdpdGggc2xhY2tfYXNfdXNlciBzZXQgdG8gZmFsc2UsIG90aGVyd2lzZSBpZ25vcmVkLlxcbiNpbnB1dHMuc2xhY2tfYXNfdXNlciA9IEZhbHNlXFxuI2lucHV0cy5zbGFja191c2VybmFtZSA9IG5vdGUudXNlcl9pZFxcblxcbiMgSUQgb2YgdGhpcyBpbmNpZGVudFxcbmlucHV0cy5pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuXFxuIyBJRCBvZiB0aGlzIFRhc2tcXG5pZiB0YXNrOlxcbiAgaW5wdXRzLnRhc2tfaWQgPSB0YXNrLmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2VcXG4jIENvbnRhaW5lciBmaWVsZCB0byByZXRhaW4gSlNPTiBmaWVsZHMgdG8gc2VuZCB0byBTbGFjay5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTRmbzgxZTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xaDQzZmdnPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTRmbzgxZVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzFyYjI4eXBcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMGd2YjBodFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWg0M2ZnZzwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFoNDNmZ2dcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xcmIyOHlwXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMGd2YjBodFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMG0xZXM3a1wiPjx0ZXh0PjwhW0NEQVRBW1NlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuXG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMXJiMjh5cFwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzBtMWVzN2tcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18xcmIyOHlwXCIgaWQ9XCJTZXJ2aWNlVGFza18xcmIyOHlwX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjI4OVwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMTRmbzgxZVwiIGlkPVwiU2VxdWVuY2VGbG93XzE0Zm84MWVfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMjg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNDMuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMGd2YjBodFwiIGlkPVwiRW5kRXZlbnRfMGd2YjBodF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ5MVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MDlcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xaDQzZmdnXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMWg0M2ZnZ19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0OTFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ0MFwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMG0xZXM3a1wiIGlkPVwiVGV4dEFubm90YXRpb25fMG0xZXM3a19kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiNzVcIiB3aWR0aD1cIjQzOVwiIHg9XCIxMzBcIiB5PVwiNDZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnXCIgaWQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNDNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM0OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTIxXCIvPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiJ9LCAiY29udGVudF92ZXJzaW9uIjogNSwgImRlc2NyaXB0aW9uIjogIlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIE5vdGUgdG8geW91ciBTbGFjayBjaGFubmVsLiBTZW5kIHNwZWNpZmljcyBhYm91dCB0aGUgSW5jaWRlbnQgb3IgVGFzayBOb3RlIHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS4iLCAiZXhwb3J0X2tleSI6ICJjcmVhdGVfc2xhY2tfcmVwbHkiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MjY0Mzg3LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAibm90ZSIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJjcmVhdGVfc2xhY2tfcmVwbHkiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImQ5ZWRhYTM4LTIwZGYtNGMwZS1hMDE3LTlmZTcyMTM2ODAyNSIsICJ3b3JrZmxvd19pZCI6IDM4fSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogImNyZWF0ZV9zbGFja19tZXNzYWdlIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJjcmVhdGVfc2xhY2tfbWVzc2FnZVwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFja1wiPjxkb2N1bWVudGF0aW9uPlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIEluY2lkZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEluY2lkZW50IHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFncXMyN3E8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFncXMyN3FcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18xOThyMjF0XCIvPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzFxb3d0ODdcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzF4NmlhZDg8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMTk4cjIxdFwiIG5hbWU9XCJQb3N0IG1lc3NhZ2UgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImRlZDI4MjZjLTY1MjgtNGEyNi1iMmM4LTBjZjIxNWRjZTNjM1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJJbmNpZGVudCB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxuaW5jaWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcbiMgSW5jaWRlbnQgZGF0YSAgICAgI1xcbiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcblxcbiMgU2xhY2sgYWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2VcXG4jIEFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS5cXG5ydWxlX2FkZGl0aW9uYWxfdGV4dCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpcyBub3QgTm9uZSBlbHNlICcnXFxuXFxuIyBcXFwiZGF0ZXRpbWVcXFwiIGZpZWxkczogQXNzaWduIDAgaWYgaXQncyBOb25lXFxuZGF0ZV9vY2N1cmVkID0gaW5jaWRlbnQuc3RhcnRfZGF0ZSBpZiBpbmNpZGVudC5zdGFydF9kYXRlIGVsc2UgMFxcbmRhdGVfZGlzY292ZXJlZCA9IGluY2lkZW50LmRpc2NvdmVyZWRfZGF0ZSBpZiBpbmNpZGVudC5kaXNjb3ZlcmVkX2RhdGUgZWxzZSAwXFxuXFxuIyBJbmNpZGVudCBpZCBmb3IgdGhlIFVSTFxcbmluY2lkZW50X2lkX3N0ciA9IHN0cihpbmNpZGVudC5pZClcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSAgXFxuI1xcbiMgVGV4dCBmaWVsZHMgbGlrZSAnaW5jaWRlbnQgbmFtZScsICdkZXNjcmlwdGlvbicgb3IgJ1NsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlJyBjYW4gaW5jbHVkZSBkb3VibGUgcXVvdGVzLlxcbiMgV2F0Y2ggb3V0IGZvciBlbWJlZGRlZCBkb3VibGUgcXVvdGVzIGluIHRoZXNlIHRleHQgZmllbGRzIGFuZCBlc2NhcGUgd2l0aCBmaWVsZC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgb3RoZXJ3aXNlIGpzb24ubG9hZHMgd2lsbCBmYWlsLlxcbnNsYWNrX3RleHQgPSB1XFxcIlxcXCJcXFwie3tcXG4gIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInswfVxcXCIgfX0sXFxuICBcXFwiUmVzaWxpZW50IFVSTFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiaW5jaWRlbnRcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MX1cXFwiIH19LFxcbiAgXFxcIlR5cGUgb2YgZGF0YVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezJ9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBJRFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezN9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBuYW1lXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIkRlc2NyaXB0aW9uXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJyaWNodGV4dFxcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns1fVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgVHlwZXNcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiTklTVCBBdHRhY2sgVmVjdG9yc1xcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezd9XFxcIiB9fSxcXG4gIFxcXCJDb25maXJtZWRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImJvb2xlYW5cXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7OH1cXFwiIH19LFxcbiAgXFxcIkRhdGUgQ3JlYXRlZFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs5fSB9fSxcXG4gIFxcXCJEYXRlIE9jY3VycmVkXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJkYXRldGltZVxcXCIsIFxcXCJkYXRhXFxcIjogezEwfSB9fSxcXG4gIFxcXCJEYXRlIERpc2NvdmVyZWRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiB7MTF9IH19LFxcbiAgXFxcIlNldmVyaXR5XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MTJ9XFxcIiB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJJbmNpZGVudFxcXCIsXFxuICBpbmNpZGVudF9pZF9zdHIsXFxuICBpbmNpZGVudC5uYW1lLnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50LmRlc2NyaXB0aW9uLmNvbnRlbnQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIGlmIGluY2lkZW50LmRlc2NyaXB0aW9uIGlzIG5vdCBOb25lIGVsc2UgJycsXFxuICBpbmNpZGVudC5pbmNpZGVudF90eXBlX2lkcyxcXG4gIGluY2lkZW50Lm5pc3RfYXR0YWNrX3ZlY3RvcnMsXFxuICBpbmNpZGVudC5jb25maXJtZWQsXFxuICBpbmNpZGVudC5jcmVhdGVfZGF0ZSxcXG4gIGRhdGVfb2NjdXJlZCxcXG4gIGRhdGVfZGlzY292ZXJlZCxcXG4gIGluY2lkZW50LnNldmVyaXR5X2NvZGUpXFxuXFxuIyBJRCBvZiB0aGlzIGluY2lkZW50XFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5cXG4jIFNsYWNrIGNoYW5uZWwgbmFtZVxcbiMgTmFtZSBvZiB0aGUgZXhpc3RpbmcgU2xhY2sgV29ya3NwYWNlIGNoYW5uZWwgb3IgYSBuZXcgU2xhY2sgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8uIFxcbiMgQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4gXFxuIyBJZiB5b3UgbGVhdmUgdGhpcyBmaWVsZCBlbXB0eSwgZnVuY3Rpb24gd2lsbCB0cnkgdG8gdXNlIHRoZSBzbGFja19jaGFubmVsIGFzc29jaWF0ZWQgd2l0aCB0aGUgSW5jaWRlbnQgb3IgVGFzayBmb3VuZCBpbiB0aGUgU2xhY2sgQ29udmVyc2F0aW9ucyBkYXRhdGFibGUuIFxcbiMgSWYgdGhlcmUgaXNuXHUyMDE5dCBvbmUgZGVmaW5lZCwgdGhlIHdvcmtmbG93IHdpbGwgdGVybWluYXRlLlxcbmlucHV0cy5zbGFja19jaGFubmVsID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxcXG5cXG4jIElzIGNoYW5uZWwgcHJpdmF0ZVxcbiMgSW5kaWNhdGUgaWYgdGhlIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvIHNob3VsZCBiZSBwcml2YXRlLlxcbmlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGUgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZVxcblxcbiMgU2xhY2sgdXNlciBlbWFpbHNcXG4jIENvbW1hIHNlcGFyYXRlZCBsaXN0IG9mIGVtYWlscyBiZWxvbmdpbmcgdG8gU2xhY2sgdXNlcnMgaW4geW91ciB3b3Jrc3BhY2UgdGhhdCB3aWxsIGJlIGFkZGVkIHRvIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by5cXG5pbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHNcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZVxcbiMgQ29udGFpbmVyIGZpZWxkIHRvIHJldGFpbiBKU09OIGZpZWxkcyB0byBzZW5kIHRvIFNsYWNrLlxcbmlucHV0cy5zbGFja190ZXh0ID0gc2xhY2tfdGV4dFxcblxcbiMgU2xhY2sgQ2hhbm5lbCBJRCwgZmFzdGVyIHRoYW4gZmluZGluZyB2aWEgY2hhbm5lbCBuYW1lXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWQgPSBydWxlLnByb3BlcnRpZXMuc2xhY2tfY2hhbm5lbF9pZCBpZiBydWxlLnByb3BlcnRpZXMuc2xhY2tfY2hhbm5lbF9pZCBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsX2lkXFxuXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRfbGFuZ3VhZ2VcIjpcInB5dGhvblwiLFwicmVzdWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xZ3FzMjdxPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzF4NmlhZDg8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xeDZpYWQ4XCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMTk4cjIxdFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzFxb3d0ODdcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzF4ejJpcjVcIj48dGV4dD5TZWxlY3QgdGhlIHNsYWNrX2NoYW5uZWwgdG8gcG9zdCBpbiBhbmQgYWRqdXN0IHRoZSBwb3N0aW5nIHBhcmFtZXRlcnMgYXMgbmVlZGVkLjwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzBpamZpd25cIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xOThyMjF0XCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMXh6MmlyNVwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzFncXMyN3FcIiBpZD1cIlNlcXVlbmNlRmxvd18xZ3FzMjdxX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjI4M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjE5NS41XCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzFxb3d0ODdcIiBpZD1cIkVuZEV2ZW50XzFxb3d0ODdfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI0NDVcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjQxOFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzE5OHIyMXRcIiBpZD1cIlNlcnZpY2VUYXNrXzE5OHIyMXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMjgzXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xeDZpYWQ4XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMXg2aWFkOF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzgzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0NDVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQxNFwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xeHoyaXI1XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xeHoyaXI1X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI1NlwiIHdpZHRoPVwiMjQ1XCIgeD1cIjE2MVwiIHk9XCIzNFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzBpamZpd25cIiBpZD1cIkFzc29jaWF0aW9uXzBpamZpd25fZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjMyMFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMjk0XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI5MFwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDUsICJkZXNjcmlwdGlvbiI6ICJQb3N0IGEgbWVzc2FnZSBmcm9tIHRoZSBJbmNpZGVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwuIFNlbmQgc3BlY2lmaWNzIGFib3V0IHRoZSBJbmNpZGVudCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuIiwgImV4cG9ydF9rZXkiOiAiY3JlYXRlX3NsYWNrX21lc3NhZ2UiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MTQyOTgwLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogImNyZWF0ZV9zbGFja19tZXNzYWdlIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICI4ZGY2ZjMzMy00NDIzLTRlOWQtOTU1NC1kY2VhY2QzMTFjYmEiLCAid29ya2Zsb3dfaWQiOiAzMn0sIHsiYWN0aW9ucyI6IFtdLCAiY29udGVudCI6IHsidmVyc2lvbiI6IDQsICJ3b3JrZmxvd19pZCI6ICJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwic2xhY2tfZXhhbXBsZV9hcmNoaXZlX3NsYWNrX2NoYW5uZWxfX3Rhc2tcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsXCI+PGRvY3VtZW50YXRpb24+RXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFRhc2sgYXNzb2NpYXRlZCBTbGFjayBjaGFubmVsIHRvIGEgdGV4dCBmaWxlLCBzYXZlcyB0aGUgdGV4dCBmaWxlIGFzIGFuIEF0dGFjaG1lbnQgYW5kIGFyY2hpdmVzIHRoZSBTbGFjayBjaGFubmVsLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGtobHlncTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIiBuYW1lPVwiQXJjaGl2ZSBTbGFjayBDaGFubmVsXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI4ZjNhOWQxZC04MTgyLTRjNWItYjQyMi1jZmVlZTMzZGUwZGNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIm5vdGVUZXh0ID0gdVxcXCJcXFwiXFxcIlNsYWNrIGNoYW5uZWwge30gaGFzIGJlZW4gYXJjaGl2ZWQuIFRoZSBjb252ZXJzYXRpb24gaGlzdG9yeSBoYXMgYmVlbiBzYXZlZCBhcyBhbiBhdHRhY2htZW50LlxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy5jaGFubmVsKVxcbnRhc2suYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIElEIG9mIHRoaXMgaW5jaWRlbnRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcblxcbiMgSUQgb2YgdGhpcyBUYXNrXFxuaW5wdXRzLnRhc2tfaWQgPSB0YXNrLmlkXFxuXFxuIyBTbGFjayBDaGFubmVsIElELCBmYXN0ZXIgdGhhbiBmaW5kaW5nIHZpYSBjaGFubmVsIG5hbWVcXG5pbnB1dHMuc2xhY2tfY2hhbm5lbF9pZCA9IHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGlmIHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWRcXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBraGx5Z3E8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGp3ZXdrazwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xNDhmcWNzXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wandld2trPC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMGtobHlncVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIi8+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wandld2trXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMHV2ZGhqc1wiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzE0OGZxY3NcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzBmc2ZkYXdcIj48dGV4dD5BdXRvbWF0aWMgcnVsZSBhcmNoaXZlcyBzbGFja19jaGFubmVsIGFzc29jaWF0ZWQgd2l0aCB0aGUgVGFzazwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFncXIzd2pcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wdXZkaGpzXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMGZzZmRhd1wiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIiBpZD1cIlNlcnZpY2VUYXNrXzB1dmRoanNfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzYzXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xNDhmcWNzXCIgaWQ9XCJFbmRFdmVudF8xNDhmcWNzX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjMxXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjY0OVwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBraGx5Z3FcIiBpZD1cIlNlcXVlbmNlRmxvd18wa2hseWdxX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM2M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjgwLjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBqd2V3a2tcIiBpZD1cIlNlcXVlbmNlRmxvd18wandld2trX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NjNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjYzMVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTQ3XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wZnNmZGF3XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wZnNmZGF3X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI0M1wiIHdpZHRoPVwiMjM3XCIgeD1cIjIyNFwiIHk9XCI2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFncXIzd2pcIiBpZD1cIkFzc29jaWF0aW9uXzFncXIzd2pfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM4OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMDlcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiA0LCAiZGVzY3JpcHRpb24iOiAiRXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFRhc2sgYXNzb2NpYXRlZCBTbGFjayBjaGFubmVsIHRvIGEgdGV4dCBmaWxlLCBzYXZlcyB0aGUgdGV4dCBmaWxlIGFzIGFuIEF0dGFjaG1lbnQgYW5kIGFyY2hpdmVzIHRoZSBTbGFjayBjaGFubmVsLiIsICJleHBvcnRfa2V5IjogInNsYWNrX2V4YW1wbGVfYXJjaGl2ZV9zbGFja19jaGFubmVsX190YXNrIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTM4MTY1ODQyNCwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBUYXNrIFNsYWNrIENoYW5uZWwiLCAib2JqZWN0X3R5cGUiOiAidGFzayIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiZmNjOTQ4MjgtY2I5MS00NzgxLWI3MDYtZjNhNmFlMDFlODA1IiwgIndvcmtmbG93X2lkIjogMzF9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiAxNCwgIndvcmtmbG93X2lkIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX19hcnRpZmFjdCIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX2FydGlmYWN0XCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+UG9zdCBhIG1lc3NhZ2UgZnJvbSB0aGUgQXJ0aWZhY3QgdG8geW91ciBTbGFjayBjaGFubmVsLiBTZW5kIHNwZWNpZmljcyBhYm91dCB0aGUgQXJ0aWZhY3Qgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMDhnMjk0OTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzB4eXlhcXRcIiBuYW1lPVwiUG9zdCBtZXNzYWdlIHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiQXJ0aWZhY3Qgd2FzIHBvc3RlZCB0byAmbHQ7YSBocmVmPSd7fScmZ3Q7U2xhY2sgY2hhbm5lbCAje30mbHQ7L2EmZ3Q7LiBNZW1iZXJzIG9mIHRoaXMgY2hhbm5lbCBhcmU6IFxcXFxue31cXFwiXFxcIlxcXCIuZm9ybWF0KHJlc3VsdHMudXJsLCByZXN1bHRzLmNoYW5uZWwsIHVzZXJzKVxcbmluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcIixcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRfbGFuZ3VhZ2VcIjpcInB5dGhvblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIyMjIyMjIyMjIyMjIyMjIyMjIyNcXG4jIEFydGlmYWN0IGRhdGEgICAgICNcXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyNcXG5cXG4jIFNsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlXFxuIyBBZGRpdGlvbmFsIHRleHQgbWVzc2FnZSB0byBpbmNsdWRlIHdpdGggdGhlIEluY2lkZW50LCBOb3RlLCBBcnRpZmFjdCwgQXR0YWNobWVudCBvciBUYXNrIGRhdGEuXFxucnVsZV9hZGRpdGlvbmFsX3RleHQgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaXMgbm90IE5vbmUgZWxzZSAnJ1xcblxcbiMgSW5jaWRlbnQgaWQgZm9yIHRoZSBVUkxcXG5pbmNpZGVudF9pZF9zdHIgPSBzdHIoaW5jaWRlbnQuaWQpXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2UgaW4gSlNPTiBmb3JtYXRcXG4jIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxcbiMgRG8gbm90IHJlbW92ZSBmaXJzdCAzIGVsZW1lbnRzIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiLCBcXFwiUmVzaWxpZW50IFVSTFxcXCIgYW5kIFxcXCJUeXBlIG9mIGRhdGFcXFwiLFxcbiMgdGhlIGluZm9ybWF0aW9uIGlzIHVzZWQgdG8gZ2VuZXJhdGUgdGhlIHRpdGxlIG9mIHRoZSBtZXNzYWdlLlxcbiNcXG4jIEFkZC9yZW1vdmUgaW5mb3JtYXRpb24gdXNpbmcgdGhlIHN5bnRheDpcXG4jIFxcXCJsYWJlbFxcXCI6IHt7IFxcXCJ0eXBlXFxcIjogXFxcIltzdHJpbmd8cmljaHRleHR8Ym9vbGVhbnxkYXRldGltZVxcXCIsIFxcXCJkYXRhXFxcIjogXFxcInJlc2lsaWVudCBmaWVsZCBkYXRhXFxcIiB9fVxcbiNcXG4jIE1ha2Ugc3VyZSB0byBzZW5kIFxcXCJkYXRldGltZVxcXCIgdHlwZXMgYXMgaW50ZWdlcnMgYW5kIG5vdCBzdHJpbmdzOlxcbiMgd2l0aG91dCBkb3VibGUgcXVvdGVzOiB7IFxcXCJ0eXBlXFxcIjogXFxcImRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiByZXNpbGllbnQgZGF0ZXRpbWUgZGF0YX0gIFxcbiNcXG4jIFRleHQgZmllbGRzIGxpa2UgJ2FydGlmYWN0LnZhbHVlJywgb3IgJ1NsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlJyBjYW4gaW5jbHVkZSBkb3VibGUgcXVvdGVzLlxcbiMgV2F0Y2ggb3V0IGZvciBlbWJlZGRlZCBkb3VibGUgcXVvdGVzIGluIHRoZXNlIHRleHQgZmllbGRzIGFuZCBlc2NhcGUgd2l0aCBmaWVsZC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgb3RoZXJ3aXNlIGpzb24ubG9hZHMgd2lsbCBmYWlsLlxcbnNsYWNrX3RleHQgPSB1XFxcIlxcXCJcXFwie3tcXG4gIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInswfVxcXCIgfX0sXFxuICBcXFwiUmVzaWxpZW50IFVSTFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiaW5jaWRlbnRcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MX1cXFwiIH19LFxcbiAgXFxcIlR5cGUgb2YgZGF0YVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezJ9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBJRFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezN9XFxcIiB9fSxcXG4gIFxcXCJBcnRpZmFjdCBUeXBlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIkFydGlmYWN0IFZhbHVlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NX1cXFwiIH19LFxcbiAgXFxcIkFydGlmYWN0IENyZWF0ZWQgQnlcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiQXJ0aWZhY3QgQ3JlYXRlZCBvblxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs3fSB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJBcnRpZmFjdFxcXCIsXFxuICBpbmNpZGVudF9pZF9zdHIsXFxuICBhcnRpZmFjdC50eXBlLFxcbiAgYXJ0aWZhY3QudmFsdWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpLFxcbiAgYXJ0aWZhY3QuY3JlYXRvci5kaXNwbGF5X25hbWUsXFxuICBhcnRpZmFjdC5jcmVhdGVkKVxcblxcbiMgSUQgb2YgdGhpcyBpbmNpZGVudFxcbmlucHV0cy5pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2VcXG4jIENvbnRhaW5lciBmaWVsZCB0byByZXRhaW4gSlNPTiBmaWVsZHMgdG8gc2VuZCB0byBTbGFjay5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDhnMjk0OTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wd2hxc2t5PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzA3ODNnMG1cIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB3aHFza3k8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wOGcyOTQ5XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMHh5eWFxdFwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzB3aHFza3lcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18weHl5YXF0XCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMDc4M2cwbVwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMXhvaXZsZFwiPjx0ZXh0PlNlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMW56ZHhhelwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzB4eXlhcXRcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xeG9pdmxkXCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMHh5eWFxdFwiIGlkPVwiU2VydmljZVRhc2tfMHh5eWFxdF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzNTVcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzA3ODNnMG1cIiBpZD1cIkVuZEV2ZW50XzA3ODNnMG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI2MTdcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjM1XCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMDhnMjk0OVwiIGlkPVwiU2VxdWVuY2VGbG93XzA4ZzI5NDlfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNzYuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMHdocXNreVwiIGlkPVwiU2VxdWVuY2VGbG93XzB3aHFza3lfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ1NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNjE3XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MzZcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMXhvaXZsZFwiIGlkPVwiVGV4dEFubm90YXRpb25fMXhvaXZsZF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzNcIiB3aWR0aD1cIjMzMFwiIHg9XCIyMzhcIiB5PVwiMzlcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xbnpkeGF6XCIgaWQ9XCJBc3NvY2lhdGlvbl8xbnpkeGF6X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MDRcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjQwM1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiNzJcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiAxNCwgImRlc2NyaXB0aW9uIjogIlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIEFydGlmYWN0IHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEFydGlmYWN0IHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS4iLCAiZXhwb3J0X2tleSI6ICJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fYXJ0aWZhY3QiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MzMzNzM0LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX19hcnRpZmFjdCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiYjM4NDZlMDItZTFmOS00MjBlLTg2YWMtNWJmMGI4Zjk1YTlmIiwgIndvcmtmbG93X2lkIjogMzd9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA0LCAid29ya2Zsb3dfaWQiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJhcmNoaXZlX3NsYWNrX2NoYW5uZWxcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEFyY2hpdmUgSW5jaWRlbnQgU2xhY2sgQ2hhbm5lbFwiPjxkb2N1bWVudGF0aW9uPkV4cG9ydHMgY29udmVyc2F0aW9uIGhpc3RvcnkgZnJvbSBJbmNpZGVudCBhc3NvY2lhdGVkIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xM3JkZ3p0PC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMXgyNGM0MFwiIG5hbWU9XCJBcmNoaXZlIFNsYWNrIENoYW5uZWxcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjhmM2E5ZDFkLTgxODItNGM1Yi1iNDIyLWNmZWVlMzNkZTBkY1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwibm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiU2xhY2sgY2hhbm5lbCB7fSBoYXMgYmVlbiBhcmNoaXZlZC4gVGhlIGNvbnZlcnNhdGlvbiBoaXN0b3J5IGhhcyBiZWVuIHNhdmVkIGFzIGFuIGF0dGFjaG1lbnQuXFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLmNoYW5uZWwpXFxuaW5jaWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIElEIG9mIHRoaXMgaW5jaWRlbnRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTNyZGd6dDwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wcXBoMXBsPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTNyZGd6dFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzF4MjRjNDBcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMHdnenE1dFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHFwaDFwbDwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBxcGgxcGxcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xeDI0YzQwXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHdnenE1dFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMDU4YnZhMVwiPjx0ZXh0PjwhW0NEQVRBW0F1dG9tYXRpYyBydWxlIGFyY2hpdmVzIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudFxuXV0+PC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMGl1MGoxNFwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzF4MjRjNDBcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wNThidmExXCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMXgyNGM0MFwiIGlkPVwiU2VydmljZVRhc2tfMXgyNGM0MF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzNzZcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzEzcmRnenRcIiBpZD1cIlNlcXVlbmNlRmxvd18xM3JkZ3p0X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM3NlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjg3XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8wd2d6cTV0XCIgaWQ9XCJFbmRFdmVudF8wd2d6cTV0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjc2XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjY5NFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBxcGgxcGxcIiBpZD1cIlNlcXVlbmNlRmxvd18wcXBoMXBsX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NzZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjY3NlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTc2XCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzA1OGJ2YTFcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzA1OGJ2YTFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjYwXCIgd2lkdGg9XCIyMjhcIiB4PVwiMjE5XCIgeT1cIjM3XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMGl1MGoxNFwiIGlkPVwiQXNzb2NpYXRpb25fMGl1MGoxNF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzk5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxNjZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNTJcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjk3XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiJ9LCAiY29udGVudF92ZXJzaW9uIjogNCwgImRlc2NyaXB0aW9uIjogIkV4cG9ydHMgY29udmVyc2F0aW9uIGhpc3RvcnkgZnJvbSBJbmNpZGVudCBhc3NvY2lhdGVkIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuIiwgImV4cG9ydF9rZXkiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTM4MTYyMzQzOCwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBJbmNpZGVudCBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogImFyY2hpdmVfc2xhY2tfY2hhbm5lbCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiMzkwNDI1YzEtMWNlNi00ZjMxLWE1MjItMzcyYzE5YmEyMzcwIiwgIndvcmtmbG93X2lkIjogMzV9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA2LCAid29ya2Zsb3dfaWQiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+VXBsb2FkIEluY2lkZW50IG9yIFRhc2sgQXR0YWNobWVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMXBwMGp0dzwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzBua2I1bnVcIiBuYW1lPVwiUG9zdCBhdHRhY2htZW50IHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI1ZmVkNGRkNS05Y2NjLTQ5MmEtOTBlMS00ZjE3ZTZhNWM1YzhcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiQXR0YWNobWVudCB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxuaWYgbm90IHRhc2s6XFxuICBpbmNpZGVudC5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXFxuZWxzZTpcXG4gIHRhc2suYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcbiMgQXR0YWNobWVudCBkYXRhICAgI1xcbiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcblxcbiMgUmVxdWlyZWQgaW5wdXRzIGFyZTogdGhlIGluY2lkZW50IGlkIGFuZCBhdHRhY2htZW50IGlkXFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5pbnB1dHMuYXR0YWNobWVudF9pZCA9IGF0dGFjaG1lbnQuaWRcXG5cXG4jIElmIHRoaXMgaXMgYSBcXFwidGFzayBhdHRhY2htZW50XFxcIiB0aGVuIHdlIHdpbGwgYWRkaXRpb25hbGx5IGhhdmUgYSB0YXNrLWlkXFxuaWYgdGFzayBpcyBub3QgTm9uZTpcXG4gIGlucHV0cy50YXNrX2lkID0gdGFzay5pZFxcblxcbiMgU2xhY2sgY2hhbm5lbCBuYW1lXFxuIyBOYW1lIG9mIHRoZSBleGlzdGluZyBTbGFjayBXb3Jrc3BhY2UgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gXFxuIyBDaGFubmVsIG5hbWVzIGNhbiBvbmx5IGNvbnRhaW4gbG93ZXJjYXNlIGxldHRlcnMsIG51bWJlcnMsIGh5cGhlbnMsIGFuZCB1bmRlcnNjb3JlcywgYW5kIG11c3QgYmUgMjEgY2hhcmFjdGVycyBvciBsZXNzLiBcXG4jIElmIHlvdSBsZWF2ZSB0aGlzIGZpZWxkIGVtcHR5LCBmdW5jdGlvbiB3aWxsIHRyeSB0byB1c2UgdGhlIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrIGZvdW5kIGluIHRoZSBTbGFjayBDb252ZXJzYXRpb25zIGRhdGF0YWJsZS4gXFxuIyBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWwgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbFxcblxcbiMgSXMgY2hhbm5lbCBwcml2YXRlXFxuIyBJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuXFxuaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlXFxuXFxuIyBTbGFjayB1c2VyIGVtYWlsc1xcbiMgQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLlxcbmlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlsc1xcblxcbiMgU2xhY2sgYWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2VcXG4jIEFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpcyBub3QgTm9uZSBlbHNlICcnXFxuXFxuIyBTbGFjayBDaGFubmVsIElELCBmYXN0ZXIgdGhhbiBmaW5kaW5nIHZpYSBjaGFubmVsIG5hbWVcXG5pbnB1dHMuc2xhY2tfY2hhbm5lbF9pZCA9IHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGlmIHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWRcXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzFwcDBqdHc8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTR3bWNsczwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8wYTRzNW50XCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xNHdtY2xzPC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMXBwMGp0d1wiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzBua2I1bnVcIi8+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xNHdtY2xzXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMG5rYjVudVwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzBhNHM1bnRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzAzYzg1dWpcIj48dGV4dD48IVtDREFUQVtQb3N0IHRoZSBhdHRhY2htZW50IHRvIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrXG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wMm93amtqXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMG5rYjVudVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzAzYzg1dWpcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18wbmtiNW51XCIgaWQ9XCJTZXJ2aWNlVGFza18wbmtiNW51X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjMyMVwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMGE0czVudFwiIGlkPVwiRW5kRXZlbnRfMGE0czVudF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjU3MFwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1ODhcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xcHAwanR3XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMXBwMGp0d19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzMjFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI1OS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xNHdtY2xzXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMTR3bWNsc19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDIxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1NzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ5NS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wM2M4NXVqXCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wM2M4NXVqX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMzI3XCIgeD1cIjIyN1wiIHk9XCI0OFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzAyb3dqa2pcIiBpZD1cIkFzc29jaWF0aW9uXzAyb3dqa2pfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM3N1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI3OFwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDYsICJkZXNjcmlwdGlvbiI6ICJVcGxvYWQgSW5jaWRlbnQgb3IgVGFzayBBdHRhY2htZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuIiwgImV4cG9ydF9rZXkiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MDgxMTk2LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImRjNGM4MzFjLWE0NDQtNGFhYy1hYTFjLWM3NDg5OWVmOWE1MCIsICJ3b3JrZmxvd19pZCI6IDM0fSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fdGFza1wiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogUG9zdCBUYXNrIHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+UG9zdCBtZXNzYWdlIGZyb20gYSBUYXNrIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIFRhc2sgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTl4cmdyeTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzFyOWpyMTJcIiBuYW1lPVwiUG9zdCBtZXNzYWdlIHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiVGFzayB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxudGFzay5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBUYXNrIGRhdGEgICAgICAgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBJbmNpZGVudCBpZCBmb3IgdGhlIFVSTFxcbmluY2lkZW50X2lkX3N0ciA9IHN0cihpbmNpZGVudC5pZClcXG5pZiB0YXNrOlxcbiAgaW5jaWRlbnRfaWRfc3RyICs9IFxcXCI/dGFza19pZD1cXFwiK3N0cih0YXNrLmlkKVxcblxcbiMgVGFzayBkdWUgZGF0ZSwgc2VuZCAwIGlmIGl0J3MgTm9uZVxcbnRhc2tfZHVlX2RhdGUgPSB0YXNrLmR1ZV9kYXRlIGlmIHRhc2suZHVlX2RhdGUgZWxzZSAwXFxuXFxuIyBUYXNrIFN0YXR1c1xcbnRhc2tfc3RhdHVzID0gXFxcIk9wZW5cXFwiIGlmIHRhc2suc3RhdHVzID09IFxcXCJPXFxcIiBlbHNlIFxcXCJDbG9zZWRcXFwiXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbnJ1bGVfYWRkaXRpb25hbF90ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSBcXG4jXFxuIyBUZXh0IGZpZWxkcyBsaWtlICd0YXNrIG5hbWUnIG9yICdTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZScgY2FuIGluY2x1ZGUgZG91YmxlIHF1b3Rlcy5cXG4jIFdhdGNoIG91dCBmb3IgZW1iZWRkZWQgZG91YmxlIHF1b3RlcyBpbiB0aGVzZSB0ZXh0IGZpZWxkcyBhbmQgZXNjYXBlIHdpdGggZmllbGQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIG90aGVyd2lzZSBqc29uLmxvYWRzIHdpbGwgZmFpbC5cXG5zbGFja190ZXh0ID0gdVxcXCJcXFwiXFxcInt7XFxuICBcXFwiQWRkaXRpb25hbCBUZXh0XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MH1cXFwiIH19LFxcbiAgXFxcIlJlc2lsaWVudCBVUkxcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImluY2lkZW50XFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezF9XFxcIiB9fSxcXG4gIFxcXCJUeXBlIG9mIGRhdGFcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInsyfVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgSURcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInszfVxcXCIgfX0sXFxuICBcXFwiVGFzayBOYW1lXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIlRhc2sgU3RhdHVzXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NX1cXFwiIH19LFxcbiAgXFxcIlRhc2sgT3duZXJcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiVGFzayBEdWUgRGF0ZVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs3fSB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJUYXNrXFxcIixcXG4gIHN0cihpbmNpZGVudC5pZCksXFxuICB0YXNrLm5hbWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpLFxcbiAgdGFza19zdGF0dXMsXFxuICB0YXNrLm93bmVyX2lkLFxcbiAgdGFza19kdWVfZGF0ZSlcXG5cXG4jIFNsYWNrIHVzZXJuYW1lIC0gb3B0aW9uYWwgc2V0dGluZ1xcbiMgU2V0IHRvIHRydWUgYW5kIHRoZSBhdXRoZW50aWNhdGVkIHVzZXIgb2YgdGhlIFNsYWNrIEFwcCB3aWxsIGFwcGVhciBhcyB0aGUgYXV0aG9yIG9mIHRoZSBtZXNzYWdlLCBpZ25vcmluZyBhbnkgdmFsdWVzIHByb3ZpZGVkIGZvciBzbGFja191c2VybmFtZS4gXFxuIyBTZXQgeW91ciBib3QncyBuYW1lIHRvIFRhc2sncyBjcmVhdG9yIHRvIGFwcGVhciBhcyB0aGUgYXV0aG9yIG9mIHRoZSBtZXNzYWdlLiBNdXN0IGJlIHVzZWQgaW4gY29uanVuY3Rpb24gd2l0aCBzbGFja19hc191c2VyIHNldCB0byBmYWxzZSwgb3RoZXJ3aXNlIGlnbm9yZWQuXFxuI2lucHV0cy5zbGFja19hc191c2VyID0gRmFsc2VcXG4jaW5wdXRzLnNsYWNrX3VzZXJuYW1lID0gdGFzay5jcmVhdG9yX2lkXFxuXFxuIyBJRCBvZiB0aGlzIGluY2lkZW50XFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5cXG4jIElEIG9mIHRoaXMgVGFza1xcbmlucHV0cy50YXNrX2lkID0gdGFzay5pZFxcblxcbiMgU2xhY2sgY2hhbm5lbCBuYW1lXFxuIyBOYW1lIG9mIHRoZSBleGlzdGluZyBTbGFjayBXb3Jrc3BhY2UgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gXFxuIyBDaGFubmVsIG5hbWVzIGNhbiBvbmx5IGNvbnRhaW4gbG93ZXJjYXNlIGxldHRlcnMsIG51bWJlcnMsIGh5cGhlbnMsIGFuZCB1bmRlcnNjb3JlcywgYW5kIG11c3QgYmUgMjEgY2hhcmFjdGVycyBvciBsZXNzLiBcXG4jIElmIHlvdSBsZWF2ZSB0aGlzIGZpZWxkIGVtcHR5LCBmdW5jdGlvbiB3aWxsIHRyeSB0byB1c2UgdGhlIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrIGZvdW5kIGluIHRoZSBTbGFjayBDb252ZXJzYXRpb25zIGRhdGF0YWJsZS4gXFxuIyBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWwgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbFxcblxcbiMgSXMgY2hhbm5lbCBwcml2YXRlXFxuIyBJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuXFxuaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlXFxuXFxuIyBTbGFjayB1c2VyIGVtYWlsc1xcbiMgQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLlxcbmlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlsc1xcblxcbiMgU2xhY2sgdGV4dCBtZXNzYWdlXFxuIyBDb250YWluZXIgZmllbGQgdG8gcmV0YWluIEpTT04gZmllbGRzIHRvIHNlbmQgdG8gU2xhY2tcXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTl4cmdyeTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wZTAxcWkwPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzBwMzNlN3NcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBlMDFxaTA8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xOXhyZ3J5XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMXI5anIxMlwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBlMDFxaTBcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xcjlqcjEyXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHAzM2U3c1wiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMHBmcjY4N1wiPjx0ZXh0PlNlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXN3MzlsbVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFyOWpyMTJcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wcGZyNjg3XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMXI5anIxMlwiIGlkPVwiU2VydmljZVRhc2tfMXI5anIxMl9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMzJcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzBwMzNlN3NcIiBpZD1cIkVuZEV2ZW50XzBwMzNlN3NfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI1ODNcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjAxXCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMTl4cmdyeVwiIGlkPVwiU2VxdWVuY2VGbG93XzE5eHJncnlfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzMyXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBlMDFxaTBcIiBpZD1cIlNlcXVlbmNlRmxvd18wZTAxcWkwX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MzJcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjU4M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTA3LjVcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMHBmcjY4N1wiIGlkPVwiVGV4dEFubm90YXRpb25fMHBmcjY4N19kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjI4NlwiIHg9XCIxOTdcIiB5PVwiNTFcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc3czOWxtXCIgaWQ9XCJBc3NvY2lhdGlvbl8xc3czOWxtX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM0NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiODFcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiA1LCAiZGVzY3JpcHRpb24iOiAiUG9zdCBtZXNzYWdlIGZyb20gYSBUYXNrIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIFRhc2sgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLiIsICJleHBvcnRfa2V5IjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTU1NDMxNzI0MSwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBUYXNrIHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX3Rhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImViYThmMjcwLTJkMDMtNGRhOC1hODEyLTJjODc4Mzc0MjQ1NCIsICJ3b3JrZmxvd19pZCI6IDM2fV0sICJ3b3Jrc3BhY2VzIjogW119\"}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"info\": {\"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"date_time\": {\"type\": \"integer\"}, \"compress_type\": {\"type\": \"integer\"}, \"comment\": {\"type\": \"string\"}, \"create_system\": {\"type\": \"integer\"}, \"create_version\": {\"type\": \"integer\"}, \"extract_version\": {\"type\": \"integer\"}, \"flag_bits\": {\"type\": \"integer\"}, \"volume\": {\"type\": \"integer\"}, \"internal_attr\": {\"type\": \"integer\"}, \"external_attr\": {\"type\": \"integer\"}, \"header_offset\": {\"type\": \"integer\"}, \"CRC\": {\"type\": \"integer\"}, \"compress_size\": {\"type\": \"integer\"}, \"file_size\": {\"type\": \"integer\"}}}, \"content\": {\"type\": \"string\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "023044a4-f71f-4768-87f3-aad822d53723",
      "version": 5,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 81
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Zip Extract to Artifact",
          "object_type": "attachment",
          "programmatic_name": "example_soar_utilities_zip_extract_to_artifact",
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815247,
      "name": "soar_utils_attachment_zip_list",
      "output_json_example": "{\"namelist\": [\"fn_slack-2.0.0.tar.gz\", \"app.json\", \"export.res\"], \"infolist\": [{\"filename\": \"fn_slack-2.0.0.tar.gz\", \"date_time\": 1661452332000, \"compress_type\": 8, \"comment\": \"\", \"create_system\": 3, \"create_version\": 20, \"extract_version\": 20, \"flag_bits\": 0, \"volume\": 0, \"internal_attr\": 0, \"external_attr\": 2175008768, \"header_offset\": 0, \"CRC\": 2624755629, \"compress_size\": 563006, \"file_size\": 562852}, {\"filename\": \"app.json\", \"date_time\": 1661452332000, \"compress_type\": 8, \"comment\": \"\", \"create_system\": 3, \"create_version\": 20, \"extract_version\": 20, \"flag_bits\": 0, \"volume\": 0, \"internal_attr\": 0, \"external_attr\": 2175008768, \"header_offset\": 563057, \"CRC\": 3145654620, \"compress_size\": 25265, \"file_size\": 33851}, {\"filename\": \"export.res\", \"date_time\": 1661452332000, \"compress_type\": 8, \"comment\": \"\", \"create_system\": 3, \"create_version\": 20, \"extract_version\": 20, \"flag_bits\": 0, \"volume\": 0, \"internal_attr\": 0, \"external_attr\": 2175008768, \"header_offset\": 588360, \"CRC\": 1492648105, \"compress_size\": 10780, \"file_size\": 101541}]}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"namelist\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"infolist\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"date_time\": {\"type\": \"integer\"}, \"compress_type\": {\"type\": \"integer\"}, \"comment\": {\"type\": \"string\"}, \"create_system\": {\"type\": \"integer\"}, \"create_version\": {\"type\": \"integer\"}, \"extract_version\": {\"type\": \"integer\"}, \"flag_bits\": {\"type\": \"integer\"}, \"volume\": {\"type\": \"integer\"}, \"internal_attr\": {\"type\": \"integer\"}, \"external_attr\": {\"type\": \"integer\"}, \"header_offset\": {\"type\": \"integer\"}, \"CRC\": {\"type\": \"integer\"}, \"compress_size\": {\"type\": \"integer\"}, \"file_size\": {\"type\": \"integer\"}}}}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "a111dc9b-9ea4-42a2-8590-23ca399d8387",
      "version": 4,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815285,
      "name": "soar_utils_base64_to_artifact",
      "output_json_example": "{\"id\": 547, \"type\": 7, \"value\": \"export.res.b64\", \"description\": null, \"attachment\": {\"type\": \"artifact\", \"id\": 71, \"uuid\": \"b2fb5c8f-92f8-46a8-a2a8-8b9342a1bb64\", \"name\": \"tmppe_6ed00\", \"content_type\": \"image/jpeg\", \"created\": 1663775473887, \"creator_id\": 6, \"size\": 180520, \"actions\": [{\"id\": 33, \"name\": \"Example: Virus Total for Attachments\", \"enabled\": true}, {\"id\": 34, \"name\": \"Example: Google Cloud - Inspect Attachment for PII\", \"enabled\": true}, {\"id\": 35, \"name\": \"Example: Google Cloud - Remove PII from Attachment\", \"enabled\": true}, {\"id\": 47, \"name\": \"Example: Attachment Hash\", \"enabled\": true}, {\"id\": 48, \"name\": \"Example: Attachment to Base64\", \"enabled\": true}, {\"id\": 52, \"name\": \"Example: Email Parsing (Attachment)\", \"enabled\": true}, {\"id\": 41, \"name\": \"Example: Post Incident / Task Attachment to Slack\", \"enabled\": true}, {\"id\": 85, \"name\": \"Example: SOAR Utilities Attachment Hash\", \"enabled\": true}, {\"id\": 87, \"name\": \"Example: SOAR Utilities Attachment to Base64\", \"enabled\": true}, {\"id\": 59, \"name\": \"Example: PDFiD\", \"enabled\": true}, {\"id\": 60, \"name\": \"Example: Resilient Search\", \"enabled\": true}, {\"id\": 90, \"name\": \"Example: SOAR Utilities SOAR Search\", \"enabled\": true}, {\"id\": 65, \"name\": \"Example: Use Excel Data\", \"enabled\": false}, {\"id\": 67, \"name\": \"Example: Zip Extract\", \"enabled\": false}, {\"id\": 68, \"name\": \"Example: Zip List\", \"enabled\": false}, {\"id\": 96, \"name\": \"Example: SOAR Utilities Zip List\", \"enabled\": false}, {\"id\": 95, \"name\": \"Example: SOAR Utilities Zip Extract\", \"enabled\": false}, {\"id\": 97, \"name\": \"Example: SOAR Utilities Zip Extract to Artifact\", \"enabled\": false}], \"playbooks\": [], \"task_id\": null, \"task_name\": null, \"task_custom\": null, \"task_members\": null, \"task_at_id\": null, \"vers\": 12, \"inc_id\": 2112, \"inc_name\": \"SOAR Utilities\", \"inc_owner\": 1}, \"parent_id\": null, \"inc_id\": 2112, \"inc_name\": \"SOAR Utilities\", \"inc_owner\": 1, \"hits\": [], \"created\": 1663775473530, \"last_modified_time\": 1663775473899, \"last_modified_by\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Integration Server v43\"}, \"pending_sources\": [], \"perms\": null, \"properties\": null, \"actions\": [], \"playbooks\": [], \"hash\": \"c670630c6c19434d3d62b9f6e800bffd4cf5d5c361d64c8c92c628f1aba368ee\", \"relating\": true, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Integration Server v43\"}, \"related_incident_count\": null, \"pending_scan_result\": false, \"global_info\": null, \"ip\": {\"source\": null, \"destination\": null}, \"global_artifact\": []}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}, \"description\": {}, \"attachment\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"uuid\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"created\": {\"type\": \"integer\"}, \"creator_id\": {\"type\": \"integer\"}, \"size\": {\"type\": \"integer\"}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"playbooks\": {\"type\": \"array\"}, \"task_id\": {}, \"task_name\": {}, \"task_custom\": {}, \"task_members\": {}, \"task_at_id\": {}, \"vers\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}}}, \"parent_id\": {}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}, \"hits\": {\"type\": \"array\"}, \"created\": {\"type\": \"integer\"}, \"last_modified_time\": {\"type\": \"integer\"}, \"last_modified_by\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"pending_sources\": {\"type\": \"array\"}, \"perms\": {}, \"properties\": {}, \"actions\": {\"type\": \"array\"}, \"playbooks\": {\"type\": \"array\"}, \"hash\": {\"type\": \"string\"}, \"relating\": {\"type\": \"boolean\"}, \"creator_principal\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"related_incident_count\": {}, \"pending_scan_result\": {\"type\": \"boolean\"}, \"global_info\": {}, \"ip\": {\"type\": \"object\", \"properties\": {\"source\": {}, \"destination\": {}}}, \"global_artifact\": {\"type\": \"array\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "2710d4db-7c32-42cc-a264-1f0e66a64826",
      "version": 5,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815324,
      "name": "soar_utils_base64_to_attachment",
      "output_json_example": "{\"type\": \"incident\", \"id\": 70, \"uuid\": \"999c463c-4382-4435-9b3e-663f166080a8\", \"name\": \"export.res.b64\", \"content_type\": \"image/jpeg\", \"created\": 1663772427768, \"creator_id\": 6, \"size\": 101541, \"actions\": [{\"id\": 33, \"name\": \"Example: Virus Total for Attachments\", \"enabled\": true}, {\"id\": 34, \"name\": \"Example: Google Cloud - Inspect Attachment for PII\", \"enabled\": true}, {\"id\": 35, \"name\": \"Example: Google Cloud - Remove PII from Attachment\", \"enabled\": true}, {\"id\": 47, \"name\": \"Example: Attachment Hash\", \"enabled\": true}, {\"id\": 48, \"name\": \"Example: Attachment to Base64\", \"enabled\": true}, {\"id\": 52, \"name\": \"Example: Email Parsing (Attachment)\", \"enabled\": true}, {\"id\": 41, \"name\": \"Example: Post Incident / Task Attachment to Slack\", \"enabled\": true}, {\"id\": 85, \"name\": \"Example: SOAR Utilities Attachment Hash\", \"enabled\": true}, {\"id\": 87, \"name\": \"Example: SOAR Utilities Attachment to Base64\", \"enabled\": true}, {\"id\": 59, \"name\": \"Example: PDFiD\", \"enabled\": true}, {\"id\": 60, \"name\": \"Example: Resilient Search\", \"enabled\": true}, {\"id\": 90, \"name\": \"Example: SOAR Utilities SOAR Search\", \"enabled\": true}, {\"id\": 65, \"name\": \"Example: Use Excel Data\", \"enabled\": false}, {\"id\": 67, \"name\": \"Example: Zip Extract\", \"enabled\": false}, {\"id\": 68, \"name\": \"Example: Zip List\", \"enabled\": false}, {\"id\": 96, \"name\": \"Example: SOAR Utilities Zip List\", \"enabled\": false}, {\"id\": 95, \"name\": \"Example: SOAR Utilities Zip Extract\", \"enabled\": false}], \"playbooks\": [], \"task_id\": null, \"task_name\": null, \"task_custom\": null, \"task_members\": null, \"task_at_id\": null, \"vers\": 11, \"inc_id\": 2112, \"inc_name\": \"SOAR Utilities\", \"inc_owner\": 1}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"uuid\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"content_type\": {\"type\": \"string\"}, \"created\": {\"type\": \"integer\"}, \"creator_id\": {\"type\": \"integer\"}, \"size\": {\"type\": \"integer\"}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"playbooks\": {\"type\": \"array\"}, \"task_id\": {}, \"task_name\": {}, \"task_custom\": {}, \"task_members\": {}, \"task_at_id\": {}, \"vers\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"integer\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "337c083e-2c30-4907-8000-0b9a4496154b",
      "version": 5,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815366,
      "name": "soar_utils_close_incident",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"title\": null, \"message\": null, \"hints\": []}, \"raw\": \"{\\\"success\\\": true, \\\"title\\\": null, \\\"message\\\": null, \\\"hints\\\": []}\", \"inputs\": {\"incident_id\": 2114, \"soar_utils_close_fields\": \"{\\\"resolution_id\\\":\\\"Resolved\\\",\\\"resolution_summary\\\":\\\"closing\\\"}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-soar-utils\", \"package_version\": \"1.0.0\", \"host\": \"Christophers-MacBook-Pro-2.local\", \"execution_time_ms\": 1781, \"timestamp\": \"2022-09-19 14:00:50\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"title\": {}, \"message\": {}, \"hints\": {\"type\": \"array\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"soar_utils_close_fields\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "836a3505-3306-4eda-9703-6297fad907da",
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815408,
      "name": "soar_utils_create_incident",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"dtm\": {}, \"cm\": {\"unassigneds\": [], \"total\": 0, \"geo_counts\": {}}, \"regulators\": {\"ids\": []}, \"hipaa\": {\"hipaa_adverse\": null, \"hipaa_misused\": null, \"hipaa_acquired\": null, \"hipaa_additional_misuse\": null, \"hipaa_breach\": null, \"hipaa_adverse_comment\": null, \"hipaa_misused_comment\": null, \"hipaa_acquired_comment\": null, \"hipaa_additional_misuse_comment\": null, \"hipaa_breach_comment\": null}, \"tasks\": null, \"artifacts\": null, \"name\": \"Create Incident\", \"description\": \"Testing\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_incident_id\": null, \"sdlp_policy_group_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663297953098, \"comments\": null, \"actions\": [{\"id\": 69, \"name\": \"Timer Epoch\", \"enabled\": true}, {\"id\": 70, \"name\": \"Timer in Parallel\", \"enabled\": true}, {\"id\": 72, \"name\": \"Symantec DLP: Get DLP Notes\", \"enabled\": false}, {\"id\": 37, \"name\": \"Example: Archive Incident Slack Channel\", \"enabled\": true}, {\"id\": 42, \"name\": \"Example: Post Incident to Slack\", \"enabled\": true}, {\"id\": 75, \"name\": \"Symantec DLP: Update DLP Incident\", \"enabled\": false}, {\"id\": 78, \"name\": \"Symantec DLP: Upload Binaries as Artifact\", \"enabled\": false}, {\"id\": 79, \"name\": \"Symantec DLP: Write DLP Incident Details to Note\", \"enabled\": false}, {\"id\": 81, \"name\": \"Example: Close Incident\", \"enabled\": true}, {\"id\": 82, \"name\": \"Example: Create Incident\", \"enabled\": true}, {\"id\": 83, \"name\": \"Example: Search Incidents\", \"enabled\": true}, {\"id\": 55, \"name\": \"Example: Get Incident Contact Info\", \"enabled\": true}, {\"id\": 88, \"name\": \"Example: SOAR Utilities Close Incident\", \"enabled\": true}, {\"id\": 89, \"name\": \"Example: SOAR Utilities Create Incident\", \"enabled\": true}, {\"id\": 91, \"name\": \"Example: SOAR Utilities Get Incident Contact Info\", \"enabled\": true}, {\"id\": 63, \"name\": \"Example: Timer Epoch\", \"enabled\": true}, {\"id\": 64, \"name\": \"Example: Timers in Parallel\", \"enabled\": true}, {\"id\": 93, \"name\": \"Example: SOAR Utilities Search Incidents\", \"enabled\": true}], \"playbooks\": [{\"playbook_handle\": 1, \"display_name\": \"TImer\"}], \"timer_field_summarized_incident_data\": [], \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2114, \"sequence_code\": null, \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663297952673, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"A\"}, \"raw\": \"{\\\"dtm\\\": {}, \\\"cm\\\": {\\\"unassigneds\\\": [], \\\"total\\\": 0, \\\"geo_counts\\\": {}}, \\\"regulators\\\": {\\\"ids\\\": []}, \\\"hipaa\\\": {\\\"hipaa_adverse\\\": null, \\\"hipaa_misused\\\": null, \\\"hipaa_acquired\\\": null, \\\"hipaa_additional_misuse\\\": null, \\\"hipaa_breach\\\": null, \\\"hipaa_adverse_comment\\\": null, \\\"hipaa_misused_comment\\\": null, \\\"hipaa_acquired_comment\\\": null, \\\"hipaa_additional_misuse_comment\\\": null, \\\"hipaa_breach_comment\\\": null}, \\\"tasks\\\": null, \\\"artifacts\\\": null, \\\"name\\\": \\\"Create Incident\\\", \\\"description\\\": \\\"Testing\\\", \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": null, \\\"creator_principal\\\": {\\\"id\\\": 6, \\\"type\\\": \\\"apikey\\\", \\\"name\\\": \\\"0228e00e-2c47-43e6-a736-550f104c94ea\\\", \\\"display_name\\\": \\\"Chris\u0027 Integration Server v43\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": false, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_incident_id\\\": null, \\\"sdlp_policy_group_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1621110044000, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1663297953098, \\\"comments\\\": null, \\\"actions\\\": [{\\\"id\\\": 69, \\\"name\\\": \\\"Timer Epoch\\\", \\\"enabled\\\": true}, {\\\"id\\\": 70, \\\"name\\\": \\\"Timer in Parallel\\\", \\\"enabled\\\": true}, {\\\"id\\\": 72, \\\"name\\\": \\\"Symantec DLP: Get DLP Notes\\\", \\\"enabled\\\": false}, {\\\"id\\\": 37, \\\"name\\\": \\\"Example: Archive Incident Slack Channel\\\", \\\"enabled\\\": true}, {\\\"id\\\": 42, \\\"name\\\": \\\"Example: Post Incident to Slack\\\", \\\"enabled\\\": true}, {\\\"id\\\": 75, \\\"name\\\": \\\"Symantec DLP: Update DLP Incident\\\", \\\"enabled\\\": false}, {\\\"id\\\": 78, \\\"name\\\": \\\"Symantec DLP: Upload Binaries as Artifact\\\", \\\"enabled\\\": false}, {\\\"id\\\": 79, \\\"name\\\": \\\"Symantec DLP: Write DLP Incident Details to Note\\\", \\\"enabled\\\": false}, {\\\"id\\\": 81, \\\"name\\\": \\\"Example: Close Incident\\\", \\\"enabled\\\": true}, {\\\"id\\\": 82, \\\"name\\\": \\\"Example: Create Incident\\\", \\\"enabled\\\": true}, {\\\"id\\\": 83, \\\"name\\\": \\\"Example: Search Incidents\\\", \\\"enabled\\\": true}, {\\\"id\\\": 55, \\\"name\\\": \\\"Example: Get Incident Contact Info\\\", \\\"enabled\\\": true}, {\\\"id\\\": 88, \\\"name\\\": \\\"Example: SOAR Utilities Close Incident\\\", \\\"enabled\\\": true}, {\\\"id\\\": 89, \\\"name\\\": \\\"Example: SOAR Utilities Create Incident\\\", \\\"enabled\\\": true}, {\\\"id\\\": 91, \\\"name\\\": \\\"Example: SOAR Utilities Get Incident Contact Info\\\", \\\"enabled\\\": true}, {\\\"id\\\": 63, \\\"name\\\": \\\"Example: Timer Epoch\\\", \\\"enabled\\\": true}, {\\\"id\\\": 64, \\\"name\\\": \\\"Example: Timers in Parallel\\\", \\\"enabled\\\": true}, {\\\"id\\\": 93, \\\"name\\\": \\\"Example: SOAR Utilities Search Incidents\\\", \\\"enabled\\\": true}], \\\"playbooks\\\": [{\\\"playbook_handle\\\": 1, \\\"display_name\\\": \\\"TImer\\\"}], \\\"timer_field_summarized_incident_data\\\": [], \\\"admin_id\\\": null, \\\"creator_id\\\": 6, \\\"crimestatus_id\\\": 1, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2114, \\\"sequence_code\\\": null, \\\"discovered_date\\\": 1621110044000, \\\"due_date\\\": null, \\\"create_date\\\": 1663297952673, \\\"owner_id\\\": 3, \\\"severity_code\\\": null, \\\"plan_status\\\": \\\"A\\\"}\", \"inputs\": {\"soar_utils_create_fields\": \"{\\\"name\\\":\\\"Create Incident\\\",\\\"description\\\":\\\"Testing\\\",\\\"discovered_date\\\":1621110044000}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-soar-utils\", \"package_version\": \"1.0.0\", \"host\": \"Christophers-MacBook-Pro-2.local\", \"execution_time_ms\": 1705, \"timestamp\": \"2022-09-15 23:12:33\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"dtm\": {\"type\": \"object\"}, \"cm\": {\"type\": \"object\", \"properties\": {\"unassigneds\": {\"type\": \"array\"}, \"total\": {\"type\": \"integer\"}, \"geo_counts\": {\"type\": \"object\"}}}, \"regulators\": {\"type\": \"object\", \"properties\": {\"ids\": {\"type\": \"array\"}}}, \"hipaa\": {\"type\": \"object\", \"properties\": {\"hipaa_adverse\": {}, \"hipaa_misused\": {}, \"hipaa_acquired\": {}, \"hipaa_additional_misuse\": {}, \"hipaa_breach\": {}, \"hipaa_adverse_comment\": {}, \"hipaa_misused_comment\": {}, \"hipaa_acquired_comment\": {}, \"hipaa_additional_misuse_comment\": {}, \"hipaa_breach_comment\": {}}}, \"tasks\": {}, \"artifacts\": {}, \"name\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"phase_id\": {\"type\": \"integer\"}, \"inc_training\": {\"type\": \"boolean\"}, \"vers\": {\"type\": \"integer\"}, \"addr\": {}, \"city\": {}, \"creator\": {}, \"creator_principal\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"exposure_type_id\": {\"type\": \"integer\"}, \"incident_type_ids\": {\"type\": \"array\"}, \"reporter\": {}, \"state\": {}, \"country\": {}, \"zip\": {}, \"workspace\": {\"type\": \"integer\"}, \"exposure\": {\"type\": \"integer\"}, \"org_handle\": {\"type\": \"integer\"}, \"members\": {\"type\": \"array\"}, \"negative_pr_likely\": {}, \"perms\": {\"type\": \"object\", \"properties\": {\"read\": {\"type\": \"boolean\"}, \"write\": {\"type\": \"boolean\"}, \"comment\": {\"type\": \"boolean\"}, \"assign\": {\"type\": \"boolean\"}, \"close\": {\"type\": \"boolean\"}, \"change_members\": {\"type\": \"boolean\"}, \"attach_file\": {\"type\": \"boolean\"}, \"read_attachments\": {\"type\": \"boolean\"}, \"delete_attachments\": {\"type\": \"boolean\"}, \"create_milestones\": {\"type\": \"boolean\"}, \"list_milestones\": {\"type\": \"boolean\"}, \"create_artifacts\": {\"type\": \"boolean\"}, \"list_artifacts\": {\"type\": \"boolean\"}, \"delete\": {\"type\": \"boolean\"}, \"change_workspace\": {\"type\": \"boolean\"}}}, \"confirmed\": {\"type\": \"boolean\"}, \"task_changes\": {\"type\": \"object\", \"properties\": {\"added\": {\"type\": \"array\"}, \"removed\": {\"type\": \"array\"}}}, \"assessment\": {\"type\": \"string\"}, \"data_compromised\": {}, \"draft\": {\"type\": \"boolean\"}, \"properties\": {\"type\": \"object\", \"properties\": {\"sdlp_policy_name\": {}, \"sdlp_policy_group_name\": {}, \"sdlp_policy_id\": {}, \"sdlp_incident_status\": {}, \"sdlp_incident_url\": {}, \"internal_customizations_field\": {}, \"sdlp_incident_id\": {}, \"sdlp_policy_group_id\": {}}}, \"resolution_id\": {}, \"resolution_summary\": {}, \"pii\": {\"type\": \"object\", \"properties\": {\"data_compromised\": {}, \"determined_date\": {\"type\": \"integer\"}, \"harmstatus_id\": {\"type\": \"integer\"}, \"data_encrypted\": {}, \"data_contained\": {}, \"impact_likely\": {}, \"ny_impact_likely\": {}, \"or_impact_likely\": {}, \"wa_impact_likely\": {}, \"dc_impact_likely\": {}, \"data_source_ids\": {\"type\": \"array\"}, \"data_format\": {}, \"assessment\": {\"type\": \"string\"}, \"exposure\": {\"type\": \"integer\"}, \"gdpr_harm_risk\": {}, \"gdpr_lawful_data_processing_categories\": {\"type\": \"array\"}, \"alberta_health_risk_assessment\": {}, \"california_health_risk_assessment\": {}, \"new_zealand_risk_assessment\": {}, \"singapore_risk_assessment\": {}}}, \"gdpr\": {\"type\": \"object\", \"properties\": {\"gdpr_breach_circumstances\": {\"type\": \"array\"}, \"gdpr_breach_type\": {}, \"gdpr_personal_data\": {}, \"gdpr_identification\": {}, \"gdpr_consequences\": {}, \"gdpr_final_assessment\": {}, \"gdpr_breach_type_comment\": {}, \"gdpr_personal_data_comment\": {}, \"gdpr_identification_comment\": {}, \"gdpr_consequences_comment\": {}, \"gdpr_final_assessment_comment\": {}, \"gdpr_subsequent_notification\": {}}}, \"regulator_risk\": {\"type\": \"object\"}, \"inc_last_modified_date\": {\"type\": \"integer\"}, \"comments\": {}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"playbooks\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"playbook_handle\": {\"type\": \"integer\"}, \"display_name\": {\"type\": \"string\"}}}}, \"timer_field_summarized_incident_data\": {\"type\": \"array\"}, \"admin_id\": {}, \"creator_id\": {\"type\": \"integer\"}, \"crimestatus_id\": {\"type\": \"integer\"}, \"employee_involved\": {}, \"end_date\": {}, \"exposure_dept_id\": {}, \"exposure_individual_name\": {}, \"exposure_vendor_id\": {}, \"jurisdiction_name\": {}, \"jurisdiction_reg_id\": {}, \"start_date\": {}, \"inc_start\": {}, \"org_id\": {\"type\": \"integer\"}, \"is_scenario\": {\"type\": \"boolean\"}, \"hard_liability\": {\"type\": \"integer\"}, \"nist_attack_vectors\": {\"type\": \"array\"}, \"id\": {\"type\": \"integer\"}, \"sequence_code\": {}, \"discovered_date\": {\"type\": \"integer\"}, \"due_date\": {}, \"create_date\": {\"type\": \"integer\"}, \"owner_id\": {\"type\": \"integer\"}, \"severity_code\": {}, \"plan_status\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"soar_utils_create_fields\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "c6f170f3-61f6-4a46-a397-f2b3ae095be4",
      "version": 5,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815451,
      "name": "soar_utils_get_contact_info",
      "output_json_example": "{\"owner\": {\"fname\": \"Admin\", \"lname\": \"User\", \"title\": \"\", \"display_name\": \"Admin User\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\"}, \"members\": []}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"owner\": {\"type\": \"object\", \"properties\": {\"fname\": {\"type\": \"string\"}, \"lname\": {\"type\": \"string\"}, \"title\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}, \"email\": {\"type\": \"string\"}, \"phone\": {\"type\": \"string\"}, \"cell\": {\"type\": \"string\"}}}, \"members\": {\"type\": \"array\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "7edb9444-2b81-4756-8fbe-3483cdafb9eb",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Get Incident Contact Info",
          "object_type": "incident",
          "programmatic_name": "example_soar_utilities_get_incident_contact_info",
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 86
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: SOAR Utilities Get Task Contact Info",
          "object_type": "task",
          "programmatic_name": "example_soar_utilities_get_task_contact_info",
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815493,
      "name": "soar_utils_search_incidents",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"recordsTotal\": 17, \"recordsFiltered\": 17, \"data\": [{\"name\": \"AbuseIPDB\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1643922138662, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647529122634, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2095, \"sequence_code\": \"E2E5-1\", \"discovered_date\": 1643922138662, \"due_date\": null, \"create_date\": 1643922148213, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"GoogleSafeBrowsing\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1645039833651, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647461667230, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2096, \"sequence_code\": \"E2E5-2\", \"discovered_date\": 1645039833651, \"due_date\": null, \"create_date\": 1645039847583, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"PassiveTotal\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1646103998739, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647974941312, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2097, \"sequence_code\": \"E2E5-3\", \"discovered_date\": 1646103998739, \"due_date\": null, \"create_date\": 1646142354974, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"ShadowServer\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1647975098216, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1653512178112, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2098, \"sequence_code\": \"E2E5-4\", \"discovered_date\": 1647975098216, \"due_date\": null, \"create_date\": 1647975111873, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Yeti\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1648839797719, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1649700668706, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2099, \"sequence_code\": \"E2E5-5\", \"discovered_date\": 1648839797719, \"due_date\": null, \"create_date\": 1648839806477, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"hibp\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1649858935196, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1651092229697, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2100, \"sequence_code\": \"E2E5-6\", \"discovered_date\": 1649858935196, \"due_date\": null, \"create_date\": 1649858943997, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"VirusTotal\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 4, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1651000728764, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1653580063528, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2101, \"sequence_code\": \"E2E5-7\", \"discovered_date\": 1651000728764, \"due_date\": null, \"create_date\": 1651000737927, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"URLScan.io\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 74, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1651264262077, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1652814527143, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2102, \"sequence_code\": \"E2E5-8\", \"discovered_date\": 1651264262077, \"due_date\": null, \"create_date\": 1651264273600, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Google Cloud DLP\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 12, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1655912228120, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1655924984252, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2103, \"sequence_code\": \"E2E5-9\", \"discovered_date\": 1655912228120, \"due_date\": null, \"create_date\": 1655912245009, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Slack\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 16, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1656527528505, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661269393325, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2104, \"sequence_code\": \"E2E5-10\", \"discovered_date\": 1656527528505, \"due_date\": null, \"create_date\": 1656527541659, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"New Slack\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 4, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1660155959409, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661281207911, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2107, \"sequence_code\": \"E2E5-13\", \"discovered_date\": 1660155959409, \"due_date\": null, \"create_date\": 1660155971260, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Slack2\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 6, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1660245674318, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661280682539, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2108, \"sequence_code\": \"E2E5-14\", \"discovered_date\": 1660245674318, \"due_date\": null, \"create_date\": 1660245680733, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"debug incident\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 13, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1661346194202, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661447571753, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2110, \"sequence_code\": \"E2E5-16\", \"discovered_date\": 1661346194202, \"due_date\": null, \"create_date\": 1661346206429, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Timer\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1661800148708, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1662747629777, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2111, \"sequence_code\": \"E2E5-17\", \"discovered_date\": 1661800148708, \"due_date\": null, \"create_date\": 1661800169751, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"SOAR Utilities\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 7, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1663093285999, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663699613661, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2112, \"sequence_code\": \"E2E5-18\", \"discovered_date\": 1663093285999, \"due_date\": null, \"create_date\": 1663093296645, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"SOAR Utils\", \"description\": \"Test\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663613729686, \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2113, \"sequence_code\": \"E2E5-19\", \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663188001122, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"A\"}, {\"name\": \"Create Incident\", \"description\": \"Testing\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 3, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_incident_id\": null, \"sdlp_policy_group_id\": null}, \"resolution_id\": 10, \"resolution_summary\": \"closing\", \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663610451616, \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": 1663610449718, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2114, \"sequence_code\": \"E2E5-20\", \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663297952673, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"C\"}]}, \"raw\": \"{\\\"recordsTotal\\\": 17, \\\"recordsFiltered\\\": 17, \\\"data\\\": [{\\\"name\\\": \\\"AbuseIPDB\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1643922138662, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1647529122634, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2095, \\\"sequence_code\\\": \\\"E2E5-1\\\", \\\"discovered_date\\\": 1643922138662, \\\"due_date\\\": null, \\\"create_date\\\": 1643922148213, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"GoogleSafeBrowsing\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1645039833651, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1647461667230, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2096, \\\"sequence_code\\\": \\\"E2E5-2\\\", \\\"discovered_date\\\": 1645039833651, \\\"due_date\\\": null, \\\"create_date\\\": 1645039847583, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"PassiveTotal\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1646103998739, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1647974941312, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2097, \\\"sequence_code\\\": \\\"E2E5-3\\\", \\\"discovered_date\\\": 1646103998739, \\\"due_date\\\": null, \\\"create_date\\\": 1646142354974, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"ShadowServer\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1647975098216, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1653512178112, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2098, \\\"sequence_code\\\": \\\"E2E5-4\\\", \\\"discovered_date\\\": 1647975098216, \\\"due_date\\\": null, \\\"create_date\\\": 1647975111873, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Yeti\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1648839797719, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1649700668706, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2099, \\\"sequence_code\\\": \\\"E2E5-5\\\", \\\"discovered_date\\\": 1648839797719, \\\"due_date\\\": null, \\\"create_date\\\": 1648839806477, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"hibp\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1649858935196, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1651092229697, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2100, \\\"sequence_code\\\": \\\"E2E5-6\\\", \\\"discovered_date\\\": 1649858935196, \\\"due_date\\\": null, \\\"create_date\\\": 1649858943997, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"VirusTotal\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 4, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1651000728764, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1653580063528, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2101, \\\"sequence_code\\\": \\\"E2E5-7\\\", \\\"discovered_date\\\": 1651000728764, \\\"due_date\\\": null, \\\"create_date\\\": 1651000737927, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"URLScan.io\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 74, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1651264262077, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1652814527143, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2102, \\\"sequence_code\\\": \\\"E2E5-8\\\", \\\"discovered_date\\\": 1651264262077, \\\"due_date\\\": null, \\\"create_date\\\": 1651264273600, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Google Cloud DLP\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 12, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1655912228120, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1655924984252, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2103, \\\"sequence_code\\\": \\\"E2E5-9\\\", \\\"discovered_date\\\": 1655912228120, \\\"due_date\\\": null, \\\"create_date\\\": 1655912245009, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Slack\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 16, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1656527528505, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1661269393325, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2104, \\\"sequence_code\\\": \\\"E2E5-10\\\", \\\"discovered_date\\\": 1656527528505, \\\"due_date\\\": null, \\\"create_date\\\": 1656527541659, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"New Slack\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 4, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1660155959409, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1661281207911, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2107, \\\"sequence_code\\\": \\\"E2E5-13\\\", \\\"discovered_date\\\": 1660155959409, \\\"due_date\\\": null, \\\"create_date\\\": 1660155971260, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Slack2\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 6, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1660245674318, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1661280682539, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2108, \\\"sequence_code\\\": \\\"E2E5-14\\\", \\\"discovered_date\\\": 1660245674318, \\\"due_date\\\": null, \\\"create_date\\\": 1660245680733, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"debug incident\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 13, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1661346194202, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1661447571753, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2110, \\\"sequence_code\\\": \\\"E2E5-16\\\", \\\"discovered_date\\\": 1661346194202, \\\"due_date\\\": null, \\\"create_date\\\": 1661346206429, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Timer\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1661800148708, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1662747629777, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2111, \\\"sequence_code\\\": \\\"E2E5-17\\\", \\\"discovered_date\\\": 1661800148708, \\\"due_date\\\": null, \\\"create_date\\\": 1661800169751, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"SOAR Utilities\\\", \\\"description\\\": null, \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 7, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": {\\\"id\\\": 1, \\\"fname\\\": \\\"Admin\\\", \\\"lname\\\": \\\"User\\\", \\\"display_name\\\": \\\"Admin User\\\", \\\"status\\\": \\\"A\\\", \\\"email\\\": \\\"admin@example.com\\\", \\\"phone\\\": \\\"\\\", \\\"cell\\\": \\\"\\\", \\\"title\\\": \\\"\\\", \\\"locked\\\": false, \\\"password_changed\\\": false, \\\"is_external\\\": false, \\\"ui_theme\\\": \\\"verydarkmode\\\", \\\"is_ldap\\\": false, \\\"is_saml\\\": false}, \\\"creator_principal\\\": {\\\"id\\\": 1, \\\"type\\\": \\\"user\\\", \\\"name\\\": \\\"admin@example.com\\\", \\\"display_name\\\": \\\"Admin User\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": true, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1663093285999, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1663699613661, \\\"admin_id\\\": null, \\\"creator_id\\\": 1, \\\"crimestatus_id\\\": 5, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2112, \\\"sequence_code\\\": \\\"E2E5-18\\\", \\\"discovered_date\\\": 1663093285999, \\\"due_date\\\": null, \\\"create_date\\\": 1663093296645, \\\"owner_id\\\": 1, \\\"severity_code\\\": 4, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"SOAR Utils\\\", \\\"description\\\": \\\"Test\\\", \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 2, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": null, \\\"creator_principal\\\": {\\\"id\\\": 6, \\\"type\\\": \\\"apikey\\\", \\\"name\\\": \\\"0228e00e-2c47-43e6-a736-550f104c94ea\\\", \\\"display_name\\\": \\\"Chris\u0027 Integration Server v43\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": false, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_policy_group_id\\\": null, \\\"sdlp_incident_id\\\": null}, \\\"resolution_id\\\": null, \\\"resolution_summary\\\": null, \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1621110044000, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1663613729686, \\\"admin_id\\\": null, \\\"creator_id\\\": 6, \\\"crimestatus_id\\\": 1, \\\"employee_involved\\\": null, \\\"end_date\\\": null, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2113, \\\"sequence_code\\\": \\\"E2E5-19\\\", \\\"discovered_date\\\": 1621110044000, \\\"due_date\\\": null, \\\"create_date\\\": 1663188001122, \\\"owner_id\\\": 3, \\\"severity_code\\\": null, \\\"plan_status\\\": \\\"A\\\"}, {\\\"name\\\": \\\"Create Incident\\\", \\\"description\\\": \\\"Testing\\\", \\\"phase_id\\\": 1000, \\\"inc_training\\\": false, \\\"vers\\\": 3, \\\"addr\\\": null, \\\"city\\\": null, \\\"creator\\\": null, \\\"creator_principal\\\": {\\\"id\\\": 6, \\\"type\\\": \\\"apikey\\\", \\\"name\\\": \\\"0228e00e-2c47-43e6-a736-550f104c94ea\\\", \\\"display_name\\\": \\\"Chris\u0027 Integration Server v43\\\"}, \\\"exposure_type_id\\\": 1, \\\"incident_type_ids\\\": [], \\\"reporter\\\": null, \\\"state\\\": null, \\\"country\\\": null, \\\"zip\\\": null, \\\"workspace\\\": 1, \\\"exposure\\\": 0, \\\"org_handle\\\": 201, \\\"members\\\": [], \\\"negative_pr_likely\\\": null, \\\"perms\\\": {\\\"read\\\": true, \\\"write\\\": true, \\\"comment\\\": true, \\\"assign\\\": true, \\\"close\\\": true, \\\"change_members\\\": true, \\\"attach_file\\\": true, \\\"read_attachments\\\": true, \\\"delete_attachments\\\": true, \\\"create_milestones\\\": true, \\\"list_milestones\\\": true, \\\"create_artifacts\\\": true, \\\"list_artifacts\\\": true, \\\"delete\\\": true, \\\"change_workspace\\\": true}, \\\"confirmed\\\": false, \\\"task_changes\\\": {\\\"added\\\": [], \\\"removed\\\": []}, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"data_compromised\\\": null, \\\"draft\\\": false, \\\"properties\\\": {\\\"sdlp_policy_name\\\": null, \\\"sdlp_policy_group_name\\\": null, \\\"sdlp_policy_id\\\": null, \\\"sdlp_incident_status\\\": null, \\\"sdlp_incident_url\\\": null, \\\"internal_customizations_field\\\": null, \\\"sdlp_incident_id\\\": null, \\\"sdlp_policy_group_id\\\": null}, \\\"resolution_id\\\": 10, \\\"resolution_summary\\\": \\\"closing\\\", \\\"pii\\\": {\\\"data_compromised\\\": null, \\\"determined_date\\\": 1621110044000, \\\"harmstatus_id\\\": 2, \\\"data_encrypted\\\": null, \\\"data_contained\\\": null, \\\"impact_likely\\\": null, \\\"ny_impact_likely\\\": null, \\\"or_impact_likely\\\": null, \\\"wa_impact_likely\\\": null, \\\"dc_impact_likely\\\": null, \\\"data_source_ids\\\": [], \\\"data_format\\\": null, \\\"assessment\\\": \\\"\u003c?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\" standalone=\\\\\\\"yes\\\\\\\"?\u003e\\\\n\u003cassessment\u003e\\\\n    \u003crollups/\u003e\\\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\\\n\u003c/assessment\u003e\\\\n\\\", \\\"exposure\\\": 0, \\\"gdpr_harm_risk\\\": null, \\\"gdpr_lawful_data_processing_categories\\\": [], \\\"alberta_health_risk_assessment\\\": null, \\\"california_health_risk_assessment\\\": null, \\\"new_zealand_risk_assessment\\\": null, \\\"singapore_risk_assessment\\\": null}, \\\"gdpr\\\": {\\\"gdpr_breach_circumstances\\\": [], \\\"gdpr_breach_type\\\": null, \\\"gdpr_personal_data\\\": null, \\\"gdpr_identification\\\": null, \\\"gdpr_consequences\\\": null, \\\"gdpr_final_assessment\\\": null, \\\"gdpr_breach_type_comment\\\": null, \\\"gdpr_personal_data_comment\\\": null, \\\"gdpr_identification_comment\\\": null, \\\"gdpr_consequences_comment\\\": null, \\\"gdpr_final_assessment_comment\\\": null, \\\"gdpr_subsequent_notification\\\": null}, \\\"regulator_risk\\\": {}, \\\"inc_last_modified_date\\\": 1663610451616, \\\"admin_id\\\": null, \\\"creator_id\\\": 6, \\\"crimestatus_id\\\": 1, \\\"employee_involved\\\": null, \\\"end_date\\\": 1663610449718, \\\"exposure_dept_id\\\": null, \\\"exposure_individual_name\\\": null, \\\"exposure_vendor_id\\\": null, \\\"jurisdiction_name\\\": null, \\\"jurisdiction_reg_id\\\": null, \\\"start_date\\\": null, \\\"inc_start\\\": null, \\\"org_id\\\": 201, \\\"is_scenario\\\": false, \\\"hard_liability\\\": 0, \\\"nist_attack_vectors\\\": [], \\\"id\\\": 2114, \\\"sequence_code\\\": \\\"E2E5-20\\\", \\\"discovered_date\\\": 1621110044000, \\\"due_date\\\": null, \\\"create_date\\\": 1663297952673, \\\"owner_id\\\": 3, \\\"severity_code\\\": null, \\\"plan_status\\\": \\\"C\\\"}]}\", \"inputs\": {\"soar_utils_sort_fields\": \"[{\\\"field_name\\\":\\\"id\\\",\\\"type\\\":\\\"asc\\\"}]\", \"soar_utils_filter_conditions\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-soar-utils\", \"package_version\": \"1.0.0\", \"host\": \"Christophers-MacBook-Pro-2.local\", \"execution_time_ms\": 276, \"timestamp\": \"2022-09-20 14:46:54\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"recordsTotal\": {\"type\": \"integer\"}, \"recordsFiltered\": {\"type\": \"integer\"}, \"data\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"description\": {\"type\": [\"null\", \"string\"]}, \"phase_id\": {\"type\": \"integer\"}, \"inc_training\": {\"type\": \"boolean\"}, \"vers\": {\"type\": \"integer\"}, \"addr\": {}, \"city\": {}, \"creator\": {}, \"creator_principal\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}}}, \"exposure_type_id\": {\"type\": \"integer\"}, \"incident_type_ids\": {\"type\": \"array\"}, \"reporter\": {}, \"state\": {}, \"country\": {}, \"zip\": {}, \"workspace\": {\"type\": \"integer\"}, \"exposure\": {\"type\": \"integer\"}, \"org_handle\": {\"type\": \"integer\"}, \"members\": {\"type\": \"array\"}, \"negative_pr_likely\": {}, \"perms\": {\"type\": \"object\", \"properties\": {\"read\": {\"type\": \"boolean\"}, \"write\": {\"type\": \"boolean\"}, \"comment\": {\"type\": \"boolean\"}, \"assign\": {\"type\": \"boolean\"}, \"close\": {\"type\": \"boolean\"}, \"change_members\": {\"type\": \"boolean\"}, \"attach_file\": {\"type\": \"boolean\"}, \"read_attachments\": {\"type\": \"boolean\"}, \"delete_attachments\": {\"type\": \"boolean\"}, \"create_milestones\": {\"type\": \"boolean\"}, \"list_milestones\": {\"type\": \"boolean\"}, \"create_artifacts\": {\"type\": \"boolean\"}, \"list_artifacts\": {\"type\": \"boolean\"}, \"delete\": {\"type\": \"boolean\"}, \"change_workspace\": {\"type\": \"boolean\"}}}, \"confirmed\": {\"type\": \"boolean\"}, \"task_changes\": {\"type\": \"object\", \"properties\": {\"added\": {\"type\": \"array\"}, \"removed\": {\"type\": \"array\"}}}, \"assessment\": {\"type\": \"string\"}, \"data_compromised\": {}, \"draft\": {\"type\": \"boolean\"}, \"properties\": {\"type\": \"object\", \"properties\": {\"sdlp_policy_name\": {}, \"sdlp_policy_group_name\": {}, \"sdlp_policy_id\": {}, \"sdlp_incident_status\": {}, \"sdlp_incident_url\": {}, \"internal_customizations_field\": {}, \"sdlp_policy_group_id\": {}, \"sdlp_incident_id\": {}}}, \"resolution_id\": {\"type\": [\"integer\", \"null\"]}, \"resolution_summary\": {\"type\": [\"null\", \"string\"]}, \"pii\": {\"type\": \"object\", \"properties\": {\"data_compromised\": {}, \"determined_date\": {\"type\": \"integer\"}, \"harmstatus_id\": {\"type\": \"integer\"}, \"data_encrypted\": {}, \"data_contained\": {}, \"impact_likely\": {}, \"ny_impact_likely\": {}, \"or_impact_likely\": {}, \"wa_impact_likely\": {}, \"dc_impact_likely\": {}, \"data_source_ids\": {\"type\": \"array\"}, \"data_format\": {}, \"assessment\": {\"type\": \"string\"}, \"exposure\": {\"type\": \"integer\"}, \"gdpr_harm_risk\": {}, \"gdpr_lawful_data_processing_categories\": {\"type\": \"array\"}, \"alberta_health_risk_assessment\": {}, \"california_health_risk_assessment\": {}, \"new_zealand_risk_assessment\": {}, \"singapore_risk_assessment\": {}}}, \"gdpr\": {\"type\": \"object\", \"properties\": {\"gdpr_breach_circumstances\": {\"type\": \"array\"}, \"gdpr_breach_type\": {}, \"gdpr_personal_data\": {}, \"gdpr_identification\": {}, \"gdpr_consequences\": {}, \"gdpr_final_assessment\": {}, \"gdpr_breach_type_comment\": {}, \"gdpr_personal_data_comment\": {}, \"gdpr_identification_comment\": {}, \"gdpr_consequences_comment\": {}, \"gdpr_final_assessment_comment\": {}, \"gdpr_subsequent_notification\": {}}}, \"regulator_risk\": {\"type\": \"object\"}, \"inc_last_modified_date\": {\"type\": \"integer\"}, \"admin_id\": {}, \"creator_id\": {\"type\": \"integer\"}, \"crimestatus_id\": {\"type\": \"integer\"}, \"employee_involved\": {}, \"end_date\": {\"type\": [\"integer\", \"null\"]}, \"exposure_dept_id\": {}, \"exposure_individual_name\": {}, \"exposure_vendor_id\": {}, \"jurisdiction_name\": {}, \"jurisdiction_reg_id\": {}, \"start_date\": {}, \"inc_start\": {}, \"org_id\": {\"type\": \"integer\"}, \"is_scenario\": {\"type\": \"boolean\"}, \"hard_liability\": {\"type\": \"integer\"}, \"nist_attack_vectors\": {\"type\": \"array\"}, \"id\": {\"type\": \"integer\"}, \"sequence_code\": {\"type\": \"string\"}, \"discovered_date\": {\"type\": \"integer\"}, \"due_date\": {}, \"create_date\": {\"type\": \"integer\"}, \"owner_id\": {\"type\": \"integer\"}, \"severity_code\": {\"type\": [\"integer\", \"null\"]}, \"plan_status\": {\"type\": \"string\"}}}}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"soar_utils_sort_fields\": {\"type\": \"string\"}, \"soar_utils_filter_conditions\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "949d5b2c-0e50-4b89-9318-c509850c8b68",
      "version": 4,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815539,
      "name": "soar_utils_soar_search",
      "output_json_example": "{\"results\": [{\"match_highlights\": [{\"match_field_name\": \"Content Type\", \"match_field_value\": \"application/\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e\"}, {\"match_field_name\": \"Name\", \"match_field_value\": \"\u003cResilientHighlight\u003eapp\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003efn_slack\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003e2.0.0\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003e13477\u003c/ResilientHighlight\u003e.\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e\"}], \"score\": 18.473476, \"result\": {\"actions\": [], \"content_type\": \"application/zip\", \"created\": 1663640024209, \"creator_id\": {\"display_name\": \"Admin User\", \"id\": 1, \"name\": \"admin@example.com\", \"type\": \"user\"}, \"id\": 68, \"inc_id\": 2112, \"inc_name\": \"SOAR Utilities\", \"inc_owner\": {\"display_name\": \"Admin User\", \"id\": 1, \"name\": \"admin@example.com\", \"type\": \"user\"}, \"name\": \"app-fn_slack-2.0.0-13477.zip\", \"playbooks\": [], \"size\": 599379, \"task_at_id\": null, \"task_custom\": null, \"task_id\": null, \"task_members\": null, \"task_name\": null, \"type\": \"incident\", \"uuid\": \"e5868c93-581b-4543-8113-358becb2c9cc\", \"vers\": 7}, \"type_id\": \"attachment\", \"org_id\": 201, \"obj_id\": 68, \"obj_name\": \"app-fn_slack-2.0.0-13477.zip\", \"obj_creator_id\": 1, \"obj_create_date\": 1663640024209, \"inc_id\": 2112, \"inc_name\": \"SOAR Utilities\", \"inc_owner_id\": 1, \"task_id\": null, \"task_name\": null, \"match_field_name\": \"Content Type\", \"match_field_value\": \"application/\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e\"}]}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"results\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"match_highlights\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"match_field_name\": {\"type\": \"string\"}, \"match_field_value\": {\"type\": \"string\"}}}}, \"score\": {\"type\": \"number\"}, \"result\": {\"type\": \"object\", \"properties\": {\"actions\": {\"type\": \"array\"}, \"content_type\": {\"type\": \"string\"}, \"created\": {\"type\": \"integer\"}, \"creator_id\": {\"type\": \"object\", \"properties\": {\"display_name\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}}}, \"id\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"object\", \"properties\": {\"display_name\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}}}, \"name\": {\"type\": \"string\"}, \"playbooks\": {\"type\": \"array\"}, \"size\": {\"type\": \"integer\"}, \"task_at_id\": {}, \"task_custom\": {}, \"task_id\": {}, \"task_members\": {}, \"task_name\": {}, \"type\": {\"type\": \"string\"}, \"uuid\": {\"type\": \"string\"}, \"vers\": {\"type\": \"integer\"}}}, \"type_id\": {\"type\": \"string\"}, \"org_id\": {\"type\": \"integer\"}, \"obj_id\": {\"type\": \"integer\"}, \"obj_name\": {\"type\": \"string\"}, \"obj_creator_id\": {\"type\": \"integer\"}, \"obj_create_date\": {\"type\": \"integer\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner_id\": {\"type\": \"integer\"}, \"task_id\": {}, \"task_name\": {}, \"match_field_name\": {\"type\": \"string\"}, \"match_field_value\": {\"type\": \"string\"}}}}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "125b3261-250e-4b34-aad8-eb4b49fc262c",
      "version": 4,
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
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
      "last_modified_time": 1664750815593,
      "name": "soar_utils_string_to_attachment",
      "output_json_example": "{\"attachment_id\": 72}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"attachment_id\": {\"type\": \"integer\"}}}",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "59d7c5d2-b9c0-4dff-a3b4-c8341913287b",
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
          "tags": [
            {
              "tag_handle": "fn_soar_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 133,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1665000744294,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1665000744294,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea",
        "85b2df27-3cdc-45bf-943f-6b115b3d66e2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_soar_utils",
      "name": "fn_soar_utils",
      "programmatic_name": "fn_soar_utils",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
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
        "version": 3,
        "workflow_id": "example_soar_utilities_close_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_close_incident\" isExecutable=\"true\" name=\"Example: SOAR Utilities Close Incident\"\u003e\u003cdocumentation\u003eAn example workflow which takes an incident_id and optional close_fields in order to close an Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0wyjqvg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_16mtae1\"\u003e\u003cincoming\u003eSequenceFlow_1x7e4gy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wyjqvg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xmnymz\"/\u003e\u003cserviceTask id=\"ServiceTask_0xmnymz\" name=\"SOAR Utilities: Close Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"836a3505-3306-4eda-9703-6297fad907da\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = \\\"Result from Example: Close Incident on Incident {0}: \u0026lt;strong\u0026gt;{1}\u0026lt;/strong\u0026gt;\\\".format(results.inputs[\u0027incident_id\u0027], \\\\\\n\\\"success\\\" if results.success else \\\"failure.\u0026lt;br\u0026gt;Reason: {}\\\".format(results.reason))\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\niu_close_fields = rule.properties.soar_utils_close_fields.content\\ninputs.soar_utils_close_fields = u\\\"{}\\\".format(iu_close_fields)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wyjqvg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1x7e4gy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x7e4gy\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"EndEvent_16mtae1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02c13t7\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\nincident_id, close_fields]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17ut8cn\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"TextAnnotation_02c13t7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16mj7cm\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nCloses the Incident should reflect the action after the function runs. A Note is created with the function results.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_01rq8aj\" sourceRef=\"ServiceTask_0xmnymz\" targetRef=\"TextAnnotation_16mj7cm\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16mtae1\" id=\"EndEvent_16mtae1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"599\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"617\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wyjqvg\" id=\"SequenceFlow_0wyjqvg_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"271\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xmnymz\" id=\"ServiceTask_0xmnymz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"344\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x7e4gy\" id=\"SequenceFlow_1x7e4gy_di\"\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"599\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"521.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02c13t7\" id=\"TextAnnotation_02c13t7_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"103\" x=\"199\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17ut8cn\" id=\"Association_17ut8cn_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16mj7cm\" id=\"TextAnnotation_16mj7cm_di\"\u003e\u003comgdc:Bounds height=\"89\" width=\"171\" x=\"506\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_01rq8aj\" id=\"Association_01rq8aj_di\"\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"521\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example workflow which takes an incident_id and optional close_fields in order to close an Incident.",
      "export_key": "example_soar_utilities_close_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750815951,
      "name": "Example: SOAR Utilities Close Incident",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_close_incident",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "8a2320a9-0dba-4de1-8702-b01ad29dee73",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_soar_utilities_zip_list",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_list\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip List\"\u003e\u003cdocumentation\u003eAn example showing how to list the contents of a ZIP file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0kvfjgi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ogd9y3\"\u003e\u003cincoming\u003eSequenceFlow_0kvraz7\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0ahd0wo\" name=\"SOAR Utilities: Attachment Zip Li...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a111dc9b-9ea4-42a2-8590-23ca399d8387\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output contains two lists:\\n# - \\\"namelist\\\", which is just a list of the filenames (paths) within the zip file,\\n# - \\\"infolist\\\", which has full information for each file, including its name, size, and so on.\\n\\n# For this example, let\u0027s create two notes\\n\\n# One with a list of the namelist\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor filename in results.namelist:\\n  html = html + u\\\"{}\u0026lt;br\u0026gt;\\\".format(filename)\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\\n# Another with more detailed information\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor fileinfo in results.infolist:\\n  html = html + u\\\"{} ({} bytes, {} compressed) {}\u0026lt;br\u0026gt;\\\".format(fileinfo[\\\"filename\\\"], fileinfo[\\\"file_size\\\"], fileinfo[\\\"compress_size\\\"], fileinfo[\\\"comment\\\"])\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0kvfjgi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kvraz7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0kvfjgi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ahd0wo\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0kvraz7\" sourceRef=\"ServiceTask_0ahd0wo\" targetRef=\"EndEvent_0ogd9y3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0kqgg4l\"\u003e\u003ctext\u003eFunction reads the attachment (by id) then produces a list of its contents, in a structured data format.\u00a0 The post-processing script writes these results into a note on the incident.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1amd98w\" sourceRef=\"ServiceTask_0ahd0wo\" targetRef=\"TextAnnotation_0kqgg4l\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ogd9y3\" id=\"EndEvent_0ogd9y3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"691\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"709\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ahd0wo\" id=\"ServiceTask_0ahd0wo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kvfjgi\" id=\"SequenceFlow_0kvfjgi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"285.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kvraz7\" id=\"SequenceFlow_0kvraz7_di\"\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"691\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"582\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0kqgg4l\" id=\"TextAnnotation_0kqgg4l_di\"\u003e\u003comgdc:Bounds height=\"103\" width=\"230\" x=\"523\" y=\"1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1amd98w\" id=\"Association_1amd98w_di\"\u003e\u003comgdi:waypoint x=\"470\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"566\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "An example showing how to list the contents of a ZIP file attachment.",
      "export_key": "example_soar_utilities_zip_list",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750816830,
      "name": "Example: SOAR Utilities Zip List",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_list",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "1a1ffaaa-3781-4f90-a44b-aa4700ca3d07",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_string_to_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_string_to_attachment\" isExecutable=\"true\" name=\"Example: SOAR Utilities String to Attachment\"\u003e\u003cdocumentation\u003eAn example of creating an attachment from an input string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0depya1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1560ig6\"\u003e\u003cincoming\u003eSequenceFlow_1l95am2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0depya1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1n72a19\"/\u003e\u003cserviceTask id=\"ServiceTask_1n72a19\" name=\"SOAR Utilities: String to Attachm...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"59d7c5d2-b9c0-4dff-a3b4-c8341913287b\"\u003e{\"inputs\":{\"03955f53-5940-49ff-a9df-0b607099657b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"A Test Attachment Name\"}}},\"post_processing_script\":\"# result: {\u0027attachment_id\u0027: 28}\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the string to convert, the incident id and the attachment name\\ninputs.soar_utils_string_to_convert_to_attachment = artifact.value\\ninputs.incident_id = incident.id\\n#inputs.attachment_name = \\\"A Test Attachment Name\\\"\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0depya1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1l95am2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1l95am2\" sourceRef=\"ServiceTask_1n72a19\" targetRef=\"EndEvent_1560ig6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1560ig6\" id=\"EndEvent_1560ig6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"489\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"507\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0depya1\" id=\"SequenceFlow_0depya1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"239.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1n72a19\" id=\"ServiceTask_1n72a19_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"281\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l95am2\" id=\"SequenceFlow_1l95am2_di\"\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"489\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"435\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example of creating an attachment from an input string",
      "export_key": "example_soar_utilities_string_to_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750816591,
      "name": "Example: SOAR Utilities String to Attachment",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_string_to_attachment",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "5a74758c-edf6-431c-8f28-57daeca0d5af",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_soar_utilities_search_incidents",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_search_incidents\" isExecutable=\"true\" name=\"Example: SOAR Utilities Search Incidents\"\u003e\u003cdocumentation\u003eSearch incidents based on filtering fields. Sort field are optional\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1l7fhuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_09f9rll\"\u003e\u003cincoming\u003eSequenceFlow_0blh56i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1l7fhuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0iqh4z0\"/\u003e\u003cserviceTask id=\"ServiceTask_0iqh4z0\" name=\"SOAR Utilities: Search Incidents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"949d5b2c-0e50-4b89-9318-c509850c8b68\"\u003e{\"inputs\":{},\"post_processing_script\":\"msgs = [u\\\"Filter conditions: {}\\\".format(results.inputs[\u0027soar_utils_filter_conditions\u0027])]\\nif results.success:\\n  for inc in results.content[\u0027data\u0027]:\\n    msgs.append(u\\\"id: \u0026lt;a target=\u0027blank\u0027 href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt; Name: {1}\\\".format(inc[\u0027id\u0027], inc[\u0027name\u0027]))\\n  incident.addNote(helper.createRichText(u\\\"Found {} incidents\u0026lt;br\u0026gt;{}\\\".format(results.content[\u0027recordsTotal\u0027], \u0027\u0026lt;br\u0026gt;\u0027.join(msgs))))\\n\\nelse:\\n  incident.addNote(u\\\"Search error found: {}\u0026lt;br\u0026gt;Filter conditions: {}\u0026lt;br\u0026gt;Sort Fields conditions: {}\\\".format(results.reason, \\n      results.inputs.get(\\\"soar_utils_filter_conditions\\\"), results.inputs.get(\\\"soar_utils_sort_fields\\\")))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_filter_conditions = rule.properties.soar_utils_search_fields.content\\ninputs.soar_utils_sort_fields = rule.properties.soar_utils_sort_fields.content\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1l7fhuk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0blh56i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0blh56i\" sourceRef=\"ServiceTask_0iqh4z0\" targetRef=\"EndEvent_09f9rll\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09f9rll\" id=\"EndEvent_09f9rll_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"535\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"553\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l7fhuk\" id=\"SequenceFlow_1l7fhuk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"301\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"249.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0iqh4z0\" id=\"ServiceTask_0iqh4z0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"301\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0blh56i\" id=\"SequenceFlow_0blh56i_di\"\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"468\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "description": "Search incidents based on filtering fields. Sort field are optional",
      "export_key": "example_soar_utilities_search_incidents",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1665000661761,
      "name": "Example: SOAR Utilities Search Incidents",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_search_incidents",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "c65e3d60-0f50-4383-a689-33784d4f8c31",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "example_soar_utilities_attachment_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_attachment_hash\" isExecutable=\"true\" name=\"Example: SOAR Utilities Attachment Hash\"\u003e\u003cdocumentation\u003eAn example that calculates hash artifacts from an attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dooi7f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_04vzzkb\"\u003e\u003cincoming\u003eSequenceFlow_0rl0lje\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_01dxzwo\" name=\"SOAR Utilities: Attachment Hash\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"897779c3-b7bf-4a2b-b3f5-fa43058bad16\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\u0027sha256\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-256 Hash\\\", results.get(\u0027sha256\u0027), u\\\"SHA-256 hash of \u0027{}\u0027\\\".format(attachment.name))\\n\\nif results.get(\u0027sha1\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-1 Hash\\\", results.get(\u0027sha1\u0027), u\\\"SHA-1 hash of \u0027{}\u0027\\\".format(attachment.name))\\n\\nif results.get(\u0027md5\u0027, None):\\n  incident.addArtifact(\\\"Malware MD5 Hash\\\", results.get(\u0027md5\u0027), u\\\"MD5 hash of \u0027{}\u0027\\\".format(attachment.name))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dooi7f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0rl0lje\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dooi7f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01dxzwo\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0rl0lje\" sourceRef=\"ServiceTask_01dxzwo\" targetRef=\"EndEvent_04vzzkb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_08t8dqp\"\u003e\u003ctext\u003e\u003c![CDATA[Calculate hashes of a file attachment.\n\nThe results are added to the incident as new artifacts.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1bftw41\" sourceRef=\"ServiceTask_01dxzwo\" targetRef=\"TextAnnotation_08t8dqp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04vzzkb\" id=\"EndEvent_04vzzkb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"472\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"490\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01dxzwo\" id=\"ServiceTask_01dxzwo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_08t8dqp\" id=\"TextAnnotation_08t8dqp_di\"\u003e\u003comgdc:Bounds height=\"87\" width=\"122\" x=\"394\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1bftw41\" id=\"Association_1bftw41_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dooi7f\" id=\"SequenceFlow_1dooi7f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rl0lje\" id=\"SequenceFlow_0rl0lje_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"472\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"423\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "An example that calculates hash artifacts from an attachment.",
      "export_key": "example_soar_utilities_attachment_hash",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1665000252065,
      "name": "Example: SOAR Utilities Attachment Hash",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_attachment_hash",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "d99cc4d1-db2d-4487-8c06-78eea1256980",
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "example_soar_utilities_zip_extract",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_extract\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip Extract\"\u003e\u003cdocumentation\u003eAn example showing how to extract a file, in this example the file is a jpeg, from a ZIP file attachment and create a new attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1auywqg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_03jmhgm\"\u003e\u003cincoming\u003eSequenceFlow_0q6icfq\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0rnx372\" name=\"SOAR Utilities: Attachment Zip Ex...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"023044a4-f71f-4768-87f3-aad822d53723\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# The path within the zip that we want to extract\\ninputs.soar_utils_file_path = rule.properties.soar_utils_extract_file_path\\n\\n# If the zipfile is password protected, specify here\\n# inputs.zipfile_password = \\nif rule.properties.soar_utils_zip_password:\\n  inputs.soar_utils_zipfile_password = rule.properties.soar_utils_zip_password\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"extracted_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1auywqg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1y4isbs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_171egfi\" name=\"SOAR Utilities: Base64 to Attachm...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"337c083e-2c30-4907-8000-0b9a4496154b\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_base64content = workflow.properties.extracted_file.content\\nfile_name = rule.properties.soar_utils_extract_file_path.split(\u0027/\u0027)[-1]\\n\\ninputs.incident_id = incident.id\\ninputs.soar_utils_file_name = file_name + \\\".b64\\\"\\ninputs.soar_utils_content_type = \\\"image/jpeg\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1y4isbs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q6icfq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1auywqg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rnx372\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1y4isbs\" sourceRef=\"ServiceTask_0rnx372\" targetRef=\"ServiceTask_171egfi\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0q6icfq\" sourceRef=\"ServiceTask_171egfi\" targetRef=\"EndEvent_03jmhgm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1by3ic1\"\u003e\u003ctext\u003e\u003c![CDATA[In this example we assume that the file attachment is a Word, Excel or Powerpoint document (docx, xlsx, pptx).\u00a0 These are zipfiles, and may contain a thumbnail image (\"docProps/thumbnail.jpeg\").\n\n\nThe \"zip extract\" function produces base64-encoded contents of the extracted file.\u00a0 In the \"output\", we give that a name so it can be used downstream.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0k3f371\" sourceRef=\"ServiceTask_0rnx372\" targetRef=\"TextAnnotation_1by3ic1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14sh9j5\"\u003e\u003ctext\u003eFrom the output of the first function, create a new file attachment.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0han8fp\" sourceRef=\"ServiceTask_171egfi\" targetRef=\"TextAnnotation_14sh9j5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03jmhgm\" id=\"EndEvent_03jmhgm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"735\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"753\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rnx372\" id=\"ServiceTask_0rnx372_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"293\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_171egfi\" id=\"ServiceTask_171egfi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"525\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1auywqg\" id=\"SequenceFlow_1auywqg_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"245.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1y4isbs\" id=\"SequenceFlow_1y4isbs_di\"\u003e\u003comgdi:waypoint x=\"393\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"459\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q6icfq\" id=\"SequenceFlow_0q6icfq_di\"\u003e\u003comgdi:waypoint x=\"625\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"735\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"680\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1by3ic1\" id=\"TextAnnotation_1by3ic1_di\"\u003e\u003comgdc:Bounds height=\"145\" width=\"257\" x=\"85\" y=\"-28\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0k3f371\" id=\"Association_0k3f371_di\"\u003e\u003comgdi:waypoint x=\"311\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14sh9j5\" id=\"TextAnnotation_14sh9j5_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"112\" x=\"681\" y=\"22\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0han8fp\" id=\"Association_0han8fp_di\"\u003e\u003comgdi:waypoint x=\"617\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "An example showing how to extract a file, in this example the file is a jpeg, from a ZIP file attachment and create a new attachment.",
      "export_key": "example_soar_utilities_zip_extract",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1665000739818,
      "name": "Example: SOAR Utilities Zip Extract",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_extract",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "2ddbfca8-90f8-4c92-ab31-1e65fd8ad846",
      "workflow_id": 81
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_artifact_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_artifact_hash\" isExecutable=\"true\" name=\"Example: SOAR Utilities Artifact Hash\"\u003e\u003cdocumentation\u003eAn example that calculates hash from an artifact attachment\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dmwndm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1wyx46y\"\u003e\u003cincoming\u003eSequenceFlow_0wxnbxr\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1qsvrwc\" name=\"SOAR Utilities Artifact Hash\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"357842c2-e4bc-4e80-b510-f0ed4675a6d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The result contains at least these three hashes\\nif results.get(\u0027sha256\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-256 Hash\\\", results.get(\u0027sha256\u0027), u\\\"SHA-256 hash of \u0027{}\u0027\\\".format(artifact.value))\\n\\nif results.get(\u0027sha1\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-1 Hash\\\", results.get(\u0027sha1\u0027), u\\\"SHA-1 hash of \u0027{}\u0027\\\".format(artifact.value))\\n\\nif results.get(\u0027md5\u0027, None):\\n  incident.addArtifact(\\\"Malware MD5 Hash\\\", results.get(\u0027md5\u0027), u\\\"MD5 hash of \u0027{}\u0027\\\".format(artifact.value))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dmwndm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wxnbxr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dmwndm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qsvrwc\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0wxnbxr\" sourceRef=\"ServiceTask_1qsvrwc\" targetRef=\"EndEvent_1wyx46y\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wyx46y\" id=\"EndEvent_1wyx46y_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"528\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"501\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qsvrwc\" id=\"ServiceTask_1qsvrwc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"313\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dmwndm\" id=\"SequenceFlow_1dmwndm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"313\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"255.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wxnbxr\" id=\"SequenceFlow_0wxnbxr_di\"\u003e\u003comgdi:waypoint x=\"413\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"528\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"470.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example that calculates hash from an artifact attachment",
      "export_key": "example_soar_utilities_artifact_hash",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750815821,
      "name": "Example: SOAR Utilities Artifact Hash",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_artifact_hash",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "e2f3e5e7-15e5-4580-8fe5-b0e56e4bb799",
      "workflow_id": 78
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_soar_utilities_create_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_create_incident\" isExecutable=\"true\" name=\"Example: SOAR Utilities Create Incident\"\u003e\u003cdocumentation\u003eCreate an incident based on json field data. Artifacts and notes can be created at the same time.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0el966k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0qsfyx6\"\u003e\u003cincoming\u003eSequenceFlow_1da5p43\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0el966k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gshre3\"/\u003e\u003cserviceTask id=\"ServiceTask_1gshre3\" name=\"SOAR Utilities: Create Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c6f170f3-61f6-4a46-a397-f2b3ae095be4\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{0}\\\"\u0026gt;{0}: {1}\u0026lt;/a\u0026gt;\u0027.format(results.content[\u0027id\u0027], results.content[\u0027name\u0027])\\n  incident.addNote(helper.createRichText(u\\\"Incident successfully created: {}\\\".format(link)))\\nelse:\\n  incident.addNote(u\\\"Incident creation failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.soar_utils_create_fields = rule.properties.soar_utils_create_fields.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0el966k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1da5p43\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1da5p43\" sourceRef=\"ServiceTask_1gshre3\" targetRef=\"EndEvent_0qsfyx6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0giavvu\"\u003e\u003ctext\u003eA note with the results is added\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h9k9bt\" sourceRef=\"ServiceTask_1gshre3\" targetRef=\"TextAnnotation_0giavvu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0qsfyx6\" id=\"EndEvent_0qsfyx6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"557\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"530\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0el966k\" id=\"SequenceFlow_0el966k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"330\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"219\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gshre3\" id=\"ServiceTask_1gshre3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"330\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1da5p43\" id=\"SequenceFlow_1da5p43_di\"\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"448.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0giavvu\" id=\"TextAnnotation_0giavvu_di\"\u003e\u003comgdc:Bounds height=\"38\" width=\"101\" x=\"454\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h9k9bt\" id=\"Association_0h9k9bt_di\"\u003e\u003comgdi:waypoint x=\"418\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"95\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Create an incident based on json field data. Artifacts and notes can be created at the same time.",
      "export_key": "example_soar_utilities_create_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750817314,
      "name": "Example: SOAR Utilities Create Incident",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_create_incident",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "3afcf022-6310-4dd1-a650-988eb3eb8880",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_soar_utilities_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_attachment_to_base64\" isExecutable=\"true\" name=\"Example: SOAR Utilities Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting a file attachment to a Base64 encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ci0etf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0w7dz2z\"\u003e\u003cincoming\u003eSequenceFlow_0g2zmh9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ci0etf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_039vgvd\"/\u003e\u003cserviceTask id=\"ServiceTask_039vgvd\" name=\"SOAR Utilities: Attachment to Bas...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"71a8e169-ea42-4e1d-be8f-d0dbcd702908\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = str(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\")[1:20])\\n    \\n  incident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task id\\nif task is not None:\\n  inputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ci0etf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0g2zmh9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0g2zmh9\" sourceRef=\"ServiceTask_039vgvd\" targetRef=\"EndEvent_0w7dz2z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18w5qwi\"\u003e\u003ctext\u003eConvert a file attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1npiyrk\" sourceRef=\"ServiceTask_039vgvd\" targetRef=\"TextAnnotation_18w5qwi\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0w7dz2z\" id=\"EndEvent_0w7dz2z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"460\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"478\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ci0etf\" id=\"SequenceFlow_0ci0etf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_039vgvd\" id=\"ServiceTask_039vgvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0g2zmh9\" id=\"SequenceFlow_0g2zmh9_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"460\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18w5qwi\" id=\"TextAnnotation_18w5qwi_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"105\" x=\"405\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1npiyrk\" id=\"Association_1npiyrk_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example converting a file attachment to a Base64 encoded string",
      "export_key": "example_soar_utilities_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750816082,
      "name": "Example: SOAR Utilities Attachment to Base64",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_attachment_to_base64",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "77797d3f-0bcb-43fc-8c13-b8d0b7815e21",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "example_soar_utilities_soar_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_soar_search\" isExecutable=\"true\" name=\"Example: SOAR Utilities SOAR Search\"\u003e\u003cdocumentation\u003e\u003c![CDATA[This function searches the SOAR platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, incidents currently assigned to a given user, or a very wide range of other search conditions.\n\nNOTE: The search results may include data from incidents that the current SOAR user (the person who triggered the workflow) cannot access. Often your SOAR users have the Default role that allows them to only see incidents where they are members. This function runs with the permissions of your app account, which typically may have much wider access privileges. Use with caution, to avoid information disclosure.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0fcgpbb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_057b85i\"\u003e\u003cincoming\u003eSequenceFlow_1h1rfil\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1afc98z\" name=\"SOAR Utilities: SOAR Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"125b3261-250e-4b34-aad8-eb4b49fc262c\"\u003e{\"inputs\":{\"357b3f18-2df2-4b39-8128-af57eb91821a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n  \\\"types\\\": [\\\"attachment\\\"],\\n  \\\"filters\\\": {\\n    \\\"incident\\\": [{\\n        \\\"conditions\\\": [{\\\"field_name\\\": \\\"plan_status\\\", \\\"method\\\": \\\"in\\\", \\\"value\\\": [\\\"A\\\"]}]\\n      }]\\n  }\\n}\"}}}},\"post_processing_script\":\"# Search results include \\\"results\\\", which is a list of the search hits.\\n# There might be lots of results!\\n\\n# In this example we add a note with information about each result.\\nresult_info = []\\nfor result in results.results:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{}\\\"\u0026gt;{}\u0026lt;/a\u0026gt;\u0027.format(result[\u0027result\u0027][\u0027inc_id\u0027], result[\u0027result\u0027][\u0027inc_name\u0027])\\n  result_info.append(u\\\"\u0026lt;p\u0026gt;{} - {}\u0026lt;/p\u0026gt;\\\".format(link, result[\u0027obj_name\u0027]))\\n  \\nif len(result_info)==0:\\n  html = \\\"\u0026lt;div\u0026gt;No results\u0026lt;/div\u0026gt;\\\"\\nelse:\\n  html = u\\\"\u0026lt;div\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(\\\"\\\".join(result_info))\\n\\nincident.addNote(helper.createRichText(html))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Search for other occurrences of the same file attachment in Resilient.\\n\\n# The search template determines the type(s) of object to search, and the filter conditions.\\n# This can be used to search within a specific incident field, or to search only incidents that meet other criteria.\\n# Refer to SearchExInputDTO in the REST API documentation for additional details of this data structure.\\n\\n# The search query can be a simple string.\\ninputs.soar_search_query = attachment.name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fcgpbb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1h1rfil\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fcgpbb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1afc98z\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1h1rfil\" sourceRef=\"ServiceTask_1afc98z\" targetRef=\"EndEvent_057b85i\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_057b85i\" id=\"EndEvent_057b85i_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"542\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"560\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1afc98z\" id=\"ServiceTask_1afc98z_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"328\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fcgpbb\" id=\"SequenceFlow_0fcgpbb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"263\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1h1rfil\" id=\"SequenceFlow_1h1rfil_di\"\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"542\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"485\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "This function searches the SOAR platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, incidents currently assigned to a given user, or a very wide range of other search conditions.\n\nNOTE: The search results may include data from incidents that the current SOAR user (the person who triggered the workflow) cannot access. Often your SOAR users have the Default role that allows them to only see incidents where they are members. This function runs with the permissions of your app account, which typically may have much wider access privileges. Use with caution, to avoid information disclosure.",
      "export_key": "example_soar_utilities_soar_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1665000595458,
      "name": "Example: SOAR Utilities SOAR Search",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_soar_search",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "dc3082ae-d200-4587-9b97-2f4494189913",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_zip_extract_to_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_zip_extract_to_artifact\" isExecutable=\"true\" name=\"Example: SOAR Utilities Zip Extract to Artifact\"\u003e\u003cdocumentation\u003eAn example showing how to extract a file from a ZIP file attachment and create a new artifact.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rk2qdo\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1ssbfkh\"\u003e\u003cincoming\u003eSequenceFlow_14ghbpb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1rk2qdo\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1wux4mf\"/\u003e\u003cserviceTask id=\"ServiceTask_1wux4mf\" name=\"SOAR Utilities: Attachment Zip Ex...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"023044a4-f71f-4768-87f3-aad822d53723\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# The path within the zip that we want to extract\\ninputs.soar_utils_file_path = rule.properties.soar_utils_extract_file_path\\n\\n# If the zipfile is password protected, specify here\\n# inputs.zipfile_password = \\nif rule.properties.soar_utils_zip_password:\\n  inputs.soar_utils_zipfile_password = rule.properties.soar_utils_zip_password\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"extracted_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rk2qdo\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qfknru\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qfknru\" sourceRef=\"ServiceTask_1wux4mf\" targetRef=\"ServiceTask_0f92p9r\"/\u003e\u003cserviceTask id=\"ServiceTask_0f92p9r\" name=\"SOAR Utilities: Base64 to Artifac...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2710d4db-7c32-42cc-a264-1f0e66a64826\"\u003e{\"inputs\":{\"a2811c56-b510-40fd-bbbd-afafe0ddf6f0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"beb27e7a-5081-4be4-b33c-fc28095fddb2\"}}},\"pre_processing_script\":\"inputs.soar_utils_base64content = workflow.properties.extracted_file.content\\nfile_name = rule.properties.soar_utils_extract_file_path.split(\u0027/\u0027)[-1]\\n\\ninputs.incident_id = incident.id\\ninputs.soar_utils_file_name = file_name + \\\".b64\\\"\\ninputs.soar_utils_content_type = \\\"image/jpeg\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qfknru\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14ghbpb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14ghbpb\" sourceRef=\"ServiceTask_0f92p9r\" targetRef=\"EndEvent_1ssbfkh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0z05feh\"\u003e\u003ctext\u003e\u003c![CDATA[In this example we assume that the file attachment is a Word, Excel or Powerpoint document (docx, xlsx, pptx).\u00a0 These are zipfiles, and may contain a thumbnail image (\"docProps/thumbnail.jpeg\").\n\n\nThe \"zip extract\" function produces base64-encoded contents of the extracted file.\u00a0 In the \"output\", we give that a name so it can be used downstream.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13pf015\" sourceRef=\"ServiceTask_1wux4mf\" targetRef=\"TextAnnotation_0z05feh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1dy0d5v\"\u003e\u003ctext\u003eFrom the output of the first function, create a new artifact.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_162ex5g\" sourceRef=\"ServiceTask_0f92p9r\" targetRef=\"TextAnnotation_1dy0d5v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ssbfkh\" id=\"EndEvent_1ssbfkh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"548\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"566\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rk2qdo\" id=\"SequenceFlow_1rk2qdo_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1wux4mf\" id=\"ServiceTask_1wux4mf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qfknru\" id=\"SequenceFlow_0qfknru_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"379.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0z05feh\" id=\"TextAnnotation_0z05feh_di\"\u003e\u003comgdc:Bounds height=\"179\" width=\"179\" x=\"90\" y=\"-97\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13pf015\" id=\"Association_13pf015_di\"\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"232\" xsi:type=\"omgdc:Point\" y=\"82\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f92p9r\" id=\"ServiceTask_0f92p9r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"405\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14ghbpb\" id=\"SequenceFlow_14ghbpb_di\"\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"526.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1dy0d5v\" id=\"TextAnnotation_1dy0d5v_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"100\" x=\"516\" y=\"27\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_162ex5g\" id=\"Association_162ex5g_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example showing how to extract a file from a ZIP file attachment and create a new artifact.",
      "export_key": "example_soar_utilities_zip_extract_to_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750816475,
      "name": "Example: SOAR Utilities Zip Extract to Artifact",
      "object_type": "attachment",
      "programmatic_name": "example_soar_utilities_zip_extract_to_artifact",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "4d981842-4587-41bd-9fcd-706b90a1b9c9",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_get_task_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_get_task_contact_info\" isExecutable=\"true\" name=\"Example: SOAR Utilities Get Task Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for a task in an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_01tqdx3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ra7rtl\"\u003e\u003cincoming\u003eSequenceFlow_0mvgj5u\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0qznvra\" name=\"SOAR Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7edb9444-2b81-4756-8fbe-3483cdafb9eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"owner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\ntask.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_01tqdx3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mvgj5u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_01tqdx3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qznvra\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0mvgj5u\" sourceRef=\"ServiceTask_0qznvra\" targetRef=\"EndEvent_0ra7rtl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ra7rtl\" id=\"EndEvent_0ra7rtl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"563\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"581\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qznvra\" id=\"ServiceTask_0qznvra_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"323\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01tqdx3\" id=\"SequenceFlow_01tqdx3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"260.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mvgj5u\" id=\"SequenceFlow_0mvgj5u_di\"\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"563\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"493\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Get owner and member contact information for a task in an Incident",
      "export_key": "example_soar_utilities_get_task_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750817067,
      "name": "Example: SOAR Utilities Get Task Contact Info",
      "object_type": "task",
      "programmatic_name": "example_soar_utilities_get_task_contact_info",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "b6f04e6b-32fa-4e2b-b3c9-5f9a88f23da2",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "example_soar_utilities_artifact_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_artifact_attachment_to_base64\" isExecutable=\"true\" name=\"Example: SOAR Utilities (Artifact) Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting an Artifact of type File to a Base64 Encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_148uk59\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1up8nde\"\u003e\u003cincoming\u003eSequenceFlow_0c4ts4v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_148uk59\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0trmhbs\"/\u003e\u003cserviceTask id=\"ServiceTask_0trmhbs\" name=\"SOAR Utilities: Attachment to Bas...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"71a8e169-ea42-4e1d-be8f-d0dbcd702908\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = str(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\", \\\"\\\")[1:20] )\\n\\n  incident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: incident_id artifact_id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_148uk59\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c4ts4v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0c4ts4v\" sourceRef=\"ServiceTask_0trmhbs\" targetRef=\"EndEvent_1up8nde\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00fnkrh\"\u003e\u003ctext\u003eConvert a file attachment attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1p30sfl\" sourceRef=\"ServiceTask_0trmhbs\" targetRef=\"TextAnnotation_00fnkrh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1up8nde\" id=\"EndEvent_1up8nde_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"498\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"516\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_148uk59\" id=\"SequenceFlow_148uk59_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0trmhbs\" id=\"ServiceTask_0trmhbs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"290\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c4ts4v\" id=\"SequenceFlow_0c4ts4v_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"498\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"444\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00fnkrh\" id=\"TextAnnotation_00fnkrh_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"146\" x=\"426\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1p30sfl\" id=\"Association_1p30sfl_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "An example converting an Artifact of type File to a Base64 Encoded string",
      "export_key": "example_soar_utilities_artifact_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750816950,
      "name": "Example: SOAR Utilities (Artifact) Attachment to Base64",
      "object_type": "artifact",
      "programmatic_name": "example_soar_utilities_artifact_attachment_to_base64",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "d1fee528-3870-4d5a-9b6e-a6b0a68d6951",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_soar_utilities_get_incident_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_soar_utilities_get_incident_contact_info\" isExecutable=\"true\" name=\"Example: SOAR Utilities Get Incident Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0z9atne\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_05qhqog\"\u003e\u003cincoming\u003eSequenceFlow_0kwuavs\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0z77voh\" name=\"SOAR Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7edb9444-2b81-4756-8fbe-3483cdafb9eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"# {\u0027owner\u0027: {\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}, \u0027members\u0027: []}\\n# {\u0027owner\u0027: None, \u0027members\u0027: [{\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}]}\\nowner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\nincident.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0z9atne\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kwuavs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0z9atne\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0z77voh\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0kwuavs\" sourceRef=\"ServiceTask_0z77voh\" targetRef=\"EndEvent_05qhqog\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bm4wjs\"\u003e\u003ctext\u003eResults returned in an incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0y01zho\" sourceRef=\"ServiceTask_0z77voh\" targetRef=\"TextAnnotation_0bm4wjs\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05qhqog\" id=\"EndEvent_05qhqog_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"505\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0z77voh\" id=\"ServiceTask_0z77voh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"300\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z9atne\" id=\"SequenceFlow_0z9atne_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"300\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"249\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kwuavs\" id=\"SequenceFlow_0kwuavs_di\"\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bm4wjs\" id=\"TextAnnotation_0bm4wjs_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"107\" x=\"429\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0y01zho\" id=\"Association_0y01zho_di\"\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Get owner and member contact information for an Incident",
      "export_key": "example_soar_utilities_get_incident_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664750817402,
      "name": "Example: SOAR Utilities Get Incident Contact Info",
      "object_type": "incident",
      "programmatic_name": "example_soar_utilities_get_incident_contact_info",
      "tags": [
        {
          "tag_handle": "fn_soar_utils",
          "value": null
        }
      ],
      "uuid": "da40c7a7-dcb8-40d5-a6dd-954600796854",
      "workflow_id": 86
    }
  ],
  "workspaces": []
}
