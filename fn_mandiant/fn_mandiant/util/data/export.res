{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1695727754116,
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
      "export_key": "__function/mandiant_artifact_type",
      "hide_notification": false,
      "id": 445,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mandiant_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mandiant_artifact_type",
      "tooltip": "Artifact data type",
      "type_id": 11,
      "uuid": "e8aa4b21-3b13-4b68-9253-949bf261dc71",
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
      "export_key": "__function/mandiant_artifact_data",
      "hide_notification": false,
      "id": 444,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mandiant_artifact_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "mandiant_artifact_data",
      "tooltip": "Data from the artifact",
      "type_id": 11,
      "uuid": "61553bb8-4a9e-4ced-8c5b-ebd3de6865e3",
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
      "created_date": 1695039658348,
      "description": {
        "content": "Provides customers with intelligence on who is most likely going to attack them, how they are going to attack, and what tools they will use.  This allows customers to prepare their defenses against an imminent attack.",
        "format": "text"
      },
      "destination_handle": "fn_mandiant",
      "display_name": "Mandiant: Threat Intelligence",
      "export_key": "mandiant_threat_intelligence",
      "id": 31,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1695381086149,
      "name": "mandiant_threat_intelligence",
      "tags": [],
      "uuid": "4512cffd-9ea6-4246-ae93-e4d4c13f436b",
      "version": 3,
      "view_items": [
        {
          "content": "61553bb8-4a9e-4ced-8c5b-ebd3de6865e3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e8aa4b21-3b13-4b68-9253-949bf261dc71",
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
  "id": 51,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1695727751929,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1695727751929,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "dcf298e4-8875-49fc-962f-f2e3a82ab248"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_mandiant",
      "name": "fn_mandiant",
      "programmatic_name": "fn_mandiant",
      "tags": [],
      "users": [],
      "uuid": "88c3ce4e-571b-404b-a2c0-6fc6c00a7307"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": 2,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "IP Address"
            },
            {
              "evaluation_id": 3,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "URL"
            },
            {
              "evaluation_id": 4,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Malware MD5 Hash"
            },
            {
              "evaluation_id": 1,
              "field_name": null,
              "method": "object_added",
              "type": null,
              "value": null
            }
          ],
          "custom_condition": "1 AND (2 OR 3 OR 4)",
          "logic_type": "advanced"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 40,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\" isExecutable=\"true\" name=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1tkd9qq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Mandiant: Threat Intelligence\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4512cffd-9ea6-4246-ae93-e4d4c13f436b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.mandiant_artifact_data = artifact.value\\ninputs.mandiant_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"mandiant_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tkd9qq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1dhtg4b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1tkd9qq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0vp4mzt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1dhtg4b\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Add search results to HITS\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"9804bc3f-ba90-478d-8bdc-c0a87a27b917\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1dhtg4b\u003c/incoming\u003e\u003coutgoing\u003eFlow_0vp4mzt\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0vp4mzt\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vp4mzt\" id=\"Flow_0vp4mzt_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"492\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dhtg4b\" id=\"Flow_1dhtg4b_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"372\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"408\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tkd9qq\" id=\"Flow_1tkd9qq_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"288\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"619\" y=\"164\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"288\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"644\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"611.5\" y=\"408\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1695380488072,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Mandiant: Scan artifact",
      "export_key": "mandiant_scan_artifact",
      "field_type_handle": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
      "fields_type": {
        "actions": [],
        "display_name": "Mandiant: Scan artifact",
        "export_key": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
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
        "type_name": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
        "uuid": "199c20c0-78f3-4a71-9ef2-6eda376007ee"
      },
      "has_logical_errors": false,
      "id": 32,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1695723716683,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1695381472551,
          "description": "",
          "enabled": false,
          "export_key": "Add search results to HITS",
          "id": 20,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1695723714850,
          "name": "Add search results to HITS",
          "object_type": "artifact",
          "playbook_handle": "mandiant_scan_artifact",
          "programmatic_name": "mandiant_scan_artifact_add_search_results_to_hits",
          "script_text": "import json \n\ndef complie_section_by_dtype(value, name):\n    subsection_type = \"string\"\n    if \"http\" in value:\n        subsection_type = \"uri\"\n    elif value.isdigit():\n        subsection_type = \"number\"\n        value = int(value)\n    subsection = {\n        \"name\"  : name,\n        \"type\"  : subsection_type,\n        \"value\" : value\n    }\n    return subsection\n\ndef dedup_section(section):\n    unique_keys = {}\n    for idx, each_item in enumerate(section):\n        if each_item[\"name\"] not in unique_keys:\n            unique_keys[each_item[\"name\"]] = 0\n        else:\n            unique_keys[each_item[\"name\"]] += 1\n            section[idx][\"name\"] = section[idx][\"name\"] + str(unique_keys[each_item[\"name\"]])\n    return section\n\ndef dedup_verdict_section(section):\n    verdict_name = \"\"\n\n    for each_item in section:\n        if each_item[\"name\"] == \"name\":\n            verdict_name = each_item[\"value\"]\n        if verdict_name:\n            each_item[\"name\"] = f\"{verdict_name} {each_item[\u0027name\u0027]}\"\n    return section\n\ndef compile_hits_section(gathered_info:dict, compiled_section:list) -\u003e list:\n    for each_key in gathered_info:\n        if isinstance(each_key, dict):\n            compile_hits_section(each_key, compiled_section)\n        elif isinstance(gathered_info[each_key], dict):\n            compile_hits_section(gathered_info[each_key], compiled_section)\n        elif isinstance(gathered_info[each_key], list):\n            for each_entity in gathered_info[each_key]:\n                if isinstance(each_entity, dict) or isinstance(each_entity, list):\n                    subsection = compile_hits_section(each_entity, compiled_section)\n                    compiled_section.append(subsection)\n        else:\n            subsection = complie_section_by_dtype(str(gathered_info[each_key]), each_key)\n            compiled_section.append(subsection)\n    return compiled_section\n\ndef add_response_as_hits(response):\n    main_section , other_sections = {}, {}\n    for section in response:\n        if isinstance(response[section], list) or isinstance(response[section], dict):\n            other_sections[section] = response[section]\n        else:\n            main_section[section ] = response[section]\n\n\n    for each_section in other_sections:\n        section = compile_hits_section(other_sections[each_section], [])\n        if each_section == \"verdict\":\n            section = dedup_verdict_section(section)\n        section = dedup_section(section)\n        artifact.addHit(f\"Mandiant Threat intelligence: {each_section.title()}\", section)\n    \n    section = compile_hits_section(main_section, [])\n    section = dedup_section(section)\n    artifact.addHit(\"Mandiant Threat intelligence: MScore\", section)\n\n\nresult = playbook.functions.results.mandiant_results\n\nif not result.success:\n  incident.addNote(helper.createRichText(result.reason))\nelif \"error\" not in result.content:\n  add_response_as_hits(result.content)\n",
          "tags": [],
          "uuid": "9804bc3f-ba90-478d-8bdc-c0a87a27b917"
        }
      ],
      "name": "mandiant_scan_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a87ae009-da8b-4a6b-b5ff-ff205216ed34",
        "id": 35,
        "name": "playbook_a87ae009_da8b_4a6b_b5ff_ff205216ed34",
        "type": "playbook",
        "uuid": "98374d47-0f1b-43cc-aafe-76f312650454"
      },
      "tags": [],
      "type": "default",
      "uuid": "a87ae009-da8b-4a6b-b5ff-ff205216ed34",
      "version": 45
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
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
