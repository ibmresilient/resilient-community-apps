{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "extrahop_device_id"
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop revealx assign tag",
      "id": 34,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx assign tag",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6ad4aaa4-74cd-4193-8211-e6c5ae27792c",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_assign_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get activitymaps",
      "id": 38,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get activitymaps",
      "object_type": "incident",
      "tags": [],
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
      "id": 30,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get detections",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac9f8677-a9e3-4bba-998b-9956748c88f2",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_detections"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get devices",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "57789c28-de6a-46b4-8819-16ea53859de6",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_devices"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get watchlist",
      "id": 35,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get watchlist",
      "object_type": "incident",
      "tags": [],
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
      "id": 29,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx search detections",
      "object_type": "incident",
      "tags": [],
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
      "id": 28,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "tags": [],
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
          "field_name": "incident.plan_status",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.extrahop_detection_id",
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
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop revealx update detection",
      "id": 37,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Extrahop revealx update detection",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "0f56d4b2-8f07-48e5-8207-3b25f4ffda99",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_update_detection"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx update watchlist",
      "id": 36,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx update watchlist",
      "object_type": "artifact",
      "tags": [],
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
  "export_date": 1636393373778,
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
      "id": 579,
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
      "tags": [],
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
      "id": 563,
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
      "tags": [],
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
      "export_key": "__function/extrahop_unassign",
      "hide_notification": false,
      "id": 571,
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
      "tags": [],
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
      "id": 570,
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
      "tags": [],
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
      "id": 548,
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
      "tags": [],
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
      "id": 552,
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
      "tags": [],
      "templates": [],
      "text": "extrahop_update_time",
      "tooltip": "Return detections that were updated on or after the specified date, expressed in milliseconds since the epoch.",
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
      "export_key": "__function/extrahop_offset",
      "hide_notification": false,
      "id": 551,
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
      "tags": [],
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
      "id": 578,
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
      "tags": [],
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
      "export_key": "__function/soar_inc_plan_status",
      "hide_notification": false,
      "id": 577,
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
      "tags": [],
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
      "export_key": "__function/extrahop_activitymap_id",
      "hide_notification": false,
      "id": 581,
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
      "tags": [],
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
      "id": 565,
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
      "tags": [],
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
      "export_key": "__function/extrahop_sort",
      "hide_notification": false,
      "id": 554,
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
      "tags": [],
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
      "id": 536,
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
      "tags": [],
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 576,
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
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "SOAR incident ID",
      "type_id": 11,
      "uuid": "130d1b04-3a9b-4687-ab6b-48faeb3033d4",
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
      "id": 580,
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
      "tags": [],
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
      "export_key": "__function/extrahop_detection_id",
      "hide_notification": false,
      "id": 558,
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
      "tags": [],
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
      "id": 555,
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
      "tags": [],
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
      "export_key": "__function/extrahop_tag_id",
      "hide_notification": false,
      "id": 569,
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
      "tags": [],
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
      "id": 550,
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
      "tags": [],
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
      "id": 549,
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
      "tags": [],
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
      "export_key": "__function/extrahop_device_id",
      "hide_notification": false,
      "id": 559,
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
      "tags": [],
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
      "export_key": "actioninvocation/extrahop_detection_search_filter",
      "hide_notification": false,
      "id": 560,
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
      "tags": [],
      "templates": [],
      "text": "Extrahop detection search filter",
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
      "id": 574,
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
      "tags": [],
      "templates": [],
      "text": "extrahop_watchlist_action",
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
          "value": 307
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "remove",
          "properties": null,
          "uuid": "302c895f-5535-4ac6-ab4c-7bd6de4294b1",
          "value": 308
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
      "id": 540,
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
      "tags": [],
      "templates": [],
      "text": "Extrahop device search filter",
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
      "export_key": "incident/extrahop_detection_id",
      "hide_notification": false,
      "id": 575,
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
      "tags": [],
      "templates": [],
      "text": "Extrahop detection ID",
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
      "created_date": 1635785099361,
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
      "id": 39,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635860418052,
      "name": "funct_extrahop_rx_assign_tag",
      "tags": [],
      "uuid": "f0d2fc8c-20ab-440c-b4f5-46776a0b561e",
      "version": 6,
      "view_items": [
        {
          "content": "f7117970-a76c-4505-87b3-5dbcc35eabdc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
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
          "object_type": "artifact",
          "programmatic_name": "wf_extrahop_rx_assign_tag",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        }
      ]
    },
    {
      "created_date": 1635526394849,
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
      "id": 38,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635769059563,
      "name": "funct_extrahop_rx_create_tag",
      "tags": [],
      "uuid": "d566e4b3-6692-4599-a351-7530cdb4874e",
      "version": 6,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    },
    {
      "created_date": 1636392482742,
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
      "id": 43,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1636392758765,
      "name": "funct_extrahop_rx_get_activitymaps",
      "tags": [],
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
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    },
    {
      "created_date": 1634748855771,
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
      "id": 2,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635768783227,
      "name": "funct_extrahop_rx_get_detections",
      "tags": [],
      "uuid": "fc71fc68-991e-4825-bc07-2191e58745f3",
      "version": 9,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1634229838220,
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
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635768794624,
      "name": "funct_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "75447029-32ca-4363-b753-bc970cee66d5",
      "version": 16,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        }
      ]
    },
    {
      "created_date": 1635520990181,
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
      "id": 37,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635860402634,
      "name": "funct_extrahop_rx_get_tags",
      "tags": [],
      "uuid": "55ced5bd-cd23-4212-b661-956fed40722b",
      "version": 8,
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
          "name": "Example: Extrahop revealx get tags",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_tags",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        }
      ]
    },
    {
      "created_date": 1635875831395,
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
      "id": 40,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635943208317,
      "name": "funct_extrahop_rx_get_watchlist",
      "tags": [],
      "uuid": "4d5690ce-998c-4fbb-bf25-765800aaa246",
      "version": 3,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop revealx get watchlist",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_watchlist",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1635417902829,
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
      "id": 36,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635768814946,
      "name": "funct_extrahop_rx_search_detections",
      "tags": [],
      "uuid": "b70037a5-fcaf-4e78-a1e2-6acdc4dff239",
      "version": 8,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        }
      ]
    },
    {
      "created_date": 1635258053984,
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
      "id": 35,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635768823701,
      "name": "funct_extrahop_rx_search_devices",
      "tags": [],
      "uuid": "e7384abd-0046-4b46-97af-d34d8cc9c711",
      "version": 11,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    },
    {
      "created_date": 1636044409786,
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
      "id": 42,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1636379849618,
      "name": "funct_extrahop_rx_update_detection",
      "tags": [],
      "uuid": "8ee5a0dc-d7d9-4d02-85a3-55d340a43aa0",
      "version": 13,
      "view_items": [
        {
          "content": "130d1b04-3a9b-4687-ab6b-48faeb3033d4",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop revealx update detection",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_detection",
          "tags": [],
          "uuid": null,
          "workflow_id": 13
        }
      ]
    },
    {
      "created_date": 1635943689780,
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
      "id": 41,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635947532835,
      "name": "funct_extrahop_rx_update_watchlist",
      "tags": [],
      "uuid": "b8d33930-3417-436e-82a1-267a5dc9fa91",
      "version": 5,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 79,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1636393348038,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1636393348038,
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
      "export_key": "extrahop",
      "name": "extrahop",
      "programmatic_name": "extrahop",
      "tags": [],
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
    "build_number": 6783,
    "major": 41,
    "minor": 0,
    "version": "41.0.6783"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 21,
        "workflow_id": "wf_extrahop_rx_search_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx search devices\"\u003e\u003cdocumentation\u003eSearch for devices information from Extrahop Reveal(x) using a filter.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0m2u56o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10yatj6\" name=\"Extrahop revealx search devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7384abd-0046-4b46-97af-d34d8cc9c711\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_filter = rule.properties.extrahop_search_filter.content\\nif inputs.extrahop_search_filter is None:\\n    raise ValueError(\\\"The search filter is not set\\\")\\nfor prop in [\\\"filter\\\", \\\"field\\\", \\\"operator\\\", \\\"operand\\\"]:\\n  if prop not in inputs.extrahop_search_filter:\\n    raise ValueError(\\\"The search filter is missing property \u0027{}\u0027\\\".format(prop))\\n\\n\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0m2u56o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081bn3v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0m2u56o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_10yatj6\"/\u003e\u003cendEvent id=\"EndEvent_0t2xr17\"\u003e\u003cincoming\u003eSequenceFlow_081bn3v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081bn3v\" sourceRef=\"ServiceTask_10yatj6\" targetRef=\"EndEvent_0t2xr17\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10yatj6\" id=\"ServiceTask_10yatj6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0m2u56o\" id=\"SequenceFlow_0m2u56o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0t2xr17\" id=\"EndEvent_0t2xr17_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"375\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081bn3v\" id=\"SequenceFlow_081bn3v_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"355\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 21,
      "creator_id": "a@a.com",
      "description": "Search for devices information from Extrahop Reveal(x) using a filter.",
      "export_key": "wf_extrahop_rx_search_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381237654,
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_devices",
      "tags": [],
      "uuid": "7d82fa2a-339c-4306-9a2c-ab4886101e2e",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_extrahop_rx_get_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_tags\" isExecutable=\"true\" name=\"Example: Extrahop revealx get tags\"\u003e\u003cdocumentation\u003eGet tags information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dns9ig\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_189ulsl\" name=\"Extrahop revealx get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dns9ig\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vd5haa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dns9ig\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_189ulsl\"/\u003e\u003cendEvent id=\"EndEvent_0y9myii\"\u003e\u003cincoming\u003eSequenceFlow_0vd5haa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vd5haa\" sourceRef=\"ServiceTask_189ulsl\" targetRef=\"EndEvent_0y9myii\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_189ulsl\" id=\"ServiceTask_189ulsl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"244\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dns9ig\" id=\"SequenceFlow_1dns9ig_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"244\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"221\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y9myii\" id=\"EndEvent_0y9myii_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"388\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"406\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vd5haa\" id=\"SequenceFlow_0vd5haa_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"366\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@a.com",
      "description": "Get tags information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_tags",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381163336,
      "name": "Example: Extrahop revealx get tags",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_tags",
      "tags": [],
      "uuid": "3385d752-805c-4275-9092-4af1c3e9abe4",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "wf_extrahop_rx_update_detection",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_detection\" isExecutable=\"true\" name=\"Example: Extrahop revealx update detection\"\u003e\u003cdocumentation\u003eUpdate a detection in Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1cnettx\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00ubu6s\" name=\"Extrahop revealx update detection\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8ee5a0dc-d7d9-4d02-85a3-55d340a43aa0\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.extrahop_detection_id = incident.properties.extrahop_detection_id\\ninputs.soar_inc_owner_id = incident.owner_id\\ninputs.soar_inc_resolution_id = incident.resolution_id\\ninputs.soar_inc_plan_status = incident.plan_status\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1cnettx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fvygiq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1cnettx\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00ubu6s\"/\u003e\u003cendEvent id=\"EndEvent_0eleim3\"\u003e\u003cincoming\u003eSequenceFlow_0fvygiq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0fvygiq\" sourceRef=\"ServiceTask_00ubu6s\" targetRef=\"EndEvent_0eleim3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00ubu6s\" id=\"ServiceTask_00ubu6s_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"253\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cnettx\" id=\"SequenceFlow_1cnettx_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"225.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0eleim3\" id=\"EndEvent_0eleim3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"421\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fvygiq\" id=\"SequenceFlow_0fvygiq_di\"\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"387\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "creator_id": "a@a.com",
      "description": "Update a detection in Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_update_detection",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381264376,
      "name": "Example: Extrahop revealx update detection",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_update_detection",
      "tags": [],
      "uuid": "3daa437a-0baf-4091-bf7f-745825e87438",
      "workflow_id": 13
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_extrahop_rx_search_detections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_detections\" isExecutable=\"true\" name=\"Example: Extrahop revealx search detections\"\u003e\u003cdocumentation\u003eSearch for detections information from Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0v0udss\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bnujpl\" name=\"Extrahop revealx search detection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b70037a5-fcaf-4e78-a1e2-6acdc4dff239\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_filter = rule.properties.extrahop_detection_search_filter.content\\nif inputs.extrahop_search_filter is None:\\n    raise ValueError(\\\"The search filter is not set\\\")\\nfor prop in [\\\"filter\\\", \\\"category\\\", \\\"assignee\\\", \\\"ticket_id\\\", \\\"status\\\", \\\"resolution\\\"]:\\n  if prop not in inputs.extrahop_search_filter:\\n    raise ValueError(\\\"The search filter is missing property \u0027{}\u0027\\\".format(prop))\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0v0udss\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17ve9fh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0v0udss\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bnujpl\"/\u003e\u003cendEvent id=\"EndEvent_0jhirff\"\u003e\u003cincoming\u003eSequenceFlow_17ve9fh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17ve9fh\" sourceRef=\"ServiceTask_1bnujpl\" targetRef=\"EndEvent_0jhirff\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bnujpl\" id=\"ServiceTask_1bnujpl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"242\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v0udss\" id=\"SequenceFlow_0v0udss_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"242\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0jhirff\" id=\"EndEvent_0jhirff_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"378\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"396\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17ve9fh\" id=\"SequenceFlow_17ve9fh_di\"\u003e\u003comgdi:waypoint x=\"342\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"360\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Search for detections information from Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_search_detections",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381212671,
      "name": "Example: Extrahop revealx search detections",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_detections",
      "tags": [],
      "uuid": "7e68a246-23c6-40bd-8f0a-77217f69a01c",
      "workflow_id": 5
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "wf_extrahop_rx_get_activitymaps",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_activitymaps\" isExecutable=\"true\" name=\"Example: Extrahop revealx get activitymaps\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_104u30s\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03b8xn3\" name=\"Extrahop revealx get activitymaps\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"18aa0964-745b-4329-a04b-a92f5f3fab40\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_104u30s\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17yb9c4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_104u30s\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03b8xn3\"/\u003e\u003cendEvent id=\"EndEvent_03rpj82\"\u003e\u003cincoming\u003eSequenceFlow_17yb9c4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17yb9c4\" sourceRef=\"ServiceTask_03b8xn3\" targetRef=\"EndEvent_03rpj82\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03b8xn3\" id=\"ServiceTask_03b8xn3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_104u30s\" id=\"SequenceFlow_104u30s_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03rpj82\" id=\"EndEvent_03rpj82_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"399\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17yb9c4\" id=\"SequenceFlow_17yb9c4_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"376.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@a.com",
      "description": "",
      "export_key": "wf_extrahop_rx_get_activitymaps",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636393195075,
      "name": "Example: Extrahop revealx get activitymaps",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_activitymaps",
      "tags": [],
      "uuid": "37240452-0a4d-478b-83c4-2b8965d9fcb4",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_extrahop_rx_assign_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_assign_tag\" isExecutable=\"true\" name=\"Example: Extrahop revealx assign tag\"\u003e\u003cdocumentation\u003eAssign a tag to a devices id for Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00jmg5k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0twwdja\" name=\"Extrahop revealx assign tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f0d2fc8c-20ab-440c-b4f5-46776a0b561e\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_device_ids = artifact.value\\ninputs.extrahop_tag_id = 1\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00jmg5k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ydkfof\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_05plo24\"\u003e\u003cincoming\u003eSequenceFlow_1ydkfof\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ydkfof\" sourceRef=\"ServiceTask_0twwdja\" targetRef=\"EndEvent_05plo24\"/\u003e\u003csequenceFlow id=\"SequenceFlow_00jmg5k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0twwdja\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0twwdja\" id=\"ServiceTask_0twwdja_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"327\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05plo24\" id=\"EndEvent_05plo24_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"547\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"520\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ydkfof\" id=\"SequenceFlow_1ydkfof_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"442\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00jmg5k\" id=\"SequenceFlow_00jmg5k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"327\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"217.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@a.com",
      "description": "Assign a tag to a devices id for Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_assign_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1635860556746,
      "name": "Example: Extrahop revealx assign tag",
      "object_type": "artifact",
      "programmatic_name": "wf_extrahop_rx_assign_tag",
      "tags": [],
      "uuid": "224f8e6a-eb3f-4263-b8b1-4ccdadddcdb2",
      "workflow_id": 9
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "wf_extrahop_rx_update_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop revealx update watchlist\"\u003e\u003cdocumentation\u003eAdd or remove devices from the watchlist on Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ext1r1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xfdq4t\" name=\"Extrahop revealx update watchlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8d33930-3417-436e-82a1-267a5dc9fa91\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"action = rule.properties.extrahop_watchlist_action\\nif action == \\\"add\\\":\\n    inputs.extrahop_assign = artifact.value\\nelif action == \\\"remove\\\":\\n    inputs.extrahop_unassign = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ext1r1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fbq6er\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ext1r1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xfdq4t\"/\u003e\u003cendEvent id=\"EndEvent_08ib1fu\"\u003e\u003cincoming\u003eSequenceFlow_0fbq6er\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0fbq6er\" sourceRef=\"ServiceTask_0xfdq4t\" targetRef=\"EndEvent_08ib1fu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xfdq4t\" id=\"ServiceTask_0xfdq4t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ext1r1\" id=\"SequenceFlow_1ext1r1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08ib1fu\" id=\"EndEvent_08ib1fu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"387\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"405\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fbq6er\" id=\"SequenceFlow_0fbq6er_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"369\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "a@a.com",
      "description": "Add or remove devices from the watchlist on Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_update_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381289262,
      "name": "Example: Extrahop revealx update watchlist",
      "object_type": "artifact",
      "programmatic_name": "wf_extrahop_rx_update_watchlist",
      "tags": [],
      "uuid": "1063d67c-e3ed-4a3b-9c5c-aa88ce60c7c5",
      "workflow_id": 11
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "wf_extrahop_rx_get_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop revealx get watchlist\"\u003e\u003cdocumentation\u003eRetrieve all devices that are in the watchlist from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0j0orct\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03t8ciq\" name=\"Extrahop revealx get watchlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4d5690ce-998c-4fbb-bf25-765800aaa246\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0j0orct\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0u8wmby\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0j0orct\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03t8ciq\"/\u003e\u003cendEvent id=\"EndEvent_1nup12z\"\u003e\u003cincoming\u003eSequenceFlow_0u8wmby\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0u8wmby\" sourceRef=\"ServiceTask_03t8ciq\" targetRef=\"EndEvent_1nup12z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03t8ciq\" id=\"ServiceTask_03t8ciq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j0orct\" id=\"SequenceFlow_0j0orct_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nup12z\" id=\"EndEvent_1nup12z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"391\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u8wmby\" id=\"SequenceFlow_0u8wmby_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "a@a.com",
      "description": "Retrieve all devices that are in the watchlist from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381191214,
      "name": "Example: Extrahop revealx get watchlist",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_watchlist",
      "tags": [],
      "uuid": "1a397ec4-4b9c-41fc-a4c3-a302ac7de149",
      "workflow_id": 10
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_extrahop_rx_get_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx get devices\"\u003e\u003cdocumentation\u003eGet devices information from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lf3pjh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16ic9ye\" name=\"Extrahop revealx get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_type =\\\"any\\\"\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lf3pjh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10jo0yc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lf3pjh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16ic9ye\"/\u003e\u003cendEvent id=\"EndEvent_1tnn5yc\"\u003e\u003cincoming\u003eSequenceFlow_10jo0yc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10jo0yc\" sourceRef=\"ServiceTask_16ic9ye\" targetRef=\"EndEvent_1tnn5yc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16ic9ye\" id=\"ServiceTask_16ic9ye_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lf3pjh\" id=\"SequenceFlow_1lf3pjh_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tnn5yc\" id=\"EndEvent_1tnn5yc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"427\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"445\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10jo0yc\" id=\"SequenceFlow_10jo0yc_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@a.com",
      "description": "Get devices information from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381136715,
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "c0ea7fdb-37a1-4f70-92a1-2c427ea93232",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_extrahop_rx_get_detections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_detections\" isExecutable=\"true\" name=\"Example: Extrahop revealx get detections\"\u003e\u003cdocumentation\u003eGet detections information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0o3iz5f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_084ezxp\" name=\"Extrahop revealx get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0o3iz5f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ordt64\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0o3iz5f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_084ezxp\"/\u003e\u003cendEvent id=\"EndEvent_0itl0u4\"\u003e\u003cincoming\u003eSequenceFlow_1ordt64\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ordt64\" sourceRef=\"ServiceTask_084ezxp\" targetRef=\"EndEvent_0itl0u4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_084ezxp\" id=\"ServiceTask_084ezxp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o3iz5f\" id=\"SequenceFlow_0o3iz5f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0itl0u4\" id=\"EndEvent_0itl0u4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ordt64\" id=\"SequenceFlow_1ordt64_di\"\u003e\u003comgdi:waypoint x=\"338\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"367\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Get detections information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_detections",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381103760,
      "name": "Example: Extrahop revealx get detections",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_detections",
      "tags": [],
      "uuid": "3415df1f-b5af-47e3-aea9-c7e22b11c854",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_extrahop_rx_create_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_create_tag\" isExecutable=\"true\" name=\"Example: Extrahop revealx create tag\"\u003e\u003cdocumentation\u003eCreate a new tag for  Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dto6o1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1km27wt\" name=\"Extrahop revealx create tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d566e4b3-6692-4599-a351-7530cdb4874e\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_tag_name = rule.properties.extrahop_tag_name\\nif inputs.extrahop_tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\n\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dto6o1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0lqhvgt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dto6o1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1km27wt\"/\u003e\u003cendEvent id=\"EndEvent_1fv39zp\"\u003e\u003cincoming\u003eSequenceFlow_0lqhvgt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0lqhvgt\" sourceRef=\"ServiceTask_1km27wt\" targetRef=\"EndEvent_1fv39zp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1km27wt\" id=\"ServiceTask_1km27wt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"259\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dto6o1\" id=\"SequenceFlow_0dto6o1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"259\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1fv39zp\" id=\"EndEvent_1fv39zp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lqhvgt\" id=\"SequenceFlow_0lqhvgt_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"377.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Create a new tag for  Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_create_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1636381078925,
      "name": "Example: Extrahop revealx create tag",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_create_tag",
      "tags": [],
      "uuid": "ceb2ade6-72f4-490d-bae2-7824953d3c91",
      "workflow_id": 7
    }
  ],
  "workspaces": []
}
