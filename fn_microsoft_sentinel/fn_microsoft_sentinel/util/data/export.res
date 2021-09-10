{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinel_incident_number",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.user_id",
          "method": "in",
          "type": null,
          "value": [
            "a@example.com"
          ]
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
      "export_key": "Sentinel Comment Sync",
      "id": 130,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Sentinel Comment Sync",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "8ef219a9-798d-40f2-9005-d6dc5c2246c5",
      "view_items": [],
      "workflows": [
        "sentinel_comment_sync"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinel_incident_number",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Sentinel Get Incident Alerts",
      "id": 168,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Sentinel Get Incident Alerts",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3a3ca131-3665-442d-8b92-d04870889991",
      "view_items": [],
      "workflows": [
        "sentinel_get_incident_alerts"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinel_incident_number",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Sentinel Get Incident Comments",
      "id": 131,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Sentinel Get Incident Comments",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "675b4011-ad16-41b5-ba8a-eb45492b0b3a",
      "view_items": [],
      "workflows": [
        "sentinel_get_incident_comments"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinel_incident_number",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Sentinel Get Incident Entities",
      "id": 132,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Sentinel Get Incident Entities",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2b464269-54d1-4c50-b654-f78f1c8e2509",
      "view_items": [],
      "workflows": [
        "sentinel_get_incident_entities"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sentinel_incident_number",
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
      "export_key": "Sentinel Incident Sync",
      "id": 133,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Sentinel Incident Sync",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "33510935-6a9b-41b7-8ea9-752318cdb096",
      "view_items": [],
      "workflows": [
        "sentinel_get_incident_alerts",
        "sentinel_get_incident_entities"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": 1,
          "field_name": "incident.description",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 2,
          "field_name": "incident.name",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 6,
          "field_name": "incident.properties.sentinel_incident_number",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 3,
          "field_name": "incident.resolution_id",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 4,
          "field_name": "incident.resolution_summary",
          "method": "changed",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": 5,
          "field_name": "incident.severity_code",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "custom_condition": "6 AND (1 OR 2 OR 3 OR 4 OR 5)",
      "enabled": true,
      "export_key": "Sentinel Update Incident",
      "id": 134,
      "logic_type": "advanced",
      "message_destinations": [
        "fn_microsoft_sentinel"
      ],
      "name": "Sentinel Update Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "510a6409-ac5c-4846-a29a-042de327093e",
      "view_items": [],
      "workflows": []
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1631299576654,
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
      "export_key": "__function/sentinel_incident_id",
      "hide_notification": false,
      "id": 716,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "sentinel_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b39c86f1-d5de-40f9-886a-054304aa9b22",
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
      "export_key": "__function/sentinel_incident_comment",
      "hide_notification": false,
      "id": 717,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "sentinel_incident_comment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b496b255-913e-4898-8146-72401be0fb7e",
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
      "export_key": "__function/sentinel_profile",
      "hide_notification": false,
      "id": 718,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_profile",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "sentinel_profile",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
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
      "id": 230,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Resilient Incident ID",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        },
        {
          "tag_handle": "fn_remedy",
          "value": null
        },
        {
          "tag_handle": "fn_scheduler",
          "value": null
        },
        {
          "tag_handle": "fn_urlscanio",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "IncidentID",
      "type_id": 11,
      "uuid": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
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
      "export_key": "incident/sentinel_incident_classification_comment",
      "hide_notification": false,
      "id": 699,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_classification_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Classification Comment",
      "tooltip": "",
      "type_id": 0,
      "uuid": "aa039b8d-bd8d-4ba3-ad18-863a5e37fc0b",
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
      "export_key": "incident/sentinel_incident_assigned_to",
      "hide_notification": false,
      "id": 700,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_assigned_to",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Assigned To",
      "tooltip": "",
      "type_id": 0,
      "uuid": "c34e6ac7-cdcf-4de3-a1ad-e472928b0a66",
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
      "export_key": "incident/sentinel_incident_classification",
      "hide_notification": false,
      "id": 701,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_classification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Classification",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e06a30d5-3015-4f8c-844c-8d37d409126a",
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
      "export_key": "incident/sentinel_incident_status",
      "hide_notification": false,
      "id": 702,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "e6710b80-81bb-49ba-a121-7a33488f6046",
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
      "export_key": "incident/sentinel_incident_classification_reason",
      "hide_notification": false,
      "id": 703,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_classification_reason",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Classification Reason",
      "tooltip": "",
      "type_id": 0,
      "uuid": "f8ff2574-1cfd-4af5-8d8f-f7126c7dc78e",
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
      "export_key": "incident/sentinel_incident_number",
      "hide_notification": false,
      "id": 720,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_number",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Number",
      "tooltip": "",
      "type_id": 0,
      "uuid": "f9f36a0d-7bec-4383-ab72-40283116c104",
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
      "export_key": "incident/sentinel_incident_id",
      "hide_notification": false,
      "id": 704,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "1bae2697-feb5-48a8-8792-e2a0698adebb",
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
      "export_key": "incident/sentinel_incident_tactics",
      "hide_notification": false,
      "id": 705,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_tactics",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Tactics",
      "tooltip": "",
      "type_id": 0,
      "uuid": "2d748cf6-d484-47c5-8074-4092cd551540",
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
      "export_key": "incident/sentinel_profile",
      "hide_notification": false,
      "id": 706,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_profile",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Profile",
      "tooltip": "",
      "type_id": 0,
      "uuid": "2fa680d9-d625-48bf-973f-48834d5ea47b",
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
      "export_key": "incident/sentinel_incident_url",
      "hide_notification": false,
      "id": 707,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident URL",
      "tooltip": "",
      "type_id": 0,
      "uuid": "353dbf6a-b077-4813-8660-5313c801c903",
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
      "export_key": "incident/sentinel_incident_labels",
      "hide_notification": false,
      "id": 708,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sentinel_incident_labels",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sentinel Incident Labels",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7c63205c-6dab-40e4-8924-028f00b21c27",
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
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create a comment for a given Sentinel incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_sentinel",
      "display_name": "Sentinel Add Incident Comment",
      "export_key": "sentinel_add_incident_comment",
      "id": 95,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1628254059483,
      "name": "sentinel_add_incident_comment",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "1c88215e-970d-49bc-97ce-e914ffa63b3f",
      "version": 2,
      "view_items": [
        {
          "content": "b39c86f1-d5de-40f9-886a-054304aa9b22",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b496b255-913e-4898-8146-72401be0fb7e",
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
          "name": "Sentinel Comment Sync",
          "object_type": "note",
          "programmatic_name": "sentinel_comment_sync",
          "tags": [
            {
              "tag_handle": "fn_microsoft_sentinel",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 121
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
        "content": "Sentinel Get Incident Alerts",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_sentinel",
      "display_name": "Sentinel Get Incident Alerts",
      "export_key": "sentinel_get_incident_alerts",
      "id": 125,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1629303337399,
      "name": "sentinel_get_incident_alerts",
      "tags": [],
      "uuid": "3cc8ebb2-b61f-449a-a7fb-efc3350f755c",
      "version": 1,
      "view_items": [
        {
          "content": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b39c86f1-d5de-40f9-886a-054304aa9b22",
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
          "name": "Sentinel Get Incident Alerts",
          "object_type": "incident",
          "programmatic_name": "sentinel_get_incident_alerts",
          "tags": [],
          "uuid": null,
          "workflow_id": 154
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
        "content": "Get Comments from a Sentinel Incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_sentinel",
      "display_name": "Sentinel Get Incident Comments",
      "export_key": "sentinel_get_incident_comments",
      "id": 96,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1630431025978,
      "name": "sentinel_get_incident_comments",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "5753fe01-6c13-404b-9df2-e1308c3a1f04",
      "version": 5,
      "view_items": [
        {
          "content": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b39c86f1-d5de-40f9-886a-054304aa9b22",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
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
          "name": "Sentinel Get Incident Comments",
          "object_type": "incident",
          "programmatic_name": "sentinel_get_incident_comments",
          "tags": [
            {
              "tag_handle": "fn_microsoft_sentinel",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 123
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
        "content": "Get the Entities associated with a Sentinel Incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_sentinel",
      "display_name": "Sentinel Get Incident Entities",
      "export_key": "sentinel_get_incident_entities",
      "id": 97,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1628254059483,
      "name": "sentinel_get_incident_entities",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "92ff2bad-f427-472f-bca1-f071d687fbb5",
      "version": 2,
      "view_items": [
        {
          "content": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b39c86f1-d5de-40f9-886a-054304aa9b22",
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
          "name": "Sentinel Get Incident Entities",
          "object_type": "incident",
          "programmatic_name": "sentinel_get_incident_entities",
          "tags": [
            {
              "tag_handle": "fn_microsoft_sentinel",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 120
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
        "content": "Update / Close a Sentinel incident based on Sentinel field changes in the Resilient Incident",
        "format": "text"
      },
      "destination_handle": "fn_microsoft_sentinel",
      "display_name": "Sentinel Update Incident",
      "export_key": "sentinel_update_incident",
      "id": 98,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1630431025978,
      "name": "sentinel_update_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "e41efc23-c78d-4215-8a77-dfb68eca0548",
      "version": 5,
      "view_items": [
        {
          "content": "5eaaeb87-cb70-4877-aa5e-0a5b10f73f3a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b39c86f1-d5de-40f9-886a-054304aa9b22",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c25bfde8-219e-4ceb-ae63-4926ced321fc",
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
          "name": "Sentinel Update Incident",
          "object_type": "incident",
          "programmatic_name": "sentinel_update_incident",
          "tags": [
            {
              "tag_handle": "fn_microsoft_sentinel",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 122
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 127,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1631299575281,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1631299575281,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "deb9f4fb-1cdd-4b87-a267-8ec480cf9b12"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_microsoft_sentinel",
      "name": "fn_microsoft_sentinel",
      "programmatic_name": "fn_microsoft_sentinel",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "2aa1bbb1-09bc-4a4b-a47f-7bb5195ce878"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
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
      "display_name": "Sentinel Incident Alerts",
      "export_key": "sentinel_incident_alerts",
      "fields": {
        "alert_compromised_entity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_compromised_entity",
          "hide_notification": false,
          "id": 865,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_compromised_entity",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Compromised Entity",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "439e7e66-4cda-4d8d-a585-e3e1a62a0f29",
          "values": [],
          "width": 106
        },
        "alert_confidence_level": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_confidence_level",
          "hide_notification": false,
          "id": 866,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_confidence_level",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Confidence Level",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "400c4dd4-5bb9-41cc-ad1e-30767a3c0c7b",
          "values": [],
          "width": 87
        },
        "alert_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_date",
          "hide_notification": false,
          "id": 982,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "alert_date",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert Date",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "59fb8f55-544a-4a66-b448-126a2b0ee61a",
          "values": [],
          "width": 38
        },
        "alert_description": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_description",
          "hide_notification": false,
          "id": 868,
          "input_type": "textarea",
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
          "type_id": 1019,
          "uuid": "846df39a-3406-4ddd-b106-85d08eb13226",
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
          "export_key": "sentinel_incident_alerts/alert_id",
          "hide_notification": false,
          "id": 952,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert Id",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "9aa30762-4043-4e63-8929-a280a9136137",
          "values": [],
          "width": 38
        },
        "alert_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_name",
          "hide_notification": false,
          "id": 869,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_name",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert Name",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "b02bf41d-799e-4ef7-81a4-14c7b5a21f48",
          "values": [],
          "width": 45
        },
        "alert_remediation_steps": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_remediation_steps",
          "hide_notification": false,
          "id": 870,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "alert_remediation_steps",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Remediation Steps",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "8653751a-79a7-4962-8110-f19b3e9f6e03",
          "values": [],
          "width": 97
        },
        "alert_severity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_severity",
          "hide_notification": false,
          "id": 871,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_severity",
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
          "type_id": 1019,
          "uuid": "d7ec7809-6a88-45f1-968a-a4c4ece571eb",
          "values": [],
          "width": 63
        },
        "alert_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_status",
          "hide_notification": false,
          "id": 872,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_status",
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
          "type_id": 1019,
          "uuid": "b96fdad7-88cd-43ac-941d-e65a2aa56bde",
          "values": [],
          "width": 50
        },
        "alert_tactics": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_tactics",
          "hide_notification": false,
          "id": 873,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_tactics",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tactics",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "de82c523-d240-4987-abcb-3c58b165b5fe",
          "values": [],
          "width": 54
        },
        "alert_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_type",
          "hide_notification": false,
          "id": 874,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_type",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert Type",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "0d8fbe15-0a74-4066-98c2-e902deaddf0d",
          "values": [],
          "width": 38
        },
        "alert_url": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/alert_url",
          "hide_notification": false,
          "id": 875,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "alert_url",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Link",
          "tooltip": "",
          "type_id": 1019,
          "uuid": "50e9c795-1e4d-42ca-afd3-5eb4e9e05563",
          "values": [],
          "width": 33
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_alerts/report_date",
          "hide_notification": false,
          "id": 953,
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
          "type_id": 1019,
          "uuid": "558def38-fcb9-4ea1-8c7f-6552f60c2644",
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
      "tags": [],
      "type_id": 8,
      "type_name": "sentinel_incident_alerts",
      "uuid": "97b04e40-2763-49ed-8e83-e67f2f563897"
    },
    {
      "actions": [],
      "display_name": "Sentinel Incident Entities",
      "export_key": "sentinel_incident_entities",
      "fields": {
        "alert_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/alert_id",
          "hide_notification": false,
          "id": 711,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "alert_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Alert ID",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "48ce4eff-adb6-437a-8600-97c0bfb813c2",
          "values": [],
          "width": 152
        },
        "entity_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/entity_id",
          "hide_notification": false,
          "id": 712,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "entity_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Entity ID",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "83778103-f43b-4ae7-b4cf-e02733da6275",
          "values": [],
          "width": 152
        },
        "entity_properties": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/entity_properties",
          "hide_notification": false,
          "id": 713,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "entity_properties",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Entity Properties",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "3ad6a9d8-06a3-44e2-bfbe-ed058a833255",
          "values": [],
          "width": 213
        },
        "entity_type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/entity_type",
          "hide_notification": false,
          "id": 714,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "entity_type",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Entity Type",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "ec3260a0-7665-455e-858a-85f93662d30a",
          "values": [],
          "width": 86
        },
        "entity_value": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/entity_value",
          "hide_notification": false,
          "id": 715,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "entity_value",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Entity Value",
          "tooltip": "",
          "type_id": 1013,
          "uuid": "41ba7c3c-d987-439e-910a-bc53341d5f75",
          "values": [],
          "width": 80
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sentinel_incident_entities/report_date",
          "hide_notification": false,
          "id": 954,
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
          "type_id": 1013,
          "uuid": "5b8fd925-5236-4782-911f-a11e3067a898",
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
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "sentinel_incident_entities",
      "uuid": "004f4c47-b149-4563-aa3f-d6f0832324e9"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "sentinel_update_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinel_update_incident\" isExecutable=\"true\" name=\"Sentinel Update Incident\"\u003e\u003cdocumentation\u003eUpdate a Sentinel Incident based on changes to the IBM SOAR incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0hrpkgu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qps3wt\" name=\"Sentinel Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e41efc23-c78d-4215-8a77-dfb68eca0548\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.sentinel_incident_id = incident.properties.sentinel_incident_number\\ninputs.sentinel_profile = incident.properties.sentinel_profile\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hrpkgu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13rk7po\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hrpkgu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qps3wt\"/\u003e\u003cendEvent id=\"EndEvent_13jer8x\"\u003e\u003cincoming\u003eSequenceFlow_13rk7po\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13rk7po\" sourceRef=\"ServiceTask_1qps3wt\" targetRef=\"EndEvent_13jer8x\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qps3wt\" id=\"ServiceTask_1qps3wt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"272\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hrpkgu\" id=\"SequenceFlow_0hrpkgu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_13jer8x\" id=\"EndEvent_13jer8x_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13rk7po\" id=\"SequenceFlow_13rk7po_di\"\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@example.com",
      "description": "Update a Sentinel Incident based on changes to the IBM SOAR incident.",
      "export_key": "sentinel_update_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1630617519969,
      "name": "Sentinel Update Incident",
      "object_type": "incident",
      "programmatic_name": "sentinel_update_incident",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "929f3854-b594-48f4-897d-44a51ce3c1f1",
      "workflow_id": 122
    },
    {
      "actions": [],
      "content": {
        "version": 38,
        "workflow_id": "sentinel_get_incident_alerts",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinel_get_incident_alerts\" isExecutable=\"true\" name=\"Sentinel Get Incident Alerts\"\u003e\u003cdocumentation\u003eGet alerts for a Sentinel Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14idxaz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zpmvkd\" name=\"Sentinel Get Incident Alerts\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3cc8ebb2-b61f-449a-a7fb-efc3350f755c\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results[\u0027success\u0027]:\\n  for alert in results[\u0027content\u0027][\u0027value\u0027]:\\n    properties = alert.get(\u0027properties\u0027, {})\\n    row = incident.addRow(\\\"sentinel_incident_alerts\\\")\\n    row[\u0027report_date\u0027] = current_dt \\n    row[\u0027alert_date\u0027] = properties[\u0027timeGenerated_ms\u0027]\\n    row[\u0027alert_name\u0027] = properties.get(\u0027alertDisplayName\u0027)\\n    row[\u0027alert_description\u0027] = properties.get(\u0027description\u0027)\\n    row[\u0027alert_type\u0027] = properties.get(\u0027alertType\u0027)\\n    row[\u0027alert_status\u0027] = properties.get(\u0027status\u0027)\\n    row[\u0027alert_severity\u0027] = properties.get(\u0027severity\u0027)\\n    row[\u0027alert_confidence_level\u0027] = properties.get(\u0027confidenceLevel\u0027)\\n    row[\u0027alert_tactics\u0027] = \\\",\\\".join(properties.get(\u0027tactics\u0027, []))\\n    row[\u0027alert_compromised_entity\u0027] = properties.get(\u0027compromisedEntity\u0027)\\n    row[\u0027alert_remediation_steps\u0027] = helper.createPlainText(\u0027\\\\n\u0027.join(properties.get(\u0027remediationSteps\u0027, [])))\\n    row[\u0027alert_id\u0027] = properties.get(\u0027systemAlertId\u0027)\\n    if properties.get(\u0027alertLink\u0027):\\n        row[\u0027alert_url\u0027] = helper.createRichText(\\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{}\u0027\u0026gt;Alert Link\u0026lt;/a\u0026gt;\\\".format(properties[\u0027alertLink\u0027]))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinel_incident_id = incident.properties.sentinel_incident_number\\ninputs.sentinel_profile = incident.properties.sentinel_profile\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14idxaz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0dz6vk0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14idxaz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zpmvkd\"/\u003e\u003cendEvent id=\"EndEvent_028huo5\"\u003e\u003cincoming\u003eSequenceFlow_0dz6vk0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0dz6vk0\" sourceRef=\"ServiceTask_0zpmvkd\" targetRef=\"EndEvent_028huo5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ql3kd1\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Sentinel Incident Alerts datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nxdcch\" sourceRef=\"ServiceTask_0zpmvkd\" targetRef=\"TextAnnotation_1ql3kd1\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zpmvkd\" id=\"ServiceTask_0zpmvkd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"281\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14idxaz\" id=\"SequenceFlow_14idxaz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"281\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"239.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_028huo5\" id=\"EndEvent_028huo5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"467\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"485\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dz6vk0\" id=\"SequenceFlow_0dz6vk0_di\"\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"467\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"424\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ql3kd1\" id=\"TextAnnotation_1ql3kd1_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"200\" x=\"366\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nxdcch\" id=\"Association_1nxdcch_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 38,
      "creator_id": "a@example.com",
      "description": "Get alerts for a Sentinel Incident",
      "export_key": "sentinel_get_incident_alerts",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631290583069,
      "name": "Sentinel Get Incident Alerts",
      "object_type": "incident",
      "programmatic_name": "sentinel_get_incident_alerts",
      "tags": [],
      "uuid": "e83697ed-0144-405c-b461-7762e3459ef5",
      "workflow_id": 154
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "sentinel_get_incident_comments",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinel_get_incident_comments\" isExecutable=\"true\" name=\"Sentinel Get Incident Comments\"\u003e\u003cdocumentation\u003eGet Sentinel Comments\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0acb8n3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0w5kb54\" name=\"Sentinel Get Incident Comments\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5753fe01-6c13-404b-9df2-e1308c3a1f04\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  for comment in results.content[\u0027value\u0027]:\\n    incident.addNote(helper.createRichText(comment[\u0027properties\u0027][\u0027message\u0027]))\\n      \\n    # remember the comment in our datatable\\n    row = incident.addRow(\u0027sentinel_comment_ids\u0027)\\n    row[\u0027comment_id\u0027] = comment[\u0027name\u0027]\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinel_incident_id = incident.properties.sentinel_incident_number\\ninputs.incident_id = incident.id\\ninputs.sentinel_profile = incident.properties.sentinel_profile\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0acb8n3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t8hmr9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0acb8n3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0w5kb54\"/\u003e\u003cendEvent id=\"EndEvent_1l54jpr\"\u003e\u003cincoming\u003eSequenceFlow_1t8hmr9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t8hmr9\" sourceRef=\"ServiceTask_0w5kb54\" targetRef=\"EndEvent_1l54jpr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17ye6n7\"\u003e\u003ctext\u003e\u003c![CDATA[Results added as Resilient Incident comments\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0s3eo5g\" sourceRef=\"ServiceTask_0w5kb54\" targetRef=\"TextAnnotation_17ye6n7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0w5kb54\" id=\"ServiceTask_0w5kb54_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"259\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0acb8n3\" id=\"SequenceFlow_0acb8n3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"259\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1l54jpr\" id=\"EndEvent_1l54jpr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"422\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"440\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t8hmr9\" id=\"SequenceFlow_1t8hmr9_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"422\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"390.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17ye6n7\" id=\"TextAnnotation_17ye6n7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"246\" x=\"345\" y=\"74\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0s3eo5g\" id=\"Association_0s3eo5g_di\"\u003e\u003comgdi:waypoint x=\"356\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "a@example.com",
      "description": "Get Sentinel Comments",
      "export_key": "sentinel_get_incident_comments",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1630617503562,
      "name": "Sentinel Get Incident Comments",
      "object_type": "incident",
      "programmatic_name": "sentinel_get_incident_comments",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "1e1bce64-8186-448b-9a2f-72ca11a1188b",
      "workflow_id": 123
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "sentinel_get_incident_entities",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinel_get_incident_entities\" isExecutable=\"true\" name=\"Sentinel Get Incident Entities\"\u003e\u003cdocumentation\u003eGet Entities for a Sentinel Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_02y6lci\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_04q3ibt\" name=\"Sentinel Get Incident Entities\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"92ff2bad-f427-472f-bca1-f071d687fbb5\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\n\\ncurrent_dt = Date().getTime()\\n\\nif results.success:\\n  for alert in results.content.keys():\\n      for entity in results.content[alert]:\\n        row = incident.addRow(\\\"sentinel_incident_entities\\\")\\n        row[\u0027report_date\u0027] = current_dt\\n        row[\u0027alert_id\u0027] = alert\\n        row[\u0027entity_id\u0027] = entity[\u0027name\u0027]\\n        row[\u0027entity_type\u0027] = entity[\u0027kind\u0027]\\n        row[\u0027entity_value\u0027] = entity[\u0027properties\u0027][\u0027friendlyName\u0027]\\n        row[\u0027entity_properties\u0027] = \\\"\u0026lt;br\u0026gt;\\\".join([\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(k, v) for k, v in entity[\u0027properties\u0027].items()])\\n        \\n        # create an artifact\\n        desc = [\\\"created from Sentinel entity: {}\\\".format(entity[\u0027name\u0027])]\\n        if entity[\u0027properties\u0027].get(\u0027azureID\u0027):\\n          desc.append(entity[\u0027properties\u0027][\u0027azureID\u0027])\\n        incident.addArtifact(entity[\u0027resilient_artifact_type\u0027], entity[\u0027resilient_artifact_value\u0027], \\\"\\\\n\\\".join(desc))\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinel_incident_id = incident.properties.sentinel_incident_number\\ninputs.sentinel_profile = incident.properties.sentinel_profile\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02y6lci\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1bmb984\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_02y6lci\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_04q3ibt\"/\u003e\u003cendEvent id=\"EndEvent_0lx8a8o\"\u003e\u003cincoming\u003eSequenceFlow_1bmb984\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1bmb984\" sourceRef=\"ServiceTask_04q3ibt\" targetRef=\"EndEvent_0lx8a8o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0b0fvdh\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned as new artifacts and in the \u0027Sentinel Incident Entities\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10wxryp\" sourceRef=\"ServiceTask_04q3ibt\" targetRef=\"TextAnnotation_0b0fvdh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_04q3ibt\" id=\"ServiceTask_04q3ibt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"265\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02y6lci\" id=\"SequenceFlow_02y6lci_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"265\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"231.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lx8a8o\" id=\"EndEvent_0lx8a8o_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"425\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"443\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bmb984\" id=\"SequenceFlow_1bmb984_di\"\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"425\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"395\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0b0fvdh\" id=\"TextAnnotation_0b0fvdh_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"172\" x=\"350\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10wxryp\" id=\"Association_10wxryp_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"140\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Get Entities for a Sentinel Incident",
      "export_key": "sentinel_get_incident_entities",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631298721245,
      "name": "Sentinel Get Incident Entities",
      "object_type": "incident",
      "programmatic_name": "sentinel_get_incident_entities",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "b4ab56ea-7bac-42d9-b469-c1351107dcd2",
      "workflow_id": 120
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "sentinel_comment_sync",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinel_comment_sync\" isExecutable=\"true\" name=\"Sentinel Comment Sync\"\u003e\u003cdocumentation\u003eSync an Incident note to a Sentinel Incident comment\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ul3s6y\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1md7yld\" name=\"Sentinel Add Incident Comment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1c88215e-970d-49bc-97ce-e914ffa63b3f\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Import Date\\nfrom java.util import Date\\n\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to Sentinel at {0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\\\".format(dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.sentinel_incident_comment = note.text.content\\ninputs.sentinel_incident_id = incident.properties.sentinel_incident_number\\ninputs.sentinel_profile = incident.properties.sentinel_profile\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ul3s6y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1805exs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ul3s6y\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1md7yld\"/\u003e\u003cendEvent id=\"EndEvent_0osq6is\"\u003e\u003cincoming\u003eSequenceFlow_1805exs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1805exs\" sourceRef=\"ServiceTask_1md7yld\" targetRef=\"EndEvent_0osq6is\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1md7yld\" id=\"ServiceTask_1md7yld_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"291\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ul3s6y\" id=\"SequenceFlow_0ul3s6y_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"291\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"244.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0osq6is\" id=\"EndEvent_0osq6is_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"481\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"499\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1805exs\" id=\"SequenceFlow_1805exs_di\"\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"436\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@example.com",
      "description": "Sync an Incident note to a Sentinel Incident comment",
      "export_key": "sentinel_comment_sync",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1630689736736,
      "name": "Sentinel Comment Sync",
      "object_type": "note",
      "programmatic_name": "sentinel_comment_sync",
      "tags": [
        {
          "tag_handle": "fn_microsoft_sentinel",
          "value": null
        }
      ],
      "uuid": "6113cb51-2705-4b92-bf41-b8fa5582ddf0",
      "workflow_id": 121
    }
  ],
  "workspaces": []
}
