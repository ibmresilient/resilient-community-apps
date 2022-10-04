{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post an Incident to Microsoft Teams",
      "id": 42,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post an Incident to Microsoft Teams",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ab423457-6a80-43e1-ba72-24d7729359dd",
      "view_items": [],
      "workflows": [
        "example_post_incident_to_ms_teams"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Post a Task to Microsoft Teams",
      "id": 41,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Post a Task to Microsoft Teams",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a4ea172e-6103-4db1-87a0-17a5e2e27a97",
      "view_items": [],
      "workflows": [
        "example_post_task_to_microsoft_teams"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Group",
      "id": 50,
      "logic_type": "all",
      "message_destinations": [
        "fn_teams"
      ],
      "name": "MS Teams: Create Group",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f63657ce-d1d9-4459-bb26-e8ee61eb71cf",
      "view_items": [],
      "workflows": [
        "incident_create_a_teams_group"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1664884493474,
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 325,
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
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
      "export_key": "__function/teams_mrkdown",
      "hide_notification": false,
      "id": 327,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "teams_mrkdown",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_mrkdown",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
      "export_key": "__function/teams_payload",
      "hide_notification": false,
      "id": 324,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_payload",
      "tooltip": "json of teams conversation message: sections, title, text, facts",
      "type_id": 11,
      "uuid": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
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
      "id": 326,
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
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
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
      "export_key": "__function/teams_channel",
      "hide_notification": false,
      "id": 323,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "templates": [],
      "text": "teams_channel",
      "tooltip": "Lookup value to channel to post a message",
      "type_id": 11,
      "uuid": "76023ce3-fc17-41d1-9002-2392283ce315",
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
      "created_date": 1664451842940,
      "description": {
        "content": "A function to create a Microsoft Group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create group",
      "export_key": "ms_teams_create_group",
      "id": 11,
      "last_modified_by": {
        "display_name": "Admin Resilient",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1664884312183,
      "name": "ms_teams_create_group",
      "tags": [],
      "uuid": "120d2055-a0de-413b-b5d7-444d289dd469",
      "version": 3,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Incident: Create a Teams Group",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_teams_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    },
    {
      "created_date": 1664190890396,
      "description": {
        "content": "Post a message to a Microsoft Teams channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "Teams Post Message",
      "export_key": "teams_post_message",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin Resilient",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1664884307458,
      "name": "teams_post_message",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "0c8e4497-c131-4d5d-bdf3-3153d30b9bbc",
      "version": 4,
      "view_items": [
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "76023ce3-fc17-41d1-9002-2392283ce315",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
          "name": "Example: Post Incident to Microsoft Teams",
          "object_type": "incident",
          "programmatic_name": "example_post_incident_to_ms_teams",
          "tags": [
            {
              "tag_handle": "fn_teams",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 30
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Post Task to Microsoft Teams",
          "object_type": "task",
          "programmatic_name": "example_post_task_to_microsoft_teams",
          "tags": [
            {
              "tag_handle": "fn_teams",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 29
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 83,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1664884490997,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1664884490997,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "fa955774-f138-427c-9278-ce463aa6c484"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_teams",
      "name": "fn_teams",
      "programmatic_name": "fn_teams",
      "tags": [],
      "users": [],
      "uuid": "44d59a45-1647-438d-ba45-0bbf0c7506f7"
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
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
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
        "workflow_id": "example_post_task_to_microsoft_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_post_task_to_microsoft_teams\" isExecutable=\"true\" name=\"Example: Post Task to Microsoft Teams\"\u003e\u003cdocumentation\u003eExample of posting incident and task information to Teams as two sections\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0q5lshb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17n68bf\" name=\"Teams Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"testchannel\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\ninputs.task_id = task.id\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"Resilient Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }},\\n  {{ \\\"text\\\": \\\"Task\\\", \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Task\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Instructions\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Due Date\\\", \\\"value\\\": \\\"{}\\\" }}\\n    ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code,\\n   task.name, task.owner_id if task.owner_id else \\\"-\\\", task.instructions.content.replace(\u0027\\\"\u0027, \\\"\u0027\\\") if task.instructions else \\\"-\\\", Date(task.due_date) if task.due_date else \\\"-\\\"\\n   )\\n\\ninputs.teams_payload = payload\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0q5lshb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1j9da45\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0q5lshb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17n68bf\"/\u003e\u003cendEvent id=\"EndEvent_1d26c7r\"\u003e\u003cincoming\u003eSequenceFlow_1j9da45\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1j9da45\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"EndEvent_1d26c7r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1q8nu40\"\u003e\u003ctext\u003eFormat teams_payload as a json object. See pre-processor script for format.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1925sdu\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"TextAnnotation_1q8nu40\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17n68bf\" id=\"ServiceTask_17n68bf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q5lshb\" id=\"SequenceFlow_0q5lshb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1d26c7r\" id=\"EndEvent_1d26c7r_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"415\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1j9da45\" id=\"SequenceFlow_1j9da45_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"415\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"383\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1q8nu40\" id=\"TextAnnotation_1q8nu40_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"185\" x=\"130\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1925sdu\" id=\"Association_1925sdu_di\"\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Example of posting incident and task information to Teams as two sections",
      "export_key": "example_post_task_to_microsoft_teams",
      "last_modified_by": "f32c43b9-be25-4e07-b8a1-fd1c75f57dbd",
      "last_modified_time": 1664795681697,
      "name": "Example: Post Task to Microsoft Teams",
      "object_type": "task",
      "programmatic_name": "example_post_task_to_microsoft_teams",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "b0e19468-93dd-43c1-b73a-be681885870c",
      "workflow_id": 29
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_post_incident_to_ms_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_post_incident_to_ms_teams\" isExecutable=\"true\" name=\"Example: Post Incident to Microsoft Teams\"\u003e\u003cdocumentation\u003eExample of posting incident data to a Microsoft Teams channel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tqeuuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0nrnlka\" name=\"Teams Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"testchannel\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\n\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"Resilient Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code\\n   )\\n\\ninputs.teams_payload = payload\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tqeuuk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14r6yw4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tqeuuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nrnlka\"/\u003e\u003cendEvent id=\"EndEvent_1cx5ym9\"\u003e\u003cincoming\u003eSequenceFlow_14r6yw4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14r6yw4\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"EndEvent_1cx5ym9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ing8rr\"\u003e\u003ctext\u003e\u003c![CDATA[Format teams_payload as a json object. See pre-processor script for format.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cgzb03\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"TextAnnotation_0ing8rr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nrnlka\" id=\"ServiceTask_0nrnlka_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tqeuuk\" id=\"SequenceFlow_1tqeuuk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1cx5ym9\" id=\"EndEvent_1cx5ym9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"457\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"475\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14r6yw4\" id=\"SequenceFlow_14r6yw4_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ing8rr\" id=\"TextAnnotation_0ing8rr_di\"\u003e\u003comgdc:Bounds height=\"82\" width=\"207\" x=\"130\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cgzb03\" id=\"Association_1cgzb03_di\"\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"139\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Example of posting incident data to a Microsoft Teams channel.",
      "export_key": "example_post_incident_to_ms_teams",
      "last_modified_by": "f32c43b9-be25-4e07-b8a1-fd1c75f57dbd",
      "last_modified_time": 1664795681554,
      "name": "Example: Post Incident to Microsoft Teams",
      "object_type": "incident",
      "programmatic_name": "example_post_incident_to_ms_teams",
      "tags": [
        {
          "tag_handle": "fn_teams",
          "value": null
        }
      ],
      "uuid": "d5b5842c-2715-4087-b434-ddd99e38c3f8",
      "workflow_id": 30
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "incident_create_a_teams_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_teams_group\" isExecutable=\"true\" name=\"Incident: Create a Teams Group\"\u003e\u003cdocumentation\u003eA sample workflow to create a Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_04ysv08\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1yr7w4e\" name=\"MS Teams: Create group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"120d2055-a0de-413b-b5d7-444d289dd469\"\u003e{\"inputs\":{},\"post_processing_script\":\"import json\\n\\ncontent = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(json.dumps(content))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_04ysv08\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1uefxxo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_04ysv08\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1yr7w4e\"/\u003e\u003cendEvent id=\"EndEvent_0ie5va2\"\u003e\u003cincoming\u003eSequenceFlow_1uefxxo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1uefxxo\" sourceRef=\"ServiceTask_1yr7w4e\" targetRef=\"EndEvent_0ie5va2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1yr7w4e\" id=\"ServiceTask_1yr7w4e_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"307\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04ysv08\" id=\"SequenceFlow_04ysv08_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"307\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ie5va2\" id=\"EndEvent_0ie5va2_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"561\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"579\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uefxxo\" id=\"SequenceFlow_1uefxxo_di\"\u003e\u003comgdi:waypoint x=\"407\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"561\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"484\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "A sample workflow to create a Group",
      "export_key": "incident_create_a_teams_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1664796299628,
      "name": "Incident: Create a Teams Group",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_teams_group",
      "tags": [],
      "uuid": "6fc91ac2-437c-488f-808b-b4c6c93fac6d",
      "workflow_id": 33
    }
  ],
  "workspaces": []
}
