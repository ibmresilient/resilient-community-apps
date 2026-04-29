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
      "export_key": "Example: URL to DNS",
      "id": 445,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: URL to DNS",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ee7790cd-2d17-4829-a071-b089d2f12760",
      "view_items": [],
      "workflows": [
        "example_url_to_dns"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1742926039138,
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
      "export_key": "__function/urltodns_url",
      "hide_notification": false,
      "id": 2990,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urltodns_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urltodns_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f0fadbb7-aba9-4b25-bda9-71eee933e642",
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
      "created_date": 1742923141325,
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "url_to_dns",
      "display_name": "URL to DNS",
      "export_key": "url_to_dns",
      "id": 302,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1742923141325,
      "name": "url_to_dns",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "227c7fbe-5c55-4531-9a81-8b26a3593907",
      "version": 0,
      "view_items": [
        {
          "content": "f0fadbb7-aba9-4b25-bda9-71eee933e642",
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
          "name": "Example: URL to DNS",
          "object_type": "artifact",
          "programmatic_name": "example_url_to_dns",
          "tags": [],
          "uuid": null,
          "workflow_id": 418
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 74,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1742926036752,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1742926036752,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0cfdffd2-a058-4f3e-be88-24059a5b3a9e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "url_to_dns",
      "name": "url_to_dns",
      "programmatic_name": "url_to_dns",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "d01bf73a-ac7b-4a2f-a767-337756d28034"
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
        "workflow_id": "example_url_to_dns",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_url_to_dns\" isExecutable=\"true\" name=\"Example: URL to DNS\"\u003e\u003cdocumentation\u003eThis workflow takes a URL artifact value and passes it to the URL to DNS function which returns the DNS string.  An DNS artifact is created.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_06cdz56\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1t90rx5\" name=\"URL to DNS\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"227c7fbe-5c55-4531-9a81-8b26a3593907\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  content = results.get(\u0027content\u0027)\\n  dns_name = content.get(\u0027dns\u0027)\\n\\n  incident.addArtifact(\\\"DNS Name\\\", dns_name, \\\"Created from URL\\\")\\nelse:\\n  incident.addNote(\\\"URL to DNS function failed.\\\")\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.urltodns_url = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_06cdz56\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tuuiwo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_06cdz56\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1t90rx5\"/\u003e\u003cendEvent id=\"EndEvent_0dtmxaf\"\u003e\u003cincoming\u003eSequenceFlow_0tuuiwo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tuuiwo\" sourceRef=\"ServiceTask_1t90rx5\" targetRef=\"EndEvent_0dtmxaf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1434wz9\"\u003e\u003ctext\u003eOutput: DNS Artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pvxy8o\" sourceRef=\"ServiceTask_1t90rx5\" targetRef=\"TextAnnotation_1434wz9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kldp6o\"\u003e\u003ctext\u003eInput: URL artifact value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1mldj8h\" sourceRef=\"ServiceTask_1t90rx5\" targetRef=\"TextAnnotation_1kldp6o\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1t90rx5\" id=\"ServiceTask_1t90rx5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"323\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06cdz56\" id=\"SequenceFlow_06cdz56_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"323\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"260.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0dtmxaf\" id=\"EndEvent_0dtmxaf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"521\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"539\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tuuiwo\" id=\"SequenceFlow_0tuuiwo_di\"\u003e\u003comgdi:waypoint x=\"423\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"521\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"472\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1434wz9\" id=\"TextAnnotation_1434wz9_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"435\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pvxy8o\" id=\"Association_0pvxy8o_di\"\u003e\u003comgdi:waypoint x=\"413\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"470\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kldp6o\" id=\"TextAnnotation_1kldp6o_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"244\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1mldj8h\" id=\"Association_1mldj8h_di\"\u003e\u003comgdi:waypoint x=\"345\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"305\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "This workflow takes a URL artifact value and passes it to the URL to DNS function which returns the DNS string.  An DNS artifact is created.",
      "export_key": "example_url_to_dns",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1742923292302,
      "name": "Example: URL to DNS",
      "object_type": "artifact",
      "programmatic_name": "example_url_to_dns",
      "tags": [],
      "uuid": "7dc41429-1722-45cb-bca5-1be11d1a93f6",
      "workflow_id": 418
    }
  ],
  "workspaces": []
}
