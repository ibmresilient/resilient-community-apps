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
            "File Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Yeti Observable Query",
      "id": 21,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Yeti Observable Query",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "3c263085-950a-4c33-aee8-12d49019cc7e",
      "view_items": [],
      "workflows": [
        "yeti_observables_query"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1649351291896,
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
      "export_key": "__function/yeti_artifact_type",
      "hide_notification": false,
      "id": 285,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "yeti_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "yeti_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a25b8b59-cd43-4b1c-b68c-485c84cc6861",
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
      "export_key": "__function/yeti_artifact_value",
      "hide_notification": false,
      "id": 286,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "yeti_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "yeti_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b5cb7a1d-5896-4c12-912a-a40c98eabc03",
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
      "created_date": 1648493506559,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Queries Yeti and updates SOAR with any information gained on the artifact. All Yeti observables are supported by this integration. For more info about YETI platform, please visit https://yeti-platform.github.io.",
        "format": "text"
      },
      "destination_handle": "yeti",
      "display_name": "Yeti",
      "export_key": "fn_yeti",
      "id": 9,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649351267202,
      "name": "fn_yeti",
      "tags": [],
      "uuid": "c40c1c28-5054-4d6b-b50d-48e639309c29",
      "version": 4,
      "view_items": [
        {
          "content": "a25b8b59-cd43-4b1c-b68c-485c84cc6861",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b5cb7a1d-5896-4c12-912a-a40c98eabc03",
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
          "name": "Yeti Observables Query",
          "object_type": "artifact",
          "programmatic_name": "yeti_observables_query",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
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
      "create_date": 1649351290319,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1649351290319,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "yeti",
      "name": "Yeti",
      "programmatic_name": "yeti",
      "tags": [],
      "users": [],
      "uuid": "6b32b080-d283-47d2-8c90-f7bd3e9f2d47"
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
        "version": 14,
        "workflow_id": "yeti_observables_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"yeti_observables_query\" isExecutable=\"true\" name=\"Yeti Observables Query\"\u003e\u003cdocumentation\u003eQueries Yeti and returns details on artifacts that are turned into a hit in the post-processing script if information is found.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0323eue\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1j0px72\"\u003e\u003cincoming\u003eSequenceFlow_0l11xh0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0323eue\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1102nvc\"/\u003e\u003cserviceTask id=\"ServiceTask_1102nvc\" name=\"Yeti\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c40c1c28-5054-4d6b-b50d-48e639309c29\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  if results.content:\\n    resp = results.content\\n    hit = []\\n\\n    tags = \\\"\\\"\\n    for tag in resp[0][\\\"tags\\\"]:\\n        if tags != \\\"\\\":\\n            tags += \\\", \\\"\\n        tags += tag[\\\"name\\\"]\\n    \\n    descript = resp[0][\\\"description\\\"] if resp[0][\\\"description\\\"] else \\\"None\\\"\\n    hit = [\\n        {\\n          \\\"name\\\": \\\"Type\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(resp[0][\\\"type\\\"])\\n        }, \\n        {\\n          \\\"name\\\": \\\"Value\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(resp[0][\\\"value\\\"])\\n        }, \\n        {\\n          \\\"name\\\": \\\"Tags\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(tags)\\n        },\\n        {\\n          \\\"name\\\": \\\"Created\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(resp[0][\\\"created\\\"])\\n        },\\n        {\\n          \\\"name\\\": \\\"URL\\\",\\n          \\\"type\\\": \\\"uri\\\",\\n          \\\"value\\\": \\\"{}\\\".format(resp[0][\\\"human_url\\\"])\\n        },\\n        {\\n          \\\"name\\\": \\\"Description\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(descript)\\n        }\\n        ]\\n    artifact.addHit(\\\"Yeti Function hits added\\\", hit)\\nelse:\\n  incident.addNote(\\\"Yeti query failed: {}\\\".format(results.reason))\\n  \",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.yeti_artifact_type = artifact.type\\ninputs.yeti_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0323eue\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0l11xh0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0l11xh0\" sourceRef=\"ServiceTask_1102nvc\" targetRef=\"EndEvent_1j0px72\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0wggi5y\"\u003e\u003ctext\u003eResults are returned as a hit in the artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0l2mmzy\" sourceRef=\"ServiceTask_1102nvc\" targetRef=\"TextAnnotation_0wggi5y\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1j0px72\" id=\"EndEvent_1j0px72_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"398\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"416\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0323eue\" id=\"SequenceFlow_0323eue_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"246\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"177\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1102nvc\" id=\"ServiceTask_1102nvc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"246\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l11xh0\" id=\"SequenceFlow_0l11xh0_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"398\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"327\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0wggi5y\" id=\"TextAnnotation_0wggi5y_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"100\" x=\"352\" y=\"75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0l2mmzy\" id=\"Association_0l2mmzy_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "creator_id": "admin@example.com",
      "description": "Queries Yeti and returns details on artifacts that are turned into a hit in the post-processing script if information is found.",
      "export_key": "yeti_observables_query",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1649275114108,
      "name": "Yeti Observables Query",
      "object_type": "artifact",
      "programmatic_name": "yeti_observables_query",
      "tags": [],
      "uuid": "19370fe3-c4ca-472b-80ea-28ea170f27bd",
      "workflow_id": 14
    }
  ],
  "workspaces": []
}
