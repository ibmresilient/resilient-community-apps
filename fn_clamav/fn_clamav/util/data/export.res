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
          "value": "Email Attachment"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware Sample"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Other File"
        }
      ],
      "enabled": true,
      "export_key": "Example: ClamAV scan artifact attachment",
      "id": 43,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: ClamAV scan artifact attachment",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f307b784-152c-451a-808c-a0e436e1fa1c",
      "view_items": [],
      "workflows": [
        "example_clamav_scan_artifact_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: ClamAV scan attachment",
      "id": 44,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ClamAV scan attachment",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9aea3d13-c335-4853-9cb9-5e10a6561808",
      "view_items": [],
      "workflows": [
        "example_clamav_scan_attachment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1630595803493,
  "export_format_version": 2,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 279,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
      "id": 266,
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
      "uuid": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "export_key": "__function/artifact_id",
      "hide_notification": false,
      "id": 269,
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
      "uuid": "efdbca7e-6ae8-4269-a3d1-80f1716a6222",
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
      "id": 278,
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
      "created_date": 1630515683345,
      "creator": {
        "display_name": "Chris\u0027 Integration Server",
        "id": 6,
        "name": "d69a1504-6fff-496b-a846-6871e9af9766",
        "type": "apikey"
      },
      "description": {
        "content": "Function to send the contents of an attachment as a data-stream to a ClamAV server instance, to scan for malware or viruses.",
        "format": "text"
      },
      "destination_handle": "fn_clamav",
      "display_name": "ClamAV scan stream",
      "export_key": "clamav_scan_stream",
      "id": 29,
      "last_modified_by": {
        "display_name": "Chris\u0027 Integration Server",
        "id": 6,
        "name": "d69a1504-6fff-496b-a846-6871e9af9766",
        "type": "apikey"
      },
      "last_modified_time": 1630515683396,
      "name": "clamav_scan_stream",
      "tags": [],
      "uuid": "e9b68f1c-b48f-41c2-84f1-680142a0d8d5",
      "version": 1,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "efdbca7e-6ae8-4269-a3d1-80f1716a6222",
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
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
          "name": "Example: ClamAV scan artifact attachment",
          "object_type": "artifact",
          "programmatic_name": "example_clamav_scan_artifact_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 30
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: ClamAV scan attachment",
          "object_type": "attachment",
          "programmatic_name": "example_clamav_scan_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 31
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 5,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1630595802322,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1630595802322,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "d69a1504-6fff-496b-a846-6871e9af9766"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_clamav",
      "name": "fn_clamav",
      "programmatic_name": "fn_clamav",
      "tags": [],
      "users": [],
      "uuid": "2f537865-c061-4a71-a226-5927c276a1ce"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6783,
    "major": 41,
    "minor": 0,
    "version": "41.0.6783"
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
        "workflow_id": "example_clamav_scan_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_clamav_scan_attachment\" isExecutable=\"true\" name=\"Example: ClamAV scan attachment\"\u003e\u003cdocumentation\u003eAn example workflow to scan an incident or task attachment for malware or viruses using ClamAV.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_09isobd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1kqkbp3\" name=\"ClamAV scan stream\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e9b68f1c-b48f-41c2-84f1-680142a0d8d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  CLAMAV - clamav_scan_stream script ##\\n# Example results:\\n\\\"\\\"\\\"\\n# Virus found incident attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n# Virus found task attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 25, \\\"artifact_id\\\": null, \\\"task_id\\\": 2251251},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n\\n# Virus found artifact attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": null, \\\"artifact_id\\\": 10, \\\"task_id\\\": null},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n# No malware or  detected\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null}\\n             \\\"response\\\": {\\\"stream\\\": [\\\"OK\\\", \u0027\u0027]},\\n             \\\"file_name\\\": \\\"test.txt\\\",\\n           }\\n\\n# Got an error\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null\\n             \\\"response\\\": {\\\"stream\\\": [\\\"ERROR\\\", \u0027\u0026lt;reason\u0026gt;\u0027]},\\n             \\\"file_name\\\": \\\"test.txt\\\",\\n           }\\n\\\"\\\"\\\"\\n# Processing\\n\\ncolor = \\\"#45bc27\\\"\\n\\nresponse = results.response\\nfile_name = results.file_name\\ninputs = results.inputs\\n\\nif response is not None and response.stream[0] != \\\"ERROR\\\":\\n    if response.stream[0] == \\\"FOUND\\\":\\n        color = \\\"#ff402b\\\"\\n\\n    if inputs.incident_id is not None and inputs.artifact_id is not None:\\n        noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete          \\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Incident ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Artifact ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{1}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.incident_id,\\n                                                                                    inputs.artifact_id,\\n                                                                                    file_name, color, response.stream[1])\\n    elif inputs.attachment_id is not None:\\n        if inputs.task_id is not None:\\n            noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete           \\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Task ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{1}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.task_id,\\n                                                                                      inputs.attachment_id,\\n                                                                                      file_name, color, response.stream[1])\\n        elif inputs.incident_id is not None:\\n            noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete          \\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Incident ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\u0027{1}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.incident_id,\\n                                                                                      inputs.attachment_id,\\n                                                                                      file_name, color, response.stream[1])\\n    if inputs.task_id is not None:\\n        task.addNote(helper.createRichText(noteText))\\n    else:\\n        incident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"# Required inputs are: the incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.task_id = task.id\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_09isobd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ifeeve\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_09isobd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kqkbp3\"/\u003e\u003cendEvent id=\"EndEvent_11vr3zw\"\u003e\u003cincoming\u003eSequenceFlow_0ifeeve\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ifeeve\" sourceRef=\"ServiceTask_1kqkbp3\" targetRef=\"EndEvent_11vr3zw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0v0ts03\"\u003e\u003ctext\u003e\u003c![CDATA[Stream the file content to ClamAV to scan for viruses. A note is added with result of the virus scan.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_12yk8ek\" sourceRef=\"ServiceTask_1kqkbp3\" targetRef=\"TextAnnotation_0v0ts03\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0m3zm02\"\u003e\u003ctext\u003eInput to the ClamAV scan stream function is an incident id or task id and an attachment id.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rwf5rw\" sourceRef=\"ServiceTask_1kqkbp3\" targetRef=\"TextAnnotation_0m3zm02\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kqkbp3\" id=\"ServiceTask_1kqkbp3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"300\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0v0ts03\" id=\"TextAnnotation_0v0ts03_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"197\" x=\"472\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_12yk8ek\" id=\"Association_12yk8ek_di\"\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"520\" xsi:type=\"omgdc:Point\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09isobd\" id=\"SequenceFlow_09isobd_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"300\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"249\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_11vr3zw\" id=\"EndEvent_11vr3zw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"444.63390663390663\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"462.63390663390663\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ifeeve\" id=\"SequenceFlow_0ifeeve_di\"\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"445\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"422.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0m3zm02\" id=\"TextAnnotation_0m3zm02_di\"\u003e\u003comgdc:Bounds height=\"85\" width=\"180\" x=\"148\" y=\"41\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rwf5rw\" id=\"Association_0rwf5rw_di\"\u003e\u003comgdi:waypoint x=\"314\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"277\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "d69a1504-6fff-496b-a846-6871e9af9766",
      "description": "An example workflow to scan an incident or task attachment for malware or viruses using ClamAV.",
      "export_key": "example_clamav_scan_attachment",
      "last_modified_by": "d69a1504-6fff-496b-a846-6871e9af9766",
      "last_modified_time": 1630515683990,
      "name": "Example: ClamAV scan attachment",
      "object_type": "attachment",
      "programmatic_name": "example_clamav_scan_attachment",
      "tags": [],
      "uuid": "9e173e10-aeeb-4eb7-8ef9-045fa39f932c",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_clamav_scan_artifact_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_clamav_scan_artifact_attachment\" isExecutable=\"true\" name=\"Example: ClamAV scan artifact attachment\"\u003e\u003cdocumentation\u003eAn example workflow to scan an artifact attachment for malware or viruses using ClamAV.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14n1aiq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13ch31t\" name=\"ClamAV scan stream\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e9b68f1c-b48f-41c2-84f1-680142a0d8d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  CLAMAV - clamav_scan_stream script ##\\n# Example results:\\n\\\"\\\"\\\"\\n# Virus found incident attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n# Virus found task attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 25, \\\"artifact_id\\\": null, \\\"task_id\\\": 2251251},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n\\n# Virus found artifact attachment\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": null, \\\"artifact_id\\\": 10, \\\"task_id\\\": null},\\n             \\\"response\\\": {\\\"stream\\\": [\\\"FOUND\\\", \\\"Eicar-Test-Signature\\\"]},\\n             \\\"file_name\\\": \\\"eicar.txt\\\"\\n}\\n# No malware or  detected\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null}\\n             \\\"response\\\": {\\\"stream\\\": [\\\"OK\\\", \u0027\u0027]},\\n             \\\"file_name\\\": \\\"test.txt\\\",\\n           }\\n\\n# Got an error\\nResult:    { \\\"inputs\\\": {\\\"incident_id\\\": 2095, \\\"attachment_id\\\": 3, \\\"artifact_id\\\": null, \\\"task_id\\\": null\\n             \\\"response\\\": {\\\"stream\\\": [\\\"ERROR\\\", \u0027\u0026lt;reason\u0026gt;\u0027]},\\n             \\\"file_name\\\": \\\"test.txt\\\",\\n           }\\n\\\"\\\"\\\"\\n# Processing\\n\\ncolor = \\\"#45bc27\\\"\\n\\nresponse = results.response\\nfile_name = results.file_name\\ninputs = results.inputs\\n\\nif response is not None and response.stream[0] != \\\"ERROR\\\":\\n    if response.stream[0] == \\\"FOUND\\\":\\n        color = \\\"#ff402b\\\"\\n\\n    if inputs.incident_id is not None and inputs.artifact_id is not None:\\n        noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete          \\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Incident ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Artifact ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{1}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                        \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.incident_id,\\n                                                                                    inputs.artifact_id,\\n                                                                                    file_name, color, response.stream[1])\\n    elif inputs.attachment_id is not None:\\n        if inputs.task_id is not None:\\n            noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete           \\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Task ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{1}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.task_id,\\n                                                                                      inputs.attachment_id,\\n                                                                                      file_name, color, response.stream[1])\\n        elif inputs.incident_id is not None:\\n            noteText = u\\\"\\\"\\\"\u0026lt;br\u0026gt;ClamAV scan complete          \\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Incident ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{0}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment ID:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\u0027{1}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Attachment Name:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt; \u0027{2}\u0027\\n                          \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Scan Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\"\\\"\\\".format(inputs.incident_id,\\n                                                                                      inputs.attachment_id,\\n                                                                                      file_name, color, response.stream[1])\\n    if inputs.task_id is not None:\\n        task.addNote(helper.createRichText(noteText))\\n    else:\\n        incident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"# Required inputs are: the incident id and artifact id\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\\n\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14n1aiq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_18q36rk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14n1aiq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13ch31t\"/\u003e\u003cendEvent id=\"EndEvent_1lb0qd8\"\u003e\u003cincoming\u003eSequenceFlow_18q36rk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_18q36rk\" sourceRef=\"ServiceTask_13ch31t\" targetRef=\"EndEvent_1lb0qd8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1079hhw\"\u003e\u003ctext\u003eStream the file content to ScanAV to scan for viruses. A note is added with result of the virus scan.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ivfzzz\" sourceRef=\"ServiceTask_13ch31t\" targetRef=\"TextAnnotation_1079hhw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ciolhk\"\u003e\u003ctext\u003eInput to the ClamAV scan stream function is an incident id and an artifact id.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_191sp4q\" sourceRef=\"ServiceTask_13ch31t\" targetRef=\"TextAnnotation_0ciolhk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13ch31t\" id=\"ServiceTask_13ch31t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"260\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14n1aiq\" id=\"SequenceFlow_14n1aiq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"229\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1lb0qd8\" id=\"EndEvent_1lb0qd8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"419\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"437\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18q36rk\" id=\"SequenceFlow_18q36rk_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"419\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"389.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1079hhw\" id=\"TextAnnotation_1079hhw_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"203\" x=\"425\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ivfzzz\" id=\"Association_0ivfzzz_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"112\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ciolhk\" id=\"TextAnnotation_0ciolhk_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"140\" x=\"152\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_191sp4q\" id=\"Association_191sp4q_di\"\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"246\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "d69a1504-6fff-496b-a846-6871e9af9766",
      "description": "An example workflow to scan an artifact attachment for malware or viruses using ClamAV.",
      "export_key": "example_clamav_scan_artifact_attachment",
      "last_modified_by": "d69a1504-6fff-496b-a846-6871e9af9766",
      "last_modified_time": 1630515683833,
      "name": "Example: ClamAV scan artifact attachment",
      "object_type": "artifact",
      "programmatic_name": "example_clamav_scan_artifact_attachment",
      "tags": [],
      "uuid": "f25c67ea-0602-4735-a0d5-89adbb93b44e",
      "workflow_id": 30
    }
  ],
  "workspaces": []
}
