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
      "export_key": "RiskIQ PassiveTotal Query",
      "id": 19,
      "logic_type": "all",
      "message_destinations": [],
      "name": "RiskIQ PassiveTotal Query",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "57eb44d2-e20d-42b3-abc8-a3b57368e736",
      "view_items": [],
      "workflows": [
        "passivetotal_site_lookup"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1647282991228,
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
      "export_key": "__function/passivetotal_artifact_value",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "passivetotal_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "passivetotal_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "09c83183-5a5c-4abb-9f69-5a288da7490a",
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
      "export_key": "__function/passivetotal_artifact_type",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "passivetotal_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "passivetotal_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "30dee09c-2dac-4dd3-accf-6e07266c1a44",
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
      "created_date": 1646234466157,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Queries PassiveTotal and checks if the site is compromised according to your definition. Needs a PassiveTotal account and api key to work.",
        "format": "text"
      },
      "destination_handle": "passivetotal",
      "display_name": "PassiveTotal",
      "export_key": "fn_passivetotal",
      "id": 7,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1646853960301,
      "name": "fn_passivetotal",
      "tags": [],
      "uuid": "490b5e45-2e1f-4909-b905-a009e9a7255b",
      "version": 3,
      "view_items": [
        {
          "content": "09c83183-5a5c-4abb-9f69-5a288da7490a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "30dee09c-2dac-4dd3-accf-6e07266c1a44",
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
          "name": "PassiveTotal Site Lookup",
          "object_type": "artifact",
          "programmatic_name": "passivetotal_site_lookup",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 50,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1647282989797,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1647282989797,
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
      "export_key": "passivetotal",
      "name": "PassiveTotal",
      "programmatic_name": "passivetotal",
      "tags": [],
      "users": [],
      "uuid": "31c7de9b-5d7f-4660-bd17-07d5bb879fd8"
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
        "version": 6,
        "workflow_id": "passivetotal_site_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"passivetotal_site_lookup\" isExecutable=\"true\" name=\"PassiveTotal Site Lookup\"\u003e\u003cdocumentation\u003eQueries RiskIQ PassiveTotal API for given DNS, URL, and IP addresses. This workflow will generate a hit if the site is compromised according to your definition.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0u47izu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1uq6240\"\u003e\u003cincoming\u003eSequenceFlow_01qu44r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0u47izu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_073mjd2\"/\u003e\u003cserviceTask id=\"ServiceTask_073mjd2\" name=\"PassiveTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"490b5e45-2e1f-4909-b905-a009e9a7255b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.content:\\n  data = {}\\n  for dictionary in results.content:\\n    data.update(dictionary)\\n  pdns_hit_number = data[\\\"pdns_hit_number\\\"]\\n  pdns_first_seen = data[\\\"pdns_first_seen\\\"]\\n  pdns_last_seen = data[\\\"pdns_last_seen\\\"]\\n  subdomain_hits_number = data[\\\"subdomain_hits_number\\\"]\\n  first_ten_subdomains = data[\\\"first_ten_subdomains\\\"]\\n  tags_hits = data[\\\"tags_hits_str\\\"]\\n  classification_hit = data[\\\"classification_hit\\\"]\\n  report_url = data[\\\"report_url\\\"]\\n\\n            \\n  hit = [\\n        {\\n          \\\"name\\\": \\\"Number of Passive DNS Records\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(pdns_hit_number)\\n        }, \\n        {\\n          \\\"name\\\": \\\"First Seen\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(pdns_first_seen)\\n        }, \\n        {\\n          \\\"name\\\": \\\"Last Seen\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(pdns_last_seen)\\n        },\\n        {\\n          \\\"name\\\": \\\"Subdomains - All\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(subdomain_hits_number)\\n        },\\n        {\\n          \\\"name\\\": \\\"Subdomains - First ten Hostnames\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(first_ten_subdomains)\\n        },\\n        {\\n          \\\"name\\\": \\\"Tags\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(tags_hits)\\n        },\\n        {\\n          \\\"name\\\": \\\"Classification\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(classification_hit)\\n        },\\n        {\\n          \\\"name\\\": \\\"Report Link\\\",\\n          \\\"type\\\": \\\"uri\\\",\\n          \\\"value\\\": \\\"{}\\\".format(report_url)\\n        }\\n        ]\\n  artifact.addHit(\\\"PassiveTotal Function hits added\\\", hit)\\nelse:\\n  incident.addNote(\\\"PassiveTotal Query failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.passivetotal_artifact_type = artifact.type\\ninputs.passivetotal_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0u47izu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01qu44r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_01qu44r\" sourceRef=\"ServiceTask_073mjd2\" targetRef=\"EndEvent_1uq6240\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kirggk\"\u003e\u003ctext\u003eResults are returned as a hit in the artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hxfqjv\" sourceRef=\"ServiceTask_073mjd2\" targetRef=\"TextAnnotation_1kirggk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1uq6240\" id=\"EndEvent_1uq6240_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"503\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"476\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u47izu\" id=\"SequenceFlow_0u47izu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"294\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"201\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_073mjd2\" id=\"ServiceTask_073mjd2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"294\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01qu44r\" id=\"SequenceFlow_01qu44r_di\"\u003e\u003comgdi:waypoint x=\"394\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"403.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kirggk\" id=\"TextAnnotation_1kirggk_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"114\" x=\"427\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hxfqjv\" id=\"Association_0hxfqjv_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "admin@example.com",
      "description": "Queries RiskIQ PassiveTotal API for given DNS, URL, and IP addresses. This workflow will generate a hit if the site is compromised according to your definition.",
      "export_key": "passivetotal_site_lookup",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1647282806580,
      "name": "PassiveTotal Site Lookup",
      "object_type": "artifact",
      "programmatic_name": "passivetotal_site_lookup",
      "tags": [],
      "uuid": "585ce4d0-f664-43a6-bca5-f3754f296d9c",
      "workflow_id": 11
    }
  ],
  "workspaces": []
}
