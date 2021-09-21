{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: HTML2PDF",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: HTML2PDF",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cdb49a34-0912-4c4a-bef3-0bf5cce34ae6",
      "view_items": [],
      "workflows": [
        "example_html2pdf"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1631563773751,
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
      "export_key": "__function/html2pdf_data",
      "hide_notification": false,
      "id": 228,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "html2pdf_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "html2pdf_data",
      "tooltip": "specify either a html string or url reference",
      "type_id": 11,
      "uuid": "9d0e2887-91bc-45ec-831f-b51996e01fa6",
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
      "export_key": "__function/html2pdf_data_type",
      "hide_notification": false,
      "id": 229,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "html2pdf_data_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "html2pdf_data_type",
      "tooltip": "the type of data passed, usually the artifact type. URL or URI are needed for webpage scaping",
      "type_id": 11,
      "uuid": "21ac2ac0-abc9-485a-a66e-5ab680415b40",
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
      "export_key": "__function/html2pdf_stylesheet",
      "hide_notification": false,
      "id": 230,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "html2pdf_stylesheet",
      "operation_perms": {},
      "operations": [],
      "placeholder": "@page { size: landscape; }* { font-family: Arial; font-size: small; }table { border-collapse: collapse; }table, th, td { border: 1px solid black; }",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "html2pdf_stylesheet",
      "tooltip": "css formatted stylesheet information to use when rendering PDF document",
      "type_id": 11,
      "uuid": "3b01d61f-cd93-47d7-ab4a-b32c2b8e1bfa",
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
      "apps": [],
      "created_date": 1631561531553,
      "creator": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "description": {
        "content": "Convert html text or a url reference to a base64 encoded pdf document.",
        "format": "text"
      },
      "destination_handle": "fn_html2pdf",
      "display_name": "HTML to PDF",
      "export_key": "fn_html2pdf",
      "id": 1,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1631561531635,
      "name": "fn_html2pdf",
      "tags": [],
      "uuid": "cabfaa1b-1e97-4f96-b034-753ad6da512c",
      "version": 1,
      "view_items": [
        {
          "content": "9d0e2887-91bc-45ec-831f-b51996e01fa6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b01d61f-cd93-47d7-ab4a-b32c2b8e1bfa",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "21ac2ac0-abc9-485a-a66e-5ab680415b40",
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
          "name": "Example: HTML2PDF",
          "object_type": "artifact",
          "programmatic_name": "example_html2pdf",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
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
      "create_date": 1631563771906,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1631563771906,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_html2pdf",
      "name": "fn_html2pdf",
      "programmatic_name": "fn_html2pdf",
      "tags": [],
      "users": [],
      "uuid": "90986388-823f-4e24-a110-b2dcff60279b"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6554,
    "major": 40,
    "minor": 0,
    "version": "40.0.6554"
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
        "workflow_id": "example_html2pdf",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_html2pdf\" isExecutable=\"true\" name=\"Example: HTML2PDF\"\u003e\u003cdocumentation\u003eConvert HTML coded string to base64 encoded PDF format\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0swz6ob\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08npund\" name=\"HTML to PDF\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"cabfaa1b-1e97-4f96-b034-753ad6da512c\"\u003e{\"inputs\":{\"9d0e2887-91bc-45ec-831f-b51996e01fa6\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\u0026lt;table\u0026gt;\u0026lt;tr\u0026gt;\u0026lt;td\u0026gt;a\u0026lt;/td\u0026gt;\u0026lt;td\u0026gt;b\u0026lt;/td\u0026gt;\u0026lt;/tr\u0026gt;\u0026lt;tr\u0026gt;\u0026lt;td\u0026gt;c\u0026lt;/td\u0026gt;\u0026lt;td\u0026gt;d\u0026lt;/td\u0026gt;\u0026lt;/tr\u0026gt;\u0026lt;/table\u0026gt;\"}},\"3b01d61f-cd93-47d7-ab4a-b32c2b8e1bfa\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"@page { size: landscape; }* { font-family: Arial; font-size: small; }table { border-collapse: collapse; }table, th, td { border: 1px solid black; }\"}},\"21ac2ac0-abc9-485a-a66e-5ab680415b40\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"string\"}}},\"post_processing_script\":\"# results in base64. see output property \u0027content\u0027:\\n# results.content\\n# or use workflow properties, such as \u0027pdf\u0027, when using this function with another function such as utilities: base64 to attachment:\\n# inputs.base64content = workflow.properties.pdf.content\",\"result_name\":\"pdf\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0swz6ob\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vpr79x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0swz6ob\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08npund\"/\u003e\u003cendEvent id=\"EndEvent_093wsxw\"\u003e\u003cincoming\u003eSequenceFlow_0vpr79x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vpr79x\" sourceRef=\"ServiceTask_08npund\" targetRef=\"EndEvent_093wsxw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1odmx2x\"\u003e\u003ctext\u003eResults in base64\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1g3h8m8\" sourceRef=\"ServiceTask_08npund\" targetRef=\"TextAnnotation_1odmx2x\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08npund\" id=\"ServiceTask_08npund_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0swz6ob\" id=\"SequenceFlow_0swz6ob_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_093wsxw\" id=\"EndEvent_093wsxw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"447\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"465\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vpr79x\" id=\"SequenceFlow_0vpr79x_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"402.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1odmx2x\" id=\"TextAnnotation_1odmx2x_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"133\" x=\"375\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1g3h8m8\" id=\"Association_1g3h8m8_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "Convert HTML coded string to base64 encoded PDF format",
      "export_key": "example_html2pdf",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1631561532559,
      "name": "Example: HTML2PDF",
      "object_type": "artifact",
      "programmatic_name": "example_html2pdf",
      "tags": [],
      "uuid": "b31e90f8-583c-45c0-a7c0-15d94b969b37",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
