{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Watson Translate Note",
      "id": 170,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Watson Translate Note",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c7a1a9b8-65b0-4867-9cf9-ad08d79afa5d",
      "view_items": [],
      "workflows": [
        "watson_translate_note"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1629393812670,
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
      "export_key": "__function/fn_watson_translate_target_lang",
      "hide_notification": false,
      "id": 879,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watson_translate_target_lang",
      "operation_perms": {},
      "operations": [],
      "placeholder": "en",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watson_translate_target_lang",
      "tooltip": "Target language\u0027s 2 character ID",
      "type_id": 11,
      "uuid": "0f45d775-7415-4af4-93d7-b7a034762349",
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
      "export_key": "__function/fn_watson_translate_source_lang",
      "hide_notification": false,
      "id": 877,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watson_translate_source_lang",
      "operation_perms": {},
      "operations": [],
      "placeholder": "fr",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watson_translate_source_lang",
      "tooltip": "Source language\u0027s 2 character ID",
      "type_id": 11,
      "uuid": "0ffc433d-0acf-447c-bbee-29ab471b1e95",
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
      "export_key": "__function/fn_watson_translate_source_text",
      "hide_notification": false,
      "id": 878,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watson_translate_source_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "lorem impsum",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watson_translate_source_text",
      "tooltip": "Text to be translated",
      "type_id": 11,
      "uuid": "498b428f-fa65-481a-aaef-2151bb98392e",
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
        "content": "Translates input text to a target language from source language, or if it is not specified attempts to guess the original language.",
        "format": "text"
      },
      "destination_handle": "fn_watson_queue",
      "display_name": "Watson Translate",
      "export_key": "fn_watson_translate",
      "id": 127,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1629375287312,
      "name": "fn_watson_translate",
      "tags": [],
      "uuid": "a41aa5ef-b796-464d-9807-b0a2d208beaa",
      "version": 1,
      "view_items": [
        {
          "content": "0f45d775-7415-4af4-93d7-b7a034762349",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0ffc433d-0acf-447c-bbee-29ab471b1e95",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "498b428f-fa65-481a-aaef-2151bb98392e",
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
          "name": "Example: Watson Translate Note",
          "object_type": "note",
          "programmatic_name": "watson_translate_note",
          "tags": [],
          "uuid": null,
          "workflow_id": 156
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 104,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1629393812003,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1629393812003,
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
      "export_key": "fn_watson_queue",
      "name": "fn_watson_queue",
      "programmatic_name": "fn_watson_queue",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "c8fced14-93ff-45ef-9868-84a085f15af0"
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
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "watson_translate_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"watson_translate_note\" isExecutable=\"true\" name=\"Example: Watson Translate Note\"\u003e\u003cdocumentation\u003eThis workflow takes text of the note it was called on and translates it to the selected language and attaches the translated version as a comment to the note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1wl7cuf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19hvm2o\" name=\"Watson Translate\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a41aa5ef-b796-464d-9807-b0a2d208beaa\"\u003e{\"inputs\":{\"0f45d775-7415-4af4-93d7-b7a034762349\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"en\"}}},\"post_processing_script\":\"note.addNote(\\\"Translated by Watson: \\\\n\\\" + results.value)\",\"pre_processing_script\":\"inputs.fn_watson_translate_source_text = note.text.content\",\"result_name\":\"translated_text\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1wl7cuf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_023klzo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wl7cuf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19hvm2o\"/\u003e\u003cendEvent id=\"EndEvent_02a93u0\"\u003e\u003cincoming\u003eSequenceFlow_023klzo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_023klzo\" sourceRef=\"ServiceTask_19hvm2o\" targetRef=\"EndEvent_02a93u0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"186\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"181\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"190\" xsi:type=\"omgdc:Point\" y=\"217\"/\u003e\u003comgdi:waypoint x=\"159\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19hvm2o\" id=\"ServiceTask_19hvm2o_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"326\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wl7cuf\" id=\"SequenceFlow_1wl7cuf_di\"\u003e\u003comgdi:waypoint x=\"222\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"326\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"229\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02a93u0\" id=\"EndEvent_02a93u0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"479\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"452\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_023klzo\" id=\"SequenceFlow_023klzo_di\"\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"479\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"407.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "This workflow takes text of the note it was called on and translates it to the selected language and attaches the translated version as a comment to the note.",
      "export_key": "watson_translate_note",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1629375287773,
      "name": "Example: Watson Translate Note",
      "object_type": "note",
      "programmatic_name": "watson_translate_note",
      "tags": [],
      "uuid": "b6558796-7e42-4fdc-b18f-71aca3788b8a",
      "workflow_id": 156
    }
  ],
  "workspaces": []
}
