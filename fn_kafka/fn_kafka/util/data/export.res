{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Kafka Send",
      "id": 88,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Kafka Send",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "222ce89f-5532-47ad-b8c1-00fccc659e58",
      "view_items": [
        {
          "content": "53e772f4-0cd0-403f-a0df-b25941ab529a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9fd31a50-f0a7-47b6-8c27-3274e211da01",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a5fbf032-a1bf-4523-a4e2-069109b1b260",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64bca175-952c-41a6-91ee-21214323230e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_kafka_send"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1619621896596,
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
      "export_key": "__function/kafka_topic",
      "hide_notification": false,
      "id": 335,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_topic",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "kafka_topic",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8b5cb7e3-a801-42f5-8253-6cb2f557e536",
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
      "export_key": "__function/kafka_key",
      "hide_notification": false,
      "id": 336,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "kafka_key",
      "tooltip": "optional key/value data sending",
      "type_id": 11,
      "uuid": "b0911574-5221-405d-bf6e-f14d8b8477b0",
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
      "export_key": "__function/kafka_message",
      "hide_notification": false,
      "id": 337,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_message",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "kafka_message",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b41dae3b-b0e7-41ef-a097-ac12db1832c5",
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
      "export_key": "__function/kafka_broker_label",
      "hide_notification": false,
      "id": 338,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_broker_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "kafka_broker_label",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fa964900-3f10-493d-bde0-4105c73cd31a",
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
      "export_key": "actioninvocation/kafka_topic",
      "hide_notification": false,
      "id": 331,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_topic",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "Topic",
      "tooltip": "Kafka topic overrides topics defined in Broker settings",
      "type_id": 6,
      "uuid": "9fd31a50-f0a7-47b6-8c27-3274e211da01",
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
      "export_key": "actioninvocation/kafka_key",
      "hide_notification": false,
      "id": 332,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "Key",
      "tooltip": "optional use of key/value messages",
      "type_id": 6,
      "uuid": "a5fbf032-a1bf-4523-a4e2-069109b1b260",
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
      "export_key": "actioninvocation/kafka_broker_label",
      "hide_notification": false,
      "id": 333,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_broker_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "Broker Label",
      "tooltip": "Broker label defined in app.config",
      "type_id": 6,
      "uuid": "53e772f4-0cd0-403f-a0df-b25941ab529a",
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
      "export_key": "actioninvocation/kafka_message",
      "hide_notification": false,
      "id": 334,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "kafka_message",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "templates": [],
      "text": "Message",
      "tooltip": "Message to send, can be in json format",
      "type_id": 6,
      "uuid": "64bca175-952c-41a6-91ee-21214323230e",
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
        "content": "Send messages through Kafka based on a named topic",
        "format": "text"
      },
      "destination_handle": "fn_kafka",
      "display_name": "Kafka Send",
      "export_key": "kafka_send",
      "id": 58,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1619618685910,
      "name": "kafka_send",
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "uuid": "6974cf84-6b1c-4f77-985c-17ea824d9ac3",
      "version": 1,
      "view_items": [
        {
          "content": "fa964900-3f10-493d-bde0-4105c73cd31a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8b5cb7e3-a801-42f5-8253-6cb2f557e536",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b0911574-5221-405d-bf6e-f14d8b8477b0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b41dae3b-b0e7-41ef-a097-ac12db1832c5",
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
          "name": "Example: Kafka Send",
          "object_type": "incident",
          "programmatic_name": "example_kafka_send",
          "tags": [
            {
              "tag_handle": "fn_kafka",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 68
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 1,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1619621894456,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1619621894456,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "20322ad9-8fd0-45f1-9ca3-a6d8b2d869e4"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_kafka",
      "name": "fn_kafka",
      "programmatic_name": "fn_kafka",
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "users": [],
      "uuid": "babcbb7b-03fb-4ee4-93dc-0c845e47bc5c"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6006,
    "major": 38,
    "minor": 0,
    "version": "38.0.6006"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_kafka_send",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_kafka_send\" isExecutable=\"true\" name=\"Example: Kafka Send\"\u003e\u003cdocumentation\u003eSend a message to a Kafka topic with an optional key\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0haggmv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1sjw8a6\" name=\"Kafka Send\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6974cf84-6b1c-4f77-985c-17ea824d9ac3\"\u003e{\"inputs\":{},\"post_processing_script\":\"msg = u\\\"Kafka Send Status: {}\\\\nBroker: {} Topic: {} Key: {}\\\".format(\\\"success\\\" if results.success else \\\"failure\\\", results.inputs[\u0027kafka_broker_label\u0027], results.inputs[\u0027kafka_topic\u0027], results.inputs[\u0027kafka_key\u0027])\\nincident.addNote(helper.createPlainText(msg))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.kafka_topic = rule.properties.kafka_topic\\ninputs.kafka_message = rule.properties.kafka_message.content\\ninputs.kafka_broker_label = rule.properties.kafka_broker_label\\ninputs.kafka_key = rule.properties.kafka_key\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0haggmv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o0oang\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0haggmv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1sjw8a6\"/\u003e\u003cendEvent id=\"EndEvent_1tuxcwo\"\u003e\u003cincoming\u003eSequenceFlow_0o0oang\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0o0oang\" sourceRef=\"ServiceTask_1sjw8a6\" targetRef=\"EndEvent_1tuxcwo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07mgwxd\"\u003e\u003ctext\u003eSend results returned in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0tzq8sf\" sourceRef=\"ServiceTask_1sjw8a6\" targetRef=\"TextAnnotation_07mgwxd\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sjw8a6\" id=\"ServiceTask_1sjw8a6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0haggmv\" id=\"SequenceFlow_0haggmv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tuxcwo\" id=\"EndEvent_1tuxcwo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o0oang\" id=\"SequenceFlow_0o0oang_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"392\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07mgwxd\" id=\"TextAnnotation_07mgwxd_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"187\" x=\"346\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0tzq8sf\" id=\"Association_0tzq8sf_di\"\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"413\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@example.com",
      "description": "Send a message to a Kafka topic with an optional key",
      "export_key": "example_kafka_send",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1619621808275,
      "name": "Example: Kafka Send",
      "object_type": "incident",
      "programmatic_name": "example_kafka_send",
      "tags": [
        {
          "tag_handle": "fn_kafka",
          "value": null
        }
      ],
      "uuid": "dc46b7b4-003a-4735-9166-d5b760295171",
      "workflow_id": 68
    }
  ],
  "workspaces": []
}
