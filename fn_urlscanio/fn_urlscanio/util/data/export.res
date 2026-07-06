{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "URL",
            "URL Referer"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: urlscan.io",
      "id": 32,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: urlscan.io",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "93828a35-d948-4e5f-9196-3a317fd38855",
      "view_items": [],
      "workflows": [
        "example_urlscanio"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "connectors": null,
  "export_date": 1781081748683,
  "export_format_version": 2,
  "export_notes": null,
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
      "export_key": "__function/urlscanio_referer",
      "hide_notification": false,
      "id": 455,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
      "name": "urlscanio_referer",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_referer",
      "tooltip": "Custom referer URL for this scan",
      "type_id": 11,
      "uuid": "a2ebdb5b-3d5a-425c-a0c7-fa35904fa5c4",
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 456,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "the id of the incident",
      "type_id": 11,
      "uuid": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "export_key": "__function/urlscanio_public",
      "hide_notification": false,
      "id": 457,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
      "name": "urlscanio_public",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_public",
      "tooltip": "Should the scan be posted as public?",
      "type_id": 11,
      "uuid": "ee9263c1-432a-41a8-8bbd-6917d35fb3ac",
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
      "export_key": "__function/urlscanio_url",
      "hide_notification": false,
      "id": 458,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
      "name": "urlscanio_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "62f95ee9-a112-4d1a-aa65-a6d0e1ef7348",
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
      "export_key": "__function/urlscanio_useragent",
      "hide_notification": false,
      "id": 459,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
      "name": "urlscanio_useragent",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "urlscanio_useragent",
      "tooltip": "Override User-Agent for this scan",
      "type_id": 11,
      "uuid": "7381875c-7a32-439d-8f55-76239a4c72b7",
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
      "created_date": 1780859619143,
      "description": {
        "content": "Analyze a URL with urlscan.io",
        "format": "text"
      },
      "destination_handle": "urlscanio",
      "display_name": "Scan with urlscan.io",
      "export_key": "urlscanio",
      "id": 5,
      "last_modified_by": {
        "display_name": "aaa",
        "id": 4,
        "name": "2683b631-db4a-4209-baaf-2ee08660fbeb",
        "type": "apikey"
      },
      "last_modified_time": 1780859619143,
      "name": "urlscanio",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d19c1f00-b4f1-4480-b8a3-7bdd19143041",
      "version": 0,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "62f95ee9-a112-4d1a-aa65-a6d0e1ef7348",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ee9263c1-432a-41a8-8bbd-6917d35fb3ac",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7381875c-7a32-439d-8f55-76239a4c72b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a2ebdb5b-3d5a-425c-a0c7-fa35904fa5c4",
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
          "name": "Example: urlscan.io",
          "object_type": "artifact",
          "programmatic_name": "example_urlscanio",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 3,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1781081747120,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1781081747120,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "2683b631-db4a-4209-baaf-2ee08660fbeb"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "urlscanio",
      "name": "urlscan.io",
      "programmatic_name": "urlscanio",
      "tags": [],
      "users": [],
      "uuid": "9c4e0143-d84b-4fd2-be43-e52eeb1e1e08"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb\" isExecutable=\"true\" name=\"playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_09ung60\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Scan with urlscan.io\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d19c1f00-b4f1-4480-b8a3-7bdd19143041\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# This is an artifact workflow; \\n# The URL to scan is the artifact value\\ninputs.urlscanio_url = artifact.value\\n\\n# Set the incident id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"urlscanio\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09ung60\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ui22co\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09ung60\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0ui22co\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0ui22co\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09ung60\" id=\"Flow_09ung60_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ui22co\" id=\"Flow_0ui22co_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"304\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"304\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1780859620079,
      "creator_principal": {
        "display_name": "aaa",
        "id": 4,
        "name": "2683b631-db4a-4209-baaf-2ee08660fbeb",
        "type": "apikey"
      },
      "deployment_id": "playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: urlscan.io",
      "export_key": "example_urlscanio",
      "field_type_handle": "playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb",
      "fields_type": {
        "actions": [],
        "display_name": "Example: urlscan.io",
        "export_key": "playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb",
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
        "type_name": "playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb",
        "uuid": "ea82a80c-8086-4e53-b40b-674eac3210c4"
      },
      "has_logical_errors": false,
      "id": 19,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "aaa",
        "id": 4,
        "name": "2683b631-db4a-4209-baaf-2ee08660fbeb",
        "type": "apikey"
      },
      "last_modified_time": 1781017803244,
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
                "URL",
                "URL Referer"
              ]
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_urlscanio",
      "object_type": "artifact",
      "playbook_change_log_info": {
        "change_log_id": 47,
        "change_log_items": [],
        "change_number": 4,
        "change_number_prefix": "74629734-7afa-4a41-94f6-4be073d1997f",
        "create_date": 1781017803054,
        "modified_principal": {
          "display_name": "aaa",
          "id": 4,
          "name": "2683b631-db4a-4209-baaf-2ee08660fbeb",
          "type": "apikey"
        }
      },
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_60ef90bb-4aad-4ce6-90df-a7431e41c0eb",
        "id": 19,
        "name": "playbook_60ef90bb_4aad_4ce6_90df_a7431e41c0eb",
        "type": "playbook",
        "uuid": "7796b85d-26a6-49bc-8c62-d8475517de25"
      },
      "tags": [],
      "type": "default",
      "uuid": "60ef90bb-4aad-4ce6-90df-a7431e41c0eb",
      "version": 6
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 20726,
    "f": 0,
    "m": 8,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.8.0.20726"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_urlscanio",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_urlscanio\" isExecutable=\"true\" name=\"Example: urlscan.io\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0wcctos\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0m3chvd\" name=\"Scan with urlscan.io\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d19c1f00-b4f1-4480-b8a3-7bdd19143041\"\u003e{\"inputs\":{\"ee9263c1-432a-41a8-8bbd-6917d35fb3ac\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"# The result contains,\\n# {\\n#   \\\"png_url\\\": the URL of the screenshot image\\n#   \\\"png_base64content\\\": the base64-encoded screenshot (PNG)\\n#   \\\"report_url\\\": the URL of the JSON report_url\\n#   \\\"report\\\": the JSON report, which will contain lots of detail of the page analysis (see urlscan.io for details).\\n# }\\n#\\n# In this case, the file is already attached to the incident.  Nothing to do here.\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# This is an artifact workflow; \\n# The URL to scan is the artifact value\\ninputs.urlscanio_url = artifact.value\\n\\n# Set the incident id\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"urlscanio\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wcctos\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0oivuzv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0wcctos\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0m3chvd\"/\u003e\u003cendEvent id=\"EndEvent_0rbv6vt\"\u003e\u003cincoming\u003eSequenceFlow_0oivuzv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0oivuzv\" sourceRef=\"ServiceTask_0m3chvd\" targetRef=\"EndEvent_0rbv6vt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eRun for a URL artifact\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0wbrg5r\"\u003e\u003ctext\u003eScan the URL\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pw8z8e\" sourceRef=\"ServiceTask_0m3chvd\" targetRef=\"TextAnnotation_0wbrg5r\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"160\" y=\"185\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"155\" y=\"220\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"100\" x=\"160\" y=\"85\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"180\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"200\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0m3chvd\" id=\"ServiceTask_0m3chvd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"163\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wcctos\" id=\"SequenceFlow_0wcctos_di\"\u003e\u003comgdi:waypoint x=\"196\" y=\"203\"/\u003e\u003comgdi:waypoint x=\"279\" y=\"203\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"237.5\" y=\"181.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0wbrg5r\" id=\"TextAnnotation_0wbrg5r_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"379\" y=\"83\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pw8z8e\" id=\"Association_0pw8z8e_di\"\u003e\u003comgdi:waypoint x=\"367\" y=\"163\"/\u003e\u003comgdi:waypoint x=\"415\" y=\"113\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0rbv6vt\" id=\"EndEvent_0rbv6vt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"450\" y=\"185\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"468\" y=\"224\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0oivuzv\" id=\"SequenceFlow_0oivuzv_di\"\u003e\u003comgdi:waypoint x=\"379\" y=\"203\"/\u003e\u003comgdi:waypoint x=\"450\" y=\"203\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414.5\" y=\"181\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "",
      "export_key": "example_urlscanio",
      "last_modified_by": "admin@co3sys.com",
      "last_modified_time": 1781081494432,
      "name": "Example: urlscan.io",
      "object_type": "artifact",
      "programmatic_name": "example_urlscanio",
      "tags": [],
      "uuid": "c253fa8f-56c8-45e9-84be-c16cf4b65b36",
      "workflow_id": 19
    }
  ],
  "workspaces": []
}
