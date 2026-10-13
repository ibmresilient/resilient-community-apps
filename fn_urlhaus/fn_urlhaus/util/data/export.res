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
      "id": 389,
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
      "id": 390,
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
  "export_date": 1741796092282,
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
      "id": 2783,
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
      "id": 2784,
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
      "created_date": 1741776991798,
      "description": {
        "content": "Perform a lookup on several artifacts of types",
        "format": "text"
      },
      "destination_handle": "fn_urlhaus",
      "display_name": "URLhaus Lookup",
      "export_key": "fn_urlhaus",
      "id": 265,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1741776991798,
      "name": "fn_urlhaus",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": \"ok\", \"content\": {\"query_status\": \"ok\", \"id\": \"3183014\", \"urlhaus_reference\": \"https://urlhaus.abuse.ch/url/3183014/\", \"url\": \"http://94.156.65.232/arm6.nn\", \"url_status\": \"online\", \"host\": \"94.156.65.232\", \"date_added\": \"2024-09-20 15:28:09 UTC\", \"last_online\": null, \"threat\": \"malware_download\", \"blacklists\": {\"spamhaus_dbl\": \"not listed\", \"surbl\": \"not listed\"}, \"reporter\": \"Try0\", \"larted\": \"true\", \"takedown_time_seconds\": null, \"tags\": [\"elf\", \"GorillaBotnet\", \"mirai\", \"ua-wget\"], \"payloads\": [{\"firstseen\": \"2024-09-20\", \"filename\": null, \"file_type\": \"elf\", \"response_size\": \"128210\", \"response_md5\": \"\", \"response_sha256\": \"\", \"urlhaus_download\": \"https://urlhaus-api.abuse.ch/v1/download/81c775f9540a66fded643fe4ec53dbbf35742bd3b069d95d689da313fc9b80a9/\", \"signature\": null, \"virustotal\": {\"result\": \"31 / 65\", \"percent\": \"47.69\", \"link\": \"https://www.virustotal.com/gui/file/81c775f9540a66fded643fe4ec53dbbf35742bd3b069d95d689da313fc9b80a9/detection/f-81c775f\"}, \"imphash\": null, \"ssdeep\": \"3072:Ymv6Z16i0qNNCXVak5C3fPzfDtudHm0WPZQk:9v6ZeECFa1jfMdHYPZT\", \"tlsh\": \"T10FC33A0269528A13C1C617B9BAAF415D3722AB78C3DB3315D9147FB42F827DE0E3B6\"}]}, \"raw\": \"\", \"inputs\": {\"urlhaus_artifact_type\": \"URL\", \"urlhaus_artifact_value\": \"http://94.156.65.232/arm6.nn\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-urlhaus\", \"package_version\": \"1.0.3\", \"host\": \"97472623-103e-44d1-a1da-c1d6296cbf8e-669f5f5bfc-sg65t\", \"execution_time_ms\": 599, \"timestamp\": \"2024-09-20 15:38:27\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {\"type\": \"string\"}, \"content\": {\"type\": \"object\", \"properties\": {\"query_status\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"urlhaus_reference\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}, \"url_status\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"date_added\": {\"type\": \"string\"}, \"last_online\": {}, \"threat\": {\"type\": \"string\"}, \"blacklists\": {\"type\": \"object\", \"properties\": {\"spamhaus_dbl\": {\"type\": \"string\"}, \"surbl\": {\"type\": \"string\"}}}, \"reporter\": {\"type\": \"string\"}, \"larted\": {\"type\": \"string\"}, \"takedown_time_seconds\": {}, \"tags\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"payloads\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"firstseen\": {\"type\": \"string\"}, \"filename\": {}, \"file_type\": {\"type\": \"string\"}, \"response_size\": {\"type\": \"string\"}, \"response_md5\": {\"type\": \"string\"}, \"response_sha256\": {\"type\": \"string\"}, \"urlhaus_download\": {\"type\": \"string\"}, \"signature\": {}, \"virustotal\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}, \"percent\": {\"type\": \"string\"}, \"link\": {\"type\": \"string\"}}}, \"imphash\": {}, \"ssdeep\": {\"type\": \"string\"}, \"tlsh\": {\"type\": \"string\"}}}}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"urlhaus_artifact_type\": {\"type\": \"string\"}, \"urlhaus_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 356
        }
      ]
    },
    {
      "created_date": 1741776991899,
      "description": {
        "content": "Submit a url to URLhaus as distributing malware",
        "format": "text"
      },
      "destination_handle": "fn_urlhaus",
      "display_name": "URLhaus Submission",
      "export_key": "fn_urlhaus_submission",
      "id": 266,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1741776991899,
      "name": "fn_urlhaus_submission",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": \"inserted: https://www.autohausmeister.eu\\n\", \"raw\": \"\", \"inputs\": {\"urlhaus_artifact_value\": \"https://www.autohausmeister.eu\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-urlhaus\", \"package_version\": \"1.0.3\", \"host\": \"97472623-103e-44d1-a1da-c1d6296cbf8e-669f5f5bfc-sg65t\", \"execution_time_ms\": 330, \"timestamp\": \"2024-09-20 15:53:23\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"string\"}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"urlhaus_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
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
          "workflow_id": 355
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 34,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1741796089765,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1741796089765,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "fff39ea7-42dd-4959-94c0-530a2c095b55"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_urlhaus",
      "name": "fn_urlhaus",
      "programmatic_name": "fn_urlhaus",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
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
        "workflow_id": "example_urlhaus_url_submission",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlhaus_url_submission\" isExecutable=\"true\" name=\"Example: URLhaus URL Submission\"\u003e\u003cdocumentation\u003eSubmit a URL to URLhaus has distributing malware. No other type of url will be accepted\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_141jz2y\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1f2y9aq\" name=\"URLhaus Submission\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a659028e-e39e-4da9-8505-75e0f7a14bfe\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addNote(\\\"Artifact {} submitted to URLhaus\\\\n{}\\\".format(artifact.value, results.content))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.urlhaus_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_141jz2y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0foda58\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_141jz2y\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1f2y9aq\"/\u003e\u003cendEvent id=\"EndEvent_1olyp4c\"\u003e\u003cincoming\u003eSequenceFlow_0foda58\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0foda58\" sourceRef=\"ServiceTask_1f2y9aq\" targetRef=\"EndEvent_1olyp4c\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1f2y9aq\" id=\"ServiceTask_1f2y9aq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"240\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_141jz2y\" id=\"SequenceFlow_141jz2y_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"240\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1olyp4c\" id=\"EndEvent_1olyp4c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"415\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0foda58\" id=\"SequenceFlow_0foda58_di\"\u003e\u003comgdi:waypoint x=\"340\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"415\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"377.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Submit a URL to URLhaus has distributing malware. No other type of url will be accepted",
      "export_key": "example_urlhaus_url_submission",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1741794057404,
      "name": "Example: URLhaus URL Submission",
      "object_type": "artifact",
      "programmatic_name": "example_urlhaus_url_submission",
      "tags": [],
      "uuid": "ecb47fb5-2308-41f0-ac10-25abbace23d5",
      "workflow_id": 355
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_urlhaus_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlhaus_lookup\" isExecutable=\"true\" name=\"Example: URLhaus Lookup\"\u003e\u003cdocumentation\u003ePerform an analysis on artifact types: IP Address, DNS Name, URL and Malware Hashes\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1toa5qk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ln9emm\" name=\"URLhaus Lookup\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1990b61b-109a-4b97-aabb-0103fd2e9b16\"\u003e{\"inputs\":{},\"post_processing_script\":\"def format_link(item):\\n  if item and (\\\"https://\\\" in item or \\\"http://\\\" in item):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        else:\\n          items.append(format_link(item))\\n      return separator.join(items)\\n    except:\\n        pass\\n\\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n  return \\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n\\nnote = \\\"\u0026lt;b\u0026gt;URLhaus look up for artifact:\u0026lt;/b\u0026gt; {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(artifact.value)\\n\\nif results[\\\"success\\\"]:\\n  note = note + walk_dict(results[\\\"content\\\"])\\nelse:\\n  note = note + \\\"This Artifact has no accessible registry information\\\"\\n  \\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.urlhaus_artifact_type = artifact.type\\ninputs.urlhaus_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1toa5qk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c423zs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1toa5qk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ln9emm\"/\u003e\u003cendEvent id=\"EndEvent_1jv1slg\"\u003e\u003cincoming\u003eSequenceFlow_0c423zs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c423zs\" sourceRef=\"ServiceTask_1ln9emm\" targetRef=\"EndEvent_1jv1slg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ln9emm\" id=\"ServiceTask_1ln9emm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"264\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1toa5qk\" id=\"SequenceFlow_1toa5qk_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"231\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jv1slg\" id=\"EndEvent_1jv1slg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"434.9552845528455\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.9552845528455\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c423zs\" id=\"SequenceFlow_0c423zs_di\"\u003e\u003comgdi:waypoint x=\"364\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Perform an analysis on artifact types: IP Address, DNS Name, URL and Malware Hashes",
      "export_key": "example_urlhaus_lookup",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1741793971166,
      "name": "Example: URLhaus Lookup",
      "object_type": "artifact",
      "programmatic_name": "example_urlhaus_lookup",
      "tags": [],
      "uuid": "51e6193b-d475-48f6-a44a-395195908066",
      "workflow_id": 356
    }
  ],
  "workspaces": []
}
