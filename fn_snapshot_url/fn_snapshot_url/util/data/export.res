{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1704216542371,
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
      "export_key": "__function/snapshot_incident_id",
      "hide_notification": false,
      "id": 777,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "snapshot_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "snapshot_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "917ea007-a927-4dda-8783-f5ecfc7f4213",
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
      "export_key": "__function/snapshot_url",
      "hide_notification": false,
      "id": 775,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "snapshot_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "snapshot_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d920070a-1d84-4db1-8829-1ef753f604c4",
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
      "export_key": "__function/snapshot_timeout",
      "hide_notification": false,
      "id": 1102,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "snapshot_timeout",
      "operation_perms": {},
      "operations": [],
      "placeholder": "30",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "snapshot_timeout",
      "tooltip": "default is 30 seconds",
      "type_id": 11,
      "uuid": "d96a4169-49f6-451d-8def-0393d5f67f5a",
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
      "export_key": "__function/snapshot_fullpage",
      "hide_notification": false,
      "id": 1103,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "snapshot_fullpage",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "snapshot_fullpage",
      "tooltip": "set to \u0027Yes\u0027 to collect the entire page",
      "type_id": 11,
      "uuid": "35671ae6-422d-4ac3-8ef8-ca66cda8c4c5",
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
      "created_date": 1700243202901,
      "description": {
        "content": "Snapshot URL as png image attachment.",
        "format": "text"
      },
      "destination_handle": "fn_snapshot_url",
      "display_name": "SnapShot URL",
      "export_key": "snapshot_url",
      "id": 33,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1704208839338,
      "name": "snapshot_url",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2, \"success\": true, \"reason\": null, \"content\": {\"attachment_name\": \"https://cybersecuritynordic.messukeskus.com/program-3/.png\"}, \"raw\": null, \"inputs\": {\"snapshot_incident_id\": 2103, \"snapshot_url\": \"https://cybersecuritynordic.messukeskus.com/program-3/\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-snapshot-url\", \"package_version\": \"1.0.0\", \"host\": \"1fd9269d-5558-411b-ba33-e4767f763c59-8678ccd8c8-xs2vr\", \"execution_time_ms\": 49769, \"timestamp\": \"2023-12-28 20:51:10\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-04/schema#\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"integer\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {\"type\": \"null\"}, \"content\": {\"type\": \"object\", \"properties\": {\"attachment_name\": {\"type\": \"string\"}}, \"required\": [\"attachment_name\"]}, \"raw\": {\"type\": \"null\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"snapshot_incident_id\": {\"type\": \"integer\"}, \"snapshot_url\": {\"type\": \"string\"}}, \"required\": [\"snapshot_incident_id\", \"snapshot_url\"]}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}, \"required\": [\"version\", \"package\", \"package_version\", \"host\", \"execution_time_ms\", \"timestamp\"]}}, \"required\": [\"version\", \"success\", \"reason\", \"content\", \"inputs\", \"metrics\"]}",
      "tags": [],
      "uuid": "058ba37d-dbd0-4f68-94d5-787a5121c0d8",
      "version": 11,
      "view_items": [
        {
          "content": "d920070a-1d84-4db1-8829-1ef753f604c4",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "917ea007-a927-4dda-8783-f5ecfc7f4213",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d96a4169-49f6-451d-8def-0393d5f67f5a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "35671ae6-422d-4ac3-8ef8-ca66cda8c4c5",
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
  "id": 22,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1704216541088,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1704216541088,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "103b67c0-8d83-464d-ba6a-ad78419c5438"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_snapshot_url",
      "name": "fn_snapshot_url",
      "programmatic_name": "fn_snapshot_url",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "1b1c1592-7a20-43a4-935e-a9a9918771e6"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 24,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7\" isExecutable=\"true\" name=\"playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_01csd5e\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SnapShot URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"058ba37d-dbd0-4f68-94d5-787a5121c0d8\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.snapshot_incident_id = incident.id\\ninputs.snapshot_url = artifact.value\\nif getattr(playbook.inputs, \\\"snapshot_url_load_timeout\\\", None):\\n  inputs.snapshot_timeout = playbook.inputs.snapshot_url_load_timeout\\ninputs.snapshot_fullpage = playbook.inputs.snapshot_full_screen_capture\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"snapshot_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_01csd5e\u003c/incoming\u003e\u003coutgoing\u003eFlow_14k7a76\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_01csd5e\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_14vyaha\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_14k7a76\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"snapshot_results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"02f115f0-ef41-4eee-88fa-838996615045\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14k7a76\u003c/incoming\u003e\u003coutgoing\u003eFlow_14vyaha\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_14vyaha\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14vyaha\" id=\"Flow_14vyaha_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"372\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"414\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14k7a76\" id=\"Flow_14k7a76_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"288\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_01csd5e\" id=\"Flow_01csd5e_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.515625\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"655\" y=\"414\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"287.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1700247384039,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
      "description": {
        "content": "Snapshot URL as png image attachment.",
        "format": "text"
      },
      "display_name": "Snapshot URL",
      "export_key": "snapshot_url__example",
      "field_type_handle": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
      "fields_type": {
        "actions": [],
        "display_name": "Snapshot URL",
        "export_key": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
        "fields": {
          "snapshot_full_screen_capture": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7/snapshot_full_screen_capture",
            "hide_notification": false,
            "id": 1104,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "snapshot_full_screen_capture",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Full Screen Capture",
            "tooltip": "",
            "type_id": 1030,
            "uuid": "e7a7c02b-ec4e-4140-b469-c715f9e63cef",
            "values": []
          },
          "snapshot_url_load_timeout": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7/snapshot_url_load_timeout",
            "hide_notification": false,
            "id": 1105,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "snapshot_url_load_timeout",
            "operation_perms": {},
            "operations": [],
            "placeholder": "30",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "URL Load Timeout",
            "tooltip": "In seconds",
            "type_id": 1030,
            "uuid": "ed354b4b-8ac3-480a-8339-7499f0acc70a",
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
        "type_name": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
        "uuid": "2eb96192-bdc6-44db-bcd0-4d7d9663030e"
      },
      "has_logical_errors": false,
      "id": 29,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1704216505170,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1703791293103,
          "description": "",
          "enabled": false,
          "export_key": "snapshot_results",
          "id": 29,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1703792412903,
          "name": "snapshot_results",
          "object_type": "artifact",
          "playbook_handle": "snapshot_url__example",
          "programmatic_name": "snapshot_url__example_snapshot_results",
          "script_text": "results = playbook.functions.results.snapshot_results\n\nif results.success:\n  incident.addNote(f\"Snapshot URL for {results.inputs.snapshot_url} succeeded with attachment: {results.content.attachment_name}\")\nelse:\n  incident.addNote(f\"Snapshot URL {results.reason}\")\n",
          "tags": [],
          "uuid": "02f115f0-ef41-4eee-88fa-838996615045"
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
              "value": "URL"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "e7a7c02b-ec4e-4140-b469-c715f9e63cef",
            "element": "field_uuid",
            "field_type": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "ed354b4b-8ac3-480a-8339-7499f0acc70a",
            "element": "field_uuid",
            "field_type": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snapshot_url__example",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7faa5aa3-cdfa-424e-bd65-1951522f9bd7",
        "id": 37,
        "name": "playbook_7faa5aa3_cdfa_424e_bd65_1951522f9bd7",
        "type": "playbook",
        "uuid": "decef958-3785-4a43-b23d-86e256bd5020"
      },
      "tags": [],
      "type": "default",
      "uuid": "7faa5aa3-cdfa-424e-bd65-1951522f9bd7",
      "version": 32
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 45,
    "major": 48,
    "minor": 2,
    "version": "48.2.45"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
