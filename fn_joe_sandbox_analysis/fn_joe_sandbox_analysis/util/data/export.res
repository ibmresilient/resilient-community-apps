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
          "value": "DNS Name"
        },
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
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Other File"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URI Path"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: Joe Sandbox Analysis [Artifact]",
      "id": 217,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Joe Sandbox Analysis [Artifact]",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "050c7c78-5f4d-46f6-a27a-af8a07e7b518",
      "view_items": [],
      "workflows": [
        "example_joe_sandbox_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Joe Sandbox Analysis [Attachment]",
      "id": 218,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Joe Sandbox Analysis [Attachment]",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3df312b3-fd45-46db-9a2c-5eae37d698ca",
      "view_items": [],
      "workflows": [
        "example_joe_sandbox_analysis_attachment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1671032556143,
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
      "export_key": "__function/artifact_value",
      "hide_notification": false,
      "id": 4155,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8d80daa3-ea09-4d10-b1ec-6fc118f45173",
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
      "export_key": "__function/artifact_type",
      "hide_notification": false,
      "id": 4156,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b8178334-f606-404a-8cc7-689cef3463e2",
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
      "id": 4153,
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
      "id": 4160,
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
      "uuid": "f6d29475-11ac-403a-87e0-15086e45caea",
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
      "id": 4152,
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
      "export_key": "__function/jsb_report_type",
      "hide_notification": false,
      "id": 4154,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "jsb_report_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "jsb_report_type",
      "tooltip": "The format of the report to be returned from Joe Sandbox",
      "type_id": 11,
      "uuid": "24cd65fa-e06c-4580-8a7b-923585f9d81b",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "html",
          "properties": null,
          "uuid": "222faf2b-f446-471e-a3c7-9eb21c807318",
          "value": 755
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "pdf",
          "properties": null,
          "uuid": "d746ab19-7615-4581-8749-ecca266b1a55",
          "value": 756
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "json",
          "properties": null,
          "uuid": "49cae5fd-9c09-4988-a09d-354b680cd9b1",
          "value": 757
        }
      ]
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
      "created_date": 1670952911762,
      "description": {
        "content": "A function that allows an Attachment or Artifact (File/URL) to be analyzed by Joe Sandbox",
        "format": "text"
      },
      "destination_handle": "joe_sandbox_message_destination",
      "display_name": "Joe Sandbox Analysis",
      "export_key": "fn_joe_sandbox_analysis",
      "id": 19,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 17,
        "name": "c@example.com",
        "type": "user"
      },
      "last_modified_time": 1671032529783,
      "name": "fn_joe_sandbox_analysis",
      "tags": [],
      "uuid": "76d63c86-c5fd-41f7-a43a-2922d6fb3d91",
      "version": 10,
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
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24cd65fa-e06c-4580-8a7b-923585f9d81b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8d80daa3-ea09-4d10-b1ec-6fc118f45173",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b8178334-f606-404a-8cc7-689cef3463e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f6d29475-11ac-403a-87e0-15086e45caea",
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
          "name": "Example: Joe Sandbox [Artifact]",
          "object_type": "artifact",
          "programmatic_name": "example_joe_sandbox_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 22
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Joe Sandbox Analysis [Attachment]",
          "object_type": "attachment",
          "programmatic_name": "example_joe_sandbox_analysis_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 21
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 9,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1671032554503,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1671032554503,
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
      "export_key": "joe_sandbox_message_destination",
      "name": "Joe Sandbox Message Destination",
      "programmatic_name": "joe_sandbox_message_destination",
      "tags": [],
      "users": [
        "c@example.com"
      ],
      "uuid": "dd789db8-2a05-48b9-9e90-75b49a10eeed"
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
    "build_number": 7585,
    "major": 44,
    "minor": 0,
    "version": "44.0.7585"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "example_joe_sandbox_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_joe_sandbox_artifact\" isExecutable=\"true\" name=\"Example: Joe Sandbox [Artifact]\"\u003e\u003cdocumentation\u003eAn example of having an artifact sample analyzed by Joe Sandbox\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ngud9y\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_16frtlo\"\u003e\u003cincoming\u003eSequenceFlow_1v3ye91\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0gwboyh\" name=\"Joe Sandbox Analysis\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"76d63c86-c5fd-41f7-a43a-2922d6fb3d91\"\u003e{\"inputs\":{\"24cd65fa-e06c-4580-8a7b-923585f9d81b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"222faf2b-f446-471e-a3c7-9eb21c807318\"}}},\"post_processing_script\":\"color = \\\"#45bc27\\\"\\n\\nif (results.analysis_status != \\\"clean\\\"):\\n  color = \\\"#ff402b\\\"\\n  \\nnoteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Joe Sandbox analysis \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; complete\\n              \u0026lt;b\u0026gt;Artifact:\u0026lt;/b\u0026gt; \u0027{1}\u0027\\n              \u0026lt;b\u0026gt;Report URL:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{2}\u0027\u0026gt;{2}\u0026lt;/a\u0026gt;\\n              \u0026lt;b\u0026gt;Detection Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.analysis_report_name, artifact.value, results.analysis_report_url, color, results.analysis_status)\\n\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.artifact_value = artifact.value\\ninputs.artifact_type = artifact.type\\ninputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ngud9y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1v3ye91\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ngud9y\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gwboyh\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1v3ye91\" sourceRef=\"ServiceTask_0gwboyh\" targetRef=\"EndEvent_16frtlo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16frtlo\" id=\"EndEvent_16frtlo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"634\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"652\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gwboyh\" id=\"ServiceTask_0gwboyh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"352\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ngud9y\" id=\"SequenceFlow_0ngud9y_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"275\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1v3ye91\" id=\"SequenceFlow_1v3ye91_di\"\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"634\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"543\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "description": "An example of having an artifact sample analyzed by Joe Sandbox",
      "export_key": "example_joe_sandbox_artifact",
      "last_modified_by": "c@example.com",
      "last_modified_time": 1671032551283,
      "name": "Example: Joe Sandbox [Artifact]",
      "object_type": "artifact",
      "programmatic_name": "example_joe_sandbox_artifact",
      "tags": [],
      "uuid": "ab6aaa61-0f70-4432-b15f-b994b46b30f5",
      "workflow_id": 22
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "example_joe_sandbox_analysis_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_joe_sandbox_analysis_attachment\" isExecutable=\"true\" name=\"Example: Joe Sandbox Analysis [Attachment]\"\u003e\u003cdocumentation\u003eAn example of having an attachment sample analyzed by Joe Sandbox\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12ic7g4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0920lp5\"\u003e\u003cincoming\u003eSequenceFlow_0zk4elj\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_10hkln1\" name=\"Joe Sandbox Analysis\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"76d63c86-c5fd-41f7-a43a-2922d6fb3d91\"\u003e{\"inputs\":{\"24cd65fa-e06c-4580-8a7b-923585f9d81b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"222faf2b-f446-471e-a3c7-9eb21c807318\"}}},\"post_processing_script\":\"color = \\\"#45bc27\\\"\\n\\nif (results.analysis_status != \\\"clean\\\"):\\n  color = \\\"#ff402b\\\"\\n  \\nnoteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Joe Sandbox analysis \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; complete\\n              \u0026lt;b\u0026gt;Attachment:\u0026lt;/b\u0026gt; \u0027{1}\u0027\\n              \u0026lt;b\u0026gt;Report URL:\u0026lt;/b\u0026gt; \u0026lt;a href=\u0027{2}\u0027\u0026gt;{2}\u0026lt;/a\u0026gt;\\n              \u0026lt;b\u0026gt;Detection Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {3}\\\"\u0026gt;{4}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.analysis_report_name, attachment.name, results.analysis_report_url, color, results.analysis_status)\\n\\nincident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12ic7g4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zk4elj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_12ic7g4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_10hkln1\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0zk4elj\" sourceRef=\"ServiceTask_10hkln1\" targetRef=\"EndEvent_0920lp5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0920lp5\" id=\"EndEvent_0920lp5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"583\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"601\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10hkln1\" id=\"ServiceTask_10hkln1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"336\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12ic7g4\" id=\"SequenceFlow_12ic7g4_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"267\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zk4elj\" id=\"SequenceFlow_0zk4elj_di\"\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"583\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"509.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "An example of having an attachment sample analyzed by Joe Sandbox",
      "export_key": "example_joe_sandbox_analysis_attachment",
      "last_modified_by": "c@example.com",
      "last_modified_time": 1671031185387,
      "name": "Example: Joe Sandbox Analysis [Attachment]",
      "object_type": "attachment",
      "programmatic_name": "example_joe_sandbox_analysis_attachment",
      "tags": [],
      "uuid": "b6888a4b-1cdf-4b1e-9414-71eb4bb1232f",
      "workflow_id": 21
    }
  ],
  "workspaces": []
}
