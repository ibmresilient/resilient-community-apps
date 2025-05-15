{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "URL",
            "URL Referer"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: urlscan.io",
      "id": 501,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: urlscan.io",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "bbb9072a-263c-4316-8da3-da885c04f814",
      "view_items": [],
      "workflows": [
        "example_urlscanio"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1743688985333,
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
      "export_key": "__function/urlscanio_referer",
      "hide_notification": false,
      "id": 3458,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urlscanio_referer",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_referer",
      "tooltip": "Custom referer URL for this scan",
      "type_id": 11,
      "uuid": "a2ebdb5b-3d5a-425c-a0c7-fa35904fa5c4",
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
      "id": 2753,
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
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "the id of the incident",
      "type_id": 11,
      "uuid": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "export_key": "__function/urlscanio_public",
      "hide_notification": false,
      "id": 3457,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "urlscanio_public",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_public",
      "tooltip": "Should the scan be posted as public?",
      "type_id": 11,
      "uuid": "ee9263c1-432a-41a8-8bbd-6917d35fb3ac",
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
      "export_key": "__function/urlscanio_url",
      "hide_notification": false,
      "id": 3456,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urlscanio_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "62f95ee9-a112-4d1a-aa65-a6d0e1ef7348",
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
      "export_key": "__function/urlscanio_useragent",
      "hide_notification": false,
      "id": 3459,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urlscanio_useragent",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_useragent",
      "tooltip": "Override User-Agent for this scan",
      "type_id": 11,
      "uuid": "7381875c-7a32-439d-8f55-76239a4c72b7",
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
      "created_date": 1743688484750,
      "description": {
        "content": "Analyze a URL with urlscan.io",
        "format": "text"
      },
      "destination_handle": "urlscanio",
      "display_name": "Scan with urlscan.io",
      "export_key": "urlscanio",
      "id": 335,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743688484750,
      "name": "urlscanio",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d19c1f00-b4f1-4480-b8a3-7bdd19143041",
      "version": 0,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "62f95ee9-a112-4d1a-aa65-a6d0e1ef7348",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ee9263c1-432a-41a8-8bbd-6917d35fb3ac",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7381875c-7a32-439d-8f55-76239a4c72b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a2ebdb5b-3d5a-425c-a0c7-fa35904fa5c4",
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
          "name": "Example: urlscan.io",
          "object_type": "artifact",
          "programmatic_name": "example_urlscanio",
          "tags": [],
          "uuid": null,
          "workflow_id": 467
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 110,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1743688982928,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1743688982928,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3de34c0b-5d5a-4687-a124-dde71e1f8e98"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "urlscanio",
      "name": "urlscan.io",
      "programmatic_name": "urlscanio",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "9c4e0143-d84b-4fd2-be43-e52eeb1e1e08"
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
        "version": 2,
        "workflow_id": "example_urlscanio",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlscanio\" isExecutable=\"true\" name=\"Example: urlscan.io\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_17do46t\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0c3esun\" name=\"Scan with urlscan.io\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d19c1f00-b4f1-4480-b8a3-7bdd19143041\"\u003e{\"inputs\":{\"ee9263c1-432a-41a8-8bbd-6917d35fb3ac\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"# The result contains,\\n# {\\n#   \\\"png_url\\\": the URL of the screenshot image\\n#   \\\"png_base64content\\\": the base64-encoded screenshot (PNG)\\n#   \\\"report_url\\\": the URL of the JSON report_url\\n#   \\\"report\\\": the JSON report, which will contain lots of detail of the page analysis (see urlscan.io for details).\\n# }\\n#\\n# In this case, the file is already attached to the incident.  Nothing to do here.\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# This is an artifact workflow; \\n# The URL to scan is the artifact value\\ninputs.urlscanio_url = artifact.value\\n\\n# Set the incident id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"urlscanio\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_17do46t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dael78\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_17do46t\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0c3esun\"/\u003e\u003cendEvent id=\"EndEvent_08t8m44\"\u003e\u003cincoming\u003eSequenceFlow_1dael78\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1dael78\" sourceRef=\"ServiceTask_0c3esun\" targetRef=\"EndEvent_08t8m44\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eRun for a URL artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1i8h9sh\"\u003e\u003ctext\u003eScan the URL\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dkator\" sourceRef=\"ServiceTask_0c3esun\" targetRef=\"TextAnnotation_1i8h9sh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"100\" x=\"174\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"183\" y=\"189\"/\u003e\u003comgdi:waypoint x=\"215\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0c3esun\" id=\"ServiceTask_0c3esun_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"297\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17do46t\" id=\"SequenceFlow_17do46t_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"297\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"247.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08t8m44\" id=\"EndEvent_08t8m44_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"460\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1i8h9sh\" id=\"TextAnnotation_1i8h9sh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"348\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dkator\" id=\"Association_0dkator_di\"\u003e\u003comgdi:waypoint x=\"364\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"392\" y=\"99\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dael78\" id=\"SequenceFlow_1dael78_di\"\u003e\u003comgdi:waypoint x=\"397\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"460\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"428.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "",
      "export_key": "example_urlscanio",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743688554215,
      "name": "Example: urlscan.io",
      "object_type": "artifact",
      "programmatic_name": "example_urlscanio",
      "tags": [],
      "uuid": "21b841bb-f3f3-41b7-92a1-c44f027d14a1",
      "workflow_id": 467
    }
  ],
  "workspaces": []
}
