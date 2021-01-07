{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: Phish.AI URL scan",
      "id": 84,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Phish.AI URL scan",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fe8ae39b-88e3-4dc2-9b15-c8fcc2194670",
      "view_items": [],
      "workflows": [
        "example_phishai_scan_url"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1610034445191,
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
      "export_key": "__function/artifact_value",
      "hide_notification": false,
      "id": 398,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b09e1899-7452-4f4f-bde1-23b2fbccd904",
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
      "export_key": "__function/phishai_scan_id",
      "hide_notification": false,
      "id": 409,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "phishai_scan_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "phishai_scan_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b6ac2adb-71f3-4d33-ab71-e6a36231926e",
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
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Returns report of a URL scan from Phish.AI.",
        "format": "text"
      },
      "destination_handle": "phish_ai_message_destination",
      "display_name": "Phish.AI Get Report",
      "export_key": "phish_ai_get_report",
      "id": 43,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1610034336846,
      "name": "phish_ai_get_report",
      "tags": [],
      "uuid": "01e4e115-333a-45a4-9e01-f470aac54d33",
      "version": 1,
      "view_items": [
        {
          "content": "b6ac2adb-71f3-4d33-ab71-e6a36231926e",
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
          "name": "Example: Phish.AI Scan URL",
          "object_type": "artifact",
          "programmatic_name": "example_phishai_scan_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 60
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Scans URL against Phish.AI.",
        "format": "text"
      },
      "destination_handle": "phish_ai_message_destination",
      "display_name": "Phish.AI Scan URL",
      "export_key": "phish_ai_scan_url",
      "id": 44,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1610034337025,
      "name": "phish_ai_scan_url",
      "tags": [],
      "uuid": "ed23b904-fd2e-4d73-b645-d5fa4fcb4ba0",
      "version": 1,
      "view_items": [
        {
          "content": "b09e1899-7452-4f4f-bde1-23b2fbccd904",
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
          "name": "Example: Phish.AI Scan URL",
          "object_type": "artifact",
          "programmatic_name": "example_phishai_scan_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 60
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 147,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1610034443589,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1610034443589,
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
      "export_key": "phish_ai_message_destination",
      "name": "Phish AI Message Destination",
      "programmatic_name": "phish_ai_message_destination",
      "tags": [],
      "users": [
        "a@a.com"
      ],
      "uuid": "4c7e10bd-5865-45e1-90bf-0b60ccd79563"
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
        "version": 1,
        "workflow_id": "example_phishai_scan_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_phishai_scan_url\" isExecutable=\"true\" name=\"Example: Phish.AI Scan URL\"\u003e\u003cdocumentation\u003eScans URL using Phish.AI and returns a report based on the results.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1k5w0tn\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03llsab\" name=\"Phish.AI Scan URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ed23b904-fd2e-4d73-b645-d5fa4fcb4ba0\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\nExample response\\n\\n{  \\n   \\\"content\\\":{  \\n      \\\"url\\\":\\\"https://startup417.gb.net/M3?mes1=asdf@asdf.com\\\",\\n      \\\"scan_id\\\":\\\"gGBSaVvlN5qc5PcwvnuT\\\"\\n   },\\n   \\\"inputs\\\":{  \\n      \\\"artifact_value\\\":\\\"https://startup417.gb.net/M3?mes1=asdf@asdf.com\\\"\\n   },\\n   \\\"run_time\\\":\\\"0.446181058884\\\"\\n}\\n\\\"\\\"\\\"\",\"pre_processing_script\":\"inputs.artifact_value = artifact.value\",\"result_name\":\"phishai_scan_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1k5w0tn\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hcmmas\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1k5w0tn\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03llsab\"/\u003e\u003cserviceTask id=\"ServiceTask_1229plo\" name=\"Phish.AI Get Report\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"01e4e115-333a-45a4-9e01-f470aac54d33\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.content:\\n  note = \\\"Phish.AI url: \\\" + results.content.url\\n  note = note + \\\"\u0026lt;br/\u0026gt;Phish.AI verdict: \\\" + results.content.verdict\\n  note = note + \\\"\u0026lt;br/\u0026gt;\u0026lt;a href=\\\\\\\"https://app.phish.ai/incident/{}\\\\\\\"\u0026gt;Phish.AI report link\u0026lt;/a\u0026gt;\\\".format(results.inputs.phishai_scan_id)\\n  incident.addNote(helper.createRichText(note))\\n\\n\\n\\\"\\\"\\\"\\nExample Response\\n\\n{  \\n   \\\"content\\\":{  \\n      \\\"status\\\":\\\"completed\\\",\\n      \\\"domain\\\":\\\"startup417.gb.net\\\",\\n      \\\"user_agent\\\":\\\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36\\\",\\n      \\\"target\\\":\\\"Microsoft\\\",\\n      \\\"title\\\":\\\"sign_in_to_your_microsoft_account\\\",\\n      \\\"url\\\":\\\"https://startup417.gb.net/M3?mes1=asdf@asdf.com\\\",\\n      \\\"time\\\":\\\"2018-12-06T22:39:34.210Z\\\",\\n      \\\"verdict\\\":\\\"malicious\\\",\\n      \\\"plan\\\":\\\"free\\\",\\n      \\\"tld\\\":\\\"net\\\",\\n      \\\"iso_code\\\":\\\"US\\\",\\n      \\\"first_seen\\\":\\\"2018-12-06T19:16:20.825Z\\\",\\n      \\\"ip_address\\\":\\\"104.24.104.116\\\",\\n      \\\"asn\\\":13335,\\n      \\\"user_email\\\":\\\"api\\\",\\n      \\\"user\\\":\\\"free-api\\\"\\n   },\\n   \\\"inputs\\\":{  \\n      \\\"phishai_scan_id\\\":\\\"gGBSaVvlN5qc5PcwvnuT\\\"\\n   },\\n   \\\"run_time\\\":\\\"0.419372797012\\\"\\n}\\n\\\"\\\"\\\"\",\"pre_processing_script\":\"inputs.phishai_scan_id = workflow.properties.phishai_scan_output[\\\"content\\\"][\\\"scan_id\\\"]\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hcmmas\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0x4ya9r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hcmmas\" sourceRef=\"ServiceTask_03llsab\" targetRef=\"ServiceTask_1229plo\"/\u003e\u003cendEvent id=\"EndEvent_0hrzcl0\"\u003e\u003cincoming\u003eSequenceFlow_0x4ya9r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0x4ya9r\" sourceRef=\"ServiceTask_1229plo\" targetRef=\"EndEvent_0hrzcl0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1imchu7\"\u003e\u003ctext\u003eInput URL\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1bbf1u7\" sourceRef=\"ServiceTask_03llsab\" targetRef=\"TextAnnotation_1imchu7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0dev0gu\"\u003e\u003ctext\u003eOutputs report from Phish.AI\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14xexoq\" sourceRef=\"ServiceTask_1229plo\" targetRef=\"TextAnnotation_0dev0gu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03llsab\" id=\"ServiceTask_03llsab_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"246\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k5w0tn\" id=\"SequenceFlow_1k5w0tn_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"246\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1229plo\" id=\"ServiceTask_1229plo_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"431.32515894641233\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hcmmas\" id=\"SequenceFlow_0hcmmas_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"388.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hrzcl0\" id=\"EndEvent_0hrzcl0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"605.3251589464123\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"623.3251589464123\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0x4ya9r\" id=\"SequenceFlow_0x4ya9r_di\"\u003e\u003comgdi:waypoint x=\"531\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"605\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"568\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1imchu7\" id=\"TextAnnotation_1imchu7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"130\" y=\"89.77839335180056\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1bbf1u7\" id=\"Association_1bbf1u7_di\"\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"197\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0dev0gu\" id=\"TextAnnotation_0dev0gu_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"573\" y=\"90\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14xexoq\" id=\"Association_14xexoq_di\"\u003e\u003comgdi:waypoint x=\"528\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"602\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@a.com",
      "description": "Scans URL using Phish.AI and returns a report based on the results.",
      "export_key": "example_phishai_scan_url",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1610034337695,
      "name": "Example: Phish.AI Scan URL",
      "object_type": "artifact",
      "programmatic_name": "example_phishai_scan_url",
      "tags": [],
      "uuid": "01311ca8-b9cc-4c14-b9bc-9ee114d474b4",
      "workflow_id": 60
    }
  ],
  "workspaces": []
}
