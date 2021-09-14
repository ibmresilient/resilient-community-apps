{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflow/playbook frequency",
      "id": 192,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow/playbook frequency",
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
      "export_key": "PB: Get workflow/playbook usage",
      "id": 193,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow/playbook usage",
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
      "export_key": "PB: Get workflow/playbook usage at incident close",
      "id": 194,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflow/playbook usage at incident close",
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
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "PB: Get workflows/playbooks by artifact value",
      "id": 195,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows/playbooks by artifact value",
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
      "export_key": "PB: Get workflows/playbooks by artifact value for last 30 days",
      "id": 125,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows/playbooks by artifact value for last 30 days",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
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
      "export_key": "PB: Get workflows/playbooks by attachment name",
      "id": 196,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows/playbooks by attachment name",
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
      "export_key": "PB: Get workflows/playbooks by task name",
      "id": 197,
      "logic_type": "all",
      "message_destinations": [],
      "name": "PB: Get workflows/playbooks by task name",
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
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1631558157416,
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
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
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
      "export_key": "__function/pb_object_type",
      "hide_notification": false,
      "id": 698,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pb_object_type",
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
      "text": "pb_object_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5cce9a2b-2be8-49e9-b375-2bcfc8f176e3",
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
      "export_key": "__function/pb_object_name",
      "hide_notification": false,
      "id": 697,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pb_object_name",
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
      "text": "pb_object_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "70e912c6-af8a-464e-98e4-dde1a8cac210",
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
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
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
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
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
      "id": 979,
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
      "id": 980,
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
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
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
      "last_modified_time": 1631276200765,
      "name": "pb_get_playbook_data",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5",
      "version": 5,
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
        },
        {
          "content": "70e912c6-af8a-464e-98e4-dde1a8cac210",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5cce9a2b-2be8-49e9-b375-2bcfc8f176e3",
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
          "name": "PB: Get workflow/playbook usage",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_data",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 182
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow/playbook usage at incident close",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_usage_at_incident_close",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 180
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow/playbooks frequency",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_frequency",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 178
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by artifact value",
          "object_type": "artifact",
          "programmatic_name": "wf_get_workflows_by_artifact_value",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 179
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by artifact value for last 30 days",
          "object_type": "artifact",
          "programmatic_name": "pb_get_workflows_by_artifact_value_for_last_30_days",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 113
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by attachment filename",
          "object_type": "attachment",
          "programmatic_name": "wf_get_workflows_by_attachment_filename",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 177
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by task name",
          "object_type": "task",
          "programmatic_name": "wf_get_workflows_by_task_name",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 181
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
      "last_modified_time": 1631276200765,
      "name": "pb_get_workflow_data",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "ece3eb1b-2c95-4f0b-b00e-c610d418264a",
      "version": 11,
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
        },
        {
          "content": "70e912c6-af8a-464e-98e4-dde1a8cac210",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5cce9a2b-2be8-49e9-b375-2bcfc8f176e3",
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
          "name": "PB: Get workflow/playbook usage",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_data",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 182
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow/playbook usage at incident close",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_usage_at_incident_close",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 180
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflow/playbooks frequency",
          "object_type": "incident",
          "programmatic_name": "wf_get_workflow_frequency",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 178
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by artifact value",
          "object_type": "artifact",
          "programmatic_name": "wf_get_workflows_by_artifact_value",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 179
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by artifact value for last 30 days",
          "object_type": "artifact",
          "programmatic_name": "pb_get_workflows_by_artifact_value_for_last_30_days",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 113
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by attachment filename",
          "object_type": "attachment",
          "programmatic_name": "wf_get_workflows_by_attachment_filename",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 177
        },
        {
          "actions": [],
          "description": null,
          "name": "PB: Get workflows/playbooks by task name",
          "object_type": "task",
          "programmatic_name": "wf_get_workflows_by_task_name",
          "tags": [
            {
              "tag_handle": "fn_playbook_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 181
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 130,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1631558154241,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1631558154241,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3dd8165f-c6cf-4369-befa-556a2f3fffde"
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
  "scripts": [
    {
      "actions": [],
      "creator_id": "a@example.com",
      "description": "Display usage data for playbooks\nThis script relies on the workflow property: playbook_data",
      "export_key": "PB: Display playbook data",
      "id": 9,
      "language": "python",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631555088617,
      "name": "PB: Display playbook data",
      "object_type": "incident",
      "script_text": "from java.util import Date\n\ncurrent_dt = Date().getTime()\n\nURL_MAP  = {\n  \u0027incident\u0027: \"\u003ca href=\u0027/#incidents/{0}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027incident_element\u0027: \"\u003ca href=\u0027/#incidents/{0}\u0027\u003e{0}\u003c/a\u003e\",\n  \u0027task\u0027: \"\u003ca href=\u0027/#incidents/{0}?taskId={1}\u0026tabName=details\u0026org_id={2}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027artifact\u0027: \"\u003ca href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027workflow\u0027: \"\u003ca href=\u0027/#customize?tab=workflows\u0026workflow={1}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027playbook\u0027: \"\u003ca href=\u0027/#playbooks/designer/{1}\u0027\u003e{3}\u003c/a\u003e\"\n}\n\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\n  if element_type in URL_MAP:\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\n\n  return str(element_name)\n\n# --- S T A R T\nresults = workflow.properties.playbook_data\n\nif results.success:\n  org_id = results.content[\u0027org_id\u0027]\n  data_flg = None\n  for key_incident, value_playbooks in results.content[\u0027playbook_content\u0027].items():\n    data_flg = False\n    for entity in value_playbooks:\n      # skip these workflows/playbooks\n      if \"PB: Get\" in entity.get(\"playbook\", {}).get(\"display_name\"):\n        continue\n\n      if (results.inputs.get(\u0027pb_object_name\u0027) and results.inputs[\u0027pb_object_name\u0027] == entity.get(\"object\", {}).get(\"object_name\")) or not results.inputs.get(\u0027pb_object_name\u0027):\n        row = incident.addRow(\u0027workflow_usage\u0027)\n        row[\u0027report_date\u0027] = current_dt\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        row[\u0027type\u0027] = \u0027playbook\u0027\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027playbook\u0027, entity.get(\"playbook\", {}).get(\"id\"), entity.get(\"playbook\", {}).get(\"display_name\")))\n        row[\u0027workflow_id\u0027] = entity.get(\"playbook\", {}).get(\"id\")\n        row[\u0027execution_date\u0027] = entity.get(\"start_time\")\n        row[\u0027element_type\u0027] = entity.get(\"object\", {}).get(\"type_name\")\n        if entity.get(\"object\", {}).get(\"type_name\") == \u0027incident\u0027:\n            row[\u0027element_value\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident_element\u0027, entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        else:\n            row[\u0027element_value\u0027] = helper.createRichText(make_url(org_id, key_incident, entity.get(\"object\", {}).get(\"type_name\"), entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        data_flg = True\n  \n  if data_flg == False:\n    incident.addNote(\"PB: Get playbook usage ({}) returned no results for incident range: {}-{}\".format(results.inputs.get(\u0027pb_object_name\u0027), results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\nelse:\n  incident.addNote(\"PB: Get playbook usage ({}) failed: {}\".format(results.inputs.get(\u0027pb_object_name\u0027), results.reason))\n",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "fadb0f23-7415-4029-a502-552ccb523002"
    },
    {
      "actions": [],
      "creator_id": "a@example.com",
      "description": "Display usage data for workflows\nThis script relies on the workflow property: workflow_data",
      "export_key": "PB: Display workflow data",
      "id": 10,
      "language": "python",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631303432732,
      "name": "PB: Display workflow data",
      "object_type": "incident",
      "script_text": "from java.util import Date\n\ncurrent_dt = Date().getTime()\n\nURL_MAP  = {\n  \u0027incident\u0027: \"\u003ca href=\u0027/#incidents/{0}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027incident_element\u0027: \"\u003ca href=\u0027/#incidents/{0}\u0027\u003e{0}\u003c/a\u003e\",\n  \u0027task\u0027: \"\u003ca href=\u0027/#incidents/{0}?taskId={1}\u0026tabName=details\u0026org_id={2}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027artifact\u0027: \"\u003ca href=\u0027/#incidents/{0}/artifact/{1}?org_id={2}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027workflow\u0027: \"\u003ca href=\u0027/#customize?tab=workflows\u0026workflow={1}\u0027\u003e{3}\u003c/a\u003e\",\n  \u0027playbook\u0027: \"\u003ca href=\u0027/#playbooks/designer/{1}\u0027\u003e{3}\u003c/a\u003e\"\n}\n\ndef make_url(org_id, inc_id, element_type, element_id, element_name):\n  if element_type in URL_MAP:\n    return URL_MAP[element_type].format(inc_id, element_id, org_id, element_name)\n\n  return str(element_name)\n\n# --- S T A R T\nresults = workflow.properties.workflow_data\n\nif results.success:\n  org_id = results.content[\u0027org_id\u0027]\n  data_flg = False\n  for key_incident, value_workflow in results.content[\u0027workflow_content\u0027].items():\n    for entity in value_workflow[\u0027entities\u0027]:\n      # skip these workflows/playbooks\n      if \"PB: Get\" in entity.get(\"workflow\", {}).get(\"name\"):\n        continue\n\n      if (results.inputs.get(\u0027pb_object_name\u0027) and results.inputs[\u0027pb_object_name\u0027] == entity.get(\"object\", {}).get(\"object_name\")) or not results.inputs.get(\u0027pb_object_name\u0027):\n        row = incident.addRow(\u0027workflow_usage\u0027)\n        row[\u0027report_date\u0027] = current_dt\n        row[\u0027incident\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident\u0027, entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        row[\u0027type\u0027] = \u0027workflow\u0027\n        row[\u0027workflow\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027workflow\u0027, entity.get(\"workflow\", {}).get(\"workflow_id\"), entity.get(\"workflow\", {}).get(\"name\")))\n        row[\u0027workflow_id\u0027] = entity.get(\"workflow\", {}).get(\"workflow_id\")\n        row[\u0027execution_date\u0027] = entity.get(\"start_date\")\n        row[\u0027element_type\u0027] = entity.get(\"object\", {}).get(\"type_name\")\n        if entity.get(\"object\", {}).get(\"type_name\") == \u0027incident\u0027:\n            row[\u0027element_value\u0027] = helper.createRichText(make_url(org_id, key_incident, \u0027incident_element\u0027, entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        else:\n            row[\u0027element_value\u0027] = helper.createRichText(make_url(org_id, key_incident, entity.get(\"object\", {}).get(\"type_name\"), entity.get(\"object\", {}).get(\"object_id\"), entity.get(\"object\", {}).get(\"object_name\")))\n        data_flg = True\n  \n  if not data_flg:\n    incident.addNote(\"PB: Get workflow usage ({}) returned no results for incident range: {}-{}\".format(results.inputs.get(\u0027pb_object_name\u0027), results.content[\u0027min_id\u0027], results.content[\u0027max_id\u0027]))\nelse:\n  incident.addNote(\"PB: Get workflow usage ({}) failed: {}\".format(results.inputs.get(\u0027pb_object_name\u0027), results.reason))\n",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "52b3f960-ee96-4fff-80bb-71744f6f9a2c"
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
      "display_name": "Playbook Usage",
      "export_key": "workflow_usage",
      "fields": {
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
          "order": 6,
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
          "order": 7,
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
          "order": 5,
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
        "type": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "workflow_usage/type",
          "hide_notification": false,
          "id": 696,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "6ddf6205-f72c-4e76-a530-cafe3b7e16e5",
          "values": [],
          "width": 37
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
          "order": 3,
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
          "order": 4,
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
        "version": 26,
        "workflow_id": "pb_get_workflows_by_artifact_value_for_last_30_days",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pb_get_workflows_by_artifact_value_for_last_30_days\" isExecutable=\"true\" name=\"PB: Get workflows/playbooks by artifact value for last 30 days\"\u003e\u003cdocumentation\u003eRetrieve workflows and playbooks associated with this artifact run over the last 30 days\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1xxdd8t\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1cxqtfx\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import time\\n\\nTHIRTY_DAYS = 60*60*24*30*1000\\n\\ninputs.pb_min_incident_id = None\\ninputs.pb_max_incident_id = None\\ninputs.pb_min_incident_date = int(time.time()*1000) - THIRTY_DAYS\\ninputs.pb_max_incident_date = None\\n\\ninputs.pb_object_name = artifact.value\\ninputs.pb_object_type = \u0027artifact\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1xxdd8t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_112b03o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1xxdd8t\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1cxqtfx\"/\u003e\u003cendEvent id=\"EndEvent_1ngcv42\"\u003e\u003cincoming\u003eSequenceFlow_0z71v18\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_112b03o\" sourceRef=\"ServiceTask_1cxqtfx\" targetRef=\"ScriptTask_1atc3bo\"/\u003e\u003cscriptTask id=\"ScriptTask_1atc3bo\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_112b03o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17t2z68\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_17t2z68\" sourceRef=\"ScriptTask_1atc3bo\" targetRef=\"ServiceTask_03gy3b0\"/\u003e\u003cserviceTask id=\"ServiceTask_03gy3b0\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"pre_processing_script\":\"import time\\n\\nTHIRTY_DAYS = 60*60*24*30*1000\\n\\ninputs.pb_min_incident_id = None\\ninputs.pb_max_incident_id = None\\ninputs.pb_min_incident_date = int(time.time()*1000) - THIRTY_DAYS\\ninputs.pb_max_incident_date = None\\n\\ninputs.pb_object_name = artifact.value\\ninputs.pb_object_type = \u0027artifact\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_17t2z68\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16jfo1r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16jfo1r\" sourceRef=\"ServiceTask_03gy3b0\" targetRef=\"ScriptTask_0jpgbb1\"/\u003e\u003cscriptTask id=\"ScriptTask_0jpgbb1\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16jfo1r\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z71v18\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0z71v18\" sourceRef=\"ScriptTask_0jpgbb1\" targetRef=\"EndEvent_1ngcv42\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1sc6hqp\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15fn24g\" sourceRef=\"ScriptTask_1atc3bo\" targetRef=\"TextAnnotation_1sc6hqp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1v5es7b\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h5ha5z\" sourceRef=\"ScriptTask_0jpgbb1\" targetRef=\"TextAnnotation_1v5es7b\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cxqtfx\" id=\"ServiceTask_1cxqtfx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xxdd8t\" id=\"SequenceFlow_1xxdd8t_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ngcv42\" id=\"EndEvent_1ngcv42_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"920\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"893\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_112b03o\" id=\"SequenceFlow_112b03o_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"336.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1atc3bo\" id=\"ScriptTask_1atc3bo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"408\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17t2z68\" id=\"SequenceFlow_17t2z68_di\"\u003e\u003comgdi:waypoint x=\"508\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"562\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"535\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1sc6hqp\" id=\"TextAnnotation_1sc6hqp_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"168\" x=\"537\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15fn24g\" id=\"Association_15fn24g_di\"\u003e\u003comgdi:waypoint x=\"506\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"590\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03gy3b0\" id=\"ServiceTask_03gy3b0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"562\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16jfo1r\" id=\"SequenceFlow_16jfo1r_di\"\u003e\u003comgdi:waypoint x=\"662\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"731\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"696.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0jpgbb1\" id=\"ScriptTask_0jpgbb1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"731\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z71v18\" id=\"SequenceFlow_0z71v18_di\"\u003e\u003comgdi:waypoint x=\"831\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"920\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"875.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1v5es7b\" id=\"TextAnnotation_1v5es7b_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"184\" x=\"836\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h5ha5z\" id=\"Association_0h5ha5z_di\"\u003e\u003comgdi:waypoint x=\"828\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"901\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 26,
      "creator_id": "a@example.com",
      "description": "Retrieve workflows and playbooks associated with this artifact run over the last 30 days",
      "export_key": "pb_get_workflows_by_artifact_value_for_last_30_days",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539224,
      "name": "PB: Get workflows/playbooks by artifact value for last 30 days",
      "object_type": "artifact",
      "programmatic_name": "pb_get_workflows_by_artifact_value_for_last_30_days",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "258d9d41-9d5e-42fb-b95b-ad5de773e5ee",
      "workflow_id": 113
    },
    {
      "actions": [],
      "content": {
        "version": 30,
        "workflow_id": "wf_get_workflows_by_attachment_filename",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_attachment_filename\" isExecutable=\"true\" name=\"PB: Get workflows/playbooks by attachment filename\"\u003e\u003cdocumentation\u003eFind all workflows and playbooks run on a specific attachment filename\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0cgocx1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_06stk11\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = attachment.name\\ninputs.pb_object_type = \u0027attachment\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0cgocx1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t4vykg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0cgocx1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_06stk11\"/\u003e\u003cendEvent id=\"EndEvent_1on4ur3\"\u003e\u003cincoming\u003eSequenceFlow_1t5mqzn\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0t4vykg\" sourceRef=\"ServiceTask_06stk11\" targetRef=\"ScriptTask_13xfvec\"/\u003e\u003cscriptTask id=\"ScriptTask_13xfvec\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0t4vykg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0sod6hl\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0sod6hl\" sourceRef=\"ScriptTask_13xfvec\" targetRef=\"ServiceTask_1nzh41v\"/\u003e\u003cserviceTask id=\"ServiceTask_1nzh41v\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = attachment.name\\ninputs.pb_object_type = \u0027attachment\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0sod6hl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hewqjh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hewqjh\" sourceRef=\"ServiceTask_1nzh41v\" targetRef=\"ScriptTask_1byfs4r\"/\u003e\u003cscriptTask id=\"ScriptTask_1byfs4r\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hewqjh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t5mqzn\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t5mqzn\" sourceRef=\"ScriptTask_1byfs4r\" targetRef=\"EndEvent_1on4ur3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_135sy8d\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_05ewxev\" sourceRef=\"ScriptTask_13xfvec\" targetRef=\"TextAnnotation_135sy8d\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_11tz2gz\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0iza15n\" sourceRef=\"ScriptTask_1byfs4r\" targetRef=\"TextAnnotation_11tz2gz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_06stk11\" id=\"ServiceTask_06stk11_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cgocx1\" id=\"SequenceFlow_0cgocx1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1on4ur3\" id=\"EndEvent_1on4ur3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"973\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"946\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t4vykg\" id=\"SequenceFlow_0t4vykg_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"448\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"368\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_13xfvec\" id=\"ScriptTask_13xfvec_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"448\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0sod6hl\" id=\"SequenceFlow_0sod6hl_di\"\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"628\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"588\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_135sy8d\" id=\"TextAnnotation_135sy8d_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"182\" x=\"530\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_05ewxev\" id=\"Association_05ewxev_di\"\u003e\u003comgdi:waypoint x=\"540\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"596\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1nzh41v\" id=\"ServiceTask_1nzh41v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"628\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hewqjh\" id=\"SequenceFlow_0hewqjh_di\"\u003e\u003comgdi:waypoint x=\"728\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"804\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"766\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1byfs4r\" id=\"ScriptTask_1byfs4r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"804\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t5mqzn\" id=\"SequenceFlow_1t5mqzn_di\"\u003e\u003comgdi:waypoint x=\"904\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"936\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"936\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"973\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"951\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_11tz2gz\" id=\"TextAnnotation_11tz2gz_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"176\" x=\"895\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0iza15n\" id=\"Association_0iza15n_di\"\u003e\u003comgdi:waypoint x=\"899\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"953\" xsi:type=\"omgdc:Point\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 30,
      "creator_id": "a@example.com",
      "description": "Find all workflows and playbooks run on a specific attachment filename",
      "export_key": "wf_get_workflows_by_attachment_filename",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539785,
      "name": "PB: Get workflows/playbooks by attachment filename",
      "object_type": "attachment",
      "programmatic_name": "wf_get_workflows_by_attachment_filename",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "57feeca6-23eb-47d0-95b2-08193c32e425",
      "workflow_id": 177
    },
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "wf_get_workflow_usage_at_incident_close",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_usage_at_incident_close\" isExecutable=\"true\" name=\"PB: Get workflow/playbook usage at incident close\"\u003e\u003cdocumentation\u003eCapture all workflows and playbooks run on an incident when the incident is closed\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10epyhv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qcmmk4\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = incident.id\\ninputs.pb_min_incident_id = incident.id\\n\\ninputs.pb_min_incident_date = None\\ninputs.pb_max_incident_date = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10epyhv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jsegx4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10epyhv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qcmmk4\"/\u003e\u003cendEvent id=\"EndEvent_1qqwo3o\"\u003e\u003cincoming\u003eSequenceFlow_1wrqrkq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jsegx4\" sourceRef=\"ServiceTask_1qcmmk4\" targetRef=\"ScriptTask_0xqpmjg\"/\u003e\u003cscriptTask id=\"ScriptTask_0xqpmjg\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0jsegx4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1byclef\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1byclef\" sourceRef=\"ScriptTask_0xqpmjg\" targetRef=\"ServiceTask_1bhxchq\"/\u003e\u003cserviceTask id=\"ServiceTask_1bhxchq\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pb_max_incident_id = incident.id\\ninputs.pb_min_incident_id = incident.id\\n\\ninputs.pb_min_incident_date = None\\ninputs.pb_max_incident_date = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1byclef\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hjno1i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hjno1i\" sourceRef=\"ServiceTask_1bhxchq\" targetRef=\"ScriptTask_08uznym\"/\u003e\u003cscriptTask id=\"ScriptTask_08uznym\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hjno1i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1wrqrkq\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wrqrkq\" sourceRef=\"ScriptTask_08uznym\" targetRef=\"EndEvent_1qqwo3o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1i4f0dj\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1lvmfjc\" sourceRef=\"ScriptTask_0xqpmjg\" targetRef=\"TextAnnotation_1i4f0dj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1bwlbuf\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in the \u0027workflow usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0uqrer5\" sourceRef=\"ScriptTask_08uznym\" targetRef=\"TextAnnotation_1bwlbuf\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qcmmk4\" id=\"ServiceTask_1qcmmk4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10epyhv\" id=\"SequenceFlow_10epyhv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1qqwo3o\" id=\"EndEvent_1qqwo3o_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"918\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"891\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jsegx4\" id=\"SequenceFlow_0jsegx4_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"422\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"345\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0xqpmjg\" id=\"ScriptTask_0xqpmjg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"422\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1byclef\" id=\"SequenceFlow_1byclef_di\"\u003e\u003comgdi:waypoint x=\"522\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"584\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"553\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bhxchq\" id=\"ServiceTask_1bhxchq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"584\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hjno1i\" id=\"SequenceFlow_0hjno1i_di\"\u003e\u003comgdi:waypoint x=\"684\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"751\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"717.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_08uznym\" id=\"ScriptTask_08uznym_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"751\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wrqrkq\" id=\"SequenceFlow_1wrqrkq_di\"\u003e\u003comgdi:waypoint x=\"851\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"918\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"884.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1i4f0dj\" id=\"TextAnnotation_1i4f0dj_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"169\" x=\"502\" y=\"74\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1lvmfjc\" id=\"Association_1lvmfjc_di\"\u003e\u003comgdi:waypoint x=\"513\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"564\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1bwlbuf\" id=\"TextAnnotation_1bwlbuf_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"160\" x=\"827\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0uqrer5\" id=\"Association_0uqrer5_di\"\u003e\u003comgdi:waypoint x=\"840\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"882\" xsi:type=\"omgdc:Point\" y=\"123\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "a@example.com",
      "description": "Capture all workflows and playbooks run on an incident when the incident is closed",
      "export_key": "wf_get_workflow_usage_at_incident_close",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539566,
      "name": "PB: Get workflow/playbook usage at incident close",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_usage_at_incident_close",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "46f6eb99-5cb9-4642-a933-799552db2e31",
      "workflow_id": 180
    },
    {
      "actions": [],
      "content": {
        "version": 69,
        "workflow_id": "wf_get_workflow_data",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_data\" isExecutable=\"true\" name=\"PB: Get workflow/playbook usage\"\u003e\u003cdocumentation\u003eGet workflows and playbooks for one or a range of incidents\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12rs1ep\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_179cb3k\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = inputs.pb_object_type = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12rs1ep\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t49ggr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12rs1ep\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_179cb3k\"/\u003e\u003cendEvent id=\"EndEvent_0lsb71q\"\u003e\u003cincoming\u003eSequenceFlow_1xfpxs2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t49ggr\" sourceRef=\"ServiceTask_179cb3k\" targetRef=\"ScriptTask_1qiws89\"/\u003e\u003cscriptTask id=\"ScriptTask_1qiws89\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t49ggr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_02ja9q7\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_02ja9q7\" sourceRef=\"ScriptTask_1qiws89\" targetRef=\"ServiceTask_17mehun\"/\u003e\u003cserviceTask id=\"ServiceTask_17mehun\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = inputs.pb_object_type = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_02ja9q7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t1jh5v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t1jh5v\" sourceRef=\"ServiceTask_17mehun\" targetRef=\"ScriptTask_02drekp\"/\u003e\u003cscriptTask id=\"ScriptTask_02drekp\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t1jh5v\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1xfpxs2\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1xfpxs2\" sourceRef=\"ScriptTask_02drekp\" targetRef=\"EndEvent_0lsb71q\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0dsjioy\"\u003e\u003ctext\u003e\u003c![CDATA[results returned in the \u0027Playbook usage\u0027 datatable]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0vejugd\" sourceRef=\"ScriptTask_1qiws89\" targetRef=\"TextAnnotation_0dsjioy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bf9io7\"\u003e\u003ctext\u003e\u003c![CDATA[\u00a0results returned in the \u0027Playbook usage\u0027 datatable]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_034vcht\" sourceRef=\"ScriptTask_02drekp\" targetRef=\"TextAnnotation_0bf9io7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_179cb3k\" id=\"ServiceTask_179cb3k_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12rs1ep\" id=\"SequenceFlow_12rs1ep_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lsb71q\" id=\"EndEvent_0lsb71q_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"929\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"902\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t49ggr\" id=\"SequenceFlow_1t49ggr_di\"\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"450\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"368.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1qiws89\" id=\"ScriptTask_1qiws89_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"450\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02ja9q7\" id=\"SequenceFlow_02ja9q7_di\"\u003e\u003comgdi:waypoint x=\"550\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"616\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"538\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0dsjioy\" id=\"TextAnnotation_0dsjioy_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"190\" x=\"550\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0vejugd\" id=\"Association_0vejugd_di\"\u003e\u003comgdi:waypoint x=\"548\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"606\" xsi:type=\"omgdc:Point\" y=\"135\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17mehun\" id=\"ServiceTask_17mehun_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"616\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t1jh5v\" id=\"SequenceFlow_1t1jh5v_di\"\u003e\u003comgdi:waypoint x=\"716\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"771\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"743.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_02drekp\" id=\"ScriptTask_02drekp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"771\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xfpxs2\" id=\"SequenceFlow_1xfpxs2_di\"\u003e\u003comgdi:waypoint x=\"871\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"929\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"900\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bf9io7\" id=\"TextAnnotation_0bf9io7_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"165\" x=\"880\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_034vcht\" id=\"Association_034vcht_di\"\u003e\u003comgdi:waypoint x=\"870\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"930\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 69,
      "creator_id": "a@example.com",
      "description": "Get workflows and playbooks for one or a range of incidents",
      "export_key": "wf_get_workflow_data",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539970,
      "name": "PB: Get workflow/playbook usage",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_data",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "468bdecf-4136-47d6-9b39-321e1f2927e9",
      "workflow_id": 182
    },
    {
      "actions": [],
      "content": {
        "version": 30,
        "workflow_id": "wf_get_workflows_by_task_name",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_task_name\" isExecutable=\"true\" name=\"PB: Get workflows/playbooks by task name\"\u003e\u003cdocumentation\u003eFind all the workflows and playbooks run on a specific task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t5c7t5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1spb4jp\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = task.name\\ninputs.pb_object_type = \u0027task\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t5c7t5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fwgw8x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t5c7t5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1spb4jp\"/\u003e\u003cendEvent id=\"EndEvent_1v1dbm5\"\u003e\u003cincoming\u003eSequenceFlow_0dwmf23\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0fwgw8x\" sourceRef=\"ServiceTask_1spb4jp\" targetRef=\"ScriptTask_1eakgyn\"/\u003e\u003cscriptTask id=\"ScriptTask_1eakgyn\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fwgw8x\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ueznch\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ueznch\" sourceRef=\"ScriptTask_1eakgyn\" targetRef=\"ServiceTask_1ll519b\"/\u003e\u003cserviceTask id=\"ServiceTask_1ll519b\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = task.name\\ninputs.pb_object_type = \u0027task\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ueznch\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_024a1jr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_024a1jr\" sourceRef=\"ServiceTask_1ll519b\" targetRef=\"ScriptTask_0ndvump\"/\u003e\u003cscriptTask id=\"ScriptTask_0ndvump\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_024a1jr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0dwmf23\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dwmf23\" sourceRef=\"ScriptTask_0ndvump\" targetRef=\"EndEvent_1v1dbm5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1p37hid\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0kihjst\" sourceRef=\"ScriptTask_1eakgyn\" targetRef=\"TextAnnotation_1p37hid\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0q8ukxs\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Workflow usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_189nn4o\" sourceRef=\"ScriptTask_0ndvump\" targetRef=\"TextAnnotation_0q8ukxs\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1spb4jp\" id=\"ServiceTask_1spb4jp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t5c7t5\" id=\"SequenceFlow_1t5c7t5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1v1dbm5\" id=\"EndEvent_1v1dbm5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"963\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"936\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fwgw8x\" id=\"SequenceFlow_0fwgw8x_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"366.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1eakgyn\" id=\"ScriptTask_1eakgyn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"447\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ueznch\" id=\"SequenceFlow_1ueznch_di\"\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"616\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"581.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1p37hid\" id=\"TextAnnotation_1p37hid_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"165\" x=\"533\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0kihjst\" id=\"Association_0kihjst_di\"\u003e\u003comgdi:waypoint x=\"539\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ll519b\" id=\"ServiceTask_1ll519b_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"616\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_024a1jr\" id=\"SequenceFlow_024a1jr_di\"\u003e\u003comgdi:waypoint x=\"716\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"791\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"753.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0ndvump\" id=\"ScriptTask_0ndvump_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"791\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dwmf23\" id=\"SequenceFlow_0dwmf23_di\"\u003e\u003comgdi:waypoint x=\"891\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"963\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"927\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0q8ukxs\" id=\"TextAnnotation_0q8ukxs_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162\" x=\"888\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_189nn4o\" id=\"Association_189nn4o_di\"\u003e\u003comgdi:waypoint x=\"884\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"940\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 30,
      "creator_id": "a@example.com",
      "description": "Find all the workflows and playbooks run on a specific task",
      "export_key": "wf_get_workflows_by_task_name",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539676,
      "name": "PB: Get workflows/playbooks by task name",
      "object_type": "task",
      "programmatic_name": "wf_get_workflows_by_task_name",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "03cb0a64-bfe7-4ac3-afea-75052d60de24",
      "workflow_id": 181
    },
    {
      "actions": [],
      "content": {
        "version": 51,
        "workflow_id": "wf_get_workflow_frequency",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflow_frequency\" isExecutable=\"true\" name=\"PB: Get workflow/playbooks frequency\"\u003e\u003cdocumentation\u003eProvide a summary of workflows and playbooks runs across a range of incidents\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mgeiob\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kd0k0p\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script\":\"INCIDENT_URL = \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\"\\nOBJECT_TYPES = [\u0027incident\u0027, \u0027task\u0027, \u0027artifact\u0027, \u0027attachment\u0027, \u0027note\u0027, \u0027milestone\u0027]\\nwf_stats = {}\\nobject_stats = { object: {} for object in OBJECT_TYPES }\\n\\n\\ndef update_workflow_stats(workflow_name, workflow_id, workflow_type):\\n  \\\"\\\"\\\"[tracking frequency of workflows by workflow id]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    workflow_id ([int]): [id of workflow]\\n    workflow_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if workflow_id not in wf_stats:\\n    wf_stats[workflow_id] = {\\n      \\\"name\\\": workflow_name,\\n      \\\"type\\\": workflow_type,\\n      \\\"workflows\\\": 0\\n    }\\n\\n  wf_stats[workflow_id][\u0027workflows\u0027] += 1\\n\\ndef update_object_stats(workflow_name, object_name, object_type):\\n  \\\"\\\"\\\"[track what workflows are run on a given attachment, task or artifact]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    object_name ([str]): [value of artifact or name to attachment/task]\\n    object_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if object_name not in object_stats.get(object_type, []):\\n    if object_type not in object_stats:\\n      object_stats[object_type] = {}\\n    object_stats[object_type][object_name] = []\\n\\n  object_stats[object_type][object_name].append(workflow_name)\\n\\ndef sort_wf_stats(wf_stats):\\n  \\\"\\\"\\\"[sort worflow stats by most frequent]\\n\\n  Args:\\n    wf_stats ([dict]): [dictionary of workflows keyed by id]\\n\\n  Returns:\\n    [list]: [list of workflows sorted by most frequent]\\n  \\\"\\\"\\\"\\n  wf_list = []\\n  for _, wf in wf_stats.items():\\n    wf_list.append((wf[\u0027name\u0027], wf[\u0027type\u0027], wf[\u0027workflows\u0027]))\\n\\n  return sorted(wf_list, key=lambda wf: wf[2], reverse=True)\\n\\ndef count_items_in_tuple_list(tuple_list, ndx):\\n  \\\"\\\"\\\"[count the repeat items in the workflow list and dedup the list]\\n  \\\"\\\"\\\"\\n  # count the list\\n  counted_objects = []\\n  for items in tuple_list:\\n    counted_wfs = []\\n    for wf in items[ndx]:\\n      counted_wfs.append(\\\"{1}- {0}\\\".format(wf, items[ndx].count(wf)))\\n      \\n    new_tuple = items[:ndx]\\n    new_tuple += tuple([list(set(counted_wfs))])\\n    \\n    counted_objects.append(new_tuple)\\n    \\n  return counted_objects\\n\\ndef sort_object_stats(object_list):\\n  \\\"\\\"\\\"[sort workflow frequency by specific artifact, task, incident, attachment]\\n\\n  Args:\\n    object_list ([dict]): [dictionary of object types and the workflows used within each object]\\n\\n  Returns:\\n    [list]: [description]\\n  \\\"\\\"\\\"\\n  sort_list = []\\n  for k, v in object_list.items():\\n    sort_list.append((k, len(v), v))\\n\\n  sorted_objects = sorted(sort_list, key=lambda obj: obj[1], reverse=True)\\n  # count the list\\n  return count_items_in_tuple_list(sorted_objects, 2)\\n\\n# MAIN\\nif results[\u0027success\u0027]:\\n  msg = []\\n  # get all workflows grouped by incident\\n  for inc_id, entities in results[\u0027content\u0027][\u0027workflow_content\u0027].items():\\n    for entity in entities[\u0027entities\u0027]:\\n      # filter out these workflows to get content\\n      if \\\"PB: Get\\\" not in entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027):\\n        update_workflow_stats(entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027), entity.get(\u0027workflow\u0027, {}).get(\u0027workflow_id\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n        update_object_stats(entity.get(\u0027workflow\u0027, {}).get(\u0027name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027object_name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n\\n  # make tuples so we can sort\\n  wf_list = sort_wf_stats(wf_stats)\\n  msg.append(\\\"Top 10 workflows. Incidents {} to {}\\\".format(results[\u0027content\u0027][\u0027min_id\u0027], results[\u0027content\u0027][\u0027max_id\u0027]))\\n  msg.extend([\\\"  {2}: {0} ({1})\\\".format(wf_list[x][0], wf_list[x][1], wf_list[x][2]) for x in range(0, 10) if x \u0026lt; len(wf_list)])\\n\\n  for obj in OBJECT_TYPES:\\n    msg.append(\\\"\\\\nTop 10 workflows by {}\\\".format(obj))\\n    obj_list = sort_object_stats(object_stats[obj])\\n    if obj_list:\\n      msg.extend([\\\"  {1}: {0}\\\\n  {2}\\\".format(obj_list[x][0], obj_list[x][1], obj_list[x][2])  for x in range(0, 10) if x \u0026lt; len(obj_list)])\\n    else:\\n      msg.append(\\\"  None\\\")\\n\\n  incident.addNote(helper.createPlainText(\\\"\\\\n\\\".join(msg)))\\nelse:\\n  incident.addNote(\\\"PB: Get workflow frequency failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mgeiob\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0taijrv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mgeiob\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kd0k0p\"/\u003e\u003cendEvent id=\"EndEvent_0fco8ag\"\u003e\u003cincoming\u003eSequenceFlow_0qct073\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0taijrv\" sourceRef=\"ServiceTask_0kd0k0p\" targetRef=\"ServiceTask_1r7m2z6\"/\u003e\u003cserviceTask id=\"ServiceTask_1r7m2z6\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"post_processing_script\":\"INCIDENT_URL = \\\"\u0026lt;a href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\"\\nOBJECT_TYPES = [\u0027incident\u0027, \u0027task\u0027, \u0027artifact\u0027, \u0027attachment\u0027]\\nwf_stats = {}\\nobject_stats = { object: {} for object in OBJECT_TYPES }\\n\\n\\ndef update_workflow_stats(workflow_name, workflow_id, workflow_type):\\n  \\\"\\\"\\\"[tracking frequency of workflows by workflow id]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    workflow_id ([int]): [id of workflow]\\n    workflow_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if workflow_id not in wf_stats:\\n    wf_stats[workflow_id] = {\\n      \\\"name\\\": workflow_name,\\n      \\\"type\\\": workflow_type,\\n      \\\"workflows\\\": 0\\n    }\\n\\n  wf_stats[workflow_id][\u0027workflows\u0027] += 1\\n\\ndef update_object_stats(workflow_name, object_name, object_type):\\n  \\\"\\\"\\\"[track what workflows are run on a given attachment, task or artifact]\\n\\n  Args:\\n    workflow_name ([str]): [workflow name]\\n    object_name ([str]): [value of artifact or name to attachment/task]\\n    object_type ([str]): [artifact, incident, task, or attachment]\\n  \\\"\\\"\\\"\\n  if object_name not in object_stats.get(object_type, []):\\n    if object_type not in object_stats:\\n      object_stats[object_type] = {}\\n    object_stats[object_type][object_name] = []\\n\\n  object_stats[object_type][object_name].append(workflow_name)\\n\\ndef sort_wf_stats(wf_stats):\\n  \\\"\\\"\\\"[sort worflow stats by most frequent]\\n\\n  Args:\\n    wf_stats ([dict]): [dictionary of workflows keyed by id]\\n\\n  Returns:\\n    [list]: [list of workflows sorted by most frequent]\\n  \\\"\\\"\\\"\\n  wf_list = []\\n  for _, wf in wf_stats.items():\\n    wf_list.append((wf[\u0027name\u0027], wf[\u0027type\u0027], wf[\u0027workflows\u0027]))\\n\\n  return sorted(wf_list, key=lambda wf: wf[2], reverse=True)\\n\\ndef count_items_in_tuple_list(tuple_list, ndx):\\n  \\\"\\\"\\\"[count the repeat items in the workflow list and dedup the list]\\n  \\\"\\\"\\\"\\n  # count the list\\n  counted_objects = []\\n  for items in tuple_list:\\n    counted_wfs = []\\n    for wf in items[ndx]:\\n      counted_wfs.append(\\\"{1}- {0}\\\".format(wf, items[ndx].count(wf)))\\n      \\n    new_tuple = items[:ndx]\\n    new_tuple += tuple([list(set(counted_wfs))])\\n    \\n    counted_objects.append(new_tuple)\\n    \\n  return counted_objects\\n\\ndef sort_object_stats(object_list):\\n  \\\"\\\"\\\"[sort workflow frequency by specific artifact, task, incident, attachment]\\n\\n  Args:\\n    object_list ([dict]): [dictionary of object types and the workflows used within each object]\\n\\n  Returns:\\n    [list]: [description]\\n  \\\"\\\"\\\"\\n  sort_list = []\\n  for k, v in object_list.items():\\n    sort_list.append((k, len(v), v))\\n\\n  sorted_objects = sorted(sort_list, key=lambda obj: obj[1], reverse=True)\\n  # count the list\\n  return count_items_in_tuple_list(sorted_objects, 2)\\n\\n# MAIN\\nif results[\u0027success\u0027]:\\n  msg = []\\n  # get all workflows grouped by incident\\n  for inc_id, entities in results[\u0027content\u0027][\u0027playbook_content\u0027].items():\\n    for entity in entities:\\n      # filter out these workflows to get content\\n      if \\\"PB: Get\\\" not in entity.get(\u0027playbook\u0027, {}).get(\u0027display_name\u0027):\\n        update_workflow_stats(entity.get(\u0027playbook\u0027, {}).get(\u0027display_name\u0027), entity.get(\u0027playbook\u0027, {}).get(\u0027id\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n        update_object_stats(entity.get(\u0027playbook\u0027, {}).get(\u0027display_name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027object_name\u0027), entity.get(\u0027object\u0027, {}).get(\u0027type_name\u0027))\\n\\n  # make tuples so we can sort\\n  wf_list = sort_wf_stats(wf_stats)\\n  msg.append(\\\"Top 10 playbooks. Incidents {} to {}\\\".format(results[\u0027content\u0027][\u0027min_id\u0027], results[\u0027content\u0027][\u0027max_id\u0027]))\\n  msg.extend([\\\"  {2}: {0} ({1})\\\".format(wf_list[x][0], wf_list[x][1], wf_list[x][2]) for x in range(0, 10) if x \u0026lt; len(wf_list)])\\n\\n  for obj in OBJECT_TYPES:\\n    msg.append(\\\"\\\\nTop 10 playbooks by {}\\\".format(obj))\\n    obj_list = sort_object_stats(object_stats[obj])\\n    if obj_list:\\n      msg.extend([\\\"  {1}: {0}\\\\n  {2}\\\".format(obj_list[x][0], obj_list[x][1], obj_list[x][2])  for x in range(0, 10) if x \u0026lt; len(obj_list)])\\n    else:\\n      msg.append(\\\"  None\\\")\\n\\n  incident.addNote(helper.createPlainText(\\\"\\\\n\\\".join(msg)))\\nelse:\\n  incident.addNote(\\\"PB: Get playbook frequency failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0taijrv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qct073\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qct073\" sourceRef=\"ServiceTask_1r7m2z6\" targetRef=\"EndEvent_0fco8ag\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nnedv0\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1erm5lh\" sourceRef=\"ServiceTask_0kd0k0p\" targetRef=\"TextAnnotation_1nnedv0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0nejpq6\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_191nyn8\" sourceRef=\"ServiceTask_1r7m2z6\" targetRef=\"TextAnnotation_0nejpq6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kd0k0p\" id=\"ServiceTask_0kd0k0p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mgeiob\" id=\"SequenceFlow_1mgeiob_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"241.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fco8ag\" id=\"EndEvent_0fco8ag_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"620\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"593\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0taijrv\" id=\"SequenceFlow_0taijrv_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"377\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nnedv0\" id=\"TextAnnotation_1nnedv0_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"165\" x=\"378\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1erm5lh\" id=\"Association_1erm5lh_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1r7m2z6\" id=\"ServiceTask_1r7m2z6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"459\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qct073\" id=\"SequenceFlow_0qct073_di\"\u003e\u003comgdi:waypoint x=\"559\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"620\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"589.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0nejpq6\" id=\"TextAnnotation_0nejpq6_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"143\" x=\"601\" y=\"60\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_191nyn8\" id=\"Association_191nyn8_di\"\u003e\u003comgdi:waypoint x=\"555\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"640\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 51,
      "creator_id": "a@example.com",
      "description": "Provide a summary of workflows and playbooks runs across a range of incidents",
      "export_key": "wf_get_workflow_frequency",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539468,
      "name": "PB: Get workflow/playbooks frequency",
      "object_type": "incident",
      "programmatic_name": "wf_get_workflow_frequency",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "ca7bc04f-f527-4d4b-a23f-fea3a90c6175",
      "workflow_id": 178
    },
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "wf_get_workflows_by_artifact_value",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_get_workflows_by_artifact_value\" isExecutable=\"true\" name=\"PB: Get workflows/playbooks by artifact value\"\u003e\u003cdocumentation\u003eFind all the workflows and playbooks across incidents which have been run on a specific artifact value\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rcehd3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0itsgbv\" name=\"PB: Get workflow data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ece3eb1b-2c95-4f0b-b00e-c610d418264a\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = artifact.value\\ninputs.pb_object_type = \u0027artifact\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"workflow_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rcehd3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tna49c\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1rcehd3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0itsgbv\"/\u003e\u003cendEvent id=\"EndEvent_0zw51b5\"\u003e\u003cincoming\u003eSequenceFlow_0oqgvol\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tna49c\" sourceRef=\"ServiceTask_0itsgbv\" targetRef=\"ScriptTask_1pc2emd\"/\u003e\u003cscriptTask id=\"ScriptTask_1pc2emd\" name=\"PB: Display workflow data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"52b3f960-ee96-4fff-80bb-71744f6f9a2c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tna49c\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0lgsnb0\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0lgsnb0\" sourceRef=\"ScriptTask_1pc2emd\" targetRef=\"ServiceTask_0hvy9nv\"/\u003e\u003cserviceTask id=\"ServiceTask_0hvy9nv\" name=\"PB: Get playbook data\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d3b215fc-8c94-45eb-97d9-0c1b3a71e3a5\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pb_max_incident_id = rule.properties.pb_max_incident_id\\ninputs.pb_min_incident_id = rule.properties.pb_min_incident_id\\n\\ninputs.pb_min_incident_date = rule.properties.pb_min_incident_date\\ninputs.pb_max_incident_date = rule.properties.pb_max_incident_date\\n\\ninputs.pb_object_name = artifact.value\\ninputs.pb_object_type = \u0027artifact\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_data\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0lgsnb0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hthweg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1hthweg\" sourceRef=\"ServiceTask_0hvy9nv\" targetRef=\"ScriptTask_041ocss\"/\u003e\u003cscriptTask id=\"ScriptTask_041ocss\" name=\"PB: Display playbook data\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fadb0f23-7415-4029-a502-552ccb523002\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1hthweg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0oqgvol\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0oqgvol\" sourceRef=\"ScriptTask_041ocss\" targetRef=\"EndEvent_0zw51b5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_052tcaa\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Playbook usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18df6ci\" sourceRef=\"ScriptTask_1pc2emd\" targetRef=\"TextAnnotation_052tcaa\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_15qgqlh\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to the \u0027Workflow usage\u0027 datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1sd5o3t\" sourceRef=\"ScriptTask_041ocss\" targetRef=\"TextAnnotation_15qgqlh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0itsgbv\" id=\"ServiceTask_0itsgbv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rcehd3\" id=\"SequenceFlow_1rcehd3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"237\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0zw51b5\" id=\"EndEvent_0zw51b5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"953\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"926\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tna49c\" id=\"SequenceFlow_1tna49c_di\"\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"368.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1pc2emd\" id=\"ScriptTask_1pc2emd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"451\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lgsnb0\" id=\"SequenceFlow_0lgsnb0_di\"\u003e\u003comgdi:waypoint x=\"551\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"622\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"541.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_052tcaa\" id=\"TextAnnotation_052tcaa_di\"\u003e\u003comgdc:Bounds height=\"47\" width=\"163\" x=\"511\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18df6ci\" id=\"Association_18df6ci_di\"\u003e\u003comgdi:waypoint x=\"536\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"573\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0hvy9nv\" id=\"ServiceTask_0hvy9nv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"622\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hthweg\" id=\"SequenceFlow_1hthweg_di\"\u003e\u003comgdi:waypoint x=\"722\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"783\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"707.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_041ocss\" id=\"ScriptTask_041ocss_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"783\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0oqgvol\" id=\"SequenceFlow_0oqgvol_di\"\u003e\u003comgdi:waypoint x=\"883\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"953\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"918\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_15qgqlh\" id=\"TextAnnotation_15qgqlh_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"163\" x=\"881\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1sd5o3t\" id=\"Association_1sd5o3t_di\"\u003e\u003comgdi:waypoint x=\"878\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"932\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "a@example.com",
      "description": "Find all the workflows and playbooks across incidents which have been run on a specific artifact value",
      "export_key": "wf_get_workflows_by_artifact_value",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1631276539897,
      "name": "PB: Get workflows/playbooks by artifact value",
      "object_type": "artifact",
      "programmatic_name": "wf_get_workflows_by_artifact_value",
      "tags": [
        {
          "tag_handle": "fn_playbook_utils",
          "value": null
        }
      ],
      "uuid": "1c00217c-5716-47a4-b7d9-5505e8f639ac",
      "workflow_id": 179
    }
  ],
  "workspaces": []
}
