{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Wiki Create Page",
      "id": 155,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Wiki Create Page",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e415937f-2bfc-4063-9189-ca7e72cbbe27",
      "view_items": [],
      "workflows": [
        "example_wiki_create_page"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Wiki Get Contents",
      "id": 156,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Wiki Get Contents",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "83559ce1-3816-4a95-849a-c9621a4c5284",
      "view_items": [],
      "workflows": [
        "example_wiki_get_contents"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Wiki Lookup",
      "id": 158,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Wiki Lookup",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e7745033-6fe4-4ad9-b49b-1c92651578c7",
      "view_items": [],
      "workflows": [
        "example_wiki_lookup"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1612812546517,
  "export_format_version": 2,
  "extensions": [],
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/wiki_create_if_missing",
      "hide_notification": false,
      "id": 1170,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "wiki_create_if_missing",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "wiki_create_if_missing",
      "tooltip": "",
      "type_id": 11,
      "uuid": "920634f7-7d23-440f-9074-1fc217c24cf5",
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
      "export_key": "__function/wiki_contents_as_json",
      "hide_notification": false,
      "id": 1172,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "wiki_contents_as_json",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "wiki_contents_as_json",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fae9af8d-bf1b-4e60-8e8d-187d228a8c0d",
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
      "export_key": "__function/wiki_path",
      "hide_notification": false,
      "id": 1468,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "wiki_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "parent/sub parent/target_wiki",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "wiki_path",
      "tooltip": "Use slash between wiki pages",
      "type_id": 11,
      "uuid": "92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517",
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
      "export_key": "__function/wiki_body",
      "hide_notification": false,
      "id": 1169,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "wiki_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "wiki_body",
      "tooltip": "",
      "type_id": 11,
      "uuid": "120e7089-5f1a-46cc-9c90-c2b02207aa78",
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
      "export_key": "__function/wiki_search_term",
      "hide_notification": false,
      "id": 1168,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "wiki_search_term",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "wiki_search_term",
      "tooltip": "text or regular expression format",
      "type_id": 11,
      "uuid": "91400a58-c674-465d-b129-9756cabd179a",
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
        "content": "Create or update a wiki page in Resilient based on the page\u0027s title or id.",
        "format": "text"
      },
      "destination_handle": "fn_wiki",
      "display_name": "Wiki Create or Update Page",
      "export_key": "fn_wiki_create_update",
      "id": 75,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1612295601867,
      "name": "fn_wiki_create_update",
      "tags": [],
      "uuid": "9e3610c7-878f-4851-bf6c-3ce7eabff05f",
      "version": 8,
      "view_items": [
        {
          "content": "92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "120e7089-5f1a-46cc-9c90-c2b02207aa78",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "920634f7-7d23-440f-9074-1fc217c24cf5",
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
          "name": "Example: Wiki Create Page",
          "object_type": "incident",
          "programmatic_name": "example_wiki_create_page",
          "tags": [],
          "uuid": null,
          "workflow_id": 96
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
        "content": "Return the contents of a wiki page based on the page\u0027s title or id. Optionally convert the results to JSON format (for string-encoded JSON data).",
        "format": "text"
      },
      "destination_handle": "fn_wiki",
      "display_name": "Wiki Get Contents",
      "export_key": "fn_wiki_get_contents",
      "id": 76,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1612295324327,
      "name": "fn_wiki_get_contents",
      "tags": [],
      "uuid": "1c530663-d245-4ed9-aa7b-c262b42dc623",
      "version": 13,
      "view_items": [
        {
          "content": "92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fae9af8d-bf1b-4e60-8e8d-187d228a8c0d",
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
          "name": "1test wiki",
          "object_type": "incident",
          "programmatic_name": "test_wiki",
          "tags": [],
          "uuid": null,
          "workflow_id": 155
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Wiki Get Contents",
          "object_type": "incident",
          "programmatic_name": "example_wiki_get_contents",
          "tags": [],
          "uuid": null,
          "workflow_id": 97
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
        "content": "Search a wiki page based on a search term and return the matching lines",
        "format": "text"
      },
      "destination_handle": "fn_wiki",
      "display_name": "Wiki Lookup",
      "export_key": "fn_wiki_lookup",
      "id": 74,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1612297050589,
      "name": "fn_wiki_lookup",
      "tags": [],
      "uuid": "662a77af-cb4c-409e-b578-5d73b64d9ca1",
      "version": 10,
      "view_items": [
        {
          "content": "92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "91400a58-c674-465d-b129-9756cabd179a",
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
          "name": "Example: Wiki Lookup",
          "object_type": "incident",
          "programmatic_name": "example_wiki_lookup",
          "tags": [],
          "uuid": null,
          "workflow_id": 98
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 99,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1612812544478,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1612812544478,
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
      "export_key": "fn_wiki",
      "name": "fn_wiki",
      "programmatic_name": "fn_wiki",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "7a13609d-b0ac-4ef1-b421-e7b809eebebf"
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
        "version": 37,
        "workflow_id": "example_wiki_get_contents",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_wiki_get_contents\" isExecutable=\"true\" name=\"Example: Wiki Get Contents\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get the contents of a wiki page by it\u0027s title or id. If contents are string-based JSON data, optionally return in JSON format.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_18jvqtv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1cnrubp\" name=\"Wiki Get Contents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1c530663-d245-4ed9-aa7b-c262b42dc623\"\u003e{\"inputs\":{\"92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"test page \u03a3\u03a4\"}},\"fae9af8d-bf1b-4e60-8e8d-187d228a8c0d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"note = u\\\"Page: \u0027{}\u0027\\\".format(results.title if results.get(\u0027title\u0027) else results.inputs[\u0027wiki_path\u0027])\\nif results.content:\\n    note = u\\\"{} contents:\\\\n\\\\n{}\\\".format(note, results.content[\u0027text\u0027])\\n    if results.content.get(\u0027json\u0027):\\n        note = u\\\"{} \\\\nJSON contents:\\\\n\\\\n{}\\\".format(note, results.content[\u0027json\u0027])\\nelse:\\n    note = u\\\"{} not found\\\".format(note)\\n    \\nincident.addNote(note)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_18jvqtv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1u7tqqc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_18jvqtv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1cnrubp\"/\u003e\u003cendEvent id=\"EndEvent_1kwjg57\"\u003e\u003cincoming\u003eSequenceFlow_1u7tqqc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1u7tqqc\" sourceRef=\"ServiceTask_1cnrubp\" targetRef=\"EndEvent_1kwjg57\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19dtn36\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pjr2au\" sourceRef=\"ServiceTask_1cnrubp\" targetRef=\"TextAnnotation_19dtn36\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cnrubp\" id=\"ServiceTask_1cnrubp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18jvqtv\" id=\"SequenceFlow_18jvqtv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1kwjg57\" id=\"EndEvent_1kwjg57_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"406\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"424\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1u7tqqc\" id=\"SequenceFlow_1u7tqqc_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"406\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"380\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19dtn36\" id=\"TextAnnotation_19dtn36_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"193\" x=\"357\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pjr2au\" id=\"Association_0pjr2au_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 37,
      "creator_id": "a@example.com",
      "description": "Get the contents of a wiki page by it\u0027s title or id. If contents are string-based JSON data, optionally return in JSON format.",
      "export_key": "example_wiki_get_contents",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1612296922457,
      "name": "Example: Wiki Get Contents",
      "object_type": "incident",
      "programmatic_name": "example_wiki_get_contents",
      "tags": [],
      "uuid": "2ea006d7-430e-419b-affb-53187e3a636b",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 26,
        "workflow_id": "example_wiki_create_page",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_wiki_create_page\" isExecutable=\"true\" name=\"Example: Wiki Create Page\"\u003e\u003cdocumentation\u003eCreate or update a wiki page. Specify the page by title or by id (for updates)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12dwp07\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1v0rbxl\" name=\"Wiki Create or Update Page\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9e3610c7-878f-4851-bf6c-3ce7eabff05f\"\u003e{\"inputs\":{\"92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"test page \u03a3\u03a4\"}},\"120e7089-5f1a-46cc-9c90-c2b02207aa78\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"test of fn_wiki_create_update\u03a3 \u03a4 \"}},\"920634f7-7d23-440f-9074-1fc217c24cf5\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"note = u\\\"Page: \u0027{}\u0027\\\".format(results.inputs.get(\u0027wiki_path\u0027))\\nif results.content:\\n    incident.addNote(u\\\"{} created/updated:\\\\n\\\\n{}\\\".format(note, results.content[\u0027text\u0027]))\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12dwp07\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0un0a7i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12dwp07\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1v0rbxl\"/\u003e\u003cendEvent id=\"EndEvent_0hgmx1z\"\u003e\u003cincoming\u003eSequenceFlow_0un0a7i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0un0a7i\" sourceRef=\"ServiceTask_1v0rbxl\" targetRef=\"EndEvent_0hgmx1z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1txgi2c\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0zseidh\" sourceRef=\"ServiceTask_1v0rbxl\" targetRef=\"TextAnnotation_1txgi2c\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1v0rbxl\" id=\"ServiceTask_1v0rbxl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"262\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12dwp07\" id=\"SequenceFlow_12dwp07_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"230\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hgmx1z\" id=\"EndEvent_0hgmx1z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"412\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"430\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0un0a7i\" id=\"SequenceFlow_0un0a7i_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"387\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1txgi2c\" id=\"TextAnnotation_1txgi2c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"189\" x=\"361\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0zseidh\" id=\"Association_0zseidh_di\"\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 26,
      "creator_id": "a@example.com",
      "description": "Create or update a wiki page. Specify the page by title or by id (for updates)",
      "export_key": "example_wiki_create_page",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1612811551365,
      "name": "Example: Wiki Create Page",
      "object_type": "incident",
      "programmatic_name": "example_wiki_create_page",
      "tags": [],
      "uuid": "5dbcf92a-7034-4305-a104-ee279539b42d",
      "workflow_id": 96
    },
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "example_wiki_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_wiki_lookup\" isExecutable=\"true\" name=\"Example: Wiki Lookup\"\u003e\u003cdocumentation\u003eSearch a wiki page and return the matching lines of data\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0uuhujl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1dx76fa\" name=\"Wiki Lookup\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"662a77af-cb4c-409e-b578-5d73b64d9ca1\"\u003e{\"inputs\":{\"92a9ee23-6b3b-48aa-b4a5-2a6ebf7a7517\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"test page \u03a3\u03a4\"}},\"91400a58-c674-465d-b129-9756cabd179a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\u03a3 \u03a4\"}}},\"post_processing_script\":\"note = u\\\"Page: \u0027{}\u0027 Search term: \u0027{}\u0027\\\".format(results.title if results.get(\u0027title\u0027) else results.inputs[\u0027wiki_path\u0027], results.inputs[\u0027wiki_search_term\u0027])\\nif results.content:\\n    incident.addNote(u\\\"{} Lookup result:\\\\n\\\\n{}\\\".format(note, \\\"\\\\n\\\".join(results.content)))\\nelse:\\n    incident.addNote(u\\\"{} lookup failure: {}\\\".format(note, results.reason))\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0uuhujl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17bp69h\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0uuhujl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1dx76fa\"/\u003e\u003cendEvent id=\"EndEvent_0iky01x\"\u003e\u003cincoming\u003eSequenceFlow_17bp69h\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17bp69h\" sourceRef=\"ServiceTask_1dx76fa\" targetRef=\"EndEvent_0iky01x\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0hunhah\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in an Incident note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1v19dw4\" sourceRef=\"ServiceTask_1dx76fa\" targetRef=\"TextAnnotation_0hunhah\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1dx76fa\" id=\"ServiceTask_1dx76fa_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uuhujl\" id=\"SequenceFlow_0uuhujl_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0iky01x\" id=\"EndEvent_0iky01x_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"439\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"457\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17bp69h\" id=\"SequenceFlow_17bp69h_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"439\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"406.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0hunhah\" id=\"TextAnnotation_0hunhah_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"167\" x=\"360\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1v19dw4\" id=\"Association_1v19dw4_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"113\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "a@example.com",
      "description": "Search a wiki page and return the matching lines of data",
      "export_key": "example_wiki_lookup",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1612811900526,
      "name": "Example: Wiki Lookup",
      "object_type": "incident",
      "programmatic_name": "example_wiki_lookup",
      "tags": [],
      "uuid": "640bfc4d-e436-4f00-ae67-04c39a924f74",
      "workflow_id": 98
    }
  ],
  "workspaces": []
}
