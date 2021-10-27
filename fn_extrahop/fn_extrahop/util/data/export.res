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
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop revealx search devices",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "60bf1021-e9f0-4395-bdaf-08e9006c4db0",
      "view_items": [
        {
          "content": "183c411d-c4e5-4995-a711-e58f2ea40221",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_devices"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1635351818889,
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
      "export_key": "__function/extrahop_active_from",
      "hide_notification": false,
      "id": 548,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_active_from",
      "tooltip": "(Optional) The beginning timestamp for the request. Return only devices active after this time. Time is expressed in milliseconds since the epoch. 0 indicates the time of the request.",
      "type_id": 11,
      "uuid": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
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
      "export_key": "__function/extrahop_offset",
      "hide_notification": false,
      "id": 551,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_offset",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_offset",
      "tooltip": "(Optional) Skip the specified number of devices. This parameter is often combined with the limit parameter to paginate result sets.",
      "type_id": 11,
      "uuid": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
      "export_key": "__function/extrahop_search_filter",
      "hide_notification": false,
      "id": 536,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_search_filter",
      "tooltip": "The  filter criteria for Extrahop search results.",
      "type_id": 11,
      "uuid": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
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
      "export_key": "__function/extrahop_limit",
      "hide_notification": false,
      "id": 550,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_limit",
      "tooltip": "(Optional) Limit the number of devices returned to the specified maximum number.",
      "type_id": 11,
      "uuid": "64a89cad-9373-4017-ba04-d06f97a28e8c",
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
      "export_key": "__function/extrahop_active_until",
      "hide_notification": false,
      "id": 549,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_until",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "extrahop_active_until",
      "tooltip": "(Optional) The ending timestamp for the request. Return only devices active before this time.",
      "type_id": 11,
      "uuid": "68a4691f-8609-4d19-9208-3a7589a37997",
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
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/extrahop_search_filter",
      "hide_notification": false,
      "id": 540,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{   \"filter\": {     \"field\": \"string\",     \"operator\": \"string\",     \"operand\": \"string\",     \"rules\": []   } }",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Extrahop search filter",
      "tooltip": "",
      "type_id": 6,
      "uuid": "183c411d-c4e5-4995-a711-e58f2ea40221",
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
        "content": "Get devices information from Extrahop Reveal(x) . Optional parameters  device_id, active_from, active_util, limit and offset",
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
      "last_modified_time": 1635350284830,
      "name": "funct_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "75447029-32ca-4363-b753-bc970cee66d5",
      "version": 10,
      "view_items": [
        {
          "content": "72f4b927-f617-4ee7-8c37-841a1a113062",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
    },
    {
      "created_date": 1635258053984,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for devices information from Extrahop Reveal(x). Optional parameter search_filter, active_from, active_util, limit and offset",
        "format": "text"
      },
      "destination_handle": "extrahop",
      "display_name": "Extrahop revealx search devices",
      "export_key": "funct_extrahop_rx_search_devices",
      "id": 35,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1635350072177,
      "name": "funct_extrahop_rx_search_devices",
      "tags": [],
      "uuid": "e7384abd-0046-4b46-97af-d34d8cc9c711",
      "version": 10,
      "view_items": [
        {
          "content": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
          "name": "Example: Extrahop revealx search devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_devices",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 44,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1635351809217,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1635351809217,
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
      "users": [
        "a@a.com"
      ],
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
        "version": 7,
        "workflow_id": "wf_extrahop_rx_get_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx get devices\"\u003e\u003cdocumentation\u003eGet devices information from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1lf3pjh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16ic9ye\" name=\"Extrahop revealx get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lf3pjh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10jo0yc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1lf3pjh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16ic9ye\"/\u003e\u003cendEvent id=\"EndEvent_1tnn5yc\"\u003e\u003cincoming\u003eSequenceFlow_10jo0yc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10jo0yc\" sourceRef=\"ServiceTask_16ic9ye\" targetRef=\"EndEvent_1tnn5yc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16ic9ye\" id=\"ServiceTask_16ic9ye_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lf3pjh\" id=\"SequenceFlow_1lf3pjh_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tnn5yc\" id=\"EndEvent_1tnn5yc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"427\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"445\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10jo0yc\" id=\"SequenceFlow_10jo0yc_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Get devices information from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1635349708067,
      "name": "Example: Extrahop revealx get devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_devices",
      "tags": [],
      "uuid": "c0ea7fdb-37a1-4f70-92a1-2c427ea93232",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "wf_extrahop_rx_search_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_devices\" isExecutable=\"true\" name=\"Example: Extrahop revealx search devices\"\u003e\u003cdocumentation\u003eSearch for devices information from Extrahop Reveal(x) using a filter.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0m2u56o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10yatj6\" name=\"Extrahop revealx search devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7384abd-0046-4b46-97af-d34d8cc9c711\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_search_filter = rule.properties.extrahop_search_filter.content\\nif inputs.extrahop_search_filter is None:\\n    raise ValueError(\\\"The search filter is not set\\\")\\nfor prop in [\\\"filter\\\", \\\"field\\\", \\\"operator\\\", \\\"operand\\\"]:\\n  if prop not in inputs.extrahop_search_filter:\\n    raise ValueError(\\\"The search filter is missing property \u0027{}\u0027\\\".format(prop))\\ninputs.extrahop_limit = 100\\ninputs.extrahop_offset = 100\\n\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0m2u56o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081bn3v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0m2u56o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_10yatj6\"/\u003e\u003cendEvent id=\"EndEvent_0t2xr17\"\u003e\u003cincoming\u003eSequenceFlow_081bn3v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081bn3v\" sourceRef=\"ServiceTask_10yatj6\" targetRef=\"EndEvent_0t2xr17\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10yatj6\" id=\"ServiceTask_10yatj6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0m2u56o\" id=\"SequenceFlow_0m2u56o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0t2xr17\" id=\"EndEvent_0t2xr17_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"375\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081bn3v\" id=\"SequenceFlow_081bn3v_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"355\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "creator_id": "a@a.com",
      "description": "Search for devices information from Extrahop Reveal(x) using a filter.",
      "export_key": "wf_extrahop_rx_search_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1635349737446,
      "name": "Example: Extrahop revealx search devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_devices",
      "tags": [],
      "uuid": "7d82fa2a-339c-4306-9a2c-ab4886101e2e",
      "workflow_id": 3
    }
  ],
  "workspaces": []
}
