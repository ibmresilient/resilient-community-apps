{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1742494667713,
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
      "export_key": "__function/greynoise_value",
      "hide_notification": false,
      "id": 2906,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "greynoise_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "greynoise_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b5caca14-688a-4a2d-9c7c-09c1c578bbcd",
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
      "export_key": "__function/greynoise_type",
      "hide_notification": false,
      "id": 2907,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "greynoise_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "greynoise_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5122154c-c377-435e-9baf-ea79ebc6e601",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "context",
          "properties": null,
          "uuid": "5eb47553-7819-4d10-bdc9-994fc3dd3094",
          "value": 3370
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "quick",
          "properties": null,
          "uuid": "1237dd73-222a-4569-875f-caf281f436c2",
          "value": 3371
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "community",
          "properties": null,
          "uuid": "30998522-adc0-4600-9958-2e354afbd2b2",
          "value": 3375
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
      "created_date": 1742397377880,
      "description": {
        "content": "Perform IP Address analysis",
        "format": "text"
      },
      "destination_handle": "fn_greynoise",
      "display_name": "GreyNoise IP Query",
      "export_key": "greynoise_ip_query",
      "id": 284,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "last_modified_time": 1742397377880,
      "name": "greynoise_ip_query",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "4cdf2cff-89ae-4004-be1a-b40c1f8e85be",
      "version": 0,
      "view_items": [
        {
          "content": "b5caca14-688a-4a2d-9c7c-09c1c578bbcd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5122154c-c377-435e-9baf-ea79ebc6e601",
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
      "created_date": 1742493465401,
      "description": {
        "content": "Perform IP Address analysis",
        "format": "text"
      },
      "destination_handle": "fn_greynoise",
      "display_name": "GreyNoise IP Query Community",
      "export_key": "greynoise_ip_query_community",
      "id": 289,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "last_modified_time": 1742493465401,
      "name": "greynoise_ip_query_community",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c0fb4a33-4b7a-4a8b-946e-b7bea8c87e65",
      "version": 0,
      "view_items": [
        {
          "content": "5122154c-c377-435e-9baf-ea79ebc6e601",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b5caca14-688a-4a2d-9c7c-09c1c578bbcd",
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
  "id": 61,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1742494664990,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1742494664990,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3a78f053-8182-4eef-9ac9-15e14371e8b5"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_greynoise",
      "name": "fn_greynoise",
      "programmatic_name": "fn_greynoise",
      "tags": [],
      "users": [
        "sysadmin@example.com"
      ],
      "uuid": "cdd6b18c-e7f0-464a-a078-e29da5d92502"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_f227cce8_32de_4ccc_869f_d47b9024e63a\" isExecutable=\"true\" name=\"playbook_f227cce8_32de_4ccc_869f_d47b9024e63a\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0wprx2d\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"GreyNoise IP Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4cdf2cff-89ae-4004-be1a-b40c1f8e85be\"\u003e{\"inputs\":{\"5122154c-c377-435e-9baf-ea79ebc6e601\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"5eb47553-7819-4d10-bdc9-994fc3dd3094\"}},\"b5caca14-688a-4a2d-9c7c-09c1c578bbcd\":{\"expression_input\":{\"expression\":\"artifact.value\"},\"input_type\":\"expression\"}},\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wprx2d\u003c/incoming\u003e\u003coutgoing\u003eFlow_07uxm1v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0wprx2d\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Greynoise Results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"5fc4354a-5285-41c8-b7e4-0ae9b0e8e27c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_07uxm1v\u003c/incoming\u003e\u003coutgoing\u003eFlow_0hk4a4q\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_07uxm1v\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0hk4a4q\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0hk4a4q\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_f227cce8_32de_4ccc_869f_d47b9024e63a\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0hk4a4q\" id=\"Flow_0hk4a4q_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"484\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_07uxm1v\" id=\"Flow_07uxm1v_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wprx2d\" id=\"Flow_0wprx2d_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"484\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1742493468137,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_f227cce8_32de_4ccc_869f_d47b9024e63a",
      "description": {
        "content": "This is for enterprise version",
        "format": "text"
      },
      "display_name": "Greynoise IP Query (Example)",
      "export_key": "greynoise_ip_query",
      "field_type_handle": "playbook_f227cce8_32de_4ccc_869f_d47b9024e63a",
      "fields_type": {
        "actions": [],
        "display_name": "Greynoise IP Query (Example)",
        "export_key": "playbook_f227cce8_32de_4ccc_869f_d47b9024e63a",
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
        "type_name": "playbook_f227cce8_32de_4ccc_869f_d47b9024e63a",
        "uuid": "22274ef4-fea3-44cc-96c6-6f1f39c530cd"
      },
      "has_logical_errors": false,
      "id": 195,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "last_modified_time": 1742493471444,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1742493468770,
          "description": "",
          "enabled": false,
          "export_key": "Greynoise Results",
          "id": 182,
          "language": "python3",
          "last_modified_by": "sysadmin@example.com",
          "last_modified_time": 1742493468770,
          "name": "Greynoise Results",
          "object_type": "artifact",
          "playbook_handle": "greynoise_ip_query",
          "programmatic_name": "greynoise_ip_query_greynoise_results",
          "script_text": "results = playbook.functions.results.results\nif results.success:\n  msg = [f\"Greynoise successful for IP: {artifact.value}\"]\n  for k,v in results.content.items():\n    msg.append(f\"\u003cbr\u003e\u003cb\u003e{k}\u003c/b\u003e: {v}\")\n  incident.addNote(helper.createRichText(\"\".join(msg)))\nelse:\n  incident.addNote(f\u0027Greynoise ip query failed:{results.reason}. Artifact value:{artifact.value}\u0027)",
          "tags": [],
          "uuid": "5fc4354a-5285-41c8-b7e4-0ae9b0e8e27c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "IP Address"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "greynoise_ip_query",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_f227cce8-32de-4ccc-869f-d47b9024e63a",
        "id": 268,
        "name": "playbook_f227cce8_32de_4ccc_869f_d47b9024e63a",
        "type": "playbook",
        "uuid": "3dc17dbc-1079-47cd-b837-44b9ac892f33"
      },
      "tags": [],
      "type": "default",
      "uuid": "f227cce8-32de-4ccc-869f-d47b9024e63a",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f\" isExecutable=\"true\" name=\"playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1w0328v\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"GreyNoise IP Query Community\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c0fb4a33-4b7a-4a8b-946e-b7bea8c87e65\"\u003e{\"inputs\":{\"5122154c-c377-435e-9baf-ea79ebc6e601\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"30998522-adc0-4600-9958-2e354afbd2b2\"}},\"b5caca14-688a-4a2d-9c7c-09c1c578bbcd\":{\"expression_input\":{\"expression\":\"artifact.value\"},\"input_type\":\"expression\"}},\"result_name\":\"results_greynoise\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1w0328v\u003c/incoming\u003e\u003coutgoing\u003eFlow_0gvd9i6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1w0328v\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Greynoise Community Results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"2db8f8e6-8e34-4ea2-94a6-d288942855f6\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0gvd9i6\u003c/incoming\u003e\u003coutgoing\u003eFlow_04dhfl3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0gvd9i6\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_04dhfl3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_04dhfl3\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04dhfl3\" id=\"Flow_04dhfl3_di\"\u003e\u003comgdi:waypoint x=\"900\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"900\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0gvd9i6\" id=\"Flow_0gvd9i6_di\"\u003e\u003comgdi:waypoint x=\"900\" y=\"342\"/\u003e\u003comgdi:waypoint x=\"900\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1w0328v\" id=\"Flow_1w0328v_di\"\u003e\u003comgdi:waypoint x=\"900\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"900\" y=\"258\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"809\" y=\"124\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"802\" y=\"258\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"802\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"834\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1742493471324,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f",
      "description": {
        "content": "This is an example for the community api",
        "format": "text"
      },
      "display_name": "Greynoise IP Query Community (Example)",
      "export_key": "greynoise_ip_query_community_example",
      "field_type_handle": "playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f",
      "fields_type": {
        "actions": [],
        "display_name": "Greynoise IP Query Community (Example)",
        "export_key": "playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f",
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
        "type_name": "playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f",
        "uuid": "5b2b6857-e7a7-4e34-b17c-d7c33fd0b6c5"
      },
      "has_logical_errors": false,
      "id": 196,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 20,
        "name": "sysadmin@example.com",
        "type": "user"
      },
      "last_modified_time": 1742493474333,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1742493471830,
          "description": "",
          "enabled": false,
          "export_key": "Greynoise Community Results",
          "id": 183,
          "language": "python3",
          "last_modified_by": "sysadmin@example.com",
          "last_modified_time": 1742493471830,
          "name": "Greynoise Community Results",
          "object_type": "artifact",
          "playbook_handle": "greynoise_ip_query_community_example",
          "programmatic_name": "greynoise_ip_query_community_example_greynoise_community_results",
          "script_text": "results = playbook.functions.results.results_greynoise\nif results.success:\n  msg = [f\"Greynoise successful for IP: {artifact.value}\"]\n  for k,v in results.content.items():\n    msg.append(f\"\u003cbr\u003e\u003cb\u003e{k}\u003c/b\u003e: {v}\")\n  incident.addNote(helper.createRichText(\"\".join(msg)))\nelse:\n  incident.addNote(f\u0027Greynoise ip community query failed:{results.reason}. Artifact value:{artifact.value}\u0027)",
          "tags": [],
          "uuid": "2db8f8e6-8e34-4ea2-94a6-d288942855f6"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "IP Address"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "greynoise_ip_query_community_example",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8d0b002c-62e7-48fa-ba6a-99dc5c85633f",
        "id": 269,
        "name": "playbook_8d0b002c_62e7_48fa_ba6a_99dc5c85633f",
        "type": "playbook",
        "uuid": "a7cf5626-0b5e-43dd-b131-3eb9666c3797"
      },
      "tags": [],
      "type": "default",
      "uuid": "8d0b002c-62e7-48fa-ba6a-99dc5c85633f",
      "version": 4
    }
  ],
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
  "workflows": [],
  "workspaces": []
}
