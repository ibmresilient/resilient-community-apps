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
            "URL",
            "Malware MD5 Hash",
            "System Name",
            "String",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: URLhaus Lookup",
      "id": 316,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: URLhaus Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "28b270e9-e2de-4f72-9d2f-41ae02105af7",
      "view_items": [],
      "workflows": [
        "example_urlhaus_lookup"
      ]
    },
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
      "export_key": "Example: URLhaus URL Submission",
      "id": 317,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: URLhaus URL Submission",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e12cf059-a482-448f-aaad-09d09202d68c",
      "view_items": [],
      "workflows": [
        "example_urlhaus_url_submission"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1726848140848,
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
      "export_key": "__function/urlhaus_artifact_value",
      "hide_notification": false,
      "id": 2447,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urlhaus_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlhaus_artifact_value",
      "tooltip": "The value of the artifact",
      "type_id": 11,
      "uuid": "919c6ea0-4e09-4ce2-99b6-fd91d0ac9771",
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
      "export_key": "__function/urlhaus_artifact_type",
      "hide_notification": false,
      "id": 2448,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "urlhaus_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlhaus_artifact_type",
      "tooltip": "The artifact\u0027s type",
      "type_id": 11,
      "uuid": "ffa828c8-6daa-4754-8fbf-aa802df549d2",
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
      "created_date": 1726844870723,
      "description": {
        "content": "Perform a lookup on several artifacts of types",
        "format": "text"
      },
      "destination_handle": "fn_urlhaus",
      "display_name": "URLhaus Lookup",
      "export_key": "fn_urlhaus",
      "id": 226,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 7,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1726844870723,
      "name": "fn_urlhaus",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "1990b61b-109a-4b97-aabb-0103fd2e9b16",
      "version": 0,
      "view_items": [
        {
          "content": "ffa828c8-6daa-4754-8fbf-aa802df549d2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "919c6ea0-4e09-4ce2-99b6-fd91d0ac9771",
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
          "name": "Example: URLhaus Lookup",
          "object_type": "artifact",
          "programmatic_name": "example_urlhaus_lookup",
          "tags": [],
          "uuid": null,
          "workflow_id": 274
        }
      ]
    },
    {
      "created_date": 1726844871041,
      "description": {
        "content": "Submit a url to URLhaus as distributing malware",
        "format": "text"
      },
      "destination_handle": "fn_urlhaus",
      "display_name": "URLhaus Submission",
      "export_key": "fn_urlhaus_submission",
      "id": 227,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 7,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1726844871041,
      "name": "fn_urlhaus_submission",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "a659028e-e39e-4da9-8505-75e0f7a14bfe",
      "version": 0,
      "view_items": [
        {
          "content": "919c6ea0-4e09-4ce2-99b6-fd91d0ac9771",
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
          "name": "Example: URLhaus URL Submission",
          "object_type": "artifact",
          "programmatic_name": "example_urlhaus_url_submission",
          "tags": [],
          "uuid": null,
          "workflow_id": 273
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 80,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1726848138443,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1726848138443,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ba3f13dd-bdfa-40ed-9bcd-167c32649eac"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_urlhaus",
      "name": "fn_urlhaus",
      "programmatic_name": "fn_urlhaus",
      "tags": [],
      "users": [],
      "uuid": "62d8b030-2df8-452d-a9d2-bf32f67190c4"
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
    "build_number": 9340,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.9340"
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
        "workflow_id": "example_urlhaus_url_submission",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlhaus_url_submission\" isExecutable=\"true\" name=\"Example: URLhaus URL Submission\"\u003e\u003cdocumentation\u003eSubmit a URL to URLhaus has distributing malware. No other type of url will be accepted\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_141jz2y\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1f2y9aq\" name=\"URLhaus Submission\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a659028e-e39e-4da9-8505-75e0f7a14bfe\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addNote(u\\\"Artifact {} submitted to URLhaus\\\\n{}\\\".format(artifact.value, results.content))\",\"pre_processing_script\":\"inputs.urlhaus_artifact_value = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_141jz2y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0foda58\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_141jz2y\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1f2y9aq\"/\u003e\u003cendEvent id=\"EndEvent_1olyp4c\"\u003e\u003cincoming\u003eSequenceFlow_0foda58\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0foda58\" sourceRef=\"ServiceTask_1f2y9aq\" targetRef=\"EndEvent_1olyp4c\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1f2y9aq\" id=\"ServiceTask_1f2y9aq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"240\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_141jz2y\" id=\"SequenceFlow_141jz2y_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"240\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1olyp4c\" id=\"EndEvent_1olyp4c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"415\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0foda58\" id=\"SequenceFlow_0foda58_di\"\u003e\u003comgdi:waypoint x=\"340\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"415\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"377.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Submit a URL to URLhaus has distributing malware. No other type of url will be accepted",
      "export_key": "example_urlhaus_url_submission",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1726844872436,
      "name": "Example: URLhaus URL Submission",
      "object_type": "artifact",
      "programmatic_name": "example_urlhaus_url_submission",
      "tags": [],
      "uuid": "ecb47fb5-2308-41f0-ac10-25abbace23d5",
      "workflow_id": 273
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_urlhaus_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlhaus_lookup\" isExecutable=\"true\" name=\"Example: URLhaus Lookup\"\u003e\u003cdocumentation\u003ePerform an analysis on artifact types: IP Address, DNS Name, URL and Malware Hashes\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1toa5qk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ln9emm\" name=\"URLhaus Lookup\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1990b61b-109a-4b97-aabb-0103fd2e9b16\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\ndef format_link(item):\\n  if item and (\\\"https://\\\" in item or \\\"http://\\\" in item):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        else:\\n          items.append(format_link(item))\\n      return separator.join(items)\\n    except:\\n        pass\\n\\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(u\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(u\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n  return u\\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n\\nnote = u\\\"\u0026lt;b\u0026gt;URLhaus look up for artifact:\u0026lt;/b\u0026gt; {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(artifact.value)\\n\\nif results[\\\"success\\\"]:\\n  note = note + walk_dict(results[\\\"content\\\"])\\nelse:\\n  note = note + u\\\"This Artifact has no accessible registry information\\\"\\n  \\nincident.addNote(helper.createRichText(note))\",\"pre_processing_script\":\"inputs.urlhaus_artifact_type = artifact.type\\ninputs.urlhaus_artifact_value = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1toa5qk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c423zs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1toa5qk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ln9emm\"/\u003e\u003cendEvent id=\"EndEvent_1jv1slg\"\u003e\u003cincoming\u003eSequenceFlow_0c423zs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c423zs\" sourceRef=\"ServiceTask_1ln9emm\" targetRef=\"EndEvent_1jv1slg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ln9emm\" id=\"ServiceTask_1ln9emm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"264\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1toa5qk\" id=\"SequenceFlow_1toa5qk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"231\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jv1slg\" id=\"EndEvent_1jv1slg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"434.9552845528455\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.9552845528455\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c423zs\" id=\"SequenceFlow_0c423zs_di\"\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Perform an analysis on artifact types: IP Address, DNS Name, URL and Malware Hashes",
      "export_key": "example_urlhaus_lookup",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1726844872936,
      "name": "Example: URLhaus Lookup",
      "object_type": "artifact",
      "programmatic_name": "example_urlhaus_lookup",
      "tags": [],
      "uuid": "51e6193b-d475-48f6-a44a-395195908066",
      "workflow_id": 274
    }
  ],
  "workspaces": []
}
