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
        }
      ],
      "enabled": true,
      "export_key": "Example: IsItPhishing Analyze HTML Document: Artifact",
      "id": 51,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: IsItPhishing Analyze HTML Document: Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cb18b265-76a5-448e-83ce-7b84a8936375",
      "view_items": [],
      "workflows": [
        "example_isitphishing_analyze_html_document_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: IsItPhishing Analyze HTML Document: Attachment",
      "id": 52,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: IsItPhishing Analyze HTML Document: Attachment",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "326a1b3e-d1e5-434b-b7aa-73281bc2e5eb",
      "view_items": [],
      "workflows": [
        "example_isitphishing_analyze_html_document"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: IsItPhishing Analyze URL",
      "id": 53,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: IsItPhishing Analyze URL",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cad9a90a-1597-4ab4-bd31-20335c06aeed",
      "view_items": [],
      "workflows": [
        "example_isitphishing_analyze_url"
      ]
    }
  ],
  "automatic_tasks": [],
  "export_date": 1607043046255,
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
      "export_key": "__function/isitphishing_url",
      "hide_notification": false,
      "id": 341,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "isitphishing_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "isitphishing_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c8d3a8b4-b915-4fb7-8a88-821d6b365586",
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
      "id": 340,
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
      "export_key": "__function/attachment_id",
      "hide_notification": false,
      "id": 321,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 188,
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
      "uuid": "0dd1c2e1-95c9-444c-8688-269dea6fb7f1",
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 252,
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
      "uuid": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
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
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Analyze an HTML document using the Vade Secure IsItPhishing Webservice API.",
        "format": "text"
      },
      "destination_handle": "fn_isitphishing",
      "display_name": "IsItPhishing HTML document",
      "export_key": "isitphishing_html_document",
      "id": 26,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1604696582630,
      "name": "isitphishing_html_document",
      "tags": [],
      "uuid": "e7360c49-014f-4033-838b-240131ae552b",
      "version": 25,
      "view_items": [
        {
          "content": "0dd1c2e1-95c9-444c-8688-269dea6fb7f1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
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
          "name": "Example: IsItPhishing Analyze HTML Document: Artifact",
          "object_type": "artifact",
          "programmatic_name": "example_isitphishing_analyze_html_document_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 31
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: IsItPhishing Analyze HTML Document: Attachment",
          "object_type": "attachment",
          "programmatic_name": "example_isitphishing_analyze_html_document",
          "tags": [],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Analyze a URL using the Vade Secure IsItPhishing Webservice API.",
        "format": "text"
      },
      "destination_handle": "fn_isitphishing",
      "display_name": "IsItPhishing URL",
      "export_key": "isitphishing_url",
      "id": 27,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1604696582630,
      "name": "isitphishing_url",
      "tags": [],
      "uuid": "94f5697a-ddfd-4fc5-ad9b-8b56386c0ba6",
      "version": 23,
      "view_items": [
        {
          "content": "c8d3a8b4-b915-4fb7-8a88-821d6b365586",
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
          "name": "Example: IsItPhishing Analyze URL",
          "object_type": "artifact",
          "programmatic_name": "example_isitphishing_analyze_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 32
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 73,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1607091555929,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1607091555929,
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
      "export_key": "fn_isitphishing",
      "name": "fn_isitPhishing",
      "programmatic_name": "fn_isitphishing",
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
        "version": 28,
        "workflow_id": "example_isitphishing_analyze_html_document_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_isitphishing_analyze_html_document_artifact\" isExecutable=\"true\" name=\"Example: IsItPhishing Analyze HTML Document: Artifact\"\u003e\u003cdocumentation\u003eThis workflow takes an HTML document artifact as input and calls the isitPhishing_HTML_document function to determine if the document contains phishing.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1w93wjp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17jclyq\" name=\"IsItPhishing HTML document\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7360c49-014f-4033-838b-240131ae552b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  content = u\\\"IsItPhishing analysis of artifact document {0} : {1}\\\".format(results[\\\"inputs\\\"][\\\"filename\\\"],results[\u0027content\u0027][\u0027result\u0027])\\nelse:\\n  content = u\\\"IsItPhishing analysis of artifact document {0} : ERROR\\\".format(results[\\\"inputs\\\"][\\\"filename\\\"])\\n  \\n# Create a note\\nnote = helper.createPlainText(content)\\n\\n# Add note to the task or incident\\nif task:\\n  task.addNote(note)\\nelse:\\n  incident.addNote(note)\",\"pre_processing_script\":\"# Required inputs are: incident id and artifact id.\\ninputs.incident_id = incident.id\\ninputs.artifact_id = artifact.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1w93wjp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0juvd1y\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1w93wjp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17jclyq\"/\u003e\u003cendEvent id=\"EndEvent_0z3mt4l\"\u003e\u003cincoming\u003eSequenceFlow_0juvd1y\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0juvd1y\" sourceRef=\"ServiceTask_17jclyq\" targetRef=\"EndEvent_0z3mt4l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0pt9m2l\"\u003e\u003ctext\u003e\u003c![CDATA[Input: artifact id, incident id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ambjgc\" sourceRef=\"ServiceTask_17jclyq\" targetRef=\"TextAnnotation_0pt9m2l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mpawn9\"\u003e\u003ctext\u003e\u003c![CDATA[Output: Incident note indicating results of IsItPhishing Analysis\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1rgwv0x\" sourceRef=\"ServiceTask_17jclyq\" targetRef=\"TextAnnotation_1mpawn9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17jclyq\" id=\"ServiceTask_17jclyq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"431\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1w93wjp\" id=\"SequenceFlow_1w93wjp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"314.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0z3mt4l\" id=\"EndEvent_0z3mt4l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"656\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"674\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0juvd1y\" id=\"SequenceFlow_0juvd1y_di\"\u003e\u003comgdi:waypoint x=\"531\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"656\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"593.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0pt9m2l\" id=\"TextAnnotation_0pt9m2l_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"205\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ambjgc\" id=\"Association_1ambjgc_di\"\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mpawn9\" id=\"TextAnnotation_1mpawn9_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"604\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1rgwv0x\" id=\"Association_1rgwv0x_di\"\u003e\u003comgdi:waypoint x=\"526\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"634\" xsi:type=\"omgdc:Point\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 28,
      "creator_id": "a@a.com",
      "description": "This workflow takes an HTML document artifact as input and calls the isitPhishing_HTML_document function to determine if the document contains phishing.",
      "export_key": "example_isitphishing_analyze_html_document_artifact",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1605220327047,
      "name": "Example: IsItPhishing Analyze HTML Document: Artifact",
      "object_type": "artifact",
      "programmatic_name": "example_isitphishing_analyze_html_document_artifact",
      "tags": [],
      "uuid": "c522dc94-3a68-4f93-ac26-3a01c5e296da",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 26,
        "workflow_id": "example_isitphishing_analyze_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_isitphishing_analyze_url\" isExecutable=\"true\" name=\"Example: IsItPhishing Analyze URL\"\u003e\u003cdocumentation\u003eThis workflow takes an artifact as input and calls the isitPhishing function to determine if the URL is a phishing URL. The URL analysis result is returned in an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0z0728r\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0etwcc2\" name=\"IsItPhishing URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"94f5697a-ddfd-4fc5-ad9b-8b56386c0ba6\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Get the results and post to an incident note.\\nif results.success:\\n  content = u\u0027IsItPhishing analysis of URL {0} : {1}\\\\n\u0027.format(results[\u0027inputs\u0027][\u0027isitphishing_url\u0027], results[\u0027content\u0027][\u0027status\u0027])\\nelse:\\n  content = u\u0027IsItPhishing analysis of URL {0} : ERROR\\\\n\u0027.format(results[\u0027inputs\u0027][\u0027isitphishing_url\u0027])\\nnote = helper.createPlainText(content)\\nincident.addNote(note)\",\"pre_processing_script\":\"# Get the URL from the artifact value\\ninputs.isitphishing_url = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0z0728r\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1xchx2b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0z0728r\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0etwcc2\"/\u003e\u003cendEvent id=\"EndEvent_1d76caj\"\u003e\u003cincoming\u003eSequenceFlow_1xchx2b\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1xchx2b\" sourceRef=\"ServiceTask_0etwcc2\" targetRef=\"EndEvent_1d76caj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1j5fnxr\"\u003e\u003ctext\u003e\u003c![CDATA[Input: artifact value contains the URL to be queried\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1d034c9\" sourceRef=\"ServiceTask_0etwcc2\" targetRef=\"TextAnnotation_1j5fnxr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ss2dkx\"\u003e\u003ctext\u003e\u003c![CDATA[Result: Incident note added with results of query on the URL.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0d5ftme\" sourceRef=\"ServiceTask_0etwcc2\" targetRef=\"TextAnnotation_0ss2dkx\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0etwcc2\" id=\"ServiceTask_0etwcc2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"392\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z0728r\" id=\"SequenceFlow_0z0728r_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"295\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1d76caj\" id=\"EndEvent_1d76caj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"647\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"665\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xchx2b\" id=\"SequenceFlow_1xchx2b_di\"\u003e\u003comgdi:waypoint x=\"492\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"647\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"569.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1j5fnxr\" id=\"TextAnnotation_1j5fnxr_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"170\" y=\"59\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1d034c9\" id=\"Association_1d034c9_di\"\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"245\" xsi:type=\"omgdc:Point\" y=\"89\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ss2dkx\" id=\"TextAnnotation_0ss2dkx_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"559\" y=\"59\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0d5ftme\" id=\"Association_0d5ftme_di\"\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"590\" xsi:type=\"omgdc:Point\" y=\"89\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 26,
      "creator_id": "a@a.com",
      "description": "This workflow takes an artifact as input and calls the isitPhishing function to determine if the URL is a phishing URL. The URL analysis result is returned in an incident note.",
      "export_key": "example_isitphishing_analyze_url",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1605218405867,
      "name": "Example: IsItPhishing Analyze URL",
      "object_type": "artifact",
      "programmatic_name": "example_isitphishing_analyze_url",
      "tags": [],
      "uuid": "c086dce3-1be7-4bdc-9205-95aecad8df3d",
      "workflow_id": 32
    },
    {
      "actions": [],
      "content": {
        "version": 26,
        "workflow_id": "example_isitphishing_analyze_html_document",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_isitphishing_analyze_html_document\" isExecutable=\"true\" name=\"Example: IsItPhishing Analyze HTML Document: Attachment\"\u003e\u003cdocumentation\u003eThis workflow takes an attachment as input and calls the isitPhishing_HTML_document function to determine if the document contains phishing.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0v9whde\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_07uhi7c\" name=\"IsItPhishing HTML document\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7360c49-014f-4033-838b-240131ae552b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  content = u\\\"IsItPhishing analysis of attachment document {0} : {1}\\\".format(results[\\\"inputs\\\"][\\\"filename\\\"],results[\u0027content\u0027][\u0027result\u0027])\\nelse:\\n  content = u\\\"IsItPhishing analysis of attachment document {0} : ERROR\\\".format(results[\\\"inputs\\\"][\\\"filename\\\"])\\n  \\n# Create a note\\nnote = helper.createPlainText(content)\\n\\n# Add note to the task or incident\\nif task:\\n  task.addNote(note)\\nelse:\\n  incident.addNote(note)\",\"pre_processing_script\":\"# Required inputs are: incident id and attachment id\\ninputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\n\\nif task is not None:\\n  inputs.task_id = task.id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0v9whde\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1f929kw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0v9whde\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_07uhi7c\"/\u003e\u003cendEvent id=\"EndEvent_0ye91po\"\u003e\u003cincoming\u003eSequenceFlow_1f929kw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1f929kw\" sourceRef=\"ServiceTask_07uhi7c\" targetRef=\"EndEvent_0ye91po\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0395yz1\"\u003e\u003ctext\u003e\u003c![CDATA[Input: attachment id and incident or task id\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0gg5vxe\" sourceRef=\"ServiceTask_07uhi7c\" targetRef=\"TextAnnotation_0395yz1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1foa7rt\"\u003e\u003ctext\u003e\u003c![CDATA[Output: an incident or task note containing the results of the isitPhishing html document analysis\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_07sn0fa\" sourceRef=\"ServiceTask_07uhi7c\" targetRef=\"TextAnnotation_1foa7rt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_07uhi7c\" id=\"ServiceTask_07uhi7c_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"389\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v9whde\" id=\"SequenceFlow_0v9whde_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"293.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ye91po\" id=\"EndEvent_0ye91po_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"640.694591728526\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"658.694591728526\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f929kw\" id=\"SequenceFlow_1f929kw_di\"\u003e\u003comgdi:waypoint x=\"489\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"641\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"565\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0395yz1\" id=\"TextAnnotation_0395yz1_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"188.69459172852598\" y=\"70.07317073170732\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0gg5vxe\" id=\"Association_0gg5vxe_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"264\" xsi:type=\"omgdc:Point\" y=\"100\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1foa7rt\" id=\"TextAnnotation_1foa7rt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"534.694591728526\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_07sn0fa\" id=\"Association_07sn0fa_di\"\u003e\u003comgdi:waypoint x=\"483\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"567\" xsi:type=\"omgdc:Point\" y=\"100\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 26,
      "creator_id": "a@a.com",
      "description": "This workflow takes an attachment as input and calls the isitPhishing_HTML_document function to determine if the document contains phishing.",
      "export_key": "example_isitphishing_analyze_html_document",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1605220353944,
      "name": "Example: IsItPhishing Analyze HTML Document: Attachment",
      "object_type": "attachment",
      "programmatic_name": "example_isitphishing_analyze_html_document",
      "tags": [],
      "uuid": "93f24b27-7ddb-4331-8d59-b5a917df75c0",
      "workflow_id": 33
    }
  ],
  "workspaces": []
}
