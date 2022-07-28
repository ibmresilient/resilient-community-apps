{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO apply a tag",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO apply a tag",
      "object_type": "mcafee_epo_tags",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4b83ab93-bdae-4f1b-8516-ad4b870c850e",
      "view_items": [
        {
          "content": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_apply_a_tag"
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
            "IP Address",
            "DNS Name",
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO apply tags",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO apply tags",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fb53f6ab-d562-4cb7-841e-23099694c171",
      "view_items": [
        {
          "content": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_apply_tags"
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
            "IP Address",
            "DNS Name",
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO get system info",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO get system info",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "58a2bcde-39cb-40e9-ab23-7f7da4c6cc26",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_system_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO list tags",
      "id": 17,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO list tags",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9567fff9-5b8a-4d12-8e83-cde96e8b3ec9",
      "view_items": [],
      "workflows": [
        "mcafee_epo_list_tags"
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
            "IP Address",
            "DNS Name",
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO remove tags",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO remove tags",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fcd70bd0-931e-42d5-886a-db45920f2af5",
      "view_items": [
        {
          "content": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_remove_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Wake up Agent",
      "id": 19,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Wake up Agent",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f273f809-b8f7-4420-8c35-e8c00b767bb7",
      "view_items": [
        {
          "content": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_wake_up_agent"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1658860088638,
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
      "export_key": "__function/mcafee_epo_systems",
      "hide_notification": false,
      "id": 277,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_systems",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mcafee_epo_systems",
      "tooltip": "Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO",
      "type_id": 11,
      "uuid": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
      "export_key": "__function/mcafee_epo_tag",
      "hide_notification": false,
      "id": 276,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_tag",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mcafee_epo_tag",
      "tooltip": "Tag managed on ePO",
      "type_id": 11,
      "uuid": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
      "export_key": "actioninvocation/epo_system",
      "hide_notification": false,
      "id": 274,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_system",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ePO System",
      "tooltip": "Comma seperated list of systems properties or one system ",
      "type_id": 6,
      "uuid": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
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
      "export_key": "actioninvocation/ss_tags",
      "hide_notification": false,
      "id": 275,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "ss_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "List of tags",
      "tooltip": "Multiselect tags. Edit the list for your system",
      "type_id": 6,
      "uuid": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "a6e80147-c8ac-4c7f-b8d1-ac68a8406a37",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Excluded from Compliance Check",
          "properties": null,
          "uuid": "cb328af4-0cf1-49a7-87c0-89e846125299",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Server",
          "properties": null,
          "uuid": "4a896abb-838a-4cb0-a501-4a3e296b6c7d",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Shut Down",
          "properties": null,
          "uuid": "2fae2f32-cf34-4494-8c2d-4b86896b815b",
          "value": 55
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Workstation",
          "properties": null,
          "uuid": "2a7a4656-6043-4bb6-9379-1f71a92ebd20",
          "value": 56
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u0100 \u0101 \u0102 \u0103 \u0104 \u0105",
          "properties": null,
          "uuid": "9bf8605d-5791-4ef8-9095-bb9866bfb010",
          "value": 57
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
      "created_date": 1656008479060,
      "description": {
        "content": "Find an ePO system based on a property such as system name, tag, IP address, MAC address, etc.",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO find a system",
      "export_key": "mcafee_epo_find_a_system",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656008479117,
      "name": "mcafee_epo_find_a_system",
      "tags": [],
      "uuid": "0030078d-417f-4d92-9212-6853914b56af",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
          "name": "McAfee ePO get system info",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_get_system_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Get System Info from Property",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_system_info_from_property",
          "tags": [],
          "uuid": null,
          "workflow_id": 49
        }
      ]
    },
    {
      "created_date": 1656008479154,
      "description": {
        "content": "Find all tags specified in ePO",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO list tags",
      "export_key": "mcafee_epo_list_tags",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656008479197,
      "name": "mcafee_epo_list_tags",
      "tags": [],
      "uuid": "b9d82be9-83b0-4b88-90ca-7e0d2fb09dc7",
      "version": 1,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO list tags",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_list_tags",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1656008479232,
      "description": {
        "content": "Remove a tag associated with an ePO system(s).",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO remove tag",
      "export_key": "mcafee_epo_remove_tag",
      "id": 3,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656008479277,
      "name": "mcafee_epo_remove_tag",
      "tags": [],
      "uuid": "1cb1fd7a-0eeb-4230-9edb-c8f6f47b1ae9",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
          "name": "McAfee ePO remove tag",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_remove_tag",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1657036188744,
      "description": {
        "content": "Wake up an ePO agent",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Wake up agent",
      "export_key": "mcafee_epo_wake_up_agent",
      "id": 5,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1657036188858,
      "name": "mcafee_epo_wake_up_agent",
      "tags": [],
      "uuid": "a8b3bef5-36fc-4d69-b366-6fd3def996d2",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
          "name": "McAfee ePO Wake up Agent",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_wake_up_agent",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        }
      ]
    },
    {
      "created_date": 1656008479311,
      "description": {
        "content": "Applies tag to the systems in ePO. Inputs include:\n- mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.\n- mcafee_epo_tag: A tag managed on ePO.",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee tag an ePO asset",
      "export_key": "mcafee_tag_an_epo_asset",
      "id": 4,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656008479356,
      "name": "mcafee_tag_an_epo_asset",
      "tags": [],
      "uuid": "67c5b852-f38f-40f7-8a68-1ae8e8a78549",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
          "name": "McAfee ePO apply a tag",
          "object_type": "mcafee_epo_tags",
          "programmatic_name": "mcafee_epo_apply_a_tag",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO apply tags",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_apply_tags",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 13,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1658860087505,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1658860087505,
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
      "export_key": "mcafee_epo_message_destination",
      "name": "McAfee ePO Message Destination",
      "programmatic_name": "mcafee_epo_message_destination",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "b0a31bf9-305f-4120-a5e6-aab5a965cac6"
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
      "display_name": "McAfee ePO tags",
      "export_key": "mcafee_epo_tags",
      "fields": {
        "epo_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_id",
          "hide_notification": false,
          "id": 271,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "epo_id",
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
          "text": "Id",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "565bbe14-2671-442e-9f9c-1fd9cdc82dd5",
          "values": [],
          "width": 35
        },
        "epo_notes": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_notes",
          "hide_notification": false,
          "id": 272,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "epo_notes",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Notes",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "bf2dc924-ab97-40fe-abba-3e395d175323",
          "values": [],
          "width": 490
        },
        "epo_tag": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_tag",
          "hide_notification": false,
          "id": 273,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "epo_tag",
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
          "text": "Tag",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "033ee0aa-d253-47c1-976e-0bcfbce40f46",
          "values": [],
          "width": 88
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
      "type_name": "mcafee_epo_tags",
      "uuid": "b40555f7-9353-447e-b4c3-2ac166936dfa"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "mcafee_epo_remove_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_remove_tag\" isExecutable=\"true\" name=\"McAfee ePO remove tag\"\u003e\u003cdocumentation\u003eRemove tag(s) from an ePO system. This workflow use an artifact representing the system to tag.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pzlzpj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1spfyme\" name=\"McAfee ePO remove tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1cb1fd7a-0eeb-4230-9edb-c8f6f47b1ae9\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.content:\\n  note = u\\\"ePO system not found or tag not applied: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\nelse:\\n  note = u\\\"ePO tag(s) removed: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, note)\\nelse:\\n  artifact.description = note\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\\ninputs.mcafee_epo_tag = str(rule.properties.ss_tags)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pzlzpj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ygkcww\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1pzlzpj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1spfyme\"/\u003e\u003cendEvent id=\"EndEvent_1johhu0\"\u003e\u003cincoming\u003eSequenceFlow_1ygkcww\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ygkcww\" sourceRef=\"ServiceTask_1spfyme\" targetRef=\"EndEvent_1johhu0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1spfyme\" id=\"ServiceTask_1spfyme_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pzlzpj\" id=\"SequenceFlow_1pzlzpj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1johhu0\" id=\"EndEvent_1johhu0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"400\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"418\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ygkcww\" id=\"SequenceFlow_1ygkcww_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"376\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Remove tag(s) from an ePO system. This workflow use an artifact representing the system to tag.",
      "export_key": "mcafee_epo_remove_tag",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656686143855,
      "name": "McAfee ePO remove tag",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_remove_tag",
      "tags": [],
      "uuid": "477b4168-74da-4c1a-b073-4e4be021b89a",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "mcafee_epo_list_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_list_tags\" isExecutable=\"true\" name=\"McAfee ePO list tags\"\u003e\u003cdocumentation\u003eList available tags defined in ePO. Results are displayed in a datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0a2179k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1734ypy\" name=\"McAfee ePO list tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b9d82be9-83b0-4b88-90ca-7e0d2fb09dc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  for tag in sorted(results.content, key = lambda i: i[\u0027tagName\u0027].lower()):\\n    row = incident.addRow(\\\"mcafee_epo_tags\\\")\\n    row[\u0027epo_id\u0027] = tag[\u0027tagId\u0027]\\n    row[\u0027epo_tag\u0027] = tag[\u0027tagName\u0027]\\n    row[\u0027epo_notes\u0027] = tag[\u0027tagNotes\u0027]\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0a2179k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081gl9p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0a2179k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1734ypy\"/\u003e\u003cendEvent id=\"EndEvent_1sd36bh\"\u003e\u003cincoming\u003eSequenceFlow_081gl9p\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081gl9p\" sourceRef=\"ServiceTask_1734ypy\" targetRef=\"EndEvent_1sd36bh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ryo4jh\"\u003e\u003ctext\u003e\u003c![CDATA[Display results in a datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0qxjkvx\" sourceRef=\"ServiceTask_1734ypy\" targetRef=\"TextAnnotation_1ryo4jh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1734ypy\" id=\"ServiceTask_1734ypy_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0a2179k\" id=\"SequenceFlow_0a2179k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1sd36bh\" id=\"EndEvent_1sd36bh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"411.8027906976744\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"429.8027906976744\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081gl9p\" id=\"SequenceFlow_081gl9p_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"383.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ryo4jh\" id=\"TextAnnotation_1ryo4jh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"349\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0qxjkvx\" id=\"Association_0qxjkvx_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "List available tags defined in ePO. Results are displayed in a datatable.",
      "export_key": "mcafee_epo_list_tags",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656686122002,
      "name": "McAfee ePO list tags",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_list_tags",
      "tags": [],
      "uuid": "50099f17-2f9a-4b2d-91d2-63625065cfee",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "mcafee_epo_apply_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_apply_tags\" isExecutable=\"true\" name=\"McAfee ePO apply tags\"\u003e\u003cdocumentation\u003eApply tag(s) to an ePO system. This workflow uses an artifact as representing the ePO system to tag.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mees7m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16nkdp9\" name=\"McAfee tag an ePO asset\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"67c5b852-f38f-40f7-8a68-1ae8e8a78549\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.content:\\n  note = u\\\"ePO tag(s) added: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\nelse:\\n  note = u\\\"ePO system not found or tag already applied: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, note)\\nelse:\\n  artifact.description = note\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\\ninputs.mcafee_epo_tag = str(rule.properties.ss_tags)\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mees7m\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jns448\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mees7m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16nkdp9\"/\u003e\u003cendEvent id=\"EndEvent_0ct39x5\"\u003e\u003cincoming\u003eSequenceFlow_0jns448\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jns448\" sourceRef=\"ServiceTask_16nkdp9\" targetRef=\"EndEvent_0ct39x5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_15dsftr\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17pn86l\" sourceRef=\"ServiceTask_16nkdp9\" targetRef=\"TextAnnotation_15dsftr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16nkdp9\" id=\"ServiceTask_16nkdp9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"264\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mees7m\" id=\"SequenceFlow_1mees7m_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"231\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ct39x5\" id=\"EndEvent_0ct39x5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jns448\" id=\"SequenceFlow_0jns448_di\"\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"395\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_15dsftr\" id=\"TextAnnotation_15dsftr_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"137\" x=\"353\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17pn86l\" id=\"Association_17pn86l_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Apply tag(s) to an ePO system. This workflow uses an artifact as representing the ePO system to tag.",
      "export_key": "mcafee_epo_apply_tags",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656686039392,
      "name": "McAfee ePO apply tags",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_apply_tags",
      "tags": [],
      "uuid": "23de1b1f-1cb8-4f97-95fa-bb2a8e657cfb",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "mcafee_epo_wake_up_agent",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_wake_up_agent\" isExecutable=\"true\" name=\"McAfee ePO Wake up Agent\"\u003e\u003cdocumentation\u003eWake up agent\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qn10xw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0wapcdn\" name=\"McAfee ePO Wake up agent\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a8b3bef5-36fc-4d69-b366-6fd3def996d2\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addNote(results[\\\"content\\\"])\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = rule.properties.epo_system\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qn10xw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0i01ddl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qn10xw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0wapcdn\"/\u003e\u003cendEvent id=\"EndEvent_0yc6dui\"\u003e\u003cincoming\u003eSequenceFlow_0i01ddl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0i01ddl\" sourceRef=\"ServiceTask_0wapcdn\" targetRef=\"EndEvent_0yc6dui\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0wapcdn\" id=\"ServiceTask_0wapcdn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"283\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qn10xw\" id=\"SequenceFlow_1qn10xw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"283\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"240.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0yc6dui\" id=\"EndEvent_0yc6dui_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"435\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0i01ddl\" id=\"SequenceFlow_0i01ddl_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "description": "Wake up agent",
      "export_key": "mcafee_epo_wake_up_agent",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658843726546,
      "name": "McAfee ePO Wake up Agent",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_wake_up_agent",
      "tags": [],
      "uuid": "902abf9a-af7b-47f5-9d3b-c567e0f3ae56",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "mcafee_epo_get_system_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_system_info\" isExecutable=\"true\" name=\"McAfee ePO get system info\"\u003e\u003cdocumentation\u003eGet information on an ePO system\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ww09gi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_02avpdz\" name=\"McAfee ePO find a system\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0030078d-417f-4d92-9212-6853914b56af\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.content:\\n  info = u\\\"ePO system not found\\\"\\nelse:\\n  info = u\\\"ePO system info\\\\n\\\"\\n  for system in results.content:\\n    for setting in system:\\n      info = u\\\"{}\\\\n{}: {}\\\".format(info, setting, system[setting])\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, info)\\nelse:\\n  artifact.description = info\\n\\nincident.addNote(info)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ww09gi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11w64qz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ww09gi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_02avpdz\"/\u003e\u003cendEvent id=\"EndEvent_1shs028\"\u003e\u003cincoming\u003eSequenceFlow_11w64qz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_11w64qz\" sourceRef=\"ServiceTask_02avpdz\" targetRef=\"EndEvent_1shs028\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1p16xdz\"\u003e\u003ctext\u003e\u003c![CDATA[Return system info as the artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0v38vt5\" sourceRef=\"ServiceTask_02avpdz\" targetRef=\"TextAnnotation_1p16xdz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_02avpdz\" id=\"ServiceTask_02avpdz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ww09gi\" id=\"SequenceFlow_0ww09gi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1shs028\" id=\"EndEvent_1shs028_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"405\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"423\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11w64qz\" id=\"SequenceFlow_11w64qz_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"378.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1p16xdz\" id=\"TextAnnotation_1p16xdz_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"178\" x=\"347\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0v38vt5\" id=\"Association_0v38vt5_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Get information on an ePO system",
      "export_key": "mcafee_epo_get_system_info",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1657131067684,
      "name": "McAfee ePO get system info",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_get_system_info",
      "tags": [],
      "uuid": "1498bc37-0695-4b96-9fa8-02fee0c06da4",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "mcafee_epo_apply_a_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_apply_a_tag\" isExecutable=\"true\" name=\"McAfee ePO apply a tag\"\u003e\u003cdocumentation\u003eApply a tag to an ePO system from a list of tags\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_141ihiy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1lbiutl\" name=\"McAfee tag an ePO asset\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"67c5b852-f38f-40f7-8a68-1ae8e8a78549\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.content:\\n  note = u\\\"ePO tags: {} applied to system(s): {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027], results.inputs[\u0027mcafee_epo_systems\u0027])\\nelse:\\n  note = u\\\"ePO system(s): {} either not found or tag already applied for tags: {}\\\".format(results.inputs[\u0027mcafee_epo_systems\u0027], results.inputs[\u0027mcafee_epo_tag\u0027])\\n\\nincident.addNote(note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = rule.properties.epo_system\\ninputs.mcafee_epo_tag = row[\u0027epo_tag\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_141ihiy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1pimmx0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_141ihiy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1lbiutl\"/\u003e\u003cendEvent id=\"EndEvent_10zkq01\"\u003e\u003cincoming\u003eSequenceFlow_1pimmx0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pimmx0\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"EndEvent_10zkq01\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_143umko\"\u003e\u003ctext\u003e\u003c![CDATA[A note is written with the result\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1oemzei\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"TextAnnotation_143umko\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04zssm3\"\u003e\u003ctext\u003e\u003c![CDATA[The ePO asset is\u00a0 input through a rule dialog\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vgvj54\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"TextAnnotation_04zssm3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1lbiutl\" id=\"ServiceTask_1lbiutl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_141ihiy\" id=\"SequenceFlow_141ihiy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10zkq01\" id=\"EndEvent_10zkq01_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"421\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pimmx0\" id=\"SequenceFlow_1pimmx0_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"386\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_143umko\" id=\"TextAnnotation_143umko_di\"\u003e\u003comgdc:Bounds height=\"55\" width=\"192\" x=\"338\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1oemzei\" id=\"Association_1oemzei_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"398\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04zssm3\" id=\"TextAnnotation_04zssm3_di\"\u003e\u003comgdc:Bounds height=\"44\" width=\"131\" x=\"130\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vgvj54\" id=\"Association_1vgvj54_di\"\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"218\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Apply a tag to an ePO system from a list of tags",
      "export_key": "mcafee_epo_apply_a_tag",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1658844230311,
      "name": "McAfee ePO apply a tag",
      "object_type": "mcafee_epo_tags",
      "programmatic_name": "mcafee_epo_apply_a_tag",
      "tags": [],
      "uuid": "d8b90c47-57fa-43db-acb2-bcca4812fb2c",
      "workflow_id": 5
    }
  ],
  "workspaces": []
}
