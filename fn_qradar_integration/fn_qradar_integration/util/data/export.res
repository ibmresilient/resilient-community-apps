{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Add Item to this Reference Set",
      "id": 117,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Add Item to this Reference Set",
      "object_type": "qradar_reference_set",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d78fcd92-8cb8-42e0-8a57-9d1ac4210308",
      "view_items": [
        {
          "content": "04e83f93-0f11-45b2-bfa3-617b36c031ae",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "qradar_add_reference_set_item"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Add Item to this Reference Table",
      "id": 84,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Add Item to this Reference Table",
      "object_type": "qradar_reference_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bd0cb0ee-eb93-4b59-a93a-f5e0a7a38c87",
      "view_items": [
        {
          "content": "3db539de-c782-4327-be2e-6a16367616a9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f1268a24-803e-4165-8167-7c7210775a13",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "76916f18-75f7-49f8-be4d-a8edd2f83a13",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_qradar__add_reference_table_item_dt"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "qradar_reference_table_queried_rows.status",
          "method": "not_equals",
          "type": null,
          "value": "deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: QRadar - Delete this Reference Table Item",
      "id": 85,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Delete this Reference Table Item",
      "object_type": "qradar_reference_table_queried_rows",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "26573c4c-61a7-4ee9-bed9-0b0855a1b9ee",
      "view_items": [],
      "workflows": [
        "example_qradar__delete_reference_table_item_dt"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Find All Reference Sets with Artifact",
      "id": 119,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Find All Reference Sets with Artifact",
      "object_type": "qradar_servers",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1b0f4f09-caa8-4ff0-afa3-07b77e9be7a0",
      "view_items": [
        {
          "content": "04e83f93-0f11-45b2-bfa3-617b36c031ae",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "qradar_find_reference_sets_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Find in Reference Set",
      "id": 116,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Find in Reference Set",
      "object_type": "qradar_reference_set",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "137a10f9-482b-4963-a5d9-733bb78a63dc",
      "view_items": [
        {
          "content": "04e83f93-0f11-45b2-bfa3-617b36c031ae",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "qradar_find_reference_set_item"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Gather Reference Table Data",
      "id": 86,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Gather Reference Table Data",
      "object_type": "qradar_reference_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "52114e07-f585-4a09-83b1-595a2b629bf4",
      "view_items": [],
      "workflows": [
        "qradar_get_reference_table_data"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Get all Reference Tables",
      "id": 114,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Get all Reference Tables",
      "object_type": "qradar_servers",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f504be85-46b4-427a-bc84-03d3d0e13786",
      "view_items": [],
      "workflows": [
        "example_qradar__get_all_reference_tables"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Move from one Reference Set to another Reference Set",
      "id": 118,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Move from one Reference Set to another Reference Set",
      "object_type": "qradar_reference_set",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4b4f275f-d605-43e1-a14b-6dd1a21d18dd",
      "view_items": [
        {
          "content": "2cfc91b4-ec90-4d2d-ae34-9373cfb3625d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "04e83f93-0f11-45b2-bfa3-617b36c031ae",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "qradar_move_item_to_different_ref_set"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: QRadar - Search for offense id",
      "id": 94,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Search for offense id",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c82db24e-8fed-4e73-9b72-304cc1308148",
      "view_items": [
        {
          "content": "d46dc683-2d1e-4269-be07-317ba6d5398f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69a95edd-b20f-488a-9a9d-ef01aae3b740",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "qradar_search_event_offense"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "qradar_reference_table_queried_rows.status",
          "method": "not_equals",
          "type": null,
          "value": "deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: QRadar - Update this Reference Table Item",
      "id": 101,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: QRadar - Update this Reference Table Item",
      "object_type": "qradar_reference_table_queried_rows",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a1d17e72-9fc6-404d-91ec-67fa0e037b99",
      "view_items": [
        {
          "content": "3db539de-c782-4327-be2e-6a16367616a9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f1268a24-803e-4165-8167-7c7210775a13",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "76916f18-75f7-49f8-be4d-a8edd2f83a13",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_qradar__update_this_reference_table_item"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1628610571243,
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
      "export_key": "__function/qradar_query_param2",
      "hide_notification": false,
      "id": 358,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_param2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_param2",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9d8fc645-5067-4ab0-b151-1d106dad91d6",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_label",
      "hide_notification": false,
      "id": 387,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "qradar_label",
      "tooltip": "Enter name of QRadar server to use from the app.config",
      "type_id": 11,
      "uuid": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_reference_set_name",
      "hide_notification": false,
      "id": 364,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_set_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_set_name",
      "tooltip": "Name of a QRadar reference set",
      "type_id": 11,
      "uuid": "aa5e211d-b5e0-4289-88bb-47595afac385",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_reference_table_item_value",
      "hide_notification": false,
      "id": 361,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_table_item_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_table_item_value",
      "tooltip": "Value of a QRadar reference table item",
      "type_id": 11,
      "uuid": "b4571837-c795-4ead-99fe-0fb86c034355",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_param3",
      "hide_notification": false,
      "id": 357,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_param3",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_param3",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b6053690-d7b2-4204-b48a-f86503b419d9",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_reference_table_item_outer_key",
      "hide_notification": false,
      "id": 354,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_table_item_outer_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_table_item_outer_key",
      "tooltip": "The outer key for a QRadar Reference Table ",
      "type_id": 11,
      "uuid": "bb68e39f-e677-47d5-9877-c89c572410f2",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_range_start",
      "hide_notification": false,
      "id": 362,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_range_start",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_range_start",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c33fbe1d-125c-4a79-82e8-6608d1c7bb5e",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_range_end",
      "hide_notification": false,
      "id": 363,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_range_end",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_range_end",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d21f2814-40e6-4f7a-b269-6ff2c7a3196e",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_all_results",
      "hide_notification": false,
      "id": 356,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_all_results",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_all_results",
      "tooltip": "Display all results from search. By default, a range for the number of returned results is set.",
      "type_id": 11,
      "uuid": "d7a544ff-689b-4f15-b3c1-a7ebd20bbf3b",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Yes",
          "properties": null,
          "uuid": "d480e32c-fd0d-4c0c-850f-390bf3a7dbe8",
          "value": 162
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "No",
          "properties": null,
          "uuid": "54c4eb52-d955-4e05-9f76-c3819853ff68",
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
      "export_key": "__function/qradar_reference_set_item_value",
      "hide_notification": false,
      "id": 366,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_set_item_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_set_item_value",
      "tooltip": "Value of a QRadar reference set item",
      "type_id": 11,
      "uuid": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_reference_table_item_inner_key",
      "hide_notification": false,
      "id": 355,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_table_item_inner_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_table_item_inner_key",
      "tooltip": "The inner key for a QRadar Reference Table ",
      "type_id": 11,
      "uuid": "ea049a47-2536-4bf5-9a8f-6aa1626430ba",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_param4",
      "hide_notification": false,
      "id": 360,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_param4",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_param4",
      "tooltip": "",
      "type_id": 11,
      "uuid": "eefc9e56-2806-4534-b409-42e25154ecc9",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_param1",
      "hide_notification": false,
      "id": 353,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_param1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_param1",
      "tooltip": "",
      "type_id": 11,
      "uuid": "01ed4652-fe61-4dbf-bc83-f81c62c5563c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query",
      "hide_notification": false,
      "id": 359,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [
        {
          "id": 13,
          "name": "search ip address",
          "template": {
            "content": "SELECT %param1% FROM events WHERE sourceip=\u0027%param2%\u0027 LAST %param3% MINUTES",
            "format": "text"
          },
          "uuid": "dcbdb7c8-2068-4e97-8127-57131cbdccbf"
        },
        {
          "id": 14,
          "name": "search events for offense_id",
          "template": {
            "content": "SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% MINUTES",
            "format": "text"
          },
          "uuid": "2b88eb5c-504a-4950-8674-0cf8f56f1a83"
        },
        {
          "id": 15,
          "name": "search events for username",
          "template": {
            "content": "SELECT %param1% FROM events WHERE username=%param2% LAST %param3% MINUTES",
            "format": "text"
          },
          "uuid": "34fa3300-c28c-4346-8d3b-745a1afa75dc"
        }
      ],
      "text": "qradar_query",
      "tooltip": "A qradar query string with parameters",
      "type_id": 11,
      "uuid": "048ba39a-ab94-4d1f-a0f8-2462de3c044c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_reference_table_name",
      "hide_notification": false,
      "id": 365,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_table_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_reference_table_name",
      "tooltip": "Value of a QRadar reference table item",
      "type_id": 11,
      "uuid": "0bf3b72c-f8a4-4b45-af51-4014b822b162",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/qradar_query_param5",
      "hide_notification": false,
      "id": 367,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_param5",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_enhanced_data",
          "value": null
        },
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_query_param5",
      "tooltip": "",
      "type_id": 11,
      "uuid": "19778fc0-9a30-4b8b-9c21-642495f9eebc",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_query_all_results",
      "hide_notification": false,
      "id": 350,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_query_all_results",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "QRadar Query all Results",
      "tooltip": "Display all results from search. By default, a range for the number of returned results is set.",
      "type_id": 6,
      "uuid": "d46dc683-2d1e-4269-be07-317ba6d5398f",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Yes",
          "properties": null,
          "uuid": "f9ad4248-be8f-4bf1-8dd3-bf95a1b194ca",
          "value": 160
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "No",
          "properties": null,
          "uuid": "abda100b-3058-4683-82f8-23d65e1addc8",
          "value": 161
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
      "export_key": "actioninvocation/qradar_ref_table_inner_key",
      "hide_notification": false,
      "id": 348,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_ref_table_inner_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "Inner Key",
      "tooltip": "",
      "type_id": 6,
      "uuid": "f1268a24-803e-4165-8167-7c7210775a13",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_reference_set_item_value",
      "hide_notification": false,
      "id": 488,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_set_item_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "QRadar reference set item value",
      "tooltip": "Value of QRadar reference set item",
      "type_id": 6,
      "uuid": "04e83f93-0f11-45b2-bfa3-617b36c031ae",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_reference_set_name_to_move_to",
      "hide_notification": false,
      "id": 498,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_reference_set_name_to_move_to",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "QRadar reference set name to move to",
      "tooltip": "Enter reference set to move item to",
      "type_id": 6,
      "uuid": "2cfc91b4-ec90-4d2d-ae34-9373cfb3625d",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_ref_table_outer_key",
      "hide_notification": false,
      "id": 351,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_ref_table_outer_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "Outer Key",
      "tooltip": "",
      "type_id": 6,
      "uuid": "3db539de-c782-4327-be2e-6a16367616a9",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_label",
      "hide_notification": false,
      "id": 386,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "QRadar Label",
      "tooltip": "Enter the name of the server you would like to use",
      "type_id": 6,
      "uuid": "69a95edd-b20f-488a-9a9d-ef01aae3b740",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/qradar_ref_table_update",
      "hide_notification": false,
      "id": 352,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_ref_table_update",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_integration",
          "value": null
        }
      ],
      "templates": [],
      "text": "Update Value",
      "tooltip": "",
      "type_id": 6,
      "uuid": "76916f18-75f7-49f8-be4d-a8edd2f83a13",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "incident/qradar_id",
      "hide_notification": false,
      "id": 466,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "qradar_id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "aedb7df6-642a-4438-824d-fe24be34cfc0",
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
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Add an item to a given QRadar reference set",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Add Reference Set Item",
      "export_key": "qradar_add_reference_set_item",
      "id": 77,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1628183339863,
      "name": "qradar_add_reference_set_item",
      "tags": [],
      "uuid": "30b6899a-d015-48c3-8fd9-500788d4b437",
      "version": 1,
      "view_items": [
        {
          "content": "aa5e211d-b5e0-4289-88bb-47595afac385",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Add Reference Set Item",
          "object_type": "qradar_reference_set",
          "programmatic_name": "qradar_add_reference_set_item",
          "tags": [],
          "uuid": null,
          "workflow_id": 104
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: QRadar - Move Item from one Reference Set to another",
          "object_type": "qradar_reference_set",
          "programmatic_name": "qradar_move_item_to_different_ref_set",
          "tags": [],
          "uuid": null,
          "workflow_id": 109
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Delete an item from a given QRadar reference set",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Delete Reference Set Item",
      "export_key": "qradar_delete_reference_set_item",
      "id": 78,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1628183339968,
      "name": "qradar_delete_reference_set_item",
      "tags": [],
      "uuid": "a7dc3d26-ab97-44a3-b56a-e367315b08e0",
      "version": 1,
      "view_items": [
        {
          "content": "aa5e211d-b5e0-4289-88bb-47595afac385",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Delete Reference Set Item",
          "object_type": "qradar_reference_set_queried_rows",
          "programmatic_name": "example_qradar__delete_reference_set_item",
          "tags": [],
          "uuid": null,
          "workflow_id": 113
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: QRadar - Move Item from one Reference Set to another",
          "object_type": "qradar_reference_set",
          "programmatic_name": "qradar_move_item_to_different_ref_set",
          "tags": [],
          "uuid": null,
          "workflow_id": 109
        }
      ]
    },
    {
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Return all of the reference sets on a given QRadar server",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Find All Reference Sets",
      "export_key": "qradar_find_all_reference_sets",
      "id": 82,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628273498985,
      "name": "qradar_find_all_reference_sets",
      "tags": [],
      "uuid": "48e76c4d-4f63-4db1-a49d-4466afa384f4",
      "version": 1,
      "view_items": [
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Find All Reference Sets",
          "object_type": "qradar_servers",
          "programmatic_name": "example_qradar__find_all_reference_sets",
          "tags": [],
          "uuid": null,
          "workflow_id": 105
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Find an item in a given QRadar reference set",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Find Reference Set Item",
      "export_key": "qradar_find_reference_set_item",
      "id": 79,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1628183340078,
      "name": "qradar_find_reference_set_item",
      "tags": [],
      "uuid": "9d817ee3-a8cf-4a0a-a8a6-969f6090f276",
      "version": 1,
      "view_items": [
        {
          "content": "aa5e211d-b5e0-4289-88bb-47595afac385",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Find Item in Reference Set",
          "object_type": "qradar_reference_set",
          "programmatic_name": "qradar_find_reference_set_item",
          "tags": [],
          "uuid": null,
          "workflow_id": 108
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Find reference sets that contain a given item value, together with information about this item in those reference sets. Information includes whether this item is added to the reference set manually or by a rule.",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Find Reference Sets",
      "export_key": "qradar_find_reference_sets",
      "id": 80,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1628183340196,
      "name": "qradar_find_reference_sets",
      "tags": [],
      "uuid": "09885813-f640-45bc-8892-d1a741a7d53e",
      "version": 1,
      "view_items": [
        {
          "content": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Find all Reference Sets for artifact",
          "object_type": "qradar_servers",
          "programmatic_name": "qradar_find_reference_sets_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 107
        }
      ]
    },
    {
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Return all of the servers in the app.config",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Get all Servers",
      "export_key": "qradar_get_all_servers",
      "id": 81,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628255636776,
      "name": "qradar_get_all_servers",
      "tags": [],
      "uuid": "8ae32a72-2783-4501-80b7-a58240eab8f0",
      "version": 2,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: QRadar - Get all Servers",
          "object_type": "incident",
          "programmatic_name": "example_qradar__get_all_servers",
          "tags": [],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    },
    {
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get the elements in a specified reference set",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Get Reference Set Data",
      "export_key": "qradar_get_reference_set_data",
      "id": 83,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628528654742,
      "name": "qradar_get_reference_set_data",
      "tags": [],
      "uuid": "e216a4d3-d6ca-4894-a5c9-78a38d9ab477",
      "version": 1,
      "view_items": [
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa5e211d-b5e0-4289-88bb-47595afac385",
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
          "name": "Example: QRadar - Get Reference Set Data",
          "object_type": "qradar_reference_set",
          "programmatic_name": "example_qradar__get_reference_set_data",
          "tags": [],
          "uuid": null,
          "workflow_id": 110
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Get all reference tables from a QRadar instance",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Table Get All Tables",
      "export_key": "qradar_get_reference_tables",
      "id": 71,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174546145,
      "name": "qradar_get_reference_tables",
      "tags": [],
      "uuid": "0abff118-314e-4728-964d-03558088a62a",
      "version": 2,
      "view_items": [
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Get All Reference Tables",
          "object_type": "qradar_servers",
          "programmatic_name": "example_qradar__get_all_reference_tables",
          "tags": [],
          "uuid": null,
          "workflow_id": 97
        }
      ]
    },
    {
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update an item in a given QRadar reference set",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Set Update Item",
      "export_key": "qradar_reference_set_update_item",
      "id": 84,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628606226787,
      "name": "qradar_reference_set_update_item",
      "tags": [],
      "uuid": "c6f020a4-2ec3-4030-bf58-86b53a26059e",
      "version": 3,
      "view_items": [
        {
          "content": "aa5e211d-b5e0-4289-88bb-47595afac385",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db5af2ee-cb1a-46c7-82ff-c6f88a5aa7e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Update this Reference Set Item",
          "object_type": "qradar_reference_set_queried_rows",
          "programmatic_name": "example_qradar__update_this_reference_set_item",
          "tags": [],
          "uuid": null,
          "workflow_id": 112
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Add an item to a given QRadar reference table",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Table Add Item",
      "export_key": "qradar_reference_table_add_item",
      "id": 72,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174534409,
      "name": "qradar_reference_table_add_item",
      "tags": [],
      "uuid": "2843283c-4d98-4c71-b2e3-b0636c7a0df8",
      "version": 2,
      "view_items": [
        {
          "content": "0bf3b72c-f8a4-4b45-af51-4014b822b162",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea049a47-2536-4bf5-9a8f-6aa1626430ba",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bb68e39f-e677-47d5-9877-c89c572410f2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4571837-c795-4ead-99fe-0fb86c034355",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Add Reference Table Item DT",
          "object_type": "qradar_reference_table",
          "programmatic_name": "example_qradar__add_reference_table_item_dt",
          "tags": [],
          "uuid": null,
          "workflow_id": 74
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Delete an item from a given QRadar reference table",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Table Delete Item",
      "export_key": "qradar_reference_table_delete_item",
      "id": 73,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174540006,
      "name": "qradar_reference_table_delete_item",
      "tags": [],
      "uuid": "10b6522f-ffc5-4742-8174-06ffe108aaf7",
      "version": 2,
      "view_items": [
        {
          "content": "0bf3b72c-f8a4-4b45-af51-4014b822b162",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bb68e39f-e677-47d5-9877-c89c572410f2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea049a47-2536-4bf5-9a8f-6aa1626430ba",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4571837-c795-4ead-99fe-0fb86c034355",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Delete Reference Table Item DT",
          "object_type": "qradar_reference_table_queried_rows",
          "programmatic_name": "example_qradar__delete_reference_table_item_dt",
          "tags": [],
          "uuid": null,
          "workflow_id": 80
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Table Get Table Data",
      "export_key": "qradar_reference_table_get_table",
      "id": 74,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174551697,
      "name": "qradar_reference_table_get_table",
      "tags": [],
      "uuid": "6450077b-708a-4e65-9eda-6e403a3f4410",
      "version": 2,
      "view_items": [
        {
          "content": "0bf3b72c-f8a4-4b45-af51-4014b822b162",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Get Reference Table Data",
          "object_type": "qradar_reference_table",
          "programmatic_name": "qradar_get_reference_table_data",
          "tags": [],
          "uuid": null,
          "workflow_id": 75
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Update an item in a given QRadar reference table",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Reference Table Update Item",
      "export_key": "qradar_reference_table_update_item",
      "id": 75,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174557788,
      "name": "qradar_reference_table_update_item",
      "tags": [],
      "uuid": "2f0ec2b9-0266-42bc-ac4c-71ddfe593344",
      "version": 2,
      "view_items": [
        {
          "content": "0bf3b72c-f8a4-4b45-af51-4014b822b162",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bb68e39f-e677-47d5-9877-c89c572410f2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea049a47-2536-4bf5-9a8f-6aa1626430ba",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4571837-c795-4ead-99fe-0fb86c034355",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: Qradar - Update this Reference Table Item DT",
          "object_type": "qradar_reference_table_queried_rows",
          "programmatic_name": "example_qradar__update_this_reference_table_item",
          "tags": [],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "creator": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "description": {
        "content": "Search QRadar for events",
        "format": "text"
      },
      "destination_handle": "fn_qradar_integration",
      "display_name": "QRadar Search",
      "export_key": "qradar_search",
      "id": 76,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1628174563817,
      "name": "qradar_search",
      "tags": [],
      "uuid": "c3e6f6cc-8905-41e6-9841-ebe99845d778",
      "version": 2,
      "view_items": [
        {
          "content": "048ba39a-ab94-4d1f-a0f8-2462de3c044c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "01ed4652-fe61-4dbf-bc83-f81c62c5563c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d8fc645-5067-4ab0-b151-1d106dad91d6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b6053690-d7b2-4204-b48a-f86503b419d9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eefc9e56-2806-4534-b409-42e25154ecc9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "19778fc0-9a30-4b8b-9c21-642495f9eebc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c33fbe1d-125c-4a79-82e8-6608d1c7bb5e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d21f2814-40e6-4f7a-b269-6ff2c7a3196e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d7a544ff-689b-4f15-b3c1-a7ebd20bbf3b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a49a50f2-68ba-4ccb-87d5-c7e55d2cbfef",
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
          "name": "Example: QRadar - Search Events using Offense id",
          "object_type": "incident",
          "programmatic_name": "qradar_search_event_offense",
          "tags": [],
          "uuid": null,
          "workflow_id": 77
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 61,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1628610570281,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1628610570281,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "77a37273-a484-4fd1-8d02-2c28513d5343"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_qradar_integration",
      "name": "fn_qradar_integration",
      "programmatic_name": "fn_qradar_integration",
      "tags": [],
      "users": [],
      "uuid": "1184d338-96e3-4315-8b2c-b0b9e623573c"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6328,
    "major": 39,
    "minor": 0,
    "version": "39.0.6328"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "QRadar Offense Events",
      "export_key": "qradar_offense_event",
      "fields": {
        "category": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/category",
          "hide_notification": false,
          "id": 467,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "category",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category",
          "tooltip": "category",
          "type_id": 1011,
          "uuid": "265ef12d-92ce-40d6-96bb-f6e0c300dcf2",
          "values": [],
          "width": 123
        },
        "log_source": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/log_source",
          "hide_notification": false,
          "id": 468,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "log_source",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Log Source",
          "tooltip": "logsourceid",
          "type_id": 1011,
          "uuid": "329c8249-a81e-444a-aaf8-ccd8558dc980",
          "values": [],
          "width": 140
        },
        "protocol": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/protocol",
          "hide_notification": false,
          "id": 469,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "protocol",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Protocol",
          "tooltip": "protocolid",
          "type_id": 1011,
          "uuid": "630337b1-fea8-471e-9601-f89629ec13b4",
          "values": [],
          "width": 123
        },
        "qradar_label": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/qradar_label",
          "hide_notification": false,
          "id": 484,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_label",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "QRadar Label",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "6f320e88-37a8-47c3-a653-ca9781a7a942",
          "values": [],
          "width": 57
        },
        "rule": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/rule",
          "hide_notification": false,
          "id": 470,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "rule",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Rule",
          "tooltip": "creeventlist",
          "type_id": 1011,
          "uuid": "e9fc2abf-43df-4f4c-8c2a-27f1d073f010",
          "values": [],
          "width": 123
        },
        "start_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_offense_event/start_time",
          "hide_notification": false,
          "id": 471,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "start_time",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Start Time",
          "tooltip": "starttime",
          "type_id": 1011,
          "uuid": "d99b3a20-5a56-46f5-a15c-d4171489401a",
          "values": [],
          "width": 131
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
      "type_name": "qradar_offense_event",
      "uuid": "8fceee8c-9d0e-4e33-8d37-366ec71cfed3"
    },
    {
      "actions": [],
      "display_name": "QRadar Reference Sets",
      "export_key": "qradar_reference_set",
      "fields": {
        "data_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_set/data_type",
          "hide_notification": false,
          "id": 499,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "data_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Data Type",
          "tooltip": "",
          "type_id": 1012,
          "uuid": "d087aaf2-3949-4314-afe1-0b9cdbecac50",
          "values": [],
          "width": 146
        },
        "elements": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_set/elements",
          "hide_notification": false,
          "id": 500,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "elements",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Elements",
          "tooltip": "",
          "type_id": 1012,
          "uuid": "743d860e-d486-444b-8905-182f94921fa1",
          "values": [],
          "width": 141
        },
        "qradar_label": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_set/qradar_label",
          "hide_notification": false,
          "id": 501,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_label",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Qradar Label",
          "tooltip": "",
          "type_id": 1012,
          "uuid": "2db5280e-93d5-42c0-a718-bbbd3710c45a",
          "values": [],
          "width": 184
        },
        "reference_set": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_set/reference_set",
          "hide_notification": false,
          "id": 502,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "reference_set",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Reference Set",
          "tooltip": "",
          "type_id": 1012,
          "uuid": "146108ce-5ca6-4841-968c-5b786ae7638c",
          "values": [],
          "width": 198
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
      "type_name": "qradar_reference_set",
      "uuid": "1eef8608-0621-475e-a28e-e92a382046ac"
    },
    {
      "actions": [],
      "display_name": "QRadar Reference Tables",
      "export_key": "qradar_reference_table",
      "fields": {
        "collection_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table/collection_id",
          "hide_notification": false,
          "id": 475,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "collection_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Collection Id",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "d4a93bb2-a6ae-4b1f-a70c-7f5bc2b85fc9",
          "values": [],
          "width": 193
        },
        "namespace": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table/namespace",
          "hide_notification": false,
          "id": 476,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "namespace",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Namespace",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "3ba3eaa4-bbed-436c-bf2f-7649752d4565",
          "values": [],
          "width": 90
        },
        "number_of_elements": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table/number_of_elements",
          "hide_notification": false,
          "id": 477,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "number_of_elements",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Number Of Elements",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "15a5979f-a942-40ce-a44a-e5a75b06c13d",
          "values": [],
          "width": 207
        },
        "qradar_label": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table/qradar_label",
          "hide_notification": false,
          "id": 487,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_label",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "QRadar Label",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "8321c298-70a2-4e1e-a142-55fb16db090b",
          "values": [],
          "width": 117
        },
        "reference_table": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table/reference_table",
          "hide_notification": false,
          "id": 478,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "reference_table",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Reference Table",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "1be69e07-4d48-412e-98d1-ca83e086e159",
          "values": [],
          "width": 282
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
      "type_name": "qradar_reference_table",
      "uuid": "0add7e37-b3bf-4e35-9b82-123e2790aab9"
    },
    {
      "actions": [],
      "display_name": "QRadar Reference Table Queried Rows",
      "export_key": "qradar_reference_table_queried_rows",
      "fields": {
        "inner_key": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/inner_key",
          "hide_notification": false,
          "id": 479,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "inner_key",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Inner Key",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "c771fb55-91e7-4eec-9310-7de7e232b58e",
          "values": [],
          "width": 127
        },
        "outer_key": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/outer_key",
          "hide_notification": false,
          "id": 480,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "outer_key",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Outer Key",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "ae89d5d2-9036-4560-997b-ce15c2b3f488",
          "values": [],
          "width": 132
        },
        "qradar_label": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/qradar_label",
          "hide_notification": false,
          "id": 486,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_label",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "QRadar Label",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "a39bcc03-1cbf-436d-9603-f7ea833b9a93",
          "values": [],
          "width": 69
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/status",
          "hide_notification": false,
          "id": 481,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "49ae33c0-f2a9-4da6-a63a-158ae5f9125f",
          "values": [],
          "width": 50
        },
        "table": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/table",
          "hide_notification": false,
          "id": 482,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "table",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Table",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "b90fbf39-8688-4f7a-ace4-9cf802de9074",
          "values": [],
          "width": 127
        },
        "value": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_reference_table_queried_rows/value",
          "hide_notification": false,
          "id": 483,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "value",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Value",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "20200102-b242-4505-ac95-d3441b79ae40",
          "values": [],
          "width": 127
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
      "type_name": "qradar_reference_table_queried_rows",
      "uuid": "cc6aeb37-eced-48c3-9536-971a6b015ef4"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "example_qradar__get_all_reference_tables",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_qradar__get_all_reference_tables\" isExecutable=\"true\" name=\"Example: QRadar - Get All Reference Tables\"\u003e\u003cdocumentation\u003eReturn all reference tables on selected server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1jft75w\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0wac85x\" name=\"QRadar Reference Table Get All Ta...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0abff118-314e-4728-964d-03558088a62a\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\n  Sample data:\\n  [{u\u0027creation_time\u0027: 1464119408489L, u\u0027collection_id\u0027: 186, u\u0027key_name_types\u0027: {u\u0027First Seen Date\u0027: u\u0027DATE\u0027, u\u0027Confidence\u0027: u\u0027NUM\u0027, u\u0027Last Seen Date\u0027: u\u0027DATE\u0027, u\u0027Provider\u0027: u\u0027ALN\u0027}, u\u0027timeout_type\u0027: u\u0027LAST_SEEN\u0027, u\u0027name\u0027: u\u0027Phishing Senders Data\u0027, u\u0027namespace\u0027: u\u0027SHARED\u0027, u\u0027element_type\u0027: u\u0027ALNIC\u0027, u\u0027number_of_elements\u0027: 0}, {u\u0027creation_time\u0027: 1464119422432L, u\u0027collection_id\u0027: 182, u\u0027key_name_types\u0027: {u\u0027First Seen Date\u0027: u\u0027DATE\u0027, u\u0027Confidence\u0027: u\u0027NUM\u0027, u\u0027Last Seen Date\u0027: u\u0027DATE\u0027, u\u0027Provider\u0027: u\u0027ALN\u0027}, u\u0027timeout_type\u0027: u\u0027LAST_SEEN\u0027, u\u0027name\u0027: u\u0027Rogue Process Names Data\u0027, u\u0027namespace\u0027: u\u0027SHARED\u0027, u\u0027element_type\u0027: u\u0027ALNIC\u0027, u\u0027number_of_elements\u0027: 0}]\\n\\\"\\\"\\\"\\nif results.success:\\n  if results.content:\\n    for item in results.content:\\n      item_row = incident.addRow(\\\"qradar_reference_table\\\")\\n      item_row[\\\"reference_table\\\"] = item[\\\"name\\\"]\\n      item_row[\\\"collection_id\\\"] = item[\\\"collection_id\\\"]\\n      item_row[\\\"number_of_elements\\\"] = item[\\\"number_of_elements\\\"]\\n      item_row[\\\"namespace\\\"] = item[\\\"namespace\\\"]\\n      item_row[\\\"qradar_label\\\"] = str(row[\\\"server_name\\\"])\\n  else:\\n    incident.addNote(\\\"No reference tables found on QRadar server {}\\\".format(row[\\\"server_name\\\"]))\\nelse:\\n  incident.addNote(\\\"An error occurred getting the reference tables: {} on QRadar server: {}\\\".formt(results.reason, row[\\\"server_name\\\"]))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_label = row[\\\"server_name\\\"]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1jft75w\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1pv9q2o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1jft75w\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0wac85x\"/\u003e\u003cendEvent id=\"EndEvent_0jbou28\"\u003e\u003cincoming\u003eSequenceFlow_1pv9q2o\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pv9q2o\" sourceRef=\"ServiceTask_0wac85x\" targetRef=\"EndEvent_0jbou28\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0wac85x\" id=\"ServiceTask_0wac85x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"286\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jft75w\" id=\"SequenceFlow_1jft75w_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"242\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0jbou28\" id=\"EndEvent_0jbou28_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"485\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"503\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pv9q2o\" id=\"SequenceFlow_1pv9q2o_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"435.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "admin@example.com",
      "description": "Return all reference tables on selected server",
      "export_key": "example_qradar__get_all_reference_tables",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628517781521,
      "name": "Example: QRadar - Get All Reference Tables",
      "object_type": "qradar_servers",
      "programmatic_name": "example_qradar__get_all_reference_tables",
      "tags": [],
      "uuid": "db76f78c-8183-4cc4-9cc3-95d9564fc838",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 25,
        "workflow_id": "qradar_add_reference_set_item",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_add_reference_set_item\" isExecutable=\"true\" name=\"Example: QRadar - Add Reference Set Item\"\u003e\u003cdocumentation\u003eAdd an artifact to the QRadar reference set.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ie98y1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tzklx9\" name=\"QRadar Add Reference Set Item\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"30b6899a-d015-48c3-8fd9-500788d4b437\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.status_code == 200:\\n  incident.addNote(u\\\"Value: {} added to reference set: {} on QRadar server: {}\\\".format(rule.properties.qradar_reference_set_item_value, results[\u0027content\u0027][\u0027name\u0027], row[\\\"qradar_label\\\"]))\\n  row.elements = str(results[\\\"content\\\"][\\\"number_of_elements\\\"])\\nelse:\\n  incident.addNote(u\\\"Failed to add Value: {} to reference set: {} on QRadar server: {}. Status Code: {}, message: {}\\\".format(rule.properties.qradar_reference_set_item_value, row[\\\"qradar_label\\\"], results[\u0027content\u0027][\u0027name\u0027], results.status_code, results[\u0027content\u0027][\u0027message\u0027]))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_reference_set_item_value = rule.properties.qradar_reference_set_item_value\\ninputs.qradar_reference_set_name = row[\\\"reference_set\\\"]\\ninputs.qradar_label = row[\\\"qradar_label\\\"]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ie98y1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_016nev4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ie98y1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tzklx9\"/\u003e\u003cendEvent id=\"EndEvent_0i6sla0\"\u003e\u003cincoming\u003eSequenceFlow_016nev4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_016nev4\" sourceRef=\"ServiceTask_1tzklx9\" targetRef=\"EndEvent_0i6sla0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tzklx9\" id=\"ServiceTask_1tzklx9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"297\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ie98y1\" id=\"SequenceFlow_1ie98y1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"297\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"247.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0i6sla0\" id=\"EndEvent_0i6sla0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"510\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"528\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_016nev4\" id=\"SequenceFlow_016nev4_di\"\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"510\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 25,
      "creator_id": "admin@example.com",
      "description": "Add an artifact to the QRadar reference set.",
      "export_key": "qradar_add_reference_set_item",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628527717473,
      "name": "Example: QRadar - Add Reference Set Item",
      "object_type": "qradar_reference_set",
      "programmatic_name": "qradar_add_reference_set_item",
      "tags": [],
      "uuid": "a9fa7e6d-2e98-43ad-b0bd-74fbf666a3d9",
      "workflow_id": 104
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "qradar_find_reference_sets_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_find_reference_sets_artifact\" isExecutable=\"true\" name=\"Example: QRadar - Find all Reference Sets for artifact\"\u003e\u003cdocumentation\u003eFind all the QRadar reference sets that contain the given artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0hdql82\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s1bltx\" name=\"QRadar Find Reference Sets\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"09885813-f640-45bc-8892-d1a741a7d53e\"\u003e{\"inputs\":{},\"post_processing_script\":\"items = results.reference_items\\n\\\"\\\"\\\"\\n  Sample data:\\n  [{u\u0027name\u0027: u\u0027RF Risklist\u0027, u\u0027timeout_type\u0027: u\u0027FIRST_SEEN\u0027, u\u0027creation_time\u0027: 1549376859164, u\u0027element_type\u0027: u\u0027IP\u0027, u\u0027number_of_elements\u0027: 5, u\u0027data\u0027: [{u\u0027source\u0027: u\u0027admin\u0027, u\u0027first_seen\u0027: 1549477737993, u\u0027value\u0027: u\u002746.21.147.161\u0027, u\u0027last_seen\u0027: 1549477737993}]}]\\n\\n\\\"\\\"\\\"\\nreference_set_names = []\\nif items:\\n  for item in items:\\n    reference_set_names.append(item[\\\"name\\\"])\\n      #item_row = incident.addRow(\\\"qradar_reference_set\\\")\\n      #item_row[\\\"reference_set\\\"] = item[\\\"name\\\"]\\n      #item_row[\\\"item_value\\\"] = item[\\\"data\\\"][0][\\\"value\\\"]\\n      #item_row[\\\"source\\\"] = item[\\\"data\\\"][0][\\\"source\\\"]\\n      #item_row[\\\"qradar_label\\\"] = row[\\\"server_name\\\"]\\n      #item_row[\\\"searched_value\\\"] = rule.properties.qradar_reference_set_item_value\\n  incident.addNote(\\\"Value: {} found in reference sets: {} on QRadar Server: {}\\\".format(rule.properties.qradar_reference_set_item_value, str(reference_set_names), row[\\\"server_name\\\"]))\\nelse:\\n  incident.addNote(\\\"No reference sets contain artifact: {}\\\".format(rule.properties.qradar_reference_set_item_value))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_label = row[\\\"server_name\\\"]\\ninputs.qradar_reference_set_item_value = rule.properties.qradar_reference_set_item_value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hdql82\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1f05bgv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hdql82\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s1bltx\"/\u003e\u003cendEvent id=\"EndEvent_1ag4eny\"\u003e\u003cincoming\u003eSequenceFlow_1f05bgv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1f05bgv\" sourceRef=\"ServiceTask_0s1bltx\" targetRef=\"EndEvent_1ag4eny\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s1bltx\" id=\"ServiceTask_0s1bltx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"284\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hdql82\" id=\"SequenceFlow_0hdql82_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"284\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"241\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ag4eny\" id=\"EndEvent_1ag4eny_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"466\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"484\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f05bgv\" id=\"SequenceFlow_1f05bgv_di\"\u003e\u003comgdi:waypoint x=\"384\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"466\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"425\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "admin@example.com",
      "description": "Find all the QRadar reference sets that contain the given artifact",
      "export_key": "qradar_find_reference_sets_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628518811838,
      "name": "Example: QRadar - Find all Reference Sets for artifact",
      "object_type": "qradar_servers",
      "programmatic_name": "qradar_find_reference_sets_artifact",
      "tags": [],
      "uuid": "6fadb968-e2f2-4e23-8525-2b02b980e7d6",
      "workflow_id": 107
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "qradar_search_event_offense",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_search_event_offense\" isExecutable=\"true\" name=\"Example: QRadar - Search Events using Offense id\"\u003e\u003cdocumentation\u003eUse the qradar_id field of the incident to search qradar events, and update the data table, qradar_offense_event, with the first 5 results.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_026bbbi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1gto8k0\" name=\"QRadar Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c3e6f6cc-8905-41e6-9841-ebe99845d778\"\u003e{\"inputs\":{\"048ba39a-ab94-4d1f-a0f8-2462de3c044c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% MINUTES\"}}},\"01ed4652-fe61-4dbf-bc83-f81c62c5563c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"DATEFORMAT(starttime, \u0027YYYY-MM-dd HH:mm\u0027) as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)\"}},\"b6053690-d7b2-4204-b48a-f86503b419d9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"43320\"}},\"c33fbe1d-125c-4a79-82e8-6608d1c7bb5e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":1}},\"d7a544ff-689b-4f15-b3c1-a7ebd20bbf3b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"54c4eb52-d955-4e05-9f76-c3819853ff68\"}}},\"post_processing_script\":\"for event in results.events:\\n  qradar_event = incident.addRow(\\\"qradar_offense_event\\\")\\n  qradar_event.start_time = event.StartTime\\n  qradar_event.category = event.categoryname_category\\n  qradar_event.log_source = event.logsourcename_logsourceid\\n  qradar_event.protocol = event.protocolname_protocolid\\n  qradar_event.rule = event.rulename_creeventlist\\n  qradar_event.qradar_label = rule.properties.qradar_label\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.qradar_query_param2 = incident.properties.qradar_id\\ninputs.qradar_label = rule.properties.qradar_label\\ninputs.qradar_query_all_results = rule.properties.qradar_query_all_results\\nif rule.properties.qradar_query_all_results:\\n  inputs.qradar_query_all_results = rule.properties.qradar_query_all_results\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_026bbbi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0cs0bcr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_026bbbi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gto8k0\"/\u003e\u003cendEvent id=\"EndEvent_0ehbn4w\"\u003e\u003cincoming\u003eSequenceFlow_0cs0bcr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0cs0bcr\" sourceRef=\"ServiceTask_1gto8k0\" targetRef=\"EndEvent_0ehbn4w\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xq6ex9\"\u003e\u003ctext\u003e\u003c![CDATA[Return results in qradar_offense_event datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0fkdkst\" sourceRef=\"ServiceTask_1gto8k0\" targetRef=\"TextAnnotation_0xq6ex9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"366\" y=\"174\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"361\" y=\"209\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"247\" y=\"239\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"316\" xsi:type=\"omgdc:Point\" y=\"239\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gto8k0\" id=\"ServiceTask_1gto8k0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"482.0945157526254\" y=\"152\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_026bbbi\" id=\"SequenceFlow_026bbbi_di\"\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"192\"/\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"192\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"442\" y=\"170\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ehbn4w\" id=\"EndEvent_0ehbn4w_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"662\" y=\"174\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"635\" y=\"213\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cs0bcr\" id=\"SequenceFlow_0cs0bcr_di\"\u003e\u003comgdi:waypoint x=\"582\" xsi:type=\"omgdc:Point\" y=\"192\"/\u003e\u003comgdi:waypoint x=\"662\" xsi:type=\"omgdc:Point\" y=\"192\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"577\" y=\"170.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xq6ex9\" id=\"TextAnnotation_0xq6ex9_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"136\" x=\"589\" y=\"67\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0fkdkst\" id=\"Association_0fkdkst_di\"\u003e\u003comgdi:waypoint x=\"577\" xsi:type=\"omgdc:Point\" y=\"157\"/\u003e\u003comgdi:waypoint x=\"619\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "Use the qradar_id field of the incident to search qradar events, and update the data table, qradar_offense_event, with the first 5 results.",
      "export_key": "qradar_search_event_offense",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628519057917,
      "name": "Example: QRadar - Search Events using Offense id",
      "object_type": "incident",
      "programmatic_name": "qradar_search_event_offense",
      "tags": [],
      "uuid": "e37d2dae-a71f-4b2f-8830-b03ed320fdff",
      "workflow_id": 77
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "example_qradar__delete_reference_table_item_dt",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_qradar__delete_reference_table_item_dt\" isExecutable=\"true\" name=\"Example: QRadar - Delete Reference Table Item DT\"\u003e\u003cdocumentation\u003eAn example workflow that takes in a Reference Table name, an inner key, an outer key and a value to delete for the table\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1fpmqih\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0737k88\" name=\"QRadar Reference Table Delete Ite...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"10b6522f-ffc5-4742-8174-06ffe108aaf7\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = u\\\"\\\"\\\"QRadar Label: {}\\nOuter key: {}\\nInner key: {}\\nEntry: {}\\nReference table: {}\\\"\\\"\\\".format(results.inputs.qradar_label,\\n                              results.inputs.qradar_reference_table_item_outer_key,\\n                              results.inputs.qradar_reference_table_item_inner_key,\\n                              results.inputs.qradar_reference_table_item_value, \\n                              results.inputs.qradar_reference_table_name)\\nif results.success:\\n    incident.addNote(u\\\"Successful delete\\\\n{}\\\".format(note))\\n    row[\u0027status\u0027] = \\\"deleted\\\"\\nelse:\\n    incident.addNote(u\\\"Failure to delete item: {}\\\\n{}\\\".format(results[\u0027reason\u0027], note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.qradar_reference_table_name = row.table\\ninputs.qradar_reference_table_item_outer_key = row.outer_key\\ninputs.qradar_reference_table_item_inner_key = row.inner_key\\ninputs.qradar_reference_table_item_value = row.value\\ninputs.qradar_label = row.qradar_label\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1fpmqih\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dw21s8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1fpmqih\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0737k88\"/\u003e\u003cendEvent id=\"EndEvent_0tt8h3e\"\u003e\u003cincoming\u003eSequenceFlow_1dw21s8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1dw21s8\" sourceRef=\"ServiceTask_0737k88\" targetRef=\"EndEvent_0tt8h3e\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0nykfdr\"\u003e\u003ctext\u003e\u003c![CDATA[Result placed in a row and datatable row is set to \u0027deleted\u0027\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dgavrh\" sourceRef=\"ServiceTask_0737k88\" targetRef=\"TextAnnotation_0nykfdr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0737k88\" id=\"ServiceTask_0737k88_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"269\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fpmqih\" id=\"SequenceFlow_1fpmqih_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"269\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"188.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tt8h3e\" id=\"EndEvent_0tt8h3e_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"416\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"434\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dw21s8\" id=\"SequenceFlow_1dw21s8_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"347.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0nykfdr\" id=\"TextAnnotation_0nykfdr_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"242\" x=\"347\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dgavrh\" id=\"Association_0dgavrh_di\"\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "An example workflow that takes in a Reference Table name, an inner key, an outer key and a value to delete for the table",
      "export_key": "example_qradar__delete_reference_table_item_dt",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628517696797,
      "name": "Example: QRadar - Delete Reference Table Item DT",
      "object_type": "qradar_reference_table_queried_rows",
      "programmatic_name": "example_qradar__delete_reference_table_item_dt",
      "tags": [],
      "uuid": "6338645d-3f08-4acb-b49d-f46fede6d8cd",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "example_qradar__update_this_reference_table_item",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_qradar__update_this_reference_table_item\" isExecutable=\"true\" name=\"Example: Qradar - Update this Reference Table Item DT\"\u003e\u003cdocumentation\u003eUpdate an existing reference table item. If it does not exist, it will be added\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16hfg6o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16hfg6o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gd7hlv\"/\u003e\u003cendEvent id=\"EndEvent_0s8l4hf\"\u003e\u003cincoming\u003eSequenceFlow_1nnixb6\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1gd7hlv\" name=\"QRadar Reference Table Update Ite...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2f0ec2b9-0266-42bc-ac4c-71ddfe593344\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = u\\\"\\\"\\\"QRadar Label: {}\\nOuter key: {}\\nInner key: {}\\nEntry: {}\\nReference table: {}\\\"\\\"\\\".format(results.inputs.qradar_label,\\n                              results.inputs.qradar_reference_table_item_outer_key,\\n                              results.inputs.qradar_reference_table_item_inner_key,\\n                              results.inputs.qradar_reference_table_item_value, \\n                              results.inputs.qradar_reference_table_name)\\nif results.success:\\n    incident.addNote(u\\\"Successful updated\\\\n{}\\\".format(note))\\n    row[\u0027status\u0027] = \u0027updated\u0027\\n    row[\u0027value\u0027] = results.inputs.qradar_reference_table_item_value\\n    row[\u0027outer_key\u0027] = results.inputs.qradar_reference_table_item_outer_key\\n    row[\u0027inner_key\u0027] = results.inputs.qradar_reference_table_item_inner_key\\nelse:\\n    incident.addNote(u\\\"Failure to update item: {}\\\\n{}\\\".format(results[\u0027reason\u0027], note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.qradar_reference_table_name = row.table\\ninputs.qradar_label = row.qradar_label\\n\\nif inputs.qradar_reference_table_item_inner_key:\\n  inputs.qradar_reference_table_item_inner_key = rule.properties.qradar_reference_table_item_inner_key\\nelse:\\n  inputs.qradar_reference_table_item_inner_key = row.inner_key\\n\\nif inputs.qradar_reference_table_item_outer_key:\\n  inputs.qradar_reference_table_item_outer_key = rule.properties.qradar_ref_table_outer_key\\nelse:\\n  inputs.qradar_reference_table_item_outer_key = row.outer_key\\n\\nif rule.properties.qradar_ref_table_update:\\n  inputs.qradar_reference_table_item_value = rule.properties.qradar_ref_table_update\\nelse:\\n  inputs.qradar_reference_table_item_value = \\\"This is an example\\\"\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16hfg6o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nnixb6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1nnixb6\" sourceRef=\"ServiceTask_1gd7hlv\" targetRef=\"EndEvent_0s8l4hf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bzrivy\"\u003e\u003ctext\u003e\u003c![CDATA[Result added as a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0jp4p4y\" sourceRef=\"ServiceTask_1gd7hlv\" targetRef=\"TextAnnotation_0bzrivy\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16hfg6o\" id=\"SequenceFlow_16hfg6o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"311\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"209.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0s8l4hf\" id=\"EndEvent_0s8l4hf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"491\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"464\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gd7hlv\" id=\"ServiceTask_1gd7hlv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"311\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nnixb6\" id=\"SequenceFlow_1nnixb6_di\"\u003e\u003comgdi:waypoint x=\"411\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"491\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"406\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bzrivy\" id=\"TextAnnotation_0bzrivy_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"119\" x=\"403\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0jp4p4y\" id=\"Association_0jp4p4y_di\"\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"113\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "Update an existing reference table item. If it does not exist, it will be added",
      "export_key": "example_qradar__update_this_reference_table_item",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628608794535,
      "name": "Example: Qradar - Update this Reference Table Item DT",
      "object_type": "qradar_reference_table_queried_rows",
      "programmatic_name": "example_qradar__update_this_reference_table_item",
      "tags": [],
      "uuid": "4f260795-608f-431c-a851-ef39679e2f60",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "qradar_move_item_to_different_ref_set",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_move_item_to_different_ref_set\" isExecutable=\"true\" name=\"Example: QRadar - Move Item from one Reference Set to another\"\u003e\u003cdocumentation\u003eMove an item from one reference set to another reference set. Add a note to the Incident after completing each step.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_13z9jub\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1i90888\" name=\"QRadar Delete Reference Set Item\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a7dc3d26-ab97-44a3-b56a-e367315b08e0\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.status_code == 200:\\n  #Add a note\\n  incident.addNote(\\\"Value {} removed successfully from Reference Set: {} on QRadar Server: {}\\\".format(rule.properties.qradar_reference_set_item_value, row[\\\"reference_set\\\"], row[\\\"qradar_label\\\"]))\\n  row.elements = str(results[\\\"content\\\"][\\\"number_of_elements\\\"])\\nelse:\\n  incident.addNote(u\\\"Failed to remove value {} from Reference Set: {} on QRadar Server: {}, message: {}\\\".format(rule.properties.qradar_reference_set_item_value, row[\\\"reference_set\\\"], row[\\\"qradar_label\\\"], results[\u0027content\u0027][\u0027message\u0027]))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_label = row[\\\"qradar_label\\\"]\\ninputs.qradar_reference_set_item_value = rule.properties.qradar_reference_set_item_value\\ninputs.qradar_reference_set_name = row[\\\"reference_set\\\"]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_13z9jub\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19jlia9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_13z9jub\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1i90888\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0ko87l5\"\u003e\u003cincoming\u003eSequenceFlow_19jlia9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ula0kz\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1e0lezq\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_19jlia9\" sourceRef=\"ServiceTask_1i90888\" targetRef=\"ExclusiveGateway_0ko87l5\"/\u003e\u003cserviceTask id=\"ServiceTask_1693xdd\" name=\"QRadar Add Reference Set Item\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"30b6899a-d015-48c3-8fd9-500788d4b437\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.status_code == 200:\\n  #Add a note\\n  incident.addNote(\\\"Value {} added successfully to Reference Set: {} on QRadar Server: {}\\\".format(rule.properties.qradar_reference_set_item_value, rule.properties.qradar_reference_set_name_to_move_to, row[\\\"qradar_label\\\"]))\\n  row.elements = str(results[\\\"content\\\"][\\\"number_of_elements\\\"])\\nelse:\\n  incident.addNote(u\\\"Failed to add value {} to Reference Set: {} on QRadar Server: {}, message: {}\\\".format(rule.properties.qradar_reference_set_item_value, rule.properties.qradar_reference_set_name_to_move_to, row[\\\"qradar_label\\\"], results[\u0027content\u0027][\u0027message\u0027]))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_label = row[\\\"qradar_label\\\"]\\ninputs.qradar_reference_set_item_value = rule.properties.qradar_reference_set_item_value\\ninputs.qradar_reference_set_name = rule.properties.qradar_reference_set_name_to_move_to\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ula0kz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f5e92z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ula0kz\" name=\"Success\" sourceRef=\"ExclusiveGateway_0ko87l5\" targetRef=\"ServiceTask_1693xdd\"/\u003e\u003cendEvent id=\"EndEvent_1519d8f\"\u003e\u003cincoming\u003eSequenceFlow_0f5e92z\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1e0lezq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0f5e92z\" sourceRef=\"ServiceTask_1693xdd\" targetRef=\"EndEvent_1519d8f\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1e0lezq\" name=\"Failure\" sourceRef=\"ExclusiveGateway_0ko87l5\" targetRef=\"EndEvent_1519d8f\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"if results.status_code not equal 200\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1i90888\" id=\"ServiceTask_1i90888_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"366\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13z9jub\" id=\"SequenceFlow_13z9jub_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"282\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0ko87l5\" id=\"ExclusiveGateway_0ko87l5_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"531\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"556\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19jlia9\" id=\"SequenceFlow_19jlia9_di\"\u003e\u003comgdi:waypoint x=\"466\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"531\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"498.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1693xdd\" id=\"ServiceTask_1693xdd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"674\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ula0kz\" id=\"SequenceFlow_1ula0kz_di\"\u003e\u003comgdi:waypoint x=\"581\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"674\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"45\" x=\"605\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1519d8f\" id=\"EndEvent_1519d8f_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"868\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"886\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f5e92z\" id=\"SequenceFlow_0f5e92z_di\"\u003e\u003comgdi:waypoint x=\"774\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"868\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"821\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e0lezq\" id=\"SequenceFlow_1e0lezq_di\"\u003e\u003comgdi:waypoint x=\"556\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"556\" xsi:type=\"omgdc:Point\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"886\" xsi:type=\"omgdc:Point\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"886\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"37\" x=\"703\" y=\"309\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Move an item from one reference set to another reference set. Add a note to the Incident after completing each step.",
      "export_key": "qradar_move_item_to_different_ref_set",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628528535102,
      "name": "Example: QRadar - Move Item from one Reference Set to another",
      "object_type": "qradar_reference_set",
      "programmatic_name": "qradar_move_item_to_different_ref_set",
      "tags": [],
      "uuid": "80a2b1cc-d82b-4c44-b781-b50ac9870410",
      "workflow_id": 109
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "qradar_find_reference_set_item",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_find_reference_set_item\" isExecutable=\"true\" name=\"Example: QRadar - Find Item in Reference Set\"\u003e\u003cdocumentation\u003eLook for an item in the QRadar reference set than add a note to the Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12d2pzs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0bpiqfb\" name=\"QRadar Find Reference Set Item\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9d817ee3-a8cf-4a0a-a8a6-969f6090f276\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.found == \\\"True\\\":\\n  incident.addNote(u\\\"Found Value: {} in list: {} on QRadar server: {}.\\\".format(rule.properties.qradar_reference_set_item_value, results[\u0027content\u0027][\u0027name\u0027], row[\\\"qradar_label\\\"]))\\nelse:\\n  incident.addNote(\\\"Value: {} not found in list: {} on QRadar server: {}.\\\".format(rule.properties.qradar_reference_set_item_value, results[\u0027content\u0027][\u0027name\u0027], row[\\\"qradar_label\\\"]))\\n  \\n\\\"\\\"\\\"\\n{\\n  \u0027status_code\u0027: 200,\\n  \u0027found\u0027: \u0027True\u0027,\\n  \u0027content\u0027: {\\n    \u0027time_to_live\u0027: \u002720 years 4 mons 22 days 0 hours 0 mins 0.00 secs\u0027,\\n    \u0027timeout_type\u0027: \u0027FIRST_SEEN\u0027,\\n    \u0027number_of_elements\u0027: 2,\\n    \u0027data\u0027: [\\n      {\\n        \u0027last_seen\u0027: 1594386447789,\\n        \u0027first_seen\u0027: 1594386447789,\\n        \u0027source\u0027: \u0027reference data api\u0027,\\n        \u0027value\u0027: \u0027169.254.3.2\u0027,\\n        \u0027domain_id\u0027: None\\n      },\\n      {\\n        \u0027last_seen\u0027: 1595364392956,\\n        \u0027first_seen\u0027: 1595364392956,\\n        \u0027source\u0027: \u0027reference data api\u0027,\\n        \u0027value\u0027: \u00271.2.3.4\u0027,\\n        \u0027domain_id\u0027: None\\n      }\\n    ],\\n    \u0027creation_time\u0027: 1587585219697,\\n    \u0027name\u0027: \u0027Sample Blocked IPs\u0027,\\n    \u0027namespace\u0027: \u0027SHARED\u0027,\\n    \u0027element_type\u0027: \u0027IP\u0027,\\n    \u0027collection_id\u0027: 32\\n  }\\n}\\n\\\"\\\"\\\"\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.qradar_reference_set_name = row[\\\"reference_set\\\"]\\ninputs.qradar_reference_set_item_value = rule.properties.qradar_reference_set_item_value\\ninputs.qradar_label = row[\\\"qradar_label\\\"]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12d2pzs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0guq6gs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12d2pzs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0bpiqfb\"/\u003e\u003cendEvent id=\"EndEvent_0v8hqxp\"\u003e\u003cincoming\u003eSequenceFlow_0guq6gs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0guq6gs\" sourceRef=\"ServiceTask_0bpiqfb\" targetRef=\"EndEvent_0v8hqxp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0bpiqfb\" id=\"ServiceTask_0bpiqfb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"304\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12d2pzs\" id=\"SequenceFlow_12d2pzs_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"304\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"251\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0v8hqxp\" id=\"EndEvent_0v8hqxp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"501\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"519\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0guq6gs\" id=\"SequenceFlow_0guq6gs_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"501\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "admin@example.com",
      "description": "Look for an item in the QRadar reference set than add a note to the Incident.",
      "export_key": "qradar_find_reference_set_item",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628519011849,
      "name": "Example: QRadar - Find Item in Reference Set",
      "object_type": "qradar_reference_set",
      "programmatic_name": "qradar_find_reference_set_item",
      "tags": [],
      "uuid": "495f3cff-2364-49de-88e9-fea9c1ae20f3",
      "workflow_id": 108
    },
    {
      "actions": [],
      "content": {
        "version": 16,
        "workflow_id": "qradar_get_reference_table_data",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_get_reference_table_data\" isExecutable=\"true\" name=\"Example: QRadar - Get Reference Table Data\"\u003e\u003cdocumentation\u003eMake a query on a reference table and return its results into another datatable\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1nxvqxc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_07x3ec6\" name=\"QRadar Reference Table Get Table ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6450077b-708a-4e65-9eda-6e403a3f4410\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  for outer_key, item in results.content.get(\u0027data\u0027,[]).items():\\n    for inner_key, inner_item in item.items():\\n      section = incident.addRow(\u0027qradar_reference_table_queried_rows\u0027)\\n      section[\u0027table\u0027] = results.inputs.qradar_reference_table_name\\n      section[\u0027outer_key\u0027] = outer_key\\n      section[\u0027inner_key\u0027] = inner_key\\n      \\n      section[\u0027value\u0027] = inner_item[\u0027value\u0027]\\n      section[\u0027status\u0027] = \u0027active\u0027\\n      section[\u0027qradar_label\u0027] = row.qradar_label\\nelse:\\n  incident.addNote(\\\"An error occurred getting the reference table data: {} from QRadar server: {}\\\".format(results.reason, row.qradar_label))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.qradar_reference_table_name = row[\u0027reference_table\u0027]\\ninputs.qradar_label = row[\u0027qradar_label\u0027]\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1nxvqxc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z0k0dh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1nxvqxc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_07x3ec6\"/\u003e\u003cendEvent id=\"EndEvent_1nux67n\"\u003e\u003cincoming\u003eSequenceFlow_0z0k0dh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0z0k0dh\" sourceRef=\"ServiceTask_07x3ec6\" targetRef=\"EndEvent_1nux67n\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0sh11kc\"\u003e\u003ctext\u003e\u003c![CDATA[Results added to the \u0027qradar_reference_table_queried_rows\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_06q1lrf\" sourceRef=\"ServiceTask_07x3ec6\" targetRef=\"TextAnnotation_0sh11kc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_07x3ec6\" id=\"ServiceTask_07x3ec6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"329\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nxvqxc\" id=\"SequenceFlow_1nxvqxc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"329\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"218.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nux67n\" id=\"EndEvent_1nux67n_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"569\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"542\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z0k0dh\" id=\"SequenceFlow_0z0k0dh_di\"\u003e\u003comgdi:waypoint x=\"429\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"569\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"454\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0sh11kc\" id=\"TextAnnotation_0sh11kc_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"239\" x=\"423\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_06q1lrf\" id=\"Association_06q1lrf_di\"\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"500\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 16,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "Make a query on a reference table and return its results into another datatable",
      "export_key": "qradar_get_reference_table_data",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628531006067,
      "name": "Example: QRadar - Get Reference Table Data",
      "object_type": "qradar_reference_table",
      "programmatic_name": "qradar_get_reference_table_data",
      "tags": [],
      "uuid": "0d7e5d45-b9d1-48cb-ab2c-9d148f5a0e22",
      "workflow_id": 75
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "example_qradar__add_reference_table_item_dt",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_qradar__add_reference_table_item_dt\" isExecutable=\"true\" name=\"Example: QRadar - Add Reference Table Item DT\"\u003e\u003cdocumentation\u003eAdd a reference table item based on an existing named reference table\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1yzers7\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ovaala\" name=\"QRadar Reference Table Add Item\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2843283c-4d98-4c71-b2e3-b0636c7a0df8\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = u\\\"\\\"\\\"QRadar Label: {}\\nOuter key: {}\\nInner key: {}\\nEntry: {}\\nReference table: {}\\\"\\\"\\\".format(results.inputs.qradar_label,\\n                              results.inputs.qradar_reference_table_item_outer_key,\\n                              results.inputs.qradar_reference_table_item_inner_key,\\n                              results.inputs.qradar_reference_table_item_value, \\n                              results.inputs.qradar_reference_table_name)\\nif results.success:\\n    incident.addNote(u\\\"Successful add\\\\n{}\\\".format(note))\\n    row.number_of_elements = str(results[\\\"content\\\"][\\\"content\\\"][\\\"number_of_elements\\\"])\\nelse:\\n    incident.addNote(u\\\"Failure to add item: {}\\\\n{}\\\".format(results[\u0027reason\u0027], note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"\\n# Example inputs \\ninputs.qradar_reference_table_name = row.reference_table\\ninputs.qradar_reference_table_item_outer_key = rule.properties.qradar_ref_table_outer_key or \\\"1\\\"\\ninputs.qradar_reference_table_item_inner_key = rule.properties.qradar_ref_table_inner_key or \\\"city\\\"\\ninputs.qradar_reference_table_item_value = rule.properties.qradar_ref_table_update\\ninputs.qradar_label = row.qradar_label\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yzers7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1jnyry3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1yzers7\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ovaala\"/\u003e\u003cendEvent id=\"EndEvent_0kkxsgk\"\u003e\u003cincoming\u003eSequenceFlow_1jnyry3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1jnyry3\" sourceRef=\"ServiceTask_1ovaala\" targetRef=\"EndEvent_0kkxsgk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0n4muq5\"\u003e\u003ctext\u003e\u003c![CDATA[Result placed in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rhmzw8\" sourceRef=\"ServiceTask_1ovaala\" targetRef=\"TextAnnotation_0n4muq5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ovaala\" id=\"ServiceTask_1ovaala_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"318\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yzers7\" id=\"SequenceFlow_1yzers7_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"318\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"213\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0kkxsgk\" id=\"EndEvent_0kkxsgk_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"526\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"499\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jnyry3\" id=\"SequenceFlow_1jnyry3_di\"\u003e\u003comgdi:waypoint x=\"418\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"526\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"472\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0n4muq5\" id=\"TextAnnotation_0n4muq5_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"410\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rhmzw8\" id=\"Association_0rhmzw8_di\"\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "Add a reference table item based on an existing named reference table",
      "export_key": "example_qradar__add_reference_table_item_dt",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1628517686527,
      "name": "Example: QRadar - Add Reference Table Item DT",
      "object_type": "qradar_reference_table",
      "programmatic_name": "example_qradar__add_reference_table_item_dt",
      "tags": [],
      "uuid": "b6056f90-c979-417a-b18e-dfaa661e24f0",
      "workflow_id": 74
    }
  ],
  "workspaces": []
}
