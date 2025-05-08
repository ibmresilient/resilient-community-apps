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
      "export_key": "Example: PhishTank: Submit URL",
      "id": 109,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: PhishTank: Submit URL",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e845e515-03fd-46dc-8150-6851d19f468a",
      "view_items": [],
      "workflows": [
        "example_phishtank_submit_url"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1724056721943,
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
      "export_key": "__function/phish_tank_check_url",
      "hide_notification": false,
      "id": 534,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "phish_tank_check_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "http://www.example.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "phish_tank_check_url",
      "tooltip": "URL to lookup in PhishTank\u0027s Database",
      "type_id": 11,
      "uuid": "e3c9e446-935c-4d7d-9bc0-99add6932099",
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
      "created_date": 1724056715461,
      "description": {
        "content": "Searches the PhishTank database (https://www.phishtank.com/) to determine if a URL is a phishing URL or not. The information returned from PhishTank is used to update the Artifacts description and add a note to the incident.",
        "format": "text"
      },
      "destination_handle": "fn_phish_tank",
      "display_name": "Phish Tank Submit URL",
      "export_key": "fn_phish_tank_submit_url",
      "id": 70,
      "last_modified_by": {
        "display_name": "App Refresh API Key",
        "id": 4,
        "name": "c51c03f0-8386-4109-a41f-5edc05306428",
        "type": "apikey"
      },
      "last_modified_time": 1724056715563,
      "name": "fn_phish_tank_submit_url",
      "tags": [],
      "uuid": "5b9e6717-8c9d-4fd3-bef3-46fae089f1b1",
      "version": 1,
      "view_items": [
        {
          "content": "e3c9e446-935c-4d7d-9bc0-99add6932099",
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
          "name": "Example: PhishTank: Submit URL",
          "object_type": "artifact",
          "programmatic_name": "example_phishtank_submit_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 96
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 36,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1724056719526,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1724056719526,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "c51c03f0-8386-4109-a41f-5edc05306428"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_phish_tank",
      "name": "fn_phish_tank",
      "programmatic_name": "fn_phish_tank",
      "tags": [],
      "users": [],
      "uuid": "d9cb5962-e542-4723-8bf2-8fd7519fe398"
    }
  ],
  "notifications": null,
  "overrides": null,
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
        "version": 1,
        "workflow_id": "example_phishtank_submit_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_phishtank_submit_url\" isExecutable=\"true\" name=\"Example: PhishTank: Submit URL\"\u003e\u003cdocumentation\u003eSearches the PhishTank database (https://www.phishtank.com/) to determine if a URL is a phishing URL or not. The information returned from PhishTank is used to update the Artifacts description and add a note to the incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1min7o3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_15te4wj\" name=\"Phish Tank Submit URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5b9e6717-8c9d-4fd3-bef3-46fae089f1b1\"\u003e{\"inputs\":{},\"post_processing_script\":\"def append_artifact_description(the_artifact, the_text):\\n  \\\"\\\"\\\"Appends the_text to the_artifact.description safely\\n  handling unicode\\\"\\\"\\\"\\n  \\n  new_description = u\\\"\\\"\\n  \\n  if the_artifact.description is None:\\n    current_description = None\\n  else:\\n    current_description = the_artifact.description.get(\\\"content\\\", None)\\n\\n  if current_description is not None:\\n    new_description = u\\\"{0}\u0026lt;br\u0026gt;---\u0026lt;br\u0026gt;{1}\\\".format(unicode(current_description), unicode(the_text))\\n\\n  else:\\n    new_description = u\\\"{0}\\\".format(unicode(the_text))\\n\\n  the_artifact.description = helper.createRichText(new_description)\\n\\n\\nif results.success:\\n  \\n  # Get the PhishTank Results\\n  phish_tank_results = results.content.get(\\\"results\\\", {})\\n  url = phish_tank_results.get(\\\"url\\\", u\\\"\\\")\\n  in_database = phish_tank_results.get(\\\"in_database\\\", False)\\n  is_verified = phish_tank_results.get(\\\"verified\\\", False)\\n  is_valid = phish_tank_results.get(\\\"valid\\\", False)\\n  \\n  # Define the comment and msg to be appended to the Artifact\u0027s Description\\n  comment = u\\\"\\\"\\n  msg = u\\\"\\\"\\\"\u0026lt;b\u0026gt;PhishTank Lookup\u0026lt;/b\u0026gt; has complete\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;URL:\u0026lt;/b\u0026gt; {0}\u0026lt;/b\u0026gt;\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Found in Database:\u0026lt;/b\u0026gt; {1}\\\"\\\"\\\".format(url, unicode(in_database))\\n\\n  if not in_database:\\n    comment = u\\\"Nothing known about this url\\\"\\n  \\n  else:\\n    phish_id = phish_tank_results.get(\\\"phish_id\\\")\\n    phish_detail_page_url = phish_tank_results.get(\\\"phish_detail_page\\\")\\n    \\n    msg = u\\\"\\\"\\\"{0}\\n          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Phish ID:\u0026lt;/b\u0026gt; {1}\\n          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Valid Phish:\u0026lt;/b\u0026gt; {2}\\n          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Verified:\u0026lt;/b\u0026gt; {3}\\n          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Link to PhishTank: \u0026lt;a href={4}\u0026gt;{4}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(msg, phish_id, u\\\"Yes\\\" if is_valid else u\\\"No\\\", u\\\"Yes\\\" if is_verified else \\\"No\\\", phish_detail_page_url)\\n    \\n    if is_verified and is_valid:\\n      comment = u\\\"Verified: Is a phishing site\\\"\\n  \\n    elif is_verified and not is_valid:\\n      comment = u\\\"This site is not a phishing site\\\"\\n      \\n    elif not is_verified:\\n      comment = u\\\"This url has not been verified\\\"\\n  \\n  msg = u\\\"\\\"\\\"{0}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Comment:\u0026lt;/b\u0026gt; {1}\\\"\\\"\\\".format(msg, comment)\\n  \\n  append_artifact_description(artifact, msg)\\n  incident.addNote(helper.createRichText(msg))\",\"pre_processing_script\":\"# Get the url from the Artifact\u0027s Value\\ninputs.phish_tank_check_url = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1min7o3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wtz98i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1min7o3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_15te4wj\"/\u003e\u003cendEvent id=\"EndEvent_06xj5dl\"\u003e\u003cincoming\u003eSequenceFlow_0wtz98i\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wtz98i\" sourceRef=\"ServiceTask_15te4wj\" targetRef=\"EndEvent_06xj5dl\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"234\" y=\"89\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"229\" y=\"124\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_15te4wj\" id=\"ServiceTask_15te4wj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"403\" y=\"67\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1min7o3\" id=\"SequenceFlow_1min7o3_di\"\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"291.5\" y=\"85.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06xj5dl\" id=\"EndEvent_06xj5dl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"610\" y=\"89\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"583\" y=\"128\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wtz98i\" id=\"SequenceFlow_0wtz98i_di\"\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003comgdi:waypoint x=\"610\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"511.5\" y=\"85.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Searches the PhishTank database (https://www.phishtank.com/) to determine if a URL is a phishing URL or not. The information returned from PhishTank is used to update the Artifacts description and add a note to the incident.",
      "export_key": "example_phishtank_submit_url",
      "last_modified_by": "c51c03f0-8386-4109-a41f-5edc05306428",
      "last_modified_time": 1724056716377,
      "name": "Example: PhishTank: Submit URL",
      "object_type": "artifact",
      "programmatic_name": "example_phishtank_submit_url",
      "tags": [],
      "uuid": "310ed2fb-ddc1-4979-b62e-4c6435fc9bc5",
      "workflow_id": 96
    }
  ],
  "workspaces": []
}
