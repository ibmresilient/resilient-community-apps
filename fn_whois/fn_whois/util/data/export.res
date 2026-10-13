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
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Run Whois Query Against Artifact",
      "id": 383,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Run Whois Query Against Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0da05211-c8c3-4c58-abbd-9927c45a9f06",
      "view_items": [],
      "workflows": [
        "example_whois_query_against_artifact"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1741882498172,
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
      "export_key": "__function/whois_query",
      "hide_notification": false,
      "id": 2757,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "whois_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "google.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "whois_query",
      "tooltip": "A URL or IP value which will be queried against a WHOIS server.",
      "type_id": 11,
      "uuid": "8584adf4-aba7-4149-84c4-af9e15f7bd0f",
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
      "created_date": 1741625869768,
      "description": {
        "content": "Used to send a query directly to a WHOIS server to gather information about an IP Or URL taken as an input.",
        "format": "text"
      },
      "destination_handle": "fn_whois",
      "display_name": "Whois: Query",
      "export_key": "whois_query",
      "id": 260,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1741625869768,
      "name": "whois_query",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "6e2e2cfb-e50a-4d48-85a9-eb80d965f55d",
      "version": 0,
      "view_items": [
        {
          "content": "8584adf4-aba7-4149-84c4-af9e15f7bd0f",
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
          "name": "Example: Whois Query Against Artifact",
          "object_type": "artifact",
          "programmatic_name": "example_whois_query_against_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 348
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 41,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1741882495881,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1741882495881,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "5369edd7-a0a7-444a-ab36-7d89e58b14eb"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_whois",
      "name": "Whois Message Destination",
      "programmatic_name": "fn_whois",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "4ef50702-6e05-4673-9aff-6531331176d2"
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
        "workflow_id": "example_whois_query_against_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_whois_query_against_artifact\" isExecutable=\"true\" name=\"Example: Whois Query Against Artifact\"\u003e\u003cdocumentation\u003eAn example workflow which is ran on an artifact. Takes in the artifacts value is an input and submits a WHOIS query against this input. Results are returned in the form of a note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1yo9j0o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08era5d\" name=\"Whois: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6e2e2cfb-e50a-4d48-85a9-eb80d965f55d\"\u003e{\"inputs\":{},\"post_processing_script\":\"def format_link(item):\\n  if item and (item.startswith(\\\"https://\\\") or item.startswith(\\\"http://\\\")):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        else:\\n          items.append(format_link(item))\\n      return separator.join(items)\\n    except:\\n        pass\\n    \\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n      \\n  return \\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n    \\n\\nnote = \\\"Whois for artifact: {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(artifact.value)\\nif results[\\\"success\\\"]:\\n  note = note + walk_dict(results[\\\"domain_details\\\"])\\nelse:\\n  note = note + \\\"This Artifact has no whois information\\\"\\n\\nincident.addNote(helper.createRichText(note))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.whois_query = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yo9j0o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1th83ja\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1yo9j0o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08era5d\"/\u003e\u003cendEvent id=\"EndEvent_1e9lyf4\"\u003e\u003cincoming\u003eSequenceFlow_1th83ja\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1th83ja\" sourceRef=\"ServiceTask_08era5d\" targetRef=\"EndEvent_1e9lyf4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_03c4p2w\"\u003e\u003ctext\u003eResults displayed in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1qje2yz\" sourceRef=\"ServiceTask_08era5d\" targetRef=\"TextAnnotation_03c4p2w\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08era5d\" id=\"ServiceTask_08era5d_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"294\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yo9j0o\" id=\"SequenceFlow_1yo9j0o_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"294\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"201\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1e9lyf4\" id=\"EndEvent_1e9lyf4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"484\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"457\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1th83ja\" id=\"SequenceFlow_1th83ja_di\"\u003e\u003comgdi:waypoint x=\"394\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"484\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"394\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_03c4p2w\" id=\"TextAnnotation_03c4p2w_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"156\" x=\"395\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1qje2yz\" id=\"Association_1qje2yz_di\"\u003e\u003comgdi:waypoint x=\"390\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"441\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example workflow which is ran on an artifact. Takes in the artifacts value is an input and submits a WHOIS query against this input. Results are returned in the form of a note.",
      "export_key": "example_whois_query_against_artifact",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1741626559168,
      "name": "Example: Whois Query Against Artifact",
      "object_type": "artifact",
      "programmatic_name": "example_whois_query_against_artifact",
      "tags": [],
      "uuid": "04484f6d-3a03-4992-a781-7eb9da038343",
      "workflow_id": 348
    }
  ],
  "workspaces": []
}
