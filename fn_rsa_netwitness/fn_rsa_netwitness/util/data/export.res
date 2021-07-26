{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "(Example) NetWitness Get Meta Values",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "(Example) NetWitness Get Meta Values",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "59b3853e-2544-40ea-aaa1-e0fdd8b6ba46",
      "view_items": [
        {
          "content": "b6ba9aab-a7be-41b5-9f09-55358372ee98",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_netwitness_get_meta_values"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "(Example) NetWitness Retrieve Log File",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "(Example) NetWitness Retrieve Log File",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a8d6a2b2-5963-4557-a46c-fb142dbedb27",
      "view_items": [
        {
          "content": "e68e122d-c289-4706-9dfe-f5080bc9edd1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2da1097c-a08a-4808-8619-862c5a54be12",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d944f34-86bf-4b92-ae88-563d598140ac",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_netwitness_retrieve_log_file"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "(Example) NetWitness Retrieve PCAP File",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [],
      "name": "(Example) NetWitness Retrieve PCAP File",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d6873150-3b3b-46c4-93e8-fd127446c970",
      "view_items": [
        {
          "content": "b6ba9aab-a7be-41b5-9f09-55358372ee98",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_netwitness_retrieve_pcap_file"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "(Example) NetWitness Retrieve PCAP File (Time)",
      "id": 17,
      "logic_type": "all",
      "message_destinations": [],
      "name": "(Example) NetWitness Retrieve PCAP File (Time)",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b137b151-7631-4371-8af7-27922d73e46c",
      "view_items": [
        {
          "content": "e68e122d-c289-4706-9dfe-f5080bc9edd1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2da1097c-a08a-4808-8619-862c5a54be12",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_netwitness_retrieve_pcap_file_time"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1627323680956,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 217,
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
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
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
      "export_key": "__function/nw_end_time",
      "hide_notification": false,
      "id": 218,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "nw_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_end_time",
      "tooltip": "End time for PCAP for log file.",
      "type_id": 11,
      "uuid": "ab3fe737-49da-4e28-ae52-b4eef2aae095",
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
      "export_key": "__function/nw_results_size",
      "hide_notification": false,
      "id": 219,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "nw_results_size",
      "operation_perms": {},
      "operations": [],
      "placeholder": "100",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_results_size",
      "tooltip": "Number of results to return back from the query, no limit is implied if nothing is set.",
      "type_id": 11,
      "uuid": "bd4dc898-2b7e-49b2-8851-fd10359951ea",
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
      "export_key": "__function/nw_start_time",
      "hide_notification": false,
      "id": 220,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "nw_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_start_time",
      "tooltip": "Start time for PCAP or log file.",
      "type_id": 11,
      "uuid": "cbdcde0a-c099-4e37-83ac-c4bdbbf3cdde",
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
      "export_key": "__function/nw_data_format",
      "hide_notification": false,
      "id": 221,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "nw_data_format",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_data_format",
      "tooltip": "Format and data to return.",
      "type_id": 11,
      "uuid": "e1123711-9103-48d1-84d7-36733ff79ded",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_text",
          "properties": null,
          "uuid": "6595d51c-128e-4597-83c8-bcde7e17ed8f",
          "value": 56
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_csv",
          "properties": null,
          "uuid": "4a52b073-a81c-429f-8586-a58d22e90ecc",
          "value": 57
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_xml",
          "properties": null,
          "uuid": "a5f04fe0-2bf7-4f2c-8c88-0e01751a6a51",
          "value": 58
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_json",
          "properties": null,
          "uuid": "6b05703f-9508-423f-8c98-48a7077566a4",
          "value": 59
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
      "export_key": "__function/nw_event_session_ids",
      "hide_notification": false,
      "id": 222,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "nw_event_session_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "9918846992,9917240212",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_event_session_ids",
      "tooltip": "Comma separated string of session IDs.",
      "type_id": 11,
      "uuid": "e5dd0ab1-8e62-4a03-96d2-bb207033800b",
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
      "export_key": "__function/nw_query",
      "hide_notification": false,
      "id": 223,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "nw_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [
        {
          "id": 1,
          "name": "alais.ip = x.x.x.x",
          "template": {
            "content": "select sessionid where alias.ip=203.205.179.181",
            "format": "text"
          },
          "uuid": "e5611009-0b22-44c4-a59c-9859f11fdcf8"
        }
      ],
      "text": "nw_query",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0f3351c8-acd1-4ae4-9840-b7e93192d566",
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
      "export_key": "__function/nw_meta_id2",
      "hide_notification": false,
      "id": 224,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "nw_meta_id2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "2326",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_meta_id2",
      "tooltip": "Last meta ID value in the range.",
      "type_id": 11,
      "uuid": "1c2505f9-4794-435a-a1f3-5e608b769cb9",
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
      "export_key": "__function/nw_session_id1",
      "hide_notification": false,
      "id": 225,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "nw_session_id1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "100",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_session_id1",
      "tooltip": "First session ID in the range.",
      "type_id": 11,
      "uuid": "230a70a3-4886-4ba9-a04b-d4c50c81d834",
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
      "export_key": "__function/nw_session_id2",
      "hide_notification": false,
      "id": 226,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "nw_session_id2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "102",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_session_id2",
      "tooltip": "Last session ID in the range.",
      "type_id": 11,
      "uuid": "2cdc191e-6ab3-434a-9b79-35c95f42dc3b",
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
      "export_key": "__function/nw_meta_id1",
      "hide_notification": false,
      "id": 227,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "nw_meta_id1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "2258",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "nw_meta_id1",
      "tooltip": "First meta ID value in the range.",
      "type_id": 11,
      "uuid": "4f88c6fa-8a7e-4adc-ac62-79e48c048fc5",
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
      "export_key": "actioninvocation/netwitness_query",
      "hide_notification": false,
      "id": 213,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "netwitness_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "select sessionid where time=\u00272018-Dec-06 08:00:00\u0027-\u00272018-Dec-06 09:00:00\u0027\u0026\u0026ip.src=10.10.10.123\u0026\u0026alias.host=example.test.com",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "NetWitness Query",
      "tooltip": "",
      "type_id": 6,
      "uuid": "b6ba9aab-a7be-41b5-9f09-55358372ee98",
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
      "export_key": "actioninvocation/netwitness_start_time",
      "hide_notification": false,
      "id": 214,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "netwitness_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "NetWitness Start Time",
      "tooltip": "",
      "type_id": 6,
      "uuid": "e68e122d-c289-4706-9dfe-f5080bc9edd1",
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
      "export_key": "actioninvocation/netwitness_end_time",
      "hide_notification": false,
      "id": 215,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "netwitness_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "NetWitness End Time",
      "tooltip": "",
      "type_id": 6,
      "uuid": "2da1097c-a08a-4808-8619-862c5a54be12",
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
      "export_key": "actioninvocation/netwitness_data_format",
      "hide_notification": false,
      "id": 216,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "netwitness_data_format",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "templates": [],
      "text": "NetWitness Data Format",
      "tooltip": "",
      "type_id": 6,
      "uuid": "7d944f34-86bf-4b92-ae88-563d598140ac",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "logs_text",
          "properties": null,
          "uuid": "305351a2-2a43-4449-a8c1-482f63e5cd98",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_csv",
          "properties": null,
          "uuid": "d2119c80-7ba3-4dcf-8ad2-44c97a1d819b",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_xml",
          "properties": null,
          "uuid": "84b8d239-fc0b-4d2b-a4e2-79366c6c9a16",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "logs_json",
          "properties": null,
          "uuid": "c034cd4a-7d7f-4531-be05-4daef2a56052",
          "value": 55
        }
      ]
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
        "content": "Returns the meta ID ranges given the start and end session IDs.",
        "format": "text"
      },
      "destination_handle": "rsa_netwitness_message_destination",
      "display_name": "NetWitness Get Meta ID ranges",
      "export_key": "netwitness_get_meta_id_ranges",
      "id": 1,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1627323289351,
      "name": "netwitness_get_meta_id_ranges",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "9517f6a9-b873-4016-a5f3-a7aba5332974",
      "version": 1,
      "view_items": [
        {
          "content": "230a70a3-4886-4ba9-a04b-d4c50c81d834",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2cdc191e-6ab3-434a-9b79-35c95f42dc3b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd4dc898-2b7e-49b2-8851-fd10359951ea",
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
          "name": "(Example) NetWitness Get Meta Values",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_get_meta_values",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 3
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
        "content": "Returns the meta values given the start and end meta IDs.",
        "format": "text"
      },
      "destination_handle": "rsa_netwitness_message_destination",
      "display_name": "NetWitness Get Meta Values",
      "export_key": "netwitness_get_meta_values",
      "id": 2,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1627323289548,
      "name": "netwitness_get_meta_values",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "1535d518-222b-447b-99b4-0caf0200d6eb",
      "version": 1,
      "view_items": [
        {
          "content": "4f88c6fa-8a7e-4adc-ac62-79e48c048fc5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1c2505f9-4794-435a-a1f3-5e608b769cb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd4dc898-2b7e-49b2-8851-fd10359951ea",
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
          "name": "(Example) NetWitness Get Meta Values",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_get_meta_values",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 3
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
        "content": "Queries NetWitness and returns metadata related to the query.",
        "format": "text"
      },
      "destination_handle": "rsa_netwitness_message_destination",
      "display_name": "NetWitness Query",
      "export_key": "netwitness_query",
      "id": 3,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1627323289758,
      "name": "netwitness_query",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "01daa61c-dc22-4b1a-9c00-24836f61e687",
      "version": 1,
      "view_items": [
        {
          "content": "0f3351c8-acd1-4ae4-9840-b7e93192d566",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd4dc898-2b7e-49b2-8851-fd10359951ea",
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
          "name": "(Example) NetWitness Get Meta Values",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_get_meta_values",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 3
        },
        {
          "actions": [],
          "description": null,
          "name": "(Example) NetWitness Retrieve PCAP File",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_retrieve_pcap_file",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 1
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
        "content": "Returns log file from NetWitness in the specified format based on the given time frame.",
        "format": "text"
      },
      "destination_handle": "rsa_netwitness_message_destination",
      "display_name": "NetWitness Retrieve Log Data",
      "export_key": "netwitness_retrieve_log_data",
      "id": 4,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1627323289987,
      "name": "netwitness_retrieve_log_data",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "410c00e1-d0ee-4f13-9ef6-53c9e95dd114",
      "version": 1,
      "view_items": [
        {
          "content": "cbdcde0a-c099-4e37-83ac-c4bdbbf3cdde",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab3fe737-49da-4e28-ae52-b4eef2aae095",
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
          "content": "e1123711-9103-48d1-84d7-36733ff79ded",
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
          "name": "(Example) NetWitness Retrieve Log File",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_retrieve_log_file",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 2
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
        "content": "Returns a PCAP file from NetWitness based on session IDs or a time frame and attaches to an incident.",
        "format": "text"
      },
      "destination_handle": "rsa_netwitness_message_destination",
      "display_name": "NetWitness Retrieve PCAP Data",
      "export_key": "netwitness_retrieve_pcap_data",
      "id": 5,
      "last_modified_by": {
        "display_name": "local",
        "id": 6,
        "name": "77a37273-a484-4fd1-8d02-2c28513d5343",
        "type": "apikey"
      },
      "last_modified_time": 1627323290229,
      "name": "netwitness_retrieve_pcap_data",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "1e6619f5-ca89-4a43-8741-cccfc6c78299",
      "version": 1,
      "view_items": [
        {
          "content": "e5dd0ab1-8e62-4a03-96d2-bb207033800b",
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
          "content": "cbdcde0a-c099-4e37-83ac-c4bdbbf3cdde",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab3fe737-49da-4e28-ae52-b4eef2aae095",
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
          "name": "(Example) NetWitness Retrieve PCAP File",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_retrieve_pcap_file",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 1
        },
        {
          "actions": [],
          "description": null,
          "name": "(Example) NetWitness Retrieve PCAP File (Time)",
          "object_type": "incident",
          "programmatic_name": "example_netwitness_retrieve_pcap_file_time",
          "tags": [
            {
              "tag_handle": "fn_rsa_netwitness",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 4,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1627323678990,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1627323678990,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "77a37273-a484-4fd1-8d02-2c28513d5343",
        "ac5c453e-edde-40a6-9330-66ff729c2ed2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "rsa_netwitness_message_destination",
      "name": "RSA NetWitness Message Destination",
      "programmatic_name": "rsa_netwitness_message_destination",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "users": [],
      "uuid": "bc786afa-b305-47ae-9903-3b5400b269c6"
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
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_netwitness_get_meta_values",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_netwitness_get_meta_values\" isExecutable=\"true\" name=\"(Example) NetWitness Get Meta Values\"\u003e\u003cdocumentation\u003eAn example that returns the meta values based on session meta ID ranges.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ztc54j\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0skjobb\" name=\"NetWitness Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"01daa61c-dc22-4b1a-9c00-24836f61e687\"\u003e{\"inputs\":{\"bd4dc898-2b7e-49b2-8851-fd10359951ea\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":50}}},\"pre_processing_script\":\"inputs.nw_query = rule.properties.netwitness_query\",\"result_name\":\"nw_query\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ztc54j\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ebl4uj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0nneig5\"\u003e\u003cincoming\u003eSequenceFlow_0jv3l16\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1ajztsj\" name=\"NetWitness Get Meta ID ranges\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9517f6a9-b873-4016-a5f3-a7aba5332974\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.nw_session_id1 = workflow.properties.nw_query.content.results.id1\\ninputs.nw_session_id2 = workflow.properties.nw_query.content.results.id2\\n\",\"result_name\":\"nw_meta_id_ranges\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ebl4uj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jfhn4l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ebl4uj\" sourceRef=\"ServiceTask_0skjobb\" targetRef=\"ServiceTask_1ajztsj\"/\u003e\u003cserviceTask id=\"ServiceTask_1c07xg0\" name=\"NetWitness Get Meta Values\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1535d518-222b-447b-99b4-0caf0200d6eb\"\u003e{\"inputs\":{\"bd4dc898-2b7e-49b2-8851-fd10359951ea\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":10}}},\"post_processing_script\":\"incident.addNote(helper.createRichText(\\\"Meta values between {} and {} are listed below.\u0026lt;br/\u0026gt; {}\\\".format(results.inputs.nw_meta_id1, results.inputs.nw_meta_id2, str(results.content.results))))\",\"pre_processing_script\":\"inputs.nw_meta_id1 = workflow.properties.nw_meta_id_ranges.content.params.field1\\ninputs.nw_meta_id2 = workflow.properties.nw_meta_id_ranges.content.params.field2\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0jfhn4l\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jv3l16\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0jfhn4l\" sourceRef=\"ServiceTask_1ajztsj\" targetRef=\"ServiceTask_1c07xg0\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0jv3l16\" sourceRef=\"ServiceTask_1c07xg0\" targetRef=\"EndEvent_0nneig5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0ztc54j\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0skjobb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0skjobb\" id=\"ServiceTask_0skjobb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nneig5\" id=\"EndEvent_0nneig5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"842\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"860\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ajztsj\" id=\"ServiceTask_1ajztsj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"467\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ebl4uj\" id=\"SequenceFlow_0ebl4uj_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"467\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"423\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1c07xg0\" id=\"ServiceTask_1c07xg0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"650.503345724907\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jfhn4l\" id=\"SequenceFlow_0jfhn4l_di\"\u003e\u003comgdi:waypoint x=\"567\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"609\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jv3l16\" id=\"SequenceFlow_0jv3l16_di\"\u003e\u003comgdi:waypoint x=\"751\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"842\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"796.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ztc54j\" id=\"SequenceFlow_0ztc54j_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "An example that returns the meta values based on session meta ID ranges.",
      "export_key": "example_netwitness_get_meta_values",
      "last_modified_by": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "last_modified_time": 1627323291973,
      "name": "(Example) NetWitness Get Meta Values",
      "object_type": "incident",
      "programmatic_name": "example_netwitness_get_meta_values",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "9cd6544d-aacc-458d-9329-f71795500185",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_netwitness_retrieve_log_file",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_netwitness_retrieve_log_file\" isExecutable=\"true\" name=\"(Example) NetWitness Retrieve Log File\"\u003e\u003cdocumentation\u003eAn example that uses NetWitness Retrieve Log Data function to return log data during a specific time frame and attaches it to the incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_063tqs9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1e0ceur\" name=\"NetWitness Retrieve Log Data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"410c00e1-d0ee-4f13-9ef6-53c9e95dd114\"\u003e{\"inputs\":{\"e1123711-9103-48d1-84d7-36733ff79ded\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"6595d51c-128e-4597-83c8-bcde7e17ed8f\"}}},\"post_processing_script\":\"# Empty log_file has been retrieved\\nif not workflow.properties.nw_log_file.content:\\n  incident.addNote(\\\"Log file for requested dates is empty\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.nw_start_time = rule.properties.netwitness_start_time\\ninputs.nw_end_time = rule.properties.netwitness_end_time\\ninputs.nw_data_format = rule.properties.netwitness_data_format\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"nw_log_file\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_063tqs9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vk0f44\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_063tqs9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1e0ceur\"/\u003e\u003cendEvent id=\"EndEvent_0n5s5yq\"\u003e\u003cincoming\u003eSequenceFlow_1vk0f44\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vk0f44\" sourceRef=\"ServiceTask_1e0ceur\" targetRef=\"EndEvent_0n5s5yq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1e0ceur\" id=\"ServiceTask_1e0ceur_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"296\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_063tqs9\" id=\"SequenceFlow_063tqs9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"296\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"247\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0n5s5yq\" id=\"EndEvent_0n5s5yq_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"505\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"478\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vk0f44\" id=\"SequenceFlow_1vk0f44_di\"\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"450.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "An example that uses NetWitness Retrieve Log Data function to return log data during a specific time frame and attaches it to the incident.",
      "export_key": "example_netwitness_retrieve_log_file",
      "last_modified_by": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "last_modified_time": 1627323291611,
      "name": "(Example) NetWitness Retrieve Log File",
      "object_type": "incident",
      "programmatic_name": "example_netwitness_retrieve_log_file",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "a7caaba7-5f5b-49f7-8534-defc7fce9fa6",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_netwitness_retrieve_pcap_file",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_netwitness_retrieve_pcap_file\" isExecutable=\"true\" name=\"(Example) NetWitness Retrieve PCAP File\"\u003e\u003cdocumentation\u003eAn example that returns a PCAP file of packet data within the given session ID range and attaches it to the incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14sx7sp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_04lg0w0\" name=\"NetWitness Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"01daa61c-dc22-4b1a-9c00-24836f61e687\"\u003e{\"inputs\":{\"bd4dc898-2b7e-49b2-8851-fd10359951ea\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":100}}},\"pre_processing_script\":\"inputs.nw_query = rule.properties.netwitness_query\",\"result_name\":\"nw_query\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14sx7sp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1kagcyq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14sx7sp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_04lg0w0\"/\u003e\u003cserviceTask id=\"ServiceTask_0gvbjpd\" name=\"NetWitness Retrieve PCAP Data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1e6619f5-ca89-4a43-8741-cccfc6c78299\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addNote(\\\"Added PCAP file for sessions {} as an attachment to the Incident.\\\".format(results.inputs.nw_event_session_ids))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"session_id1 = workflow.properties.nw_query.content.results.id1\\nsession_id2 = workflow.properties.nw_query.content.results.id2\\n\\ninputs.nw_event_session_ids = str(session_id1)+\\\", \\\"+str(session_id2)\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kagcyq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0bfsqfj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1kagcyq\" sourceRef=\"ServiceTask_04lg0w0\" targetRef=\"ServiceTask_0gvbjpd\"/\u003e\u003cendEvent id=\"EndEvent_05hj1gu\"\u003e\u003cincoming\u003eSequenceFlow_0bfsqfj\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0bfsqfj\" sourceRef=\"ServiceTask_0gvbjpd\" targetRef=\"EndEvent_05hj1gu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_04lg0w0\" id=\"ServiceTask_04lg0w0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14sx7sp\" id=\"SequenceFlow_14sx7sp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"241.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gvbjpd\" id=\"ServiceTask_0gvbjpd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"516\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kagcyq\" id=\"SequenceFlow_1kagcyq_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"516\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"450.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05hj1gu\" id=\"EndEvent_05hj1gu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"762\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"780\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bfsqfj\" id=\"SequenceFlow_0bfsqfj_di\"\u003e\u003comgdi:waypoint x=\"616\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"762\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"689\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "An example that returns a PCAP file of packet data within the given session ID range and attaches it to the incident.",
      "export_key": "example_netwitness_retrieve_pcap_file",
      "last_modified_by": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "last_modified_time": 1627323291241,
      "name": "(Example) NetWitness Retrieve PCAP File",
      "object_type": "incident",
      "programmatic_name": "example_netwitness_retrieve_pcap_file",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "a3fcd091-5559-44d9-adba-869e2c1cdb04",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_netwitness_retrieve_pcap_file_time",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_netwitness_retrieve_pcap_file_time\" isExecutable=\"true\" name=\"(Example) NetWitness Retrieve PCAP File (Time)\"\u003e\u003cdocumentation\u003eAn example that returns a PCAP file of packet data within the given time frame and attaches it to the incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15hno8i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kf710n\" name=\"NetWitness Retrieve PCAP Data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1e6619f5-ca89-4a43-8741-cccfc6c78299\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.nw_start_time = rule.properties.netwitness_start_time\\ninputs.nw_end_time = rule.properties.netwitness_end_time\\ninputs.incident_id = incident.id\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15hno8i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1m0vuvj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15hno8i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kf710n\"/\u003e\u003cendEvent id=\"EndEvent_10r7m9m\"\u003e\u003cincoming\u003eSequenceFlow_1m0vuvj\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1m0vuvj\" sourceRef=\"ServiceTask_0kf710n\" targetRef=\"EndEvent_10r7m9m\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kf710n\" id=\"ServiceTask_0kf710n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"286\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15hno8i\" id=\"SequenceFlow_15hno8i_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"242\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10r7m9m\" id=\"EndEvent_10r7m9m_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"545\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"563\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m0vuvj\" id=\"SequenceFlow_1m0vuvj_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"545\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"465.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "description": "An example that returns a PCAP file of packet data within the given time frame and attaches it to the incident.",
      "export_key": "example_netwitness_retrieve_pcap_file_time",
      "last_modified_by": "77a37273-a484-4fd1-8d02-2c28513d5343",
      "last_modified_time": 1627323292262,
      "name": "(Example) NetWitness Retrieve PCAP File (Time)",
      "object_type": "incident",
      "programmatic_name": "example_netwitness_retrieve_pcap_file_time",
      "tags": [
        {
          "tag_handle": "fn_rsa_netwitness",
          "value": null
        }
      ],
      "uuid": "e80d41a8-bbd8-46c0-9b7b-332b22d75268",
      "workflow_id": 4
    }
  ],
  "workspaces": []
}
