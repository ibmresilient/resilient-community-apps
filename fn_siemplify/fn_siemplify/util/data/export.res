{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
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
          "value": "Closed from Siemplify"
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Auto Close Case",
      "id": 105,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Auto Close Case",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "377ad15d-eea1-4265-a9d9-51c50a8bd20c",
      "view_items": [],
      "workflows": [
        "siemplify_close_case"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
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
      "export_key": "Siemplify Auto Sync Artifact",
      "id": 106,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Auto Sync Artifact",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "993bdf12-3f6f-4802-b7f0-e7305ace1d7e",
      "view_items": [],
      "workflows": [
        "siemplify_sync_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
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
      "export_key": "Siemplify Auto Sync Attachment",
      "id": 107,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Auto Sync Attachment",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "0eefbf5e-ad27-4c9f-9991-0895bced9143",
      "view_items": [],
      "workflows": [
        "siemplify_sync_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Auto Sync Case",
      "id": 108,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Auto Sync Case",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "a85325b8-39cf-41e2-980a-dea32e63046a",
      "view_items": [],
      "workflows": [
        "siemplify_sync_case"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "Siemplify Sync"
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
      "export_key": "Siemplify Auto Sync Comment",
      "id": 109,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Auto Sync Comment",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "74b8a60c-e938-4ec4-b3ab-86ca9e5ff135",
      "view_items": [],
      "workflows": [
        "siemplify_sync_comment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Sync Artifact",
      "id": 110,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Sync Artifact",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7597068a-ee80-4836-9c81-54ee00076106",
      "view_items": [],
      "workflows": [
        "siemplify_sync_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Siemplify Sync Case",
      "id": 111,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Sync Case",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9f32ca75-27bd-406a-bd94-ace0d0627eaa",
      "view_items": [],
      "workflows": [
        "siemplify_m_sync_case"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Sync Comment",
      "id": 112,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Sync Comment",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9afc8612-3b98-4ee5-8d9e-08fddbc8ac9d",
      "view_items": [],
      "workflows": [
        "siemplify_sync_comment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.siemplify_case_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Sync Task",
      "id": 113,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Sync Task",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "98be7df3-a3fc-48e1-a0ae-fb5f89e55075",
      "view_items": [],
      "workflows": [
        "siemplify_sync_task"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1640624994293,
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
      "export_key": "__function/siemplify_assigned_user",
      "hide_notification": false,
      "id": 835,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_assigned_user",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_assigned_user",
      "tooltip": "Set Assigned User. Default is none. ",
      "type_id": 11,
      "uuid": "952eacab-d865-44a9-be9d-850cf2594a97",
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
      "export_key": "__function/siemplify_sync_comments",
      "hide_notification": false,
      "id": 836,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_comments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_sync_comments",
      "tooltip": "Set to Yes to sync comments to Siemplify",
      "type_id": 11,
      "uuid": "ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97",
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
      "export_key": "__function/siemplify_attachment_id",
      "hide_notification": false,
      "id": 837,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "dd4c3c21-bf50-4b65-9129-bac0ae37fe1c",
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
      "export_key": "__function/siemplify_sync_artifacts",
      "hide_notification": false,
      "id": 838,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_artifacts",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_sync_artifacts",
      "tooltip": "Set to Yes to sync artifacts to Siemplify",
      "type_id": 11,
      "uuid": "dd93eb58-531b-4807-8ea8-4471b70e204d",
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
      "export_key": "__function/siemplify_reason",
      "hide_notification": false,
      "id": 839,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_reason",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_reason",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e264fa36-6dfc-4dd9-a864-36e66fdd1ef9",
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
      "export_key": "__function/siemplify_environment",
      "hide_notification": false,
      "id": 840,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_environment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Default Environment",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_environment",
      "tooltip": "Set environment. See app.config setting for default",
      "type_id": 11,
      "uuid": "fb54fdf6-0536-42fb-80ea-d44a09e6a4a7",
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
      "export_key": "__function/siemplify_case_id",
      "hide_notification": false,
      "id": 841,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_case_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_case_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "06db2b8f-8af3-4364-98d7-c4b534e00784",
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
      "export_key": "__function/siemplify_artifact_type",
      "hide_notification": false,
      "id": 842,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0c53b615-8d82-447a-8964-2efe578a7d1e",
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
      "export_key": "__function/siemplify_soar_task_id",
      "hide_notification": false,
      "id": 843,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_soar_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_soar_task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "18a603a9-22ef-4ec9-9017-f0fe33abf49a",
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
      "export_key": "__function/siemplify_artifact_id",
      "hide_notification": false,
      "id": 844,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "1aaa5ae3-5882-4e25-a39b-3b0765207789",
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
      "export_key": "__function/siemplify_comment",
      "hide_notification": false,
      "id": 845,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_comment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "32c42bdb-65dd-46ce-8c21-ef0104e99377",
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
      "export_key": "__function/siemplify_alert_id",
      "hide_notification": false,
      "id": 846,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_alert_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "465a56ac-2586-4013-b674-4164e03385ed",
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
      "export_key": "__function/siemplify_artifact_value",
      "hide_notification": false,
      "id": 847,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6a49bc98-0c31-4a5e-8e14-a9a46c6c893f",
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
      "export_key": "__function/siemplify_root_cause",
      "hide_notification": false,
      "id": 848,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_root_cause",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_root_cause",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6de1a4f0-26d9-412e-ad8f-1f5c98f5d154",
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
      "export_key": "__function/siemplify_incident_id",
      "hide_notification": false,
      "id": 849,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "75be91fc-7719-4339-a332-d87a55a14e3d",
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
      "export_key": "__function/siemplify_sync_attachments",
      "hide_notification": false,
      "id": 850,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_attachments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_sync_attachments",
      "tooltip": "Set to Yes to sync attachments to Siemplify",
      "type_id": 11,
      "uuid": "7b6dde8b-b1f0-476c-a442-f8e7cd706a34",
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
      "export_key": "__function/siemplify_task_assignee",
      "hide_notification": false,
      "id": 851,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_task_assignee",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "siemplify_task_assignee",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7fd18451-a0b0-4187-baa5-fd02d0951861",
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
      "export_key": "incident/siemplify_case_id",
      "hide_notification": false,
      "id": 832,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_case_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "Siemplify Case Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "806ddc17-0e5e-4cda-a1a8-79ad3188ac75",
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
      "export_key": "incident/siemplify_case_link",
      "hide_notification": false,
      "id": 833,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_case_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "Siemplify Case Link",
      "tooltip": "URL link back to Case",
      "type_id": 0,
      "uuid": "aac39e8a-21fc-44ec-a36e-7a9690fc1456",
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
      "export_key": "incident/siemplify_alert_id",
      "hide_notification": false,
      "id": 834,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "templates": [],
      "text": "Siemplify Alert Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "bf3de7b7-1643-4d6e-828c-375a951a24a5",
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
      "created_date": 1639601983863,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Close a Siemplify Case",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Close Case",
      "export_key": "siemplify_close_case",
      "id": 180,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601983916,
      "name": "siemplify_close_case",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "bca6302b-7f12-4b86-a931-d1e8b3d58e84",
      "version": 1,
      "view_items": [
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "465a56ac-2586-4013-b674-4164e03385ed",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "32c42bdb-65dd-46ce-8c21-ef0104e99377",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e264fa36-6dfc-4dd9-a864-36e66fdd1ef9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6de1a4f0-26d9-412e-ad8f-1f5c98f5d154",
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
          "name": "Siemplify Close Case",
          "object_type": "incident",
          "programmatic_name": "siemplify_close_case",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        }
      ]
    },
    {
      "created_date": 1639601983937,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Sync a SOAR Incident artifact to a Siemplify CASE alert and entity",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Sync Artifact",
      "export_key": "siemplify_sync_artifact",
      "id": 181,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601983977,
      "name": "siemplify_sync_artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "f5320892-50c9-4aae-8d08-45bc25b6e682",
      "version": 1,
      "view_items": [
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "465a56ac-2586-4013-b674-4164e03385ed",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c53b615-8d82-447a-8964-2efe578a7d1e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6a49bc98-0c31-4a5e-8e14-a9a46c6c893f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1aaa5ae3-5882-4e25-a39b-3b0765207789",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb54fdf6-0536-42fb-80ea-d44a09e6a4a7",
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
          "name": "Siemplify Sync Artifact",
          "object_type": "artifact",
          "programmatic_name": "siemplify_sync_artifact",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 93
        }
      ]
    },
    {
      "created_date": 1639601983995,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create a Siemplify Attachment from a SOAR Case Attachment",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Sync Attachment",
      "export_key": "siemplify_sync_attachment",
      "id": 182,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601984036,
      "name": "siemplify_sync_attachment",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "d3036407-650f-4e31-8528-4f6b0847560b",
      "version": 1,
      "view_items": [
        {
          "content": "75be91fc-7719-4339-a332-d87a55a14e3d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "465a56ac-2586-4013-b674-4164e03385ed",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dd4c3c21-bf50-4b65-9129-bac0ae37fe1c",
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
          "name": "Siemplify Sync Attachment",
          "object_type": "attachment",
          "programmatic_name": "siemplify_sync_attachment",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 98
        }
      ]
    },
    {
      "created_date": 1639601984054,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Sync a SOAR Case to Siemplify",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Sync Case",
      "export_key": "siemplify_sync_case",
      "id": 183,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601984096,
      "name": "siemplify_sync_case",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "bf1b6ee8-4853-4a6a-8c21-808446de4c80",
      "version": 1,
      "view_items": [
        {
          "content": "75be91fc-7719-4339-a332-d87a55a14e3d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "952eacab-d865-44a9-be9d-850cf2594a97",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb54fdf6-0536-42fb-80ea-d44a09e6a4a7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dd93eb58-531b-4807-8ea8-4471b70e204d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7b6dde8b-b1f0-476c-a442-f8e7cd706a34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "465a56ac-2586-4013-b674-4164e03385ed",
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
          "name": "Siemplify Auto Sync Case",
          "object_type": "incident",
          "programmatic_name": "siemplify_sync_case",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        },
        {
          "actions": [],
          "description": null,
          "name": "Siemplify Sync Case",
          "object_type": "incident",
          "programmatic_name": "siemplify_m_sync_case",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    },
    {
      "created_date": 1639601984114,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create a Siemplify Case comment",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Sync Comment",
      "export_key": "siemplify_sync_comment",
      "id": 184,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601984157,
      "name": "siemplify_sync_comment",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "d4c2ae89-f290-4135-aef9-79108685e92e",
      "version": 1,
      "view_items": [
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "465a56ac-2586-4013-b674-4164e03385ed",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "32c42bdb-65dd-46ce-8c21-ef0104e99377",
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
          "name": "Siemplify Sync Comment",
          "object_type": "note",
          "programmatic_name": "siemplify_sync_comment",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        }
      ]
    },
    {
      "created_date": 1639601984173,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Sync a SOAR Task to Siemplify",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Sync Task",
      "export_key": "siemplify_sync_task",
      "id": 185,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1639601984214,
      "name": "siemplify_sync_task",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "d8b35373-e80d-42cc-9120-e0073847252a",
      "version": 1,
      "view_items": [
        {
          "content": "06db2b8f-8af3-4364-98d7-c4b534e00784",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "18a603a9-22ef-4ec9-9017-f0fe33abf49a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7fd18451-a0b0-4187-baa5-fd02d0951861",
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
          "name": "Siemplify Sync Task",
          "object_type": "task",
          "programmatic_name": "siemplify_sync_task",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 97
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 6,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1640624993786,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1640624993786,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "011604d3-230a-42ba-9ce1-a541a1cff42a"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_siemplify",
      "name": "fn_siemplify",
      "programmatic_name": "fn_siemplify",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "a4fe1c3e-9dff-436c-ba62-1ab465008259"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 81,
    "major": 40,
    "minor": 2,
    "version": "40.2.81"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "siemplify_m_sync_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_m_sync_case\" isExecutable=\"true\" name=\"Siemplify Sync Case\"\u003e\u003cdocumentation\u003eSynchronize an incident, artifacts, comments and attachments with a Siemplify Case. An existing case is updated if the custom field Siemplify_case_id is not set.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0aytvve\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0w67d7h\" name=\"Siemplify Sync Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bf1b6ee8-4853-4a6a-8c21-808446de4c80\"\u003e{\"inputs\":{\"ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"dd93eb58-531b-4807-8ea8-4471b70e204d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"7b6dde8b-b1f0-476c-a442-f8e7cd706a34\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results.success:\\n  incident.properties.siemplify_case_id = results.content.get(\u0027id\u0027)\\n  incident.properties.siemplify_case_link = helper.createRichText(\\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results.content.get(\u0027siemplify_case_url\u0027), results.content.get(\u0027title\u0027)))\\n  if results.content.get(\u0027alerts\u0027):\\n    incident.properties.siemplify_alert_id = results.content[\u0027alerts\u0027][0][\u0027identifier\u0027]\\n  incident.addNote(\\\"Siemplify Sync Case {} created\\\".format(results.content.get(\u0027id\u0027)))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Case failed: {}\\\".format(str(results.content)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_incident_id = incident.id\\ninputs.siemplify_assigned_user = \\\"@Administrator\\\"\\ninputs.siemplify_environment = \\\"Default Environment\\\"\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0aytvve\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hhztx1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0aytvve\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0w67d7h\"/\u003e\u003cendEvent id=\"EndEvent_0p32n4t\"\u003e\u003cincoming\u003eSequenceFlow_1hhztx1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hhztx1\" sourceRef=\"ServiceTask_0w67d7h\" targetRef=\"EndEvent_0p32n4t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1dq6ysr\"\u003e\u003ctext\u003e\u003c![CDATA[Sync results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1afda0h\" sourceRef=\"ServiceTask_0w67d7h\" targetRef=\"TextAnnotation_1dq6ysr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0w67d7h\" id=\"ServiceTask_0w67d7h_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0aytvve\" id=\"SequenceFlow_0aytvve_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0p32n4t\" id=\"EndEvent_0p32n4t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"423\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"441\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hhztx1\" id=\"SequenceFlow_1hhztx1_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"388.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1dq6ysr\" id=\"TextAnnotation_1dq6ysr_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"161\" x=\"343\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1afda0h\" id=\"Association_1afda0h_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Synchronize an incident, artifacts, comments and attachments with a Siemplify Case. An existing case is updated if the custom field Siemplify_case_id is not set.",
      "export_key": "siemplify_m_sync_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640624082861,
      "name": "Siemplify Sync Case",
      "object_type": "incident",
      "programmatic_name": "siemplify_m_sync_case",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "4f78e937-238b-4e31-86f5-095e3dc02efe",
      "workflow_id": 96
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "siemplify_sync_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_task\" isExecutable=\"true\" name=\"Siemplify Sync Task\"\u003e\u003cdocumentation\u003eSync a SOAR incident task to Siemplify\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1igd3a2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0o6ht79\" name=\"Siemplify Sync Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d8b35373-e80d-42cc-9120-e0073847252a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  task.addNote(\\\"Siemplify Sync Task: {}\\\".format(task.name))\\nelse:\\n  task.addNote(\\\"Siemplify Sync Task: {} failed: {}\\\".format(task.name, results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_soar_task_id = task.id\\ninputs.siemplify_task_assignee = \\\"@Administrator\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1igd3a2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1s0qzhm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1igd3a2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0o6ht79\"/\u003e\u003cendEvent id=\"EndEvent_0is86cj\"\u003e\u003cincoming\u003eSequenceFlow_1s0qzhm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1s0qzhm\" sourceRef=\"ServiceTask_0o6ht79\" targetRef=\"EndEvent_0is86cj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ynurxt\"\u003e\u003ctext\u003e\u003c![CDATA[Sync results returned in a task note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1tfbar0\" sourceRef=\"ServiceTask_0o6ht79\" targetRef=\"TextAnnotation_1ynurxt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0o6ht79\" id=\"ServiceTask_0o6ht79_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"263\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1igd3a2\" id=\"SequenceFlow_1igd3a2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"263\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"230.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0is86cj\" id=\"EndEvent_0is86cj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"431\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"449\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1s0qzhm\" id=\"SequenceFlow_1s0qzhm_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"397\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ynurxt\" id=\"TextAnnotation_1ynurxt_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"162\" x=\"342\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1tfbar0\" id=\"Association_1tfbar0_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR incident task to Siemplify",
      "export_key": "siemplify_sync_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640624787532,
      "name": "Siemplify Sync Task",
      "object_type": "task",
      "programmatic_name": "siemplify_sync_task",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "bc450264-e7eb-48e7-8bd3-2039ee9287df",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "siemplify_sync_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_artifact\" isExecutable=\"true\" name=\"Siemplify Sync Artifact\"\u003e\u003cdocumentation\u003eSync a SOAR Incident artifact to a Siemplify Case alert and entity\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lp0b0i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0bvtpg3\" name=\"Siemplify Sync Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f5320892-50c9-4aae-8d08-45bc25b6e682\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(\\\"Siemplify Sync Artifact: {} ({}) created\\\".format(artifact.value, artifact.type))\\nelse:\\n  incident.addNote(\\\"Simeplify Sync Artifact: {} ({}) failed\\\".format(artifact.value, artifact.type))\\n  \",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_artifact_type = artifact.type\\ninputs.siemplify_artifact_value = artifact.value\\ninputs.siemplify_environment = None\\ninputs.siemplify_artifact_id = artifact.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lp0b0i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1n8bleh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lp0b0i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0bvtpg3\"/\u003e\u003cendEvent id=\"EndEvent_1wew0w9\"\u003e\u003cincoming\u003eSequenceFlow_1n8bleh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1n8bleh\" sourceRef=\"ServiceTask_0bvtpg3\" targetRef=\"EndEvent_1wew0w9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ypf2yo\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_133e51o\" sourceRef=\"ServiceTask_0bvtpg3\" targetRef=\"TextAnnotation_1ypf2yo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0bvtpg3\" id=\"ServiceTask_0bvtpg3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"286\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lp0b0i\" id=\"SequenceFlow_1lp0b0i_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"242\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wew0w9\" id=\"EndEvent_1wew0w9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"486\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1n8bleh\" id=\"SequenceFlow_1n8bleh_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ypf2yo\" id=\"TextAnnotation_1ypf2yo_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"371\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_133e51o\" id=\"Association_133e51o_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR Incident artifact to a Siemplify Case alert and entity",
      "export_key": "siemplify_sync_artifact",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640623885555,
      "name": "Siemplify Sync Artifact",
      "object_type": "artifact",
      "programmatic_name": "siemplify_sync_artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "4f23c3cb-c55d-4d3a-bf9f-f1f0c7b55afe",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "siemplify_sync_comment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_comment\" isExecutable=\"true\" name=\"Siemplify Sync Comment\"\u003e\u003cdocumentation\u003eSync an IBM SOAR Comment with Siemplify\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dw9j37\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tfr8rw\" name=\"Siemplify Sync Comment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d4c2ae89-f290-4135-aef9-79108685e92e\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note.text = \\\"\u0026lt;b\u0026gt;Siemplify Sync complete\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\"+note.text.content\\nelse:\\n  incident.addNote(helper.createRichText(\\\"Siemplify Sync for note failed. Reason: {}\\\".format(results.reason)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_comment = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dw9j37\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qtoy8t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dw9j37\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tfr8rw\"/\u003e\u003cendEvent id=\"EndEvent_1iowpy1\"\u003e\u003cincoming\u003eSequenceFlow_1qtoy8t\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1qtoy8t\" sourceRef=\"ServiceTask_1tfr8rw\" targetRef=\"EndEvent_1iowpy1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0cyhbqr\"\u003e\u003ctext\u003e\u003c![CDATA[Note updated to reflect sync\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1yhse3a\" sourceRef=\"ServiceTask_1tfr8rw\" targetRef=\"TextAnnotation_0cyhbqr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tfr8rw\" id=\"ServiceTask_1tfr8rw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dw9j37\" id=\"SequenceFlow_1dw9j37_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1iowpy1\" id=\"EndEvent_1iowpy1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"399\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"417\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qtoy8t\" id=\"SequenceFlow_1qtoy8t_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"373\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0cyhbqr\" id=\"TextAnnotation_0cyhbqr_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"352\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1yhse3a\" id=\"Association_1yhse3a_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"112\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Sync an IBM SOAR Comment with Siemplify",
      "export_key": "siemplify_sync_comment",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640624565461,
      "name": "Siemplify Sync Comment",
      "object_type": "note",
      "programmatic_name": "siemplify_sync_comment",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "7a04573e-eb89-4cae-b250-411e25ca083f",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "siemplify_close_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_close_case\" isExecutable=\"true\" name=\"Siemplify Close Case\"\u003e\u003cdocumentation\u003eSync SOAR incident close with Siemplify Case\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bwyqvy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ev7ddc\" name=\"Siemplify Close Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bca6302b-7f12-4b86-a931-d1e8b3d58e84\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note = \\\"Siemplify Sync cased {} closed\\\".format(incident.properties.siemplify_case_id)\\nelse:\\n  note = \\\"Siemplify Sync cased {} failed to close: {}\\\".format(incident.properties.siemplify_case_id, results.reason)\\nincident.addNote(helper.createPlainText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# change as necessary. Value Siemplify values are:  Malicious, Non Malicious, Maintenance, Inconclusive\\nLOOKUP_STATUS = {\\n    \\\"7\\\": \\\"Inconclusive\\\", # Unresolved\\n    \\\"8\\\": \\\"Inconclusive\\\", # Duplicate\\n    \\\"9\\\": \\\"Non Malicious\\\", # Not an Issue\\n    \\\"10\\\": \\\"Malicious\\\" # Resolved\\n}\\n\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_root_cause = incident.resolution_summary.content\\ninputs.siemplify_reason = LOOKUP_STATUS.get(str(incident.resolution_id), \u0027Inconclusive\u0027)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bwyqvy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_034lepw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bwyqvy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ev7ddc\"/\u003e\u003cendEvent id=\"EndEvent_0k9rsis\"\u003e\u003cincoming\u003eSequenceFlow_034lepw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_034lepw\" sourceRef=\"ServiceTask_1ev7ddc\" targetRef=\"EndEvent_0k9rsis\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07y1lm0\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14io1nw\" sourceRef=\"ServiceTask_1ev7ddc\" targetRef=\"TextAnnotation_07y1lm0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ev7ddc\" id=\"ServiceTask_1ev7ddc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"303\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bwyqvy\" id=\"SequenceFlow_1bwyqvy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"303\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"250.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0k9rsis\" id=\"EndEvent_0k9rsis_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"486\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"504\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_034lepw\" id=\"SequenceFlow_034lepw_di\"\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"444.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07y1lm0\" id=\"TextAnnotation_07y1lm0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"389\" y=\"87\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14io1nw\" id=\"Association_14io1nw_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Sync SOAR incident close with Siemplify Case",
      "export_key": "siemplify_close_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640623873449,
      "name": "Siemplify Close Case",
      "object_type": "incident",
      "programmatic_name": "siemplify_close_case",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "d1cf9a32-cc5b-4b58-a22a-88f0505aa6cd",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "siemplify_sync_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_case\" isExecutable=\"true\" name=\"Siemplify Auto Sync Case\"\u003e\u003cdocumentation\u003eSync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_133ewo1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ao7iqd\" name=\"Siemplify Sync Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bf1b6ee8-4853-4a6a-8c21-808446de4c80\"\u003e{\"inputs\":{\"ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"dd93eb58-531b-4807-8ea8-4471b70e204d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"7b6dde8b-b1f0-476c-a442-f8e7cd706a34\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results.success:\\n  incident.properties.siemplify_case_id = results.content.get(\u0027id\u0027)\\n  incident.properties.siemplify_case_link = helper.createRichText(\\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results.content.get(\u0027siemplify_case_url\u0027), results.content.get(\u0027title\u0027)))\\n  if results.content.get(\u0027alerts\u0027):\\n    incident.properties.siemplify_alert_id = results.content[\u0027alerts\u0027][0][\u0027identifier\u0027]\\n  incident.addNote(\\\"Siemplify Sync Case {} created\\\".format(results.content.get(\u0027id\u0027)))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Case failed: {}\\\".format(str(results.content)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_incident_id = incident.id\\ninputs.siemplify_assigned_user = None\\ninputs.siemplify_environment = None\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_133ewo1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14vcfso\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_133ewo1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ao7iqd\"/\u003e\u003cendEvent id=\"EndEvent_04a6awv\"\u003e\u003cincoming\u003eSequenceFlow_14vcfso\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14vcfso\" sourceRef=\"ServiceTask_0ao7iqd\" targetRef=\"EndEvent_04a6awv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02eb4gg\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0a4pfoi\" sourceRef=\"ServiceTask_0ao7iqd\" targetRef=\"TextAnnotation_02eb4gg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ao7iqd\" id=\"ServiceTask_0ao7iqd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_133ewo1\" id=\"SequenceFlow_133ewo1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04a6awv\" id=\"EndEvent_04a6awv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"452\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"425\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14vcfso\" id=\"SequenceFlow_14vcfso_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"368\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02eb4gg\" id=\"TextAnnotation_02eb4gg_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"202\" x=\"362\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0a4pfoi\" id=\"Association_0a4pfoi_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"446\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments",
      "export_key": "siemplify_sync_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640623855405,
      "name": "Siemplify Auto Sync Case",
      "object_type": "incident",
      "programmatic_name": "siemplify_sync_case",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "43ab935d-a6dd-4c48-b44f-00b059891799",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "siemplify_sync_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_attachment\" isExecutable=\"true\" name=\"Siemplify Sync Attachment\"\u003e\u003cdocumentation\u003eSync a SOAR case attachment to a Siemplify case attachment\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_04748ia\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cggez0\" name=\"Siemplify Sync Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3036407-650f-4e31-8528-4f6b0847560b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(\\\"Siemplify Sync Attachment: {} created\\\".format(attachment.name))\\nelse:\\n  incident.addNote(\\\"Simeplify Sync Attachment: {} failed. Reason: {}\\\".format(attachment.name, results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_incident_id = incident.id\\ninputs.siemplify_attachment_id = attachment.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_04748ia\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1adbvuz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_04748ia\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cggez0\"/\u003e\u003cendEvent id=\"EndEvent_08r0xmm\"\u003e\u003cincoming\u003eSequenceFlow_1adbvuz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1adbvuz\" sourceRef=\"ServiceTask_0cggez0\" targetRef=\"EndEvent_08r0xmm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1wa60c0\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_136xpb6\" sourceRef=\"ServiceTask_0cggez0\" targetRef=\"TextAnnotation_1wa60c0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cggez0\" id=\"ServiceTask_0cggez0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04748ia\" id=\"SequenceFlow_04748ia_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08r0xmm\" id=\"EndEvent_08r0xmm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"441\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1adbvuz\" id=\"SequenceFlow_1adbvuz_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"404.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1wa60c0\" id=\"TextAnnotation_1wa60c0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"358\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_136xpb6\" id=\"Association_136xpb6_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR case attachment to a Siemplify case attachment",
      "export_key": "siemplify_sync_attachment",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1640624031750,
      "name": "Siemplify Sync Attachment",
      "object_type": "attachment",
      "programmatic_name": "siemplify_sync_attachment",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "9bc3cee3-3540-400c-8f39-90d19d448032",
      "workflow_id": 98
    }
  ],
  "workspaces": []
}
