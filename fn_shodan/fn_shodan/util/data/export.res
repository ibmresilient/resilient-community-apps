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
        }
      ],
      "enabled": true,
      "export_key": "Example: Shodan Host Lookup",
      "id": 413,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Shodan Host Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "21a4b9fe-fe92-4426-b39d-9b904337843b",
      "view_items": [],
      "workflows": [
        "example_shodan_host_lookup"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1742466024579,
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
      "export_key": "__function/shodan_lookuphost",
      "hide_notification": false,
      "id": 2905,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shodan_lookuphost",
      "operation_perms": {},
      "operations": [],
      "placeholder": "127.0.0.1",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "shodan_lookuphost",
      "tooltip": "The IP Address to lookup in Shodan",
      "type_id": 11,
      "uuid": "7bd1534f-e5dc-4f05-9178-a5ea469abc5b",
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
      "created_date": 1742395302345,
      "description": {
        "content": "Function to look up an IP Address in Shodan",
        "format": "text"
      },
      "destination_handle": "fn_shodan",
      "display_name": "Shodan Lookup",
      "export_key": "shodan_lookup",
      "id": 283,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1742395302345,
      "name": "shodan_lookup",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "5935ed68-bdbe-4744-a9a7-045c789a7657",
      "version": 0,
      "view_items": [
        {
          "content": "7bd1534f-e5dc-4f05-9178-a5ea469abc5b",
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
          "name": "Example: Shodan Host Lookup",
          "object_type": "artifact",
          "programmatic_name": "example_shodan_host_lookup",
          "tags": [],
          "uuid": null,
          "workflow_id": 380
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 58,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1742466022763,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1742466022763,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "4957e83e-d50f-4a5f-9c7a-33d393078d55"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_shodan",
      "name": "fn_shodan",
      "programmatic_name": "fn_shodan",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "f0d841ab-2608-4794-afa3-399527282335"
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
        "version": 7,
        "workflow_id": "example_shodan_host_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_shodan_host_lookup\" isExecutable=\"true\" name=\"Example: Shodan Host Lookup\"\u003e\u003cdocumentation\u003eAn example workflow to look up an IP Address in Shodan. Updates the artifacts description and adds a note to the Incident\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1p1982o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ydqkto\"\u003e\u003cincoming\u003eSequenceFlow_0h7xcdr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1p1982o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1apcpx8\"/\u003e\u003cserviceTask id=\"ServiceTask_1apcpx8\" name=\"Shodan Lookup\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5935ed68-bdbe-4744-a9a7-045c789a7657\"\u003e{\"inputs\":{},\"post_processing_script\":\"def append_artifact_description(the_artifact, the_text):\\n  \\\"\\\"\\\"Appends the_text to the_artifact.description\\\"\\\"\\\"\\n  \\n  new_description = \\\"\\\"\\n  \\n  if the_artifact.description is None:\\n    current_description = None\\n  else:\\n    current_description = the_artifact.description.get(\\\"content\\\", None)\\n\\n  if current_description:\\n    new_description = \\\"{0}\u0026lt;br\u0026gt;---\u0026lt;br\u0026gt;{1}\\\".format(current_description, the_text)\\n\\n  else:\\n    new_description = \\\"{0}\\\".format(the_text)\\n\\n  the_artifact.description = helper.createRichText(new_description)\\n\\ncomment = \\\"\\\"\\\"\u0026lt;b\u0026gt;Shodan Host Lookup\u0026lt;/b\u0026gt; has complete\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Found:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color:{found_color}\\\"\u0026gt;{was_found}\u0026lt;/b\u0026gt;\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Artifact Type:\u0026lt;/b\u0026gt; {artifact_type}\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Artifact Value:\u0026lt;/b\u0026gt; {artifact_value}\\\"\\\"\\\"\\n\\nif results.success:\\n  results_content = results.get(\\\"content\\\", {})\\n  comment = comment.format(found_color=\\\"#ff402b\\\", was_found=\\\"Yes\\\", artifact_type=artifact.type, artifact_value=artifact.value)\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Organization:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(results_content.get(\\\"org\\\", \\\"Unknown\\\"))\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ISP:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(results_content.get(\\\"isp\\\", \\\"Unknown\\\"))\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Location:\u0026lt;/b\u0026gt; {0}, {1}\\\"\\\"\\\".format(results_content.get(\\\"city\\\", \\\"Unknown City\\\"), results_content.get(\\\"country_name\\\", \\\"Unknown Country\\\"))\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Vulnerabilities:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(results_content.get(\\\"vulns\\\", \\\"None Found\\\"))\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Ports:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(results_content.get(\\\"ports\\\", \\\"None Found\\\"))\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Link:\u0026lt;/b\u0026gt; \u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(results.get(\\\"shodan_url\\\", \\\"404\\\"))\\n\\nelse:\\n  comment = comment.format(found_color=\\\"#45bc27\\\", was_found=\\\"No\\\", artifact_type=artifact.get(type, artifact_value=artifact.value)\\n  comment += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {reason}\\\"\\\"\\\".format(reason=results.get(\\\"reason\\\", \\\"Not found in Shodan\\\"))\\n  \\nappend_artifact_description(artifact, comment)\\nincident.addNote(helper.createRichText(comment))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.shodan_lookuphost = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1p1982o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0h7xcdr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0h7xcdr\" sourceRef=\"ServiceTask_1apcpx8\" targetRef=\"EndEvent_0ydqkto\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"121\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"391\" y=\"156\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ydqkto\" id=\"EndEvent_0ydqkto_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"911\" y=\"121\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"929\" y=\"160\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1p1982o\" id=\"SequenceFlow_1p1982o_di\"\u003e\u003comgdi:waypoint x=\"432\" y=\"139\"/\u003e\u003comgdi:waypoint x=\"611\" y=\"139\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"521.5\" y=\"117.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1apcpx8\" id=\"ServiceTask_1apcpx8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"611\" y=\"99\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0h7xcdr\" id=\"SequenceFlow_0h7xcdr_di\"\u003e\u003comgdi:waypoint x=\"711\" y=\"139\"/\u003e\u003comgdi:waypoint x=\"911\" y=\"139\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"811\" y=\"117\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "description": "An example workflow to look up an IP Address in Shodan. Updates the artifacts description and adds a note to the Incident",
      "export_key": "example_shodan_host_lookup",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1742465503316,
      "name": "Example: Shodan Host Lookup",
      "object_type": "artifact",
      "programmatic_name": "example_shodan_host_lookup",
      "tags": [],
      "uuid": "cf752d8d-e9fe-44b1-a395-e77d530054d9",
      "workflow_id": 380
    }
  ],
  "workspaces": []
}
