{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Create Pastebin",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Create Pastebin",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "aa3a5c17-41e0-496f-9da8-8d225aeae18e",
      "view_items": [],
      "workflows": [
        "example_create_pastebin"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1591932913166,
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
      "export_key": "__function/pastebin_code",
      "hide_notification": false,
      "id": 185,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pastebin_code",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pastebin_code",
      "tooltip": "This is the text that will be written inside your paste.",
      "type_id": 11,
      "uuid": "318c14fb-3edd-4d48-877c-fcd515d37a7a",
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
      "export_key": "__function/pastebin_privacy",
      "hide_notification": false,
      "id": 184,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "pastebin_privacy",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pastebin_privacy",
      "tooltip": "This makes a paste public, unlisted or private. (Public = 0. Unlisted = 1. Private = 2)",
      "type_id": 11,
      "uuid": "0c951c5a-101a-4393-8744-d4ed45eb684a",
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
      "export_key": "__function/pastebin_name",
      "hide_notification": false,
      "id": 182,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pastebin_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pastebin_name",
      "tooltip": "This will be the name / title of your paste.",
      "type_id": 11,
      "uuid": "aaa72035-a9d8-4fee-ae06-9edaf14fb857",
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
      "export_key": "__function/pastebin_expiration",
      "hide_notification": false,
      "id": 181,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pastebin_expiration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pastebin_expiration",
      "tooltip": "This sets the expiration date of your paste.",
      "type_id": 11,
      "uuid": "c48a9e72-94bc-4cce-b0dc-c77eefb1e8a9",
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
      "export_key": "__function/pastebin_format",
      "hide_notification": false,
      "id": 183,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pastebin_format",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pastebin_format",
      "tooltip": "This will be the syntax highlighting value",
      "type_id": 11,
      "uuid": "3e327c6d-aed6-402c-8ad8-837296978dd5",
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
        "id": 1,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Function that dumps any text/code to pastebin.com and returns a link to that paste",
        "format": "text"
      },
      "destination_handle": "fn_pastebin",
      "display_name": "Create Pastebin",
      "export_key": "fn_create_pastebin",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 1,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1591898142662,
      "name": "fn_create_pastebin",
      "tags": [],
      "uuid": "95bfe66e-d7e7-4038-a557-9f650a5bdd50",
      "version": 1,
      "view_items": [
        {
          "content": "318c14fb-3edd-4d48-877c-fcd515d37a7a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aaa72035-a9d8-4fee-ae06-9edaf14fb857",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3e327c6d-aed6-402c-8ad8-837296978dd5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c951c5a-101a-4393-8744-d4ed45eb684a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c48a9e72-94bc-4cce-b0dc-c77eefb1e8a9",
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
          "name": "Example: Create Pastebin",
          "object_type": "artifact",
          "programmatic_name": "example_create_pastebin",
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
      "create_date": 1611244916054,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1611244916054,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "4d896020-da4d-4fd6-a175-ed3bb3eb0647"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_pastebin",
      "name": "fn_pastebin",
      "programmatic_name": "fn_pastebin",
      "tags": [],
      "users": [
        "a@a.com"
      ],
      "uuid": "56fb3a28-26aa-4d7c-9dba-0622be5a7bce"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 0,
    "major": 35,
    "minor": 0,
    "version": "35.0.0"
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
        "workflow_id": "example_create_pastebin",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_create_pastebin\" isExecutable=\"true\" name=\"Example: Create Pastebin\"\u003e\u003cdocumentation\u003eAn Example Workflow that shows how to create a Pastebin\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1gdnkm8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1605dx0\" name=\"Create Pastebin\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"95bfe66e-d7e7-4038-a557-9f650a5bdd50\"\u003e{\"inputs\":{},\"post_processing_script\":\"if (results.success):\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Pastebin Created\u0026lt;/b\u0026gt;\\n                \u0026lt;b\u0026gt;Name:\u0026lt;/b\u0026gt; {0}\\n                \u0026lt;b\u0026gt;Link:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{1}\u0027\u0026gt;{1}\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(results.inputs.pastebin_name, results.pastebin_link)\\n  incident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"# This is the text that will be written inside your paste\\ninputs.pastebin_code = \\\"\\\"\\\" example code here \\\"\\\"\\\"\\n\\n# This will be the name / title of your paste\\ninputs.pastebin_name = \\\"Example Name\\\"\\n\\n# This will be the syntax highlighting value. Format codes, see here: https://pastebin.com/api\\ninputs.pastebin_format = \\\"python\\\"\\n\\n# This makes a paste public, unlisted or private. (Public = 0, Unlisted = 1, Private = 2)\\ninputs.pastebin_privacy = 2\\n\\n# This sets the expiration date of your paste. Expiration codes, see here: https://pastebin.com/api\\ninputs.pastebin_expiration = \\\"1H\\\"\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1gdnkm8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06ifogl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1gdnkm8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1605dx0\"/\u003e\u003cendEvent id=\"EndEvent_1beoa53\"\u003e\u003cincoming\u003eSequenceFlow_06ifogl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_06ifogl\" sourceRef=\"ServiceTask_1605dx0\" targetRef=\"EndEvent_1beoa53\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1605dx0\" id=\"ServiceTask_1605dx0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"317\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gdnkm8\" id=\"SequenceFlow_1gdnkm8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"317\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"257.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1beoa53\" id=\"EndEvent_1beoa53_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"559\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"577\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06ifogl\" id=\"SequenceFlow_06ifogl_di\"\u003e\u003comgdi:waypoint x=\"417\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"559\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"488\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@a.com",
      "description": "An Example Workflow that shows how to create a Pastebin",
      "export_key": "example_create_pastebin",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1591898143026,
      "name": "Example: Create Pastebin",
      "object_type": "artifact",
      "programmatic_name": "example_create_pastebin",
      "tags": [],
      "uuid": "a190d87e-78c0-49cc-a903-47f65c23e7df",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
