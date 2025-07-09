{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1751963487628,
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
      "id": 913,
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 917,
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
      "export_key": "__function/task_name",
      "hide_notification": false,
      "id": 1038,
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
      "export_key": "__function/task_utils_payload",
      "hide_notification": false,
      "id": 1039,
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
          "id": 7,
          "name": "Update Existing Task Marking it as optional",
          "template": {
            "content": "{\n\"required\": false\n}",
            "format": "text"
          },
          "uuid": "cd76e6ec-aa6d-4fa3-934e-8faa2690c463"
        },
        {
          "id": 8,
          "name": "Create New Optional Task",
          "template": {
            "content": "{\n\"required\" : false\n}\n",
            "format": "text"
          },
          "uuid": "eb8e7b75-11fc-4cc5-b0e2-1bf89e6066de"
        },
        {
          "id": 9,
          "name": "Create New Required Task with Instructions Text",
          "template": {
            "content": "{\n\"instr_text\": \"Please complete this required task.\",\n\"required\" : true\n}\n",
            "format": "text"
          },
          "uuid": "176a2b05-74f0-4e47-951d-9e094871b02b"
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
      "export_key": "__function/task_utils_note_body",
      "hide_notification": false,
      "id": 1040,
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
      "export_key": "__function/task_utils_note_type",
      "hide_notification": false,
      "id": 1041,
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
          "value": 302
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "html",
          "properties": null,
          "uuid": "561fd0f9-c557-4d63-a8fc-20539ea8c86a",
          "value": 303
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
      "created_date": 1750845283701,
      "description": {
        "content": "A function which takes in the ID of an existing Task and then adds either a plain or richtext note to the Task.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Add Note",
      "export_key": "task_utils_add_note",
      "id": 62,
      "last_modified_by": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1750845283701,
      "name": "task_utils_add_note",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "da653a3d-964a-4e28-a6e0-c436db0b6774",
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
          "workflow_id": 106
        }
      ]
    },
    {
      "created_date": 1750845283861,
      "description": {
        "content": "A function which will attempt to close either a System or Custom task using the REST API.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Close Task",
      "export_key": "task_utils_close_task",
      "id": 63,
      "last_modified_by": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1750845283861,
      "name": "task_utils_close_task",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "7227998a-16d3-46f6-bc88-cdc625ff99da",
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
          "workflow_id": 104
        }
      ]
    },
    {
      "created_date": 1750845283992,
      "description": {
        "content": "A function which can be used to create a custom task using the REST API.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Create Custom Task",
      "export_key": "task_utils_create",
      "id": 64,
      "last_modified_by": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1750845283992,
      "name": "task_utils_create",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c4281bd4-d872-4562-b7c8-b0e379aea8ad",
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
          "workflow_id": 107
        }
      ]
    },
    {
      "created_date": 1750845284125,
      "description": {
        "content": "A function which takes in the ID of an existing Task and a task_utils_payload which is a JSON String of the task details to update.",
        "format": "text"
      },
      "destination_handle": "fn_task_utils",
      "display_name": "Task Utils: Update Task",
      "export_key": "task_utils_update_task",
      "id": 65,
      "last_modified_by": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1750845284125,
      "name": "task_utils_update_task",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "bd8df53a-6443-40f1-90f9-eb5993996925",
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
          "workflow_id": 105
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 90,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1751963485112,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1751963485112,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "34f15e91-6f19-4cb7-9529-6d1dc37f4ce7"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_task_utils",
      "name": "fn_task_utils",
      "programmatic_name": "fn_task_utils",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "c697d977-c173-42e1-b6d8-8580b591f0cb"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce\" isExecutable=\"true\" name=\"playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_06uey7j\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Task Utils: Add Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"da653a3d-964a-4e28-a6e0-c436db0b6774\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id \\ninputs.task_name = playbook.inputs.task_utils_task_name\\ninputs.task_utils_note_type = \\\"text\\\"  #html or text\\ninputs.task_utils_note_body = playbook.inputs.task_utils_task_note.content\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"task_note_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_06uey7j\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ob2g5b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_06uey7j\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Task Utils: Add notes\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"5bbf5ecc-9243-4596-a96c-33b8be7fe16c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ob2g5b\u003c/incoming\u003e\u003coutgoing\u003eFlow_03tb879\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0ob2g5b\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_03tb879\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_03tb879\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_03tb879\" id=\"Flow_03tb879_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ob2g5b\" id=\"Flow_0ob2g5b_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06uey7j\" id=\"Flow_06uey7j_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.1875\" x=\"628\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"656\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1751019310408,
      "creator_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
      "description": {
        "content": "An example playbook which takes a task\u0027s name and adds either a new text or richtext note to that task.",
        "format": "text"
      },
      "display_name": "Task Utils: Add Note To Task - Example (PB)",
      "export_key": "task_utils_add_note_to_task_example_pb",
      "field_type_handle": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
      "fields_type": {
        "actions": [],
        "display_name": "Task Utils: Add Note To Task - Example (PB)",
        "export_key": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
        "fields": {
          "task_utils_task_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce/task_utils_task_name",
            "hide_notification": false,
            "id": 1044,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "task_utils_task_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Task Name",
            "tooltip": "Enter the task name to add note",
            "type_id": 1052,
            "uuid": "6620992e-8b83-40eb-a7fe-cf6900d4bc8d",
            "values": []
          },
          "task_utils_task_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce/task_utils_task_note",
            "hide_notification": false,
            "id": 1050,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "task_utils_task_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Task Note",
            "tooltip": "Enter a note to add.",
            "type_id": 1052,
            "uuid": "1ac1d5d4-6ab6-453d-b894-675a3f4f4d86",
            "values": []
          }
        },
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
        "type_name": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
        "uuid": "55c9db8f-737f-4cd4-ae28-5005ecebbfec"
      },
      "has_logical_errors": false,
      "id": 48,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1751963006611,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1751019310603,
          "description": "Adding task notes.",
          "enabled": false,
          "export_key": "Task Utils: Add notes",
          "id": 49,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1751962854735,
          "name": "Task Utils: Add notes",
          "object_type": "incident",
          "playbook_handle": "task_utils_add_note_to_task_example_pb",
          "programmatic_name": "task_utils_add_note_to_task_example_pb_task_utils_add_notes",
          "script_text": "results = playbook.functions.results.task_note_result\nif not results.success:\n  note_text = f\"\u003cb\u003eTask Utils: Add Note to Task - Example (PB):\u003c/b\u003e Failure: {results.reason}\"",
          "tags": [],
          "uuid": "5bbf5ecc-9243-4596-a96c-33b8be7fe16c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "6620992e-8b83-40eb-a7fe-cf6900d4bc8d",
            "element": "field_uuid",
            "field_type": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "1ac1d5d4-6ab6-453d-b894-675a3f4f4d86",
            "element": "field_uuid",
            "field_type": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "task_utils_add_note_to_task_example_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_93de684a-b0d1-452e-8a3a-8b532a9ec1ce",
        "id": 51,
        "name": "playbook_93de684a_b0d1_452e_8a3a_8b532a9ec1ce",
        "type": "playbook",
        "uuid": "57e58175-271d-47d7-895b-da92f381f098"
      },
      "tags": [],
      "type": "default",
      "uuid": "93de684a-b0d1-452e-8a3a-8b532a9ec1ce",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_566ceec9_3828_4880_9559_463ae7041d49\" isExecutable=\"true\" name=\"playbook_566ceec9_3828_4880_9559_463ae7041d49\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1cwqtof\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Task Utils: Close Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7227998a-16d3-46f6-bc88-cdc625ff99da\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_name = playbook.inputs.task_utils_task_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"task_close_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1cwqtof\u003c/incoming\u003e\u003coutgoing\u003eFlow_15jvjow\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1cwqtof\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Task Utils: Close Task\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"d0e4f040-365c-473c-aaf6-1b4558701a67\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_15jvjow\u003c/incoming\u003e\u003coutgoing\u003eFlow_1mtpjiq\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_15jvjow\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1mtpjiq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1mtpjiq\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_566ceec9_3828_4880_9559_463ae7041d49\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1mtpjiq\" id=\"Flow_1mtpjiq_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"432\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"494\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_15jvjow\" id=\"Flow_15jvjow_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"348\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1cwqtof\" id=\"Flow_1cwqtof_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.1875\" x=\"628\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"348\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"656\" y=\"494\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1751020408610,
      "creator_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
      "description": {
        "content": "An example playbook which takes a task name from an activity field and attempts to close the task.",
        "format": "text"
      },
      "display_name": "Task Utils: Close Task - Example (PB)",
      "export_key": "task_utils_close_task_example_pb",
      "field_type_handle": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
      "fields_type": {
        "actions": [],
        "display_name": "Task Utils: Close Task - Example (PB)",
        "export_key": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
        "fields": {
          "task_utils_task_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_566ceec9_3828_4880_9559_463ae7041d49/task_utils_task_name",
            "hide_notification": false,
            "id": 1049,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "task_utils_task_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Task name",
            "tooltip": "Enter task name to close",
            "type_id": 1053,
            "uuid": "00066ff7-a395-4166-bf7d-b1f6d71b1b23",
            "values": []
          }
        },
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
        "type_name": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
        "uuid": "c0b23501-fce8-481b-8b2a-61d03ef32075"
      },
      "has_logical_errors": false,
      "id": 49,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1751963089655,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1751021301601,
          "description": "Closes a given task.",
          "enabled": false,
          "export_key": "Task Utils: Close Task",
          "id": 50,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1751034063313,
          "name": "Task Utils: Close Task",
          "object_type": "incident",
          "playbook_handle": "task_utils_close_task_example_pb",
          "programmatic_name": "task_utils_close_task_example_pb_task_util_close_task",
          "script_text": "results = playbook.functions.results.task_close_result\n\nif results:\n  note_text = f\"\u003cb\u003e Task Utils: Close Task - Example (PB): \u003c/b\u003e Task: {playbook.inputs.task_utils_task_name} closed successfully\"\nelse:\n  note_text = f\"\u003cb\u003e Task Utils: Close Task - Example (PB): \u003c/b\u003e Failed: {results.reason}\"\n  \nincident.addNote(note_text)",
          "tags": [],
          "uuid": "d0e4f040-365c-473c-aaf6-1b4558701a67"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "00066ff7-a395-4166-bf7d-b1f6d71b1b23",
            "element": "field_uuid",
            "field_type": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "task_utils_close_task_example_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_566ceec9-3828-4880-9559-463ae7041d49",
        "id": 52,
        "name": "playbook_566ceec9_3828_4880_9559_463ae7041d49",
        "type": "playbook",
        "uuid": "5d227e06-44f7-4614-98b4-4bab41aacdc0"
      },
      "tags": [],
      "type": "default",
      "uuid": "566ceec9-3828-4880-9559-463ae7041d49",
      "version": 11
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 16,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0\" isExecutable=\"true\" name=\"playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qaif69\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Task Utils: Create Custom Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4281bd4-d872-4562-b7c8-b0e379aea8ad\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n\\n# Take the incident id from this incident\\ninputs.incident_id = incident.id\\n\\n# If you specified a value in the Activity Field then use it for task_name\\nif playbook.inputs.task_utils_task_name:\\n    inputs.task_name = playbook.inputs.task_utils_task_name\\n\\npayload = {\\n    \\\"required\\\": True,\\n    \\\"instr_text\\\": \\\"Close out this required Task\\\",\\n    \\\"phase_id\\\": \\\"Initial\\\"\\n}\\n\\ninputs.task_utils_payload = dumps(payload)\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_task_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qaif69\u003c/incoming\u003e\u003coutgoing\u003eFlow_0twv0al\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qaif69\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Task Utils: Create Custom Task\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f8672af1-eb92-488d-b52a-c96b72d194ed\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0twv0al\u003c/incoming\u003e\u003coutgoing\u003eFlow_0658fag\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0twv0al\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0658fag\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0658fag\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0658fag\" id=\"Flow_0658fag_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0twv0al\" id=\"Flow_0twv0al_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qaif69\" id=\"Flow_0qaif69_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.1875\" x=\"628\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"656\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1751030481272,
      "creator_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
      "description": {
        "content": "An example playbook used to demonstrate how you can create a custom task using the Task Utils Integration. This example playbook shows how you can use the Pre-Processing script to prepare a custom JSON Payload based on your use case.",
        "format": "text"
      },
      "display_name": "Task Utils: Create Custom Task - Example (PB)",
      "export_key": "task_utils_create_custom_task_example_pb",
      "field_type_handle": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
      "fields_type": {
        "actions": [],
        "display_name": "Task Utils: Create Custom Task - Example (PB)",
        "export_key": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
        "fields": {
          "task_utils_task_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0/task_utils_task_name",
            "hide_notification": false,
            "id": 1048,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "task_utils_task_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Task Name",
            "tooltip": "Enter task name you want to create.",
            "type_id": 1056,
            "uuid": "4c9ca784-450d-4b31-9d73-a4693c0c8808",
            "values": []
          }
        },
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
        "type_name": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
        "uuid": "28453a29-187c-48c0-a9eb-8bbfc534d27f"
      },
      "has_logical_errors": false,
      "id": 52,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1751963120144,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1751030481424,
          "description": "Creating a new custom task.",
          "enabled": false,
          "export_key": "Task Utils: Create Custom Task",
          "id": 53,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1751033646535,
          "name": "Task Utils: Create Custom Task",
          "object_type": "incident",
          "playbook_handle": "task_utils_create_custom_task_example_pb",
          "programmatic_name": "task_utils_create_custom_task_example_pb_task_util_create_custom_task",
          "script_text": "results = playbook.functions.results.create_task_result\n\nif results.success:\n  note_text = f\"\u003cb\u003eTask Utils: Create Custom Task - Example (PB):\u003c/b\u003e {playbook.inputs.task_utils_task_name} created sucessfully\"\nelse:\n  note_text = f\"\u003cb\u003eTask Utils: Create Custom Task - Example (PB):\u003c/b\u003e Failed: {results.reason}\"\n  \nincident.addNote(note_text)",
          "tags": [],
          "uuid": "f8672af1-eb92-488d-b52a-c96b72d194ed"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "4c9ca784-450d-4b31-9d73-a4693c0c8808",
            "element": "field_uuid",
            "field_type": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "task_utils_create_custom_task_example_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_3aa344a5-1dab-4581-a1ad-6bc6550d5ee0",
        "id": 55,
        "name": "playbook_3aa344a5_1dab_4581_a1ad_6bc6550d5ee0",
        "type": "playbook",
        "uuid": "b76cf270-47f9-4fb7-a980-6a322f59234b"
      },
      "tags": [],
      "type": "default",
      "uuid": "3aa344a5-1dab-4581-a1ad-6bc6550d5ee0",
      "version": 19
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_18045e38_6981_4b7f_923b_8e3e9d759242\" isExecutable=\"true\" name=\"playbook_18045e38_6981_4b7f_923b_8e3e9d759242\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1w5788o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Task Utils: Update Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bd8df53a-6443-40f1-90f9-eb5993996925\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n\\ninputs.task_id = task.id\\ninputs.incident_id = incident.id\\ninputs.task_name = task.name\\n\\npayload = {\\n\\\"required\\\": False\\n}\\ninputs.task_utils_payload = dumps(payload)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"task_as_optional_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1w5788o\u003c/incoming\u003e\u003coutgoing\u003eFlow_1sgcflo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1w5788o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Task Util: Mark Task a Optional\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"86c0804b-7927-40ba-a29b-84d3b58ee877\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1sgcflo\u003c/incoming\u003e\u003coutgoing\u003eFlow_16d98q0\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1sgcflo\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_16d98q0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_16d98q0\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_18045e38_6981_4b7f_923b_8e3e9d759242\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_16d98q0\" id=\"Flow_16d98q0_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"454\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sgcflo\" id=\"Flow_1sgcflo_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1w5788o\" id=\"Flow_1w5788o_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.578125\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"655\" y=\"454\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1751031119115,
      "creator_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_18045e38_6981_4b7f_923b_8e3e9d759242",
      "description": {
        "content": "An example playbook to make task optional",
        "format": "text"
      },
      "display_name": "Task Utils: Mark Task as Optional - Example (PB)",
      "export_key": "task_utils_mark_task_as_optional__example_pb",
      "field_type_handle": "playbook_18045e38_6981_4b7f_923b_8e3e9d759242",
      "fields_type": {
        "actions": [],
        "display_name": "Task Utils: Mark Task as Optional - Example (PB)",
        "export_key": "playbook_18045e38_6981_4b7f_923b_8e3e9d759242",
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
        "type_name": "playbook_18045e38_6981_4b7f_923b_8e3e9d759242",
        "uuid": "61e51d01-6ea5-4cbb-a030-97e56801b3ce"
      },
      "has_logical_errors": false,
      "id": 53,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "admin example",
        "id": 5,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1751031611773,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1751031119265,
          "description": "Mark task as optional.",
          "enabled": false,
          "export_key": "Task Util: Mark Task a Optional",
          "id": 54,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1751032016353,
          "name": "Task Util: Mark Task a Optional",
          "object_type": "task",
          "playbook_handle": "task_utils_mark_task_as_optional__example_pb",
          "programmatic_name": "task_utils_mark_task_as_optional__example_pb_task_util_mark_task_a_optional",
          "script_text": "results = playbook.functions.results.task_as_optional_result\n\nif results:\n  note_text = f\"\u003cb\u003e Task Utils: Mark Task as Optional - Example (PB):\u003c/b\u003e Task: {task.name} marked as optinal\"\nelse:\n  note_text = f\"\u003cb\u003e Task Utils: Mark Task as Optional - Example (PB):\u003c/b\u003e Failed: {results.reason}\"\n  \ntask.addNote(note_text)",
          "tags": [],
          "uuid": "86c0804b-7927-40ba-a29b-84d3b58ee877"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "task_utils_mark_task_as_optional__example_pb",
      "object_type": "task",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_18045e38-6981-4b7f-923b-8e3e9d759242",
        "id": 56,
        "name": "playbook_18045e38_6981_4b7f_923b_8e3e9d759242",
        "type": "playbook",
        "uuid": "5d724e97-99b0-4f06-b7ea-437ee84a33d0"
      },
      "tags": [],
      "type": "default",
      "uuid": "18045e38-6981-4b7f-923b-8e3e9d759242",
      "version": 6
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 9339,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.9339"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
