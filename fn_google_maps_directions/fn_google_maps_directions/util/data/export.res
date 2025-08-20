{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get Directions",
      "id": 670,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get Directions",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9ad14505-32eb-48df-9a96-3494a3b2dbc3",
      "view_items": [
        {
          "content": "67cd5479-0cb7-40de-b5ad-79312ef80a93",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a26404ca-0544-40ce-9770-77972c31723d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_google_maps_directions"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1745934830841,
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
      "export_key": "__function/google_maps_destination",
      "hide_notification": false,
      "id": 4277,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "google_maps_destination",
      "operation_perms": {},
      "operations": [],
      "placeholder": "IBM, Armonk, New York",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "google_maps_destination",
      "tooltip": "The end location",
      "type_id": 11,
      "uuid": "b9eca6ea-63fe-4991-a399-839e878c3201",
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
      "export_key": "__function/google_maps_origin",
      "hide_notification": false,
      "id": 4276,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "google_maps_origin",
      "operation_perms": {},
      "operations": [],
      "placeholder": "IBM, Armonk, New York",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "google_maps_origin",
      "tooltip": "The starting location",
      "type_id": 11,
      "uuid": "28709f80-4325-4668-ac64-f9a2c8e9a0f1",
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
      "export_key": "actioninvocation/destination",
      "hide_notification": false,
      "id": 4279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "destination",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Destination",
      "tooltip": "",
      "type_id": 6,
      "uuid": "a26404ca-0544-40ce-9770-77972c31723d",
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
      "export_key": "actioninvocation/source",
      "hide_notification": false,
      "id": 4278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "source",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Source",
      "tooltip": "",
      "type_id": 6,
      "uuid": "67cd5479-0cb7-40de-b5ad-79312ef80a93",
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
      "created_date": 1745834698526,
      "description": {
        "content": "A Function that takes an Origin and a Destination and returns a Google Maps Link with Directions",
        "format": "text"
      },
      "destination_handle": "fn_google_maps_directions",
      "display_name": "fn_google_maps_directions",
      "export_key": "fn_google_maps_directions",
      "id": 439,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1745834698526,
      "name": "fn_google_maps_directions",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d9c8c2a0-ac34-4f6f-a091-fbd1ff019bff",
      "version": 0,
      "view_items": [
        {
          "content": "28709f80-4325-4668-ac64-f9a2c8e9a0f1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9eca6ea-63fe-4991-a399-839e878c3201",
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
          "name": "Example: Google Maps Directions",
          "object_type": "incident",
          "programmatic_name": "example_google_maps_directions",
          "tags": [],
          "uuid": null,
          "workflow_id": 643
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 210,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1745934828011,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1745934828011,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "c90011ca-3006-4022-be56-6e50c6945d73"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_google_maps_directions",
      "name": "fn_google_maps_directions",
      "programmatic_name": "fn_google_maps_directions",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "0f1224bd-e4b7-4024-b1c7-e461d2a74fc3"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [],
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
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "example_google_maps_directions",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_google_maps_directions\" isExecutable=\"true\" name=\"Example: Google Maps Directions\"\u003e\u003cdocumentation\u003eAn Example workflow showing how to use the Google Maps Directions Function\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0qpaa2v\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_116le9p\" name=\"fn_google_maps_directions\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d9c8c2a0-ac34-4f6f-a091-fbd1ff019bff\"\u003e{\"inputs\":{},\"post_processing_script\":\"if (results.success):\\n  \\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Example: Google Maps Directions Workflow has complete\u0026lt;/b\u0026gt;\\n                \u0026lt;b\u0026gt;Directions Link:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(results.directions_link)\\n  \\n  incident.addNote(helper.createRichText(noteText))\\n\\nelse:\\n  incident.addNote(f\\\"google maps directions failure: {results.reason}\\\")\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Set Origin\\ninputs.google_maps_origin = rule.properties.source\\n\\n# Get destination from Incident Details\\n# destination = \\\"{0}, {1}, {2}\\\".format(incident.addr, incident.city, incident.country)\\n\\n# Set Destination\\ninputs.google_maps_destination = rule.properties.destination\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qpaa2v\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01q99e4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0tqwwyc\"\u003e\u003cincoming\u003eSequenceFlow_01q99e4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01q99e4\" sourceRef=\"ServiceTask_116le9p\" targetRef=\"EndEvent_0tqwwyc\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0qpaa2v\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_116le9p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_116le9p\" id=\"ServiceTask_116le9p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"307\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tqwwyc\" id=\"EndEvent_0tqwwyc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"529\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"547\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01q99e4\" id=\"SequenceFlow_01q99e4_di\"\u003e\u003comgdi:waypoint x=\"407\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"529\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"468\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qpaa2v\" id=\"SequenceFlow_0qpaa2v_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"307\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"252.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "An Example workflow showing how to use the Google Maps Directions Function",
      "export_key": "example_google_maps_directions",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1745934811008,
      "name": "Example: Google Maps Directions",
      "object_type": "incident",
      "programmatic_name": "example_google_maps_directions",
      "tags": [],
      "uuid": "1c686ce1-d5b8-4701-92d7-d4a7cab06ed3",
      "workflow_id": 643
    }
  ],
  "workspaces": []
}
