{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.devs_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop revealx assign tag",
      "id": 126,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx assign tag",
      "object_type": "extrahop_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "911c76f4-ea2e-4fef-9512-7bfd72117e67",
      "view_items": [
        {
          "content": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_assign_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx create tag",
      "id": 127,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx create tag",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "decd187f-500b-4eda-9ee1-d8a9ab298dae",
      "view_items": [
        {
          "content": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_create_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get activitymaps",
      "id": 128,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get activitymaps",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d4f01da3-6489-4314-a7c6-0898a8f5e4b5",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_activitymaps"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get detections",
      "id": 129,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get detections",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac9f8677-a9e3-4bba-998b-9956748c88f2",
      "view_items": [
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_get_detections"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get devices",
      "id": 130,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "57789c28-de6a-46b4-8819-16ea53859de6",
      "view_items": [
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "059e3b00-b65d-4eb0-a81c-de01b3b1959c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_get_devices"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get tags",
      "id": 131,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get tags",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b3318147-5a01-40da-8187-ca9140c04797",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_tags"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get watchlist",
      "id": 132,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get watchlist",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6adc7665-89bd-4448-a0be-bc205fc385a1",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_watchlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx search detections",
      "id": 133,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx search detections",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e09ea0e6-ec4d-4c03-804e-1420cdd10cd6",
      "view_items": [
        {
          "content": "db088f98-801f-49e4-b9fe-4f0b6f4d33f5",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d46ebaf8-c9c1-4ca6-9c6c-b13c33886362",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_detections"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx search devices",
      "id": 134,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "60bf1021-e9f0-4395-bdaf-08e9006c4db0",
      "view_items": [
        {
          "content": "183c411d-c4e5-4995-a711-e58f2ea40221",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_devices"
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
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "MAC Address"
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop revealx update watchlist",
      "id": 137,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Extrahop revealx update watchlist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ad8f9e79-e167-4e7c-814c-7e3e297a4b83",
      "view_items": [
        {
          "content": "f7e7aa61-a227-4545-bede-653afe438414",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_update_watchlist"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647626290379,
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
      "export_key": "__function/soar_inc_owner_id",
      "hide_notification": false,
      "id": 995,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_owner_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_owner_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "88360341-cb95-4040-9f2c-920f41d138bf",
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
      "export_key": "__function/extrahop_tag_name",
      "hide_notification": false,
      "id": 996,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_tag_name",
      "tooltip": "The string value for an Etrahop  tag name.",
      "type_id": 11,
      "uuid": "9274ccb1-cebb-4be8-b7f1-f768f0eabbcf",
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
      "export_key": "__function/extrahop_always_return_body",
      "hide_notification": false,
      "id": 997,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_always_return_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_always_return_body",
      "tooltip": "If True return an empty packet capture file and an HTTP status of 200.",
      "type_id": 11,
      "uuid": "980e64f8-1d36-4d58-a611-0d3c54a9bf02",
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
      "export_key": "__function/extrahop_unassign",
      "hide_notification": false,
      "id": 998,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_unassign",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_unassign",
      "tooltip": "Comma or newline seperated list of device ids to unassign from a watchlist.",
      "type_id": 11,
      "uuid": "a19c702d-206d-48a7-8b26-80d7d4aaa4b6",
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
      "export_key": "__function/extrahop_assign",
      "hide_notification": false,
      "id": 999,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_assign",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_assign",
      "tooltip": "Comma or newline seperated list of device ids to assign to a watchlist.",
      "type_id": 11,
      "uuid": "a4628ae7-81c6-4208-ba4f-e71295f3c117",
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
      "export_key": "__function/extrahop_active_from",
      "hide_notification": false,
      "id": 1000,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_active_from",
      "tooltip": "(Optional) The beginning timestamp for the request. Return only devices active after this time. Time is expressed in milliseconds since the epoch. 0 indicates the time of the request.",
      "type_id": 11,
      "uuid": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
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
      "export_key": "__function/extrahop_update_time",
      "hide_notification": false,
      "id": 1001,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_update_time",
      "tooltip": "(Optional) Return detections that were updated on or after the specified date, expressed in milliseconds since the epoch.",
      "type_id": 11,
      "uuid": "b175d32a-198e-403d-adcd-052b56876488",
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
      "export_key": "__function/extrahop_port2",
      "hide_notification": false,
      "id": 1002,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_port2",
      "tooltip": " Return packets sent from or received on the specified port.",
      "type_id": 11,
      "uuid": "bd451766-afc3-40d7-86c8-5c512586b7d0",
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
      "export_key": "__function/extrahop_offset",
      "hide_notification": false,
      "id": 1003,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_offset",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_offset",
      "tooltip": "(Optional) Skip the specified number of devices. This parameter is often combined with the limit parameter to paginate result sets.",
      "type_id": 11,
      "uuid": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
      "export_key": "__function/soar_inc_resolution_id",
      "hide_notification": false,
      "id": 1004,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_resolution_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_resolution_id",
      "tooltip": "SOAR incident resolution",
      "type_id": 11,
      "uuid": "ccbe84af-c0ae-4ae5-a280-c84d1bde5f4d",
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
      "export_key": "__function/extrahop_limit_search_duration",
      "hide_notification": false,
      "id": 1005,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_search_duration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit_search_duration",
      "tooltip": "The maximum amount of time to run the packet search.",
      "type_id": 11,
      "uuid": "d265d66f-635b-4f5c-8aa5-d7146f65ac15",
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
      "export_key": "__function/soar_inc_plan_status",
      "hide_notification": false,
      "id": 1006,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_plan_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_plan_status",
      "tooltip": "SOAR incident status",
      "type_id": 11,
      "uuid": "dce787c0-2575-4dde-b0fa-a453fff3c941",
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
      "export_key": "__function/extrahop_limit_bytes",
      "hide_notification": false,
      "id": 1007,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_bytes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit_bytes",
      "tooltip": "The maximum number of bytes to return.",
      "type_id": 11,
      "uuid": "eef5fc53-d7d2-4711-9263-ccec47dacd13",
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
      "export_key": "__function/extrahop_activitymap_id",
      "hide_notification": false,
      "id": 1008,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_activitymap_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_activitymap_id",
      "tooltip": "The unique identifier for the activity map.",
      "type_id": 11,
      "uuid": "f1d0366d-e216-4071-8070-c67fe27f834b",
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
      "export_key": "__function/extrahop_device_ids",
      "hide_notification": false,
      "id": 1009,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_device_ids",
      "tooltip": "Comma or newline seperated list of device ids.",
      "type_id": 11,
      "uuid": "f7117970-a76c-4505-87b3-5dbcc35eabdc",
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
      "export_key": "__function/extrahop_ip1",
      "hide_notification": false,
      "id": 1010,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_ip1",
      "tooltip": "Return packets sent to or received by the specified IP address.",
      "type_id": 11,
      "uuid": "f844555a-e911-4ea3-95c2-44ad4f8c5ef9",
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
      "export_key": "__function/extrahop_sort",
      "hide_notification": false,
      "id": 1011,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_sort",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_sort",
      "tooltip": "Sorts returned detections by the specified fields. By default, detections are sorted by most recent update time and then ID in ascending order.",
      "type_id": 11,
      "uuid": "0b7aca53-b3b4-42b0-8386-3f19042acf55",
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
      "export_key": "__function/extrahop_search_filter",
      "hide_notification": false,
      "id": 1012,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_search_filter",
      "tooltip": "The  filter criteria for Extrahop search results.",
      "type_id": 11,
      "uuid": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
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
      "export_key": "__function/extrahop_participants",
      "hide_notification": false,
      "id": 1013,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_participants",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{ \"id\": 0, \"usernames\": [], \"origins\": [] }",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_participants",
      "tooltip": "A list of devices and applications associated with a detection. ",
      "type_id": 11,
      "uuid": "13f7dfc8-67b0-4ead-a5c7-191d915cf79b",
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
      "export_key": "__function/extrahop_bpf",
      "hide_notification": false,
      "id": 1014,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_bpf",
      "operation_perms": {},
      "operations": [],
      "placeholder": "host 192.168.1.2  dst host 192.168.1.3",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_bpf",
      "tooltip": "Filter packets with Berkeley Packet Filter syntax.",
      "type_id": 11,
      "uuid": "19778340-0ca0-47af-bb7b-61d0d2be6fa1",
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
      "export_key": "__function/extrahop_detection_id",
      "hide_notification": false,
      "id": 1015,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_detection_id",
      "tooltip": "Extrahop detection ID",
      "type_id": 11,
      "uuid": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
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
      "export_key": "__function/extrahop_search_type",
      "hide_notification": false,
      "id": 1016,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_search_type",
      "tooltip": "Indicates the field to search.",
      "type_id": 11,
      "uuid": "3a2068f3-d76c-4dac-8776-819499720814",
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
      "id": 1017,
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "The ID for the incident in Resilient",
      "type_id": 11,
      "uuid": "3eb56561-8f36-458f-845a-eb3923bd0073",
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
      "export_key": "__function/extrahop_ip2",
      "hide_notification": false,
      "id": 1018,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_ip2",
      "tooltip": "Return packets sent to or received by the specified IP address.",
      "type_id": 11,
      "uuid": "4756201b-b5b0-4a90-934d-815e13644e5e",
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
      "export_key": "__function/extrahop_tag_id",
      "hide_notification": false,
      "id": 1019,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_tag_id",
      "tooltip": "The unique identifier for the tag.",
      "type_id": 11,
      "uuid": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
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
      "export_key": "__function/extrahop_limit",
      "hide_notification": false,
      "id": 1020,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit",
      "tooltip": "(Optional) Limit the number of devices returned to the specified maximum number.",
      "type_id": 11,
      "uuid": "64a89cad-9373-4017-ba04-d06f97a28e8c",
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
      "export_key": "__function/extrahop_active_until",
      "hide_notification": false,
      "id": 1021,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_until",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_active_until",
      "tooltip": "(Optional) The ending timestamp for the request. Return only devices active before this time.",
      "type_id": 11,
      "uuid": "68a4691f-8609-4d19-9208-3a7589a37997",
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
      "export_key": "__function/extrahop_port1",
      "hide_notification": false,
      "id": 1022,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_port1",
      "tooltip": "Return packets sent from or received on the specified port.",
      "type_id": 11,
      "uuid": "6aa0c2da-9841-4b51-9c22-bd8d245d9cc6",
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
      "export_key": "__function/extrahop_output",
      "hide_notification": false,
      "id": 1023,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_output",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_output",
      "tooltip": "The output format. Valid values pcap , keylog_txt  and zip",
      "type_id": 11,
      "uuid": "70f63d36-2b02-4939-ad37-620659809eaa",
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
      "export_key": "__function/extrahop_device_id",
      "hide_notification": false,
      "id": 1024,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_device_id",
      "tooltip": "Extrahop device ID",
      "type_id": 11,
      "uuid": "77f58f54-c4a9-4720-ab05-34e2beb94521",
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
      "export_key": "actioninvocation/extrahop_active_until",
      "hide_notification": false,
      "id": 983,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_until",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop active until",
      "tooltip": " (Optional) The ending timestamp for the request. ",
      "type_id": 6,
      "uuid": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
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
      "export_key": "actioninvocation/extrahop_tag_name",
      "hide_notification": false,
      "id": 985,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop tag name",
      "tooltip": "The string value for an Etrahop  tag name.",
      "type_id": 6,
      "uuid": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
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
      "export_key": "actioninvocation/extrahop_limit",
      "hide_notification": false,
      "id": 986,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop limit",
      "tooltip": "(Optional) Limit the number of devices returned to the specified maximum number.",
      "type_id": 6,
      "uuid": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
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
      "export_key": "actioninvocation/extrahop_offset",
      "hide_notification": false,
      "id": 987,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_offset",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop offset",
      "tooltip": "(Optional) Skip the specified number of devices. This parameter is often combined with the limit parameter to paginate result sets.",
      "type_id": 6,
      "uuid": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
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
      "export_key": "actioninvocation/extrahop_update_time",
      "hide_notification": false,
      "id": 988,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop update time",
      "tooltip": "(Optional) Return detections that were updated on or after the specified date, expressed in milliseconds since the epoch.",
      "type_id": 6,
      "uuid": "d46ebaf8-c9c1-4ca6-9c6c-b13c33886362",
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
      "export_key": "actioninvocation/extrahop_detection_search_filter",
      "hide_notification": false,
      "id": 989,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"filter\": {\"category\": \"string\",\"assignee\": [], \"ticket_id\": [], \"status\": [], \"resolution\": []}}",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop detection search filter",
      "tooltip": "The  filter criteria for Extrahop detection search results.",
      "type_id": 6,
      "uuid": "db088f98-801f-49e4-b9fe-4f0b6f4d33f5",
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
      "export_key": "actioninvocation/extrahop_watchlist_action",
      "hide_notification": false,
      "id": 990,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_watchlist_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop watchlist action",
      "tooltip": "Add or remove device to or from the watchlist.",
      "type_id": 6,
      "uuid": "f7e7aa61-a227-4545-bede-653afe438414",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "add",
          "properties": null,
          "uuid": "1907ca01-4f6e-4ed4-b6e8-f99b8404ec6d",
          "value": 524
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "remove",
          "properties": null,
          "uuid": "302c895f-5535-4ac6-ab4c-7bd6de4294b1",
          "value": 525
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
      "export_key": "actioninvocation/extrahop_search_type",
      "hide_notification": false,
      "id": 991,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop search type",
      "tooltip": "Indicates the field to search.",
      "type_id": 6,
      "uuid": "059e3b00-b65d-4eb0-a81c-de01b3b1959c",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "any",
          "properties": null,
          "uuid": "8276c5a2-f8d0-4361-988f-0227fa8262b6",
          "value": 526
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "name",
          "properties": null,
          "uuid": "05685c68-2b4e-456e-bad0-6bb6339acb1f",
          "value": 527
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "discovery_id",
          "properties": null,
          "uuid": "cbfd6cf3-5d01-4bc4-8d1b-a7b0cd0b04be",
          "value": 528
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ip address",
          "properties": null,
          "uuid": "ec95787b-a0f8-409e-ab14-5a77e453cb9d",
          "value": 529
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "mac address",
          "properties": null,
          "uuid": "7c13af45-60e3-48f0-afc6-b28e486c8c36",
          "value": 530
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vendor",
          "properties": null,
          "uuid": "a5a8c59b-fa8a-41b0-b6ad-e40e8cd08823",
          "value": 531
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "type",
          "properties": null,
          "uuid": "d1fd9de4-0499-4374-a7dc-e9307ea795f7",
          "value": 532
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "tag",
          "properties": null,
          "uuid": "0772e646-8fee-4df1-91e8-90cdd464f358",
          "value": 533
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "activity",
          "properties": null,
          "uuid": "7670eeb0-792d-498b-92f2-6386038dbd82",
          "value": 534
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "node",
          "properties": null,
          "uuid": "84ce8788-aafa-475e-9a0b-74eb59f6a8d2",
          "value": 535
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vlan",
          "properties": null,
          "uuid": "6e2316fd-dc8c-48aa-911d-8313a3d37ac6",
          "value": 536
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "discover time",
          "properties": null,
          "uuid": "8081cae6-138d-4e7e-a6d2-dd5325abeb8c",
          "value": 537
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
      "export_key": "actioninvocation/extrahop_device_search_filter",
      "hide_notification": false,
      "id": 992,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{   \"filter\": {     \"field\": \"string\",     \"operator\": \"string\",     \"operand\": \"string\",     \"rules\": []   } }",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop device search filter",
      "tooltip": "",
      "type_id": 6,
      "uuid": "183c411d-c4e5-4995-a711-e58f2ea40221",
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
      "export_key": "actioninvocation/extrahop_active_from",
      "hide_notification": false,
      "id": 993,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop active from",
      "tooltip": "(Optional) The beginning timestamp for the request.",
      "type_id": 6,
      "uuid": "472c0398-165f-4543-a42e-e689031485a0",
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
      "export_key": "incident/extrahop_detection_link",
      "hide_notification": false,
      "id": 1048,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Extrahop Detection Link",
      "tooltip": "Link back to ExtraHop detection",
      "type_id": 0,
      "uuid": "9ebbe669-25c7-4669-9eab-122113403cc4",
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
      "export_key": "incident/extrahop_detection_id",
      "hide_notification": false,
      "id": 609,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Detection ID",
      "tooltip": "Extrahop detecion ID.",
      "type_id": 0,
      "uuid": "264154d1-778e-4fe8-afff-485d86020976",
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
      "created_date": 1645624876476,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Assign a tag to a list of devices ids forExtrahop Reveal(x). Optional parameters tag_id. devices_ids.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx assign tag",
      "export_key": "funct_extrahop_rx_assign_tag",
      "id": 97,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123507,
      "name": "funct_extrahop_rx_assign_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "f0d2fc8c-20ab-440c-b4f5-46776a0b561e",
      "version": 2,
      "view_items": [
        {
          "content": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f7117970-a76c-4505-87b3-5dbcc35eabdc",
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
          "name": "Example: Extrahop revealx assign tag",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_assign_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        }
      ]
    },
    {
      "created_date": 1645624876604,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Create a new tag for  Extrahop Reveal(x). Optional parameters tag_id.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx create tag",
      "export_key": "funct_extrahop_rx_create_tag",
      "id": 98,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123594,
      "name": "funct_extrahop_rx_create_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "d566e4b3-6692-4599-a351-7530cdb4874e",
      "version": 2,
      "view_items": [
        {
          "content": "9274ccb1-cebb-4be8-b7f1-f768f0eabbcf",
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
          "name": "Example: Extrahop revealx create tag",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_create_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 91
        }
      ]
    },
    {
      "created_date": 1645624876738,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get activitymap information from Extrahop Reveal(x) . Optional parameters activitymap_id.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get activitymaps",
      "export_key": "funct_extrahop_rx_get_activitymaps",
      "id": 99,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123689,
      "name": "funct_extrahop_rx_get_activitymaps",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "18aa0964-745b-4329-a04b-a92f5f3fab40",
      "version": 2,
      "view_items": [
        {
          "content": "f1d0366d-e216-4071-8070-c67fe27f834b",
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
          "name": "Example: Extrahop revealx get activitymaps",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_activitymaps",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 97
        }
      ]
    },
    {
      "created_date": 1645624876886,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get detections information from Extrahop Reveal(x) . Optional parameters extrahop_detecion_id.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get detections",
      "export_key": "funct_extrahop_rx_get_detections",
      "id": 100,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123796,
      "name": "funct_extrahop_rx_get_detections",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "fc71fc68-991e-4825-bc07-2191e58745f3",
      "version": 2,
      "view_items": [
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
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
          "name": "Example: Extrahop revealx get detections",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_detections",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    },
    {
      "created_date": 1645624877010,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get devices information from Extrahop Reveal(x) . Optional parameters  device_id, active_from, active_util, limit and offset.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get devices",
      "export_key": "funct_extrahop_rx_get_devices",
      "id": 101,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123885,
      "name": "funct_extrahop_rx_get_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "75447029-32ca-4363-b753-bc970cee66d5",
      "version": 2,
      "view_items": [
        {
          "content": "77f58f54-c4a9-4720-ab05-34e2beb94521",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a2068f3-d76c-4dac-8776-819499720814",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
          "name": "Example: Extrahop revealx get devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_devices",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 89
        }
      ]
    },
    {
      "created_date": 1645624877122,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get tags information from Extrahop Reveal(x) . Optional parameters tag_id.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get tags",
      "export_key": "funct_extrahop_rx_get_tags",
      "id": 102,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698123969,
      "name": "funct_extrahop_rx_get_tags",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "55ced5bd-cd23-4212-b661-956fed40722b",
      "version": 2,
      "view_items": [
        {
          "content": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
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
          "name": "Example: Extrahop revealx assign tag",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_assign_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop revealx get tags",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_tags",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        }
      ]
    },
    {
      "created_date": 1645624877254,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Retrieve all devices that are in the watchlist from Extrahop Reveal(x) .",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get watchlist",
      "export_key": "funct_extrahop_rx_get_watchlist",
      "id": 103,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124085,
      "name": "funct_extrahop_rx_get_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "4d5690ce-998c-4fbb-bf25-765800aaa246",
      "version": 2,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop revealx get watchlist",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 93
        }
      ]
    },
    {
      "created_date": 1645624877365,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for detections information from Extrahop Reveal(x). Optional parameter search_filter, active_from, active_util, limit , offset, update_time and sort.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx search detections",
      "export_key": "funct_extrahop_rx_search_detections",
      "id": 104,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124199,
      "name": "funct_extrahop_rx_search_detections",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b70037a5-fcaf-4e78-a1e2-6acdc4dff239",
      "version": 2,
      "view_items": [
        {
          "content": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b175d32a-198e-403d-adcd-052b56876488",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b7aca53-b3b4-42b0-8386-3f19042acf55",
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
          "name": "Example: Extrahop revealx search detections",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_detections",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    },
    {
      "created_date": 1645624877489,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for devices information from Extrahop Reveal(x). Optional parameter search_filter, active_from, active_util, limit and offset.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx search devices",
      "export_key": "funct_extrahop_rx_search_devices",
      "id": 105,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124304,
      "name": "funct_extrahop_rx_search_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "e7384abd-0046-4b46-97af-d34d8cc9c711",
      "version": 2,
      "view_items": [
        {
          "content": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
          "name": "Example: Extrahop revealx search devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_devices",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 99
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop revealx update watchlist",
          "object_type": "artifact",
          "programmatic_name": "wf_extrahop_rx_update_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 98
        }
      ]
    },
    {
      "created_date": 1645624877595,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for and download packets stored on the ExtraHop Reveal(x) system.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx search packets",
      "export_key": "funct_extrahop_rx_search_packets",
      "id": 106,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124424,
      "name": "funct_extrahop_rx_search_packets",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "f551a853-62d0-468d-9e36-df5904c5bf96",
      "version": 2,
      "view_items": [
        {
          "content": "3eb56561-8f36-458f-845a-eb3923bd0073",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70f63d36-2b02-4939-ad37-620659809eaa",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eef5fc53-d7d2-4711-9263-ccec47dacd13",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d265d66f-635b-4f5c-8aa5-d7146f65ac15",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "980e64f8-1d36-4d58-a611-0d3c54a9bf02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "19778340-0ca0-47af-bb7b-61d0d2be6fa1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f844555a-e911-4ea3-95c2-44ad4f8c5ef9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6aa0c2da-9841-4b51-9c22-bd8d245d9cc6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4756201b-b5b0-4a90-934d-815e13644e5e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd451766-afc3-40d7-86c8-5c512586b7d0",
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
      "created_date": 1645624877696,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Update a detection in Extrahop Reveal(x). Required parameter incident_id, detection_id, owner_id, plan_status, resolution. Optional parameters participants.",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx update detection",
      "export_key": "funct_extrahop_rx_update_detection",
      "id": 107,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124524,
      "name": "funct_extrahop_rx_update_detection",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "8ee5a0dc-d7d9-4d02-85a3-55d340a43aa0",
      "version": 2,
      "view_items": [
        {
          "content": "3eb56561-8f36-458f-845a-eb3923bd0073",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dce787c0-2575-4dde-b0fa-a453fff3c941",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ccbe84af-c0ae-4ae5-a280-c84d1bde5f4d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "88360341-cb95-4040-9f2c-920f41d138bf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13f7dfc8-67b0-4ead-a5c7-191d915cf79b",
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
      "created_date": 1645624877864,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add or remove devices from the watchlist on Extrahop reveal(x)).",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx update watchlist",
      "export_key": "funct_extrahop_rx_update_watchlist",
      "id": 108,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1645698124605,
      "name": "funct_extrahop_rx_update_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b8d33930-3417-436e-82a1-267a5dc9fa91",
      "version": 2,
      "view_items": [
        {
          "content": "a4628ae7-81c6-4208-ba4f-e71295f3c117",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a19c702d-206d-48a7-8b26-80d7d4aaa4b6",
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
          "name": "Example: Extrahop revealx update watchlist",
          "object_type": "artifact",
          "programmatic_name": "wf_extrahop_rx_update_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 98
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 20,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647626259738,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647626259738,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "4310b8e4-589b-4f9c-884e-5629b86b285c"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "extrahop",
      "name": "extrahop",
      "programmatic_name": "extrahop",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "users": [
        "a@a.com"
      ],
      "uuid": "f81b5729-e662-495a-8b49-b2c934b5c26e"
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
      "display_name": "ExtraHop Activitymaps",
      "export_key": "extrahop_activitymaps",
      "fields": {
        "ams_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_description",
          "hide_notification": false,
          "id": 884,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_description",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "c2b5859c-61be-4e53-9560-3677fe57c0ff",
          "values": [],
          "width": 88
        },
        "ams_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_id",
          "hide_notification": false,
          "id": 885,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "39022bfb-713f-43f7-ac47-f17d6a857f8a",
          "values": [],
          "width": 18
        },
        "ams_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_name",
          "hide_notification": false,
          "id": 886,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_name",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Name",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "41121269-26c3-4cbd-8131-d65339a7455e",
          "values": [],
          "width": 44
        },
        "mod_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/mod_time",
          "hide_notification": false,
          "id": 887,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mod time",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "7467ba91-6d24-4d7e-9e8b-ca27877ad449",
          "values": [],
          "width": 34
        },
        "mode": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/mode",
          "hide_notification": false,
          "id": 888,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mode",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mode",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "779f44c3-eb2d-41fe-b570-1b5195847dec",
          "values": [],
          "width": 41
        },
        "owner": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/owner",
          "hide_notification": false,
          "id": 889,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "owner",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Owner",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "309b4088-7cc0-4ff3-96f6-e9d9de24b965",
          "values": [],
          "width": 50
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/query_execution_date",
          "hide_notification": false,
          "id": 890,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "cbe6cb23-7dbb-468b-a3ae-097fede6a055",
          "values": [],
          "width": 75
        },
        "rights": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/rights",
          "hide_notification": false,
          "id": 891,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "rights",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Rights",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "d0ee5116-6629-4ca4-b87b-89ac91240207",
          "values": [],
          "width": 48
        },
        "short_code": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/short_code",
          "hide_notification": false,
          "id": 892,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "short_code",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Short code",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "438e0eec-1608-462e-89c0-bcac47d1e2d4",
          "values": [],
          "width": 42
        },
        "show_alert_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/show_alert_status",
          "hide_notification": false,
          "id": 893,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "show_alert_status",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Show alert status",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "ed6be14d-c73d-43ad-bcc0-22650a4811b2",
          "values": [],
          "width": 47
        },
        "walks": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/walks",
          "hide_notification": false,
          "id": 894,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "walks",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Walks",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "004aa07c-fcf4-40b8-93d5-3e9b965c092f",
          "values": [],
          "width": 98
        },
        "weighting": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/weighting",
          "hide_notification": false,
          "id": 895,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "weighting",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Weighting",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "48a3c9a6-2502-40db-9dce-71a0715c48b4",
          "values": [],
          "width": 77
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_activitymaps",
      "uuid": "7ff13989-c3e2-4797-81cd-3766c947c452"
    },
    {
      "actions": [],
      "display_name": "Extrahop Detections",
      "export_key": "extrahop_detections",
      "fields": {
        "appliance_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/appliance_id",
          "hide_notification": false,
          "id": 1025,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "appliance_id",
          "operation_perms": {},
          "operations": [],
          "order": 20,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Appliance id",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "e07d8028-42a2-4e38-8b55-06485e4aba47",
          "values": [],
          "width": 77
        },
        "assignee": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/assignee",
          "hide_notification": false,
          "id": 1026,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "assignee",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Assignee",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "3ae88e4a-bed0-4120-9af0-908cb0cdb75a",
          "values": [],
          "width": 69
        },
        "categories": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/categories",
          "hide_notification": false,
          "id": 1027,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "categories",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Categories",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "6ebb268c-f45a-4fc9-9259-d0e389302d76",
          "values": [],
          "width": 82
        },
        "det_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/det_description",
          "hide_notification": false,
          "id": 1028,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "det_description",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "7a0898df-d4cb-4b2a-8270-97f08ebeab5a",
          "values": [],
          "width": 305
        },
        "det_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/det_id",
          "hide_notification": false,
          "id": 1029,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "det_id",
          "operation_perms": {},
          "operations": [],
          "order": 19,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "337912b5-f97b-4746-b1c8-1b915d82b2d0",
          "values": [],
          "width": 18
        },
        "end_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/end_time",
          "hide_notification": false,
          "id": 1030,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "end_time",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "End time",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "3147a5ba-eafd-4ae9-9787-0d06533db4d3",
          "values": [],
          "width": 34
        },
        "is_user_created": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/is_user_created",
          "hide_notification": false,
          "id": 1031,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "is_user_created",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Is user created",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "0b055da1-91f0-4437-be4b-3899ece4c732",
          "values": [],
          "width": 58
        },
        "mitre_tactics": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/mitre_tactics",
          "hide_notification": false,
          "id": 1032,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mitre_tactics",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mitre tactics",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "dd7b464d-629f-4a6d-adb3-ce035dd1f7f4",
          "values": [],
          "width": 218
        },
        "mitre_techniques": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/mitre_techniques",
          "hide_notification": false,
          "id": 1033,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mitre_techniques",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mitre techniques",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "feb16d57-13de-42c0-a9bd-78308de095de",
          "values": [],
          "width": 223
        },
        "participants": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/participants",
          "hide_notification": false,
          "id": 1034,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "participants",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Participants",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "039c878d-c07e-440b-9bab-fc7d87de4921",
          "values": [],
          "width": 173
        },
        "properties": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/properties",
          "hide_notification": false,
          "id": 1035,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "properties",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Properties",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "4a88b4aa-6141-4872-b5e5-4cd69c1b8506",
          "values": [],
          "width": 80
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/query_execution_date",
          "hide_notification": false,
          "id": 1036,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "c3476aba-a7e1-4f01-bfd0-8ab3fd6f98b1",
          "values": [],
          "width": 119
        },
        "resolution": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/resolution",
          "hide_notification": false,
          "id": 1037,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "resolution",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Resolution",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "cbb2a8e0-b616-464a-a386-5eaa8cbeb151",
          "values": [],
          "width": 81
        },
        "risk_score": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/risk_score",
          "hide_notification": false,
          "id": 1038,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "risk_score",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Risk score",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "2f42568a-0acd-449f-8ce0-0f6bd46c2712",
          "values": [],
          "width": 41
        },
        "start_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/start_time",
          "hide_notification": false,
          "id": 1039,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "start_time",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Start time",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "8ba5c84e-df1d-466b-8c64-205589895e76",
          "values": [],
          "width": 38
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/status",
          "hide_notification": false,
          "id": 1040,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "fd8fa146-2f02-42a7-be7a-95d0ffaa1ccc",
          "values": [],
          "width": 49
        },
        "ticket_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/ticket_id",
          "hide_notification": false,
          "id": 1041,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_id",
          "operation_perms": {},
          "operations": [],
          "order": 18,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket ID",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "2947aabf-4274-48cc-b5cb-76ec2816a5ad",
          "values": [],
          "width": 47
        },
        "ticket_url": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/ticket_url",
          "hide_notification": false,
          "id": 1042,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_url",
          "operation_perms": {},
          "operations": [],
          "order": 16,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket URL",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "065d5317-5a89-4834-8a72-8ff9658d9563",
          "values": [],
          "width": 47
        },
        "title": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/title",
          "hide_notification": false,
          "id": 1043,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "title",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Title",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "85a98923-5167-4f7b-8a6c-3d2c96c0cdf6",
          "values": [],
          "width": 34
        },
        "type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/type",
          "hide_notification": false,
          "id": 1044,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type",
          "operation_perms": {},
          "operations": [],
          "order": 17,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "3e8d5dcd-2a86-47b0-bd51-8396d8404244",
          "values": [],
          "width": 36
        },
        "update_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/update_time",
          "hide_notification": false,
          "id": 1045,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "update_time",
          "operation_perms": {},
          "operations": [],
          "order": 15,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Update time",
          "tooltip": "",
          "type_id": 1018,
          "uuid": "8bd44e1b-f2ca-43c5-9b6b-15961c328fc7",
          "values": [],
          "width": 55
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
      "tags": [],
      "type_id": 8,
      "type_name": "extrahop_detections",
      "uuid": "712e0e4e-8209-472d-8978-d72f18c2e583"
    },
    {
      "actions": [],
      "display_name": "ExtraHop Devices",
      "export_key": "extrahop_devices",
      "fields": {
        "activity": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/activity",
          "hide_notification": false,
          "id": 917,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "activity",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Activity",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "fb3dd873-04ee-4836-9a4e-e51408568069",
          "values": [],
          "width": 59
        },
        "default_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/default_name",
          "hide_notification": false,
          "id": 918,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "default_name",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Default name",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "e0a7c1d0-9c01-4f1f-8902-341c0bfcaee4",
          "values": [],
          "width": 56
        },
        "devs_description": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/devs_description",
          "hide_notification": false,
          "id": 919,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "devs_description",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "b2041256-ddea-4577-803b-a18389a4d876",
          "values": [],
          "width": 88
        },
        "devs_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/devs_id",
          "hide_notification": false,
          "id": 920,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "devs_id",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "e23fc672-29b3-457d-b118-bc9ae13a80ff",
          "values": [],
          "width": 18
        },
        "display_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/display_name",
          "hide_notification": false,
          "id": 921,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "display_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Display name",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "2afb30e5-422f-4663-810f-fe8b965a482c",
          "values": [],
          "width": 57
        },
        "dns_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/dns_name",
          "hide_notification": false,
          "id": 922,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "dns_name",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "DNS name",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "88e6cf47-4b8e-4dce-adde-206212ed97b9",
          "values": [],
          "width": 83
        },
        "extrahop_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/extrahop_id",
          "hide_notification": false,
          "id": 923,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "extrahop_id",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ExtraHop id",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "2ce02cd6-4559-42de-b65f-84f63237528f",
          "values": [],
          "width": 71
        },
        "ipaddr4": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/ipaddr4",
          "hide_notification": false,
          "id": 1046,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr4",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr4",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "9c3eed4d-a6a6-40ac-bf9b-cf92a19c71e2",
          "values": [],
          "width": 83
        },
        "ipaddr6": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/ipaddr6",
          "hide_notification": false,
          "id": 925,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr6",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr6",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "61994faf-d774-4e3d-a2d7-51c0ace7a18a",
          "values": [],
          "width": 88
        },
        "macaddr": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/macaddr",
          "hide_notification": false,
          "id": 926,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "macaddr",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "MACaddr",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "c0a1d534-8346-4082-aec8-fbcbd4c01845",
          "values": [],
          "width": 70
        },
        "on_watchlist": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/on_watchlist",
          "hide_notification": false,
          "id": 927,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "on_watchlist",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "On watchlist",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "5b6864c2-5177-45d7-8a46-c85721e569f1",
          "values": [],
          "width": 71
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/query_execution_date",
          "hide_notification": false,
          "id": 928,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "9100b462-eafd-4a19-9c0f-9380a168e8d7",
          "values": [],
          "width": 75
        },
        "role": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/role",
          "hide_notification": false,
          "id": 929,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "role",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Role",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "e337a0f0-19c9-461e-878d-0968c0a55260",
          "values": [],
          "width": 34
        },
        "vendor": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/vendor",
          "hide_notification": false,
          "id": 930,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "vendor",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Vendor",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "bb6fa4e4-6ea3-45b9-9a07-cd7096c78051",
          "values": [],
          "width": 54
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_devices",
      "uuid": "611de6ae-8b44-4bba-a2d9-9169ab0da2ec"
    },
    {
      "actions": [],
      "display_name": "Extrahop Tags",
      "export_key": "extrahop_tags",
      "fields": {
        "mod_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/mod_time",
          "hide_notification": false,
          "id": 931,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mod time",
          "tooltip": "Tag modification time",
          "type_id": 1016,
          "uuid": "3da16404-eb26-428a-95d9-c22c422ca126",
          "values": [],
          "width": 108
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/query_execution_date",
          "hide_notification": false,
          "id": 932,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "ec8fcd62-3285-411d-abc2-6e0a92ec9a14",
          "values": [],
          "width": 167
        },
        "tag": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/tag",
          "hide_notification": false,
          "id": 933,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "tag",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tag",
          "tooltip": "Tag name",
          "type_id": 1016,
          "uuid": "842086e3-6e1a-4d5c-bed6-5bd33f313c08",
          "values": [],
          "width": 137
        },
        "tag_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/tag_id",
          "hide_notification": false,
          "id": 934,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "tag_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "Tag ID",
          "type_id": 1016,
          "uuid": "10a76105-22ed-4191-9154-30f37908f537",
          "values": [],
          "width": 98
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_tags",
      "uuid": "1bbbcc65-f200-4041-8445-da134d8eb6cb"
    },
    {
      "actions": [],
      "display_name": "ExtraHop Watchlist",
      "export_key": "extrahop_watchlist",
      "fields": {
        "display_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/display_name",
          "hide_notification": false,
          "id": 935,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "display_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Display name",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "0da314e0-a21b-4022-be04-5f25dd66baad",
          "values": [],
          "width": 140
        },
        "extrahop_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/extrahop_id",
          "hide_notification": false,
          "id": 936,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "extrahop_id",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ExtraHop ID",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "ef6bdb00-9852-4c35-b06e-7b73233d5e61",
          "values": [],
          "width": 156
        },
        "ipaddr4": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/ipaddr4",
          "hide_notification": false,
          "id": 937,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr4",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr4",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "db777ffc-8430-4b3c-a411-385320425bf7",
          "values": [],
          "width": 84
        },
        "ipaddr6": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/ipaddr6",
          "hide_notification": false,
          "id": 938,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr6",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr6",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "fcb8e407-4077-46d7-ba71-5ec6ec800d6e",
          "values": [],
          "width": 83
        },
        "macaddr": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/macaddr",
          "hide_notification": false,
          "id": 939,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "macaddr",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "MACaddr",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "67a77a85-93b4-4fc5-a27c-0749d959ab15",
          "values": [],
          "width": 128
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/query_execution_date",
          "hide_notification": false,
          "id": 940,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1017,
          "uuid": "a95bfd25-6f88-4193-8781-f3797e20c0e7",
          "values": [],
          "width": 147
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_watchlist",
      "uuid": "224bf5b6-346d-455a-a949-b62be7e74b90"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "wf_extrahop_rx_get_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx get devices\"\u003e\u003cdocumentation\u003eGet devices information from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lf3pjh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16ic9ye\" name=\"Extrahop revealx get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_devices\\\"\\nWF_NAME = \\\"Example: Extrahop revealx get devices\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Devices returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME)\\n        if devs:\\n            note_text += u\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\\".format(devs)\\n            for dev in devs:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                  f2 = f1\\n                  if f1.startswith(\\\"devs_\\\"):\\n                      f2 = f1.split(\u0027_\u0027, 1)[1]\\n                  if dev[f1] is None:\\n                      newrow[f1] = dev[f2]\\n                  elif isinstance(dev[f2], list):\\n                      newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n                  elif isinstance(dev[f2], bool):\\n                      newrow[f1] = str(dev[f2])\\n                  else:\\n                      newrow[f1] = \\\"{}\\\".format(dev[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get devices.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"if rule.properties.extrahop_active_from:\\n  inputs.extrahop_active_from = rule.properties.extrahop_active_from\\nif rule.properties.extrahop_active_until:\\n  inputs.extrahop_active_until = rule.properties.extrahop_active_until\\nif rule.properties.extrahop_limit:\\n  inputs.extrahop_limit = rule.properties.extrahop_limit\\nif rule.properties.extrahop_offset:\\n  inputs.extrahop_offset = rule.properties.extrahop_offset\\ninputs.extrahop_search_type = rule.properties.extrahop_search_type\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lf3pjh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10jo0yc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lf3pjh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16ic9ye\"/\u003e\u003cendEvent id=\"EndEvent_1tnn5yc\"\u003e\u003cincoming\u003eSequenceFlow_10jo0yc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10jo0yc\" sourceRef=\"ServiceTask_16ic9ye\" targetRef=\"EndEvent_1tnn5yc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16ic9ye\" id=\"ServiceTask_16ic9ye_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lf3pjh\" id=\"SequenceFlow_1lf3pjh_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tnn5yc\" id=\"EndEvent_1tnn5yc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"427\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"445\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10jo0yc\" id=\"SequenceFlow_10jo0yc_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "creator_id": "a@a.com",
      "description": "Get devices information from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698129817,
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "c0ea7fdb-37a1-4f70-92a1-2c427ea93232",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "wf_extrahop_rx_search_detections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_detections\" isExecutable=\"true\" name=\"Example: Extrahop revealx search detections\"\u003e\u003cdocumentation\u003eSearch for detections information from Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0v0udss\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bnujpl\" name=\"Extrahop revealx search detection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b70037a5-fcaf-4e78-a1e2-6acdc4dff239\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_detections post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_detections\\\"\\nWF_NAME = \\\"Example: Extrahop revealx search detections\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        dets = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Detections returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(dets), FN_NAME)\\n        if dets:\\n            note_text += u\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\\".format(dets)\\n            for det in dets:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"det_\\\"):\\n                      f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if det[f1] is None:\\n                        newrow[f1] = det[f2]\\n                    if isinstance(det[f1], list):\\n                      if f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                          newrow[f1] = \\\"{}\\\".format(det[f2])\\n                      else:\\n                          newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                    elif isinstance(det[f2], (bool, dict)):\\n                        newrow[f1] = str(det[f2])\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search detections.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_filter = rule.properties.extrahop_detection_search_filter.content\\nif inputs.extrahop_search_filter is None:\\n    raise ValueError(\\\"The search filter is not set\\\")\\nfor prop in [\\\"filter\\\", \\\"category\\\", \\\"assignee\\\", \\\"ticket_id\\\", \\\"status\\\", \\\"resolution\\\"]:\\n  if prop not in inputs.extrahop_search_filter:\\n    raise ValueError(\\\"The search filter is missing property \u0027{}\u0027\\\".format(prop))\\nif rule.properties.extrahop_active_from:\\n  inputs.extrahop_active_from = rule.properties.extrahop_active_from\\nif rule.properties.extrahop_active_until:\\n  inputs.extrahop_active_until = rule.properties.extrahop_active_until\\nif rule.properties.extrahop_limit:\\n  inputs.extrahop_limit = rule.properties.extrahop_limit\\nif rule.properties.extrahop_offset:\\n  inputs.extrahop_offset = rule.properties.extrahop_offset\\nif rule.properties.extrahop_update_time:\\n  inputs.extrahop_update_time = rule.properties.extrahop_update_time\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0v0udss\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17ve9fh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0v0udss\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bnujpl\"/\u003e\u003cendEvent id=\"EndEvent_0jhirff\"\u003e\u003cincoming\u003eSequenceFlow_17ve9fh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17ve9fh\" sourceRef=\"ServiceTask_1bnujpl\" targetRef=\"EndEvent_0jhirff\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bnujpl\" id=\"ServiceTask_1bnujpl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"242\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v0udss\" id=\"SequenceFlow_0v0udss_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"242\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0jhirff\" id=\"EndEvent_0jhirff_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"378\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"396\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17ve9fh\" id=\"SequenceFlow_17ve9fh_di\"\u003e\u003comgdi:waypoint x=\"342\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"360\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "a@a.com",
      "description": "Search for detections information from Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_search_detections",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698126078,
      "name": "Example: Extrahop revealx search detections",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_detections",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "7e68a246-23c6-40bd-8f0a-77217f69a01c",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_extrahop_rx_get_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_tags\" isExecutable=\"true\" name=\"Example: Extrahop revealx get tags\"\u003e\u003cdocumentation\u003eGet tags information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dns9ig\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_189ulsl\" name=\"Extrahop revealx get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_tags post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_tags\\\"\\nWF_NAME = \\\"Example: Extrahop revealx get tags\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TBL_FIELDS = [\\\"am_description\\\", \\\"am_id\\\", \\\"mod_time\\\", \\\"mode\\\", \\\"name\\\", \\\"owner\\\", \\\"rights\\\", \\\"short_code\\\", \\\"show_alert_status\\\", \\\"walks\\\", \\\"weighting\\\"]\\n\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        tags = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Tags returned for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, len(tags), FN_NAME)\\n        if tags:\\n            for tag in tags:\\n                newrow = incident.addRow(\\\"extrahop_tags\\\")\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                newrow.tag = tag.name\\n                newrow.mod_time = tag.mod_time\\n                newrow.tag_id = tag.id\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Tags\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get tags.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dns9ig\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vd5haa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dns9ig\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_189ulsl\"/\u003e\u003cendEvent id=\"EndEvent_0y9myii\"\u003e\u003cincoming\u003eSequenceFlow_0vd5haa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vd5haa\" sourceRef=\"ServiceTask_189ulsl\" targetRef=\"EndEvent_0y9myii\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_189ulsl\" id=\"ServiceTask_189ulsl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"244\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dns9ig\" id=\"SequenceFlow_1dns9ig_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"244\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"221\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y9myii\" id=\"EndEvent_0y9myii_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"388\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"406\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vd5haa\" id=\"SequenceFlow_0vd5haa_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"366\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@a.com",
      "description": "Get tags information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_tags",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698127081,
      "name": "Example: Extrahop revealx get tags",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_tags",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "3385d752-805c-4275-9092-4af1c3e9abe4",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_extrahop_rx_search_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx search devices\"\u003e\u003cdocumentation\u003eSearch for devices information from Extrahop Reveal(x) using a filter.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0m2u56o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10yatj6\" name=\"Extrahop revealx search devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7384abd-0046-4b46-97af-d34d8cc9c711\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_devices\\\"\\nWF_NAME = \\\"Example: Extrahop revealx search devices\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Devices returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME)\\n        if devs:\\n            note_text += u\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\\".format(devs)\\n            for dev in devs:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"devs_\\\"):\\n                        f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if dev[f1] is None:\\n                        newrow[f1] = dev[f2]\\n                    if isinstance(dev[f1], list):\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n                    elif isinstance(dev[f1], bool):\\n                        newrow[f1] = str(dev[f2])\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(dev[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search devices.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_filter = rule.properties.extrahop_device_search_filter.content\\nif inputs.extrahop_search_filter is None:\\n    raise ValueError(\\\"The search filter is not set\\\")\\nfor prop in [\\\"filter\\\", \\\"field\\\", \\\"operator\\\", \\\"operand\\\"]:\\n  if prop not in inputs.extrahop_search_filter:\\n    raise ValueError(\\\"The search filter is missing property \u0027{}\u0027\\\".format(prop))\\nif rule.properties.extrahop_active_from:\\n  inputs.extrahop_active_from = rule.properties.extrahop_active_from\\nif rule.properties.extrahop_active_until:\\n  inputs.extrahop_active_until = rule.properties.extrahop_active_until\\nif rule.properties.extrahop_limit:\\n  inputs.extrahop_limit = rule.properties.extrahop_limit\\nif rule.properties.extrahop_offset:\\n  inputs.extrahop_offset = rule.properties.extrahop_offset\\n\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0m2u56o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081bn3v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0m2u56o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_10yatj6\"/\u003e\u003cendEvent id=\"EndEvent_0t2xr17\"\u003e\u003cincoming\u003eSequenceFlow_081bn3v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081bn3v\" sourceRef=\"ServiceTask_10yatj6\" targetRef=\"EndEvent_0t2xr17\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10yatj6\" id=\"ServiceTask_10yatj6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0m2u56o\" id=\"SequenceFlow_0m2u56o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0t2xr17\" id=\"EndEvent_0t2xr17_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"375\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081bn3v\" id=\"SequenceFlow_081bn3v_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"355\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@a.com",
      "description": "Search for devices information from Extrahop Reveal(x) using a filter.",
      "export_key": "wf_extrahop_rx_search_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698129524,
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "7d82fa2a-339c-4306-9a2c-ab4886101e2e",
      "workflow_id": 99
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_extrahop_rx_get_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop revealx get watchlist\"\u003e\u003cdocumentation\u003eRetrieve all devices that are in the watchlist from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0j0orct\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03t8ciq\" name=\"Extrahop revealx get watchlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4d5690ce-998c-4fbb-bf25-765800aaa246\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_watchlist post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_watchlist\\\"\\nWF_NAME = \\\"Example: Extrahop revealx get watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_watchlist\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\", \\\"extrahop_id\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; devices returned in the Watchlist\\\" \\\\\\n                    u\\\" for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME)\\n        if devs:\\n            for dev in devs:\\n                newrow = incident.addRow(\\\"extrahop_watchlist\\\")\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                  f2 = f1\\n                  if dev[f1] is None:\\n                      newrow[f1] = dev[f2]\\n                  if isinstance(dev[f1], list):\\n                      newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n                  elif isinstance(dev[f1], bool):\\n                      newrow[f1] = str(dev[f2])\\n                  else:\\n                      newrow[f1] = \\\"{}\\\".format(dev[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get the watchlist.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0j0orct\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0u8wmby\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0j0orct\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03t8ciq\"/\u003e\u003cendEvent id=\"EndEvent_1nup12z\"\u003e\u003cincoming\u003eSequenceFlow_0u8wmby\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0u8wmby\" sourceRef=\"ServiceTask_03t8ciq\" targetRef=\"EndEvent_1nup12z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03t8ciq\" id=\"ServiceTask_03t8ciq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j0orct\" id=\"SequenceFlow_0j0orct_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nup12z\" id=\"EndEvent_1nup12z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"391\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u8wmby\" id=\"SequenceFlow_0u8wmby_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Retrieve all devices that are in the watchlist from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1646054285521,
      "name": "Example: Extrahop revealx get watchlist",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "1a397ec4-4b9c-41fc-a4c3-a302ac7de149",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "wf_extrahop_rx_update_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop revealx update watchlist\"\u003e\u003cdocumentation\u003eAdd or remove devices from the watchlist on Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_06dgzw4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xfdq4t\" name=\"Extrahop revealx update watchlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8d33930-3417-436e-82a1-267a5dc9fa91\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_watchlist post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_update_watchlist\\\"\\nWF_NAME = \\\"Example: Extrahop revealx update watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully updated the watchlist for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME)\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to update the watchlist for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME)\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Update watchlist failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME)\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to update the watchlist \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"search_devices_content = workflow.properties.search_devices_results.content\\naction = rule.properties.extrahop_watchlist_action\\ndevs = search_devices_content.result\\nif devs:\\n    dev_id = str(devs.pop()[\\\"id\\\"])\\n    if action == \\\"add\\\":\\n        inputs.extrahop_assign = dev_id\\n    elif action == \\\"remove\\\":\\n        inputs.extrahop_unassign = dev_id\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kxwk83\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fbq6er\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_08ib1fu\"\u003e\u003cincoming\u003eSequenceFlow_0fbq6er\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0kb3b4x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0fbq6er\" sourceRef=\"ServiceTask_0xfdq4t\" targetRef=\"EndEvent_08ib1fu\"/\u003e\u003cserviceTask id=\"ServiceTask_1tl00j8\" name=\"Extrahop revealx search devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7384abd-0046-4b46-97af-d34d8cc9c711\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_devices\\\"\\nWF_NAME = \\\"Example: Extrahop revealx update watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = CONTENT.result\\n        if devs:\\n            if len(devs) \u0026gt; 1:\\n                note_text += u\\\"ExtraHop Integration: Workflow: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; : There were too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned \\\" \\\\\\n                    u\\\"while attempting to search for a device to add to the watchlist \\\" \\\\\\n                    u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;\\\".format(WF_NAME, len(devs), FN_NAME)\\n            else:\\n                workflow.addProperty(\\\"device_exists\\\", {})\\n        else:\\n            note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; device returned while attempting \\\" \\\\\\n                  u\\\"to search for a device to add to the watchlist.\\\".format(WF_NAME, FN_NAME)\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search for a device to add to the watchlist.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"ip = artifact.value\\nsearch_filter = {\\n  \\\"filter\\\": {\\n    \\\"field\\\": \\\"ipaddr\\\",\\n    \\\"operand\\\": str(ip),\\n    \\\"operator\\\": \\\"=\\\"\\n  }\\n}\\ninputs.extrahop_search_filter = str(search_filter).replace(\\\"\u0027\\\", \u0027\\\"\u0027)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"search_devices_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_06dgzw4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hc4i9t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_06dgzw4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tl00j8\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1lo5m17\"\u003e\u003cincoming\u003eSequenceFlow_0hc4i9t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1kxwk83\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0kb3b4x\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0hc4i9t\" sourceRef=\"ServiceTask_1tl00j8\" targetRef=\"ExclusiveGateway_1lo5m17\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1kxwk83\" name=\"Device exists\" sourceRef=\"ExclusiveGateway_1lo5m17\" targetRef=\"ServiceTask_0xfdq4t\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"device_exists\\\", None)  != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0kb3b4x\" name=\"Device doesn\u0027t exist\" sourceRef=\"ExclusiveGateway_1lo5m17\" targetRef=\"EndEvent_08ib1fu\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"device_exists\\\", None)  == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xfdq4t\" id=\"ServiceTask_0xfdq4t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"507\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08ib1fu\" id=\"EndEvent_08ib1fu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"641\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"614\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fbq6er\" id=\"SequenceFlow_0fbq6er_di\"\u003e\u003comgdi:waypoint x=\"607\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"641\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"579\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tl00j8\" id=\"ServiceTask_1tl00j8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"231\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06dgzw4\" id=\"SequenceFlow_06dgzw4_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1lo5m17\" id=\"ExclusiveGateway_1lo5m17_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"377\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"402\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hc4i9t\" id=\"SequenceFlow_0hc4i9t_di\"\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kxwk83\" id=\"SequenceFlow_1kxwk83_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"507\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"69\" x=\"433\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kb3b4x\" id=\"SequenceFlow_0kb3b4x_di\"\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"304\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"304\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"77\" x=\"492\" y=\"283\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "a@a.com",
      "description": "Add or remove devices from the watchlist on Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_update_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698127577,
      "name": "Example: Extrahop revealx update watchlist",
      "object_type": "artifact",
      "programmatic_name": "wf_extrahop_rx_update_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "1063d67c-e3ed-4a3b-9c5c-aa88ce60c7c5",
      "workflow_id": 98
    },
    {
      "actions": [],
      "content": {
        "version": 35,
        "workflow_id": "wf_extrahop_rx_get_activitymaps",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_activitymaps\" isExecutable=\"true\" name=\"Example: Extrahop revealx get activitymaps\"\u003e\u003cdocumentation\u003eGet activitymaps information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_104u30s\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03b8xn3\" name=\"Extrahop revealx get activitymaps\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"18aa0964-745b-4329-a04b-a92f5f3fab40\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_activitymaps post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_activitymaps\\\"\\nWF_NAME = \\\"Example: Extrahop revealx get activitymaps\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_activitymaps\\\"\\nDATA_TBL_FIELDS = [\\\"ams_description\\\", \\\"ams_id\\\", \\\"mod_time\\\", \\\"mode\\\", \\\"ams_name\\\", \\\"owner\\\", \\\"rights\\\", \\\"short_code\\\",\\n                   \\\"show_alert_status\\\", \\\"walks\\\", \\\"weighting\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        ams = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Activitymaps returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(ams), FN_NAME)\\n        if ams:\\n            for am in ams:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"ams_\\\"):\\n                        f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if am[f2] is None:\\n                        newrow[f1] = am[f2]\\n                    if isinstance(am[f2], list):\\n                      if f1 in [\\\"walks\\\",\\\"steps\\\"]:\\n                          newrow[f1] = \\\"{}\\\".format(am[f2])\\n                      else:\\n                          newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(am[f2]))\\n                    elif isinstance(am[f2], (bool, dict)):\\n                        newrow[f1] = str(am[f2])\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(am[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Activitymaps\\\")\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get activitymaps.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_104u30s\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17yb9c4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_104u30s\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03b8xn3\"/\u003e\u003cendEvent id=\"EndEvent_03rpj82\"\u003e\u003cincoming\u003eSequenceFlow_17yb9c4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17yb9c4\" sourceRef=\"ServiceTask_03b8xn3\" targetRef=\"EndEvent_03rpj82\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03b8xn3\" id=\"ServiceTask_03b8xn3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_104u30s\" id=\"SequenceFlow_104u30s_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03rpj82\" id=\"EndEvent_03rpj82_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"399\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17yb9c4\" id=\"SequenceFlow_17yb9c4_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"376.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 35,
      "creator_id": "a@a.com",
      "description": "Get activitymaps information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_activitymaps",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698125587,
      "name": "Example: Extrahop revealx get activitymaps",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_activitymaps",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "37240452-0a4d-478b-83c4-2b8965d9fcb4",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "wf_extrahop_rx_assign_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_assign_tag\" isExecutable=\"true\" name=\"Example: Extrahop revealx assign tag\"\u003e\u003cdocumentation\u003eAssign a tag to a devices id for Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0l449vv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_04jmpas\" name=\"Extrahop revealx get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_tags_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0l449vv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_073ebus\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0l449vv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_04jmpas\"/\u003e\u003cserviceTask id=\"ServiceTask_1hdcy5r\" name=\"Extrahop revealx assign tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f0d2fc8c-20ab-440c-b4f5-46776a0b561e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_assign_tag post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_assign_tag\\\"\\nWF_NAME = \\\"Example: Extrahop revealx assign tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            device_id = INPUTS.get(\\\"extrahop_device_ids\\\")\\n            tag_id = INPUTS.get(\\\"extrahop_tag_id\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully assigned tag id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_id, device_id, FN_NAME)\\n\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to assign tag id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_id, device_id, FN_NAME)\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Assign tag id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_id, device_id, FN_NAME)\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to assign a tag id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, tag_id, device_id, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"tag_name = rule.properties.extrahop_tag_name\\nget_tags_content = workflow.properties.get_tags_result.content\\ninputs.extrahop_device_ids = row.devs_id\\nif tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\ninputs.extrahop_tag_id = None\\nfor tag in get_tags_content[\\\"result\\\"]:\\n    if tag_name == tag[\\\"name\\\"]:\\n        inputs.extrahop_tag_id = tag[\\\"id\\\"]\\n        break\\nif not inputs.extrahop_tag_id:\\n    raise ValueError(\\\"Tag {} not found.\\\".format(tag_name))\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_073ebus\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1db2q7n\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_073ebus\" sourceRef=\"ServiceTask_04jmpas\" targetRef=\"ServiceTask_1hdcy5r\"/\u003e\u003cendEvent id=\"EndEvent_0bh06jd\"\u003e\u003cincoming\u003eSequenceFlow_1db2q7n\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1db2q7n\" sourceRef=\"ServiceTask_1hdcy5r\" targetRef=\"EndEvent_0bh06jd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_04jmpas\" id=\"ServiceTask_04jmpas_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"239\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l449vv\" id=\"SequenceFlow_0l449vv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"239\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1hdcy5r\" id=\"ServiceTask_1hdcy5r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"399\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_073ebus\" id=\"SequenceFlow_073ebus_di\"\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"369\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0bh06jd\" id=\"EndEvent_0bh06jd_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"544\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"562\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1db2q7n\" id=\"SequenceFlow_1db2q7n_di\"\u003e\u003comgdi:waypoint x=\"499\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"521.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@a.com",
      "description": "Assign a tag to a devices id for Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_assign_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698128036,
      "name": "Example: Extrahop revealx assign tag",
      "object_type": "extrahop_devices",
      "programmatic_name": "wf_extrahop_rx_assign_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "6ab655c4-a62d-43bc-b896-a198871aef15",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "wf_extrahop_rx_create_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_create_tag\" isExecutable=\"true\" name=\"Example: Extrahop revealx create tag\"\u003e\u003cdocumentation\u003eCreate a new tag for  Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dto6o1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1km27wt\" name=\"Extrahop revealx create tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d566e4b3-6692-4599-a351-7530cdb4874e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_create_tag post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_create_tag\\\"\\nWF_NAME = \\\"Example: Extrahop revealx create tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully created tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag, FN_NAME)\\n            newrow = incident.addRow(\\\"extrahop_tags\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.tag = tag\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Tags\\\")\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to create tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag, FN_NAME)\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Create tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag, FN_NAME)\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to create a tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, tag, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_tag_name = rule.properties.extrahop_tag_name\\nif inputs.extrahop_tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dto6o1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0lqhvgt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dto6o1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1km27wt\"/\u003e\u003cendEvent id=\"EndEvent_1fv39zp\"\u003e\u003cincoming\u003eSequenceFlow_0lqhvgt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0lqhvgt\" sourceRef=\"ServiceTask_1km27wt\" targetRef=\"EndEvent_1fv39zp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1km27wt\" id=\"ServiceTask_1km27wt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"259\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dto6o1\" id=\"SequenceFlow_0dto6o1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"259\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1fv39zp\" id=\"EndEvent_1fv39zp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lqhvgt\" id=\"SequenceFlow_0lqhvgt_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"377.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@a.com",
      "description": "Create a new tag for  Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_create_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1645698129075,
      "name": "Example: Extrahop revealx create tag",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_create_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "ceb2ade6-72f4-490d-bae2-7824953d3c91",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 22,
        "workflow_id": "wf_extrahop_rx_get_detections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_detections\" isExecutable=\"true\" name=\"Example: Extrahop revealx get detections\"\u003e\u003cdocumentation\u003eGet detections information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0o3iz5f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_084ezxp\" name=\"Extrahop revealx get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_detections post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detections\\\"\\nWF_NAME = \\\"Example: Extrahop revealx get detections\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        dets = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Detections returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(dets), FN_NAME)\\n        note_text += u\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\\".format(dets)\\n        if dets:\\n            for det in dets:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"det_\\\"):\\n                      f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if det[f1] is None:\\n                        newrow[f1] = det[f2]\\n                    if isinstance(det[f1], list):\\n                      if f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                          newrow[f1] = \\\"{}\\\".format(det[f2])\\n                      else:\\n                          newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                    elif isinstance(det[f2], (bool, dict)):\\n                        newrow[f1] = str(det[f2])\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search detections.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_limit = rule.properties.extrahop_limit\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0o3iz5f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ordt64\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0o3iz5f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_084ezxp\"/\u003e\u003cendEvent id=\"EndEvent_0itl0u4\"\u003e\u003cincoming\u003eSequenceFlow_1ordt64\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ordt64\" sourceRef=\"ServiceTask_084ezxp\" targetRef=\"EndEvent_0itl0u4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_084ezxp\" id=\"ServiceTask_084ezxp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o3iz5f\" id=\"SequenceFlow_0o3iz5f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0itl0u4\" id=\"EndEvent_0itl0u4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ordt64\" id=\"SequenceFlow_1ordt64_di\"\u003e\u003comgdi:waypoint x=\"338\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"367\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 22,
      "creator_id": "a@a.com",
      "description": "Get detections information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_detections",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1646050195156,
      "name": "Example: Extrahop revealx get detections",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_detections",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "3415df1f-b5af-47e3-aea9-c7e22b11c854",
      "workflow_id": 96
    }
  ],
  "workspaces": []
}
