{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1682025779472,
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
      "export_key": "__function/artifact_id",
      "hide_notification": false,
      "id": 666,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d8c303ee-9ac9-4d06-8e18-2fcaf2c1a6b6",
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
      "export_key": "__function/vt_data",
      "hide_notification": false,
      "id": 665,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "vt_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "vt_data",
      "tooltip": "data field for virusTotal lookup",
      "type_id": 11,
      "uuid": "f19de6f6-b219-4e67-885c-0185901d0e34",
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
      "export_key": "__function/attachment_id",
      "hide_notification": false,
      "id": 667,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "17c3e652-6559-4935-9f95-74374ca37a7b",
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
      "export_key": "__function/vt_type",
      "hide_notification": false,
      "id": 668,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "vt_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "vt_type",
      "tooltip": "descriptor for the type of virusTotal lookup to perform",
      "type_id": 11,
      "uuid": "192e72c4-13ac-4be6-b636-c99841e72d10",
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 300,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "509d6b58-e4b5-4150-b1d0-6843c6dcfb8d",
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
      "created_date": 1682018701880,
      "description": {
        "content": "perform scans and return reports on ip addresses, urls, domains, hashes and files",
        "format": "text"
      },
      "destination_handle": "fn_virustotal",
      "display_name": "VirusTotal",
      "export_key": "virustotal",
      "id": 37,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1682018701996,
      "name": "virustotal",
      "tags": [],
      "uuid": "d108590a-21f9-4e42-92c4-d2a6fe39c9b4",
      "version": 1,
      "view_items": [
        {
          "content": "509d6b58-e4b5-4150-b1d0-6843c6dcfb8d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d8c303ee-9ac9-4d06-8e18-2fcaf2c1a6b6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "192e72c4-13ac-4be6-b636-c99841e72d10",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f19de6f6-b219-4e67-885c-0185901d0e34",
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
          "name": "Example: VirusTotal Scan",
          "object_type": "artifact",
          "programmatic_name": "example_virustotal_scan",
          "tags": [],
          "uuid": null,
          "workflow_id": 142
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: VirusTotal Scan (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_virustotal_scan_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 141
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 328,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1682025777513,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1682025777513,
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
      "export_key": "fn_virustotal",
      "name": "fn_virustotal",
      "programmatic_name": "fn_virustotal",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "d7456a95-a78e-47ae-a3a8-49eb690cc371"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\" isExecutable=\"true\" name=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qvbax8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"VirusTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d108590a-21f9-4e42-92c4-d2a6fe39c9b4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"typeLookup = { \u0027Email Attachment\u0027: \u0027file\u0027, \u0027Malware Sample\u0027: \u0027file\u0027, \u0027Malware MD5 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-1 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-256 Hash\u0027: \u0027hash\u0027, \u0027Other File\u0027: \u0027file\u0027, \u0027RCF 822 Email Message Fife\u0027: \u0027file\u0027, \u0027File Name\u0027: \u0027filename\u0027,\\n \u0027URL\u0027: \u0027url\u0027, \u0027IP Address\u0027: \u0027ip\u0027, \u0027DNS Name\u0027:\u0027domain\u0027}\\nif artifact.type in typeLookup:\\n  inputs.vt_type = typeLookup.get(artifact.type, artifact.type)\\nelse:\\n  inputs.vt_type = artifact.type\\n\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\ninputs.vt_data = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"vt_scan_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qvbax8\u003c/incoming\u003e\u003coutgoing\u003eFlow_12ot3ft\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qvbax8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"VirusTotal: Write artifact scan to a note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a4feb482-12fb-4a48-b09b-a68f1a227daf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12ot3ft\u003c/incoming\u003e\u003coutgoing\u003eFlow_1yh0cma\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_12ot3ft\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1yh0cma\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1yh0cma\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qvbax8\" id=\"Flow_0qvbax8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12ot3ft\" id=\"Flow_12ot3ft_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1yh0cma\" id=\"Flow_1yh0cma_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168.35000610351562\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318.3500061035156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"474.3500061035156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1682019057832,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
      "description": {
        "content": "Perform a VirusTotal scan an artifact and write the results to a note for review.  \n\nIn some cases, the scan results may not be available immediately. \nIn those cases, a link to the VirusTotal report is provided for review when complete. ",
        "format": "text"
      },
      "display_name": "VirusTotal: Scan Artifact",
      "export_key": "virustotal_scan_artifact",
      "field_type_handle": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
      "fields_type": {
        "actions": [],
        "display_name": "VirusTotal: Scan Artifact",
        "export_key": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
        "uuid": "54d8b3cb-979f-45bb-b548-50ba6ff268c6"
      },
      "has_logical_errors": false,
      "id": 64,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1682020086280,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1682019251876,
          "description": "Write VirusTotal scan results to an incident note.",
          "enabled": false,
          "export_key": "VirusTotal: Write artifact scan to a note",
          "id": 86,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1682019472403,
          "name": "VirusTotal: Write artifact scan to a note",
          "object_type": "artifact",
          "playbook_handle": "virustotal_scan_artifact",
          "programmatic_name": "virustotal_scan_artifact_virustotal_write_artifact_scan_to_a_note",
          "script_text": "results = playbook.functions.results.vt_scan_results\n\ndef mk_report(link):\n  return u\"\u003ca target=\u0027blank\u0027 href=\u0027{}\u0027\u003eVirusTotal Report\u003c/a\u003e\u003c/p\u003e\".format(link)\n  \nmsg = u\"\u003cp\u003eArtifact: {}\u003c/p\u003e\".format(artifact.value)\nif results.scan.get(\u0027positives\u0027) is not None:\n  msg = msg + u\"\u003cp\u003ePositives: \u003cspan style=\u0027color:red\u0027\u003e{}\u003c/span\u003e out of {}\u003c/p\u003e \u003cp\u003e{}\u003c/p\u003e\".format(results.scan.get(\u0027positives\u0027), results.scan.get(\u0027total\u0027), mk_report(results.scan.get(\u0027permalink\u0027)))\nelif results.scan.get(\u0027detected_urls\u0027) is not None:\n  analysis = []\n  for section in [\u0027detected_referrer_samples\u0027, \u0027detected_communicating_samples\u0027, \u0027detected_urls\u0027]:\n    test_for_positive = results.scan.get(section)\n    if test_for_positive is not None:\n      is_positive = False\n      positive_value = 0\n      latest_date = None\n      first_date = None\n      url = None\n      for sample in test_for_positive:\n        if sample.get(\u0027positives\u0027, -1) \u003e 0:\n          if not is_positive:\n            latest_date = sample.get(\u0027date\u0027) or sample.get(\u0027scan_date\u0027)\n            is_positive = sample.get(\u0027positives\u0027)  or sample.get(\u0027scan_date\u0027)\n            url = sample.get(\u0027url\u0027)\n            \n          first_date = sample.get(\u0027date\u0027) or sample.get(\u0027scan_date\u0027)\n      \n      if url:\n        scan = u\"\"\"\u003cp\u003e\u003cb\u003e{}\u003c/b\u003e\nPositives: \u003cspan style=\u0027color:{}\u0027\u003e{}\u003c/span\u003e\nFirst Seen Date: {}\nLast Seen Date: {}\nURL: {}\u003c/p\u003e\"\"\".format(section, \"red\" if is_positive else \"black\", is_positive, first_date, latest_date, url)\n      else:\n        scan = u\"\"\"\u003cp\u003e\u003cb\u003e{}\u003c/b\u003e\nPositives: \u003cspan style=\u0027color:{}\u0027\u003e{}\u003c/span\u003e\nFirst Seen Date: {}\nLast Seen Date: {}\u003c/p\u003e\"\"\".format(section, \"red\" if is_positive else \"black\", is_positive, first_date, latest_date)\n      analysis.append(scan)\n    \n  msg = msg + u\"\\n\".join(analysis)\nelse:\n  msg = msg + results.scan[\u0027verbose_msg\u0027]\n  if results.scan.get(\u0027permalink\u0027):\n    msg = msg + \"\\n{}\".format(mk_report(results.scan.get(\u0027permalink\u0027)))\n\nincident.addNote(helper.createRichText(u\"\u003cdiv\u003e{}\u003c/div\u003e\".format(msg)))\n\nif results.scan.get(\"permalink\"):\n  if artifact.description:\n    artifact.description = artifact.description.content +\"\\nVirusTotal Report: {}\".format(results.scan.get(\"permalink\"))\n  else:\n    artifact.description = \"\\nVirusTotal Report: {}\".format(results.scan.get(\"permalink\"))\n\nif results.scan.get(\u0027md5\u0027) is not None:\n  incident.addArtifact(\u0027Malware MD5 Hash\u0027, results.scan.get(\u0027md5\u0027), None)\n\nif results.scan.get(\u0027sha1\u0027) is not None:\n  incident.addArtifact(\u0027Malware SHA-1 Hash\u0027, results.scan.get(\u0027sha1\u0027), None)\n  \nif results.scan.get(\u0027sha256\u0027) is not None:\n  incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, results.scan.get(\u0027sha256\u0027), None)\n# domain results\n# {\u0027scan\u0027: {u\u0027domain_siblings\u0027: [], u\u0027BitDefender domain info\u0027: u\u0027This URL domain/host was seen to host badware at some point in time\u0027, u\u0027undetected_downloaded_samples\u0027: [], u\u0027whois\u0027: None, u\u0027detected_downloaded_samples\u0027: [], u\u0027response_code\u0027: 1, u\u0027verbose_msg\u0027: u\u0027Domain found in dataset\u0027, u\u0027Forcepoint ThreatSeeker category\u0027: u\u0027malicious web sites\u0027, u\u0027undetected_urls\u0027: [], u\u0027resolutions\u0027: [{u\u0027last_resolved\u0027: u\u00272017-12-04 19:48:01\u0027, u\u0027ip_address\u0027: u\u0027185.61.138.74\u0027}], u\u0027detected_urls\u0027: [{u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/\u0027, u\u0027positives\u0027: 7, u\u0027total\u0027: 67, u\u0027scan_date\u0027: u\u00272018-08-01 13:28:18\u0027}, {u\u0027url\u0027: u\u0027https://amazon-sicherheit.kunden-ueberpruefung.xyz/\u0027, u\u0027positives\u0027: 7, u\u0027total\u0027: 67, u\u0027scan_date\u0027: u\u00272018-06-06 21:49:59\u0027}, {u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/favicon.ico\u0027, u\u0027positives\u0027: 7, u\u0027total\u0027: 65, u\u0027scan_date\u0027: u\u00272017-07-16 02:19:48\u0027}, {u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/,http:/amazon-sicherheit,http:/amazon-sicherheit.kunden-ueberpruefung.xyz\u0027, u\u0027positives\u0027: 9, u\u0027total\u0027: 65, u\u0027scan_date\u0027: u\u00272017-06-14 07:52:22\u0027}, {u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/information/\u0027, u\u0027positives\u0027: 7, u\u0027total\u0027: 64, u\u0027scan_date\u0027: u\u00272017-06-12 13:42:45\u0027}, {u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/,http:/amazon-sicherheit/\u0027, u\u0027positives\u0027: 8, u\u0027total\u0027: 64, u\u0027scan_date\u0027: u\u00272017-05-21 09:01:11\u0027}, {u\u0027url\u0027: u\u0027http://amazon-sicherheit.kunden-ueberpruefung.xyz/,http:/amazon-sicherheit\u0027, u\u0027positives\u0027: 9, u\u0027total\u0027: 64, u\u0027scan_date\u0027: u\u00272017-05-18 06:46:46\u0027}], u\u0027categories\u0027: [u\u0027malicious web sites\u0027]}}\n# url results\n# {\u0027scan\u0027: {u\u0027permalink\u0027: u\u0027https://www.virustotal.com/url/518c9fe795d329ad2871dc8f003fba8ad6428ad7c936ec35da38b6f7f5e79f54/analysis/1533139178/\u0027, u\u0027resource\u0027: u\u0027http://frsc0016.geico.net:3000/\u0027, u\u0027url\u0027: u\u0027http://frsc0016.geico.net:3000/\u0027, u\u0027response_code\u0027: 1, u\u0027scan_date\u0027: u\u00272018-08-01 15:59:38\u0027, u\u0027scan_id\u0027: u\u0027518c9fe795d329ad2871dc8f003fba8ad6428ad7c936ec35da38b6f7f5e79f54-1533139178\u0027, u\u0027verbose_msg\u0027: u\u0027Scan request successfully queued, come back later for the report\u0027}}\n# {\u0027scan\u0027: {u\u0027permalink\u0027: u\u0027https://www.virustotal.com/url/518c9fe795d329ad2871dc8f003fba8ad6428ad7c936ec35da38b6f7f5e79f54/analysis/1533173246/\u0027, u\u0027resource\u0027: u\u0027http://frsc0016.geico.net:3000\u0027, u\u0027url\u0027: u\u0027http://frsc0016.geico.net:3000/\u0027, u\u0027response_code\u0027: 1, u\u0027scan_date\u0027: u\u00272018-08-02 01:27:26\u0027, u\u0027scan_id\u0027: u\u0027518c9fe795d329ad2871dc8f003fba8ad6428ad7c936ec35da38b6f7f5e79f54-1533173246\u0027, u\u0027verbose_msg\u0027: u\u0027Scan finished, scan information embedded in this object\u0027, u\u0027filescan_id\u0027: None, u\u0027positives\u0027: 0, u\u0027total\u0027: 67, u\u0027scans\u0027: {u\u0027CLEAN MX\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027DNS8\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027VX Vault\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ZDB Zeus\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Tencent\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027AutoShun\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027Netcraft\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027PhishLabs\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027Zerofox\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027K7AntiVirus\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Virusdie External Site Scan\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Quttera\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027AegisLab WebGuard\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027MalwareDomainList\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027, u\u0027detail\u0027: u\u0027http://www.malwaredomainlist.com/mdl.php?search=frsc0016.geico.net\u0027}, u\u0027ZeusTracker\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027, u\u0027detail\u0027: u\u0027https://zeustracker.abuse.ch/monitor.php?host=frsc0016.geico.net\u0027}, u\u0027zvelo\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Google Safebrowsing\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Kaspersky\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027BitDefender\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Dr.Web\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Certly\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027G-Data\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027C-SIRT\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027OpenPhish\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Malware Domain Blocklist\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027MalwarePatrol\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Webutation\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Trustwave\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Web Security Guard\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027CyRadar\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027desenmascara.me\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ADMINUSLabs\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Malwarebytes hpHosts\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Opera\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027AlienVault\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Emsisoft\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Malc0de Database\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027, u\u0027detail\u0027: u\u0027http://malc0de.com/database/index.php?search=frsc0016.geico.net\u0027}, u\u0027malwares.com URL checker\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Phishtank\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Malwared\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Avira\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027NotMining\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027CyberCrime\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Antiy-AVL\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Forcepoint ThreatSeeker\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027FraudSense\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Comodo Site Inspector\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Malekal\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ESET\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Sophos\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027Yandex Safebrowsing\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027, u\u0027detail\u0027: u\u0027http://yandex.com/infected?l10n=en\u0026url=http://frsc0016.geico.net:3000/\u0027}, u\u0027SecureBrain\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Nucleon\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Sucuri SiteCheck\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Blueliv\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ZCloudsec\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027SCUMWARE.org\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ThreatHive\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027FraudScore\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Rising\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027URLQuery\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027StopBadware\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027unrated site\u0027}, u\u0027Fortinet\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027ZeroCERT\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Spam404\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027securolytics\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}, u\u0027Baidu-International\u0027: {u\u0027detected\u0027: False, u\u0027result\u0027: u\u0027clean site\u0027}}}}\n# ip results\n# {\u0027scan\u0027: {u\u0027country\u0027: u\u0027CN\u0027, u\u0027response_code\u0027: 1, u\u0027as_owner\u0027: u\u0027CNCGROUP China169 Backbone\u0027, u\u0027verbose_msg\u0027: u\u0027IP address in dataset\u0027, u\u0027resolutions\u0027: [], u\u0027detected_urls\u0027: [], u\u0027asn\u0027: u\u00274837\u0027}}\n# {\u0027scan\u0027: {u\u0027asn\u0027: u\u002739743\u0027, u\u0027undetected_referrer_samples\u0027: [{u\u0027positives\u0027: 0, u\u0027total\u0027: 59, u\u0027sha256\u0027: u\u002725d6e157f52899bb80d76f2620fd3e40d94229147d718e77454539ae89b991c5\u0027}], u\u0027country\u0027: u\u0027RO\u0027, u\u0027response_code\u0027: 1, u\u0027as_owner\u0027: u\u0027Voxility S.R.L.\u0027, u\u0027detected_referrer_samples\u0027: [{u\u0027date\u0027: u\u00272018-03-01 12:23:54\u0027, u\u0027positives\u0027: 1, u\u0027total\u0027: 70, u\u0027sha256\u0027: u\u00272025815e09ab99c4abdec66402ee3cbaaaa13700fb7bc83e1ec5df2b9b40d7fa\u0027}], u\u0027verbose_msg\u0027: u\u0027IP address in dataset\u0027, u\u0027detected_urls\u0027: [{u\u0027url\u0027: u\u0027http://109.163.234.2/\u0027, u\u0027positives\u0027: 1, u\u0027total\u0027: 67, u\u0027scan_date\u0027: u\u00272018-07-23 03:40:50\u0027}, {u\u0027url\u0027: u\u0027http://109.163.234.2:443/\u0027, u\u0027positives\u0027: 1, u\u0027total\u0027: 67, u\u0027scan_date\u0027: u\u00272018-07-23 03:40:01\u0027}, {u\u0027url\u0027: u\u0027https://109.163.234.2/\u0027, u\u0027positives\u0027: 1, u\u0027total\u0027: 68, u\u0027scan_date\u0027: u\u00272016-08-10 10:23:09\u0027}], u\u0027detected_communicating_samples\u0027: [{u\u0027date\u0027: u\u00272017-04-02 03:37:37\u0027, u\u0027positives\u0027: 30, u\u0027total\u0027: 62, u\u0027sha256\u0027: u\u002731227cad8b8e9f154371eef25773a8b33ac1e067da188943cba1756e6551c612\u0027}, {u\u0027date\u0027: u\u00272014-06-15 11:08:54\u0027, u\u0027positives\u0027: 11, u\u0027total\u0027: 54, u\u0027sha256\u0027: u\u002721da33807c1bf3891ea6aa4163711970706a57facf5b4739ab3c5d55ed3e9775\u0027}], u\u0027resolutions\u0027: [{u\u0027last_resolved\u0027: u\u00272018-05-28 10:41:56\u0027, u\u0027hostname\u0027: u\u0027hessel0.torservers.net\u0027}]}}\n# hash results\n# {\u0027scan\u0027: {u\u0027scan_id\u0027: u\u00274e7267dd4ce5a0a780a836040f91e042dff0d8c0c5f26cb4dcb9ec6635265812-1493150616\u0027, u\u0027sha1\u0027: u\u0027cd9d22df6e8db01333f13e03422647551f191f8c\u0027, u\u0027resource\u0027: u\u0027cd9d22df6e8db01333f13e03422647551f191f8c\u0027, u\u0027response_code\u0027: 1, u\u0027scan_date\u0027: u\u00272017-04-25 20:03:36\u0027, u\u0027permalink\u0027: u\u0027https://www.virustotal.com/file/4e7267dd4ce5a0a780a836040f91e042dff0d8c0c5f26cb4dcb9ec6635265812/analysis/1493150616/\u0027, u\u0027verbose_msg\u0027: u\u0027Scan finished, information embedded\u0027, u\u0027sha256\u0027: u\u00274e7267dd4ce5a0a780a836040f91e042dff0d8c0c5f26cb4dcb9ec6635265812\u0027, u\u0027positives\u0027: 0, u\u0027total\u0027: 61, u\u0027md5\u0027: u\u002754562fe4ac3a071639d000512ecc6967\u0027, u\u0027scans\u0027: {u\u0027Bkav\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.3.0.8876\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027MicroWorld-eScan\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002712.0.250.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027nProtect\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272017-04-25.02\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027CMC\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.1.0.977\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170421\u0027}, u\u0027CAT-QuickHeal\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002714.00\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027ALYac\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.1.9\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Malwarebytes\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272.1.1.1115\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027VIPRE\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002757624\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027SUPERAntiSpyware\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.6.0.1032\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027TheHacker\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00276.8.0.5.1468\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170424\u0027}, u\u0027K7GW\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002710.9.23121\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027K7AntiVirus\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002710.9.23125\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Invincea\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00276.3.0.25213\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170413\u0027}, u\u0027Baidu\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170424\u0027}, u\u0027Cyren\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.4.30.7\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Symantec\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.3.0.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027ESET-NOD32\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002715311\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027TrendMicro-HouseCall\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00279.900.0.1004\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Paloalto\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027ClamAV\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00270.99.2.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Kaspersky\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002715.0.1.13\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027BitDefender\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00277.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027NANO-Antivirus\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.74.16482\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027AegisLab\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Avast\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00278.0.1489.320\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Tencent\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Ad-Aware\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00273.0.3.1010\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Emsisoft\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.0.0.834\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Comodo\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002726976\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027F-Secure\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002711.0.19100.45\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027DrWeb\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00277.0.28.2020\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Zillya\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272.0.0.3263\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027TrendMicro\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00279.740.0.1012\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027McAfee-GW-Edition\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u0027v2015\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Sophos\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.98.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Ikarus\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00270.1.5.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027F-Prot\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.7.1.166\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Jiangmin\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002716.0.100\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Webroot\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.207\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Avira\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00278.3.3.4\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Fortinet\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.4.233.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Antiy-AVL\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Kingsoft\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272013.8.14.323\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Endgame\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00270.4.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170419\u0027}, u\u0027Arcabit\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.802\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027ViRobot\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272014.3.20.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027ZoneAlarm\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Microsoft\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.1.13701.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027AhnLab-V3\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00273.9.0.17342\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027McAfee\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00276.0.6.653\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027AVware\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.5.0.42\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027VBA32\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00273.12.26.4\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170421\u0027}, u\u0027Zoner\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Rising\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002728.0.0.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Yandex\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.5.1.3\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170424\u0027}, u\u0027SentinelOne\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.154\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170330\u0027}, u\u0027GData\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u0027A:25.12056B:25.9393\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027AVG\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002716.0.0.4776\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}, u\u0027Panda\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.6.4.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170424\u0027}, u\u0027CrowdStrike\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170130\u0027}, u\u0027Qihoo-360\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.1120\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720170425\u0027}}}}\n# file scan\n# {\u0027scan\u0027: {u\u0027permalink\u0027: u\u0027https://www.virustotal.com/file/97be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a/analysis/1533171813/\u0027, u\u0027sha1\u0027: u\u00279a419d1a7d4a515d03db7f08fdd27e11ae896b11\u0027, u\u0027resource\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a\u0027, u\u0027response_code\u0027: 1, u\u0027scan_id\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a-1533171813\u0027, u\u0027verbose_msg\u0027: u\u0027Scan request successfully queued, come back later for the report\u0027, u\u0027sha256\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a\u0027, u\u0027md5\u0027: u\u0027d6e447ddcc6f74cac89322ff25e7835e\u0027}}\n# {\u0027scan\u0027: {u\u0027scan_id\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a-1533171813\u0027, u\u0027sha1\u0027: u\u00279a419d1a7d4a515d03db7f08fdd27e11ae896b11\u0027, u\u0027resource\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a\u0027, u\u0027response_code\u0027: 1, u\u0027scan_date\u0027: u\u00272018-08-02 01:03:33\u0027, u\u0027permalink\u0027: u\u0027https://www.virustotal.com/file/97be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a/analysis/1533171813/\u0027, u\u0027verbose_msg\u0027: u\u0027Scan finished, information embedded\u0027, u\u0027sha256\u0027: u\u002797be2d515e01ba66091148456b392f7539b43ab1ba412c493107e93aeda1536a\u0027, u\u0027positives\u0027: 48, u\u0027total\u0027: 68, u\u0027md5\u0027: u\u0027d6e447ddcc6f74cac89322ff25e7835e\u0027, u\u0027scans\u0027: {u\u0027Bkav\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.3.0.9466\u0027, u\u0027result\u0027: u\u0027HW32.Packed.C390\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027MicroWorld-eScan\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002714.0.297.0\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027CMC\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.1.0.977\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027CAT-QuickHeal\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002714.00\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027McAfee\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00276.0.6.653\u0027, u\u0027result\u0027: u\u0027RDN/Generic PUP.x\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Cylance\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00272.3.1.101\u0027, u\u0027result\u0027: u\u0027Unsafe\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Zillya\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272.0.0.3607\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027TheHacker\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00276.8.0.5.3467\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180730\u0027}, u\u0027K7GW\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002710.56.27942\u0027, u\u0027result\u0027: u\u0027Trojan ( 0051506d1 )\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027K7AntiVirus\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002710.56.27942\u0027, u\u0027result\u0027: u\u0027Trojan ( 0051506d1 )\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027TrendMicro\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002710.0.0.1040\u0027, u\u0027result\u0027: u\u0027TROJ_GEN.R002C0OCL18\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Baidu\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Babable\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00279107201\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180725\u0027}, u\u0027F-Prot\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.7.1.166\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Symantec\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.6.0.0\u0027, u\u0027result\u0027: u\u0027PUA.Gen.2\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027TotalDefense\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u002737.1.62.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027TrendMicro-HouseCall\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00279.950.0.1006\u0027, u\u0027result\u0027: u\u0027TROJ_GEN.R002C0OCL18\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Avast\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002718.4.3895.0\u0027, u\u0027result\u0027: u\u0027Win32:Malware-gen\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027ClamAV\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00270.100.1.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027GData\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u0027A:25.17963B:25.12867\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Kaspersky\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002715.0.1.13\u0027, u\u0027result\u0027: u\u0027not-a-virus:HEUR:RiskTool.Win32.Generic\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027BitDefender\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00277.2\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027NANO-Antivirus\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0.116.23366\u0027, u\u0027result\u0027: u\u0027Riskware.Win32.Mlw.eyrsjw\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027ViRobot\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00272014.3.20.0\u0027, u\u0027result\u0027: u\u0027Trojan.Win32.S.Agent.710144.I\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027AegisLab\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00274.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Rising\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002725.0.0.24\u0027, u\u0027result\u0027: u\u0027Trojan.Azden!8.F0E3 (CLOUD)\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Ad-Aware\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00273.0.5.370\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Sophos\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00274.98.0\u0027, u\u0027result\u0027: u\u0027Generic PUA JK (PUA)\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Comodo\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002729451\u0027, u\u0027result\u0027: u\u0027ApplicUnwnt\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027F-Secure\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002711.0.19100.45\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027DrWeb\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00277.0.33.6080\u0027, u\u0027result\u0027: u\u0027Trojan.KeyLogger.40115\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027VIPRE\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002768554\u0027, u\u0027result\u0027: u\u0027Trojan.Win32.Generic!BT\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Invincea\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00276.3.5.26121\u0027, u\u0027result\u0027: u\u0027heuristic\u0027, u\u0027update\u0027: u\u002720180717\u0027}, u\u0027McAfee-GW-Edition\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u0027v2017.3010\u0027, u\u0027result\u0027: u\u0027BehavesLike.Win32.Ramnit.jc\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Emsisoft\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00272018.4.0.1029\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884 (B)\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Ikarus\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00270.1.5.2\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Cyren\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00276.0.0.4\u0027, u\u0027result\u0027: u\u0027W32/Trojan.FSWK-1704\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Jiangmin\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002716.0.100\u0027, u\u0027result\u0027: u\u0027RiskTool.Agent.wc\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Webroot\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0.0.403\u0027, u\u0027result\u0027: u\u0027W32.Malware.Gen\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Avira\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00278.3.3.6\u0027, u\u0027result\u0027: u\u0027HEUR/AGEN.1000279\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027MAX\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272017.11.15.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Antiy-AVL\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00273.0.0.1\u0027, u\u0027result\u0027: u\u0027RiskWare[RiskTool]/Win32.Agent\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Kingsoft\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00272013.8.14.323\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Endgame\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00273.0.1\u0027, u\u0027result\u0027: u\u0027malicious (high confidence)\u0027, u\u0027update\u0027: u\u002720180730\u0027}, u\u0027Arcabit\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.831\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027SUPERAntiSpyware\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.6.0.1032\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027ZoneAlarm\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: u\u0027not-a-virus:HEUR:RiskTool.Win32.Generic\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Avast-Mobile\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u0027180801-02\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Microsoft\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.1.15100.1\u0027, u\u0027result\u0027: u\u0027PUA:Win32/Presenoker\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027AhnLab-V3\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00273.13.1.21616\u0027, u\u0027result\u0027: u\u0027Malware/Gen.Generic.C2426212\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027ALYac\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.1.1.5\u0027, u\u0027result\u0027: u\u0027Adware.GenericKD.30431884\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027AVware\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.6.0.52\u0027, u\u0027result\u0027: u\u0027Trojan.Win32.Generic!BT\u0027, u\u0027update\u0027: u\u002720180727\u0027}, u\u0027TACHYON\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00272018-08-01.02\u0027, u\u0027result\u0027: u\u0027Trojan/W32.CoinMiner.710144\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027VBA32\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00273.12.32.0\u0027, u\u0027result\u0027: u\u0027Trojan.Keyloggerger\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Malwarebytes\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00272.1.1.1115\u0027, u\u0027result\u0027: u\u0027Trojan.MalPack\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Panda\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00274.6.4.2\u0027, u\u0027result\u0027: u\u0027Trj/GdSda.A\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Zoner\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027ESET-NOD32\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002717814\u0027, u\u0027result\u0027: u\u0027a variant of Win32/Packed.Autoit.X suspicious\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Tencent\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00271.0.0.1\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Yandex\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00275.5.1.3\u0027, u\u0027result\u0027: u\u0027Riskware.Agent!\u0027, u\u0027update\u0027: u\u002720180731\u0027}, u\u0027SentinelOne\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0.17.227\u0027, u\u0027result\u0027: u\u0027static engine - malicious\u0027, u\u0027update\u0027: u\u002720180701\u0027}, u\u0027eGambit\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: None, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027Fortinet\u0027: {u\u0027detected\u0027: False, u\u0027version\u0027: u\u00275.4.247.0\u0027, u\u0027result\u0027: None, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027AVG\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u002718.4.3895.0\u0027, u\u0027result\u0027: u\u0027Win32:Malware-gen\u0027, u\u0027update\u0027: u\u002720180801\u0027}, u\u0027Cybereason\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.2.27\u0027, u\u0027result\u0027: u\u0027malicious.a7d4a5\u0027, u\u0027update\u0027: u\u002720180225\u0027}, u\u0027Paloalto\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: u\u0027generic.ml\u0027, u\u0027update\u0027: u\u002720180802\u0027}, u\u0027CrowdStrike\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0\u0027, u\u0027result\u0027: u\u0027malicious_confidence_100% (D)\u0027, u\u0027update\u0027: u\u002720180723\u0027}, u\u0027Qihoo-360\u0027: {u\u0027detected\u0027: True, u\u0027version\u0027: u\u00271.0.0.1120\u0027, u\u0027result\u0027: u\u0027Win32/Virus.RiskTool.734\u0027, u\u0027update\u0027: u\u002720180802\u0027}}}}",
          "tags": [],
          "uuid": "a4feb482-12fb-4a48-b09b-a68f1a227daf"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "virustotal_scan_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8d6fda2b-f434-4735-956c-0bc347ed1757",
        "id": 64,
        "name": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
        "type": "playbook",
        "uuid": "cb51a1e8-df6a-44e3-8d37-1947f378cf83"
      },
      "tags": [],
      "type": "default",
      "uuid": "8d6fda2b-f434-4735-956c-0bc347ed1757",
      "version": 5
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 7899,
    "major": 45,
    "minor": 0,
    "version": "45.0.7899"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
