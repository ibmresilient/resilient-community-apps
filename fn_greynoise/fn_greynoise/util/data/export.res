{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: GreyNoise IP Query",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: GreyNoise IP Query",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "819595af-c5a0-4dc6-8a63-42a230d96954",
      "view_items": [],
      "workflows": [
        "example_greynoise_ip_query"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1591999758837,
  "export_format_version": 2,
  "extensions": [],
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/greynoise_type",
      "hide_notification": false,
      "id": 181,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "greynoise_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "greynoise_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5122154c-c377-435e-9baf-ea79ebc6e601",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "context",
          "properties": null,
          "uuid": "5eb47553-7819-4d10-bdc9-994fc3dd3094",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "quick",
          "properties": null,
          "uuid": "1237dd73-222a-4569-875f-caf281f436c2",
          "value": 53
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/greynoise_value",
      "hide_notification": false,
      "id": 182,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "greynoise_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "greynoise_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b5caca14-688a-4a2d-9c7c-09c1c578bbcd",
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
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 1,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Perform IP Address analysis",
        "format": "text"
      },
      "destination_handle": "fn_greynoise",
      "display_name": "GreyNoise IP Query",
      "export_key": "greynoise_ip_query",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 1,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1591900084905,
      "name": "greynoise_ip_query",
      "tags": [],
      "uuid": "4cdf2cff-89ae-4004-be1a-b40c1f8e85be",
      "version": 1,
      "view_items": [
        {
          "content": "b5caca14-688a-4a2d-9c7c-09c1c578bbcd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5122154c-c377-435e-9baf-ea79ebc6e601",
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
          "name": "Example: GreyNoise IP Query",
          "object_type": "artifact",
          "programmatic_name": "example_greynoise_ip_query",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 3,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1607691385434,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1607691385434,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_greynoise",
      "name": "fn_greynoise",
      "programmatic_name": "fn_greynoise",
      "tags": [],
      "users": [
        "a@a.com"
      ],
      "uuid": "cdd6b18c-e7f0-464a-a078-e29da5d92502"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 5634,
    "major": 36,
    "minor": 0,
    "version": "36.0.5634"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_greynoise_ip_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_greynoise_ip_query\" isExecutable=\"true\" name=\"Example: GreyNoise IP Query\"\u003e\u003cdocumentation\u003ePerform IP Address analysis\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1llgl3c\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q9ztob\" name=\"GreyNoise IP Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4cdf2cff-89ae-4004-be1a-b40c1f8e85be\"\u003e{\"inputs\":{\"5122154c-c377-435e-9baf-ea79ebc6e601\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"5eb47553-7819-4d10-bdc9-994fc3dd3094\"}}},\"post_processing_script\":\"if results[\u0027success\u0027]:\\n  note = u\\\"\\\"\\\"\u0026lt;div\u0026gt;Seen: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;IP: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;Classification: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;Tags: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;First seen: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;Last seen: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\n\u0026lt;div\u0026gt;Reverse DNS: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\\"\\\"\\\".format(\u0027True\u0027 if results.content[\u0027seen\u0027] else \u0027False\u0027, results.content[\u0027ip\u0027], results.content.get(\u0027classification\u0027), \\n                                          str(results.content.get(\u0027tags\u0027)), \\n                                          results.content.get(\u0027first_seen\u0027), results.content.get(\u0027last_seen\u0027),\\n                                          results.content.get(\u0027metadata\u0027, {}).get(\u0027rdns\u0027))\\n  if results.content.get(\u0027code\u0027):\\n    code_lookup = { \\n      \\\"0x00\\\": \\\"Never Observed\\\",\\n      \\\"0x01\\\": \\\"Observed\\\",\\n      \\\"0x02\\\": \\\"Observed, but incomplete\\\",\\n      \\\"0x03\\\": \\\"Adjacent to another observed\\\",\\n      \\\"0x04\\\": \\\"Reserved\\\",\\n      \\\"0x05\\\": \\\"Commonly Spoofed\\\",\\n      \\\"0x06\\\": \\\"Noise\\\",\\n      \\\"0x07\\\": \\\"Invalid setting\\\",\\n      \\\"0x08\\\": \\\"Not observed in last 60 days\\\"\\n    }\\n    note = note + u\\\"\u0026lt;div\u0026gt;Code: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\\\".format(code_lookup[results.content[\u0027code\u0027]])\\n  incident.addNote(helper.createRichText(note))\\nelse:\\n  incident.addNote(str(results.content))\\n\\n\\\"\\\"\\\"\\n{\u0027content\u0027: {u\u0027code\u0027: u\u00270x01\u0027, u\u0027ip\u0027: u\u002723.129.64.159\u0027, u\u0027noise\u0027: True}, \u0027success\u0027: True}\\n{\\n  \u0027content\u0027: {\\n    u\u0027classification\u0027: u\u0027malicious\u0027,\\n    u\u0027tags\u0027: [\\n      u\u0027CHINANET SSH Bruteforcer\u0027,\\n      u\u0027Go SSH Scanner\u0027,\\n      u\u0027HNAP Crawler\u0027,\\n      u\u0027HTTP Alt Scanner\u0027,\\n      u\u0027Nmap\u0027,\\n      u\u0027SSH Bruteforcer\u0027,\\n      u\u0027SSH Scanner\u0027,\\n      u\u0027SSH Worm\u0027,\\n      u\u0027TLS/SSL Crawler\u0027,\\n      u\u0027Tor\u0027,\\n      u\u0027VNC Bruteforcer\u0027,\\n      u\u0027VNC Scanner\u0027,\\n      u\u0027Web Crawler\u0027,\\n      u\u0027Web Scanner\u0027\\n    ],\\n    u\u0027ip\u0027: u\u002723.129.64.159\u0027,\\n    u\u0027actor\u0027: u\u0027unknown\u0027,\\n    u\u0027raw_data\u0027: {\\n      u\u0027web\u0027: {\\n        u\u0027paths\u0027: [\\n          u\u0027/HNAP1/\u0027\\n        ],\\n        u\u0027useragents\u0027: [\\n          u\u0027Mozilla/5.0 (Windows NT 5.1; rv:9.0.1) Gecko/20100101 Firefox/9.0.1\u0027\\n        ]\\n      },\\n      u\u0027ja3\u0027: [\\n        {\\n          u\u0027port\u0027: 443,\\n          u\u0027fingerprint\u0027: u\u002795d6f221c32953590c3a85cbee0d9e61\u0027\\n        },\\n        {\\n          u\u0027port\u0027: 8443,\\n          u\u0027fingerprint\u0027: u\u002797f7c02d49f8b261f4b7157e38945459\u0027\\n        },\\n        {\\n          u\u0027port\u0027: 10000,\\n          u\u0027fingerprint\u0027: u\u00270d85f6adde9dc6aa98804d6cfa2f90c1\u0027\\n        },\\n        {\\n          u\u0027port\u0027: 8080,\\n          u\u0027fingerprint\u0027: u\u0027ac8cb78cabd066a9ce1e90848a0ba5d9\u0027\\n        }\\n      ],\\n      u\u0027scan\u0027: [\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 22\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 443\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 1027\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 1028\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 5000\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 5800\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 5900\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 5905\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 8000\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 8080\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 8443\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 10000\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 32768\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 41798\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 43719\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 49152\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 49153\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 49154\\n        },\\n        {\\n          u\u0027protocol\u0027: u\u0027TCP\u0027,\\n          u\u0027port\u0027: 49157\\n        }\\n      ]\\n    },\\n    u\u0027seen\u0027: True,\\n    u\u0027first_seen\u0027: u\u00272019-04-23\u0027,\\n    u\u0027metadata\u0027: {\\n      u\u0027category\u0027: u\u0027business\u0027,\\n      u\u0027city\u0027: u\u0027Seattle\u0027,\\n      u\u0027tor\u0027: True,\\n      u\u0027country\u0027: u\u0027United States\u0027,\\n      u\u0027country_code\u0027: u\u0027US\u0027,\\n      u\u0027organization\u0027: u\u0027Emerald Onion\u0027,\\n      u\u0027os\u0027: u\u0027FreeBSD\u0027,\\n      u\u0027asn\u0027: u\u0027AS396507\u0027\\n    },\\n    u\u0027last_seen\u0027: u\u00272019-10-10\u0027\\n  },\\n  \u0027success\u0027: True\\n}\\n\\\"\\\"\\\"\",\"pre_processing_script\":\"inputs.greynoise_value = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1llgl3c\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wo2ppk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1llgl3c\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q9ztob\"/\u003e\u003cendEvent id=\"EndEvent_1puydmf\"\u003e\u003cincoming\u003eSequenceFlow_0wo2ppk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0wo2ppk\" sourceRef=\"ServiceTask_0q9ztob\" targetRef=\"EndEvent_1puydmf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q9ztob\" id=\"ServiceTask_0q9ztob_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"249\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1llgl3c\" id=\"SequenceFlow_1llgl3c_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"223.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1puydmf\" id=\"EndEvent_1puydmf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"401\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"419\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wo2ppk\" id=\"SequenceFlow_0wo2ppk_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"375\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@a.com",
      "description": "Perform IP Address analysis",
      "export_key": "example_greynoise_ip_query",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1591998839746,
      "name": "Example: GreyNoise IP Query",
      "object_type": "artifact",
      "programmatic_name": "example_greynoise_ip_query",
      "tags": [],
      "uuid": "cdd6b18c-e7f0-464a-a078-e29da5d92502",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
