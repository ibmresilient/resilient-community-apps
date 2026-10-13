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
          "value": "RFC 822 Email Message File"
        }
      ],
      "enabled": true,
      "export_key": "Example: Email Header Validation Using DKIM/ARC [Artifact]",
      "id": 689,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Email Header Validation Using DKIM/ARC [Artifact]",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "78954f6d-fc85-4c01-8db6-a5e6a649aa8d",
      "view_items": [],
      "workflows": [
        "example_email_header_validation_using_dkimarc_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Email Header Validation Using DKIM/ARC [Attachment]",
      "id": 690,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Email Header Validation Using DKIM/ARC [Attachment]",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3aa76add-4985-411e-8c5b-c081d083368f",
      "view_items": [],
      "workflows": [
        "example_email_header_validation_using_dkimarc_attachment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1747320478568,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 2753,
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
      "uuid": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
      "id": 2802,
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
      "uuid": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
      "export_key": "__function/email_header_validation_target_email",
      "hide_notification": false,
      "id": 4362,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "email_header_validation_target_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "email_header_validation_target_email",
      "tooltip": "RFC822 email to perform header analysis on. Can be used in place of attachment/artifact ids in chained workflows",
      "type_id": 11,
      "uuid": "0582d2d7-d715-4f64-81d3-50c94cfa1f29",
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
      "id": 2803,
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
      "created_date": 1746269345006,
      "description": {
        "content": "Analyzes the DKIM and ARC headers for a RFC822 formatted email.",
        "format": "text"
      },
      "destination_handle": "fn_email_header_validation",
      "display_name": "Email Header Validation Using DKIM/ARC",
      "export_key": "email_header_validation_using_dkimarc",
      "id": 450,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1747216966920,
      "name": "email_header_validation_using_dkimarc",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "423276f4-cae3-4f99-b7f6-c72604eb2f91",
      "version": 4,
      "view_items": [
        {
          "content": "0582d2d7-d715-4f64-81d3-50c94cfa1f29",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
          "name": "Example: Email Header Validation Using DKIM/ARC [Artifact]",
          "object_type": "artifact",
          "programmatic_name": "example_email_header_validation_using_dkimarc_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 667
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Email Header Validation Using DKIM/ARC [Attachment]",
          "object_type": "attachment",
          "programmatic_name": "example_email_header_validation_using_dkimarc_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 666
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 232,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1747320475885,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1747320475885,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "a35281f3-c8c2-4819-8455-abfe6280d85e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_email_header_validation",
      "name": "fn_email_header_validation",
      "programmatic_name": "fn_email_header_validation",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "a7fd6931-2b8b-460b-aa23-5b35eae48328"
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
        "version": 2,
        "workflow_id": "example_email_header_validation_using_dkimarc_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_email_header_validation_using_dkimarc_attachment\" isExecutable=\"true\" name=\"Example: Email Header Validation Using DKIM/ARC [Attachment]\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1joxzn2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bgejwn\" name=\"Email Header Validation Using DKI...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"423276f4-cae3-4f99-b7f6-c72604eb2f91\"\u003e{\"inputs\":{},\"post_processing_script\":\"# results = {\\n#                 \\\"dkim_verify\\\": True/False,\\n#                 \\\"arc_verify\\\": True/False,\\n#                 \\\"dkim_message\\\": reason for True/False\\n#                 \\\"arc_message\\\": reason for True/False\\n#             }\\n\\noutput = f\\\"DKIM Analysis: {str(results.dkim_verify)}. {results.dkim_message}\\\\nARC Analysis: {str(results.arc_verify)}. {results.arc_message}\\\"\\nincident.addNote(output)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1joxzn2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_044yfhc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1joxzn2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bgejwn\"/\u003e\u003cendEvent id=\"EndEvent_02zvls5\"\u003e\u003cincoming\u003eSequenceFlow_044yfhc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_044yfhc\" sourceRef=\"ServiceTask_1bgejwn\" targetRef=\"EndEvent_02zvls5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"176\" y=\"233\"/\u003e\u003comgdi:waypoint x=\"158\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bgejwn\" id=\"ServiceTask_1bgejwn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"292\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1joxzn2\" id=\"SequenceFlow_1joxzn2_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"292\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"206\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02zvls5\" id=\"EndEvent_02zvls5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"459\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"477\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_044yfhc\" id=\"SequenceFlow_044yfhc_di\"\u003e\u003comgdi:waypoint x=\"392\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"459\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"425.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "",
      "export_key": "example_email_header_validation_using_dkimarc_attachment",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1746269593189,
      "name": "Example: Email Header Validation Using DKIM/ARC [Attachment]",
      "object_type": "attachment",
      "programmatic_name": "example_email_header_validation_using_dkimarc_attachment",
      "tags": [],
      "uuid": "ace581a8-891b-4d71-b6c3-d74e6ff693f7",
      "workflow_id": 666
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_email_header_validation_using_dkimarc_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_email_header_validation_using_dkimarc_artifact\" isExecutable=\"true\" name=\"Example: Email Header Validation Using DKIM/ARC [Artifact]\"\u003e\u003cdocumentation\u003eAn example of having an artifact email\u0027s header validated using DKIM/ARC.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0bgsi2n\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1nule12\" name=\"Email Header Validation Using DKI...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"423276f4-cae3-4f99-b7f6-c72604eb2f91\"\u003e{\"inputs\":{},\"post_processing_script\":\"# results = {\\n#                 \\\"dkim_verify\\\": True/False,\\n#                 \\\"arc_verify\\\": True/False,\\n#                 \\\"dkim_message\\\": reason for True/False\\n#                 \\\"arc_message\\\": reason for True/False\\n#             }\\n\\noutput = f\\\"DKIM Analysis: {str(results.dkim_verify)}. {results.dkim_message}\\\\nARC Analysis: {str(results.arc_verify)}. {results.arc_message}\\\"\\nincident.addNote(output)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0bgsi2n\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1932xwo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0bgsi2n\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1nule12\"/\u003e\u003cendEvent id=\"EndEvent_0arnekp\"\u003e\u003cincoming\u003eSequenceFlow_1932xwo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1932xwo\" sourceRef=\"ServiceTask_1nule12\" targetRef=\"EndEvent_0arnekp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1nule12\" id=\"ServiceTask_1nule12_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"299\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bgsi2n\" id=\"SequenceFlow_0bgsi2n_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"299\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"213\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0arnekp\" id=\"EndEvent_0arnekp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"485\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"458\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1932xwo\" id=\"SequenceFlow_1932xwo_di\"\u003e\u003comgdi:waypoint x=\"399\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"485\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"397\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example of having an artifact email\u0027s header validated using DKIM/ARC.",
      "export_key": "example_email_header_validation_using_dkimarc_artifact",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1746269510736,
      "name": "Example: Email Header Validation Using DKIM/ARC [Artifact]",
      "object_type": "artifact",
      "programmatic_name": "example_email_header_validation_using_dkimarc_artifact",
      "tags": [],
      "uuid": "7d0436d9-0275-488e-afc0-e0ebfdefa68b",
      "workflow_id": 667
    }
  ],
  "workspaces": []
}
