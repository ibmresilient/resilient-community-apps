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
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Add Playbook",
      "id": 185,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Add Playbook",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c59ba2eb-f27a-4b9a-9eb2-1a552facf502",
      "view_items": [
        {
          "content": "23f7bf6d-288e-4f1c-bca6-7c642078fcfe",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a34f8b24-7b34-4d02-b504-a81945e65a14",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "siemplify_add_playbook"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Siemplify: Add/Update Entity to Blocklist",
      "id": 120,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify: Add/Update Entity to Blocklist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ba6473af-7bb2-4b80-9d24-a0fb25a7410b",
      "view_items": [
        {
          "content": "73a403f8-ec0f-4179-981e-6f67c278d7fc",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "siemplify_addupdate_entity_to_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Siemplify: Add/Update Entity to Custom List",
      "id": 121,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify: Add/Update Entity to Custom List",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f3d92f0b-1a32-456f-bb68-f98c60149803",
      "view_items": [
        {
          "content": "0168d870-f533-4ef8-bd3c-892d2d291233",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "73a403f8-ec0f-4179-981e-6f67c278d7fc",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "siemplify_addupdate_entity_to_customlist"
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
      "id": 111,
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
      "id": 112,
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
      "id": 113,
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
      "id": 114,
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
          "value": "Siemplify"
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
      "id": 115,
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
      "conditions": [],
      "enabled": true,
      "export_key": "Siemplify: Get Blocklist Entities",
      "id": 122,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify: Get Blocklist Entities",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8707261f-6a0c-4793-8cc1-1843c4ad2049",
      "view_items": [
        {
          "content": "80eddc12-5b73-4af1-9dd0-b782c088bfc9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24d9cb0a-af51-450e-abf7-bc532e8ba299",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "siemplify_get_blocklist_entities"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Siemplify: Get Custom List Entities",
      "id": 123,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify: Get Custom List Entities",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e45102f1-39bc-4703-ad58-02526e9bbd1f",
      "view_items": [
        {
          "content": "73a403f8-ec0f-4179-981e-6f67c278d7fc",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24d9cb0a-af51-450e-abf7-bc532e8ba299",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "siemplify_get_customlist_entities"
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
      "id": 116,
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
      "id": 117,
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
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "From Siemplify"
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Sync Comment",
      "id": 118,
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
      "id": 119,
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
  "export_date": 1648762335257,
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
      "id": 1093,
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
      "id": 1094,
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
      "export_key": "__function/siemplify_category",
      "hide_notification": false,
      "id": 1095,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_category",
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
      "text": "siemplify_category",
      "tooltip": "If left empty, the artifact type is used",
      "type_id": 11,
      "uuid": "c166fab3-4c59-4359-ad85-4e7743ad2478",
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
      "export_key": "__function/siemplify_playbook_name",
      "hide_notification": false,
      "id": 1300,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_playbook_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_playbook_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c3e9448d-c211-45ed-b971-9da673b2bb0a",
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
      "id": 1096,
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
      "id": 1097,
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
      "id": 1098,
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
      "id": 1099,
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
      "id": 1100,
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
      "id": 1101,
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
      "export_key": "__function/siemplify_limit",
      "hide_notification": false,
      "id": 1102,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_limit",
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
      "text": "siemplify_limit",
      "tooltip": "Limit the results returned",
      "type_id": 11,
      "uuid": "15ba4bcb-0ec2-42c9-b62d-2fb58e52ef42",
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
      "id": 1103,
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
      "id": 1104,
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
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/siemplify_run_playbook_automatically",
      "hide_notification": false,
      "id": 1301,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_run_playbook_automatically",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_run_playbook_automatically",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2e0837b3-eaf4-4aa8-8e9a-2109171092ce",
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
      "id": 1105,
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
      "id": 1106,
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
      "export_key": "__function/siemplify_environments",
      "hide_notification": false,
      "id": 1113,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_environments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "environment1,environment2",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_environments",
      "tooltip": "Comma separated list of environments to filter results",
      "type_id": 11,
      "uuid": "4dc7c76c-277c-41d6-b4eb-a9d8bfeb7e60",
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
      "id": 1107,
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
      "id": 1108,
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
      "export_key": "__function/siemplify_search",
      "hide_notification": false,
      "id": 1109,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_search",
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
      "text": "siemplify_search",
      "tooltip": "Filter results based on a search entry",
      "type_id": 11,
      "uuid": "6f10f317-77be-4cf6-9b07-b53c1586c4b7",
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
      "id": 1110,
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
      "id": 1111,
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
      "id": 1112,
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
      "export_key": "actioninvocation/siemplify_search_term",
      "hide_notification": false,
      "id": 1089,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_search_term",
      "operation_perms": {},
      "operations": [],
      "placeholder": "1.2.3.4",
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
      "text": "Search Term",
      "tooltip": "Artifact value to search or none for entire list",
      "type_id": 6,
      "uuid": "80eddc12-5b73-4af1-9dd0-b782c088bfc9",
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
      "export_key": "actioninvocation/siemplify_run_playbook_automatically",
      "hide_notification": false,
      "id": 1303,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_run_playbook_automatically",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Run Playbook Automatically",
      "tooltip": "",
      "type_id": 6,
      "uuid": "a34f8b24-7b34-4d02-b504-a81945e65a14",
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
      "export_key": "actioninvocation/siemplify_list_category",
      "hide_notification": false,
      "id": 1090,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_list_category",
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
      "text": "List Category",
      "tooltip": "If left empty, the artifact type is used",
      "type_id": 6,
      "uuid": "0168d870-f533-4ef8-bd3c-892d2d291233",
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
      "export_key": "actioninvocation/siemplify_playbook_name",
      "hide_notification": false,
      "id": 1302,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_playbook_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Siemplify Playbook Name",
      "tooltip": "",
      "type_id": 6,
      "uuid": "23f7bf6d-288e-4f1c-bca6-7c642078fcfe",
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
      "export_key": "actioninvocation/siemplify_limit_result",
      "hide_notification": false,
      "id": 1091,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_limit_result",
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
      "text": "Limit Result",
      "tooltip": "Number of results to limit the search",
      "type_id": 6,
      "uuid": "24d9cb0a-af51-450e-abf7-bc532e8ba299",
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
      "export_key": "actioninvocation/siemplify_environments",
      "hide_notification": false,
      "id": 1092,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_environments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "environment1,environment2",
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
      "text": "Environments",
      "tooltip": "comma separated list of Simplify environments",
      "type_id": 6,
      "uuid": "73a403f8-ec0f-4179-981e-6f67c278d7fc",
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
      "id": 1076,
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
      "id": 1077,
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
      "id": 1078,
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
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "incident/siemplify_stage",
      "hide_notification": false,
      "id": 1079,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_stage",
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
      "text": "Siemplify Stage",
      "tooltip": "",
      "type_id": 0,
      "uuid": "d95e044e-b05b-414b-8915-6a0be0325fb4",
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
      "export_key": "incident/siemplify_priority",
      "hide_notification": false,
      "id": 1080,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_priority",
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
      "text": "Siemplify Priority",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e9dcff8a-16e8-4988-a7bd-ad9d281c7f20",
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
      "export_key": "incident/siemplify_assignee",
      "hide_notification": false,
      "id": 1081,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_assignee",
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
      "text": "Siemplify Assignee",
      "tooltip": "",
      "type_id": 0,
      "uuid": "fd406227-4433-4735-b2a5-e2d5c55374e6",
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
      "export_key": "incident/siemplify_tags",
      "hide_notification": false,
      "id": 1082,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_tags",
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
      "text": "Siemplify Tags",
      "tooltip": "comma separated list of tags used with this Case",
      "type_id": 0,
      "uuid": "570c52cc-4633-497a-8ae0-48975e37b930",
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
      "export_key": "incident/siemplify_is_important",
      "hide_notification": false,
      "id": 1083,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_is_important",
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
      "text": "Siemplify Is Important",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7a5a8552-bfea-48f0-8d3f-e173753a441f",
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
      "created_date": 1648759704866,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Add a playbook to a Siemplify Case",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Add Playbook",
      "export_key": "siemplify_add_playbook",
      "id": 178,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1648759704911,
      "name": "siemplify_add_playbook",
      "tags": [],
      "uuid": "b8f05f74-95fa-4861-8264-5398d247da7b",
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
          "content": "c3e9448d-c211-45ed-b971-9da673b2bb0a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2e0837b3-eaf4-4aa8-8e9a-2109171092ce",
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
          "name": "Siemplify Add Playbook",
          "object_type": "incident",
          "programmatic_name": "siemplify_add_playbook",
          "tags": [],
          "uuid": null,
          "workflow_id": 152
        }
      ]
    },
    {
      "created_date": 1645797091353,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Add an artifact to the Siemplify Blacklist",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify: Add/Update Entity to Blocklist",
      "export_key": "siemplify_addupdate_entity_to_blocklist",
      "id": 125,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091395,
      "name": "siemplify_addupdate_entity_to_blocklist",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"entityIdentifier\": \"abc@example.com\", \"entityType\": \"USERUNIQNAME\", \"scope\": 2, \"environments\": [\"Default Environment\"]}, \"raw\": null, \"inputs\": {\"siemplify_artifact_type\": \"Email Recipient\", \"siemplify_environment\": null, \"siemplify_artifact_value\": \"abc@example.com\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 330, \"timestamp\": \"2022-01-07 14:36:05\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"entityIdentifier\": {\"type\": \"string\"}, \"entityType\": {\"type\": \"string\"}, \"scope\": {\"type\": \"integer\"}, \"environments\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_artifact_type\": {\"type\": \"string\"}, \"siemplify_environment\": {}, \"siemplify_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "bc122044-f6a1-4c39-b433-842a59eb9bcd",
      "version": 1,
      "view_items": [
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
          "name": "Siemplify: Add/Update Entity to Block List",
          "object_type": "artifact",
          "programmatic_name": "siemplify_addupdate_entity_to_blocklist",
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
      "created_date": 1645797091416,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Add an artifact to the Siemplify custom list",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Add/Update Entity to Custom List",
      "export_key": "siemplify_addupdate_entity_to_customlist",
      "id": 126,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091455,
      "name": "siemplify_addupdate_entity_to_customlist",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"entityIdentifier\": \"abc@example.com\", \"category\": \"USERUNIQNAME\", \"environments\": [\"Default Environment\"]}, \"raw\": null, \"inputs\": {\"siemplify_artifact_type\": \"Email Recipient\", \"siemplify_environment\": null, \"siemplify_category\": null, \"siemplify_artifact_value\": \"abc@example.com\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 282, \"timestamp\": \"2022-01-07 14:35:57\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"entityIdentifier\": {\"type\": \"string\"}, \"category\": {\"type\": \"string\"}, \"environments\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_artifact_type\": {\"type\": \"string\"}, \"siemplify_environment\": {}, \"siemplify_category\": {}, \"siemplify_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "dc383d80-a189-4763-977c-75452f33d917",
      "version": 1,
      "view_items": [
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
          "content": "c166fab3-4c59-4359-ad85-4e7743ad2478",
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
          "name": "Siemplify Add/Update Entity to Custom List",
          "object_type": "artifact",
          "programmatic_name": "siemplify_addupdate_entity_to_customlist",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        }
      ]
    },
    {
      "created_date": 1645797091472,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 127,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091511,
      "name": "siemplify_close_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"close_case\": true}, \"raw\": null, \"inputs\": {\"siemplify_root_cause\": \"\u003cdiv class=\\\"rte\\\"\u003e\u003cdiv\u003emsg for siemplify\u003c/div\u003e\u003c/div\u003e\", \"siemplify_alert_id\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\", \"siemplify_reason\": \"Inconclusive\", \"siemplify_case_id\": 66}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 626, \"timestamp\": \"2022-01-07 14:36:29\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"close_case\": {\"type\": \"boolean\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_root_cause\": {\"type\": \"string\"}, \"siemplify_alert_id\": {\"type\": \"string\"}, \"siemplify_reason\": {\"type\": \"string\"}, \"siemplify_case_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 87
        }
      ]
    },
    {
      "created_date": 1645797091529,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get entities from Siemplify\u0027s Blacklist",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify: Get Blocklist Entities",
      "export_key": "siemplify_get_blocklist_entities",
      "id": 128,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091567,
      "name": "siemplify_get_blocklist_entities",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"id\": 1, \"entityIdentifier\": \"https://abc.com\", \"entityType\": \"DestinationURL\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}, {\"id\": 2, \"entityIdentifier\": \"1.2.3.4\", \"entityType\": \"IPSET\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}, {\"id\": 3, \"entityIdentifier\": \"5.6.7.8\", \"entityType\": \"IPSET\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}, {\"id\": 4, \"entityIdentifier\": \"a@example.com\", \"entityType\": \"USERUNIQNAME\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}, {\"id\": 5, \"entityIdentifier\": \"aaa.exe\", \"entityType\": \"PROCESS\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}, {\"id\": 6, \"entityIdentifier\": \"malicious.exe\", \"entityType\": \"FILENAME\", \"elementType\": 0, \"scope\": 2, \"environments\": [\"Default Environment\"]}], \"raw\": null, \"inputs\": {\"siemplify_search\": null, \"siemplify_limit\": 100}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 253, \"timestamp\": \"2022-01-07 14:35:14\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"entityIdentifier\": {\"type\": \"string\"}, \"entityType\": {\"type\": \"string\"}, \"elementType\": {\"type\": \"integer\"}, \"scope\": {\"type\": \"integer\"}, \"environments\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_search\": {}, \"siemplify_limit\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "2bf54da4-8de2-4b4b-8baf-d7e74d0c2d58",
      "version": 1,
      "view_items": [
        {
          "content": "6f10f317-77be-4cf6-9b07-b53c1586c4b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "15ba4bcb-0ec2-42c9-b62d-2fb58e52ef42",
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
          "name": "Siemplify Get Block List Entities",
          "object_type": "incident",
          "programmatic_name": "siemplify_get_blocklist_entities",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    },
    {
      "created_date": 1645797091583,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get entities from Siemplify\u0027s custom list",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify Get Custom List Entities",
      "export_key": "siemplify_get_customlist_entities",
      "id": 129,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645898107795,
      "name": "siemplify_get_customlist_entities",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"entityIdentifier\": \"soar_list\", \"category\": \"soar_category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 1, \"creationTimeUnixTimeInMs\": 1638827701814, \"modificationTimeUnixTimeInMs\": 1638827701814}, {\"entityIdentifier\": \"soar2_list\", \"category\": \"soar_category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 2, \"creationTimeUnixTimeInMs\": 1641490099338, \"modificationTimeUnixTimeInMs\": 1641490099338}, {\"entityIdentifier\": \"soar3_list\", \"category\": \"aa\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 3, \"creationTimeUnixTimeInMs\": 1641507308926, \"modificationTimeUnixTimeInMs\": 1641507308926}, {\"entityIdentifier\": \"123\", \"category\": \"soar_category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 4, \"creationTimeUnixTimeInMs\": 1641511563361, \"modificationTimeUnixTimeInMs\": 1641511563361}, {\"entityIdentifier\": \"def.com\", \"category\": \"new category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 5, \"creationTimeUnixTimeInMs\": 1641515897058, \"modificationTimeUnixTimeInMs\": 1641515897058}, {\"entityIdentifier\": \"service\", \"category\": \"new category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 6, \"creationTimeUnixTimeInMs\": 1641516046817, \"modificationTimeUnixTimeInMs\": 1641516046817}, {\"entityIdentifier\": \"something\", \"category\": \"new category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 7, \"creationTimeUnixTimeInMs\": 1641516166266, \"modificationTimeUnixTimeInMs\": 1641516166266}, {\"entityIdentifier\": \"malicious.exe\", \"category\": \"Malicious Category\", \"forDBMigration\": false, \"environments\": [\"Default Environment\"], \"id\": 8, \"creationTimeUnixTimeInMs\": 1641572735756, \"modificationTimeUnixTimeInMs\": 1641572735756}], \"raw\": null, \"inputs\": {\"siemplify_search\": null, \"siemplify_limit\": 100}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 574, \"timestamp\": \"2022-01-07 14:35:19\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"entityIdentifier\": {\"type\": \"string\"}, \"category\": {\"type\": \"string\"}, \"forDBMigration\": {\"type\": \"boolean\"}, \"environments\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"id\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_search\": {}, \"siemplify_limit\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "f7c15417-71ef-4ab5-adff-e3ab84768f4e",
      "version": 2,
      "view_items": [
        {
          "content": "4dc7c76c-277c-41d6-b4eb-a9d8bfeb7e60",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "15ba4bcb-0ec2-42c9-b62d-2fb58e52ef42",
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
          "name": "Siemplify Get Custom List Entities",
          "object_type": "incident",
          "programmatic_name": "siemplify_get_customlist_entities",
          "tags": [
            {
              "tag_handle": "fn_siemplify",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 89
        }
      ]
    },
    {
      "created_date": 1645797091638,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 130,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091677,
      "name": "siemplify_sync_artifact",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {}, \"raw\": null, \"inputs\": {\"siemplify_artifact_type\": \"IP Address\", \"siemplify_alert_id\": \"IBM SOAR Alert 2142_492b8ecf-1a40-4752-a498-437468c4d111\", \"siemplify_environment\": null, \"siemplify_artifact_id\": 205, \"siemplify_artifact_value\": \"192.168.1.190\", \"siemplify_case_id\": 64}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 435, \"timestamp\": \"2022-01-12 12:19:39\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_artifact_type\": {\"type\": \"string\"}, \"siemplify_alert_id\": {\"type\": \"string\"}, \"siemplify_environment\": {}, \"siemplify_artifact_id\": {\"type\": \"integer\"}, \"siemplify_artifact_value\": {\"type\": \"string\"}, \"siemplify_case_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
      "created_date": 1645797091693,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 131,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091730,
      "name": "siemplify_sync_attachment",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"evidenceName\": \"app-rc_data_feed_plugin_odbcfeed-1\", \"description\": \"created by IBM SOAR\", \"evidenceThumbnailBase64\": \"\", \"evidenceId\": 14, \"fileType\": \".0.5.zip\", \"creatorUserId\": \"Siemplify automation\", \"id\": 14, \"type\": 4, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584095781, \"creationTimeUnixTimeInMs\": 1641584095781, \"alertIdentifier\": null}, \"raw\": null, \"inputs\": {\"siemplify_incident_id\": 2149, \"siemplify_alert_id\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\", \"siemplify_case_id\": 66, \"siemplify_attachment_id\": 16}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 748, \"timestamp\": \"2022-01-07 14:34:55\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"evidenceName\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"evidenceThumbnailBase64\": {\"type\": \"string\"}, \"evidenceId\": {\"type\": \"integer\"}, \"fileType\": {\"type\": \"string\"}, \"creatorUserId\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"integer\"}, \"caseId\": {\"type\": \"integer\"}, \"isFavorite\": {\"type\": \"boolean\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"alertIdentifier\": {}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_incident_id\": {\"type\": \"integer\"}, \"siemplify_alert_id\": {\"type\": \"string\"}, \"siemplify_case_id\": {\"type\": \"integer\"}, \"siemplify_attachment_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 86
        }
      ]
    },
    {
      "created_date": 1645797091746,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 132,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091785,
      "name": "siemplify_sync_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"wallData\": [{\"comment\": \"Case creation reason: IBM SOAR Incident 2149\", \"creatorUserId\": \"Siemplify automation\", \"id\": 66, \"type\": 7, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584057814, \"creationTimeUnixTimeInMs\": 1641584057814, \"alertIdentifier\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\"}, {\"comment\": \"Playbook SentinelOne Threat Remediation attached to case.\", \"creatorUserId\": \"Siemplify automation\", \"id\": 47, \"type\": 5, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584057945, \"creationTimeUnixTimeInMs\": 1641584057945, \"alertIdentifier\": null}, {\"description\": \"Tag \u0027Manual Case\u0027 added\", \"activityKind\": 15, \"newValue\": \"Manual Case\", \"creatorUserId\": \"Siemplify automation\", \"id\": 98, \"type\": 1, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584057852, \"creationTimeUnixTimeInMs\": 1641584057852, \"alertIdentifier\": null}, {\"description\": \"Case stage set to Triage\", \"activityKind\": 10, \"newValue\": null, \"creatorUserId\": \"System\", \"id\": 67, \"type\": 1, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584057714, \"creationTimeUnixTimeInMs\": 1641584057714, \"alertIdentifier\": null}, {\"actionTriggerType\": 0, \"integration\": \"Siemplify\", \"executingUser\": null, \"playbookName\": \"SentinelOne Threat Remediation\", \"playbookIsInDebugMode\": false, \"status\": 5, \"actionProvider\": \"Scripts\", \"actionIdentifier\": \"Insight - Threat Information\", \"actionResult\": \"Action started\", \"alertIdentifiers\": [\"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\"], \"creatorUserId\": null, \"id\": 13, \"type\": 3, \"caseId\": 0, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584058246, \"creationTimeUnixTimeInMs\": 1641584058246, \"alertIdentifier\": null}], \"alerts\": [{\"ticketId\": \"\", \"identifier\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\", \"hasWorkflows\": true, \"workflowsStatus\": 1, \"sourceSystemName\": \"\", \"securityEventCards\": [{\"caseId\": 66, \"eventId\": null, \"alertIdentifier\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\", \"eventName\": null, \"product\": null, \"sources\": [], \"destinations\": [], \"artificats\": [], \"port\": null, \"outcome\": null, \"time\": \"2022-01-07T19:32:24Z\", \"deviceEventClassId\": null, \"fields\": []}], \"entityCards\": [], \"productFamilies\": [\"Default\"], \"fields\": [{\"isHighlight\": true, \"groupName\": \"HIGHLIGHTED FIELDS\", \"items\": [{\"originalName\": \"AlertName\", \"name\": \"Alert Name\", \"value\": \"IBM SOAR Alert 2149\"}, {\"originalName\": \"EndTime\", \"name\": \"End Time\", \"value\": \"1641583944000\"}, {\"originalName\": \"StartTime\", \"name\": \"Start Time\", \"value\": \"1641583944000\"}]}, {\"isHighlight\": false, \"groupName\": \"Time\", \"items\": [{\"originalName\": \"DetectionTime\", \"name\": \"Detection Time\", \"value\": \"1641583944000\"}, {\"originalName\": \"EndTime\", \"name\": \"End Time\", \"value\": \"1641583944000\"}, {\"originalName\": \"StartTime\", \"name\": \"Start Time\", \"value\": \"1641583944000\"}]}, {\"isHighlight\": false, \"groupName\": \"Case\", \"items\": [{\"originalName\": \"AlertName\", \"name\": \"Alert Name\", \"value\": \"IBM SOAR Alert 2149\"}, {\"originalName\": \"RuleGenerator\", \"name\": \"Rule Generator\", \"value\": \"Manual Case\"}]}, {\"isHighlight\": false, \"groupName\": \"Default\", \"items\": [{\"originalName\": \"AlertGroupIdentifier\", \"name\": \"AlertGroupIdentifier\", \"value\": \"Manual Case_0e65479c-d123-4cae-a017-fc38339e42ab\"}, {\"originalName\": \"IsManualAlert\", \"name\": \"IsManualAlert\", \"value\": \"True\"}]}, {\"isHighlight\": false, \"groupName\": \"Threat\", \"items\": [{\"originalName\": \"Priority\", \"name\": \"Priority\", \"value\": \"Unchanged\"}]}], \"name\": \"IBM SOAR Alert 2149\", \"product\": null, \"startTimeUnixTimeInMs\": 1641583944000, \"apiSlaExpiration\": {\"slaExpirationTime\": null, \"criticalExpirationTime\": null, \"expirationStatus\": 2}, \"isManualAlert\": true, \"priority\": 0, \"id\": 0, \"creationTimeUnixTimeInMs\": 0, \"modificationTimeUnixTimeInMs\": 0, \"additionalProperties\": {\"identifier\": \"IBM SOAR Alert 2149_42e7d42f-f307-4f50-8407-98e2eb49f4f3\", \"detectionTime\": \"1641583944000\", \"alertName\": \"IBM SOAR Alert 2149\", \"ruleGenerator\": \"Manual Case\", \"alertGroupIdentifier\": \"Manual Case_0e65479c-d123-4cae-a017-fc38339e42ab\", \"isManualAlert\": \"True\", \"priority\": \"Unchanged\", \"endTime\": \"1641583944000\", \"startTime\": \"1641583944000\"}}], \"caseRecommendations\": null, \"tags\": [{\"caseId\": 66, \"tag\": \"IBMSOAR\", \"priority\": 0}, {\"caseId\": 66, \"tag\": \"Manual Case\", \"priority\": 0}], \"insights\": [], \"productFamilies\": [], \"summary\": {\"fields\": []}, \"entityCards\": [], \"entities\": [], \"description\": null, \"canOpenIncident\": false, \"hasIncident\": false, \"title\": \"IBM SOAR - sync this with siemplify\", \"isTouched\": false, \"hasSuspiciousEntity\": false, \"isMerged\": false, \"isImportant\": true, \"isIncident\": false, \"hasWorkflow\": true, \"environment\": \"Default Environment\", \"priority\": 50, \"stage\": \"Triage\", \"assignedUserName\": \"@Administrator\", \"apiSlaExpiration\": {\"slaExpirationTime\": null, \"criticalExpirationTime\": null, \"expirationStatus\": 2}, \"apiStageSlaExpiration\": {\"slaExpirationTime\": null, \"criticalExpirationTime\": null, \"expirationStatus\": 2}, \"status\": 1, \"isTestCase\": false, \"caseSource\": \"User\", \"isOverflowCase\": false, \"id\": 66, \"creationTimeUnixTimeInMs\": 1641584057689, \"modificationTimeUnixTimeInMs\": 1641584057739, \"additionalProperties\": {}, \"siemplify_case_url\": \"https://9.55.194.8/#/main/cases/classic-view/66\"}, \"raw\": null, \"inputs\": {\"siemplify_incident_id\": 2149, \"siemplify_sync_attachments\": true, \"siemplify_assigned_user\": \"@Administrator\", \"siemplify_environment\": \"Default Environment\", \"siemplify_alert_id\": \"IBM SOAR Alert 2149_fab80a96-28cd-4110-ad7b-2d1c9128e864\", \"siemplify_sync_comments\": true, \"siemplify_sync_artifacts\": true, \"siemplify_case_id\": 65}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 1775, \"timestamp\": \"2022-01-07 14:34:18\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"wallData\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"comment\": {\"type\": \"string\"}, \"creatorUserId\": {\"type\": [\"null\", \"string\"]}, \"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"integer\"}, \"caseId\": {\"type\": \"integer\"}, \"isFavorite\": {\"type\": \"boolean\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"alertIdentifier\": {\"type\": [\"null\", \"string\"]}, \"description\": {\"type\": \"string\"}, \"activityKind\": {\"type\": \"integer\"}, \"newValue\": {\"type\": [\"null\", \"string\"]}, \"actionTriggerType\": {\"type\": \"integer\"}, \"integration\": {\"type\": \"string\"}, \"executingUser\": {}, \"playbookName\": {\"type\": \"string\"}, \"playbookIsInDebugMode\": {\"type\": \"boolean\"}, \"status\": {\"type\": \"integer\"}, \"actionProvider\": {\"type\": \"string\"}, \"actionIdentifier\": {\"type\": \"string\"}, \"actionResult\": {\"type\": \"string\"}, \"alertIdentifiers\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}, \"alerts\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"ticketId\": {\"type\": \"string\"}, \"identifier\": {\"type\": \"string\"}, \"hasWorkflows\": {\"type\": \"boolean\"}, \"workflowsStatus\": {\"type\": \"integer\"}, \"sourceSystemName\": {\"type\": \"string\"}, \"securityEventCards\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"caseId\": {\"type\": \"integer\"}, \"eventId\": {}, \"alertIdentifier\": {\"type\": \"string\"}, \"eventName\": {}, \"product\": {}, \"sources\": {\"type\": \"array\"}, \"destinations\": {\"type\": \"array\"}, \"artificats\": {\"type\": \"array\"}, \"port\": {}, \"outcome\": {}, \"time\": {\"type\": \"string\"}, \"deviceEventClassId\": {}, \"fields\": {\"type\": \"array\"}}}}, \"entityCards\": {\"type\": \"array\"}, \"productFamilies\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"fields\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"isHighlight\": {\"type\": \"boolean\"}, \"groupName\": {\"type\": \"string\"}, \"items\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"originalName\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}}}}}, \"name\": {\"type\": \"string\"}, \"product\": {}, \"startTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"apiSlaExpiration\": {\"type\": \"object\", \"properties\": {\"slaExpirationTime\": {}, \"criticalExpirationTime\": {}, \"expirationStatus\": {\"type\": \"integer\"}}}, \"isManualAlert\": {\"type\": \"boolean\"}, \"priority\": {\"type\": \"integer\"}, \"id\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"additionalProperties\": {\"type\": \"object\", \"properties\": {\"identifier\": {\"type\": \"string\"}, \"detectionTime\": {\"type\": \"string\"}, \"alertName\": {\"type\": \"string\"}, \"ruleGenerator\": {\"type\": \"string\"}, \"alertGroupIdentifier\": {\"type\": \"string\"}, \"isManualAlert\": {\"type\": \"string\"}, \"priority\": {\"type\": \"string\"}, \"endTime\": {\"type\": \"string\"}, \"startTime\": {\"type\": \"string\"}}}}}}, \"caseRecommendations\": {}, \"tags\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"caseId\": {\"type\": \"integer\"}, \"tag\": {\"type\": \"string\"}, \"priority\": {\"type\": \"integer\"}}}}, \"insights\": {\"type\": \"array\"}, \"productFamilies\": {\"type\": \"array\"}, \"summary\": {\"type\": \"object\", \"properties\": {\"fields\": {\"type\": \"array\"}}}, \"entityCards\": {\"type\": \"array\"}, \"entities\": {\"type\": \"array\"}, \"description\": {}, \"canOpenIncident\": {\"type\": \"boolean\"}, \"hasIncident\": {\"type\": \"boolean\"}, \"title\": {\"type\": \"string\"}, \"isTouched\": {\"type\": \"boolean\"}, \"hasSuspiciousEntity\": {\"type\": \"boolean\"}, \"isMerged\": {\"type\": \"boolean\"}, \"isImportant\": {\"type\": \"boolean\"}, \"isIncident\": {\"type\": \"boolean\"}, \"hasWorkflow\": {\"type\": \"boolean\"}, \"environment\": {\"type\": \"string\"}, \"priority\": {\"type\": \"integer\"}, \"stage\": {\"type\": \"string\"}, \"assignedUserName\": {\"type\": \"string\"}, \"apiSlaExpiration\": {\"type\": \"object\", \"properties\": {\"slaExpirationTime\": {}, \"criticalExpirationTime\": {}, \"expirationStatus\": {\"type\": \"integer\"}}}, \"apiStageSlaExpiration\": {\"type\": \"object\", \"properties\": {\"slaExpirationTime\": {}, \"criticalExpirationTime\": {}, \"expirationStatus\": {\"type\": \"integer\"}}}, \"status\": {\"type\": \"integer\"}, \"isTestCase\": {\"type\": \"boolean\"}, \"caseSource\": {\"type\": \"string\"}, \"isOverflowCase\": {\"type\": \"boolean\"}, \"id\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"additionalProperties\": {\"type\": \"object\"}, \"siemplify_case_url\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_incident_id\": {\"type\": \"integer\"}, \"siemplify_sync_attachments\": {\"type\": \"boolean\"}, \"siemplify_assigned_user\": {\"type\": \"string\"}, \"siemplify_environment\": {\"type\": \"string\"}, \"siemplify_alert_id\": {\"type\": \"string\"}, \"siemplify_sync_comments\": {\"type\": \"boolean\"}, \"siemplify_sync_artifacts\": {\"type\": \"boolean\"}, \"siemplify_case_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 88
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
          "workflow_id": 85
        }
      ]
    },
    {
      "created_date": 1645797091805,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 133,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091844,
      "name": "siemplify_sync_comment",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {}, \"raw\": null, \"inputs\": {\"siemplify_alert_id\": \"IBM SOAR Alert 2142_492b8ecf-1a40-4752-a498-437468c4d111\", \"siemplify_comment\": \"\u003cdiv class=\\\"rte\\\"\u003e\u003cdiv\u003esync insight 3rd\u003c/div\u003e\u003c/div\u003e\", \"siemplify_case_id\": 64}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 292, \"timestamp\": \"2022-01-12 11:43:52\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_alert_id\": {\"type\": \"string\"}, \"siemplify_comment\": {\"type\": \"string\"}, \"siemplify_case_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 84
        }
      ]
    },
    {
      "created_date": 1645797091861,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
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
      "id": 134,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1645797091902,
      "name": "siemplify_sync_task",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"status\": 0, \"priority\": 0, \"name\": \"IBM SOAR: Investigate Exposure of Personal Information/Data\", \"owner\": \"@Administrator\", \"completor\": null, \"completionComment\": null, \"completionDateTimeUnixTimeInMs\": null, \"dueDateUnixTimeInMs\": null, \"creatorUserId\": \"Siemplify automation\", \"id\": 21, \"type\": 2, \"caseId\": 66, \"isFavorite\": false, \"modificationTimeUnixTimeInMs\": 1641584072788, \"creationTimeUnixTimeInMs\": 1641584072788, \"alertIdentifier\": null}, \"raw\": null, \"inputs\": {\"siemplify_task_assignee\": \"@Administrator\", \"siemplify_soar_task_id\": 803, \"siemplify_case_id\": 66}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-siemplify\", \"package_version\": \"1.0.0\", \"host\": \"Marks-MacBook-Pro.local\", \"execution_time_ms\": 457, \"timestamp\": \"2022-01-07 14:34:32\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"status\": {\"type\": \"integer\"}, \"priority\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"owner\": {\"type\": \"string\"}, \"completor\": {}, \"completionComment\": {}, \"completionDateTimeUnixTimeInMs\": {}, \"dueDateUnixTimeInMs\": {}, \"creatorUserId\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"type\": {\"type\": \"integer\"}, \"caseId\": {\"type\": \"integer\"}, \"isFavorite\": {\"type\": \"boolean\"}, \"modificationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"creationTimeUnixTimeInMs\": {\"type\": \"integer\"}, \"alertIdentifier\": {}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"siemplify_task_assignee\": {\"type\": \"string\"}, \"siemplify_soar_task_id\": {\"type\": \"integer\"}, \"siemplify_case_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 91
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 62,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1648762327518,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1648762327518,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "250d8dd7-cd55-45a9-9ad7-3307ca5d6830"
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
      "display_name": "Siemplify List Entries",
      "export_key": "siemplify_list_entries",
      "fields": {
        "entity": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "siemplify_list_entries/entity",
          "hide_notification": false,
          "id": 1084,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "entity",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Entity",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "db9de9ee-a326-4021-b47d-76742a720fab",
          "values": [],
          "width": 135
        },
        "entity_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "siemplify_list_entries/entity_type",
          "hide_notification": false,
          "id": 1085,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "entity_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Entity Type/Category",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "4f6f34ee-3231-47df-b5de-e8139831bcd1",
          "values": [],
          "width": 151
        },
        "environments": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "siemplify_list_entries/environments",
          "hide_notification": false,
          "id": 1086,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "environments",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Environments",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "88f67d49-01c3-4ab2-8c72-170dc3905b40",
          "values": [],
          "width": 106
        },
        "list_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "siemplify_list_entries/list_name",
          "hide_notification": false,
          "id": 1087,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "list_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "List Name",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "ced8db69-d169-4352-8cbe-6400a31b5adf",
          "values": [],
          "width": 135
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "siemplify_list_entries/report_date",
          "hide_notification": false,
          "id": 1088,
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
          "type_id": 1016,
          "uuid": "54dbb0f0-186b-420c-ab06-1c82416d6bcd",
          "values": [],
          "width": 247
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
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "siemplify_list_entries",
      "uuid": "0b104210-3821-4a86-a6a3-d5dde67a05c3"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_addupdate_entity_to_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_addupdate_entity_to_customlist\" isExecutable=\"true\" name=\"Siemplify Add/Update Entity to Custom List\"\u003e\u003cdocumentation\u003eAdd or update an artifact on the Siemplify custom list\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0wvg533\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wvg533\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0baktjt\"/\u003e\u003cendEvent id=\"EndEvent_0nlfy5d\"\u003e\u003cincoming\u003eSequenceFlow_1mojhds\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0baktjt\" name=\"Siemplify Add/Update Entity to Cu...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"dc383d80-a189-4763-977c-75452f33d917\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results.success:\\n  entity = results.content\\n  row = incident.addRow(\u0027siemplify_list_entries\u0027)\\n  row[\u0027report_date\u0027] = current_dt\\n  row[\u0027list_name\u0027] = \u0027Custom List\u0027\\n  row[\u0027entity\u0027] = entity[\u0027entityIdentifier\u0027]\\n  row[\u0027entity_type\u0027] = entity[\u0027category\u0027]\\n  row[\u0027environments\u0027] = \\\", \\\".join(entity[\u0027environments\u0027])\\n  incident.addNote(\\\"Siemplify Add/Update Custom List successful for: {} ({})\\\".format(artifact.value, artifact.type))\\nelse:\\n  incident.addNote(\\\"Siemplify Add/Update Custom List Entity failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.siemplify_artifact_type = artifact.type\\ninputs.siemplify_artifact_value = artifact.value\\ninputs.siemplify_category = rule.properties.siemplify_list_category\\ninputs.siemplify_environment = rule.properties.siemplify_environments\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wvg533\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mojhds\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mojhds\" sourceRef=\"ServiceTask_0baktjt\" targetRef=\"EndEvent_0nlfy5d\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00sbgdr\"\u003e\u003ctext\u003eSuccessful updates will display in the Siemplify Blocklist datatable\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0db5drn\" sourceRef=\"ServiceTask_0baktjt\" targetRef=\"TextAnnotation_00sbgdr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wvg533\" id=\"SequenceFlow_0wvg533_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"196.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nlfy5d\" id=\"EndEvent_0nlfy5d_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"471\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0baktjt\" id=\"ServiceTask_0baktjt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mojhds\" id=\"SequenceFlow_1mojhds_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"471\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"428\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00sbgdr\" id=\"TextAnnotation_00sbgdr_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"197\" x=\"367\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0db5drn\" id=\"Association_0db5drn_di\"\u003e\u003comgdi:waypoint x=\"380\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Add or update an artifact on the Siemplify custom list",
      "export_key": "siemplify_addupdate_entity_to_customlist",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797094187,
      "name": "Siemplify Add/Update Entity to Custom List",
      "object_type": "artifact",
      "programmatic_name": "siemplify_addupdate_entity_to_customlist",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "dd607730-0a3c-487e-9974-98366644f061",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_m_sync_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_m_sync_case\" isExecutable=\"true\" name=\"Siemplify Sync Case\"\u003e\u003cdocumentation\u003eSynchronize an incident, artifacts, comments and attachments with a Siemplify Case. An existing case is updated if the custom field Siemplify_case_id is not set.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0aytvve\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0w67d7h\" name=\"Siemplify Sync Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bf1b6ee8-4853-4a6a-8c21-808446de4c80\"\u003e{\"inputs\":{\"ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"dd93eb58-531b-4807-8ea8-4471b70e204d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"7b6dde8b-b1f0-476c-a442-f8e7cd706a34\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results.success:\\n  incident.properties.siemplify_case_id = results.content.get(\u0027id\u0027)\\n  incident.properties.siemplify_case_link = helper.createRichText(\\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results.content.get(\u0027siemplify_case_url\u0027), results.content.get(\u0027title\u0027)))\\n  if results.content.get(\u0027alerts\u0027):\\n    incident.properties.siemplify_alert_id = results.content[\u0027alerts\u0027][0][\u0027identifier\u0027]\\n  incident.addNote(\\\"Siemplify Sync Case {} created\\\".format(results.content.get(\u0027id\u0027)))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Case failed: {}\\\".format(str(results.content)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_incident_id = incident.id\\ninputs.siemplify_assigned_user = \\\"@Administrator\\\"\\ninputs.siemplify_environment = \\\"Default Environment\\\"\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0aytvve\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hhztx1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0aytvve\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0w67d7h\"/\u003e\u003cendEvent id=\"EndEvent_0p32n4t\"\u003e\u003cincoming\u003eSequenceFlow_1hhztx1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hhztx1\" sourceRef=\"ServiceTask_0w67d7h\" targetRef=\"EndEvent_0p32n4t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1dq6ysr\"\u003e\u003ctext\u003e\u003c![CDATA[Sync results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1afda0h\" sourceRef=\"ServiceTask_0w67d7h\" targetRef=\"TextAnnotation_1dq6ysr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0w67d7h\" id=\"ServiceTask_0w67d7h_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0aytvve\" id=\"SequenceFlow_0aytvve_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0p32n4t\" id=\"EndEvent_0p32n4t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"423\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"441\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hhztx1\" id=\"SequenceFlow_1hhztx1_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"388.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1dq6ysr\" id=\"TextAnnotation_1dq6ysr_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"161\" x=\"343\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1afda0h\" id=\"Association_1afda0h_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Synchronize an incident, artifacts, comments and attachments with a Siemplify Case. An existing case is updated if the custom field Siemplify_case_id is not set.",
      "export_key": "siemplify_m_sync_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797092524,
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
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_sync_comment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_comment\" isExecutable=\"true\" name=\"Siemplify Sync Comment\"\u003e\u003cdocumentation\u003eSync an IBM SOAR Comment with Siemplify\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dw9j37\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tfr8rw\" name=\"Siemplify Sync Comment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d4c2ae89-f290-4135-aef9-79108685e92e\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note.text = \\\"\u0026lt;b\u0026gt;Siemplify Sync complete\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\"+note.text.content\\nelse:\\n  incident.addNote(helper.createRichText(\\\"Siemplify Sync for note failed. Reason: {}\\\".format(results.reason)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_comment = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dw9j37\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qtoy8t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dw9j37\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tfr8rw\"/\u003e\u003cendEvent id=\"EndEvent_1iowpy1\"\u003e\u003cincoming\u003eSequenceFlow_1qtoy8t\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1qtoy8t\" sourceRef=\"ServiceTask_1tfr8rw\" targetRef=\"EndEvent_1iowpy1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0cyhbqr\"\u003e\u003ctext\u003e\u003c![CDATA[Note updated to reflect sync\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1yhse3a\" sourceRef=\"ServiceTask_1tfr8rw\" targetRef=\"TextAnnotation_0cyhbqr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tfr8rw\" id=\"ServiceTask_1tfr8rw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dw9j37\" id=\"SequenceFlow_1dw9j37_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1iowpy1\" id=\"EndEvent_1iowpy1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"399\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"417\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qtoy8t\" id=\"SequenceFlow_1qtoy8t_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"373\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0cyhbqr\" id=\"TextAnnotation_0cyhbqr_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"352\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1yhse3a\" id=\"Association_1yhse3a_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"112\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync an IBM SOAR Comment with Siemplify",
      "export_key": "siemplify_sync_comment",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797092319,
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
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "siemplify_add_playbook",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_add_playbook\" isExecutable=\"true\" name=\"Siemplify Add Playbook\"\u003e\u003cdocumentation\u003eAdd a playbook to a Siemplify Case\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0mhr8ri\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0m0ppu0\" name=\"Siemplify Add Playbook\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8f05f74-95fa-4861-8264-5398d247da7b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_playbook_name = rule.properties.siemplify_playbook_name\\ninputs.siemplify_run_playbook_automatically = rule.properties.siemplify_run_playbook_automatically\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0mhr8ri\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1x391sy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0mhr8ri\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0m0ppu0\"/\u003e\u003cendEvent id=\"EndEvent_17sdlcf\"\u003e\u003cincoming\u003eSequenceFlow_1x391sy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1x391sy\" sourceRef=\"ServiceTask_0m0ppu0\" targetRef=\"EndEvent_17sdlcf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0m0ppu0\" id=\"ServiceTask_0m0ppu0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mhr8ri\" id=\"SequenceFlow_0mhr8ri_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"237.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_17sdlcf\" id=\"EndEvent_17sdlcf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"456.8784956605593\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"474.8784956605593\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x391sy\" id=\"SequenceFlow_1x391sy_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "a@example.com",
      "description": "Add a playbook to a Siemplify Case",
      "export_key": "siemplify_add_playbook",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1648761392940,
      "name": "Siemplify Add Playbook",
      "object_type": "incident",
      "programmatic_name": "siemplify_add_playbook",
      "tags": [],
      "uuid": "7a124e43-c80a-4d63-b8ea-f5dff40b9543",
      "workflow_id": 152
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_sync_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_attachment\" isExecutable=\"true\" name=\"Siemplify Sync Attachment\"\u003e\u003cdocumentation\u003eSync a SOAR case attachment to a Siemplify case attachment\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_04748ia\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cggez0\" name=\"Siemplify Sync Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3036407-650f-4e31-8528-4f6b0847560b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(\\\"Siemplify Sync Attachment: {} created\\\".format(attachment.name))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Attachment: {} failed. Reason: {}\\\".format(attachment.name, results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_incident_id = incident.id\\ninputs.siemplify_attachment_id = attachment.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_04748ia\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1adbvuz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_04748ia\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cggez0\"/\u003e\u003cendEvent id=\"EndEvent_08r0xmm\"\u003e\u003cincoming\u003eSequenceFlow_1adbvuz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1adbvuz\" sourceRef=\"ServiceTask_0cggez0\" targetRef=\"EndEvent_08r0xmm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1wa60c0\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_136xpb6\" sourceRef=\"ServiceTask_0cggez0\" targetRef=\"TextAnnotation_1wa60c0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cggez0\" id=\"ServiceTask_0cggez0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04748ia\" id=\"SequenceFlow_04748ia_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08r0xmm\" id=\"EndEvent_08r0xmm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"441\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1adbvuz\" id=\"SequenceFlow_1adbvuz_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"404.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1wa60c0\" id=\"TextAnnotation_1wa60c0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"358\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_136xpb6\" id=\"Association_136xpb6_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR case attachment to a Siemplify case attachment",
      "export_key": "siemplify_sync_attachment",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797092713,
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
      "workflow_id": 86
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_sync_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_artifact\" isExecutable=\"true\" name=\"Siemplify Sync Artifact\"\u003e\u003cdocumentation\u003eSync a SOAR Incident artifact to a Siemplify Case alert and entity\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lp0b0i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0bvtpg3\" name=\"Siemplify Sync Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f5320892-50c9-4aae-8d08-45bc25b6e682\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  incident.addNote(\\\"Siemplify Sync Artifact: {} ({}) created\\\".format(artifact.value, artifact.type))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Artifact: {} ({}) failed\\\".format(artifact.value, artifact.type))\\n  \",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_artifact_type = artifact.type\\ninputs.siemplify_artifact_value = artifact.value\\ninputs.siemplify_environment = None\\ninputs.siemplify_artifact_id = artifact.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lp0b0i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1n8bleh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lp0b0i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0bvtpg3\"/\u003e\u003cendEvent id=\"EndEvent_1wew0w9\"\u003e\u003cincoming\u003eSequenceFlow_1n8bleh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1n8bleh\" sourceRef=\"ServiceTask_0bvtpg3\" targetRef=\"EndEvent_1wew0w9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ypf2yo\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_133e51o\" sourceRef=\"ServiceTask_0bvtpg3\" targetRef=\"TextAnnotation_1ypf2yo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0bvtpg3\" id=\"ServiceTask_0bvtpg3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"286\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lp0b0i\" id=\"SequenceFlow_1lp0b0i_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"242\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wew0w9\" id=\"EndEvent_1wew0w9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"486\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"459\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1n8bleh\" id=\"SequenceFlow_1n8bleh_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ypf2yo\" id=\"TextAnnotation_1ypf2yo_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"371\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_133e51o\" id=\"Association_133e51o_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR Incident artifact to a Siemplify Case alert and entity",
      "export_key": "siemplify_sync_artifact",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797094053,
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
        "version": 1,
        "workflow_id": "siemplify_sync_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_case\" isExecutable=\"true\" name=\"Siemplify Auto Sync Case\"\u003e\u003cdocumentation\u003eSync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_133ewo1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ao7iqd\" name=\"Siemplify Sync Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bf1b6ee8-4853-4a6a-8c21-808446de4c80\"\u003e{\"inputs\":{\"ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"dd93eb58-531b-4807-8ea8-4471b70e204d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"7b6dde8b-b1f0-476c-a442-f8e7cd706a34\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results.success:\\n  incident.properties.siemplify_case_id = results.content.get(\u0027id\u0027)\\n  incident.properties.siemplify_case_link = helper.createRichText(\\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{}\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results.content.get(\u0027siemplify_case_url\u0027), results.content.get(\u0027title\u0027)))\\n  incident.properties.siemplify_is_important = results.content.get(\u0027isImportant\u0027)\\n  incident.properties.siemplify_stage = results.content.get(\u0027stage\u0027)\\n  incident.properties.siemplify_assignee = results.content.get(\u0027assignedUserName\u0027)\\n  incident.properties.siemplify_priority = results.content.get(\u0027priority\u0027)\\n  incident.properties.siemplify_tags = \\\", \\\".join([tag[\u0027tag\u0027] for tag in results.content.get(\u0027tags\u0027)])\\n  \\n  if results.content.get(\u0027alerts\u0027):\\n    incident.properties.siemplify_alert_id = results.content[\u0027alerts\u0027][0][\u0027identifier\u0027]\\n  incident.addNote(\\\"Siemplify Sync Case {} created\\\".format(results.content.get(\u0027id\u0027)))\\nelse:\\n  incident.addNote(\\\"Siemplify Sync Case failed: {}\\\".format(str(results.content)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_incident_id = incident.id\\ninputs.siemplify_assigned_user = None\\ninputs.siemplify_environment = None\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_133ewo1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14vcfso\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_133ewo1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ao7iqd\"/\u003e\u003cendEvent id=\"EndEvent_04a6awv\"\u003e\u003cincoming\u003eSequenceFlow_14vcfso\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14vcfso\" sourceRef=\"ServiceTask_0ao7iqd\" targetRef=\"EndEvent_04a6awv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02eb4gg\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0a4pfoi\" sourceRef=\"ServiceTask_0ao7iqd\" targetRef=\"TextAnnotation_02eb4gg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ao7iqd\" id=\"ServiceTask_0ao7iqd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_133ewo1\" id=\"SequenceFlow_133ewo1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04a6awv\" id=\"EndEvent_04a6awv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"452\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"425\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14vcfso\" id=\"SequenceFlow_14vcfso_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"368\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02eb4gg\" id=\"TextAnnotation_02eb4gg_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"202\" x=\"362\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0a4pfoi\" id=\"Association_0a4pfoi_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"446\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments",
      "export_key": "siemplify_sync_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797093104,
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
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_sync_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_task\" isExecutable=\"true\" name=\"Siemplify Sync Task\"\u003e\u003cdocumentation\u003eSync a SOAR incident task to Siemplify\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1igd3a2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0o6ht79\" name=\"Siemplify Sync Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d8b35373-e80d-42cc-9120-e0073847252a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  task.addNote(\\\"Siemplify Sync Task: {}\\\".format(task.name))\\nelse:\\n  task.addNote(\\\"Siemplify Sync Task: {} failed: {}\\\".format(task.name, results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_soar_task_id = task.id\\ninputs.siemplify_task_assignee = \\\"@Administrator\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1igd3a2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1s0qzhm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1igd3a2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0o6ht79\"/\u003e\u003cendEvent id=\"EndEvent_0is86cj\"\u003e\u003cincoming\u003eSequenceFlow_1s0qzhm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1s0qzhm\" sourceRef=\"ServiceTask_0o6ht79\" targetRef=\"EndEvent_0is86cj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ynurxt\"\u003e\u003ctext\u003e\u003c![CDATA[Sync results returned in a task note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1tfbar0\" sourceRef=\"ServiceTask_0o6ht79\" targetRef=\"TextAnnotation_1ynurxt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0o6ht79\" id=\"ServiceTask_0o6ht79_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"263\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1igd3a2\" id=\"SequenceFlow_1igd3a2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"263\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"230.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0is86cj\" id=\"EndEvent_0is86cj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"431\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"449\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1s0qzhm\" id=\"SequenceFlow_1s0qzhm_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"397\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ynurxt\" id=\"TextAnnotation_1ynurxt_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"162\" x=\"342\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1tfbar0\" id=\"Association_1tfbar0_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR incident task to Siemplify",
      "export_key": "siemplify_sync_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797093712,
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
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_addupdate_entity_to_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_addupdate_entity_to_blocklist\" isExecutable=\"true\" name=\"Siemplify: Add/Update Entity to Block List\"\u003e\u003cdocumentation\u003eAdd or update an artifact on the Siemplify Block List\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0wvg533\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1kie8gk\" name=\"Siemplify: Add/Update Entity to B...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bc122044-f6a1-4c39-b433-842a59eb9bcd\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results.success:\\n  entity = results.content\\n  row = incident.addRow(\u0027siemplify_list_entries\u0027)\\n  row[\u0027report_date\u0027] = current_dt\\n  row[\u0027list_name\u0027] = \u0027Block List\u0027\\n  row[\u0027entity\u0027] = entity[\u0027entityIdentifier\u0027]\\n  row[\u0027entity_type\u0027] = entity[\u0027entityType\u0027]\\n  row[\u0027environments\u0027] = \\\", \\\".join(entity[\u0027environments\u0027])\\n  incident.addNote(\\\"Siemplify Add/Update Blocklist successful for: {} ({})\\\".format(artifact.value, artifact.type))\\nelse:\\n  incident.addNote(\\\"Siemplify Add/Update Blocklist Entity failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.siemplify_artifact_type = artifact.type\\ninputs.siemplify_artifact_value = artifact.value\\ninputs.siemplify_environment = rule.properties.siemplify_environments\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wvg533\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_15k6wil\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0wvg533\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kie8gk\"/\u003e\u003cendEvent id=\"EndEvent_0nlfy5d\"\u003e\u003cincoming\u003eSequenceFlow_15k6wil\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_15k6wil\" sourceRef=\"ServiceTask_1kie8gk\" targetRef=\"EndEvent_0nlfy5d\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1aqpfcq\"\u003e\u003ctext\u003e\u003c![CDATA[Successful updates will display in the Siemplify List datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_12x21le\" sourceRef=\"ServiceTask_1kie8gk\" targetRef=\"TextAnnotation_1aqpfcq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kie8gk\" id=\"ServiceTask_1kie8gk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wvg533\" id=\"SequenceFlow_0wvg533_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"236.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nlfy5d\" id=\"EndEvent_0nlfy5d_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"456.1147208121827\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"474.1147208121827\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15k6wil\" id=\"SequenceFlow_15k6wil_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"415.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1aqpfcq\" id=\"TextAnnotation_1aqpfcq_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"210\" x=\"364\" y=\"75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_12x21le\" id=\"Association_12x21le_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"135\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Add or update an artifact on the Siemplify Block List",
      "export_key": "siemplify_addupdate_entity_to_blocklist",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797093885,
      "name": "Siemplify: Add/Update Entity to Block List",
      "object_type": "artifact",
      "programmatic_name": "siemplify_addupdate_entity_to_blocklist",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "bb64bd31-d6ee-4dbc-a687-47b0f160fae1",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_get_blocklist_entities",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_get_blocklist_entities\" isExecutable=\"true\" name=\"Siemplify Get Block List Entities\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get entities associated with Siemplify\u0027s Block List]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0uqgmpq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0rzsl0z\" name=\"Siemplify: Get Blocklist Entities\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2bf54da4-8de2-4b4b-8baf-d7e74d0c2d58\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results.success:\\n  if isinstance(results.content, list):\\n    entity_list = results.content\\n  else:\\n    entity_list = results.content.get(\\\"objectsList\\\", {})\\n    \\n  for entity in entity_list:\\n    row = incident.addRow(\u0027siemplify_list_entries\u0027)\\n    row[\u0027report_date\u0027] = current_dt\\n    row[\u0027list_name\u0027] = \u0027Block List\u0027\\n    row[\u0027entity\u0027] = entity[\u0027entityIdentifier\u0027]\\n    row[\u0027entity_type\u0027] = entity[\u0027entityType\u0027]\\n    row[\u0027environments\u0027] = \\\", \\\".join(entity[\u0027environments\u0027])\\nelse:\\n  incident.addNote(\\\"Siemplify Get Blocklist Entities failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.siemplify_limit = rule.properties.siemplify_limit_result if rule.properties.siemplify_limit_result else 100\\ninputs.siemplify_search = rule.properties.siemplify_search_term \",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0uqgmpq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vv3388\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0uqgmpq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rzsl0z\"/\u003e\u003cendEvent id=\"EndEvent_0dqezus\"\u003e\u003cincoming\u003eSequenceFlow_0vv3388\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vv3388\" sourceRef=\"ServiceTask_0rzsl0z\" targetRef=\"EndEvent_0dqezus\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1a96ruo\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Siemplify List Entities datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0u1kr0b\" sourceRef=\"ServiceTask_0rzsl0z\" targetRef=\"TextAnnotation_1a96ruo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rzsl0z\" id=\"ServiceTask_0rzsl0z_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"294\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uqgmpq\" id=\"SequenceFlow_0uqgmpq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"294\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"246\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0dqezus\" id=\"EndEvent_0dqezus_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"466\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"484\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vv3388\" id=\"SequenceFlow_0vv3388_di\"\u003e\u003comgdi:waypoint x=\"394\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"466\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"430\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1a96ruo\" id=\"TextAnnotation_1a96ruo_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"186\" x=\"382\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0u1kr0b\" id=\"Association_0u1kr0b_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"138\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Get entities associated with Siemplify\u0027s Block List",
      "export_key": "siemplify_get_blocklist_entities",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797093512,
      "name": "Siemplify Get Block List Entities",
      "object_type": "incident",
      "programmatic_name": "siemplify_get_blocklist_entities",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "89f744a1-0df5-43e6-a198-45a0b5177df7",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "siemplify_close_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_close_case\" isExecutable=\"true\" name=\"Siemplify Close Case\"\u003e\u003cdocumentation\u003eSync SOAR incident close with Siemplify Case\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bwyqvy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ev7ddc\" name=\"Siemplify Close Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bca6302b-7f12-4b86-a931-d1e8b3d58e84\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note = \\\"Siemplify Sync cased {} closed\\\".format(incident.properties.siemplify_case_id)\\nelse:\\n  note = \\\"Siemplify Sync cased {} failed to close: {}\\\".format(incident.properties.siemplify_case_id, results.reason)\\nincident.addNote(helper.createPlainText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# change as necessary. Value Siemplify values are:  Malicious, Non Malicious, Maintenance, Inconclusive\\nLOOKUP_STATUS = {\\n    \\\"7\\\": \\\"Inconclusive\\\", # Unresolved\\n    \\\"8\\\": \\\"Inconclusive\\\", # Duplicate\\n    \\\"9\\\": \\\"Non Malicious\\\", # Not an Issue\\n    \\\"10\\\": \\\"Malicious\\\" # Resolved\\n}\\n\\ninputs.siemplify_alert_id = incident.properties.siemplify_alert_id\\ninputs.siemplify_case_id = incident.properties.siemplify_case_id\\ninputs.siemplify_root_cause = incident.resolution_summary.content\\ninputs.siemplify_reason = LOOKUP_STATUS.get(str(incident.resolution_id), \u0027Inconclusive\u0027)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bwyqvy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_034lepw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bwyqvy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ev7ddc\"/\u003e\u003cendEvent id=\"EndEvent_0k9rsis\"\u003e\u003cincoming\u003eSequenceFlow_034lepw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_034lepw\" sourceRef=\"ServiceTask_1ev7ddc\" targetRef=\"EndEvent_0k9rsis\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07y1lm0\"\u003e\u003ctext\u003eCreates a note with sync status\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14io1nw\" sourceRef=\"ServiceTask_1ev7ddc\" targetRef=\"TextAnnotation_07y1lm0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ev7ddc\" id=\"ServiceTask_1ev7ddc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"303\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bwyqvy\" id=\"SequenceFlow_1bwyqvy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"303\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"250.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0k9rsis\" id=\"EndEvent_0k9rsis_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"486\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"504\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_034lepw\" id=\"SequenceFlow_034lepw_di\"\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"444.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07y1lm0\" id=\"TextAnnotation_07y1lm0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"389\" y=\"87\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14io1nw\" id=\"Association_14io1nw_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync SOAR incident close with Siemplify Case",
      "export_key": "siemplify_close_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645797092905,
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
      "workflow_id": 87
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "siemplify_get_customlist_entities",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_get_customlist_entities\" isExecutable=\"true\" name=\"Siemplify Get Custom List Entities\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get entities associated with Siemplify\u0027s Custom List]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0uqgmpq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0uqgmpq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1nklqx7\"/\u003e\u003cendEvent id=\"EndEvent_0dqezus\"\u003e\u003cincoming\u003eSequenceFlow_1hsasdt\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1nklqx7\" name=\"Siemplify Get Custom List Entitie...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f7c15417-71ef-4ab5-adff-e3ab84768f4e\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results.success:\\n  if isinstance(results.content, list):\\n    entity_list = results.content\\n  else:\\n    entity_list = results.content.get(\\\"objectsList\\\", {})\\n    \\n  for entity in entity_list:\\n    row = incident.addRow(\u0027siemplify_list_entries\u0027)\\n    row[\u0027report_date\u0027] = current_dt\\n    row[\u0027list_name\u0027] = \u0027Custom List\u0027\\n    row[\u0027entity\u0027] = entity[\u0027entityIdentifier\u0027]\\n    row[\u0027entity_type\u0027] = entity[\u0027category\u0027]\\n    row[\u0027environments\u0027] = \\\", \\\".join(entity[\u0027environments\u0027])\\nelse:\\n  incident.addNote(\\\"Siemplify Get Custom List Entities failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.siemplify_limit = rule.properties.siemplify_limit_result if rule.properties.siemplify_limit_result else None\\ninputs.siemplify_environments = rule.properties.siemplify_environments\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0uqgmpq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hsasdt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1hsasdt\" sourceRef=\"ServiceTask_1nklqx7\" targetRef=\"EndEvent_0dqezus\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0iq82z7\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Siemplify List Entities datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0czgph8\" sourceRef=\"ServiceTask_1nklqx7\" targetRef=\"TextAnnotation_0iq82z7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uqgmpq\" id=\"SequenceFlow_0uqgmpq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"299\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"203.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0dqezus\" id=\"EndEvent_0dqezus_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"502\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"475\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1nklqx7\" id=\"ServiceTask_1nklqx7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"299\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hsasdt\" id=\"SequenceFlow_1hsasdt_di\"\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"502\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"450.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0iq82z7\" id=\"TextAnnotation_0iq82z7_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"167\" x=\"391\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0czgph8\" id=\"Association_0czgph8_di\"\u003e\u003comgdi:waypoint x=\"395\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"143\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@example.com",
      "description": "Get entities associated with Siemplify\u0027s Custom List",
      "export_key": "siemplify_get_customlist_entities",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1645899974759,
      "name": "Siemplify Get Custom List Entities",
      "object_type": "incident",
      "programmatic_name": "siemplify_get_customlist_entities",
      "tags": [
        {
          "tag_handle": "fn_siemplify",
          "value": null
        }
      ],
      "uuid": "8ca9d4ae-41be-4aa6-9548-263fa40f6b3f",
      "workflow_id": 89
    }
  ],
  "workspaces": []
}
