{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Create Zoom Meeting: Incident",
      "id": 62,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Create Zoom Meeting: Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b268f718-ce4d-4e7d-91eb-56eb245cde23",
      "view_items": [
        {
          "content": "Enter zoom meeting details",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c794ecfd-0277-42d8-8497-aa22312a78db",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dae12339-37dd-495b-966f-ed59c697f361",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8b7306bb-7c82-484d-9a2d-dee3696256d3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fa58ee1c-d87d-4e37-b0ce-aa7200a55d72",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_create_zoom_meeting_incident"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1635280604709,
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
      "export_key": "__function/zoom_record_meeting",
      "hide_notification": false,
      "id": 341,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_record_meeting",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "zoom_record_meeting",
      "tooltip": "Check this to record the meeting",
      "type_id": 11,
      "uuid": "a5a5d049-ab75-4986-a963-9bd2190f8e7e",
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
      "export_key": "__function/zoom_agenda",
      "hide_notification": false,
      "id": 337,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "zoom_agenda",
      "tooltip": "Agenda for this meeting",
      "type_id": 11,
      "uuid": "d1b91963-d07d-4463-a924-a959043a188f",
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
      "export_key": "__function/zoom_topic",
      "hide_notification": false,
      "id": 338,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_topic",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "zoom_topic",
      "tooltip": "Meeting topic",
      "type_id": 11,
      "uuid": "dc0da531-5a0e-4259-95d1-f15b1cecb470",
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
      "export_key": "__function/zoom_password",
      "hide_notification": false,
      "id": 339,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "zoom_password",
      "tooltip": "Meeting password",
      "type_id": 11,
      "uuid": "27d31a82-9c8b-4ebd-ad81-6874ba84efa0",
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
      "export_key": "actioninvocation/zoom_password",
      "hide_notification": false,
      "id": 345,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Zoom Password",
      "tooltip": "",
      "type_id": 6,
      "uuid": "8b7306bb-7c82-484d-9a2d-dee3696256d3",
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
      "export_key": "actioninvocation/zoom_topic",
      "hide_notification": false,
      "id": 343,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_topic",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Zoom Topic",
      "tooltip": "",
      "type_id": 6,
      "uuid": "c794ecfd-0277-42d8-8497-aa22312a78db",
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
      "export_key": "actioninvocation/zoom_agenda",
      "hide_notification": false,
      "id": 344,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Zoom Agenda",
      "tooltip": "",
      "type_id": 6,
      "uuid": "dae12339-37dd-495b-966f-ed59c697f361",
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
      "export_key": "actioninvocation/zoom_record_meeting",
      "hide_notification": false,
      "id": 346,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "zoom_record_meeting",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "templates": [],
      "text": "Record Meeting",
      "tooltip": "",
      "type_id": 6,
      "uuid": "fa58ee1c-d87d-4e37-b0ce-aa7200a55d72",
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
      "created_date": 1634237033057,
      "creator": {
        "display_name": "Chris\u0027 Integration Server v40",
        "id": 6,
        "name": "05c96997-7401-4089-a039-df21d0e54b07",
        "type": "apikey"
      },
      "description": {
        "content": "This will return a meeting URL to connect to a zoom meeting",
        "format": "text"
      },
      "destination_handle": "zoom",
      "display_name": "Create Zoom Meeting",
      "export_key": "fn_create_zoom_meeting",
      "id": 41,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1635280518255,
      "name": "fn_create_zoom_meeting",
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "uuid": "7badee36-5f2d-431a-b17c-d60fb677bbdb",
      "version": 4,
      "view_items": [
        {
          "content": "dc0da531-5a0e-4259-95d1-f15b1cecb470",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d1b91963-d07d-4463-a924-a959043a188f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27d31a82-9c8b-4ebd-ad81-6874ba84efa0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a5a5d049-ab75-4986-a963-9bd2190f8e7e",
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
          "name": "Example: Create Zoom Meeting: Incident",
          "object_type": "incident",
          "programmatic_name": "example_create_zoom_meeting_incident",
          "tags": [
            {
              "tag_handle": "fn_create_zoom_meeting",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 49
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 12,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1635280603433,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1635280603433,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "05c96997-7401-4089-a039-df21d0e54b07",
        "ac7e72bc-80f3-460c-826b-0c074ba234d3"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "zoom",
      "name": "zoom",
      "programmatic_name": "zoom",
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "users": [],
      "uuid": "1cd136c8-7933-44f3-9973-a50055347ee2"
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
        "version": 7,
        "workflow_id": "example_create_zoom_meeting_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_create_zoom_meeting_incident\" isExecutable=\"true\" name=\"Example: Create Zoom Meeting: Incident\"\u003e\u003cdocumentation\u003eAn example that creates a Zoom meeting based on incident properties.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lcxyhs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1kph3ld\" name=\"Create Zoom Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7badee36-5f2d-431a-b17c-d60fb677bbdb\"\u003e{\"inputs\":{\"a5a5d049-ab75-4986-a963-9bd2190f8e7e\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"# results:\\n# {\\n#   \\\"host_url\\\": \\\"https://zoom.us/s/x?zak=x\\\", \\n#   \\\"attendee_url\\\": \\\"https://zoom.us/j/x\\\", \\n#   \\\"date_created\\\": \\\"01/01/1971 12:00:00\\\"\\n# }\\nif results.host_url is not None and results.attendee_url is not None:\\n  host_url = results.host_url\\n  attendee_url = results.attendee_url\\n  \\n  if host_url is None:\\n    host_url = \\\"\\\"\\n  \\n  if attendee_url is None:\\n    attendee_url = \\\"\\\"\\n  \\ntext = \\\"\\\"\\\"\u0026lt;b\u0026gt;Zoom Meeting:\u0026lt;/b\u0026gt;\\n          \u0026lt;b\u0026gt;Host URL:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\n          \u0026lt;b\u0026gt;Attendee URL:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{1}\u0027\u0026gt;{1}\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(results.host_url, results.attendee_url)\\n\\nincident.addNote(helper.createRichText(text))\",\"pre_processing_script\":\"inputs.zoom_topic = rule.properties.zoom_topic\\n\\ninputs.zoom_password = inputs.zoom_password if rule.properties.zoom_password is None else rule.properties.zoom_password\\n\\nif rule.properties.zoom_agenda is not None:\\n  inputs.zoom_agenda = rule.properties.zoom_agenda\\nelse:\\n  if inputs.zoom_agenda is None and incident.description is not None and incident.description.content is not None:\\n    inputs.zoom_agenda = incident.description.content\\n\\ninputs.zoom_record_meeting = inputs.zoom_record_meeting if rule.properties.zoom_record_meeting is None else rule.properties.zoom_record_meeting\\n\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lcxyhs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1lcohow\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_149o5on\"\u003e\u003cincoming\u003eSequenceFlow_1lcohow\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1lcxyhs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kph3ld\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1lcohow\" sourceRef=\"ServiceTask_1kph3ld\" targetRef=\"EndEvent_149o5on\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18o8pzs\"\u003e\u003ctext\u003einputs: zoom_creator_id, zoom_topic, zoom_agenda, zoom_password, and zoom_record_meeting\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_071vqwd\" sourceRef=\"ServiceTask_1kph3ld\" targetRef=\"TextAnnotation_18o8pzs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1x80p9p\"\u003e\u003ctext\u003eoutputs: host_url and attendee_url\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02j1jqy\" sourceRef=\"ServiceTask_1kph3ld\" targetRef=\"TextAnnotation_1x80p9p\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"313\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"308\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"178\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"315\" xsi:type=\"omgdc:Point\" y=\"213\"/\u003e\u003comgdi:waypoint x=\"248\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kph3ld\" id=\"ServiceTask_1kph3ld_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"503\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_149o5on\" id=\"EndEvent_149o5on_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"726\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"699\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lcxyhs\" id=\"SequenceFlow_1lcxyhs_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"381\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lcohow\" id=\"SequenceFlow_1lcohow_di\"\u003e\u003comgdi:waypoint x=\"603\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"665\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"665\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"726\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"635\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18o8pzs\" id=\"TextAnnotation_18o8pzs_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"336\" x=\"182\" y=\"120\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_071vqwd\" id=\"Association_071vqwd_di\"\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"189\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"152\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1x80p9p\" id=\"TextAnnotation_1x80p9p_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"250\" x=\"669\" y=\"121\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02j1jqy\" id=\"Association_02j1jqy_di\"\u003e\u003comgdi:waypoint x=\"603\" xsi:type=\"omgdc:Point\" y=\"191\"/\u003e\u003comgdi:waypoint x=\"744\" xsi:type=\"omgdc:Point\" y=\"151\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "05c96997-7401-4089-a039-df21d0e54b07",
      "description": "An example that creates a Zoom meeting based on incident properties.",
      "export_key": "example_create_zoom_meeting_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1635280536705,
      "name": "Example: Create Zoom Meeting: Incident",
      "object_type": "incident",
      "programmatic_name": "example_create_zoom_meeting_incident",
      "tags": [
        {
          "tag_handle": "fn_create_zoom_meeting",
          "value": null
        }
      ],
      "uuid": "873bb550-0f2d-4d18-9e3e-9dc4f3a69bf0",
      "workflow_id": 49
    }
  ],
  "workspaces": []
}
