{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "equals",
          "type": null,
          "value": "Active"
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_status",
          "method": "changed_to",
          "type": null,
          "value": "Resolved"
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Close DLP Case",
      "id": 277,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Close DLP Case",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "9ea5f7ac-36d2-499b-8845-dcb6a29c226a",
      "view_items": [],
      "workflows": [
        "sdlp_close_dlp_case"
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
      "export_key": "Symantec DLP: Get DLP Notes",
      "id": 278,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Get DLP Notes",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1932d664-77d8-4941-b664-2373cad189ed",
      "view_items": [],
      "workflows": [
        "sdlp_get_notes"
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
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Resolve Incident in DLP",
      "id": 279,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Resolve Incident in DLP",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "1ba80be8-5865-48d1-b57b-15af316a9830",
      "view_items": [],
      "workflows": [
        "sdlp_resolve_incident_in_dlp"
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
      "export_key": "Symantec DLP: Send SOAR Note to DLP",
      "id": 280,
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
      "export_key": "Symantec DLP: Update DLP Incident",
      "id": 281,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Update DLP Incident",
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
        },
        {
          "content": "bbe52d00-1cc0-40da-9054-6f681375fd1a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "sdlp_update_incident"
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
          "field_name": "incident.severity_code",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Update Severity in DLP",
      "id": 282,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Update Severity in DLP",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "726658e8-8b16-4056-b229-7a393b4fe6d8",
      "view_items": [],
      "workflows": [
        "sdlp_update_severity_in_dlp"
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
      "id": 283,
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
      "id": 284,
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
      "id": 285,
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
  "case_matching_profiles": [],
  "export_date": 1718717932937,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 5362,
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
      "tags": [],
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
      "export_key": "__function/sdlp_attachment_upload_type",
      "hide_notification": false,
      "id": 5657,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_attachment_upload_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_attachment_upload_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9e168b4e-0e5a-4d2c-93f8-8e45865d2e4e",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "artifact",
          "properties": null,
          "uuid": "5a7c5a8e-3acc-495f-a27f-a72f73ed4f42",
          "value": 1941
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "attachment",
          "properties": null,
          "uuid": "889a47bb-ba84-447f-b1d8-0c8d077bcad3",
          "value": 1942
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
      "export_key": "__function/sdlp_incident_id",
      "hide_notification": false,
      "id": 5363,
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
      "id": 5364,
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
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/sdlp_incident_severity_id",
      "hide_notification": false,
      "id": 5365,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_severity_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_incident_severity_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "439264c3-b4d7-493b-8358-89a310ab0d8e",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "dd83848b-eeda-4e14-bf40-a67f6df33594",
          "value": 1704
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "e1f2f082-7b94-42e3-a9e9-cad5c52f3d84",
          "value": 1705
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "a673371b-a4a2-49fe-a51a-8744428e9a2f",
          "value": 1706
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Info",
          "properties": null,
          "uuid": "82ca0d66-6f50-4956-83d5-69a5c13263d9",
          "value": 1707
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
      "export_key": "__function/sdlp_incident_status",
      "hide_notification": false,
      "id": 5366,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_incident_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "79413c7b-ad2f-4149-a97b-dd6a70e72afe",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "d4f4001e-291a-4fca-a2c0-fb900b1197cc",
          "value": 1708
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "a3434db8-d0d7-4a4f-9b24-c603a26203e5",
          "value": 1709
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "47e781b2-212f-4f6f-97f8-0b32723b2472",
          "value": 1710
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "7a8cbfd9-c81c-4a38-952f-f86d3f7b3024",
          "value": 1711
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "fd4ed4d0-35ef-417e-a944-3e2859ba069f",
          "value": 1712
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/sdlp_incident_severity_id",
      "hide_notification": false,
      "id": 5360,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_severity_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident Severity",
      "tooltip": "",
      "type_id": 6,
      "uuid": "bbe52d00-1cc0-40da-9054-6f681375fd1a",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "2e9923bf-a135-4d58-856c-939e4cbed05f",
          "value": 1695
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "fe8f684a-404a-454d-b7ae-c98b2ebfbaa4",
          "value": 1696
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "124df61c-69f2-4ade-ad89-86542206e4ff",
          "value": 1697
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Info",
          "properties": null,
          "uuid": "4e63d89c-de9d-46aa-a44d-dbe9f1d29600",
          "value": 1698
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/sdlp_incident_status",
      "hide_notification": false,
      "id": 5361,
      "input_type": "select",
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
      "type_id": 6,
      "uuid": "710445d8-3fcd-4650-8428-3b18cc62b216",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "d69dddc0-dbf7-4ed2-bbe5-aae97d6412c4",
          "value": 1699
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "45cf43bd-df22-47ac-ad9e-1f7f77761391",
          "value": 1700
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "ecd10a36-d09a-43c6-b212-ef84e8c19e77",
          "value": 1701
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "f8cd108a-9ce4-4250-b120-02141ecc7e72",
          "value": 1702
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "a50db2cb-9694-49df-a0f3-47073871959b",
          "value": 1703
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
      "export_key": "incident/sdlp_policy_group_id",
      "hide_notification": false,
      "id": 5352,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_policy_group_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Policy Group ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "9553c75e-2d56-43f8-ab95-a50630cc52d5",
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
      "export_key": "incident/sdlp_policy_group_name",
      "hide_notification": false,
      "id": 5353,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_policy_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Policy Group Name",
      "tooltip": "",
      "type_id": 0,
      "uuid": "df63232a-3eb7-4b12-beb1-20b5bb1a0f90",
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
      "export_key": "incident/sdlp_policy_name",
      "hide_notification": false,
      "id": 5354,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_policy_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Policy Name",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e96a002c-d610-479a-bd5f-6cf9d515d02b",
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
      "export_key": "incident/sdlp_policy_id",
      "hide_notification": false,
      "id": 5355,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_policy_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Policy ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "190c4f61-f417-4b9d-9011-9ca3316edd05",
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
      "export_key": "incident/sdlp_incident_url",
      "hide_notification": false,
      "id": 5356,
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
      "id": 5357,
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
      "tooltip": "",
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
      "id": 5358,
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
      "created_date": 1716556157136,
      "description": {
        "content": "Close SOAR case when the DLP incident status is set to Resolve.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Close DLP Case",
      "export_key": "symantec_dlp_close_dlp_case",
      "id": 69,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1716556157136,
      "name": "symantec_dlp_close_dlp_case",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "581c6770-d1c8-4caf-ab39-cd155fa53a09",
      "version": 0,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "name": "Symantec DLP: Close DLP Case",
          "object_type": "incident",
          "programmatic_name": "sdlp_close_dlp_case",
          "tags": [],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "created_date": 1716556157246,
      "description": {
        "content": "Get the information on the Symantec DLP incident by calling the DLP REST API incident endpoints and return the information in JSON format.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Get Incident Details",
      "export_key": "symantec_dlp_get_incident_details",
      "id": 70,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1716556157246,
      "name": "symantec_dlp_get_incident_details",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"notes\": [\"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-07T16:23:50.32\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded a note 2/7/2022 4:23pm\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-08T08:31:12.158\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded a second note 2/7/2022\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-10T20:49:58.47\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded note to SOAR and will send it to DLP\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-10T20:49:58.47\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded note to SOAR and will send it to DLP\u003c/p\u003e\\n                        \"], \"editableIncidentDetails\": {\"incidentId\": 468, \"infoMap\": {\"detectedRemediationStatus\": 0, \"preventOrProtectStatusId\": 0, \"incidentStatusName\": \"Resolved\", \"isHidingNotAllowed\": false, \"severityId\": 1, \"incidentStatusId\": 3, \"isHidden\": false}, \"customAttributeGroups\": [{\"name\": \"custom_attribute_group.default\", \"nameInternationalized\": true, \"customAttributes\": [{\"name\": \"ibm_soar_case_url\", \"index\": 17, \"displayOrder\": 1, \"value\": \"https://mysoar.com:443/#incidents/3449\", \"email\": false}, {\"name\": \"ibm_soar_case_id\", \"index\": 18, \"displayOrder\": 2, \"value\": \"3449\", \"email\": false}]}, {\"name\": \"Predefined\", \"nameInternationalized\": false, \"customAttributes\": [{\"name\": \"Resolution\", \"index\": 1, \"displayOrder\": 1, \"value\": \"Business Issue\", \"email\": false}, {\"name\": \"Dismissal Reason\", \"index\": 2, \"displayOrder\": 2, \"value\": \"Bus. Process Issue\", \"email\": false}, {\"name\": \"Assigned To\", \"index\": 3, \"displayOrder\": 3, \"email\": false}, {\"name\": \"Business Unit\", \"index\": 4, \"displayOrder\": 4, \"email\": false}, {\"name\": \"Employee Code\", \"index\": 5, \"displayOrder\": 5, \"email\": false}, {\"name\": \"First Name\", \"index\": 6, \"displayOrder\": 6, \"email\": false}, {\"name\": \"Last Name\", \"index\": 7, \"displayOrder\": 7, \"email\": false}, {\"name\": \"Phone\", \"index\": 8, \"displayOrder\": 8, \"email\": false}, {\"name\": \"Sender Email\", \"index\": 9, \"displayOrder\": 9, \"email\": true}, {\"name\": \"Manager First Name\", \"index\": 11, \"displayOrder\": 10, \"email\": false}, {\"name\": \"Manager Last Name\", \"index\": 10, \"displayOrder\": 11, \"email\": false}, {\"name\": \"Manager Phone\", \"index\": 12, \"displayOrder\": 12, \"email\": false}, {\"name\": \"Manager Email\", \"index\": 13, \"displayOrder\": 13, \"email\": true}, {\"name\": \"Region\", \"index\": 14, \"displayOrder\": 14, \"email\": false}, {\"name\": \"Country\", \"index\": 15, \"displayOrder\": 15, \"email\": false}, {\"name\": \"Postal Code\", \"index\": 16, \"displayOrder\": 16, \"email\": false}]}]}, \"staticIncidentDetails\": {\"incidentId\": 468, \"infoMap\": {\"messageType\": \"EDAR\", \"discoverContentRootPath\": \"DLP-WINDOWS10-8\", \"policyName\": \"Customer Data Protection\", \"discoverMillisSinceFirstSeen\": 165799618, \"detectionServerName\": \"Single-tier Detection Server\", \"discoverTargetId\": 21, \"discoverName\": \"passwordpolicy.ini\", \"fileOwner\": \"BUILTIN\\\\administrators\", \"policyVersion\": 2, \"discoverServer\": \"DLP-WINDOWS10-8\", \"discoverRepositoryLocation\": \"DLP-WINDOWS10-8 - c:\\\\passwordpolicy.ini\", \"discoverScanId\": 41, \"endpointConnectionStatus\": \"CONNECTED\", \"policyId\": 16, \"detectionServerId\": 1, \"messageId\": 468, \"creationDate\": \"2022-02-04T16:08:48.678\", \"isBlockedStatusSuperseded\": false, \"detectionDate\": \"2022-02-04T16:08:43.08\", \"messageDate\": \"2022-02-03T22:40:43\", \"attachmentInfo\": [{\"messageComponentName\": \"c:\\\\passwordpolicy.ini\", \"messageComponentId\": 981, \"wasCracked\": false, \"documentFormat\": \"unicode\", \"messageComponentType\": 3, \"originalSize\": 16482}], \"fileCreateDate\": \"2021-02-12T09:50:16.39\", \"fileAccessDate\": \"2022-02-04T16:01:06.431\", \"discoverTargetName\": \"SS number on 9.30.94.38\", \"policyGroupName\": \"Customer Data Protection\", \"policyGroupId\": 5, \"messageSource\": \"DISCOVER\", \"matchCount\": 2, \"messageAclEntries\": [{\"cloudStorageCollaborator\": \"BUILTIN\\\\administrators\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\administrators\", \"readACLShare\": \"BUILTIN\\\\administrators\", \"readACLFile\": \"BUILTIN\\\\administrators\"}, {\"cloudStorageCollaborator\": \"BUILTIN\\\\administrators\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\administrators\", \"readACLShare\": \"BUILTIN\\\\administrators\", \"readACLFile\": \"BUILTIN\\\\administrators\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\system\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\system\", \"readACLShare\": \"NT AUTHORITY\\\\system\", \"readACLFile\": \"NT AUTHORITY\\\\system\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\system\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\system\", \"readACLShare\": \"NT AUTHORITY\\\\system\", \"readACLFile\": \"NT AUTHORITY\\\\system\"}, {\"cloudStorageCollaborator\": \"BUILTIN\\\\users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\users\", \"readACLShare\": \"BUILTIN\\\\users\", \"readACLFile\": \"BUILTIN\\\\users\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\authenticated users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\authenticated users\", \"readACLShare\": \"NT AUTHORITY\\\\authenticated users\", \"readACLFile\": \"NT AUTHORITY\\\\authenticated users\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\authenticated users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\authenticated users\", \"readACLShare\": \"NT AUTHORITY\\\\authenticated users\", \"readACLFile\": \"NT AUTHORITY\\\\authenticated users\"}], \"messageTypeId\": 15, \"discoverScanStartDate\": \"2022-02-04T15:39:28\", \"discoverUrl\": \"DLP-WINDOWS10-8 - c:\\\\passwordpolicy.ini\"}}, \"sdlp_incident_url\": \"https://my-IP/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id\u0026value(operator_1)=incident.id_in\u0026value(operand_1)=468\"}, \"raw\": null, \"inputs\": {\"sdlp_incident_id\": 468}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 7312, \"timestamp\": \"2022-03-03 10:53:00\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"notes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"editableIncidentDetails\": {\"type\": \"object\", \"properties\": {\"incidentId\": {\"type\": \"integer\"}, \"infoMap\": {\"type\": \"object\", \"properties\": {\"detectedRemediationStatus\": {\"type\": \"integer\"}, \"preventOrProtectStatusId\": {\"type\": \"integer\"}, \"incidentStatusName\": {\"type\": \"string\"}, \"isHidingNotAllowed\": {\"type\": \"boolean\"}, \"severityId\": {\"type\": \"integer\"}, \"incidentStatusId\": {\"type\": \"integer\"}, \"isHidden\": {\"type\": \"boolean\"}}}, \"customAttributeGroups\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"nameInternationalized\": {\"type\": \"boolean\"}, \"customAttributes\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"index\": {\"type\": \"integer\"}, \"displayOrder\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}, \"email\": {\"type\": \"boolean\"}}}}}}}}}, \"staticIncidentDetails\": {\"type\": \"object\", \"properties\": {\"incidentId\": {\"type\": \"integer\"}, \"infoMap\": {\"type\": \"object\", \"properties\": {\"messageType\": {\"type\": \"string\"}, \"discoverContentRootPath\": {\"type\": \"string\"}, \"policyName\": {\"type\": \"string\"}, \"discoverMillisSinceFirstSeen\": {\"type\": \"integer\"}, \"detectionServerName\": {\"type\": \"string\"}, \"discoverTargetId\": {\"type\": \"integer\"}, \"discoverName\": {\"type\": \"string\"}, \"fileOwner\": {\"type\": \"string\"}, \"policyVersion\": {\"type\": \"integer\"}, \"discoverServer\": {\"type\": \"string\"}, \"discoverRepositoryLocation\": {\"type\": \"string\"}, \"discoverScanId\": {\"type\": \"integer\"}, \"endpointConnectionStatus\": {\"type\": \"string\"}, \"policyId\": {\"type\": \"integer\"}, \"detectionServerId\": {\"type\": \"integer\"}, \"messageId\": {\"type\": \"integer\"}, \"creationDate\": {\"type\": \"string\"}, \"isBlockedStatusSuperseded\": {\"type\": \"boolean\"}, \"detectionDate\": {\"type\": \"string\"}, \"messageDate\": {\"type\": \"string\"}, \"attachmentInfo\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"messageComponentName\": {\"type\": \"string\"}, \"messageComponentId\": {\"type\": \"integer\"}, \"wasCracked\": {\"type\": \"boolean\"}, \"documentFormat\": {\"type\": \"string\"}, \"messageComponentType\": {\"type\": \"integer\"}, \"originalSize\": {\"type\": \"integer\"}}}}, \"fileCreateDate\": {\"type\": \"string\"}, \"fileAccessDate\": {\"type\": \"string\"}, \"discoverTargetName\": {\"type\": \"string\"}, \"policyGroupName\": {\"type\": \"string\"}, \"policyGroupId\": {\"type\": \"integer\"}, \"messageSource\": {\"type\": \"string\"}, \"matchCount\": {\"type\": \"integer\"}, \"messageAclEntries\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"cloudStorageCollaborator\": {\"type\": \"string\"}, \"aclType\": {\"type\": \"string\"}, \"sharepointPermission\": {\"type\": \"string\"}, \"cloudstorageRole\": {\"type\": \"string\"}, \"grantDeny\": {\"type\": \"string\"}, \"sharePointACL\": {\"type\": \"string\"}, \"readACLShare\": {\"type\": \"string\"}, \"readACLFile\": {\"type\": \"string\"}}}}, \"messageTypeId\": {\"type\": \"integer\"}, \"discoverScanStartDate\": {\"type\": \"string\"}, \"discoverUrl\": {\"type\": \"string\"}}}}}, \"sdlp_incident_url\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"sdlp_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "7e128530-9e09-405b-8f04-d7e23f5fb359",
      "version": 0,
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
          "workflow_id": 88
        }
      ]
    },
    {
      "created_date": 1716556157350,
      "description": {
        "content": "The get Symantec DLP notes and add to the corresponding SOAR case/incident.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Get DLP Notes",
      "export_key": "symantec_dlp_get_notes",
      "id": 71,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1716556157350,
      "name": "symantec_dlp_get_notes",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "ed8bf45e-c87e-4331-8e55-4f25966658e1",
      "version": 0,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "name": "Symantec DLP: Get DLP Notes",
          "object_type": "incident",
          "programmatic_name": "sdlp_get_notes",
          "tags": [],
          "uuid": null,
          "workflow_id": 85
        }
      ]
    },
    {
      "created_date": 1716556157454,
      "description": {
        "content": "Send a note from SOAR to the corresponding Symantec DLP incident.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Send Note to DLP Incident",
      "export_key": "symantec_dlp_send_note_to_dlp_incident",
      "id": 72,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1716556157454,
      "name": "symantec_dlp_send_note_to_dlp_incident",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"reason:\": null}, \"raw\": null, \"inputs\": {\"sdlp_note_text\": \"\u003cb\u003eSymantec DLP: Update Incident Status\u003c/b\u003e\u003cbr /\u003e DLP incident 468 status set to: Resolved.\", \"sdlp_incident_id\": 468}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 30032, \"timestamp\": \"2022-03-03 11:29:55\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"reason:\": {}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"sdlp_note_text\": {\"type\": \"string\"}, \"sdlp_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "1b03031b-cbfc-4ccb-8a01-ab7e109f1a33",
      "version": 0,
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
          "workflow_id": 84
        }
      ]
    },
    {
      "created_date": 1716556157552,
      "description": {
        "content": "Update the incident status of the Symantec DLP incident in DLP.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Update Incident in DLP",
      "export_key": "symantec_dlp_update_incident",
      "id": 73,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1716556157552,
      "name": "symantec_dlp_update_incident",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"sdlp_incident_id\": 468, \"sdlp_incident_status\": \"Resolved\"}, \"raw\": null, \"inputs\": {\"incident_id\": 3449, \"sdlp_incident_status\": \"Resolved\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 16146, \"timestamp\": \"2022-03-03 10:53:44\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"sdlp_incident_id\": {\"type\": \"integer\"}, \"sdlp_incident_status\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"sdlp_incident_status\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "4258886f-e439-41f2-9679-864a3d291add",
      "version": 0,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
        },
        {
          "content": "439264c3-b4d7-493b-8358-89a310ab0d8e",
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
          "name": "Symantec DLP:  Resolve Incident in DLP",
          "object_type": "incident",
          "programmatic_name": "sdlp_resolve_incident_in_dlp",
          "tags": [],
          "uuid": null,
          "workflow_id": 89
        },
        {
          "actions": [],
          "description": null,
          "name": "Symantec DLP: Update Incident in DLP",
          "object_type": "incident",
          "programmatic_name": "sdlp_update_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 83
        },
        {
          "actions": [],
          "description": null,
          "name": "Symantec DLP: Update Severity in DLP",
          "object_type": "incident",
          "programmatic_name": "sdlp_update_severity_in_dlp",
          "tags": [],
          "uuid": null,
          "workflow_id": 86
        }
      ]
    },
    {
      "created_date": 1716556157650,
      "description": {
        "content": "Upload the Symantec DLP Component binary files and add as artifact files.",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Upload Binaries",
      "export_key": "symantec_dlp_upload_binaries",
      "id": 74,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1718714943975,
      "name": "symantec_dlp_upload_binaries",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [],
      "uuid": "64c9eafd-e365-4b8b-ba61-33aa6010c601",
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
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e168b4e-0e5a-4d2c-93f8-8e45865d2e4e",
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
          "workflow_id": 87
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
      "create_date": 1718717931524,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1718717931524,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
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
        "b@example.com"
      ],
      "uuid": "d75c8560-64d2-44ca-87ce-4db510a3c5d1"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386\" isExecutable=\"true\" name=\"playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_11b2u2l\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Symantec DLP: Upload Binaries\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64c9eafd-e365-4b8b-ba61-33aa6010c601\"\u003e{\"inputs\":{\"eddd5084-0033-49af-8431-f8775bc98d6a\":{\"expression_input\":{\"expression\":\"incident.properties.sdlp_incident_id\"},\"input_type\":\"expression\"},\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"expression_input\":{\"expression\":\"incident.id\"},\"input_type\":\"expression\"},\"9e168b4e-0e5a-4d2c-93f8-8e45865d2e4e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"889a47bb-ba84-447f-b1d8-0c8d077bcad3\"}}},\"result_name\":\"upload_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_11b2u2l\u003c/incoming\u003e\u003coutgoing\u003eFlow_1rvt3y9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_11b2u2l\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SDLP upload binary as attachment\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"7f023485-40b0-40e9-b846-120a22d6621c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1rvt3y9\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ys7r14\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1rvt3y9\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1ys7r14\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1ys7r14\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ys7r14\" id=\"Flow_1ys7r14_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"462\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1rvt3y9\" id=\"Flow_1rvt3y9_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"378\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_11b2u2l\" id=\"Flow_11b2u2l_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"626\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"625.5\" y=\"378\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"658\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1718714712797,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386",
      "description": {
        "content": "Upload binaries from a specified Symantec DLP incident to the SOAR incident as attachments.",
        "format": "text"
      },
      "display_name": "Symantec DLP: Upload Binaries as Attachment - Example (PB)",
      "export_key": "symantec_dlp_upload_binaries_as_attachment__example_pb",
      "field_type_handle": "playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386",
      "fields_type": {
        "actions": [],
        "display_name": "Symantec DLP: Upload Binaries as Attachment - Example (PB)",
        "export_key": "playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386",
        "uuid": "fd0ab6d8-b87b-4476-be53-e7cd7bc60aed"
      },
      "has_logical_errors": false,
      "id": 123,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1718715925246,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1718715404890,
          "description": "",
          "enabled": false,
          "export_key": "SDLP upload binary as attachment",
          "id": 120,
          "language": "python3",
          "last_modified_by": "b@example.com",
          "last_modified_time": 1718715404890,
          "name": "SDLP upload binary as attachment",
          "object_type": "incident",
          "playbook_handle": "symantec_dlp_upload_binaries_as_attachment__example_pb",
          "programmatic_name": "symantec_dlp_upload_binaries_as_attachment__example_pb_sdlp_upload_binary_as_attachment",
          "script_text": "results = playbook.functions.results.upload_result\nsdlp_inputs = results.get(\"inputs\")\nsdlp_incident_id = sdlp_inputs.get(\"sdlp_incident_id\")\n\nnote = \"\u003cb\u003eSymantec DLP: Upload Binaries for incident Id {0}\u003c/b\u003e\u003cbr\u003e\".format(sdlp_incident_id)\ncontent = results.get(\"content\")\nif content.get(\"success\"):\n  artifact_list = content.get(\u0027artifact_name_list\u0027)\n  num_artifacts = len(artifact_list)\n  note = \"{0} {1} Attachment files added\".format(note, num_artifacts)\nelse:\n  note = \"{0} attachment NOT added\".format(note)\nincident.addNote(helper.createRichText(note))",
          "tags": [],
          "uuid": "7f023485-40b0-40e9-b846-120a22d6621c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sdlp_incident_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "symantec_dlp_upload_binaries_as_attachment__example_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_e3129ef2-363b-495d-8cc3-ebdb0a1c6386",
        "id": 127,
        "name": "playbook_e3129ef2_363b_495d_8cc3_ebdb0a1c6386",
        "type": "playbook",
        "uuid": "aaf0ccda-9491-44df-8066-227a1656ece6"
      },
      "tags": [],
      "type": "default",
      "uuid": "e3129ef2-363b-495d-8cc3-ebdb0a1c6386",
      "version": 14
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1716556156658,
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\n\nTypically, a function will create the workflow property \u0027convert_json_to_rich_text\u0027, and this script will run after that function to perform the conversion.\n\nFeatures:\n* Display the hierarchical nature of json, presenting the json keys (sorted if specified) as bold labels\n* Provide links to found URLs\n* Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.1",
      "id": 57,
      "language": "python3",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556156658,
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
    "build_number": 9340,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.9340"
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
        "workflow_id": "sdlp_close_dlp_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_close_dlp_case\" isExecutable=\"true\" name=\"Symantec DLP: Close DLP Case\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_11ugad9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1sps51b\" name=\"Symantec DLP: Close DLP Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"581c6770-d1c8-4caf-ab39-cd155fa53a09\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11ugad9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o0eesv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11ugad9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1sps51b\"/\u003e\u003cendEvent id=\"EndEvent_1wphoud\"\u003e\u003cincoming\u003eSequenceFlow_0o0eesv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0o0eesv\" sourceRef=\"ServiceTask_1sps51b\" targetRef=\"EndEvent_1wphoud\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sps51b\" id=\"ServiceTask_1sps51b_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"481\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11ugad9\" id=\"SequenceFlow_11ugad9_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"481\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"339.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wphoud\" id=\"EndEvent_1wphoud_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"819\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"837\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o0eesv\" id=\"SequenceFlow_0o0eesv_di\"\u003e\u003comgdi:waypoint x=\"581\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"819\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"700\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "",
      "export_key": "sdlp_close_dlp_case",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556219521,
      "name": "Symantec DLP: Close DLP Case",
      "object_type": "incident",
      "programmatic_name": "sdlp_close_dlp_case",
      "tags": [],
      "uuid": "8b5e8af5-beee-41f6-bd24-529433ef6570",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "sdlp_resolve_incident_in_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_resolve_incident_in_dlp\" isExecutable=\"true\" name=\"Symantec DLP:  Resolve Incident in DLP\"\u003e\u003cdocumentation\u003eResolve an incident in Symantec DLP.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0npzznd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0npzznd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_09iby9q\"/\u003e\u003cendEvent id=\"EndEvent_1pbf5bg\"\u003e\u003cincoming\u003eSequenceFlow_1qrl10d\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_09iby9q\" name=\"Symantec DLP: Update Incident in ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7a8cbfd9-c81c-4a38-952f-f86d3f7b3024\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nsdlp_incident_id = content.get(\\\"sdlp_incident_id\\\", None)\\nif success:\\n  noteText = \u0027\u0026lt;b\u0026gt;Symantec DLP: Resolve Incident in DLP\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentId {0} Resolved.\u0027.format(sdlp_incident_id)\\nelse:\\n  noteText = \u0027\u0026lt;b\u0026gt;Symantec DLP: Resolve Incident in DLP\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentId {0}: check the status in Symantec DLP.\u0027.format(sdlp_incident_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_status = \\\"Resolved\\\"\\ninputs.sdlp_incident_severity_id = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0npzznd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qrl10d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qrl10d\" sourceRef=\"ServiceTask_09iby9q\" targetRef=\"EndEvent_1pbf5bg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0npzznd\" id=\"SequenceFlow_0npzznd_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"240.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1pbf5bg\" id=\"EndEvent_1pbf5bg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"700\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"718\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_09iby9q\" id=\"ServiceTask_09iby9q_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qrl10d\" id=\"SequenceFlow_1qrl10d_di\"\u003e\u003comgdi:waypoint x=\"473\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"586.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Resolve an incident in Symantec DLP.",
      "export_key": "sdlp_resolve_incident_in_dlp",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556297291,
      "name": "Symantec DLP:  Resolve Incident in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_resolve_incident_in_dlp",
      "tags": [],
      "uuid": "d0d48db3-c9dd-4561-955a-82a935e8d74f",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_update_severity_in_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_update_severity_in_dlp\" isExecutable=\"true\" name=\"Symantec DLP: Update Severity in DLP\"\u003e\u003cdocumentation\u003eUpdate the severity in the associated DLP incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1etkl43\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1t85xwh\" name=\"Symantec DLP: Update Incident in ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"d4f4001e-291a-4fca-a2c0-fb900b1197cc\"}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_severity_id = incident.severity_code\\ninputs.sdlp_incident_status = None\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1etkl43\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_07c74o9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1etkl43\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1t85xwh\"/\u003e\u003cendEvent id=\"EndEvent_0hjuoi6\"\u003e\u003cincoming\u003eSequenceFlow_07c74o9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_07c74o9\" sourceRef=\"ServiceTask_1t85xwh\" targetRef=\"EndEvent_0hjuoi6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1t85xwh\" id=\"ServiceTask_1t85xwh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"452\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1etkl43\" id=\"SequenceFlow_1etkl43_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"325\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hjuoi6\" id=\"EndEvent_0hjuoi6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"770.6292629262927\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"788.6292629262927\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07c74o9\" id=\"SequenceFlow_07c74o9_di\"\u003e\u003comgdi:waypoint x=\"552\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"771\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"661.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Update the severity in the associated DLP incident.",
      "export_key": "sdlp_update_severity_in_dlp",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556429315,
      "name": "Symantec DLP: Update Severity in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_update_severity_in_dlp",
      "tags": [],
      "uuid": "b40ac8ad-a538-4ea4-bc88-68e3098f2924",
      "workflow_id": 86
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_upload_binaries",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_upload_binaries\" isExecutable=\"true\" name=\"Symantec DLP: Upload Binaries\"\u003e\u003cdocumentation\u003eGet the binary files associated with a DLP incident and upload to the corresponding IBM SOAR case as artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0u9x6bq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0y2wmdt\"\u003e\u003cincoming\u003eSequenceFlow_1e1upjv\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0r6tnd5\" name=\"Symantec DLP: Upload Binaries\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64c9eafd-e365-4b8b-ba61-33aa6010c601\"\u003e{\"inputs\":{},\"post_processing_script\":\"sdlp_inputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = sdlp_inputs.get(\\\"sdlp_incident_id\\\")\\n\\nnote = \\\"\u0026lt;b\u0026gt;Symantec DLP: Upload Binaries for incident Id {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\".format(sdlp_incident_id)\\ncontent = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\")\\nif success:\\n  artifact_list = content.get(\u0027artifact_name_list\u0027)\\n  num_artifacts = len(artifact_list)\\n  note = \\\"{0} {1} artifact files added\\\".format(note, num_artifacts)\\nelse:\\n  note = \\\"{0} artifact NOT added\\\".format(note)\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0u9x6bq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e1upjv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0u9x6bq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0r6tnd5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1e1upjv\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"EndEvent_0y2wmdt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_09o1nkq\"\u003e\u003ctext\u003eInput: Symantec DLP incident Id, SOAR case id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0k77hge\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"TextAnnotation_09o1nkq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0i0mox2\"\u003e\u003ctext\u003eOutput: Symantec DLP incident files addesd as artifact files in SOAR; result written to a SOAR note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0j0ewky\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"TextAnnotation_0i0mox2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y2wmdt\" id=\"EndEvent_0y2wmdt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"811\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"829\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0r6tnd5\" id=\"ServiceTask_0r6tnd5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"447\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u9x6bq\" id=\"SequenceFlow_0u9x6bq_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"322.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e1upjv\" id=\"SequenceFlow_1e1upjv_di\"\u003e\u003comgdi:waypoint x=\"547\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"811\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"679\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_09o1nkq\" id=\"TextAnnotation_09o1nkq_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"287\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0k77hge\" id=\"Association_0k77hge_di\"\u003e\u003comgdi:waypoint x=\"454\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"354\" y=\"83\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0i0mox2\" id=\"TextAnnotation_0i0mox2_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"579\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0j0ewky\" id=\"Association_0j0ewky_di\"\u003e\u003comgdi:waypoint x=\"535\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"615\" y=\"83\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Get the binary files associated with a DLP incident and upload to the corresponding IBM SOAR case as artifacts.",
      "export_key": "sdlp_upload_binaries",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556354580,
      "name": "Symantec DLP: Upload Binaries",
      "object_type": "incident",
      "programmatic_name": "sdlp_upload_binaries",
      "tags": [],
      "uuid": "18314a54-a9c0-49f7-b1f9-98af37c7ec7d",
      "workflow_id": 87
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "sdlp_send_soar_note_to_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_send_soar_note_to_dlp\" isExecutable=\"true\" name=\"Symantec DLP: Send SOAR Note to DLP\"\u003e\u003cdocumentation\u003eSend a SOAR note to the corresponding DLP incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0w8abzz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19r4cvd\" name=\"Symantec DLP: Send Note to DLP In...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1b03031b-cbfc-4ccb-8a01-ab7e109f1a33\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Import Date\\nfrom java.util import Date\\n\\n# Edit note in SOAR to indicate it was sent to SentinelOne\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = \\\"\u0026lt;b\u0026gt;Sent to Symantec DLP at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.sdlp_note_text = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0w8abzz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mfe8fq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0w8abzz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19r4cvd\"/\u003e\u003cendEvent id=\"EndEvent_1obxbt6\"\u003e\u003cincoming\u003eSequenceFlow_0mfe8fq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0mfe8fq\" sourceRef=\"ServiceTask_19r4cvd\" targetRef=\"EndEvent_1obxbt6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19r4cvd\" id=\"ServiceTask_19r4cvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"485\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w8abzz\" id=\"SequenceFlow_0w8abzz_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"485\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"341.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1obxbt6\" id=\"EndEvent_1obxbt6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"756\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"774\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mfe8fq\" id=\"SequenceFlow_0mfe8fq_di\"\u003e\u003comgdi:waypoint x=\"585\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"756\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"670.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Send a SOAR note to the corresponding DLP incident.",
      "export_key": "sdlp_send_soar_note_to_dlp",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556392148,
      "name": "Symantec DLP: Send SOAR Note to DLP",
      "object_type": "note",
      "programmatic_name": "sdlp_send_soar_note_to_dlp",
      "tags": [],
      "uuid": "6e3f7a89-e689-448d-ad08-ed3c8f1988fc",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_update_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_update_incident\" isExecutable=\"true\" name=\"Symantec DLP: Update Incident in DLP\"\u003e\u003cdocumentation\u003eUpdate the DLP incident status and severity in DLP.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1hgy1g1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hgy1g1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_085sbtd\"/\u003e\u003cendEvent id=\"EndEvent_0gmht6l\"\u003e\u003cincoming\u003eSequenceFlow_062edc4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_085sbtd\" name=\"Symantec DLP: Update Incident in ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7a8cbfd9-c81c-4a38-952f-f86d3f7b3024\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nsdlp_incident_id = content.get(\\\"sdlp_incident_id\\\", None)\\nsdlp_incident_status = content.get(\\\"sdlp_incident_status\\\", None)\\nsdlp_incident_severity_id = content.get(\\\"sdlp_incident_severity_id\\\", None)\\n\\nif success:\\n  noteText = \u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; DLP incident {0}\u0026lt;br\u0026gt;   Status set to: {1}\u0026lt;br\u0026gt;   Severity set to: {2}\u0027.format(sdlp_incident_id, sdlp_incident_status, sdlp_incident_severity_id)\\nelse:\\n  noteText = \u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;DLP incident {0} was not updated.  Check input values.\u0027.format(sdlp_incident_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_status = rule.properties.sdlp_incident_status\\ninputs.sdlp_incident_severity_id = rule.properties.sdlp_incident_severity_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1hgy1g1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_062edc4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_062edc4\" sourceRef=\"ServiceTask_085sbtd\" targetRef=\"EndEvent_0gmht6l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hgy1g1\" id=\"SequenceFlow_1hgy1g1_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"444\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"276\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gmht6l\" id=\"EndEvent_0gmht6l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"784\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"802\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_085sbtd\" id=\"ServiceTask_085sbtd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"444\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_062edc4\" id=\"SequenceFlow_062edc4_di\"\u003e\u003comgdi:waypoint x=\"544\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"784\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"619\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Update the DLP incident status and severity in DLP.",
      "export_key": "sdlp_update_incident",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556416445,
      "name": "Symantec DLP: Update Incident in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_update_incident",
      "tags": [],
      "uuid": "1fd78ffa-7f75-4513-bf77-88fa7d019ce8",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_write_incident_details_to_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_write_incident_details_to_note\" isExecutable=\"true\" name=\"Symantec DLP: Write Incident Details to Note\"\u003e\u003cdocumentation\u003eCall the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15u7h7q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13cc5dk\" name=\"Symantec DLP: Get Incident Detail...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e128530-9e09-405b-8f04-d7e23f5fb359\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = inputs.get(\\\"sdlp_incident_id\\\")\\ncontent = results.get(\\\"content\\\")\\n\\nheader = \\\"Symantec DLP Incident Id: {0} Details:\\\".format(sdlp_incident_id)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15u7h7q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f1dod6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15u7h7q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13cc5dk\"/\u003e\u003cscriptTask id=\"ScriptTask_038nkue\" name=\"Convert JSON to rich text v1.1\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v11\" uuid=\"874d929b-7b4c-4f47-983a-58295c93d6bf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f1dod6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16xnfca\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f1dod6\" sourceRef=\"ServiceTask_13cc5dk\" targetRef=\"ScriptTask_038nkue\"/\u003e\u003cendEvent id=\"EndEvent_1a5c3zv\"\u003e\u003cincoming\u003eSequenceFlow_16xnfca\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16xnfca\" sourceRef=\"ScriptTask_038nkue\" targetRef=\"EndEvent_1a5c3zv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13cc5dk\" id=\"ServiceTask_13cc5dk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"385\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15u7h7q\" id=\"SequenceFlow_15u7h7q_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"291.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_038nkue\" id=\"ScriptTask_038nkue_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"703.936\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f1dod6\" id=\"SequenceFlow_0f1dod6_di\"\u003e\u003comgdi:waypoint x=\"485\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"704\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"594.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1a5c3zv\" id=\"EndEvent_1a5c3zv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"963.936\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"981.936\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16xnfca\" id=\"SequenceFlow_16xnfca_di\"\u003e\u003comgdi:waypoint x=\"804\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"964\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"884\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Call the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.",
      "export_key": "sdlp_write_incident_details_to_note",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556451344,
      "name": "Symantec DLP: Write Incident Details to Note",
      "object_type": "incident",
      "programmatic_name": "sdlp_write_incident_details_to_note",
      "tags": [],
      "uuid": "7887e541-1511-4432-9890-ebeebbc2873c",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "sdlp_get_notes",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_get_notes\" isExecutable=\"true\" name=\"Symantec DLP: Get DLP Notes\"\u003e\u003cdocumentation\u003eGet the Symantec DLP incident notes and add any new notes to the SOAR case/incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02pmk6d\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1vpa8b7\" name=\"Symantec DLP: Get DLP Notes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ed8bf45e-c87e-4331-8e55-4f25966658e1\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02pmk6d\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_12iu10z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02pmk6d\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1vpa8b7\"/\u003e\u003cendEvent id=\"EndEvent_01esxdz\"\u003e\u003cincoming\u003eSequenceFlow_12iu10z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_12iu10z\" sourceRef=\"ServiceTask_1vpa8b7\" targetRef=\"EndEvent_01esxdz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1vpa8b7\" id=\"ServiceTask_1vpa8b7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"505\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02pmk6d\" id=\"SequenceFlow_02pmk6d_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"351.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01esxdz\" id=\"EndEvent_01esxdz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"825\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"843\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12iu10z\" id=\"SequenceFlow_12iu10z_di\"\u003e\u003comgdi:waypoint x=\"605\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"825\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"715\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get the Symantec DLP incident notes and add any new notes to the SOAR case/incident.",
      "export_key": "sdlp_get_notes",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1716556158592,
      "name": "Symantec DLP: Get DLP Notes",
      "object_type": "incident",
      "programmatic_name": "sdlp_get_notes",
      "tags": [],
      "uuid": "11072739-c6f1-4820-8863-fa8f0caf4156",
      "workflow_id": 85
    }
  ],
  "workspaces": []
}
