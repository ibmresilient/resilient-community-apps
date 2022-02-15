{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Send SOAR Note to DLP",
      "id": 50,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Send SOAR Note to DLP",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "963231e7-9e0c-4dc1-aa7c-37283df7f178",
      "view_items": [],
      "workflows": [
        "sdlp_send_soar_note_to_dlp"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Update DLP Incident Status",
      "id": 51,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Update DLP Incident Status",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "68fee783-e2fd-4b54-8fdd-ac2092c6967f",
      "view_items": [
        {
          "content": "710445d8-3fcd-4650-8428-3b18cc62b216",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "sdlp_update_incident_status"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
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
      "enabled": false,
      "export_key": "Symantec DLP: Upload Binaries",
      "id": 48,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Upload Binaries",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "c05524c1-9356-4c3c-b6d0-cbb9cfd53fc9",
      "view_items": [],
      "workflows": [
        "sdlp_upload_binaries"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Upload Binaries as Artifact",
      "id": 49,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Upload Binaries as Artifact",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8af2230a-901a-4d07-99a3-4d0f7965e6ad",
      "view_items": [],
      "workflows": [
        "sdlp_upload_binaries"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Write DLP Incident Details to Note",
      "id": 47,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Write DLP Incident Details to Note",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1cdb703e-4dc7-46e9-aad7-d384b74c2204",
      "view_items": [],
      "workflows": [
        "sdlp_write_incident_details_to_note"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1644951553396,
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
      "export_key": "__function/sdlp_update_payload",
      "hide_notification": false,
      "id": 297,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_update_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_update_payload",
      "tooltip": "A JSON-like object which contains values to be updated on a given Symantec DLP Incident",
      "type_id": 11,
      "uuid": "b15871eb-b436-4266-b1bb-8368b743972b",
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
      "id": 269,
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
          "tag_handle": "fn_exchange_online",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "the id of the incident",
      "type_id": 11,
      "uuid": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "export_key": "__function/sdlp_incident_id",
      "hide_notification": false,
      "id": 355,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "eddd5084-0033-49af-8431-f8775bc98d6a",
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
      "export_key": "__function/sdlp_note_text",
      "hide_notification": false,
      "id": 356,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_note_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_note_text",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f2881c23-5b6e-4947-bf2c-79fb43a789ad",
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
      "export_key": "__function/sdlp_incident_status",
      "hide_notification": false,
      "id": 359,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_incident_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "79413c7b-ad2f-4149-a97b-dd6a70e72afe",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "incident.status.New",
          "properties": null,
          "uuid": "dd70d539-26fb-40fb-8b8c-92afba3cb3f8",
          "value": 158
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "a3434db8-d0d7-4a4f-9b24-c603a26203e5",
          "value": 159
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "47e781b2-212f-4f6f-97f8-0b32723b2472",
          "value": 160
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "7a8cbfd9-c81c-4a38-952f-f86d3f7b3024",
          "value": 161
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "fd4ed4d0-35ef-417e-a944-3e2859ba069f",
          "value": 162
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
      "export_key": "actioninvocation/sdlp_incident_status",
      "hide_notification": false,
      "id": 358,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident Status",
      "tooltip": "",
      "type_id": 6,
      "uuid": "710445d8-3fcd-4650-8428-3b18cc62b216",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "incident.status.New",
          "properties": null,
          "uuid": "a8ce6cd4-26d7-4218-bf83-884cf42be204",
          "value": 153
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "45cf43bd-df22-47ac-ad9e-1f7f77761391",
          "value": 154
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "ecd10a36-d09a-43c6-b212-ef84e8c19e77",
          "value": 155
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "f8cd108a-9ce4-4250-b120-02141ecc7e72",
          "value": 156
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "a50db2cb-9694-49df-a0f3-47073871959b",
          "value": 157
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
      "export_key": "incident/sdlp_incident_url",
      "hide_notification": false,
      "id": 295,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident URL ",
      "tooltip": "",
      "type_id": 0,
      "uuid": "49598693-2ac3-43af-a26b-011cdbe7bd4a",
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
      "export_key": "incident/sdlp_incident_id",
      "hide_notification": false,
      "id": 294,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident ID",
      "tooltip": "The ID of a Symantec DLP Incident",
      "type_id": 0,
      "uuid": "55f35e22-1610-42b0-accc-f65974e86e4e",
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
      "export_key": "incident/sdlp_incident_status",
      "hide_notification": false,
      "id": 357,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7cd1095b-07e3-49bd-bf8c-58ea2776e983",
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
      "created_date": 1643732716400,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function which is used to update the details of a Symantec DLP Incident. Takes 1 input which is a dictionary of things to be changed. To enable to updating of multiple custom attributes, provide a list or dictionary of all the attributes to be changed in the format: \u003cattribute_name\u003e: \u003cnew_value\u003e",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Update Incident",
      "export_key": "fn_symantec_dlp_update_incident",
      "id": 17,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1643734109733,
      "name": "fn_symantec_dlp_update_incident",
      "tags": [],
      "uuid": "8962f715-6114-4e8f-a247-29c40623b98c",
      "version": 2,
      "view_items": [
        {
          "content": "b15871eb-b436-4266-b1bb-8368b743972b",
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
          "name": "Example: Symantec DLP - Send Note to Incident",
          "object_type": "incident",
          "programmatic_name": "sdlp_send_note_to_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 22
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Symantec DLP - Set Incident Status to Closed",
          "object_type": "incident",
          "programmatic_name": "sdlp_set_incident_status",
          "tags": [],
          "uuid": null,
          "workflow_id": 21
        }
      ]
    },
    {
      "created_date": 1644346548311,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get the information on the Symantec DLP incident by calling the DLP REST API incident endpoints and return the information in JSON format.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Get Incident Details",
      "export_key": "symantec_dlp_get_incident_details",
      "id": 27,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1644346548346,
      "name": "symantec_dlp_get_incident_details",
      "tags": [],
      "uuid": "7e128530-9e09-405b-8f04-d7e23f5fb359",
      "version": 1,
      "view_items": [
        {
          "content": "eddd5084-0033-49af-8431-f8775bc98d6a",
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
          "name": "Symantec DLP: Write Incident Details to Note",
          "object_type": "incident",
          "programmatic_name": "sdlp_write_incident_details_to_note",
          "tags": [],
          "uuid": null,
          "workflow_id": 40
        }
      ]
    },
    {
      "created_date": 1644529875193,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Send a note from SOAR to the corresponding Symantec DLP incident.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Send Note to DLP Incident",
      "export_key": "symantec_dlp_send_note_to_dlp_incident",
      "id": 29,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1644529875222,
      "name": "symantec_dlp_send_note_to_dlp_incident",
      "tags": [],
      "uuid": "1b03031b-cbfc-4ccb-8a01-ab7e109f1a33",
      "version": 1,
      "view_items": [
        {
          "content": "eddd5084-0033-49af-8431-f8775bc98d6a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f2881c23-5b6e-4947-bf2c-79fb43a789ad",
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
          "name": "Symantec DLP: Send SOAR Note to DLP",
          "object_type": "note",
          "programmatic_name": "sdlp_send_soar_note_to_dlp",
          "tags": [],
          "uuid": null,
          "workflow_id": 38
        }
      ]
    },
    {
      "created_date": 1644855344845,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update the incident status of the Symantec DLP incident in DLP.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Update Incident Status in DLP",
      "export_key": "symantec_dlp_update_incident_status",
      "id": 30,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1644943184279,
      "name": "symantec_dlp_update_incident_status",
      "tags": [],
      "uuid": "4258886f-e439-41f2-9679-864a3d291add",
      "version": 6,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "79413c7b-ad2f-4149-a97b-dd6a70e72afe",
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
          "name": "Symantec DLP: Update Incident Status in DLP",
          "object_type": "incident",
          "programmatic_name": "sdlp_update_incident_status",
          "tags": [],
          "uuid": null,
          "workflow_id": 41
        }
      ]
    },
    {
      "created_date": 1644520759910,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Upload the Symantec DLP Component binary files and add as artifact files.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Upload Binaries",
      "export_key": "symantec_dlp_upload_binaries",
      "id": 28,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1644527590377,
      "name": "symantec_dlp_upload_binaries",
      "tags": [],
      "uuid": "64c9eafd-e365-4b8b-ba61-33aa6010c601",
      "version": 2,
      "view_items": [
        {
          "content": "eddd5084-0033-49af-8431-f8775bc98d6a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
          "name": "Symantec DLP: Upload Binaries",
          "object_type": "incident",
          "programmatic_name": "sdlp_upload_binaries",
          "tags": [],
          "uuid": null,
          "workflow_id": 39
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 247,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1644951551030,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1644951551030,
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
      "export_key": "fn_symantec_dlp",
      "name": "Symantec DLP Message Destination",
      "programmatic_name": "fn_symantec_dlp",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "d75c8560-64d2-44ca-87ce-4db510a3c5d1"
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
      "created_date": 1636050132380,
      "creator_id": "admin@example.com",
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\n\nTypically, a function will create the workflow property \u0027convert_json_to_rich_text\u0027, and this script will run after that function to perform the conversion.\n\nFeatures:\n* Display the hierarchical nature of json, presenting the json keys (sorted if specified) as bold labels\n* Provide links to found URLs\n* Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.1",
      "id": 2,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1636050132402,
      "name": "Convert JSON to rich text v1.1",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text_v11",
      "script_text": "# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.\nVERSION = 1.1\n\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to define the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, {\n    \"version\": 1.1,\n    \"header\": \"Artifact scan results for: {}\".format(artifact.value),\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr /\u003e\",\n    \"sort\": True,\n    \"json\": results.content,\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.1, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr /\u003e\"|list such as [\u0027\u003cspan\u003e\u0027,\u0027\u003c/span\u003e\u0027], [html separator between json keys and lists or defaults to html break: \u0027\u003cbr /\u003e\u0027. \n                                                If a list, then the data is brackets by the pair specified]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\"\"\"\n\nimport re\n\n# needed for python 3\ntry:\n    unicode(\"abc\")\nexcept:\n    unicode = str\n\n\nrc = re.compile(r\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#\\?]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n    \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n\n    def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr /\u003e\", sort_keys=False):\n        self.omit_keys = omit_keys\n        self.padding = padding\n        self.separator = separator\n        self.sort_keys = sort_keys\n\n\n    def format_link(self, item):\n        \"\"\"[summary]\n          Find embedded urls (http(s)) and add html anchor tags to display as links\n          Args:\n              item ([string])\n\n          Returns:\n              [str]: None|original text if no links|text with html links\n        \"\"\"\n        formatted_item = item\n        if item and not isinstance(item, (int, bool, float)):\n            list = rc.findall(item)\n            if list:\n                for link in list:\n                    formatted_item = formatted_item.replace(link, u\"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n        return formatted_item\n\n    def expand_list(self, list_value, is_list=False):\n        \"\"\"[summary]\n          convert items to html, adding indents to nested dictionaries.\n          Args:\n              list_value ([dict|list]): json element\n\n          Returns:\n              [str]: html converted code\n        \"\"\"\n        if not isinstance(list_value, list):\n            return self.format_link(list_value)\n        elif not list_value:\n            return u\"None\u003cbr\u003e\"\n\n        try:\n            items_list = []  # this will ensure list starts on second line of key label\n            for item in list_value:\n                if isinstance(item, dict):\n                    result = self.convert_json_to_rich_text(item)\n                    if is_list:\n                        items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(result))\n                    else:\n                        items_list.append(result)\n                elif isinstance(item, list):\n                    items_list.append(self.expand_list(item, is_list=True))\n                elif is_list:\n                    items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(self.format_link(unicode(item))))\n                else:\n                    items_list.append(self.format_link(unicode(item)))\n\n            expand_list_result = self.add_separator(self.separator if not is_list else u\"\",\n                                                    items_list,\n                                                    is_list=is_list)\n\n            if is_list:\n                return u\"\u003cul\u003e{}\u003c/ul\u003e\".format(expand_list_result)\n            else:\n                return u\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(expand_list_result)\n        except Exception as err:\n            return str(err)\n\n    def convert_json_to_rich_text(self, sub_dict):\n        \"\"\"[summary]\n          Walk dictionary tree and convert to html for better display\n          Args:\n              sub_dict ([type]): [description]\n\n          Returns:\n              [type]: [description]\n        \"\"\"\n        notes = []\n        if sub_dict:\n            if isinstance(sub_dict, list):\n                expanded_list = self.expand_list(sub_dict, is_list=True)\n                notes.append(self.add_separator(self.separator, expanded_list))\n            else:\n                keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n                for key in keys:\n                    if key not in self.omit_keys:\n                        value = sub_dict[key]\n                        is_list = isinstance(value, list)\n                        item_list = [u\"\u003cstrong\u003e{0}\u003c/strong\u003e: \".format(key)]\n                        if isinstance(value, dict):\n                            convert_result = self.convert_json_to_rich_text(value)\n                            if convert_result:\n                                item_list.append(u\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, convert_result))\n                            else:\n                                item_list.append(u\"None\u003cbr\u003e\")\n                        else:\n                            item_list.append(self.expand_list(value, is_list=is_list))\n                        notes.append(self.add_separator(self.separator, u\"\".join(unicode(v) for v in item_list), is_list=is_list))\n\n        result_notes = u\"\".join(notes)\n        if isinstance(self.separator, list):\n            return result_notes\n        else:\n            return result_notes.replace(\n                u\"\u003c/div\u003e{0}\".format(self.separator), u\"\u003c/div\u003e\").replace(\n                u\"{0}\u003c/div\u003e\".format(self.separator), u\"\u003c/div\u003e\"\n            )  # tighten up result\n\n    def add_separator(self, separator, items, is_list=False):\n        \"\"\"\n        apply the separator to the data\n        :param separator: None, str or list such as [\u0027\u003cspan\u003e\u0027, \u0027\u003c/span\u003e\u0027]\n        :param items: str or list to add separator\n        :return: text with separator applied\n        \"\"\"\n        _items = items\n\n        if not _items:\n            return \"\u003cbr\u003e\"\n\n        if not isinstance(_items, list):\n            _items = [_items]\n\n        if isinstance(separator, list):\n            return u\"\".join([u\"{}{}{}\".format(separator[0], item, separator[1]) for item in _items])\n\n        return u\"{}{}\".format(separator.join(_items), separator if not is_list else u\"\")\n\ndef get_properties(property_name):\n    \"\"\"\n    Logic to collect the json and parameters from a workflow property.\n    Args:\n      property_name: workflow property to reference\n    Returns:\n      padding, separator, header, json_omit_list, incident_field, json, sort_keys\n    \"\"\"\n    if not workflow.properties.get(property_name):\n        helper.fail(\"workflow.properties.{} undefined\".format(property_name))\n\n    padding = int(workflow.properties[property_name].get(\"padding\", 10))\n    separator = workflow.properties[property_name].get(\"separator\", u\"\u003cbr /\u003e\")\n    if isinstance(separator, list) and len(separator) != 2:\n        helper.fail(\"list of separators should be specified as a pair such as [\u0027\u003cdiv\u003e\u0027, \u0027\u003c/div\u003e\u0027]: {}\".format(separator))\n\n    header = workflow.properties[property_name].get(\"header\")\n    json_omit_list = workflow.properties[property_name].get(\"json_omit_list\")\n    if not json_omit_list:\n        json_omit_list = []\n    incident_field = workflow.properties[property_name].get(\"incident_field\")\n    json = workflow.properties[property_name].get(\"json\", {})\n    if not isinstance(json, dict) and not isinstance(json, list):\n        helper.fail(\"json element is not formatted correctly: {}\".format(json))\n    sort_keys = bool(workflow.properties[property_name].get(\"sort\", False))\n\n    return padding, separator, header, json_omit_list, incident_field, json, sort_keys\n\n\n## S T A R T\nif \u0027workflow\u0027 in globals():\n    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\n\n    if header:\n        if isinstance(separator, list):\n            hdr = u\"{0}{1}{2}\".format(separator[0], header, separator[1])\n        else:\n            hdr = u\"{0}{1}\".format(header, separator)\n    else:\n        hdr = u\"\"\n\n    convert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\n    converted_json = convert.convert_json_to_rich_text(json)\n    result = u\"{}{}\".format(hdr, converted_json if converted_json else \"\\nNone\")\n\n    rich_text_note = helper.createRichText(result)\n    if incident_field:\n        incident[incident_field] = rich_text_note\n    else:\n        incident.addNote(rich_text_note)\n",
      "tags": [],
      "uuid": "874d929b-7b4c-4f47-983a-58295c93d6bf"
    }
  ],
  "server_version": {
    "build_number": 81,
    "major": 40,
    "minor": 2,
    "version": "40.2.81"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_set_incident_status",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_set_incident_status\" isExecutable=\"true\" name=\"Example: Symantec DLP - Set Incident Status to Closed\"\u003e\u003cdocumentation\u003eAn example workflow which is used to update a DLP Incidents Status to Closed.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dzyxvb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1fby33m\" name=\"Symantec DLP: Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8962f715-6114-4e8f-a247-29c40623b98c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON stringself.\\n     Supports basestring, bool and int.\\n     If the value is None, it sets it to False\\\"\\\"\\\"\\n\\n  json_str = \u0027\\\"{ {0} }\\\"\u0027\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  json_entry_unicode = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n  \\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n    \\n      \\n    if value is None:\\n      value = False\\n      \\n    if isinstance(value, unicode):\\n      entries.append(json_entry_unicode.format(key, value))\\n    elif isinstance(value, basestring):\\n      entries.append(json_entry_str.format(key, value))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n    \\n    else:\\n      entries.append(json_entry.format(key, value))\\n  \\n  return \u0027{\u0027 + \u0027,\u0027.join(entries) + \u0027}\u0027\\n\\nfrom java.util import Date\\n\\n\\npayload = {\\n\\\"status\\\": \\\"Closed\\\",\\n\\\"incident_id\\\": incident.properties.sdlp_incident_id\\n}\\n\\npayload[\u0027note\u0027] = u\\\"[{}] Resilient sent an Update Request to this Incident. Status was changed to {}\\\".format(Date(), payload[\\\"status\\\"])\\n\\n\\ninputs.sdlp_update_payload = dict_to_json_str(payload)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dzyxvb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vrfby7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dzyxvb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1fby33m\"/\u003e\u003cendEvent id=\"EndEvent_1c2r23k\"\u003e\u003cincoming\u003eSequenceFlow_0vrfby7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vrfby7\" sourceRef=\"ServiceTask_1fby33m\" targetRef=\"EndEvent_1c2r23k\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1fby33m\" id=\"ServiceTask_1fby33m_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"376\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dzyxvb\" id=\"SequenceFlow_0dzyxvb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"287\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1c2r23k\" id=\"EndEvent_1c2r23k_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"659\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"677\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vrfby7\" id=\"SequenceFlow_0vrfby7_di\"\u003e\u003comgdi:waypoint x=\"476\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"567.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "An example workflow which is used to update a DLP Incidents Status to Closed.",
      "export_key": "sdlp_set_incident_status",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1643734110283,
      "name": "Example: Symantec DLP - Set Incident Status to Closed",
      "object_type": "incident",
      "programmatic_name": "sdlp_set_incident_status",
      "tags": [],
      "uuid": "68af500f-fb0a-490a-b438-5f90024dfe1e",
      "workflow_id": 21
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "sdlp_upload_binaries",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_upload_binaries\" isExecutable=\"true\" name=\"Symantec DLP: Upload Binaries\"\u003e\u003cdocumentation\u003eCall the function to get the binary files associate with a DLP incident and upload to the corresponding IBM SOAR case.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0u9x6bq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0y2wmdt\"\u003e\u003cincoming\u003eSequenceFlow_1e1upjv\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0r6tnd5\" name=\"Symantec DLP: Upload Binaries\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64c9eafd-e365-4b8b-ba61-33aa6010c601\"\u003e{\"inputs\":{},\"post_processing_script\":\"sdlp_inputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = sdlp_inputs.get(\\\"sdlp_incident_id\\\")\\n\\nnote = u\\\"\u0026lt;b\u0026gt;Symantec DLP: Upload Binaries for incident Id {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\".format(sdlp_incident_id)\\nsuccess = results.get(\\\"success\\\")\\nif success:\\n  content = results.get(\u0027artifact_name_list\u0027)\\n  num_artifacts = len(content)\\n  note = u\\\"{0} {1} artifact files added\\\".format(note, num_artifacts)\\nelse\\n  note = u\\\"{0}artifact NOT added\\\".format(note)\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0u9x6bq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e1upjv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0u9x6bq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0r6tnd5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1e1upjv\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"EndEvent_0y2wmdt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y2wmdt\" id=\"EndEvent_0y2wmdt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"811\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"829\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0r6tnd5\" id=\"ServiceTask_0r6tnd5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"447\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u9x6bq\" id=\"SequenceFlow_0u9x6bq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"322.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e1upjv\" id=\"SequenceFlow_1e1upjv_di\"\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"811\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"679\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "admin@example.com",
      "description": "Call the function to get the binary files associate with a DLP incident and upload to the corresponding IBM SOAR case.",
      "export_key": "sdlp_upload_binaries",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1644951478119,
      "name": "Symantec DLP: Upload Binaries",
      "object_type": "incident",
      "programmatic_name": "sdlp_upload_binaries",
      "tags": [],
      "uuid": "18314a54-a9c0-49f7-b1f9-98af37c7ec7d",
      "workflow_id": 39
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "sdlp_update_incident_status",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_update_incident_status\" isExecutable=\"true\" name=\"Symantec DLP: Update Incident Status in DLP\"\u003e\u003cdocumentation\u003eUpdate the DLP incident status in DLP.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1hgy1g1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hgy1g1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_085sbtd\"/\u003e\u003cendEvent id=\"EndEvent_0gmht6l\"\u003e\u003cincoming\u003eSequenceFlow_062edc4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_085sbtd\" name=\"Symantec DLP: Update Incident Sta...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"dd70d539-26fb-40fb-8b8c-92afba3cb3f8\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nsdlp_incident_id = content.get(\\\"sdlp_incident_id\\\", None)\\nsdlp_incident_status = content.get(\\\"sdlp_incident_status\\\", None)\\nif success:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident Status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; DLP incident {0} status set to: {1}.\u0027.format(sdlp_incident_id, sdlp_incident_status)\\nelse:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident Status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;Error: Check DLP incidentId {0} status in Symantec DLP.\u0027.format(sdlp_incident_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_status = rule.properties.sdlp_incident_status\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1hgy1g1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_062edc4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_062edc4\" sourceRef=\"ServiceTask_085sbtd\" targetRef=\"EndEvent_0gmht6l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hgy1g1\" id=\"SequenceFlow_1hgy1g1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"278\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gmht6l\" id=\"EndEvent_0gmht6l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"784\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"802\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_085sbtd\" id=\"ServiceTask_085sbtd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"448\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_062edc4\" id=\"SequenceFlow_062edc4_di\"\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"784\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"666\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "admin@example.com",
      "description": "Update the DLP incident status in DLP.",
      "export_key": "sdlp_update_incident_status",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1644942515246,
      "name": "Symantec DLP: Update Incident Status in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_update_incident_status",
      "tags": [],
      "uuid": "6347ccec-1997-4af5-a798-702609486951",
      "workflow_id": 41
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_send_soar_note_to_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_send_soar_note_to_dlp\" isExecutable=\"true\" name=\"Symantec DLP: Send SOAR Note to DLP\"\u003e\u003cdocumentation\u003eSend a SOAR note to the corresponding DLP incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0w8abzz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19r4cvd\" name=\"Symantec DLP: Send Note to DLP In...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1b03031b-cbfc-4ccb-8a01-ab7e109f1a33\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Import Date\\nfrom java.util import Date\\n\\n# Edit note in SOAR to indicate it was sent to SentinelOne\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to Symantec DLP at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.sdlp_note_text = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0w8abzz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mfe8fq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0w8abzz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19r4cvd\"/\u003e\u003cendEvent id=\"EndEvent_1obxbt6\"\u003e\u003cincoming\u003eSequenceFlow_0mfe8fq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0mfe8fq\" sourceRef=\"ServiceTask_19r4cvd\" targetRef=\"EndEvent_1obxbt6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19r4cvd\" id=\"ServiceTask_19r4cvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"485\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w8abzz\" id=\"SequenceFlow_0w8abzz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"341.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1obxbt6\" id=\"EndEvent_1obxbt6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"756\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"774\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mfe8fq\" id=\"SequenceFlow_0mfe8fq_di\"\u003e\u003comgdi:waypoint x=\"585\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"756\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"670.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "Send a SOAR note to the corresponding DLP incident.",
      "export_key": "sdlp_send_soar_note_to_dlp",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1644863094679,
      "name": "Symantec DLP: Send SOAR Note to DLP",
      "object_type": "note",
      "programmatic_name": "sdlp_send_soar_note_to_dlp",
      "tags": [],
      "uuid": "6e3f7a89-e689-448d-ad08-ed3c8f1988fc",
      "workflow_id": 38
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_write_incident_details_to_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_write_incident_details_to_note\" isExecutable=\"true\" name=\"Symantec DLP: Write Incident Details to Note\"\u003e\u003cdocumentation\u003eCall the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15u7h7q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13cc5dk\" name=\"Symantec DLP: Get Incident Detail...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e128530-9e09-405b-8f04-d7e23f5fb359\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = inputs.get(\\\"sdlp_incident_id\\\")\\ncontent = results.get(\\\"content\\\")\\n\\nheader = u\\\"Symantec DLP Incident Id: {0} Details:\\\".format(sdlp_incident_id)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15u7h7q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f1dod6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15u7h7q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13cc5dk\"/\u003e\u003cscriptTask id=\"ScriptTask_038nkue\" name=\"Convert JSON to rich text v1.1\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v11\" uuid=\"874d929b-7b4c-4f47-983a-58295c93d6bf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f1dod6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16xnfca\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f1dod6\" sourceRef=\"ServiceTask_13cc5dk\" targetRef=\"ScriptTask_038nkue\"/\u003e\u003cendEvent id=\"EndEvent_1a5c3zv\"\u003e\u003cincoming\u003eSequenceFlow_16xnfca\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16xnfca\" sourceRef=\"ScriptTask_038nkue\" targetRef=\"EndEvent_1a5c3zv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13cc5dk\" id=\"ServiceTask_13cc5dk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"385\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15u7h7q\" id=\"SequenceFlow_15u7h7q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"291.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_038nkue\" id=\"ScriptTask_038nkue_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"703.936\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f1dod6\" id=\"SequenceFlow_0f1dod6_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"704\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"594.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1a5c3zv\" id=\"EndEvent_1a5c3zv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"963.936\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"981.936\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16xnfca\" id=\"SequenceFlow_16xnfca_di\"\u003e\u003comgdi:waypoint x=\"804\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"964\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"884\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "Call the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.",
      "export_key": "sdlp_write_incident_details_to_note",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1644863676057,
      "name": "Symantec DLP: Write Incident Details to Note",
      "object_type": "incident",
      "programmatic_name": "sdlp_write_incident_details_to_note",
      "tags": [],
      "uuid": "7887e541-1511-4432-9890-ebeebbc2873c",
      "workflow_id": 40
    }
  ],
  "workspaces": []
}
