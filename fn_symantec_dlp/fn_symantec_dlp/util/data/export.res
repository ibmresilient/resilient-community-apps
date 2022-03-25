{
  "action_order": [],
  "actions": [
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
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_status",
          "method": "not_equals",
          "type": null,
          "value": "Resolved"
        }
      ],
      "enabled": true,
      "export_key": "Symantec DLP: Resolve Incident in DLP",
      "id": 682,
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
      "id": 660,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Send SOAR Note to DLP",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 661,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Update DLP Incident Status",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 662,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Upload Binaries",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 663,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Upload Binaries as Artifact",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 664,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Symantec DLP: Write DLP Incident Details to Note",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
  "export_date": 1648228614254,
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
      "id": 309,
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
          "tag_handle": "fn_crowd_strike",
          "value": null
        },
        {
          "tag_handle": "fn_exchange_online",
          "value": null
        },
        {
          "tag_handle": "fn_jira",
          "value": null
        },
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        },
        {
          "tag_handle": "fn_sentinelone",
          "value": null
        },
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
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
      "export_key": "__function/sdlp_incident_id",
      "hide_notification": false,
      "id": 920,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 921,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 922,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
          "value": 957
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "a3434db8-d0d7-4a4f-9b24-c603a26203e5",
          "value": 958
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "47e781b2-212f-4f6f-97f8-0b32723b2472",
          "value": 959
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "7a8cbfd9-c81c-4a38-952f-f86d3f7b3024",
          "value": 960
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "fd4ed4d0-35ef-417e-a944-3e2859ba069f",
          "value": 961
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
      "id": 919,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
          "value": 952
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "45cf43bd-df22-47ac-ad9e-1f7f77761391",
          "value": 953
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Investigation",
          "properties": null,
          "uuid": "ecd10a36-d09a-43c6-b212-ef84e8c19e77",
          "value": 954
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "f8cd108a-9ce4-4250-b120-02141ecc7e72",
          "value": 955
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Dismissed",
          "properties": null,
          "uuid": "a50db2cb-9694-49df-a0f3-47073871959b",
          "value": 956
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
      "id": 894,
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
      "id": 892,
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
      "id": 890,
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
      "id": 893,
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
      "id": 842,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 841,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "id": 857,
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
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "created_date": 1646686888544,
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
      "id": 542,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1646686888586,
      "name": "symantec_dlp_get_incident_details",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"notes\": [\"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-07T16:23:50.32\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded a note 2/7/2022 4:23pm\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-08T08:31:12.158\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded a second note 2/7/2022\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-10T20:49:58.47\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded note to SOAR and will send it to DLP\u003c/p\u003e\\n                        \", \"\u003cb\u003eFrom Symantec DLP\u003c/b\u003e\\n                        \u003cbr\u003e\\n                        \u003cb\u003eUser: \u003c/b\u003eAdministrator added note at 2022-02-10T20:49:58.47\\n                        \u003cbr\u003e\\n                        \u003cb\u003eNote detail\u003c/b\u003e: \u003cp\u003eadded note to SOAR and will send it to DLP\u003c/p\u003e\\n                        \"], \"editableIncidentDetails\": {\"incidentId\": 468, \"infoMap\": {\"detectedRemediationStatus\": 0, \"preventOrProtectStatusId\": 0, \"incidentStatusName\": \"Resolved\", \"isHidingNotAllowed\": false, \"severityId\": 1, \"incidentStatusId\": 3, \"isHidden\": false}, \"customAttributeGroups\": [{\"name\": \"custom_attribute_group.default\", \"nameInternationalized\": true, \"customAttributes\": [{\"name\": \"ibm_soar_case_url\", \"index\": 17, \"displayOrder\": 1, \"value\": \"https://mysoar.com:443/#incidents/3449\", \"email\": false}, {\"name\": \"ibm_soar_case_id\", \"index\": 18, \"displayOrder\": 2, \"value\": \"3449\", \"email\": false}]}, {\"name\": \"Predefined\", \"nameInternationalized\": false, \"customAttributes\": [{\"name\": \"Resolution\", \"index\": 1, \"displayOrder\": 1, \"value\": \"Business Issue\", \"email\": false}, {\"name\": \"Dismissal Reason\", \"index\": 2, \"displayOrder\": 2, \"value\": \"Bus. Process Issue\", \"email\": false}, {\"name\": \"Assigned To\", \"index\": 3, \"displayOrder\": 3, \"email\": false}, {\"name\": \"Business Unit\", \"index\": 4, \"displayOrder\": 4, \"email\": false}, {\"name\": \"Employee Code\", \"index\": 5, \"displayOrder\": 5, \"email\": false}, {\"name\": \"First Name\", \"index\": 6, \"displayOrder\": 6, \"email\": false}, {\"name\": \"Last Name\", \"index\": 7, \"displayOrder\": 7, \"email\": false}, {\"name\": \"Phone\", \"index\": 8, \"displayOrder\": 8, \"email\": false}, {\"name\": \"Sender Email\", \"index\": 9, \"displayOrder\": 9, \"email\": true}, {\"name\": \"Manager First Name\", \"index\": 11, \"displayOrder\": 10, \"email\": false}, {\"name\": \"Manager Last Name\", \"index\": 10, \"displayOrder\": 11, \"email\": false}, {\"name\": \"Manager Phone\", \"index\": 12, \"displayOrder\": 12, \"email\": false}, {\"name\": \"Manager Email\", \"index\": 13, \"displayOrder\": 13, \"email\": true}, {\"name\": \"Region\", \"index\": 14, \"displayOrder\": 14, \"email\": false}, {\"name\": \"Country\", \"index\": 15, \"displayOrder\": 15, \"email\": false}, {\"name\": \"Postal Code\", \"index\": 16, \"displayOrder\": 16, \"email\": false}]}]}, \"staticIncidentDetails\": {\"incidentId\": 468, \"infoMap\": {\"messageType\": \"EDAR\", \"discoverContentRootPath\": \"DLP-WINDOWS10-8\", \"policyName\": \"Customer Data Protection\", \"discoverMillisSinceFirstSeen\": 165799618, \"detectionServerName\": \"Single-tier Detection Server\", \"discoverTargetId\": 21, \"discoverName\": \"passwordpolicy.ini\", \"fileOwner\": \"BUILTIN\\\\administrators\", \"policyVersion\": 2, \"discoverServer\": \"DLP-WINDOWS10-8\", \"discoverRepositoryLocation\": \"DLP-WINDOWS10-8 - c:\\\\passwordpolicy.ini\", \"discoverScanId\": 41, \"endpointConnectionStatus\": \"CONNECTED\", \"policyId\": 16, \"detectionServerId\": 1, \"messageId\": 468, \"creationDate\": \"2022-02-04T16:08:48.678\", \"isBlockedStatusSuperseded\": false, \"detectionDate\": \"2022-02-04T16:08:43.08\", \"messageDate\": \"2022-02-03T22:40:43\", \"attachmentInfo\": [{\"messageComponentName\": \"c:\\\\passwordpolicy.ini\", \"messageComponentId\": 981, \"wasCracked\": false, \"documentFormat\": \"unicode\", \"messageComponentType\": 3, \"originalSize\": 16482}], \"fileCreateDate\": \"2021-02-12T09:50:16.39\", \"fileAccessDate\": \"2022-02-04T16:01:06.431\", \"discoverTargetName\": \"SS number on 9.30.94.38\", \"policyGroupName\": \"Customer Data Protection\", \"policyGroupId\": 5, \"messageSource\": \"DISCOVER\", \"matchCount\": 2, \"messageAclEntries\": [{\"cloudStorageCollaborator\": \"BUILTIN\\\\administrators\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\administrators\", \"readACLShare\": \"BUILTIN\\\\administrators\", \"readACLFile\": \"BUILTIN\\\\administrators\"}, {\"cloudStorageCollaborator\": \"BUILTIN\\\\administrators\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\administrators\", \"readACLShare\": \"BUILTIN\\\\administrators\", \"readACLFile\": \"BUILTIN\\\\administrators\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\system\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\system\", \"readACLShare\": \"NT AUTHORITY\\\\system\", \"readACLFile\": \"NT AUTHORITY\\\\system\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\system\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\system\", \"readACLShare\": \"NT AUTHORITY\\\\system\", \"readACLFile\": \"NT AUTHORITY\\\\system\"}, {\"cloudStorageCollaborator\": \"BUILTIN\\\\users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"BUILTIN\\\\users\", \"readACLShare\": \"BUILTIN\\\\users\", \"readACLFile\": \"BUILTIN\\\\users\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\authenticated users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"WRITE\", \"cloudstorageRole\": \"WRITE\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\authenticated users\", \"readACLShare\": \"NT AUTHORITY\\\\authenticated users\", \"readACLFile\": \"NT AUTHORITY\\\\authenticated users\"}, {\"cloudStorageCollaborator\": \"NT AUTHORITY\\\\authenticated users\", \"aclType\": \"FILE\", \"sharepointPermission\": \"READ\", \"cloudstorageRole\": \"READ\", \"grantDeny\": \"GRANT\", \"sharePointACL\": \"NT AUTHORITY\\\\authenticated users\", \"readACLShare\": \"NT AUTHORITY\\\\authenticated users\", \"readACLFile\": \"NT AUTHORITY\\\\authenticated users\"}], \"messageTypeId\": 15, \"discoverScanStartDate\": \"2022-02-04T15:39:28\", \"discoverUrl\": \"DLP-WINDOWS10-8 - c:\\\\passwordpolicy.ini\"}}, \"sdlp_incident_url\": \"https://my-IP/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id\u0026value(operator_1)=incident.id_in\u0026value(operand_1)=468\"}, \"raw\": null, \"inputs\": {\"sdlp_incident_id\": 468}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"my-laptop\", \"execution_time_ms\": 7312, \"timestamp\": \"2022-03-03 10:53:00\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"notes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"editableIncidentDetails\": {\"type\": \"object\", \"properties\": {\"incidentId\": {\"type\": \"integer\"}, \"infoMap\": {\"type\": \"object\", \"properties\": {\"detectedRemediationStatus\": {\"type\": \"integer\"}, \"preventOrProtectStatusId\": {\"type\": \"integer\"}, \"incidentStatusName\": {\"type\": \"string\"}, \"isHidingNotAllowed\": {\"type\": \"boolean\"}, \"severityId\": {\"type\": \"integer\"}, \"incidentStatusId\": {\"type\": \"integer\"}, \"isHidden\": {\"type\": \"boolean\"}}}, \"customAttributeGroups\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"nameInternationalized\": {\"type\": \"boolean\"}, \"customAttributes\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"index\": {\"type\": \"integer\"}, \"displayOrder\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}, \"email\": {\"type\": \"boolean\"}}}}}}}}}, \"staticIncidentDetails\": {\"type\": \"object\", \"properties\": {\"incidentId\": {\"type\": \"integer\"}, \"infoMap\": {\"type\": \"object\", \"properties\": {\"messageType\": {\"type\": \"string\"}, \"discoverContentRootPath\": {\"type\": \"string\"}, \"policyName\": {\"type\": \"string\"}, \"discoverMillisSinceFirstSeen\": {\"type\": \"integer\"}, \"detectionServerName\": {\"type\": \"string\"}, \"discoverTargetId\": {\"type\": \"integer\"}, \"discoverName\": {\"type\": \"string\"}, \"fileOwner\": {\"type\": \"string\"}, \"policyVersion\": {\"type\": \"integer\"}, \"discoverServer\": {\"type\": \"string\"}, \"discoverRepositoryLocation\": {\"type\": \"string\"}, \"discoverScanId\": {\"type\": \"integer\"}, \"endpointConnectionStatus\": {\"type\": \"string\"}, \"policyId\": {\"type\": \"integer\"}, \"detectionServerId\": {\"type\": \"integer\"}, \"messageId\": {\"type\": \"integer\"}, \"creationDate\": {\"type\": \"string\"}, \"isBlockedStatusSuperseded\": {\"type\": \"boolean\"}, \"detectionDate\": {\"type\": \"string\"}, \"messageDate\": {\"type\": \"string\"}, \"attachmentInfo\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"messageComponentName\": {\"type\": \"string\"}, \"messageComponentId\": {\"type\": \"integer\"}, \"wasCracked\": {\"type\": \"boolean\"}, \"documentFormat\": {\"type\": \"string\"}, \"messageComponentType\": {\"type\": \"integer\"}, \"originalSize\": {\"type\": \"integer\"}}}}, \"fileCreateDate\": {\"type\": \"string\"}, \"fileAccessDate\": {\"type\": \"string\"}, \"discoverTargetName\": {\"type\": \"string\"}, \"policyGroupName\": {\"type\": \"string\"}, \"policyGroupId\": {\"type\": \"integer\"}, \"messageSource\": {\"type\": \"string\"}, \"matchCount\": {\"type\": \"integer\"}, \"messageAclEntries\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"cloudStorageCollaborator\": {\"type\": \"string\"}, \"aclType\": {\"type\": \"string\"}, \"sharepointPermission\": {\"type\": \"string\"}, \"cloudstorageRole\": {\"type\": \"string\"}, \"grantDeny\": {\"type\": \"string\"}, \"sharePointACL\": {\"type\": \"string\"}, \"readACLShare\": {\"type\": \"string\"}, \"readACLFile\": {\"type\": \"string\"}}}}, \"messageTypeId\": {\"type\": \"integer\"}, \"discoverScanStartDate\": {\"type\": \"string\"}, \"discoverUrl\": {\"type\": \"string\"}}}}}, \"sdlp_incident_url\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"sdlp_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
          "tags": [
            {
              "tag_handle": "fn_symantec_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 603
        }
      ]
    },
    {
      "created_date": 1646686888609,
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
      "id": 543,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1646686888647,
      "name": "symantec_dlp_send_note_to_dlp_incident",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"reason:\": null}, \"raw\": null, \"inputs\": {\"sdlp_note_text\": \"\u003cb\u003eSymantec DLP: Update Incident Status\u003c/b\u003e\u003cbr /\u003e DLP incident 468 status set to: Resolved.\", \"sdlp_incident_id\": 468}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"my-laptop\", \"execution_time_ms\": 30032, \"timestamp\": \"2022-03-03 11:29:55\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"reason:\": {}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"sdlp_note_text\": {\"type\": \"string\"}, \"sdlp_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
          "tags": [
            {
              "tag_handle": "fn_symantec_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 605
        }
      ]
    },
    {
      "created_date": 1646686888671,
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
      "id": 544,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647026411167,
      "name": "symantec_dlp_update_incident_status",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"sdlp_incident_id\": 468, \"sdlp_incident_status\": \"Resolved\"}, \"raw\": null, \"inputs\": {\"incident_id\": 3449, \"sdlp_incident_status\": \"Resolved\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-symantec-dlp\", \"package_version\": \"2.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 16146, \"timestamp\": \"2022-03-03 10:53:44\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"sdlp_incident_id\": {\"type\": \"integer\"}, \"sdlp_incident_status\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"sdlp_incident_status\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "4258886f-e439-41f2-9679-864a3d291add",
      "version": 2,
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
          "workflow_id": 624
        },
        {
          "actions": [],
          "description": null,
          "name": "Symantec DLP: Update Incident Status in DLP",
          "object_type": "incident",
          "programmatic_name": "sdlp_update_incident_status",
          "tags": [
            {
              "tag_handle": "fn_symantec_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 604
        }
      ]
    },
    {
      "created_date": 1646686888735,
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
      "id": 545,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1647026411167,
      "name": "symantec_dlp_upload_binaries",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
          "name": "Symantec DLP: Upload Binaries",
          "object_type": "incident",
          "programmatic_name": "sdlp_upload_binaries",
          "tags": [
            {
              "tag_handle": "fn_symantec_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 602
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 21,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1648228610293,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1648228610293,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "cb29d896-6a40-44c5-83e4-6d0e87603323"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_symantec_dlp",
      "name": "Symantec DLP Message Destination",
      "programmatic_name": "fn_symantec_dlp",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
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
      "created_date": 1642702025668,
      "creator_id": "admin@example.com",
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\n\nTypically, a function will create the workflow property \u0027convert_json_to_rich_text\u0027, and this script will run after that function to perform the conversion.\n\nFeatures:\n* Display the hierarchical nature of json, presenting the json keys (sorted if specified) as bold labels\n* Provide links to found URLs\n* Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.1",
      "id": 39,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1642702025685,
      "name": "Convert JSON to rich text v1.1",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text_v11",
      "script_text": "# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.\nVERSION = 1.1\n\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to define the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, {\n    \"version\": 1.1,\n    \"header\": \"Artifact scan results for: {}\".format(artifact.value),\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr /\u003e\",\n    \"sort\": True,\n    \"json\": results.content,\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.1, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr /\u003e\"|list such as [\u0027\u003cspan\u003e\u0027,\u0027\u003c/span\u003e\u0027], [html separator between json keys and lists or defaults to html break: \u0027\u003cbr /\u003e\u0027. \n                                                If a list, then the data is brackets by the pair specified]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\"\"\"\n\nimport re\n\n# needed for python 3\ntry:\n    unicode(\"abc\")\nexcept:\n    unicode = str\n\n\nrc = re.compile(r\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#\\?]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n    \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n\n    def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr /\u003e\", sort_keys=False):\n        self.omit_keys = omit_keys\n        self.padding = padding\n        self.separator = separator\n        self.sort_keys = sort_keys\n\n\n    def format_link(self, item):\n        \"\"\"[summary]\n          Find embedded urls (http(s)) and add html anchor tags to display as links\n          Args:\n              item ([string])\n\n          Returns:\n              [str]: None|original text if no links|text with html links\n        \"\"\"\n        formatted_item = item\n        if item and not isinstance(item, (int, bool, float)):\n            list = rc.findall(item)\n            if list:\n                for link in list:\n                    formatted_item = formatted_item.replace(link, u\"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n        return formatted_item\n\n    def expand_list(self, list_value, is_list=False):\n        \"\"\"[summary]\n          convert items to html, adding indents to nested dictionaries.\n          Args:\n              list_value ([dict|list]): json element\n\n          Returns:\n              [str]: html converted code\n        \"\"\"\n        if not isinstance(list_value, list):\n            return self.format_link(list_value)\n        elif not list_value:\n            return u\"None\u003cbr\u003e\"\n\n        try:\n            items_list = []  # this will ensure list starts on second line of key label\n            for item in list_value:\n                if isinstance(item, dict):\n                    result = self.convert_json_to_rich_text(item)\n                    if is_list:\n                        items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(result))\n                    else:\n                        items_list.append(result)\n                elif isinstance(item, list):\n                    items_list.append(self.expand_list(item, is_list=True))\n                elif is_list:\n                    items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(self.format_link(unicode(item))))\n                else:\n                    items_list.append(self.format_link(unicode(item)))\n\n            expand_list_result = self.add_separator(self.separator if not is_list else u\"\",\n                                                    items_list,\n                                                    is_list=is_list)\n\n            if is_list:\n                return u\"\u003cul\u003e{}\u003c/ul\u003e\".format(expand_list_result)\n            else:\n                return u\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(expand_list_result)\n        except Exception as err:\n            return str(err)\n\n    def convert_json_to_rich_text(self, sub_dict):\n        \"\"\"[summary]\n          Walk dictionary tree and convert to html for better display\n          Args:\n              sub_dict ([type]): [description]\n\n          Returns:\n              [type]: [description]\n        \"\"\"\n        notes = []\n        if sub_dict:\n            if isinstance(sub_dict, list):\n                expanded_list = self.expand_list(sub_dict, is_list=True)\n                notes.append(self.add_separator(self.separator, expanded_list))\n            else:\n                keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n                for key in keys:\n                    if key not in self.omit_keys:\n                        value = sub_dict[key]\n                        is_list = isinstance(value, list)\n                        item_list = [u\"\u003cstrong\u003e{0}\u003c/strong\u003e: \".format(key)]\n                        if isinstance(value, dict):\n                            convert_result = self.convert_json_to_rich_text(value)\n                            if convert_result:\n                                item_list.append(u\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, convert_result))\n                            else:\n                                item_list.append(u\"None\u003cbr\u003e\")\n                        else:\n                            item_list.append(self.expand_list(value, is_list=is_list))\n                        notes.append(self.add_separator(self.separator, u\"\".join(unicode(v) for v in item_list), is_list=is_list))\n\n        result_notes = u\"\".join(notes)\n        if isinstance(self.separator, list):\n            return result_notes\n        else:\n            return result_notes.replace(\n                u\"\u003c/div\u003e{0}\".format(self.separator), u\"\u003c/div\u003e\").replace(\n                u\"{0}\u003c/div\u003e\".format(self.separator), u\"\u003c/div\u003e\"\n            )  # tighten up result\n\n    def add_separator(self, separator, items, is_list=False):\n        \"\"\"\n        apply the separator to the data\n        :param separator: None, str or list such as [\u0027\u003cspan\u003e\u0027, \u0027\u003c/span\u003e\u0027]\n        :param items: str or list to add separator\n        :return: text with separator applied\n        \"\"\"\n        _items = items\n\n        if not _items:\n            return \"\u003cbr\u003e\"\n\n        if not isinstance(_items, list):\n            _items = [_items]\n\n        if isinstance(separator, list):\n            return u\"\".join([u\"{}{}{}\".format(separator[0], item, separator[1]) for item in _items])\n\n        return u\"{}{}\".format(separator.join(_items), separator if not is_list else u\"\")\n\ndef get_properties(property_name):\n    \"\"\"\n    Logic to collect the json and parameters from a workflow property.\n    Args:\n      property_name: workflow property to reference\n    Returns:\n      padding, separator, header, json_omit_list, incident_field, json, sort_keys\n    \"\"\"\n    if not workflow.properties.get(property_name):\n        helper.fail(\"workflow.properties.{} undefined\".format(property_name))\n\n    padding = int(workflow.properties[property_name].get(\"padding\", 10))\n    separator = workflow.properties[property_name].get(\"separator\", u\"\u003cbr /\u003e\")\n    if isinstance(separator, list) and len(separator) != 2:\n        helper.fail(\"list of separators should be specified as a pair such as [\u0027\u003cdiv\u003e\u0027, \u0027\u003c/div\u003e\u0027]: {}\".format(separator))\n\n    header = workflow.properties[property_name].get(\"header\")\n    json_omit_list = workflow.properties[property_name].get(\"json_omit_list\")\n    if not json_omit_list:\n        json_omit_list = []\n    incident_field = workflow.properties[property_name].get(\"incident_field\")\n    json = workflow.properties[property_name].get(\"json\", {})\n    if not isinstance(json, dict) and not isinstance(json, list):\n        helper.fail(\"json element is not formatted correctly: {}\".format(json))\n    sort_keys = bool(workflow.properties[property_name].get(\"sort\", False))\n\n    return padding, separator, header, json_omit_list, incident_field, json, sort_keys\n\n\n## S T A R T\nif \u0027workflow\u0027 in globals():\n    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\n\n    if header:\n        if isinstance(separator, list):\n            hdr = u\"{0}{1}{2}\".format(separator[0], header, separator[1])\n        else:\n            hdr = u\"{0}{1}\".format(header, separator)\n    else:\n        hdr = u\"\"\n\n    convert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\n    converted_json = convert.convert_json_to_rich_text(json)\n    result = u\"{}{}\".format(hdr, converted_json if converted_json else \"\\nNone\")\n\n    rich_text_note = helper.createRichText(result)\n    if incident_field:\n        incident[incident_field] = rich_text_note\n    else:\n        incident.addNote(rich_text_note)\n",
      "tags": [
        {
          "tag_handle": "fn_sentinelone",
          "value": null
        },
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "874d929b-7b4c-4f47-983a-58295c93d6bf"
    }
  ],
  "server_version": {
    "build_number": 7058,
    "major": 42,
    "minor": 0,
    "version": "42.0.7058"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "sdlp_write_incident_details_to_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_write_incident_details_to_note\" isExecutable=\"true\" name=\"Symantec DLP: Write Incident Details to Note\"\u003e\u003cdocumentation\u003eCall the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15u7h7q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13cc5dk\" name=\"Symantec DLP: Get Incident Detail...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7e128530-9e09-405b-8f04-d7e23f5fb359\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = inputs.get(\\\"sdlp_incident_id\\\")\\ncontent = results.get(\\\"content\\\")\\n\\nheader = u\\\"Symantec DLP Incident Id: {0} Details:\\\".format(sdlp_incident_id)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15u7h7q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f1dod6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15u7h7q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13cc5dk\"/\u003e\u003cscriptTask id=\"ScriptTask_038nkue\" name=\"Convert JSON to rich text v1.1\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v11\" uuid=\"874d929b-7b4c-4f47-983a-58295c93d6bf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f1dod6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16xnfca\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f1dod6\" sourceRef=\"ServiceTask_13cc5dk\" targetRef=\"ScriptTask_038nkue\"/\u003e\u003cendEvent id=\"EndEvent_1a5c3zv\"\u003e\u003cincoming\u003eSequenceFlow_16xnfca\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16xnfca\" sourceRef=\"ScriptTask_038nkue\" targetRef=\"EndEvent_1a5c3zv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13cc5dk\" id=\"ServiceTask_13cc5dk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"385\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15u7h7q\" id=\"SequenceFlow_15u7h7q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"291.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_038nkue\" id=\"ScriptTask_038nkue_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"703.936\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f1dod6\" id=\"SequenceFlow_0f1dod6_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"704\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"594.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1a5c3zv\" id=\"EndEvent_1a5c3zv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"963.936\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"981.936\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16xnfca\" id=\"SequenceFlow_16xnfca_di\"\u003e\u003comgdi:waypoint x=\"804\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"964\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"884\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Call the function to get DLP incident details in JSON format and use the convert_json_to_rich_text script to print readable formatted JSON to an incident note.",
      "export_key": "sdlp_write_incident_details_to_note",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1646686889131,
      "name": "Symantec DLP: Write Incident Details to Note",
      "object_type": "incident",
      "programmatic_name": "sdlp_write_incident_details_to_note",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "7887e541-1511-4432-9890-ebeebbc2873c",
      "workflow_id": 603
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "sdlp_send_soar_note_to_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_send_soar_note_to_dlp\" isExecutable=\"true\" name=\"Symantec DLP: Send SOAR Note to DLP\"\u003e\u003cdocumentation\u003eSend a SOAR note to the corresponding DLP incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0w8abzz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19r4cvd\" name=\"Symantec DLP: Send Note to DLP In...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1b03031b-cbfc-4ccb-8a01-ab7e109f1a33\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Import Date\\nfrom java.util import Date\\n\\n# Edit note in SOAR to indicate it was sent to SentinelOne\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to Symantec DLP at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.sdlp_note_text = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0w8abzz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mfe8fq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0w8abzz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19r4cvd\"/\u003e\u003cendEvent id=\"EndEvent_1obxbt6\"\u003e\u003cincoming\u003eSequenceFlow_0mfe8fq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0mfe8fq\" sourceRef=\"ServiceTask_19r4cvd\" targetRef=\"EndEvent_1obxbt6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19r4cvd\" id=\"ServiceTask_19r4cvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"485\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w8abzz\" id=\"SequenceFlow_0w8abzz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"341.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1obxbt6\" id=\"EndEvent_1obxbt6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"756\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"774\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mfe8fq\" id=\"SequenceFlow_0mfe8fq_di\"\u003e\u003comgdi:waypoint x=\"585\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"756\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"670.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Send a SOAR note to the corresponding DLP incident.",
      "export_key": "sdlp_send_soar_note_to_dlp",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1646686889367,
      "name": "Symantec DLP: Send SOAR Note to DLP",
      "object_type": "note",
      "programmatic_name": "sdlp_send_soar_note_to_dlp",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "6e3f7a89-e689-448d-ad08-ed3c8f1988fc",
      "workflow_id": 605
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_resolve_incident_in_dlp",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_resolve_incident_in_dlp\" isExecutable=\"true\" name=\"Symantec DLP:  Resolve Incident in DLP\"\u003e\u003cdocumentation\u003eResolve an incident in Symantec DLP.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0npzznd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0npzznd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_09iby9q\"/\u003e\u003cendEvent id=\"EndEvent_1pbf5bg\"\u003e\u003cincoming\u003eSequenceFlow_1qrl10d\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_09iby9q\" name=\"Symantec DLP: Update Incident Sta...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"dd70d539-26fb-40fb-8b8c-92afba3cb3f8\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nsdlp_incident_id = content.get(\\\"sdlp_incident_id\\\", None)\\nif success:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Resolve Incident in DLP\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentId {0} Resolved.\u0027.format(sdlp_incident_id)\\nelse:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Resolve Incident in DLP\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentId {0}: check the status in Symantec DLP.\u0027.format(sdlp_incident_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_status = \\\"Resolved\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0npzznd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qrl10d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qrl10d\" sourceRef=\"ServiceTask_09iby9q\" targetRef=\"EndEvent_1pbf5bg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0npzznd\" id=\"SequenceFlow_0npzznd_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"240.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1pbf5bg\" id=\"EndEvent_1pbf5bg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"700\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"718\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_09iby9q\" id=\"ServiceTask_09iby9q_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qrl10d\" id=\"SequenceFlow_1qrl10d_di\"\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"700\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"586.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "Resolve an incident in Symantec DLP.",
      "export_key": "sdlp_resolve_incident_in_dlp",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1648228545671,
      "name": "Symantec DLP:  Resolve Incident in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_resolve_incident_in_dlp",
      "tags": [],
      "uuid": "d0d48db3-c9dd-4561-955a-82a935e8d74f",
      "workflow_id": 624
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "sdlp_update_incident_status",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_update_incident_status\" isExecutable=\"true\" name=\"Symantec DLP: Update Incident Status in DLP\"\u003e\u003cdocumentation\u003eUpdate the DLP incident status in DLP.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1hgy1g1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hgy1g1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_085sbtd\"/\u003e\u003cendEvent id=\"EndEvent_0gmht6l\"\u003e\u003cincoming\u003eSequenceFlow_062edc4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_085sbtd\" name=\"Symantec DLP: Update Incident Sta...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4258886f-e439-41f2-9679-864a3d291add\"\u003e{\"inputs\":{\"79413c7b-ad2f-4149-a97b-dd6a70e72afe\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"dd70d539-26fb-40fb-8b8c-92afba3cb3f8\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nsdlp_incident_id = content.get(\\\"sdlp_incident_id\\\", None)\\nsdlp_incident_status = content.get(\\\"sdlp_incident_status\\\", None)\\nif success:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident Status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; DLP incident {0} status set to: {1}.\u0027.format(sdlp_incident_id, sdlp_incident_status)\\nelse:\\n  noteText = u\u0027\u0026lt;b\u0026gt;Symantec DLP: Update Incident Status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;Error: Check DLP incidentId {0} status in Symantec DLP.\u0027.format(sdlp_incident_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sdlp_incident_status = rule.properties.sdlp_incident_status\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1hgy1g1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_062edc4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_062edc4\" sourceRef=\"ServiceTask_085sbtd\" targetRef=\"EndEvent_0gmht6l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hgy1g1\" id=\"SequenceFlow_1hgy1g1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"278\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gmht6l\" id=\"EndEvent_0gmht6l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"784\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"802\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_085sbtd\" id=\"ServiceTask_085sbtd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"448\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_062edc4\" id=\"SequenceFlow_062edc4_di\"\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"784\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"666\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Update the DLP incident status in DLP.",
      "export_key": "sdlp_update_incident_status",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1646686889271,
      "name": "Symantec DLP: Update Incident Status in DLP",
      "object_type": "incident",
      "programmatic_name": "sdlp_update_incident_status",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "6347ccec-1997-4af5-a798-702609486951",
      "workflow_id": 604
    },
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "sdlp_upload_binaries",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_upload_binaries\" isExecutable=\"true\" name=\"Symantec DLP: Upload Binaries\"\u003e\u003cdocumentation\u003eGet the binary files associated with a DLP incident and upload to the corresponding IBM SOAR case as artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0u9x6bq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0y2wmdt\"\u003e\u003cincoming\u003eSequenceFlow_1e1upjv\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0r6tnd5\" name=\"Symantec DLP: Upload Binaries\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64c9eafd-e365-4b8b-ba61-33aa6010c601\"\u003e{\"inputs\":{},\"post_processing_script\":\"sdlp_inputs = results.get(\\\"inputs\\\")\\nsdlp_incident_id = sdlp_inputs.get(\\\"sdlp_incident_id\\\")\\n\\nnote = u\\\"\u0026lt;b\u0026gt;Symantec DLP: Upload Binaries for incident Id {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\".format(sdlp_incident_id)\\ncontent = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\")\\nif success:\\n  artifact_list = content.get(\u0027artifact_name_list\u0027)\\n  num_artifacts = len(artifact_list)\\n  note = u\\\"{0} {1} artifact files added\\\".format(note, num_artifacts)\\nelse:\\n  note = u\\\"{0} artifact NOT added\\\".format(note)\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sdlp_incident_id = incident.properties.sdlp_incident_id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0u9x6bq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e1upjv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0u9x6bq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0r6tnd5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1e1upjv\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"EndEvent_0y2wmdt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_09o1nkq\"\u003e\u003ctext\u003e\u003c![CDATA[Input: Symantec DLP incident Id, SOAR case id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0k77hge\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"TextAnnotation_09o1nkq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0i0mox2\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Symantec DLP incident files addesd as artifact files in SOAR; result written to a SOAR note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0j0ewky\" sourceRef=\"ServiceTask_0r6tnd5\" targetRef=\"TextAnnotation_0i0mox2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y2wmdt\" id=\"EndEvent_0y2wmdt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"811\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"829\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0r6tnd5\" id=\"ServiceTask_0r6tnd5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"447\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u9x6bq\" id=\"SequenceFlow_0u9x6bq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"322.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e1upjv\" id=\"SequenceFlow_1e1upjv_di\"\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"811\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"679\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_09o1nkq\" id=\"TextAnnotation_09o1nkq_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"287\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0k77hge\" id=\"Association_0k77hge_di\"\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"83\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0i0mox2\" id=\"TextAnnotation_0i0mox2_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"579\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0j0ewky\" id=\"Association_0j0ewky_di\"\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"615\" xsi:type=\"omgdc:Point\" y=\"83\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "creator_id": "admin@example.com",
      "description": "Get the binary files associated with a DLP incident and upload to the corresponding IBM SOAR case as artifacts.",
      "export_key": "sdlp_upload_binaries",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1646686888987,
      "name": "Symantec DLP: Upload Binaries",
      "object_type": "incident",
      "programmatic_name": "sdlp_upload_binaries",
      "tags": [
        {
          "tag_handle": "fn_symantec_dlp",
          "value": null
        }
      ],
      "uuid": "18314a54-a9c0-49f7-b1f9-98af37c7ec7d",
      "workflow_id": 602
    }
  ],
  "workspaces": []
}
