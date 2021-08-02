{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflow content",
      "id": 118,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow content",
      "object_type": "workflow_usage",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "06bbb735-fdb3-49e8-a712-25af7c3a8986",
      "view_items": [],
      "workflows": [
        "wf_get_workflow_content"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflow frequency",
      "id": 119,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow frequency",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "194b24db-7e62-4386-b6a9-12d01dfc188f",
      "view_items": [
        {
          "content": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ede550e6-8394-489c-9a0d-cd0d9456771f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d82c4e9f-7163-428a-b1fe-169df253d35f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_get_workflow_frequency"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflows by artifact value",
      "id": 111,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows by artifact value",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5c7bd4ee-ef5b-4adb-998a-95c25397c981",
      "view_items": [
        {
          "content": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ede550e6-8394-489c-9a0d-cd0d9456771f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d82c4e9f-7163-428a-b1fe-169df253d35f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_get_workflows_by_artifact_value"
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
      "enabled": false,
      "export_key": "PB: Get workflows by artifact value for last 30 days",
      "id": 125,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows by artifact value for last 30 days",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "279b6bec-f67b-4c90-9baa-4b74f998d18b",
      "view_items": [],
      "workflows": [
        "pb_get_workflows_by_artifact_value_for_last_30_days"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflows by attachment name",
      "id": 113,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows by attachment name",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e2e9a810-b1c5-45c2-add2-1b611db01b43",
      "view_items": [
        {
          "content": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ede550e6-8394-489c-9a0d-cd0d9456771f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d82c4e9f-7163-428a-b1fe-169df253d35f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_get_workflows_by_attachment_filename"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflows by task name",
      "id": 112,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows by task name",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f4cb4afc-51d6-474f-a296-df59cd666b33",
      "view_items": [
        {
          "content": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ede550e6-8394-489c-9a0d-cd0d9456771f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d82c4e9f-7163-428a-b1fe-169df253d35f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_get_workflows_by_task_name"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflow usage",
      "id": 110,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow usage",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "43192662-df29-435c-a067-e365688fc9ab",
      "view_items": [
        {
          "content": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ede550e6-8394-489c-9a0d-cd0d9456771f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d82c4e9f-7163-428a-b1fe-169df253d35f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_get_workflow_data"
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
        }
      ],
      "enabled": false,
      "export_key": "PB: Get workflow usage at incident close",
      "id": 116,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow usage at incident close",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "ef6d0546-31de-4020-9389-eb4e63281be4",
      "view_items": [],
      "workflows": [
        "wf_get_workflow_usage_at_incident_close"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1627925358765,
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
      "export_key": "__function/pb_min_incident_date",
      "hide_notification": false,
      "id": 692,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "pb_min_incident_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pb_min_incident_date",
      "tooltip": "",
      "type_id": 11,
      "uuid": "903b98e5-add5-4a75-90b9-6892bf9c3ecc",
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
      "export_key": "__function/pb_id",
      "hide_notification": false,
      "id": 627,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pb_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "pb_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d63b66e3-a0e2-4538-950a-84dd352a4e7f",
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
      "export_key": "__function/pb_min_incident_id",
      "hide_notification": false,
      "id": 623,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pb_min_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "pb_min_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2aefc15a-903d-4d35-95b9-fb33903d788c",
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
      "export_key": "__function/pb_max_incident_id",
      "hide_notification": false,
      "id": 624,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pb_max_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "pb_max_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "72a0140a-d90a-420f-9047-edf56fc14f8a",
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
      "export_key": "__function/pb_max_incident_date",
      "hide_notification": false,
      "id": 693,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "pb_max_incident_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pb_max_incident_date",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7d535619-1d5f-4298-8e7b-2dafe3ecda28",
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
      "export_key": "actioninvocation/pb_max_incident_date",
      "hide_notification": false,
      "id": 695,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "pb_max_incident_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Max incident date",
      "tooltip": "",
      "type_id": 6,
      "uuid": "d82c4e9f-7163-428a-b1fe-169df253d35f",
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
      "export_key": "actioninvocation/pb_min_incident_id",
      "hide_notification": false,
      "id": 638,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pb_min_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Min incident Id",
      "tooltip": "First incident to search",
      "type_id": 6,
      "uuid": "e5b835b6-6ad9-4537-88eb-1d741208b95b",
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
      "export_key": "actioninvocation/pb_max_incident_id",
      "hide_notification": false,
      "id": 639,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pb_max_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Max incident Id",
      "tooltip": "Last incident to search",
      "type_id": 6,
      "uuid": "ede550e6-8394-489c-9a0d-cd0d9456771f",
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
      "export_key": "actioninvocation/pb_min_incident_date",
      "hide_notification": false,
      "id": 694,
      "input_type": "datepicker",
      "internal": false,
      "is_tracked": false,
      "name": "pb_min_incident_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Min incident date",
      "tooltip": "",
      "type_id": 6,
      "uuid": "7dc54f82-cee6-4c3f-9093-4bf5ab95e873",
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
        "content": "Get a list of functions, scripts, tasks and sub-playbooks used within a playbook",
        "format": "text"
      },
      "destination_handle": "fn_playbook_utils",
      "display_name": "PB: Get playbook content",
      "export_key": "pb_get_playbook_content",
      "id": 93,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1627593476826,
      "name": "pb_get_playbook_content",
      "tags": [],
      "uuid": "688cc0f8-85c5-4033-b9bf-66f01b35698c",
      "version": 2,
      "view_items": [
        {
          "content": "2aefc15a-903d-4d35-95b9-fb33903d788c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "72a0140a-d90a-420f-9047-edf56fc14f8a",
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
          "name": "PB: Get playbook content",
          "object_type": "incident",
          "programmatic_name": "pb_get_playbook_content",
          "tags": [],
          "uuid": null,
          "workflow_id": 110
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
        "content": "Get information on playbook run a given incident or for a range of incidents",
        "format": "text"
      },
      "destination_handle": "fn_playbook_utils",
      "display_name": "PB: Get playbook data",
      "export_key": "pb_get_playbook_data",
      "id": 94,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1627913459142,
      "name": "pb_get_playbook_data",
      "tags": [],
      "uuid": "d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5",
      "version": 3,
      "view_items": [
        {
          "content": "2aefc15a-903d-4d35-95b9-fb33903d788c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "72a0140a-d90a-420f-9047-edf56fc14f8a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "903b98e5-add5-4a75-90b9-6892bf9c3ecc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d535619-1d5f-4298-8e7b-2dafe3ecda28",
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
          "name": "PB: Get playbook data",
          "object_type": "incident",
          "programmatic_name": "pb_get_playbook_data",
          "tags": [],
          "uuid": null,
          "workflow_id": 112
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
        "content": "Get a list of functions, scripts, tasks and sub-workflows used within a workflow",
        "format": "text"
      },
      "destination_handle": "fn_playbook_utils",
      "display_name": "PB: Get workflow content",
      "export_key": "pb_get_workflow_content",
      "id": 87,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1627593487887,
      "name": "pb_get_workflow_content",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "a3b3eba1-03e6-4e97-b3f5-57d21f1454fc",
      "version": 7,
      "view_items": [
        {
          "content": "d63b66e3-a0e2-4538-950a-84dd352a4e7f",
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
          "name": "PB: Get workflow content",
          "object_type": "workflow_usage",
          "programmatic_name": "wf_get_workflow_content",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 102
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
        "content": "Get information on workflows run a given incident or for a range of incidents",
        "format": "text"
      },
      "destination_handle": "fn_playbook_utils",
      "display_name": "PB: Get workflow data",
      "export_key": "pb_get_workflow_data",
      "id": 84,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1627913637710,
      "name": "pb_get_workflow_data",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "ece3eb1b-2c95-4f0b-b00e-c610d418264a",
      "version": 8,
      "view_items": [
        {
          "content": "2aefc15a-903d-4d35-95b9-fb33903d788c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "72a0140a-d90a-420f-9047-edf56fc14f8a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "903b98e5-add5-4a75-90b9-6892bf9c3ecc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d535619-1d5f-4298-8e7b-2dafe3ecda28",
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
          "name": "PB: Get workflow frequency",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_frequency",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 104
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow usage",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_data",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow usage at incident close",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_usage_at_incident_close",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 100
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows by artifact value",
          "object_type": "artifact",
          "programmatic_name": "wf_get_workflows_by_artifact_value",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows by artifact value for last 30 days",
          "object_type": "artifact",
          "programmatic_name": "pb_get_workflows_by_artifact_value_for_last_30_days",
          "tags": [],
          "uuid": null,
          "workflow_id": 113
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows by attachment filename",
          "object_type": "attachment",
          "programmatic_name": "wf_get_workflows_by_attachment_filename",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 97
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows by task name",
          "object_type": "task",
          "programmatic_name": "wf_get_workflows_by_task_name",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 41,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1627925358424,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1627925358424,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3b736739-8900-4fbe-925b-cbc6e97b1957"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_playbook_utils",
      "name": "fn_playbook_utils",
      "programmatic_name": "fn_playbook_utils",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "d55df3da-7223-40d8-9ca8-72e1f3167267"
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
      "display_name": "Playbook Usage",
      "export_key": "workflow_usage",
      "fields": {
        "element_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/element_id",
          "hide_notification": false,
          "id": 658,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "element_id",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Element Id",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "63aa5330-463b-4667-b1ab-b74005b35552",
          "values": [],
          "width": 64
        },
        "element_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/element_type",
          "hide_notification": false,
          "id": 650,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "element_type",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Element type",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "091ecc44-0670-4670-a86e-d80e6d546cee",
          "values": [],
          "width": 70
        },
        "element_value": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/element_value",
          "hide_notification": false,
          "id": 651,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "element_value",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Element value",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "790a0c5b-20fe-4e2b-944e-71d57a256e03",
          "values": [],
          "width": 160
        },
        "execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/execution_date",
          "hide_notification": false,
          "id": 652,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Execution date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "9812673d-950c-46ed-9542-f6e4acb2f959",
          "values": [],
          "width": 84
        },
        "incident": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/incident",
          "hide_notification": false,
          "id": 653,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "incident",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Incident",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "726985cb-ad0e-4266-8f97-3ad09828507e",
          "values": [],
          "width": 68
        },
        "report_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/report_date",
          "hide_notification": false,
          "id": 654,
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
          "text": "Report date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "23313ce9-1667-4e9e-a94a-fc34c354c4ba",
          "values": [],
          "width": 63
        },
        "workflow": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/workflow",
          "hide_notification": false,
          "id": 655,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "workflow",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Playbook/Workflow",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "3ab02cb2-1486-4ef0-bd79-6c12fb165125",
          "values": [],
          "width": 153
        },
        "workflow_content": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/workflow_content",
          "hide_notification": false,
          "id": 656,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "workflow_content",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Playbook content",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "be98840d-cdf0-4ad7-aa7c-4474ecea4dd3",
          "values": [],
          "width": 75
        },
        "workflow_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/workflow_id",
          "hide_notification": false,
          "id": 657,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "workflow_id",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Id",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "a04a6f72-7174-4737-a320-deac86878adf",
          "values": [],
          "width": 74
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
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "workflow_usage",
      "uuid": "ee895dbb-2e2d-4ac1-b6a6-d93de03ab899"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 23,
        "workflow_id": "wf_get_workflow_content",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_content\" isExecutable=\"true\" name=\"PB: Get workflow content\"\u003e\u003cdocumentation\u003eGet functions, tasks, scripts and sub-workflows of a workflow\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mqw0w1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0hkvdcp\" name=\"PB: Get Workflow content\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a3b3eba1-03e6-4e97-b3f5-57d21f1454fc\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  content = []\\n  for k in sorted(results.content.keys()):\\n    lizt = [v for v in results.content[k]]\\n    content.append(\\\"{}:\u0026lt;br\u0026gt;\u0026amp;nbsp;\u0026amp;nbsp;{}\\\".format(k, \\\"\u0026lt;br\u0026gt;\u0026amp;nbsp;\u0026amp;nbsp;\\\".join(lizt)))\\n    \\n  row[\u0027workflow_content\u0027] = helper.createRichText(\\\"\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".join(content))\\nelse:\\n  incident.addNote(\\\"PB: Get workflow content failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_id = row[\u0027workflow_id\u0027]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mqw0w1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ib87iz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mqw0w1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0hkvdcp\"/\u003e\u003cendEvent id=\"EndEvent_1q7w4kj\"\u003e\u003cincoming\u003eSequenceFlow_0ib87iz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ib87iz\" sourceRef=\"ServiceTask_0hkvdcp\" targetRef=\"EndEvent_1q7w4kj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rnzxgr\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the same datatable row\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1kv5o8t\" sourceRef=\"ServiceTask_0hkvdcp\" targetRef=\"TextAnnotation_1rnzxgr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0hkvdcp\" id=\"ServiceTask_0hkvdcp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mqw0w1\" id=\"SequenceFlow_1mqw0w1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1q7w4kj\" id=\"EndEvent_1q7w4kj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"462\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"480\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ib87iz\" id=\"SequenceFlow_0ib87iz_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"462\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"419\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rnzxgr\" id=\"TextAnnotation_1rnzxgr_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"198\" x=\"366\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1kv5o8t\" id=\"Association_1kv5o8t_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"441\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 23,
      "creator_id": "a@example.com",
      "description": "Get functions, tasks, scripts and sub-workflows of a workflow",
      "export_key": "wf_get_workflow_content",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627590107065,
      "name": "PB: Get workflow content",
      "object_type": "workflow_usage",
      "programmatic_name": "wf_get_workflow_content",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "26a5830b-3c91-4c52-9e8c-fe46f8af8567",
      "workflow_id": 102
    },
    {
      "actions": [],
      "content": {
        "version": 58,
        "workflow_id": "wf_get_workflow_data",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_data\" isExecutable=\"true\" name=\"PB: Get workflow usage\"\u003e\u003cdocumentation\u003eGet workflows for one or a range of incidents\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12rs1ep\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_179cb3k\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"PB: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n\\n      row = incident.addRow(\u0027workflow_usage\u0027)\\n      row[\u0027report_date\u0027] = int(time.time())*1000\\n      row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n      row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n      row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n      row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n      row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n      row[\u0027element_value\u0027] =  helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n      row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\n  else:\\n    incident.addNote(\\\"PB: Get workflow usage returned no results for incident range: {}-{}\\\".format(results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\\nelse:\\n  incident.addNote(\\\"PB: Get workflow usage failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12rs1ep\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t49ggr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12rs1ep\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_179cb3k\"/\u003e\u003cendEvent id=\"EndEvent_0lsb71q\"\u003e\u003cincoming\u003eSequenceFlow_1t49ggr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t49ggr\" sourceRef=\"ServiceTask_179cb3k\" targetRef=\"EndEvent_0lsb71q\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0b3n7dz\"\u003e\u003ctext\u003e\u003c![CDATA[results returned in the \u0027Workflow Usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_16ddwx1\" sourceRef=\"ServiceTask_179cb3k\" targetRef=\"TextAnnotation_0b3n7dz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_179cb3k\" id=\"ServiceTask_179cb3k_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12rs1ep\" id=\"SequenceFlow_12rs1ep_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lsb71q\" id=\"EndEvent_0lsb71q_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"444\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"462\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t49ggr\" id=\"SequenceFlow_1t49ggr_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"444\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"410.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0b3n7dz\" id=\"TextAnnotation_0b3n7dz_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"186\" x=\"384\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_16ddwx1\" id=\"Association_16ddwx1_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 58,
      "creator_id": "a@example.com",
      "description": "Get workflows for one or a range of incidents",
      "export_key": "wf_get_workflow_data",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627925021698,
      "name": "PB: Get workflow usage",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_data",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "468bdecf-4136-47d6-9b39-321e1f2927e9",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 17,
        "workflow_id": "wf_get_workflows_by_attachment_filename",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_attachment_filename\" isExecutable=\"true\" name=\"PB: Get workflows by attachment filename\"\u003e\u003cdocumentation\u003eFind all workflows run on a specific attachment filename\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0cgocx1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_06stk11\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"PB: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n\\n      if entity.get(\\\"object\\\", {}).get(\\\"type_name\\\") == \u0027attachment\u0027 and entity.get(\\\"object\\\", {}).get(\\\"object_name\\\") == attachment.name:\\n        row = incident.addRow(\u0027workflow_usage\u0027)\\n        row[\u0027report_date\u0027] = int(time.time())*1000\\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n        row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n        row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n        row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n        row[\u0027element_value\u0027] =  helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\n  else:\\n    incident.addNote(\\\"PB: Get workflows by attachment filename ({}) returned no results for indicent range: {}-{}\\\".format(attachment.name, results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\\nelse:\\n  incident.addNote(\\\"PB: Get workflows by attachment filename failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0cgocx1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t4vykg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0cgocx1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_06stk11\"/\u003e\u003cendEvent id=\"EndEvent_1on4ur3\"\u003e\u003cincoming\u003eSequenceFlow_0t4vykg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0t4vykg\" sourceRef=\"ServiceTask_06stk11\" targetRef=\"EndEvent_1on4ur3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0fni8ne\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ba1rzh\" sourceRef=\"ServiceTask_06stk11\" targetRef=\"TextAnnotation_0fni8ne\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_06stk11\" id=\"ServiceTask_06stk11_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cgocx1\" id=\"SequenceFlow_0cgocx1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1on4ur3\" id=\"EndEvent_1on4ur3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"450\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"468\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t4vykg\" id=\"SequenceFlow_0t4vykg_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"450\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"414\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0fni8ne\" id=\"TextAnnotation_0fni8ne_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"168\" x=\"362\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ba1rzh\" id=\"Association_1ba1rzh_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"416\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 17,
      "creator_id": "a@example.com",
      "description": "Find all workflows run on a specific attachment filename",
      "export_key": "wf_get_workflows_by_attachment_filename",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627924776925,
      "name": "PB: Get workflows by attachment filename",
      "object_type": "attachment",
      "programmatic_name": "wf_get_workflows_by_attachment_filename",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "57feeca6-23eb-47d0-95b2-08193c32e425",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "wf_get_workflows_by_artifact_value",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_artifact_value\" isExecutable=\"true\" name=\"PB: Get workflows by artifact value\"\u003e\u003cdocumentation\u003eFind all the workflows across incidents which have been run on a specific artifact value\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rcehd3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0itsgbv\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"WF: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n      \\n      if entity.get(\\\"object\\\", {}).get(\\\"type_name\\\") == \u0027artifact\u0027 and entity.get(\\\"object\\\", {}).get(\\\"object_name\\\") == artifact.value:\\n        row = incident.addRow(\u0027workflow_usage\u0027)\\n        row[\u0027report_date\u0027] = int(time.time())*1000\\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n        row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n        row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n        row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n        row[\u0027element_value\u0027] =  helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\n  else:\\n    incident.addNote(\\\"PB: Get workflows by artifact value ({}) returned no results for incident range: {}-{}\\\".format(artifact.value, results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\\nelse:\\n  incident.addNote(\\\"PB: Get workflows by artifact value failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rcehd3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tna49c\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1rcehd3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0itsgbv\"/\u003e\u003cendEvent id=\"EndEvent_0zw51b5\"\u003e\u003cincoming\u003eSequenceFlow_1tna49c\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tna49c\" sourceRef=\"ServiceTask_0itsgbv\" targetRef=\"EndEvent_0zw51b5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_03bpbrt\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Workflow Usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13b44qn\" sourceRef=\"ServiceTask_0itsgbv\" targetRef=\"TextAnnotation_03bpbrt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0itsgbv\" id=\"ServiceTask_0itsgbv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rcehd3\" id=\"SequenceFlow_1rcehd3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0zw51b5\" id=\"EndEvent_0zw51b5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"462\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"480\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tna49c\" id=\"SequenceFlow_1tna49c_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"462\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"419\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_03bpbrt\" id=\"TextAnnotation_03bpbrt_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"252\" x=\"358\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13b44qn\" id=\"Association_13b44qn_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "creator_id": "a@example.com",
      "description": "Find all the workflows across incidents which have been run on a specific artifact value",
      "export_key": "wf_get_workflows_by_artifact_value",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627924658154,
      "name": "PB: Get workflows by artifact value",
      "object_type": "artifact",
      "programmatic_name": "wf_get_workflows_by_artifact_value",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "1c00217c-5716-47a4-b7d9-5505e8f639ac",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 23,
        "workflow_id": "wf_get_workflow_usage_at_incident_close",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_usage_at_incident_close\" isExecutable=\"true\" name=\"PB: Get workflow usage at incident close\"\u003e\u003cdocumentation\u003eCapture all workflows run on a incident when the incident is closed\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10epyhv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qcmmk4\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"PB: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n\\n      row = incident.addRow(\u0027workflow_usage\u0027)\\n      row[\u0027report_date\u0027] = int(time.time())*1000\\n      row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n      row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n      row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n      row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n      row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n      row[\u0027element_value\u0027] =  helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n      row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\nelse:\\n  incident.addNote(\\\"PB: Get workflow usage at incident close failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = incident.id\\ninputs.pb_min_incident_id = incident.id\\n\\ninputs.pb_min_incident_date = None\\ninputs.pb_max_incident_date = None\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10epyhv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jsegx4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10epyhv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qcmmk4\"/\u003e\u003cendEvent id=\"EndEvent_1qqwo3o\"\u003e\u003cincoming\u003eSequenceFlow_0jsegx4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jsegx4\" sourceRef=\"ServiceTask_1qcmmk4\" targetRef=\"EndEvent_1qqwo3o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_106tayq\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the \u0027workflow usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_138hjrp\" sourceRef=\"ServiceTask_1qcmmk4\" targetRef=\"TextAnnotation_106tayq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qcmmk4\" id=\"ServiceTask_1qcmmk4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10epyhv\" id=\"SequenceFlow_10epyhv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1qqwo3o\" id=\"EndEvent_1qqwo3o_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"433\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"451\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jsegx4\" id=\"SequenceFlow_0jsegx4_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"395.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_106tayq\" id=\"TextAnnotation_106tayq_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"181\" x=\"355\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_138hjrp\" id=\"Association_138hjrp_di\"\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"150\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 23,
      "creator_id": "a@example.com",
      "description": "Capture all workflows run on a incident when the incident is closed",
      "export_key": "wf_get_workflow_usage_at_incident_close",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627913802638,
      "name": "PB: Get workflow usage at incident close",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_usage_at_incident_close",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "46f6eb99-5cb9-4642-a933-799552db2e31",
      "workflow_id": 100
    },
    {
      "actions": [],
      "content": {
        "version": 34,
        "workflow_id": "wf_get_workflow_frequency",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_frequency\" isExecutable=\"true\" name=\"PB: Get workflow frequency\"\u003e\u003cdocumentation\u003eProvide a summary of workflows runs across a range of incidents\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mgeiob\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kd0k0p\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"INCIDENT_URL = \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\"\\nOBJECT_TYPES = [\u0027incident\u0027, \u0027task\u0027, \u0027artifact\u0027, \u0027attachment\u0027]\\nwf_stats = {}\\nobject_stats = { object: {} for object in OBJECT_TYPES }\\n\\n\\ndef update_workflow_stats(workflow_name, workflow_id, workflow_type):\\n  \\\"\\\"\\\"[tracking frequency of workflows by workflow id]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    workflow_id ([int]): [id of workflow]\\n    workflow_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if workflow_id not in wf_stats:\\n    wf_stats[workflow_id] = {\\n      \\\"name\\\": workflow_name,\\n      \\\"type\\\": workflow_type,\\n      \\\"workflows\\\": 0\\n    }\\n\\n  wf_stats[workflow_id][\u0027workflows\u0027] += 1\\n\\ndef update_object_stats(workflow_name, object_name, object_type):\\n  \\\"\\\"\\\"[track what workflows are run on a given attachment, task or artifact]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    object_name ([str]): [value of artifact or name to attachment/task]\\n    object_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if object_name not in object_stats[object_type]:\\n    object_stats[object_type][object_name] = []\\n\\n  object_stats[object_type][object_name].append(workflow_name)\\n\\ndef sort_wf_stats(wf_stats):\\n  \\\"\\\"\\\"[sort worflow stats by most frequent]\\n\\n  Args:\\n    wf_stats ([dict]): [dictionary of workflows keyed by id]\\n\\n  Returns:\\n    [list]: [list of workflows sorted by most frequent]\\n  \\\"\\\"\\\"\\n  wf_list = []\\n  for _, wf in wf_stats.items():\\n    wf_list.append((wf[\u0027name\u0027], wf[\u0027type\u0027], wf[\u0027workflows\u0027]))\\n\\n  return sorted(wf_list, key=lambda wf: wf[2], reverse=True)\\n\\ndef count_items_in_tuple_list(tuple_list, ndx):\\n  \\\"\\\"\\\"[count the repeat items in the workflow list and dedup the list]\\n  \\\"\\\"\\\"\\n  # count the list\\n  counted_objects = []\\n  for items in tuple_list:\\n    counted_wfs = []\\n    for wf in items[ndx]:\\n      counted_wfs.append(\\\"{1}- {0}\\\".format(wf, items[ndx].count(wf)))\\n      \\n    new_tuple = items[:ndx]\\n    new_tuple += tuple([list(set(counted_wfs))])\\n    \\n    counted_objects.append(new_tuple)\\n    \\n  return counted_objects\\n\\ndef sort_object_stats(object_list):\\n  \\\"\\\"\\\"[sort workflow frequency by specific artifact, task, incident, attachment]\\n\\n  Args:\\n    object_list ([dict]): [dictionary of object types and the workflows used within each object]\\n\\n  Returns:\\n    [list]: [description]\\n  \\\"\\\"\\\"\\n  sort_list = []\\n  for k, v in object_list.items():\\n    sort_list.append((k, len(v), v))\\n\\n  sorted_objects = sorted(sort_list, key=lambda obj: obj[1], reverse=True)\\n  # count the list\\n  return count_items_in_tuple_list(sorted_objects, 2)\\n\\n# MAIN\\nif results[\u0027success\u0027]:\\n  msg = []\\n  # get all workflows grouped by incident\\n  for inc_id, entities in results[\u0027content\u0027][\u0027workflow_content\u0027].items():\\n    for entity in entities[\u0027entities\u0027]:\\n      # filter out these workflows to get content\\n      if \\\"PB: Get workflow\\\" not in entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027):\\n        update_workflow_stats(entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027), entity.get(\u0027workflow\u0027, {}).get(\u0027workflow_id\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n        update_object_stats(entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027object_name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n\\n  # make tuples so we can sort\\n  wf_list = sort_wf_stats(wf_stats)\\n  msg.append(\\\"Top 10 Workflows for incidents: {} to {}\\\".format(results[\u0027content\u0027][\u0027min_id\u0027], results[\u0027content\u0027][\u0027max_id\u0027]))\\n  msg.extend([\\\"  {2}: {0} ({1})\\\".format(wf_list[x][0], wf_list[x][1], wf_list[x][2]) for x in range(0, 10) if x \u0026lt; len(wf_list)])\\n\\n  for obj in OBJECT_TYPES:\\n    msg.append(\\\"\\\\nTop 10 Workflows for {}s\\\".format(obj))\\n    obj_list = sort_object_stats(object_stats[obj])\\n    if obj_list:\\n      msg.extend([\\\"  {1}: {0}\\\\n  {2}\\\".format(obj_list[x][0], obj_list[x][1], obj_list[x][2])  for x in range(0, 10) if x \u0026lt; len(obj_list)])\\n    else:\\n      msg.append(\\\"  None\\\")\\n\\n  incident.addNote(helper.createPlainText(\\\"\\\\n\\\".join(msg)))\\nelse:\\n  incident.addNote(\\\"PB: Get workflow frequency failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mgeiob\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0taijrv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mgeiob\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kd0k0p\"/\u003e\u003cendEvent id=\"EndEvent_0fco8ag\"\u003e\u003cincoming\u003eSequenceFlow_0taijrv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0taijrv\" sourceRef=\"ServiceTask_0kd0k0p\" targetRef=\"EndEvent_0fco8ag\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nnedv0\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1erm5lh\" sourceRef=\"ServiceTask_0kd0k0p\" targetRef=\"TextAnnotation_1nnedv0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kd0k0p\" id=\"ServiceTask_0kd0k0p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mgeiob\" id=\"SequenceFlow_1mgeiob_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"241.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fco8ag\" id=\"EndEvent_0fco8ag_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"455\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"473\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0taijrv\" id=\"SequenceFlow_0taijrv_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"420\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nnedv0\" id=\"TextAnnotation_1nnedv0_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181\" x=\"378\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1erm5lh\" id=\"Association_1erm5lh_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"440\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 34,
      "creator_id": "a@example.com",
      "description": "Provide a summary of workflows runs across a range of incidents",
      "export_key": "wf_get_workflow_frequency",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627923638752,
      "name": "PB: Get workflow frequency",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_frequency",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "ca7bc04f-f527-4d4b-a23f-fea3a90c6175",
      "workflow_id": 104
    },
    {
      "actions": [],
      "content": {
        "version": 20,
        "workflow_id": "wf_get_workflows_by_task_name",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_task_name\" isExecutable=\"true\" name=\"PB: Get workflows by task name\"\u003e\u003cdocumentation\u003eFind all the workflows run on a specific task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t5c7t5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1spb4jp\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"PB: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n\\n      if entity.get(\\\"object\\\", {}).get(\\\"type_name\\\") == \u0027task\u0027 and entity.get(\\\"object\\\", {}).get(\\\"object_name\\\") == task.name:\\n        row = incident.addRow(\u0027workflow_usage\u0027)\\n        row[\u0027report_date\u0027] = int(time.time())*1000\\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n        row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n        row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n        row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n        row[\u0027element_value\u0027] = helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\n  else:\\n    incident.addNote(\\\"PB: Get workflows by task name ({}) returned no results for incident range: {}-{}\\\".format(task.name, results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\\nelse:\\n  incident.addNote(\\\"PB: Get workflows by task name failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t5c7t5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fwgw8x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t5c7t5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1spb4jp\"/\u003e\u003cendEvent id=\"EndEvent_1v1dbm5\"\u003e\u003cincoming\u003eSequenceFlow_0fwgw8x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0fwgw8x\" sourceRef=\"ServiceTask_1spb4jp\" targetRef=\"EndEvent_1v1dbm5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_15x3ja3\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Workflow usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1472kzp\" sourceRef=\"ServiceTask_1spb4jp\" targetRef=\"TextAnnotation_15x3ja3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1spb4jp\" id=\"ServiceTask_1spb4jp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t5c7t5\" id=\"SequenceFlow_1t5c7t5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1v1dbm5\" id=\"EndEvent_1v1dbm5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"454\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"472\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fwgw8x\" id=\"SequenceFlow_0fwgw8x_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"415\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_15x3ja3\" id=\"TextAnnotation_15x3ja3_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"205\" x=\"363\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1472kzp\" id=\"Association_1472kzp_di\"\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"134\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 20,
      "creator_id": "a@example.com",
      "description": "Find all the workflows run on a specific task",
      "export_key": "wf_get_workflows_by_task_name",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627924879683,
      "name": "PB: Get workflows by task name",
      "object_type": "task",
      "programmatic_name": "wf_get_workflows_by_task_name",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "03cb0a64-bfe7-4ac3-afea-75052d60de24",
      "workflow_id": 96
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "pb_get_workflows_by_artifact_value_for_last_30_days",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pb_get_workflows_by_artifact_value_for_last_30_days\" isExecutable=\"true\" name=\"PB: Get workflows by artifact value for last 30 days\"\u003e\u003cdocumentation\u003eRetrieve workflows associated with this artifact run over the last 30 days\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1xxdd8t\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1cxqtfx\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"import time\\n\\nURL_MAP  = {\\n  \u0027incident\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\",\\n  \u0027task\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}?taskId={1}\u0026amp;tabName=details\u0026amp;org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027artifact\u0027: \\\"\u0026lt;a href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\",\\n  \u0027workflow\u0027: \\\"\u0026lt;a href=\u0027/#customize?tab=workflows\u0026amp;workflow={1}\u0027\u0026gt;{3}\u0026lt;/a\u0026gt;\\\"\\n}\\n\\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\\n  if element_type in URL_MAP:\\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\\n\\n  return str(element_name)\\n\\n\\nif results.success:\\n  org_id = results.content[\u0027org_id\u0027]\\n  for key_incident, value_workflows in results.content[\u0027workflow_content\u0027].items():\\n    for entity in value_workflows[\u0027entities\u0027]:\\n      # skip these workflows\\n      if \\\"WF: Get workflow\\\" in entity.get(\\\"workflow\\\", {}).get(\\\"name\\\"):\\n        continue\\n      \\n      if entity.get(\\\"object\\\", {}).get(\\\"type_name\\\") == \u0027artifact\u0027 and entity.get(\\\"object\\\", {}).get(\\\"object_name\\\") == artifact.value:\\n        row = incident.addRow(\u0027workflow_usage\u0027)\\n        row[\u0027report_date\u0027] = int(time.time())*1000\\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\"), entity.get(\\\"workflow\\\", {}).get(\\\"name\\\")))\\n        row[\u0027workflow_id\u0027] = entity.get(\\\"workflow\\\", {}).get(\\\"workflow_id\\\")\\n        row[\u0027execution_date\u0027] = entity.get(\\\"start_date\\\")\\n        row[\u0027element_type\u0027] = entity.get(\\\"object\\\", {}).get(\\\"type_name\\\")\\n        row[\u0027element_value\u0027] =  helper.createRichText(make_url(org_id, key_incident, entity.get(\\\"object\\\", {}).get(\\\"type_name\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_id\\\"), entity.get(\\\"object\\\", {}).get(\\\"object_name\\\")))\\n        row[\u0027element_id\u0027] =  entity.get(\\\"object\\\", {}).get(\\\"object_id\\\")\\n  else:\\n    incident.addNote(\\\"PB: Get workflows by artifact value returned no results for incident range: {}-{}\\\".format(results.contents[\u0027min_id\u0027], results.contents[\u0027max_id\u0027]))\\nelse:\\n  incident.addNote(\\\"PB: Get workflows by artifact value failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import time\\n\\nTHIRTY_DAYS = 60*60*24*30*1000\\n\\ninputs.pb_min_incident_id = None\\ninputs.pb_max_incident_id = None\\ninputs.pb_min_incident_date = int(time.time()*1000) - THIRTY_DAYS\\ninputs.pb_max_incident_date = None\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1xxdd8t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_112b03o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1xxdd8t\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1cxqtfx\"/\u003e\u003cendEvent id=\"EndEvent_1ngcv42\"\u003e\u003cincoming\u003eSequenceFlow_112b03o\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_112b03o\" sourceRef=\"ServiceTask_1cxqtfx\" targetRef=\"EndEvent_1ngcv42\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0knebqn\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the Playbook usage datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1f97puu\" sourceRef=\"ServiceTask_1cxqtfx\" targetRef=\"TextAnnotation_0knebqn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cxqtfx\" id=\"ServiceTask_1cxqtfx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xxdd8t\" id=\"SequenceFlow_1xxdd8t_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0knebqn\" id=\"TextAnnotation_0knebqn_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"183\" x=\"333\" y=\"65\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1f97puu\" id=\"Association_1f97puu_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ngcv42\" id=\"EndEvent_1ngcv42_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_112b03o\" id=\"SequenceFlow_112b03o_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"390.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Retrieve workflows associated with this artifact run over the last 30 days",
      "export_key": "pb_get_workflows_by_artifact_value_for_last_30_days",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1627924275400,
      "name": "PB: Get workflows by artifact value for last 30 days",
      "object_type": "artifact",
      "programmatic_name": "pb_get_workflows_by_artifact_value_for_last_30_days",
      "tags": [],
      "uuid": "258d9d41-9d5e-42fb-b95b-ad5de773e5ee",
      "workflow_id": 113
    }
  ],
  "workspaces": []
}
