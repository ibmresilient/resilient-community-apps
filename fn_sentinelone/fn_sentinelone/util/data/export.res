{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connected"
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Abort Disk Scan",
      "id": 26,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Abort Disk Scan",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6f7ee9cc-5b4b-4027-8815-1c05ebc080be",
      "view_items": [],
      "workflows": [
        "sentinelone_abort_disk_scan"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinelone_agent_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinelone_threat_id",
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
      "enabled": true,
      "export_key": "SentinelOne: Add Agent to Data Table",
      "id": 17,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Add Agent to Data Table",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "07fecdc0-b5ab-4add-9e09-f43925d60db3",
      "view_items": [],
      "workflows": [
        "sentinelone_add_agent_to_data_table"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": 3,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": 1,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "disconnected"
        },
        {
          "evaluation_id": 2,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "disconnecting"
        }
      ],
      "custom_condition": "(1 OR 2) AND 3",
      "enabled": true,
      "export_key": "SentinelOne: Connect Agent to Network",
      "id": 22,
      "logic_type": "advanced",
      "message_destinations": [],
      "name": "SentinelOne: Connect Agent to Network",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4898f29e-fdaa-491a-827f-8e71ee4060dd",
      "view_items": [],
      "workflows": [
        "sentinelone_connect_to_network"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": 3,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": 1,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connected"
        },
        {
          "evaluation_id": 2,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connecting"
        }
      ],
      "custom_condition": "(1 OR 2) AND 3",
      "enabled": true,
      "export_key": "SentinelOne: Disconnect Agent From Network",
      "id": 23,
      "logic_type": "advanced",
      "message_destinations": [],
      "name": "SentinelOne: Disconnect Agent From Network",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2080f065-31d2-4ec8-acee-01819c1eba47",
      "view_items": [],
      "workflows": [
        "sentinelone_disconnect_from_network"
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
          "value": "Malware SHA-1 Hash"
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Get Hash Reputation",
      "id": 24,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Get Hash Reputation",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fecd3414-8c56-429f-bf86-1bcc4a1c60a0",
      "view_items": [],
      "workflows": [
        "sentinelone_get_hash_reputation"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connected"
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Initiate Disk Scan",
      "id": 25,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Initiate Disk Scan",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "004ab3f1-d69c-4569-9ed5-258566c4353e",
      "view_items": [],
      "workflows": [
        "sentinelone_initiate_disk_scan"
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
          "field_name": "incident.properties.sentinelone_incident_status",
          "method": "not_equals",
          "type": null,
          "value": "resolved"
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinelone_threat_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Resolve Threat in SentinelOne",
      "id": 33,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Resolve Threat in SentinelOne",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "5351fcb6-286a-4f56-8f9a-57d23c63be61",
      "view_items": [],
      "workflows": [
        "sentinelone_resolve_threat_in_sentinelone"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connected"
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Restart Agent",
      "id": 32,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Restart Agent",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8b4f71c7-d1ac-44e1-b671-353b8851e3d3",
      "view_items": [],
      "workflows": [
        "sentinelone_restart_agent"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "SentinelOne: Send Note to SentinelOne Threat",
      "id": 31,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Send Note to SentinelOne Threat",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "650ef131-7465-4c5d-bb13-f95dcc01d8e8",
      "view_items": [],
      "workflows": [
        "sentinelone_send_soar_note_to_sentinelone"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinelone_threat_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "From SentinelOne"
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
      "export_key": "SentinelOne: Send SOAR Note to SentinelOne",
      "id": 30,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Send SOAR Note to SentinelOne",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "38d3cd38-2b52-4022-84f0-66ae78ae3932",
      "view_items": [],
      "workflows": [
        "sentinelone_send_soar_note_to_sentinelone"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_is_active",
          "method": "equals",
          "type": null,
          "value": true
        },
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_network_status",
          "method": "equals",
          "type": null,
          "value": "connected"
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Shutdown Agent",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Shutdown Agent",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b676dd4b-34a4-4654-b9fc-81bb0397b2ef",
      "view_items": [],
      "workflows": [
        "sentinelone_shutdown_agent"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "SentinelOne: Update Agent in Data table",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Update Agent in Data table",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "eac968e2-9241-4c6d-8efe-94c6b9428a68",
      "view_items": [],
      "workflows": [
        "sentinelone_update_agent_in_data_table"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinelone_threat_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Update Analyst Verdict and Threat Status",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Update Analyst Verdict and Threat Status",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cb754769-4754-453e-804b-24b8582225c6",
      "view_items": [
        {
          "content": "be983a18-91f8-4dee-af60-26424dbb12dc",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f2ea0128-0bca-4556-8dd5-5a428ccd8fee",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "sentinelone_update_threat_status"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "SentinelOne: Update Notes from SentinelOne",
      "id": 20,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Update Notes from SentinelOne",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8bb75e7b-9cd3-43f3-be5d-7ed41615c3c7",
      "view_items": [],
      "workflows": [
        "sentinelone_update_notes_from_sentinelone"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "sentinelone_agents_dt.sentinelone_dt_agent_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "SentinelOne: Write Agent Details to Note",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Write Agent Details to Note",
      "object_type": "sentinelone_agents_dt",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e4a606cd-0c5b-4b47-a348-686a7a304159",
      "view_items": [],
      "workflows": [
        "sentinelone_write_agent_details_to_note"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "SentinelOne: Write Threat Details to Note",
      "id": 19,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Write Threat Details to Note",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8825ebb9-3adc-4931-bc4b-ee87770e3f37",
      "view_items": [],
      "workflows": [
        "sentinelone_write_threat_details_to_note"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1640187788290,
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
      "export_key": "__function/sentinelone_agent_id",
      "hide_notification": false,
      "id": 234,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_agent_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_agent_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
      "export_key": "__function/sentinelone_threat_analyst_verdict",
      "hide_notification": false,
      "id": 272,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_analyst_verdict",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_threat_analyst_verdict",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e0ed407a-e9e0-40f8-b46b-5167eab16a70",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "false_positive",
          "properties": null,
          "uuid": "55fe7fb5-9ad9-4588-bc2b-cac8cf797a2c",
          "value": 77
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "suspicious",
          "properties": null,
          "uuid": "9baf9f94-0df8-4ba6-9044-3fc2a443dbba",
          "value": 68
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "true_positive",
          "properties": null,
          "uuid": "19108977-afe9-48ba-84fc-baab792216f3",
          "value": 78
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "undefined",
          "properties": null,
          "uuid": "84ca083b-c0f4-4f3e-a5bd-da8a3420920f",
          "value": 70
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
      "export_key": "__function/sentinelone_threat_status",
      "hide_notification": false,
      "id": 274,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_threat_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e823e746-184b-4ae8-9b7e-ce7f6d99d19e",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "resolved",
          "properties": null,
          "uuid": "8e342407-677a-450f-b7d1-3cb9a231f2be",
          "value": 83
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "in_progress",
          "properties": null,
          "uuid": "ad4044bf-fc24-4296-9911-4a946a3363cd",
          "value": 84
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unresolved",
          "properties": null,
          "uuid": "e38a55ab-d981-4363-810c-2bf16d71fb91",
          "value": 85
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
      "export_key": "__function/sentinelone_threat_id",
      "hide_notification": false,
      "id": 265,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_threat_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f0f85d50-0f6e-4a99-9b5c-a568c69772ce",
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
      "export_key": "__function/sentinelone_hash",
      "hide_notification": false,
      "id": 270,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_hash",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_hash",
      "tooltip": "",
      "type_id": 11,
      "uuid": "43312564-a5a6-4694-9d9f-ec51b499f0d0",
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
      "export_key": "__function/sentinelone_note_text",
      "hide_notification": false,
      "id": 276,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_note_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sentinelone_note_text",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6972b6e9-61b0-4a23-97e3-c76230d12f2e",
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
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
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
      "export_key": "actioninvocation/sentinelone_threat_analyst_verdict",
      "hide_notification": false,
      "id": 271,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_analyst_verdict",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Analyst Verdict",
      "tooltip": "Select the SentinelOne incidentStatus",
      "type_id": 6,
      "uuid": "be983a18-91f8-4dee-af60-26424dbb12dc",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "true_positive",
          "properties": null,
          "uuid": "8a97f191-bba8-443c-b78a-2954565a1843",
          "value": 75
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "undefined",
          "properties": null,
          "uuid": "109497c4-f5cf-478f-9a43-0b4d56c1b28f",
          "value": 72
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "suspicious",
          "properties": null,
          "uuid": "ddac984b-45f6-42e3-863a-73943c0921e3",
          "value": 73
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "false_positive",
          "properties": null,
          "uuid": "731798a1-7411-4d74-a63e-30da703ecfd4",
          "value": 76
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
      "export_key": "actioninvocation/sentinelone_threat_status",
      "hide_notification": false,
      "id": 275,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Status",
      "tooltip": "",
      "type_id": 6,
      "uuid": "f2ea0128-0bca-4556-8dd5-5a428ccd8fee",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "resolved",
          "properties": null,
          "uuid": "8d998659-4b80-48a7-be8e-d4f87fec9f4a",
          "value": 86
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "in_progress",
          "properties": null,
          "uuid": "61b84d9b-1174-4a04-a9fd-de18f80cc53d",
          "value": 87
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unresolved",
          "properties": null,
          "uuid": "eccb70ea-fb46-43db-846c-ef751a756304",
          "value": 88
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
      "export_key": "incident/sentinelone_mitigation_status_description",
      "hide_notification": false,
      "id": 268,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_mitigation_status_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Sentinelone Mitigation Status Description",
      "tooltip": "",
      "type_id": 0,
      "uuid": "927a8e24-a2e8-436c-a335-abb65e714761",
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
      "export_key": "incident/sentinelone_threat_analyst_verdict",
      "hide_notification": false,
      "id": 273,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_analyst_verdict",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "close",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Sentinelone Threat Analyst Verdict",
      "tooltip": "SentinelOne threat analyst verdict",
      "type_id": 0,
      "uuid": "d377bf25-737a-44f4-924b-8c6531e62ceb",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "false_positive",
          "properties": null,
          "uuid": "79663344-be90-41da-8608-3ea99621f813",
          "value": 79
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "suspicious",
          "properties": null,
          "uuid": "368d2011-6ce0-460e-a7ee-195b7a9721e4",
          "value": 80
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "true_positive",
          "properties": null,
          "uuid": "82f19a63-c9a7-472f-a53e-b2c25bd3fcfd",
          "value": 81
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "undefined",
          "properties": null,
          "uuid": "e4b6021d-14ec-4aad-94dc-fe9d038d3471",
          "value": 82
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
      "export_key": "incident/sentinelone_confidence_level",
      "hide_notification": false,
      "id": 261,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_confidence_level",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Confidence Level",
      "tooltip": "",
      "type_id": 0,
      "uuid": "d88cd581-5fb3-4dce-8c97-42c5b391f72e",
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
      "export_key": "incident/sentinelone_incident_status",
      "hide_notification": false,
      "id": 259,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Incident Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "0d9638b2-0df7-4e20-bef5-627a3faf0aa3",
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
      "export_key": "incident/sentinelone_classification",
      "hide_notification": false,
      "id": 262,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_classification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Classification",
      "tooltip": "",
      "type_id": 0,
      "uuid": "1ab10e4d-aac6-45d8-a647-b83a1693d085",
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
      "export_key": "incident/sentinelone_threat_id",
      "hide_notification": false,
      "id": 257,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "3961faa6-c6d0-4a0e-8588-dcc011e53ce4",
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
      "export_key": "incident/sentinelone_threat_name",
      "hide_notification": false,
      "id": 258,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Name",
      "tooltip": "",
      "type_id": 0,
      "uuid": "3ace162b-9529-419b-b91f-52e23e20f3fc",
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
      "export_key": "incident/sentinelone_agent_id",
      "hide_notification": false,
      "id": 264,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_agent_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Agent Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "6b4ec4a9-2dc7-463a-aa64-d1bbfa36be43",
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
      "export_key": "incident/sentinelone_threat_overview_url",
      "hide_notification": false,
      "id": 260,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_threat_overview_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Threat Overview URL",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7c5a98c7-caeb-4b73-b90b-d89ad2731373",
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
      "export_key": "incident/sentinelone_mitigation_status",
      "hide_notification": false,
      "id": 263,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinelone_mitigation_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SentinelOne Mitigation Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7f0a4b98-9245-4f0f-9c2e-16095776795a",
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
      "created_date": 1637426331845,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Initiate a Full Disk Scan on an agent managed by SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Abort Disk Scan",
      "export_key": "sentinelone_abort_disk_scan",
      "id": 10,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637426508401,
      "name": "sentinelone_abort_disk_scan",
      "tags": [],
      "uuid": "25716252-8e8c-43a5-8dbb-f9137266bf70",
      "version": 2,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Abort Disk Scan",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_abort_disk_scan",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        }
      ]
    },
    {
      "created_date": 1635258648261,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Connect an endpoint managed by Sentinel to the network.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Connect to Network",
      "export_key": "sentinelone_connect_to_network",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1639509041630,
      "name": "sentinelone_connect_to_network",
      "tags": [],
      "uuid": "517e7712-cf4f-42da-91a2-06d028dad318",
      "version": 2,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Connect to Network",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_connect_to_network",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        }
      ]
    },
    {
      "created_date": 1637339322871,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Disconnect an endpoint managed by SentinelOne from the network.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Disconnect From Network",
      "export_key": "sentinelone_disconnect_from_network",
      "id": 7,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637424833117,
      "name": "sentinelone_disconnect_from_network",
      "tags": [],
      "uuid": "49a731e0-8b31-473a-9911-cccfb794e6c5",
      "version": 3,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Disconnect From Network",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_disconnect_from_network",
          "tags": [],
          "uuid": null,
          "workflow_id": 8
        }
      ]
    },
    {
      "created_date": 1636049666316,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get details of a SentinelOne managed agent.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Get Agent Details",
      "export_key": "sentinelone_get_agent_details",
      "id": 3,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637099899759,
      "name": "sentinelone_get_agent_details",
      "tags": [],
      "uuid": "3bc833b4-0545-4db6-8ede-515d7439279a",
      "version": 2,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Add Agent to Data Table",
          "object_type": "incident",
          "programmatic_name": "sentinelone_add_agent_to_data_table",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        },
        {
          "actions": [],
          "description": null,
          "name": "SentinelOne: Update Agent in Data Table",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_update_agent_in_data_table",
          "tags": [],
          "uuid": null,
          "workflow_id": 20
        },
        {
          "actions": [],
          "description": null,
          "name": "SentinelOne: Write Agent Details to Note",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_write_agent_details_to_note",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    },
    {
      "created_date": 1637345955050,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get the SentinelOne reputation of a hash.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Get Hash Reputation",
      "export_key": "sentinelone_get_hash_reputation",
      "id": 8,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637345955079,
      "name": "sentinelone_get_hash_reputation",
      "tags": [],
      "uuid": "1cace8fb-a62d-4c3c-859a-71ad12b6fb1a",
      "version": 1,
      "view_items": [
        {
          "content": "43312564-a5a6-4694-9d9f-ec51b499f0d0",
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
          "name": "SentinelOne: Get Hash Reputation",
          "object_type": "artifact",
          "programmatic_name": "sentinelone_get_hash_reputation",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        }
      ]
    },
    {
      "created_date": 1637158497307,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get the details of a threat detected by SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Get Threat Details",
      "export_key": "sentinelone_get_threat_details",
      "id": 4,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637158497334,
      "name": "sentinelone_get_threat_details",
      "tags": [],
      "uuid": "2a2f6e9e-0fda-428e-adc0-cf0e7ca833fd",
      "version": 1,
      "view_items": [
        {
          "content": "f0f85d50-0f6e-4a99-9b5c-a568c69772ce",
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
          "name": "SentinelOne: Write Threat Details to Note",
          "object_type": "incident",
          "programmatic_name": "sentinelone_write_threat_details_to_note",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        }
      ]
    },
    {
      "created_date": 1637424960559,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Initiate a Full Disk scan on an agent managed by SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Initiate Disk Scan",
      "export_key": "sentinelone_initiate_disk_scan",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637424960598,
      "name": "sentinelone_initiate_disk_scan",
      "tags": [],
      "uuid": "3e5cb5d4-87c1-4d55-bc4e-917ebe781e6f",
      "version": 1,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Initiate Disk Scan",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_initiate_disk_scan",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1638564342098,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Resolve (close) a threat in SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Resolve Threat in SentinelOne",
      "export_key": "sentinelone_resolve_threat_in_sentinelone",
      "id": 16,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1638564342125,
      "name": "sentinelone_resolve_threat_in_sentinelone",
      "tags": [],
      "uuid": "c7a26323-ba72-4ac7-a3fc-60b3abcfaca0",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
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
          "name": "SentinelOne: Resolve Threat in SentinelOne",
          "object_type": "incident",
          "programmatic_name": "sentinelone_resolve_threat_in_sentinelone",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1638480670981,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Restart a endpoint managed by SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Restart Agent",
      "export_key": "sentinelone_restart_agent",
      "id": 15,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1638480671013,
      "name": "sentinelone_restart_agent",
      "tags": [],
      "uuid": "e0b6e8bc-fd8f-4bc4-9131-8e49b07d9a7b",
      "version": 1,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Restart Agent",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_restart_agent",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1638223289421,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Send a note created in SOAR to corresponding SentinelOne threat.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Send SOAR Note to SentinelOne",
      "export_key": "sentinelone_send_soar_note_to_sentinelone",
      "id": 14,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1638223289453,
      "name": "sentinelone_send_soar_note_to_sentinelone",
      "tags": [],
      "uuid": "fbf44fc5-ae3d-4e67-ad31-1b79fd87bdb8",
      "version": 1,
      "view_items": [
        {
          "content": "f0f85d50-0f6e-4a99-9b5c-a568c69772ce",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6972b6e9-61b0-4a23-97e3-c76230d12f2e",
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
          "name": "SentinelOne: Send SOAR Note to SentinelOne",
          "object_type": "note",
          "programmatic_name": "sentinelone_send_soar_note_to_sentinelone",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1637428470950,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Shutdown an agent managed by SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Shutdown Agent",
      "export_key": "sentinelone_shutdown_agent",
      "id": 11,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637428519803,
      "name": "sentinelone_shutdown_agent",
      "tags": [],
      "uuid": "41479530-59cd-432f-bc33-562dad5322db",
      "version": 2,
      "view_items": [
        {
          "content": "dbfe950b-d843-4105-ae4d-a586a96850f8",
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
          "name": "SentinelOne: Shutdown Agent",
          "object_type": "sentinelone_agents_dt",
          "programmatic_name": "sentinelone_shutdown_agent",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        }
      ]
    },
    {
      "created_date": 1637247442131,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Query SentinelOne threat and add any new threat notes to the SOAR incident.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SentinelOne: Update Notes From SentinelOne",
      "export_key": "sentinelone_update_notes_from_sentinelone",
      "id": 5,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1637249850349,
      "name": "sentinelone_update_notes_from_sentinelone",
      "tags": [],
      "uuid": "351d4c78-2c26-40f5-889f-6111e408068d",
      "version": 3,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f0f85d50-0f6e-4a99-9b5c-a568c69772ce",
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
          "name": "SentinelOne: Update Notes from SentinelOne",
          "object_type": "incident",
          "programmatic_name": "sentinelone_update_notes_from_sentinelone",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        }
      ]
    },
    {
      "created_date": 1637589626382,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update the incidentStatus and analystVerdict of a threat in SentinelOne.",
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "Sentinelone: Update Threat Status",
      "export_key": "sentinelone_update_threat_status",
      "id": 13,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1639522246709,
      "name": "sentinelone_update_threat_status",
      "tags": [],
      "uuid": "174b4b88-28d3-4596-97af-abbb3aef87f3",
      "version": 3,
      "view_items": [
        {
          "content": "f0f85d50-0f6e-4a99-9b5c-a568c69772ce",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e823e746-184b-4ae8-9b7e-ce7f6d99d19e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e0ed407a-e9e0-40f8-b46b-5167eab16a70",
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
          "name": "Sentinelone: Update Threat Status",
          "object_type": "incident",
          "programmatic_name": "sentinelone_update_threat_status",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 206,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1640187786556,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1640187786556,
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
      "export_key": "fn_sentinelone",
      "name": "fn_sentinelone",
      "programmatic_name": "fn_sentinelone",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "8864c644-67aa-4bd4-a7d3-6e5896b469db"
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
  "types": [
    {
      "actions": [],
      "display_name": "SentinelOne Agent",
      "export_key": "sentinelone_agents_dt",
      "fields": {
        "sentinelone_dt_agent_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_agent_id",
          "hide_notification": false,
          "id": 233,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_agent_id",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Agent ID",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "e8372600-1df3-4733-b275-a9f74658970c",
          "values": [],
          "width": 167
        },
        "sentinelone_dt_agent_version": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_agent_version",
          "hide_notification": false,
          "id": 238,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_agent_version",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Agent Version",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "8707325d-aa16-4bb6-a742-d4587ac51310",
          "values": [],
          "width": 57
        },
        "sentinelone_dt_computername": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_computername",
          "hide_notification": false,
          "id": 228,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_computername",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Computer Name",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "e8d004b3-39ec-4767-87a2-27367bc38413",
          "values": [],
          "width": 115
        },
        "sentinelone_dt_created": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_created",
          "hide_notification": false,
          "id": 254,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_created",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Created At",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "1e88f49b-24aa-44c2-9963-b2c1d18b1100",
          "values": [],
          "width": 60
        },
        "sentinelone_dt_domain": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_domain",
          "hide_notification": false,
          "id": 251,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_domain",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Domain",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "d0c01b2f-0f5a-4dfd-a7b6-b1813ea12c08",
          "values": [],
          "width": 58
        },
        "sentinelone_dt_external_ip": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_external_ip",
          "hide_notification": false,
          "id": 232,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_external_ip",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "External IP",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "c3988494-c1bc-4005-9d46-8517ca9844c2",
          "values": [],
          "width": 115
        },
        "sentinelone_dt_is_active": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_is_active",
          "hide_notification": false,
          "id": 242,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_is_active",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Is Active",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "395881b2-6f1f-454b-899e-6213a6dea781",
          "values": [],
          "width": 48
        },
        "sentinelone_dt_network_status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_network_status",
          "hide_notification": false,
          "id": 244,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_network_status",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Network Status",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "625b9b90-d165-4080-974e-865494161ad6",
          "values": [],
          "width": 65
        },
        "sentinelone_dt_os_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_os_name",
          "hide_notification": false,
          "id": 239,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_os_name",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "OS Name",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "16d80cf7-2e5c-47f9-a2d9-f09dc7951471",
          "values": [],
          "width": 57
        },
        "sentinelone_dt_query_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_query_date",
          "hide_notification": false,
          "id": 235,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_query_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query Date",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "b0366df4-4468-4d36-98f1-cfe57e85844d",
          "values": [],
          "width": 146
        },
        "sentinelone_dt_registered": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_registered",
          "hide_notification": false,
          "id": 255,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_registered",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Registered At",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "7ddf1974-f240-4bd2-8f42-81bc524f244d",
          "values": [],
          "width": 82
        },
        "sentinelone_dt_site": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_site",
          "hide_notification": false,
          "id": 231,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_site",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Site",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "b93d1433-2287-4552-af23-c3bc270d5869",
          "values": [],
          "width": 115
        },
        "sentinelone_dt_threat_count": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_threat_count",
          "hide_notification": false,
          "id": 253,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_threat_count",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Threat Count",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "8da86dc1-3594-49a4-a301-59d69250fd05",
          "values": [],
          "width": 50
        },
        "sentinelone_dt_updated": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_updated",
          "hide_notification": false,
          "id": 267,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_updated",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Updated At",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "2e41b920-64c3-438f-83a2-ceaea5874f0e",
          "values": [],
          "width": 65
        },
        "sentinelone_dt_uuid": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinelone_agents_dt/sentinelone_dt_uuid",
          "hide_notification": false,
          "id": 240,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sentinelone_dt_uuid",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "UUID",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "00f07379-46bb-436e-b4c9-75ebac817760",
          "values": [],
          "width": 40
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
      "type_name": "sentinelone_agents_dt",
      "uuid": "fbddc8a9-d2f1-4852-9c0c-efa703999ca0"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "sentinelone_resolve_threat_in_sentinelone",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_resolve_threat_in_sentinelone\" isExecutable=\"true\" name=\"SentinelOne: Resolve Threat in SentinelOne\"\u003e\u003cdocumentation\u003eResolve a SentinelOne threat in SentinelOne.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0oxnyhc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0gs1feh\" name=\"SentinelOne: Resolve Threat in Se...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c7a26323-ba72-4ac7-a3fc-60b3abcfaca0\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nsuccess = content.get(\\\"success\\\", False)\\nthreat_id = content.get(\\\"threat_id\\\", None)\\nif success:\\n  noteText = u\u0027\u0026lt;b\u0026gt;SentinelOne: Resolve Threat in SentinelOne\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; threatId {0} resolved.\u0027.format(threat_id)\\nelse:\\n  noteText = u\u0027\u0026lt;b\u0026gt;SentinelOne: Resolve Threat in SentinelOne\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; threatId {0}: check analystVerdict and incidentStatus in SentinelOne.\u0027.format(threat_id)\\n\\nincident.addNote(noteText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0oxnyhc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_09btac1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0oxnyhc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gs1feh\"/\u003e\u003cendEvent id=\"EndEvent_1nb8ang\"\u003e\u003cincoming\u003eSequenceFlow_09btac1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_09btac1\" sourceRef=\"ServiceTask_0gs1feh\" targetRef=\"EndEvent_1nb8ang\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1azjj80\"\u003e\u003ctext\u003e\u003c![CDATA[Input: incident Id,\u00a0 analystVerdict in custom incident select field\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vyvd1b\" sourceRef=\"ServiceTask_0gs1feh\" targetRef=\"TextAnnotation_1azjj80\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1a2ckbm\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Incident note indicating\u00a0 status of resolving threat in SentinelOne\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1x240ir\" sourceRef=\"ServiceTask_0gs1feh\" targetRef=\"TextAnnotation_1a2ckbm\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gs1feh\" id=\"ServiceTask_0gs1feh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"463\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0oxnyhc\" id=\"SequenceFlow_0oxnyhc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"330.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nb8ang\" id=\"EndEvent_1nb8ang_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"806\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"824\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09btac1\" id=\"SequenceFlow_09btac1_di\"\u003e\u003comgdi:waypoint x=\"563\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"806\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"684.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1azjj80\" id=\"TextAnnotation_1azjj80_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"292\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vyvd1b\" id=\"Association_1vyvd1b_di\"\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"80\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1a2ckbm\" id=\"TextAnnotation_1a2ckbm_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"616\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1x240ir\" id=\"Association_1x240ir_di\"\u003e\u003comgdi:waypoint x=\"555\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"650\" xsi:type=\"omgdc:Point\" y=\"80\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "admin@example.com",
      "description": "Resolve a SentinelOne threat in SentinelOne.",
      "export_key": "sentinelone_resolve_threat_in_sentinelone",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1640121836528,
      "name": "SentinelOne: Resolve Threat in SentinelOne",
      "object_type": "incident",
      "programmatic_name": "sentinelone_resolve_threat_in_sentinelone",
      "tags": [],
      "uuid": "460cfc51-6df0-41dc-9a96-871bd40213d0",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "sentinelone_connect_to_network",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_connect_to_network\" isExecutable=\"true\" name=\"SentinelOne: Connect to Network\"\u003e\u003cdocumentation\u003eConnect a SentinelOne managed endpoint to the network.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_152nr8l\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0lgkwfc\" name=\"SentinelOne: Connect to Network\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"517e7712-cf4f-42da-91a2-06d028dad318\"\u003e{\"inputs\":{},\"post_processing_script\":\"so_inputs = results.get(\\\"inputs\\\")\\nagent_id = so_inputs.get(\\\"sentinelone_agent_id\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Connect to Network \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Agent Id: {0}\\\".format(agent_id)\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    if int(data.get(\\\"affected\\\")) \u0026lt;= 0:\\n      note = u\\\"{0} is NOT connected to network\\\".format(note)\\n    else:\\n      networkStatus = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=\\\"green\\\", status=\\\"connected\\\")\\n      row[\\\"sentinelone_dt_network_status\\\"] = helper.createRichText(networkStatus)\\n      note = u\\\"{0} is connected to network\\\".format(note)\\n  else:\\n    note = u\\\"{0} no data returned from function\\\".format(note)\\nelse:\\n    note = u\\\"{0} no content data returned from function\\\".format(note)  \\n\\nincident.addNote(helper.createRichText(note))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_152nr8l\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16w4ax5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_152nr8l\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0lgkwfc\"/\u003e\u003cendEvent id=\"EndEvent_0oiezap\"\u003e\u003cincoming\u003eSequenceFlow_16w4ax5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16w4ax5\" sourceRef=\"ServiceTask_0lgkwfc\" targetRef=\"EndEvent_0oiezap\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_057kvhr\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne agent Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rlypu2\" sourceRef=\"ServiceTask_0lgkwfc\" targetRef=\"TextAnnotation_057kvhr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0cyyxp1\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Operation status written to an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_08qgiy0\" sourceRef=\"ServiceTask_0lgkwfc\" targetRef=\"TextAnnotation_0cyyxp1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0lgkwfc\" id=\"ServiceTask_0lgkwfc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"502\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_152nr8l\" id=\"SequenceFlow_152nr8l_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"502\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"350\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0oiezap\" id=\"EndEvent_0oiezap_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"865\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"883\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16w4ax5\" id=\"SequenceFlow_16w4ax5_di\"\u003e\u003comgdi:waypoint x=\"602\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"865\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"733.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_057kvhr\" id=\"TextAnnotation_057kvhr_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"363\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rlypu2\" id=\"Association_0rlypu2_di\"\u003e\u003comgdi:waypoint x=\"514\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"75\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0cyyxp1\" id=\"TextAnnotation_0cyyxp1_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"631\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_08qgiy0\" id=\"Association_08qgiy0_di\"\u003e\u003comgdi:waypoint x=\"587\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"668\" xsi:type=\"omgdc:Point\" y=\"75\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "creator_id": "admin@example.com",
      "description": "Connect a SentinelOne managed endpoint to the network.",
      "export_key": "sentinelone_connect_to_network",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637429446995,
      "name": "SentinelOne: Connect to Network",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_connect_to_network",
      "tags": [],
      "uuid": "c6745c6a-3649-4941-91ed-7faca74c1de4",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "sentinelone_get_hash_reputation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_get_hash_reputation\" isExecutable=\"true\" name=\"SentinelOne: Get Hash Reputation\"\u003e\u003cdocumentation\u003eGet the SentinelOne hash reputation and write it to an incident note\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0iivrif\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0vq5g5p\" name=\"SentinelOne: Get Hash Reputation\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1cace8fb-a62d-4c3c-859a-71ad12b6fb1a\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Get Hash Reputation: \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\"\\ncontent = results.get(\\\"content\\\")\\ninputs = results.get(\\\"inputs\\\")\\nhash_value = inputs.get(\\\"sentinelone_hash\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    rank = data.get(\\\"rank\\\")\\n    note = u\\\"{0} Hash \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; has rank: \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;\\\".format(note, hash_value, rank)\\n  else:\\n    note = u\\\"{0} No data returned from function.\\\".format(note)\\nelse:\\n  note = u\\\"{0} No content data returned from function.\\\".format(note)\\n  \\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_hash = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0iivrif\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16y4mwp\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0iivrif\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0vq5g5p\"/\u003e\u003cendEvent id=\"EndEvent_0y97emz\"\u003e\u003cincoming\u003eSequenceFlow_16y4mwp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16y4mwp\" sourceRef=\"ServiceTask_0vq5g5p\" targetRef=\"EndEvent_0y97emz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0q96asw\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SHA1 artifact value\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14vfhl3\" sourceRef=\"ServiceTask_0vq5g5p\" targetRef=\"TextAnnotation_0q96asw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0venepz\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Hash reputation written to incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_01jksp4\" sourceRef=\"ServiceTask_0vq5g5p\" targetRef=\"TextAnnotation_0venepz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vq5g5p\" id=\"ServiceTask_0vq5g5p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"488\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0iivrif\" id=\"SequenceFlow_0iivrif_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"343\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y97emz\" id=\"EndEvent_0y97emz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"835.5527192008879\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"853.5527192008879\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16y4mwp\" id=\"SequenceFlow_16y4mwp_di\"\u003e\u003comgdi:waypoint x=\"588\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"836\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"712\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0q96asw\" id=\"TextAnnotation_0q96asw_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"352.5527192008879\" y=\"87.89345172031076\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14vfhl3\" id=\"Association_14vfhl3_di\"\u003e\u003comgdi:waypoint x=\"493\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0venepz\" id=\"TextAnnotation_0venepz_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"629.5527192008879\" y=\"88\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_01jksp4\" id=\"Association_01jksp4_di\"\u003e\u003comgdi:waypoint x=\"584\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "admin@example.com",
      "description": "Get the SentinelOne hash reputation and write it to an incident note",
      "export_key": "sentinelone_get_hash_reputation",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637351868871,
      "name": "SentinelOne: Get Hash Reputation",
      "object_type": "artifact",
      "programmatic_name": "sentinelone_get_hash_reputation",
      "tags": [],
      "uuid": "11832502-8bef-4835-af9b-2959de4fa14f",
      "workflow_id": 9
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "sentinelone_shutdown_agent",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_shutdown_agent\" isExecutable=\"true\" name=\"SentinelOne: Shutdown Agent\"\u003e\u003cdocumentation\u003eShutdown an agent managed by SentinelOne.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_125zuq2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0az74kj\"\u003e\u003cincoming\u003eSequenceFlow_0wb46ah\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0i7kabl\" name=\"SentinelOne: Shutdown Agent\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41479530-59cd-432f-bc33-562dad5322db\"\u003e{\"inputs\":{},\"post_processing_script\":\"so_inputs = results.get(\\\"inputs\\\")\\nagent_id = so_inputs.get(\\\"sentinelone_agent_id\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Shutdown Agent \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Agent Id: {0}\\\".format(agent_id)\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    if int(data.get(\\\"affected\\\")) \u0026lt;= 0:\\n      note = u\\\"{0} Agent was NOT shutdown.\\\".format(note)\\n    else:\\n      note = u\\\"{0} Agent shutdown initiated.\\\".format(note)\\n  else:\\n    note = u\\\"{0} Agent shutdown was NOT initiated. No \u0027data\u0027 returned from function\\\".format(note)\\nelse:\\n    note = u\\\"{0} Agent shutdown was NOT initiated. No content returned from function\\\".format(note)  \\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_125zuq2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wb46ah\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_125zuq2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0i7kabl\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0wb46ah\" sourceRef=\"ServiceTask_0i7kabl\" targetRef=\"EndEvent_0az74kj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nd17wv\"\u003e\u003ctext\u003eInput: SentinelOne agent Id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0czbhti\" sourceRef=\"ServiceTask_0i7kabl\" targetRef=\"TextAnnotation_1nd17wv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0siiam8\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Shutdown agent and write results to incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0cwbfgh\" sourceRef=\"ServiceTask_0i7kabl\" targetRef=\"TextAnnotation_0siiam8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0az74kj\" id=\"EndEvent_0az74kj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"881\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"899\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0i7kabl\" id=\"ServiceTask_0i7kabl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"471\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_125zuq2\" id=\"SequenceFlow_125zuq2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"334\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"334\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"471\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"349\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wb46ah\" id=\"SequenceFlow_0wb46ah_di\"\u003e\u003comgdi:waypoint x=\"571\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"725\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"725\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"881\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"740\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nd17wv\" id=\"TextAnnotation_1nd17wv_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"258\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0czbhti\" id=\"Association_0czbhti_di\"\u003e\u003comgdi:waypoint x=\"471\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"333\" xsi:type=\"omgdc:Point\" y=\"91\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0siiam8\" id=\"TextAnnotation_0siiam8_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"624\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0cwbfgh\" id=\"Association_0cwbfgh_di\"\u003e\u003comgdi:waypoint x=\"564\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"656\" xsi:type=\"omgdc:Point\" y=\"91\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "admin@example.com",
      "description": "Shutdown an agent managed by SentinelOne.",
      "export_key": "sentinelone_shutdown_agent",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637431765341,
      "name": "SentinelOne: Shutdown Agent",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_shutdown_agent",
      "tags": [],
      "uuid": "48b48656-df28-4440-a257-e823f27a3318",
      "workflow_id": 12
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "sentinelone_write_threat_details_to_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_write_threat_details_to_note\" isExecutable=\"true\" name=\"SentinelOne: Write Threat Details to Note\"\u003e\u003cdocumentation\u003eGet the SentinelOne agent details in JSON format and call the Convert JSON to rich text script to write the information to an incident note in formatted rich text.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bqckt2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ouy5q1\" name=\"SentinelOne: Get Threat Details\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2a2f6e9e-0fda-428e-adc0-cf0e7ca833fd\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nthreat_id = inputs.get(\\\"sentinelone_threat_id\\\")\\ncontent = results.get(\\\"content\\\")\\ndata = content.get(\\\"data\\\")\\n\\nheader = u\\\"SentinelOne Threat Id: {0} Details:\\\".format(threat_id)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": data,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_threat_id = incident.properties.sentinelone_threat_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bqckt2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1w5o9qx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bqckt2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ouy5q1\"/\u003e\u003cendEvent id=\"EndEvent_0ciyxw7\"\u003e\u003cincoming\u003eSequenceFlow_1gyrzj3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1w5o9qx\" sourceRef=\"ServiceTask_1ouy5q1\" targetRef=\"ScriptTask_12ygmx0\"/\u003e\u003cscriptTask id=\"ScriptTask_12ygmx0\" name=\"Convert JSON to rich text v1.1\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"874d929b-7b4c-4f47-983a-58295c93d6bf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1w5o9qx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gyrzj3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1gyrzj3\" sourceRef=\"ScriptTask_12ygmx0\" targetRef=\"EndEvent_0ciyxw7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ouy5q1\" id=\"ServiceTask_1ouy5q1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"397\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bqckt2\" id=\"SequenceFlow_1bqckt2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"252.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ciyxw7\" id=\"EndEvent_0ciyxw7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"864\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"882\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1w5o9qx\" id=\"SequenceFlow_1w5o9qx_di\"\u003e\u003comgdi:waypoint x=\"497\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"638\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"522.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_12ygmx0\" id=\"ScriptTask_12ygmx0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"638\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gyrzj3\" id=\"SequenceFlow_1gyrzj3_di\"\u003e\u003comgdi:waypoint x=\"738\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"864\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"801\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "admin@example.com",
      "description": "Get the SentinelOne agent details in JSON format and call the Convert JSON to rich text script to write the information to an incident note in formatted rich text.",
      "export_key": "sentinelone_write_threat_details_to_note",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637159538724,
      "name": "SentinelOne: Write Threat Details to Note",
      "object_type": "incident",
      "programmatic_name": "sentinelone_write_threat_details_to_note",
      "tags": [],
      "uuid": "bf4525a9-04e9-431e-b692-725d2c553903",
      "workflow_id": 5
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "sentinelone_send_soar_note_to_sentinelone",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_send_soar_note_to_sentinelone\" isExecutable=\"true\" name=\"SentinelOne: Send SOAR Note to SentinelOne\"\u003e\u003cdocumentation\u003eSend a note created in SOAR to the corresponding SentinelOne threat as a threat note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_05zx6xi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1g7oo5b\" name=\"SentinelOne: Send SOAR Note to Se...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fbf44fc5-ae3d-4e67-ad31-1b79fd87bdb8\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Import Date\\nfrom java.util import Date\\n\\n# Edit note in SOAR to indicate it was sent to SentinelOne\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to SentinelOne at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinelone_threat_id = incident.properties.sentinelone_threat_id\\ninputs.sentinelone_note_text = note.text.content\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_05zx6xi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zia1r9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_05zx6xi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1g7oo5b\"/\u003e\u003cendEvent id=\"EndEvent_0bgblmv\"\u003e\u003cincoming\u003eSequenceFlow_0zia1r9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0zia1r9\" sourceRef=\"ServiceTask_1g7oo5b\" targetRef=\"EndEvent_0bgblmv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0x10t8u\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs: SentinelOne threatId and SOAR note text\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0in84vi\" sourceRef=\"ServiceTask_1g7oo5b\" targetRef=\"TextAnnotation_0x10t8u\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05zm0rk\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Note in SOAR is updated with Sent to SentinelOne header and new threat note is created in SentinelOne\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ygjv30\" sourceRef=\"ServiceTask_1g7oo5b\" targetRef=\"TextAnnotation_05zm0rk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1g7oo5b\" id=\"ServiceTask_1g7oo5b_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"485.66363636363633\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05zx6xi\" id=\"SequenceFlow_05zx6xi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"342\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0bgblmv\" id=\"EndEvent_0bgblmv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"827\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"845\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zia1r9\" id=\"SequenceFlow_0zia1r9_di\"\u003e\u003comgdi:waypoint x=\"586\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"827\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"706.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0x10t8u\" id=\"TextAnnotation_0x10t8u_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"327\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0in84vi\" id=\"Association_0in84vi_di\"\u003e\u003comgdi:waypoint x=\"494\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"393\" xsi:type=\"omgdc:Point\" y=\"75\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05zm0rk\" id=\"TextAnnotation_05zm0rk_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"646\" y=\"67\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ygjv30\" id=\"Association_1ygjv30_di\"\u003e\u003comgdi:waypoint x=\"581\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"677\" xsi:type=\"omgdc:Point\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "admin@example.com",
      "description": "Send a note created in SOAR to the corresponding SentinelOne threat as a threat note.",
      "export_key": "sentinelone_send_soar_note_to_sentinelone",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1638901106037,
      "name": "SentinelOne: Send SOAR Note to SentinelOne",
      "object_type": "note",
      "programmatic_name": "sentinelone_send_soar_note_to_sentinelone",
      "tags": [],
      "uuid": "0796ef56-507b-435a-b8ea-b250221140f4",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "sentinelone_update_threat_status",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_update_threat_status\" isExecutable=\"true\" name=\"Sentinelone: Update Threat Status\"\u003e\u003cdocumentation\u003eUpdate the Incident Status and Analyst Verdict of a threat in SentinelOne.  Write the results to a notes.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0t9fo6f\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1fdhas1\"\u003e\u003cincoming\u003eSequenceFlow_1tsktpi\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_15m2r9i\" name=\"Sentinelone: Update Threat Status\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"174b4b88-28d3-4596-97af-abbb3aef87f3\"\u003e{\"inputs\":{\"e823e746-184b-4ae8-9b7e-ce7f6d99d19e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"8e342407-677a-450f-b7d1-3cb9a231f2be\"}},\"e0ed407a-e9e0-40f8-b46b-5167eab16a70\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"55fe7fb5-9ad9-4588-bc2b-cac8cf797a2c\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\nthreat_id = content.get(\\\"threat_id\\\")\\nsuccess_verdict = content.get(\\\"success_verdict\\\")\\nsuccess_status = content.get(\\\"success_status\\\")\\nstatus = content.get(\\\"threat_status\\\")\\nverdict = content.get(\\\"threat_analyst_verdict\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Update Threat Status \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Threat Id: {0}\u0026lt;br\u0026gt;\\\".format(threat_id)\\ncontent = results.get(\\\"content\\\")\\nif success_verdict and success_status:\\n  note = u\\\"{0} analystVerdict set to \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentStatus set to \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; in SentinelOne\\\".format(note, verdict, status)\\nelif success_verdict:\\n  note = u\\\"{0} analystVerdict set to \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; incidentStatus was NOT set to {2} in SentinelOne\\\".format(note, verdict, status)\\nelif success_status:\\n  note = u\\\"{0} incidentStatus set to \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; analystVerdict was NOT set to {2} in SentinelOne\\\".format(note, status, verdict)\\nelse:\\n  note = u\\\"{0} analystVerdict: \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; and incidentStatus: \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; were NOT set in SentinelOne\\\".format(note, verdict, status)\\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_threat_id = incident.properties.sentinelone_threat_id\\ninputs.sentinelone_threat_status = rule.properties.sentinelone_threat_status\\ninputs.sentinelone_threat_analyst_verdict = rule.properties.sentinelone_threat_analyst_verdict\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0t9fo6f\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tsktpi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0t9fo6f\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_15m2r9i\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1tsktpi\" sourceRef=\"ServiceTask_15m2r9i\" targetRef=\"EndEvent_1fdhas1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0opn7vx\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne Threat Id, analystVerdict, incidentStatus\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ogl4g2\" sourceRef=\"ServiceTask_15m2r9i\" targetRef=\"TextAnnotation_0opn7vx\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1fdhas1\" id=\"EndEvent_1fdhas1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"899\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"917\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0opn7vx\" id=\"TextAnnotation_0opn7vx_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"367\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_15m2r9i\" id=\"ServiceTask_15m2r9i_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"477\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t9fo6f\" id=\"SequenceFlow_0t9fo6f_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"337\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"337\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"477\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"352\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tsktpi\" id=\"SequenceFlow_1tsktpi_di\"\u003e\u003comgdi:waypoint x=\"577\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"899\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"738\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ogl4g2\" id=\"Association_0ogl4g2_di\"\u003e\u003comgdi:waypoint x=\"489\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"85\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "admin@example.com",
      "description": "Update the Incident Status and Analyst Verdict of a threat in SentinelOne.  Write the results to a notes.",
      "export_key": "sentinelone_update_threat_status",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1639594120990,
      "name": "Sentinelone: Update Threat Status",
      "object_type": "incident",
      "programmatic_name": "sentinelone_update_threat_status",
      "tags": [],
      "uuid": "3d226ac0-ea1b-4c3f-8398-f5cd59817d8f",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "sentinelone_abort_disk_scan",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_abort_disk_scan\" isExecutable=\"true\" name=\"SentinelOne: Abort Disk Scan\"\u003e\u003cdocumentation\u003eAbort a Full Disk Scan on an agent managed by SentinelOne.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t7v72t\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0az74kj\"\u003e\u003cincoming\u003eSequenceFlow_1nor60t\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_127884f\" name=\"SentinelOne: Abort Disk Scan\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"25716252-8e8c-43a5-8dbb-f9137266bf70\"\u003e{\"inputs\":{},\"post_processing_script\":\"so_inputs = results.get(\\\"inputs\\\")\\nagent_id = so_inputs.get(\\\"sentinelone_agent_id\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Abort Full Disk Scan \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Agent Id: {0}\\\".format(agent_id)\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    if int(data.get(\\\"affected\\\")) \u0026lt;= 0:\\n      note = u\\\"{0} Full Disk Scan was NOT aborted.\\\".format(note)\\n    else:\\n      note = u\\\"{0} Full Disk Scan aborted.\\\".format(note)\\n  else:\\n    note = u\\\"{0} Full Disk Scan was NOT aborted. No \u0027data\u0027 returned from function\\\".format(note)\\nelse:\\n    note = u\\\"{0} Full Disk Scan was NOT aborted. No content returned from function\\\".format(note)  \\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t7v72t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nor60t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t7v72t\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_127884f\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1nor60t\" sourceRef=\"ServiceTask_127884f\" targetRef=\"EndEvent_0az74kj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18htrvk\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne agent Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003ctextAnnotation id=\"TextAnnotation_05s4y8s\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Disk scan initiated with result sent to an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0gi4coh\" sourceRef=\"ServiceTask_127884f\" targetRef=\"TextAnnotation_18htrvk\"/\u003e\u003cassociation id=\"Association_04qgm4c\" sourceRef=\"ServiceTask_127884f\" targetRef=\"TextAnnotation_05s4y8s\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0az74kj\" id=\"EndEvent_0az74kj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"881\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"899\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18htrvk\" id=\"TextAnnotation_18htrvk_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"291\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05s4y8s\" id=\"TextAnnotation_05s4y8s_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"654\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_127884f\" id=\"ServiceTask_127884f_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"488\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t7v72t\" id=\"SequenceFlow_1t7v72t_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"343\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nor60t\" id=\"SequenceFlow_1nor60t_di\"\u003e\u003comgdi:waypoint x=\"588\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"881\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"734.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0gi4coh\" id=\"Association_0gi4coh_di\"\u003e\u003comgdi:waypoint x=\"489\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"66\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_04qgm4c\" id=\"Association_04qgm4c_di\"\u003e\u003comgdi:waypoint x=\"586\" xsi:type=\"omgdc:Point\" y=\"159\"/\u003e\u003comgdi:waypoint x=\"653\" xsi:type=\"omgdc:Point\" y=\"63\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "admin@example.com",
      "description": "Abort a Full Disk Scan on an agent managed by SentinelOne.",
      "export_key": "sentinelone_abort_disk_scan",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637517728700,
      "name": "SentinelOne: Abort Disk Scan",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_abort_disk_scan",
      "tags": [],
      "uuid": "07ac8123-52cb-4a00-941b-6c100f880c04",
      "workflow_id": 11
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "sentinelone_update_notes_from_sentinelone",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_update_notes_from_sentinelone\" isExecutable=\"true\" name=\"SentinelOne: Update Notes from SentinelOne\"\u003e\u003cdocumentation\u003eQuery SentinelOne and add any new threat notes to the SOAR incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x8w1tj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1x8w1tj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0mcfhbm\"/\u003e\u003cendEvent id=\"EndEvent_0wzv9qx\"\u003e\u003cincoming\u003eSequenceFlow_06uuqvx\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0mcfhbm\" name=\"SentinelOne: Update Notes From Se...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"351d4c78-2c26-40f5-889f-6111e408068d\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sentinelone_threat_id = incident.properties.sentinelone_threat_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x8w1tj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06uuqvx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_06uuqvx\" sourceRef=\"ServiceTask_0mcfhbm\" targetRef=\"EndEvent_0wzv9qx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1g3t0v7\"\u003e\u003ctext\u003e\u003c![CDATA[Input: Incident Id and SentinelOne threat Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1kyrmqn\" sourceRef=\"ServiceTask_0mcfhbm\" targetRef=\"TextAnnotation_1g3t0v7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06qh3zq\"\u003e\u003ctext\u003e\u003c![CDATA[Output: new SentinelOne threat notes are added to SOAR incident notes\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_12wuqbb\" sourceRef=\"ServiceTask_0mcfhbm\" targetRef=\"TextAnnotation_06qh3zq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x8w1tj\" id=\"SequenceFlow_1x8w1tj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"305\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wzv9qx\" id=\"EndEvent_0wzv9qx_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"731\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"749\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0mcfhbm\" id=\"ServiceTask_0mcfhbm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"412\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06uuqvx\" id=\"SequenceFlow_06uuqvx_di\"\u003e\u003comgdi:waypoint x=\"512\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"731\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"621.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1g3t0v7\" id=\"TextAnnotation_1g3t0v7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"280\" y=\"28\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1kyrmqn\" id=\"Association_1kyrmqn_di\"\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"342\" xsi:type=\"omgdc:Point\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06qh3zq\" id=\"TextAnnotation_06qh3zq_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"517\" y=\"28\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_12wuqbb\" id=\"Association_12wuqbb_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"557\" xsi:type=\"omgdc:Point\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "admin@example.com",
      "description": "Query SentinelOne and add any new threat notes to the SOAR incident.",
      "export_key": "sentinelone_update_notes_from_sentinelone",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1638886730981,
      "name": "SentinelOne: Update Notes from SentinelOne",
      "object_type": "incident",
      "programmatic_name": "sentinelone_update_notes_from_sentinelone",
      "tags": [],
      "uuid": "1f0de141-0577-4456-83fc-8f93a1a9423a",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sentinelone_restart_agent",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_restart_agent\" isExecutable=\"true\" name=\"SentinelOne: Restart Agent\"\u003e\u003cdocumentation\u003eRestart an agent managed by SentinelOne.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lso1j4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_035fzn8\" name=\"SentinelOne: Restart Agent\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e0b6e8bc-fd8f-4bc4-9131-8e49b07d9a7b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.sentinelone_agent_id = incident.properties.sentinelone_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lso1j4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0gg9pna\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lso1j4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_035fzn8\"/\u003e\u003cendEvent id=\"EndEvent_1dqypwe\"\u003e\u003cincoming\u003eSequenceFlow_0gg9pna\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0gg9pna\" sourceRef=\"ServiceTask_035fzn8\" targetRef=\"EndEvent_1dqypwe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0psyphr\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne agent Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0g56u5b\" sourceRef=\"ServiceTask_035fzn8\" targetRef=\"TextAnnotation_0psyphr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_035fzn8\" id=\"ServiceTask_035fzn8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"408\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lso1j4\" id=\"SequenceFlow_1lso1j4_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"303\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1dqypwe\" id=\"EndEvent_1dqypwe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"739\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"757\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0gg9pna\" id=\"SequenceFlow_0gg9pna_di\"\u003e\u003comgdi:waypoint x=\"508\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"739\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"623.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0psyphr\" id=\"TextAnnotation_0psyphr_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"276\" y=\"43\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0g56u5b\" id=\"Association_0g56u5b_di\"\u003e\u003comgdi:waypoint x=\"422\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"73\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "Restart an agent managed by SentinelOne.",
      "export_key": "sentinelone_restart_agent",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1638481605076,
      "name": "SentinelOne: Restart Agent",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_restart_agent",
      "tags": [],
      "uuid": "86b83096-6d8e-4ccb-bb69-fd73f7776cd9",
      "workflow_id": 17
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "sentinelone_update_agent_in_data_table",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_update_agent_in_data_table\" isExecutable=\"true\" name=\"SentinelOne: Update Agent in Data Table\"\u003e\u003cdocumentation\u003eUpdate the agent details in the SentinelOne Agent data table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_085dfqw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1j5tpey\" name=\"SentinelOne: Get Agent Details\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3bc833b4-0545-4db6-8ede-515d7439279a\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Update Agent in Data Table: \u0026lt;/b\u0026gt; \\\\n\\\"\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    for agent in data:\\n      row.sentinelone_dt_query_date = Date()\\n      row.sentinelone_dt_agent_id = agent.get(\\\"id\\\")\\n      networkStatus = agent.get(\\\"networkStatus\\\")\\n      if networkStatus == \\\"connected\\\":\\n        display_color = \\\"green\\\"\\n      else:\\n        display_color = \\\"red\\\"\\n      networkStatus = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=display_color, status=networkStatus)\\n      row.sentinelone_dt_network_status = helper.createRichText(networkStatus)\\n      row.sentinelone_dt_computername = agent.get(\\\"computerName\\\")\\n      row.sentinelone_dt_external_ip = agent.get(\\\"externalIp\\\")\\n      row.sentinelone_dt_site = agent.get(\\\"siteName\\\")\\n      row.sentinelone_dt_agent_version = agent.get(\\\"agentVersion\\\")\\n      row.sentinelone_dt_threat_count = agent.get(\\\"activeThreats\\\")\\n      row.sentinelone_dt_domain = agent.get(\\\"domain\\\")\\n      row.sentinelone_dt_os_name = agent.get(\\\"osName\\\")\\n      row.sentinelone_dt_uuid = agent.get(\\\"uuid\\\")\\n      row.sentinelone_dt_is_active = agent.get(\\\"isActive\\\")\\n      row.sentinelone_dt_registered = agent.get(\\\"registeredAt\\\")\\n      row.sentinelone_dt_created = agent.get(\\\"createdAt\\\")\\n      row.sentinelone_dt_updated = agent.get(\\\"updatedAt\\\")\\n      note = u\\\"{0} success.\\\".format(note)\\n  else:\\n    note = u\\\"{0} No agent data returned from function.\\\".format(note)\\nelse:\\n  note = u\\\"{0} No content data returned from function.\\\".format(note)\\n  \\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = incident.properties.sentinelone_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_085dfqw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19idf8v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0va3o6q\"\u003e\u003cincoming\u003eSequenceFlow_19idf8v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_19idf8v\" sourceRef=\"ServiceTask_1j5tpey\" targetRef=\"EndEvent_0va3o6q\"/\u003e\u003csequenceFlow id=\"SequenceFlow_085dfqw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1j5tpey\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1j5tpey\" id=\"ServiceTask_1j5tpey_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"444\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0va3o6q\" id=\"EndEvent_0va3o6q_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"819\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"837\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19idf8v\" id=\"SequenceFlow_19idf8v_di\"\u003e\u003comgdi:waypoint x=\"544\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"819\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"681.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_085dfqw\" id=\"SequenceFlow_085dfqw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"321\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "admin@example.com",
      "description": "Update the agent details in the SentinelOne Agent data table.",
      "export_key": "sentinelone_update_agent_in_data_table",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1639683752185,
      "name": "SentinelOne: Update Agent in Data Table",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_update_agent_in_data_table",
      "tags": [],
      "uuid": "17e50d67-f695-456a-9c3b-3a4e122ec59a",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "sentinelone_disconnect_from_network",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_disconnect_from_network\" isExecutable=\"true\" name=\"SentinelOne: Disconnect From Network\"\u003e\u003cdocumentation\u003eDisconnect a SentinelOne managed endpoint from the network.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02en5qi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0oiezap\"\u003e\u003cincoming\u003eSequenceFlow_0qfre8i\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1dtzj1l\" name=\"SentinelOne: Disconnect From Netw...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"49a731e0-8b31-473a-9911-cccfb794e6c5\"\u003e{\"inputs\":{},\"post_processing_script\":\"so_inputs = results.get(\\\"inputs\\\")\\nagent_id = so_inputs.get(\\\"sentinelone_agent_id\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Disconnect From Network \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Agent Id: {0}\\\".format(agent_id)\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    if int(data.get(\\\"affected\\\")) \u0026lt;= 0:\\n      note = u\\\"{0} was not disconnected from network\\\".format(note)\\n    else:\\n      networkStatus = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=\\\"red\\\", status=\\\"disconnected\\\")\\n      row[\\\"sentinelone_dt_network_status\\\"] = helper.createRichText(networkStatus)      \\n      note = u\\\"{0} is disconnected from network\\\".format(note)\\n  else:\\n    note = u\\\"{0} no data returned from function\\\".format(note)\\nelse:\\n    note = u\\\"{0} no content data returned from function\\\".format(note)  \\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02en5qi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qfre8i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02en5qi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1dtzj1l\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0qfre8i\" sourceRef=\"ServiceTask_1dtzj1l\" targetRef=\"EndEvent_0oiezap\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0nw0h0n\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne agent Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1z0jm19\" sourceRef=\"ServiceTask_1dtzj1l\" targetRef=\"TextAnnotation_0nw0h0n\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_02j2c4w\"\u003e\u003ctext\u003eOutput: Operation status written to an incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0oz3896\" sourceRef=\"ServiceTask_1dtzj1l\" targetRef=\"TextAnnotation_02j2c4w\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0oiezap\" id=\"EndEvent_0oiezap_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"865\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"883\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1dtzj1l\" id=\"ServiceTask_1dtzj1l_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"481\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02en5qi\" id=\"SequenceFlow_02en5qi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"339.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qfre8i\" id=\"SequenceFlow_0qfre8i_di\"\u003e\u003comgdi:waypoint x=\"581\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"865\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"723\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0nw0h0n\" id=\"TextAnnotation_0nw0h0n_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"345\" y=\"60\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1z0jm19\" id=\"Association_1z0jm19_di\"\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"411\" xsi:type=\"omgdc:Point\" y=\"90\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_02j2c4w\" id=\"TextAnnotation_02j2c4w_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"641\" y=\"60\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0oz3896\" id=\"Association_0oz3896_di\"\u003e\u003comgdi:waypoint x=\"575\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"673\" xsi:type=\"omgdc:Point\" y=\"90\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "admin@example.com",
      "description": "Disconnect a SentinelOne managed endpoint from the network.",
      "export_key": "sentinelone_disconnect_from_network",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637429466103,
      "name": "SentinelOne: Disconnect From Network",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_disconnect_from_network",
      "tags": [],
      "uuid": "6efecc4e-9b8c-44b9-a44b-6cb78f69a0ac",
      "workflow_id": 8
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "sentinelone_add_agent_to_data_table",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_add_agent_to_data_table\" isExecutable=\"true\" name=\"SentinelOne: Add Agent to Data Table\"\u003e\u003cdocumentation\u003eAdd information from an agent managed by SentinelOne to the SentinelOne Agent data table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0xs67fy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0i9nhcf\" name=\"SentinelOne: Get Agent Details\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3bc833b4-0545-4db6-8ede-515d7439279a\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Add Agent to Data Table: \u0026lt;/b\u0026gt; \\\\n\\\"\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    data_len = len(data)\\n    note = u\\\"{0} {1} agent added to SentinelOne Agent data table.\\\".format(note, data_len)\\n    for agent in data:\\n      agent_row = incident.addRow(\\\"sentinelone_agents_dt\\\")\\n      agent_row.sentinelone_dt_query_date = Date()\\n      agent_row.sentinelone_dt_agent_id = agent.get(\\\"id\\\")\\n      networkStatus = agent.get(\\\"networkStatus\\\")\\n      if networkStatus == \\\"connected\\\":\\n        display_color = \\\"green\\\"\\n      else:\\n        display_color = \\\"red\\\"\\n      networkStatus = u\\\"\\\"\\\"\u0026lt;p style= \\\"color:{color}\\\"\u0026gt;{status}\u0026lt;/p\u0026gt;\\\"\\\"\\\".format(color=display_color, status=networkStatus)\\n      agent_row.sentinelone_dt_network_status = helper.createRichText(networkStatus)\\n      agent_row.sentinelone_dt_computername = agent.get(\\\"computerName\\\")\\n      agent_row.sentinelone_dt_external_ip = agent.get(\\\"externalIp\\\")\\n      agent_row.sentinelone_dt_site = agent.get(\\\"siteName\\\")\\n      agent_row.sentinelone_dt_agent_version = agent.get(\\\"agentVersion\\\")\\n      agent_row.sentinelone_dt_threat_count = agent.get(\\\"activeThreats\\\")\\n      agent_row.sentinelone_dt_domain = agent.get(\\\"domain\\\")\\n      agent_row.sentinelone_dt_os_name = agent.get(\\\"osName\\\")\\n      agent_row.sentinelone_dt_uuid = agent.get(\\\"uuid\\\")\\n      agent_row.sentinelone_dt_is_active = agent.get(\\\"isActive\\\")\\n      agent_row.sentinelone_dt_registered = agent.get(\\\"registeredAt\\\")\\n      agent_row.sentinelone_dt_created = agent.get(\\\"createdAt\\\")\\n      agent_row.sentinelone_dt_updated = agent.get(\\\"updatedAt\\\")\\n  else:\\n    note = u\\\"{0} No data returned from function.\\\".format(note)\\nelse:\\n  note = u\\\"{0} No content data returned from function.\\\".format(note)\\n  \\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = incident.properties.sentinelone_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xs67fy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06orzrw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xs67fy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0i9nhcf\"/\u003e\u003cendEvent id=\"EndEvent_1hac1ij\"\u003e\u003cincoming\u003eSequenceFlow_06orzrw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_06orzrw\" sourceRef=\"ServiceTask_0i9nhcf\" targetRef=\"EndEvent_1hac1ij\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0i9nhcf\" id=\"ServiceTask_0i9nhcf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"517\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xs67fy\" id=\"SequenceFlow_0xs67fy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"517\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"357.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1hac1ij\" id=\"EndEvent_1hac1ij_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"888\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"906\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06orzrw\" id=\"SequenceFlow_06orzrw_di\"\u003e\u003comgdi:waypoint x=\"617\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"888\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"752.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "creator_id": "admin@example.com",
      "description": "Add information from an agent managed by SentinelOne to the SentinelOne Agent data table.",
      "export_key": "sentinelone_add_agent_to_data_table",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1638486064817,
      "name": "SentinelOne: Add Agent to Data Table",
      "object_type": "incident",
      "programmatic_name": "sentinelone_add_agent_to_data_table",
      "tags": [],
      "uuid": "bb1dc479-5577-4699-b073-ffcac119edc5",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "sentinelone_initiate_disk_scan",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_initiate_disk_scan\" isExecutable=\"true\" name=\"SentinelOne: Initiate Disk Scan\"\u003e\u003cdocumentation\u003eInitiate a full disk scan on an agent managed by SentinelOne.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ndwwif\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1jg9a3c\" name=\"SentinelOne: Initiate Disk Scan\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3e5cb5d4-87c1-4d55-bc4e-917ebe781e6f\"\u003e{\"inputs\":{},\"post_processing_script\":\"so_inputs = results.get(\\\"inputs\\\")\\nagent_id = so_inputs.get(\\\"sentinelone_agent_id\\\")\\nnote = u\\\"\u0026lt;b\u0026gt;SentinelOne: Initiate Full Disk Scan \u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;  SentinelOne Agent Id: {0}\\\".format(agent_id)\\ncontent = results.get(\\\"content\\\")\\nif content:\\n  data = content.get(\\\"data\\\")\\n  if data:\\n    if int(data.get(\\\"affected\\\")) \u0026lt;= 0:\\n      note = u\\\"{0} Full Disk Scan was NOT initiated.\\\".format(note)\\n    else:\\n      note = u\\\"{0} Full Disk Scan initiated.\\\".format(note)\\n  else:\\n    note = u\\\"{0} Full Disk Scan was NOT initiated. No \u0027data\u0027 returned from function\\\".format(note)\\nelse:\\n    note = u\\\"{0} Full Disk Scan was NOT initiated. No content returned from function\\\".format(note)  \\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ndwwif\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1sxjobi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ndwwif\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1jg9a3c\"/\u003e\u003cendEvent id=\"EndEvent_0az74kj\"\u003e\u003cincoming\u003eSequenceFlow_1sxjobi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1sxjobi\" sourceRef=\"ServiceTask_1jg9a3c\" targetRef=\"EndEvent_0az74kj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18htrvk\"\u003e\u003ctext\u003e\u003c![CDATA[Input: SentinelOne agent Id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1w99o8g\" sourceRef=\"ServiceTask_1jg9a3c\" targetRef=\"TextAnnotation_18htrvk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05s4y8s\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Disk scan initiated with result sent to an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hqu1no\" sourceRef=\"ServiceTask_1jg9a3c\" targetRef=\"TextAnnotation_05s4y8s\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1jg9a3c\" id=\"ServiceTask_1jg9a3c_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"504\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ndwwif\" id=\"SequenceFlow_0ndwwif_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"504\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"351\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0az74kj\" id=\"EndEvent_0az74kj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"881\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"899\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1sxjobi\" id=\"SequenceFlow_1sxjobi_di\"\u003e\u003comgdi:waypoint x=\"604\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"881\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"742.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18htrvk\" id=\"TextAnnotation_18htrvk_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"300\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1w99o8g\" id=\"Association_1w99o8g_di\"\u003e\u003comgdi:waypoint x=\"509\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"370\" xsi:type=\"omgdc:Point\" y=\"66\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05s4y8s\" id=\"TextAnnotation_05s4y8s_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"654\" y=\"36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hqu1no\" id=\"Association_0hqu1no_di\"\u003e\u003comgdi:waypoint x=\"593\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"689\" xsi:type=\"omgdc:Point\" y=\"66\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "admin@example.com",
      "description": "Initiate a full disk scan on an agent managed by SentinelOne.",
      "export_key": "sentinelone_initiate_disk_scan",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637425592681,
      "name": "SentinelOne: Initiate Disk Scan",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_initiate_disk_scan",
      "tags": [],
      "uuid": "8112237e-9a84-4a77-961f-e299ffd948ea",
      "workflow_id": 10
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "sentinelone_write_agent_details_to_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_write_agent_details_to_note\" isExecutable=\"true\" name=\"SentinelOne: Write Agent Details to Note\"\u003e\u003cdocumentation\u003eGet the SentinelOne agent details in JSON format and call the Convert JSON to rich text script to write the information to an incident note in formatted rich text.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1svkmpo\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0f7rjj9\"\u003e\u003cincoming\u003eSequenceFlow_1e8ozvn\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1svkmpo\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0j6jsvr\"/\u003e\u003cserviceTask id=\"ServiceTask_0j6jsvr\" name=\"SentinelOne: Get Agent Details\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3bc833b4-0545-4db6-8ede-515d7439279a\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nagent_id = inputs.get(\\\"sentinelone_agent_id\\\")\\ncontent = results.get(\\\"content\\\")\\ndata = content.get(\\\"data\\\")\\n\\nheader = u\\\"SentinelOne Agent Id: {0} Details:\\\".format(agent_id)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": data,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1svkmpo\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_15uagt9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_0eb1rkd\" name=\"Convert JSON to rich text v1.1\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"874d929b-7b4c-4f47-983a-58295c93d6bf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15uagt9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e8ozvn\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1e8ozvn\" sourceRef=\"ScriptTask_0eb1rkd\" targetRef=\"EndEvent_0f7rjj9\"/\u003e\u003csequenceFlow id=\"SequenceFlow_15uagt9\" sourceRef=\"ServiceTask_0j6jsvr\" targetRef=\"ScriptTask_0eb1rkd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0f7rjj9\" id=\"EndEvent_0f7rjj9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"932\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"905\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1svkmpo\" id=\"SequenceFlow_1svkmpo_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"241.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0j6jsvr\" id=\"ServiceTask_0j6jsvr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"375\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0eb1rkd\" id=\"ScriptTask_0eb1rkd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"644.9570990806945\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e8ozvn\" id=\"SequenceFlow_1e8ozvn_di\"\u003e\u003comgdi:waypoint x=\"745\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"932\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"838.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15uagt9\" id=\"SequenceFlow_15uagt9_di\"\u003e\u003comgdi:waypoint x=\"475\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"645\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"560\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "admin@example.com",
      "description": "Get the SentinelOne agent details in JSON format and call the Convert JSON to rich text script to write the information to an incident note in formatted rich text.",
      "export_key": "sentinelone_write_agent_details_to_note",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1637159127620,
      "name": "SentinelOne: Write Agent Details to Note",
      "object_type": "sentinelone_agents_dt",
      "programmatic_name": "sentinelone_write_agent_details_to_note",
      "tags": [],
      "uuid": "345566e4-1715-42a2-9ffa-75f76840ca3f",
      "workflow_id": 3
    }
  ],
  "workspaces": []
}
