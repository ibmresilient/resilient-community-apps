{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Siemplify Sync Case",
      "id": 152,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Siemplify Sync Case",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "a85325b8-39cf-41e2-980a-dea32e63046a",
      "view_items": [],
      "workflows": [
        "siemplify_sync_case"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1638636099330,
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
      "export_key": "__function/siemplify_sync_comments",
      "hide_notification": false,
      "id": 2426,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_comments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_sync_comments",
      "tooltip": "Set to Yes to sync comments to Siemplify",
      "type_id": 11,
      "uuid": "ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97",
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
      "export_key": "__function/siemplify_sync_artifacts",
      "hide_notification": false,
      "id": 2427,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_artifacts",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_sync_artifacts",
      "tooltip": "Set to Yes to sync artifacts to Siemplify",
      "type_id": 11,
      "uuid": "dd93eb58-531b-4807-8ea8-4471b70e204d",
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
      "export_key": "__function/siemplify_incident_id",
      "hide_notification": false,
      "id": 2425,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "75be91fc-7719-4339-a332-d87a55a14e3d",
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
      "export_key": "__function/siemplify_sync_attachments",
      "hide_notification": false,
      "id": 2428,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "siemplify_sync_attachments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "siemplify_sync_attachments",
      "tooltip": "Set to Yes to sync attachments to Siemplify",
      "type_id": 11,
      "uuid": "7b6dde8b-b1f0-476c-a442-f8e7cd706a34",
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
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Sync a SOAR Case to Siemplify",
        "format": "text"
      },
      "destination_handle": "fn_siemplify",
      "display_name": "Siemplify: Sync Case",
      "export_key": "siemplify_sync_case",
      "id": 372,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1638635863961,
      "name": "siemplify_sync_case",
      "tags": [],
      "uuid": "bf1b6ee8-4853-4a6a-8c21-808446de4c80",
      "version": 1,
      "view_items": [
        {
          "content": "75be91fc-7719-4339-a332-d87a55a14e3d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dd93eb58-531b-4807-8ea8-4471b70e204d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7b6dde8b-b1f0-476c-a442-f8e7cd706a34",
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
          "name": "Siemplify Sync Case",
          "object_type": "incident",
          "programmatic_name": "siemplify_sync_case",
          "tags": [],
          "uuid": null,
          "workflow_id": 147
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 66,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1638636095919,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1638636095919,
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
      "export_key": "fn_siemplify",
      "name": "fn_siemplify",
      "programmatic_name": "fn_siemplify",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "a4fe1c3e-9dff-436c-ba62-1ab465008259"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6328,
    "major": 39,
    "minor": 0,
    "version": "39.0.6328"
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
        "workflow_id": "siemplify_sync_case",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"siemplify_sync_case\" isExecutable=\"true\" name=\"Siemplify Sync Case\"\u003e\u003cdocumentation\u003eSync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_133ewo1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ao7iqd\" name=\"Siemplify: Sync Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bf1b6ee8-4853-4a6a-8c21-808446de4c80\"\u003e{\"inputs\":{\"ab66d425-a3e0-4fed-b99e-0fd7ce3e1b97\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"dd93eb58-531b-4807-8ea8-4471b70e204d\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}},\"7b6dde8b-b1f0-476c-a442-f8e7cd706a34\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.siemplify_incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_133ewo1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14vcfso\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_133ewo1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ao7iqd\"/\u003e\u003cendEvent id=\"EndEvent_04a6awv\"\u003e\u003cincoming\u003eSequenceFlow_14vcfso\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14vcfso\" sourceRef=\"ServiceTask_0ao7iqd\" targetRef=\"EndEvent_04a6awv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ao7iqd\" id=\"ServiceTask_0ao7iqd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"274\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_133ewo1\" id=\"SequenceFlow_133ewo1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04a6awv\" id=\"EndEvent_04a6awv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"443\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"461\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14vcfso\" id=\"SequenceFlow_14vcfso_di\"\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"443\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"408.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "a@example.com",
      "description": "Sync a SOAR Case to Siemplify, specifying the additional synchronization of artifacts, attachments and comments",
      "export_key": "siemplify_sync_case",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1638636009469,
      "name": "Siemplify Sync Case",
      "object_type": "incident",
      "programmatic_name": "siemplify_sync_case",
      "tags": [],
      "uuid": "43ab935d-a6dd-4c48-b44f-00b059891799",
      "workflow_id": 147
    }
  ],
  "workspaces": []
}
