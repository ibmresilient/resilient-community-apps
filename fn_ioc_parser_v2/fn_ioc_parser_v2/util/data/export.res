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
            "RFC 822 Email Message File",
            "Email Attachment",
            "Log File",
            "Other File",
            "String"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Parse IOCs (Artifact)",
      "id": 484,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Parse IOCs (Artifact)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b5ce45d0-b552-4bb7-8d4b-44ca1ff72280",
      "view_items": [],
      "workflows": [
        "example_parse_iocs_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Parse IOCs (Attachment)",
      "id": 485,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Parse IOCs (Attachment)",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6ef0b401-f98d-43a3-b8e0-a29086bfd1e8",
      "view_items": [],
      "workflows": [
        "example_parse_iocs_attachment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1743512734733,
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
      "export_key": "__function/ioc_parser_v2_incident_id",
      "hide_notification": false,
      "id": 3433,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ioc_parser_v2_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ioc_parser_v2_incident_id",
      "tooltip": "ID of the incident",
      "type_id": 11,
      "uuid": "dcc9c884-2742-4f17-a0de-5624b68b7b13",
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
      "export_key": "__function/ioc_parser_v2_artifact_id",
      "hide_notification": false,
      "id": 3432,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ioc_parser_v2_artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ioc_parser_v2_artifact_id",
      "tooltip": "ID of the artifact",
      "type_id": 11,
      "uuid": "ded90d15-4521-45d3-9c4a-2b17a42e97ec",
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
      "export_key": "__function/ioc_parser_v2_artifact_value",
      "hide_notification": false,
      "id": 3430,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ioc_parser_v2_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ioc_parser_v2_artifact_value",
      "tooltip": "Artifact\u0027s value",
      "type_id": 11,
      "uuid": "161c3359-e7e3-4b49-b34c-6f390126a9d1",
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
      "export_key": "__function/ioc_parser_v2_task_id",
      "hide_notification": false,
      "id": 3429,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ioc_parser_v2_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ioc_parser_v2_task_id",
      "tooltip": "ID of the task",
      "type_id": 11,
      "uuid": "5abc8ade-a2de-4ca4-8538-ecc4a54152d3",
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
      "export_key": "__function/ioc_parser_v2_attachment_id",
      "hide_notification": false,
      "id": 3431,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ioc_parser_v2_attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ioc_parser_v2_attachment_id",
      "tooltip": "ID of the attachment",
      "type_id": 11,
      "uuid": "6e64cb91-9a9e-48d5-9f08-f489be54c30b",
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
      "created_date": 1743502214747,
      "description": {
        "content": "Extract IOCs from incident/task/artifact attachments, and string-based artifacts.",
        "format": "text"
      },
      "destination_handle": "fn_ioc_parser_v2",
      "display_name": "IOC Parser v2",
      "export_key": "func_ioc_parser_v2",
      "id": 328,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743502214747,
      "name": "func_ioc_parser_v2",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "52803581-019a-4c68-8f8d-8be9ca31b2f6",
      "version": 0,
      "view_items": [
        {
          "content": "dcc9c884-2742-4f17-a0de-5624b68b7b13",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ded90d15-4521-45d3-9c4a-2b17a42e97ec",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "161c3359-e7e3-4b49-b34c-6f390126a9d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6e64cb91-9a9e-48d5-9f08-f489be54c30b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5abc8ade-a2de-4ca4-8538-ecc4a54152d3",
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
          "name": "Parse IOCs (Artifact)",
          "object_type": "artifact",
          "programmatic_name": "example_parse_iocs_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 450
        },
        {
          "actions": [],
          "description": null,
          "name": "Parse IOCs (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_parse_iocs_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 449
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 100,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1743512732206,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1743512732206,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "5c1294bd-eb54-45d7-be71-96fc1726b85f"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_ioc_parser_v2",
      "name": "fn_ioc_parser_v2",
      "programmatic_name": "fn_ioc_parser_v2",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "377ecd3d-de87-48a4-89ff-a626cb78a401"
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
        "version": 4,
        "workflow_id": "example_parse_iocs_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_iocs_attachment\" isExecutable=\"true\" name=\"Parse IOCs (Attachment)\"\u003e\u003cdocumentation\u003eExample workflow showing how to extract IOC\u0027s (Indicators of Compromise) from Incident/Task Attachments. Each unique IOC is added to the Incident as an Artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0hbjx6m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qbn70o\" name=\"IOC Parser v2\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"52803581-019a-4c68-8f8d-8be9ca31b2f6\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\ndef get_artifact_type(artifact_value, artifact_type):\\n  \\\"\\\"\\\"Use some regex expressions to try and identify\\n  from the Artifact\u0027s value, what Artifact type it is.\\n  Return original artifact_type if we cannot figure it out\\\"\\\"\\\"\\n\\n  dns_name_regex = re.compile(r\u0027^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\\\\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\\\\.[a-zA-Z]{2,3})$\u0027)\\n  \\n  if re.match(dns_name_regex, artifact_value):\\n    return \\\"DNS Name\\\"\\n  \\n  return artifact_type\\n\\n# Map ioc.type to Resilient Artifact Type\\nioc_type_to_artifact_type_map = {\\n    \u0027uri\u0027: \u0027URI Path\u0027,\\n    \u0027IP\u0027: \u0027IP Address\u0027,\\n    \u0027md5\u0027: \u0027Malware MD5 Hash\u0027,\\n    \u0027sha1\u0027: \u0027Malware SHA-1 Hash\u0027,\\n    \u0027sha256\u0027: \u0027Malware SHA-256 Hash\u0027,\\n    \u0027CVE\u0027: \u0027Threat CVE ID\u0027,\\n    \u0027email\u0027: \u0027Email Sender\u0027,\\n    \u0027filename\u0027: \u0027File Name\u0027,\\n    \u0027file\u0027: \u0027File Name\u0027\\n}\\n\\n# Get the IOCs\\niocs = results.iocs\\n\\nartifact_list = []\\nif iocs:\\n    # Loop IOCs and add each on as an Artifact\\n    for ioc in iocs:\\n      \\n      # If attachment_file_name is not defined, use the ioc.value as in the Artifact\u0027s Description\\n      if results.attachment_file_name:\\n        artifact_description = \\\"This IOC occurred {0} time(s) in the attachment: {1}\\\".format(ioc.get(\u0027count\u0027), results.attachment_file_name)\\n      \\n      else:\\n        artifact_description = \\\"This IOC occurred {0} time(s) in the attachment: {1}\\\".format(ioc.get(\u0027count\u0027), ioc.get(\u0027value\u0027))\\n\\n      artifact_value = ioc.get(\u0027value\u0027)\\n      artifact_type = ioc_type_to_artifact_type_map.get(ioc.get(\u0027type\u0027), \\\"String\\\")\\n      \\n      # If the artifact_type is \u0027URI Path\u0027, call get_artifact_type to try intentify the type using regex\\n      if artifact_type == \\\"URI Path\\\":\\n        artifact_type = get_artifact_type(artifact_value, artifact_type)\\n      \\n      incident.addArtifact(artifact_type, artifact_value, artifact_description)\\n      artifact_list.append(\\\"{}: {}\\\".format(artifact_type, artifact_value))\\n      \\n\\nif artifact_list:\\n  msg = \\\"The following artifacts were added from {}attachment: {}\\\\n{}\\\".format(\\\"Task \\\" if task else \\\"\\\", results.attachment_file_name, \\\"\\\\n\\\".join(artifact_list))\\nelse:\\n  msg = \\\"No artifacts were added from {}attachment: {}\\\\n{}\\\".format(\\\"Task \\\" if task else \\\"\\\", results.attachment_file_name, \\\"\\\\n\\\".join(artifact_list))\\n  \\nincident.addNote(msg)\\nif task:\\n  task.addNote(msg)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Define Pre-Process Inputs\\ninputs.ioc_parser_v2_incident_id = incident.id\\ninputs.ioc_parser_v2_attachment_id = attachment.id\\n\\n# If this is a Task, set the Task ID\\nif task:\\n     inputs.ioc_parser_v2_task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hbjx6m\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0eyqcql\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_14pmxvf\"\u003e\u003cincoming\u003eSequenceFlow_0eyqcql\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0eyqcql\" sourceRef=\"ServiceTask_1qbn70o\" targetRef=\"EndEvent_14pmxvf\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0hbjx6m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qbn70o\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0tnk96p\"\u003e\u003ctext\u003eArtifacts added to the incident from the artifact file. A note is created with summary information\n.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0cu95sl\" sourceRef=\"ServiceTask_1qbn70o\" targetRef=\"TextAnnotation_0tnk96p\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"179\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"174\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qbn70o\" id=\"ServiceTask_1qbn70o_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"329\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_14pmxvf\" id=\"EndEvent_14pmxvf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"529\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"547\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0eyqcql\" id=\"SequenceFlow_0eyqcql_di\"\u003e\u003comgdi:waypoint x=\"429\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"529\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"479\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hbjx6m\" id=\"SequenceFlow_0hbjx6m_di\"\u003e\u003comgdi:waypoint x=\"215\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"329\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"272\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0tnk96p\" id=\"TextAnnotation_0tnk96p_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"208\" x=\"410\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0cu95sl\" id=\"Association_0cu95sl_di\"\u003e\u003comgdi:waypoint x=\"425\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"479\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Example workflow showing how to extract IOC\u0027s (Indicators of Compromise) from Incident/Task Attachments. Each unique IOC is added to the Incident as an Artifact",
      "export_key": "example_parse_iocs_attachment",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743512658107,
      "name": "Parse IOCs (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "example_parse_iocs_attachment",
      "tags": [],
      "uuid": "5a26c0f1-3437-4f70-b874-d3be0965f415",
      "workflow_id": 449
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "example_parse_iocs_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_iocs_artifact\" isExecutable=\"true\" name=\"Parse IOCs (Artifact)\"\u003e\u003cdocumentation\u003eExample workflow showing how to extract IOC\u0027s (Indicators of Compromise) from an artifact file or text-based artifact. Each unique IOC is added to the incident as an artifact.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00jrs4u\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08sv9vd\" name=\"IOC Parser v2\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"52803581-019a-4c68-8f8d-8be9ca31b2f6\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\ndef get_artifact_type(artifact_value, artifact_type):\\n  \\\"\\\"\\\"Use some regex expressions to try and identify\\n  from the Artifact\u0027s value, what Artifact type it is.\\n  Return original artifact_type if we cannot figure it out\\\"\\\"\\\"\\n\\n  dns_name_regex = re.compile(r\u0027^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\\\\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\\\\.[a-zA-Z]{2,3})$\u0027)\\n  \\n  if re.match(dns_name_regex, artifact_value):\\n    return \\\"DNS Name\\\"\\n  \\n  return artifact_type\\n\\n# Map ioc.type to Resilient Artifact Type\\nioc_type_to_artifact_type_map = {\\n    \u0027uri\u0027: \u0027URI Path\u0027,\\n    \u0027IP\u0027: \u0027IP Address\u0027,\\n    \u0027md5\u0027: \u0027Malware MD5 Hash\u0027,\\n    \u0027sha1\u0027: \u0027Malware SHA-1 Hash\u0027,\\n    \u0027sha256\u0027: \u0027Malware SHA-256 Hash\u0027,\\n    \u0027CVE\u0027: \u0027Threat CVE ID\u0027,\\n    \u0027email\u0027: \u0027Email Sender\u0027,\\n    \u0027filename\u0027: \u0027File Name\u0027,\\n    \u0027file\u0027: \u0027File Name\u0027\\n}\\n\\n# Get the IOCs\\niocs = results.iocs\\n\\nartifact_list = []\\nif iocs:\\n    # Loop IOCs and add each on as an Artifact\\n    for ioc in iocs:\\n      \\n      # If attachment_file_name is not defined, use the ioc.value as in the Artifact\u0027s Description\\n      if results.attachment_file_name:\\n        artifact_description = \\\"This IOC occurred {0} time(s) in the artifact: {1}\\\".format(ioc.get(\u0027count\u0027), results.attachment_file_name)\\n      \\n      else:\\n        artifact_description = \\\"This IOC occurred {0} time(s) in the artifact: {1}\\\".format(ioc.get(\u0027count\u0027), ioc.get(\u0027value\u0027))\\n\\n      artifact_value = ioc.get(\u0027value\u0027)\\n      artifact_type = ioc_type_to_artifact_type_map.get(ioc.get(\u0027type\u0027), \\\"String\\\")\\n      \\n      # If the artifact_type is \u0027URI Path\u0027, call get_artifact_type to try intentify the type using regex\\n      if artifact_type == \\\"URI Path\\\":\\n        artifact_type = get_artifact_type(artifact_value, artifact_type)\\n      \\n      incident.addArtifact(artifact_type, artifact_value, artifact_description)\\n      artifact_list.append(\\\"{}: {}\\\".format(artifact_type, artifact_value))\\n      \\nif artifact_list:\\n  incident.addNote(\\\"The following artifacts were added from artifact: {} - {}\\\\n{}\\\".format(artifact.type, results.attachment_file_name or artifact.value, \\\"\\\\n\\\".join(artifact_list)))\\nelse:\\n  incident.addNote(\\\"No artifacts were added from artifact: {} - {}\\\\n{}\\\".format(artifact.type, results.attachment_file_name or artifact.value, \\\"\\\\n\\\".join(artifact_list)))\\n\\n  \\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Define Pre-Process Inputs\\ninputs.ioc_parser_v2_incident_id = incident.id\\ninputs.ioc_parser_v2_artifact_id = artifact.id\\ninputs.ioc_parser_v2_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00jrs4u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0j9vqg5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_00jrs4u\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08sv9vd\"/\u003e\u003cendEvent id=\"EndEvent_0fh1yih\"\u003e\u003cincoming\u003eSequenceFlow_0j9vqg5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0j9vqg5\" sourceRef=\"ServiceTask_08sv9vd\" targetRef=\"EndEvent_0fh1yih\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14tovnv\"\u003e\u003ctext\u003eartifacts added to the incident from the artifact file. A note is created with summary information\n.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_00dh0em\" sourceRef=\"ServiceTask_08sv9vd\" targetRef=\"TextAnnotation_14tovnv\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08sv9vd\" id=\"ServiceTask_08sv9vd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"270\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00jrs4u\" id=\"SequenceFlow_00jrs4u_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"270\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"189\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fh1yih\" id=\"EndEvent_0fh1yih_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"428\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"401\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j9vqg5\" id=\"SequenceFlow_0j9vqg5_di\"\u003e\u003comgdi:waypoint x=\"370\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"428\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"354\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14tovnv\" id=\"TextAnnotation_14tovnv_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"209\" x=\"377\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_00dh0em\" id=\"Association_00dh0em_di\"\u003e\u003comgdi:waypoint x=\"370\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"421\" y=\"155\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Example workflow showing how to extract IOC\u0027s (Indicators of Compromise) from an artifact file or text-based artifact. Each unique IOC is added to the incident as an artifact.",
      "export_key": "example_parse_iocs_artifact",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743512554833,
      "name": "Parse IOCs (Artifact)",
      "object_type": "artifact",
      "programmatic_name": "example_parse_iocs_artifact",
      "tags": [],
      "uuid": "7ad8e210-c47e-4725-98bd-478240fff0f9",
      "workflow_id": 450
    }
  ],
  "workspaces": []
}
