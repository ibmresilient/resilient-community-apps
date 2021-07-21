{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Task Utils - Add Note to Task",
      "id": 213,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Task Utils - Add Note to Task",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e5231741-196c-4303-872f-42547805ed55",
      "view_items": [
        {
          "content": "eb9b0faf-dcf2-4a25-8f8e-b6454bdc5ab0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_utils_add_note_to_task"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Task Utils - Close Task",
      "id": 214,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Task Utils - Close Task",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "35ea572b-b7c7-4653-b4f0-efb8f861b7a3",
      "view_items": [
        {
          "content": "eb9b0faf-dcf2-4a25-8f8e-b6454bdc5ab0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_utils_close_task"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Task Utils - Create Custom Task",
      "id": 215,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Task Utils - Create Custom Task",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8af1bc2f-5cba-459f-a15d-e6935e55a37f",
      "view_items": [
        {
          "content": "eb9b0faf-dcf2-4a25-8f8e-b6454bdc5ab0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_utils_create_custom_task"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Task Utils - Make this Task Optional",
      "id": 216,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Task Utils - Make this Task Optional",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bb1d7585-8ea4-40ba-ab82-ad1073c63cde",
      "view_items": [],
      "workflows": [
        "task_utils_mark_task_optional"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1613527698789,
  "export_format_version": 2,
  "extensions": [],
  "fields": [
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
      "id": 188,
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
      "tags": [],
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
      "export_key": "__function/task_utils_payload",
      "hide_notification": false,
      "id": 1471,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "task_utils_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 9,
          "name": "Create New Optional Task",
          "template": {
            "content": "{\n\"required\" : false\n}\n",
            "format": "text"
          },
          "uuid": "eb8e7b75-11fc-4cc5-b0e2-1bf89e6066de"
        },
        {
          "id": 7,
          "name": "Create New Required Task with Instructions Text",
          "template": {
            "content": "{\n\"instr_text\": \"Please complete this required task.\",\n\"required\" : true\n}\n",
            "format": "text"
          },
          "uuid": "176a2b05-74f0-4e47-951d-9e094871b02b"
        },
        {
          "id": 8,
          "name": "Update Existing Task Marking it as optional",
          "template": {
            "content": "{\n\"required\": false\n}",
            "format": "text"
          },
          "uuid": "cd76e6ec-aa6d-4fa3-934e-8faa2690c463"
        }
      ],
      "text": "task_utils_payload",
      "tooltip": "A JSON Object which may contain the Phase, Instruction Set or Assigned User values for a new task",
      "type_id": 11,
      "uuid": "361f420f-3184-4426-9fdc-7649d58eac92",
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
      "export_key": "__function/task_name",
      "hide_notification": false,
      "id": 1473,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "task_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e9af077a-3b1c-4ff7-befb-8dfedd3c7dbc",
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
      "export_key": "__function/task_utils_note_type",
      "hide_notification": false,
      "id": 1474,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "task_utils_note_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_utils_note_type",
      "tooltip": "A field used to specify where the field task_utils_note_body is plaintext or html.",
      "type_id": 11,
      "uuid": "5e23b145-2bec-4d82-ad50-dc115f355360",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "text",
          "properties": null,
          "uuid": "6a2e4e13-7f0c-4dab-a460-86b04769ceeb",
          "value": 1252
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "html",
          "properties": null,
          "uuid": "561fd0f9-c557-4d63-a8fc-20539ea8c86a",
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
      "export_key": "__function/task_utils_note_body",
      "hide_notification": false,
      "id": 1472,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "task_utils_note_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_utils_note_body",
      "tooltip": "A Text field used to specify the note that will be added to a given Task. Accepts text or html and is parsed based on the result of task_utils_note_type. Default is text",
      "type_id": 11,
      "uuid": "44c4c600-f22d-4bf5-bbf4-efad358f02f5",
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
      "id": 217,
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
      "export_key": "actioninvocation/task_utils_task_name",
      "hide_notification": false,
      "id": 1470,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "task_utils_task_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Task Utils Task Name",
      "tooltip": "",
      "type_id": 6,
      "uuid": "eb9b0faf-dcf2-4a25-8f8e-b6454bdc5ab0",
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
        "content": "A function which takes in the ID of an existing Task and then adds either a plain or richtext note to the Task.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Add Note",
      "export_key": "task_utils_add_note",
      "id": 117,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1613526993690,
      "name": "task_utils_add_note",
      "tags": [],
      "uuid": "da653a3d-964a-4e28-a6e0-c436db0b6774",
      "version": 1,
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
          "content": "e9af077a-3b1c-4ff7-befb-8dfedd3c7dbc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5e23b145-2bec-4d82-ad50-dc115f355360",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "44c4c600-f22d-4bf5-bbf4-efad358f02f5",
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
          "name": "Example: Task Utils - Add Note to Task",
          "object_type": "incident",
          "programmatic_name": "task_utils_add_note_to_task",
          "tags": [],
          "uuid": null,
          "workflow_id": 161
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
        "content": "A function which will attempt to close either a System or Custom task using the REST API.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Close Task",
      "export_key": "task_utils_close_task",
      "id": 118,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1613527062867,
      "name": "task_utils_close_task",
      "tags": [],
      "uuid": "7227998a-16d3-46f6-bc88-cdc625ff99da",
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
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e9af077a-3b1c-4ff7-befb-8dfedd3c7dbc",
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
          "name": "Example: Task Utils - Close Task",
          "object_type": "incident",
          "programmatic_name": "task_utils_close_task",
          "tags": [],
          "uuid": null,
          "workflow_id": 162
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
        "content": "A function which can be used to create a custom task using the REST API.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Create Custom Task",
      "export_key": "task_utils_create",
      "id": 119,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1613526993883,
      "name": "task_utils_create",
      "tags": [],
      "uuid": "c4281bd4-d872-4562-b7c8-b0e379aea8ad",
      "version": 1,
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
          "content": "e9af077a-3b1c-4ff7-befb-8dfedd3c7dbc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "361f420f-3184-4426-9fdc-7649d58eac92",
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
          "name": "Example: Task Utils - Create Custom Task",
          "object_type": "incident",
          "programmatic_name": "task_utils_create_custom_task",
          "tags": [],
          "uuid": null,
          "workflow_id": 160
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
        "content": "A function which takes in the ID of an existing Task and a task_utils_payload which is a JSON String of the task details to update.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Update Task",
      "export_key": "task_utils_update_task",
      "id": 120,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1613526993978,
      "name": "task_utils_update_task",
      "tags": [],
      "uuid": "bd8df53a-6443-40f1-90f9-eb5993996925",
      "version": 1,
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
          "content": "e9af077a-3b1c-4ff7-befb-8dfedd3c7dbc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "361f420f-3184-4426-9fdc-7649d58eac92",
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
          "name": "Example: Task Utils - Mark Task a Optional",
          "object_type": "task",
          "programmatic_name": "task_utils_mark_task_optional",
          "tags": [],
          "uuid": null,
          "workflow_id": 163
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 103,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1613527696706,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1613527696706,
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
      "export_key": "fn_task_utils",
      "name": "fn_task_utils",
      "programmatic_name": "fn_task_utils",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "c697d977-c173-42e1-b6d8-8580b591f0cb"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 5634,
    "major": 36,
    "minor": 0,
    "version": "36.0.5634"
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
        "workflow_id": "task_utils_add_note_to_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_utils_add_note_to_task\" isExecutable=\"true\" name=\"Example: Task Utils - Add Note to Task\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow which takes a Task\u0027s ID and a adds either a new text or richtext note to that task.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p9kocl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_092ivum\" name=\"Task Utils: Add Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"da653a3d-964a-4e28-a6e0-c436db0b6774\"\u003e{\"inputs\":{\"5e23b145-2bec-4d82-ad50-dc115f355360\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"6a2e4e13-7f0c-4dab-a460-86b04769ceeb\"}},\"44c4c600-f22d-4bf5-bbf4-efad358f02f5\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"test\"}}},\"pre_processing_script\":\"inputs.incident_id = incident.id \\ninputs.task_name = rule.properties.task_utils_task_name\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p9kocl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c0q3pi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p9kocl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_092ivum\"/\u003e\u003cendEvent id=\"EndEvent_0bawsi0\"\u003e\u003cincoming\u003eSequenceFlow_0c0q3pi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c0q3pi\" sourceRef=\"ServiceTask_092ivum\" targetRef=\"EndEvent_0bawsi0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_092ivum\" id=\"ServiceTask_092ivum_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"437\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p9kocl\" id=\"SequenceFlow_0p9kocl_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"317.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0bawsi0\" id=\"EndEvent_0bawsi0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"768\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"786\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c0q3pi\" id=\"SequenceFlow_0c0q3pi_di\"\u003e\u003comgdi:waypoint x=\"537\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"654\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"654\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"768\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"669\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "a@example.com",
      "description": "An example workflow which takes a Task\u0027s ID and a adds either a new text or richtext note to that task.",
      "export_key": "task_utils_add_note_to_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1613527228394,
      "name": "Example: Task Utils - Add Note to Task",
      "object_type": "incident",
      "programmatic_name": "task_utils_add_note_to_task",
      "tags": [],
      "uuid": "0e4cc9b4-7b19-420c-8051-b3c8aafb78ab",
      "workflow_id": 161
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_utils_mark_task_optional",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_utils_mark_task_optional\" isExecutable=\"true\" name=\"Example: Task Utils - Mark Task a Optional\"\u003e\u003cdocumentation\u003eAn example workflow which is invoked on a Task object setting its Required attribute to false.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12el6ix\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1cbi5k2\" name=\"Task Utils: Update Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bd8df53a-6443-40f1-90f9-eb5993996925\"\u003e{\"inputs\":{\"361f420f-3184-4426-9fdc-7649d58eac92\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n\\\"required\\\": false\\n}\"}}}},\"pre_processing_script\":\"inputs.task_id = task.id\\ninputs.incident_id = incident.id\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12el6ix\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10dzipb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12el6ix\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1cbi5k2\"/\u003e\u003cendEvent id=\"EndEvent_1idpf1w\"\u003e\u003cincoming\u003eSequenceFlow_10dzipb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10dzipb\" sourceRef=\"ServiceTask_1cbi5k2\" targetRef=\"EndEvent_1idpf1w\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cbi5k2\" id=\"ServiceTask_1cbi5k2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"464\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12el6ix\" id=\"SequenceFlow_12el6ix_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"464\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"346\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1idpf1w\" id=\"EndEvent_1idpf1w_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"785\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"803\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10dzipb\" id=\"SequenceFlow_10dzipb_di\"\u003e\u003comgdi:waypoint x=\"564\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"785\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"674.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "An example workflow which is invoked on a Task object setting its Required attribute to false.",
      "export_key": "task_utils_mark_task_optional",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1613526996043,
      "name": "Example: Task Utils - Mark Task a Optional",
      "object_type": "task",
      "programmatic_name": "task_utils_mark_task_optional",
      "tags": [],
      "uuid": "92aac380-cb33-454d-a12f-95efe1554ef7",
      "workflow_id": 163
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_utils_close_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_utils_close_task\" isExecutable=\"true\" name=\"Example: Task Utils - Close Task\"\u003e\u003cdocumentation\u003eAn example workflow which takes a Task name from an activity field and attempts to close the task.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ftz4ce\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0bcdcvx\" name=\"Task Utils: Close Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7227998a-16d3-46f6-bc88-cdc625ff99da\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_name = rule.properties.task_utils_task_name\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ftz4ce\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0egwi7i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ftz4ce\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0bcdcvx\"/\u003e\u003cendEvent id=\"EndEvent_0pwbflo\"\u003e\u003cincoming\u003eSequenceFlow_0egwi7i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0egwi7i\" sourceRef=\"ServiceTask_0bcdcvx\" targetRef=\"EndEvent_0pwbflo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0bcdcvx\" id=\"ServiceTask_0bcdcvx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"385\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ftz4ce\" id=\"SequenceFlow_1ftz4ce_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"291.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0pwbflo\" id=\"EndEvent_0pwbflo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"694\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"712\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0egwi7i\" id=\"SequenceFlow_0egwi7i_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"694\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"589.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "An example workflow which takes a Task name from an activity field and attempts to close the task.",
      "export_key": "task_utils_close_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1613526995783,
      "name": "Example: Task Utils - Close Task",
      "object_type": "incident",
      "programmatic_name": "task_utils_close_task",
      "tags": [],
      "uuid": "0afd335d-46bc-439b-9629-fdcf9a4916c0",
      "workflow_id": 162
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_utils_create_custom_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_utils_create_custom_task\" isExecutable=\"true\" name=\"Example: Task Utils - Create Custom Task\"\u003e\u003cdocumentation\u003eAn example workflow used to demonstrate how you can create a custom task using the Task Utils Integration. This example workflow shows how you can use the Pre-Processing script to prepare a custom JSON Payload based on your use case.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qndso1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_09xgwbr\" name=\"Task Utils: Create Custom Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4281bd4-d872-4562-b7c8-b0e379aea8ad\"\u003e{\"inputs\":{\"361f420f-3184-4426-9fdc-7649d58eac92\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n\\\"required\\\" : false\\n}\\n\"}}}},\"pre_processing_script\":\"#######################################\\n### Define pre-processing functions ###\\n#######################################\\npayload = {\\n\\\"required\\\": True,\\n\\\"instr_text\\\": \\\"Close out this required Task\\\",\\n\\\"phase_id\\\": \\\"Initial\\\"\\n}\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON stringself.\\n     Supports basestring, bool and int.\\n     If the value is None, it sets it to False\\\"\\\"\\\"\\n\\n  json_str = \u0027\\\"{ {0} }\\\"\u0027\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n  \\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n    \\n      \\n    if value is None:\\n      value = False\\n      \\n    \\n    if isinstance(value, basestring):\\n      entries.append(json_entry_str.format(key, value))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n    \\n    else:\\n      entries.append(json_entry.format(key, value))\\n  \\n  return \u0027{\u0027 + \u0027,\u0027.join(entries) + \u0027}\u0027\\n\\n# If you don\u0027t already have something in task_utils_payload\\nif inputs.task_utils_payload != None: \\n  # prepare a JSON payload using above code; \\n  inputs.task_utils_payload = dict_to_json_str(payload)\\n\\n# Take the incident id from this incident\\ninputs.incident_id = incident.id\\n\\n# If you specified a value in the Activity Field then use it for task_name\\nif rule.properties.task_utils_task_name != None:\\n  inputs.task_name = rule.properties.task_utils_task_name\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qndso1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1y7ygs4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qndso1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_09xgwbr\"/\u003e\u003cendEvent id=\"EndEvent_09t1as3\"\u003e\u003cincoming\u003eSequenceFlow_1y7ygs4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1y7ygs4\" sourceRef=\"ServiceTask_09xgwbr\" targetRef=\"EndEvent_09t1as3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_09xgwbr\" id=\"ServiceTask_09xgwbr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"430\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qndso1\" id=\"SequenceFlow_1qndso1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"430\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"314\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09t1as3\" id=\"EndEvent_09t1as3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"781\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"799\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1y7ygs4\" id=\"SequenceFlow_1y7ygs4_di\"\u003e\u003comgdi:waypoint x=\"530\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"655.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "An example workflow used to demonstrate how you can create a custom task using the Task Utils Integration. This example workflow shows how you can use the Pre-Processing script to prepare a custom JSON Payload based on your use case.",
      "export_key": "task_utils_create_custom_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1613526995017,
      "name": "Example: Task Utils - Create Custom Task",
      "object_type": "incident",
      "programmatic_name": "task_utils_create_custom_task",
      "tags": [],
      "uuid": "61c095e5-db99-4db9-aa0a-8b94125f1978",
      "workflow_id": 160
    }
  ],
  "workspaces": []
}
