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
      "id": 18,
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
        "passivetotal"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1646233856994,
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
      "created_date": 1645643819720,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "passivetotal",
      "display_name": "PassiveTotal",
      "export_key": "fn_passivetotal",
      "id": 6,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1646165769260,
      "name": "fn_passivetotal",
      "tags": [],
      "uuid": "490b5e45-2e1f-4909-b905-a009e9a7255b",
      "version": 7,
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
          "name": "PassiveTotal",
          "object_type": "artifact",
          "programmatic_name": "passivetotal",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 33,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1646233855551,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1646233855551,
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
        "version": 1,
        "workflow_id": "passivetotal",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"passivetotal\" isExecutable=\"true\" name=\"PassiveTotal\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ecxcq2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_13g5qp1\"\u003e\u003cincoming\u003eSequenceFlow_0lrwu2s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ecxcq2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0313pfu\"/\u003e\u003cserviceTask id=\"ServiceTask_0313pfu\" name=\"PassiveTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"490b5e45-2e1f-4909-b905-a009e9a7255b\"\u003e{\"inputs\":{},\"post_processing_script\":\"# if results.success:\\n\\n# def _generate_hit(self, artifact_value, tags_hits_list):\\n#         \\\"\\\"\\\"\\n#         Query RiskIQ PassiveTotal API for the given \u0027net.name\u0027 (domain name artifact), \u0027net.uri\u0027 (URL) or \u0027net.ip\u0027\\n#         (IP address) and generate a Hit.\\n#         :param artifact_value\\n#         :param tags_hits_list\\n#         \\\"\\\"\\\"\\n#         # Passive DNS Results - Hits\\n#         # We grab the totalRecords number and show the First Seen date to Last Seen date interval\\n#         pdns_results_response = self._passivetotal_get_response(self.passivetotal_passive_dns_api_url,\\n#                                                                 artifact_value)\\n#         pdns_hit_number, pdns_first_seen, pdns_last_seen = None, None, None\\n#         if pdns_results_response.status_code == 200:\\n#             pdns_results = pdns_results_response.json()\\n#             pdns_hit_number = pdns_results.get(\\\"totalRecords\\\", None)\\n#             pdns_first_seen = pdns_results.get(\\\"firstSeen\\\", None)\\n#             pdns_last_seen = pdns_results.get(\\\"lastSeen\\\", None)\\n#             LOG.info(pdns_hit_number)\\n#             LOG.info(pdns_first_seen)\\n#             LOG.info(pdns_last_seen)\\n#         else:\\n#             LOG.info(\\\"No Passive DNS information found for artifact value: {0}\\\".format(artifact_value))\\n#             LOG.debug(pdns_results_response.text)\\n\\n#         # URL Classification - suspicious, malicious etc\\n#         classification_results_response = self._passivetotal_get_response(self.passivetotal_actions_class_api_url,\\n#                                                                           artifact_value)\\n#         classification_hit = None\\n#         if classification_results_response.status_code == 200:\\n#             classification_results = classification_results_response.json()\\n#             classification_hit = classification_results.get(\\\"classification\\\", None)\\n#             LOG.info(classification_hit)\\n#         else:\\n#             LOG.info(\\\"No URL classification found for artifact value: {0}\\\".format(artifact_value))\\n#             LOG.debug(classification_results_response.text)\\n\\n#         # Count of subdomains\\n#         subdomain_results_response = self._passivetotal_get_response(self.passivetotal_enrich_subdom_api_url,\\n#                                                                     artifact_value)\\n#         subdomain_hits_number, first_ten_subdomains = None, None\\n#         if subdomain_results_response.status_code == 200:\\n#             subdomain_results = subdomain_results_response.json()\\n#             subdomain_hits = subdomain_results.get(\\\"subdomains\\\", None)\\n#             subdomain_hits_number = len(subdomain_hits) if subdomain_hits else None\\n#             first_ten_subdomains = \u0027, \u0027.join(subdomain_hits[:10]) if subdomain_hits else None\\n#             LOG.info(subdomain_hits_number)\\n#             LOG.info(first_ten_subdomains)\\n#         else:\\n#             LOG.info(\\\"No subdomain information found for artifact value: {0}\\\".format(artifact_value))\\n#             LOG.debug(subdomain_results_response.text)\\n\\n#         # Convert tags hits list to str\\n#         tags_hits = \\\", \\\".join(tags_hits_list) if tags_hits_list else None\\n\\n#         # Construct url back to to PassiveThreat\\n#         report_url = self.passivetotal_community_url + artifact_value\\n\\n#         return Hit(\\n#             NumberProp(name=\\\"Number of Passive DNS Records\\\", value=pdns_hit_number),\\n#             StringProp(name=\\\"First Seen\\\", value=pdns_first_seen),\\n#             StringProp(name=\\\"Last Seen\\\", value=pdns_last_seen),\\n#             NumberProp(name=\\\"Subdomains - All\\\", value=subdomain_hits_number),\\n#             StringProp(name=\\\"Subdomains - First ten Hostnames\\\", value=first_ten_subdomains),\\n#             StringProp(name=\\\"Tags\\\", value=tags_hits),\\n#             StringProp(name=\\\"Classification\\\", value=classification_hit),\\n#             UriProp(name=\\\"Report Link\\\", value=report_url)\\n#             )\\n            \\n#             hit = [\\n#         {\\n#           \\\"name\\\": \\\"Number of Passive DNS Records\\\",\\n#           \\\"type\\\": \\\"number\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(pdns_hit_number)\\n#         }, \\n#         {\\n#           \\\"name\\\": \\\"First Seen\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(pdns_first_seen)\\n#         }, \\n#         {\\n#           \\\"name\\\": \\\"Last Seen\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(pdns_last_seen)\\n#         },\\n#         {\\n#           \\\"name\\\": \\\"Subdomains - All\\\",\\n#           \\\"type\\\": \\\"number\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(subdomain_hits_number)\\n#         },\\n#         {\\n#           \\\"name\\\": \\\"Subdomains - First ten Hostnames\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(first_ten_subdomains)\\n#         },\\n#         {\\n#           \\\"name\\\": \\\"Subdomains - First ten Hostnames\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(first_ten_subdomains)\\n#         },\\n#         {\\n#           \\\"name\\\": \\\"Subdomains - First ten Hostnames\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(first_ten_subdomains)\\n#         },\\n#         {\\n#           \\\"name\\\": \\\"Subdomains - First ten Hostnames\\\",\\n#           \\\"type\\\": \\\"string\\\",\\n#           \\\"value\\\": \\\"{}\\\".format(first_ten_subdomains)\\n#         }\\n#         ]\\n#   artifact.addHit(\\\"AbuseIPDB Function hits added\\\", hit)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.passivetotal_artifact_type = artifact.type\\ninputs.passivetotal_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ecxcq2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0lrwu2s\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0lrwu2s\" sourceRef=\"ServiceTask_0313pfu\" targetRef=\"EndEvent_13g5qp1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_13g5qp1\" id=\"EndEvent_13g5qp1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"378\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"396\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ecxcq2\" id=\"SequenceFlow_1ecxcq2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"228\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0313pfu\" id=\"ServiceTask_0313pfu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"228\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lrwu2s\" id=\"SequenceFlow_0lrwu2s_di\"\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"353\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "",
      "export_key": "passivetotal",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1646166093098,
      "name": "PassiveTotal",
      "object_type": "artifact",
      "programmatic_name": "passivetotal",
      "tags": [],
      "uuid": "9e1756e1-9eea-44a2-9ea8-13bce2d8a98c",
      "workflow_id": 9
    }
  ],
  "workspaces": []
}
