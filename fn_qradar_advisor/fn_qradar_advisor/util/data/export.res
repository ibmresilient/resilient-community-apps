{
  "action_order": [],
  "actions": [
    {
      "automations": [
        {
          "scripts_to_run": "Create Artifact for QRadar Advisor Analysis Observable",
          "type": "run_script",
          "value": null
        }
      ],
      "conditions": [],
      "enabled": true,
      "export_key": "Create Artifact (QRadar Advisor Analysis)",
      "id": 199,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Create Artifact (QRadar Advisor Analysis)",
      "object_type": "qradar_advisor_observable",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "89557225-b234-4901-9ba2-9ef175528918",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [
        {
          "scripts_to_run": "Create Artifact for Watson Search with Local Context",
          "type": "run_script",
          "value": null
        }
      ],
      "conditions": [],
      "enabled": true,
      "export_key": "Create Artifact (Watson Search with Local Context)",
      "id": 200,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Create Artifact (Watson Search with Local Context)",
      "object_type": "qradar_advisor_observable_for_artifact",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "964a81b7-83be-4e72-942d-e4e3016ee2e3",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Map QRadar rule",
      "id": 201,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Map QRadar rule",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2db278bc-8a12-4e24-b57f-1541cbd762e1",
      "view_items": [],
      "workflows": [
        "qradar_advisor_map_rule"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "QRadar Advisor Offense Analysis",
      "id": 202,
      "logic_type": "all",
      "message_destinations": [],
      "name": "QRadar Advisor Offense Analysis",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "dc0fe48a-7172-4f5f-82c3-266505f44094",
      "view_items": [],
      "workflows": [
        "qradar_advisor_offense_analysis"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "DNS Name"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware MD5 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-1 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-256 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Watson Search",
      "id": 203,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Watson Search",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f43eedb1-388c-4b2f-8235-3a20b30a6409",
      "view_items": [],
      "workflows": [
        "qradar_advisor_quick_search"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "DNS Name"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware MD5 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-1 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-256 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "User Account"
        }
      ],
      "enabled": true,
      "export_key": "Watson Search with Local Context",
      "id": 204,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Watson Search with Local Context",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "347e9b3e-6ee3-4b76-8744-6efce24f0339",
      "view_items": [],
      "workflows": [
        "qradar_advisor_full_search"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1659105785178,
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
      "export_key": "__function/qradar_advisor_search_value",
      "hide_notification": false,
      "id": 642,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_advisor_search_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_advisor_search_value",
      "tooltip": "indicator to search, types include Domain Name, IP Address, hashes, URL, or user name.",
      "type_id": 11,
      "uuid": "d976e380-5864-4eb5-b096-51250a166982",
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
      "export_key": "__function/qradar_analysis_restart_if_existed",
      "hide_notification": false,
      "id": 643,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_analysis_restart_if_existed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_analysis_restart_if_existed",
      "tooltip": "restart the analysis if there is an existing result",
      "type_id": 11,
      "uuid": "eb4d07be-006d-41d9-9392-ed22cefff172",
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
      "export_key": "__function/qradar_advisor_result_stage",
      "hide_notification": false,
      "id": 645,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_advisor_result_stage",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_advisor_result_stage",
      "tooltip": "stage1(Local), stage2(Watson enriched), stage3(Expanded local context)",
      "type_id": 11,
      "uuid": "48819fe4-2c70-488a-9996-9581a81d886a",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "stage1",
          "properties": null,
          "uuid": "8c5ac94f-df6f-4247-9071-36eb3ff100a9",
          "value": 474
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "stage2",
          "properties": null,
          "uuid": "1a5d6dac-cc24-404c-a655-28bad64aa0a5",
          "value": 475
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "stage3",
          "properties": null,
          "uuid": "bee62681-b35f-4ff8-9c4f-52489e6920cf",
          "value": 476
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
      "export_key": "__function/qradar_offense_id",
      "hide_notification": false,
      "id": 644,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_offense_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_offense_id",
      "tooltip": "QRadar Offense ID",
      "type_id": 11,
      "uuid": "6ad482db-6291-4667-abe2-88f0d9f8e644",
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
      "export_key": "__function/qradar_rule_name",
      "hide_notification": false,
      "id": 646,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_rule_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_rule_name",
      "tooltip": "Name of QRadar rule",
      "type_id": 11,
      "uuid": "78a948ce-77d3-4bad-9b53-fe184925950e",
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
      "id": 630,
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
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "aedb7df6-642a-4438-824d-fe24be34cfc0",
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
      "export_key": "incident/qradar_rule",
      "hide_notification": false,
      "id": 631,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "qradar_rule",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "qradar_rule",
      "tooltip": "Name of a QRadar rule",
      "type_id": 0,
      "uuid": "f2a82adc-674c-4a0e-9fa0-0c97d9569c21",
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
      "export_key": "incident/mitre_tactic_name",
      "hide_notification": false,
      "id": 629,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mitre_tactic_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "MITRE tactic name",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "templates": [],
      "text": "MITRE ATT\u0026CK Tactic name",
      "tooltip": "MITRE ATT\u0026CK Tactic name",
      "type_id": 0,
      "uuid": "67773a55-452f-42fb-a9e9-4ae04710dfa9",
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
      "created_date": 1656531327547,
      "description": {
        "content": "Given a Resilient artifact, this function performs a Watson Search with Local Context (a QRadar Advisor full search) and returns Local, Watson enriched, or Expanded local context (default) results.",
        "format": "text"
      },
      "destination_handle": "fn_qradar_advisor",
      "display_name": "Watson Search with Local Context",
      "export_key": "qradar_advisor_full_search",
      "id": 137,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656531327586,
      "name": "qradar_advisor_full_search",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "3f733a87-6abb-41b6-ad67-1e06f076a8a0",
      "version": 1,
      "view_items": [
        {
          "content": "d976e380-5864-4eb5-b096-51250a166982",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48819fe4-2c70-488a-9996-9581a81d886a",
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
          "name": "Example of Watson Search with Local Context",
          "object_type": "artifact",
          "programmatic_name": "qradar_advisor_full_search",
          "tags": [
            {
              "tag_handle": "fn_qradar_advisor",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 164
        }
      ]
    },
    {
      "created_date": 1656531327604,
      "description": {
        "content": "Map rule to MITRE ATT\u0026CK tactic",
        "format": "text"
      },
      "destination_handle": "fn_qradar_advisor",
      "display_name": "QRadar Advisor Map Rule",
      "export_key": "qradar_advisor_map_rule",
      "id": 138,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656531327640,
      "name": "qradar_advisor_map_rule",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "f1dbf8b7-a5ed-45e4-b788-4edc49830993",
      "version": 1,
      "view_items": [
        {
          "content": "78a948ce-77d3-4bad-9b53-fe184925950e",
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
          "name": "Example of mapping QRadar Rule",
          "object_type": "incident",
          "programmatic_name": "qradar_advisor_map_rule",
          "tags": [
            {
              "tag_handle": "fn_qradar_advisor",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 161
        }
      ]
    },
    {
      "created_date": 1656531327656,
      "description": {
        "content": "Given a Resilient artifact, this function performs a QRadar Advisor analysis and returns Local, Watson enriched, or Expanded local context (default) results.",
        "format": "text"
      },
      "destination_handle": "fn_qradar_advisor",
      "display_name": "QRadar Advisor Offense Analysis",
      "export_key": "qradar_advisor_offense_analysis",
      "id": 139,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656531327693,
      "name": "qradar_advisor_offense_analysis",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "744e9c8b-f00f-4a71-9ae6-c3dde388d6fa",
      "version": 1,
      "view_items": [
        {
          "content": "6ad482db-6291-4667-abe2-88f0d9f8e644",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48819fe4-2c70-488a-9996-9581a81d886a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eb4d07be-006d-41d9-9392-ed22cefff172",
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
          "name": "Example of QRadar Advisor Offense Analysis",
          "object_type": "incident",
          "programmatic_name": "qradar_advisor_offense_analysis",
          "tags": [
            {
              "tag_handle": "fn_qradar_advisor",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 162
        }
      ]
    },
    {
      "created_date": 1656531327710,
      "description": {
        "content": "Given a Resilient artifact, this function performs a Watson Search (a QRadar Advisor quick search) and returns a summary.",
        "format": "text"
      },
      "destination_handle": "fn_qradar_advisor",
      "display_name": "Watson Search",
      "export_key": "qradar_advisor_quick_search",
      "id": 140,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656531327748,
      "name": "qradar_advisor_quick_search",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "beb212da-a0df-47e6-a88e-5990738a5fb9",
      "version": 1,
      "view_items": [
        {
          "content": "d976e380-5864-4eb5-b096-51250a166982",
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
          "name": "Example of Watson Search",
          "object_type": "artifact",
          "programmatic_name": "qradar_advisor_quick_search",
          "tags": [
            {
              "tag_handle": "fn_qradar_advisor",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 163
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 18,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1659105783785,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1659105783785,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "59a978ea-4e79-4718-8dea-0163f8f55d3c"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_qradar_advisor",
      "name": "fn_qradar_advisor",
      "programmatic_name": "fn_qradar_advisor",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "users": [],
      "uuid": "20c95fca-1ff4-468d-b1b0-d237ce9f1bc2"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1656531327108,
      "description": "Create an artifact for the selected observable.",
      "enabled": false,
      "export_key": "Create Artifact for QRadar Advisor Analysis Observable",
      "id": 9,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531327127,
      "name": "Create Artifact for QRadar Advisor Analysis Observable",
      "object_type": "qradar_advisor_observable",
      "playbook_handle": null,
      "programmatic_name": "create_artifact_for_qradar_advisor_analysis_observable",
      "script_text": "#\n# We create artifacts for those observables according to how they can be mapped to \n# Resilient default artifacts. If user has custom artifacts, and wants\n# to map them as well, please modify the following mapping dict. \n#\n# All the other observables without direct mapping, try to make decision depending\n# on the qradar_advisor_description of them. If not decision can be made, then \n# a String type artifact will be created.\n#\nmapping = {\n    \"domain-name\": \"DNS Name\",\n    \"domain\": \"DNS Name\",\n    \"EmailContent\": \"Email Body\",\n    \"ipv4-addr\": \"IP Address\",\n    \"malware\": \"Malware Family/Variant\",\n    \"url\": \"URL\",\n    \"identity\": \"User Account\"\n}\n\nartifact_description = \"QRadar Advisor Analysis observable\"\ntype = row.qradar_advisor_type\nif type in mapping:\n    incident.addArtifact(mapping[type], row.qradar_advisor_description, artifact_description)\nelse:\n    artifact_type = \"String\"\n    #\n    # if the type is \"file\", the description could be MD5 hash, SHA-256 hash, SHA-1.\n    # Distinguish them according to the length.\n    #\n    # Anything else is considered \"File Name\"\n    #\n    if type == \"file\":\n        if len(row.qradar_advisor_description) == 32:\n            artifact_type = \"Malware MD5 Hash\"\n        elif len(row.qradar_advisor_description) == 64:\n            artifact_type = \"Malware SHA-256 Hash\"\n        elif len(row.qradar_advisor_description) == 40:\n            artifact_type = \"Malware SHA-1 Hash\"\n        else:\n            artifact_type = \"File Name\"\n\n    incident.addArtifact(artifact_type, row.qradar_advisor_description, artifact_description)",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "f5081fce-e1cc-4665-a1fb-0747182d2ca2"
    },
    {
      "actions": [],
      "created_date": 1656531327150,
      "description": "Create an artifact for the selected row",
      "enabled": false,
      "export_key": "Create Artifact for Watson Search with Local Context",
      "id": 10,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531327168,
      "name": "Create Artifact for Watson Search with Local Context",
      "object_type": "qradar_advisor_observable_for_artifact",
      "playbook_handle": null,
      "programmatic_name": "create_artifact_for_watson_search_with_local_context",
      "script_text": "#\n# We create artifacts for those observables according to how they can be mapped to\n# Resilient default artifacts. If user has custom artifacts, and wants\n# to map them as well, please modify the following mapping dict.\n#\n# All the other observables without direct mapping, try to make decision depending\n# on the qradar_advisor_description of them. If not decision can be made, then\n# a String type artifact will be created.\n#\nmapping = {\n    \"domain-name\": \"DNS Name\",\n    \"domain\": \"DNS Name\",\n    \"EmailContent\": \"Email Body\",\n    \"ipv4-addr\": \"IP Address\",\n    \"malware\": \"Malware Family/Variant\",\n    \"url\": \"URL\",\n    \"identity\": \"User Account\"\n}\n\nartifact_description = \"Watson Search with Local Context observable\"\ntype = row.qradar_advisor_type\nif type in mapping:\n    incident.addArtifact(mapping[type], row.qradar_advisor_description, artifact_description)\nelse:\n    artifact_type = \"String\"\n    #\n    # if the type is \"file\", the description could be MD5 hash, SHA-256 hash, SHA-1.\n    # Distinguish them according to the length.\n    #\n    # Anything else is considered \"File Name\"\n    #\n    if type == \"file\":\n        if len(row.qradar_advisor_description) == 32:\n            artifact_type = \"Malware MD5 Hash\"\n        elif len(row.qradar_advisor_description) == 64:\n            artifact_type = \"Malware SHA-256 Hash\"\n        elif len(row.qradar_advisor_description) == 40:\n            artifact_type = \"Malware SHA-1 Hash\"\n        else:\n            artifact_type = \"File Name\"\n\n    incident.addArtifact(artifact_type, row.qradar_advisor_description, artifact_description)",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "34de392a-ac67-4fc1-a76a-a3a1ad9e49b9"
    }
  ],
  "server_version": {
    "build_number": 7583,
    "major": 44,
    "minor": 0,
    "version": "44.0.7583"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "QRadar Advisor analysis results",
      "export_key": "qradar_advisor_observable",
      "fields": {
        "qradar_advisor_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable/qradar_advisor_description",
          "hide_notification": false,
          "id": 632,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_description",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "observable description",
          "type_id": 1005,
          "uuid": "0e0c631c-e356-4b95-acdc-06fcedba08aa",
          "values": [],
          "width": 221
        },
        "qradar_advisor_relevance": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable/qradar_advisor_relevance",
          "hide_notification": false,
          "id": 633,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_relevance",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Relevance",
          "tooltip": "x_ibm_security_relevance from QRadar Advisor return",
          "type_id": 1005,
          "uuid": "3c03ed19-11b2-49c1-af72-e5c0cd069bdb",
          "values": [],
          "width": 125
        },
        "qradar_advisor_toxicity": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable/qradar_advisor_toxicity",
          "hide_notification": false,
          "id": 634,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_toxicity",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Toxicity",
          "tooltip": "x_ibm_security_toxicity from QRadar Advisor return",
          "type_id": 1005,
          "uuid": "24dcfd20-abc4-4aeb-86c6-02cf6927e648",
          "values": [],
          "width": 221
        },
        "qradar_advisor_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable/qradar_advisor_type",
          "hide_notification": false,
          "id": 635,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_type",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "observable type",
          "type_id": 1005,
          "uuid": "6831fbb9-b415-4bbb-8071-879e43302fc9",
          "values": [],
          "width": 222
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
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "qradar_advisor_observable",
      "uuid": "3f02d47b-d73c-4b48-8ee8-111b01e1d93a"
    },
    {
      "actions": [],
      "display_name": "Watson Search with Local Context results",
      "export_key": "qradar_advisor_observable_for_artifact",
      "fields": {
        "artifact_related": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/artifact_related",
          "hide_notification": false,
          "id": 636,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "artifact_related",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Artifact Searched",
          "tooltip": "artifact used to perform the Watson Search with Local Context",
          "type_id": 1006,
          "uuid": "94ae874c-a2d0-4792-aff9-31e0b099b167",
          "values": [],
          "width": 132
        },
        "full_search_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/full_search_time",
          "hide_notification": false,
          "id": 637,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "full_search_time",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Search Time",
          "tooltip": "time when search performed",
          "type_id": 1006,
          "uuid": "a74d7d4c-5831-4b4c-8c33-98360466a1c5",
          "values": [],
          "width": 111
        },
        "qradar_advisor_description": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/qradar_advisor_description",
          "hide_notification": false,
          "id": 638,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_description",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "observerable description",
          "type_id": 1006,
          "uuid": "5e29d17e-f07d-4474-bb42-c970addbf8af",
          "values": [],
          "width": 104
        },
        "qradar_advisor_relevance": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/qradar_advisor_relevance",
          "hide_notification": false,
          "id": 639,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_relevance",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Relevance",
          "tooltip": "x_ibm_security_relevance from QRadar Advisor return",
          "type_id": 1006,
          "uuid": "e35c0733-da0b-446b-a5fa-6a53c70dcfa7",
          "values": [],
          "width": 96
        },
        "qradar_advisor_toxicity": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/qradar_advisor_toxicity",
          "hide_notification": false,
          "id": 640,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_toxicity",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Toxicity",
          "tooltip": "x_ibm_security_toxicity from QRadar Advisor return",
          "type_id": 1006,
          "uuid": "8396d20c-75b3-4afc-b439-41a73bf28001",
          "values": [],
          "width": 90
        },
        "qradar_advisor_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "qradar_advisor_observable_for_artifact/qradar_advisor_type",
          "hide_notification": false,
          "id": 641,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "qradar_advisor_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "observable type",
          "type_id": 1006,
          "uuid": "bcc696cd-5e39-49f9-874d-41fea3c10630",
          "values": [],
          "width": 90
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
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "qradar_advisor_observable_for_artifact",
      "uuid": "9dff52d0-ac34-45a8-9f79-e4e42caa3b1c"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "qradar_advisor_map_rule",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_advisor_map_rule\" isExecutable=\"true\" name=\"Example of mapping QRadar Rule\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Map a QRadar rule to MITRE ATT\u0026CK tactic(s) using QRadar Advisor with Watson]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_175mg1b\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0t43aet\" name=\"QRadar Advisor Map Rule\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f1dbf8b7-a5ed-45e4-b788-4edc49830993\"\u003e{\"inputs\":{},\"post_processing_script\":\"tactics = results.tactics\\nmapping = tactics[\\\"mapping\\\"]\\natt_tactics = \\\", \\\".join(mapping.keys())\\nincident.properties.mitre_tactic_name = att_tactics\\n\",\"pre_processing_script\":\"inputs.qradar_rule_name = incident.properties.qradar_rule\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_175mg1b\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tnbp2z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_175mg1b\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0t43aet\"/\u003e\u003cendEvent id=\"EndEvent_1ivv81t\"\u003e\u003cincoming\u003eSequenceFlow_0tnbp2z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tnbp2z\" sourceRef=\"ServiceTask_0t43aet\" targetRef=\"EndEvent_1ivv81t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12uzu93\"\u003e\u003ctext\u003e\u003c![CDATA[Input:\nqradar_rule\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_19z7ncc\" sourceRef=\"ServiceTask_0t43aet\" targetRef=\"TextAnnotation_12uzu93\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1yo5it8\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nMITRE ATT\u0026CK tactic\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0bho8cu\" sourceRef=\"ServiceTask_0t43aet\" targetRef=\"TextAnnotation_1yo5it8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"187\" y=\"190\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"182\" y=\"225\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"191\" xsi:type=\"omgdc:Point\" y=\"219\"/\u003e\u003comgdi:waypoint x=\"160\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0t43aet\" id=\"ServiceTask_0t43aet_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"299\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_175mg1b\" id=\"SequenceFlow_175mg1b_di\"\u003e\u003comgdi:waypoint x=\"223\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003comgdi:waypoint x=\"299\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"216\" y=\"186.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ivv81t\" id=\"EndEvent_1ivv81t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"487\" y=\"190\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"505\" y=\"229\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tnbp2z\" id=\"SequenceFlow_0tnbp2z_di\"\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"208\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"398\" y=\"186.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12uzu93\" id=\"TextAnnotation_12uzu93_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"183\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_19z7ncc\" id=\"Association_19z7ncc_di\"\u003e\u003comgdi:waypoint x=\"311\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1yo5it8\" id=\"TextAnnotation_1yo5it8_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"401\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0bho8cu\" id=\"Association_0bho8cu_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"438\" xsi:type=\"omgdc:Point\" y=\"102\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Map a QRadar rule to MITRE ATT\u0026CK tactic(s) using QRadar Advisor with Watson",
      "export_key": "qradar_advisor_map_rule",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531328037,
      "name": "Example of mapping QRadar Rule",
      "object_type": "incident",
      "programmatic_name": "qradar_advisor_map_rule",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "2cb51368-2cdd-4266-9c4d-ac34f91b6292",
      "workflow_id": 161
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "qradar_advisor_offense_analysis",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_advisor_offense_analysis\" isExecutable=\"true\" name=\"Example of QRadar Advisor Offense Analysis\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Performs an offense analysis in QRadar Advisor. Results will populate a Data Table, create a Task, and generate a STIX representation in Notes.\nQRadar Advisor with Watson returns MITRE ATT\u0026CK tactic name.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0oqrvut\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_024fq4j\" name=\"QRadar Advisor Offense Analysis\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"744e9c8b-f00f-4a71-9ae6-c3dde388d6fa\"\u003e{\"inputs\":{\"48819fe4-2c70-488a-9996-9581a81d886a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"bee62681-b35f-4ff8-9c4f-52489e6920cf\"}},\"eb4d07be-006d-41d9-9392-ed22cefff172\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"#\\n# Result retured by the QRadar Advisor Offense Analysis function:\\n#   * results.observables: observables and their details, used here to be output to Data table.\\n#   * results.note: html representation of STIX data, used here to generate a Note.\\n#   * results.insights: used here to create a Task.\\n#   * results.stix: raw stix data, preserved for any customized parsing.\\n#\\n#   Note: results.insights can be a status code e.g. 404\\n#\\n# We publish a data table according to the stix\\n\\n# Check that we didn\u0027t get a status of 404 (no observables) for insights.\\nif \\\"status_code\\\" in results[\\\"insights\\\"] and results[\\\"insights\\\"][\\\"status_code\\\"] == 404:\\n    process_insights = False\\nelse:\\n    process_insights = True\\n\\nfor observable in results.observables:\\n  qradar_obs = incident.addRow(\\\"qradar_advisor_observable\\\")\\n  qradar_obs.qradar_advisor_toxicity = observable.toxicity\\n  qradar_obs.qradar_advisor_relevance = observable.relevance\\n  qradar_obs.qradar_advisor_type = observable.type\\n  qradar_obs.qradar_advisor_description = observable.description\\n\\n# Pass insights data (with MITRE ATTACK tactics information) to following function\\n# using workflow.properties.qraw_offense_insights. Refer to the Output tab please\\n\\n# Our STIX tree or error status.\\nhtml = helper.createRichText(results.note)\\nincident.addNote(html)\\n\\nif process_insights:\\n    # If we didn\u0027t get a 404 (no observables) status process for insights.\\n    # Task\\n    task_title = \\\"Review QRadar Advisor Analysis for Offense \\\" + str(incident.properties.qradar_id)\\n    task_summary = results.insights.insights + \\\"\\\\n\\\\n\\\" + results.insights.stage3_insights\\n    incident.addTask(task_title, \\\"Initial\\\", task_summary)\\n\\n    #\\n    # MITRE tactic information\\n    #\\n    tactics = results.insights[\\\"tactics\\\"]\\n\\n    mitre_tactic_names = []\\n    if tactics is not None:\\n      for tactic in tactics:\\n        #\\n        # Note, even though QRAW calls it tactic_id, it is more a tactic name\\n        #\\n        mitre_tactic_names.append(tactic[\\\"tactic_id\\\"])\\n    #\\n    # QRadar Advisor might return more than one tactics for a given offense. Include them inputs\\n    # a comma separated string\\n    #\\n    incident.properties.mitre_tactic_name = \\\", \\\".join(mitre_tactic_names)\\n\\n# Note that results.stix is the raw stix return from QRadar Advisor in stix 2 (json) format\\n# Users can add their customize codes to handle the stix data here\\n#\",\"pre_processing_script\":\"#\\n# This sample workflow uses the custom field (qradar_id) to perform \\n# an offense analysis in QRadar Advisor\\n#\\ninputs.qradar_offense_id = incident.properties.qradar_id\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0oqrvut\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t4jafu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0oqrvut\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_024fq4j\"/\u003e\u003cendEvent id=\"EndEvent_0epxc1j\"\u003e\u003cincoming\u003eSequenceFlow_1t4jafu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t4jafu\" sourceRef=\"ServiceTask_024fq4j\" targetRef=\"EndEvent_0epxc1j\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1f1d48b\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\nresults.observables\n\u2028results.note\u2028\nresults.insights\nresults.insights.tactics\n\u2028results.stix]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1hxl8ii\" sourceRef=\"ServiceTask_024fq4j\" targetRef=\"TextAnnotation_1f1d48b\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06k1jgt\"\u003e\u003ctext\u003e\u003c![CDATA[Input:\u00a0\n\u2028qradar_offense_id\u2028\nqradar_advisor_result_stage\u2028\nqradar_analysis_restart_if_existed]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0i2mo9y\" sourceRef=\"ServiceTask_024fq4j\" targetRef=\"TextAnnotation_06k1jgt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"274\" y=\"175\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"269\" y=\"210\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_024fq4j\" id=\"ServiceTask_024fq4j_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"396\" y=\"153\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0oqrvut\" id=\"SequenceFlow_0oqrvut_di\"\u003e\u003comgdi:waypoint x=\"310\" xsi:type=\"omgdc:Point\" y=\"193\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"193\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"308\" y=\"171.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1f1d48b\" id=\"TextAnnotation_1f1d48b_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"173\" x=\"506\" y=\"-8\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1hxl8ii\" id=\"Association_1hxl8ii_di\"\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"153\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"69\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06k1jgt\" id=\"TextAnnotation_06k1jgt_di\"\u003e\u003comgdc:Bounds height=\"73\" width=\"243\" x=\"146\" y=\"-6\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0i2mo9y\" id=\"Association_0i2mo9y_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"155\"/\u003e\u003comgdi:waypoint x=\"307\" xsi:type=\"omgdc:Point\" y=\"67\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0epxc1j\" id=\"EndEvent_0epxc1j_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"659.2844155844156\" y=\"175\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"677.2844155844156\" y=\"214\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t4jafu\" id=\"SequenceFlow_1t4jafu_di\"\u003e\u003comgdi:waypoint x=\"496\" xsi:type=\"omgdc:Point\" y=\"193\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"193\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"577.5\" y=\"171.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Performs an offense analysis in QRadar Advisor. Results will populate a Data Table, create a Task, and generate a STIX representation in Notes.\nQRadar Advisor with Watson returns MITRE ATT\u0026CK tactic name.",
      "export_key": "qradar_advisor_offense_analysis",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531328185,
      "name": "Example of QRadar Advisor Offense Analysis",
      "object_type": "incident",
      "programmatic_name": "qradar_advisor_offense_analysis",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "b110dc73-a9ff-4d21-8b6b-a9d4add4e00d",
      "workflow_id": 162
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "qradar_advisor_quick_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_advisor_quick_search\" isExecutable=\"true\" name=\"Example of Watson Search\"\u003e\u003cdocumentation\u003ePerforms a Watson Search (a quick search) of observables in QRadar Advisor. Results will be displayed in incident Notes. This sample workflow also creates artifacts for suspicious observables which can be mapped to Resilient artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0fttoak\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1b4w6ep\" name=\"Watson Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"beb212da-a0df-47e6-a88e-5990738a5fb9\"\u003e{\"inputs\":{},\"post_processing_script\":\"#\\n# Return data in this example\\n#   results.search_results.suspicious_observables:\\n#     Suspicious observables related to this indicator. Used in the post-process script to create artifacts,\\n#     if the type of the observable can be mapped to an default artifact type.\\n#\\n#  Note: results.return_search can have status code e.g. 422\\n#\\nreturn_search = results.search\\n\\nstatus_set = True if \\\"status_code\\\" in return_search else False\\nif not status_set:\\n    api_version = 2 if \\\"suspicious_observables\\\" in return_search.search_results else 1\\n\\n#\\n# Sample return json dict for v2.0\\n#\\n\u0027\u0027\u0027{\\n      \\\"search\\\": {\\n          \\\"search_value_type\\\": \\\"DomainName\\\", \\n          \\\"other_count\\\": 1, \\n          \\\"search_results\\\": {\\n          \\\"suspicious_observables\\\": [\\n                  {\\n                      \\\"reference_count\\\": 1, \\n                      \\\"timestamp\\\": 1529421998, \\n                      \\\"type\\\": \\\"DomainName\\\", \\n                      \\\"label\\\": \\\"mydomain.com\\\"\\n                  }, \\n                  {\\n                      \\\"reference_count\\\": 1, \\n                      \\\"timestamp\\\": 1462407300, \\n                      \\\"type\\\": \\\"EmailContent\\\", \\n                      \\\"label\\\": \\\"ccf2d5f4ab37650ccbb582f351aa6fdd:\\\"\\n                  }, \\n                  {\\n                      \\\"reference_count\\\": 1, \\n                      \\\"timestamp\\\": 1462407300, \\n                      \\\"type\\\": \\\"File\\\", \\n                      \\\"label\\\": \\\"ccf2d5f4ab37650ccbb582f351aa6fdd\\\"\\n                  }, \\n                  {\\n                      \\\"reference_count\\\": 1, \\n                      \\\"timestamp\\\": 1463566500, \\n                      \\\"type\\\": \\\"IpAddress\\\", \\n                      \\\"label\\\": \\\"190.104.198.116\\\"\\n                  },\\n                  {\\n                      \\\"reference_count\\\": 1, \\n                      \\\"timestamp\\\": 1463072400, \\n                      \\\"type\\\": \\\"Hash\\\", \\n                      \\\"label\\\": \\\"51417677b5e7b17542d383f5b25e2b43\\\"\\n                  }\\n          ], \\n          \\\"other_observables\\\": [\\n              {\\n                  \\\"reference_count\\\": 1, \\n                  \\\"timestamp\\\": 1529421998, \\n                  \\\"type\\\": \\\"DomainName\\\", \\n                  \\\"label\\\": \\\"mydomain.com\\\"\\n              }\\n          ]\\n      }, \\n      \\\"suspicious_count\\\": 5, \\n      \\\"search_value\\\": \\\"mydomain.com\\\", \\n      \\\"reference_count\\\": 1, \\n      \\\"is_toxic\\\": false}, \\n      \\\"whois\\\": {\\n          \\\"updated_date\\\": \\\"2015-09-15T23:25:25.000Z\\\", \\n          \\\"contact_country\\\": \\\"Canada\\\", \\n          \\\"registrar_name\\\": \\\"Domain.com, LLC\\\", \\n          \\\"contact_email\\\": \\\"noreply@data-protected.net\\\", \\n          \\\"created_date\\\": \\\"2000-06-22T04:00:00.000Z\\\", \\n          \\\"contact_name\\\": \\\"Data Protected Data Protected\\\", \\n          \\\"contact_type\\\": \\\"registrant\\\", \\\"contact_org\\\": \\\"Data Protected\\\"\\n      }\\n      }\\n\u0027\u0027\u0027\\n#\\n# We ONLY create artifacts for those observables that can be mapped to\\n# default Resilient artifacts. If customer has custom artifacts, and wants\\n# to map them as well, please modify the following mapping dict.\\n#\\nmapping = {\\n    \\\"DomainName\\\": \\\"DNS Name\\\",\\n    \\\"EmailContent\\\": \\\"Email Body\\\",\\n    \\\"File\\\": \\\"Malware MD5 Hash\\\",  # File type is a hash value. So we map File to Malware MD5 Hash\\n    \\\"IpAddress\\\": \\\"IP Address\\\",\\n    \\\"Hash\\\": {\\n        32: \\\"Malware MD5 Hash\\\",\\n        40: \\\"Malware SHA-1 Hash\\\",\\n        64: \\\"Malware SHA-256 Hash\\\"\\n    }\\n}\\n\\n#\\n# Note that in this example workflow, we only extract the suspicious_observables\\n#\\nif status_set:\\n    # Add an error status note.\\n    summary_string = \u0027The artifact returned an error.\u0027\\n    status_string = \\\"QRadar Advisor returned status code \u0027{}\u0027.\\\".format(return_search[\\\"status_code\\\"])\\n    if return_search[\\\"status_code\\\"] == 422:\\n        summary_string = \\\"This artifact has an unsupported value.\\\"\\n\\n    note_string = \\\"\u0026lt;h3\u0026gt;Watson Search Result Summary\u0026lt;/h3\u0026gt;\u0026lt;hr\u0026gt;\\\"\\n    note_string += \\\"\u0026lt;br\u0026gt;\u0026lt;p\u0026gt;\u0026lt;span style=\\\\\\\"font-weight:bold\\\\\\\"\u0026gt;\\\" + status_string + \\\"\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\\\"\\n    note_string += \\\"\u0026lt;p\u0026gt;\u0026lt;span style=\\\\\\\"font-weight:bold\\\\\\\"\u0026gt;\\\" + summary_string + \\\"\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\u0026lt;br\u0026gt;\\\"\\n    note_string +=  \\\"\u0026lt;p\u0026gt;Search Value: \\\" + return_search.search_value + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string +=  \\\"\u0026lt;p\u0026gt;Search Type:  \u0026lt;span style=\\\\\\\"color:white; border-bottom-left-radius: 2.96667px;background-color:#808080\\\\\\\"\u0026gt;\u0026amp;nbsp \\\" + artifact.type + \\\"\u0026amp;nbsp\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\\\"\\n    html_note = helper.createRichText(note_string)\\n    incident.addNote(html_note)\\n\\nelif api_version == 2:\\n    # v2.0\\n    suspicious_observables = return_search.search_results.suspicious_observables\\n\\n    new_artifact_count = 0\\n    summary_string = \\\"This artifact is not a suspicious observable\\\"\\n\\n    for observable in suspicious_observables:\\n        #\\n        # We support only those defined in mapping dict above\\n        #\\n        if observable.type in mapping:\\n            #\\n            # Note sometimes QRadar Advisor return the artifact itself as a suspicious observable. We don\u0027t want to\\n            # duplicate here.\\n            #\\n            if mapping[observable.type] != artifact.type or observable.label != artifact.value:\\n                new_artifact_count += 1\\n                if observable.type == \\\"Hash\\\":\\n                    if len(observable.label) in mapping[observable.type] and  observable.label.isalnum():\\n                        # Hash is likely MD5, SHA1 or SHA256.\\n                        incident.addArtifact(mapping[observable.type][len(observable.label)], observable.label,\\n                                             \\\"Watson Search result\\\")\\n                else:\\n                    incident.addArtifact(mapping[observable.type], observable.label, \\\"Watson Search result\\\")\\n            else:\\n                #\\n                # The artifact itself is a suspicious observable. We don\u0027t create new (duplicated) artifact. But we show this info\\n                #\\n                summary_string = \\\"This artifact is a suspicious observable\\\"\\n\\n    # Add a note about number of suspicious_observables\\n    note_string = \\\"\u0026lt;h3\u0026gt;Watson Search Result Summary\u0026lt;/h3\u0026gt;\u0026lt;hr\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;br\u0026gt;\u0026lt;p\u0026gt;\u0026lt;span style=\\\\\\\"font-weight:bold\\\\\\\"\u0026gt;\\\" + summary_string + \\\"\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\u0026lt;br\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Search Value: \\\" + return_search.search_value + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Search Type:  \u0026lt;span style=\\\\\\\"color:white; border-bottom-left-radius: 2.96667px;background-color:#808080\\\\\\\"\u0026gt;\u0026amp;nbsp \\\" + return_search.search_value_type + \\\"\u0026amp;nbsp\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p style=\\\\\\\"color:#FF00FF;\\\\\\\"\u0026gt;Suspicious observables: \\\" + str(\\n        return_search.suspicious_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p style=\\\\\\\"color:red;\\\\\\\"\u0026gt;New artifacts mapped from suspicious observables: \\\" + str(\\n        new_artifact_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Other observables: \\\" + str(return_search.other_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    html_note = helper.createRichText(note_string)\\n    incident.addNote(html_note)\\n\\nelse:\\n    # v1.0?\\n    new_artifact_count = 0\\n    toxic_count = 0\\n    non_toxic_count = 0\\n    summary_string = \\\"This artifact is not a suspicious observable\\\"\\n    for result in return_search.search_results:\\n        value_type = result[\\\"type\\\"]\\n        if value_type in mapping:\\n            #\\n            # We know what artifact type corresponds to this value type\\n            #\\n            for val in result[\\\"values\\\"]:\\n                #\\n                # We care about the toxic ones only\\n                #\\n                if val[\\\"is_toxic\\\"]:\\n                    toxic_count += 1\\n                    #\\n                    # Note sometimes QRadar Advisor return the artifact itself as a suspicious observable. We don\u0027t want to\\n                    # duplicate here.\\n                    #\\n                    if mapping[value_type] != artifact.type or val.label != artifact.value:\\n                        new_artifact_count += 1\\n                        if value_type == \\\"Hash\\\":\\n                            if len(val.label) in mapping[value_type] and  val.label.isalnum():\\n                                # Hash is likely MD5, SHA1 or SHA256.\\n                                incident.addArtifact(mapping[value_type][len(val.label)], val.label, \\\"Watson Search result\\\")\\n                        else:\\n                            incident.addArtifact(mapping[value_type], val.label, \\\"Watson Search result\\\")\\n                    else:\\n                        #\\n                        # The artifact itself is a suspicious observable. We don\u0027t create new (duplicated) artifact. But we show this info\\n                        #\\n                        summary_string = \\\"This artifact is a suspicious observable\\\"\\n                else:\\n                    non_toxic_count += 1\\n\\n    # Add a note about number of suspicious_observables\\n    note_string = \\\"\u0026lt;h3\u0026gt;Watson Search Result Summary\u0026lt;/h3\u0026gt;\u0026lt;hr\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;br\u0026gt;\u0026lt;p\u0026gt;\u0026lt;span style=\\\\\\\"font-weight:bold\\\\\\\"\u0026gt;\\\" + summary_string + \\\"\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\u0026lt;br\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Search Value: \\\" + return_search.search_value + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Search Type:  \u0026lt;span style=\\\\\\\"color:white; border-bottom-left-radius: 2.96667px;background-color:#808080\\\\\\\"\u0026gt;\u0026amp;nbsp \\\" + return_search.search_value_type + \\\"\u0026amp;nbsp\u0026lt;/span\u0026gt;\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p style=\\\\\\\"color:#FF00FF;\\\\\\\"\u0026gt;Toxic observables: \\\" + str(toxic_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p style=\\\\\\\"color:red;\\\\\\\"\u0026gt;New artifacts mapped from toxic observables: \\\" + str(\\n        new_artifact_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    note_string = note_string + \\\"\u0026lt;p\u0026gt;Non toxic observables: \\\" + str(non_toxic_count) + \\\"\u0026lt;/p\u0026gt;\\\"\\n    html_note = helper.createRichText(note_string)\\n    incident.addNote(html_note)\\n\\n\\n\",\"pre_processing_script\":\"value = artifact.value\\ntype = artifact.type\\n\\n#\\n# Watson Search only supports 5 indicator types: IP Address, Hash, Domain, URL, Username. \\n# The \u201cuser:\u201d prefix needs to be added to a username search\\n#\\nmapping = {\\n  \\\"User Account\\\":\\\"user:\\\"       \\n}\\nprefix = \\\"\\\"\\nif type in mapping:\\n  prefix = mapping[type]\\n\\ninputs.qradar_advisor_search_value = prefix + value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fttoak\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01do7i3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fttoak\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1b4w6ep\"/\u003e\u003cendEvent id=\"EndEvent_16xtc8r\"\u003e\u003cincoming\u003eSequenceFlow_01do7i3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01do7i3\" sourceRef=\"ServiceTask_1b4w6ep\" targetRef=\"EndEvent_16xtc8r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_187tigx\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nresults.search_results.suspicious_observables\nresults.search_results.other_observables\nresults.search_results.whois: Returned from QRadar Advisor]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xzi71y\" sourceRef=\"ServiceTask_1b4w6ep\" targetRef=\"TextAnnotation_187tigx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0voqqky\"\u003e\u003ctext\u003e\u003c![CDATA[Input:\nqradar_advisor_search_value]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0tnepoo\" sourceRef=\"ServiceTask_1b4w6ep\" targetRef=\"TextAnnotation_0voqqky\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"260\" y=\"187\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"255\" y=\"222\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1b4w6ep\" id=\"ServiceTask_1b4w6ep_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"424\" y=\"165\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fttoak\" id=\"SequenceFlow_0fttoak_di\"\u003e\u003comgdi:waypoint x=\"296\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"315\" y=\"183.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16xtc8r\" id=\"EndEvent_16xtc8r_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"639\" y=\"187\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"657\" y=\"226\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01do7i3\" id=\"SequenceFlow_01do7i3_di\"\u003e\u003comgdi:waypoint x=\"524\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003comgdi:waypoint x=\"639\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"536.5\" y=\"183.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_187tigx\" id=\"TextAnnotation_187tigx_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"364\" x=\"513\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xzi71y\" id=\"Association_0xzi71y_di\"\u003e\u003comgdi:waypoint x=\"524\" xsi:type=\"omgdc:Point\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"617\" xsi:type=\"omgdc:Point\" y=\"134\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0voqqky\" id=\"TextAnnotation_0voqqky_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"223\" x=\"166\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0tnepoo\" id=\"Association_0tnepoo_di\"\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"325\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Performs a Watson Search (a quick search) of observables in QRadar Advisor. Results will be displayed in incident Notes. This sample workflow also creates artifacts for suspicious observables which can be mapped to Resilient artifacts.",
      "export_key": "qradar_advisor_quick_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531328342,
      "name": "Example of Watson Search",
      "object_type": "artifact",
      "programmatic_name": "qradar_advisor_quick_search",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "d973635c-d561-43dd-8563-32ea1a089dc5",
      "workflow_id": 163
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "qradar_advisor_full_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"qradar_advisor_full_search\" isExecutable=\"true\" name=\"Example of Watson Search with Local Context\"\u003e\u003cdocumentation\u003ePerforms a Watson Search with Local Context (a full search) of observables in QRadar Advisor. Results will populate a Data Table, create a Task, and generate a HTML representation of the STIX bundles in Notes.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0golowh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0uogka9\" name=\"Watson Search with Local Context\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3f733a87-6abb-41b6-ad67-1e06f076a8a0\"\u003e{\"inputs\":{\"48819fe4-2c70-488a-9996-9581a81d886a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"8c5ac94f-df6f-4247-9071-36eb3ff100a9\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\n# Return data of function Watson Search with Local Context:\\n#   * results.observables: observables and their details, used here to be output to Data table.\\n#   * results.note: html representation of STIX data, used here to generate a Note.\\n#   * results.summary: used here to create a Task.\\n#   * results.stix: raw stix data (not used here), for any customized parsing.\\n\\n# Check that we didn\u0027t get a status of 404 (no observables) for insights.\\nif \\\"status_code\\\" in results[\\\"stix\\\"] and results[\\\"stix\\\"][\\\"status_code\\\"] == 404:\\n    add_task = False\\nelse:\\n    add_task  = True\\n# We publish a data table according to the stix if obserables found.\\ndate_str = str(Date())\\nfor observable in results.observables:\\n  qradar_obs = incident.addRow(\\\"qradar_advisor_observable_for_artifact\\\")\\n  qradar_obs.qradar_advisor_toxicity = observable.toxicity \\n  qradar_obs.qradar_advisor_relevance = observable.relevance\\n  qradar_obs.qradar_advisor_type = observable.type \\n  qradar_obs.qradar_advisor_description = observable.description \\n  qradar_obs.artifact_related = artifact.value\\n  qradar_obs.full_search_time = date_str\\n# Our STIX tree or error message\\nhtml = helper.createRichText(results.note)\\nincident.addNote(html)\\n\\nif add_task:\\n    # Create a task\\n    incident.addTask(\\\"Review Watson Search with Local Context of artifact: \\\" + artifact.value, \\\"Initial\\\", results.summary)\",\"pre_processing_script\":\"value = artifact.value\\ntype = artifact.type\\n\\n#\\n# Watso Search with Local Context only supports 5 indicator types: IP Address, Hash, DomainName, URL, Username. \\n# The \u201cuser:\u201d prefix needs to be added to a username search.\\n#\\nmapping = {\\n  \\\"User Account\\\":\\\"user:\\\"       \\n}\\nprefix = \\\"\\\"\\nif type in mapping:\\n  prefix = mapping[type]\\n\\ninputs.qradar_advisor_search_value = prefix + value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0golowh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zgzph7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0golowh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0uogka9\"/\u003e\u003cendEvent id=\"EndEvent_1nvpztt\"\u003e\u003cincoming\u003eSequenceFlow_0zgzph7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0zgzph7\" sourceRef=\"ServiceTask_0uogka9\" targetRef=\"EndEvent_1nvpztt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16li1l5\"\u003e\u003ctext\u003e\u003c![CDATA[Input:\nqradar_advisor_search_value\nqradar_advisor_result_stage]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1hwl6s9\" sourceRef=\"ServiceTask_0uogka9\" targetRef=\"TextAnnotation_16li1l5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mnq562\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nresults.observables\nresults.note\nresults.summary\nresults.stix]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0l7sx8d\" sourceRef=\"ServiceTask_0uogka9\" targetRef=\"TextAnnotation_1mnq562\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"207\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"202\" y=\"240\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0uogka9\" id=\"ServiceTask_0uogka9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"385\" y=\"183\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0golowh\" id=\"SequenceFlow_0golowh_di\"\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"311\" y=\"216.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nvpztt\" id=\"EndEvent_1nvpztt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"630\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"603\" y=\"244\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zgzph7\" id=\"SequenceFlow_0zgzph7_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"545\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"545\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"630\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"515\" y=\"216.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16li1l5\" id=\"TextAnnotation_16li1l5_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"184\" x=\"178\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1hwl6s9\" id=\"Association_1hwl6s9_di\"\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"190\"/\u003e\u003comgdi:waypoint x=\"316\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mnq562\" id=\"TextAnnotation_1mnq562_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"161\" x=\"524\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0l7sx8d\" id=\"Association_0l7sx8d_di\"\u003e\u003comgdi:waypoint x=\"480\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"559\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Performs a Watson Search with Local Context (a full search) of observables in QRadar Advisor. Results will populate a Data Table, create a Task, and generate a HTML representation of the STIX bundles in Notes.",
      "export_key": "qradar_advisor_full_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656531328453,
      "name": "Example of Watson Search with Local Context",
      "object_type": "artifact",
      "programmatic_name": "qradar_advisor_full_search",
      "tags": [
        {
          "tag_handle": "fn_qradar_advisor",
          "value": null
        }
      ],
      "uuid": "eb61a94a-315d-4eaf-af8e-edd1adf476cb",
      "workflow_id": 164
    }
  ],
  "workspaces": []
}
