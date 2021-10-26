{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx get devices",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "57789c28-de6a-46b4-8819-16ea53859de6",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_devices"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1634749309896,
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
      "export_key": "__function/extrahop_device_id",
      "hide_notification": false,
      "id": 503,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_device_id",
      "tooltip": "Extrahop devide ID",
      "type_id": 11,
      "uuid": "72f4b927-f617-4ee7-8c37-841a1a113062",
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
      "created_date": 1634229838220,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get or search for devices information from Extrahop Reveal(x) . Optional parameter extrahop_device_id",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx get devices",
      "export_key": "funct_extrahop_rx_get_devices",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1634749080120,
      "name": "funct_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "75447029-32ca-4363-b753-bc970cee66d5",
      "version": 4,
      "view_items": [
        {
          "content": "72f4b927-f617-4ee7-8c37-841a1a113062",
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
          "name": "Example: Extrahop revealx get devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_devices",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 2,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1634749279244,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1634749279244,
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
      "export_key": "extrahop",
      "name": "extrahop",
      "programmatic_name": "extrahop",
      "tags": [],
      "users": [],
      "uuid": "f81b5729-e662-495a-8b49-b2c934b5c26e"
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
        "version": 3,
        "workflow_id": "wf_extrahop_rx_get_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx get devices\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lf3pjh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16ic9ye\" name=\"Extrahop revealx get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{}}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lf3pjh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10jo0yc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lf3pjh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16ic9ye\"/\u003e\u003cendEvent id=\"EndEvent_1tnn5yc\"\u003e\u003cincoming\u003eSequenceFlow_10jo0yc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10jo0yc\" sourceRef=\"ServiceTask_16ic9ye\" targetRef=\"EndEvent_1tnn5yc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16ic9ye\" id=\"ServiceTask_16ic9ye_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lf3pjh\" id=\"SequenceFlow_1lf3pjh_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tnn5yc\" id=\"EndEvent_1tnn5yc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"427\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"445\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10jo0yc\" id=\"SequenceFlow_10jo0yc_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@a.com",
      "description": "",
      "export_key": "wf_extrahop_rx_get_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1634230530731,
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "c0ea7fdb-37a1-4f70-92a1-2c427ea93232",
      "workflow_id": 2
    }
  ],
  "workspaces": []
}
