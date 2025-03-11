{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Artifact",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "3c627aa8-5810-44a4-a25d-e5a8db19b6a6",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Attachment",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Attachment",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "2b628b8c-1b52-4e51-a5f3-c323d7ff037e",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Incident",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "5bc0b99b-8f87-48de-97d9-9333f1139d5d",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Milestone",
      "id": 30,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Milestone",
      "object_type": "milestone",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "c7fcaf50-4402-4c62-9552-c26df6e5be9b",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Note",
      "id": 31,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Note",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "780f2ebe-9aac-41e9-98ab-70688ac9af7a",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Data Feeder: Task",
      "id": 33,
      "logic_type": "all",
      "message_destinations": [
        "feed_data"
      ],
      "name": "Data Feeder: Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "ee0d92ee-e53d-4ebd-a28f-df959e949ed7",
      "view_items": [],
      "workflows": []
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1687453010581,
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
      "export_key": "__function/df_min_incident_id",
      "hide_notification": false,
      "id": 548,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "df_min_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "df_min_incident_id",
      "tooltip": "Enter an incident # or 0 to indicate the start of all incidents",
      "type_id": 11,
      "uuid": "b80d11d4-9c6b-4cd7-951a-4fe8c572c9ef",
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
      "export_key": "__function/df_max_incident_id",
      "hide_notification": false,
      "id": 547,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "df_max_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "df_max_incident_id",
      "tooltip": "Enter incident # for upper range or 0 to indicate all incidents",
      "type_id": 11,
      "uuid": "e7820e44-4087-4ce2-84af-0fe93630a03c",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/df_query_api_method",
      "hide_notification": false,
      "id": 549,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "df_query_api_method",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "df_query_api_method",
      "tooltip": "",
      "type_id": 11,
      "uuid": "731e94ff-822f-48f1-83a9-a78380fd636b",
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
      "created_date": 1687446879113,
      "description": {
        "content": "Synchronize Incident(s) and their associated tasks, notes, attachments, artifacts, milestones and associated datatables",
        "format": "text"
      },
      "destination_handle": "feed_data",
      "display_name": "Data Feeder: Sync Incidents",
      "export_key": "data_feeder_sync_incidents",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1687446879142,
      "name": "data_feeder_sync_incidents",
      "tags": [],
      "uuid": "7ffed4e5-72fb-4162-bdef-4ea3ebfa89de",
      "version": 1,
      "view_items": [
        {
          "content": "b80d11d4-9c6b-4cd7-951a-4fe8c572c9ef",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e7820e44-4087-4ce2-84af-0fe93630a03c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "731e94ff-822f-48f1-83a9-a78380fd636b",
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
  "id": 5,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1687453008445,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1687453008445,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "2aaac5ce-b8fa-420d-8a03-18bc7d4608c2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "feed_data",
      "name": "feed_data",
      "programmatic_name": "feed_data",
      "tags": [],
      "users": [],
      "uuid": "e05282fb-6cfc-4709-af84-cd71438581c8"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 5,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786\" isExecutable=\"true\" name=\"playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1i1alyh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Feeder: Sync Incidents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7ffed4e5-72fb-4162-bdef-4ea3ebfa89de\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.df_min_incident_id = playbook.inputs.minimum_incident_id\\ninputs.df_max_incident_id = playbook.inputs.maximum_incident_id\\ninputs.df_query_api_method = playbook.inputs.query_api_method\\n  \",\"pre_processing_script_language\":\"python3\",\"result_name\":\"sync_incident_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1i1alyh\u003c/incoming\u003e\u003coutgoing\u003eFlow_04qk21l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1i1alyh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1sh3nix\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"process sync_incident results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"10ca78a6-6405-47ea-8178-275c43e1256b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04qk21l\u003c/incoming\u003e\u003coutgoing\u003eFlow_1sh3nix\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_04qk21l\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_1sh3nix\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sh3nix\" id=\"Flow_1sh3nix_di\"\u003e\u003comgdi:waypoint x=\"740\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04qk21l\" id=\"Flow_04qk21l_di\"\u003e\u003comgdi:waypoint x=\"740\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1i1alyh\" id=\"Flow_1i1alyh_di\"\u003e\u003comgdi:waypoint x=\"740\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.1875\" x=\"646\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"642\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.21875\" x=\"674\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"642\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1687446941527,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
      "description": {
        "content": "Synchronize Incident(s) and their associated tasks, notes, attachments, artifacts, milestones and associated datatables",
        "format": "text"
      },
      "display_name": "Data Feeder: Sync Incidents (PB)",
      "export_key": "data_feeder_sync_incidents_pb",
      "field_type_handle": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
      "fields_type": {
        "actions": [],
        "display_name": "Data Feeder: Sync Incidents (PB)",
        "export_key": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
        "fields": {
          "maximum_incident_id": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786/maximum_incident_id",
            "hide_notification": false,
            "id": 550,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "maximum_incident_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Maximum Incident Id",
            "tooltip": "",
            "type_id": 1000,
            "uuid": "b4aace79-0b71-4c0a-b5a9-085a23bb04d1",
            "values": []
          },
          "minimum_incident_id": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786/minimum_incident_id",
            "hide_notification": false,
            "id": 551,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "minimum_incident_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Minimum Incident Id",
            "tooltip": "",
            "type_id": 1000,
            "uuid": "5e8be77e-2a9f-44d6-ab24-ccb80884e094",
            "values": []
          },
          "query_api_method": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786/query_api_method",
            "hide_notification": false,
            "id": 552,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "query_api_method",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Query API Method",
            "tooltip": "",
            "type_id": 1000,
            "uuid": "4c499958-b468-46d2-83d9-83d1c356bf5b",
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
        "type_name": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
        "uuid": "8bfc4dd9-8f62-451d-968d-6aff7627d175"
      },
      "has_logical_errors": false,
      "id": 1,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1687450928817,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1687447241654,
          "description": "",
          "enabled": false,
          "export_key": "process sync_incident results",
          "id": 3,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1687450922589,
          "name": "process sync_incident results",
          "object_type": "incident",
          "playbook_handle": "data_feeder_sync_incidents_pb",
          "programmatic_name": "data_feeder_sync_incidents_pb_process_sync_incident_results",
          "script_text": "# {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \u0027content\u0027: {\u0027num_of_sync_incidents\u0027: 2}, \u0027raw\u0027: \u0027{\"num_of_sync_incidents\": 2}\u0027, \u0027inputs\u0027: {\u0027df_max_incident_id\u0027: None, \u0027df_min_incident_id\u0027: 0}, \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027unknown\u0027, \u0027package_version\u0027: \u0027unknown\u0027, \u0027host\u0027: \u0027Marks-MBP.fios-router.home\u0027, \u0027execution_time_ms\u0027: 2062, \u0027timestamp\u0027: \u00272019-05-14 21:37:05\u0027}}\nresults = playbook.functions.results.sync_incident_results\nif results.success:\n  incident.addNote(f\"Data Feeder Sync\\nMin: {results[\u0027inputs\u0027][\u0027df_min_incident_id\u0027]} Max: {results[\u0027inputs\u0027][\u0027df_max_incident_id\u0027]}\\nIncidents Sync\u0027d: {results[\u0027content\u0027][\u0027num_of_sync_incidents\u0027]}\")\nelse: \n  incident.addNote(f\"Data Feeder Sync failed: {results.reason}\")\n",
          "tags": [],
          "uuid": "10ca78a6-6405-47ea-8178-275c43e1256b"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "5e8be77e-2a9f-44d6-ab24-ccb80884e094",
            "element": "field_uuid",
            "field_type": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b4aace79-0b71-4c0a-b5a9-085a23bb04d1",
            "element": "field_uuid",
            "field_type": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "4c499958-b468-46d2-83d9-83d1c356bf5b",
            "element": "field_uuid",
            "field_type": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "data_feeder_sync_incidents_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_2a2cd2ba-bee0-42fa-a1fb-0e5a68727786",
        "id": 2,
        "name": "playbook_2a2cd2ba_bee0_42fa_a1fb_0e5a68727786",
        "type": "playbook",
        "uuid": "a6035656-c7ea-499f-8929-9940f1518057"
      },
      "tags": [],
      "type": "default",
      "uuid": "2a2cd2ba-bee0-42fa-a1fb-0e5a68727786",
      "version": 10
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 7899,
    "major": 45,
    "minor": 0,
    "version": "45.0.7899"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
