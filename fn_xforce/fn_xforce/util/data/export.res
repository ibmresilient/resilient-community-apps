{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1684320457068,
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
      "export_key": "__function/xforce_collection_type",
      "hide_notification": false,
      "id": 4368,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_collection_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_collection_type",
      "tooltip": "Which type of collections to search. Public or private collections available.",
      "type_id": 11,
      "uuid": "ce99b64a-5259-439c-ab60-7137f3b88806",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "public",
          "properties": null,
          "uuid": "022ba2a8-90d6-433e-bea4-e2cc8ca0bb74",
          "value": 870
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "private",
          "properties": null,
          "uuid": "6f57b1c6-d066-4185-b317-8161d877389b",
          "value": 871
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
      "export_key": "__function/xforce_collection_id",
      "hide_notification": false,
      "id": 4367,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_collection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_collection_id",
      "tooltip": "A collection ID for use with the XForce API",
      "type_id": 11,
      "uuid": "55c686a5-4611-40ba-bc87-2524141760e1",
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
      "export_key": "__function/xforce_query",
      "hide_notification": false,
      "id": 4369,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_query",
      "tooltip": "A query to submit for searching XForce Collections",
      "type_id": 11,
      "uuid": "6439ec40-9c26-475e-9abe-b738422ca9d0",
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
      "created_date": 1683566156016,
      "description": {
        "content": "A function that takes in a parameter of a xforce_collection_id and then submits this to the X-Force API to gather data for the provided case.",
        "format": "text"
      },
      "destination_handle": "fn_xforce",
      "display_name": "X-Force Utilities: Get Collection by ID",
      "export_key": "xforce_get_collection_by_id",
      "id": 29,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683566156059,
      "name": "xforce_get_collection_by_id",
      "tags": [],
      "uuid": "b792f6ec-2dac-439e-9504-15cf23061499",
      "version": 1,
      "view_items": [
        {
          "content": "55c686a5-4611-40ba-bc87-2524141760e1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": []
    },
    {
      "created_date": 1683566156086,
      "description": {
        "content": "A function that allows a user to submit a query to the X-Force Collections API. Supports searching either public or private collections.",
        "format": "text"
      },
      "destination_handle": "fn_xforce",
      "display_name": "X-Force Utilities: Query Collection",
      "export_key": "xforce_query_collection",
      "id": 30,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683566156127,
      "name": "xforce_query_collection",
      "tags": [],
      "uuid": "a6473838-d1fe-4d40-b284-c48d3b6a91f6",
      "version": 1,
      "view_items": [
        {
          "content": "6439ec40-9c26-475e-9abe-b738422ca9d0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ce99b64a-5259-439c-ab60-7137f3b88806",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": []
    }
  ],
  "geos": null,
  "groups": null,
  "id": 29,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1684320455926,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1684320455926,
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
      "export_key": "fn_xforce",
      "name": "fn_xforce",
      "programmatic_name": "fn_xforce",
      "tags": [],
      "users": [
        "g@example.com"
      ],
      "uuid": "9125153a-7a5d-4ba2-b963-701cc6f8a3d0"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 14,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b\" isExecutable=\"true\" name=\"playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0be43t4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"X-Force Utilities: Get Collection by ID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.xforce_collection_id = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"collection_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0be43t4\u003c/incoming\u003e\u003coutgoing\u003eFlow_15txe4o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0be43t4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_02cxowy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_15txe4o\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"collection output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"722fead1-b185-45ea-8a0f-ca95867d4264\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_15txe4o\u003c/incoming\u003e\u003coutgoing\u003eFlow_02cxowy\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_02cxowy\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_15txe4o\" id=\"Flow_15txe4o_di\"\u003e\u003comgdi:waypoint x=\"690\" y=\"-88\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"-42\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0be43t4\" id=\"Flow_0be43t4_di\"\u003e\u003comgdi:waypoint x=\"690\" y=\"-224\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"-172\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02cxowy\" id=\"Flow_02cxowy_di\"\u003e\u003comgdi:waypoint x=\"690\" y=\"42\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"599\" y=\"-276\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"592\" y=\"-172\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"624\" y=\"94\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"591.5\" y=\"-42\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683631724904,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b",
      "description": {
        "content": "Takes in a parameter of a xforce_collection_id and then attempts to gather enriching information for that collection via the X-Force API.",
        "format": "text"
      },
      "display_name": "Example: X-Force Query Collection by ID (PB)",
      "export_key": "example_xforce_query_collection_by_id",
      "field_type_handle": "playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b",
      "fields_type": {
        "actions": [],
        "display_name": "Example: X-Force Query Collection by ID (PB)",
        "export_key": "playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b",
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
        "type_name": "playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b",
        "uuid": "616fe06e-29db-4838-8a03-eefa40f0e9f7"
      },
      "has_logical_errors": false,
      "id": 24,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683637615328,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683637606466,
          "description": "",
          "enabled": false,
          "export_key": "collection output",
          "id": 52,
          "language": "python3",
          "last_modified_by": "g@example.com",
          "last_modified_time": 1683637606503,
          "name": "collection output",
          "object_type": "artifact",
          "playbook_handle": "example_xforce_query_collection_by_id",
          "programmatic_name": "example_xforce_query_collection_by_id_collection_output",
          "script_text": "results = playbook.functions.results.collection_results\nif results.get(\"success\"):\n  content = results.get(\"content\", {})\n  if content.get(\"contents\"):\n    noteText = f\"\"\"\u003cb\u003eTitle:\u003c/b\u003e {content.get(\u0027title\u0027)}\n    \u003cb\u003eCreated:\u003c/b\u003e {content.get(\u0027created\u0027)}\n    \u003cb\u003eTags:\u003c/b\u003e {content.get(\u0027tags\u0027)}\n    \n    {content.get(\u0027contents\u0027, {}).get(\u0027wiki\u0027)}\n    \"\"\"\n    incident.addNote(noteText)\n  else:\n   incident.addNote(content)",
          "tags": [],
          "uuid": "722fead1-b185-45ea-8a0f-ca95867d4264"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "in",
              "type": null,
              "value": [
                "IP Address",
                "DNS Name",
                "URL",
                "Malware MD5 Hash",
                "Malware SHA-1 Hash",
                "String",
                "Malware SHA-256 Hash"
              ]
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_xforce_query_collection_by_id",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8c244a13-1a74-4c2f-b727-74243e52bc7b",
        "id": 24,
        "name": "playbook_8c244a13_1a74_4c2f_b727_74243e52bc7b",
        "type": "playbook",
        "uuid": "97081f3f-3ee2-4f9d-a3fa-4a7468fb9acb"
      },
      "tags": [],
      "type": "default",
      "uuid": "8c244a13-1a74-4c2f-b727-74243e52bc7b",
      "version": 24
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_83930999_45ff_4d39_a347_8456a29c2a23\" isExecutable=\"true\" name=\"playbook_83930999_45ff_4d39_a347_8456a29c2a23\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1be04nh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"X-Force Utilities: Query Collection\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a6473838-d1fe-4d40-b284-c48d3b6a91f6\"\u003e{\"inputs\":{\"6439ec40-9c26-475e-9abe-b738422ca9d0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"ce99b64a-5259-439c-ab60-7137f3b88806\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"022ba2a8-90d6-433e-bea4-e2cc8ca0bb74\"}}},\"pre_processing_script\":\"inputs.xforce_query = artifact.value\\ninputs.xforce_collection_type = \\\"private\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"query_collections_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1be04nh\u003c/incoming\u003e\u003coutgoing\u003eFlow_0m32q8z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1be04nh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"query collections output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"6a9eb993-d3ad-4963-9c97-0a384a862864\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0m32q8z\u003c/incoming\u003e\u003coutgoing\u003eFlow_1h56yi3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0m32q8z\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1h56yi3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1h56yi3\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_83930999_45ff_4d39_a347_8456a29c2a23\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1h56yi3\" id=\"Flow_1h56yi3_di\"\u003e\u003comgdi:waypoint x=\"630\" y=\"92\"/\u003e\u003comgdi:waypoint x=\"630\" y=\"154\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0m32q8z\" id=\"Flow_0m32q8z_di\"\u003e\u003comgdi:waypoint x=\"630\" y=\"-38\"/\u003e\u003comgdi:waypoint x=\"630\" y=\"8\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1be04nh\" id=\"Flow_1be04nh_di\"\u003e\u003comgdi:waypoint x=\"630\" y=\"-184\"/\u003e\u003comgdi:waypoint x=\"630\" y=\"-122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"539\" y=\"-236\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"532\" y=\"-122\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"532\" y=\"8\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"564\" y=\"154\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683631748363,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_83930999_45ff_4d39_a347_8456a29c2a23",
      "description": {
        "content": "takes in a provided artifact as a query and then submits this to the X-Force API searching collections for casefiles relevant to the query.",
        "format": "text"
      },
      "display_name": "Example: X-Force Query from Artifact (PB)",
      "export_key": "example_xforce_query_from_artifact_pb",
      "field_type_handle": "playbook_83930999_45ff_4d39_a347_8456a29c2a23",
      "fields_type": {
        "actions": [],
        "display_name": "Example: X-Force Query from Artifact (PB)",
        "export_key": "playbook_83930999_45ff_4d39_a347_8456a29c2a23",
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
        "type_name": "playbook_83930999_45ff_4d39_a347_8456a29c2a23",
        "uuid": "7156a300-db57-41ca-b5b3-ef65a7239ea4"
      },
      "has_logical_errors": false,
      "id": 25,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683637548574,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "in",
              "type": null,
              "value": [
                "IP Address",
                "DNS Name",
                "URL",
                "Malware MD5 Hash",
                "Malware SHA-1 Hash",
                "String",
                "Malware SHA-256 Hash"
              ]
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_xforce_query_from_artifact_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_83930999-45ff-4d39-a347-8456a29c2a23",
        "id": 25,
        "name": "playbook_83930999_45ff_4d39_a347_8456a29c2a23",
        "type": "playbook",
        "uuid": "eca229e2-2adc-4bb1-9a67-aeb35def80a3"
      },
      "tags": [],
      "type": "default",
      "uuid": "83930999-45ff-4d39-a347-8456a29c2a23",
      "version": 15
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 16,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141\" isExecutable=\"true\" name=\"playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_15l9d9q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"X-Force Utilities: Query Collection\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a6473838-d1fe-4d40-b284-c48d3b6a91f6\"\u003e{\"inputs\":{\"6439ec40-9c26-475e-9abe-b738422ca9d0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"ce99b64a-5259-439c-ab60-7137f3b88806\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"022ba2a8-90d6-433e-bea4-e2cc8ca0bb74\"}}},\"pre_processing_script\":\"inputs.xforce_query = artifact.value\\ninputs.xforce_collection_type = \\\"public\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"query_collections_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_15l9d9q\u003c/incoming\u003e\u003coutgoing\u003eFlow_0504r97\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_15l9d9q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"query collections output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"6a9eb993-d3ad-4963-9c97-0a384a862864\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0504r97\u003c/incoming\u003e\u003coutgoing\u003eFlow_18w8pe6\u003c/outgoing\u003e\u003coutgoing\u003eFlow_131xyd0\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0bw122n\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"X-Force Utilities: Get Collection by ID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"pre_processing_script\":\"results = playbook.functions.results.query_collections_results\\ninputs.xforce_collection_id = results.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[1].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"collection2_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0158qt9\u003c/incoming\u003e\u003coutgoing\u003eFlow_0uapfot\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"X-Force Utilities: Get Collection by ID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"pre_processing_script\":\"results = playbook.functions.results.query_collections_results\\ninputs.xforce_collection_id = results.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[2].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"collection3_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0q8pch8\u003c/incoming\u003e\u003coutgoing\u003eFlow_105wgrf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"X-Force Utilities: Get Collection by ID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"pre_processing_script\":\"results = playbook.functions.results.query_collections_results\\ninputs.xforce_collection_id = results.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[0].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"collection1_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1jqhax1\u003c/incoming\u003e\u003coutgoing\u003eFlow_0hi0lbq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0hi0lbq\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_15\"/\u003e\u003csequenceFlow id=\"Flow_0uapfot\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_13\"/\u003e\u003csequenceFlow id=\"Flow_105wgrf\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_14\"/\u003e\u003cendEvent id=\"EndPoint_11\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_18tiue2\u003c/incoming\u003e\u003cincoming\u003eFlow_1m6owu3\u003c/incoming\u003e\u003cincoming\u003eFlow_1xejeqd\u003c/incoming\u003e\u003cincoming\u003eFlow_0f9uki8\u003c/incoming\u003e\u003cincoming\u003eFlow_122k381\u003c/incoming\u003e\u003cincoming\u003eFlow_06ieobz\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_13\" name=\"collection 2\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8a5bc500-0c92-441b-9143-19cdcc7cee06\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0uapfot\u003c/incoming\u003e\u003coutgoing\u003eFlow_18tiue2\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_18tiue2\" sourceRef=\"ScriptTask_13\" targetRef=\"EndPoint_11\"/\u003e\u003cscriptTask id=\"ScriptTask_14\" name=\"collection 3\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"7ee91d02-addb-4b21-8a70-26e514cbbb93\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_105wgrf\u003c/incoming\u003e\u003coutgoing\u003eFlow_1xejeqd\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cscriptTask id=\"ScriptTask_15\" name=\"collection 1\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"81d81605-5977-4091-8be9-6985c871f4de\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0hi0lbq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1m6owu3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1m6owu3\" sourceRef=\"ScriptTask_15\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_1xejeqd\" sourceRef=\"ScriptTask_14\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_0504r97\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_0f9uki8\" id=\"ConditionPoint_16\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_18w8pe6\u003c/incoming\u003e\u003coutgoing\u003eFlow_1jqhax1\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0f9uki8\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cexclusiveGateway default=\"Flow_06ieobz\" id=\"ConditionPoint_17\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0bw122n\u003c/incoming\u003e\u003coutgoing\u003eFlow_0158qt9\u003c/outgoing\u003e\u003coutgoing\u003eFlow_06ieobz\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cexclusiveGateway default=\"Flow_122k381\" id=\"ConditionPoint_18\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_131xyd0\u003c/incoming\u003e\u003coutgoing\u003eFlow_0q8pch8\u003c/outgoing\u003e\u003coutgoing\u003eFlow_122k381\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_18w8pe6\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_16\"/\u003e\u003csequenceFlow id=\"Flow_131xyd0\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_18\"/\u003e\u003csequenceFlow id=\"Flow_0bw122n\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_17\"/\u003e\u003csequenceFlow id=\"Flow_1jqhax1\" name=\"Atleast 1 collection\" sourceRef=\"ConditionPoint_16\" targetRef=\"ServiceTask_5\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Atleast 1 collection\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.query_collections_results\\nif results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\", 0) \u0026gt; 0:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0f9uki8\" name=\"Else\" sourceRef=\"ConditionPoint_16\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_0q8pch8\" name=\"Atleast 3 collections\" sourceRef=\"ConditionPoint_18\" targetRef=\"ServiceTask_4\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Atleast 3 collections\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.query_collections_results\\nif results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\", 0) \u0026gt;= 3:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_122k381\" name=\"Else\" sourceRef=\"ConditionPoint_18\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_0158qt9\" name=\"Atleast 2 collections\" sourceRef=\"ConditionPoint_17\" targetRef=\"ServiceTask_3\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Atleast 2 collections\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.query_collections_results\\nif results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\", 0) \u0026gt;= 2:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_06ieobz\" name=\"Else\" sourceRef=\"ConditionPoint_17\" targetRef=\"EndPoint_11\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0f9uki8\" id=\"Flow_0f9uki8_di\"\u003e\u003comgdi:waypoint x=\"422\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"460\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"460\" y=\"510\"/\u003e\u003comgdi:waypoint x=\"574\" y=\"510\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"432\" y=\"3\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jqhax1\" id=\"Flow_1jqhax1_di\"\u003e\u003comgdi:waypoint x=\"300\" y=\"26\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"48\" x=\"276\" y=\"86\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_122k381\" id=\"Flow_122k381_di\"\u003e\u003comgdi:waypoint x=\"858\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"510\"/\u003e\u003comgdi:waypoint x=\"706\" y=\"510\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"808\" y=\"3\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0q8pch8\" id=\"Flow_0q8pch8_di\"\u003e\u003comgdi:waypoint x=\"980\" y=\"26\"/\u003e\u003comgdi:waypoint x=\"980\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"54\" x=\"953\" y=\"86\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06ieobz\" id=\"Flow_06ieobz_di\"\u003e\u003comgdi:waypoint x=\"518\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"0\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"510\"/\u003e\u003comgdi:waypoint x=\"574\" y=\"510\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"478\" y=\"3\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0158qt9\" id=\"Flow_0158qt9_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"26\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"178\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"54\" x=\"613\" y=\"86\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bw122n\" id=\"Flow_0bw122n_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"-108\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_131xyd0\" id=\"Flow_131xyd0_di\"\u003e\u003comgdi:waypoint x=\"738\" y=\"-150\"/\u003e\u003comgdi:waypoint x=\"980\" y=\"-150\"/\u003e\u003comgdi:waypoint x=\"980\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18w8pe6\" id=\"Flow_18w8pe6_di\"\u003e\u003comgdi:waypoint x=\"542\" y=\"-150\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"-150\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0504r97\" id=\"Flow_0504r97_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"-218\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"-192\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1xejeqd\" id=\"Flow_1xejeqd_di\"\u003e\u003comgdi:waypoint x=\"980\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"980\" y=\"510\"/\u003e\u003comgdi:waypoint x=\"706\" y=\"510\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1m6owu3\" id=\"Flow_1m6owu3_di\"\u003e\u003comgdi:waypoint x=\"300\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"510\"/\u003e\u003comgdi:waypoint x=\"574\" y=\"510\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18tiue2\" id=\"Flow_18tiue2_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"484\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_105wgrf\" id=\"Flow_105wgrf_di\"\u003e\u003comgdi:waypoint x=\"980\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"980\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0uapfot\" id=\"Flow_0uapfot_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0hi0lbq\" id=\"Flow_0hi0lbq_di\"\u003e\u003comgdi:waypoint x=\"300\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_15l9d9q\" id=\"Flow_15l9d9q_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"-324\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"-302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"549\" y=\"-376\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"542\" y=\"-302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"542\" y=\"-192\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"542\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"882\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"202\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_11\" id=\"EndPoint_11_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"574\" y=\"484\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_13\" id=\"ScriptTask_13_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"542.2\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_14\" id=\"ScriptTask_14_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"882\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_15\" id=\"ScriptTask_15_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"202\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_16\" id=\"ConditionPoint_16_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"178\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_17\" id=\"ConditionPoint_17_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"518\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_18\" id=\"ConditionPoint_18_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"858\" y=\"-26\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683631791115,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: X-Force Return Top 3 from Collection(s) (PB)",
      "export_key": "example_xforce_return_top_3_from_collections_pb",
      "field_type_handle": "playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141",
      "fields_type": {
        "actions": [],
        "display_name": "Example: X-Force Return Top 3 from Collection(s) (PB)",
        "export_key": "playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141",
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
        "type_name": "playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141",
        "uuid": "5e6b624a-0971-463d-9296-f0c4e1ab91a3"
      },
      "has_logical_errors": false,
      "id": 26,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683637903095,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683634694828,
          "description": "",
          "enabled": false,
          "export_key": "collection 1",
          "id": 51,
          "language": "python3",
          "last_modified_by": "g@example.com",
          "last_modified_time": 1683634729880,
          "name": "collection 1",
          "object_type": "artifact",
          "playbook_handle": "example_xforce_return_top_3_from_collections_pb",
          "programmatic_name": "example_xforce_return_top_3_from_collections_pb_collection_1",
          "script_text": "results = playbook.functions.results.collection1_results\n\nif results.get(\"success\"):\n  content = results.get(\"content\", {})\n  if content.get(\"contents\"):\n    noteText = f\"\"\"\u003cb\u003eTitle:\u003c/b\u003e {content.get(\u0027title\u0027)}\n    \u003cb\u003eCreated:\u003c/b\u003e {content.get(\u0027created\u0027)}\n    \u003cb\u003eTags:\u003c/b\u003e {content.get(\u0027tags\u0027)}\n    \n    {content.get(\u0027contents\u0027, {}).get(\u0027wiki\u0027)}\n    \"\"\"\n    incident.addNote(noteText)\n  else:\n   incident.addNote(content)",
          "tags": [],
          "uuid": "81d81605-5977-4091-8be9-6985c871f4de"
        },
        {
          "actions": [],
          "created_date": 1683634652449,
          "description": "",
          "enabled": false,
          "export_key": "collection 2",
          "id": 49,
          "language": "python3",
          "last_modified_by": "g@example.com",
          "last_modified_time": 1683634738625,
          "name": "collection 2",
          "object_type": "artifact",
          "playbook_handle": "example_xforce_return_top_3_from_collections_pb",
          "programmatic_name": "example_xforce_return_top_3_from_collections_pb_collection_2",
          "script_text": "results = playbook.functions.results.collection2_results\n\nif results.get(\"success\"):\n  content = results.get(\"content\", {})\n  if content.get(\"contents\"):\n    noteText = f\"\"\"\u003cb\u003eTitle:\u003c/b\u003e {content.get(\u0027title\u0027)}\n    \u003cb\u003eCreated:\u003c/b\u003e {content.get(\u0027created\u0027)}\n    \u003cb\u003eTags:\u003c/b\u003e {content.get(\u0027tags\u0027)}\n    \n    {content.get(\u0027contents\u0027, {}).get(\u0027wiki\u0027)}\n    \"\"\"\n    incident.addNote(noteText)\n  else:\n   incident.addNote(content)",
          "tags": [],
          "uuid": "8a5bc500-0c92-441b-9143-19cdcc7cee06"
        },
        {
          "actions": [],
          "created_date": 1683634672204,
          "description": "",
          "enabled": false,
          "export_key": "collection 3",
          "id": 50,
          "language": "python3",
          "last_modified_by": "g@example.com",
          "last_modified_time": 1683634749794,
          "name": "collection 3",
          "object_type": "artifact",
          "playbook_handle": "example_xforce_return_top_3_from_collections_pb",
          "programmatic_name": "example_xforce_return_top_3_from_collections_pb_collection_3",
          "script_text": "results = playbook.functions.results.collection3_results\n\nif results.get(\"success\"):\n  content = results.get(\"content\", {})\n  if content.get(\"contents\"):\n    noteText = f\"\"\"\u003cb\u003eTitle:\u003c/b\u003e {content.get(\u0027title\u0027)}\n    \u003cb\u003eCreated:\u003c/b\u003e {content.get(\u0027created\u0027)}\n    \u003cb\u003eTags:\u003c/b\u003e {content.get(\u0027tags\u0027)}\n    \n    {content.get(\u0027contents\u0027, {}).get(\u0027wiki\u0027)}\n    \"\"\"\n    incident.addNote(noteText)\n  else:\n   incident.addNote(content)",
          "tags": [],
          "uuid": "7ee91d02-addb-4b21-8a70-26e514cbbb93"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "in",
              "type": null,
              "value": [
                "IP Address",
                "DNS Name",
                "URL",
                "Malware MD5 Hash",
                "Malware SHA-1 Hash",
                "String",
                "Malware SHA-256 Hash"
              ]
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_xforce_return_top_3_from_collections_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_9f1ee96c-1c24-41b1-b5fc-ee7d8d57e141",
        "id": 26,
        "name": "playbook_9f1ee96c_1c24_41b1_b5fc_ee7d8d57e141",
        "type": "playbook",
        "uuid": "1dcfb480-5d92-4ce1-ab5f-b3197a2fc773"
      },
      "tags": [],
      "type": "default",
      "uuid": "9f1ee96c-1c24-41b1-b5fc-ee7d8d57e141",
      "version": 21
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1683632895245,
      "description": "",
      "enabled": false,
      "export_key": "query collections output",
      "id": 47,
      "language": "python3",
      "last_modified_by": "g@example.com",
      "last_modified_time": 1683637530368,
      "name": "query collections output",
      "object_type": "artifact",
      "playbook_handle": null,
      "programmatic_name": "example_xforce_query_from_artifact_pb_query_collections_output",
      "script_text": "results = playbook.functions.results.query_collections_results\nif results.get(\"success\"):\n  content = results.get(\"content\", {})\n  if content.get(\"num_of_casefiles\") \u003e 0:\n    noteText = \"\"\"\u003cb\u003eX-Force Query status\u003c/b\u003e\u003cbr\u003eTotal matched case files: \u003cb\u003e{}\u003c/b\u003e\"\"\".format(content.get(\"num_of_casefiles\", 0))\n    incident.addNote(helper.createRichText(noteText))\n  else:\n    noteText = \"\"\"\u003cb\u003eX-Force Query status\u003c/b\u003e\u003cbr\u003e{}\"\"\".format(content)\n    incident.addNote(helper.createRichText(noteText))",
      "tags": [],
      "uuid": "6a9eb993-d3ad-4963-9c97-0a384a862864"
    }
  ],
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
