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
            "URI Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "GoogleSafeBrowsing URL Lookup",
      "id": 17,
      "logic_type": "all",
      "message_destinations": [],
      "name": "GoogleSafeBrowsing URL Lookup",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "925dfa0d-05de-4a81-b089-a879fce5a693",
      "view_items": [],
      "workflows": [
        "google_safe_browsing_url_lookup"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647463510676,
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
      "export_key": "__function/googlesafebrowsing_artifact_value",
      "hide_notification": false,
      "id": 277,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "googlesafebrowsing_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "templates": [],
      "text": "googlesafebrowsing_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f05434e4-2e9e-4d4d-8bd5-247ef2d1f10b",
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
      "export_key": "__function/googlesafebrowsing_artifact_type",
      "hide_notification": false,
      "id": 278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "googlesafebrowsing_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "templates": [],
      "text": "googlesafebrowsing_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fd5a7efc-6f3d-48e9-9031-39dd26106ec6",
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
      "created_date": 1645555031068,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "This app uses Google Safe Browsing to check artifacts with a URL type and adds a hit if the site is potentially unsafe. The hit contains a link to Google Transparency Report that gives information on the potentially unsafe url.",
        "format": "text"
      },
      "destination_handle": "googlesafebrowsing",
      "display_name": "Google Safe Browsing",
      "export_key": "fn_googlesafebrowsing",
      "id": 5,
      "last_modified_by": {
        "display_name": "Chris\u0027 Integration Server v43",
        "id": 6,
        "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
        "type": "apikey"
      },
      "last_modified_time": 1645643013109,
      "name": "fn_googlesafebrowsing",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"matches\": [{\"threatType\": \"MALWARE\", \"platformType\": \"ANY_PLATFORM\", \"threat\": {\"url\": \"http://malware.testing.google.test/testing/malware/*\"}, \"cacheDuration\": \"300s\", \"threatEntryType\": \"URL\"}]}, \"raw\": null, \"inputs\": {\"googlesafebrowsing_artifact_value\": \"http://malware.testing.google.test/testing/malware/*\", \"googlesafebrowsing_artifact_type\": \"URL\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-googlesafebrowsing\", \"package_version\": \"1.0.0\", \"host\": \"My Host\", \"execution_time_ms\": 411, \"timestamp\": \"2022-02-17 14:05:42\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"matches\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"threatType\": {\"type\": \"string\"}, \"platformType\": {\"type\": \"string\"}, \"threat\": {\"type\": \"object\", \"properties\": {\"url\": {\"type\": \"string\"}}}, \"cacheDuration\": {\"type\": \"string\"}, \"threatEntryType\": {\"type\": \"string\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"googlesafebrowsing_artifact_value\": {\"type\": \"string\"}, \"googlesafebrowsing_artifact_type\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "uuid": "abef1962-356f-4961-9a46-5f98d96b645a",
      "version": 2,
      "view_items": [
        {
          "content": "f05434e4-2e9e-4d4d-8bd5-247ef2d1f10b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fd5a7efc-6f3d-48e9-9031-39dd26106ec6",
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
          "name": "Google Safe Browsing URL Lookup",
          "object_type": "artifact",
          "programmatic_name": "google_safe_browsing_url_lookup",
          "tags": [
            {
              "tag_handle": "fn_googlesafebrowsing",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 59,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647463508878,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647463508878,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea",
        "ce235132-4a44-4166-b797-3e26b91fe9bb"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "googlesafebrowsing",
      "name": "GoogleSafeBrowsing",
      "programmatic_name": "googlesafebrowsing",
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "users": [],
      "uuid": "013b222a-68cc-4428-b013-37152b30ca20"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 25,
        "workflow_id": "google_safe_browsing_url_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"google_safe_browsing_url_lookup\" isExecutable=\"true\" name=\"Google Safe Browsing URL Lookup\"\u003e\u003cdocumentation\u003eThis app uses Google Safe Browsing to check artifacts with a URL type and adds a hit if the site is potentially unsafe. The hit contains a link to Google Transparency Report that gives information on the potentially unsafe url.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10jh7md\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0x0wioq\"\u003e\u003cincoming\u003eSequenceFlow_03xms9t\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10jh7md\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00lurk8\"/\u003e\u003cserviceTask id=\"ServiceTask_00lurk8\" name=\"Google Safe Browsing\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"abef1962-356f-4961-9a46-5f98d96b645a\"\u003e{\"inputs\":{},\"post_processing_script\":\"# This link contains further information on the site status of the url that is being checked\\nLINK_URL = \\\"https://www.google.com/transparencyreport/safebrowsing/diagnostic/#url={}\\\"\\nif results.success:\\n  if results.content:\\n    resp = results.content\\n    hit = []\\n    for match in resp.get(\\\"matches\\\", []):\\n      linkurl = match[\\\"threat\\\"][\\\"url\\\"]\\n      link = LINK_URL.format(match[\\\"threat\\\"][\\\"url\\\"])\\n      hit = [\\n      {\\n        \\\"name\\\": \\\"Threat Type\\\",\\n        \\\"type\\\": \\\"string\\\",\\n        \\\"value\\\": \\\"{}\\\".format(match[\\\"threatType\\\"])\\n      }, \\n      {\\n        \\\"name\\\": \\\"Report Link\\\",\\n        \\\"type\\\": \\\"uri\\\",\\n        \\\"value\\\": \\\"{}\\\".format(link)\\n      }, \\n      {\\n        \\\"name\\\": \\\"Platform Type\\\",\\n        \\\"type\\\": \\\"string\\\",\\n        \\\"value\\\": \\\"{}\\\".format(match[\\\"platformType\\\"])\\n      },\\n      {\\n        \\\"name\\\": \\\"URL Name\\\",\\n        \\\"type\\\": \\\"string\\\",\\n        \\\"value\\\": \\\"{}\\\".format(linkurl)\\n      }\\n      ]\\n      artifact.addHit(\\\"Google Safe Browsing Function\\\", hit)\\nelse:\\n  incident.addNote(\\\"Google Safe Browsing url check failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.googlesafebrowsing_artifact_type = artifact.type\\ninputs.googlesafebrowsing_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10jh7md\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03xms9t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_03xms9t\" sourceRef=\"ServiceTask_00lurk8\" targetRef=\"EndEvent_0x0wioq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19y2k6e\"\u003e\u003ctext\u003eResults are returned as a hit in the artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wr045i\" sourceRef=\"ServiceTask_00lurk8\" targetRef=\"TextAnnotation_19y2k6e\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0x0wioq\" id=\"EndEvent_0x0wioq_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"589\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"562\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10jh7md\" id=\"SequenceFlow_10jh7md_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"229.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00lurk8\" id=\"ServiceTask_00lurk8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"351\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03xms9t\" id=\"SequenceFlow_03xms9t_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"589\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"475\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19y2k6e\" id=\"TextAnnotation_19y2k6e_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"102\" x=\"461\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wr045i\" id=\"Association_0wr045i_di\"\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"95\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 25,
      "creator_id": "admin@example.com",
      "description": "This app uses Google Safe Browsing to check artifacts with a URL type and adds a hit if the site is potentially unsafe. The hit contains a link to Google Transparency Report that gives information on the potentially unsafe url.",
      "export_key": "google_safe_browsing_url_lookup",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647463298101,
      "name": "Google Safe Browsing URL Lookup",
      "object_type": "artifact",
      "programmatic_name": "google_safe_browsing_url_lookup",
      "tags": [
        {
          "tag_handle": "fn_googlesafebrowsing",
          "value": null
        }
      ],
      "uuid": "86e4e091-e62c-41ab-88b0-1b753933891b",
      "workflow_id": 7
    }
  ],
  "workspaces": []
}
