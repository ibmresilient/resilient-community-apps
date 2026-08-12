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
        }
      ],
      "enabled": true,
      "export_key": "Example: MXToolbox MX query",
      "id": 424,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: MXToolbox MX query",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d209576f-1e03-46af-a296-841dda70546f",
      "view_items": [],
      "workflows": [
        "example_mxtoolbox_mx_query"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1742834677620,
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
      "export_key": "__function/mx_param1",
      "hide_notification": false,
      "id": 2919,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mx_param1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mx_param1",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b3f7def1-ebe3-48f3-9d78-47eaeba7863b",
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
      "export_key": "__function/mx_command",
      "hide_notification": false,
      "id": 2918,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mx_command",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mx_command",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ca88493d-a9a7-4a4a-8af8-b3cdf0989c99",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "mx",
          "properties": null,
          "uuid": "267f420b-dcca-4740-9d54-933d03bca8b7",
          "value": 3402
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "a",
          "properties": null,
          "uuid": "43acde04-33a1-4050-b1f0-36bb079c2fea",
          "value": 3403
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "dns",
          "properties": null,
          "uuid": "73b416ef-66ed-44d8-bce9-1506acf42e0b",
          "value": 3404
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "spf",
          "properties": null,
          "uuid": "40b46118-73fb-4086-8e6d-b7be09cd151b",
          "value": 3405
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "txt",
          "properties": null,
          "uuid": "d4ee6ead-218a-4b74-852d-c2d25406f4ad",
          "value": 3406
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "soa",
          "properties": null,
          "uuid": "2f2fac15-5c68-4466-a3c5-deabaf9a4f82",
          "value": 3407
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ptr",
          "properties": null,
          "uuid": "fea62841-c9a6-4d60-82ed-f6e6cc9bcb3d",
          "value": 3408
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "blacklist",
          "properties": null,
          "uuid": "da853567-ca87-4f01-8fa0-18362cbb5940",
          "value": 3409
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "smtp",
          "properties": null,
          "uuid": "9f297efd-8f0b-4f2d-844e-c257f49ec011",
          "value": 3410
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "tcp",
          "properties": null,
          "uuid": "33e2f608-a4a4-49f1-abbd-ba97a4352bd4",
          "value": 3411
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "http",
          "properties": null,
          "uuid": "e5793684-38c5-4f35-90c5-6f0dd90cebac",
          "value": 3412
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "https",
          "properties": null,
          "uuid": "5b8a48c4-4697-436e-a04e-c692b7fbe906",
          "value": 3413
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ping",
          "properties": null,
          "uuid": "e8e2a099-e1e9-480f-8a05-cac057c02bdf",
          "value": 3414
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "trace",
          "properties": null,
          "uuid": "40ef7c9f-6ce9-439d-874a-79da9eed93da",
          "value": 3415
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
      "export_key": "__function/mx_argument",
      "hide_notification": false,
      "id": 2920,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mx_argument",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mx_argument",
      "tooltip": "Argument is specific to the command selection",
      "type_id": 11,
      "uuid": "013b764d-909f-40be-8a65-bf8278418b61",
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
      "created_date": 1742815030838,
      "description": {
        "content": "MxToolbox function makes an MxToolBox API request to execute an MX command and returns the results.",
        "format": "text"
      },
      "destination_handle": "fn_mxtoolbox",
      "display_name": "MXToolbox",
      "export_key": "fn_mxtoolbox",
      "id": 290,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1742815030838,
      "name": "fn_mxtoolbox",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d472cb96-1e55-4bb8-aacd-e78402d101b0",
      "version": 0,
      "view_items": [
        {
          "content": "ca88493d-a9a7-4a4a-8af8-b3cdf0989c99",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "013b764d-909f-40be-8a65-bf8278418b61",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3f7def1-ebe3-48f3-9d78-47eaeba7863b",
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
          "name": "Example: MXToolbox MX query",
          "object_type": "artifact",
          "programmatic_name": "example_mxtoolbox_mx_query",
          "tags": [],
          "uuid": null,
          "workflow_id": 397
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 71,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1742834675543,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1742834675543,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "dc6d9065-4b61-4465-8352-fd8fe2cfc69b"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_mxtoolbox",
      "name": "fn_mxtoolbox",
      "programmatic_name": "fn_mxtoolbox",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "67bec660-a9b6-4358-8b69-062c42a173fb"
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
        "version": 9,
        "workflow_id": "example_mxtoolbox_mx_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_mxtoolbox_mx_query\" isExecutable=\"true\" name=\"Example: MXToolbox MX query\"\u003e\u003cdocumentation\u003eQuery MX record. Create a note containing the Reporting Name Server and an artifact for each IP address.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rlopwq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1h7z5uq\" name=\"MXToolbox\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d472cb96-1e55-4bb8-aacd-e78402d101b0\"\u003e{\"inputs\":{\"ca88493d-a9a7-4a4a-8af8-b3cdf0989c99\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"267f420b-dcca-4740-9d54-933d03bca8b7\"}}},\"post_processing_script\":\"# Put the ReportingNameServer in a note\\ncontent = \u0027MxToolbox MX Query Result: Reporting Name Server: {}\\\\n\u0027.format(results[\u0027value\u0027][\u0027ReportingNameServer\u0027])\\nnote = helper.createPlainText(content)\\nincident.addNote(note)\\n\\n# Create artifacts for each IP Address\\nfor info in results[\u0027value\u0027][\u0027Information\u0027]:\\n  incident.addArtifact(\u0027IP Address\u0027, info[\u0027IP Address\u0027], info[\u0027Hostname\u0027])\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.mx_argument = artifact.value\\ninputs.mx_param1 = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rlopwq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ls9jyg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1rlopwq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1h7z5uq\"/\u003e\u003cendEvent id=\"EndEvent_0yc8i0l\"\u003e\u003cincoming\u003eSequenceFlow_0ls9jyg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ls9jyg\" sourceRef=\"ServiceTask_1h7z5uq\" targetRef=\"EndEvent_0yc8i0l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0en2ch4\"\u003e\u003ctext\u003eInput: MxToolbox mx command; artifact value is argument to mx command;\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_067xhcj\" sourceRef=\"ServiceTask_1h7z5uq\" targetRef=\"TextAnnotation_0en2ch4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0dgfiy5\"\u003e\u003ctext\u003eResults: Incident note created containing Reporting Name Server;\nArtifacts created for each IP Address\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15vfkxv\" sourceRef=\"ServiceTask_1h7z5uq\" targetRef=\"TextAnnotation_0dgfiy5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"303\" y=\"165\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"298\" y=\"200\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"187\" y=\"257\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"310\" y=\"197\"/\u003e\u003comgdi:waypoint x=\"253\" y=\"257\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1h7z5uq\" id=\"ServiceTask_1h7z5uq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"454\" y=\"143\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rlopwq\" id=\"SequenceFlow_1rlopwq_di\"\u003e\u003comgdi:waypoint x=\"339\" y=\"183\"/\u003e\u003comgdi:waypoint x=\"454\" y=\"183\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"351.5\" y=\"162\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0yc8i0l\" id=\"EndEvent_0yc8i0l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"645\" y=\"165\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"0\" x=\"663\" y=\"205\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ls9jyg\" id=\"SequenceFlow_0ls9jyg_di\"\u003e\u003comgdi:waypoint x=\"554\" y=\"183\"/\u003e\u003comgdi:waypoint x=\"645\" y=\"183\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"554.5\" y=\"162\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0en2ch4\" id=\"TextAnnotation_0en2ch4_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"241\" x=\"113\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_067xhcj\" id=\"Association_067xhcj_di\"\u003e\u003comgdi:waypoint x=\"454\" y=\"163\"/\u003e\u003comgdi:waypoint x=\"276\" y=\"91\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0dgfiy5\" id=\"TextAnnotation_0dgfiy5_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"293\" x=\"596\" y=\"59\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15vfkxv\" id=\"Association_15vfkxv_di\"\u003e\u003comgdi:waypoint x=\"554\" y=\"160\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"89\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "Query MX record. Create a note containing the Reporting Name Server and an artifact for each IP address.",
      "export_key": "example_mxtoolbox_mx_query",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1742834612866,
      "name": "Example: MXToolbox MX query",
      "object_type": "artifact",
      "programmatic_name": "example_mxtoolbox_mx_query",
      "tags": [],
      "uuid": "34d22adc-7884-4761-98f9-4b292e53648a",
      "workflow_id": 397
    }
  ],
  "workspaces": []
}
