{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "User Account",
            "Port"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Microsoft Security Graph Alert Search",
      "id": 24,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Microsoft Security Graph Alert Search",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3083eb0d-331d-4c98-b797-ba9a77e335fc",
      "view_items": [
        {
          "content": "bb3f1411-a132-4bbc-8f5e-eadafe253974",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a91d62f-97e7-4d5a-b293-608598e1c9df",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_microsoft_security_graph_alert_search"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Microsoft Security Graph Get Details",
      "id": 25,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Microsoft Security Graph Get Details",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6a22b40e-0bc1-419d-86a6-4081764f990a",
      "view_items": [],
      "workflows": [
        "example_microsoft_security_graph_get_alert_details"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "changed_to",
          "type": null,
          "value": "Closed"
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.microsoft_security_graph_alert_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Microsoft Security Graph Resolve Alert",
      "id": 26,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Microsoft Security Graph Resolve Alert",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "6bf70434-b578-4602-b660-a4bc832ca003",
      "view_items": [],
      "workflows": [
        "example_microsoft_security_graph_resolve_alert"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Microsoft Security Graph Update Alert",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Microsoft Security Graph Update Alert",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "063cb165-3c81-476f-986f-f935b15d7353",
      "view_items": [
        {
          "content": "d95846bd-96cd-45ab-a9cb-5a8b96fadd4d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c89eb4b1-8502-4747-b4dc-eb59e698728a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b5c3ab85-9f50-451e-9e6a-9756a2dfa6b0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cefc1998-32d1-48af-a932-b972722428ab",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d87413dd-1edf-45a3-8f4e-31fb0b042637",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5106fedf-cda1-43e5-b5a7-dd787810e15e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_microsoft_security_graph_update_alert"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1649337230767,
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
      "export_key": "__function/microsoft_security_graph_alert_id",
      "hide_notification": false,
      "id": 290,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "microsoft_security_graph_alert_id",
      "tooltip": "ID of an alert.",
      "type_id": 11,
      "uuid": "a1841f3c-c510-42d7-9a46-d638fb71a979",
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
      "export_key": "__function/microsoft_security_graph_alert_search_query",
      "hide_notification": false,
      "id": 288,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_search_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "filter=assignedTo eq \u0027analyst@m365x594651.onmicrosoft.com\u0027 and severity eq \u0027high\u0027",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "microsoft_security_graph_alert_search_query",
      "tooltip": "String to filter alert search results on",
      "type_id": 11,
      "uuid": "d2012512-9b9e-4a4f-8ed2-b5376c12d578",
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
      "export_key": "__function/microsoft_security_graph_alert_data",
      "hide_notification": false,
      "id": 289,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 1,
          "name": "Vendor Info Needed",
          "template": {
            "content": "{\n        \"vendorInformation\": {\n            \"provider\": \"String\",\n            \"vendor\": \"String\"\n        }\n    }",
            "format": "text"
          },
          "uuid": "9ffc04c7-dad6-49f4-a781-4b7205b4bfff"
        },
        {
          "id": 2,
          "name": "Resolve Alert",
          "template": {
            "content": "{\n        \"status\": \"resolved\",\n        \"vendorInformation\": {\n            \"provider\": \"String\",\n            \"vendor\": \"String\"\n        }\n    }",
            "format": "text"
          },
          "uuid": "683c60cf-d394-4cfc-b7ad-66b72427218c"
        }
      ],
      "text": "microsoft_security_graph_alert_data",
      "tooltip": "JSON string of data to update an alert with.",
      "type_id": 11,
      "uuid": "f25d5a0f-7f3a-4615-b7e3-41358e2989b4",
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_comment",
      "hide_notification": false,
      "id": 286,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert comment",
      "tooltip": "",
      "type_id": 6,
      "uuid": "b5c3ab85-9f50-451e-9e6a-9756a2dfa6b0",
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
      "export_key": "actioninvocation/microsoft_security_graph_query_start_datetime",
      "hide_notification": false,
      "id": 280,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_query_start_datetime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Query Start DateTime",
      "tooltip": "",
      "type_id": 6,
      "uuid": "bb3f1411-a132-4bbc-8f5e-eadafe253974",
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_closeddatetime",
      "hide_notification": false,
      "id": 283,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_closeddatetime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert closedDateTime",
      "tooltip": "",
      "type_id": 6,
      "uuid": "c89eb4b1-8502-4747-b4dc-eb59e698728a",
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_feedback",
      "hide_notification": false,
      "id": 287,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_feedback",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert feedback",
      "tooltip": "",
      "type_id": 6,
      "uuid": "cefc1998-32d1-48af-a932-b972722428ab",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unknown",
          "properties": null,
          "uuid": "2a100da9-2e94-46ff-bfe5-0cfe7343244f",
          "value": 80
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "truePositive",
          "properties": null,
          "uuid": "837e563f-0e9f-4ae7-996c-342d9057716c",
          "value": 81
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "falsePositive",
          "properties": null,
          "uuid": "cbd22550-cb13-4264-b567-958842c6a587",
          "value": 82
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "benignPositive",
          "properties": null,
          "uuid": "342198e0-aeb6-43dc-9c31-8bf1e650b083",
          "value": 83
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_status",
      "hide_notification": false,
      "id": 282,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert status",
      "tooltip": "",
      "type_id": 6,
      "uuid": "d87413dd-1edf-45a3-8f4e-31fb0b042637",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "unknown",
          "properties": null,
          "uuid": "6c175068-e2fc-477e-a81b-f5140015728f",
          "value": 76
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "newAlert",
          "properties": null,
          "uuid": "935515e8-cafa-4a6e-a3e9-5a0a835ff195",
          "value": 77
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "inProgress",
          "properties": null,
          "uuid": "738d7832-b259-4bfc-96da-264c7af2b60f",
          "value": 78
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "resolved",
          "properties": null,
          "uuid": "e7571c0a-d1cd-4df5-9df5-a8386818bb20",
          "value": 79
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_assignedto",
      "hide_notification": false,
      "id": 285,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_assignedto",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert assignedTo",
      "tooltip": "",
      "type_id": 6,
      "uuid": "d95846bd-96cd-45ab-a9cb-5a8b96fadd4d",
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
      "export_key": "actioninvocation/microsoft_security_graph_query_end_datetime",
      "hide_notification": false,
      "id": 281,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_query_end_datetime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Query End DateTime",
      "tooltip": "",
      "type_id": 6,
      "uuid": "3a91d62f-97e7-4d5a-b293-608598e1c9df",
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
      "export_key": "actioninvocation/microsoft_security_graph_alert_tags",
      "hide_notification": false,
      "id": 284,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert tags",
      "tooltip": "",
      "type_id": 6,
      "uuid": "5106fedf-cda1-43e5-b5a7-dd787810e15e",
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
      "export_key": "incident/microsoft_security_graph_alert_id",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "microsoft_security_graph_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Field for Microsoft Security Graph Alert ID",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Microsoft Security Graph Alert ID",
      "tooltip": "ID of an alert from Microsoft Security Graph",
      "type_id": 0,
      "uuid": "bcc7f2c6-7f1f-4bb7-8e25-3586fe611afc",
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
      "created_date": 1648662013851,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Search across Microsoft Security Graph for alerts which match the corresponding search filters.",
        "format": "text"
      },
      "destination_handle": "microsoft_security_graph_message_destination",
      "display_name": "Microsoft Security Graph Alert Search",
      "export_key": "microsoft_security_graph_alert_search",
      "id": 7,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1648662013919,
      "name": "microsoft_security_graph_alert_search",
      "tags": [],
      "uuid": "c966466f-bc96-484a-b38b-f68e5f480327",
      "version": 1,
      "view_items": [
        {
          "content": "d2012512-9b9e-4a4f-8ed2-b5376c12d578",
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
          "name": "Example: Microsoft Security Graph Alert Search",
          "object_type": "artifact",
          "programmatic_name": "example_microsoft_security_graph_alert_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 13
        }
      ]
    },
    {
      "created_date": 1648662013954,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get the details of an alert from the Microsoft Security Graph API.",
        "format": "text"
      },
      "destination_handle": "microsoft_security_graph_message_destination",
      "display_name": "Microsoft Security Graph Get Alert Details",
      "export_key": "microsoft_security_graph_get_alert_details",
      "id": 8,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1648662013999,
      "name": "microsoft_security_graph_get_alert_details",
      "tags": [],
      "uuid": "c0476b6d-9d57-4a98-b74a-a867bdb3f039",
      "version": 1,
      "view_items": [
        {
          "content": "a1841f3c-c510-42d7-9a46-d638fb71a979",
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
          "name": "Example: Microsoft Security Graph Get Alert Details",
          "object_type": "incident",
          "programmatic_name": "example_microsoft_security_graph_get_alert_details",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Microsoft Security Graph Resolve Alert",
          "object_type": "incident",
          "programmatic_name": "example_microsoft_security_graph_resolve_alert",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Microsoft Security Graph Update Alert",
          "object_type": "incident",
          "programmatic_name": "example_microsoft_security_graph_update_alert",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    },
    {
      "created_date": 1648662014039,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update an alert in the Microsoft Security Graph.",
        "format": "text"
      },
      "destination_handle": "microsoft_security_graph_message_destination",
      "display_name": "Microsoft Security Graph Update Alert",
      "export_key": "microsoft_security_graph_update_alert",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1648662014083,
      "name": "microsoft_security_graph_update_alert",
      "tags": [],
      "uuid": "8e675085-820e-4e5a-983a-3943b558ba26",
      "version": 1,
      "view_items": [
        {
          "content": "a1841f3c-c510-42d7-9a46-d638fb71a979",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f25d5a0f-7f3a-4615-b7e3-41358e2989b4",
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
          "name": "Example: Microsoft Security Graph Resolve Alert",
          "object_type": "incident",
          "programmatic_name": "example_microsoft_security_graph_resolve_alert",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Microsoft Security Graph Update Alert",
          "object_type": "incident",
          "programmatic_name": "example_microsoft_security_graph_update_alert",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 9,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1649337229563,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1649337229563,
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
      "export_key": "microsoft_security_graph_message_destination",
      "name": "Microsoft Security Graph Message Destination",
      "programmatic_name": "microsoft_security_graph_message_destination",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "45af4afe-7ac1-41ed-a5bc-cbda9824bb27"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1648662013489,
      "creator_id": "admin@example.com",
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\nTypically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert json to rich text",
      "id": 2,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649336246582,
      "name": "Convert json to rich text",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text",
      "script_text": "\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, { \n    \"version\": 1.0,\n    \"header\": \"Artifact scan results for 12.34.221.1\",\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr\u003e\",\n    \"sort\": True,\n    \"json\": { \"some\": \"json\", \"omit\": \"this\", \"list\": [\"a\", \"b\", \"c\"] },\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.0, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr\u003e\", [html separator between json keys and lists or defaults to html break: \u0027\u003cbr\u003e\u0027]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\"\"\"\n\nimport re\n\nrc = re.compile(\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n  \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n  \n  def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr\u003e\", sort_keys=False):\n    self.omit_keys = omit_keys\n    self.padding = padding\n    self.separator = separator\n    self.sort_keys = sort_keys\n\n  def format_link(self, item):\n    \"\"\"[summary]\n      Find embedded urls (http(s)) and add html anchor tags to display as links\n      Args:\n          item ([string])\n\n      Returns:\n          [str]: None|original text if no links|text with html links\n    \"\"\"\n    formatted_item = item\n    if item and not isinstance(item, int) and not isinstance(item, bool):\n        list = rc.findall(item)\n        if list:\n            for link in list:\n                formatted_item = formatted_item.replace(link, \"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n    return formatted_item\n\n  def expand_list(self, list_value, is_list=False):\n    \"\"\"[summary]\n      convert items to html, adding indents to nested dictionaries.\n      Args:\n          list_value ([dict|list]): json element\n\n      Returns:\n          [str]: html converted code\n    \"\"\"\n    if not isinstance(list_value, list):\n      return self.format_link(list_value)\n    elif list_value:\n      try:\n        items = []  # this will ensure list starts on second line of key label\n        for item in list_value:\n          if isinstance(item, dict):\n            result = self.convert_json_to_rich_text(item)\n            if is_list:\n              items.append(\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, result))\n            else:\n              items.append(result)\n          elif isinstance(item, list):\n            items.append(\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(self.expand_list(item, is_list=True)))\n          else:\n            items.append(self.format_link(str(item)))\n        return \"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(self.separator.join(items))\n      except Exception as err:\n          return str(err)\n\n  def convert_json_to_rich_text(self, sub_dict):\n    \"\"\"[summary]\n      Walk dictionary tree and convert to html for better display\n      Args:\n          sub_dict ([type]): [description]\n\n      Returns:\n          [type]: [description]\n    \"\"\"\n    notes = []\n    loop_separator = \"\"  # first time through no separator\n    keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n    for key in keys:\n      value = sub_dict[key]\n\n      if key not in self.omit_keys:\n        if isinstance(value, dict):\n          result = self.convert_json_to_rich_text(value)\n          notes.append(u\"{}\u003cb\u003e{}\u003c/b\u003e: \u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(loop_separator, key, self.padding, result))\n        else:\n          notes.append(u\"{}\u003cb\u003e{}\u003c/b\u003e: {}\".format(loop_separator, key, self.expand_list(value, is_list=isinstance(value, list))))\n          \n      loop_separator = self.separator # subsequent times, add in separator\n\n    result = u\"\".join(notes)\n    return result.replace(u\"\u003c/div\u003e{0}\".format(separator), \"\u003c/div\u003e\")  # tighten up result\n\ndef get_properties(property_name):\n  \"\"\"\n  Logic to collect the json and parameters from a workflow property.\n  Args:\n    property_name: workflow property to reference\n  Returns:\n    padding, separator, header, json_omit_list, incident_field, json, sort_keys\n  \"\"\"\n  if not workflow.properties.get(property_name):\n    helper.fail(\"workflow.properties.{} undefined\".format(property_name))\n  if not workflow.properties[property_name].get(\u0027json\u0027):\n    helper.fail(\"workflow.properties.{}.json undefined\".format(property_name))\n\n  padding = workflow.properties[property_name].get(\"padding\", 10)\n  separator = workflow.properties[property_name].get(\"separator\", u\"\u003cbr\u003e\")\n  header = workflow.properties[property_name].get(\"header\")\n  json_omit_list = workflow.properties[property_name].get(\"json_omit_list\")\n  if not json_omit_list:\n    json_omit_list = []\n  incident_field = workflow.properties[property_name].get(\"incident_field\")\n  json = workflow.properties[property_name].get(\"json\")\n  if not isinstance(json, dict):\n    helper.fail(\"json element is not formatted correctly: {}\".format(json))\n  sort_keys = workflow.properties[property_name].get(\"sort\", False)\n\n  return padding, separator, header, json_omit_list, incident_field, json, sort_keys\n\n## S T A R T\npadding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\n\nif header:\n  hdr = u\"{0}{1}\".format(header, separator)\nelse:\n  hdr = u\"\"\n\nconvert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\nconverted_json = convert.convert_json_to_rich_text(json)\nresult = u\"{}{}\".format(hdr, converted_json)\n\nrich_text_note = helper.createRichText(result)\nif incident_field:\n  incident[incident_field] = rich_text_note\nelse:\n  incident.addNote(rich_text_note)\n",
      "tags": [],
      "uuid": "f7276ff0-1770-4058-9e89-40ee79c6e41b"
    }
  ],
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
        "version": 5,
        "workflow_id": "example_microsoft_security_graph_get_alert_details",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_microsoft_security_graph_get_alert_details\" isExecutable=\"true\" name=\"Example: Microsoft Security Graph Get Alert Details\"\u003e\u003cdocumentation\u003eReturns all details of an alert and adds artifacts of certain types based on the results.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02ujy4b\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qrq2z2\" name=\"Microsoft Security Graph Get Aler...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c0476b6d-9d57-4a98-b74a-a867bdb3f039\"\u003e{\"inputs\":{},\"post_processing_script\":\"user_states = results.content.userStates\\n\\nfor state in user_states:\\n  if state.logonIp:\\n    incident.addArtifact(\\\"IP Address\\\", state.logonIp, \\\"\\\")\\n\\n  if state.accountName:\\n    incident.addArtifact(\\\"User Account\\\", state.accountName, \\\"\\\")\\n\\n  if state.userPrincipalName:\\n    incident.addArtifact(\\\"User Account\\\", state.userPrincipalName, \\\"\\\")\\n\\n# Put the results json into a workflow property so we can call the\\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\njson_note = {\\n              \\\"version\\\": \\\"1.0.\\\",\\n              \\\"header\\\": \\\"Microsoft Security Graph Get Alert Details\\\",\\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.microsoft_security_graph_alert_id = incident.properties.microsoft_security_graph_alert_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02ujy4b\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_05koi9q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02ujy4b\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qrq2z2\"/\u003e\u003cscriptTask id=\"ScriptTask_0xqr1u6\" name=\"Convert json to rich text\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f7276ff0-1770-4058-9e89-40ee79c6e41b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_05koi9q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10dps91\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_05koi9q\" sourceRef=\"ServiceTask_1qrq2z2\" targetRef=\"ScriptTask_0xqr1u6\"/\u003e\u003cendEvent id=\"EndEvent_0906oyu\"\u003e\u003cincoming\u003eSequenceFlow_10dps91\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10dps91\" sourceRef=\"ScriptTask_0xqr1u6\" targetRef=\"EndEvent_0906oyu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qrq2z2\" id=\"ServiceTask_1qrq2z2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"306\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02ujy4b\" id=\"SequenceFlow_02ujy4b_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"306\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0xqr1u6\" id=\"ScriptTask_0xqr1u6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"592\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05koi9q\" id=\"SequenceFlow_05koi9q_di\"\u003e\u003comgdi:waypoint x=\"406\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"592\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"499\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0906oyu\" id=\"EndEvent_0906oyu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"864\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"882\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10dps91\" id=\"SequenceFlow_10dps91_di\"\u003e\u003comgdi:waypoint x=\"692\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"864\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"778\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "admin@example.com",
      "description": "Returns all details of an alert and adds artifacts of certain types based on the results.",
      "export_key": "example_microsoft_security_graph_get_alert_details",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649336861363,
      "name": "Example: Microsoft Security Graph Get Alert Details",
      "object_type": "incident",
      "programmatic_name": "example_microsoft_security_graph_get_alert_details",
      "tags": [],
      "uuid": "e17f4a6a-4018-480b-8dcb-c35b6a764696",
      "workflow_id": 12
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "example_microsoft_security_graph_update_alert",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_microsoft_security_graph_update_alert\" isExecutable=\"true\" name=\"Example: Microsoft Security Graph Update Alert\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Updates alert fields based on input provided in the popup module when the rule is triggered.\n\nFields that can be updated:\nassignedTo\nclosedDateTime\ncomments\nfeedback\nstatus\ntags]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0vdjzb6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_148dikw\" name=\"Microsoft Security Graph Update A...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8e675085-820e-4e5a-983a-3943b558ba26\"\u003e{\"inputs\":{\"f25d5a0f-7f3a-4615-b7e3-41358e2989b4\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n        \\\"vendorInformation\\\": {\\n            \\\"provider\\\": \\\"String\\\",\\n            \\\"vendor\\\": \\\"String\\\"\\n        }\\n    }\"}}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the\\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\njson_note = {\\\"version\\\": \\\"1.0.\\\",\\n             \\\"header\\\": \\\"Microsoft Security Graph Update Alert\\\",\\n             \\\"json\\\": results.content}\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\ninputs.microsoft_security_graph_alert_id = incident.properties.microsoft_security_graph_alert_id\\n\\nassignedTo = rule.properties.microsoft_security_graph_alert_assignedto if rule.properties.microsoft_security_graph_alert_assignedto else \\\"\\\"\\n\\nclosedDateTime = \\\"\\\"\\nif rule.properties.microsoft_security_graph_alert_closeddatetime:\\n  time_stamp = rule.properties.microsoft_security_graph_alert_closeddatetime\\n  epoch_time = Date(time_stamp)\\n  closedDateTime = \\\"\\\\\\\"closedDateTime\\\\\\\": \\\\\\\"{0}\\\\\\\",\\\".format(str(epoch_time.toInstant()))\\n  \\ncomment = rule.properties.microsoft_security_graph_alert_comment if rule.properties.microsoft_security_graph_alert_comment else \\\"\\\"\\n\\nfeedback = \\\"\\\"\\nif rule.properties.microsoft_security_graph_alert_feedback:\\n  feedback = rule.properties.microsoft_security_graph_alert_feedback\\nelif workflow.properties.msg_alert_details.content.feedback:\\n  feedback = workflow.properties.msg_alert_details.content.feedback\\n\\nstatus = rule.properties.microsoft_security_graph_alert_status if rule.properties.microsoft_security_graph_alert_status else workflow.properties.msg_alert_details.content.status\\ntags = rule.properties.microsoft_security_graph_alert_tags if rule.properties.microsoft_security_graph_alert_tags else \\\"\\\"\\n\\nprovider = workflow.properties.msg_alert_details.content.vendorInformation.provider\\nvendor = workflow.properties.msg_alert_details.content.vendorInformation.vendor\\n\\nall_comments = [\\\"\\\"]\\nif workflow.properties.msg_alert_details.content.comments:\\n  all_comments = list(workflow.properties.msg_alert_details.content.comments)\\nall_comments = all_comments + [comment]\\n\\nall_tags = [\\\"\\\"]\\nif workflow.properties.msg_alert_details.content.tags:\\n  all_tags = workflow.properties.msg_alert_details.content.tags\\nall_tags = all_tags + [tags]\\n\\n#[\\\"{5}\\\"]\\ndata = u\u0027\u0027\u0027{{\\n        \\\"assignedTo\\\": \\\"{0}\\\",\\n        {1}\\n        \\\"comments\\\": {2},\\n        \\\"feedback\\\": \\\"{3}\\\",\\n        \\\"status\\\": \\\"{4}\\\",\\n        \\\"tags\\\": {5},\\n        \\\"vendorInformation\\\":\\n        {{\\n            \\\"provider\\\": \\\"{6}\\\",\\n            \\\"vendor\\\": \\\"{7}\\\"\\n        }}\\n    }}\u0027\u0027\u0027.format(assignedTo, closedDateTime, all_comments, feedback, status, all_tags, provider, vendor)\\n\\ninputs.microsoft_security_graph_alert_data = data\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_19zuy4w\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0k8hn5l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_041hkj1\" name=\"Microsoft Security Graph Get Aler...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c0476b6d-9d57-4a98-b74a-a867bdb3f039\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.microsoft_security_graph_alert_id = incident.properties.microsoft_security_graph_alert_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"msg_alert_details\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0vdjzb6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19zuy4w\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0vdjzb6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_041hkj1\"/\u003e\u003csequenceFlow id=\"SequenceFlow_19zuy4w\" sourceRef=\"ServiceTask_041hkj1\" targetRef=\"ServiceTask_148dikw\"/\u003e\u003cendEvent id=\"EndEvent_075up1a\"\u003e\u003cincoming\u003eSequenceFlow_1da9ly4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_04da6ac\" name=\"Convert json to rich text\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f7276ff0-1770-4058-9e89-40ee79c6e41b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0k8hn5l\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1da9ly4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0k8hn5l\" sourceRef=\"ServiceTask_148dikw\" targetRef=\"ScriptTask_04da6ac\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1da9ly4\" sourceRef=\"ScriptTask_04da6ac\" targetRef=\"EndEvent_075up1a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_148dikw\" id=\"ServiceTask_148dikw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"476\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_041hkj1\" id=\"ServiceTask_041hkj1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vdjzb6\" id=\"SequenceFlow_0vdjzb6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"237.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19zuy4w\" id=\"SequenceFlow_19zuy4w_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"476\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"426.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_075up1a\" id=\"EndEvent_075up1a_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"913\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"931\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_04da6ac\" id=\"ScriptTask_04da6ac_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"687\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0k8hn5l\" id=\"SequenceFlow_0k8hn5l_di\"\u003e\u003comgdi:waypoint x=\"576\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"687\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"631.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1da9ly4\" id=\"SequenceFlow_1da9ly4_di\"\u003e\u003comgdi:waypoint x=\"787\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"913\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"850\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Updates alert fields based on input provided in the popup module when the rule is triggered.\n\nFields that can be updated:\nassignedTo\nclosedDateTime\ncomments\nfeedback\nstatus\ntags",
      "export_key": "example_microsoft_security_graph_update_alert",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649337147751,
      "name": "Example: Microsoft Security Graph Update Alert",
      "object_type": "incident",
      "programmatic_name": "example_microsoft_security_graph_update_alert",
      "tags": [],
      "uuid": "b15041be-349c-4b96-bf69-9a30db2ce323",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_microsoft_security_graph_alert_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_microsoft_security_graph_alert_search\" isExecutable=\"true\" name=\"Example: Microsoft Security Graph Alert Search\"\u003e\u003cdocumentation\u003eSearches the Microsoft Security Graph alerts for alerts that fit the search/filter criteria.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1eedcvz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19u37rs\" name=\"Microsoft Security Graph Alert Se...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c966466f-bc96-484a-b38b-f68e5f480327\"\u003e{\"inputs\":{},\"post_processing_script\":\"alerts = results.content.value\\nnote = \\\"Microsoft Security Graph Alert Search\u0026lt;br\u0026gt;There are \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt; alerts based on the artifact of value \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;.\\\".format(str(len(alerts)), artifact.value)\\n\\nif len(alerts):\\n  note = note + \\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Alert ids:\u0026lt;/b\u0026gt;\\\"\\n  for alert in alerts:\\n    note = note + \\\"\u0026lt;br\u0026gt;- {}\\\".format(alert.id)\\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\nsearch = \\\"filter=\\\"\\nconjunction = False\\n\\nif rule.properties.microsoft_security_graph_query_start_datetime:\\n  start = Date(rule.properties.microsoft_security_graph_query_start_datetime)\\n  start_ts = str(start.toInstant())\\n  start_filter = \\\"createdDateTime%20ge%20{}\\\".format(start_ts)\\n  search = search + start_filter\\n  conjunction = True\\n\\nif rule.properties.microsoft_security_graph_query_end_datetime:\\n  end = Date(rule.properties.microsoft_security_graph_query_end_datetime)\\n  end_ts = str(end.toInstant())\\n  end_filter = \\\"createdDateTime%20le%20{}\\\".format(end_ts)\\n  if conjunction: search = search + \\\"%20and%20\\\"\\n  search = search + end_filter\\n  conjunction = True\\n\\nif artifact.type == \\\"User Account\\\":\\n  artifact_filter = \\\"userStates/any(user:%20user/accountName%20eq%20\u0027{}\u0027)\\\".format(artifact.value)\\n  if conjunction: search = search + \\\"%20and%20\\\"\\n  search = search + artifact_filter\\n  conjunction = True\\n\\ninputs.microsoft_security_graph_alert_search_query = search\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1eedcvz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14nlt4s\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14nlt4s\" sourceRef=\"ServiceTask_19u37rs\" targetRef=\"EndEvent_0v9uizz\"/\u003e\u003cendEvent id=\"EndEvent_0v9uizz\"\u003e\u003cincoming\u003eSequenceFlow_14nlt4s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1eedcvz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19u37rs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19u37rs\" id=\"ServiceTask_19u37rs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14nlt4s\" id=\"SequenceFlow_14nlt4s_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"480\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"384\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0v9uizz\" id=\"EndEvent_0v9uizz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"480\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1eedcvz\" id=\"SequenceFlow_1eedcvz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "admin@example.com",
      "description": "Searches the Microsoft Security Graph alerts for alerts that fit the search/filter criteria.",
      "export_key": "example_microsoft_security_graph_alert_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649336808729,
      "name": "Example: Microsoft Security Graph Alert Search",
      "object_type": "artifact",
      "programmatic_name": "example_microsoft_security_graph_alert_search",
      "tags": [],
      "uuid": "b85e5e97-48bd-4ff0-94fb-3905aecf40f0",
      "workflow_id": 13
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_microsoft_security_graph_resolve_alert",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_microsoft_security_graph_resolve_alert\" isExecutable=\"true\" name=\"Example: Microsoft Security Graph Resolve Alert\"\u003e\u003cdocumentation\u003eSets the Microsoft Security Graph alert status to Resolved and sets the closedDateTime field to the current date time.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0qoo66r\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1p5nwtc\" name=\"Microsoft Security Graph Update A...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8e675085-820e-4e5a-983a-3943b558ba26\"\u003e{\"inputs\":{\"f25d5a0f-7f3a-4615-b7e3-41358e2989b4\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n        \\\"status\\\": \\\"resolved\\\",\\n        \\\"vendorInformation\\\": {\\n            \\\"provider\\\": \\\"String\\\",\\n            \\\"vendor\\\": \\\"String\\\"\\n        }\\n    }\"}}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the\\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\njson_note = {\\\"version\\\": \\\"1.0.\\\",\\n             \\\"header\\\": \\\"Microsoft Security Graph Resolve Alert\\\",\\n             \\\"json\\\": results.content}\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\nepoch_time = Date()\\nclosedDateTime = str(epoch_time.toInstant())\\n\\nprovider = workflow.properties.msg_alert_details.content.vendorInformation.provider\\nvendor = workflow.properties.msg_alert_details.content.vendorInformation.vendor\\n\\ndata = \u0027\u0027\u0027{{\\n        \\\"closedDateTime\\\": \\\"{0}\\\",\\n        \\\"status\\\": \\\"{1}\\\",\\n        \\\"vendorInformation\\\":\\n        {{\\n            \\\"provider\\\": \\\"{2}\\\",\\n            \\\"vendor\\\": \\\"{3}\\\"\\n        }}\\n    }}\u0027\u0027\u0027.format(closedDateTime, \\\"resolved\\\", provider, vendor)\\n\\ninputs.microsoft_security_graph_alert_data = data\\ninputs.microsoft_security_graph_alert_id = incident.properties.microsoft_security_graph_alert_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_19wyk70\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t3xnav\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_1sratfh\" name=\"Microsoft Security Graph Get Aler...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c0476b6d-9d57-4a98-b74a-a867bdb3f039\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.microsoft_security_graph_alert_id = incident.properties.microsoft_security_graph_alert_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"msg_alert_details\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qoo66r\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19wyk70\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qoo66r\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1sratfh\"/\u003e\u003csequenceFlow id=\"SequenceFlow_19wyk70\" sourceRef=\"ServiceTask_1sratfh\" targetRef=\"ServiceTask_1p5nwtc\"/\u003e\u003cscriptTask id=\"ScriptTask_0s51q52\" name=\"Convert json to rich text\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f7276ff0-1770-4058-9e89-40ee79c6e41b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0t3xnav\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1b6bsw8\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndEvent_04qz6tc\"\u003e\u003cincoming\u003eSequenceFlow_1b6bsw8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1b6bsw8\" sourceRef=\"ScriptTask_0s51q52\" targetRef=\"EndEvent_04qz6tc\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0t3xnav\" sourceRef=\"ServiceTask_1p5nwtc\" targetRef=\"ScriptTask_0s51q52\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1p5nwtc\" id=\"ServiceTask_1p5nwtc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"644\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sratfh\" id=\"ServiceTask_1sratfh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qoo66r\" id=\"SequenceFlow_0qoo66r_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"276.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19wyk70\" id=\"SequenceFlow_19wyk70_di\"\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"644\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"549.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0s51q52\" id=\"ScriptTask_0s51q52_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"881\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04qz6tc\" id=\"EndEvent_04qz6tc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1126\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1144\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1b6bsw8\" id=\"SequenceFlow_1b6bsw8_di\"\u003e\u003comgdi:waypoint x=\"981\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1126\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1053.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t3xnav\" id=\"SequenceFlow_0t3xnav_di\"\u003e\u003comgdi:waypoint x=\"744\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"881\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"812.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "admin@example.com",
      "description": "Sets the Microsoft Security Graph alert status to Resolved and sets the closedDateTime field to the current date time.",
      "export_key": "example_microsoft_security_graph_resolve_alert",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649336979090,
      "name": "Example: Microsoft Security Graph Resolve Alert",
      "object_type": "incident",
      "programmatic_name": "example_microsoft_security_graph_resolve_alert",
      "tags": [],
      "uuid": "4198a59f-8d2d-49f5-be94-a91afed26d2e",
      "workflow_id": 11
    }
  ],
  "workspaces": []
}
