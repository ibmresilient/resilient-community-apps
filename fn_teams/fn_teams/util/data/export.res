{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Group from incident",
      "id": 56,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Group from incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f63657ce-d1d9-4459-bb26-e8ee61eb71cf",
      "view_items": [
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9e46e44-a4db-4190-8e31-f4b959a2568d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Group from task",
      "id": 57,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Group from task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1452ff67-bf9c-41ed-930b-a126783f0eed",
      "view_items": [
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d0e04cd2-57f9-4a93-a919-b84adb5ff7ac",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Delete Group from incident",
      "id": 58,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Delete Group from incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a7581e16-da65-48c3-a21f-8a55a949ceaa",
      "view_items": [
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_delete_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Post incident information to teams",
      "id": 55,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Post incident information to teams",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ab423457-6a80-43e1-ba72-24d7729359dd",
      "view_items": [],
      "workflows": [
        "incident_post_message_to_teams"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Post task information to teams",
      "id": 54,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Post task information to teams",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a4ea172e-6103-4db1-87a0-17a5e2e27a97",
      "view_items": [],
      "workflows": [
        "task_post_message_to_teams"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1667838173812,
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
      "export_key": "__function/ms_group_mail_nickname",
      "hide_notification": false,
      "id": 356,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_mail_nickname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_mail_nickname",
      "tooltip": "Group mail nickname",
      "type_id": 11,
      "uuid": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
      "export_key": "__function/ms_team_name",
      "hide_notification": false,
      "id": 369,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_team_name",
      "tooltip": "Name of the Microsoft Team",
      "type_id": 11,
      "uuid": "8c740ee5-6b2d-4555-be2e-e0dce0fe93fc",
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
      "id": 348,
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
          "tag_handle": "fn_teams",
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
      "export_key": "__function/add_members_from",
      "hide_notification": false,
      "id": 358,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "add_members_from",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "9602467c-8872-4fe0-9992-20498e6b076e",
          "value": 152
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Task",
          "properties": null,
          "uuid": "40b72b22-9485-47ac-9ade-ee2f97a38515",
          "value": 162
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Incident",
          "properties": null,
          "uuid": "054edd56-3fd2-4068-8779-bcc24e8e2c5d",
          "value": 163
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
      "export_key": "__function/additional_members",
      "hide_notification": false,
      "id": 357,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "additional_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "additional_members",
      "tooltip": "A list of members of the group",
      "type_id": 11,
      "uuid": "caa4ac0d-4869-46bb-b0f5-e585c43b396e",
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
      "export_key": "__function/ms_owners_list",
      "hide_notification": false,
      "id": 366,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_owners_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_owners_list",
      "tooltip": "A list of owners for the group or team",
      "type_id": 11,
      "uuid": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
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
      "export_key": "__function/ms_group_name",
      "hide_notification": false,
      "id": 355,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_name",
      "tooltip": "Microsoft Group Name",
      "type_id": 11,
      "uuid": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
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
      "export_key": "__function/teams_mrkdown",
      "hide_notification": false,
      "id": 349,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "teams_mrkdown",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_mrkdown",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
      "export_key": "__function/teams_payload",
      "hide_notification": false,
      "id": 350,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_payload",
      "tooltip": "json of teams conversation message: sections, title, text, facts",
      "type_id": 11,
      "uuid": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
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
      "id": 351,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
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
      "export_key": "__function/ms_group_description",
      "hide_notification": false,
      "id": 364,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6c7730f3-4872-4709-b60a-cabee7e5a208",
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
      "export_key": "__function/ms_team_description",
      "hide_notification": false,
      "id": 370,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_team_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_team_description",
      "tooltip": "Description for the team to be created",
      "type_id": 11,
      "uuid": "6dc5af14-2a95-418f-9094-e388a3fb2053",
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
      "export_key": "__function/teams_channel",
      "hide_notification": false,
      "id": 352,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_channel",
      "tooltip": "Lookup value to channel to post a message",
      "type_id": 11,
      "uuid": "76023ce3-fc17-41d1-9002-2392283ce315",
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
      "export_key": "actioninvocation/ms_group_mail_nickname",
      "hide_notification": false,
      "id": 359,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_mail_nickname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Mail nickname",
      "tooltip": "This value must be a unique value as no two MS Objects can have the same email ID",
      "type_id": 6,
      "uuid": "80a3cfc0-209d-45d2-a422-54531b7123a8",
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
      "export_key": "actioninvocation/additional_members",
      "hide_notification": false,
      "id": 362,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "additional_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Additional members",
      "tooltip": "Add members who are not members of this incident or task",
      "type_id": 6,
      "uuid": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
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
      "export_key": "actioninvocation/ms_owners_list",
      "hide_notification": false,
      "id": 367,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_owners_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Owners",
      "tooltip": "",
      "type_id": 6,
      "uuid": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
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
      "export_key": "actioninvocation/ms_group_description",
      "hide_notification": false,
      "id": 365,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Description",
      "tooltip": "",
      "type_id": 6,
      "uuid": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
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
      "export_key": "actioninvocation/add_members_task",
      "hide_notification": false,
      "id": 363,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_task",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Add members",
      "tooltip": "",
      "type_id": 6,
      "uuid": "d0e04cd2-57f9-4a93-a919-b84adb5ff7ac",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "Incident",
          "properties": null,
          "uuid": "358dd2e0-92ef-411d-baab-e11c33778440",
          "value": 160
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "e54c978e-266e-4c8d-9c09-5de4d5d0f70d",
          "value": 161
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All task members",
          "properties": null,
          "uuid": "97c9273e-5c12-45fc-ae17-c077cf44e25b",
          "value": 205
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All incident members",
          "properties": null,
          "uuid": "3bf0cc9d-09fe-4536-950d-22c47c29ff64",
          "value": 206
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
      "export_key": "actioninvocation/add_members_incident",
      "hide_notification": false,
      "id": 368,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_incident",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Add members",
      "tooltip": "",
      "type_id": 6,
      "uuid": "d9e46e44-a4db-4190-8e31-f4b959a2568d",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "ab334806-2665-4498-bd3a-e9ff05d62c50",
          "value": 203
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All incident members",
          "properties": null,
          "uuid": "6ba20604-b094-4fcf-ae8b-6e3141f63d9b",
          "value": 204
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
      "export_key": "actioninvocation/ms_group_name",
      "hide_notification": false,
      "id": 354,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Group name",
      "tooltip": "Name of the Group to be created",
      "type_id": 6,
      "uuid": "27cd3210-769a-4443-b25e-947b4270ebc8",
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
      "created_date": 1665141108187,
      "description": {
        "content": "A function to create a Microsoft Group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create group",
      "export_key": "ms_teams_create_group",
      "id": 17,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1667477505368,
      "name": "ms_teams_create_group",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "120d2055-a0de-413b-b5d7-444d289dd469",
      "version": 7,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
          "content": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "caa4ac0d-4869-46bb-b0f5-e585c43b396e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6c7730f3-4872-4709-b60a-cabee7e5a208",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
          "name": "Incident: Create a Microsoft Group",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 45
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Microsoft Group",
          "object_type": "task",
          "programmatic_name": "task_create_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 46
        }
      ]
    },
    {
      "created_date": 1667489279447,
      "description": {
        "content": "A sample workflow to create a team",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create team",
      "export_key": "ms_teams_create_team",
      "id": 20,
      "last_modified_by": {
        "display_name": "Admin Resilient",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667820400029,
      "name": "ms_teams_create_team",
      "tags": [],
      "uuid": "9acc046d-60f3-4be8-97cf-c966436e6f9b",
      "version": 2,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
          "content": "8c740ee5-6b2d-4555-be2e-e0dce0fe93fc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6dc5af14-2a95-418f-9094-e388a3fb2053",
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
          "name": "Incident: Create a Microsoft Team",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_microsoft_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 49
        }
      ]
    },
    {
      "created_date": 1667472924989,
      "description": {
        "content": "A sample function to delete a group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Delete Group",
      "export_key": "ms_teams_delete_group",
      "id": 19,
      "last_modified_by": {
        "display_name": "Admin Resilient",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667472925020,
      "name": "ms_teams_delete_group",
      "tags": [],
      "uuid": "c710fb72-c934-45ce-9205-e36794fee376",
      "version": 1,
      "view_items": [
        {
          "content": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
          "name": "Incident: Delete a Microsoft Group",
          "object_type": "incident",
          "programmatic_name": "incident_delete_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 52
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Delete a Microsoft Group",
          "object_type": "task",
          "programmatic_name": "task_delete_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 53
        }
      ]
    },
    {
      "created_date": 1665141108217,
      "description": {
        "content": "Post a message to a Microsoft Teams channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Post Message",
      "export_key": "ms_teams_post_message",
      "id": 18,
      "last_modified_by": {
        "display_name": "Admin Resilient",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667492872177,
      "name": "ms_teams_post_message",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "0c8e4497-c131-4d5d-bdf3-3153d30b9bbc",
      "version": 6,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
          "content": "76023ce3-fc17-41d1-9002-2392283ce315",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
          "name": "Incident: Post message to Teams",
          "object_type": "incident",
          "programmatic_name": "incident_post_message_to_teams",
          "tags": [
            {
              "tag_handle": "fn_teams",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 50
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Post message to Teams",
          "object_type": "task",
          "programmatic_name": "task_post_message_to_teams",
          "tags": [
            {
              "tag_handle": "fn_teams",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 51
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 109,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1667838169983,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1667838169983,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "f9a74b19-c933-454e-938d-bfe098efff23"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_teams",
      "name": "fn_teams",
      "programmatic_name": "fn_teams",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "users": [],
      "uuid": "44d59a45-1647-438d-ba45-0bbf0c7506f7"
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
        "version": 13,
        "workflow_id": "task_create_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_microsoft_group\" isExecutable=\"true\" name=\"Task: Create a Microsoft Group\"\u003e\u003cdocumentation\u003eA sample workflow to create a MS Group from a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1uejmnm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q75ylm\" name=\"MS Teams: Create group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"120d2055-a0de-413b-b5d7-444d289dd469\"\u003e{\"inputs\":{\"d2f9e887-fd44-4b64-98f8-a642b4b1738c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"AdminSoarMS@5rf2xs.onmicrosoft.com\"}},\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if task:\\n    inputs.task_id = task.id\\n  \\ninputs.incident_id = str(incident.id)\\ninputs.ms_group_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_group_name is None else rule.properties.ms_group_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_task is not None:\\n  _value = rule.properties.add_members_task.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  elif _value == \\\"all task members\\\":\\n    inputs.add_members_from = \\\"Task\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_group_description.content is not None:\\n    inputs.ms_group_description = rule.properties.ms_group_description.content\\nelse:\\n    inputs.ms_group_description = f\\\"[Incident] {incident.id}: {incident.name} [Task] {task.id} : {task.name} {task.description}\\\"\\n  \\n\\nif rule.properties.ms_group_mail_nickname is not None:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1uejmnm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1avwvjy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0g889x3\"\u003e\u003cincoming\u003eSequenceFlow_1avwvjy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1avwvjy\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"EndEvent_0g889x3\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1uejmnm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q75ylm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0j0q9b4\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_19zhmo7\" sourceRef=\"EndEvent_0g889x3\" targetRef=\"TextAnnotation_0j0q9b4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0jkumgn\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: group_name, owners_list, members_list, group_description, group_mail_nickname\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1g7juie\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"TextAnnotation_0jkumgn\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1fg0k49\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Incident note with created group details\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_16nskn7\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"TextAnnotation_1fg0k49\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"139\" x=\"110\" y=\"327\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"179\" xsi:type=\"omgdc:Point\" y=\"327\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q75ylm\" id=\"ServiceTask_0q75ylm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"341.3485838779956\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0g889x3\" id=\"EndEvent_0g889x3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"605.3485838779957\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"623.3485838779957\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1avwvjy\" id=\"SequenceFlow_1avwvjy_di\"\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"605\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uejmnm\" id=\"SequenceFlow_1uejmnm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"269.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0j0q9b4\" id=\"TextAnnotation_0j0q9b4_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"573\" y=\"329\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_19zhmo7\" id=\"Association_19zhmo7_di\"\u003e\u003comgdi:waypoint x=\"623\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"623\" xsi:type=\"omgdc:Point\" y=\"329\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0jkumgn\" id=\"TextAnnotation_0jkumgn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"233\" x=\"128\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1g7juie\" id=\"Association_1g7juie_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"284\" xsi:type=\"omgdc:Point\" y=\"95\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1fg0k49\" id=\"TextAnnotation_1fg0k49_di\"\u003e\u003comgdc:Bounds height=\"85\" width=\"165\" x=\"511\" y=\"12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_16nskn7\" id=\"Association_16nskn7_di\"\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"538\" xsi:type=\"omgdc:Point\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "description": "A sample workflow to create a MS Group from a task",
      "export_key": "task_create_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667488190305,
      "name": "Task: Create a Microsoft Group",
      "object_type": "task",
      "programmatic_name": "task_create_a_microsoft_group",
      "tags": [],
      "uuid": "1a53cc12-68ce-4824-a7ab-c3ddd814f642",
      "workflow_id": 46
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "incident_post_message_to_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_post_message_to_teams\" isExecutable=\"true\" name=\"Incident: Post message to Teams\"\u003e\u003cdocumentation\u003eExample of posting incident data to a Microsoft Teams channel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tqeuuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0nrnlka\" name=\"MS Teams: Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"resilient\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to Post message\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n  text = helper.createRichText(text)\\n  incident.addNote(text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\n\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"Resilient Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code\\n   )\\n\\ninputs.teams_payload = payload\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tqeuuk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14r6yw4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tqeuuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nrnlka\"/\u003e\u003cendEvent id=\"EndEvent_1cx5ym9\"\u003e\u003cincoming\u003eSequenceFlow_14r6yw4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14r6yw4\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"EndEvent_1cx5ym9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ing8rr\"\u003e\u003ctext\u003e\u003c![CDATA[Format teams_payload as a json object. See pre-processor script for format.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cgzb03\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"TextAnnotation_0ing8rr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nrnlka\" id=\"ServiceTask_0nrnlka_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tqeuuk\" id=\"SequenceFlow_1tqeuuk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1cx5ym9\" id=\"EndEvent_1cx5ym9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"457\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"475\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14r6yw4\" id=\"SequenceFlow_14r6yw4_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ing8rr\" id=\"TextAnnotation_0ing8rr_di\"\u003e\u003comgdc:Bounds height=\"82\" width=\"207\" x=\"130\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cgzb03\" id=\"Association_1cgzb03_di\"\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"139\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example of posting incident data to a Microsoft Teams channel.",
      "export_key": "incident_post_message_to_teams",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667559848225,
      "name": "Incident: Post message to Teams",
      "object_type": "incident",
      "programmatic_name": "incident_post_message_to_teams",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "abecd789-c436-4006-be07-4d2db698252c",
      "workflow_id": 50
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "task_post_message_to_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_post_message_to_teams\" isExecutable=\"true\" name=\"Task: Post message to Teams\"\u003e\u003cdocumentation\u003eExample of posting incident and task information to Teams as two sections\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0q5lshb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17n68bf\" name=\"MS Teams: Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"testchannel\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to Post message\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n  text = helper.createRichText(text)\\n  task.addNote(text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\ninputs.task_id = task.id\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"Resilient Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }},\\n  {{ \\\"text\\\": \\\"Task\\\", \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Task\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Instructions\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Due Date\\\", \\\"value\\\": \\\"{}\\\" }}\\n    ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code,\\n   task.name, task.owner_id if task.owner_id else \\\"-\\\", task.instructions.content.replace(\u0027\\\"\u0027, \\\"\u0027\\\") if task.instructions else \\\"-\\\", Date(task.due_date) if task.due_date else \\\"-\\\"\\n   )\\n\\ninputs.teams_payload = payload\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0q5lshb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1j9da45\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0q5lshb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17n68bf\"/\u003e\u003cendEvent id=\"EndEvent_1d26c7r\"\u003e\u003cincoming\u003eSequenceFlow_1j9da45\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1j9da45\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"EndEvent_1d26c7r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1q8nu40\"\u003e\u003ctext\u003eFormat teams_payload as a json object. See pre-processor script for format.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1925sdu\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"TextAnnotation_1q8nu40\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17n68bf\" id=\"ServiceTask_17n68bf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q5lshb\" id=\"SequenceFlow_0q5lshb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1d26c7r\" id=\"EndEvent_1d26c7r_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"415\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1j9da45\" id=\"SequenceFlow_1j9da45_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"415\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"383\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1q8nu40\" id=\"TextAnnotation_1q8nu40_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"185\" x=\"130\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1925sdu\" id=\"Association_1925sdu_di\"\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example of posting incident and task information to Teams as two sections",
      "export_key": "task_post_message_to_teams",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667559972937,
      "name": "Task: Post message to Teams",
      "object_type": "task",
      "programmatic_name": "task_post_message_to_teams",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "2500846e-793a-4f40-8945-004fd7a736b6",
      "workflow_id": 51
    },
    {
      "actions": [],
      "content": {
        "version": 35,
        "workflow_id": "incident_create_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_microsoft_group\" isExecutable=\"true\" name=\"Incident: Create a Microsoft Group\"\u003e\u003cdocumentation\u003eA sample workflow to create a MS Group from an incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rhfah8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xcbxw8\" name=\"MS Teams: Create group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"120d2055-a0de-413b-b5d7-444d289dd469\"\u003e{\"inputs\":{\"d2f9e887-fd44-4b64-98f8-a642b4b1738c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"AdminSoarMS@5rf2xs.onmicrosoft.com\"}},\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if task:\\n    inputs.task_id = task.id\\n  \\ninputs.incident_id = str(incident.id)\\ninputs.ms_group_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_group_name is None else rule.properties.ms_group_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_incident is not None:\\n  _value = rule.properties.add_members_incident.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_group_description.content is not None:\\n    inputs.ms_group_description = rule.properties.ms_group_description.content\\nelse:\\n    inputs.ms_group_description = f\\\"Incident {incident.id}: {incident.name} {incident.description}\\\"\\n  \\n\\nif rule.properties.ms_group_mail_nickname is not None:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rhfah8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19sx12p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_00djqtl\"\u003e\u003cincoming\u003eSequenceFlow_19sx12p\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_19sx12p\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"EndEvent_00djqtl\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0rhfah8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xcbxw8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17bn2hx\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: group_name, owners_list, members_list, group_description, group_mail_nickname\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14jwjkk\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"TextAnnotation_17bn2hx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0so7w7l\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Incident note with created group details\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1wzfeh6\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"TextAnnotation_0so7w7l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1cot0pb\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nzxqcp\" sourceRef=\"EndEvent_00djqtl\" targetRef=\"TextAnnotation_1cot0pb\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"145\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"140\" y=\"233\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"160\" x=\"88\" y=\"326\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"163\" xsi:type=\"omgdc:Point\" y=\"238\"/\u003e\u003comgdi:waypoint x=\"163\" xsi:type=\"omgdc:Point\" y=\"326\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xcbxw8\" id=\"ServiceTask_0xcbxw8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"381\" y=\"176\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_00djqtl\" id=\"EndEvent_00djqtl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"681\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"699\" y=\"237\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19sx12p\" id=\"SequenceFlow_19sx12p_di\"\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"681\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"581\" y=\"194\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rhfah8\" id=\"SequenceFlow_0rhfah8_di\"\u003e\u003comgdi:waypoint x=\"181\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"305\" y=\"209\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17bn2hx\" id=\"TextAnnotation_17bn2hx_di\"\u003e\u003comgdc:Bounds height=\"89\" width=\"176\" x=\"175\" y=\"19\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14jwjkk\" id=\"Association_14jwjkk_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"312\" xsi:type=\"omgdc:Point\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0so7w7l\" id=\"TextAnnotation_0so7w7l_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"129\" x=\"529\" y=\"34\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1wzfeh6\" id=\"Association_1wzfeh6_di\"\u003e\u003comgdi:waypoint x=\"472\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"562\" xsi:type=\"omgdc:Point\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1cot0pb\" id=\"TextAnnotation_1cot0pb_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"150\" x=\"624\" y=\"325\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nzxqcp\" id=\"Association_1nzxqcp_di\"\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"239\"/\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"325\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 35,
      "description": "A sample workflow to create a MS Group from an incident",
      "export_key": "incident_create_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667819206775,
      "name": "Incident: Create a Microsoft Group",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_microsoft_group",
      "tags": [],
      "uuid": "36c20e30-8577-4109-b019-2e8e280f5798",
      "workflow_id": 45
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "incident_delete_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_delete_a_microsoft_group\" isExecutable=\"true\" name=\"Incident: Delete a Microsoft Group\"\u003e\u003cdocumentation\u003eA sample workflow to delete a MS Group from within an Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_07l5bga\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tk0xvp\" name=\"MS Teams: Delete Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c710fb72-c934-45ce-9205-e36794fee376\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text = u\\\"\u0026lt;b\u0026gt;Microsoft Groups:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(content.get(\\\"message\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_group_mail_nickname:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\\nelif rule.properties.ms_group_name:\\n    inputs.ms_group_name = rule.properties.ms_group_name\\n\\nelse:\\n    helper.fail(\\\"Atleast one option must be specified to delete a group\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_07l5bga\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1q6a4wt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1eb2hkm\"\u003e\u003cincoming\u003eSequenceFlow_1q6a4wt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1q6a4wt\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"EndEvent_1eb2hkm\"/\u003e\u003csequenceFlow id=\"SequenceFlow_07l5bga\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tk0xvp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1se85ex\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: Group name or Mail nickname\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1p7fhja\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_1se85ex\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10kzg48\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1m6api6\" sourceRef=\"EndEvent_1eb2hkm\" targetRef=\"TextAnnotation_10kzg48\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_142txyo\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Incident Note with group name that was deleted\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0lc1nip\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_142txyo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"169\" x=\"95\" y=\"312\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"174\" xsi:type=\"omgdc:Point\" y=\"312\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tk0xvp\" id=\"ServiceTask_1tk0xvp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"363\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1eb2hkm\" id=\"EndEvent_1eb2hkm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"631\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"649\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1q6a4wt\" id=\"SequenceFlow_1q6a4wt_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"502\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07l5bga\" id=\"SequenceFlow_07l5bga_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"235.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1se85ex\" id=\"TextAnnotation_1se85ex_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"144\" x=\"108\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1p7fhja\" id=\"Association_1p7fhja_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"225\" xsi:type=\"omgdc:Point\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10kzg48\" id=\"TextAnnotation_10kzg48_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"143\" x=\"577\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1m6api6\" id=\"Association_1m6api6_di\"\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_142txyo\" id=\"TextAnnotation_142txyo_di\"\u003e\u003comgdc:Bounds height=\"83\" width=\"172\" x=\"563\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0lc1nip\" id=\"Association_0lc1nip_di\"\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"586\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "A sample workflow to delete a MS Group from within an Incident",
      "export_key": "incident_delete_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667566524134,
      "name": "Incident: Delete a Microsoft Group",
      "object_type": "incident",
      "programmatic_name": "incident_delete_a_microsoft_group",
      "tags": [],
      "uuid": "ca256b94-e3cb-4b3e-9595-12ab0f9607d9",
      "workflow_id": 52
    }
  ],
  "workspaces": []
}
