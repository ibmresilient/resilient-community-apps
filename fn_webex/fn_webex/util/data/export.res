{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create a Team with Room",
      "id": 23,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create a Team with Room",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "702ea905-d534-4c69-8ec9-f64948d00668",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "create_webex_team_with_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create Meeting",
      "id": 24,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create Meeting",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "af9ff0aa-d576-4f31-b4a1-3d5285628a34",
      "view_items": [
        {
          "content": "fa3356eb-b605-4281-a786-0baa02aec9ce",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "528de451-32db-41eb-818e-360d379ebf3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "222ce2a2-58c8-44ff-ad02-f53ffc7fb85c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8eb75601-5cf5-4661-9eb7-8c9606671fca",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46f5cd03-e633-4dc9-b541-35870569e526",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4e514df5-880e-4255-b9f3-8179cbdb2600",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e635549-f5f6-4817-ad48-a9f9c0beca7c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_webex_meeting"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create Room",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create Room",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bf0638d7-e0ef-44a4-a24c-e554557a8e1b",
      "view_items": [
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e71eb54e-afbf-4131-a6aa-2d7a5dcadc00",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_webex_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create task Meeting",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create task Meeting",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "aadde0fe-fb56-4d6d-9616-7b67bf592e53",
      "view_items": [
        {
          "content": "fa3356eb-b605-4281-a786-0baa02aec9ce",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "528de451-32db-41eb-818e-360d379ebf3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "222ce2a2-58c8-44ff-ad02-f53ffc7fb85c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8eb75601-5cf5-4661-9eb7-8c9606671fca",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46f5cd03-e633-4dc9-b541-35870569e526",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4e514df5-880e-4255-b9f3-8179cbdb2600",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e635549-f5f6-4817-ad48-a9f9c0beca7c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_webex_meeting"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create task Room",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create task Room",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bd69d04e-1666-42e8-ae4c-942845bfc049",
      "view_items": [
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e71eb54e-afbf-4131-a6aa-2d7a5dcadc00",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_webex_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create task Team",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create task Team",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2f734854-a0cf-4658-a08c-230da842947a",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_webex_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create task Team with Room",
      "id": 30,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create task Team with Room",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2d1fff55-6a83-4ce6-8d50-4083eec9622f",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_webex_team_with_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Create Team",
      "id": 22,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Create Team",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "902d5457-66f1-4c09-9c63-16c12049581a",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_webex_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Delete Room",
      "id": 26,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Delete Room",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e5129ccc-ee9c-42c1-86ef-227b52fd32ac",
      "view_items": [
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e96f60ad-7963-43fb-bb15-c4986d38c500",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_delete_a_webex_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Delete task Room",
      "id": 32,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Delete task Room",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "597485cf-c062-47f2-87b5-a38e222fe5fe",
      "view_items": [
        {
          "content": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e96f60ad-7963-43fb-bb15-c4986d38c500",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_delete_a_webex_room"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Delete task Team",
      "id": 33,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Delete task Team",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6a6bbbc4-fe0b-4ba4-ae9c-b74b5cf6a045",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e71eb54e-afbf-4131-a6aa-2d7a5dcadc00",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_delete_a_webex_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Webex: Delete Team",
      "id": 31,
      "logic_type": "all",
      "message_destinations": [
        "fn_webex"
      ],
      "name": "Webex: Delete Team",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "88b38df8-6583-477a-bf48-c9c6551e2d97",
      "view_items": [
        {
          "content": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e71eb54e-afbf-4131-a6aa-2d7a5dcadc00",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_delete_a_webex_team"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1663752542645,
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
      "export_key": "__function/webex_team_id",
      "hide_notification": false,
      "id": 294,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_team_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8dc95f18-ff66-4ac4-a29e-a35c7ad3730f",
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
      "export_key": "__function/webex_incident_id",
      "hide_notification": false,
      "id": 289,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Leave this field blank",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9aa23a09-3fd0-4f44-8932-729d1edff840",
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
      "export_key": "__function/webex_meeting_end_time",
      "hide_notification": false,
      "id": 281,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_end_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
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
      "export_key": "__function/webex_meeting_duration",
      "hide_notification": false,
      "id": 309,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_duration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "0 - 1439 (minutes)",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_duration",
      "tooltip": "Meeting duration. Taken into consideration only when the END-TIME is not specified.",
      "type_id": 11,
      "uuid": "ac4105e8-e49d-4822-a9e6-777e2bc6e87b",
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
      "export_key": "__function/webex_room_name",
      "hide_notification": false,
      "id": 290,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_room_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_room_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ae2a9043-96f5-4ab8-915c-52d898dfdd0b",
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
      "export_key": "__function/webex_send_email",
      "hide_notification": false,
      "id": 311,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "webex_send_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_send_email",
      "tooltip": "Send an invite to meeting attendees",
      "type_id": 11,
      "uuid": "bfed0c81-a924-44fa-b3be-401d77b69093",
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
      "export_key": "__function/webex_meeting_attendees",
      "hide_notification": false,
      "id": 286,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_attendees",
      "operation_perms": {},
      "operations": [],
      "placeholder": "If only specific members are to be added, specify their email addresses in a comma-separated manner and set add_all_members to NO",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_attendees",
      "tooltip": "The list of email address of the attendees in a space-seperated format. Leave blank to select all attendees",
      "type_id": 11,
      "uuid": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
      "export_key": "__function/webex_meeting_password",
      "hide_notification": false,
      "id": 278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "More than 4 characters",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_password",
      "tooltip": "Meeting password",
      "type_id": 11,
      "uuid": "03dd1531-acbb-4db8-9950-53520eabbb5c",
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
      "export_key": "__function/webex_task_id",
      "hide_notification": false,
      "id": 316,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "075307ab-25c7-44ef-9f4d-18184606cb24",
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
      "export_key": "__function/webex_add_all_members",
      "hide_notification": false,
      "id": 288,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "webex_add_all_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_add_all_members",
      "tooltip": "Select this option to add all members to the webex meeting. If only selected members are to be added, specify their email address below.",
      "type_id": 11,
      "uuid": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
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
      "export_key": "__function/webex_meeting_name",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_name",
      "tooltip": "Meeting name",
      "type_id": 11,
      "uuid": "14438dc7-4874-4971-9aa7-5596b13276a1",
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
      "export_key": "__function/webex_meeting_agenda",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_agenda",
      "tooltip": "Meeting agenda",
      "type_id": 11,
      "uuid": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
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
      "export_key": "__function/webex_meeting_start_time",
      "hide_notification": false,
      "id": 282,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_start_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5706ac62-97ee-4b54-9807-9f4b124ececc",
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
      "export_key": "__function/webex_room_id",
      "hide_notification": false,
      "id": 297,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_room_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_room_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5a0b1585-3dfc-48ce-882f-4313850cc445",
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
      "export_key": "__function/webex_team_name",
      "hide_notification": false,
      "id": 292,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_team_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6f5a8140-bebb-45a5-b639-6d581fc49f3e",
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
      "export_key": "actioninvocation/webex_send_email",
      "hide_notification": false,
      "id": 308,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "webex_send_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Send Invite?",
      "tooltip": "Send invite as email to attendees?",
      "type_id": 6,
      "uuid": "8eb75601-5cf5-4661-9eb7-8c9606671fca",
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
      "export_key": "actioninvocation/webex_meeting_end_time",
      "hide_notification": false,
      "id": 275,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Meeting End Time",
      "tooltip": "If this field is left blank, meeting will automatically end in 45 minutes from the start time",
      "type_id": 6,
      "uuid": "9e635549-f5f6-4817-ad48-a9f9c0beca7c",
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
      "export_key": "actioninvocation/webex_room_name",
      "hide_notification": false,
      "id": 291,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_room_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Room Name",
      "tooltip": "The name of the room to be created or deleted",
      "type_id": 6,
      "uuid": "a0e121d9-d4b6-4e5c-bfe3-fd52ec06d994",
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
      "export_key": "actioninvocation/webex_add_all_members",
      "hide_notification": false,
      "id": 287,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "webex_add_all_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Include all members",
      "tooltip": "Select to add all incident members to the team or room",
      "type_id": 6,
      "uuid": "c1b49aae-f8a6-4735-8a9f-007f7b8d6bb6",
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
      "export_key": "actioninvocation/webex_team_id",
      "hide_notification": false,
      "id": 295,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Team ID",
      "tooltip": "Specify any existing team id to add them to the Room",
      "type_id": 6,
      "uuid": "e71eb54e-afbf-4131-a6aa-2d7a5dcadc00",
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
      "export_key": "actioninvocation/webex_room_id",
      "hide_notification": false,
      "id": 298,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_room_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Room ID",
      "tooltip": "ID of the Room to be Deleted",
      "type_id": 6,
      "uuid": "e96f60ad-7963-43fb-bb15-c4986d38c500",
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
      "export_key": "actioninvocation/webex_meeting_attendees",
      "hide_notification": false,
      "id": 285,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_attendees",
      "operation_perms": {},
      "operations": [],
      "placeholder": "sara@example.com, mathew@example.com",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Additional attendees",
      "tooltip": "Specify any additional attendees",
      "type_id": 6,
      "uuid": "ef2d73b0-8610-4fbe-8243-bec9257c4a94",
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
      "export_key": "actioninvocation/webex_meeting_name",
      "hide_notification": false,
      "id": 296,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Meeting Name",
      "tooltip": "If this filed is left blank, the incident name will be set as the meeting name",
      "type_id": 6,
      "uuid": "fa3356eb-b605-4281-a786-0baa02aec9ce",
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
      "export_key": "actioninvocation/webex_meeting_agenda",
      "hide_notification": false,
      "id": 274,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Agenda",
      "tooltip": "",
      "type_id": 6,
      "uuid": "222ce2a2-58c8-44ff-ad02-f53ffc7fb85c",
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
      "export_key": "actioninvocation/webex_team_name",
      "hide_notification": false,
      "id": 293,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Team Name",
      "tooltip": "Name of the team that is being created",
      "type_id": 6,
      "uuid": "26d1dd80-a2a3-4a43-96d9-f95a530e76a0",
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
      "export_key": "actioninvocation/webex_meeting_duration",
      "hide_notification": false,
      "id": 310,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_duration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "0 - 1439 (minutes)",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Duration",
      "tooltip": "Meeting duration in minutes. Taken into consideration only when the END_TIME is not specified.",
      "type_id": 6,
      "uuid": "46f5cd03-e633-4dc9-b541-35870569e526",
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
      "export_key": "actioninvocation/webex_meeting_start_time",
      "hide_notification": false,
      "id": 276,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Meeting Start Time",
      "tooltip": "If this field is left blank, meeting will be set to start immediately",
      "type_id": 6,
      "uuid": "4e514df5-880e-4255-b9f3-8179cbdb2600",
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
      "export_key": "actioninvocation/webex_meeting_password",
      "hide_notification": false,
      "id": 277,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Password",
      "tooltip": "",
      "type_id": 6,
      "uuid": "528de451-32db-41eb-818e-360d379ebf3a",
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
      "created_date": 1659727541157,
      "description": {
        "content": "Function to create meetings from an incident or task",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Meeting",
      "export_key": "webex_create_meeting",
      "id": 4,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1663680705725,
      "name": "webex_create_meeting",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"7abca37c1c124cb2a4e74661f4a8c47e\", \"meetingNumber\": \"25967357926\", \"title\": \"Soar Sample Instant Meeting\", \"agenda\": \"Testing the application\", \"password\": \"abcd12345\", \"phoneAndVideoSystemPassword\": \"22231234\", \"meetingType\": \"meetingSeries\", \"state\": \"active\", \"timezone\": \"UTC\", \"start\": \"2022-08-11T13:33:00Z\", \"end\": \"2022-08-11T14:18:00Z\", \"hostUserId\": \"Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODM0YjBlYi1mZmY1LTRjY2YtYTcwOC04Nzk1YmFjYjQ3NzU\", \"hostDisplayName\": \"admin@examples-5xth.wbx.ai\", \"hostEmail\": \"admin@examples-5xth.wbx.ai\", \"hostKey\": \"109420\", \"siteUrl\": \"examples-5xth.webex.com\", \"webLink\": \"https://examples-5xth.webex.com/examples-5xth/j.php?MTID=m4a809400de110cbedaa89ff5e55b3d73\", \"sipAddress\": \"25967357926@examples-5xth.webex.com\", \"dialInIpAddress\": \"173.243.2.68\", \"enabledAutoRecordMeeting\": \"false\", \"allowAnyUserToBeCoHost\": \"false\", \"allowFirstUserToBeCoHost\": \"false\", \"allowAuthenticatedDevices\": \"true\", \"enabledJoinBeforeHost\": \"false\", \"joinBeforeHostMinutes\": \"0\", \"enableConnectAudioBeforeHost\": \"false\", \"excludePassword\": \"false\", \"publicMeeting\": \"false\", \"enableAutomaticLock\": \"false\", \"unlockedMeetingJoinSecurity\": \"allowJoin\", \"telephony\": \"accessCode:25967357926\", \"callInNumbers\": \"label:United States Toll\", \"callInNumber\": \"+1-000-000-0000\", \"tollType\": \"toll\", \"links\": \"rel:globalCallinNumbers\", \"href\": \"/v1/meetings/7abca37c1c124cb2a4e74661f4a8c47e/globalCallinNumbers\", \"method\": \"GET\", \"meetingOptions\": \"enabledChat:true\", \"enabledVideo\": \"true\", \"enabledPolling\": \"false\", \"enabledNote\": \"true\", \"noteType\": \"allowAll\", \"enabledClosedCaptions\": \"false\", \"enabledFileTransfer\": \"true\", \"enabledUCFRichMedia\": \"true\", \"sessionTypeId\": \"3\", \"scheduledType\": \"meeting\", \"simultaneousInterpretation\": \"enabled:false\", \"enabledBreakoutSessions\": \"false\", \"status\": true}, \"raw\": null, \"inputs\": {\"webex_meeting_name\": \"Soar Sample Instant Meeting\", \"webex_meeting_password\": \"abcd12345\", \"webex_meeting_agenda\": \"Testing the application\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-webex\", \"package_version\": \"2.0.0\", \"host\": \"AppHost\", \"execution_time_ms\": 5448, \"timestamp\": \"2022-08-11 13:31:40\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {\"type\": \"string\"}, \"content\": {\"type\": \"object\", \"properties\": {\"message\": {\"type\": \"string\"}, \"errors\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"description\": {\"type\": \"string\"}}}}, \"trackingId\": {\"type\": \"string\"}, \"status_code\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"webex_meeting_name\": {\"type\": \"string\"}, \"webex_meeting_password\": {\"type\": \"string\"}, \"webex_send_email\": {\"type\": \"boolean\"}, \"webex_meeting_start_time\": {}, \"webex_meeting_agenda\": {\"type\": \"string\"}, \"webex_meeting_duration\": {\"type\": \"integer\"}, \"webex_meeting_end_time\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "674a0970-dab8-4bd1-8e67-4ac8d5068b38",
      "version": 38,
      "view_items": [
        {
          "content": "14438dc7-4874-4971-9aa7-5596b13276a1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03dd1531-acbb-4db8-9950-53520eabbb5c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bfed0c81-a924-44fa-b3be-401d77b69093",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ac4105e8-e49d-4822-a9e6-777e2bc6e87b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5706ac62-97ee-4b54-9807-9f4b124ececc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
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
          "name": "Incident: Create a Webex Meeting",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_webex_meeting",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 20
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Webex Meeting",
          "object_type": "task",
          "programmatic_name": "task_create_a_webex_meeting",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 24
        }
      ]
    },
    {
      "created_date": 1656947489905,
      "description": {
        "content": "Function to create a room from a meeting or task",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Room",
      "export_key": "webex_create_room",
      "id": 2,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1663680705765,
      "name": "webex_create_room",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"roomId\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmU4ZjFmNTAtMWEwMy0xMWVkLWJiZDktMzcwMDcyNTIyMGJl\", \"meetingLink\": \"https://examples-5xth.webex.com/m/a9a09646-9c84-4c9b-92f3-142faa4598ba\", \"sipAddress\": \"25923177804@examples-5xth.webex.com\", \"meetingNumber\": \"25923177804\", \"meetingId\": \"725c8064c775432fb85ea16d7b7c85c7\", \"callInTollFreeNumber\": \"\", \"callInTollNumber\": \"+1-650-479-3208\", \"attendees\": \"\", \"status\": true, \"roomName\": \"Incident Room\"}, \"raw\": null, \"inputs\": {\"webex_incident_id\": \"2096\", \"webex_room_name\": \"Incident room\", \"webex_add_all_members\": false, \"webex_team_id\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1RFQU0vZmU4ZjFmNTAtMWEwMy0xMWVkLWJiZDktMzcwMDcyNTIyMGJl\", \"webex_meeting_attendees\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-webex\", \"package_version\": \"2.0.0\", \"host\": \"AppHost\", \"execution_time_ms\": 9591, \"timestamp\": \"2022-08-12 07:00:17\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"roomId\": {\"type\": \"string\"}, \"meetingLink\": {\"type\": \"string\"}, \"sipAddress\": {\"type\": \"string\"}, \"meetingNumber\": {\"type\": \"string\"}, \"meetingId\": {\"type\": \"string\"}, \"callInTollFreeNumber\": {\"type\": \"string\"}, \"callInTollNumber\": {\"type\": \"string\"}, \"status_code\": {\"type\": \"integer\"}, \"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"attendees\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"webex_incident_id\": {\"type\": \"string\"}, \"webex_room_name\": {\"type\": \"string\"}, \"webex_task_id\": {\"type\": \"string\"}, \"webex_add_all_members\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "ab9bd63a-728e-4c80-aa36-27e288813c34",
      "version": 83,
      "view_items": [
        {
          "content": "075307ab-25c7-44ef-9f4d-18184606cb24",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9aa23a09-3fd0-4f44-8932-729d1edff840",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8dc95f18-ff66-4ac4-a29e-a35c7ad3730f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae2a9043-96f5-4ab8-915c-52d898dfdd0b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
          "name": "Incident: Create a Webex Room",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_webex_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 21
        },
        {
          "actions": [],
          "description": null,
          "name": "Incident: Create a Webex Team with Room",
          "object_type": "incident",
          "programmatic_name": "create_webex_team_with_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 7
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Webex Room",
          "object_type": "task",
          "programmatic_name": "task_create_a_webex_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 16
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Webex Team with Room",
          "object_type": "task",
          "programmatic_name": "task_create_a_webex_team_with_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1659727464787,
      "description": {
        "content": "Function to create a Webex team from an incident or task",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Team",
      "export_key": "webex_create_team",
      "id": 3,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1663680705806,
      "name": "webex_create_team",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1RFQU0vZmU4ZjFmNTAtMWEwMy0xMWVkLWJiZDktMzcwMDcyNTIyMGJl\", \"name\": \"Incident room\", \"creatorId\": \"Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODM0YjBlYi1mZmY1LTRjY2YtYTcwOC04Nzk1YmFjYjQ3NzU\", \"created\": \"2022-08-12T05:59:57.637Z\", \"attendees\": \"c.example9+soar1@nuigalway.ie, c.example9+soar2@nuigalway.ie, c.example9+soar3@nuigalway.ie, c.example9+soar4@nuigalway.ie, c.example9+soar5@nuigalway.ie\", \"status\": true}, \"raw\": null, \"inputs\": {\"webex_team_name\": \"Incident room\", \"webex_incident_id\": \"2096\", \"webex_add_all_members\": true}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-webex\", \"package_version\": \"2.0.0\", \"host\": \"Apphost\", \"execution_time_ms\": 13623, \"timestamp\": \"2022-08-12 07:00:05\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {\"type\": \"string\"}, \"content\": {}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"webex_team_name\": {\"type\": \"string\"}, \"webex_incident_id\": {\"type\": \"string\"}, \"webex_task_id\": {\"type\": \"string\"}, \"webex_add_all_members\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "7e202188-beda-403c-b0e8-0b626c201382",
      "version": 35,
      "view_items": [
        {
          "content": "075307ab-25c7-44ef-9f4d-18184606cb24",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9aa23a09-3fd0-4f44-8932-729d1edff840",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6f5a8140-bebb-45a5-b639-6d581fc49f3e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
          "name": "Incident: Create a Webex Team",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_webex_team",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 22
        },
        {
          "actions": [],
          "description": null,
          "name": "Incident: Create a Webex Team with Room",
          "object_type": "incident",
          "programmatic_name": "create_webex_team_with_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 7
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Webex Team",
          "object_type": "task",
          "programmatic_name": "task_create_a_webex_team",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 17
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Webex Team with Room",
          "object_type": "task",
          "programmatic_name": "task_create_a_webex_team_with_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1663582253801,
      "description": {
        "content": "Function to delete a Webex Room from an incident or task",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Delete Room",
      "export_key": "webex_delete_room",
      "id": 7,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1663680705845,
      "name": "webex_delete_room",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"status_code\": 204, \"message\": \"Successfully deleted room : Incident 2096 Task 102: Webex Initial Test\"}, \"raw\": null, \"inputs\": {\"webex_room_name\": \"Incident 2096 Task 102: Webex Initial Test\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-webex\", \"package_version\": \"2.0.0\", \"host\": \"Calvins-MacBook-Pro.local\", \"execution_time_ms\": 3383, \"timestamp\": \"2022-09-19 11:29:54\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"status_code\": {\"type\": \"integer\"}, \"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"webex_room_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "62cc9b38-ac80-4dfd-8a2f-ddef3044b85b",
      "version": 7,
      "view_items": [
        {
          "content": "ae2a9043-96f5-4ab8-915c-52d898dfdd0b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5a0b1585-3dfc-48ce-882f-4313850cc445",
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
          "name": "Incident: Delete a Webex Room",
          "object_type": "incident",
          "programmatic_name": "incident_delete_a_webex_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 23
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Delete a Webex Room",
          "object_type": "task",
          "programmatic_name": "task_delete_a_webex_room",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 25
        }
      ]
    },
    {
      "created_date": 1661773747157,
      "description": {
        "content": "Function to delete a Webex team from an incident or task",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Delete Team",
      "export_key": "webex_delete_team",
      "id": 6,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1663680705886,
      "name": "webex_delete_team",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"status_code\": 204, \"message\": \"Successfully deleted team : Incident 2096 task 102: Webex Initial Test\"}, \"raw\": null, \"inputs\": {\"webex_team_name\": \"Incident 2096 task 102: Webex Initial Test\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-webex\", \"package_version\": \"2.0.0\", \"host\": \"Calvins-MacBook-Pro.local\", \"execution_time_ms\": 4362, \"timestamp\": \"2022-09-19 11:31:16\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"status_code\": {\"type\": \"integer\"}, \"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"webex_team_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "74619406-5f6f-4a10-b934-9445ec95e98c",
      "version": 22,
      "view_items": [
        {
          "content": "6f5a8140-bebb-45a5-b639-6d581fc49f3e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8dc95f18-ff66-4ac4-a29e-a35c7ad3730f",
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
          "name": "Incident: Delete a Webex Team",
          "object_type": "incident",
          "programmatic_name": "incident_delete_a_webex_team",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 19
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Delete a Webex Team",
          "object_type": "task",
          "programmatic_name": "task_delete_a_webex_team",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 27
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 75,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1663752540333,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1663752540333,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "62990bb9-d5c8-4eb0-be98-f17aacd4c95c",
        "e14b8f3e-6652-408c-8abf-448093f7f4ea"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_webex",
      "name": "fn_webex",
      "programmatic_name": "fn_webex",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "users": [
        "admin@example.com"
      ],
      "uuid": "7fc77005-9552-4cbe-90c6-d9b6037c937c"
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
        "version": 11,
        "workflow_id": "task_create_a_webex_meeting",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_webex_meeting\" isExecutable=\"true\" name=\"Task: Create a Webex Meeting\"\u003e\u003cdocumentation\u003eA sample workflow to create a meeting form a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14rpa0x\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q0w8js\" name=\"Webex: Create Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"674a0970-dab8-4bd1-8e67-4ac8d5068b38\"\u003e{\"inputs\":{\"bfed0c81-a924-44fa-b3be-401d77b69093\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}},\"ac4105e8-e49d-4822-a9e6-777e2bc6e87b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":45}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Cisco WebEx Meeting\\\"\\n\\n  if results.reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, results.reason)\\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"webLink\\\"))\\n\\n  text = u\\\"\u0026lt;b\u0026gt;Cisco Webex Meeting:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;Webex Room URL: {0}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting Name: {}\\\".format(content.get(\\\"title\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Password: {}\\\".format(content.get(\\\"password\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Agenda: {}\\\".format(content.get(\\\"agenda\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Start Time: {}\\\".format(content.get(\\\"start\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;End Time: {}\\\".format(content.get(\\\"end\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Timezone: {}\\\".format(content.get(\\\"timezone\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting Id: {}\\\".format(content.get(\\\"id\\\"))\\n  \\nnote = helper.createRichText(text)\\ntask.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_meeting_name = incident.name if rule.properties.webex_meeting_name is None else rule.properties.webex_meeting_name\\n\\nif rule.properties.webex_meeting_start_time:\\n  inputs.webex_meeting_start_time = rule.properties.webex_meeting_start_time      \\nelse:\\n  inputs.webex_meeting_start_time = None\\n\\nif rule.properties.webex_meeting_end_time:\\n  inputs.webex_meeting_end_time = rule.properties.webex_meeting_end_time      \\nelse:\\n  inputs.webex_meeting_end_time = None\\n  \\nif rule.properties.webex_send_email is not None:\\n  inputs.webex_send_email = rule.properties.webex_send_email\\n\\nif rule.properties.webex_meeting_duration:\\n  inputs.webex_meeting_duration = rule.properties.webex_meeting_duration\\n  \\n# Get the agenda from the activity field or the incident description\\nif rule.properties.webex_meeting_agenda is None:\\n  if incident.description is not None and incident.description.content is not None:\\n    inputs.webex_meeting_agenda = incident.description.content\\n  else:\\n    inputs.webex_meeting_agenda = \\\"\\\"\\nelse:\\n  inputs.webex_meeting_agenda = rule.properties.webex_meeting_agenda\\n\\ninputs.webex_meeting_password = inputs.webex_meeting_password if rule.properties.webex_meeting_password is None else rule.properties.webex_meeting_password\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14rpa0x\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1cdkwgt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1h8neod\"\u003e\u003cincoming\u003eSequenceFlow_1cdkwgt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1cdkwgt\" sourceRef=\"ServiceTask_0q0w8js\" targetRef=\"EndEvent_1h8neod\"/\u003e\u003csequenceFlow id=\"SequenceFlow_14rpa0x\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q0w8js\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_03d6c2e\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0lpyqat\" sourceRef=\"EndEvent_1h8neod\" targetRef=\"TextAnnotation_03d6c2e\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1iwx7tc\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\u00a0webex_meeting_name, webex_meeting_agenda, webex_meeting_password, webex_meeting_duration, webex_meeting_start_time, webex_end_time\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0qrioxx\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1iwx7tc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19rojp4\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs: Meeting_URL, Name, Password,\u00a0 Agenda, Start_Time, End_Time, Timezone, MeetingID\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0p6s0pn\" sourceRef=\"EndEvent_1h8neod\" targetRef=\"TextAnnotation_19rojp4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"332\" y=\"152\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"327\" y=\"187\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"174\" x=\"263\" y=\"266\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"345\" xsi:type=\"omgdc:Point\" y=\"266\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q0w8js\" id=\"ServiceTask_0q0w8js_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"583\" y=\"130\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1h8neod\" id=\"EndEvent_1h8neod_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"915\" y=\"152\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"933\" y=\"191\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cdkwgt\" id=\"SequenceFlow_1cdkwgt_di\"\u003e\u003comgdi:waypoint x=\"683\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"915\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"799\" y=\"148\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14rpa0x\" id=\"SequenceFlow_14rpa0x_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"583\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"475.5\" y=\"148\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_03d6c2e\" id=\"TextAnnotation_03d6c2e_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"140\" x=\"863\" y=\"266\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0lpyqat\" id=\"Association_0lpyqat_di\"\u003e\u003comgdi:waypoint x=\"933\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"933\" xsi:type=\"omgdc:Point\" y=\"266\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1iwx7tc\" id=\"TextAnnotation_1iwx7tc_di\"\u003e\u003comgdc:Bounds height=\"134\" width=\"168\" x=\"266\" y=\"-77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0qrioxx\" id=\"Association_0qrioxx_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"152\"/\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"57\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19rojp4\" id=\"TextAnnotation_19rojp4_di\"\u003e\u003comgdc:Bounds height=\"111\" width=\"123\" x=\"871\" y=\"-66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0p6s0pn\" id=\"Association_0p6s0pn_di\"\u003e\u003comgdi:waypoint x=\"933\" xsi:type=\"omgdc:Point\" y=\"152\"/\u003e\u003comgdi:waypoint x=\"934\" xsi:type=\"omgdc:Point\" y=\"45\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "description": "A sample workflow to create a meeting form a task",
      "export_key": "task_create_a_webex_meeting",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663752524838,
      "name": "Task: Create a Webex Meeting",
      "object_type": "task",
      "programmatic_name": "task_create_a_webex_meeting",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "af95b087-b5e6-4e24-b325-76b1943e2377",
      "workflow_id": 24
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "task_delete_a_webex_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_delete_a_webex_room\" isExecutable=\"true\" name=\"Task: Delete a Webex Room\"\u003e\u003cdocumentation\u003eA sample workflow to delete a Webex Room form task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16i9eut\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_01ea82x\" name=\"Webex: Delete Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"62cc9b38-ac80-4dfd-8a2f-ddef3044b85b\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete the room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += content.get(\\\"message\\\")\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.webex_room_id:\\n  inputs.webex_room_id = rule.properties.webex_room_id\\n\\nif rule.properties.webex_room_name:\\n  inputs.webex_room_name = rule.properties.webex_room_name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16i9eut\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_07toz64\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16i9eut\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01ea82x\"/\u003e\u003cendEvent id=\"EndEvent_0rte35y\"\u003e\u003cincoming\u003eSequenceFlow_07toz64\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_07toz64\" sourceRef=\"ServiceTask_01ea82x\" targetRef=\"EndEvent_0rte35y\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_000r45b\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wpsse2\" sourceRef=\"EndEvent_0rte35y\" targetRef=\"TextAnnotation_000r45b\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1vr08p9\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: Room_name, Room_Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0eg9jem\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1vr08p9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0vylcrz\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Confirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1g5l09e\" sourceRef=\"EndEvent_0rte35y\" targetRef=\"TextAnnotation_0vylcrz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"360\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"355\" y=\"213\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"165\" x=\"295\" y=\"282\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"213\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"282\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01ea82x\" id=\"ServiceTask_01ea82x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"529\" y=\"156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16i9eut\" id=\"SequenceFlow_16i9eut_di\"\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"529\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"462.5\" y=\"174\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0rte35y\" id=\"EndEvent_0rte35y_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"763\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"781\" y=\"217\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07toz64\" id=\"SequenceFlow_07toz64_di\"\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"763\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"174.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_000r45b\" id=\"TextAnnotation_000r45b_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"143\" x=\"709\" y=\"281\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wpsse2\" id=\"Association_0wpsse2_di\"\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"214\"/\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"281\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1vr08p9\" id=\"TextAnnotation_1vr08p9_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"104\" x=\"326\" y=\"46\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0eg9jem\" id=\"Association_0eg9jem_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"105\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0vylcrz\" id=\"TextAnnotation_0vylcrz_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"102\" x=\"730\" y=\"51\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1g5l09e\" id=\"Association_1g5l09e_di\"\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "description": "A sample workflow to delete a Webex Room form task",
      "export_key": "task_delete_a_webex_room",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680707134,
      "name": "Task: Delete a Webex Room",
      "object_type": "task",
      "programmatic_name": "task_delete_a_webex_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "a50fad32-ae4c-4055-944f-8d0825072a6e",
      "workflow_id": 25
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "incident_create_a_webex_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_webex_room\" isExecutable=\"true\" name=\"Incident: Create a Webex Room\"\u003e\u003cdocumentation\u003eA sample workflow to create rooms\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0xrnhdd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0nf3pfi\" name=\"Webex: Create Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ab9bd63a-728e-4c80-aa36-27e288813c34\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create a Webex Room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"meetingLink\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Room Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting link: {}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Room ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting ID: {}\\\".format(content.get(\\\"meetingId\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in Toll Number: {}\\\".format(content.get(\\\"callInTollNumber\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in TollFree Number: {}\\\".format(content.get(\\\"callInTollFreeNumber\\\", \\\"-\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_room_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.webex_room_name is None else rule.properties.webex_room_name\\n\\nif rule.properties.webex_team_id:\\n    inputs.webex_team_id = rule.properties.webex_team_id\\n    \\nif rule.properties.webex_meeting_attendees:\\n    if rule.properties.webex_meeting_attendees.content:\\n      inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n    inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xrnhdd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1rm1n1a\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xrnhdd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nf3pfi\"/\u003e\u003cendEvent id=\"EndEvent_0tlaazw\"\u003e\u003cincoming\u003eSequenceFlow_1rm1n1a\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1rm1n1a\" sourceRef=\"ServiceTask_0nf3pfi\" targetRef=\"EndEvent_0tlaazw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1t9bd21\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow end here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1jhqo7y\" sourceRef=\"EndEvent_0tlaazw\" targetRef=\"TextAnnotation_1t9bd21\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0dlefs5\"\u003e\u003ctext\u003eInputs: Room_Name, Team_ID, Include_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_09v2g4e\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_0dlefs5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ybp2pe\"\u003e\u003ctext\u003eOutput: Room_Name, URL, Meeting_ID, Created_Time, Call_in_TollNumber\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17wsr0v\" sourceRef=\"EndEvent_0tlaazw\" targetRef=\"TextAnnotation_1ybp2pe\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"151\" x=\"104\" y=\"263\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"263\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nf3pfi\" id=\"ServiceTask_0nf3pfi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xrnhdd\" id=\"SequenceFlow_0xrnhdd_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"276.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tlaazw\" id=\"EndEvent_0tlaazw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"632.807821982468\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"650.807821982468\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rm1n1a\" id=\"SequenceFlow_1rm1n1a_di\"\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"633\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"544\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1t9bd21\" id=\"TextAnnotation_1t9bd21_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"128\" x=\"587\" y=\"263\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1jhqo7y\" id=\"Association_1jhqo7y_di\"\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"652\" xsi:type=\"omgdc:Point\" y=\"263\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0dlefs5\" id=\"TextAnnotation_0dlefs5_di\"\u003e\u003comgdc:Bounds height=\"107\" width=\"140\" x=\"110\" y=\"26\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_09v2g4e\" id=\"Association_09v2g4e_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"181\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ybp2pe\" id=\"TextAnnotation_1ybp2pe_di\"\u003e\u003comgdc:Bounds height=\"113\" width=\"130\" x=\"586\" y=\"23\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17wsr0v\" id=\"Association_17wsr0v_di\"\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "description": "A sample workflow to create rooms",
      "export_key": "incident_create_a_webex_room",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706989,
      "name": "Incident: Create a Webex Room",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_webex_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "c77a46f7-b467-4aad-bb5e-b60cc0b58695",
      "workflow_id": 21
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "incident_create_a_webex_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_webex_team\" isExecutable=\"true\" name=\"Incident: Create a Webex Team\"\u003e\u003cdocumentation\u003eA sample workflow to create teams\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t8tdhk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0sxwkke\" name=\"Webex: Create Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e202188-beda-403c-b0e8-0b626c201382\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Webex Team\\\"\\n\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created Time: {}\\\".format(content.get(\\\"created\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Members: {}\\\".format(content.get(\\\"attendees\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.webex_team_name is None else rule.properties.webex_team_name\\n\\nif rule.properties.webex_meeting_attendees:\\n  if rule.properties.webex_meeting_attendees.content:\\n    inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n  inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t8tdhk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gh5jts\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0y8nmq1\"\u003e\u003cincoming\u003eSequenceFlow_1gh5jts\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t8tdhk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0sxwkke\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1gh5jts\" sourceRef=\"ServiceTask_0sxwkke\" targetRef=\"EndEvent_0y8nmq1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1n5b88u\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1mhgbw1\" sourceRef=\"EndEvent_0y8nmq1\" targetRef=\"TextAnnotation_1n5b88u\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1srei1q\"\u003e\u003ctext\u003eInputs: Team_name, Include_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1kxml3z\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1srei1q\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bd3lig\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Team_name, Created_time, Team_id, Team_members\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_025ruwe\" sourceRef=\"EndEvent_0y8nmq1\" targetRef=\"TextAnnotation_0bd3lig\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"433\" y=\"161\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"428\" y=\"196\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"160\" x=\"371\" y=\"258\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"446\" xsi:type=\"omgdc:Point\" y=\"258\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0sxwkke\" id=\"ServiceTask_0sxwkke_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"652\" y=\"139\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y8nmq1\" id=\"EndEvent_0y8nmq1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"927\" y=\"161\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"945\" y=\"200\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t8tdhk\" id=\"SequenceFlow_1t8tdhk_di\"\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003comgdi:waypoint x=\"652\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"515.5\" y=\"157\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gh5jts\" id=\"SequenceFlow_1gh5jts_di\"\u003e\u003comgdi:waypoint x=\"752\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003comgdi:waypoint x=\"927\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"794.5\" y=\"157\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1n5b88u\" id=\"TextAnnotation_1n5b88u_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"147\" x=\"871\" y=\"260\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1mhgbw1\" id=\"Association_1mhgbw1_di\"\u003e\u003comgdi:waypoint x=\"944\" xsi:type=\"omgdc:Point\" y=\"197\"/\u003e\u003comgdi:waypoint x=\"946\" xsi:type=\"omgdc:Point\" y=\"260\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1srei1q\" id=\"TextAnnotation_1srei1q_di\"\u003e\u003comgdc:Bounds height=\"109\" width=\"135\" x=\"383\" y=\"-5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1kxml3z\" id=\"Association_1kxml3z_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"161\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bd3lig\" id=\"TextAnnotation_0bd3lig_di\"\u003e\u003comgdc:Bounds height=\"111\" width=\"111\" x=\"889\" y=\"-6\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_025ruwe\" id=\"Association_025ruwe_di\"\u003e\u003comgdi:waypoint x=\"945\" xsi:type=\"omgdc:Point\" y=\"161\"/\u003e\u003comgdi:waypoint x=\"945\" xsi:type=\"omgdc:Point\" y=\"105\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "A sample workflow to create teams",
      "export_key": "incident_create_a_webex_team",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706740,
      "name": "Incident: Create a Webex Team",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_webex_team",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "32ef7a27-0c5d-455b-8abc-617879dccbc0",
      "workflow_id": 22
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "task_create_a_webex_team_with_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_webex_team_with_room\" isExecutable=\"true\" name=\"Task: Create a Webex Team with Room\"\u003e\u003cdocumentation\u003eA sample workflow to create a Webex team and assign a room to the team from a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ecp17w\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1r7pmch\" name=\"Webex: Create Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e202188-beda-403c-b0e8-0b626c201382\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Webex Team\\\"\\n\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n\\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created Time: {}\\\".format(content.get(\\\"created\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Members: {}\\\".format(content.get(\\\"attendees\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\nif task:\\n  inputs.webex_task_id = str(task.id)\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.webex_team_name is None else rule.properties.webex_team_name\\n\\nif rule.properties.webex_meeting_attendees:\\n  if rule.properties.webex_meeting_attendees.content:\\n    inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n  inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"team\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ecp17w\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mttq3c\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_0hp8mlw\" name=\"Webex: Create Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ab9bd63a-728e-4c80-aa36-27e288813c34\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create a Webex Room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"meetingLink\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Room Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting link: {}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Room ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting ID: {}\\\".format(content.get(\\\"meetingId\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in Toll Number: {}\\\".format(content.get(\\\"callInTollNumber\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in TollFree Number: {}\\\".format(content.get(\\\"callInTollFreeNumber\\\", \\\"-\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\nif task:\\n  inputs.webex_task_id = str(task.id)\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_room_name = rule.properties.webex_room_name if rule.properties.webex_room_name else \\\" \\\".join([workflow.properties.team.get(\\\"content\\\").get(\\\"name\\\"), \\\"Room\\\"])\\ninputs.webex_team_id = workflow.properties.team.get(\\\"content\\\").get(\\\"id\\\")\\ninputs.webex_meeting_attendees = None\\ninputs.webex_add_all_members = False\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mttq3c\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_09s2yql\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0wzbcud\"\u003e\u003cincoming\u003eSequenceFlow_09s2yql\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ecp17w\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1r7pmch\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1mttq3c\" sourceRef=\"ServiceTask_1r7pmch\" targetRef=\"ServiceTask_0hp8mlw\"/\u003e\u003csequenceFlow id=\"SequenceFlow_09s2yql\" sourceRef=\"ServiceTask_0hp8mlw\" targetRef=\"EndEvent_0wzbcud\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mrndlm\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hka3t2\" sourceRef=\"EndEvent_0wzbcud\" targetRef=\"TextAnnotation_1mrndlm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0pj0nqd\"\u003e\u003ctext\u003eInputs: Team_Name, Room_Name, Add_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1m7844g\" sourceRef=\"ServiceTask_1r7pmch\" targetRef=\"TextAnnotation_0pj0nqd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1h62xt7\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Note with Team details\u00a0 Room details, Note with Room details\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17ud7rq\" sourceRef=\"ServiceTask_0hp8mlw\" targetRef=\"TextAnnotation_1h62xt7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"190\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"185\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"172\" x=\"122\" y=\"292\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"208\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"208\" xsi:type=\"omgdc:Point\" y=\"292\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1r7pmch\" id=\"ServiceTask_1r7pmch_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"344\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0hp8mlw\" id=\"ServiceTask_0hp8mlw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"544\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wzbcud\" id=\"EndEvent_0wzbcud_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"789\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"807\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ecp17w\" id=\"SequenceFlow_1ecp17w_di\"\u003e\u003comgdi:waypoint x=\"226\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"285\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mttq3c\" id=\"SequenceFlow_1mttq3c_di\"\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"494\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09s2yql\" id=\"SequenceFlow_09s2yql_di\"\u003e\u003comgdi:waypoint x=\"644\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"789\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"716.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mrndlm\" id=\"TextAnnotation_1mrndlm_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"168\" x=\"723\" y=\"295\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hka3t2\" id=\"Association_0hka3t2_di\"\u003e\u003comgdi:waypoint x=\"807\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"808\" xsi:type=\"omgdc:Point\" y=\"295\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0pj0nqd\" id=\"TextAnnotation_0pj0nqd_di\"\u003e\u003comgdc:Bounds height=\"91\" width=\"136\" x=\"152\" y=\"2\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1m7844g\" id=\"Association_1m7844g_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1h62xt7\" id=\"TextAnnotation_1h62xt7_di\"\u003e\u003comgdc:Bounds height=\"96\" width=\"134\" x=\"740\" y=\"0\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17ud7rq\" id=\"Association_17ud7rq_di\"\u003e\u003comgdi:waypoint x=\"640\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"743\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "description": "A sample workflow to create a Webex team and assign a room to the team from a task",
      "export_key": "task_create_a_webex_team_with_room",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680707410,
      "name": "Task: Create a Webex Team with Room",
      "object_type": "task",
      "programmatic_name": "task_create_a_webex_team_with_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "626b74ca-430d-4620-9c67-dcf00a6b861e",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "incident_delete_a_webex_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_delete_a_webex_team\" isExecutable=\"true\" name=\"Incident: Delete a Webex Team\"\u003e\u003cdocumentation\u003eA sample workflow to delete a team from an incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12v0zri\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0amp70f\" name=\"Webex: Delete Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74619406-5f6f-4a10-b934-9445ec95e98c\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete the team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += content.get(\\\"message\\\")\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.webex_team_id:\\n  inputs.webex_team_id = rule.properties.webex_team_id\\n\\nif rule.properties.webex_team_name:\\n  inputs.webex_team_name = rule.properties.webex_team_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12v0zri\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06vnb8g\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1qbr1ye\"\u003e\u003cincoming\u003eSequenceFlow_06vnb8g\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_12v0zri\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0amp70f\"/\u003e\u003csequenceFlow id=\"SequenceFlow_06vnb8g\" sourceRef=\"ServiceTask_0amp70f\" targetRef=\"EndEvent_1qbr1ye\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1gottij\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: Team_name, Team_id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_16cnpze\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1gottij\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04i0tx5\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14p4ckj\" sourceRef=\"EndEvent_1qbr1ye\" targetRef=\"TextAnnotation_04i0tx5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0nnempg\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Confirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1mhhx8z\" sourceRef=\"EndEvent_1qbr1ye\" targetRef=\"TextAnnotation_0nnempg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"235\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"230\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"147\" x=\"179\" y=\"281\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"248\" xsi:type=\"omgdc:Point\" y=\"281\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0amp70f\" id=\"ServiceTask_0amp70f_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"404\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1qbr1ye\" id=\"EndEvent_1qbr1ye_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"615\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"588\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12v0zri\" id=\"SequenceFlow_12v0zri_di\"\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"292.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06vnb8g\" id=\"SequenceFlow_06vnb8g_di\"\u003e\u003comgdi:waypoint x=\"504\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"615\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"514.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1gottij\" id=\"TextAnnotation_1gottij_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"104\" x=\"201\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_16cnpze\" id=\"Association_16cnpze_di\"\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04i0tx5\" id=\"TextAnnotation_04i0tx5_di\"\u003e\u003comgdc:Bounds height=\"37\" width=\"147\" x=\"559\" y=\"291\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14p4ckj\" id=\"Association_14p4ckj_di\"\u003e\u003comgdi:waypoint x=\"633\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"633\" xsi:type=\"omgdc:Point\" y=\"291\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0nnempg\" id=\"TextAnnotation_0nnempg_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"118\" x=\"574\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1mhhx8z\" id=\"Association_1mhhx8z_di\"\u003e\u003comgdi:waypoint x=\"633\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"633\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "description": "A sample workflow to delete a team from an incident",
      "export_key": "incident_delete_a_webex_team",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706443,
      "name": "Incident: Delete a Webex Team",
      "object_type": "incident",
      "programmatic_name": "incident_delete_a_webex_team",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "0be761fa-e66c-405a-9e59-92b57790e87b",
      "workflow_id": 19
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "task_create_a_webex_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_webex_room\" isExecutable=\"true\" name=\"Task: Create a Webex Room\"\u003e\u003cdocumentation\u003eA sample workflow to create a room from a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_01b52a8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1wy5hbb\" name=\"Webex: Create Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ab9bd63a-728e-4c80-aa36-27e288813c34\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create a Webex Room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"meetingLink\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Room Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting link: {}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Room ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting ID: {}\\\".format(content.get(\\\"meetingId\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in Toll Number: {}\\\".format(content.get(\\\"callInTollNumber\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in TollFree Number: {}\\\".format(content.get(\\\"callInTollFreeNumber\\\", \\\"-\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\nif task:\\n  inputs.webex_task_id = str(task.id)\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_room_name = \\\"Incident {} Task {}: {}\\\".format(str(incident.id),  str(task.id), incident.name) if rule.properties.webex_room_name is None else rule.properties.webex_room_name\\n\\nif rule.properties.webex_team_id:\\n    inputs.webex_team_id = rule.properties.webex_team_id\\n    \\nif rule.properties.webex_meeting_attendees:\\n    if rule.properties.webex_meeting_attendees.content:\\n      inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n    inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_01b52a8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11zqw8z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0fyg75o\"\u003e\u003cincoming\u003eSequenceFlow_11zqw8z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01b52a8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1wy5hbb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_11zqw8z\" sourceRef=\"ServiceTask_1wy5hbb\" targetRef=\"EndEvent_0fyg75o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1lvuocc\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1wbtk4g\" sourceRef=\"EndEvent_0fyg75o\" targetRef=\"TextAnnotation_1lvuocc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01d99a4\"\u003e\u003ctext\u003eInputs: Room_Name, Team_ID, Include_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02xy3m6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_01d99a4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05u743v\"\u003e\u003ctext\u003eOutput: Room_Name, URL, Meeting_ID, Created_Time, Call_in_Number\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0k5hal4\" sourceRef=\"EndEvent_0fyg75o\" targetRef=\"TextAnnotation_05u743v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"147\" x=\"106\" y=\"271\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"271\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1wy5hbb\" id=\"ServiceTask_1wy5hbb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"320\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fyg75o\" id=\"EndEvent_0fyg75o_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"535\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"553\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01b52a8\" id=\"SequenceFlow_01b52a8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"320\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"259\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11zqw8z\" id=\"SequenceFlow_11zqw8z_di\"\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"477.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1lvuocc\" id=\"TextAnnotation_1lvuocc_di\"\u003e\u003comgdc:Bounds height=\"49\" width=\"156\" x=\"475\" y=\"273\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1wbtk4g\" id=\"Association_1wbtk4g_di\"\u003e\u003comgdi:waypoint x=\"553\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"553\" xsi:type=\"omgdc:Point\" y=\"273\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01d99a4\" id=\"TextAnnotation_01d99a4_di\"\u003e\u003comgdc:Bounds height=\"83\" width=\"140\" x=\"110\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02xy3m6\" id=\"Association_02xy3m6_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"181\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05u743v\" id=\"TextAnnotation_05u743v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"146\" x=\"480\" y=\"40\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0k5hal4\" id=\"Association_0k5hal4_di\"\u003e\u003comgdi:waypoint x=\"553\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"554\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "description": "A sample workflow to create a room from a task",
      "export_key": "task_create_a_webex_room",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680707265,
      "name": "Task: Create a Webex Room",
      "object_type": "task",
      "programmatic_name": "task_create_a_webex_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "4f550d47-c29d-4bf4-9b93-2bc185b8ec9d",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 16,
        "workflow_id": "incident_create_a_webex_meeting",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_webex_meeting\" isExecutable=\"true\" name=\"Incident: Create a Webex Meeting\"\u003e\u003cdocumentation\u003eA sample workflow to create a meeting with team members\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1l9mx5g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00ckq2f\" name=\"Webex: Create Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"674a0970-dab8-4bd1-8e67-4ac8d5068b38\"\u003e{\"inputs\":{\"bfed0c81-a924-44fa-b3be-401d77b69093\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}},\"ac4105e8-e49d-4822-a9e6-777e2bc6e87b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":45}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Cisco WebEx Meeting\\\"\\n\\n  if results.reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, results.reason)\\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"webLink\\\"))\\n\\n  text = u\\\"\u0026lt;b\u0026gt;Cisco Webex Meeting:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;Webex Room URL: {0}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting Name: {}\\\".format(content.get(\\\"title\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Password: {}\\\".format(content.get(\\\"password\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Agenda: {}\\\".format(content.get(\\\"agenda\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Start Time: {}\\\".format(content.get(\\\"start\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;End Time: {}\\\".format(content.get(\\\"end\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Timezone: {}\\\".format(content.get(\\\"timezone\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting Id: {}\\\".format(content.get(\\\"id\\\"))\\n  \\nnote = helper.createRichText(text)\\nincident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_meeting_name = incident.name if rule.properties.webex_meeting_name is None else rule.properties.webex_meeting_name\\n\\nif rule.properties.webex_meeting_start_time:\\n  inputs.webex_meeting_start_time = rule.properties.webex_meeting_start_time      \\nelse:\\n  inputs.webex_meeting_start_time = None\\n\\nif rule.properties.webex_meeting_end_time:\\n  inputs.webex_meeting_end_time = rule.properties.webex_meeting_end_time      \\nelse:\\n  inputs.webex_meeting_end_time = None\\n  \\nif rule.properties.webex_send_email is not None:\\n  inputs.webex_send_email = rule.properties.webex_send_email\\n\\nif rule.properties.webex_meeting_duration:\\n  inputs.webex_meeting_duration = rule.properties.webex_meeting_duration\\n  \\n# Get the agenda from the activity field or the incident description\\nif rule.properties.webex_meeting_agenda is None:\\n  if incident.description is not None and incident.description.content is not None:\\n    inputs.webex_meeting_agenda = incident.description.content\\n  else:\\n    inputs.webex_meeting_agenda = \\\"\\\"\\nelse:\\n  inputs.webex_meeting_agenda = rule.properties.webex_meeting_agenda\\n\\ninputs.webex_meeting_password = inputs.webex_meeting_password if rule.properties.webex_meeting_password is None else rule.properties.webex_meeting_password\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1l9mx5g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o0eh50\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0khgson\"\u003e\u003cincoming\u003eSequenceFlow_0o0eh50\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1l9mx5g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00ckq2f\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0o0eh50\" sourceRef=\"ServiceTask_00ckq2f\" targetRef=\"EndEvent_0khgson\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0nwsweg\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\u00a0webex_meeting_name, webex_meeting_agenda, webex_meeting_password, webex_meeting_duration, webex_meeting_start_time and webex_end_time\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0q1uv1b\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_0nwsweg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1a9594n\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs: Meeting_URL, Name, Password,\u00a0 Agenda, Start_Time, End_Time, Timezone, MeetingID\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1t48ex4\" sourceRef=\"EndEvent_0khgson\" targetRef=\"TextAnnotation_1a9594n\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0mx1g42\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0sh91te\" sourceRef=\"EndEvent_0khgson\" targetRef=\"TextAnnotation_0mx1g42\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"270\" y=\"180\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"265\" y=\"215\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"156\" x=\"207\" y=\"277\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"283\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"277\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00ckq2f\" id=\"ServiceTask_00ckq2f_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"484.7916279069767\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0khgson\" id=\"EndEvent_0khgson_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"732\" y=\"180\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"750\" y=\"219\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l9mx5g\" id=\"SequenceFlow_1l9mx5g_di\"\u003e\u003comgdi:waypoint x=\"306\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"395.5\" y=\"176\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o0eh50\" id=\"SequenceFlow_0o0eh50_di\"\u003e\u003comgdi:waypoint x=\"585\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"732\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"658.5\" y=\"176\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0nwsweg\" id=\"TextAnnotation_0nwsweg_di\"\u003e\u003comgdc:Bounds height=\"110\" width=\"188\" x=\"194\" y=\"11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0q1uv1b\" id=\"Association_0q1uv1b_di\"\u003e\u003comgdi:waypoint x=\"288\" xsi:type=\"omgdc:Point\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"288\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1a9594n\" id=\"TextAnnotation_1a9594n_di\"\u003e\u003comgdc:Bounds height=\"110\" width=\"138\" x=\"681\" y=\"11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1t48ex4\" id=\"Association_1t48ex4_di\"\u003e\u003comgdi:waypoint x=\"750\" xsi:type=\"omgdc:Point\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"751\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0mx1g42\" id=\"TextAnnotation_0mx1g42_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"144\" x=\"678\" y=\"277\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0sh91te\" id=\"Association_0sh91te_di\"\u003e\u003comgdi:waypoint x=\"750\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"750\" xsi:type=\"omgdc:Point\" y=\"277\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 16,
      "description": "A sample workflow to create a meeting with team members",
      "export_key": "incident_create_a_webex_meeting",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663752508009,
      "name": "Incident: Create a Webex Meeting",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_webex_meeting",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "7b2aec21-abaf-42dd-bbf1-55fd7742441c",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "task_delete_a_webex_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_delete_a_webex_team\" isExecutable=\"true\" name=\"Task: Delete a Webex Team\"\u003e\u003cdocumentation\u003eA sample workflow to delete a team from a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0io84j5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_115ijt1\" name=\"Webex: Delete Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74619406-5f6f-4a10-b934-9445ec95e98c\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete the team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += content.get(\\\"message\\\")\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.webex_team_id:\\n  inputs.webex_team_id = rule.properties.webex_team_id\\n\\nif rule.properties.webex_team_name:\\n  inputs.webex_team_name = rule.properties.webex_team_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0io84j5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1h195pf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0x9miwe\"\u003e\u003cincoming\u003eSequenceFlow_1h195pf\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1h195pf\" sourceRef=\"ServiceTask_115ijt1\" targetRef=\"EndEvent_0x9miwe\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0io84j5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_115ijt1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1jub3ou\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ysfxzv\" sourceRef=\"EndEvent_0x9miwe\" targetRef=\"TextAnnotation_1jub3ou\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0o9xxhl\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: Team_name, Team_Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_195omsr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_0o9xxhl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13e77j3\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Confirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03bszo5\" sourceRef=\"EndEvent_0x9miwe\" targetRef=\"TextAnnotation_13e77j3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"628\" y=\"160\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"623\" y=\"195\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"156\" x=\"568\" y=\"307\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"642\" xsi:type=\"omgdc:Point\" y=\"195\"/\u003e\u003comgdi:waypoint x=\"641\" xsi:type=\"omgdc:Point\" y=\"307\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_115ijt1\" id=\"ServiceTask_115ijt1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"863\" y=\"138\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0x9miwe\" id=\"EndEvent_0x9miwe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1191\" y=\"160\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1209\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1h195pf\" id=\"SequenceFlow_1h195pf_di\"\u003e\u003comgdi:waypoint x=\"963\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"1191\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1077\" y=\"156\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0io84j5\" id=\"SequenceFlow_0io84j5_di\"\u003e\u003comgdi:waypoint x=\"664\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"863\" xsi:type=\"omgdc:Point\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"763.5\" y=\"156\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1jub3ou\" id=\"TextAnnotation_1jub3ou_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"132\" x=\"1143\" y=\"307\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ysfxzv\" id=\"Association_0ysfxzv_di\"\u003e\u003comgdi:waypoint x=\"1209\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"1209\" xsi:type=\"omgdc:Point\" y=\"307\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0o9xxhl\" id=\"TextAnnotation_0o9xxhl_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"98\" x=\"596\" y=\"25\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_195omsr\" id=\"Association_195omsr_di\"\u003e\u003comgdi:waypoint x=\"646\" xsi:type=\"omgdc:Point\" y=\"160\"/\u003e\u003comgdi:waypoint x=\"645\" xsi:type=\"omgdc:Point\" y=\"81\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13e77j3\" id=\"TextAnnotation_13e77j3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"142\" x=\"1138\" y=\"35\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03bszo5\" id=\"Association_03bszo5_di\"\u003e\u003comgdi:waypoint x=\"1209\" xsi:type=\"omgdc:Point\" y=\"160\"/\u003e\u003comgdi:waypoint x=\"1209\" xsi:type=\"omgdc:Point\" y=\"71\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "description": "A sample workflow to delete a team from a task",
      "export_key": "task_delete_a_webex_team",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706300,
      "name": "Task: Delete a Webex Team",
      "object_type": "task",
      "programmatic_name": "task_delete_a_webex_team",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "5ef1fcd4-5d58-4371-ae58-215e57b07227",
      "workflow_id": 27
    },
    {
      "actions": [],
      "content": {
        "version": 84,
        "workflow_id": "create_webex_team_with_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"create_webex_team_with_room\" isExecutable=\"true\" name=\"Incident: Create a Webex Team with Room\"\u003e\u003cdocumentation\u003eA sample workflow to create a Webex team and assign a room to the team.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0enfnbl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0byh8zs\" name=\"Webex: Create Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e202188-beda-403c-b0e8-0b626c201382\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Webex Team\\\"\\n\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n\\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created Time: {}\\\".format(content.get(\\\"created\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Members: {}\\\".format(content.get(\\\"attendees\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.webex_team_name is None else rule.properties.webex_team_name\\n\\nif rule.properties.webex_meeting_attendees:\\n  if rule.properties.webex_meeting_attendees.content:\\n    inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n  inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"team\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0enfnbl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1o039xg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_082snff\" name=\"Webex: Create Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ab9bd63a-728e-4c80-aa36-27e288813c34\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create a Webex Room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"meetingLink\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Room Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting link: {}\\\".format(ref_html_room)\\n  text += u\\\"\u0026lt;br /\u0026gt;Room ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Meeting ID: {}\\\".format(content.get(\\\"meetingId\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in Toll Number: {}\\\".format(content.get(\\\"callInTollNumber\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Call in TollFree Number: {}\\\".format(content.get(\\\"callInTollFreeNumber\\\", \\\"-\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Webex Room name has to be different from the Team name\\n_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name)\\nif workflow.properties.team.get(\\\"content\\\"):\\n  _team_name = workflow.properties.team.get(\\\"content\\\").get(\\\"name\\\") if workflow.properties.team.get(\\\"content\\\").get(\\\"name\\\") else _team_name\\n\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_room_name = rule.properties.webex_room_name if rule.properties.webex_room_name else \\\" \\\".join([_team_name, \\\"Room\\\"])\\ninputs.webex_team_id = workflow.properties.team.get(\\\"content\\\").get(\\\"id\\\")\\ninputs.webex_meeting_attendees = None\\ninputs.webex_add_all_members = False\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1o039xg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e6xewt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0l0k2fk\"\u003e\u003cincoming\u003eSequenceFlow_1e6xewt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0enfnbl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0byh8zs\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1o039xg\" sourceRef=\"ServiceTask_0byh8zs\" targetRef=\"ServiceTask_082snff\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1e6xewt\" sourceRef=\"ServiceTask_082snff\" targetRef=\"EndEvent_0l0k2fk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_047z8ar\"\u003e\u003ctext\u003eInputs: Team_Name, Room_Name, Add_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ktgpu3\" sourceRef=\"ServiceTask_0byh8zs\" targetRef=\"TextAnnotation_047z8ar\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10u3aqh\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Note with Team details\u00a0 Room details, Note with Room details\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xyiinp\" sourceRef=\"ServiceTask_082snff\" targetRef=\"TextAnnotation_10u3aqh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13nxji3\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow starts here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15s1ib1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_13nxji3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1m45d0d\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ahcs1s\" sourceRef=\"EndEvent_0l0k2fk\" targetRef=\"TextAnnotation_1m45d0d\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"301\" y=\"200\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"296\" y=\"235\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0byh8zs\" id=\"ServiceTask_0byh8zs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"425\" y=\"175\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_082snff\" id=\"ServiceTask_082snff_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"602\" y=\"175\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0l0k2fk\" id=\"EndEvent_0l0k2fk_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"762\" y=\"197\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"735\" y=\"236\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0enfnbl\" id=\"SequenceFlow_0enfnbl_di\"\u003e\u003comgdi:waypoint x=\"338\" xsi:type=\"omgdc:Point\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"425\" xsi:type=\"omgdc:Point\" y=\"218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"352\" y=\"211\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1o039xg\" id=\"SequenceFlow_1o039xg_di\"\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"602\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"518.5\" y=\"193\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e6xewt\" id=\"SequenceFlow_1e6xewt_di\"\u003e\u003comgdi:waypoint x=\"702\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"762\" xsi:type=\"omgdc:Point\" y=\"214\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"687\" y=\"192.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_047z8ar\" id=\"TextAnnotation_047z8ar_di\"\u003e\u003comgdc:Bounds height=\"78\" width=\"141\" x=\"266\" y=\"43\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ktgpu3\" id=\"Association_1ktgpu3_di\"\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10u3aqh\" id=\"TextAnnotation_10u3aqh_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"191\" x=\"684\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xyiinp\" id=\"Association_0xyiinp_di\"\u003e\u003comgdi:waypoint x=\"691\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"751\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13nxji3\" id=\"TextAnnotation_13nxji3_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"138\" x=\"247\" y=\"311\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15s1ib1\" id=\"Association_15s1ib1_di\"\u003e\u003comgdi:waypoint x=\"319\" xsi:type=\"omgdc:Point\" y=\"236\"/\u003e\u003comgdi:waypoint x=\"317\" xsi:type=\"omgdc:Point\" y=\"311\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1m45d0d\" id=\"TextAnnotation_1m45d0d_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"135\" x=\"712\" y=\"317\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ahcs1s\" id=\"Association_1ahcs1s_di\"\u003e\u003comgdi:waypoint x=\"780\" xsi:type=\"omgdc:Point\" y=\"233\"/\u003e\u003comgdi:waypoint x=\"780\" xsi:type=\"omgdc:Point\" y=\"317\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 84,
      "description": "A sample workflow to create a Webex team and assign a room to the team.",
      "export_key": "create_webex_team_with_room",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1663684393933,
      "name": "Incident: Create a Webex Team with Room",
      "object_type": "incident",
      "programmatic_name": "create_webex_team_with_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "dfb93dc9-c166-40c3-ac68-e5a1bc9b0596",
      "workflow_id": 7
    },
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "incident_delete_a_webex_room",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_delete_a_webex_room\" isExecutable=\"true\" name=\"Incident: Delete a Webex Room\"\u003e\u003cdocumentation\u003eA sample workflow to delete a Webex Room\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0hrzvwv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1yqlhga\" name=\"Webex: Delete Room\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"62cc9b38-ac80-4dfd-8a2f-ddef3044b85b\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete the room\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += content.get(\\\"message\\\")\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.webex_room_id:\\n  inputs.webex_room_id = rule.properties.webex_room_id\\n\\nif rule.properties.webex_room_name:\\n  inputs.webex_room_name = rule.properties.webex_room_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hrzvwv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1fstr57\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hrzvwv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1yqlhga\"/\u003e\u003cendEvent id=\"EndEvent_0cip3kb\"\u003e\u003cincoming\u003eSequenceFlow_1fstr57\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1fstr57\" sourceRef=\"ServiceTask_1yqlhga\" targetRef=\"EndEvent_0cip3kb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ao5zlw\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0tqymx9\" sourceRef=\"EndEvent_0cip3kb\" targetRef=\"TextAnnotation_0ao5zlw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0v3op0q\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: Room_name, Room_Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1r84oad\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_0v3op0q\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qkqb8r\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Confirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_190xvp8\" sourceRef=\"EndEvent_0cip3kb\" targetRef=\"TextAnnotation_0qkqb8r\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"205\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"156\" x=\"102\" y=\"275\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"275\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1yqlhga\" id=\"ServiceTask_1yqlhga_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"351\" y=\"148\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hrzvwv\" id=\"SequenceFlow_0hrzvwv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"274.5\" y=\"166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0cip3kb\" id=\"EndEvent_0cip3kb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"573\" y=\"170\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"591\" y=\"209\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fstr57\" id=\"SequenceFlow_1fstr57_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"573\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"512\" y=\"166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ao5zlw\" id=\"TextAnnotation_0ao5zlw_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"127\" x=\"527\" y=\"277\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0tqymx9\" id=\"Association_0tqymx9_di\"\u003e\u003comgdi:waypoint x=\"591\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"591\" xsi:type=\"omgdc:Point\" y=\"277\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0v3op0q\" id=\"TextAnnotation_0v3op0q_di\"\u003e\u003comgdc:Bounds height=\"73\" width=\"99\" x=\"130\" y=\"30\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1r84oad\" id=\"Association_1r84oad_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qkqb8r\" id=\"TextAnnotation_0qkqb8r_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"128\" x=\"527\" y=\"41\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_190xvp8\" id=\"Association_190xvp8_di\"\u003e\u003comgdi:waypoint x=\"591\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"591\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "description": "A sample workflow to delete a Webex Room",
      "export_key": "incident_delete_a_webex_room",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706865,
      "name": "Incident: Delete a Webex Room",
      "object_type": "incident",
      "programmatic_name": "incident_delete_a_webex_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "2ea6f1a2-4cb8-48ff-81ea-7cdae0e1d224",
      "workflow_id": 23
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "task_create_a_webex_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_webex_team\" isExecutable=\"true\" name=\"Task: Create a Webex Team\"\u003e\u003cdocumentation\u003eA sample workflow to create a team from task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_01c2hld\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_12soi2j\" name=\"Webex: Create Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e202188-beda-403c-b0e8-0b626c201382\"\u003e{\"inputs\":{\"0bc70659-40ad-4178-9174-c7841eb3c9b3\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Webex Team\\\"\\n\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Cisco Webex Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Name: {}\\\".format(content.get(\\\"name\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created Time: {}\\\".format(content.get(\\\"created\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Team Members: {}\\\".format(content.get(\\\"attendees\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\nif task:\\n  inputs.webex_task_id = str(task.id)\\ninputs.webex_incident_id = str(incident.id)\\ninputs.webex_team_name = \\\"Incident {} task {}: {}\\\".format(str(incident.id),  str(task.id), incident.name) if rule.properties.webex_team_name is None else rule.properties.webex_team_name\\n\\nif rule.properties.webex_meeting_attendees:\\n  if rule.properties.webex_meeting_attendees.content:\\n    inputs.webex_meeting_attendees = rule.properties.webex_meeting_attendees.content\\n    \\nif rule.properties.webex_add_all_members is not None:\\n  inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_01c2hld\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0v2fu9t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_01c2hld\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_12soi2j\"/\u003e\u003cendEvent id=\"EndEvent_0d54zqm\"\u003e\u003cincoming\u003eSequenceFlow_0v2fu9t\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0v2fu9t\" sourceRef=\"ServiceTask_12soi2j\" targetRef=\"EndEvent_0d54zqm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0o4963h\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1l5rg4m\" sourceRef=\"EndEvent_0d54zqm\" targetRef=\"TextAnnotation_0o4963h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1g5drfl\"\u003e\u003ctext\u003eInputs: Team_name, Include_all_members, Additional_attendees\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1g7fgt1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1g5drfl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1i5f80b\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Team_name, Created_time, Team_id, Team_members\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1uinw6s\" sourceRef=\"EndEvent_0d54zqm\" targetRef=\"TextAnnotation_1i5f80b\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"160\" x=\"100\" y=\"290\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"290\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_12soi2j\" id=\"ServiceTask_12soi2j_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"327\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01c2hld\" id=\"SequenceFlow_01c2hld_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"327\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"262.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0d54zqm\" id=\"EndEvent_0d54zqm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"547\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"565\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v2fu9t\" id=\"SequenceFlow_0v2fu9t_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"487\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0o4963h\" id=\"TextAnnotation_0o4963h_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"136\" x=\"497\" y=\"290\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1l5rg4m\" id=\"Association_1l5rg4m_di\"\u003e\u003comgdi:waypoint x=\"565\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"565\" xsi:type=\"omgdc:Point\" y=\"290\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1g5drfl\" id=\"TextAnnotation_1g5drfl_di\"\u003e\u003comgdc:Bounds height=\"99\" width=\"150\" x=\"105\" y=\"-2\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1g7fgt1\" id=\"Association_1g7fgt1_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"181\" xsi:type=\"omgdc:Point\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1i5f80b\" id=\"TextAnnotation_1i5f80b_di\"\u003e\u003comgdc:Bounds height=\"79\" width=\"149\" x=\"490\" y=\"8\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1uinw6s\" id=\"Association_1uinw6s_di\"\u003e\u003comgdi:waypoint x=\"565\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"565\" xsi:type=\"omgdc:Point\" y=\"87\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "A sample workflow to create a team from task",
      "export_key": "task_create_a_webex_team",
      "last_modified_by": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
      "last_modified_time": 1663680706153,
      "name": "Task: Create a Webex Team",
      "object_type": "task",
      "programmatic_name": "task_create_a_webex_team",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "e64bd2e5-aa14-46dd-b72b-73a0a9ee25bd",
      "workflow_id": 17
    }
  ],
  "workspaces": []
}
