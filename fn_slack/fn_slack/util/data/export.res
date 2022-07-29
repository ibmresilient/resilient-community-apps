{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Archive Incident Slack Channel",
      "id": 37,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Archive Incident Slack Channel",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1835248d-cb58-45c6-8bb6-e30be25fe5e3",
      "view_items": [
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "archive_slack_channel"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Archive Task Slack Channel",
      "id": 38,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Archive Task Slack Channel",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0ce98ccf-197d-45ed-9543-8a9d59f0e767",
      "view_items": [
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "slack_example_archive_slack_channel__task"
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
            "Log File",
            "Other File",
            "X509 Certificate File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Post Artifact Attachment to Slack",
      "id": 39,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Artifact Attachment to Slack",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0a8570be-c6ba-4f1d-83a1-67bd95647975",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_post_attachment_to_slack__artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "not_in",
          "type": null,
          "value": [
            "RFC 822 Email Message File",
            "Email Attachment",
            "Log File",
            "Other File",
            "X509 Certificate File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Post Artifact to Slack",
      "id": 40,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Artifact to Slack",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "dfd73b22-4438-46ea-9e01-888edc0174e7",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "slack_example_post_message_to_slack__artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post Incident / Task Attachment to Slack",
      "id": 41,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Incident / Task Attachment to Slack",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4bd47712-bc92-405d-9367-39affe544b91",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "slack_example_post_attachment_to_slack"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post Incident to Slack",
      "id": 42,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Incident to Slack",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c915619e-ca11-4fb1-ba9d-a2d9439c92f2",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "create_slack_message"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post Note to Slack",
      "id": 43,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Note to Slack",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac5066e7-2644-48e3-9ecb-85ec2c16bb6d",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "create_slack_reply"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post Task to Slack",
      "id": 44,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post Task to Slack",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "154221cd-f1c1-4c6c-b4d2-61ff709e23fb",
      "view_items": [
        {
          "content": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "slack_example_post_message_to_slack__task"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1659122459837,
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
      "export_key": "__function/slack_text",
      "hide_notification": false,
      "id": 313,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_text",
      "tooltip": "Text message or a container field to retain JSON fields to send to Slack.",
      "type_id": 11,
      "uuid": "85d20b77-734f-4930-9c4b-b5f8d98c581c",
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
      "uuid": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
      "export_key": "__function/slack_channel_id",
      "hide_notification": false,
      "id": 316,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_channel_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "slack_channel_id",
      "tooltip": "Optional. Executing without channel ID archives the channel that this is associated with.",
      "type_id": 11,
      "uuid": "9846df31-5b76-4299-b12b-17e0c6551791",
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
      "uuid": "9997e04c-bdbe-4f7c-9b87-2bc0390826fe",
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
      "export_key": "__function/slack_channel",
      "hide_notification": false,
      "id": 312,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_channel",
      "tooltip": "Name of the existing or a new slack channel used to send message to. Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less.",
      "type_id": 11,
      "uuid": "9caadb86-3cb1-44f8-81f4-4da30e68a106",
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
      "export_key": "__function/slack_participant_emails",
      "hide_notification": false,
      "id": 314,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_participant_emails",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_participant_emails",
      "tooltip": "Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.",
      "type_id": 11,
      "uuid": "ae82a20a-d6ae-4f77-98d8-1388dfa4b2f7",
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
      "export_key": "__function/slack_is_channel_private",
      "hide_notification": false,
      "id": 315,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "slack_is_channel_private",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_is_channel_private",
      "tooltip": "Indicate if the channel you are posting to should be private.",
      "type_id": 11,
      "uuid": "cc231126-4f49-4237-998b-d9570664d662",
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
      "uuid": "d63d16a1-c5bd-4015-9850-05316b22564c",
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
      "export_key": "__function/slack_mrkdwn",
      "hide_notification": false,
      "id": 309,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "slack_mrkdwn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_mrkdwn",
      "tooltip": "Disable Slack markup parsing by setting to false.",
      "type_id": 11,
      "uuid": "2388be49-283f-4b77-bbeb-86a2ee1dcf08",
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
      "uuid": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
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
      "export_key": "__function/slack_as_user",
      "hide_notification": false,
      "id": 310,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "slack_as_user",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_as_user",
      "tooltip": "Set to true and the authenticated user of the Slack App will appear as the author of the message, ignoring any values provided for slack_username. ",
      "type_id": 11,
      "uuid": "48e593f4-3cc4-4f3e-a809-38e5fed70f20",
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
      "export_key": "__function/slack_username",
      "hide_notification": false,
      "id": 311,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "slack_username",
      "tooltip": "Set your Slack app\u0027s name that will appear as the author of the message. Must be used in conjunction with slack_as_user set to false, otherwise ignored.",
      "type_id": 11,
      "uuid": "74365ed2-635a-446a-ba39-65b264b7ad54",
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
      "export_key": "actioninvocation/rule_slack_participant_emails",
      "hide_notification": false,
      "id": 307,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rule_slack_participant_emails",
      "operation_perms": {},
      "operations": [],
      "placeholder": "slack.user@email.com, slack.user2@email.com, ",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "Slack users emails",
      "tooltip": "Comma separated list of emails belonging to Slack users in your workspace that will be added to the channel you are posting to.",
      "type_id": 6,
      "uuid": "b2df44e2-5ae6-43ae-b86c-9c5f475f9c79",
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
      "export_key": "actioninvocation/rule_slack_channel",
      "hide_notification": false,
      "id": 305,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rule_slack_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Existing or new Slack channel name",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "Slack channel name",
      "tooltip": "Name of the existing Slack channel or a new Slack channel you are posting to. Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. If there isn\u2019t one defined, the workflow will terminate.",
      "type_id": 6,
      "uuid": "24df3e1c-2c28-4e7d-ac28-4fea0a3877a2",
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
      "export_key": "actioninvocation/rule_slack_text",
      "hide_notification": false,
      "id": 306,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rule_slack_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Please review posted Resilient Data",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "Additional text",
      "tooltip": "Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.",
      "type_id": 6,
      "uuid": "2f0fcad3-79f1-410b-b7f0-6a6fa0ee3947",
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
      "export_key": "actioninvocation/rule_slack_is_channel_private",
      "hide_notification": false,
      "id": 308,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "rule_slack_is_channel_private",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "templates": [],
      "text": "Slack is channel private",
      "tooltip": "Indicate if the channel you are posting to should be private.",
      "type_id": 6,
      "uuid": "3b1a6628-5ef0-495c-955e-10c3e5f9f4e2",
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
      "export_key": "actioninvocation/slack_channel_id",
      "hide_notification": false,
      "id": 317,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "slack_channel_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Slack Channel ID",
      "tooltip": "",
      "type_id": 6,
      "uuid": "7cbbbfdf-f1a0-4e32-9e5c-632a1835de1e",
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
      "created_date": 1656524808499,
      "description": {
        "content": "Function exports conversation history from Slack channel to a text file, saves the text file as an Attachment and archives the Slack channel.",
        "format": "text"
      },
      "destination_handle": "slack",
      "display_name": "Archive Slack Channel",
      "export_key": "slack_archive_channel",
      "id": 16,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1658779455388,
      "name": "slack_archive_channel",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "8f3a9d1d-8182-4c5b-b422-cfeee33de0dc",
      "version": 3,
      "view_items": [
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9846df31-5b76-4299-b12b-17e0c6551791",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
          "name": "Example: Archive Incident Slack Channel",
          "object_type": "incident",
          "programmatic_name": "archive_slack_channel",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 35
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Archive Task Slack Channel",
          "object_type": "task",
          "programmatic_name": "slack_example_archive_slack_channel__task",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 31
        }
      ]
    },
    {
      "created_date": 1656524808581,
      "description": {
        "content": "Function uploads Incident, Task or Artifact Attachments to Slack channel.",
        "format": "text"
      },
      "destination_handle": "slack",
      "display_name": "Post attachment to Slack",
      "export_key": "slack_post_attachment",
      "id": 17,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1658953776885,
      "name": "slack_post_attachment",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "5fed4dd5-9ccc-492a-90e1-4f17e6a5c5c8",
      "version": 3,
      "view_items": [
        {
          "content": "9caadb86-3cb1-44f8-81f4-4da30e68a106",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cc231126-4f49-4237-998b-d9570664d662",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae82a20a-d6ae-4f77-98d8-1388dfa4b2f7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "85d20b77-734f-4930-9c4b-b5f8d98c581c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9846df31-5b76-4299-b12b-17e0c6551791",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d63d16a1-c5bd-4015-9850-05316b22564c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9997e04c-bdbe-4f7c-9b87-2bc0390826fe",
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
          "name": "Example: Post Artifact Attachment to Slack",
          "object_type": "artifact",
          "programmatic_name": "example_post_attachment_to_slack__artifact",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 33
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Post Incident / Task Attachment to Slack",
          "object_type": "attachment",
          "programmatic_name": "slack_example_post_attachment_to_slack",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 34
        }
      ]
    },
    {
      "created_date": 1656524808661,
      "description": {
        "content": "Function sends a message from an Incident, Task, Note or an Artifact to a Slack channel.",
        "format": "text"
      },
      "destination_handle": "slack",
      "display_name": "Post message to Slack",
      "export_key": "slack_post_message",
      "id": 18,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1658944357128,
      "name": "slack_post_message",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "ded2826c-6528-4a26-b2c8-0cf215dce3c3",
      "version": 3,
      "view_items": [
        {
          "content": "9caadb86-3cb1-44f8-81f4-4da30e68a106",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cc231126-4f49-4237-998b-d9570664d662",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae82a20a-d6ae-4f77-98d8-1388dfa4b2f7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "85d20b77-734f-4930-9c4b-b5f8d98c581c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2388be49-283f-4b77-bbeb-86a2ee1dcf08",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48e593f4-3cc4-4f3e-a809-38e5fed70f20",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9846df31-5b76-4299-b12b-17e0c6551791",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "74365ed2-635a-446a-ba39-65b264b7ad54",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
          "name": "Example: Post Artifact to Slack",
          "object_type": "artifact",
          "programmatic_name": "slack_example_post_message_to_slack__artifact",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 37
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Post Incident to Slack",
          "object_type": "incident",
          "programmatic_name": "create_slack_message",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 32
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Post Note to Slack",
          "object_type": "note",
          "programmatic_name": "create_slack_reply",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 38
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Post Task to Slack",
          "object_type": "task",
          "programmatic_name": "slack_example_post_message_to_slack__task",
          "tags": [
            {
              "tag_handle": "fn_slack",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 36
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 112,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1659122458093,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1659122458093,
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
        "bef198c5-cc54-4377-95c5-f98bf2cccfd8"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "slack",
      "name": "slack",
      "programmatic_name": "slack",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "users": [],
      "uuid": "611f10f7-1b7d-49c5-8692-3b838156d42b"
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
  "types": [
    {
      "actions": [],
      "display_name": "Slack Conversations",
      "export_key": "slack_conversations_db",
      "fields": {
        "slack_db_channel": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "slack_conversations_db/slack_db_channel",
          "hide_notification": false,
          "id": 300,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "slack_db_channel",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Slack channel name",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "df0165d4-6367-4914-b80c-c8877b20c011",
          "values": [],
          "width": 165
        },
        "slack_db_channel_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "slack_conversations_db/slack_db_channel_type",
          "hide_notification": false,
          "id": 301,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "slack_db_channel_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Slack channel type",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "ce4c8399-09e3-481a-976f-b076c98965f7",
          "values": [],
          "width": 67
        },
        "slack_db_permalink": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "slack_conversations_db/slack_db_permalink",
          "hide_notification": false,
          "id": 302,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "slack_db_permalink",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Slack URL",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "2f95366b-dd32-4035-8811-549646c0af5c",
          "values": [],
          "width": 79
        },
        "slack_db_res_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "slack_conversations_db/slack_db_res_id",
          "hide_notification": false,
          "id": 303,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "slack_db_res_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Resilient ID",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "ce3c9a1e-2800-47da-a5b9-c37825790943",
          "values": [],
          "width": 211
        },
        "slack_db_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "slack_conversations_db/slack_db_time",
          "hide_notification": false,
          "id": 304,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "slack_db_time",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Time",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "656a7daf-b64a-4559-987d-b789d0ec4c4b",
          "values": [],
          "width": 123
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
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "slack_conversations_db",
      "uuid": "e2036bf3-61ea-4752-8d6f-2b4ea262bb1b"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_post_attachment_to_slack__artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_post_attachment_to_slack__artifact\" isExecutable=\"true\" name=\"Example: Post Artifact Attachment to Slack\"\u003e\u003cdocumentation\u003eUpload Artifact Attachment to your Slack channel with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02jshqf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0dgxaqk\" name=\"Post attachment to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5fed4dd5-9ccc-492a-90e1-4f17e6a5c5c8\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Artifact Attachment was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Attachment data   #\\n#####################\\n\\n# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\ninputs.slack_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02jshqf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0p08bye\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0xull0j\"\u003e\u003cincoming\u003eSequenceFlow_0p08bye\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_02jshqf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0dgxaqk\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0p08bye\" sourceRef=\"ServiceTask_0dgxaqk\" targetRef=\"EndEvent_0xull0j\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1u0wsmu\"\u003e\u003ctext\u003e\u003c![CDATA[Post the Artifact attachment to slack_channel associated with the Incident\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_199m89l\" sourceRef=\"ServiceTask_0dgxaqk\" targetRef=\"TextAnnotation_1u0wsmu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0dgxaqk\" id=\"ServiceTask_0dgxaqk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"340\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0xull0j\" id=\"EndEvent_0xull0j_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"571\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"589\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02jshqf\" id=\"SequenceFlow_02jshqf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"340\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"269\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p08bye\" id=\"SequenceFlow_0p08bye_di\"\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"571\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"505.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1u0wsmu\" id=\"TextAnnotation_1u0wsmu_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"233\" x=\"227\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_199m89l\" id=\"Association_199m89l_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"69\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Upload Artifact Attachment to your Slack channel with an optional custom text message.",
      "export_key": "example_post_attachment_to_slack__artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953789953,
      "name": "Example: Post Artifact Attachment to Slack",
      "object_type": "artifact",
      "programmatic_name": "example_post_attachment_to_slack__artifact",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "27254f22-8ebb-4790-a557-0a83cb802196",
      "workflow_id": 33
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "slack_example_post_message_to_slack__artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"slack_example_post_message_to_slack__artifact\" isExecutable=\"true\" name=\"Example: Post Artifact to Slack\"\u003e\u003cdocumentation\u003ePost a message from the Artifact to your Slack channel. Send specifics about the Artifact with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_08g2949\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xyyaqt\" name=\"Post message to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ded2826c-6528-4a26-b2c8-0cf215dce3c3\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Artifact was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Artifact data     #\\n#####################\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\nrule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# Incident id for the URL\\nincident_id_str = str(incident.id)\\n\\n# Slack text message in JSON format\\n# ---------------------------------\\n# Do not remove first 3 elements \\\"Additional Text\\\", \\\"Resilient URL\\\" and \\\"Type of data\\\",\\n# the information is used to generate the title of the message.\\n#\\n# Add/remove information using the syntax:\\n# \\\"label\\\": {{ \\\"type\\\": \\\"[string|richtext|boolean|datetime\\\", \\\"data\\\": \\\"resilient field data\\\" }}\\n#\\n# Make sure to send \\\"datetime\\\" types as integers and not strings:\\n# without double quotes: { \\\"type\\\": \\\"datetime\\\", \\\"data\\\": resilient datetime data}  \\n#\\n# Text fields like \u0027artifact.value\u0027, or \u0027Slack additional text message\u0027 can include double quotes.\\n# Watch out for embedded double quotes in these text fields and escape with field.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) otherwise json.loads will fail.\\nslack_text = u\\\"\\\"\\\"{{\\n  \\\"Additional Text\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{0}\\\" }},\\n  \\\"Resilient URL\\\": {{\\\"type\\\": \\\"incident\\\", \\\"data\\\": \\\"{1}\\\" }},\\n  \\\"Type of data\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{2}\\\" }},\\n  \\\"Incident ID\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{3}\\\" }},\\n  \\\"Artifact Type\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{4}\\\" }},\\n  \\\"Artifact Value\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{5}\\\" }},\\n  \\\"Artifact Created By\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{6}\\\" }},\\n  \\\"Artifact Created on\\\": {{\\\"type\\\": \\\"datetime\\\", \\\"data\\\": {7} }}\\n}}\\\"\\\"\\\".format(\\n  rule_additional_text.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  incident_id_str,\\n  \\\"Artifact\\\",\\n  incident_id_str,\\n  artifact.type,\\n  artifact.value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  artifact.creator.display_name,\\n  artifact.created)\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack text message\\n# Container field to retain JSON fields to send to Slack.\\ninputs.slack_text = slack_text\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_08g2949\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0whqsky\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0783g0m\"\u003e\u003cincoming\u003eSequenceFlow_0whqsky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_08g2949\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xyyaqt\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0whqsky\" sourceRef=\"ServiceTask_0xyyaqt\" targetRef=\"EndEvent_0783g0m\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1xoivld\"\u003e\u003ctext\u003eSelect the slack_channel to post in and adjust the posting parameters as needed.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nzdxaz\" sourceRef=\"ServiceTask_0xyyaqt\" targetRef=\"TextAnnotation_1xoivld\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xyyaqt\" id=\"ServiceTask_0xyyaqt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0783g0m\" id=\"EndEvent_0783g0m_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"617\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"635\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08g2949\" id=\"SequenceFlow_08g2949_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"276.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0whqsky\" id=\"SequenceFlow_0whqsky_di\"\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"617\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"536\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1xoivld\" id=\"TextAnnotation_1xoivld_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"330\" x=\"238\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nzdxaz\" id=\"Association_1nzdxaz_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"72\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Post a message from the Artifact to your Slack channel. Send specifics about the Artifact with an optional custom text message.",
      "export_key": "slack_example_post_message_to_slack__artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658951158643,
      "name": "Example: Post Artifact to Slack",
      "object_type": "artifact",
      "programmatic_name": "slack_example_post_message_to_slack__artifact",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "b3846e02-e1f9-420e-86ac-5bf0b8f95a9f",
      "workflow_id": 37
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "archive_slack_channel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"archive_slack_channel\" isExecutable=\"true\" name=\"Example: Archive Incident Slack Channel\"\u003e\u003cdocumentation\u003eExports conversation history from Incident associated Slack channel to a text file, saves the text file as an Attachment and archives the Slack channel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_13rdgzt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1x24c40\" name=\"Archive Slack Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8f3a9d1d-8182-4c5b-b422-cfeee33de0dc\"\u003e{\"inputs\":{},\"post_processing_script\":\"noteText = u\\\"\\\"\\\"Slack channel {} has been archived. The conversation history has been saved as an attachment.\\\"\\\"\\\".format(results.channel)\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"# ID of this incident\\ninputs.incident_id = incident.id\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_13rdgzt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qph1pl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_13rdgzt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1x24c40\"/\u003e\u003cendEvent id=\"EndEvent_0wgzq5t\"\u003e\u003cincoming\u003eSequenceFlow_0qph1pl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0qph1pl\" sourceRef=\"ServiceTask_1x24c40\" targetRef=\"EndEvent_0wgzq5t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_058bva1\"\u003e\u003ctext\u003e\u003c![CDATA[Automatic rule archives slack_channel associated with the Incident\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0iu0j14\" sourceRef=\"ServiceTask_1x24c40\" targetRef=\"TextAnnotation_058bva1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1x24c40\" id=\"ServiceTask_1x24c40_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"376\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13rdgzt\" id=\"SequenceFlow_13rdgzt_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"287\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wgzq5t\" id=\"EndEvent_0wgzq5t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"676\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"694\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qph1pl\" id=\"SequenceFlow_0qph1pl_di\"\u003e\u003comgdi:waypoint x=\"476\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"676\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"576\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_058bva1\" id=\"TextAnnotation_058bva1_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"228\" x=\"219\" y=\"37\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0iu0j14\" id=\"Association_0iu0j14_di\"\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Exports conversation history from Incident associated Slack channel to a text file, saves the text file as an Attachment and archives the Slack channel.",
      "export_key": "archive_slack_channel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658856055309,
      "name": "Example: Archive Incident Slack Channel",
      "object_type": "incident",
      "programmatic_name": "archive_slack_channel",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "390425c1-1ce6-4f31-a522-372c19ba2370",
      "workflow_id": 35
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "create_slack_message",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"create_slack_message\" isExecutable=\"true\" name=\"Example: Post Incident to Slack\"\u003e\u003cdocumentation\u003ePost a message from the Incident to your Slack channel. Send specifics about the Incident with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1gqs27q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1gqs27q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_198r21t\"/\u003e\u003cendEvent id=\"EndEvent_1qowt87\"\u003e\u003cincoming\u003eSequenceFlow_1x6iad8\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_198r21t\" name=\"Post message to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ded2826c-6528-4a26-b2c8-0cf215dce3c3\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Incident was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Incident data     #\\n#####################\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\nrule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# \\\"datetime\\\" fields: Assign 0 if it\u0027s None\\ndate_occured = incident.start_date if incident.start_date else 0\\ndate_discovered = incident.discovered_date if incident.discovered_date else 0\\n\\n# Incident id for the URL\\nincident_id_str = str(incident.id)\\n\\n# Slack text message in JSON format\\n# ---------------------------------\\n# Do not remove first 3 elements \\\"Additional Text\\\", \\\"Resilient URL\\\" and \\\"Type of data\\\",\\n# the information is used to generate the title of the message.\\n#\\n# Add/remove information using the syntax:\\n# \\\"label\\\": {{ \\\"type\\\": \\\"[string|richtext|boolean|datetime\\\", \\\"data\\\": \\\"resilient field data\\\" }}\\n#\\n# Make sure to send \\\"datetime\\\" types as integers and not strings:\\n# without double quotes: { \\\"type\\\": \\\"datetime\\\", \\\"data\\\": resilient datetime data}  \\n#\\n# Text fields like \u0027incident name\u0027, \u0027description\u0027 or \u0027Slack additional text message\u0027 can include double quotes.\\n# Watch out for embedded double quotes in these text fields and escape with field.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) otherwise json.loads will fail.\\nslack_text = u\\\"\\\"\\\"{{\\n  \\\"Additional Text\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{0}\\\" }},\\n  \\\"Resilient URL\\\": {{\\\"type\\\": \\\"incident\\\", \\\"data\\\": \\\"{1}\\\" }},\\n  \\\"Type of data\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{2}\\\" }},\\n  \\\"Incident ID\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{3}\\\" }},\\n  \\\"Incident name\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{4}\\\" }},\\n  \\\"Description\\\": {{\\\"type\\\": \\\"richtext\\\", \\\"data\\\": \\\"{5}\\\" }},\\n  \\\"Incident Types\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{6}\\\" }},\\n  \\\"NIST Attack Vectors\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{7}\\\" }},\\n  \\\"Confirmed\\\": {{\\\"type\\\": \\\"boolean\\\", \\\"data\\\": \\\"{8}\\\" }},\\n  \\\"Date Created\\\": {{\\\"type\\\": \\\"datetime\\\", \\\"data\\\": {9} }},\\n  \\\"Date Occurred\\\": {{\\\"type\\\": \\\"datetime\\\", \\\"data\\\": {10} }},\\n  \\\"Date Discovered\\\": {{\\\"type\\\": \\\"datetime\\\", \\\"data\\\": {11} }},\\n  \\\"Severity\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{12}\\\" }}\\n}}\\\"\\\"\\\".format(\\n  rule_additional_text.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  incident_id_str,\\n  \\\"Incident\\\",\\n  incident_id_str,\\n  incident.name.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  incident.description.content.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) if incident.description is not None else \u0027\u0027,\\n  incident.incident_type_ids,\\n  incident.nist_attack_vectors,\\n  incident.confirmed,\\n  incident.create_date,\\n  date_occured,\\n  date_discovered,\\n  incident.severity_code)\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to the channel you are posting to.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack text message\\n# Container field to retain JSON fields to send to Slack.\\ninputs.slack_text = slack_text\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1gqs27q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1x6iad8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x6iad8\" sourceRef=\"ServiceTask_198r21t\" targetRef=\"EndEvent_1qowt87\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1xz2ir5\"\u003e\u003ctext\u003eSelect the slack_channel to post in and adjust the posting parameters as needed.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ijfiwn\" sourceRef=\"ServiceTask_198r21t\" targetRef=\"TextAnnotation_1xz2ir5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gqs27q\" id=\"SequenceFlow_1gqs27q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"283\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"195.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1qowt87\" id=\"EndEvent_1qowt87_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"445\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"418\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_198r21t\" id=\"ServiceTask_198r21t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"283\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x6iad8\" id=\"SequenceFlow_1x6iad8_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"445\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1xz2ir5\" id=\"TextAnnotation_1xz2ir5_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"245\" x=\"161\" y=\"34\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ijfiwn\" id=\"Association_0ijfiwn_di\"\u003e\u003comgdi:waypoint x=\"320\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"294\" xsi:type=\"omgdc:Point\" y=\"90\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Post a message from the Incident to your Slack channel. Send specifics about the Incident with an optional custom text message.",
      "export_key": "create_slack_message",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953416469,
      "name": "Example: Post Incident to Slack",
      "object_type": "incident",
      "programmatic_name": "create_slack_message",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "8df6f333-4423-4e9d-9554-dceacd311cba",
      "workflow_id": 32
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "slack_example_post_attachment_to_slack",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"slack_example_post_attachment_to_slack\" isExecutable=\"true\" name=\"Example: Post Incident / Task Attachment to Slack\"\u003e\u003cdocumentation\u003eUpload Incident or Task Attachment to your Slack channel with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pp0jtw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0nkb5nu\" name=\"Post attachment to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5fed4dd5-9ccc-492a-90e1-4f17e6a5c5c8\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Attachment was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\nif not task:\\n  incident.addNote(helper.createRichText(noteText))\\nelse:\\n  task.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Attachment data   #\\n#####################\\n\\n# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\ninputs.slack_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pp0jtw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14wmcls\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0a4s5nt\"\u003e\u003cincoming\u003eSequenceFlow_14wmcls\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pp0jtw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nkb5nu\"/\u003e\u003csequenceFlow id=\"SequenceFlow_14wmcls\" sourceRef=\"ServiceTask_0nkb5nu\" targetRef=\"EndEvent_0a4s5nt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_03c85uj\"\u003e\u003ctext\u003e\u003c![CDATA[Post the attachment to slack_channel associated with the Incident or Task\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02owjkj\" sourceRef=\"ServiceTask_0nkb5nu\" targetRef=\"TextAnnotation_03c85uj\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nkb5nu\" id=\"ServiceTask_0nkb5nu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"321\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0a4s5nt\" id=\"EndEvent_0a4s5nt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"570\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"588\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pp0jtw\" id=\"SequenceFlow_1pp0jtw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"321\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"259.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14wmcls\" id=\"SequenceFlow_14wmcls_di\"\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"570\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"495.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_03c85uj\" id=\"TextAnnotation_03c85uj_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"327\" x=\"227\" y=\"48\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02owjkj\" id=\"Association_02owjkj_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"78\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Upload Incident or Task Attachment to your Slack channel with an optional custom text message.",
      "export_key": "slack_example_post_attachment_to_slack",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953808722,
      "name": "Example: Post Incident / Task Attachment to Slack",
      "object_type": "attachment",
      "programmatic_name": "slack_example_post_attachment_to_slack",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "dc4c831c-a444-4aac-aa1c-c74899ef9a50",
      "workflow_id": 34
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "slack_example_archive_slack_channel__task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"slack_example_archive_slack_channel__task\" isExecutable=\"true\" name=\"Example: Archive Task Slack Channel\"\u003e\u003cdocumentation\u003eExports conversation history from Task associated Slack channel to a text file, saves the text file as an Attachment and archives the Slack channel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0khlygq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0uvdhjs\" name=\"Archive Slack Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8f3a9d1d-8182-4c5b-b422-cfeee33de0dc\"\u003e{\"inputs\":{},\"post_processing_script\":\"noteText = u\\\"\\\"\\\"Slack channel {} has been archived. The conversation history has been saved as an attachment.\\\"\\\"\\\".format(results.channel)\\ntask.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this Task\\ninputs.task_id = task.id\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0khlygq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jwewkk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_148fqcs\"\u003e\u003cincoming\u003eSequenceFlow_0jwewkk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0khlygq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0uvdhjs\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0jwewkk\" sourceRef=\"ServiceTask_0uvdhjs\" targetRef=\"EndEvent_148fqcs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0fsfdaw\"\u003e\u003ctext\u003eAutomatic rule archives slack_channel associated with the Task\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1gqr3wj\" sourceRef=\"ServiceTask_0uvdhjs\" targetRef=\"TextAnnotation_0fsfdaw\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0uvdhjs\" id=\"ServiceTask_0uvdhjs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"363\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_148fqcs\" id=\"EndEvent_148fqcs_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"631\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"649\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0khlygq\" id=\"SequenceFlow_0khlygq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"280.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jwewkk\" id=\"SequenceFlow_0jwewkk_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"547\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0fsfdaw\" id=\"TextAnnotation_0fsfdaw_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"237\" x=\"224\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1gqr3wj\" id=\"Association_1gqr3wj_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Exports conversation history from Task associated Slack channel to a text file, saves the text file as an Attachment and archives the Slack channel.",
      "export_key": "slack_example_archive_slack_channel__task",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953750397,
      "name": "Example: Archive Task Slack Channel",
      "object_type": "task",
      "programmatic_name": "slack_example_archive_slack_channel__task",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "fcc94828-cb91-4781-b706-f3a6ae01e805",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "slack_example_post_message_to_slack__task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"slack_example_post_message_to_slack__task\" isExecutable=\"true\" name=\"Example: Post Task to Slack\"\u003e\u003cdocumentation\u003ePost message from a Task to your Slack channel. Send specifics about the Task with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_19xrgry\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1r9jr12\" name=\"Post message to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ded2826c-6528-4a26-b2c8-0cf215dce3c3\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Task was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\ntask.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Task data         #\\n#####################\\n\\n# Incident id for the URL\\nincident_id_str = str(incident.id)\\nif task:\\n  incident_id_str += \\\"?task_id=\\\"+str(task.id)\\n\\n# Task due date, send 0 if it\u0027s None\\ntask_due_date = task.due_date if task.due_date else 0\\n\\n# Task Status\\ntask_status = \\\"Open\\\" if task.status == \\\"O\\\" else \\\"Closed\\\"\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\nrule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# Slack text message in JSON format\\n# ---------------------------------\\n# Do not remove first 3 elements \\\"Additional Text\\\", \\\"Resilient URL\\\" and \\\"Type of data\\\",\\n# the information is used to generate the title of the message.\\n#\\n# Add/remove information using the syntax:\\n# \\\"label\\\": {{ \\\"type\\\": \\\"[string|richtext|boolean|datetime\\\", \\\"data\\\": \\\"resilient field data\\\" }}\\n#\\n# Make sure to send \\\"datetime\\\" types as integers and not strings:\\n# without double quotes: { \\\"type\\\": \\\"datetime\\\", \\\"data\\\": resilient datetime data} \\n#\\n# Text fields like \u0027task name\u0027 or \u0027Slack additional text message\u0027 can include double quotes.\\n# Watch out for embedded double quotes in these text fields and escape with field.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) otherwise json.loads will fail.\\nslack_text = u\\\"\\\"\\\"{{\\n  \\\"Additional Text\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{0}\\\" }},\\n  \\\"Resilient URL\\\": {{\\\"type\\\": \\\"incident\\\", \\\"data\\\": \\\"{1}\\\" }},\\n  \\\"Type of data\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{2}\\\" }},\\n  \\\"Incident ID\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{3}\\\" }},\\n  \\\"Task Name\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{4}\\\" }},\\n  \\\"Task Status\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{5}\\\" }},\\n  \\\"Task Owner\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{6}\\\" }},\\n  \\\"Task Due Date\\\": {{\\\"type\\\": \\\"datetime\\\", \\\"data\\\": {7} }}\\n}}\\\"\\\"\\\".format(\\n  rule_additional_text.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  incident_id_str,\\n  \\\"Task\\\",\\n  str(incident.id),\\n  task.name.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  task_status,\\n  task.owner_id,\\n  task_due_date)\\n\\n# Slack username - optional setting\\n# Set to true and the authenticated user of the Slack App will appear as the author of the message, ignoring any values provided for slack_username. \\n# Set your bot\u0027s name to Task\u0027s creator to appear as the author of the message. Must be used in conjunction with slack_as_user set to false, otherwise ignored.\\n#inputs.slack_as_user = False\\n#inputs.slack_username = task.creator_id\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this Task\\ninputs.task_id = task.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack text message\\n# Container field to retain JSON fields to send to Slack\\ninputs.slack_text = slack_text\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_19xrgry\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0e01qi0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0p33e7s\"\u003e\u003cincoming\u003eSequenceFlow_0e01qi0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_19xrgry\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1r9jr12\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0e01qi0\" sourceRef=\"ServiceTask_1r9jr12\" targetRef=\"EndEvent_0p33e7s\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0pfr687\"\u003e\u003ctext\u003eSelect the slack_channel to post in and adjust the posting parameters as needed.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1sw39lm\" sourceRef=\"ServiceTask_1r9jr12\" targetRef=\"TextAnnotation_0pfr687\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1r9jr12\" id=\"ServiceTask_1r9jr12_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"332\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0p33e7s\" id=\"EndEvent_0p33e7s_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"583\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"601\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19xrgry\" id=\"SequenceFlow_19xrgry_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"332\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"265\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0e01qi0\" id=\"SequenceFlow_0e01qi0_di\"\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"583\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"507.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0pfr687\" id=\"TextAnnotation_0pfr687_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"286\" x=\"197\" y=\"51\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1sw39lm\" id=\"Association_1sw39lm_di\"\u003e\u003comgdi:waypoint x=\"370\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"345\" xsi:type=\"omgdc:Point\" y=\"81\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Post message from a Task to your Slack channel. Send specifics about the Task with an optional custom text message.",
      "export_key": "slack_example_post_message_to_slack__task",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953850402,
      "name": "Example: Post Task to Slack",
      "object_type": "task",
      "programmatic_name": "slack_example_post_message_to_slack__task",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "eba8f270-2d03-4da8-a812-2c8783742454",
      "workflow_id": 36
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "create_slack_reply",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"create_slack_reply\" isExecutable=\"true\" name=\"Example: Post Note to Slack\"\u003e\u003cdocumentation\u003ePost a message from the Note to your Slack channel. Send specifics about the Incident or Task Note with an optional custom text message.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14fo81e\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1rb28yp\" name=\"Post message to Slack\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ded2826c-6528-4a26-b2c8-0cf215dce3c3\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Create a note\\nnoteText = u\\\"\\\"\\\"Note was posted to \u0026lt;a href=\u0027{}\u0027\u0026gt;Slack channel #{}\u0026lt;/a\u0026gt;.\\\"\\\"\\\".format(results.url, results.channel)\\nif not task:\\n  incident.addNote(helper.createRichText(noteText))\\nelse:\\n  task.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"#####################\\n# Note data         #\\n#####################\\n\\n# Slack additional text message\\n# Additional text message to include with the Incident, Note, Artifact, Attachment or Task data.\\nrule_additional_text = rule.properties.rule_slack_text if rule.properties.rule_slack_text is not None else \u0027\u0027\\n\\n# Incident id for the URL\\nincident_id = str(incident.id)\\ntype_data = \\\"Incident Note\\\"\\nif task:\\n  incident_id += \\\"?task_id=\\\"+str(task.id)\\n  type_data = \\\"Task Note\\\"\\n\\n# Slack text message in JSON format\\n# ---------------------------------\\n# Do not remove first 3 elements \\\"Additional Text\\\", \\\"Resilient URL\\\" and \\\"Type of data\\\",\\n# the information is used to generate the title of the message.\\n#\\n# Add/remove information using the syntax:\\n# \\\"label\\\": {{ \\\"type\\\": \\\"[string|richtext|boolean|datetime\\\", \\\"data\\\": \\\"resilient field data\\\" }}\\n#\\n# Make sure to send \\\"datetime\\\" types as integers and not strings:\\n# without double quotes: { \\\"type\\\": \\\"datetime\\\", \\\"data\\\": resilient datetime data} \\n#\\n# Text fields like \u0027note.text.content\u0027, \u0027task.name\u0027 or \u0027Slack additional text message\u0027 can include double quotes.\\n# Watch out for embedded double quotes in these text fields and escape with field.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) otherwise json.loads will fail.\\nslack_text = u\\\"\\\"\\\"{{\\n  \\\"Additional Text\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{0}\\\" }},\\n  \\\"Resilient URL\\\": {{\\\"type\\\": \\\"incident\\\", \\\"data\\\": \\\"{1}\\\" }},\\n  \\\"Type of data\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{2}\\\" }},\\n  \\\"Incident ID\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{3}\\\" }},\\n  \\\"Task\\\": {{\\\"type\\\": \\\"string\\\", \\\"data\\\": \\\"{4}\\\" }},\\n  \\\"Note\\\": {{\\\"type\\\": \\\"richtext\\\", \\\"data\\\": \\\"{5}\\\" }}\\n}}\\\"\\\"\\\".format(\\n  rule_additional_text.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027),\\n  incident_id,\\n  type_data,\\n  str(incident.id),\\n  task.name.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) if task else \\\"\\\", \\n  note.text.content.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027) if note.text is not None else \u0027\u0027)\\n\\n# Slack username - optional setting\\n# Set to true and the authenticated user of the Slack App will appear as the author of the message, ignoring any values provided for slack_username. \\n# Set your bot\u0027s name to Note\u0027s creator to appear as the author of the message. Must be used in conjunction with slack_as_user set to false, otherwise ignored.\\n#inputs.slack_as_user = False\\n#inputs.slack_username = note.user_id\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this Task\\nif task:\\n  inputs.task_id = task.id\\n\\n# Slack channel name\\n# Name of the existing Slack Workspace channel or a new Slack channel you are posting to. \\n# Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 21 characters or less. \\n# If you leave this field empty, function will try to use the slack_channel associated with the Incident or Task found in the Slack Conversations datatable. \\n# If there isn\u2019t one defined, the workflow will terminate.\\ninputs.slack_channel = rule.properties.rule_slack_channel if rule.properties.rule_slack_channel is not None else inputs.slack_channel\\n\\n# Is channel private\\n# Indicate if the channel you are posting to should be private.\\ninputs.slack_is_channel_private = rule.properties.rule_slack_is_channel_private if rule.properties.rule_slack_is_channel_private is not None else inputs.slack_is_channel_private\\n\\n# Slack user emails\\n# Comma separated list of emails belonging to Slack users in your workspace that will be added to your channel.\\ninputs.slack_participant_emails = rule.properties.rule_slack_participant_emails if rule.properties.rule_slack_participant_emails is not None else inputs.slack_participant_emails\\n\\n# Slack text message\\n# Container field to retain JSON fields to send to Slack.\\ninputs.slack_text = slack_text\\n\\n# Slack Channel ID, faster than finding via channel name\\ninputs.slack_channel_id = rule.properties.slack_channel_id if rule.properties.slack_channel_id is not None else inputs.slack_channel_id\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14fo81e\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1h43fgg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14fo81e\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1rb28yp\"/\u003e\u003cendEvent id=\"EndEvent_0gvb0ht\"\u003e\u003cincoming\u003eSequenceFlow_1h43fgg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1h43fgg\" sourceRef=\"ServiceTask_1rb28yp\" targetRef=\"EndEvent_0gvb0ht\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0m1es7k\"\u003e\u003ctext\u003e\u003c![CDATA[Select the slack_channel to post in and adjust the posting parameters as needed.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dx6uag\" sourceRef=\"ServiceTask_1rb28yp\" targetRef=\"TextAnnotation_0m1es7k\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1rb28yp\" id=\"ServiceTask_1rb28yp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14fo81e\" id=\"SequenceFlow_14fo81e_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"243.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gvb0ht\" id=\"EndEvent_0gvb0ht_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"491\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"509\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1h43fgg\" id=\"SequenceFlow_1h43fgg_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"491\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"440\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0m1es7k\" id=\"TextAnnotation_0m1es7k_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"439\" x=\"130\" y=\"46\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dx6uag\" id=\"Association_0dx6uag_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Post a message from the Note to your Slack channel. Send specifics about the Incident or Task Note with an optional custom text message.",
      "export_key": "create_slack_reply",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658953837419,
      "name": "Example: Post Note to Slack",
      "object_type": "note",
      "programmatic_name": "create_slack_reply",
      "tags": [
        {
          "tag_handle": "fn_slack",
          "value": null
        }
      ],
      "uuid": "d9edaa38-20df-4c0e-a017-9fe721368025",
      "workflow_id": 38
    }
  ],
  "workspaces": []
}
