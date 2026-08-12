{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1711454642305,
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
      "export_key": "__function/ansible_parameters",
      "hide_notification": false,
      "id": 4706,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ansible_parameters",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ansible_parameters",
      "tooltip": "",
      "type_id": 11,
      "uuid": "876f27be-df66-4827-9389-eea2d118ab64",
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
      "export_key": "__function/ansible_playbook_name",
      "hide_notification": false,
      "id": 4705,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ansible_playbook_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ansible_playbook_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fb075d9d-8048-4e7f-a70c-2b3f37a5f42b",
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
      "export_key": "__function/ansible_module",
      "hide_notification": false,
      "id": 4708,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ansible_module",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ansible_module",
      "tooltip": "command and parameters to run",
      "type_id": 11,
      "uuid": "ff9dc014-f68b-4151-99c6-087921293850",
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
      "export_key": "__function/ansible_hosts",
      "hide_notification": false,
      "id": 4707,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ansible_hosts",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ansible_hosts",
      "tooltip": "host name pattern or group for module execution",
      "type_id": 11,
      "uuid": "05c3ea3f-b7ef-4300-bce9-06dfb9309180",
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
      "created_date": 1709911165550,
      "description": {
        "content": "Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time.",
        "format": "text"
      },
      "destination_handle": "fn_ansible",
      "display_name": "Ansible Playbook",
      "export_key": "fn_ansible",
      "id": 8,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1709911165550,
      "name": "fn_ansible",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "f34fab33-54d8-48fb-aa74-530af25957a9",
      "version": 0,
      "view_items": [
        {
          "content": "fb075d9d-8048-4e7f-a70c-2b3f37a5f42b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "876f27be-df66-4827-9389-eea2d118ab64",
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
      "created_date": 1709911165622,
      "description": {
        "content": "Run an Ansible Module",
        "format": "text"
      },
      "destination_handle": "fn_ansible",
      "display_name": "Ansible Module",
      "export_key": "fn_ansible_module",
      "id": 9,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1709911165622,
      "name": "fn_ansible_module",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "739bdfd8-c135-4684-93c0-71fd7dd20e34",
      "version": 0,
      "view_items": [
        {
          "content": "ff9dc014-f68b-4151-99c6-087921293850",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "876f27be-df66-4827-9389-eea2d118ab64",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "05c3ea3f-b7ef-4300-bce9-06dfb9309180",
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
  "id": 10,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1711454640831,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1711454640831,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_ansible",
      "name": "fn_ansible",
      "programmatic_name": "fn_ansible",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "7d204cde-e028-4bad-85fa-a87153622e69"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 15,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7470440b_36bd_432f_8a5e_5dd341a61698\" isExecutable=\"true\" name=\"playbook_7470440b_36bd_432f_8a5e_5dd341a61698\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_13uahjr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Ansible Module\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"739bdfd8-c135-4684-93c0-71fd7dd20e34\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.ansible_hosts = getattr(playbook.inputs, \\\"ansible_hosts\\\", None)\\ninputs.ansible_module = getattr(playbook.inputs, \\\"ansible_module\\\", None)\\nif getattr(playbook.inputs, \\\"ansible_module_arguments\\\", None):\\n  inputs.ansible_parameters = getattr(playbook.inputs, \\\"ansible_module_arguments\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"module_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_13uahjr\u003c/incoming\u003e\u003coutgoing\u003eFlow_1lu7c8l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_13uahjr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Ansible Module Post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8e046513-c7d3-45f8-9717-efb0f6cdfcbb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1lu7c8l\u003c/incoming\u003e\u003coutgoing\u003eFlow_1jeewub\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1lu7c8l\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1jeewub\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1jeewub\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7470440b_36bd_432f_8a5e_5dd341a61698\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jeewub\" id=\"Flow_1jeewub_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1lu7c8l\" id=\"Flow_1lu7c8l_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_13uahjr\" id=\"Flow_13uahjr_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1710510067192,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
      "description": {
        "content": "Run an Ansible module for ad-hoc operations",
        "format": "text"
      },
      "display_name": "Ansible: Run a Module - Example (PB)",
      "export_key": "ansible_run_a_module",
      "field_type_handle": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
      "fields_type": {
        "actions": [],
        "display_name": "Ansible: Run a Module - Example (PB)",
        "export_key": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
        "fields": {
          "ansible_hosts": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698/ansible_hosts",
            "hide_notification": false,
            "id": 4841,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_hosts",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Hosts",
            "tooltip": "Use patterns for group name",
            "type_id": 1042,
            "uuid": "45da4f04-77a7-4de8-b9f2-295a2897d8ad",
            "values": []
          },
          "ansible_module": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698/ansible_module",
            "hide_notification": false,
            "id": 4842,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_module",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Module",
            "tooltip": "",
            "type_id": 1042,
            "uuid": "74f7453f-1c8f-4f67-b3d4-eb9858b6669e",
            "values": []
          },
          "ansible_module_arguments": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698/ansible_module_arguments",
            "hide_notification": false,
            "id": 4843,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_module_arguments",
            "operation_perms": {},
            "operations": [],
            "placeholder": "param=value;param=value;",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Module Arguments",
            "tooltip": "",
            "type_id": 1042,
            "uuid": "3f077211-0da2-42eb-a4a1-fd5253b9afc4",
            "values": []
          }
        },
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
        "type_name": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
        "uuid": "2b25abc2-1ef0-4000-9f7c-c9e1dcec57d2"
      },
      "has_logical_errors": false,
      "id": 38,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1711454524489,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1710510704537,
          "description": "",
          "enabled": false,
          "export_key": "Ansible Module Post-process",
          "id": 55,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1710513321859,
          "name": "Ansible Module Post-process",
          "object_type": "incident",
          "playbook_handle": "ansible_run_a_module",
          "programmatic_name": "ansible_run_a_module_ansible_module_post_process",
          "script_text": "results = playbook.functions.results.module_results\nif results.get(\"success\"):\n  if len(results.get(\u0027content\u0027, {}).keys()) == 0:\n    note = f\"Running Ansible module: {playbook.inputs.ansible_module}\\nParameters: {results.get(\u0027inputs\u0027)}\\nNo results returned.\"\n  else:\n    for item in results.get(\u0027content\u0027, {}):\n      note = \"Running Ansible module: {}\\nParameters: {}\\nResults: {}\".format(playbook.inputs.ansible_module, results.get(\u0027inputs\u0027), results.get(\u0027content\u0027, {}).get(item, {}).get(\u0027detail\u0027))\n  incident.addNote(helper.createPlainText(note))\nelse:\n  incident.addNote(f\"Running Ansible Module: {playbook.inputs.ansible_module} failed with reason: {results.get(\u0027reason\u0027)}\")",
          "tags": [],
          "uuid": "8e046513-c7d3-45f8-9717-efb0f6cdfcbb"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "74f7453f-1c8f-4f67-b3d4-eb9858b6669e",
            "element": "field_uuid",
            "field_type": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "3f077211-0da2-42eb-a4a1-fd5253b9afc4",
            "element": "field_uuid",
            "field_type": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "45da4f04-77a7-4de8-b9f2-295a2897d8ad",
            "element": "field_uuid",
            "field_type": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "ansible_run_a_module",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7470440b-36bd-432f-8a5e-5dd341a61698",
        "id": 38,
        "name": "playbook_7470440b_36bd_432f_8a5e_5dd341a61698",
        "type": "playbook",
        "uuid": "babfe25e-192a-4802-a918-7f78640944ae"
      },
      "tags": [],
      "type": "default",
      "uuid": "7470440b-36bd-432f-8a5e-5dd341a61698",
      "version": 19
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_416e01cc_7870_491d_84a4_854535485029\" isExecutable=\"true\" name=\"playbook_416e01cc_7870_491d_84a4_854535485029\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0e1u915\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Ansible Playbook\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f34fab33-54d8-48fb-aa74-530af25957a9\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.ansible_playbook_name = getattr(playbook.inputs, \\\"ansible_playbook_name\\\", None)\\nif getattr(playbook.inputs, \\\"ansible_playbook_variables\\\", None):\\n  inputs.ansible_parameters = getattr(playbook.inputs, \\\"ansible_playbook_variables\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0e1u915\u003c/incoming\u003e\u003coutgoing\u003eFlow_1gfyyb2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0e1u915\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"ansible playbook post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"de14f3af-4591-42e7-a2eb-178423aaa7d8\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1gfyyb2\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jpod9r\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1gfyyb2\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jpod9r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jpod9r\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_416e01cc_7870_491d_84a4_854535485029\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jpod9r\" id=\"Flow_0jpod9r_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"502\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"594\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1gfyyb2\" id=\"Flow_1gfyyb2_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"418\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0e1u915\" id=\"Flow_0e1u915_di\"\u003e\u003comgdi:waypoint x=\"724\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"724\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"626\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"626\" y=\"418\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"658\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1710439451336,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_416e01cc_7870_491d_84a4_854535485029",
      "description": {
        "content": "Run a playbook from an Incident with specific hosts and parameters",
        "format": "text"
      },
      "display_name": "Ansible: Run a Playbook - Example (PB)",
      "export_key": "ansible_run_a_playbook",
      "field_type_handle": "playbook_416e01cc_7870_491d_84a4_854535485029",
      "fields_type": {
        "actions": [],
        "display_name": "Ansible: Run a Playbook - Example (PB)",
        "export_key": "playbook_416e01cc_7870_491d_84a4_854535485029",
        "fields": {
          "ansible_playbook_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_416e01cc_7870_491d_84a4_854535485029/ansible_playbook_name",
            "hide_notification": false,
            "id": 4839,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_playbook_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "playbook1",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Playbook Name",
            "tooltip": "Enter target ansible playbook name",
            "type_id": 1041,
            "uuid": "d224b633-36d4-4e0b-9c72-88eb23ace94f",
            "values": []
          },
          "ansible_playbook_variables": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_416e01cc_7870_491d_84a4_854535485029/ansible_playbook_variables",
            "hide_notification": false,
            "id": 4840,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_playbook_variables",
            "operation_perms": {},
            "operations": [],
            "placeholder": "param=value;param=value;",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Playbook Variables",
            "tooltip": "Please enter variable name and corresponding value. Example: customer=test;disable=true",
            "type_id": 1041,
            "uuid": "e6d26cf2-7e17-477c-83f4-122848d02cca",
            "values": []
          }
        },
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
        "type_name": "playbook_416e01cc_7870_491d_84a4_854535485029",
        "uuid": "f3bc7be1-91bd-4801-81b5-ea4430602b25"
      },
      "has_logical_errors": false,
      "id": 37,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1711389587528,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1710439869820,
          "description": "",
          "enabled": false,
          "export_key": "ansible playbook post-process",
          "id": 54,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1710511472627,
          "name": "ansible playbook post-process",
          "object_type": "incident",
          "playbook_handle": "ansible_run_a_playbook",
          "programmatic_name": "ansible_run_a_playbook_ansible_playbook_post_process",
          "script_text": "results = playbook.functions.results.playbook_results\nif results.get(\"success\"):\n  if len(results.get(\"content\", {}).keys()) == 0:\n    note = \"No results returned on parameters: {}\".format(results.get(\u0027inputs\u0027))\n  else:\n    for item in results.get(\u0027content\u0027):\n      note = f\"{item} - {results.get(\u0027inputs\u0027)}\\n{str(results.get(\u0027content\u0027, {}).get(item, {}).get(\u0027detail\u0027))}\"\n  incident.addNote(helper.createPlainText(note))\nelse:\n  incident.addNote(f\"Running Ansible playbook: {playbook.inputs.ansible_playbook_name} failed with reason: {results.get(\u0027reason\u0027)}\")",
          "tags": [],
          "uuid": "de14f3af-4591-42e7-a2eb-178423aaa7d8"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "d224b633-36d4-4e0b-9c72-88eb23ace94f",
            "element": "field_uuid",
            "field_type": "playbook_416e01cc_7870_491d_84a4_854535485029",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "e6d26cf2-7e17-477c-83f4-122848d02cca",
            "element": "field_uuid",
            "field_type": "playbook_416e01cc_7870_491d_84a4_854535485029",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "ansible_run_a_playbook",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_416e01cc-7870-491d-84a4-854535485029",
        "id": 37,
        "name": "playbook_416e01cc_7870_491d_84a4_854535485029",
        "type": "playbook",
        "uuid": "cb34ef7a-3e95-447c-87e3-3c017c84fad2"
      },
      "tags": [],
      "type": "default",
      "uuid": "416e01cc-7870-491d-84a4-854535485029",
      "version": 13
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_53c177b1_fcff_4bf0_bb93_664740a9affc\" isExecutable=\"true\" name=\"playbook_53c177b1_fcff_4bf0_bb93_664740a9affc\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0ukwlvx\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Ansible Playbook\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f34fab33-54d8-48fb-aa74-530af25957a9\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.ansible_playbook_name = getattr(playbook.inputs, \\\"ansible_playbook_name\\\", None)\\nartifact_value = f\u0027artifact_value={artifact.value}\u0027\\nif getattr(playbook.inputs, \\\"ansible_playbook_variables\\\", None):\\n  inputs.ansible_parameters = \u0027;\u0027.join(getattr(playbook.inputs, \\\"ansible_playbook_variables\\\", None), artifact_value)\\nelse:\\n  inputs.ansible_parameters = artifact_value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"playbook_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ukwlvx\u003c/incoming\u003e\u003coutgoing\u003eFlow_09zfs75\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0ukwlvx\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Ansible run playbook from an artifact post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"b3811ad9-3950-4ae6-a509-65bbc37d5775\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09zfs75\u003c/incoming\u003e\u003coutgoing\u003eFlow_03ij2su\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_09zfs75\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_03ij2su\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_03ij2su\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_53c177b1_fcff_4bf0_bb93_664740a9affc\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ukwlvx\" id=\"Flow_0ukwlvx_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09zfs75\" id=\"Flow_09zfs75_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_03ij2su\" id=\"Flow_03ij2su_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"534\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"534\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1710510787990,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
      "description": {
        "content": "Merge artifact_value with Ansible parameters to run a Playbook",
        "format": "text"
      },
      "display_name": "Ansible: Run a Playbook from an Artifact - Example (PB)",
      "export_key": "ansible_run_a_playbook_from_an_artifact",
      "field_type_handle": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
      "fields_type": {
        "actions": [],
        "display_name": "Ansible: Run a Playbook from an Artifact - Example (PB)",
        "export_key": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
        "fields": {
          "ansible_playbook_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc/ansible_playbook_name",
            "hide_notification": false,
            "id": 4844,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_playbook_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "playbook1",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Playbook Name",
            "tooltip": "Enter target ansible playbook name",
            "type_id": 1043,
            "uuid": "9024b2b8-742d-4823-9b1b-e605e2b1a1a5",
            "values": []
          },
          "ansible_playbook_variables": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc/ansible_playbook_variables",
            "hide_notification": false,
            "id": 4845,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "ansible_playbook_variables",
            "operation_perms": {},
            "operations": [],
            "placeholder": "param=value;param=value;",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Ansible Playbook Variables",
            "tooltip": "Please enter variable name and corresponding value. Example: customer=test;disable=true",
            "type_id": 1043,
            "uuid": "7c6c0cfe-7d6d-42ed-a1bd-f03d6e3a2fd4",
            "values": []
          }
        },
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
        "type_name": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
        "uuid": "7c072f3b-903b-40e3-bdb7-6731994f350f"
      },
      "has_logical_errors": false,
      "id": 39,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 36,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1711389587829,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1710511447615,
          "description": "",
          "enabled": false,
          "export_key": "Ansible run playbook from an artifact post-process",
          "id": 56,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1710511447615,
          "name": "Ansible run playbook from an artifact post-process",
          "object_type": "artifact",
          "playbook_handle": "ansible_run_a_playbook_from_an_artifact",
          "programmatic_name": "ansible_run_a_playbook_from_an_artifact_ansible_run_playbook_from_an_artifact_post_process",
          "script_text": "results = playbook.functions.results.playbook_results\nif results.get(\"success\"):\n  if len(results.get(\"content\", {}).keys()) == 0:\n    note = \"No results returned on parameters: {}\".format(results.get(\u0027inputs\u0027))\n  else:\n    for item in results.get(\u0027content\u0027, {}):\n      note = f\"{item} - {results.get(\u0027inputs\u0027)}\\n{str(results.get(\u0027content\u0027, {}).get(item, {}).get(\u0027detail\u0027))}\"\n  incident.addNote(helper.createPlainText(note))\nelse:\n  incident.addNote(f\"Running Ansible playbook: {playbook.inputs.ansible_playbook_name} failed with reason: {results.get(\u0027reason\u0027)}\")",
          "tags": [],
          "uuid": "b3811ad9-3950-4ae6-a509-65bbc37d5775"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "9024b2b8-742d-4823-9b1b-e605e2b1a1a5",
            "element": "field_uuid",
            "field_type": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "7c6c0cfe-7d6d-42ed-a1bd-f03d6e3a2fd4",
            "element": "field_uuid",
            "field_type": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "ansible_run_a_playbook_from_an_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_53c177b1-fcff-4bf0-bb93-664740a9affc",
        "id": 39,
        "name": "playbook_53c177b1_fcff_4bf0_bb93_664740a9affc",
        "type": "playbook",
        "uuid": "ac86924d-54f1-476b-b784-84c027be3853"
      },
      "tags": [],
      "type": "default",
      "uuid": "53c177b1-fcff-4bf0-bb93-664740a9affc",
      "version": 11
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 9097,
    "major": 50,
    "minor": 0,
    "version": "50.0.9097"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
