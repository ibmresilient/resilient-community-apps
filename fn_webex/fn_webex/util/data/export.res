{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1658230192776,
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
      "export_key": "__function/webex_meeting_end_time",
      "hide_notification": false,
      "id": 281,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_end_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
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
      "export_key": "__function/webex_meeting_password",
      "hide_notification": false,
      "id": 278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_password",
      "tooltip": "Meeting password",
      "type_id": 11,
      "uuid": "03dd1531-acbb-4db8-9950-53520eabbb5c",
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
      "export_key": "__function/webex_meeting_name",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_name",
      "tooltip": "Meeting name",
      "type_id": 11,
      "uuid": "14438dc7-4874-4971-9aa7-5596b13276a1",
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
      "export_key": "__function/webex_meeting_agenda",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_agenda",
      "tooltip": "Meeting agenda",
      "type_id": 11,
      "uuid": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
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
      "export_key": "__function/webex_meeting_start_time",
      "hide_notification": false,
      "id": 282,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_start_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5706ac62-97ee-4b54-9807-9f4b124ececc",
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
      "created_date": 1656947489905,
      "description": {
        "content": "Creates a WebEx meeting and returns the Host URL and Attendee URL.",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Create WebEx Meeting",
      "export_key": "fn_create_meeting",
      "id": 2,
      "last_modified_by": {
        "display_name": "MBP 16 (local)",
        "id": 9,
        "name": "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "type": "apikey"
      },
      "last_modified_time": 1657884351416,
      "name": "fn_create_meeting",
      "tags": [
        {
          "tag_handle": "fn_create_webex_meeting",
          "value": null
        }
      ],
      "uuid": "ab9bd63a-728e-4c80-aa36-27e288813c34",
      "version": 6,
      "view_items": [
        {
          "content": "14438dc7-4874-4971-9aa7-5596b13276a1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03dd1531-acbb-4db8-9950-53520eabbb5c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5706ac62-97ee-4b54-9807-9f4b124ececc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
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
          "name": "Example: Create WebEx Meeting: Incident",
          "object_type": "incident",
          "programmatic_name": "example_create_webex_meeting",
          "tags": [
            {
              "tag_handle": "fn_create_webex_meeting",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 3
        },
        {
          "actions": [],
          "description": null,
          "name": "WebEx Platform",
          "object_type": "incident",
          "programmatic_name": "webex_platform",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 3,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1658230190418,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1658230190418,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "e14b8f3e-6652-408c-8abf-448093f7f4ea",
        "ea00d563-3641-4d46-91dd-c7c4af20cc4d"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_webex",
      "name": "fn_webex",
      "programmatic_name": "fn_webex",
      "tags": [],
      "users": [],
      "uuid": "7fc77005-9552-4cbe-90c6-d9b6037c937c"
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
        "version": 14,
        "workflow_id": "webex_platform",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"webex_platform\" isExecutable=\"true\" name=\"WebEx Platform\"\u003e\u003cdocumentation\u003eA platform to create a meeting with team members\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1jvh0lg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cp3aej\" name=\"Create WebEx Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ab9bd63a-728e-4c80-aa36-27e288813c34\"\u003e{\"inputs\":{\"03dd1531-acbb-4db8-9950-53520eabbb5c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"abcd1234\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Cisco WebEx Meeting\\\"\\n\\n  fail_reason = content.get(\\\"fail_reason\\\")\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\nelse:\\n\\n  host_url = content.get(\\\"host_url\\\")\\n  attendee_url = content.get(\\\"attendee_url\\\")\\n\\n  if host_url is None:\\n    host_url = \\\"\\\"\\n\\n  if attendee_url is None:\\n    attendee_url = \\\"\\\"\\n    \\n  ref_html_host = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(host_url)\\n  ref_html_attendee = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(attendee_url)\\n\\n  text = u\\\"\u0026lt;b\u0026gt;Cisco WebEx Meeting Links:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;Host URL: {0}\u0026lt;br /\u0026gt;Attendee URL: {1}\\\".format(ref_html_host, ref_html_attendee)\\n  for key in content:\\n      text += u\\\"\u0026lt;br /\u0026gt;{} : {}\\\".format(key, content.get(key))\\n  \\nnote = helper.createRichText(text)\\nincident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_meeting_name = incident.name\\n\\ninputs.webex_meeting_start_time = inputs.webex_meeting_start_time if rule.properties.webex_meeting_start_time is None else rule.properties.webex_meeting_start_time\\ninputs.webex_meeting_end_time = inputs.webex_meeting_end_time if rule.properties.webex_meeting_end_time is None else rule.properties.webex_meeting_end_time\\n\\n# Get the agenda from the activity field or the incident description\\nif rule.properties.webex_meeting_agenda is None:\\n  if incident.description is not None and incident.description.content is not None:\\n    inputs.webex_meeting_agenda = incident.description.content\\n  else:\\n    inputs.webex_meeting_agenda = \\\"\\\"\\nelse:\\n  inputs.webex_meeting_agenda = rule.properties.webex_meeting_agenda\\n\\ninputs.webex_meeting_password = inputs.webex_meeting_password if rule.properties.webex_meeting_password is None else rule.properties.webex_meeting_password\\n  \",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1jvh0lg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_12scroy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_04gd8py\"\u003e\u003cincoming\u003eSequenceFlow_12scroy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1jvh0lg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cp3aej\"/\u003e\u003csequenceFlow id=\"SequenceFlow_12scroy\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"EndEvent_04gd8py\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_172tdgi\"\u003e\u003ctext\u003eInputs:\u00a0webex_meeting_name, webex_meeting_agenda, and webex_meeting_password\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0nvlnia\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"TextAnnotation_172tdgi\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01xqm6h\"\u003e\u003ctext\u003eOutputs: host_url and attendee_url written to incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1aeawdv\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"TextAnnotation_01xqm6h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_121irbg\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1kqsb5m\" sourceRef=\"EndEvent_04gd8py\" targetRef=\"TextAnnotation_121irbg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"175\" y=\"251\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"170\" y=\"286\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"65\" y=\"347\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"280\"/\u003e\u003comgdi:waypoint x=\"124\" xsi:type=\"omgdc:Point\" y=\"347\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cp3aej\" id=\"ServiceTask_0cp3aej_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"614\" y=\"229\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_172tdgi\" id=\"TextAnnotation_172tdgi_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"433\" x=\"44\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0nvlnia\" id=\"Association_0nvlnia_di\"\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"248\"/\u003e\u003comgdi:waypoint x=\"296\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01xqm6h\" id=\"TextAnnotation_01xqm6h_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"378\" x=\"854\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1aeawdv\" id=\"Association_1aeawdv_di\"\u003e\u003comgdi:waypoint x=\"714\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"1010\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04gd8py\" id=\"EndEvent_04gd8py_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1113.2577962577961\" y=\"251\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1131.2577962577961\" y=\"290\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_121irbg\" id=\"TextAnnotation_121irbg_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"1249\" y=\"347\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1kqsb5m\" id=\"Association_1kqsb5m_di\"\u003e\u003comgdi:waypoint x=\"1147\" xsi:type=\"omgdc:Point\" y=\"278\"/\u003e\u003comgdi:waypoint x=\"1272\" xsi:type=\"omgdc:Point\" y=\"347\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jvh0lg\" id=\"SequenceFlow_1jvh0lg_di\"\u003e\u003comgdi:waypoint x=\"211\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"412.5\" y=\"247\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12scroy\" id=\"SequenceFlow_12scroy_di\"\u003e\u003comgdi:waypoint x=\"714\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"1113\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"913.5\" y=\"247\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "description": "A platform to create a meeting with team members",
      "export_key": "webex_platform",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1657890700040,
      "name": "WebEx Platform",
      "object_type": "incident",
      "programmatic_name": "webex_platform",
      "tags": [],
      "uuid": "8c7a52f8-0dfc-4e8c-ba3e-d0207cb906c2",
      "workflow_id": 4
    }
  ],
  "workspaces": []
}
