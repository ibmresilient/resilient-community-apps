{
  "action_order": [],
  "actions": [
    {
      "automations": [
        {
          "scripts_to_run": "Create Artifact from Indicator",
          "type": "run_script",
          "value": null
        }
      ],
      "conditions": [],
      "enabled": true,
      "export_key": "Create Artifact from Indicator",
      "id": 75,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Create Artifact from Indicator",
      "object_type": "defender_indicators",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b236d1f4-7fff-491f-8029-61ec317745f9",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.defender_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_id",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Defender Close Incident",
      "id": 70,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Close Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "a8896934-89ea-483c-833e-7d03f50c8da8",
      "view_items": [],
      "workflows": [
        "defender_close_incident"
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
            "DNS Name",
            "System Name"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Defender Find Machine by DNS name",
      "id": 76,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Find Machine by DNS name",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b718970d-69ac-4f45-b34c-5e5122d32ce9",
      "view_items": [],
      "workflows": [
        "defender_find_machines_by_filter"
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
            "Malware SHA-1 Hash",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Defender Find Machines by File Hash",
      "id": 78,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Find Machines by File Hash",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5e65eae4-994d-4115-9fb7-b250999e1c2b",
      "view_items": [],
      "workflows": [
        "defender_atp_find_machines_by_file_hash"
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
          "value": "IP Address"
        }
      ],
      "enabled": true,
      "export_key": "Defender Find Machines by Internal IP Address",
      "id": 77,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Find Machines by Internal IP Address",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a36f4ac6-4447-41c2-a56d-f088494bb3c2",
      "view_items": [
        {
          "content": "a3f841b9-37d8-4bc5-8f86-8492bd2f47ae",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_find_machines"
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
            "Malware SHA-1 Hash",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Defender Get File Information",
      "id": 79,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Get File Information",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fea94eb0-6acb-4cac-beab-c64785ef7b4c",
      "view_items": [],
      "workflows": [
        "defender_atp_get_file_information"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.defender_incident_id",
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
      "export_key": "Defender Get Incident",
      "id": 67,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Get Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "89236781-0126-426a-804a-09c63bc2749c",
      "view_items": [],
      "workflows": [
        "defender_get_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender List Indicators",
      "id": 80,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender List Indicators",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "00ce94b8-d948-4cf7-8dc2-9c814ab304f1",
      "view_items": [
        {
          "content": "a74dc1f0-4082-48cc-957c-c549bade783e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1e031f88-c36e-4891-a8f9-6af1b56a2340",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_list_indicators"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Machine App Execution Restriction",
      "id": 81,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine App Execution Restriction",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "66f07535-cdff-4d87-9314-69880b741675",
      "view_items": [
        {
          "content": "787f3150-c790-43d3-adf1-690262a675a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_app_execution"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Machine Collect Investigation Package",
      "id": 82,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Collect Investigation Package",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "661bbcf6-10a1-495b-bec3-d3e0f85c9a31",
      "view_items": [
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_collect_machine_investigation_package"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "defender_machines.machine_health_status",
          "method": "not_contains",
          "type": null,
          "value": "Isolate"
        }
      ],
      "enabled": true,
      "export_key": "Defender Machine Isolate Action",
      "id": 83,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Isolate Action",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ecefbfd0-e63f-4e9c-8ae8-ae9d11bd2551",
      "view_items": [
        {
          "content": "0a348890-61f2-4d94-8cb2-c06d9d882fee",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9986caf3-75f9-4ff6-b582-700ae7b96dd4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_machine_isolation"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "defender_machines.machine_file_hash",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Defender Machine Quarantine File",
      "id": 84,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Quarantine File",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c7bcd5a6-a26e-47b9-834b-917a9a888fd7",
      "view_items": [
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_quarantine_file"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Machine Refresh Information",
      "id": 71,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Refresh Information",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6260c178-3c4b-4110-8869-ca9fa5eb64a8",
      "view_items": [],
      "workflows": [
        "defender_get_updated_machine_information"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Machine Scan",
      "id": 85,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Scan",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7a5413a6-83b7-477e-afed-82ff31b6fef2",
      "view_items": [
        {
          "content": "62447aea-feec-4957-a9bc-b6f053e598d0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_machine_scan"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Defender Machine Update Information",
      "id": 74,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Update Information",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "1850772d-4a5c-487f-8fa4-9cea513523a2",
      "view_items": [],
      "workflows": [
        "defender_get_updated_machine_information"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Machine Vulnerabilities",
      "id": 86,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Machine Vulnerabilities",
      "object_type": "defender_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "10eb2d59-cdc6-4420-8f5f-632d675db062",
      "view_items": [],
      "workflows": [
        "defender_atp_machine_vulnerabilities"
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
            "URL",
            "Malware SHA-1 Hash",
            "System Name",
            "Malware SHA-256 Hash",
            "URL Referer"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Defender Set Indicator",
      "id": 87,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Set Indicator",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4fd3a0c6-e4e5-4b93-94e2-9c98f9ee588c",
      "view_items": [
        {
          "content": "db43862a-c62d-4603-988d-87e97971de94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c9dc15b-62d1-477f-8658-9fca2f1af24a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f4757460-b8e5-4342-9537-79c96c84060c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a0f0f7c1-b846-4d4c-a9ef-5ea6baa78912",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c17045e-f433-4fca-8b1d-c2c396413937",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_set_indicator"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.defender_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "Defender"
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
      "export_key": "Defender Sync Comment",
      "id": 72,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Sync Comment",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "8d7832f7-9fce-4b08-ac9f-4c90bb8b19c2",
      "view_items": [],
      "workflows": [
        "defender_sync_comment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": 1,
          "field_name": "incident.properties.defender_classification",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 2,
          "field_name": "incident.properties.defender_determination",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 4,
          "field_name": "incident.properties.defender_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 3,
          "field_name": "incident.properties.defender_tags",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "custom_condition": "(1 OR 2 OR 3) AND 4",
      "enabled": true,
      "export_key": "Defender Sync Incident",
      "id": 73,
      "logic_type": "advanced",
      "message_destinations": [],
      "name": "Defender Sync Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "d1350cc1-4c5a-41c6-9c95-ab1754be9b1a",
      "view_items": [],
      "workflows": [
        "defender_sync_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Defender Update Alert",
      "id": 88,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Defender Update Alert",
      "object_type": "defender_alerts",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ad59a4dc-3460-4066-a930-e02d3e3d7140",
      "view_items": [
        {
          "content": "76625936-c52e-43f1-a0f7-8e6bc6fe543d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cec88b1e-9664-40f9-a36e-b513466877d1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "33e170c3-ab00-495d-8111-a3108054d896",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b2be6546-e5f8-4b04-9c39-fb15c45ed119",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_update_alert"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "defender_indicators.status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Delete Indicator",
      "id": 89,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Delete Indicator",
      "object_type": "defender_indicators",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4c5c773a-5d76-47e0-b01f-ec17b36d72e1",
      "view_items": [],
      "workflows": [
        "defender_atp_delete_indicator"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "defender_indicators.status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Update Indicator",
      "id": 90,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Update Indicator",
      "object_type": "defender_indicators",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "27ab5187-5394-4054-a15b-e3ca430fcd0b",
      "view_items": [
        {
          "content": "f462026e-94c5-437a-b755-0548a61a2eea",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4d6a693c-5799-458f-9c6a-83b02d2798e8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a0f0f7c1-b846-4d4c-a9ef-5ea6baa78912",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c17045e-f433-4fca-8b1d-c2c396413937",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f4757460-b8e5-4342-9537-79c96c84060c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "defender_atp_update_indicator"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1636664050436,
  "export_format_version": 2,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/defender_indicator_field",
      "hide_notification": false,
      "id": 1756,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_field",
      "tooltip": "Select which field to filter on",
      "type_id": 11,
      "uuid": "83ef8d59-9b4a-405a-bc7b-2978a214bdbf",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "title",
          "properties": null,
          "uuid": "15ca01c7-cab9-44d7-b9b8-7506130a43f1",
          "value": 1332
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "description",
          "properties": null,
          "uuid": "bcde813c-bf09-49da-b6a4-29dd01a0016d",
          "value": 1333
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "type",
          "properties": null,
          "uuid": "b92ec055-4bb2-4d21-bb15-84462c944643",
          "value": 1334
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "value",
          "properties": null,
          "uuid": "187ffd72-c287-4d67-aac7-588c3e26c757",
          "value": 1335
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
      "export_key": "__function/defender_indicator_type",
      "hide_notification": false,
      "id": 1757,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "88321e50-32cb-4e44-8806-f1e72427c24f",
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
      "export_key": "__function/defender_alert_lastseen",
      "hide_notification": false,
      "id": 1758,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_lastseen",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_lastseen",
      "tooltip": "Last Seen Alert Date",
      "type_id": 11,
      "uuid": "953d2399-baa2-4a95-8d58-2e8045c92f9a",
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
      "export_key": "__function/defender_alert_lastupdatetime",
      "hide_notification": false,
      "id": 1759,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_lastupdatetime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_lastupdatetime",
      "tooltip": "Date when alert was last updated",
      "type_id": 11,
      "uuid": "97371dfb-d65d-46dc-8d4c-a98268da8f2f",
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
      "export_key": "__function/defender_alert_severity",
      "hide_notification": false,
      "id": 1760,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_severity",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_severity",
      "tooltip": "",
      "type_id": 11,
      "uuid": "aa552c13-07fb-438d-bff8-310eb7d20b4b",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Informational",
          "properties": null,
          "uuid": "d5adbe8b-ad0e-4ba5-8451-b9ab940d04bc",
          "value": 1336
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "5159f7f0-06b3-4d79-8e5e-f3cb7d6e3c4c",
          "value": 1337
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "d2422c96-a013-45de-aceb-a8a7349f9064",
          "value": 1338
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "049ee015-7508-404c-91e8-bf9f743a60af",
          "value": 1339
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
      "export_key": "__function/defender_comment",
      "hide_notification": false,
      "id": 1729,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_comment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b296aa20-606a-46c1-b1f9-b884d45f0e79",
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
      "export_key": "__function/defender_restriction_type",
      "hide_notification": false,
      "id": 1761,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_restriction_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_restriction_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b35bd7fe-d52a-483e-ab06-16f8131ce093",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "restrictCodeExecution",
          "properties": null,
          "uuid": "c099160c-f83c-461d-9b8e-4d0edd66716d",
          "value": 1340
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unrestrictCodeExecution",
          "properties": null,
          "uuid": "7db7f1de-6702-4b7a-82d4-6a4d7640c837",
          "value": 1341
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
      "export_key": "__function/defender_indicator_value",
      "hide_notification": false,
      "id": 1762,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "bdbb9226-ec7b-48be-ac04-ae19ddb32b27",
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
      "export_key": "__function/defender_indicator_id",
      "hide_notification": false,
      "id": 1763,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "bf1e212e-9f0d-4c67-9679-0792f1223b94",
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
      "export_key": "__function/defender_alert_status",
      "hide_notification": false,
      "id": 1764,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c0c321ad-ed0a-4a1c-b5b9-a8c7387c58b0",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "3745c47c-a066-41c2-b97a-7cf850e9022d",
          "value": 1342
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "InProgress",
          "properties": null,
          "uuid": "2fead575-cda4-4ea4-837c-73ff0563ec6a",
          "value": 1343
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "886a0494-0248-4ec7-9d97-d7e29f9369b7",
          "value": 1344
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
      "export_key": "__function/defender_alert_id",
      "hide_notification": false,
      "id": 1765,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c0d41921-0099-4e06-89de-4fbf3c3bda2c",
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
      "export_key": "__function/defender_machine_id",
      "hide_notification": false,
      "id": 1766,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_machine_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_machine_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
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
      "export_key": "__function/defender_indicator_action",
      "hide_notification": false,
      "id": 1767,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_action",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c8b53f87-e1f7-49df-bfaa-5c72c1168d69",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "AlertAndBlock",
          "properties": null,
          "uuid": "79c1a5bb-b168-4868-922b-54eb17365f9b",
          "value": 1345
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Alert",
          "properties": null,
          "uuid": "033f6c5f-2c30-4198-b2e2-6acec23f098e",
          "value": 1346
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Allowed",
          "properties": null,
          "uuid": "467cc7d9-b670-41cc-8b06-5f78c58a6806",
          "value": 1347
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
      "export_key": "__function/defender_machine_scantype",
      "hide_notification": false,
      "id": 1768,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_machine_scantype",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_machine_scantype",
      "tooltip": "antivirus scan type",
      "type_id": 11,
      "uuid": "d2234b4a-1677-42f9-89dc-a2dcca236948",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Full",
          "properties": null,
          "uuid": "f80596f3-dc40-4c52-a014-cf9cf299cc28",
          "value": 1348
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Quick",
          "properties": null,
          "uuid": "b2452a60-1ed2-4079-825f-36ec97fa5357",
          "value": 1349
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
      "export_key": "__function/defender_alert_assigned_to",
      "hide_notification": false,
      "id": 1769,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_assigned_to",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_assigned_to",
      "tooltip": "",
      "type_id": 11,
      "uuid": "da1c26a1-7ffb-4f65-a7a4-2566c2d5e34d",
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
      "export_key": "__function/defender_filter_value",
      "hide_notification": false,
      "id": 513,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_filter_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_filter_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ddce05a9-d22c-4cfd-9e89-e93c28cfc492",
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
      "export_key": "__function/defender_classification",
      "hide_notification": false,
      "id": 514,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_classification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_classification",
      "tooltip": "",
      "type_id": 11,
      "uuid": "dddcd251-6cb1-4fd7-a6a8-0f4890e87049",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FalsePositive",
          "properties": null,
          "uuid": "b8bef116-f5e1-4bbb-9dd8-cd28d4706b9d",
          "value": 254
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TruePositive",
          "properties": null,
          "uuid": "7f36b143-a289-47fe-a9f8-820d7cd48ec5",
          "value": 255
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "598b11a4-8620-413e-ac9a-153f82ed7a68",
          "value": 256
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
      "export_key": "__function/defender_filter_name",
      "hide_notification": false,
      "id": 515,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_filter_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_filter_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e13612f7-f7ed-45ce-b968-99a367f8d644",
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
      "export_key": "__function/defender_description",
      "hide_notification": false,
      "id": 1770,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
      "export_key": "__function/defender_incident_id",
      "hide_notification": false,
      "id": 1724,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "efad7afb-0fe3-4348-b7cb-1e5df5d57fc2",
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
      "export_key": "__function/defender_title",
      "hide_notification": false,
      "id": 1771,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_title",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f604d3fb-c665-4267-ae40-1049ff676bf0",
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
      "export_key": "__function/defender_determination",
      "hide_notification": false,
      "id": 518,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_determination",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_determination",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0b54ef2d-c209-479a-863a-46df39ec94e6",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apt",
          "properties": null,
          "uuid": "7f6c5ad6-f742-43db-b94c-4881d93b99da",
          "value": 257
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Malware",
          "properties": null,
          "uuid": "25fa890f-a5d4-4c4e-8ffe-952995924d24",
          "value": 258
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NotAvailable",
          "properties": null,
          "uuid": "d50a938b-b026-4810-8edb-df834410d842",
          "value": 259
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityPersonnel",
          "properties": null,
          "uuid": "b10f2592-a356-47d4-9b9f-73a2d3ee047c",
          "value": 260
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityTesting",
          "properties": null,
          "uuid": "6bbfbb7e-6e45-4f70-a280-32a2a8517be3",
          "value": 261
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UnwantedSoftware",
          "properties": null,
          "uuid": "940f2947-80ca-4234-8200-acdaead2dfdd",
          "value": 262
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other",
          "properties": null,
          "uuid": "a1a41080-48b7-43fb-baa4-b3e7bf55c1d6",
          "value": 263
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
      "export_key": "__function/defender_severity",
      "hide_notification": false,
      "id": 1772,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_severity",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_severity",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0e17bb0b-6ef9-4bac-b3d7-e5e37eaa7ffa",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Informational",
          "properties": null,
          "uuid": "d5d6f175-7b00-4d92-849a-0103cf35d819",
          "value": 1350
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "a3216414-9c8b-49d4-9714-2b728e14f8c5",
          "value": 1351
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "df8ae136-3508-4ac4-9024-1c8332fd4355",
          "value": 1352
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "f83f7a58-4542-4287-bde1-14c1e672e3d8",
          "value": 1353
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
      "export_key": "__function/defender_incident_status",
      "hide_notification": false,
      "id": 1728,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_incident_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "18d59d14-35ca-46e9-a571-2f0b0e45ff8a",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Active",
          "properties": null,
          "uuid": "d316fcc8-94b7-40b1-856f-b9408f8f78b0",
          "value": 1202
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "e39e7a5b-847c-4663-9ae1-e327fe16fb82",
          "value": 1203
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Redirected",
          "properties": null,
          "uuid": "1a8575ee-f45e-4ece-8c7d-3a65a90ccd35",
          "value": 1204
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
      "export_key": "__function/defender_lookback_timeframe",
      "hide_notification": false,
      "id": 1773,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_lookback_timeframe",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_lookback_timeframe",
      "tooltip": "This value must be within 30 days of current date",
      "type_id": 11,
      "uuid": "25fd039f-ed3a-4617-9944-b0cf6b937467",
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
      "export_key": "__function/defender_expiration_time",
      "hide_notification": false,
      "id": 1774,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_expiration_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_expiration_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2af4e75c-13d3-48cd-bd1d-1b159f607f48",
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
      "export_key": "__function/defender_isolation_type",
      "hide_notification": false,
      "id": 1775,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_isolation_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_isolation_type",
      "tooltip": "Type of operation to perform",
      "type_id": 11,
      "uuid": "46ccbdc2-0d49-4e72-9310-49494aa1d4e0",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Full",
          "properties": null,
          "uuid": "11fcc5e8-b795-4719-8320-c99d323d10a6",
          "value": 1354
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Selective",
          "properties": null,
          "uuid": "1a8355ed-cff5-40e4-9e54-da14d52c36b2",
          "value": 1355
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
      "export_key": "__function/defender_isolation_action",
      "hide_notification": false,
      "id": 1776,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_isolation_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_isolation_action",
      "tooltip": "\u0027isolate\u0027 or \u0027unisolate\u0027",
      "type_id": 11,
      "uuid": "4f112eb2-0f5e-44b4-a240-d2feca9189c9",
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
      "export_key": "__function/defender_alert_info",
      "hide_notification": false,
      "id": 1777,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_info",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_info",
      "tooltip": "",
      "type_id": 11,
      "uuid": "530a270d-338e-49e9-b877-3cfb5e89ecfa",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "All",
          "properties": null,
          "uuid": "4bd4b656-7e96-4b74-80a2-3f3df542dd73",
          "value": 1356
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Devices",
          "properties": null,
          "uuid": "2fa91a70-4289-41f7-a2c8-70cdf03e754f",
          "value": 1357
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domains",
          "properties": null,
          "uuid": "02444c38-d4d6-4f1b-ad20-406cdfe2239d",
          "value": 1358
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Files",
          "properties": null,
          "uuid": "29cdb10d-a50e-4876-bd29-ba58d31d86a0",
          "value": 1359
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "IPs",
          "properties": null,
          "uuid": "c28bbc5f-f262-4485-a600-f4fa9c2271d1",
          "value": 1360
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Users",
          "properties": null,
          "uuid": "2bbc3991-526b-4425-b8de-ffd18755f8e4",
          "value": 1361
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
      "export_key": "__function/defender_alert_result_max",
      "hide_notification": false,
      "id": 525,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_result_max",
      "operation_perms": {},
      "operations": [],
      "placeholder": "5",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_alert_result_max",
      "tooltip": "Number of top results to return",
      "type_id": 11,
      "uuid": "587375da-258c-475e-b4c9-61747f35ab59",
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
      "export_key": "__function/defender_indicator_filter",
      "hide_notification": false,
      "id": 1778,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_indicator_filter",
      "tooltip": "regex capability to limit list. ie: a.* for indicators starting with \u0027a\u0027",
      "type_id": 11,
      "uuid": "5a160310-4284-43fa-88b4-97bde9f7ce73",
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
      "export_key": "__function/defender_file_hash",
      "hide_notification": false,
      "id": 1779,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_file_hash",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_file_hash",
      "tooltip": "SHA1 or SHA256",
      "type_id": 11,
      "uuid": "615b32d0-ab72-48a0-a624-9043ff55dba2",
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
      "export_key": "__function/defender_tags",
      "hide_notification": false,
      "id": 1734,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "defender_tags",
      "tooltip": "comma separated list of defender incident tags",
      "type_id": 11,
      "uuid": "7bc628da-01e7-41b8-ac4e-6d029d7872aa",
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
      "export_key": "actioninvocation/indicator_expiration",
      "hide_notification": false,
      "id": 1740,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "indicator_expiration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Expiration",
      "tooltip": "",
      "type_id": 6,
      "uuid": "8c17045e-f433-4fca-8b1d-c2c396413937",
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
      "export_key": "actioninvocation/indicator_description",
      "hide_notification": false,
      "id": 1741,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "indicator_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Description",
      "tooltip": "",
      "type_id": 6,
      "uuid": "8c9dc15b-62d1-477f-8658-9fca2f1af24a",
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
      "export_key": "actioninvocation/defender_isolation_type",
      "hide_notification": false,
      "id": 1742,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_isolation_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Isolation Type",
      "tooltip": "Only used for Isolation actions",
      "type_id": 6,
      "uuid": "9986caf3-75f9-4ff6-b582-700ae7b96dd4",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Full",
          "properties": null,
          "uuid": "4a09abe7-82fc-4c36-89a6-12c899308965",
          "value": 1302
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Selective",
          "properties": null,
          "uuid": "36ecabaf-d0cf-4ab1-bb79-dafa4d1b90de",
          "value": 1303
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
      "export_key": "actioninvocation/indicator_action",
      "hide_notification": false,
      "id": 1743,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "indicator_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Action",
      "tooltip": "",
      "type_id": 6,
      "uuid": "a0f0f7c1-b846-4d4c-a9ef-5ea6baa78912",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "AlertAndBlock",
          "properties": null,
          "uuid": "73ea0e29-2c12-4fcf-8a85-85f597c0c59e",
          "value": 1304
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Alert",
          "properties": null,
          "uuid": "50a8596e-44ae-422d-a1e2-f0bf29baa3b3",
          "value": 1305
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Allowed",
          "properties": null,
          "uuid": "ba09782b-a7e7-4fd3-b283-8431fc80ec04",
          "value": 1306
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
      "export_key": "actioninvocation/defender_lookback_timeframe",
      "hide_notification": false,
      "id": 1744,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_lookback_timeframe",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Lookback Timeframe",
      "tooltip": "Date must be within 30 days of current date",
      "type_id": 6,
      "uuid": "a3f841b9-37d8-4bc5-8f86-8492bd2f47ae",
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
      "export_key": "actioninvocation/defender_indicator_field",
      "hide_notification": false,
      "id": 1745,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Field",
      "tooltip": "field to apply the filter",
      "type_id": 6,
      "uuid": "a74dc1f0-4082-48cc-957c-c549bade783e",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "title",
          "properties": null,
          "uuid": "001e44f1-08bd-4a03-9898-15ca59b45c6d",
          "value": 1307
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "description",
          "properties": null,
          "uuid": "3935e5c9-5a98-4dd4-aaec-97ffa5fb6486",
          "value": 1308
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "type",
          "properties": null,
          "uuid": "7be34c2c-e5b8-4a04-94d8-f2a2af26aaf7",
          "value": 1309
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "value",
          "properties": null,
          "uuid": "f2ef2c29-3e51-47d7-beef-73309a7fa665",
          "value": 1310
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
      "export_key": "actioninvocation/defender_alert_determination",
      "hide_notification": false,
      "id": 1746,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_determination",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Alert Determination",
      "tooltip": "",
      "type_id": 6,
      "uuid": "b2be6546-e5f8-4b04-9c39-fb15c45ed119",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apt",
          "properties": null,
          "uuid": "bf380d44-98f4-473e-8270-57a71d9675e9",
          "value": 1311
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Malware",
          "properties": null,
          "uuid": "1844bbbf-772a-4de4-b180-573d616a9847",
          "value": 1312
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NotAvailable",
          "properties": null,
          "uuid": "1ab5b1d0-6e78-42f1-a3fc-0363c61d08e9",
          "value": 1313
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityPersonnel",
          "properties": null,
          "uuid": "f6455263-8c98-4a92-982f-2d5cae4ac3a7",
          "value": 1314
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityTesting",
          "properties": null,
          "uuid": "2b75b260-592d-4711-9b55-6b676ef524f2",
          "value": 1315
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UnwantedSoftware",
          "properties": null,
          "uuid": "388345a0-b0fe-490c-aa0d-ed5e43621b31",
          "value": 1316
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other",
          "properties": null,
          "uuid": "24d7cee7-80a4-4555-b9dd-9faa20f4a9df",
          "value": 1317
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
      "export_key": "actioninvocation/defender_alert_status",
      "hide_notification": false,
      "id": 1747,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Alert Status",
      "tooltip": "",
      "type_id": 6,
      "uuid": "cec88b1e-9664-40f9-a36e-b513466877d1",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "d5471759-196e-4775-a3d3-0558ca85cccf",
          "value": 1318
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "InProgress",
          "properties": null,
          "uuid": "17e4c3e7-6e77-4bb5-a31a-80f69cb0e289",
          "value": 1319
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "2b2a071d-b317-471d-80fa-25e803ecae86",
          "value": 1320
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
      "export_key": "actioninvocation/indicator_title",
      "hide_notification": false,
      "id": 1748,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "indicator_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Title",
      "tooltip": "",
      "type_id": 6,
      "uuid": "db43862a-c62d-4603-988d-87e97971de94",
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
      "export_key": "actioninvocation/defender_updated_indicator_title",
      "hide_notification": false,
      "id": 1737,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_updated_indicator_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Leave empty to use existing title",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Updated Indicator Title",
      "tooltip": "",
      "type_id": 6,
      "uuid": "f462026e-94c5-437a-b755-0548a61a2eea",
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
      "export_key": "actioninvocation/indicator_severity",
      "hide_notification": false,
      "id": 1749,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "indicator_severity",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Severity",
      "tooltip": "",
      "type_id": 6,
      "uuid": "f4757460-b8e5-4342-9537-79c96c84060c",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Informational",
          "properties": null,
          "uuid": "c1947352-6a19-43ce-bbfa-495ef498ab5a",
          "value": 1321
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "2a4c12e6-32b2-4b8a-bfc7-4977dff14256",
          "value": 1322
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "0516811f-a000-41a8-a73c-b5896ee1ccce",
          "value": 1323
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "4ca6cc0c-e0c6-4bdc-bb2a-392f9b7a0680",
          "value": 1324
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
      "export_key": "actioninvocation/defender_isolation_action",
      "hide_notification": false,
      "id": 1739,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_isolation_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Isolation Action",
      "tooltip": "",
      "type_id": 6,
      "uuid": "0a348890-61f2-4d94-8cb2-c06d9d882fee",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "isolate",
          "properties": null,
          "uuid": "a6fb3d3b-9589-4615-a4b2-c4db1b26a285",
          "value": 1252
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unisolate",
          "properties": null,
          "uuid": "c3f91181-31a9-4d98-a2d0-7a99dec56753",
          "value": 1253
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
      "export_key": "actioninvocation/defender_indicator_filter",
      "hide_notification": false,
      "id": 1750,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_indicator_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[ab].*",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Indicator Filter",
      "tooltip": "regex to apply ",
      "type_id": 6,
      "uuid": "1e031f88-c36e-4891-a8f9-6af1b56a2340",
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
      "export_key": "actioninvocation/defender_alert_classification",
      "hide_notification": false,
      "id": 1751,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_classification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Alert Classification",
      "tooltip": "",
      "type_id": 6,
      "uuid": "33e170c3-ab00-495d-8111-a3108054d896",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FalsePositive",
          "properties": null,
          "uuid": "ce219e93-4e5b-432f-b047-8ecce1200764",
          "value": 1325
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TruePositive",
          "properties": null,
          "uuid": "48715f37-6d2a-43d0-9170-f11b94525b72",
          "value": 1326
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "706df20e-77c4-40c4-b549-24c4762dd83c",
          "value": 1327
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
      "export_key": "actioninvocation/defender_updated_indicator_description",
      "hide_notification": false,
      "id": 1738,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_updated_indicator_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Leave empty to use existing description",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Updated Incidator Description",
      "tooltip": "",
      "type_id": 6,
      "uuid": "4d6a693c-5799-458f-9c6a-83b02d2798e8",
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
      "export_key": "actioninvocation/defender_machine_scantype",
      "hide_notification": false,
      "id": 1752,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_machine_scantype",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Scan Type",
      "tooltip": "",
      "type_id": 6,
      "uuid": "62447aea-feec-4957-a9bc-b6f053e598d0",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Full",
          "properties": null,
          "uuid": "1885ddfc-261e-497e-b0a2-976bc0183b28",
          "value": 1328
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Quick",
          "properties": null,
          "uuid": "5abacb56-006e-42b4-bfa2-f77ba3364f2f",
          "value": 1329
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
      "export_key": "actioninvocation/defender_action_comment",
      "hide_notification": false,
      "id": 1753,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_action_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Action Comment",
      "tooltip": "",
      "type_id": 6,
      "uuid": "681fde75-dd7e-4b43-b27e-6f08efa71c77",
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
      "export_key": "actioninvocation/defender_alert_assigned_to",
      "hide_notification": false,
      "id": 1754,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_alert_assigned_to",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Assigned To",
      "tooltip": "",
      "type_id": 6,
      "uuid": "76625936-c52e-43f1-a0f7-8e6bc6fe543d",
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
      "export_key": "actioninvocation/defender_app_execution_action",
      "hide_notification": false,
      "id": 1755,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_app_execution_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "App Execution Action",
      "tooltip": "",
      "type_id": 6,
      "uuid": "787f3150-c790-43d3-adf1-690262a675a8",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "restrictCodeExecution",
          "properties": null,
          "uuid": "e377138b-ac07-43e5-a63d-4fc9a3c958dd",
          "value": 1330
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "unrestrictCodeExecution",
          "properties": null,
          "uuid": "3ec8efb6-bd69-4db0-8801-009f4215b53b",
          "value": 1331
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
      "export_key": "incident/defender_incident_lastupdatetime",
      "hide_notification": false,
      "id": 1194,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_lastupdatetime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Incident LastUpdateTime",
      "tooltip": "",
      "type_id": 0,
      "uuid": "9ffdfe40-77b7-4233-b3c9-51e6ce377966",
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
      "export_key": "incident/defender_tags",
      "hide_notification": false,
      "id": 1733,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "defender_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Tags",
      "tooltip": "comma separated list of Defender tags",
      "type_id": 0,
      "uuid": "ce4b9e0f-ddeb-4ed1-ba27-e44753d0d9d6",
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
      "export_key": "incident/defender_determination",
      "hide_notification": false,
      "id": 1731,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_determination",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Determination",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e834b645-b403-4803-a0f6-e1f176e7f4c1",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "NotAvailable",
          "properties": null,
          "uuid": "783d3720-1457-4742-85f5-7b913f476449",
          "value": 1208
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apt",
          "properties": null,
          "uuid": "811e9520-4ffe-4a24-a022-a0736846af0d",
          "value": 1209
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Malware",
          "properties": null,
          "uuid": "712a9895-3e17-4a97-a77a-d00ab04f7c0f",
          "value": 1210
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityPersonnel",
          "properties": null,
          "uuid": "9aeffada-9bbc-4102-9e20-a0599ab0f18a",
          "value": 1211
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SecurityTesting",
          "properties": null,
          "uuid": "378fbc0d-2347-4d0b-a4ce-360d3e2b5c04",
          "value": 1212
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UnwantedSoftware",
          "properties": null,
          "uuid": "c6879450-1d49-4e2d-8084-1d9ce27ed9b0",
          "value": 1213
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other",
          "properties": null,
          "uuid": "02725beb-1072-4590-b32c-a7adc79f8a0b",
          "value": 1214
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
      "export_key": "incident/defender_incident_url",
      "hide_notification": false,
      "id": 1193,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Incident Url",
      "tooltip": "",
      "type_id": 0,
      "uuid": "12e093cf-2138-4a5c-a676-14854df356e5",
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
      "export_key": "incident/defender_incident_id",
      "hide_notification": false,
      "id": 435,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Incident Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "21e17c1f-d21f-41b2-bdd8-2ba42d8c62f7",
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
      "export_key": "incident/defender_incident_createtime",
      "hide_notification": false,
      "id": 1195,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "defender_incident_createtime",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Incident CreateTime",
      "tooltip": "",
      "type_id": 0,
      "uuid": "38595dca-758c-4262-af29-003e2d28702a",
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
      "export_key": "incident/defender_classification",
      "hide_notification": false,
      "id": 1730,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "defender_classification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "templates": [],
      "text": "Defender Classification",
      "tooltip": "",
      "type_id": 0,
      "uuid": "664be662-7287-425b-be99-288834c719ef",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "790517f2-a4cf-49b1-bf2d-fb33c124a20c",
          "value": 1205
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FalsePositive",
          "properties": null,
          "uuid": "d2a3e477-7275-42ab-9cec-6a7d69f42187",
          "value": 1206
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TruePositive",
          "properties": null,
          "uuid": "799a7aee-b262-45d9-9023-d270d87d800d",
          "value": 1207
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
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Return Defender alerts based on a set of search criteria",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Alert Search",
      "export_key": "defender_alert_search",
      "id": 207,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254112,
      "name": "defender_alert_search",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "b84ee1e6-d4de-4fef-8ed4-4418b87d53d5",
      "version": 2,
      "view_items": [
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa552c13-07fb-438d-bff8-310eb7d20b4b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "953d2399-baa2-4a95-8d58-2e8045c92f9a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "97371dfb-d65d-46dc-8d4c-a98268da8f2f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "587375da-258c-475e-b4c9-61747f35ab59",
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
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Perform app restriction actions on a Microsoft Defender machine",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender App Execution",
      "export_key": "defender_app_execution",
      "id": 208,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254112,
      "name": "defender_app_execution",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "92906dbe-9be4-4277-8f50-c6f15fb5dcbc",
      "version": 2,
      "view_items": [
        {
          "content": "b35bd7fe-d52a-483e-ab06-16f8131ce093",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
          "name": "Defender App Execution Restriction",
          "object_type": "defender_machines",
          "programmatic_name": "defender_atp_app_execution",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 91
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Collect the machine investigation package",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Collect Machine Investigation Package",
      "export_key": "defender_collect_machine_investigation_package",
      "id": 209,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254112,
      "name": "defender_collect_machine_investigation_package",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "bfa88004-c394-4504-92ad-d3e1cb717b20",
      "version": 2,
      "view_items": [
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
          "name": "Defender Collect Machine Investigation Package",
          "object_type": "defender_machines",
          "programmatic_name": "defender_atp_collect_machine_investigation_package",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Delete an indicator from Defender ATP",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Delete Indicator",
      "export_key": "defender_delete_indicator",
      "id": 210,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254112,
      "name": "defender_delete_indicator",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "f13cf24d-612b-47c7-aa51-3748d3c3520e",
      "version": 2,
      "view_items": [
        {
          "content": "bf1e212e-9f0d-4c67-9679-0792f1223b94",
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
          "name": "Defender Delete Indicator",
          "object_type": "defender_indicators",
          "programmatic_name": "defender_atp_delete_indicator",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Find Defender Machine(s) by internal IP address",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Find Machines by Internal IP",
      "export_key": "defender_find_machines",
      "id": 211,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1636030766924,
      "name": "defender_find_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "11f82831-e4a8-4764-8ccd-f303c63caaf4",
      "version": 4,
      "view_items": [
        {
          "content": "bdbb9226-ec7b-48be-ac04-ae19ddb32b27",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "25fd039f-ed3a-4617-9944-b0cf6b937467",
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
          "name": "Defender Find Machines by Internal IP Address",
          "object_type": "artifact",
          "programmatic_name": "defender_atp_find_machines",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Find machines which match a given file hash",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Find Machines by File",
      "export_key": "defender_find_machines_by_file",
      "id": 212,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254112,
      "name": "defender_find_machines_by_file",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "adcb85db-0dc3-4a63-8875-4f325919dc3d",
      "version": 2,
      "view_items": [
        {
          "content": "bdbb9226-ec7b-48be-ac04-ae19ddb32b27",
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
          "name": "Defender Find Machines by File Hash",
          "object_type": "artifact",
          "programmatic_name": "defender_atp_find_machines_by_file_hash",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 84
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Find machines based on the OData filter capability of Defender",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Find machines by filter",
      "export_key": "defender_find_machines_by_filter",
      "id": 46,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_find_machines_by_filter",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "3ed5fa56-77c6-464e-b0c2-f5ea81d08370",
      "version": 4,
      "view_items": [
        {
          "content": "e13612f7-f7ed-45ce-b968-99a367f8d644",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ddce05a9-d22c-4cfd-9e89-e93c28cfc492",
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
          "name": "Defender Find Machines by Filter",
          "object_type": "artifact",
          "programmatic_name": "defender_find_machines_by_filter",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 83
        },
        {
          "actions": [],
          "description": null,
          "name": "Defender Get Machine Information",
          "object_type": "defender_alerts",
          "programmatic_name": "defender_get_machine_information",
          "tags": [],
          "uuid": null,
          "workflow_id": 78
        },
        {
          "actions": [],
          "description": null,
          "name": "Defender Get Updated Machine Information",
          "object_type": "defender_machines",
          "programmatic_name": "defender_get_updated_machine_information",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 80
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get additional information about a Defender SHA1 or SHA256 file reference.",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Get File Information",
      "export_key": "defender_get_file_information",
      "id": 213,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_get_file_information",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "1121d8e5-07e7-4506-8e87-9badef1cbcae",
      "version": 2,
      "view_items": [
        {
          "content": "615b32d0-ab72-48a0-a624-9043ff55dba2",
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
          "name": "Defender Get File Information",
          "object_type": "artifact",
          "programmatic_name": "defender_atp_get_file_information",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 85
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get a Defender 365 Incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Get Incident",
      "export_key": "defender_get_incident",
      "id": 205,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_get_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "9be05644-ed7f-4ada-b2d9-6d8e2c682853",
      "version": 3,
      "view_items": [
        {
          "content": "efad7afb-0fe3-4348-b7cb-1e5df5d57fc2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "587375da-258c-475e-b4c9-61747f35ab59",
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
          "name": "Defender Get Incident",
          "object_type": "incident",
          "programmatic_name": "defender_get_incident",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 77
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get a Defender ATP machine alert details",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Get Related Alert Information",
      "export_key": "defender_get_related_alert_information",
      "id": 214,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_get_related_alert_information",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "4517e61a-240f-4026-94f7-7867f81373ee",
      "version": 2,
      "view_items": [
        {
          "content": "c0d41921-0099-4e06-89de-4fbf3c3bda2c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "530a270d-338e-49e9-b877-3cfb5e89ecfa",
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
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get a list of all Defender indicators. Optionally, specify a regex filter to limit the responses.",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender List Indicators",
      "export_key": "defender_list_indicators",
      "id": 215,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_list_indicators",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "77e866e9-9c78-41d7-b13d-4feea72d59b7",
      "version": 2,
      "view_items": [
        {
          "content": "5a160310-4284-43fa-88b4-97bde9f7ce73",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "83ef8d59-9b4a-405a-bc7b-2978a214bdbf",
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
          "name": "Defender List Indicators",
          "object_type": "incident",
          "programmatic_name": "defender_list_indicators",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 89
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Perform either an \u0027isolate\u0027 or \u0027unisolate\u0027 operation on a MS defender machine",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Machine Isolation",
      "export_key": "defender_machine_isolation",
      "id": 216,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_machine_isolation",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "0afc74fe-8301-4801-a162-9e0dbd984e1a",
      "version": 2,
      "view_items": [
        {
          "content": "4f112eb2-0f5e-44b4-a240-d2feca9189c9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46ccbdc2-0d49-4e72-9310-49494aa1d4e0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
          "name": "Defender Machine Isolation",
          "object_type": "defender_machines",
          "programmatic_name": "defender_atp_machine_isolation",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Start a Defender ATP Machine antivirus scan",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Machine Scan",
      "export_key": "defender_machine_scan",
      "id": 217,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_machine_scan",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "3e8950d3-1f51-4bcb-b9ac-26e28e7f1704",
      "version": 2,
      "view_items": [
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d2234b4a-1677-42f9-89dc-a2dcca236948",
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
          "name": "Defender Machine Scan",
          "object_type": "defender_machines",
          "programmatic_name": "defender_atp_machine_scan",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 87
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Get vulnerabilities for a given Defender machine",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Machine Vulnerabilities",
      "export_key": "defender_machine_vulnerabilities",
      "id": 218,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_machine_vulnerabilities",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "b0e17c3e-ef30-46ed-bb0b-3862990314ed",
      "version": 2,
      "view_items": [
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
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
          "name": "Defender Machine Vulnerabilities",
          "object_type": "defender_machines",
          "programmatic_name": "defender_atp_machine_vulnerabilities",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 86
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Quarantine a SHA-1 file",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Quarantine File",
      "export_key": "defender_quarantine_file",
      "id": 219,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_quarantine_file",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "656a8125-f55f-4047-a1b8-86e7dc5b05f0",
      "version": 2,
      "view_items": [
        {
          "content": "bdbb9226-ec7b-48be-ac04-ae19ddb32b27",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c4707a3e-777e-4bc8-a9b9-5f9e54b7058a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
          "name": "Defender Quarantine File",
          "object_type": "defender_machines",
          "programmatic_name": "defender_quarantine_file",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 88
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Set or update an indicator with exposure values",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Set Indicator",
      "export_key": "defender_set_indicator",
      "id": 220,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_set_indicator",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "faf52947-0e1a-4e2b-9dfb-ed5ef1605667",
      "version": 2,
      "view_items": [
        {
          "content": "c8b53f87-e1f7-49df-bfaa-5c72c1168d69",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bf1e212e-9f0d-4c67-9679-0792f1223b94",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bdbb9226-ec7b-48be-ac04-ae19ddb32b27",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "88321e50-32cb-4e44-8806-f1e72427c24f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f604d3fb-c665-4267-ae40-1049ff676bf0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0e17bb0b-6ef9-4bac-b3d7-e5e37eaa7ffa",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2af4e75c-13d3-48cd-bd1d-1b159f607f48",
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
          "name": "Defender Set Indicator",
          "object_type": "artifact",
          "programmatic_name": "defender_atp_set_indicator",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 97
        },
        {
          "actions": [],
          "description": null,
          "name": "Defender Update Indicator",
          "object_type": "defender_indicators",
          "programmatic_name": "defender_atp_update_indicator",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update a Defender Alert",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Update Alert",
      "export_key": "defender_update_alert",
      "id": 221,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_update_alert",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "7666e80b-6eb0-4bef-88cc-e3bf095caad9",
      "version": 2,
      "view_items": [
        {
          "content": "c0d41921-0099-4e06-89de-4fbf3c3bda2c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "da1c26a1-7ffb-4f65-a7a4-2566c2d5e34d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c0c321ad-ed0a-4a1c-b5b9-a8c7387c58b0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dddcd251-6cb1-4fd7-a6a8-0f4890e87049",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b54ef2d-c209-479a-863a-46df39ec94e6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea5d9a08-3bd3-4515-99d7-a661dd634d38",
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
          "name": "Defender Update Alert",
          "object_type": "defender_alerts",
          "programmatic_name": "defender_atp_update_alert",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 93
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Update a Defender Incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_defender",
      "display_name": "Defender Update Incident",
      "export_key": "defender_update_incident",
      "id": 206,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1635532254113,
      "name": "defender_update_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "af506727-09ad-4997-b2fd-8c81eb1d2ea7",
      "version": 3,
      "view_items": [
        {
          "content": "efad7afb-0fe3-4348-b7cb-1e5df5d57fc2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "18d59d14-35ca-46e9-a571-2f0b0e45ff8a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dddcd251-6cb1-4fd7-a6a8-0f4890e87049",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b54ef2d-c209-479a-863a-46df39ec94e6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7bc628da-01e7-41b8-ac4e-6d029d7872aa",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b296aa20-606a-46c1-b1f9-b884d45f0e79",
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
          "name": "Defender Close Incident",
          "object_type": "incident",
          "programmatic_name": "defender_close_incident",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 79
        },
        {
          "actions": [],
          "description": null,
          "name": "Defender Sync Comment",
          "object_type": "note",
          "programmatic_name": "defender_sync_comment",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 81
        },
        {
          "actions": [],
          "description": null,
          "name": "Defender Sync Incident",
          "object_type": "incident",
          "programmatic_name": "defender_sync_incident",
          "tags": [
            {
              "tag_handle": "fn_microsoft_defender",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 62,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1636664048637,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1636664048637,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "6bde93ab-a85d-4b7f-868d-5dbec1641a49"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_microsoft_defender",
      "name": "fn_microsoft_defender",
      "programmatic_name": "fn_microsoft_defender",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "6d9ef9ff-028c-49da-a42f-4e1fe91ceaa4"
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
      "creator_id": "a@example.com",
      "description": "Convert a Defender indicator to an Artifact for further enrichment or remediation",
      "export_key": "Create Artifact from Indicator",
      "id": 8,
      "language": "python",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635450098160,
      "name": "Create Artifact from Indicator",
      "object_type": "defender_indicators",
      "script_text": "# Convert a Defender ATP indicator to an artifact_type\n# lookup for Defender indicator types to arttfact types\ntype_lookup = {\n        \"FileSha1\": \"Malware SHA-1 Hash\",\n        \"FileSha256\": \"Malware SHA-256 Hash\",\n        \"IpAddress\": \"IP Address\",\n        \"DomainName\": \"DNS Name\",\n        \"Url\": \"URL\"\n    }\n    \nartifact_type = type_lookup.get(row[\u0027ind_type\u0027], \"String\")\nartifact_description = u\"{}\\n{}\".format(row[\u0027ind_title\u0027], row[\u0027ind_description\u0027])\nincident.addArtifact(artifact_type, row[\u0027ind_value\u0027], artifact_description)\n\nmsg = u\"Defender Action successful.\\nIndicator: {}\\nAction: Create Artifact\".format(row[\u0027ind_value\u0027])\nincident.addNote(msg)",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "cd4205de-0466-4797-b03f-2469de7d1c34"
    }
  ],
  "server_version": {
    "build_number": 6328,
    "major": 39,
    "minor": 0,
    "version": "39.0.6328"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Defender Alerts",
      "export_key": "defender_alerts",
      "fields": {
        "alert_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/alert_description",
          "hide_notification": false,
          "id": 440,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_description",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "dfa3a652-88af-4369-8d8c-4ed856d57ee4",
          "values": [],
          "width": 88
        },
        "alert_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/alert_id",
          "hide_notification": false,
          "id": 441,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_id",
          "operation_perms": {},
          "operations": [],
          "order": 15,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert ID",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "c60b0039-ea7b-4e04-8421-3540c9ab47ae",
          "values": [],
          "width": 38
        },
        "alert_link": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/alert_link",
          "hide_notification": false,
          "id": 1735,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "alert_link",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Alert Link",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "7562e969-1a88-499a-abca-49398d8617be",
          "values": [],
          "width": 38
        },
        "assigned_to": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/assigned_to",
          "hide_notification": false,
          "id": 442,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "assigned_to",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Assigned To",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "2ebda9ca-09d7-4bd4-a706-bb25c73a4f9e",
          "values": [],
          "width": 70
        },
        "category": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/category",
          "hide_notification": false,
          "id": 444,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "category",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "9cf2e13d-360c-4fe0-9f81-1fa0ea5cf7ef",
          "values": [],
          "width": 69
        },
        "classification": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/classification",
          "hide_notification": false,
          "id": 445,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "classification",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Classification",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "5b2571bb-9670-4c2c-a170-8a0870105a76",
          "values": [],
          "width": 104
        },
        "computer_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/computer_name",
          "hide_notification": false,
          "id": 446,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "computer_name",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Computer Name",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "bba1c5af-bfc2-495f-8075-7bda3a7bf005",
          "values": [],
          "width": 76
        },
        "determination": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/determination",
          "hide_notification": false,
          "id": 447,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "determination",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Determination",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "0b678f06-0acf-456c-8c16-10b3f28bf9f5",
          "values": [],
          "width": 111
        },
        "first_seen": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/first_seen",
          "hide_notification": false,
          "id": 1725,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "first_seen",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "First Seen",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "1fd85809-1bde-4e45-9ef1-98889f7ff4c8",
          "values": [],
          "width": 38
        },
        "machine_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/machine_id",
          "hide_notification": false,
          "id": 450,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_id",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Machine ID",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "870e6721-28c0-4695-b62f-a965d7a0ae2d",
          "values": [],
          "width": 64
        },
        "mitre_techniques": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/mitre_techniques",
          "hide_notification": false,
          "id": 1732,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "mitre_techniques",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Mitre Techniques",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "824dfe0f-91f2-4afb-95fa-99005306e1d1",
          "values": [],
          "width": 87
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/report_date",
          "hide_notification": false,
          "id": 1727,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "report_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report Date",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "9738e1f0-cd46-41a0-a224-4b64bc3a94d5",
          "values": [],
          "width": 52
        },
        "risk_score": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/risk_score",
          "hide_notification": false,
          "id": 1726,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "risk_score",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Risk Score",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "1cb2bf64-cc90-4f38-af5f-63fc63c0fad6",
          "values": [],
          "width": 43
        },
        "severity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/severity",
          "hide_notification": false,
          "id": 451,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "severity",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Severity",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "759656e4-4179-40d4-9f79-3b85ffd0700e",
          "values": [],
          "width": 63
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/status",
          "hide_notification": false,
          "id": 452,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "76dbd751-1312-496f-b922-85bc757d86d7",
          "values": [],
          "width": 50
        },
        "title": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_alerts/title",
          "hide_notification": false,
          "id": 453,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "title",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Title",
          "tooltip": "",
          "type_id": 1008,
          "uuid": "4c56eaf2-da18-4738-9abf-26478f647b35",
          "values": [],
          "width": 35
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
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "defender_alerts",
      "uuid": "06eb7acb-21a6-4469-bb6a-0f202c1973c7"
    },
    {
      "actions": [],
      "display_name": "Defender Indicators",
      "export_key": "defender_indicators",
      "fields": {
        "ind_action": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_action",
          "hide_notification": false,
          "id": 454,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_action",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Action",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "3371d3bc-1615-4cc8-9806-b2c431f5038f",
          "values": [],
          "width": 50
        },
        "ind_created_by": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_created_by",
          "hide_notification": false,
          "id": 455,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_created_by",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Created By",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "30726e2d-960c-447d-982f-df2d925e2c8f",
          "values": [],
          "width": 61
        },
        "ind_creation_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_creation_date",
          "hide_notification": false,
          "id": 456,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "ind_creation_date",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Creation Date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "c86a7365-797c-41b3-ac6b-c82f7c4fb64c",
          "values": [],
          "width": 65
        },
        "ind_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_description",
          "hide_notification": false,
          "id": 457,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_description",
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
          "tooltip": "",
          "type_id": 1009,
          "uuid": "31f02d97-d46d-4867-bc7a-929886c44c68",
          "values": [],
          "width": 88
        },
        "ind_expiration_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_expiration_date",
          "hide_notification": false,
          "id": 458,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "ind_expiration_date",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Expiration Date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "536f5076-ce7e-4c1b-8403-fe2cb1e59f01",
          "values": [],
          "width": 79
        },
        "ind_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_id",
          "hide_notification": false,
          "id": 459,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_id",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Indicator ID",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "08733e0b-3978-41bb-afa9-59c3e102741a",
          "values": [],
          "width": 71
        },
        "ind_severity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_severity",
          "hide_notification": false,
          "id": 460,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_severity",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Severity",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "153d3b7c-251e-4a37-98b7-fa2d58782d09",
          "values": [],
          "width": 63
        },
        "ind_title": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_title",
          "hide_notification": false,
          "id": 461,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_title",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Title",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "a9dd7dc1-c62e-458a-acea-781119d2dd39",
          "values": [],
          "width": 43
        },
        "ind_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_type",
          "hide_notification": false,
          "id": 462,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_type",
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
          "tooltip": "",
          "type_id": 1009,
          "uuid": "21483f60-fefa-4b6d-9408-2c02f839c599",
          "values": [],
          "width": 43
        },
        "ind_value": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/ind_value",
          "hide_notification": false,
          "id": 463,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ind_value",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Value",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "245aa50a-5b22-4c63-a76e-0048c2a26efa",
          "values": [],
          "width": 46
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/report_date",
          "hide_notification": false,
          "id": 464,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "report_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report Date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "a4993924-c85b-40a1-a425-85580a4f382c",
          "values": [],
          "width": 52
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_indicators/status",
          "hide_notification": false,
          "id": 465,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "662fe692-a048-421d-9715-fd655eccf7f9",
          "values": [],
          "width": 50
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
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "defender_indicators",
      "uuid": "f0f643e0-7984-4d62-b0f3-66b75aa44b04"
    },
    {
      "actions": [],
      "display_name": "Defender Machines",
      "export_key": "defender_machines",
      "fields": {
        "machine_exposure_level": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_exposure_level",
          "hide_notification": false,
          "id": 466,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_exposure_level",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Exposure Level",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "c19ecfb7-fc42-4193-9595-409f18adb4f8",
          "values": [],
          "width": 72
        },
        "machine_file_hash": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_file_hash",
          "hide_notification": false,
          "id": 467,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_file_hash",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "File Hash",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "194f5a30-6ed3-4975-a8d5-e682886d661c",
          "values": [],
          "width": 48
        },
        "machine_firstseen": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_firstseen",
          "hide_notification": false,
          "id": 468,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "machine_firstseen",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "First Seen",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "228f78d7-6f04-4d6a-89ae-6637d8e9ad74",
          "values": [],
          "width": 185
        },
        "machine_health_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_health_status",
          "hide_notification": false,
          "id": 469,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_health_status",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Health Status",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "de9c980f-2825-49c8-9268-704101b34437",
          "values": [],
          "width": 51
        },
        "machine_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_id",
          "hide_notification": false,
          "id": 470,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_id",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Machine ID",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "c80900f7-2e63-4fdb-987a-1b0907fe5e3d",
          "values": [],
          "width": 100
        },
        "machine_internal_ip": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_internal_ip",
          "hide_notification": false,
          "id": 1909,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_internal_ip",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Internal IP Address",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "758573a2-7914-425e-aa9b-3b00faeab285",
          "values": [],
          "width": 63
        },
        "machine_ip": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_ip",
          "hide_notification": false,
          "id": 471,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_ip",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IP Address",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "d25ff388-5eef-4d30-b542-252587a7b88d",
          "values": [],
          "width": 99
        },
        "machine_last_action": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_last_action",
          "hide_notification": false,
          "id": 472,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "machine_last_action",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Last Action",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "5f051976-7675-41fc-aa6b-b1b037b3cc96",
          "values": [],
          "width": 58
        },
        "machine_lastseen": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_lastseen",
          "hide_notification": false,
          "id": 473,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "machine_lastseen",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Last Seen",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "069ac674-5e1d-44ce-af16-3c08c161f712",
          "values": [],
          "width": 38
        },
        "machine_link": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_link",
          "hide_notification": false,
          "id": 1736,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "machine_link",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Machine Link",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "b3546b7f-d5ce-4754-8457-ebd3d64bd5db",
          "values": [],
          "width": 64
        },
        "machine_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_name",
          "hide_notification": false,
          "id": 474,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_name",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Machine Name",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "ede22ebf-e91b-4dff-99a6-b9a16221cd03",
          "values": [],
          "width": 120
        },
        "machine_platform": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_platform",
          "hide_notification": false,
          "id": 475,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_platform",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Platform",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "fb7b3eda-0ebc-4567-927c-7807dd53f671",
          "values": [],
          "width": 144
        },
        "machine_risk_score": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_risk_score",
          "hide_notification": false,
          "id": 476,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_risk_score",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Risk Score",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "3575df2a-9a46-459f-8808-24cb6e0477be",
          "values": [],
          "width": 43
        },
        "machine_tags": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/machine_tags",
          "hide_notification": false,
          "id": 477,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "machine_tags",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Machine Tags",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "03a0524f-e670-46bd-81e9-18f031e3a57e",
          "values": [],
          "width": 64
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "defender_machines/report_date",
          "hide_notification": false,
          "id": 478,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "report_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report Date",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "eefa547c-47e3-4f37-afe2-042291eca357",
          "values": [],
          "width": 52
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
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "defender_machines",
      "uuid": "6c3b8c98-688a-4172-a861-1ae5c89a4e5f"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "defender_find_machines_by_filter",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_find_machines_by_filter\" isExecutable=\"true\" name=\"Defender Find Machines by Filter\"\u003e\u003cdocumentation\u003eUse Microsoft OData filters to find machines controlled by Defender. See app documentation for the filters supported.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14cy2rx\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ipvdp3\" name=\"Defender Find machines by filter\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3ed5fa56-77c6-464e-b0c2-f5ea81d08370\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\n\\\"\\\"\\\"\\n\\\"value\\\": [\\n    {\\n        \\\"id\\\": \\\"04c99d46599f078f1c3da3783cf5b95f01ac61bb\\\",\\n        \\\"computerDnsName\\\": \\\"\\\",\\n        \\\"firstSeen\\\": \\\"2017-07-06T01:25:04.9480498Z\\\",\\n        \\\"osPlatform\\\": \\\"Windows10\\\",\\n    }\\n]\\n\\\"\\\"\\\"\\nif results.success:\\n    for machine in results.content.get(\u0027value\u0027, []):\\n      row = incident.addRow(\\\"defender_machines\\\")\\n      row[\u0027report_date\u0027] = now\\n      row[\u0027machine_link\u0027] = \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027https://security.microsoft.com/machines/{}/overview\u0027\u0026gt;Machine\u0026lt;/a\u0026gt;\\\".format(machine[\u0027mdatpDeviceId\u0027])\\n      row[\u0027machine_id\u0027] = machine[\u0027id\u0027]\\n      row[\u0027machine_ip\u0027] = machine[\u0027lastExternalIpAddress\u0027]\\n      row[\u0027machine_internal_ip\u0027] = machine[\u0027lastIpAddress\u0027]\\n      row[\u0027machine_name\u0027] = machine[\u0027computerDnsName\u0027]\\n      row[\u0027machine_platform\u0027] = machine[\u0027osPlatform\u0027]\\n      row[\u0027machine_firstseen\u0027] = machine[\u0027firstSeen_ts\u0027]\\n      row[\u0027machine_lastseen\u0027] = machine[\u0027lastSeen_ts\u0027]\\n      row[\u0027machine_health_status\u0027] = machine.get(\u0027healthStatus\u0027)\\n      row[\u0027machine_risk_score\u0027] = machine.get(\u0027riskScore\u0027)\\n      row[\u0027machine_exposure_level\u0027] = machine.get(\u0027exposureLevel\u0027)\\n      row[\u0027machine_tags\u0027] = \u0027, \u0027.join(machine.get(\u0027machineTags\u0027, []))\\nelse:\\n  msg = u\\\"Defender Action unsuccessful.\\\\nAction: Find Machines by filter\\\\nReason: {}\\\".format(results.reason)\\n  incident.addNote(helper.createPlainText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_filter_name = \\\"filter_by_name\\\"\\ninputs.defender_filter_value = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14cy2rx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11xdamh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14cy2rx\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ipvdp3\"/\u003e\u003cendEvent id=\"EndEvent_19rgdwa\"\u003e\u003cincoming\u003eSequenceFlow_11xdamh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_11xdamh\" sourceRef=\"ServiceTask_0ipvdp3\" targetRef=\"EndEvent_19rgdwa\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_08elm2v\"\u003e\u003ctext\u003e\u003c![CDATA[Results placed in the Defender Machines datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0c1ejsi\" sourceRef=\"ServiceTask_0ipvdp3\" targetRef=\"TextAnnotation_08elm2v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ipvdp3\" id=\"ServiceTask_0ipvdp3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14cy2rx\" id=\"SequenceFlow_14cy2rx_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_19rgdwa\" id=\"EndEvent_19rgdwa_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"445\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"463\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11xdamh\" id=\"SequenceFlow_11xdamh_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"445\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_08elm2v\" id=\"TextAnnotation_08elm2v_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"193\" x=\"374\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0c1ejsi\" id=\"Association_0c1ejsi_di\"\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "creator_id": "a@example.com",
      "description": "Use Microsoft OData filters to find machines controlled by Defender. See app documentation for the filters supported.",
      "export_key": "defender_find_machines_by_filter",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636030935483,
      "name": "Defender Find Machines by Filter",
      "object_type": "artifact",
      "programmatic_name": "defender_find_machines_by_filter",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "dd1069b4-3100-4e7c-97e8-a80c4816331f",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "defender_sync_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_sync_incident\" isExecutable=\"true\" name=\"Defender Sync Incident\"\u003e\u003cdocumentation\u003eSync SOAR Incident changes to the corresponding Defender Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0bbajk0\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bnb1v7\" name=\"Defender Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"af506727-09ad-4997-b2fd-8c81eb1d2ea7\"\u003e{\"inputs\":{\"18d59d14-35ca-46e9-a571-2f0b0e45ff8a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"d316fcc8-94b7-40b1-856f-b9408f8f78b0\"}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.defender_incident_id = incident.properties.defender_incident_id\\ninputs.defender_classification = incident.properties.defender_classification\\ninputs.defender_determination = incident.properties.defender_determination\\ninputs.defender_tags = incident.properties.defender_tags\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0bbajk0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1db1pal\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0bbajk0\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bnb1v7\"/\u003e\u003cendEvent id=\"EndEvent_03q829u\"\u003e\u003cincoming\u003eSequenceFlow_1db1pal\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1db1pal\" sourceRef=\"ServiceTask_1bnb1v7\" targetRef=\"EndEvent_03q829u\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bnb1v7\" id=\"ServiceTask_1bnb1v7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"284\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bbajk0\" id=\"SequenceFlow_0bbajk0_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"284\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"241\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03q829u\" id=\"EndEvent_03q829u_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"474\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"492\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1db1pal\" id=\"SequenceFlow_1db1pal_di\"\u003e\u003comgdi:waypoint x=\"384\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"474\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"429\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "a@example.com",
      "description": "Sync SOAR Incident changes to the corresponding Defender Incident",
      "export_key": "defender_sync_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532254411,
      "name": "Defender Sync Incident",
      "object_type": "incident",
      "programmatic_name": "defender_sync_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "209f3528-3ae4-4098-bfda-ac76e29abe9b",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "defender_atp_update_alert",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_update_alert\" isExecutable=\"true\" name=\"Defender Update Alert\"\u003e\u003cdocumentation\u003eUpdate a Defender Alert: Status, Classification, Assigned to, and Determination\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0j9rkvs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10d04cr\" name=\"Defender Update Alert\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7666e80b-6eb0-4bef-88cc-e3bf095caad9\"\u003e{\"inputs\":{\"c0c321ad-ed0a-4a1c-b5b9-a8c7387c58b0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"2fead575-cda4-4ea4-837c-73ff0563ec6a\"}},\"dddcd251-6cb1-4fd7-a6a8-0f4890e87049\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"b8bef116-f5e1-4bbb-9dd8-cd28d4706b9d\"}},\"0b54ef2d-c209-479a-863a-46df39ec94e6\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7f6c5ad6-f742-43db-b94c-4881d93b99da\"}}},\"post_processing_script\":\"msg = u\\\"Defender Action {}.\\\\nAction: Update Alert\\\\nAlert: {}\\\\nMachine: {}\\\\nComment: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           row[\u0027alert_id\u0027],\\n           row[\u0027computer_name\u0027],\\n           rule.properties.defender_action_comment)\\nif rule.properties.defender_alert_assigned_to:\\n    msg = u\\\"{}\\\\nAssigned to: {}\\\".format(msg, rule.properties.defender_alert_assigned_to)\\nif rule.properties.defender_alert_status:\\n    msg = u\\\"{}\\\\nStatus: {}\\\".format(msg, str(rule.properties.defender_alert_status))\\nif rule.properties.defender_alert_classification:\\n    msg = u\\\"{}\\\\nClassification: {}\\\".format(msg, str(rule.properties.defender_alert_classification))\\nif rule.properties.defender_alert_determination:\\n    msg = u\\\"{}\\\\nDetermination: {}\\\".format(msg, str(rule.properties.defender_alert_determination))\\n\\nif not results.success:\\n    msg = u\\\"{}\\\\nReason: {}\\\".format(msg, results.reason)\\n\\nincident.addNote(msg)\\n\\nif results.success:\\n    alert = results.content\\n    row[\u0027classification\u0027] = alert[\u0027classification\u0027]\\n    row[\u0027determination\u0027] = alert[\u0027determination\u0027]\\n    row[\u0027status\u0027] = alert[\u0027status\u0027]\\n    row[\u0027severity\u0027] = alert[\u0027severity\u0027]\\n    row[\u0027assigned_to\u0027] = alert[\u0027assignedTo\u0027]\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_alert_id = row[\u0027alert_id\u0027]\\nif rule.properties.defender_alert_classification:\\n    inputs.defender_classification = str(rule.properties.defender_alert_classification)\\nif rule.properties.defender_alert_determination:\\n    inputs.defender_determination = str(rule.properties.defender_alert_determination)\\nif rule.properties.defender_alert_status:\\n    inputs.defender_alert_status = str(rule.properties.defender_alert_status)\\ninputs.defender_description = rule.properties.defender_action_comment\\ninputs.defender_alert_assigned_to = rule.properties.defender_alert_assigned_to\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0j9rkvs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1byqvvp\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0j9rkvs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_10d04cr\"/\u003e\u003cendEvent id=\"EndEvent_0bs2mo8\"\u003e\u003cincoming\u003eSequenceFlow_1byqvvp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1byqvvp\" sourceRef=\"ServiceTask_10d04cr\" targetRef=\"EndEvent_0bs2mo8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1fzo0dn\"\u003e\u003ctext\u003e\u003c![CDATA[Results update the defender_atp_alerts datatable and a note is created.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ms2kom\" sourceRef=\"ServiceTask_10d04cr\" targetRef=\"TextAnnotation_1fzo0dn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10d04cr\" id=\"ServiceTask_10d04cr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j9rkvs\" id=\"SequenceFlow_0j9rkvs_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0bs2mo8\" id=\"EndEvent_0bs2mo8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"405\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"423\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1byqvvp\" id=\"SequenceFlow_1byqvvp_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"378.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1fzo0dn\" id=\"TextAnnotation_1fzo0dn_di\"\u003e\u003comgdc:Bounds height=\"47\" width=\"187\" x=\"331\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ms2kom\" id=\"Association_0ms2kom_di\"\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Update a Defender Alert: Status, Classification, Assigned to, and Determination",
      "export_key": "defender_atp_update_alert",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532256069,
      "name": "Defender Update Alert",
      "object_type": "defender_alerts",
      "programmatic_name": "defender_atp_update_alert",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "0da47896-a15a-47f3-9746-0527cc01b0fd",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "defender_close_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_close_incident\" isExecutable=\"true\" name=\"Defender Close Incident\"\u003e\u003cdocumentation\u003eClose the corresponding Defender incident when the SOAR incident closes\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1kzje8a\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kgahox\" name=\"Defender Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"af506727-09ad-4997-b2fd-8c81eb1d2ea7\"\u003e{\"inputs\":{\"18d59d14-35ca-46e9-a571-2f0b0e45ff8a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"d316fcc8-94b7-40b1-856f-b9408f8f78b0\"}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# change as necessary. Value Defender values are:  Active, Resolved, and Redirected.\\nLOOKUP_STATUS = {\\n    \\\"7\\\": \\\"Resolved\\\", # Unresolved\\n    \\\"8\\\": \\\"Resolved\\\", # Duplicate\\n    \\\"9\\\": \\\"Resolved\\\", # Not an Issue\\n    \\\"10\\\": \\\"Resolved\\\" # Resolved\\n}\\n\\ninputs.defender_incident_id = incident.properties.defender_incident_id\\ninputs.defender_incident_status = LOOKUP_STATUS.get(incident.resolution_id, \\\"Resolved\\\")\\ninputs.defender_comment = incident.resolution_summary.content\\ninputs.defender_classification = incident.properties.defender_classification\\ninputs.defender_determination = incident.properties.defender_determination\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kzje8a\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0sygq48\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1kzje8a\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kgahox\"/\u003e\u003cendEvent id=\"EndEvent_1jkjsil\"\u003e\u003cincoming\u003eSequenceFlow_0sygq48\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0sygq48\" sourceRef=\"ServiceTask_0kgahox\" targetRef=\"EndEvent_1jkjsil\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kgahox\" id=\"ServiceTask_0kgahox_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kzje8a\" id=\"SequenceFlow_1kzje8a_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jkjsil\" id=\"EndEvent_1jkjsil_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"423\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"441\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0sygq48\" id=\"SequenceFlow_0sygq48_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"390.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Close the corresponding Defender incident when the SOAR incident closes",
      "export_key": "defender_close_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532255481,
      "name": "Defender Close Incident",
      "object_type": "incident",
      "programmatic_name": "defender_close_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "058cbdee-22d6-4a75-a377-6a354c32a939",
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "defender_atp_machine_scan",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_machine_scan\" isExecutable=\"true\" name=\"Defender Machine Scan\"\u003e\u003cdocumentation\u003eStart an antivirus scan on a Defender machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0w46f4k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_174h93d\" name=\"Defender Machine Scan\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3e8950d3-1f51-4bcb-b9ac-26e28e7f1704\"\u003e{\"inputs\":{\"d2234b4a-1677-42f9-89dc-a2dcca236948\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"f80596f3-dc40-4c52-a014-cf9cf299cc28\"}}},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  row[\u0027report_date\u0027] = now\\n  action_msg = \\\"Action: {}\\\\nComment: {}\\\\nStatus: {}\\\\nStart Date: {}\\\".format(\\n    results.content[\u0027type\u0027],\\n    results.content[\u0027requestorComment\u0027],\\n    results.content[\u0027status\u0027],\\n    results.content[\u0027creationDateTimeUtc\u0027]\\n    )\\n  row[\u0027machine_last_action\u0027] = helper.createPlainText(action_msg)\\nelse:\\n  msg = u\\\"Defender Scan Action {}.\\\\nMachine: {} ({})\\\\nType: {}\\\\nComment: {}\\\\nReason: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           row[\u0027machine_name\u0027], row[\u0027machine_id\u0027],\\n           str(rule.properties.defender_isolation_type),\\n           rule.properties.defender_action_comment,\\n           results.reason)\\n\\n  incident.addNote(helper.createPlainText(msg))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_machine_id = row[\u0027machine_id\u0027]\\ninputs.defender_description = rule.properties.defender_action_comment\\ninputs.defender_machine_scantype = str(rule.properties.defender_machine_scantype)\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0w46f4k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vgb3q6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0w46f4k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_174h93d\"/\u003e\u003cendEvent id=\"EndEvent_12zqo78\"\u003e\u003cincoming\u003eSequenceFlow_0vgb3q6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vgb3q6\" sourceRef=\"ServiceTask_174h93d\" targetRef=\"EndEvent_12zqo78\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ga004d\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a Note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0757krv\" sourceRef=\"ServiceTask_174h93d\" targetRef=\"TextAnnotation_0ga004d\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_174h93d\" id=\"ServiceTask_174h93d_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w46f4k\" id=\"SequenceFlow_0w46f4k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_12zqo78\" id=\"EndEvent_12zqo78_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"414\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"432\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vgb3q6\" id=\"SequenceFlow_0vgb3q6_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"414\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"386\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ga004d\" id=\"TextAnnotation_0ga004d_di\"\u003e\u003comgdc:Bounds height=\"37\" width=\"164\" x=\"350\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0757krv\" id=\"Association_0757krv_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"115\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@example.com",
      "description": "Start an antivirus scan on a Defender machine",
      "export_key": "defender_atp_machine_scan",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636663407238,
      "name": "Defender Machine Scan",
      "object_type": "defender_machines",
      "programmatic_name": "defender_atp_machine_scan",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "fc9556a5-d88c-4ca8-84be-3e84b3da8b6a",
      "workflow_id": 87
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "defender_atp_machine_isolation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_machine_isolation\" isExecutable=\"true\" name=\"Defender Machine Isolation\"\u003e\u003cdocumentation\u003eIsolate/Unisolate a Defender Machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0yu2usv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0vx43uk\" name=\"Defender Machine Isolation\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0afc74fe-8301-4801-a162-9e0dbd984e1a\"\u003e{\"inputs\":{\"46ccbdc2-0d49-4e72-9310-49494aa1d4e0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"11fcc5e8-b795-4719-8320-c99d323d10a6\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nif results.success:\\n  row[\u0027report_date\u0027] = Date().getTime()\\n  \\n  action_msg = \\\"Action: {}\\\\nComment: {}\\\\nStatus: {}\\\\nStart Date: {}\\\".format(\\n    results.content[\u0027type\u0027],\\n    results.content[\u0027requestorComment\u0027],\\n    results.content[\u0027status\u0027],\\n    results.content[\u0027creationDateTimeUtc\u0027]\\n    )\\n  row[\u0027machine_last_action\u0027] = helper.createPlainText(action_msg)\\nelse:\\n  msg = u\\\"Defender Isolate Action {}.\\\\nMachine: {} ({})\\\\nAction: {}\\\\nType: {}\\\\nComment: {}\\\\nReason: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           row[\u0027machine_name\u0027], row[\u0027machine_id\u0027],\\n           str(rule.properties.defender_isolation_action),\\n           str(rule.properties.defender_isolation_type),\\n           rule.properties.defender_action_comment,\\n           results.reason)\\n\\n  incident.addNote(helper.createPlainText(msg))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_machine_id = row[\u0027machine_id\u0027]\\ninputs.defender_isolation_type = str(rule.properties.defender_isolation_type)\\ninputs.defender_description = rule.properties.defender_action_comment\\ninputs.defender_isolation_action = str(rule.properties.defender_isolation_action)\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0yu2usv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0x9zzb1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0yu2usv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0vx43uk\"/\u003e\u003cendEvent id=\"EndEvent_1bmmobf\"\u003e\u003cincoming\u003eSequenceFlow_0x9zzb1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0x9zzb1\" sourceRef=\"ServiceTask_0vx43uk\" targetRef=\"EndEvent_1bmmobf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1q6d49f\"\u003e\u003ctext\u003e\u003c![CDATA[\u0027Defender ATP Machines\u0027 datatable action status update\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1y18pzl\" sourceRef=\"ServiceTask_0vx43uk\" targetRef=\"TextAnnotation_1q6d49f\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vx43uk\" id=\"ServiceTask_0vx43uk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0yu2usv\" id=\"SequenceFlow_0yu2usv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bmmobf\" id=\"EndEvent_1bmmobf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"454\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"472\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0x9zzb1\" id=\"SequenceFlow_0x9zzb1_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"416.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1q6d49f\" id=\"TextAnnotation_1q6d49f_di\"\u003e\u003comgdc:Bounds height=\"49\" width=\"196\" x=\"372\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1y18pzl\" id=\"Association_1y18pzl_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "creator_id": "a@example.com",
      "description": "Isolate/Unisolate a Defender Machine",
      "export_key": "defender_atp_machine_isolation",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636663318725,
      "name": "Defender Machine Isolation",
      "object_type": "defender_machines",
      "programmatic_name": "defender_atp_machine_isolation",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "54c99f35-1269-456e-b1c3-ccfcb7441f0d",
      "workflow_id": 96
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "defender_atp_update_indicator",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_update_indicator\" isExecutable=\"true\" name=\"Defender Update Indicator\"\u003e\u003cdocumentation\u003eModify an existing Defender indicator\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_08m8yww\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0qfzuck\" name=\"Defender Set Indicator\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"faf52947-0e1a-4e2b-9dfb-ed5ef1605667\"\u003e{\"inputs\":{\"c8b53f87-e1f7-49df-bfaa-5c72c1168d69\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"79c1a5bb-b168-4868-922b-54eb17365f9b\"}},\"0e17bb0b-6ef9-4bac-b3d7-e5e37eaa7ffa\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"a3216414-9c8b-49d4-9714-2b728e14f8c5\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nmsg = u\\\"Defender Action {}.\\\\nAction: {}\\\\nArtifact: {}\\\\nTitle: {}\\\\nComment: {}\\\\nSeverity: {}\\\\nExpiration: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           str(rule.properties.indicator_action),\\n           row[\u0027ind_value\u0027],\\n           rule.properties.indicator_title,\\n           rule.properties.indicator_description,\\n           str(rule.properties.indicator_severity),\\n           rule.properties.indicator_expiration)\\n           \\nif not results.success:\\n    msg = u\\\"{}\\\\nReason: {}\\\".format(msg, results.reason)\\n\\nincident.addNote(msg)\\n\\nif results.success:\\n    row[\u0027report_date\u0027] = Date().getTime()\\n    row[\u0027ind_title\u0027] = results.content[\u0027title\u0027]\\n    row[\u0027ind_description\u0027] = results.content[\u0027description\u0027]\\n    row[\u0027ind_action\u0027] = results.content[\u0027action\u0027]\\n    row[\u0027ind_severity\u0027] = results.content[\u0027severity\u0027]\\n    row[\u0027ind_expiration_date\u0027] = results.content[\u0027expirationTime_ts\u0027]\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_description = rule.properties.defender_updated_indicator_description if rule.properties.defender_updated_indicator_description else row[\u0027ind_description\u0027]\\ninputs.defender_title = rule.properties.defender_updated_indicator_title if rule.properties.defender_updated_indicator_title else row[\u0027ind_title\u0027]\\ninputs.defender_indicator_action = str(rule.properties.indicator_action)\\ninputs.defender_expiration_time = rule.properties.indicator_expiration\\ninputs.defender_severity = str(rule.properties.indicator_severity)\\ninputs.defender_indicator_type = row[\u0027ind_type\u0027]\\ninputs.defender_indicator_value = row[\u0027ind_value\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_08m8yww\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16osyai\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_08m8yww\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qfzuck\"/\u003e\u003cendEvent id=\"EndEvent_1m8cg1z\"\u003e\u003cincoming\u003eSequenceFlow_16osyai\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16osyai\" sourceRef=\"ServiceTask_0qfzuck\" targetRef=\"EndEvent_1m8cg1z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0wmpc10\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note and datatable row updated upon success.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0827dlu\" sourceRef=\"ServiceTask_0qfzuck\" targetRef=\"TextAnnotation_0wmpc10\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qfzuck\" id=\"ServiceTask_0qfzuck_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"275\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08m8yww\" id=\"SequenceFlow_08m8yww_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"236.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1m8cg1z\" id=\"EndEvent_1m8cg1z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"449\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"467\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16osyai\" id=\"SequenceFlow_16osyai_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"412\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0wmpc10\" id=\"TextAnnotation_0wmpc10_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"257\" x=\"370\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0827dlu\" id=\"Association_0827dlu_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Modify an existing Defender indicator",
      "export_key": "defender_atp_update_indicator",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532256182,
      "name": "Defender Update Indicator",
      "object_type": "defender_indicators",
      "programmatic_name": "defender_atp_update_indicator",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "b5764dd7-1214-4f4c-9c40-67a7b7338f34",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "defender_get_updated_machine_information",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_get_updated_machine_information\" isExecutable=\"true\" name=\"Defender Get Updated Machine Information\"\u003e\u003cdocumentation\u003eRefresh Defender machine information\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02d5zxw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ghg9km\" name=\"Defender Find machines by filter\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3ed5fa56-77c6-464e-b0c2-f5ea81d08370\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\n\\\"\\\"\\\"\\n\\\"value\\\": [\\n    {\\n        \\\"id\\\": \\\"04c99d46599f078f1c3da3783cf5b95f01ac61bb\\\",\\n        \\\"computerDnsName\\\": \\\"\\\",\\n        \\\"firstSeen\\\": \\\"2017-07-06T01:25:04.9480498Z\\\",\\n        \\\"osPlatform\\\": \\\"Windows10\\\",\\n    }\\n]\\n\\\"\\\"\\\"\\nif results.success:\\n    for machine in results.content.get(\u0027value\u0027, []):\\n        row[\u0027report_date\u0027] = now\\n        row[\u0027machine_internal_ip\u0027] = machine[\u0027lastIpAddress\u0027]\\n        row[\u0027machine_ip\u0027] = machine[\u0027lastExternalIpAddress\u0027]\\n        row[\u0027machine_lastseen\u0027] = machine[\u0027lastSeen_ts\u0027]\\n        row[\u0027machine_health_status\u0027] = machine.get(\u0027healthStatus\u0027)\\n        row[\u0027machine_risk_score\u0027] = machine.get(\u0027riskScore\u0027)\\n        row[\u0027machine_exposure_level\u0027] = machine.get(\u0027exposureLevel\u0027)\\n        row[\u0027machine_tags\u0027] = \u0027, \u0027.join(machine.get(\u0027machineTags\u0027, []))\\nelse:\\n  msg = u\\\"Defender find machines by filter unsuccessful\\\\nReason: {}\\\".format(results.reason)\\n  incident.addNote(helper.createPlainText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_filter_name = \\\"filter_by_id\\\"\\ninputs.defender_filter_value = row[\u0027machine_id\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02d5zxw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zuncra\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02d5zxw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ghg9km\"/\u003e\u003cendEvent id=\"EndEvent_1mfpulm\"\u003e\u003cincoming\u003eSequenceFlow_0zuncra\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0zuncra\" sourceRef=\"ServiceTask_1ghg9km\" targetRef=\"EndEvent_1mfpulm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ghg9km\" id=\"ServiceTask_1ghg9km_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"284\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02d5zxw\" id=\"SequenceFlow_02d5zxw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"284\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"241\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1mfpulm\" id=\"EndEvent_1mfpulm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"456\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"474\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zuncra\" id=\"SequenceFlow_0zuncra_di\"\u003e\u003comgdi:waypoint x=\"384\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"420\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Refresh Defender machine information",
      "export_key": "defender_get_updated_machine_information",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636030685239,
      "name": "Defender Get Updated Machine Information",
      "object_type": "defender_machines",
      "programmatic_name": "defender_get_updated_machine_information",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "52ac314a-304f-4a6f-ae51-f343f4742426",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "defender_atp_get_file_information",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_get_file_information\" isExecutable=\"true\" name=\"Defender Get File Information\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get more information about a file based on it\u0027s SHA1 or SHA256 hash]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_143gc3m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_06fhjd4\" name=\"Defender Get File Information\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1121d8e5-07e7-4506-8e87-9badef1cbcae\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.success:\\n    msg = u\\\"Defender Get File Information failed: {}\\\".format(results.reason)\\nelse:\\n    info = [u\\\"{}: {}\\\".format(k, v) for k, v in results.content.items()]\\n    msg = u\\\"Defender Get File Information:\\\\n\\\\n{}\\\".format(\\\"\\\\n\\\".join(info))\\n\\nif artifact.description:\\n    artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, msg)\\nelse:\\n    artifact.description = msg\\n    \\n    \\n\\\"\\\"\\\"\\n{\\n    \\\"@odata.context\\\": \\\"https://api.securitycenter.microsoft.com/api/$metadata#Files/$entity\\\",\\n    \\\"sha1\\\": \\\"4388963aaa83afe2042a46a3c017ad50bdcdafb3\\\",\\n    \\\"sha256\\\": \\\"413c58c8267d2c8648d8f6384bacc2ae9c929b2b96578b6860b5087cd1bd6462\\\",\\n    \\\"globalPrevalence\\\": 180022,\\n    \\\"globalFirstObserved\\\": \\\"2017-09-19T03:51:27.6785431Z\\\",\\n    \\\"globalLastObserved\\\": \\\"2020-01-06T03:59:21.3229314Z\\\",\\n    \\\"size\\\": 22139496,\\n    \\\"fileType\\\": \\\"APP\\\",\\n    \\\"isPeFile\\\": true,\\n    \\\"filePublisher\\\": \\\"CHENGDU YIWO Tech Development Co., Ltd.\\\",\\n    \\\"fileProductName\\\": \\\"EaseUS MobiSaver for Android\\\",\\n    \\\"signer\\\": \\\"CHENGDU YIWO Tech Development Co., Ltd.\\\",\\n    \\\"issuer\\\": \\\"VeriSign Class 3 Code Signing 2010 CA\\\",\\n    \\\"signerHash\\\": \\\"6c3245d4a9bc0244d99dff27af259cbbae2e2d16\\\",\\n    \\\"isValidCertificate\\\": false,\\n    \\\"determinationType\\\": \\\"Pua\\\",\\n    \\\"determinationValue\\\": \\\"PUA:Win32/FusionCore\\\"\\n}\\n\\\"\\\"\\\"\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_file_hash = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_143gc3m\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1cbp0ss\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_143gc3m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_06fhjd4\"/\u003e\u003cendEvent id=\"EndEvent_084ozeq\"\u003e\u003cincoming\u003eSequenceFlow_1cbp0ss\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1cbp0ss\" sourceRef=\"ServiceTask_06fhjd4\" targetRef=\"EndEvent_084ozeq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0i6nq8h\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1smf91i\" sourceRef=\"ServiceTask_06fhjd4\" targetRef=\"TextAnnotation_0i6nq8h\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_06fhjd4\" id=\"ServiceTask_06fhjd4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_143gc3m\" id=\"SequenceFlow_143gc3m_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"243.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_084ozeq\" id=\"EndEvent_084ozeq_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"458\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"476\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cbp0ss\" id=\"SequenceFlow_1cbp0ss_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"458\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"423.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0i6nq8h\" id=\"TextAnnotation_0i6nq8h_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"189\" x=\"395\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1smf91i\" id=\"Association_1smf91i_di\"\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "creator_id": "a@example.com",
      "description": "Get more information about a file based on it\u0027s SHA1 or SHA256 hash",
      "export_key": "defender_atp_get_file_information",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532254776,
      "name": "Defender Get File Information",
      "object_type": "artifact",
      "programmatic_name": "defender_atp_get_file_information",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "c209745d-4d8c-41ea-ae22-0048ca310f76",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "defender_quarantine_file",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_quarantine_file\" isExecutable=\"true\" name=\"Defender Quarantine File\"\u003e\u003cdocumentation\u003eQuarantine a file on a given Defender ATP machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1wasesh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1l4hotc\" name=\"Defender Quarantine File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"656a8125-f55f-4047-a1b8-86e7dc5b05f0\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  row[\u0027report_date\u0027] = now\\n  action_msg = \\\"Action: {}\\\\nComment: {}\\\\nStatus: {}\\\\nStart Date: {}\\\".format(\\n    results.content[\u0027type\u0027],\\n    results.content[\u0027requestorComment\u0027],\\n    results.content[\u0027status\u0027],\\n    results.content[\u0027creationDateTimeUtc\u0027]\\n    )\\n  row[\u0027machine_last_action\u0027] = helper.createPlainText(action_msg)\\nelse:\\n  msg = u\\\"Defender Quarantine File Action {}.\\\\nMachine: {} ({})\\\\nType: {}\\\\nComment: {}\\\\nReason: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           row[\u0027machine_name\u0027], row[\u0027machine_id\u0027],\\n           str(rule.properties.defender_isolation_type),\\n           rule.properties.defender_action_comment,\\n           results.reason)\\n\\n  incident.addNote(helper.createPlainText(msg))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_description = rule.properties.defender_action_comment\\ninputs.defender_indicator_value = row[\u0027machine_file_hash\u0027]\\ninputs.defender_machine_id = row[\u0027machine_id\u0027]\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1wasesh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_04ttxgc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wasesh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1l4hotc\"/\u003e\u003cendEvent id=\"EndEvent_05gfdcs\"\u003e\u003cincoming\u003eSequenceFlow_04ttxgc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_04ttxgc\" sourceRef=\"ServiceTask_1l4hotc\" targetRef=\"EndEvent_05gfdcs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1d133ml\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h09n0s\" sourceRef=\"ServiceTask_1l4hotc\" targetRef=\"TextAnnotation_1d133ml\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1l4hotc\" id=\"ServiceTask_1l4hotc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"271\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wasesh\" id=\"SequenceFlow_1wasesh_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"234.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05gfdcs\" id=\"EndEvent_05gfdcs_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"444\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"462\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04ttxgc\" id=\"SequenceFlow_04ttxgc_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"407.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1d133ml\" id=\"TextAnnotation_1d133ml_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"162\" x=\"352\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h09n0s\" id=\"Association_0h09n0s_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"411\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@example.com",
      "description": "Quarantine a file on a given Defender ATP machine",
      "export_key": "defender_quarantine_file",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636663531537,
      "name": "Defender Quarantine File",
      "object_type": "defender_machines",
      "programmatic_name": "defender_quarantine_file",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "2299d542-4139-4138-9587-f8c900d7b898",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 42,
        "workflow_id": "defender_get_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_get_incident\" isExecutable=\"true\" name=\"Defender Get Incident\"\u003e\u003cdocumentation\u003eGet a Defender 365 Incident by incident id\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0z2vg28\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1l1anvq\" name=\"Defender Get Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9be05644-ed7f-4ada-b2d9-6d8e2c682853\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\n\\ndef mk_mitre_link(technique_list):\\n    links = []\\n    if isinstance(technique_list, list):\\n        for technique in technique_list:\\n            links.append(\u0027\u0026lt;a target=\\\"blank\\\" href=\\\"https://attack.mitre.org/techniques/{}\\\"\u0026gt;{}\u0026lt;/a\u0026gt;\u0027.format(\\n                         technique.replace(\\\".\\\", \\\"/\\\"), technique))\\n                         \\n    return links\\n            \\nnow = Date().getTime()\\n\\nresultz = results\\n\\nif resultz.success:\\n    # get max alert setting\\n    max_alerts = int(resultz.inputs.get(\u0027defender_alert_result_max\u0027, 0))\\n    row_count = 0\\n    machine_list = []\\n    for alert in resultz.content.get(\u0027alerts\u0027, {}):\\n        for device in alert.get(\u0027devices\u0027, {}):\\n            if device[\u0027mdatpDeviceId\u0027] not in machine_list:\\n                machine_list.append(device[\u0027mdatpDeviceId\u0027])\\n                row = incident.addRow(\u0027defender_machines\u0027)\\n                row[\u0027report_date\u0027] = int(Date().getTime())\\n                row[\u0027machine_link\u0027] = \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027https://security.microsoft.com/machines/{}/overview\u0027\u0026gt;Machine\u0026lt;/a\u0026gt;\\\".format(device[\u0027mdatpDeviceId\u0027])\\n                row[\u0027machine_id\u0027] = device[\u0027mdatpDeviceId\u0027]\\n                row[\u0027machine_name\u0027] = device[\u0027deviceDnsName\u0027]\\n                row[\u0027machine_ip\u0027] = device[\u0027lastExternalIpAddress\u0027]\\n                row[\u0027machine_internal_ip\u0027] = device[\u0027lastIpAddress\u0027]\\n                row[\u0027machine_platform\u0027] = device[\u0027osPlatform\u0027]\\n                row[\u0027machine_firstseen\u0027] = device[\u0027firstSeen_ts\u0027]\\n                row[\u0027machine_health_status\u0027] = device.get(\u0027healthStatus\u0027)\\n                row[\u0027machine_risk_score\u0027] = device.get(\u0027riskScore\u0027)\\n                row[\u0027machine_tags\u0027] = \u0027, \u0027.join(device.get(\u0027tags\u0027, []))\\n\\n            if row_count \u0026lt; max_alerts or not max_alerts:\\n                row = incident.addRow(\\\"defender_alerts\\\")\\n                row[\u0027report_date\u0027] = now\\n                row[\u0027alert_link\u0027] = \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027https://security.microsoft.com/alerts/{}\u0027\u0026gt;Alert\u0026lt;/a\u0026gt;\\\".format(alert[\u0027alertId\u0027])\\n                row[\u0027alert_id\u0027] = alert[\u0027alertId\u0027]\\n                row[\u0027assigned_to\u0027] = alert[\u0027assignedTo\u0027]\\n                row[\u0027severity\u0027] = alert[\u0027severity\u0027]\\n                row[\u0027status\u0027] = alert[\u0027status\u0027]\\n                row[\u0027title\u0027] = alert[\u0027title\u0027]\\n                row[\u0027alert_description\u0027] = alert[\u0027description\u0027]\\n                row[\u0027classification\u0027] = alert[\u0027classification\u0027]\\n                row[\u0027determination\u0027] = alert[\u0027determination\u0027]\\n                row[\u0027category\u0027] = alert[\u0027category\u0027]\\n                row[\u0027mitre_techniques\u0027] = str(\u0027, \u0027.join(mk_mitre_link(alert[\u0027mitreTechniques\u0027])))\\n    \\n                # include the machine inform\\n                row[\u0027computer_name\u0027] = device[\u0027deviceDnsName\u0027]\\n                row[\u0027machine_id\u0027] = device[\u0027mdatpDeviceId\u0027]\\n                row[\u0027risk_score\u0027] = device[\u0027riskScore\u0027]\\n                row[\u0027first_seen\u0027] = device[\u0027firstSeen\u0027]\\n            row_count += 1\\n\\nelse:\\n    msg = u\\\"Defender Get Incident unsuccessful.\\\\nReason: {}\\\".format(resultz.reason)\\n    incident.addNote(msg)\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_incident_id = incident.properties.defender_incident_id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0z2vg28\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_04akjnm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0z2vg28\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1l1anvq\"/\u003e\u003cendEvent id=\"EndEvent_1kg1tfe\"\u003e\u003cincoming\u003eSequenceFlow_04akjnm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_04akjnm\" sourceRef=\"ServiceTask_1l1anvq\" targetRef=\"EndEvent_1kg1tfe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16su2o7\"\u003e\u003ctext\u003e\u003c![CDATA[Defender Alert table is updated\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1pyhc5m\" sourceRef=\"ServiceTask_1l1anvq\" targetRef=\"TextAnnotation_16su2o7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1l1anvq\" id=\"ServiceTask_1l1anvq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"260\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z2vg28\" id=\"SequenceFlow_0z2vg28_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"229\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1kg1tfe\" id=\"EndEvent_1kg1tfe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"424\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"442\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04akjnm\" id=\"SequenceFlow_04akjnm_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"392\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16su2o7\" id=\"TextAnnotation_16su2o7_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"238\" x=\"355\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1pyhc5m\" id=\"Association_1pyhc5m_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"137\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 42,
      "creator_id": "a@example.com",
      "description": "Get a Defender 365 Incident by incident id",
      "export_key": "defender_get_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636661723006,
      "name": "Defender Get Incident",
      "object_type": "incident",
      "programmatic_name": "defender_get_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "bc785a1b-4279-48d5-856a-8b577272f159",
      "workflow_id": 77
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "defender_atp_find_machines_by_file_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_find_machines_by_file_hash\" isExecutable=\"true\" name=\"Defender Find Machines by File Hash\"\u003e\u003cdocumentation\u003eFind Defender machines by SHA1 file hash. Results are returned in the Defender Machines datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p9eh4w\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_05yolnv\" name=\"Defender Find Machines by File\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"adcb85db-0dc3-4a63-8875-4f325919dc3d\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n    for machine in results.content.get(\u0027value\u0027, []):\\n        row = incident.addRow(\\\"defender_machines\\\")\\n        row[\u0027report_date\u0027] = now\\n        row[\u0027machine_link\u0027] = \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027https://security.microsoft.com/machines/{}/overview\u0027\u0026gt;Machine\u0026lt;/a\u0026gt;\\\".format(machine[\u0027mdatpDeviceId\u0027])\\n        row[\u0027machine_id\u0027] = machine[\u0027id\u0027]\\n        row[\u0027machine_name\u0027] = machine[\u0027computerDnsName\u0027]\\n        row[\u0027machine_platform\u0027] = machine[\u0027osPlatform\u0027]\\n        row[\u0027machine_firstseen\u0027] = machine[\u0027firstSeen_ts\u0027]\\n        row[\u0027machine_lastseen\u0027] = machine[\u0027lastSeen_ts\u0027]\\n        row[\u0027machine_ip\u0027] = machine[\u0027lastExternalIpAddress\u0027]\\n        row[\u0027machine_internal_ip\u0027] = machine[\u0027lastIpAddress\u0027]\\n        row[\u0027machine_file_hash\u0027] = artifact.value\\n        row[\u0027machine_health_status\u0027] = machine.get(\u0027healthStatus\u0027)\\n        row[\u0027machine_risk_score\u0027] = machine.get(\u0027riskScore\u0027)\\n        row[\u0027machine_exposure_level\u0027] = machine.get(\u0027exposureLevel\u0027)\\n        row[\u0027machine_tags\u0027] = \u0027, \u0027.join(machine.get(\u0027machineTags\u0027, []))\\nelse:\\n    msg = u\\\"Defender Action unsuccessful.\\\\nAction: Find machines by file hash\\\\nReason: {}\\\".format(results.reason)\\n    incident.addNote(helper.createPlainText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_indicator_value = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p9eh4w\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tev9bq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p9eh4w\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_05yolnv\"/\u003e\u003cendEvent id=\"EndEvent_0th3eo9\"\u003e\u003cincoming\u003eSequenceFlow_1tev9bq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tev9bq\" sourceRef=\"ServiceTask_05yolnv\" targetRef=\"EndEvent_0th3eo9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ygjqnv\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the Defender Machine datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0fs2rib\" sourceRef=\"ServiceTask_05yolnv\" targetRef=\"TextAnnotation_0ygjqnv\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_05yolnv\" id=\"ServiceTask_05yolnv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p9eh4w\" id=\"SequenceFlow_0p9eh4w_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0th3eo9\" id=\"EndEvent_0th3eo9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"416\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"434\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tev9bq\" id=\"SequenceFlow_1tev9bq_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ygjqnv\" id=\"TextAnnotation_0ygjqnv_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"174\" x=\"347\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0fs2rib\" id=\"Association_0fs2rib_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"417\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "creator_id": "a@example.com",
      "description": "Find Defender machines by SHA1 file hash. Results are returned in the Defender Machines datatable.",
      "export_key": "defender_atp_find_machines_by_file_hash",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636030913926,
      "name": "Defender Find Machines by File Hash",
      "object_type": "artifact",
      "programmatic_name": "defender_atp_find_machines_by_file_hash",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "123c4514-de3d-475f-ad7e-b04a5ae0f401",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "defender_atp_set_indicator",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_set_indicator\" isExecutable=\"true\" name=\"Defender Set Indicator\"\u003e\u003cdocumentation\u003eSet an indicator on an artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rdnsyf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03n9acz\" name=\"Defender Set Indicator\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"faf52947-0e1a-4e2b-9dfb-ed5ef1605667\"\u003e{\"inputs\":{\"c8b53f87-e1f7-49df-bfaa-5c72c1168d69\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"79c1a5bb-b168-4868-922b-54eb17365f9b\"}},\"0e17bb0b-6ef9-4bac-b3d7-e5e37eaa7ffa\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"a3216414-9c8b-49d4-9714-2b728e14f8c5\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nmsg = u\\\"Defender Action {}.\\\\nAction: {}\\\\nArtifact: {}\\\\nTitle: {}\\\\nComment: {}\\\\nSeverity: {}\\\\nExpiration: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           str(rule.properties.indicator_action),\\n           artifact.value,\\n           rule.properties.indicator_title,\\n           rule.properties.indicator_description,\\n           str(rule.properties.indicator_severity),\\n           rule.properties.indicator_expiration)\\n           \\nif not results.success:\\n    msg = u\\\"{}\\\\nReason: {}\\\".format(msg, results.reason)\\n\\nincident.addNote(msg)\\n\\nif results.success:\\n    row = incident.addRow(\\\"defender_indicators\\\")\\n    row[\u0027report_date\u0027] = Date().getTime()\\n    row[\u0027ind_id\u0027] = results.content[\u0027id\u0027]\\n    row[\u0027ind_value\u0027] = results.content[\u0027indicatorValue\u0027]\\n    row[\u0027ind_type\u0027] = results.content[\u0027indicatorType\u0027]\\n    row[\u0027ind_title\u0027] = results.content[\u0027title\u0027]\\n    row[\u0027ind_description\u0027] = results.content[\u0027description\u0027]\\n    row[\u0027ind_action\u0027] = results.content[\u0027action\u0027]\\n    row[\u0027ind_severity\u0027] = results.content[\u0027severity\u0027]\\n    row[\u0027ind_created_by\u0027] = results.content[\u0027createdByDisplayName\u0027]\\n    row[\u0027ind_creation_date\u0027] = results.content[\u0027creationTimeDateTimeUtc_ts\u0027]\\n    row[\u0027ind_expiration_date\u0027] = results.content[\u0027expirationTime_ts\u0027]\\n    row[\u0027status\u0027] = \u0027Active\u0027\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_indicator_type = artifact.type\\ninputs.defender_indicator_value = artifact.value\\ninputs.defender_description = rule.properties.indicator_description\\ninputs.defender_expiration_time = rule.properties.indicator_expiration\\ninputs.defender_title = rule.properties.indicator_title\\ninputs.defender_severity = str(rule.properties.indicator_severity)\\ninputs.defender_indicator_action = str(rule.properties.indicator_action)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rdnsyf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0r0i2ak\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0rdnsyf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03n9acz\"/\u003e\u003cendEvent id=\"EndEvent_0z3geyv\"\u003e\u003cincoming\u003eSequenceFlow_0r0i2ak\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0r0i2ak\" sourceRef=\"ServiceTask_03n9acz\" targetRef=\"EndEvent_0z3geyv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0njcuna\"\u003e\u003ctext\u003e\u003c![CDATA[Adds a row to the Defender Indicators datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0prfwhg\" sourceRef=\"ServiceTask_03n9acz\" targetRef=\"TextAnnotation_0njcuna\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03n9acz\" id=\"ServiceTask_03n9acz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"264\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rdnsyf\" id=\"SequenceFlow_0rdnsyf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"231\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0z3geyv\" id=\"EndEvent_0z3geyv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"450\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"468\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r0i2ak\" id=\"SequenceFlow_0r0i2ak_di\"\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"450\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"407\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0njcuna\" id=\"TextAnnotation_0njcuna_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"195\" x=\"350\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0prfwhg\" id=\"Association_0prfwhg_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Set an indicator on an artifact",
      "export_key": "defender_atp_set_indicator",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532256635,
      "name": "Defender Set Indicator",
      "object_type": "artifact",
      "programmatic_name": "defender_atp_set_indicator",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "7c81cda4-39a6-4071-b1d9-26da710d0526",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 16,
        "workflow_id": "defender_atp_find_machines",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_find_machines\" isExecutable=\"true\" name=\"Defender Find Machines by Internal IP Address\"\u003e\u003cdocumentation\u003eFind Machines by internal IP address. Results returned in Defender Machines datatable\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0fpszeo\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ass6wf\" name=\"Defender Find Machines by Interna...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"11f82831-e4a8-4764-8ccd-f303c63caaf4\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\n\\\"\\\"\\\"\\n\\\"value\\\": [\\n    {\\n        \\\"id\\\": \\\"04c99d46599f078f1c3da3783cf5b95f01ac61bb\\\",\\n        \\\"computerDnsName\\\": \\\"\\\",\\n        \\\"firstSeen\\\": \\\"2017-07-06T01:25:04.9480498Z\\\",\\n        \\\"osPlatform\\\": \\\"Windows10\\\",\\n    }\\n]\\n\\\"\\\"\\\"\\nif results.success:\\n  if not results.content[\u0027value\u0027]:\\n    msg = u\\\"Defender ATP Find machines by Internal IP Address unsuccessful.\\\\nNothing found for {}\\\".format(artifact.value)\\n    incident.addNote(helper.createPlainText(msg))\\n  else:\\n    for machine in results.content[\u0027value\u0027]:\\n        row = incident.addRow(\\\"defender_machines\\\")\\n        row[\u0027report_date\u0027] = now\\n        row[\u0027machine_link\u0027] = \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027https://security.microsoft.com/machines/{}/overview\u0027\u0026gt;Machine\u0026lt;/a\u0026gt;\\\".format(machine[\u0027mdatpDeviceId\u0027])\\n        row[\u0027machine_id\u0027] = machine[\u0027id\u0027]\\n        row[\u0027machine_ip\u0027] = machine[\u0027lastExternalIpAddress\u0027]\\n        row[\u0027machine_internal_ip\u0027] = machine[\u0027lastIpAddress\u0027]\\n        row[\u0027machine_name\u0027] = machine[\u0027computerDnsName\u0027]\\n        row[\u0027machine_platform\u0027] = machine[\u0027osPlatform\u0027]\\n        row[\u0027machine_firstseen\u0027] = machine[\u0027firstSeen_ts\u0027]\\n        row[\u0027machine_lastseen\u0027] = machine[\u0027lastSeen_ts\u0027]\\n        row[\u0027machine_health_status\u0027] = machine.get(\u0027healthStatus\u0027)\\n        row[\u0027machine_risk_score\u0027] = machine.get(\u0027riskScore\u0027)\\n        row[\u0027machine_exposure_level\u0027] = machine.get(\u0027exposureLevel\u0027)\\n        row[\u0027machine_tags\u0027] = \u0027, \u0027.join(machine.get(\u0027machineTags\u0027, []))\\nelse:\\n    msg = u\\\"Defender Action unsuccessful.\\\\nAction: Find machines by Internal IP Address\\\\nReason: {}\\\".format(results.reason)\\n    incident.addNote(helper.createPlainText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_indicator_value = artifact.value\\ninputs.defender_lookback_timeframe = rule.properties.defender_lookback_timeframe\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fpszeo\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_00r14wq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fpszeo\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ass6wf\"/\u003e\u003cendEvent id=\"EndEvent_1oagaje\"\u003e\u003cincoming\u003eSequenceFlow_00r14wq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_00r14wq\" sourceRef=\"ServiceTask_1ass6wf\" targetRef=\"EndEvent_1oagaje\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1t7jpqu\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in Defender Machine datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1lg7u8d\" sourceRef=\"ServiceTask_1ass6wf\" targetRef=\"TextAnnotation_1t7jpqu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ass6wf\" id=\"ServiceTask_1ass6wf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"268\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fpszeo\" id=\"SequenceFlow_0fpszeo_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"268\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"233\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1oagaje\" id=\"EndEvent_1oagaje_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"431\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"449\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00r14wq\" id=\"SequenceFlow_00r14wq_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"399.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1t7jpqu\" id=\"TextAnnotation_1t7jpqu_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"170\" x=\"358\" y=\"87\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1lg7u8d\" id=\"Association_1lg7u8d_di\"\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"137\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 16,
      "creator_id": "a@example.com",
      "description": "Find Machines by internal IP address. Results returned in Defender Machines datatable",
      "export_key": "defender_atp_find_machines",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636030798676,
      "name": "Defender Find Machines by Internal IP Address",
      "object_type": "artifact",
      "programmatic_name": "defender_atp_find_machines",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "0e24252b-bfe6-4576-b9b7-ea7d8eb2d260",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "defender_atp_delete_indicator",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_delete_indicator\" isExecutable=\"true\" name=\"Defender Delete Indicator\"\u003e\u003cdocumentation\u003eRemove an indicator from Defender ATP\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tvjnhc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0g9n58t\" name=\"Defender Delete Indicator\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f13cf24d-612b-47c7-aa51-3748d3c3520e\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\n\\nmsg = u\\\"Defender Action {}.\\\\nAction: Delete Indicator\\\\nIndicator: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           row[\u0027ind_value\u0027],\\n           )\\n           \\nif results.success:\\n  row[\u0027report_date\u0027] = Date().getTime()\\n  row[\u0027status\u0027] = \u0027Inactive\u0027\\nelse:\\n  msg = u\\\"{}\\\\nReason: {}\\\".format(msg, results.reason)\\n\\nincident.addNote(helper.createPlainText(msg))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_indicator_id = row[\u0027ind_id\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tvjnhc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wb4sn4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tvjnhc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0g9n58t\"/\u003e\u003cendEvent id=\"EndEvent_0lvmxfm\"\u003e\u003cincoming\u003eSequenceFlow_0wb4sn4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wb4sn4\" sourceRef=\"ServiceTask_0g9n58t\" targetRef=\"EndEvent_0lvmxfm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10npj1n\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0y4nfg5\" sourceRef=\"ServiceTask_0g9n58t\" targetRef=\"TextAnnotation_10npj1n\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0g9n58t\" id=\"ServiceTask_0g9n58t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tvjnhc\" id=\"SequenceFlow_1tvjnhc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"238.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lvmxfm\" id=\"EndEvent_0lvmxfm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"449\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"467\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wb4sn4\" id=\"SequenceFlow_0wb4sn4_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"449\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"414\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10npj1n\" id=\"TextAnnotation_10npj1n_di\"\u003e\u003comgdc:Bounds height=\"47\" width=\"171\" x=\"369\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0y4nfg5\" id=\"Association_0y4nfg5_di\"\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Remove an indicator from Defender ATP",
      "export_key": "defender_atp_delete_indicator",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532255944,
      "name": "Defender Delete Indicator",
      "object_type": "defender_indicators",
      "programmatic_name": "defender_atp_delete_indicator",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "bc4c92be-854c-4fa4-a13c-6a0d4550d5ff",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "defender_atp_machine_vulnerabilities",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_machine_vulnerabilities\" isExecutable=\"true\" name=\"Defender Machine Vulnerabilities\"\u003e\u003cdocumentation\u003eGet Defender machine vulnerabilities\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0w27m0u\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zisxlv\" name=\"Defender Machine Vulnerabilities\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b0e17c3e-ef30-46ed-bb0b-3862990314ed\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\n [\\n        {\\n            \\\"id\\\": \\\"CVE-2019-1348\\\",\\n            \\\"name\\\": \\\"CVE-2019-1348\\\",\\n            \\\"description\\\": \\\"Git could allow a remote attacker to bypass security restrictions, caused by a flaw in the --export-marks option of git fast-import. By persuading a victim to import specially-crafted content, an attacker could exploit this vulnerability to overwrite arbitrary paths.\\\",\\n            \\\"severity\\\": \\\"Medium\\\",\\n            \\\"cvssV3\\\": 4.3,\\n            \\\"exposedMachines\\\": 1,\\n            \\\"publishedOn\\\": \\\"2019-12-13T00:00:00Z\\\",\\n            \\\"updatedOn\\\": \\\"2019-12-13T00:00:00Z\\\",\\n            \\\"publicExploit\\\": False,\\n            \\\"exploitVerified\\\": False,\\n            \\\"exploitInKit\\\": False,\\n            \\\"exploitTypes\\\": [],\\n            \\\"exploitUris\\\": []\\n        },\\n        {\\n            \\\"id\\\": \\\"CVE-2019-1348\\\",\\n            \\\"name\\\": \\\"CVE-2019-1348-2\\\",\\n            \\\"description\\\": \\\"Git could allow a remote attacker to bypass security restrictions, caused by a flaw in the --export-marks option of git fast-import. By persuading a victim to import specially-crafted content, an attacker could exploit this vulnerability to overwrite arbitrary paths.\\\",\\n            \\\"severity\\\": \\\"Medium\\\",\\n            \\\"cvssV3\\\": 4.3,\\n            \\\"exposedMachines\\\": 1,\\n            \\\"publishedOn\\\": \\\"2019-12-13T00:00:00Z\\\",\\n            \\\"updatedOn\\\": \\\"2019-12-13T00:00:00Z\\\",\\n            \\\"publicExploit\\\": False,\\n            \\\"exploitVerified\\\": False,\\n            \\\"exploitInKit\\\": False,\\n            \\\"exploitTypes\\\": [],\\n            \\\"exploitUris\\\": []\\n        }\\n    ]\\n\\\"\\\"\\\"\\n\\n\\ndef mk_note(list_of_notes):\\n    return \\\"\u0026lt;br\u0026gt;---\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".join([\\\"\u0026lt;br\u0026gt;\\\".join(note) for note in list_of_notes])\\n\\ndef format_line(k, v):\\n    return \\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(k, v)\\n\\nvulnerabilities = results.content.get(\u0027value\u0027, [])\\nif results[\u0027success\u0027]:\\n    if not vulnerabilities:\\n        incident.addNote(\\\"Defender No machine vulnerabilities for: {}\\\".format(row[\u0027machine_name\u0027]))\\n    else:\\n        note = []\\n        for risk in vulnerabilities:\\n            note_info = [\\\"Defender Machine Vulnerabilities:\\\"]\\n            note_info.append(format_line(\\\"Machine\\\", row[\u0027machine_name\u0027]))\\n            note_info.append(format_line(\\\"Machine Id\\\", row[\u0027machine_id\u0027]))\\n            note_info.append(format_line(\\\"Vulnerability\\\", risk[\u0027name\u0027]))\\n            note_info.append(format_line(\\\"Description\\\", risk[\u0027description\u0027]))\\n            note_info.append(format_line(\\\"Severity\\\", risk[\u0027severity\u0027]))\\n            note_info.append(format_line(\\\"Published\\\", risk[\u0027publishedOn\u0027]))\\n            note_info.append(format_line(\\\"Updated\\\", risk[\u0027updatedOn\u0027]))\\n    \\n            note.append(note_info)\\n        incident.addNote(helper.createRichText(mk_note(note)))\\nelse:\\n    incident.addNote(\\\"Defender Machine Vulnerabilities failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_machine_id = row[\u0027machine_id\u0027]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0w27m0u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gely5i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0w27m0u\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zisxlv\"/\u003e\u003cendEvent id=\"EndEvent_1nhwyxe\"\u003e\u003cincoming\u003eSequenceFlow_1gely5i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1gely5i\" sourceRef=\"ServiceTask_0zisxlv\" targetRef=\"EndEvent_1nhwyxe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1jpdcnq\"\u003e\u003ctext\u003eResults returned in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1njp61g\" sourceRef=\"ServiceTask_0zisxlv\" targetRef=\"TextAnnotation_1jpdcnq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zisxlv\" id=\"ServiceTask_0zisxlv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"273\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w27m0u\" id=\"SequenceFlow_0w27m0u_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"273\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"235.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nhwyxe\" id=\"EndEvent_1nhwyxe_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"448\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"466\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gely5i\" id=\"SequenceFlow_1gely5i_di\"\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1jpdcnq\" id=\"TextAnnotation_1jpdcnq_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"197\" x=\"356\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1njp61g\" id=\"Association_1njp61g_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Get Defender machine vulnerabilities",
      "export_key": "defender_atp_machine_vulnerabilities",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532254897,
      "name": "Defender Machine Vulnerabilities",
      "object_type": "defender_machines",
      "programmatic_name": "defender_atp_machine_vulnerabilities",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "1ac26ae2-bae4-41c5-ba50-c0aa44a54e64",
      "workflow_id": 86
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "defender_atp_collect_machine_investigation_package",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_collect_machine_investigation_package\" isExecutable=\"true\" name=\"Defender Collect Machine Investigation Package\"\u003e\u003cdocumentation\u003eStart a process to collect an investigation report\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15fnm73\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zt2o7y\" name=\"Defender Collect Machine Investig...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bfa88004-c394-4504-92ad-d3e1cb717b20\"\u003e{\"inputs\":{},\"post_processing_script\":\"import java.util.Date as Date\\nnow = Date().getTime()\\n\\nif results.success:\\n  msg = \\\"Action: {}\\\\nComment: {}\\\\nStatus: {}\\\\nStart Date: {}\\\".format(\\n    results.content[\u0027type\u0027],\\n    results.content[\u0027requestorComment\u0027],\\n    results.content[\u0027status\u0027],\\n    results.content[\u0027creationDateTimeUtc\u0027]\\n    )\\n  row[\u0027machine_last_action\u0027] = helper.createPlainText(msg)\\n  row[\u0027report_date\u0027] = now\\n  \\n\\\"\\\"\\\"\\n    \u0027type\u0027: \u0027CollectInvestigationPackage\u0027,\\n    \u0027title\u0027: None,\\n    \u0027requestor\u0027: \u0027f0dc3f88-f617-449c-960c-6b54818cd110\u0027,\\n    \u0027requestorComment\u0027: \u0027ss\u0027,\\n    \u0027status\u0027: \u0027Succeeded\u0027,\\n    \u0027machineId\u0027: \u00272a94aaf80aa31094790ce40da6fdfc03a9a145c5\u0027,\\n    \u0027computerDnsName\u0027: \u0027windowsvmos\u0027,\\n    \u0027creationDateTimeUtc\u0027: \u00272021-08-12T18:53:06.5259227Z\u0027,\\n    \u0027lastUpdateDateTimeUtc\u0027: \u00272021-08-12T18:54:20.4259984Z\u0027,\\n\\\"\\\"\\\"\\n  \",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_machine_id = row[\u0027machine_id\u0027]\\ninputs.defender_description = rule.properties.defender_action_comment\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15fnm73\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_05j8mjf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15fnm73\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zt2o7y\"/\u003e\u003cendEvent id=\"EndEvent_0nl0i8a\"\u003e\u003cincoming\u003eSequenceFlow_05j8mjf\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_05j8mjf\" sourceRef=\"ServiceTask_0zt2o7y\" targetRef=\"EndEvent_0nl0i8a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ntlx1f\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Defender ATP Machines datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0yjv0vh\" sourceRef=\"ServiceTask_0zt2o7y\" targetRef=\"TextAnnotation_1ntlx1f\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zt2o7y\" id=\"ServiceTask_0zt2o7y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15fnm73\" id=\"SequenceFlow_15fnm73_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nl0i8a\" id=\"EndEvent_0nl0i8a_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"458\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"476\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05j8mjf\" id=\"SequenceFlow_05j8mjf_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"458\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"416\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ntlx1f\" id=\"TextAnnotation_1ntlx1f_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"204\" x=\"362\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0yjv0vh\" id=\"Association_0yjv0vh_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"134\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Start a process to collect an investigation report",
      "export_key": "defender_atp_collect_machine_investigation_package",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532256306,
      "name": "Defender Collect Machine Investigation Package",
      "object_type": "defender_machines",
      "programmatic_name": "defender_atp_collect_machine_investigation_package",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "a0b66455-8de8-4c99-be15-1b75a1c0e72e",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "defender_atp_app_execution",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_atp_app_execution\" isExecutable=\"true\" name=\"Defender App Execution Restriction\"\u003e\u003cdocumentation\u003eRestrict/un-restrict App execution on a Defender managed machine\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1uaynxc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_010kd60\" name=\"Defender App Execution\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"92906dbe-9be4-4277-8f50-c6f15fb5dcbc\"\u003e{\"inputs\":{\"b35bd7fe-d52a-483e-ab06-16f8131ce093\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"c099160c-f83c-461d-9b8e-4d0edd66716d\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nnow = Date().getTime()\\n\\nmsg = u\\\"Defender Action {}.\\\\nAction: {}\\\\nMachine: {}\\\\nComment: {}\\\"\\\\\\n   .format(\\\"successful\\\" if results.success else \\\"unsuccessful\\\",\\n           rule.properties.defender_app_execution_action,\\n           row[\u0027machine_id\u0027],\\n           rule.properties.defender_action_comment)\\n           \\nif results.success:\\n  row[\u0027report_date\u0027] = now\\n  action_msg = \\\"Action: {}\\\\nComment: {}\\\\nStatus: {}\\\\nStart Date: {}\\\".format(\\n    results.content[\u0027type\u0027],\\n    results.content[\u0027requestorComment\u0027],\\n    results.content[\u0027status\u0027],\\n    results.content[\u0027creationDateTimeUtc\u0027]\\n    )\\n  row[\u0027machine_last_action\u0027] = helper.createPlainText(action_msg)\\nelse:\\n  msg = u\\\"{}\\\\nReason: {}\\\".format(msg, results.reason)\\n\\nincident.addNote(helper.createPlainText(msg))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_description = rule.properties.defender_action_comment\\ninputs.defender_machine_id = row[\u0027machine_id\u0027]\\ninputs.defender_restriction_type = str(rule.properties.defender_app_execution_action)\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1uaynxc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xrr3iw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1uaynxc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_010kd60\"/\u003e\u003cendEvent id=\"EndEvent_15voo0u\"\u003e\u003cincoming\u003eSequenceFlow_0xrr3iw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0xrr3iw\" sourceRef=\"ServiceTask_010kd60\" targetRef=\"EndEvent_15voo0u\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rdpuzw\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_001o3hz\" sourceRef=\"ServiceTask_010kd60\" targetRef=\"TextAnnotation_1rdpuzw\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_010kd60\" id=\"ServiceTask_010kd60_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uaynxc\" id=\"SequenceFlow_1uaynxc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_15voo0u\" id=\"EndEvent_15voo0u_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"429\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"447\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xrr3iw\" id=\"SequenceFlow_0xrr3iw_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"429\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"400.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rdpuzw\" id=\"TextAnnotation_1rdpuzw_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"152\" x=\"369\" y=\"84\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_001o3hz\" id=\"Association_001o3hz_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Restrict/un-restrict App execution on a Defender managed machine",
      "export_key": "defender_atp_app_execution",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532255708,
      "name": "Defender App Execution Restriction",
      "object_type": "defender_machines",
      "programmatic_name": "defender_atp_app_execution",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "5e9ea009-7afd-4394-882a-15609bffa82d",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "defender_list_indicators",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_list_indicators\" isExecutable=\"true\" name=\"Defender List Indicators\"\u003e\u003cdocumentation\u003eGet a list of the indicators defined in Defender.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1jfth66\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_01kd4oz\" name=\"Defender List Indicators\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e866e9-9c78-41d7-b13d-4feea72d59b7\"\u003e{\"inputs\":{\"83ef8d59-9b4a-405a-bc7b-2978a214bdbf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"15ca01c7-cab9-44d7-b9b8-7506130a43f1\"}}},\"post_processing_script\":\"import java.util.Date as Date\\n\\nif results.success and results.content.get(\\\"value\\\"):\\n    for indicator in results.content.get(\\\"value\\\"):\\n        row = incident.addRow(\\\"defender_indicators\\\")\\n        row[\u0027report_date\u0027] = Date().getTime()\\n        row[\u0027ind_id\u0027] = indicator[\u0027id\u0027]\\n        row[\u0027ind_value\u0027] = indicator[\u0027indicatorValue\u0027]\\n        row[\u0027ind_type\u0027] = indicator[\u0027indicatorType\u0027]\\n        row[\u0027ind_title\u0027] = indicator[\u0027title\u0027]\\n        row[\u0027ind_description\u0027] = indicator[\u0027description\u0027]\\n        row[\u0027ind_action\u0027] = indicator[\u0027action\u0027]\\n        row[\u0027ind_severity\u0027] = indicator[\u0027severity\u0027]\\n        row[\u0027ind_created_by\u0027] = indicator[\u0027createdByDisplayName\u0027]\\n        row[\u0027ind_creation_date\u0027] = indicator[\u0027creationTimeDateTimeUtc_ts\u0027]\\n        row[\u0027ind_expiration_date\u0027] = indicator[\u0027expirationTime_ts\u0027]\\n        row[\u0027status\u0027] = \u0027Active\u0027\\nelse:\\n    msg = u\\\"Defender ATP Action unsuccessful.\\\\nAction: List indicators\\\\nReason: {}\\\".format(results.reason)\\n    incident.addNote(msg)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.defender_indicator_filter = rule.properties.defender_indicator_filter if rule.properties.get(\u0027defender_indicator_filter\u0027) else None\\ninputs.defender_indicator_field = rule.properties.defender_indicator_field if rule.properties.get(\u0027defender_indicator_field\u0027) else None\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1jfth66\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0nljrkv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1jfth66\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01kd4oz\"/\u003e\u003cendEvent id=\"EndEvent_06bj4jw\"\u003e\u003cincoming\u003eSequenceFlow_0nljrkv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0nljrkv\" sourceRef=\"ServiceTask_01kd4oz\" targetRef=\"EndEvent_06bj4jw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14xpgky\"\u003e\u003ctext\u003e\u003c![CDATA[Results presented in the Defender datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cy0g4l\" sourceRef=\"ServiceTask_01kd4oz\" targetRef=\"TextAnnotation_14xpgky\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01kd4oz\" id=\"ServiceTask_01kd4oz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"260\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jfth66\" id=\"SequenceFlow_1jfth66_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"229\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06bj4jw\" id=\"EndEvent_06bj4jw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0nljrkv\" id=\"SequenceFlow_0nljrkv_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14xpgky\" id=\"TextAnnotation_14xpgky_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"204\" x=\"351\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cy0g4l\" id=\"Association_1cy0g4l_di\"\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"414\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Get a list of the indicators defined in Defender.",
      "export_key": "defender_list_indicators",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1636658282347,
      "name": "Defender List Indicators",
      "object_type": "incident",
      "programmatic_name": "defender_list_indicators",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "fe689986-cc3a-4f35-918a-a33de3286365",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "defender_sync_comment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"defender_sync_comment\" isExecutable=\"true\" name=\"Defender Sync Comment\"\u003e\u003cdocumentation\u003eSync Defender Incident with new IBM SOAR comments\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0n3t7gr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_07fyxkv\" name=\"Defender Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"af506727-09ad-4997-b2fd-8c81eb1d2ea7\"\u003e{\"inputs\":{\"18d59d14-35ca-46e9-a571-2f0b0e45ff8a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"d316fcc8-94b7-40b1-856f-b9408f8f78b0\"}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.defender_incident_id = incident.properties.defender_incident_id\\ninputs.defender_classification = incident.properties.defender_classification\\ninputs.defender_determination = incident.properties.defender_determination\\ninputs.defender_comment = note.text.content\\ninputs.defender_tags = incident.properties.defender_tags\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0n3t7gr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c2w6ny\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0n3t7gr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_07fyxkv\"/\u003e\u003cendEvent id=\"EndEvent_1k4hid3\"\u003e\u003cincoming\u003eSequenceFlow_0c2w6ny\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c2w6ny\" sourceRef=\"ServiceTask_07fyxkv\" targetRef=\"EndEvent_1k4hid3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1spek6h\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_00eq191\" sourceRef=\"ServiceTask_07fyxkv\" targetRef=\"TextAnnotation_1spek6h\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_07fyxkv\" id=\"ServiceTask_07fyxkv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0n3t7gr\" id=\"SequenceFlow_0n3t7gr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1k4hid3\" id=\"EndEvent_1k4hid3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"452\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"470\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c2w6ny\" id=\"SequenceFlow_0c2w6ny_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"415\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1spek6h\" id=\"TextAnnotation_1spek6h_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"189\" x=\"380\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_00eq191\" id=\"Association_00eq191_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@example.com",
      "description": "Sync Defender Incident with new IBM SOAR comments",
      "export_key": "defender_sync_comment",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1635532255014,
      "name": "Defender Sync Comment",
      "object_type": "note",
      "programmatic_name": "defender_sync_comment",
      "tags": [
        {
          "tag_handle": "fn_microsoft_defender",
          "value": null
        }
      ],
      "uuid": "6c3fcd14-7827-42ef-a2f4-aad69a7cf0ef",
      "workflow_id": 81
    }
  ],
  "workspaces": []
}
