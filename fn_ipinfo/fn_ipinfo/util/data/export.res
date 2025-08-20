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
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.value",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Query Artifact with IP Info",
      "id": 447,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Query Artifact with IP Info",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "eb1367ee-bffd-4127-957e-1a217c269232",
      "view_items": [],
      "workflows": [
        "example_query_ip_artifact_with_ipinfo"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1742995405413,
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
      "export_key": "__function/ipinfo_query_ip",
      "hide_notification": false,
      "id": 2998,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ipinfo_query_ip",
      "operation_perms": {},
      "operations": [],
      "placeholder": "8.8.8.8",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ipinfo_query_ip",
      "tooltip": "An IP address in either IPV4 of IPV6 format.",
      "type_id": 11,
      "uuid": "4fa8c581-24f4-4c23-a2bc-2192356a3dcf",
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
      "created_date": 1742990201336,
      "description": {
        "content": "Submits a query to IP Info for enrichment information on a given IP address.\nTakes in a String input representing an IP Address.",
        "format": "text"
      },
      "destination_handle": "fn_ipinfo",
      "display_name": "IpInfo: Query IP Address",
      "export_key": "fn_ipinfo_query_ip_address",
      "id": 305,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1742990201336,
      "name": "fn_ipinfo_query_ip_address",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "f12d5b1a-457c-439a-979a-08e741f5bfe9",
      "version": 0,
      "view_items": [
        {
          "content": "4fa8c581-24f4-4c23-a2bc-2192356a3dcf",
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
          "name": "Example: Query IP Artifact With IpInfo",
          "object_type": "artifact",
          "programmatic_name": "example_query_ip_artifact_with_ipinfo",
          "tags": [],
          "uuid": null,
          "workflow_id": 420
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 76,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1742995403150,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1742995403150,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "c929a480-8690-4197-8cab-50484dd83bfb"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_ipinfo",
      "name": "IpInfo Destination",
      "programmatic_name": "fn_ipinfo",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "b6ad3cd8-ec0d-4ddf-8f85-a0dcde4f6d89"
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
        "workflow_id": "example_query_ip_artifact_with_ipinfo",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_query_ip_artifact_with_ipinfo\" isExecutable=\"true\" name=\"Example: Query IP Artifact With IpInfo\"\u003e\u003cdocumentation\u003eAn example workflow which is intended to be ran on an artifact of type IP Address. Takes the IP input and submits a query to the IPInfo REST API in an attempt to return enrichment info for the IP address.\nResults are saved as a rich text note\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0hsksbl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1gjdozd\" name=\"IpInfo: Query IP Address\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f12d5b1a-457c-439a-979a-08e741f5bfe9\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\nExample output from IP Info \\n\\n{\\n\u0027success\u0027: True, \\n\u0027inputs\u0027: \\n    {\u0027ipinfo_query_ip\u0027: \u00278.8.8.8\u0027}, \\n\u0027query_result\u0027: \\n    {\u0027ip\u0027: \u00278.8.8.8\u0027, \\n    \u0027hostname\u0027: \\n    \u0027google-public-dns-a.google.com\u0027, \\n    \u0027city\u0027: \u0027Mountain View\u0027, \\n    \u0027region\u0027: \u0027California\u0027, \\n    \u0027country\u0027: \u0027US\u0027, \\n    \u0027loc\u0027: \u002737.3860,-122.0840\u0027, \\n    \u0027postal\u0027: \u002794035\u0027, \\n    \u0027phone\u0027: \u0027650\u0027, \\n    \u0027org\u0027: \u0027AS15169 Google LLC\u0027, \\n    \u0027country_name\u0027: \u0027United States\u0027, \\n    \u0027latitude\u0027: \u002737.3860\u0027, \\n    \u0027longitude\u0027: \u0027-122.0840\u0027}}\\n\\\"\\\"\\\"\\n\\nif results.query_result:\\n  noteText = \\\"\\\"\\\"IP Info Analysis ran against input \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; \u0026lt;br\u0026gt;\u0026lt;br\u0026gt; Hostname : \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0026lt;br\u0026gt; Country \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \u0026lt;br\u0026gt; GeoLocation :\u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.inputs[\\\"ipinfo_query_ip\\\"], results.query_result[\u0027hostname\u0027], results.query_result[\u0027country\u0027], results.query_result[\u0027loc\u0027])\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ipinfo_query_ip = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hsksbl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0eut4wi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_05atajz\"\u003e\u003cincoming\u003eSequenceFlow_0eut4wi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0eut4wi\" sourceRef=\"ServiceTask_1gjdozd\" targetRef=\"EndEvent_05atajz\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0hsksbl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gjdozd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1qdie0n\"\u003e\u003ctext\u003eTakes an IP Address artifacts value as its only input\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pk3eoq\" sourceRef=\"ServiceTask_1gjdozd\" targetRef=\"TextAnnotation_1qdie0n\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0krthct\"\u003e\u003ctext\u003eOutputs enrichment information for the given IP\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_05f3er1\" sourceRef=\"ServiceTask_1gjdozd\" targetRef=\"TextAnnotation_0krthct\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gjdozd\" id=\"ServiceTask_1gjdozd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"380\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05atajz\" id=\"EndEvent_05atajz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"671\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"689\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0eut4wi\" id=\"SequenceFlow_0eut4wi_di\"\u003e\u003comgdi:waypoint x=\"480\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"671\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"575.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hsksbl\" id=\"SequenceFlow_0hsksbl_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"380\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"289\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1qdie0n\" id=\"TextAnnotation_1qdie0n_di\"\u003e\u003comgdc:Bounds height=\"76\" width=\"156\" x=\"217\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pk3eoq\" id=\"Association_0pk3eoq_di\"\u003e\u003comgdi:waypoint x=\"383\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"349\" y=\"149\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0krthct\" id=\"TextAnnotation_0krthct_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"140\" x=\"523\" y=\"75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_05f3er1\" id=\"Association_05f3er1_di\"\u003e\u003comgdi:waypoint x=\"480\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"533\" y=\"146\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example workflow which is intended to be ran on an artifact of type IP Address. Takes the IP input and submits a query to the IPInfo REST API in an attempt to return enrichment info for the IP address.\nResults are saved as a rich text note",
      "export_key": "example_query_ip_artifact_with_ipinfo",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1742991342520,
      "name": "Example: Query IP Artifact With IpInfo",
      "object_type": "artifact",
      "programmatic_name": "example_query_ip_artifact_with_ipinfo",
      "tags": [],
      "uuid": "93d1c909-4fae-4f3e-9f99-ff058b97cea6",
      "workflow_id": 420
    }
  ],
  "workspaces": []
}
