{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.jira_internal_url",
          "method": "not_has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Create Jira Issue",
      "id": 52,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Create Jira Issue",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "84ffc3d2-6f6d-4a46-ac73-263b71933530",
      "view_items": [
        {
          "content": "4cced2ba-d375-4269-9d0a-4ce64ce4c5d4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bbcb0004-6af0-4310-b089-9a8817943629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "jira_open_issue"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "task.status",
          "method": "equals",
          "type": null,
          "value": "Open"
        }
      ],
      "enabled": true,
      "export_key": "Example: Create Jira Issue (Task)",
      "id": 53,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Create Jira Issue (Task)",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4df08391-63b1-4122-bd72-73a3269b1edb",
      "view_items": [
        {
          "content": "4cced2ba-d375-4269-9d0a-4ce64ce4c5d4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bbcb0004-6af0-4310-b089-9a8817943629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_jira_open_issue_task"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.jira_internal_url",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_summary",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Jira Close Issue",
      "id": 54,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Jira Close Issue",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "1acf7197-4ce3-4b20-82e1-53d3821ec352",
      "view_items": [],
      "workflows": [
        "jira_transition_issue"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "jira_task_references.status",
          "method": "equals",
          "type": null,
          "value": "Open"
        }
      ],
      "enabled": true,
      "export_key": "Example: Jira Close Issue (Task)",
      "id": 55,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Jira Close Issue (Task)",
      "object_type": "jira_task_references",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3a74a293-5cca-45c9-ad66-96cf73a2d5c9",
      "view_items": [],
      "workflows": [
        "jira_transition_issue_task"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.jira_internal_url",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "Sent to Jira at"
        },
        {
          "evaluation_id": null,
          "field_name": "task.id",
          "method": "not_has_a_value",
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
      "export_key": "Example: Jira Create Comment",
      "id": 56,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Jira Create Comment",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "8d193e80-bc1f-4195-b1d0-e50bcb849e14",
      "view_items": [],
      "workflows": [
        "jira_create_comment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "not_contains",
          "type": null,
          "value": "Sent to Jira at"
        },
        {
          "evaluation_id": null,
          "field_name": "task.id",
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
      "export_key": "Example: Jira Create Comment (Task)",
      "id": 59,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Jira Create Comment (Task)",
      "object_type": "note",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "79b55d55-c388-44d6-aa9b-96cdf844cad4",
      "view_items": [],
      "workflows": [
        "jira_create_comment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1648739578945,
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
      "id": 272,
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
      "tags": [
        {
          "tag_handle": "fn_jira",
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
      "export_key": "__function/jira_issue_id",
      "hide_notification": false,
      "id": 343,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_issue_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "JRA-1000",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "jira_issue_id",
      "tooltip": "The ID of the issue in Jira. Also known as the issue key. E.g: \"JRA-1330\"",
      "type_id": 11,
      "uuid": "883af9bd-f2aa-4a72-8d0d-77444340646b",
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 285,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
      "export_key": "__function/jira_comment",
      "hide_notification": false,
      "id": 344,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"Updated in IBM SOAR\"",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "jira_comment",
      "tooltip": "The comment to add to the issue in Jira",
      "type_id": 11,
      "uuid": "c55a9961-2b9e-4186-b32d-5ce1f0f5def5",
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
      "export_key": "__function/jira_fields",
      "hide_notification": false,
      "id": 345,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "jira_fields",
      "tooltip": "A JSON String of the fields to set in Jira",
      "type_id": 11,
      "uuid": "dcba5b1f-6709-4d4a-8b6f-9e82b44b0fa5",
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
      "export_key": "__function/jira_transition_id",
      "hide_notification": false,
      "id": 346,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_transition_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "11",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "jira_transition_id",
      "tooltip": "The ID to transition the Jira issue to. More information can be found in the Jira Documentation on transition_id",
      "type_id": 11,
      "uuid": "7e1c7fa9-7a44-4b31-9090-6679531ed32c",
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
      "export_key": "actioninvocation/jira_project_id",
      "hide_notification": false,
      "id": 360,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "jira_project_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Jira Project ID",
      "tooltip": "The id of the project you want to send this to in your Jira system. Ex: \"JRA\"",
      "type_id": 6,
      "uuid": "bbcb0004-6af0-4310-b089-9a8817943629",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "INT",
          "properties": null,
          "uuid": "e4526aae-4668-4a13-b3d0-ed4817e636c4",
          "value": 160
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "JRA",
          "properties": null,
          "uuid": "05174f17-42bd-4c07-b744-559b140a4713",
          "value": 161
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
      "export_key": "actioninvocation/jira_issue_type",
      "hide_notification": false,
      "id": 342,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "jira_issue_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "Jira Issue Type",
      "tooltip": "The type of issue to create in Jira Story/Bug etc.",
      "type_id": 6,
      "uuid": "4cced2ba-d375-4269-9d0a-4ce64ce4c5d4",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Story",
          "properties": null,
          "uuid": "297f8d3b-f582-4754-aa08-062445745864",
          "value": 152
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Bug",
          "properties": null,
          "uuid": "88057d08-737e-4fde-b6f7-fdd55f93d69b",
          "value": 153
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
      "export_key": "incident/jira_internal_url",
      "hide_notification": false,
      "id": 333,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_internal_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "Jira Internal URL",
      "tooltip": "The REST API URL",
      "type_id": 0,
      "uuid": "a9407540-8756-4140-8c4f-dd3d58a5ce24",
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
      "export_key": "incident/jira_url",
      "hide_notification": false,
      "id": 334,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "jira_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "Jira Ticket URL",
      "tooltip": "Contains URL back to the Jira issue created via the UI",
      "type_id": 0,
      "uuid": "be796d67-4ecb-4886-ad21-e6fbd04b7d18",
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
      "export_key": "incident/jira_issue_id",
      "hide_notification": false,
      "id": 335,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "jira_issue_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "JRA-1000",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "templates": [],
      "text": "Jira Issue ID",
      "tooltip": "The ID of the issue in Jira. E.g. JRA-1000",
      "type_id": 0,
      "uuid": "0b13597e-b4c4-4d37-ae00-45fb2da686ad",
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
      "created_date": 1647874014211,
      "creator": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "description": {
        "content": "Create a Jira comment. To be used when a SOAR Note is created.\nSee example workflow for configuration of function pre-processor and post-processor scripts",
        "format": "text"
      },
      "destination_handle": "fn_jira",
      "display_name": "Jira Create Comment",
      "export_key": "jira_create_comment",
      "id": 33,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1648663217238,
      "name": "jira_create_comment",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "d0e6089a-69f7-469d-8e51-a840ec2c493a",
      "version": 8,
      "view_items": [
        {
          "content": "883af9bd-f2aa-4a72-8d0d-77444340646b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c55a9961-2b9e-4186-b32d-5ce1f0f5def5",
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
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
          "name": "Example: Jira Create Comment",
          "object_type": "note",
          "programmatic_name": "jira_create_comment",
          "tags": [
            {
              "tag_handle": "fn_jira",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 43
        }
      ]
    },
    {
      "created_date": 1647874014294,
      "creator": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "description": {
        "content": "Create a jira issue. To be used when a SOAR Incident is created.\nSee example workflow for configuration of function pre-processor and post-processor scripts",
        "format": "text"
      },
      "destination_handle": "fn_jira",
      "display_name": "Jira Open Issue",
      "export_key": "jira_open_issue",
      "id": 34,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1648663217297,
      "name": "jira_open_issue",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "84476441-4b16-40fe-96c4-d07f94bda06a",
      "version": 4,
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
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dcba5b1f-6709-4d4a-8b6f-9e82b44b0fa5",
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
          "name": "Example: Jira Open Issue",
          "object_type": "incident",
          "programmatic_name": "jira_open_issue",
          "tags": [
            {
              "tag_handle": "fn_jira",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 40
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Jira Open Issue (Task)",
          "object_type": "task",
          "programmatic_name": "example_jira_open_issue_task",
          "tags": [
            {
              "tag_handle": "fn_jira",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 41
        },
        {
          "actions": [],
          "description": null,
          "name": "test_example_jira_open_issue_task",
          "object_type": "task",
          "programmatic_name": "test_example_jira_open_issue_task",
          "tags": [],
          "uuid": null,
          "workflow_id": 45
        },
        {
          "actions": [],
          "description": null,
          "name": "test_jira_open_issue",
          "object_type": "incident",
          "programmatic_name": "test_jira_open_issue",
          "tags": [],
          "uuid": null,
          "workflow_id": 46
        }
      ]
    },
    {
      "created_date": 1647874014374,
      "creator": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "description": {
        "content": "Transition a Jira issue. This can be used when a SOAR Incident is closed or to change the Jira Issue\u0027s workflow state.\nSee example workflow for configuration of function pre-processor and post-processor scripts",
        "format": "text"
      },
      "destination_handle": "fn_jira",
      "display_name": "Jira Transition Issue",
      "export_key": "jira_transition_issue",
      "id": 35,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1648663217361,
      "name": "jira_transition_issue",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "94056ccf-b3ad-4a17-9760-93b3c24b71d8",
      "version": 4,
      "view_items": [
        {
          "content": "883af9bd-f2aa-4a72-8d0d-77444340646b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7e1c7fa9-7a44-4b31-9090-6679531ed32c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dcba5b1f-6709-4d4a-8b6f-9e82b44b0fa5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c55a9961-2b9e-4186-b32d-5ce1f0f5def5",
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
          "name": "Example: Jira Transition Issue",
          "object_type": "incident",
          "programmatic_name": "jira_transition_issue",
          "tags": [
            {
              "tag_handle": "fn_jira",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 44
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Jira Transition Issue (Task)",
          "object_type": "jira_task_references",
          "programmatic_name": "jira_transition_issue_task",
          "tags": [
            {
              "tag_handle": "fn_jira",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 42
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 47,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1648739576608,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1648739576608,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3b0119a6-5956-4724-bb16-6e2dd908bd0d",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_jira",
      "name": "fn_jira",
      "programmatic_name": "fn_jira",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "users": [],
      "uuid": "609c47f4-6b11-48ab-bd9e-c9664e2cf3aa"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 41,
    "major": 42,
    "minor": 2,
    "version": "42.2.41"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Jira Task References",
      "export_key": "jira_task_references",
      "fields": {
        "date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/date",
          "hide_notification": false,
          "id": 336,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Action Date",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "9263d9a2-276c-4fb8-b0d5-e4a414de8da9",
          "values": [],
          "width": 73
        },
        "jira_issue_id_col": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/jira_issue_id_col",
          "hide_notification": false,
          "id": 337,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "jira_issue_id_col",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Jira Issue ID",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "8a603659-d1ff-46d1-8e14-ae7d3d808338",
          "values": [],
          "width": 273
        },
        "jira_link": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/jira_link",
          "hide_notification": false,
          "id": 338,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "jira_link",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Jira Link",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "28a1c558-8e64-4e44-84b8-b495a2ffdcf3",
          "values": [],
          "width": 83
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/status",
          "hide_notification": false,
          "id": 339,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "59b3dae0-9006-43de-8e23-005dd74d68dd",
          "values": [],
          "width": 73
        },
        "task": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/task",
          "hide_notification": false,
          "id": 340,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "task",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Task",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "440f0faf-b8b3-4202-a065-5b8c6c7496a3",
          "values": [],
          "width": 104
        },
        "task_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "jira_task_references/task_id",
          "hide_notification": false,
          "id": 341,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "task_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Task Id",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "c04b6de7-9de8-44a9-af36-a9b536231e6f",
          "values": [],
          "width": 30
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
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "jira_task_references",
      "uuid": "b91a89b6-450e-4344-978a-443f67c164ab"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "jira_create_comment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"jira_create_comment\" isExecutable=\"true\" name=\"Example: Jira Create Comment\"\u003e\u003cdocumentation\u003eCreate a Jira Comment for an existing linked Jira Issue. The Rule associated with this Workflow should only trigger if a Jira Issue is already linked.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1aibfo6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1770oap\" name=\"Jira Create Comment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d0e6089a-69f7-469d-8e51-a840ec2c493a\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Example: Jira Create Comment post-process script\\n\\n# Import Date\\nfrom java.util import Date\\n\\nif results.success:\\n  # Get the current time\\n  dt_now = Date()\\n  \\n  if results.get(\\\"content\\\", {}).get(\\\"jira_url\\\"):\\n    jira_url = results.get(\\\"content\\\", {}).get(\\\"jira_url\\\")\\n  else:\\n    jira_url = incident.properties.jira_url.content\\n  \\n  # Prepend message and time to the note\\n  note.text = u\\\"\u0026lt;b\u0026gt;Sent to the Jira issue {0} at {1}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{2}\\\".format(jira_url, dt_now, unicode(note.text.content))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Example: Jira Create Comment pre-processing script\\n\\ninputs.jira_issue_id = incident.properties.jira_issue_id\\ninputs.jira_comment = note.text.content\\ninputs.incident_id = incident.id\\n\\n# If this is a task note, get the taskId\\nif note.type == \u0027task\u0027:\\n  # Set the task_id\\n  inputs.task_id = task.id\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1aibfo6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01lqba1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1aibfo6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1770oap\"/\u003e\u003cendEvent id=\"EndEvent_0kzcct7\"\u003e\u003cincoming\u003eSequenceFlow_01lqba1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01lqba1\" sourceRef=\"ServiceTask_1770oap\" targetRef=\"EndEvent_0kzcct7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0555jks\"\u003e\u003ctext\u003e\u003c![CDATA[Input the Jira Issue ID and the SOAR Note text\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17q3sf8\" sourceRef=\"ServiceTask_1770oap\" targetRef=\"TextAnnotation_0555jks\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0wb03cx\"\u003e\u003ctext\u003e\u003c![CDATA[Adds Comment to Jira Issue\nand prepends info to SOAR Note]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_05o616t\" sourceRef=\"ServiceTask_1770oap\" targetRef=\"TextAnnotation_0wb03cx\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"468\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"463\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1770oap\" id=\"ServiceTask_1770oap_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"797\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1aibfo6\" id=\"SequenceFlow_1aibfo6_di\"\u003e\u003comgdi:waypoint x=\"504\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"797\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"605.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0kzcct7\" id=\"EndEvent_0kzcct7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1195\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1168\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01lqba1\" id=\"SequenceFlow_01lqba1_di\"\u003e\u003comgdi:waypoint x=\"897\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1195\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1001\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0555jks\" id=\"TextAnnotation_0555jks_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"152\" x=\"552\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17q3sf8\" id=\"Association_17q3sf8_di\"\u003e\u003comgdi:waypoint x=\"797\" xsi:type=\"omgdc:Point\" y=\"184\"/\u003e\u003comgdi:waypoint x=\"693\" xsi:type=\"omgdc:Point\" y=\"137\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0wb03cx\" id=\"TextAnnotation_0wb03cx_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"228\" x=\"933\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_05o616t\" id=\"Association_05o616t_di\"\u003e\u003comgdi:waypoint x=\"897\" xsi:type=\"omgdc:Point\" y=\"182\"/\u003e\u003comgdi:waypoint x=\"1003\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Create a Jira Comment for an existing linked Jira Issue. The Rule associated with this Workflow should only trigger if a Jira Issue is already linked.",
      "export_key": "jira_create_comment",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1648663217776,
      "name": "Example: Jira Create Comment",
      "object_type": "note",
      "programmatic_name": "jira_create_comment",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "ed7adbfe-2551-4315-a3c4-06ef84b9122d",
      "workflow_id": 43
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "example_jira_open_issue_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_jira_open_issue_task\" isExecutable=\"true\" name=\"Example: Jira Open Issue (Task)\"\u003e\u003cdocumentation\u003eOpen a Jira Issue based on a task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0d2hrps\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0hnqtx4\" name=\"Jira Open Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"84476441-4b16-40fe-96c4-d07f94bda06a\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\ntime_now = Date().time\\n\\nif results.get(\\\"success\\\"):\\n  results_content = results.get(\\\"content\\\", {})\\n\\n  url = \\\"\u0026lt;a href=\u0027{}\u0027 target=\u0027blank\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results_content.get(\\\"issue_url\\\"), results_content.get(\\\"issue_key\\\"))\\n\\n  # Add Note\\n  note = \\\"Added Jira Issue: {0}\\\".format(url)\\n  task.addNote(helper.createRichText(note))\\n  \\n  # Add Row to Jira Data Table\\n  # default is jira_task_references but can be changed by changing \u0027jira_dt_name\u0027 in app.config\\n  row = incident.addRow(results_content.get(\\\"jira_dt_name\\\")) \\n  row[\u0027date\u0027] = time_now\\n  row[\u0027task_id\u0027] = task.id\\n  row[\u0027task\u0027] = task.name\\n  row[\u0027jira_link\u0027] = helper.createRichText(url)\\n  row[\u0027jira_issue_id_col\u0027] = results_content.get(\\\"issue_key\\\")\\n  row[\u0027status\u0027] = \u0027Open\u0027\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Example: Jira Open Issue [Task] pre-processing script\\n\\n#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef list_to_json_str(l):\\n  \\\"\\\"\\\"\\n  Function that converts a list into a JSON string.\\n  Supports types: basestring, unicode, bool, int, list and dicts.\\n  If the value is None, it sets it to False.\\n  \\\"\\\"\\\"\\n  list_as_str = \u0027\u0027\\n  json_entry = u\u0027{0},\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\",\u0027\\n\\n  for value in l:\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      list_as_str += json_entry.format(list_to_json_str(value))\\n\\n    elif isinstance(value, dict):\\n      list_as_str += json_entry.format(dict_to_json_str(value))\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      value = value.replace(\\\"\\\\n\\\", \\\"\\\\\\\\n\\\")\\n      list_as_str += json_entry_str.format(unicode(value))\\n\\n    elif isinstance(value, unicode):\\n      list_as_str += json_entry.format(unicode(value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value is True else \u0027false\u0027\\n      list_as_str += json_entry.format(value)\\n\\n    elif isinstance(value, int):\\n      list_as_str += json_entry.format(value)\\n\\n    else:\\n      helper.fail(\u0027list_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027[\u0027, list_as_str[:-1], u\u0027]\u0027)\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"\\n  Function that converts a dictionary into a JSON string.\\n  Supports types: basestring, unicode, bool, int, list and nested dicts.\\n  If the value is None, it sets it to False.\\n  \\\"\\\"\\\"\\n\\n  json_entry = u\u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      entries.append(json_entry.format(unicode(key), list_to_json_str(value)))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      value = value.replace(\\\"\\\\n\\\", \\\"\\\\\\\\n\\\")\\n      entries.append(json_entry_str.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, unicode):\\n      entries.append(json_entry.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value is True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, int):\\n      entries.append(json_entry.format(unicode(key), value))\\n\\n    else:\\n      helper.fail(\u0027dict_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027{\u0027, \u0027,\u0027.join(entries), u\u0027}\u0027)\\n\\n#####################\\n### Define Inputs ###\\n#####################\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this task\\ninputs.task_id = task.id\\n\\n# A map for JIRA priorities\\npriority_map = { \\\"Low\\\": {\\\"name\\\": \\\"Low\\\"}, \\\"Medium\\\": {\\\"name\\\": \\\"Medium\\\"}, \\\"High\\\": {\\\"name\\\": \\\"High\\\"} }\\njira_priority = priority_map.get(incident.severity_code, {\\\"name\\\": \\\"Low\\\"})\\n\\n# Define JIRA fields here\\ninputs.jira_fields = dict_to_json_str({\\n  \\\"project\\\": rule.properties.jira_project_id,\\n  \\\"issuetype\\\": rule.properties.jira_issue_type,\\n  \\\"priority\\\": jira_priority,\\n  \\\"summary\\\": u\\\"IBM SOAR: {0}\\\".format(unicode(task.name)),\\n  \\\"description\\\": task.instructions.content if task.get(\\\"instructions\\\") else \\\"Created in IBM SOAR\\\"\\n})\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0d2hrps\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1k5o4il\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0d2hrps\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0hnqtx4\"/\u003e\u003cendEvent id=\"EndEvent_0n2xl2a\"\u003e\u003cincoming\u003eSequenceFlow_1k5o4il\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1k5o4il\" sourceRef=\"ServiceTask_0hnqtx4\" targetRef=\"EndEvent_0n2xl2a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1534s99\"\u003e\u003ctext\u003eMap the fields set in Jira including the project and issue type\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1mrautp\" sourceRef=\"ServiceTask_0hnqtx4\" targetRef=\"TextAnnotation_1534s99\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19dg19i\"\u003e\u003ctext\u003eAdds a row to the jira_task_references Data Table and also Adds a Note to the Task\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_11zryfq\" sourceRef=\"ServiceTask_0hnqtx4\" targetRef=\"TextAnnotation_19dg19i\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"402\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"397\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0hnqtx4\" id=\"ServiceTask_0hnqtx4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"758\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0d2hrps\" id=\"SequenceFlow_0d2hrps_di\"\u003e\u003comgdi:waypoint x=\"438\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"598\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"598\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"758\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"568\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0n2xl2a\" id=\"EndEvent_0n2xl2a_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1180\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1153\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k5o4il\" id=\"SequenceFlow_1k5o4il_di\"\u003e\u003comgdi:waypoint x=\"858\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1180\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"974\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1534s99\" id=\"TextAnnotation_1534s99_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"185\" x=\"574\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1mrautp\" id=\"Association_1mrautp_di\"\u003e\u003comgdi:waypoint x=\"763\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"702\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19dg19i\" id=\"TextAnnotation_19dg19i_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"279\" x=\"897\" y=\"67\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_11zryfq\" id=\"Association_11zryfq_di\"\u003e\u003comgdi:waypoint x=\"858\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"984\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Open a Jira Issue based on a task",
      "export_key": "example_jira_open_issue_task",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1648738980640,
      "name": "Example: Jira Open Issue (Task)",
      "object_type": "task",
      "programmatic_name": "example_jira_open_issue_task",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "17d8085d-a27a-47f5-8c72-491f928a91af",
      "workflow_id": 41
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "jira_open_issue",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"jira_open_issue\" isExecutable=\"true\" name=\"Example: Jira Open Issue\"\u003e\u003cdocumentation\u003eOpen a Jira Issue based on the Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ja7096\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1libp02\" name=\"Jira Open Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"84476441-4b16-40fe-96c4-d07f94bda06a\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\nif results.get(\\\"success\\\"):\\n  results_content = results.get(\\\"content\\\", {})\\n  incident.properties.jira_url = \\\"\u0026lt;a href=\u0027{}\u0027 target=\u0027blank\u0027\u0026gt;{}\u0026lt;/a\u0026gt;\\\".format(results_content.get(\\\"issue_url\\\"), results_content.get(\\\"issue_key\\\"))\\n  incident.properties.jira_internal_url = results_content.get(\\\"issue_url_internal\\\")\\n  incident.properties.jira_issue_id = results_content.get(\\\"issue_key\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Example: Jira Open Issue [Incident] pre-processing script\\n\\n#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef list_to_json_str(l):\\n  \\\"\\\"\\\"\\n  Function that converts a list into a JSON string.\\n  Supports types: basestring, unicode, bool, int, list and dicts.\\n  If the value is None, it sets it to False.\\n  \\\"\\\"\\\"\\n  list_as_str = \u0027\u0027\\n  json_entry = u\u0027{0},\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\",\u0027\\n\\n  for value in l:\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      list_as_str += json_entry.format(list_to_json_str(value))\\n\\n    elif isinstance(value, dict):\\n      list_as_str += json_entry.format(dict_to_json_str(value))\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      value = value.replace(\\\"\\\\n\\\", \\\"\\\\\\\\n\\\")\\n      list_as_str += json_entry_str.format(unicode(value))\\n\\n    elif isinstance(value, unicode):\\n      list_as_str += json_entry.format(unicode(value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value is True else \u0027false\u0027\\n      list_as_str += json_entry.format(value)\\n\\n    elif isinstance(value, int):\\n      list_as_str += json_entry.format(value)\\n\\n    else:\\n      helper.fail(\u0027list_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027[\u0027, list_as_str[:-1], u\u0027]\u0027)\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"\\n  Function that converts a dictionary into a JSON string.\\n  Supports types: basestring, unicode, bool, int, list and nested dicts.\\n  If the value is None, it sets it to False.\\n  \\\"\\\"\\\"\\n\\n  json_entry = u\u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      entries.append(json_entry.format(unicode(key), list_to_json_str(value)))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      value = value.replace(\\\"\\\\n\\\", \\\"\\\\\\\\n\\\")\\n      entries.append(json_entry_str.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, unicode):\\n      entries.append(json_entry.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value is True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, int):\\n      entries.append(json_entry.format(unicode(key), value))\\n\\n    else:\\n      helper.fail(\u0027dict_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027{\u0027, \u0027,\u0027.join(entries), u\u0027}\u0027)\\n\\n#####################\\n### Define Inputs ###\\n#####################\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# A map for JIRA priorities\\npriority_map = { \\\"Low\\\": {\\\"name\\\": \\\"Low\\\"}, \\\"Medium\\\": {\\\"name\\\": \\\"Medium\\\"}, \\\"High\\\": {\\\"name\\\": \\\"High\\\"} }\\njira_priority = priority_map.get(incident.severity_code, {\\\"name\\\": \\\"Low\\\"})\\n\\n# Define JIRA fields here\\ninputs.jira_fields = dict_to_json_str({\\n  \\\"project\\\": rule.properties.jira_project_id,\\n  \\\"issuetype\\\": rule.properties.jira_issue_type,\\n  \\\"priority\\\": jira_priority,\\n  \\\"summary\\\": u\\\"IBM SOAR: {0}\\\".format(incident.name),\\n  \\\"description\\\": incident.description.content if incident.get(\\\"description\\\") else \\\"Created in IBM SOAR\\\"\\n})\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ja7096\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1aadk7b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ja7096\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1libp02\"/\u003e\u003cendEvent id=\"EndEvent_02i0avr\"\u003e\u003cincoming\u003eSequenceFlow_1aadk7b\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1aadk7b\" sourceRef=\"ServiceTask_1libp02\" targetRef=\"EndEvent_02i0avr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1d2s1il\"\u003e\u003ctext\u003eOutput populates a URL back to the created Jira Issue and the jira_issue_id used to add Jira comments or to close the Issue\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0kf5ohc\" sourceRef=\"ServiceTask_1libp02\" targetRef=\"TextAnnotation_1d2s1il\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0x10biq\"\u003e\u003ctext\u003eMap the fields set in Jira including the project and issue type\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0af4n58\" sourceRef=\"ServiceTask_1libp02\" targetRef=\"TextAnnotation_0x10biq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"398\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"393\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1libp02\" id=\"ServiceTask_1libp02_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"731\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ja7096\" id=\"SequenceFlow_1ja7096_di\"\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"731\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"537.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02i0avr\" id=\"EndEvent_02i0avr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1124\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1097\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1aadk7b\" id=\"SequenceFlow_1aadk7b_di\"\u003e\u003comgdi:waypoint x=\"831\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1124\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"932.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1d2s1il\" id=\"TextAnnotation_1d2s1il_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"374\" x=\"826\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0kf5ohc\" id=\"Association_0kf5ohc_di\"\u003e\u003comgdi:waypoint x=\"831\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"937\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0x10biq\" id=\"TextAnnotation_0x10biq_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"273\" x=\"452\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0af4n58\" id=\"Association_0af4n58_di\"\u003e\u003comgdi:waypoint x=\"731\" xsi:type=\"omgdc:Point\" y=\"183\"/\u003e\u003comgdi:waypoint x=\"651\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Open a Jira Issue based on the Incident.",
      "export_key": "jira_open_issue",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1648738932327,
      "name": "Example: Jira Open Issue",
      "object_type": "incident",
      "programmatic_name": "jira_open_issue",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "243a3789-d9f8-4384-8bae-f26ab088e87e",
      "workflow_id": 40
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "jira_transition_issue_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"jira_transition_issue_task\" isExecutable=\"true\" name=\"Example: Jira Transition Issue (Task)\"\u003e\u003cdocumentation\u003eTransition a Jira Issue for a task as maintained in a data table\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0f3nkiz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ovio39\" name=\"Jira Transition Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"94056ccf-b3ad-4a17-9760-93b3c24b71d8\"\u003e{\"inputs\":{},\"post_processing_script\":\"from java.util import Date\\ntime_now = Date().time\\n\\nif results.get(\\\"success\\\"):\\n  row.date = time_now\\n  row.status = \\\"Closed\\\"\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Example: Jira Transition Issue (Task) pre-processing script\\n\\n#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, unicode, bool, int and nested dicts.\\n     Does not support lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = u\u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      helper.fail(\u0027dict_to_json_str does not support Python Lists\u0027)\\n\\n    if isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, unicode):\\n      entries.append(json_entry.format(unicode(key), unicode(value)))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, int):\\n      entries.append(json_entry.format(unicode(key), value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      helper.fail(\u0027dict_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027{\u0027, \u0027,\u0027.join(entries), u\u0027}\u0027)\\n  \\n\\n#####################\\n### Define Inputs ###\\n#####################\\n\\ninputs.jira_issue_id = row.jira_issue_id_col\\ninputs.jira_transition_id = \\\"Close\\\"\\ninputs.jira_comment = u\\\"Closed in IBM SOAR\\\\n\\\\nResolution: Done\\\\n\\\"\\n\\n# Define JIRA fields here\\ninputs.jira_fields = dict_to_json_str({\\n  \\\"resolution\\\": { \\\"name\\\": \\\"Done\\\" }\\n})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f3nkiz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_030izo8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f3nkiz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ovio39\"/\u003e\u003cendEvent id=\"EndEvent_0f4i08o\"\u003e\u003cincoming\u003eSequenceFlow_030izo8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_030izo8\" sourceRef=\"ServiceTask_1ovio39\" targetRef=\"EndEvent_0f4i08o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ung4o0\"\u003e\u003ctext\u003e\u003c![CDATA[Choose a Jira Transition Id for the Jira issue\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ie6a60\" sourceRef=\"ServiceTask_1ovio39\" targetRef=\"TextAnnotation_0ung4o0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0e4ezg9\"\u003e\u003ctext\u003e\u003c![CDATA[Update status and time in jira_task_references Data Table\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1iv5gju\" sourceRef=\"ServiceTask_1ovio39\" targetRef=\"TextAnnotation_0e4ezg9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"460\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"455\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ovio39\" id=\"ServiceTask_1ovio39_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"753\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f3nkiz\" id=\"SequenceFlow_0f3nkiz_di\"\u003e\u003comgdi:waypoint x=\"496\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"753\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"579.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0f4i08o\" id=\"EndEvent_0f4i08o_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1118\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1091\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_030izo8\" id=\"SequenceFlow_030izo8_di\"\u003e\u003comgdi:waypoint x=\"853\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1118\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"940.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ung4o0\" id=\"TextAnnotation_0ung4o0_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"133\" x=\"608\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ie6a60\" id=\"Association_1ie6a60_di\"\u003e\u003comgdi:waypoint x=\"757\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"712\" xsi:type=\"omgdc:Point\" y=\"139\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0e4ezg9\" id=\"TextAnnotation_0e4ezg9_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"164\" x=\"894\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1iv5gju\" id=\"Association_1iv5gju_di\"\u003e\u003comgdi:waypoint x=\"853\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003comgdi:waypoint x=\"917\" xsi:type=\"omgdc:Point\" y=\"144\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Transition a Jira Issue for a task as maintained in a data table",
      "export_key": "jira_transition_issue_task",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1648739573056,
      "name": "Example: Jira Transition Issue (Task)",
      "object_type": "jira_task_references",
      "programmatic_name": "jira_transition_issue_task",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "b643c95a-c025-4754-b6f7-8f03473b0e3e",
      "workflow_id": 42
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "jira_transition_issue",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"jira_transition_issue\" isExecutable=\"true\" name=\"Example: Jira Transition Issue\"\u003e\u003cdocumentation\u003eEither update a Jira Issue (such as a priority change) or close the Issue when an Incident is closed. The Rule associated with this Workflow should only trigger if a Jira Issue is already linked.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0n9xl5o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0qcmweq\" name=\"Jira Transition Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"94056ccf-b3ad-4a17-9760-93b3c24b71d8\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Example: Jira Transition Issue pre-processing script\\n\\n#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, unicode, bool, int and nested dicts.\\n     Does not support lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = u\u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      helper.fail(\u0027dict_to_json_str does not support Python Lists\u0027)\\n\\n    if isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, unicode):\\n      entries.append(json_entry.format(unicode(key), unicode(value)))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, int):\\n      entries.append(json_entry.format(unicode(key), value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      helper.fail(\u0027dict_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027{\u0027, \u0027,\u0027.join(entries), u\u0027}\u0027)\\n  \\n\\n#####################\\n### Define Inputs ###\\n#####################\\n\\ninputs.jira_issue_id = incident.properties.jira_issue_id\\ninputs.jira_transition_id = \\\"Close\\\"\\ninputs.jira_comment = u\\\"Closed in IBM SOAR\\\\n\\\\nResolution: {0}\\\\n{1}\\\".format(incident.resolution_id, incident.resolution_summary.content)\\n\\nresolution_map = { \\\"unresolved\\\": \\\"Obsolete\\\", \\\"duplicate\\\": \\\"Duplicate\\\", \\\"not an issue\\\": \\\"Won\u0027t Do\\\", \\\"resolved\\\": \\\"Done\\\" }\\n\\n# Define JIRA fields here\\ninputs.jira_fields = dict_to_json_str({\\n  \\\"resolution\\\": { \\\"name\\\": resolution_map.get(str(incident.resolution_id).lower(), \\\"Done\\\") }\\n})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0n9xl5o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t9q33k\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0n9xl5o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qcmweq\"/\u003e\u003cendEvent id=\"EndEvent_0hn51d2\"\u003e\u003cincoming\u003eSequenceFlow_0t9q33k\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0t9q33k\" sourceRef=\"ServiceTask_0qcmweq\" targetRef=\"EndEvent_0hn51d2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13lgrjc\"\u003e\u003ctext\u003e\u003c![CDATA[Choose a Jira Transition Id for the Jira issue\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0qln3nr\" sourceRef=\"ServiceTask_0qcmweq\" targetRef=\"TextAnnotation_13lgrjc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"504\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"499\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qcmweq\" id=\"ServiceTask_0qcmweq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"756\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0n9xl5o\" id=\"SequenceFlow_0n9xl5o_di\"\u003e\u003comgdi:waypoint x=\"540\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"756\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"603\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hn51d2\" id=\"EndEvent_0hn51d2_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1025\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"998\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t9q33k\" id=\"SequenceFlow_0t9q33k_di\"\u003e\u003comgdi:waypoint x=\"856\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"945\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"945\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1025\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"915\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13lgrjc\" id=\"TextAnnotation_13lgrjc_di\"\u003e\u003comgdc:Bounds height=\"66\" width=\"205\" x=\"524\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0qln3nr\" id=\"Association_0qln3nr_di\"\u003e\u003comgdi:waypoint x=\"756\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"681\" xsi:type=\"omgdc:Point\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Either update a Jira Issue (such as a priority change) or close the Issue when an Incident is closed. The Rule associated with this Workflow should only trigger if a Jira Issue is already linked.",
      "export_key": "jira_transition_issue",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1648663217934,
      "name": "Example: Jira Transition Issue",
      "object_type": "incident",
      "programmatic_name": "jira_transition_issue",
      "tags": [
        {
          "tag_handle": "fn_jira",
          "value": null
        }
      ],
      "uuid": "3460a425-4adf-419d-ad67-89b8ba427068",
      "workflow_id": 44
    }
  ],
  "workspaces": []
}
