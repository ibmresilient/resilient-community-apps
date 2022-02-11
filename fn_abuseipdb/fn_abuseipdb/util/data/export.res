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
      "export_key": "AbuseIPDB Check IP Address Blocklist",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "AbuseIPDB Check IP Address Blocklist",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "f6f43731-35c7-45bc-8331-29a173ed70fc",
      "view_items": [],
      "workflows": [
        "abuseipdb_check_ip_address_blocklist"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1644431167204,
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
      "export_key": "__function/abuseipdb_artifact_value",
      "hide_notification": false,
      "id": 271,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "abuseipdb_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "abuseipdb_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d7001b29-3bca-495f-abbb-39ee068b9356",
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
      "export_key": "__function/abuseipdb_artifact_type",
      "hide_notification": false,
      "id": 272,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "abuseipdb_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "abuseipdb_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "156070d3-a12a-4429-8084-5f7d98e027b7",
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
      "created_date": 1643921317640,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Pulls data from AbuseIPDB (www.abuseipdb.com) and checks if an IP artifact is blacklisted. Needs an AbuseIPDB account and an v2 api key to work.",
        "format": "text"
      },
      "destination_handle": "abuseipdb",
      "display_name": "AbuseIPDB",
      "export_key": "fn_abuseipdb",
      "id": 1,
      "last_modified_by": {
        "display_name": "Chris\u0027 Integration Server v43",
        "id": 6,
        "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
        "type": "apikey"
      },
      "last_modified_time": 1643921317708,
      "name": "fn_abuseipdb",
      "tags": [],
      "uuid": "f26776eb-acf7-4df7-b827-fd71a8d986a0",
      "version": 1,
      "view_items": [
        {
          "content": "156070d3-a12a-4429-8084-5f7d98e027b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d7001b29-3bca-495f-abbb-39ee068b9356",
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
          "name": "AbuseIPDB Check IP Address Blocklist",
          "object_type": "artifact",
          "programmatic_name": "abuseipdb_check_ip_address_blocklist",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 4,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1644431165748,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1644431165748,
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
      "export_key": "abuseipdb",
      "name": "AbuseIPDB",
      "programmatic_name": "abuseipdb",
      "tags": [],
      "users": [],
      "uuid": "2359b60c-9076-435b-8c9d-194076dd59bb"
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
        "version": 30,
        "workflow_id": "abuseipdb_check_ip_address_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"abuseipdb_check_ip_address_blocklist\" isExecutable=\"true\" name=\"AbuseIPDB Check IP Address Blocklist\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_146m5zt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_166ubax\"\u003e\u003cincoming\u003eSequenceFlow_1qgcmf3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_146m5zt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1itvc92\"/\u003e\u003cserviceTask id=\"ServiceTask_1itvc92\" name=\"AbuseIPDB\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f26776eb-acf7-4df7-b827-fd71a8d986a0\"\u003e{\"inputs\":{},\"post_processing_script\":\"CATEGORIES= {\\n  3: \\\"Fraud Orders\\\",\\n  4: \\\"DDoS Attack\\\",\\n  5: \\\"FTP Brute-Force\\\",\\n  6: \\\"Ping of Death\\\",\\n  7: \\\"Phishing\\\",\\n  8: \\\"Fraud VoIP\\\",\\n  9: \\\"Open Proxy\\\",\\n  10: \\\"Web Spam\\\",\\n  11: \\\"Email Spam\\\",\\n  12: \\\"Blog Spam\\\",\\n  13: \\\"VPN IP\\\",\\n  14: \\\"Port Scan\\\",\\n  15: \\\"Hacking\\\",\\n  16: \\\"SQL Injection\\\",\\n  17: \\\"Spoofing\\\",\\n  18: \\\"Brute-Force\\\",\\n  19: \\\"Bad Web Bot\\\",\\n  20: \\\"Exploited Host\\\",\\n  21: \\\"Web App Attack\\\",\\n  22: \\\"SSH\\\",\\n  23: \\\"IoT Targeted\\\",\\n}\\n\\nif results.success:\\n  resp_data = results.content[\u0027data\u0027]\\n  number_of_reports = resp_data[\u0027totalReports\u0027]\\n  country_name = resp_data[\u0027countryName\u0027]\\n  most_recent_report = resp_data[\u0027lastReportedAt\u0027]\\n  confidence_score = resp_data.get(\\\"abuseConfidenceScore\\\", 0)\\n  \\n  hit = []\\n  \\n  # get clean list of de-duped categories\\n  categories_names = \\\"\\\"\\n  if resp_data.get(\u0027reports\u0027):\\n      categories_list = []\\n      for report in resp_data[\u0027reports\u0027]:\\n          categories_list.extend(report[\\\"categories\\\"])\\n      categories_set = set(categories_list)  # dedup list\\n      categories_names = u\u0027, \u0027.join(CATEGORIES.get(item, \u0027unknown\u0027) for item in categories_set)\\n  \\n  # only return data if there\u0027s anything useful\\n  if number_of_reports or confidence_score:\\n      hit = [\\n        {\\n          \\\"name\\\": \\\"Confidence Score\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(confidence_score)\\n        }, \\n        {\\n          \\\"name\\\": \\\"Number of Reports\\\",\\n          \\\"type\\\": \\\"number\\\",\\n          \\\"value\\\": \\\"{}\\\".format(number_of_reports)\\n        }, \\n        {\\n          \\\"name\\\": \\\"Country\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(country_name)\\n        },\\n        {\\n          \\\"name\\\": \\\"Most Recent Report\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(most_recent_report)\\n        },\\n        {\\n          \\\"name\\\": \\\"Categories\\\",\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(categories_names)\\n        }\\n        ]\\n  artifact.addHit(\\\"AbuseIPDB Function hits added\\\", hit)\\nelse:\\n  incident.addNote(\\\"AbuseIPDB Check IP Address Blocklist failed: {}\\\".format(results.reason))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.abuseipdb_artifact_type = artifact.type\\ninputs.abuseipdb_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_146m5zt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qgcmf3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qgcmf3\" sourceRef=\"ServiceTask_1itvc92\" targetRef=\"EndEvent_166ubax\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_166ubax\" id=\"EndEvent_166ubax_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"644\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"662\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_146m5zt\" id=\"SequenceFlow_146m5zt_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"302\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"250\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1itvc92\" id=\"ServiceTask_1itvc92_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"302\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qgcmf3\" id=\"SequenceFlow_1qgcmf3_di\"\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"644\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 30,
      "creator_id": "admin@example.com",
      "description": "",
      "export_key": "abuseipdb_check_ip_address_blocklist",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1644263991806,
      "name": "AbuseIPDB Check IP Address Blocklist",
      "object_type": "artifact",
      "programmatic_name": "abuseipdb_check_ip_address_blocklist",
      "tags": [],
      "uuid": "a4d1ce0e-7fe0-4896-9296-0cc9d4f352d9",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
