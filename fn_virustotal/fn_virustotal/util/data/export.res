{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1684870752729,
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
      "id": 273,
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
      "id": 274,
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
      "id": 275,
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
      "id": 276,
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
      "id": 277,
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
      "created_date": 1682427075191,
      "description": {
        "content": "perform scans and return reports on ip addresses, urls, domains, hashes and files",
        "format": "text"
      },
      "destination_handle": "fn_virustotal",
      "display_name": "VirusTotal",
      "export_key": "virustotal",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1684182121858,
      "name": "virustotal",
      "tags": [],
      "uuid": "d108590a-21f9-4e42-92c4-d2a6fe39c9b4",
      "version": 3,
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
          "name": "VirusTotal Scan Hits",
          "object_type": "artifact",
          "programmatic_name": "virustotal_scan_hits",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 82,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1684870750860,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1684870750860,
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
        "content_version": 75,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\" isExecutable=\"true\" name=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qvbax8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"VirusTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d108590a-21f9-4e42-92c4-d2a6fe39c9b4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"typeLookup = { \u0027Email Attachment\u0027: \u0027file\u0027, \u0027Malware Sample\u0027: \u0027file\u0027, \u0027Malware MD5 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-1 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-256 Hash\u0027: \u0027hash\u0027, \u0027Other File\u0027: \u0027file\u0027, \u0027RCF 822 Email Message Fife\u0027: \u0027file\u0027, \u0027File Name\u0027: \u0027filename\u0027,\\n \u0027URL\u0027: \u0027url\u0027, \u0027IP Address\u0027: \u0027ip\u0027, \u0027DNS Name\u0027:\u0027domain\u0027}\\nif artifact.type in typeLookup:\\n  inputs.vt_type = typeLookup.get(artifact.type, artifact.type)\\nelse:\\n  inputs.vt_type = artifact.type\\n\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\ninputs.vt_data = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"vt_scan_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qvbax8\u003c/incoming\u003e\u003coutgoing\u003eFlow_12ot3ft\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qvbax8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"VirusTotal: Write artifact scan to a note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a4feb482-12fb-4a48-b09b-a68f1a227daf\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12ot3ft\u003c/incoming\u003e\u003coutgoing\u003eFlow_1yh0cma\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_12ot3ft\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1yh0cma\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1yh0cma\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8d6fda2b_f434_4735_956c_0bc347ed1757\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1yh0cma\" id=\"Flow_1yh0cma_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12ot3ft\" id=\"Flow_12ot3ft_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qvbax8\" id=\"Flow_0qvbax8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168.35000610351562\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318.3500061035156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"474.3500061035156\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1682427075680,
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
      "display_name": "Example VirusTotal: Scan Artifact (PB)",
      "export_key": "virustotal_scan_artifact",
      "field_type_handle": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
      "fields_type": {
        "actions": [],
        "display_name": "Example VirusTotal: Scan Artifact (PB)",
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
      "id": 1,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1684779174231,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1682427075786,
          "description": "Write VirusTotal scan results to an incident note.",
          "enabled": false,
          "export_key": "VirusTotal: Write artifact scan to a note",
          "id": 2,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1684780197352,
          "name": "VirusTotal: Write artifact scan to a note",
          "object_type": "artifact",
          "playbook_handle": "virustotal_scan_artifact",
          "programmatic_name": "virustotal_scan_artifact_virustotal_write_artifact_scan_to_a_note",
          "script_text": "import datetime\nimport json\n\nresults = playbook.functions.results.vt_scan_results\n\n# Uncomment the following line to have the results json printed formatted to a note.\n#pretty_results = json.dumps(results, indent=4, sort_keys=True)\n#incident.addNote(helper.createRichText(u\"\u003cp\u003eVirusTotal scan of {0}: {1}\u003c/p\u003e\u003cdiv\u003e{2}\u003c/div\u003e\".format(artifact.type, artifact.value, pretty_results)))\n\nmsg = u\"\u003cp\u003eVirusTotal scan of {0}: \u003cb\u003e{1}\u003c/b\u003e\u003c/p\u003e\".format(artifact.type, artifact.value)\nscan = results.get(\"scan\",  {})\nif not scan:\n  raise Exception(\"No scan data returned VirusTotal scan {0}: {1}\".format(artifact.type, artifact.value))   \n\ndata = scan.get(\"data\", {})\nscan_error = scan.get(\"error\", {})\nif scan_error:\n  msg = \"{0}Error returned: {1}\".format(msg, scan_error)\n  #helper.fail(\"Error returned from VirusTotal scan {0}: {1}: {2}\".format(artifact.type, artifact.value, scan_error))\n\nstats = {}\nattributes = {}\nif data:\n  attributes = data.get(\"attributes\", {})\n  if attributes:\n    # If this a report the stats are in last_analysis_stats otherwise they are in stats\n    stats = attributes.get(\"last_analysis_stats\", {})\n    if stats == {}:\n\t    stats = attributes.get(\"stats\", {})\n\nfor k,v in stats.items():\n  if k.lower() == \"malicious\":\n    msg = \"{0}{1}: \u003cspan style=\u0027color:red\u0027\u003e{2}\u003c/span\u003e\u003cbr\u003e\".format(msg, k, v)\n  else:\n    msg = \"{0}{1}: {2}\u003cbr\u003e\".format(msg, k, v)\n    \nlast_analysis_date = attributes.get(\"last_analysis_date\", None)\nif last_analysis_date:\n  last_analysis_date_str = datetime.datetime.fromtimestamp(last_analysis_date).strftime(\u0027%Y-%b-%d %H:%M:%S\u0027)\n  msg = \"{0}\u003cp\u003eLast analysis date: {1}\u003c/p\u003e\"\"\".format(msg, last_analysis_date_str)\n    \nif stats == {}:\n  msg = \"{0}No stats returned from scan {1}: {2}\".format(msg, artifact.type, artifact.value)  \n\nincident.addNote(helper.createRichText(\"\u003cdiv\u003e{0}\u003c/div\u003e\".format(msg)))\n\n# Create artifacts from results\nlast_http_response_content_sha256 = attributes.get(\"last_http_response_content_sha256\", None)\nif last_http_response_content_sha256:\n    incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, last_http_response_content_sha256, \"Created by VirusTotal scan of artifact type: {0} value: {1}\".format(artifact.type, artifact.value))\n\nsha256 = attributes.get(\"sha256\", None) \nif sha256:\n    incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, sha256, \"Created by VirusTotal scan of artifact type: {0} value: {1}\".format(artifact.type, artifact.value))\n\nmd5 = attributes.get(\"md5\", None)\nif md5:\n    incident.addArtifact(\u0027Malware MD5 Hash\u0027, md5, \"Created by VirusTotal scan of artifact type: {0} value: {1}\".format(artifact.type, artifact.value))\n\nsha1 = attributes.get(\"sha1\", None)\nif sha1:\n    incident.addArtifact(\u0027Malware SHA-1 Hash\u0027, sha1, \"Created by VirusTotal scan of artifact type: {0} value: {1}\".format(artifact.type, artifact.value))\n    ",
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
        "id": 1,
        "name": "playbook_8d6fda2b_f434_4735_956c_0bc347ed1757",
        "type": "playbook",
        "uuid": "cb51a1e8-df6a-44e3-8d37-1947f378cf83"
      },
      "tags": [],
      "type": "default",
      "uuid": "8d6fda2b-f434-4735-956c-0bc347ed1757",
      "version": 81
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 17,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_4aea219b_1665_43ff_ab82_c868d727f22d\" isExecutable=\"true\" name=\"playbook_4aea219b_1665_43ff_ab82_c868d727f22d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1doyyap\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"VirusTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d108590a-21f9-4e42-92c4-d2a6fe39c9b4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.vt_type = \u0027file\u0027\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\ninputs.artifact_id = None\\ninputs.vt_data = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"vt_scan_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1doyyap\u003c/incoming\u003e\u003coutgoing\u003eFlow_043blo8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1doyyap\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"VirusTotal: Write results to an incident note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"b06ebeef-e1e1-42b0-bdfc-39fd6a3aeeb8\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_043blo8\u003c/incoming\u003e\u003coutgoing\u003eFlow_1em35q0\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1em35q0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1em35q0\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_043blo8\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_4aea219b_1665_43ff_ab82_c868d727f22d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_043blo8\" id=\"Flow_043blo8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1em35q0\" id=\"Flow_1em35q0_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"464\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1doyyap\" id=\"Flow_1doyyap_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.017\" x=\"616\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"464\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1682440851511,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_4aea219b_1665_43ff_ab82_c868d727f22d",
      "description": {
        "content": "Perform a VirusTotal scan against an attachment.  Write the results to a note.",
        "format": "text"
      },
      "display_name": "Example VirusTotal: Scan Attachment (PB)",
      "export_key": "virustotal_scan_attachment",
      "field_type_handle": "playbook_4aea219b_1665_43ff_ab82_c868d727f22d",
      "fields_type": {
        "actions": [],
        "display_name": "Example VirusTotal: Scan Attachment (PB)",
        "export_key": "playbook_4aea219b_1665_43ff_ab82_c868d727f22d",
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
        "type_name": "playbook_4aea219b_1665_43ff_ab82_c868d727f22d",
        "uuid": "23374c58-8923-427d-ac3d-5b8eb1d81d3c"
      },
      "has_logical_errors": false,
      "id": 2,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1684855791475,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1682440988908,
          "description": "Write the results of an VirusTotal scan of an attachment to a note.",
          "enabled": false,
          "export_key": "VirusTotal: Write results to an incident note",
          "id": 3,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1684855788469,
          "name": "VirusTotal: Write results to an incident note",
          "object_type": "attachment",
          "playbook_handle": "virustotal_scan_attachment",
          "programmatic_name": "virustotal_scan_attachment_virustotal_write_results_to_an_incident_note",
          "script_text": "import datetime\nimport json\n\nresults = playbook.functions.results.vt_scan_results\n\n# Uncomment the following line to have the results json printed formatted to a note.\n#pretty_results = json.dumps(results, indent=4, sort_keys=True)\n#incident.addNote(helper.createRichText(u\"\u003cp\u003eVirusTotal scan of attachment: {0}\u003c/p\u003e\u003cdiv\u003e{1}\u003c/div\u003e\".format(attachment.name, pretty_results)))\n\nmsg = u\"\u003cp\u003eVirusTotal scan of Attachment: \u003cb\u003e{0}\u003c/b\u003e\u003c/p\u003e\".format(attachment.name)\nscan = results.get(\"scan\",  {})\nif not scan:\n  raise Exception(\"No scan data returned VirusTotal scan on attachment: {0}\".format(attachment.name))   \n\ndata = scan.get(\"data\", {})\nscan_error = scan.get(\"error\", {})\nif scan_error:\n  msg = \"{0}Error returned: {1}\".format(msg, scan_error)\n  #helper.fail(\"Error returned from VirusTotal scan of attachment: {0}: {1}\".format(attachment.name, scan_error))\n\nstats = {}\nattributes = {}\nif data:\n  attributes = data.get(\"attributes\", {})\n  if attributes:\n    # If this a report the stats are in last_analysis_stats otherwise they are in stats\n    stats = attributes.get(\"last_analysis_stats\", {})\n    if stats == {}:\n\t    stats = attributes.get(\"stats\", {})\n\nfor k,v in stats.items():\n  if k.lower() == \"malicious\":\n    msg = \"{0}{1}: \u003cspan style=\u0027color:red\u0027\u003e{2}\u003c/span\u003e\u003cbr\u003e\".format(msg, k, v)\n  else:\n    msg = \"{0}{1}: {2}\u003cbr\u003e\".format(msg, k, v)\n    \nlast_analysis_date = attributes.get(\"last_analysis_date\", None)\nif last_analysis_date:\n  last_analysis_date_str = datetime.datetime.fromtimestamp(last_analysis_date).strftime(\u0027%Y-%b-%d %H:%M:%S\u0027)\n  msg = \"{0}\u003cp\u003eLast analysis date: {1}\u003c/p\u003e\"\"\".format(msg, last_analysis_date_str)\n    \nif stats == {}:\n  msg = \"{0}No stats returned from scan attachment: {1}\".format(msg, attachment.name)  \n\nincident.addNote(helper.createRichText(\"\u003cdiv\u003e{0}\u003c/div\u003e\".format(msg)))\n\n# Create artifacts from results\nlast_http_response_content_sha256 = attributes.get(\"last_http_response_content_sha256\", None)\nif last_http_response_content_sha256:\n    incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, last_http_response_content_sha256, \"Created by VirusTotal scan of attachment {0}\".format(attachment.name))\n\nsha256 = attributes.get(\"sha256\", None) \nif sha256:\n    incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, sha256, \"Created by VirusTotal scan of of attachment {0}\".format(attachment.name))\n\nmd5 = attributes.get(\"md5\", None)\nif md5:\n    incident.addArtifact(\u0027Malware MD5 Hash\u0027, md5, \"Created by VirusTotal scan of of attachment {0}\".format(attachment.name))\n\nsha1 = attributes.get(\"sha1\", None)\nif sha1:\n    incident.addArtifact(\u0027Malware SHA-1 Hash\u0027, sha1, \"Created by VirusTotal scan of of attachment {0}\".format(attachment.name))\n    \n",
          "tags": [],
          "uuid": "b06ebeef-e1e1-42b0-bdfc-39fd6a3aeeb8"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "virustotal_scan_attachment",
      "object_type": "attachment",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_4aea219b-1665-43ff-ab82-c868d727f22d",
        "id": 2,
        "name": "playbook_4aea219b_1665_43ff_ab82_c868d727f22d",
        "type": "playbook",
        "uuid": "7d50df75-fd2c-409f-a8dd-3add5551c5f5"
      },
      "tags": [],
      "type": "default",
      "uuid": "4aea219b-1665-43ff-ab82-c868d727f22d",
      "version": 23
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "DNS Name"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "IP Address"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Malware MD5 Hash"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Malware SHA-256 Hash"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "URL"
            }
          ],
          "logic_type": "any"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 14,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e\" isExecutable=\"true\" name=\"playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_10ys58q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"VirusTotal\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d108590a-21f9-4e42-92c4-d2a6fe39c9b4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"typeLookup = { \u0027Email Attachment\u0027: \u0027file\u0027, \u0027Malware Sample\u0027: \u0027file\u0027, \u0027Malware MD5 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-1 Hash\u0027: \u0027hash\u0027, \u0027Malware SHA-256 Hash\u0027: \u0027hash\u0027, \u0027Other File\u0027: \u0027file\u0027, \u0027RCF 822 Email Message Fife\u0027: \u0027file\u0027, \u0027File Name\u0027: \u0027filename\u0027,\\n \u0027URL\u0027: \u0027url\u0027, \u0027IP Address\u0027: \u0027ip\u0027, \u0027DNS Name\u0027:\u0027domain\u0027}\\nif artifact.type in typeLookup:\\n  inputs.vt_type = typeLookup.get(artifact.type, artifact.type)\\nelse:\\n  inputs.vt_type = artifact.type\\n\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\ninputs.vt_data = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"vt_scan_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_10ys58q\u003c/incoming\u003e\u003coutgoing\u003eFlow_0nybqro\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_10ys58q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"VirusTotal: Create artifact hits\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f739be17-e9d4-4ccc-b889-d0fe0215f4d0\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0nybqro\u003c/incoming\u003e\u003coutgoing\u003eFlow_0iw8kar\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0nybqro\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0iw8kar\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0iw8kar\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0iw8kar\" id=\"Flow_0iw8kar_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"484\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0nybqro\" id=\"Flow_0nybqro_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_10ys58q\" id=\"Flow_10ys58q_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"484\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1682453595198,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e",
      "description": {
        "content": "Perform automatic lookups for artifacts including IP addresses, hashes, domains, and URLS and creates a hit for the artifact if it is deemed potentially malicious by VirusTotal.",
        "format": "text"
      },
      "display_name": "Example VirusTotal: Scan Hits (PB)",
      "export_key": "virustotal_scan_hits",
      "field_type_handle": "playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e",
      "fields_type": {
        "actions": [],
        "display_name": "Example VirusTotal: Scan Hits (PB)",
        "export_key": "playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e",
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
        "type_name": "playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e",
        "uuid": "12c0652f-0c9e-4c53-9b62-5a8f2636ea6e"
      },
      "has_logical_errors": false,
      "id": 3,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1684269408713,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1682454020006,
          "description": "Create artifact hits on artifacts the VirusTotal has deemed malicious. Created malware hash artifacts if found in the VT scan data results.",
          "enabled": false,
          "export_key": "VirusTotal: Create artifact hits",
          "id": 4,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1682534335868,
          "name": "VirusTotal: Create artifact hits",
          "object_type": "artifact",
          "playbook_handle": "virustotal_scan_hits",
          "programmatic_name": "virustotal_scan_hits_virustotal_create_artifact_hits",
          "script_text": "results = playbook.functions.results.vt_scan_results\n\nif results:\n  scan = results.get(\"scan\", None)\n  if scan is not None and scan.get(\"data\", None) is not None:\n    data = scan.get(\"data\", None)\n    attributes = data.get(\"attributes\", None)\n    if attributes is not None:\n      last_analysis_stats = attributes.get(\"last_analysis_stats\", None)\n      if last_analysis_stats is not None:\n        malicious = last_analysis_stats.get(\"malicious\", None)\n        if malicious is not None and malicious \u003e 0:\n          hit = [\n            {\n              \"name\": \"Artifact Value\",\n              \"type\": \"string\",\n              \"value\": \"{}\".format(artifact.value)\n            }\n          ]\n          artifact.addHit(\"VirusTotal hits added.\", hit)\n          if attributes.get(\"last_http_response_content_sha256\", None) is not None:\n            incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, attributes.get(\"last_http_response_content_sha256\", None), \"Created by VirusTotal.\")\n            \n          if attributes.get(\u0027md5\u0027, None) is not None:\n            incident.addArtifact(\u0027Malware MD5 Hash\u0027, attributes.get(\u0027md5\u0027), \"Created by VirusTotal.\")\n  \n          if attributes.get(\u0027sha1\u0027, None) is not None:\n            incident.addArtifact(\u0027Malware SHA-1 Hash\u0027, attributes.get(\u0027sha1\u0027), \"Created by VirusTotal.\")\n    \n          if attributes.get(\u0027sha256\u0027, None) is not None:\n            incident.addArtifact(\u0027Malware SHA-256 Hash\u0027, attributes.get(\u0027sha256\u0027), \"Created by VirusTotal.\")\n        else:\n          incident.addNote(\u0027VirusTotal has not found a hit.\u0027)\n      else:\n        incident.addNote(\u0027VirusTotal has failed. - no last_analysis_stats\u0027)\n    else:\n      incident.addNote(\u0027VirusTotal has failed - no attributes.\u0027)\n  else:\n    incident.addNote(\u0027VirusTotal has failed - no data.\u0027)\nelse:\n  incident.addNote(\u0027VirusTotal has failed - no results.\u0027)\n      ",
          "tags": [],
          "uuid": "f739be17-e9d4-4ccc-b889-d0fe0215f4d0"
        }
      ],
      "name": "virustotal_scan_hits",
      "object_type": "artifact",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_eff2d4c0-cdb2-4b4c-825b-347c357cf05e",
        "id": 3,
        "name": "playbook_eff2d4c0_cdb2_4b4c_825b_347c357cf05e",
        "type": "playbook",
        "uuid": "6fd8cf7a-e50c-489b-8fa2-149653a8bbe6"
      },
      "tags": [],
      "type": "default",
      "uuid": "eff2d4c0-cdb2-4b4c-825b-347c357cf05e",
      "version": 22
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 8131,
    "major": 46,
    "minor": 0,
    "version": "46.0.8131"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
