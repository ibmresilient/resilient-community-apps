{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1614292401838,
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
      "export_key": "__function/ciscso_asa_network_object_group",
      "hide_notification": false,
      "id": 193,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ciscso_asa_network_object_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ciscso_asa_network_object_group",
      "tooltip": "",
      "type_id": 11,
      "uuid": "737cf112-4adc-4e54-b7a1-a5d696340dcc",
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
      "last_modified_time": 1614284132216,
      "name": "cisco_asa_get_network_objects",
      "tags": [],
      "uuid": "af7d53df-369d-4e78-b33b-865d5a85895a",
      "version": 1,
      "view_items": [
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
          "name": "Example: Cisco ASA Get Blacklist Inbound",
          "object_type": "incident",
          "programmatic_name": "example_cisco_asa_get_blacklist_inbound",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
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
      "create_date": 1614292399720,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1614292399720,
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
  "types": [],
  "workflows": [],
  "workspaces": []
}
