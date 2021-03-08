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
          "value": "String"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        }
      ],
      "enabled": true,
      "export_key": "Cisco ASA Add Artifact to Network Object Group",
      "id": 19,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Cisco ASA Add Artifact to Network Object Group",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "56ec3aa6-c24d-431b-b142-3a0422484ab4",
      "view_items": [
        {
          "content": "a542b836-087c-4e9f-a491-9bf74a9a6239",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Choose one network object from select list or enter it in the text edit box:",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea791e0d-0210-4977-9cc1-06eac0bbd259",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b7513342-0767-4d4d-aadc-176510d26ad6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "cisco_asa_add_artifact_to_network_object_group"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "cisco_asa_network_object_dt.cisco_asa_status",
          "method": "equals",
          "type": null,
          "value": "Add"
        }
      ],
      "enabled": true,
      "export_key": "Cisco ASA Add Network Object to Network Object Group",
      "id": 21,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Cisco ASA Add Network Object to Network Object Group",
      "object_type": "cisco_asa_network_object_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "978abcaa-a304-4122-81af-b2252f6c6f2e",
      "view_items": [],
      "workflows": [
        "cisco_asa_add_network_object_to_network_object_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Cisco ASA Get Network Object Group",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Cisco ASA Get Network Object Group",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "244e64bd-d370-4151-ae81-244b5055cb98",
      "view_items": [
        {
          "content": "a542b836-087c-4e9f-a491-9bf74a9a6239",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Choose One Network Object from select list or enter in the text edit box:",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea791e0d-0210-4977-9cc1-06eac0bbd259",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b7513342-0767-4d4d-aadc-176510d26ad6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "cisco_asa_get_network_object_group"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "cisco_asa_network_object_dt.cisco_asa_status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Cisco ASA Remove Network Object from Network Object Group",
      "id": 20,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Cisco ASA Remove Network Object from Network Object Group",
      "object_type": "cisco_asa_network_object_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d1cbf8bd-d6d6-4d16-840c-462a272252ec",
      "view_items": [],
      "workflows": [
        "cisco_asa_remove_network_object_from_network_object_group"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1614770549708,
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
      "export_key": "__function/cisco_asa_firewall",
      "hide_notification": false,
      "id": 198,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_firewall",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "cisco_asa_firewall",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6e5a3cb6-18fe-4dae-9b87-a8c5d889b070",
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
      "export_key": "__function/cisco_asa_network_object_kind",
      "hide_notification": false,
      "id": 211,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_network_object_kind",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "cisco_asa_network_object_kind",
      "tooltip": "",
      "type_id": 11,
      "uuid": "eec1b660-8cf0-45ac-8a1b-cb5f40b7c52b",
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
      "export_key": "__function/cisco_asa_network_object_group",
      "hide_notification": false,
      "id": 193,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_network_object_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "cisco_asa_network_object_group",
      "tooltip": "",
      "type_id": 11,
      "uuid": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
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
      "export_key": "__function/cisco_asa_network_object_value",
      "hide_notification": false,
      "id": 210,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_network_object_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "cisco_asa_network_object_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ed9ad5be-b3c3-4105-926d-57c63228a592",
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
      "export_key": "__function/cisco_asa_artifact_type",
      "hide_notification": false,
      "id": 209,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "cisco_asa_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2f25706e-1951-4911-b198-11fb4c73c973",
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
      "export_key": "actioninvocation/cisco_asa_firewall",
      "hide_notification": false,
      "id": 205,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_firewall",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Cisco ASA Firewall",
      "tooltip": "",
      "type_id": 6,
      "uuid": "a542b836-087c-4e9f-a491-9bf74a9a6239",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "firewall_1",
          "properties": null,
          "uuid": "af5e58e6-b0f3-46f9-9c03-896e743aaa29",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "firewall_2",
          "properties": null,
          "uuid": "9f031da0-c0ca-4057-bea1-f38244e49068",
          "value": 53
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
      "export_key": "actioninvocation/cisco_asa_network_object_group_override",
      "hide_notification": false,
      "id": 208,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_network_object_group_override",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Cisco ASA Network Object Group Override",
      "tooltip": "To override the default Cisco ASA Network Object Group enter text here.",
      "type_id": 6,
      "uuid": "b7513342-0767-4d4d-aadc-176510d26ad6",
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
      "export_key": "actioninvocation/cisco_asa_network_object_group",
      "hide_notification": false,
      "id": 207,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "cisco_asa_network_object_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Cisco ASA Network Object Group",
      "tooltip": "",
      "type_id": 6,
      "uuid": "ea791e0d-0210-4977-9cc1-06eac0bbd259",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BLACKLIST_IN",
          "properties": null,
          "uuid": "f0cdf386-3357-4e24-883e-c2038986904f",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BLACKLIST_OUT",
          "properties": null,
          "uuid": "0beb379d-8ac7-4fae-b22d-240cae218598",
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
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add an artifact to a Cisco ASA network object group.",
        "format": "text"
      },
      "destination_handle": "fn_cisco_asa",
      "display_name": "Cisco ASA Add Artifact to Network Object Group",
      "export_key": "cisco_asa_add_artifact_to_network_object_group",
      "id": 5,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1614770134031,
      "name": "cisco_asa_add_artifact_to_network_object_group",
      "tags": [],
      "uuid": "95186e9d-4ebe-438e-aa4a-6f03d1a75055",
      "version": 1,
      "view_items": [
        {
          "content": "6e5a3cb6-18fe-4dae-9b87-a8c5d889b070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed9ad5be-b3c3-4105-926d-57c63228a592",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f25706e-1951-4911-b198-11fb4c73c973",
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
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add a network object to the network object group.",
        "format": "text"
      },
      "destination_handle": "fn_cisco_asa",
      "display_name": "Cisco ASA Add Network Object to Network Object Group",
      "export_key": "cisco_asa_add_network_object_to_network_object_group",
      "id": 3,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1614728034436,
      "name": "cisco_asa_add_network_object_to_network_object_group",
      "tags": [],
      "uuid": "cad2bb7d-4100-4a52-b3ef-37aca32a0504",
      "version": 3,
      "view_items": [
        {
          "content": "6e5a3cb6-18fe-4dae-9b87-a8c5d889b070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed9ad5be-b3c3-4105-926d-57c63228a592",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2f25706e-1951-4911-b198-11fb4c73c973",
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
          "name": "Cisco ASA Add Artifact to Network Object Group",
          "object_type": "artifact",
          "programmatic_name": "cisco_asa_add_artifact_to_network_object_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        },
        {
          "actions": [],
          "description": null,
          "name": "Cisco ASA Add Network Object to Network Object Group",
          "object_type": "cisco_asa_network_object_dt",
          "programmatic_name": "cisco_asa_add_network_object_to_network_object_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Query the Cisco ASA firewall and return the network objects contained in the specified network object group.",
        "format": "text"
      },
      "destination_handle": "fn_cisco_asa",
      "display_name": "Cisco ASA Get Network Objects",
      "export_key": "cisco_asa_get_network_objects",
      "id": 2,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1614372614171,
      "name": "cisco_asa_get_network_objects",
      "tags": [],
      "uuid": "af7d53df-369d-4e78-b33b-865d5a85895a",
      "version": 2,
      "view_items": [
        {
          "content": "6e5a3cb6-18fe-4dae-9b87-a8c5d889b070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
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
          "name": "Cisco ASA Get Network Object Group",
          "object_type": "incident",
          "programmatic_name": "cisco_asa_get_network_object_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Remove a network object from a Cisco ASA network object group.",
        "format": "text"
      },
      "destination_handle": "fn_cisco_asa",
      "display_name": "Cisco ASA Remove Network Object from Network Object Group",
      "export_key": "cisco_asa_remove_network_object_from_network_object_group",
      "id": 4,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1614757444863,
      "name": "cisco_asa_remove_network_object_from_network_object_group",
      "tags": [],
      "uuid": "50488692-9f80-4d9b-ad88-44e5a80e4fc7",
      "version": 3,
      "view_items": [
        {
          "content": "6e5a3cb6-18fe-4dae-9b87-a8c5d889b070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed9ad5be-b3c3-4105-926d-57c63228a592",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eec1b660-8cf0-45ac-8a1b-cb5f40b7c52b",
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
          "name": "Cisco ASA Remove Network Object from Network Object Group",
          "object_type": "cisco_asa_network_object_dt",
          "programmatic_name": "cisco_asa_remove_network_object_from_network_object_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 51,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1615244841822,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1615244841822,
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
      "export_key": "fn_cisco_asa",
      "name": "fn_cisco_asa",
      "programmatic_name": "fn_cisco_asa",
      "tags": [],
      "users": [
        "a@a.com"
      ],
      "uuid": "f2d03418-d087-4bb9-bd22-e83163f3e7d2"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 5832,
    "major": 37,
    "minor": 0,
    "version": "37.0.5832"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Cisco ASA Network Objects",
      "export_key": "cisco_asa_network_object_dt",
      "fields": {
        "cisco_asa_firewall": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_firewall",
          "hide_notification": false,
          "id": 194,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_firewall",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Cisco ASA Firewall",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "bad68072-c0ed-4111-af17-02132d5703e6",
          "values": [],
          "width": 209
        },
        "cisco_asa_network_object_group": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_network_object_group",
          "hide_notification": false,
          "id": 206,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_network_object_group",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Network Object Group",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "cd122676-2cc8-4910-94d5-c464667c99ab",
          "values": [],
          "width": 57
        },
        "cisco_asa_network_object_kind": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_network_object_kind",
          "hide_notification": false,
          "id": 195,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_network_object_kind",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Object Kind",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "15e613da-fd20-4513-a552-e60b50e99a04",
          "values": [],
          "width": 277
        },
        "cisco_asa_network_object_value": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_network_object_value",
          "hide_notification": false,
          "id": 196,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_network_object_value",
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
          "text": "Object Value",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "c1cf3945-a2c9-4a54-bf7a-ddb91a534e25",
          "values": [],
          "width": 203
        },
        "cisco_asa_query_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_query_date",
          "hide_notification": false,
          "id": 197,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_query_date",
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
          "text": "Query Date",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "1cea6acc-1d2e-4220-a8b7-dcd31da6aae2",
          "values": [],
          "width": 39
        },
        "cisco_asa_status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "cisco_asa_network_object_dt/cisco_asa_status",
          "hide_notification": false,
          "id": 203,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "cisco_asa_status",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "63d95a32-0480-4795-9e8a-0afe2bf150a8",
          "values": [],
          "width": 43
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
      "type_name": "cisco_asa_network_object_dt",
      "uuid": "b60c1bf0-cfb6-44d8-804c-229b1be36466"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "cisco_asa_remove_network_object_from_network_object_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"cisco_asa_remove_network_object_from_network_object_group\" isExecutable=\"true\" name=\"Cisco ASA Remove Network Object from Network Object Group\"\u003e\u003cdocumentation\u003eRemove the network object from the specified Cisco ASA network object group and delete the row from the data table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0zs3em8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0qz9u75\" name=\"Cisco ASA Remove Network Object f...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50488692-9f80-4d9b-ad88-44e5a80e4fc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nif results.success:\\n  text = \\\"Removed\\\"\\nelse:\\n  text = \\\"NotFound\\\"\\n  \\nstatus_text = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=\\\"red\\\", status=text)\\nrow[\u0027cisco_asa_status\u0027] = helper.createRichText(status_text)\\nrow[\\\"cisco_asa_query_date\\\" = Date()\\n\",\"pre_processing_script\":\"inputs.cisco_asa_firewall = row.cisco_asa_firewall\\ninputs.cisco_asa_network_object_group = row.cisco_asa_network_object_group\\ninputs.cisco_asa_network_object_kind = row.cisco_asa_network_object_kind\\ninputs.cisco_asa_network_object_value = row.cisco_asa_network_object_value\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zs3em8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1un9ebq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zs3em8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qz9u75\"/\u003e\u003cendEvent id=\"EndEvent_1busvxw\"\u003e\u003cincoming\u003eSequenceFlow_1un9ebq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1un9ebq\" sourceRef=\"ServiceTask_0qz9u75\" targetRef=\"EndEvent_1busvxw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qz9u75\" id=\"ServiceTask_0qz9u75_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"482\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zs3em8\" id=\"SequenceFlow_0zs3em8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"295\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1busvxw\" id=\"EndEvent_1busvxw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"840\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"858\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1un9ebq\" id=\"SequenceFlow_1un9ebq_di\"\u003e\u003comgdi:waypoint x=\"582\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003comgdi:waypoint x=\"840\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"666\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "a@a.com",
      "description": "Remove the network object from the specified Cisco ASA network object group and delete the row from the data table.",
      "export_key": "cisco_asa_remove_network_object_from_network_object_group",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1614768697209,
      "name": "Cisco ASA Remove Network Object from Network Object Group",
      "object_type": "cisco_asa_network_object_dt",
      "programmatic_name": "cisco_asa_remove_network_object_from_network_object_group",
      "tags": [],
      "uuid": "a3e14aae-44a2-421e-a4e3-d15b7438faa8",
      "workflow_id": 9
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "cisco_asa_add_artifact_to_network_object_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"cisco_asa_add_artifact_to_network_object_group\" isExecutable=\"true\" name=\"Cisco ASA Add Artifact to Network Object Group\"\u003e\u003cdocumentation\u003eAdd an artifact to the Cisco ASA network object group.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10x6vmu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ygvk97\" name=\"Cisco ASA Add Network Object to N...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"cad2bb7d-4100-4a52-b3ef-37aca32a0504\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nif results.get(\\\"success\\\"):\\n\\n  content = results.get(\\\"content\\\")\\n  firewall = content.get(\\\"firewall\\\")\\n  network_object_group = content.get(\\\"network_object_group\\\")\\n  network_object_kind = content.get(\\\"network_object_kind\\\")\\n  network_object_value = content.get(\\\"network_object_value\\\")\\n\\n  # Add each email as a row in the query results data table\\n  network_object_row = incident.addRow(\\\"cisco_asa_network_object_dt\\\")\\n  network_object_row.cisco_asa_query_date = Date()\\n  network_object_row.cisco_asa_firewall = firewall\\n  network_object_row.cisco_asa_network_object_group = network_object_group\\n  network_object_row.cisco_asa_network_object_kind = network_object_kind\\n  network_object_row.cisco_asa_network_object_value = network_object_value\\n  network_object_row.cisco_asa_status = \\\"Active\\\"\",\"pre_processing_script\":\"inputs.cisco_asa_firewall = rule.properties.cisco_asa_firewall\\noverride = rule.properties.cisco_asa_network_object_group_override\\nif override is \\\"\\\" or override is None:\\n  inputs.cisco_asa_network_object_group = rule.properties.cisco_asa_network_object_group\\nelse:\\n  inputs.cisco_asa_network_object_group = override\\ninputs.cisco_asa_network_object_value = artifact.value\\ninputs.cisco_asa_artifact_type = artifact.type\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10x6vmu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ax0yps\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10x6vmu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ygvk97\"/\u003e\u003cendEvent id=\"EndEvent_0z4dkmr\"\u003e\u003cincoming\u003eSequenceFlow_0ax0yps\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ax0yps\" sourceRef=\"ServiceTask_1ygvk97\" targetRef=\"EndEvent_0z4dkmr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ygvk97\" id=\"ServiceTask_1ygvk97_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"541\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10x6vmu\" id=\"SequenceFlow_10x6vmu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"541\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"369.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0z4dkmr\" id=\"EndEvent_0z4dkmr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"937\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"955\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ax0yps\" id=\"SequenceFlow_0ax0yps_di\"\u003e\u003comgdi:waypoint x=\"641\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"937\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"789\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@a.com",
      "description": "Add an artifact to the Cisco ASA network object group.",
      "export_key": "cisco_asa_add_artifact_to_network_object_group",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1614769984040,
      "name": "Cisco ASA Add Artifact to Network Object Group",
      "object_type": "artifact",
      "programmatic_name": "cisco_asa_add_artifact_to_network_object_group",
      "tags": [],
      "uuid": "540d75ae-8285-447f-8919-f2353ba5c971",
      "workflow_id": 11
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "cisco_asa_add_network_object_to_network_object_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"cisco_asa_add_network_object_to_network_object_group\" isExecutable=\"true\" name=\"Cisco ASA Add Network Object to Network Object Group\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0t64jhc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0mz3s17\" name=\"Cisco ASA Add Network Object to N...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"cad2bb7d-4100-4a52-b3ef-37aca32a0504\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nif results.success:\\n  text = \\\"Active\\\"\\n  \\nstatus_text = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=\\\"green\\\", status=text)\\nrow[\u0027cisco_asa_status\u0027] = helper.createRichText(status_text)\\nrow[\\\"cisco_asa_query_date\\\" = Date()\\n\",\"pre_processing_script\":\"inputs.cisco_asa_firewall = row.cisco_asa_firewall\\ninputs.cisco_asa_network_object_group = row.cisco_asa_network_object_group\\ninputs.cisco_asa_network_object_kind = row.cisco_asa_network_object_kind\\ninputs.cisco_asa_network_object_value = row.cisco_asa_network_object_value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0t64jhc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1xtx8jv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0t64jhc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0mz3s17\"/\u003e\u003cendEvent id=\"EndEvent_0js24f6\"\u003e\u003cincoming\u003eSequenceFlow_1xtx8jv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1xtx8jv\" sourceRef=\"ServiceTask_0mz3s17\" targetRef=\"EndEvent_0js24f6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0mz3s17\" id=\"ServiceTask_0mz3s17_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"510\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t64jhc\" id=\"SequenceFlow_0t64jhc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"510\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"354\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0js24f6\" id=\"EndEvent_0js24f6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"941\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"959\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xtx8jv\" id=\"SequenceFlow_1xtx8jv_di\"\u003e\u003comgdi:waypoint x=\"610\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"941\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"775.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@a.com",
      "description": "",
      "export_key": "cisco_asa_add_network_object_to_network_object_group",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1614768785173,
      "name": "Cisco ASA Add Network Object to Network Object Group",
      "object_type": "cisco_asa_network_object_dt",
      "programmatic_name": "cisco_asa_add_network_object_to_network_object_group",
      "tags": [],
      "uuid": "bfe7df3c-1b81-4ff9-9afe-a216775a4a59",
      "workflow_id": 12
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "cisco_asa_get_network_object_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"cisco_asa_get_network_object_group\" isExecutable=\"true\" name=\"Cisco ASA Get Network Object Group\"\u003e\u003cdocumentation\u003eExample workflow that gets the network objects of the specified network object group and writes them to the Cisco ASA Network Objects data table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0lrikjy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_181hekj\" name=\"Cisco ASA Get Network Objects\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"af7d53df-369d-4e78-b33b-865d5a85895a\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncontent = results.get(\\\"content\\\")\\nmember_list = content.get(\\\"members\\\")\\nfirewall = results.inputs.get(\\\"cisco_asa_firewall\\\")\\nnetwork_object_group = results.inputs.get(\\\"cisco_asa_network_object_group\\\")\\n\\n# Add each email as a row in the query results data table\\nfor network_object in member_list:\\n  network_object_row = incident.addRow(\\\"cisco_asa_network_object_dt\\\")\\n  network_object_row.cisco_asa_query_date = Date()\\n  network_object_row.cisco_asa_firewall = firewall\\n  network_object_row.cisco_asa_network_object_group = network_object_group\\n  network_object_row.cisco_asa_network_object_kind = network_object.get(\\\"kind\\\")\\n  network_object_row.cisco_asa_network_object_value = network_object.get(\\\"value\\\")\\n  status_text = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=\\\"green\\\", status=\\\"Active\\\")\\n  network_object_row.cisco_asa_status = helper.createRichText(status_text)\\n\",\"pre_processing_script\":\"inputs.cisco_asa_firewall = rule.properties.cisco_asa_firewall\\noverride = rule.properties.cisco_asa_network_object_group_override\\nif override is \\\"\\\" or override is None:\\n  inputs.cisco_asa_network_object_group = rule.properties.cisco_asa_network_object_group\\nelse:\\n  inputs.cisco_asa_network_object_group = override\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0lrikjy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0v4egf9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0lrikjy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_181hekj\"/\u003e\u003cendEvent id=\"EndEvent_14dhg81\"\u003e\u003cincoming\u003eSequenceFlow_0v4egf9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0v4egf9\" sourceRef=\"ServiceTask_181hekj\" targetRef=\"EndEvent_14dhg81\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06n52yh\"\u003e\u003ctext\u003e\u003c![CDATA[Input: Cisco ASA Host, Cisco ASA Network Object Group\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0e7erpf\" sourceRef=\"ServiceTask_181hekj\" targetRef=\"TextAnnotation_06n52yh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_017886w\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Network objects contained in the Network Object Group are written to the Network Objects data table\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_00cljd0\" sourceRef=\"ServiceTask_181hekj\" targetRef=\"TextAnnotation_017886w\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_181hekj\" id=\"ServiceTask_181hekj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"571\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lrikjy\" id=\"SequenceFlow_0lrikjy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"571\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"384.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_14dhg81\" id=\"EndEvent_14dhg81_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"976\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"994\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v4egf9\" id=\"SequenceFlow_0v4egf9_di\"\u003e\u003comgdi:waypoint x=\"671\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"976\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"823.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06n52yh\" id=\"TextAnnotation_06n52yh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"400\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0e7erpf\" id=\"Association_0e7erpf_di\"\u003e\u003comgdi:waypoint x=\"577\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"468\" xsi:type=\"omgdc:Point\" y=\"82\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_017886w\" id=\"TextAnnotation_017886w_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"749\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_00cljd0\" id=\"Association_00cljd0_di\"\u003e\u003comgdi:waypoint x=\"666\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"780\" xsi:type=\"omgdc:Point\" y=\"82\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@a.com",
      "description": "Example workflow that gets the network objects of the specified network object group and writes them to the Cisco ASA Network Objects data table.",
      "export_key": "cisco_asa_get_network_object_group",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1614768846543,
      "name": "Cisco ASA Get Network Object Group",
      "object_type": "incident",
      "programmatic_name": "cisco_asa_get_network_object_group",
      "tags": [],
      "uuid": "1a4bddfb-ef25-4fd6-ac2e-8fdc78c680dd",
      "workflow_id": 10
    }
  ],
  "workspaces": []
}
