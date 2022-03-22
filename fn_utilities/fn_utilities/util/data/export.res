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
      "export_key": "Example: (Artifact) Attachment to Base64",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: (Artifact) Attachment to Base64",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c3792981-ca39-431b-b0b0-69b9c789e2a1",
      "view_items": [],
      "workflows": [
        "example_artifact_attachment_to_base64"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Attachment Hash",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Attachment Hash",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fd7a46d6-f7e3-4942-95b0-646b86884896",
      "view_items": [],
      "workflows": [
        "example_attachment_hash"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Attachment to Base64",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Attachment to Base64",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b1486e69-916c-469e-9a3e-803cffa7585e",
      "view_items": [],
      "workflows": [
        "example_attachment_to_base64"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Call REST API",
      "id": 37,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Call REST API",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "18832253-73eb-4299-a437-db620ad4a55c",
      "view_items": [],
      "workflows": [
        "example_call_rest_api"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "DNS Name",
            "URL",
            "Email Sender",
            "Email Recipient",
            "String",
            "URL Referer",
            "URI Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Domain Distance",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Domain Distance",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "be2f9c81-7c75-4217-a0de-03004bf958cc",
      "view_items": [],
      "workflows": [
        "example_domain_distance"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "RFC 822 Email Message File",
            "Email Attachment",
            "Other File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Email Parsing (Artifact)",
      "id": 19,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Email Parsing (Artifact)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f7517b02-8cb5-47e7-afbc-93f7509be67d",
      "view_items": [],
      "workflows": [
        "example_email_parsing_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Email Parsing (Attachment)",
      "id": 20,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Email Parsing (Attachment)",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8221e851-9b18-40e5-94ee-d8db606ae4c7",
      "view_items": [],
      "workflows": [
        "example_email_parsing_attachment"
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
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: Expand URL",
      "id": 21,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Expand URL",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "efe2ef52-07ea-440c-804f-794a32ed68ab",
      "view_items": [],
      "workflows": [
        "utilities_expand_url"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "DNS Name",
            "URL",
            "URI Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Extract SSL Certificate",
      "id": 22,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extract SSL Certificate",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2c10d4c8-0c4a-437f-9397-a37f4def90d9",
      "view_items": [],
      "workflows": [
        "example_extract_ssl_cert_from_url"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Get Incident Contact Info",
      "id": 23,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Get Incident Contact Info",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4c4bc600-eda9-42a7-90da-7116cc4fa71f",
      "view_items": [],
      "workflows": [
        "example_get_incident_contact_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Get Task Contact Info",
      "id": 38,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Get Task Contact Info",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "857c9cd6-dc45-46a5-b287-82831b4eab52",
      "view_items": [],
      "workflows": [
        "example_get_task_contact_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: JSON2HTML",
      "id": 24,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: JSON2HTML",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5cc2da3f-55e4-4068-ba9e-1ef207ac7763",
      "view_items": [],
      "workflows": [
        "example_json2html"
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
          "value": "X509 Certificate File"
        }
      ],
      "enabled": true,
      "export_key": "Example: Parse SSL Certificate",
      "id": 25,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse SSL Certificate",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b9a81baf-4583-4c7a-8263-9bd26e6da46d",
      "view_items": [],
      "workflows": [
        "example_parse_ssl_certificate"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: PDFiD",
      "id": 26,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: PDFiD",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5da12eac-d54c-481b-b4cc-9997c76ccfa9",
      "view_items": [],
      "workflows": [
        "example_pdfid"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Resilient Search",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Resilient Search",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f427051f-fe61-47d6-ab12-173156a1bf97",
      "view_items": [],
      "workflows": [
        "example_resilient_search"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Shell Command",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Shell Command",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d53a8ea9-9f5f-4f1c-a8c1-e57ec7e9011f",
      "view_items": [],
      "workflows": [
        "example_shell_command"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: String to Attachment",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: String to Attachment",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4cc2f402-8a7b-4590-b4da-09376e3dedb5",
      "view_items": [],
      "workflows": [
        "example_string_to_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Timer Epoch",
      "id": 30,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Timer Epoch",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bcd95c08-bff0-4dfe-bf8f-f405bafd50e5",
      "view_items": [
        {
          "content": "897a041c-34e9-4c83-bd16-cf30adaee1c2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_timer"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Timers in Parallel",
      "id": 31,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Timers in Parallel",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e88d9e23-b3f5-4039-bd32-c105d9ed981a",
      "view_items": [
        {
          "content": "0f6ded80-e607-434a-8806-28715387ef71",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_timer_parallel"
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
          "value": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
      ],
      "enabled": true,
      "export_key": "Example: Use Excel Data",
      "id": 32,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Use Excel Data",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d5e9630d-684f-442c-9b09-4d3fb240ba34",
      "view_items": [
        {
          "content": "1ca20f57-8c5e-42ac-b7e1-3a08bf0eafeb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e7d3b83d-af8f-4bd4-a6cd-1b47e78c81c7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_create_artifacts_from_excel_data"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "Email Attachment",
            "Malware Sample",
            "Log File",
            "Other File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: XML Transformation",
      "id": 33,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: XML Transformation",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "53db3647-7eed-49fd-8120-b8bbb7e25795",
      "view_items": [],
      "workflows": [
        "example_xml_transformation"
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
      "export_key": "Example: Zip Extract",
      "id": 34,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Zip Extract",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5a984f4b-e3a0-45ab-a608-cb8be4e2d35a",
      "view_items": [
        {
          "content": "c584c1de-292c-4275-b588-1cea4e7aac08",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9061da85-a084-49e8-b8e5-6acff43bc536",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_zip_to_artifact"
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
      "export_key": "Example: Zip List",
      "id": 35,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Zip List",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6bfc4b46-a87c-4602-a6a3-7514b95cb177",
      "view_items": [],
      "workflows": [
        "example_zip_list"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647957127179,
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
      "export_key": "__function/utilities_parse_email_attachments",
      "hide_notification": false,
      "id": 260,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "utilities_parse_email_attachments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "utilities_parse_email_attachments",
      "tooltip": "If set to True, attachments found in the email file will be attached as Artifacts",
      "type_id": 11,
      "uuid": "80a22483-2db6-49c9-9a37-6cc29bb0db6f",
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
      "id": 261,
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
      "tags": [],
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
      "export_key": "__function/rest_headers",
      "hide_notification": false,
      "id": 262,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_headers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_headers",
      "tooltip": "",
      "type_id": 11,
      "uuid": "838ae9f2-fd48-4149-b6b0-7fc611673eaf",
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
      "export_key": "__function/shell_command",
      "hide_notification": false,
      "id": 263,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shell_command",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shell_command",
      "tooltip": "shell_command if  shell_remote false. remote_shell_command:remote_machine if shell remote true.",
      "type_id": 11,
      "uuid": "8405293e-4d78-44e2-ba9a-91a29674ea4c",
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
      "export_key": "__function/domain_name",
      "hide_notification": false,
      "id": 264,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "domain_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "domain_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8b066fbf-419c-4a8d-a3bf-2badfa475d23",
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
      "export_key": "__function/https_url",
      "hide_notification": false,
      "id": 265,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "https_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "https_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "94f1875f-297e-4056-bc50-42f8b242efab",
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
      "export_key": "__function/zipfile_password",
      "hide_notification": false,
      "id": 266,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zipfile_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "zipfile_password",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9ab219d3-d31e-407c-9cbb-a07c76c649a1",
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
      "export_key": "__function/rest_verify",
      "hide_notification": false,
      "id": 267,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "rest_verify",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_verify",
      "tooltip": "Verify SSL certificate?",
      "type_id": 11,
      "uuid": "9c32f347-a610-4f0f-8cf7-fad03be630ea",
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
      "export_key": "__function/resilient_url",
      "hide_notification": false,
      "id": 268,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "resilient_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "resilient_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a7e02d64-648a-4b63-be75-e33f0ebfc231",
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
      "export_key": "__function/content_type",
      "hide_notification": false,
      "id": 269,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "content_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "content_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ae9b660d-a66b-4a4e-b216-9aa53f747c89",
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
      "export_key": "__function/excel_ranges",
      "hide_notification": false,
      "id": 270,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "excel_ranges",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "excel_ranges",
      "tooltip": "Accepts a list of ranges in Excel notation, e.g.: \"Shee1\"!A1:B2, \u0027Sheet2\u0027!C3",
      "type_id": 11,
      "uuid": "b7dff025-dc52-4aa2-a531-3cddc2278b6b",
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
      "export_key": "__function/rest_url",
      "hide_notification": false,
      "id": 271,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rest_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "bed5261f-4400-45ed-9cba-a8612ac4e74f",
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
      "export_key": "__function/xml_stylesheet",
      "hide_notification": false,
      "id": 272,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xml_stylesheet",
      "operation_perms": {},
      "operations": [],
      "placeholder": "transform.xslt",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xml_stylesheet",
      "tooltip": "name of stylesheet to use for the transformation",
      "type_id": 11,
      "uuid": "bf98e57f-ee63-4a6f-b115-eb1b25653a6e",
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
      "export_key": "__function/utilities_certificate",
      "hide_notification": false,
      "id": 273,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "utilities_certificate",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "utilities_certificate",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c58f6307-9f7e-4067-9f8f-c98d714dac0f",
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
      "export_key": "__function/resilient_search_query",
      "hide_notification": false,
      "id": 274,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "resilient_search_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "resilient_search_query",
      "tooltip": "",
      "type_id": 11,
      "uuid": "caa9ac7a-2342-4062-9a99-a7f75f3eb0e9",
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
      "id": 275,
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
      "tags": [],
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
      "export_key": "__function/resilient_search_template",
      "hide_notification": false,
      "id": 276,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "resilient_search_template",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 1,
          "name": "Attachments",
          "template": {
            "content": "{\n  \"types\": [\"attachment\"],\n  \"filters\": {\n    \"incident\": [{\n        \"conditions\": [{\"field_name\": \"plan_status\", \"method\": \"in\", \"value\": [\"A\"]}]\n      }]\n  }\n}",
            "format": "text"
          },
          "uuid": "c680551e-0d18-4176-a9c5-10381701c848"
        },
        {
          "id": 2,
          "name": "Artifacts",
          "template": {
            "content": "{\n  \"types\": [\"artifact\"],\n  \"filters\": {\n    \"incident\": [{\n        \"conditions\": [{\"field_name\": \"plan_status\", \"method\": \"in\", \"value\": [\"A\"]}]\n      }]\n  }\n}",
            "format": "text"
          },
          "uuid": "1e25a6f4-0fe8-4f73-9eee-9210c07cff50"
        }
      ],
      "text": "resilient_search_template",
      "tooltip": "",
      "type_id": 11,
      "uuid": "dbc6da92-d1ae-43fa-9ff7-032de8cfb8f2",
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
      "export_key": "__function/base64content",
      "hide_notification": false,
      "id": 277,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "base64content",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "base64content",
      "tooltip": "",
      "type_id": 11,
      "uuid": "eabbb71e-334b-4765-b143-3dc3427ba273",
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
      "export_key": "__function/shell_param2",
      "hide_notification": false,
      "id": 278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shell_param2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shell_param2",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ebab7d4b-9510-4cf7-b875-3a916c5bb2bf",
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
      "export_key": "__function/shell_remote",
      "hide_notification": false,
      "id": 279,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "shell_remote",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shell_remote",
      "tooltip": "Yes if running a remote powershell script. No otherwise.",
      "type_id": 11,
      "uuid": "ece49b2b-4495-47cd-b6d4-990048260ebf",
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
      "export_key": "__function/xml_source",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xml_source",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xml_source",
      "tooltip": "xml document to transform or empty when using attachments",
      "type_id": 11,
      "uuid": "f72858a9-f4d2-459b-91c9-5e3dac0b80a8",
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
      "id": 281,
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
      "tags": [],
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
      "export_key": "__function/file_path",
      "hide_notification": false,
      "id": 282,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "file_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "file_path",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f9633eec-4afe-4e09-bd9a-8f63a45c55f0",
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
      "id": 283,
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
      "export_key": "__function/file_name",
      "hide_notification": false,
      "id": 284,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "file_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "file_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0c493e99-1135-4bea-9709-3aafbc492399",
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
      "id": 285,
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
      "tags": [],
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
      "export_key": "__function/artifact_file_type",
      "hide_notification": false,
      "id": 286,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_file_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_file_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "247c1025-f582-4641-9ce6-5da976797e50",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Attachment",
          "properties": null,
          "uuid": "930b255d-468c-4f45-95db-12b7e690ca7d",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Malware Sample",
          "properties": null,
          "uuid": "ae1cf279-942b-4609-b2e1-806162e1b151",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Log File",
          "properties": null,
          "uuid": "c326aaeb-f779-4938-8133-7526f188c006",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "X509 Certificate File",
          "properties": null,
          "uuid": "e029ee34-9dc5-471b-90a8-40de17776ea7",
          "value": 55
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RFC 822 Email Message File",
          "properties": null,
          "uuid": "6720a846-a4b1-46ec-b0c8-d8900f0a92a1",
          "value": 56
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other File",
          "properties": null,
          "uuid": "ff9f511e-8b6f-441c-8c0c-dd092893575f",
          "value": 57
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
      "export_key": "__function/json2html_data",
      "hide_notification": false,
      "id": 287,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "json2html_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "json2html_data",
      "tooltip": "json data to convert to html",
      "type_id": 11,
      "uuid": "254477f5-5999-432f-b509-66575b59a7e2",
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
      "export_key": "__function/domain_list",
      "hide_notification": false,
      "id": 288,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "domain_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "domain_list",
      "tooltip": "",
      "type_id": 11,
      "uuid": "254ea65e-c572-474b-8a94-2fc31225de16",
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
      "export_key": "__function/shell_param1",
      "hide_notification": false,
      "id": 289,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shell_param1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shell_param1",
      "tooltip": "",
      "type_id": 11,
      "uuid": "295a6d5a-bec3-4dac-b6f7-8c8f0cf37203",
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
      "export_key": "__function/utilities_time",
      "hide_notification": false,
      "id": 290,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "utilities_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "60s",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "utilities_time",
      "tooltip": "Specify time to wait as a string value/units where units is \u0027s\u0027 for seconds, \u0027m\u0027 for minutes \u0027h\u0027 for hours and \u0027d\u0027 for days. For example: 60 seconds : \"60s\"; 45 minutes : \"45m\"; 12 hours : 12h",
      "type_id": 11,
      "uuid": "2e1b9634-f5bc-475e-926b-808493e286b7",
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
      "export_key": "__function/utilities_epoch",
      "hide_notification": false,
      "id": 291,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "utilities_epoch",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "utilities_epoch",
      "tooltip": "Epoch specifying the time the timer should end",
      "type_id": 11,
      "uuid": "3357b810-3218-4cdd-8231-8d447c05a0ba",
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
      "export_key": "__function/description",
      "hide_notification": false,
      "id": 292,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "3c82d51d-265f-464c-aac4-57de599cea8a",
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
      "export_key": "__function/rest_method",
      "hide_notification": false,
      "id": 293,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "rest_method",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_method",
      "tooltip": "",
      "type_id": 11,
      "uuid": "4c1c5d09-87f0-4fb5-a236-00690b66db92",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "GET",
          "properties": null,
          "uuid": "660ae4ba-3a9d-45e5-9b08-10c5722ba780",
          "value": 58
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HEAD",
          "properties": null,
          "uuid": "5e2ff102-1222-47b4-8a71-83a90b4c8e81",
          "value": 59
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "POST",
          "properties": null,
          "uuid": "1ddb515c-5ab5-4dc2-8ca0-c37b8a72eedd",
          "value": 60
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PUT",
          "properties": null,
          "uuid": "91968afb-e4d5-4a2e-8e37-ac6a26e1569f",
          "value": 61
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DELETE",
          "properties": null,
          "uuid": "8af9df69-0c74-4708-bc4f-ea9bcc8fa01c",
          "value": 62
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "OPTIONS",
          "properties": null,
          "uuid": "67db4b2f-6da8-4f8a-a5df-e30817be8bf3",
          "value": 63
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PATCH",
          "properties": null,
          "uuid": "94486df3-4ab1-44df-8ad9-b160a095652d",
          "value": 64
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
      "export_key": "__function/string_to_convert_to_attachment",
      "hide_notification": false,
      "id": 294,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "string_to_convert_to_attachment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "string_to_convert_to_attachment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "50f06fff-4319-419d-b230-f22d4e7d6ec9",
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
      "export_key": "__function/shell_param3",
      "hide_notification": false,
      "id": 295,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shell_param3",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shell_param3",
      "tooltip": "",
      "type_id": 11,
      "uuid": "52e3f41c-f5b3-4788-bff9-5a3a29d95d0e",
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
      "export_key": "__function/json2html_keys",
      "hide_notification": false,
      "id": 296,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "json2html_keys",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "json2html_keys",
      "tooltip": "Limit portion of json to render. Example: key1[.key2[...]]",
      "type_id": 11,
      "uuid": "58f0bd61-cec6-4d85-9ab1-c72f8f5722cb",
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
      "export_key": "__function/rest_cookies",
      "hide_notification": false,
      "id": 297,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_cookies",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 3,
          "name": "rest_cookies_example",
          "template": {
            "content": "cookie1: one\ncookie2: two",
            "format": "text"
          },
          "uuid": "1b4168a8-2e4e-4956-a158-b6b96f2ae274"
        }
      ],
      "text": "rest_cookies",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5fae4c55-6eed-4bca-95df-2eaf44030d72",
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
      "export_key": "__function/rest_body",
      "hide_notification": false,
      "id": 298,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_body",
      "tooltip": "",
      "type_id": 11,
      "uuid": "746d0b25-9747-4094-909c-aea5c3431e2f",
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
      "export_key": "__function/excel_defined_names",
      "hide_notification": false,
      "id": 299,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "excel_defined_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "excel_defined_names",
      "tooltip": "Accepts a list of comma separated names of defined ranges, e.g.: test1, test2",
      "type_id": 11,
      "uuid": "7d639e07-1faf-4269-89bd-c99882f26614",
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
      "export_key": "actioninvocation/utilities_timer_end_time",
      "hide_notification": false,
      "id": 254,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "utilities_timer_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Utilities Timer end time",
      "tooltip": "",
      "type_id": 6,
      "uuid": "897a041c-34e9-4c83-bd16-cf30adaee1c2",
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
      "export_key": "actioninvocation/zip_password",
      "hide_notification": false,
      "id": 255,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zip_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ZIP Password",
      "tooltip": "",
      "type_id": 6,
      "uuid": "9061da85-a084-49e8-b8e5-6acff43bc536",
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
      "export_key": "actioninvocation/extract_file_path",
      "hide_notification": false,
      "id": 256,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extract_file_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "path/to/file.txt",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Extract file path",
      "tooltip": "enter file location within zip archive",
      "type_id": 6,
      "uuid": "c584c1de-292c-4275-b588-1cea4e7aac08",
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
      "export_key": "actioninvocation/excel_named_range",
      "hide_notification": false,
      "id": 257,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "excel_named_range",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Excel Named Range",
      "tooltip": "Specify a named ranged defined in the spreadsheet",
      "type_id": 6,
      "uuid": "e7d3b83d-af8f-4bd4-a6cd-1b47e78c81c7",
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
      "export_key": "actioninvocation/parallel_timers",
      "hide_notification": false,
      "id": 258,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parallel_timers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "1m,15s",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "parallel timers",
      "tooltip": "A comma separated list containing time to pause for each of 2 Timer instances. Timer string is \"time value\" concatenated with \"time unit\" character: \u2018s\u2019 for seconds; \u2018m\u2019 for minutes; \u2018h\u2019 for hours; \u2018d\u2019 for days",
      "type_id": 6,
      "uuid": "0f6ded80-e607-434a-8806-28715387ef71",
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
      "export_key": "actioninvocation/excel_range",
      "hide_notification": false,
      "id": 259,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "excel_range",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"Sheet1\"!A2:C8",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Excel Range",
      "tooltip": "Use worksheet and range values for cells to extract",
      "type_id": 6,
      "uuid": "1ca20f57-8c5e-42ac-b7e1-3a08bf0eafeb",
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
      "created_date": 1647872649609,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Calculate hashes for a file attachment. Returns `md5`, `sha1`, `sha256` and other hashes of the file content. Those hashes can then be used as artifacts or in other parts of your workflows.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Attachment Hash",
      "export_key": "utilities_attachment_hash",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872649660,
      "name": "utilities_attachment_hash",
      "tags": [],
      "uuid": "9e0f46f4-ae8c-4aa6-a296-3a0662a53386",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Attachment Hash",
          "object_type": "attachment",
          "programmatic_name": "example_attachment_hash",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1647872649698,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Reads a file attachment in the incident, and produces a base64-encoded string with the file attachment content. This content can then be used in combination with other workflow functions to create an artifact, a new file attachment, or to analyze the contents using various tools.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Attachment to Base64",
      "export_key": "utilities_attachment_to_base64",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872649756,
      "name": "utilities_attachment_to_base64",
      "tags": [],
      "uuid": "3a4b66c4-0465-4960-8bbf-fa3ebdc58c5a",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: (Artifact) Attachment to Base64",
          "object_type": "artifact",
          "programmatic_name": "example_artifact_attachment_to_base64",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Attachment to Base64",
          "object_type": "attachment",
          "programmatic_name": "example_attachment_to_base64",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: PDFiD",
          "object_type": "attachment",
          "programmatic_name": "example_pdfid",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1647872649794,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Extracts a file from a ZIP file attachment, producing a base64 string.\n\nThat string can then be used as input to subsequent functions that might write it as a file attachment, as a malware sample artifact, or in other ways.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Attachment Zip Extract",
      "export_key": "utilities_attachment_zip_extract",
      "id": 3,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872649844,
      "name": "utilities_attachment_zip_extract",
      "tags": [],
      "uuid": "4d9fb1df-1eab-494b-8375-c4feb0525429",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "content": "f9633eec-4afe-4e09-bd9a-8f63a45c55f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9ab219d3-d31e-407c-9cbb-a07c76c649a1",
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
          "name": "Example: Zip Extract",
          "object_type": "attachment",
          "programmatic_name": "example_zip_to_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1647872649874,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Reads a ZIP file and produces a list of the file paths, and a list with detailed information about each file.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Attachment Zip List",
      "export_key": "utilities_attachment_zip_list",
      "id": 4,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872649920,
      "name": "utilities_attachment_zip_list",
      "tags": [],
      "uuid": "c28c15ac-ecd2-4cd8-ba85-8f8c2bb307d2",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Zip List",
          "object_type": "attachment",
          "programmatic_name": "example_zip_list",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1647872649950,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Creates a new artifact from a Base64 string. You can  specify the artifact type and description.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Base64 to Artifact",
      "export_key": "utilities_base64_to_artifact",
      "id": 5,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872649997,
      "name": "utilities_base64_to_artifact",
      "tags": [],
      "uuid": "e82fa06a-584c-4f8d-9429-448ddc3d8bc4",
      "version": 1,
      "view_items": [
        {
          "content": "eabbb71e-334b-4765-b143-3dc3427ba273",
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
          "content": "247c1025-f582-4641-9ce6-5da976797e50",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c493e99-1135-4bea-9709-3aafbc492399",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae9b660d-a66b-4a4e-b216-9aa53f747c89",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3c82d51d-265f-464c-aac4-57de599cea8a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": []
    },
    {
      "created_date": 1647872650026,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Creates a new attachment from a base64 string.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Base64 to Attachment",
      "export_key": "utilities_base64_to_attachment",
      "id": 6,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650074,
      "name": "utilities_base64_to_attachment",
      "tags": [],
      "uuid": "11349159-153e-49b7-9a9b-e22676c03687",
      "version": 1,
      "view_items": [
        {
          "content": "eabbb71e-334b-4765-b143-3dc3427ba273",
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
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c493e99-1135-4bea-9709-3aafbc492399",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae9b660d-a66b-4a4e-b216-9aa53f747c89",
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
          "name": "Example: Zip Extract",
          "object_type": "attachment",
          "programmatic_name": "example_zip_to_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1647872650105,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function calls a REST web service. It supports the standard REST methods: GET, HEAD, POST, PUT, DELETE and OPTIONS.\n\nThe function parameters determine the type of call, the URL, and optionally the headers and body. The results include the text or structured (JSON) result from the web service, and additional information including the elapsed time.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Call REST API",
      "export_key": "utilities_call_rest_api",
      "id": 7,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650158,
      "name": "utilities_call_rest_api",
      "tags": [],
      "uuid": "47ca08b2-bc06-4ad0-a5ed-d8df6d33045b",
      "version": 1,
      "view_items": [
        {
          "content": "4c1c5d09-87f0-4fb5-a236-00690b66db92",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bed5261f-4400-45ed-9cba-a8612ac4e74f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "838ae9f2-fd48-4149-b6b0-7fc611673eaf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5fae4c55-6eed-4bca-95df-2eaf44030d72",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "746d0b25-9747-4094-909c-aea5c3431e2f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9c32f347-a610-4f0f-8cf7-fad03be630ea",
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
          "name": "Example: Call REST API",
          "object_type": "artifact",
          "programmatic_name": "example_call_rest_api",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        }
      ]
    },
    {
      "created_date": 1647872650191,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Identifies similarity between a suspicious domain name and a list of valid domain names.  Low distance result indicates a possible spoof attempt.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Domain Distance",
      "export_key": "utilities_domain_distance",
      "id": 8,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650238,
      "name": "utilities_domain_distance",
      "tags": [],
      "uuid": "6fd01564-96de-4482-bceb-cf396df6c758",
      "version": 1,
      "view_items": [
        {
          "content": "8b066fbf-419c-4a8d-a3bf-2badfa475d23",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "254ea65e-c572-474b-8a94-2fc31225de16",
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
          "name": "Example: Domain Distance",
          "object_type": "artifact",
          "programmatic_name": "example_domain_distance",
          "tags": [],
          "uuid": null,
          "workflow_id": 13
        }
      ]
    },
    {
      "created_date": 1647872650269,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Extracts message headers and body parts from an email message (.eml or .msg).\n\nAny attachments found are added to the incident as artifacts if `utilities_parse_email_attachments` is set to True.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Email Parse",
      "export_key": "utilities_email_parse",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650315,
      "name": "utilities_email_parse",
      "tags": [],
      "uuid": "d83f571e-8904-4123-9c2c-3f404b00cc5e",
      "version": 1,
      "view_items": [
        {
          "content": "eabbb71e-334b-4765-b143-3dc3427ba273",
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
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a22483-2db6-49c9-9a37-6cc29bb0db6f",
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
          "name": "Example: Email Parsing (Artifact)",
          "object_type": "artifact",
          "programmatic_name": "example_email_parsing_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 8
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Email Parsing (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_email_parsing_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1647872650346,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Extracts ranges of data or named ranges specified by the user from a Microsoft Excel document.\n\nThe function uses a Python library called openpyxl (http://openpyxl.readthedocs.io/en/stable/) to interface with Excel files.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Excel Query",
      "export_key": "utilities_excel_query",
      "id": 10,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650391,
      "name": "utilities_excel_query",
      "tags": [],
      "uuid": "118bd2c6-f367-4342-93b8-50257121ccf2",
      "version": 1,
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
          "content": "b7dff025-dc52-4aa2-a531-3cddc2278b6b",
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
          "content": "7d639e07-1faf-4269-89bd-c99882f26614",
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
          "name": "Example: Create Artifacts From Excel Data",
          "object_type": "attachment",
          "programmatic_name": "example_create_artifacts_from_excel_data",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        }
      ]
    },
    {
      "created_date": 1647872650421,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Takes a URL (mostly shortened) and follows it through redirects as it expands. The results include each URL, which are added to a new artifact.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Expand URL",
      "export_key": "utilities_expand_url",
      "id": 11,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650466,
      "name": "utilities_expand_url",
      "tags": [],
      "uuid": "173d3d51-3263-4f26-b927-ecd1e2bf6344",
      "version": 1,
      "view_items": [
        {
          "content": "a7e02d64-648a-4b63-be75-e33f0ebfc231",
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
          "name": "Example: Expand URL",
          "object_type": "artifact",
          "programmatic_name": "utilities_expand_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        }
      ]
    },
    {
      "created_date": 1647872650495,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function takes in a HTTPS URL or DNS input, establishes a connection and then attempts to acquire the SSL certificate. If successful, the function then saves the certificate as an artifact of type \u2018X509 Certificate File\u2019. Works on most URLs including those with self-signed or expired certificates.\n\nThe output of this function is a string representation of the certificate saved in PEM format.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Extract SSL Cert From Url",
      "export_key": "utilities_extract_ssl_cert_from_url",
      "id": 12,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650540,
      "name": "utilities_extract_ssl_cert_from_url",
      "tags": [],
      "uuid": "69123885-b3b9-4df9-a241-aaa29ba9d7d6",
      "version": 1,
      "view_items": [
        {
          "content": "94f1875f-297e-4056-bc50-42f8b242efab",
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
          "name": "Example: Extract SSL Cert from URL",
          "object_type": "artifact",
          "programmatic_name": "example_extract_ssl_cert_from_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 21
        }
      ]
    },
    {
      "created_date": 1647872650574,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Retrieves contact information of the owner and members of an incident or task.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Get Contact Info",
      "export_key": "utilities_get_contact_info",
      "id": 13,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650627,
      "name": "utilities_get_contact_info",
      "tags": [],
      "uuid": "011e399a-4508-4684-986a-e49a8be0b20b",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Get Incident Contact Info",
          "object_type": "incident",
          "programmatic_name": "example_get_incident_contact_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 20
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Get Task Contact Info",
          "object_type": "task",
          "programmatic_name": "example_get_task_contact_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 24
        }
      ]
    },
    {
      "created_date": 1647872650656,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Produces an HTML representation of JSON data. All data is converted into tables of key / value pairs or lists.\n\nProvide an optional parameter `json2html_keys` to limit the JSON data to display.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: JSON2HTML",
      "export_key": "utilities_json2html",
      "id": 14,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650709,
      "name": "utilities_json2html",
      "tags": [],
      "uuid": "7460c6a9-8c2a-42fb-a871-bef9b37c9e9a",
      "version": 1,
      "view_items": [
        {
          "content": "254477f5-5999-432f-b509-66575b59a7e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "58f0bd61-cec6-4d85-9ab1-c72f8f5722cb",
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
          "name": "Example: JSON2HTML",
          "object_type": "artifact",
          "programmatic_name": "example_json2html",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1647872650739,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function produces the structured data from a provided SSL certificate. Three inputs are accepted by the function. There are 2 defined ways to use this function for parsing certificates.\n\nOption 1 involves providing a JSON-encoded representation of a certificate. In this case the certificate input parameter should be this JSON string.\n\nOption 2 involves providing a certificate file for parsing. When the rule is triggered on an artifact, both the incident_id for that incident and the artifact_id for the specified certificate file must be provided.\n\nNOTE: The Parse SSL Certificate function expects a certificate of type PEM. If you require a way to get a PEM formatted certificate from a URL consider using this in conjunction with the Extract SSL Cert from URL function.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Parse SSL Certificate",
      "export_key": "utilities_parse_ssl_certificate",
      "id": 15,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650815,
      "name": "utilities_parse_ssl_certificate",
      "tags": [],
      "uuid": "029f623a-ae74-406e-91a5-366a7005d1b0",
      "version": 1,
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
          "content": "c58f6307-9f7e-4067-9f8f-c98d714dac0f",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Parse SSL Certificate",
          "object_type": "artifact",
          "programmatic_name": "example_parse_ssl_certificate",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    },
    {
      "created_date": 1647872650849,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Produces summary information about the structure of a PDF file, using Didier Stevens\u0027 pdfid (https://blog.didierstevens.com/programs/pdf-tools/). Provide the PDF file content as a base64-encoded string, for example the output from the \u201cAttachment to Base64\u201d function.\n\nThis function is useful in initial triage of suspicious email attachments and other files. It allows you to identify PDF documents that contain (for example) JavaScript or that execute an action when opened. PDFiD also handles name obfuscation. The combination of PDF automatic action and JavaScript makes a document very suspicious.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: PDFiD",
      "export_key": "utilities_pdfid",
      "id": 16,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647887980934,
      "name": "utilities_pdfid",
      "tags": [],
      "uuid": "3f9da4a2-cdac-4aa6-891c-1217565e734c",
      "version": 3,
      "view_items": [
        {
          "content": "eabbb71e-334b-4765-b143-3dc3427ba273",
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
          "name": "Example: PDFiD",
          "object_type": "attachment",
          "programmatic_name": "example_pdfid",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1647872650924,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function searches the Resilient platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, or incidents currently assigned to a given user, or a very wide range of other search conditions.\n\n**NOTE:** The search results may include data from incidents that the current Resilient user (the person who triggered the workflow) cannot access. Often your Resilient users have the `Default` role that allows them to only see incidents where they are members. This function runs with the permissions of your integration account, which typically may have much wider access privileges. **Use with caution, to avoid information disclosure.**",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Resilient Search",
      "export_key": "utilities_resilient_search",
      "id": 17,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872650962,
      "name": "utilities_resilient_search",
      "tags": [],
      "uuid": "213720b5-fc4b-4134-8d40-09c157608600",
      "version": 1,
      "view_items": [
        {
          "content": "dbc6da92-d1ae-43fa-9ff7-032de8cfb8f2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "caa9ac7a-2342-4062-9a99-a7f75f3eb0e9",
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
          "name": "Example: Resilient Search",
          "object_type": "attachment",
          "programmatic_name": "example_resilient_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    },
    {
      "created_date": 1647872650986,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function allows your workflows to execute shell-scripts locally or remotely, and return the result into the workflow. The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.\n\nThese functions can be run on any platform. If you install and run the resilient-circuits framework on Windows, this allows you to configure this function to run PowerShell scripts.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Shell Command",
      "export_key": "utilities_shell_command",
      "id": 18,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872651023,
      "name": "utilities_shell_command",
      "tags": [],
      "uuid": "0ecc7cb7-f448-4e9d-a38e-100ddbe7fd18",
      "version": 1,
      "view_items": [
        {
          "content": "8405293e-4d78-44e2-ba9a-91a29674ea4c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ece49b2b-4495-47cd-b6d4-990048260ebf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "295a6d5a-bec3-4dac-b6f7-8c8f0cf37203",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ebab7d4b-9510-4cf7-b875-3a916c5bb2bf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "52e3f41c-f5b3-4788-bff9-5a3a29d95d0e",
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
          "name": "Example: Shell Command",
          "object_type": "artifact",
          "programmatic_name": "example_shell_command",
          "tags": [],
          "uuid": null,
          "workflow_id": 22
        }
      ]
    },
    {
      "created_date": 1647872651046,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Creates a new file (.txt) attachment in the incident or task from a string that your workflow provides as input.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: String to Attachment",
      "export_key": "utilities_string_to_attachment",
      "id": 19,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872651090,
      "name": "utilities_string_to_attachment",
      "tags": [],
      "uuid": "cd8a23ce-63ba-42cf-8eba-8b63d5e7c872",
      "version": 1,
      "view_items": [
        {
          "content": "50f06fff-4319-419d-b230-f22d4e7d6ec9",
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
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: String to Attachment",
          "object_type": "artifact",
          "programmatic_name": "example_string_to_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        }
      ]
    },
    {
      "created_date": 1647872651117,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This function implements a timer (sleep) function that when called from a workflow will cause the workflow to pause for the specified amount of time. The function takes one of two parameters as input: `utilities_time` or `utilities_epoch`.\n\nThe utilities_time parameter is a string that specifies the total amount of time to pause. The input string is of format `time value` concatenated with a `time unit` character, where character is:\n\u2022 `s` for seconds\n\u2022 `m` for minutes\n\u2022 `h` for hours\n\u2022 `d` for days\n\nFor example: `30s` = 30 seconds; `20m` = 20 minutes; `5h` = 5 hours; `6d` = 6 days\n\nThe `utilities_epoch` parameter is the epoch time that the timer function should stop sleeping. An epoch time value is returned from the date time picker UI widget.\n\nThe timer function will break down the total amount of time to pause into smaller sleep time intervals and check in between sleep time whether the workflow has been terminated while the function is running. If the workflow has been terminated, the function will end execution.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: Timer",
      "export_key": "utilities_timer",
      "id": 20,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872651173,
      "name": "utilities_timer",
      "tags": [],
      "uuid": "0aa9d601-0a7f-4741-999e-27d3bf6de4a8",
      "version": 1,
      "view_items": [
        {
          "content": "2e1b9634-f5bc-475e-926b-808493e286b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3357b810-3218-4cdd-8231-8d447c05a0ba",
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
          "name": "Example: Timer",
          "object_type": "incident",
          "programmatic_name": "example_timer",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Timers in Parallel",
          "object_type": "incident",
          "programmatic_name": "example_timer_parallel",
          "tags": [],
          "uuid": null,
          "workflow_id": 15
        }
      ]
    },
    {
      "created_date": 1647872651202,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Transforms an XML document using a preexisting `xsl` stylesheet. The resulting content is returned.",
        "format": "text"
      },
      "destination_handle": "fn_utilities",
      "display_name": "Utilities: XML Transformation",
      "export_key": "utilities_xml_transformation",
      "id": 21,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647872651245,
      "name": "utilities_xml_transformation",
      "tags": [],
      "uuid": "b97af810-b808-46d2-90ea-bc5cef1e2fab",
      "version": 1,
      "view_items": [
        {
          "content": "f72858a9-f4d2-459b-91c9-5e3dac0b80a8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bf98e57f-ee63-4a6f-b115-eb1b25653a6e",
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
          "name": "Example: XML Transformation",
          "object_type": "artifact",
          "programmatic_name": "example_xml_transformation",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 6,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647957125818,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647957125818,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_utilities",
      "name": "fn_utilities",
      "programmatic_name": "fn_utilities",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "25d68f25-a6d9-4571-bdd2-a567a574f231"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1647872647787,
      "creator_id": "admin@example.com",
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\nTypically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys (sorted if specified) as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.0",
      "id": 2,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872647812,
      "name": "Convert JSON to rich text v1.0",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text_v10",
      "script_text": "# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.\nVERSION = 1.0\n\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to define the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, { \n    \"version\": 1.0,\n    \"header\": \"Artifact scan results for\".format(artifact.value),\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr /\u003e\",\n    \"sort\": True,\n    \"json\": results.content,\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.0, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr /\u003e\"|list such as [\u0027\u003cspan\u003e\u0027,\u0027\u003c/span\u003e\u0027], [html separator between json keys and lists or defaults to html break: \u0027\u003cbr /\u003e\u0027. \n                                                If a list, then the data is brackets by the pair specified]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\"\"\"\n\nimport re\n\n# needed for python 3\ntry:\n    unicode(\"abc\")\nexcept:\n    unicode = str\n\n\nrc = re.compile(r\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#\\?]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n    \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n\n    def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr /\u003e\", sort_keys=False):\n        self.omit_keys = omit_keys\n        self.padding = padding\n        self.separator = separator\n        self.sort_keys = sort_keys\n\n\n    def format_link(self, item):\n        \"\"\"[summary]\n          Find embedded urls (http(s)) and add html anchor tags to display as links\n          Args:\n              item ([string])\n\n          Returns:\n              [str]: None|original text if no links|text with html links\n        \"\"\"\n        formatted_item = item\n        if item and not isinstance(item, (int, bool, float)):\n            list = rc.findall(item)\n            if list:\n                for link in list:\n                    formatted_item = formatted_item.replace(link, u\"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n        return formatted_item\n\n    def expand_list(self, list_value, is_list=False):\n        \"\"\"[summary]\n          convert items to html, adding indents to nested dictionaries.\n          Args:\n              list_value ([dict|list]): json element\n\n          Returns:\n              [str]: html converted code\n        \"\"\"\n        if not isinstance(list_value, list):\n            return self.format_link(list_value)\n        elif not list_value:\n            return u\"None\u003cbr\u003e\"\n\n        try:\n            items_list = []  # this will ensure list starts on second line of key label\n            for item in list_value:\n                if isinstance(item, dict):\n                    result = self.convert_json_to_rich_text(item)\n                    if is_list:\n                        items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(result))\n                    else:\n                        items_list.append(result)\n                elif isinstance(item, list):\n                    items_list.append(self.expand_list(item, is_list=True))\n                elif is_list:\n                    items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(self.format_link(unicode(item))))\n                else:\n                    items_list.append(self.format_link(unicode(item)))\n\n            expand_list_result = self.add_separator(self.separator if not is_list else u\"\",\n                                                    items_list,\n                                                    is_list=is_list)\n\n            if is_list:\n                return u\"\u003cul\u003e{}\u003c/ul\u003e\".format(expand_list_result)\n            else:\n                return u\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(expand_list_result)\n        except Exception as err:\n            return str(err)\n\n    def convert_json_to_rich_text(self, sub_dict):\n        \"\"\"[summary]\n          Walk dictionary tree and convert to html for better display\n          Args:\n              sub_dict ([type]): [description]\n\n          Returns:\n              [type]: [description]\n        \"\"\"\n        notes = []\n        if sub_dict:\n            keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n            for key in keys:\n                if key not in self.omit_keys:\n                    value = sub_dict[key]\n                    is_list = isinstance(value, list)\n                    item_list = [u\"\u003cstrong\u003e{0}\u003c/strong\u003e: \".format(key)]\n                    if isinstance(value, dict):\n                        convert_result = self.convert_json_to_rich_text(value)\n                        if convert_result:\n                            item_list.append(u\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, convert_result))\n                        else:\n                            item_list.append(u\"None\u003cbr\u003e\")\n                    else:\n                        item_list.append(self.expand_list(value, is_list=is_list))\n                    notes.append(self.add_separator(self.separator, u\"\".join(unicode(v) for v in item_list), is_list=is_list))\n\n        result_notes = u\"\".join(notes)\n        if isinstance(self.separator, list):\n            return result_notes\n        else:\n            return result_notes.replace(\n                u\"\u003c/div\u003e{0}\".format(self.separator), u\"\u003c/div\u003e\").replace(\n                u\"{0}\u003c/div\u003e\".format(self.separator), u\"\u003c/div\u003e\"\n            )  # tighten up result\n\n    def add_separator(self, separator, items, is_list=False):\n        \"\"\"\n        apply the separator to the data\n        :param separator: None, str or list such as [\u0027\u003cspan\u003e\u0027, \u0027\u003c/span\u003e\u0027]\n        :param items: str or list to add separator\n        :return: text with separator applied\n        \"\"\"\n        _items = items\n\n        if not _items:\n            return \"\u003cbr\u003e\"\n\n        if not isinstance(_items, list):\n            _items = [_items]\n\n        if isinstance(separator, list):\n            return u\"\".join([u\"{}{}{}\".format(separator[0], item, separator[1]) for item in _items])\n\n        return u\"{}{}\".format(separator.join(_items), separator if not is_list else u\"\")\n\ndef get_properties(property_name):\n    \"\"\"\n    Logic to collect the json and parameters from a workflow property.\n    Args:\n      property_name: workflow property to reference\n    Returns:\n      padding, separator, header, json_omit_list, incident_field, json, sort_keys\n    \"\"\"\n    if not workflow.properties.get(property_name):\n        helper.fail(\"workflow.properties.{} undefined\".format(property_name))\n    if not workflow.properties[property_name].get(\u0027json\u0027):\n        helper.fail(\"workflow.properties.{}.json undefined\".format(property_name))\n\n    padding = int(workflow.properties[property_name].get(\"padding\", 10))\n    separator = workflow.properties[property_name].get(\"separator\", u\"\u003cbr /\u003e\")\n    if isinstance(separator, list) and len(separator) != 2:\n        helper.fail(\"list of separators should be specified as a pair such as [\u0027\u003cdiv\u003e\u0027, \u0027\u003c/div\u003e\u0027]: {}\".format(separator))\n\n    header = workflow.properties[property_name].get(\"header\")\n    json_omit_list = workflow.properties[property_name].get(\"json_omit_list\")\n    if not json_omit_list:\n        json_omit_list = []\n    incident_field = workflow.properties[property_name].get(\"incident_field\")\n    json = workflow.properties[property_name].get(\"json\")\n    if not isinstance(json, dict):\n        helper.fail(\"json element is not formatted correctly: {}\".format(json))\n    sort_keys = bool(workflow.properties[property_name].get(\"sort\", False))\n\n    return padding, separator, header, json_omit_list, incident_field, json, sort_keys\n\n\n## S T A R T\nif \u0027workflow\u0027 in globals():\n    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\n\n    if header:\n        if isinstance(separator, list):\n            hdr = u\"{0}{1}{2}\".format(separator[0], header, separator[1])\n        else:\n            hdr = u\"{0}{1}\".format(header, separator)\n    else:\n        hdr = u\"\"\n\n    convert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\n    converted_json = convert.convert_json_to_rich_text(json)\n    result = u\"{}{}\".format(hdr, converted_json)\n\n    rich_text_note = helper.createRichText(result)\n    if incident_field:\n        incident[incident_field] = rich_text_note\n    else:\n        incident.addNote(rich_text_note)\n",
      "tags": [],
      "uuid": "f7276ff0-1770-4058-9e89-40ee79c6e41b"
    }
  ],
  "server_version": {
    "build_number": 7058,
    "major": 42,
    "minor": 0,
    "version": "42.0.7058"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_xml_transformation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_xml_transformation\" isExecutable=\"true\" name=\"Example: XML Transformation\"\u003e\u003cdocumentation\u003eTransform an XML document using a defined xsl transform file\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_17iplwm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0o2z20v\" name=\"Utilities: XML Transformation\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b97af810-b808-46d2-90ea-bc5cef1e2fab\"\u003e{\"inputs\":{\"bf98e57f-ee63-4a6f-b115-eb1b25653a6e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"cdcatalog.xslt\"}}},\"post_processing_script\":\"# results.content is the string representation of the transformed xml document\\ncontent = helper.createPlainText(results.content)\\nincident.addNote(content)\",\"pre_processing_script\":\"#inputs.xml_stylesheet = \\\"cdcatalog.xslt\\\"\\n# In most cases, the xml_soure will come from other sources. \\n# If need be, use fn_utilities to capture data from attachments\\ninputs.xml_source = \\\"\\\"\\\"\\n\u0026lt;?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?\u0026gt;\\n\u0026lt;catalog\u0026gt;\\n  \u0026lt;cd\u0026gt;\\n    \u0026lt;title\u0026gt;Empire Burlesque\u0026lt;/title\u0026gt;\\n    \u0026lt;artist\u0026gt;Bob Dylan\u0026lt;/artist\u0026gt;\\n    \u0026lt;country\u0026gt;USA\u0026lt;/country\u0026gt;\\n    \u0026lt;company\u0026gt;Columbia\u0026lt;/company\u0026gt;\\n    \u0026lt;price\u0026gt;10.90\u0026lt;/price\u0026gt;\\n    \u0026lt;year\u0026gt;1985\u0026lt;/year\u0026gt;\\n  \u0026lt;/cd\u0026gt;\\n  \u0026lt;cd\u0026gt;\\n    \u0026lt;title\u0026gt;Hide your heart\u0026lt;/title\u0026gt;\\n    \u0026lt;artist\u0026gt;Bonnie Tyler\u0026lt;/artist\u0026gt;\\n    \u0026lt;country\u0026gt;UK\u0026lt;/country\u0026gt;\\n    \u0026lt;company\u0026gt;CBS Records\u0026lt;/company\u0026gt;\\n    \u0026lt;price\u0026gt;9.90\u0026lt;/price\u0026gt;\\n    \u0026lt;year\u0026gt;1988\u0026lt;/year\u0026gt;\\n  \u0026lt;/cd\u0026gt;\\n  \u0026lt;cd\u0026gt;\\n    \u0026lt;title\u0026gt;Greatest Hits\u0026lt;/title\u0026gt;\\n    \u0026lt;artist\u0026gt;Dolly Parton\u0026lt;/artist\u0026gt;\\n    \u0026lt;country\u0026gt;USA\u0026lt;/country\u0026gt;\\n    \u0026lt;company\u0026gt;RCA\u0026lt;/company\u0026gt;\\n    \u0026lt;price\u0026gt;9.90\u0026lt;/price\u0026gt;\\n    \u0026lt;year\u0026gt;1982\u0026lt;/year\u0026gt;\\n  \u0026lt;/cd\u0026gt;\\n  \u0026lt;cd\u0026gt;\\n    \u0026lt;title\u0026gt;Still got the blues\u0026lt;/title\u0026gt;\\n    \u0026lt;artist\u0026gt;Gary Moore\u0026lt;/artist\u0026gt;\\n    \u0026lt;country\u0026gt;UK\u0026lt;/country\u0026gt;\\n    \u0026lt;company\u0026gt;Virgin records\u0026lt;/company\u0026gt;\\n    \u0026lt;price\u0026gt;10.20\u0026lt;/price\u0026gt;\\n    \u0026lt;year\u0026gt;1990\u0026lt;/year\u0026gt;\\n  \u0026lt;/cd\u0026gt;\\n\u0026lt;/catalog\u0026gt;\\n\\\"\\\"\\\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_17iplwm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tdfmlw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_17iplwm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0o2z20v\"/\u003e\u003cendEvent id=\"EndEvent_06y9q8e\"\u003e\u003cincoming\u003eSequenceFlow_0tdfmlw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tdfmlw\" sourceRef=\"ServiceTask_0o2z20v\" targetRef=\"EndEvent_06y9q8e\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00t1y4h\"\u003e\u003ctext\u003eoutput: results.content\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i405n3\" sourceRef=\"ServiceTask_0o2z20v\" targetRef=\"TextAnnotation_00t1y4h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1f6v9c9\"\u003e\u003ctext\u003einput: xml document to transform and xsl transform file\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1azw5mz\" sourceRef=\"ServiceTask_0o2z20v\" targetRef=\"TextAnnotation_1f6v9c9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0o2z20v\" id=\"ServiceTask_0o2z20v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17iplwm\" id=\"SequenceFlow_17iplwm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06y9q8e\" id=\"EndEvent_06y9q8e_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"417\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"435\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tdfmlw\" id=\"SequenceFlow_0tdfmlw_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"417\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00t1y4h\" id=\"TextAnnotation_00t1y4h_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"363\" y=\"88\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i405n3\" id=\"Association_1i405n3_di\"\u003e\u003comgdi:waypoint x=\"345\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1f6v9c9\" id=\"TextAnnotation_1f6v9c9_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"121\" x=\"160\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1azw5mz\" id=\"Association_1azw5mz_di\"\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"241\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Transform an XML document using a defined xsl transform file",
      "export_key": "example_xml_transformation",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872656049,
      "name": "Example: XML Transformation",
      "object_type": "artifact",
      "programmatic_name": "example_xml_transformation",
      "tags": [],
      "uuid": "929a2244-4030-4677-accc-3eee2352c64f",
      "workflow_id": 19
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_email_parsing_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_email_parsing_artifact\" isExecutable=\"true\" name=\"Example: Email Parsing (Artifact)\"\u003e\u003cdocumentation\u003eExample Workflow showing to parse an Email File (.eml or .msg) from an Artifact File. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0nwjr5i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1gnnr3k\" name=\"Utilities: Email Parse\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d83f571e-8904-4123-9c2c-3f404b00cc5e\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\nif not results.success:\\n  note_text = u\\\"\\\"\\\"Workflow \u0027Example: Email Parsing (Artifact)\u0027 Failed\u0026lt;br\u0026gt;\\n                  \u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(unicode(results.reason))\\n  \\n  incident.addNote(helper.createRichText(note_text))\\n\\nelse:\\n  email = results.content\\n  \\n  # Get Email Subject\\n  eml_subject = email.get(\\\"subject\\\", \\\"BLANK SUBJECT LINE\\\")\\n\\n  #########################################\\n  # Add Artifacts for Email Recipient: to #\\n  #########################################\\n  for eml_addr in email.get(\\\"to\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  #########################################\\n  # Add Artifacts for Email Recipient: cc #\\n  #########################################\\n  for eml_addr in email.get(\\\"cc\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  ########################################\\n  # Add Artifacts for Email Sender: from #\\n  ########################################\\n  for eml_addr in email.get(\\\"from\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Sender\\\", eml_addr[1], eml_addr[0])\\n\\n  ################################################\\n  # Add Artifacts for IPs found in Email Headers #\\n  ################################################\\n  for eml_header in email.get(\\\"received\\\", []):\\n    \\n    the_header = eml_header.get(\\\"from\\\", None)\\n    \\n    if the_header:\\n      ips = re.findall(\u0027(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\u0027, the_header)\\n      unique_ips = set(ips)\\n  \\n      for an_ip in unique_ips:\\n        if an_ip:\\n          incident.addArtifact(\\\"IP Address\\\", an_ip, u\\\"Hop {0} at {1}\\\\n\\\\nHeader: {2}\\\".format(eml_header.get(\\\"hop\\\", \\\"\\\"), eml_header.get(\\\"date_utc\\\", \\\"\\\"), the_header))\\n\\n  ##############################################\\n  # Add Artifacts for URLs found in Email Body #\\n  ##############################################\\n  urls = []\\n  for eml_body_content in [email.get(\\\"plain_body\\\", \\\"\\\"), email.get(\\\"html_body\\\", \\\"\\\")]:\\n    urls.extend(re.findall(\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026amp;+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027, eml_body_content))\\n\\n  uniq_urls = set(urls)\\n\\n  for a_url in uniq_urls:\\n    # Remove any backslash as regex can add\\n    a_url = a_url.replace(\u0027\\\\\\\\\u0027,\\\"\\\")\\n    if a_url:\\n      incident.addArtifact(\\\"URL\\\", a_url, \\\"Found in parsed Email\\\")\\n  \\n  ################################################\\n  # Add the Email Body as a Note to the Incident #\\n  ################################################\\n  if email.get(\\\"body\\\"):\\n    note_text = u\\\"\\\"\\\"\u0026lt;b\u0026gt;Parsed Email::\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Subject:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;From:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;To:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{2}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Body:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{3}\\\"\\\"\\\".format(unicode(eml_subject),\\n                                  unicode(email.get(\\\"from\\\", \\\"N/A\\\")),\\n                                  unicode(email.get(\\\"to\\\", \\\"N/A\\\")), \\n                                  unicode(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n  \\n  \u0027\u0027\u0027Uncomment this if you would like to add a (safer) plain_text only Note\\n  if email.get(\\\"plain_body\\\"):\\n    note_text = u\\\"\\\"\\\"Parsed Email::\\\\n\\\\nSubject:\\\\n{0}\\\\n\\\\nFrom:\\\\n{1}\\\\n\\\\nTo:\\\\n{2}\\\\n\\\\nBody:\\\\n{3}\\\"\\\"\\\".format(unicode(eml_subject),\\n      unicode(email.get(\\\"from\\\", \\\"N/A\\\")), unicode(email.get(\\\"to\\\", \\\"N/A\\\")), unicode(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createPlainText(note_text))\\n  \u0027\u0027\u0027\",\"pre_processing_script\":\"# Define incident_id and artifact_id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\n\\n# Setting this to True will add any found attachments as an Email Attachment Artifact\\ninputs.utilities_parse_email_attachments = True\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0nwjr5i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xm73z8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0nwjr5i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gnnr3k\"/\u003e\u003cendEvent id=\"EndEvent_1w52vjy\"\u003e\u003cincoming\u003eSequenceFlow_0xm73z8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0xm73z8\" sourceRef=\"ServiceTask_1gnnr3k\" targetRef=\"EndEvent_1w52vjy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0wzvcnn\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned as additional artifacts\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_161e2uo\" sourceRef=\"ServiceTask_1gnnr3k\" targetRef=\"TextAnnotation_0wzvcnn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"168\" y=\"83\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"163\" y=\"118\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gnnr3k\" id=\"ServiceTask_1gnnr3k_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0nwjr5i\" id=\"SequenceFlow_0nwjr5i_di\"\u003e\u003comgdi:waypoint x=\"204\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"195.5\" y=\"79.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1w52vjy\" id=\"EndEvent_1w52vjy_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"439\" y=\"83\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"412\" y=\"122\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xm73z8\" id=\"SequenceFlow_0xm73z8_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003comgdi:waypoint x=\"439\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"363\" y=\"79.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0wzvcnn\" id=\"TextAnnotation_0wzvcnn_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"176\" x=\"399\" y=\"4\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_161e2uo\" id=\"Association_161e2uo_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"77\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"43\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Example Workflow showing to parse an Email File (.eml or .msg) from an Artifact File. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.",
      "export_key": "example_email_parsing_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872653580,
      "name": "Example: Email Parsing (Artifact)",
      "object_type": "artifact",
      "programmatic_name": "example_email_parsing_artifact",
      "tags": [],
      "uuid": "3422a9e6-ab15-4637-a70d-f3c874088f83",
      "workflow_id": 8
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_zip_to_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_zip_to_artifact\" isExecutable=\"true\" name=\"Example: Zip Extract\"\u003e\u003cdocumentation\u003eAn example showing how to extract a file from a ZIP file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_06xspzk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0eabem4\" name=\"Utilities: Attachment Zip Extract\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4d9fb1df-1eab-494b-8375-c4feb0525429\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# The path within the zip that we want to extract\\ninputs.file_path = rule.properties.extract_file_path\\n\\n# If the zipfile is password protected, specify here\\n# inputs.zipfile_password = \\nif rule.properties.zip_password:\\n  inputs.zipfile_password = rule.properties.zip_password\",\"result_name\":\"extracted_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_06xspzk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1xwwmdf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_06xspzk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0eabem4\"/\u003e\u003cserviceTask id=\"ServiceTask_1tdad17\" name=\"Utilities: Base64 to Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"11349159-153e-49b7-9a9b-e22676c03687\"\u003e{\"inputs\":{},\"pre_processing_script\":\"#\\ninputs.base64content = workflow.properties.extracted_file.content\\nfile_name = rule.properties.extract_file_path.split(\u0027/\u0027)[-1]\\n\\ninputs.incident_id = incident.id\\ninputs.file_name = file_name + \\\".b64\\\"\\ninputs.content_type = \\\"image/jpeg\\\"\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1xwwmdf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jm5nn7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1xwwmdf\" sourceRef=\"ServiceTask_0eabem4\" targetRef=\"ServiceTask_1tdad17\"/\u003e\u003cendEvent id=\"EndEvent_0c81k5c\"\u003e\u003cincoming\u003eSequenceFlow_0jm5nn7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jm5nn7\" sourceRef=\"ServiceTask_1tdad17\" targetRef=\"EndEvent_0c81k5c\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0w0xpq6\"\u003e\u003ctext\u003e\u003c![CDATA[In this example we assume that the file attachment is a Word, Excel or Powerpoint document (docx, xlsx, pptx).\u00a0 These are zipfiles, and may contain a thumbnail image (\"docProps/thumbnail.jpeg\").\n\n\nThe \"zip extract\" function produces base64-encoded contents of the extracted file.\u00a0 In the \"output\", we give that a name so it can be used downstream.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1od1xot\" sourceRef=\"ServiceTask_0eabem4\" targetRef=\"TextAnnotation_0w0xpq6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_177jonc\"\u003e\u003ctext\u003eFrom the output of the first function, create a new file attachment.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hx0bem\" sourceRef=\"ServiceTask_1tdad17\" targetRef=\"TextAnnotation_177jonc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0eabem4\" id=\"ServiceTask_0eabem4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"308\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06xspzk\" id=\"SequenceFlow_06xspzk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"308\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"253\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tdad17\" id=\"ServiceTask_1tdad17_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"546\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xwwmdf\" id=\"SequenceFlow_1xwwmdf_di\"\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"494\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"494\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"546\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"464\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0c81k5c\" id=\"EndEvent_0c81k5c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"730\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"748\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jm5nn7\" id=\"SequenceFlow_0jm5nn7_di\"\u003e\u003comgdi:waypoint x=\"646\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"705\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"705\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"730\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"675\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0w0xpq6\" id=\"TextAnnotation_0w0xpq6_di\"\u003e\u003comgdc:Bounds height=\"128\" width=\"376\" x=\"128\" y=\"-20\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1od1xot\" id=\"Association_1od1xot_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"333\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_177jonc\" id=\"TextAnnotation_177jonc_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"147\" x=\"600\" y=\"42\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hx0bem\" id=\"Association_0hx0bem_di\"\u003e\u003comgdi:waypoint x=\"620\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"654\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example showing how to extract a file from a ZIP file attachment.",
      "export_key": "example_zip_to_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872655849,
      "name": "Example: Zip Extract",
      "object_type": "attachment",
      "programmatic_name": "example_zip_to_artifact",
      "tags": [],
      "uuid": "d1f7b3b6-1aa9-484f-9648-11cb0d16e4ac",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_zip_list",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_zip_list\" isExecutable=\"true\" name=\"Example: Zip List\"\u003e\u003cdocumentation\u003eAn example showing how to list the contents of a ZIP file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_19qjaxi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1jqt9h0\" name=\"Utilities: Attachment Zip List\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c28c15ac-ecd2-4cd8-ba85-8f8c2bb307d2\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output contains two lists:\\n# - \\\"namelist\\\", which is just a list of the filenames (paths) within the zip file,\\n# - \\\"infolist\\\", which has full information for each file, including its name, size, and so on.\\n\\n# For this example, let\u0027s create two notes\\n\\n# One with a list of the namelist\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor filename in results.namelist:\\n  html = html + u\\\"{}\u0026lt;br\u0026gt;\\\".format(filename)\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\\n# Another with more detailed information\\nhtml = u\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;Contents of {}:\u0026lt;/p\u0026gt;\\\".format(attachment.name)\\nfor fileinfo in results.infolist:\\n  html = html + u\\\"{} ({} bytes, {} compressed) {}\u0026lt;br\u0026gt;\\\".format(fileinfo.filename, fileinfo.file_size, fileinfo.compress_size, fileinfo.comment)\\nhtml = html + \\\"\u0026lt;/div\u0026gt;\\\"\\nincident.addNote(helper.createRichText(html))\\n\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_19qjaxi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16qgouz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_19qjaxi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1jqt9h0\"/\u003e\u003cendEvent id=\"EndEvent_1khrp1p\"\u003e\u003cincoming\u003eSequenceFlow_16qgouz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16qgouz\" sourceRef=\"ServiceTask_1jqt9h0\" targetRef=\"EndEvent_1khrp1p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1o48uch\"\u003e\u003ctext\u003eFunction reads the attachment (by id) then produces a list of its contents, in a structured data format.\u00a0 The post-processing script writes these results into a note on the incident.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_01ubqgv\" sourceRef=\"ServiceTask_1jqt9h0\" targetRef=\"TextAnnotation_1o48uch\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1jqt9h0\" id=\"ServiceTask_1jqt9h0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"311\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19qjaxi\" id=\"SequenceFlow_19qjaxi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"311\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"254.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1khrp1p\" id=\"EndEvent_1khrp1p_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"545\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"563\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16qgouz\" id=\"SequenceFlow_16qgouz_di\"\u003e\u003comgdi:waypoint x=\"411\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"545\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"478\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1o48uch\" id=\"TextAnnotation_1o48uch_di\"\u003e\u003comgdc:Bounds height=\"103\" width=\"310\" x=\"391\" y=\"24\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_01ubqgv\" id=\"Association_01ubqgv_di\"\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example showing how to list the contents of a ZIP file attachment.",
      "export_key": "example_zip_list",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872655402,
      "name": "Example: Zip List",
      "object_type": "attachment",
      "programmatic_name": "example_zip_list",
      "tags": [],
      "uuid": "fcc8c11d-1501-4ff8-9447-f65d71e4991f",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_artifact_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_artifact_attachment_to_base64\" isExecutable=\"true\" name=\"Example: (Artifact) Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting an Artifact of type File to a Base64 Encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1j5vc4b\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0rxzx0p\" name=\"Utilities: Attachment to Base64\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a4b66c4-0465-4960-8bbf-fa3ebdc58c5a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = unicode(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\", \\\"\\\")[1:20] )\\n\\n  incident.addNote(note_text)\",\"pre_processing_script\":\"# Required inputs are: incident_id artifact_id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1j5vc4b\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_121ajs6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1j5vc4b\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rxzx0p\"/\u003e\u003cendEvent id=\"EndEvent_0478px6\"\u003e\u003cincoming\u003eSequenceFlow_121ajs6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_121ajs6\" sourceRef=\"ServiceTask_0rxzx0p\" targetRef=\"EndEvent_0478px6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ifa9oc\"\u003e\u003ctext\u003eConvert a file attachment attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ou0yhu\" sourceRef=\"ServiceTask_0rxzx0p\" targetRef=\"TextAnnotation_0ifa9oc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rxzx0p\" id=\"ServiceTask_0rxzx0p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1j5vc4b\" id=\"SequenceFlow_1j5vc4b_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"191.5\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0478px6\" id=\"EndEvent_0478px6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"440\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"413\" y=\"228\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_121ajs6\" id=\"SequenceFlow_121ajs6_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"362.5\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ifa9oc\" id=\"TextAnnotation_0ifa9oc_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"209\" x=\"408\" y=\"60\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ou0yhu\" id=\"Association_1ou0yhu_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"472\" xsi:type=\"omgdc:Point\" y=\"113\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example converting an Artifact of type File to a Base64 Encoded string",
      "export_key": "example_artifact_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872652349,
      "name": "Example: (Artifact) Attachment to Base64",
      "object_type": "artifact",
      "programmatic_name": "example_artifact_attachment_to_base64",
      "tags": [],
      "uuid": "33d30954-a9ab-4067-80e7-52a69567da64",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_attachment_to_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_attachment_to_base64\" isExecutable=\"true\" name=\"Example: Attachment to Base64\"\u003e\u003cdocumentation\u003eAn example converting a file attachment to a Base64 encoded string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1k2ey4q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1rw7jx0\" name=\"Utilities: Attachment to Base64\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a4b66c4-0465-4960-8bbf-fa3ebdc58c5a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\", None) is not None:\\n  \\n  file_name = unicode(results.get(\\\"filename\\\", \\\"\\\"))\\n  note_text = u\\\"File {0} converted to base64 format: {1}...\\\".format(file_name, results.get(\\\"content\\\")[1:20])\\n    \\n  incident.addNote(note_text)\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task id\\nif task is not None:\\n  inputs.task_id = task.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1k2ey4q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nnhwi4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1k2ey4q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1rw7jx0\"/\u003e\u003cendEvent id=\"EndEvent_01yksdy\"\u003e\u003cincoming\u003eSequenceFlow_1nnhwi4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1nnhwi4\" sourceRef=\"ServiceTask_1rw7jx0\" targetRef=\"EndEvent_01yksdy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ix6ku6\"\u003e\u003ctext\u003eConvert a file attachment to Base64 string and returns the encoded string.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0eg1i7s\" sourceRef=\"ServiceTask_1rw7jx0\" targetRef=\"TextAnnotation_0ix6ku6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1rw7jx0\" id=\"ServiceTask_1rw7jx0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"271\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k2ey4q\" id=\"SequenceFlow_1k2ey4q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"189.5\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01yksdy\" id=\"EndEvent_01yksdy_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"453\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"426\" y=\"228\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nnhwi4\" id=\"SequenceFlow_1nnhwi4_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"453\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"367\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ix6ku6\" id=\"TextAnnotation_0ix6ku6_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"279\" x=\"375\" y=\"93\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0eg1i7s\" id=\"Association_0eg1i7s_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"184\"/\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"146\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example converting a file attachment to a Base64 encoded string",
      "export_key": "example_attachment_to_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872654474,
      "name": "Example: Attachment to Base64",
      "object_type": "attachment",
      "programmatic_name": "example_attachment_to_base64",
      "tags": [],
      "uuid": "963a8859-4406-4cdd-b516-ba6f4d50662f",
      "workflow_id": 12
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_timer",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_timer\" isExecutable=\"true\" name=\"Example: Timer\"\u003e\u003cdocumentation\u003eThis example workflow demonstrates how to call the Utilities Timer function using an epoch time as input to define when the timer should end.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_05isvsf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0z91qwo\" name=\"Utilities: Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0aa9d601-0a7f-4741-999e-27d3bf6de4a8\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Results: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: False, \u0027reason\u0027: None, \u0027content\u0027: {\u0027instance_id\u0027: 221, \u0027status\u0027: \u0027running\u0027, \u0027start_date\u0027: 1596658216490, \u0027end_date\u0027: None, \u0027reason\u0027: None, \u0027is_terminated\u0027: False}, \u0027raw\u0027: \u0027{\\\"instance_id\\\": 221, \\\"status\\\": \\\"running\\\", \\\"start_date\\\": 1596658216490, \\\"end_date\\\": null, \\\"reason\\\": null, \\\"is_terminated\\\": false}\u0027, \u0027inputs\u0027: {\u0027utilities_epoch\u0027: 1596658320000}, \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-utilities\u0027, \u0027package_version\u0027: \u00272.0.0\u0027, \u0027host\u0027: \u0027Marks-MacBook-Pro.local\u0027, \u0027execution_time_ms\u0027: 102472, \u0027timestamp\u0027: \u00272020-08-05 16:12:00\u0027}}\",\"pre_processing_script\":\"# Get the input date/time for timer end from the rule activity field\\ninputs.utilities_epoch = rule.properties.utilities_timer_end_time\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_05isvsf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zxbldm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_05isvsf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0z91qwo\"/\u003e\u003cendEvent id=\"EndEvent_1h1hqd5\"\u003e\u003cincoming\u003eSequenceFlow_0zxbldm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0zxbldm\" sourceRef=\"ServiceTask_0z91qwo\" targetRef=\"EndEvent_1h1hqd5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_039vo75\"\u003e\u003ctext\u003e\u003c![CDATA[Input: utilities_time string indicating how long function should sleep\n\u00a0or utilities_epoch with end timer epoch\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0w30yij\" sourceRef=\"ServiceTask_0z91qwo\" targetRef=\"TextAnnotation_039vo75\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0z91qwo\" id=\"ServiceTask_0z91qwo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"327\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05isvsf\" id=\"SequenceFlow_05isvsf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"327\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"217.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1h1hqd5\" id=\"EndEvent_1h1hqd5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"523\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"496\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zxbldm\" id=\"SequenceFlow_0zxbldm_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"523\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"430\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_039vo75\" id=\"TextAnnotation_039vo75_di\"\u003e\u003comgdc:Bounds height=\"86\" width=\"205\" x=\"168\" y=\"42\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0w30yij\" id=\"Association_0w30yij_di\"\u003e\u003comgdi:waypoint x=\"342\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"309\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "This example workflow demonstrates how to call the Utilities Timer function using an epoch time as input to define when the timer should end.",
      "export_key": "example_timer",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872652091,
      "name": "Example: Timer",
      "object_type": "incident",
      "programmatic_name": "example_timer",
      "tags": [],
      "uuid": "2ef3b621-8e1f-4f9d-8491-a5f5b16c6356",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "utilities_expand_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"utilities_expand_url\" isExecutable=\"true\" name=\"Example: Expand URL\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Take a url (mostly shortened) and follow it through redirects as it\u0027s expanded]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t6zkar\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1eosian\" name=\"Utilities: Expand URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"173d3d51-3263-4f26-b927-ecd1e2bf6344\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Results: {\u0027urllist\u0027: [\u0027https://community.ibm.com/community/user/security/communities/community-home?CommunityKey=d2f71e8c-108e-4652-b59c-29d61af7163e\u0027, \u0027https://community.ibm.com/community/user/security/communities/community-home\u0027]}\\n\\n# Add the url expansions to the Artifact Description\\nexpansions = results.get(\\\"urllist\\\", [])\\nexpansion_list = u\\\"Expansions:\\\\n\\\\n{0}\\\".format(\\\"\\\\n\\\\n\\\".join(expansions)) if expansions else \\\"No Expansions\\\"\\n\\nif artifact.description:\\n  artifact.description = \\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, expansion_list)\\nelse:\\n  artifact.description = expansion_list\\n  \\nfor url in expansions:\\n  incident.addArtifact(\\\"URL\\\", url, u\\\"expansion from {}\\\".format(artifact.value))\\n\",\"pre_processing_script\":\"inputs.resilient_url = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t6zkar\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_02a827k\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t6zkar\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1eosian\"/\u003e\u003cendEvent id=\"EndEvent_0nnm7lj\"\u003e\u003cincoming\u003eSequenceFlow_02a827k\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_02a827k\" sourceRef=\"ServiceTask_1eosian\" targetRef=\"EndEvent_0nnm7lj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1omkhvp\"\u003e\u003ctext\u003e\u003c![CDATA[New artifacts are created and results update Artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_187filv\" sourceRef=\"ServiceTask_1eosian\" targetRef=\"TextAnnotation_1omkhvp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1eosian\" id=\"ServiceTask_1eosian_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t6zkar\" id=\"SequenceFlow_1t6zkar_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nnm7lj\" id=\"EndEvent_0nnm7lj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"451\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"469\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02a827k\" id=\"SequenceFlow_02a827k_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"412.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1omkhvp\" id=\"TextAnnotation_1omkhvp_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"193\" x=\"371\" y=\"88\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_187filv\" id=\"Association_187filv_di\"\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"140\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Take a url (mostly shortened) and follow it through redirects as it\u0027s expanded",
      "export_key": "utilities_expand_url",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872652861,
      "name": "Example: Expand URL",
      "object_type": "artifact",
      "programmatic_name": "utilities_expand_url",
      "tags": [],
      "uuid": "3009741f-33d8-4cdc-adf1-9aa3f0843995",
      "workflow_id": 5
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_get_task_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_get_task_contact_info\" isExecutable=\"true\" name=\"Example: Get Task Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for a task in an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ghckhk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0afrq1y\" name=\"Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"011e399a-4508-4684-986a-e49a8be0b20b\"\u003e{\"inputs\":{},\"post_processing_script\":\"owner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\ntask.addNote(note_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_id = task.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ghckhk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1fean9d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ghckhk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0afrq1y\"/\u003e\u003cendEvent id=\"EndEvent_0k0ikq0\"\u003e\u003cincoming\u003eSequenceFlow_1fean9d\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1fean9d\" sourceRef=\"ServiceTask_0afrq1y\" targetRef=\"EndEvent_0k0ikq0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0afrq1y\" id=\"ServiceTask_0afrq1y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ghckhk\" id=\"SequenceFlow_1ghckhk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0k0ikq0\" id=\"EndEvent_0k0ikq0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"442.9661214953271\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"460.9661214953271\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fean9d\" id=\"SequenceFlow_1fean9d_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"397\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "Get owner and member contact information for a task in an Incident",
      "export_key": "example_get_task_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647874741252,
      "name": "Example: Get Task Contact Info",
      "object_type": "task",
      "programmatic_name": "example_get_task_contact_info",
      "tags": [],
      "uuid": "13df6c8b-a91f-4230-9e20-1069d06de32f",
      "workflow_id": 24
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_call_rest_api",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_call_rest_api\" isExecutable=\"true\" name=\"Example: Call REST API\"\u003e\u003cdocumentation\u003eThis is a general-purpose function to call any REST API or other HTTP service.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1f2kk5d\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_127hp8b\" name=\"Utilities: Call REST API\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"47ca08b2-bc06-4ad0-a5ed-d8df6d33045b\"\u003e{\"inputs\":{\"4c1c5d09-87f0-4fb5-a236-00690b66db92\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"94486df3-4ab1-44df-8ad9-b160a095652d\"}},\"9c32f347-a610-4f0f-8cf7-fad03be630ea\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"# Set the artifact description to the Response (in plain text) of the REST call\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, results.text)\\nelse:\\n  artifact.description = results.text\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.rest_method = \\\"PATCH\\\"\\n\\n# Let\u0027s patch a URL that includes the artifact value\\ninputs.rest_url = u\\\"http://httpbin.org/patch\\\"\\n\\n# For PATCH requests, the body is text\\ninputs.rest_body = \u0027{\\\"key\\\": \\\"\u0027+artifact.value+\u0027\\\"}\u0027\\n\\n# HTTP headers can be specified as a multi-line string\\ninputs.rest_headers = \\\"\\\"\\\"\\nContent-Type: application/json\\nX-Frooble: Baz\\n\\\"\\\"\\\"\\n\\n# The \u0027rest_verify\u0027 parameter (Boolean) indicates whether to verify SSL certificates.\\n# This should be True unless you need to connect to a self-signed or other invalid cert.\\ninputs.rest_verify = True\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1f2kk5d\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_177aeon\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1jrtwdz\"\u003e\u003cincoming\u003eSequenceFlow_177aeon\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_177aeon\" sourceRef=\"ServiceTask_127hp8b\" targetRef=\"EndEvent_1jrtwdz\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1f2kk5d\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_127hp8b\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eCall from an artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1o1jwta\"\u003e\u003ctext\u003e\u003c![CDATA[Results are appended to the artifact description.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0uwb073\" sourceRef=\"ServiceTask_127hp8b\" targetRef=\"TextAnnotation_1o1jwta\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"161\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"156\" y=\"213\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"84\" y=\"247\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"167\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003comgdi:waypoint x=\"141\" xsi:type=\"omgdc:Point\" y=\"247\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_127hp8b\" id=\"ServiceTask_127hp8b_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"270\" y=\"156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jrtwdz\" id=\"EndEvent_1jrtwdz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"432\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"405\" y=\"217\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_177aeon\" id=\"SequenceFlow_177aeon_di\"\u003e\u003comgdi:waypoint x=\"370\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"356\" y=\"174.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f2kk5d\" id=\"SequenceFlow_1f2kk5d_di\"\u003e\u003comgdi:waypoint x=\"197\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"234\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"234\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"204\" y=\"189.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1o1jwta\" id=\"TextAnnotation_1o1jwta_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"212\" x=\"357\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0uwb073\" id=\"Association_0uwb073_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"165\"/\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"125\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "This is a general-purpose function to call any REST API or other HTTP service.",
      "export_key": "example_call_rest_api",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872653825,
      "name": "Example: Call REST API",
      "object_type": "artifact",
      "programmatic_name": "example_call_rest_api",
      "tags": [],
      "uuid": "f6626e9b-1850-41a4-a36d-b59a83286941",
      "workflow_id": 9
    },
    {
      "actions": [],
      "content": {
        "version": 62,
        "workflow_id": "example_pdfid",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_pdfid\" isExecutable=\"true\" name=\"Example: PDFiD\"\u003e\u003cdocumentation\u003eAn example of using the PDFiD function to get summary information about a PDF file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qm57dq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_096tnaj\" name=\"Utilities: Attachment to Base64\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a4b66c4-0465-4960-8bbf-fa3ebdc58c5a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\",\"result_name\":\"attachment_content\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qm57dq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zvggno\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qm57dq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_096tnaj\"/\u003e\u003cserviceTask id=\"ServiceTask_087cpkb\" name=\"Utilities: PDFiD\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3f9da4a2-cdac-4aa6-891c-1217565e734c\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output of PDFiD is a dictionary with the fundamental elements of the PDF file.\\n# These include,\\n#  - \\\"isPdf\\\" (True or False)\\n#  - \\\"header\\\" (the PDF version header)\\n#  - \\\"obj\\\", \\\"endobj\\\" and so on: the count of each element.\\n# More documentation can be found at https://blog.didierstevens.com/programs/pdf-tools/\\n\\n# Some sections of interest\\ninteresting_sections = [\\n  \u0027obj\u0027, \u0027endobj\u0027, \u0027stream\u0027, \u0027endstream\u0027, \u0027startxref\u0027, \u0027xref\u0027, \u0027trailer\u0027,\\n  \u0027/AA\u0027, \u0027/AcroForm\u0027, \u0027/EmbeddedFile\u0027, \u0027/Encrypt\u0027, \u0027/JBIG2Decode\u0027, \u0027/JS\u0027, \u0027/JavaScript\u0027, \u0027/Launch\u0027, \u0027/ObjStm\u0027, \u0027/OpenAction\u0027, \u0027/Page\u0027, \u0027/RichMedia\u0027, \u0027/XFA\u0027\\n  ]\\n\\nif not results.isPdf:\\n  incident.addNote(helper.createRichText(\\\"Not a PDF file: {}\\\".format(attachment.name)))\\nelse:\\n  # In this example we just write them to a note in the incident\\n  note_data = [\\\"PDFiD report for {} ({}):\\\".format(attachment.name, results.header)]\\n\\n  for section in interesting_sections:\\n    value = results.get(section)\\n    if value is not None:\\n      note_data.append(\\\"{}: {}\\\".format(section, value))\\n\\n  text = helper.createPlainText(\\\"\\\\n\\\".join(note_data))\\n  incident.addNote(text)\\n  \\n  # Maybe extend this to alert if (/JS or /JavaScript) and (/AA or /OpenAction)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# The input is the base64-encoded content that was read in a previous component\\n# That object has properties:\\n#  - filename\\n#  - content_type\\n#  - size\\n#  - created\\n#  - content (the base64-encoded data)\\ninputs.base64content = workflow.properties.attachment_content.content\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zvggno\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e0enwz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zvggno\" sourceRef=\"ServiceTask_096tnaj\" targetRef=\"ServiceTask_087cpkb\"/\u003e\u003cendEvent id=\"EndEvent_0rj6mik\"\u003e\u003cincoming\u003eSequenceFlow_1e0enwz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e0enwz\" sourceRef=\"ServiceTask_087cpkb\" targetRef=\"EndEvent_0rj6mik\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_03l5i5t\"\u003e\u003ctext\u003eInput to the PDFiD function is base64-encoded content.\u00a0 We can read this from an attachment.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pys59q\" sourceRef=\"ServiceTask_096tnaj\" targetRef=\"TextAnnotation_03l5i5t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1n1qjn9\"\u003e\u003ctext\u003ePerforms a quick analysis of the structure of the PDF file.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wviioh\" sourceRef=\"ServiceTask_087cpkb\" targetRef=\"TextAnnotation_1n1qjn9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_096tnaj\" id=\"ServiceTask_096tnaj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qm57dq\" id=\"SequenceFlow_1qm57dq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"241.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_087cpkb\" id=\"ServiceTask_087cpkb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"470\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zvggno\" id=\"SequenceFlow_0zvggno_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"470\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"427.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0rj6mik\" id=\"EndEvent_0rj6mik_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"682\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"700\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e0enwz\" id=\"SequenceFlow_1e0enwz_di\"\u003e\u003comgdi:waypoint x=\"570\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"682\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"626\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_03l5i5t\" id=\"TextAnnotation_03l5i5t_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"175\" x=\"307\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pys59q\" id=\"Association_0pys59q_di\"\u003e\u003comgdi:waypoint x=\"356\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"380\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1n1qjn9\" id=\"TextAnnotation_1n1qjn9_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"153\" x=\"509\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wviioh\" id=\"Association_0wviioh_di\"\u003e\u003comgdi:waypoint x=\"543\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"574\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 62,
      "creator_id": "admin@example.com",
      "description": "An example of using the PDFiD function to get summary information about a PDF file attachment.",
      "export_key": "example_pdfid",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647957041911,
      "name": "Example: PDFiD",
      "object_type": "attachment",
      "programmatic_name": "example_pdfid",
      "tags": [],
      "uuid": "49a1fc52-bf52-4cfa-b556-c1e1002f9c78",
      "workflow_id": 17
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_resilient_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_resilient_search\" isExecutable=\"true\" name=\"Example: Resilient Search\"\u003e\u003cdocumentation\u003eAn example of searching Resilient.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16u4gtb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0l313fr\" name=\"Utilities: Resilient Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"213720b5-fc4b-4134-8d40-09c157608600\"\u003e{\"inputs\":{\"dbc6da92-d1ae-43fa-9ff7-032de8cfb8f2\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n  \\\"types\\\": [\\\"attachment\\\"],\\n  \\\"filters\\\": {\\n    \\\"incident\\\": [{\\n        \\\"conditions\\\": [{\\\"field_name\\\": \\\"plan_status\\\", \\\"method\\\": \\\"in\\\", \\\"value\\\": [\\\"A\\\"]}]\\n      }]\\n  }\\n}\"}}}},\"post_processing_script\":\"# Search results include \\\"results\\\", which is a list of the search hits.\\n# There might be lots of results!\\n\\n# In this example we add a note with information about each result.\\nresult_info = []\\nfor result in results.results:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{}\\\"\u0026gt;{}\u0026lt;/a\u0026gt;\u0027.format(result[\u0027result\u0027][\u0027inc_id\u0027], result[\u0027result\u0027][\u0027inc_name\u0027])\\n  result_info.append(u\\\"\u0026lt;p\u0026gt;{} - {}\u0026lt;/p\u0026gt;\\\".format(link, result[\u0027obj_name\u0027]))\\n  \\nif len(result_info)==0:\\n  html = \\\"\u0026lt;div\u0026gt;No results\u0026lt;/div\u0026gt;\\\"\\nelse:\\n  html = u\\\"\u0026lt;div\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(\\\"\\\".join(result_info))\\n\\nincident.addNote(helper.createRichText(html))\",\"pre_processing_script\":\"# Search for other occurrences of the same file attachment in Resilient.\\n\\n# The search template determines the type(s) of object to search, and the filter conditions.\\n# This can be used to search within a specific incident field, or to search only incidents that meet other criteria.\\n# Refer to SearchExInputDTO in the REST API documentation for additional details of this data structure.\\n\\n# The search query can be a simple string.\\ninputs.resilient_search_query = attachment.name\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16u4gtb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1cs8z4y\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16u4gtb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0l313fr\"/\u003e\u003cendEvent id=\"EndEvent_03q83e4\"\u003e\u003cincoming\u003eSequenceFlow_1cs8z4y\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1cs8z4y\" sourceRef=\"ServiceTask_0l313fr\" targetRef=\"EndEvent_03q83e4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ad5npu\"\u003e\u003ctext\u003e\u003c![CDATA[Search for any Resilient data.\n\nThis example searches for all incidents that have an attachment with the same name.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02eoi2l\" sourceRef=\"ServiceTask_0l313fr\" targetRef=\"TextAnnotation_0ad5npu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0l313fr\" id=\"ServiceTask_0l313fr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"307\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16u4gtb\" id=\"SequenceFlow_16u4gtb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"307\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03q83e4\" id=\"EndEvent_03q83e4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"544\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"562\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cs8z4y\" id=\"SequenceFlow_1cs8z4y_di\"\u003e\u003comgdi:waypoint x=\"407\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"475.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ad5npu\" id=\"TextAnnotation_0ad5npu_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"262\" x=\"351\" y=\"55\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02eoi2l\" id=\"Association_02eoi2l_di\"\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example of searching Resilient.",
      "export_key": "example_resilient_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872653339,
      "name": "Example: Resilient Search",
      "object_type": "attachment",
      "programmatic_name": "example_resilient_search",
      "tags": [],
      "uuid": "5c9feedf-9687-4178-8fea-12d44299e95a",
      "workflow_id": 7
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_json2html",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_json2html\" isExecutable=\"true\" name=\"Example: JSON2HTML\"\u003e\u003cdocumentation\u003eExample to extract json to html table. Optionally specify a path to a portion of the json structure to convert\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0qi450y\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1wgmzwj\" name=\"Utilities: JSON2HTML\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7460c6a9-8c2a-42fb-a871-bef9b37c9e9a\"\u003e{\"inputs\":{\"254477f5-5999-432f-b509-66575b59a7e2\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"{\\\"1\\\": \\\"hello\\\", \\\"b\\\": \\\"world\\\", \\\"c\\\": {\\\"d\\\": \\\"D\\\", \\\"e\\\": null, \\\"list\\\": [1, 2, 3, {\\\"keen1n\\\": \\\"m1ch\\\", \\\"ibm\\\": null}], \\\"empty_list\\\": [], \\\"null\\\": \\\"1sdf\\\", \\\"set\\\": [\\\"s\\\", \\\"e\\\", \\\"t\\\"]}, \\\"d\\\": \\\"D2\\\", \\\"test.with.period\\\": \\\"working?\\\"}\"}},\"58f0bd61-cec6-4d85-9ab1-c72f8f5722cb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"c.list\"}}},\"post_processing_script\":\"# example output\\n# {\u0027content\u0027: \u0027\u0026lt;ul\u0026gt;\u0026lt;li\u0026gt;1\u0026lt;/li\u0026gt;\u0026lt;li\u0026gt;2\u0026lt;/li\u0026gt;\u0026lt;li\u0026gt;3\u0026lt;/li\u0026gt;\u0026lt;li\u0026gt;\u0026lt;table border=\\\"1\\\"\u0026gt;\u0026lt;tr\u0026gt;\u0026lt;th\u0026gt;keen1n\u0026lt;/th\u0026gt;\u0026lt;td\u0026gt;m1ch\u0026lt;/td\u0026gt;\u0026lt;/tr\u0026gt;\u0026lt;tr\u0026gt;\u0026lt;th\u0026gt;ibm\u0026lt;/th\u0026gt;\u0026lt;td\u0026gt;None\u0026lt;/td\u0026gt;\u0026lt;/tr\u0026gt;\u0026lt;/table\u0026gt;\u0026lt;/li\u0026gt;\u0026lt;/ul\u0026gt;\u0027}\\nincident.addNote(helper.createRichText(results[\u0027content\u0027]))\",\"pre_processing_script\":\"#data = { \\\"data\\\": artifact.value, \\\"data_type\\\": artifact.type, \\\"description\\\": artifact.description if artifact.description is not None else \\\"\\\"}\\n#inputs.json2html_data = str(data).replace(\\\"\u0027\\\", \u0027\\\"\u0027).replace(\u0027u\\\"\u0027, \u0027\\\"\u0027) # remove unicode references\\n#inputs.json2html_data = str(inputs.json2html_data).replace(\\\"\u0027\\\", \u0027\\\"\u0027).replace(\u0027u\\\"\u0027, \u0027\\\"\u0027) # remove unicode references\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qi450y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_162u142\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qi450y\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1wgmzwj\"/\u003e\u003cendEvent id=\"EndEvent_0wrakqo\"\u003e\u003cincoming\u003eSequenceFlow_162u142\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_162u142\" sourceRef=\"ServiceTask_1wgmzwj\" targetRef=\"EndEvent_0wrakqo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0fmyixl\"\u003e\u003ctext\u003e\u003c![CDATA[Example results added as an incident note. Note: tables do not render correctly has rich text.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17xhl7t\" sourceRef=\"ServiceTask_1wgmzwj\" targetRef=\"TextAnnotation_0fmyixl\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1wgmzwj\" id=\"ServiceTask_1wgmzwj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"290\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qi450y\" id=\"SequenceFlow_0qi450y_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wrakqo\" id=\"EndEvent_0wrakqo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"474\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"492\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_162u142\" id=\"SequenceFlow_162u142_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"474\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"432\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0fmyixl\" id=\"TextAnnotation_0fmyixl_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"205\" x=\"402\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17xhl7t\" id=\"Association_17xhl7t_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"465\" xsi:type=\"omgdc:Point\" y=\"125\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Example to extract json to html table. Optionally specify a path to a portion of the json structure to convert",
      "export_key": "example_json2html",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872654045,
      "name": "Example: JSON2HTML",
      "object_type": "artifact",
      "programmatic_name": "example_json2html",
      "tags": [],
      "uuid": "bd5f2bdf-4bd6-408d-9a24-2cd20a36c8ed",
      "workflow_id": 10
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_shell_command",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_shell_command\" isExecutable=\"true\" name=\"Example: Shell Command\"\u003e\u003cdocumentation\u003eAn example running shell commands for integration\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0x7veso\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ltyl63\" name=\"Utilities: Shell Command\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0ecc7cb7-f448-4e9d-a38e-100ddbe7fd18\"\u003e{\"inputs\":{\"8405293e-4d78-44e2-ba9a-91a29674ea4c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"traceroute\"}},\"ece49b2b-4495-47cd-b6d4-990048260ebf\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"# Outputs are:\\n#  - \\\"commandline\\\": the command that ran\\n#  - \\\"start\\\": timestamp, epoch milliseconds\\n#  - \\\"end\\\": timestamp, epoch milliseconds\\n#  - \\\"elapsed\\\": milliseconds\\n#  - \\\"exitcode\\\": nonzero indicates that the command failed\\n#  - \\\"stdout\\\": text output from the command\\n#  - \\\"stderr\\\": error text output from the command\\n#  - \\\"stdout_json\\\": object parsed from JSON output from the command\\n#  - \\\"stderr_json\\\": object parsed from JSON error output from the command\\n\\nif results.exitcode == 0:\\n  note_text = u\\\"Command succeeded: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(results.commandline, results.stdout, results.stderr)\\nelse:\\n  note_text = u\\\"Command failed: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(results.commandline, results.stdout, results.stderr)\\n\\nincident.addNote(helper.createPlainText(note_text))\\n\",\"pre_processing_script\":\"import re\\n# You can set the command on the \\\"Input\\\" panel or dynamically\\n# NOTE: The administrator must configure each command before you can run it!\\n#inputs.shell_command = \\\"traceroute\\\"\\n# True if running a Remote Powershell, otherwise False\\n#inputs.shell_remote = False\\n\\nif artifact.type.lower() in [\u0027url\u0027]:\\n  p = re.compile(\\\"^(?:http[s]*?:\\\\/\\\\/)?(?:[^@\\\\n]+@)?(?:www\\\\.)?([^:\\\\/\\\\n?]+)\\\")\\n  match = p.match(artifact.value)\\n  inputs.shell_param1 = match.group(1) if match else artifact.value\\nelse:\\n  # Parameters to the command.  In this case we run traceroute to the artifact\\n  inputs.shell_param1 = artifact.value\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0x7veso\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mly2iq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0x7veso\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ltyl63\"/\u003e\u003cendEvent id=\"EndEvent_19kshii\"\u003e\u003cincoming\u003eSequenceFlow_1mly2iq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1mly2iq\" sourceRef=\"ServiceTask_0ltyl63\" targetRef=\"EndEvent_19kshii\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1glr6gg\"\u003e\u003ctext\u003e\u003c![CDATA[Runs a shell command.\u00a0 The set of available commands is configured by the Resilient administrator in the integration config (refer to documentation for details).\u00a0 The results are available as text, or a dictionary if they can be parsed as JSON.\n\nIn this example we \u0027traceroute\u0027 to the artifact (domain name or IP address), and add the results as a note in the incident.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wz5xfn\" sourceRef=\"ServiceTask_0ltyl63\" targetRef=\"TextAnnotation_1glr6gg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"211\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"206\" y=\"205\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ltyl63\" id=\"ServiceTask_0ltyl63_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"148\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0x7veso\" id=\"SequenceFlow_0x7veso_di\"\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"310\" y=\"166.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_19kshii\" id=\"EndEvent_19kshii_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"588\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"606\" y=\"209\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mly2iq\" id=\"SequenceFlow_1mly2iq_di\"\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"588\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"530.5\" y=\"166.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1glr6gg\" id=\"TextAnnotation_1glr6gg_di\"\u003e\u003comgdc:Bounds height=\"131\" width=\"311\" x=\"369\" y=\"-32\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wz5xfn\" id=\"Association_0wz5xfn_di\"\u003e\u003comgdi:waypoint x=\"450\" xsi:type=\"omgdc:Point\" y=\"148\"/\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"99\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example running shell commands for integration",
      "export_key": "example_shell_command",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872656595,
      "name": "Example: Shell Command",
      "object_type": "artifact",
      "programmatic_name": "example_shell_command",
      "tags": [],
      "uuid": "f3d7cac2-b101-43b4-bbbb-840d5d9fc290",
      "workflow_id": 22
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_domain_distance",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_domain_distance\" isExecutable=\"true\" name=\"Example: Domain Distance\"\u003e\u003cdocumentation\u003eAn example testing for confusable domain names\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pyyn79\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_07w80p3\" name=\"Utilities: Domain Distance\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6fd01564-96de-4482-bceb-cf396df6c758\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The result includes:\\n#   \\\"domain_name\\\" - the name being tested\\n#   \\\"distances\\\" - a dicctionary of all the distances\\n#   \\\"closest\\\" - the closest match from the list.\\n# If the match distance is only 1 or 0, the domain name is very easily confused with one on the list!\\n\\nif results.closest.distance \u0026lt;= 1:\\n  html = u\\\"\u0026lt;div\u0026gt;Warning!  Domain {} is easily confused with {}!\u0026lt;/div\u0026gt;\\\".format(results.domain_name, results.closest.name)\\n  incident.addNote(helper.createRichText(html))\\n\",\"pre_processing_script\":\"# if email address, return only domain portion\\nif \\\"email\\\" in artifact.type.lower():\\n  split_email = artifact.value.split(\\\"@\\\")\\n  if len(split_email) \u0026gt; 1:\\n    inputs.domain_name = split_email[1]\\n  else:\\n    inputs.domain_name = artifact.value\\nelse:\\n  # The domain name being tested\\n  inputs.domain_name = artifact.value\\n\\n# The list of domains to test against\\ninputs.domain_list = \\\"ibm.com, resilientsystems.com, ibmcloud.com, bluemix.com\\\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pyyn79\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1062y94\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0fkhffe\"\u003e\u003cincoming\u003eSequenceFlow_1062y94\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1062y94\" sourceRef=\"ServiceTask_07w80p3\" targetRef=\"EndEvent_0fkhffe\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1pyyn79\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_07w80p3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1xd68s6\"\u003e\u003ctext\u003e\u003c![CDATA[Calculates the \"word distance\" between a suspect name and a list of names.\u00a0 This can be useful for detecting spoofed URLs.\n\nThe distance is small if the names are similar.\u00a0 For each different or switched character, the distance increases.\u00a0 But \"confusable Unicode characters\" are treated as identical (they have zero distance).]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0t5cp3a\" sourceRef=\"ServiceTask_07w80p3\" targetRef=\"TextAnnotation_1xd68s6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_07w80p3\" id=\"ServiceTask_07w80p3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"282\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fkhffe\" id=\"EndEvent_0fkhffe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"448\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"421\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1062y94\" id=\"SequenceFlow_1062y94_di\"\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"370\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pyyn79\" id=\"SequenceFlow_1pyyn79_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"282\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"240\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1xd68s6\" id=\"TextAnnotation_1xd68s6_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"502\" x=\"309\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0t5cp3a\" id=\"Association_0t5cp3a_di\"\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"499\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example testing for confusable domain names",
      "export_key": "example_domain_distance",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872654702,
      "name": "Example: Domain Distance",
      "object_type": "artifact",
      "programmatic_name": "example_domain_distance",
      "tags": [],
      "uuid": "46aeb812-3e5d-4e03-a881-a613a90d88ec",
      "workflow_id": 13
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_string_to_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_string_to_attachment\" isExecutable=\"true\" name=\"Example: String to Attachment\"\u003e\u003cdocumentation\u003eAn example of creating an attachment from an input string\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lr37k8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0tzwdvf\" name=\"Utilities: String to Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"cd8a23ce-63ba-42cf-8eba-8b63d5e7c872\"\u003e{\"inputs\":{\"03955f53-5940-49ff-a9df-0b607099657b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"A Test Attachment Name\"}}},\"post_processing_script\":\"# result: {\u0027attachment_id\u0027: 28}\\n\",\"pre_processing_script\":\"# Required inputs are: the string to convert, the incident id and the attachment name\\ninputs.string_to_convert_to_attachment = artifact.value\\ninputs.incident_id = incident.id\\n#inputs.attachment_name = \\\"A Test Attachment Name\\\"\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lr37k8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1m0w4as\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lr37k8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0tzwdvf\"/\u003e\u003cendEvent id=\"EndEvent_1czshr5\"\u003e\u003cincoming\u003eSequenceFlow_1m0w4as\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1m0w4as\" sourceRef=\"ServiceTask_0tzwdvf\" targetRef=\"EndEvent_1czshr5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0tzwdvf\" id=\"ServiceTask_0tzwdvf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"365.27250900360144\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lr37k8\" id=\"SequenceFlow_1lr37k8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"281.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1czshr5\" id=\"EndEvent_1czshr5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"669.2725090036015\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"687.2725090036015\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m0w4as\" id=\"SequenceFlow_1m0w4as_di\"\u003e\u003comgdi:waypoint x=\"465\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"669\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"567\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example of creating an attachment from an input string",
      "export_key": "example_string_to_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872654255,
      "name": "Example: String to Attachment",
      "object_type": "artifact",
      "programmatic_name": "example_string_to_attachment",
      "tags": [],
      "uuid": "39f4dc31-1eed-41ee-a4db-859724e476d5",
      "workflow_id": 11
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_attachment_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_attachment_hash\" isExecutable=\"true\" name=\"Example: Attachment Hash\"\u003e\u003cdocumentation\u003eAn example that calculates hash artifacts from an attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qf4wqa\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0pb6atz\" name=\"Utilities: Attachment Hash\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9e0f46f4-ae8c-4aa6-a296-3a0662a53386\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The result contains at least these three hashes\\nif results.get(\u0027sha256\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-256 Hash\\\", results.get(\u0027sha256\u0027), u\\\"SHA-256 hash of \u0027{}\u0027\\\".format(attachment.name))\\n\\nif results.get(\u0027sha1\u0027, None):\\n  incident.addArtifact(\\\"Malware SHA-1 Hash\\\", results.get(\u0027sha1\u0027), u\\\"SHA-1 hash of \u0027{}\u0027\\\".format(attachment.name))\\n\\nif results.get(\u0027md5\u0027, None):\\n  incident.addArtifact(\\\"Malware MD5 Hash\\\", results.get(\u0027md5\u0027), u\\\"MD5 hash of \u0027{}\u0027\\\".format(attachment.name))\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qf4wqa\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dhtmov\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qf4wqa\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0pb6atz\"/\u003e\u003cendEvent id=\"EndEvent_00tno9m\"\u003e\u003cincoming\u003eSequenceFlow_1dhtmov\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1dhtmov\" sourceRef=\"ServiceTask_0pb6atz\" targetRef=\"EndEvent_00tno9m\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_140whac\"\u003e\u003ctext\u003e\u003c![CDATA[Calculate hashes of a file attachment.\n\nThe results are added to the incident as new artifacts.]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1w4edth\" sourceRef=\"ServiceTask_0pb6atz\" targetRef=\"TextAnnotation_140whac\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0pb6atz\" id=\"ServiceTask_0pb6atz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"265\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qf4wqa\" id=\"SequenceFlow_1qf4wqa_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"265\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"186.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_00tno9m\" id=\"EndEvent_00tno9m_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"416\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"389\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dhtmov\" id=\"SequenceFlow_1dhtmov_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"345.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_140whac\" id=\"TextAnnotation_140whac_di\"\u003e\u003comgdc:Bounds height=\"86\" width=\"214\" x=\"388\" y=\"55\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1w4edth\" id=\"Association_1w4edth_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example that calculates hash artifacts from an attachment.",
      "export_key": "example_attachment_hash",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872652602,
      "name": "Example: Attachment Hash",
      "object_type": "attachment",
      "programmatic_name": "example_attachment_hash",
      "tags": [],
      "uuid": "c60fdfd6-d17a-42f2-877b-3b878c30969d",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_extract_ssl_cert_from_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_extract_ssl_cert_from_url\" isExecutable=\"true\" name=\"Example: Extract SSL Cert from URL\"\u003e\u003cdocumentation\u003e\u003c![CDATA[This workflow takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.\nThe workflow runs at the artifact level]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ptaupz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_12xb2eo\" name=\"Utilities: Extract SSL Cert From ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"69123885-b3b9-4df9-a241-aaa29ba9d7d6\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addArtifact(\u0027X509 Certificate File\u0027, results.certificate, \u0027A certificate file gathered from provided the provided URL\u0027)\\n\",\"pre_processing_script\":\"inputs.https_url = artifact.value\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ptaupz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1s9vql7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ptaupz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_12xb2eo\"/\u003e\u003cendEvent id=\"EndEvent_06nahzq\"\u003e\u003cincoming\u003eSequenceFlow_1s9vql7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1s9vql7\" sourceRef=\"ServiceTask_12xb2eo\" targetRef=\"EndEvent_06nahzq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_11zlt8p\"\u003e\u003ctext\u003eInput: HTTPS URL\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_067xt46\" sourceRef=\"ServiceTask_12xb2eo\" targetRef=\"TextAnnotation_11zlt8p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0b52jx9\"\u003e\u003ctext\u003e\u003c![CDATA[Artifact created of type \u0027X509 Certificate File\u0027 with SSL Certificate data; encoded in JSON]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1fh4amb\" sourceRef=\"ServiceTask_12xb2eo\" targetRef=\"TextAnnotation_0b52jx9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_12xb2eo\" id=\"ServiceTask_12xb2eo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"364\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ptaupz\" id=\"SequenceFlow_1ptaupz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"281\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06nahzq\" id=\"EndEvent_06nahzq_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"651\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"669\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1s9vql7\" id=\"SequenceFlow_1s9vql7_di\"\u003e\u003comgdi:waypoint x=\"464\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"557.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_11zlt8p\" id=\"TextAnnotation_11zlt8p_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"201\" y=\"87\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_067xt46\" id=\"Association_067xt46_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0b52jx9\" id=\"TextAnnotation_0b52jx9_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"258\" x=\"518\" y=\"87\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1fh4amb\" id=\"Association_1fh4amb_di\"\u003e\u003comgdi:waypoint x=\"464\" xsi:type=\"omgdc:Point\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"572\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "This workflow takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.\nThe workflow runs at the artifact level",
      "export_key": "example_extract_ssl_cert_from_url",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872656439,
      "name": "Example: Extract SSL Cert from URL",
      "object_type": "artifact",
      "programmatic_name": "example_extract_ssl_cert_from_url",
      "tags": [],
      "uuid": "663fd8b8-315f-41a5-a0d5-005758fabcc1",
      "workflow_id": 21
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_ssl_certificate",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_ssl_certificate\" isExecutable=\"true\" name=\"Example: Parse SSL Certificate\"\u003e\u003cdocumentation\u003eAn example workflow that takes a PEM encoded SSL certificate as input and returns structured information about the certificate.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16cp1cj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_11kkefg\" name=\"Utilities: Parse SSL Certificate\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"029f623a-ae74-406e-91a5-366a7005d1b0\"\u003e{\"inputs\":{},\"post_processing_script\":\"color = \\\"#45bc27\\\"\\n\\nif (results.expiration_status != \\\"Valid\\\"):\\n  color = \\\"#ff402b\\\"\\nnoteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Certificate Subject :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n              \u0026lt;b\u0026gt;Certificate Expiry After :\u0026lt;/b\u0026gt;{1}\u0026lt;/a\u0026gt;\\n              \u0026lt;b\u0026gt;Expiration Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {2}\\\"\u0026gt;{3}\u0026lt;/b\u0026gt;\\n              \u0026lt;br\u0026gt;Issuer Details :\u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.subject, results.notAfter, color, results.expiration_status,results.issuer)\\n\\nincident.addNote(helper.createRichText(noteText))\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, { \\n    \\\"version\\\": 1.0,\\n    \\\"header\\\": None,\\n    \\\"padding\\\": 10,\\n    \\\"separator\\\": u\\\"\u0026lt;br\u0026gt;\\\",\\n    \\\"json\\\": results,\\n    \\\"json_omit_list\\\": [],\\n    \\\"incident_field\\\": None\\n  })\",\"pre_processing_script\":\"inputs.utilities_certificate = artifact.value\\ninputs.artifact_id = artifact.id\\ninputs.incident_id = incident.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16cp1cj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_07qmd0r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1ljcycb\"\u003e\u003cincoming\u003eSequenceFlow_04l4mky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16cp1cj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_11kkefg\"/\u003e\u003csequenceFlow id=\"SequenceFlow_07qmd0r\" sourceRef=\"ServiceTask_11kkefg\" targetRef=\"ScriptTask_07jiv14\"/\u003e\u003cscriptTask id=\"ScriptTask_07jiv14\" name=\"Convert json to rich text\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f7276ff0-1770-4058-9e89-40ee79c6e41b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_07qmd0r\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_04l4mky\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_04l4mky\" sourceRef=\"ScriptTask_07jiv14\" targetRef=\"EndEvent_1ljcycb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1n6af4p\"\u003e\u003ctext\u003eInputs: certificate OR artifact_id AND incident_id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0zor1g6\" sourceRef=\"ServiceTask_11kkefg\" targetRef=\"TextAnnotation_1n6af4p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0r2063s\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs: certificate data as a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pkxak2\" sourceRef=\"ServiceTask_11kkefg\" targetRef=\"TextAnnotation_0r2063s\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11kkefg\" id=\"ServiceTask_11kkefg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ljcycb\" id=\"EndEvent_1ljcycb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"557\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"530\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16cp1cj\" id=\"SequenceFlow_16cp1cj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"179.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07qmd0r\" id=\"SequenceFlow_07qmd0r_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"395\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"328\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1n6af4p\" id=\"TextAnnotation_1n6af4p_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"169\" x=\"135\" y=\"107\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0zor1g6\" id=\"Association_0zor1g6_di\"\u003e\u003comgdi:waypoint x=\"261\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0r2063s\" id=\"TextAnnotation_0r2063s_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"156\" x=\"358\" y=\"103\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pkxak2\" id=\"Association_0pkxak2_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"144\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_07jiv14\" id=\"ScriptTask_07jiv14_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"395\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04l4mky\" id=\"SequenceFlow_04l4mky_di\"\u003e\u003comgdi:waypoint x=\"495\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"526\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "An example workflow that takes a PEM encoded SSL certificate as input and returns structured information about the certificate.",
      "export_key": "example_parse_ssl_certificate",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872654968,
      "name": "Example: Parse SSL Certificate",
      "object_type": "artifact",
      "programmatic_name": "example_parse_ssl_certificate",
      "tags": [],
      "uuid": "2248c896-c3b4-48f6-82fc-a127255d4ab8",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_get_incident_contact_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_get_incident_contact_info\" isExecutable=\"true\" name=\"Example: Get Incident Contact Info\"\u003e\u003cdocumentation\u003eGet owner and member contact information for an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_062lhqj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_062lhqj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1u4onb0\"/\u003e\u003cendEvent id=\"EndEvent_1h5oo0t\"\u003e\u003cincoming\u003eSequenceFlow_02cq3n3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1u4onb0\" name=\"Utilities: Get Contact Info\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"011e399a-4508-4684-986a-e49a8be0b20b\"\u003e{\"inputs\":{},\"post_processing_script\":\"# {\u0027owner\u0027: {\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}, \u0027members\u0027: []}\\n# {\u0027owner\u0027: None, \u0027members\u0027: [{\u0027fname\u0027: \u0027Resilient\u0027, \u0027lname\u0027: \u0027Sysadmin\u0027, \u0027title\u0027: \u0027\u0027, \u0027display_name\u0027: \u0027Resilient Sysadmin\u0027, \u0027email\u0027: \u0027b@a.com\u0027, \u0027phone\u0027: \u0027781 838 4848\u0027, \u0027cell\u0027: \u0027978 373 2839\u0027}]}\\nowner = u\\\"{} ({})\\\".format(results[\u0027owner\u0027][\u0027display_name\u0027], results[\u0027owner\u0027][\u0027email\u0027]) if results[\u0027owner\u0027] else \u0027Unassigned\u0027\\nnote_text = u\\\"Owner: {}\\\\nMembers:\\\\n{}\\\".format(owner, u\\\"\\\\n\\\".join([u\\\"{} ({})\\\".format(member[\u0027display_name\u0027], member[\u0027email\u0027]) for member in results[\u0027members\u0027]]))\\nincident.addNote(note_text)\",\"pre_processing_script\":\"inputs.incident_id = incident.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_062lhqj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_02cq3n3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02cq3n3\" sourceRef=\"ServiceTask_1u4onb0\" targetRef=\"EndEvent_1h5oo0t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1hoy6fe\"\u003e\u003ctext\u003e\u003c![CDATA[Results rerturned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1r1nuj4\" sourceRef=\"ServiceTask_1u4onb0\" targetRef=\"TextAnnotation_1hoy6fe\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_062lhqj\" id=\"SequenceFlow_062lhqj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"181\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1h5oo0t\" id=\"EndEvent_1h5oo0t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"427\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"400\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1u4onb0\" id=\"ServiceTask_1u4onb0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02cq3n3\" id=\"SequenceFlow_02cq3n3_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"390.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1hoy6fe\" id=\"TextAnnotation_1hoy6fe_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"196\" x=\"346\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1r1nuj4\" id=\"Association_1r1nuj4_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"137\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Get owner and member contact information for an Incident",
      "export_key": "example_get_incident_contact_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872656250,
      "name": "Example: Get Incident Contact Info",
      "object_type": "incident",
      "programmatic_name": "example_get_incident_contact_info",
      "tags": [],
      "uuid": "5934f408-b9da-4c05-871b-aa9320419d16",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_timer_parallel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_timer_parallel\" isExecutable=\"true\" name=\"Example: Timers in Parallel\"\u003e\u003cdocumentation\u003eThis example workflow shows how to use the Utilities Timer function to pause a workflow.  The Timer function is called twice in parallel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ys9gau\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0tzqwcu\" name=\"Utilities: Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0aa9d601-0a7f-4741-999e-27d3bf6de4a8\"\u003e{\"inputs\":{\"2e1b9634-f5bc-475e-926b-808493e286b7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"30s\"}}},\"pre_processing_script\":\"# Get the timer values from the rule properties custom field\\nlist_time_values = rule.properties.parallel_timers\\n\\n# Get the list of 2 timer values\\ntime_list = list_time_values.split(\u0027,\u0027)\\n\\n# Use the first timer for this function\\ninputs.utilities_time = time_list[0]\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mper68\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1c2sw10\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cparallelGateway id=\"ParallelGateway_0jhjvf7\"\u003e\u003cincoming\u003eSequenceFlow_0ys9gau\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mper68\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_10m6syb\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0ys9gau\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ParallelGateway_0jhjvf7\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1mper68\" sourceRef=\"ParallelGateway_0jhjvf7\" targetRef=\"ServiceTask_0tzqwcu\"/\u003e\u003cserviceTask id=\"ServiceTask_129kmr7\" name=\"Utilities: Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0aa9d601-0a7f-4741-999e-27d3bf6de4a8\"\u003e{\"inputs\":{\"2e1b9634-f5bc-475e-926b-808493e286b7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"1m\"}}},\"pre_processing_script\":\"# Get the timer values from the rule properties custom field\\nlist_time_values = rule.properties.parallel_timers\\n\\n# Get the list of 2 timer values\\ntime_list = list_time_values.split(\u0027,\u0027)\\n\\n# Use the second timer for this function\\ninputs.utilities_time = time_list[1]\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10m6syb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1god5ve\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10m6syb\" sourceRef=\"ParallelGateway_0jhjvf7\" targetRef=\"ServiceTask_129kmr7\"/\u003e\u003cendEvent id=\"EndEvent_1v4h851\"\u003e\u003cincoming\u003eSequenceFlow_0ubh5so\u003c/incoming\u003e\u003c/endEvent\u003e\u003cparallelGateway id=\"ParallelGateway_16jfah3\"\u003e\u003cincoming\u003eSequenceFlow_1c2sw10\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1god5ve\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ubh5so\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0ubh5so\" sourceRef=\"ParallelGateway_16jfah3\" targetRef=\"EndEvent_1v4h851\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1c2sw10\" sourceRef=\"ServiceTask_0tzqwcu\" targetRef=\"ParallelGateway_16jfah3\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1god5ve\" sourceRef=\"ServiceTask_129kmr7\" targetRef=\"ParallelGateway_16jfah3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0tzqwcu\" id=\"ServiceTask_0tzqwcu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"412\" y=\"74\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ParallelGateway_0jhjvf7\" id=\"ParallelGateway_0jhjvf7_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"298\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"323\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ys9gau\" id=\"SequenceFlow_0ys9gau_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"298\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"248\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mper68\" id=\"SequenceFlow_1mper68_di\"\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"338\" y=\"140.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_129kmr7\" id=\"ServiceTask_129kmr7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"412\" y=\"265\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10m6syb\" id=\"SequenceFlow_10m6syb_di\"\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"305\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"338\" y=\"261\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1v4h851\" id=\"EndEvent_1v4h851_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"697\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"670\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ParallelGateway_16jfah3\" id=\"ParallelGateway_16jfah3_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"564\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"544\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ubh5so\" id=\"SequenceFlow_0ubh5so_di\"\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"655\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"655\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"697\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"625\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1c2sw10\" id=\"SequenceFlow_1c2sw10_di\"\u003e\u003comgdi:waypoint x=\"512\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"505.5\" y=\"92.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1god5ve\" id=\"SequenceFlow_1god5ve_di\"\u003e\u003comgdi:waypoint x=\"512\" xsi:type=\"omgdc:Point\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"505.5\" y=\"283.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "This example workflow shows how to use the Utilities Timer function to pause a workflow.  The Timer function is called twice in parallel.",
      "export_key": "example_timer_parallel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872655196,
      "name": "Example: Timers in Parallel",
      "object_type": "incident",
      "programmatic_name": "example_timer_parallel",
      "tags": [],
      "uuid": "6b72e56a-7b67-4416-b50b-ad3a1402f4ad",
      "workflow_id": 15
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_create_artifacts_from_excel_data",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_create_artifacts_from_excel_data\" isExecutable=\"true\" name=\"Example: Create Artifacts From Excel Data\"\u003e\u003cdocumentation\u003eCreate artifacts with information extracted from an excel sheet.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0f4swta\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1nyeq2e\" name=\"Utilities: Excel Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"118bd2c6-f367-4342-93b8-50257121ccf2\"\u003e{\"inputs\":{},\"post_processing_script\":\"def format_link(item):\\n  if item and (\\\"https://\\\" in item or \\\"http://\\\" in item):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        elif isinstance(item, list):\\n          items.append(expand_list(item))\\n        else:\\n          items.append(format_link(str(item)))\\n      return separator.join(items)\\n    except Exception as err:\\n        return str(err)\\n\\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(u\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(u\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n\\n  return u\\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n\\n\\nnote = u\\\"Excel Extract for : {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(attachment.name)\\n\\nnote = note + walk_dict(results)\\n\\nincident.addNote(helper.createRichText(note))\\n\\n\\n# This example shows how to iterate over the sheets and create artifacts from the returned data\\n\u0027\u0027\u0027\\nkeys = results.sheets[\\\"_keys\\\"]\\nfor sheet in keys:\\n  ranges = results.sheets[sheet][\\\"_keys\\\"]\\n  for range_name in ranges:\\n    rng = results.sheets[sheet][range_name]\\n    for row in rng:\\n      incident.addArtifact(\\\"IP Address\\\", row[0], \\\"Sheet Region {0}  Priority {1}\\\".format(row[1], row[2]))\\n\u0027\u0027\u0027\\n\\n# This example shows how to iterate through the named ranges and create artifacts from them\\n# It is pretty much the same as the previous example, with an exception of extra layer of iterating through the named ranges\\n\u0027\u0027\u0027\\nkeys = results.named_ranges[\\\"_keys\\\"]\\nfor named_range in keys:\\n  sheets = results.named_ranges[named_range][\\\"_keys\\\"]\\n  for sheet in sheets:\\n    range_names = results.named_ranges[named_range][sheet][\\\"_keys\\\"]\\n    for range_name in range_names:\\n      rng = results.named_ranges[named_range][sheet][range_name]\\n      for row in rng:\\n        incident.addArtifact(\\\"IP Address\\\", row[0], \\\"Named Range Region {0}  Priority {1}\\\".format(row[1], row[2]))\\n\u0027\u0027\u0027\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\nif task is not None:\\n  inputs.task_id = task.id\\n  \\nif rule.properties.excel_named_range:\\n  inputs.excel_defined_names = rule.properties.excel_named_range\\n\\nif rule.properties.excel_range:\\n  inputs.excel_ranges = rule.properties.excel_range\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f4swta\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0d7gm0q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f4swta\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1nyeq2e\"/\u003e\u003cendEvent id=\"EndEvent_0i4recz\"\u003e\u003cincoming\u003eSequenceFlow_0d7gm0q\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0d7gm0q\" sourceRef=\"ServiceTask_1nyeq2e\" targetRef=\"EndEvent_0i4recz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_08ubcwp\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1l7jl29\" sourceRef=\"ServiceTask_1nyeq2e\" targetRef=\"TextAnnotation_08ubcwp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"172\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"207\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1nyeq2e\" id=\"ServiceTask_1nyeq2e_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"271\" y=\"150\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f4swta\" id=\"SequenceFlow_0f4swta_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"205\" y=\"183.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0i4recz\" id=\"EndEvent_0i4recz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"446\" y=\"172\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"464\" y=\"211\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0d7gm0q\" id=\"SequenceFlow_0d7gm0q_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003comgdi:waypoint x=\"446\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"408.5\" y=\"168\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_08ubcwp\" id=\"TextAnnotation_08ubcwp_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"125\" x=\"364\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1l7jl29\" id=\"Association_1l7jl29_di\"\u003e\u003comgdi:waypoint x=\"361\" xsi:type=\"omgdc:Point\" y=\"150\"/\u003e\u003comgdi:waypoint x=\"406\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Create artifacts with information extracted from an excel sheet.",
      "export_key": "example_create_artifacts_from_excel_data",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872653102,
      "name": "Example: Create Artifacts From Excel Data",
      "object_type": "attachment",
      "programmatic_name": "example_create_artifacts_from_excel_data",
      "tags": [],
      "uuid": "c277c3ae-b0f6-4fb2-a6a6-54c4281260de",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_email_parsing_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_email_parsing_attachment\" isExecutable=\"true\" name=\"Example: Email Parsing (Attachment)\"\u003e\u003cdocumentation\u003eExample Workflow showing to parse an Email File (.eml or .msg) from Incident/Task Attachments. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0a3f8pj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0mbl607\" name=\"Utilities: Email Parse\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d83f571e-8904-4123-9c2c-3f404b00cc5e\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\nif not results.success:\\n  note_text = u\\\"\\\"\\\"Workflow \u0027Example: Email Parsing (Artifact)\u0027 Failed\u0026lt;br\u0026gt;\\n                  \u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(unicode(results.reason))\\n  \\n  incident.addNote(helper.createRichText(note_text))\\n\\nelse:\\n  email = results.content\\n  \\n  # Get Email Subject\\n  eml_subject = email.get(\\\"subject\\\", \\\"BLANK SUBJECT LINE\\\")\\n\\n  #########################################\\n  # Add Artifacts for Email Recipient: to #\\n  #########################################\\n  for eml_addr in email.get(\\\"to\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  #########################################\\n  # Add Artifacts for Email Recipient: cc #\\n  #########################################\\n  for eml_addr in email.get(\\\"cc\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  ########################################\\n  # Add Artifacts for Email Sender: from #\\n  ########################################\\n  for eml_addr in email.get(\\\"from\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Sender\\\", eml_addr[1], eml_addr[0])\\n\\n  ################################################\\n  # Add Artifacts for IPs found in Email Headers #\\n  ################################################\\n  for eml_header in email.get(\\\"received\\\", []):\\n    \\n    the_header = eml_header.get(\\\"from\\\", None)\\n    \\n    if the_header:\\n      ips = re.findall(\u0027(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\u0027, the_header)\\n      unique_ips = set(ips)\\n  \\n      for an_ip in unique_ips:\\n        if an_ip:\\n          incident.addArtifact(\\\"IP Address\\\", an_ip, u\\\"Hop {0} at {1}\\\\n\\\\nHeader: {2}\\\".format(eml_header.get(\\\"hop\\\", \\\"\\\"), eml_header.get(\\\"date_utc\\\", \\\"\\\"), the_header))\\n\\n  ##############################################\\n  # Add Artifacts for URLs found in Email Body #\\n  ##############################################\\n  urls = []\\n  for eml_body_content in [email.get(\\\"plain_body\\\", \\\"\\\"), email.get(\\\"html_body\\\", \\\"\\\")]:\\n    urls.extend(re.findall(\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026amp;+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027, eml_body_content))\\n\\n  uniq_urls = set(urls)\\n\\n  for a_url in uniq_urls:\\n    # Remove any backslash as regex can add\\n    a_url = a_url.replace(\u0027\\\\\\\\\u0027,\\\"\\\")\\n    if a_url:\\n      incident.addArtifact(\\\"URL\\\", a_url, \\\"Found in parsed Email\\\")\\n  \\n  ################################################\\n  # Add the Email Body as a Note to the Incident #\\n  ################################################\\n  if email.get(\\\"body\\\"):\\n    note_text = u\\\"\\\"\\\"\u0026lt;b\u0026gt;Parsed Email::\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Subject:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;From:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;To:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{2}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Body:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{3}\\\"\\\"\\\".format(unicode(eml_subject),\\n                                  unicode(email.get(\\\"from\\\", \\\"N/A\\\")),\\n                                  unicode(email.get(\\\"to\\\", \\\"N/A\\\")), \\n                                  unicode(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n  \\n  \u0027\u0027\u0027Uncomment this if you would like to add a (safer) plain_text only Note\\n  if email.get(\\\"plain_body\\\"):\\n    note_text = u\\\"\\\"\\\"Parsed Email::\\\\n\\\\nSubject:\\\\n{0}\\\\n\\\\nFrom:\\\\n{1}\\\\n\\\\nTo:\\\\n{2}\\\\n\\\\nBody:\\\\n{3}\\\"\\\"\\\".format(unicode(eml_subject),\\n      unicode(email.get(\\\"from\\\", \\\"N/A\\\")), unicode(email.get(\\\"to\\\", \\\"N/A\\\")), unicode(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createPlainText(note_text))\\n  \u0027\u0027\u0027\",\"pre_processing_script\":\"# Define incident_id and attachment_id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# Setting this to True will add any found attachments as an Email Attachment Artifact\\ninputs.utilities_parse_email_attachments = True\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0a3f8pj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f19d8l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0a3f8pj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0mbl607\"/\u003e\u003cendEvent id=\"EndEvent_0or8ho0\"\u003e\u003cincoming\u003eSequenceFlow_0f19d8l\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0f19d8l\" sourceRef=\"ServiceTask_0mbl607\" targetRef=\"EndEvent_0or8ho0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xkpnc6\"\u003e\u003ctext\u003e\u003c![CDATA[Additional artifacts created based on the email message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rmikmt\" sourceRef=\"ServiceTask_0mbl607\" targetRef=\"TextAnnotation_0xkpnc6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"234\" y=\"123\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"229\" y=\"158\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0mbl607\" id=\"ServiceTask_0mbl607_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"403\" y=\"101\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0a3f8pj\" id=\"SequenceFlow_0a3f8pj_di\"\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"291.5\" y=\"119.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0or8ho0\" id=\"EndEvent_0or8ho0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"619\" y=\"123\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"592\" y=\"162\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f19d8l\" id=\"SequenceFlow_0f19d8l_di\"\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003comgdi:waypoint x=\"619\" xsi:type=\"omgdc:Point\" y=\"141\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"561\" y=\"119.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xkpnc6\" id=\"TextAnnotation_0xkpnc6_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"213\" x=\"492\" y=\"12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rmikmt\" id=\"Association_0rmikmt_di\"\u003e\u003comgdi:waypoint x=\"500\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"70\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "Example Workflow showing to parse an Email File (.eml or .msg) from Incident/Task Attachments. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.",
      "export_key": "example_email_parsing_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647872651827,
      "name": "Example: Email Parsing (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "example_email_parsing_attachment",
      "tags": [],
      "uuid": "3d33c5fa-1b83-4fbb-ac62-5d9053b43d40",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
