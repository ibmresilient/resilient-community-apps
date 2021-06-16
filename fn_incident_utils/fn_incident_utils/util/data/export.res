{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "equals",
          "type": null,
          "value": "Active"
        }
      ],
      "enabled": true,
      "export_key": "Example: Close Incident",
      "id": 107,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Close Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d99c9d49-a821-4f5d-9c92-2865396d62c8",
      "view_items": [
        {
          "content": "f1fe36a5-df27-49f0-85d3-834987ee4f69",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_close_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Create Incident",
      "id": 108,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Create Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c6c84d90-b042-4130-8518-8efac76d7666",
      "view_items": [
        {
          "content": "7142e7a1-93ed-423a-9961-56a14eecd523",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_create_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Search Incidents",
      "id": 109,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Search Incidents",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1b34e3b1-ec03-42ad-bd7f-fef69c1c25c3",
      "view_items": [
        {
          "content": "c798c197-f1d0-4864-9d8d-88fb738cfcb9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3d261eda-ef8c-46bf-ac20-26a0c741c5cb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_search_incidents"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1623874338491,
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
      "export_key": "__function/inc_sort_fields",
      "hide_notification": false,
      "id": 427,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "inc_sort_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"id\", \"type\": \"asc\"}]",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "inc_sort_fields",
      "tooltip": "json fields to order result set",
      "type_id": 11,
      "uuid": "a1a561e1-cf35-4b4b-9bea-4fb5e5eda25b",
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
      "id": 242,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        },
        {
          "tag_handle": "fn_scheduler",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
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
      "export_key": "__function/inc_create_fields",
      "hide_notification": false,
      "id": 428,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "inc_create_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"name\": \"sample\", \"description\": \"sample incident\", \"discovered_date\": 1621110044000}",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "inc_create_fields",
      "tooltip": "json fields to create an incident",
      "type_id": 11,
      "uuid": "b8e180a8-c1b2-4cdd-9c2d-6769a6fd369b",
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
      "export_key": "__function/inc_filter_conditions",
      "hide_notification": false,
      "id": 429,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "inc_filter_conditions",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"name\", \"method\":\"contains\", \"value\":\"sample\"}]",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "inc_filter_conditions",
      "tooltip": "json fields to filter incident records to return",
      "type_id": 11,
      "uuid": "5cba9f1e-de0d-4f09-945b-3c0d33868fe0",
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
      "export_key": "__function/close_fields",
      "hide_notification": false,
      "id": 430,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "close_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "close_fields",
      "tooltip": "A JSON String of the fields required to close an Incident e.g.: {\u0027resolution_id\u0027:\u0027Resolved\u0027,\u0027resolution_summary\u0027:\u0027closing\u0027}",
      "type_id": 11,
      "uuid": "7ad06245-c2a6-4ab4-83fd-4eac1deb83ee",
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
      "export_key": "actioninvocation/inc_search_fields",
      "hide_notification": false,
      "id": 423,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "inc_search_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"create_date\",\"method\":\"gte\",\"value\":1614574800000}]",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Search Fields",
      "tooltip": "json portion of search filter values or leave empty",
      "type_id": 6,
      "uuid": "c798c197-f1d0-4864-9d8d-88fb738cfcb9",
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
      "export_key": "actioninvocation/incident_utils_close_fields",
      "hide_notification": false,
      "id": 424,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "incident_utils_close_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "e.g.: {\"resolution_id\":\"Resolved\",\"resolution_summary\":\"closing\"}",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Incident Utils Close Fields",
      "tooltip": "Enter a JSON String of the fields required to close an Incident",
      "type_id": 6,
      "uuid": "f1fe36a5-df27-49f0-85d3-834987ee4f69",
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
      "export_key": "actioninvocation/inc_sort_fields",
      "hide_notification": false,
      "id": 425,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "inc_sort_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[{\"field_name\":\"id\",\"type\":\"asc\"}]",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Sort Fields",
      "tooltip": "json formatted sort fields or leave empty",
      "type_id": 6,
      "uuid": "3d261eda-ef8c-46bf-ac20-26a0c741c5cb",
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
      "export_key": "actioninvocation/inc_create_fields",
      "hide_notification": false,
      "id": 426,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "inc_create_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"name\": \"sample\", \"description\": \"sample incident\", \"discovered_date\": 1621110044000}",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "templates": [],
      "text": "Create Fields",
      "tooltip": "json format used by incident API call",
      "type_id": 6,
      "uuid": "7142e7a1-93ed-423a-9961-56a14eecd523",
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
        "content": "Function that takes an incident_id and a JSON String of field_name and field_value pairs to close an Incident.",
        "format": "text"
      },
      "destination_handle": "fn_incident_utils",
      "display_name": "Incident Utils: Close Incident",
      "export_key": "incident_utils_close_incident",
      "id": 73,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1621348642755,
      "name": "incident_utils_close_incident",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "7a1156f7-a00d-4f75-8035-a41f40ac980f",
      "version": 1,
      "view_items": [
        {
          "content": "b13a40e3-e7ff-464e-966c-aea83eb5abb9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7ad06245-c2a6-4ab4-83fd-4eac1deb83ee",
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
          "name": "Example: Close Incident",
          "object_type": "incident",
          "programmatic_name": "example_close_incident",
          "tags": [
            {
              "tag_handle": "fn_incident_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 88
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create an incident from a function",
        "format": "text"
      },
      "destination_handle": "fn_incident_utils",
      "display_name": "Incident Utils: Create Incident",
      "export_key": "incident_utils_create_incident",
      "id": 74,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1621348642784,
      "name": "incident_utils_create_incident",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "692045df-6155-44aa-99ca-f24ab4f59d5b",
      "version": 1,
      "view_items": [
        {
          "content": "b8e180a8-c1b2-4cdd-9c2d-6769a6fd369b",
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
          "name": "create incident",
          "object_type": "incident",
          "programmatic_name": "create_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 89
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Create Incident",
          "object_type": "incident",
          "programmatic_name": "example_create_incident",
          "tags": [
            {
              "tag_handle": "fn_incident_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 87
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Search for incidents based on filter criteria. Sorting field are optional",
        "format": "text"
      },
      "destination_handle": "fn_incident_utils",
      "display_name": "Incident Utils: Search Incidents",
      "export_key": "search_incidents",
      "id": 75,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1621348642810,
      "name": "search_incidents",
      "output_json_example": "{}",
      "output_json_schema": "{}",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "6bc47d48-9a3d-4e31-9fc6-111834d965ba",
      "version": 1,
      "view_items": [
        {
          "content": "5cba9f1e-de0d-4f09-945b-3c0d33868fe0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1a561e1-cf35-4b4b-9bea-4fb5e5eda25b",
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
          "name": "Example: Search Incidents",
          "object_type": "incident",
          "programmatic_name": "example_search_incidents",
          "tags": [
            {
              "tag_handle": "fn_incident_utils",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 86
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 20,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1623874335820,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1623874335820,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "33750e61-0f57-4484-92be-58930422924d"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_incident_utils",
      "name": "fn_incident_utils",
      "programmatic_name": "fn_incident_utils",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "36e9f3fc-c3e9-4bcf-85bd-ab22446c2461"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6006,
    "major": 38,
    "minor": 0,
    "version": "38.0.6006"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "example_search_incidents",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_search_incidents\" isExecutable=\"true\" name=\"Example: Search Incidents\"\u003e\u003cdocumentation\u003eSearch incidents based on filtering fields. Sort field are optional\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0tolny9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03e7sxd\" name=\"Incident Utils: Search Incidents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6bc47d48-9a3d-4e31-9fc6-111834d965ba\"\u003e{\"inputs\":{},\"post_processing_script\":\"msgs = [u\\\"Filter conditions: {}\\\".format(results.inputs[\u0027inc_filter_conditions\u0027])]\\nif results.success:\\n  for inc in results.content[\u0027data\u0027]:\\n    msgs.append(u\\\"id: \u0026lt;a target=\u0027blank\u0027 href=\u0027/#incidents/{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt; Name: {1}\\\".format(inc[\u0027id\u0027], inc[\u0027name\u0027]))\\n  incident.addNote(helper.createRichText(u\\\"Found {} incidents\u0026lt;br\u0026gt;{}\\\".format(results.content[\u0027recordsTotal\u0027], \u0027\u0026lt;br\u0026gt;\u0027.join(msgs))))\\n\\nelse:\\n  incident.addNote(u\\\"Search error found: {}\\\".format(results.reason))\\n  \",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.inc_filter_conditions = rule.properties.inc_search_fields.content\\ninputs.inc_sort_fields = rule.properties.inc_sort_fields.content\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0tolny9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0u8am6f\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0tolny9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03e7sxd\"/\u003e\u003cendEvent id=\"EndEvent_0yuw550\"\u003e\u003cincoming\u003eSequenceFlow_0u8am6f\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0u8am6f\" sourceRef=\"ServiceTask_03e7sxd\" targetRef=\"EndEvent_0yuw550\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ud2lnr\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i22lbk\" sourceRef=\"ServiceTask_03e7sxd\" targetRef=\"TextAnnotation_0ud2lnr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03e7sxd\" id=\"ServiceTask_03e7sxd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"253\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tolny9\" id=\"SequenceFlow_0tolny9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"225.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0yuw550\" id=\"EndEvent_0yuw550_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"419\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"437\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u8am6f\" id=\"SequenceFlow_0u8am6f_di\"\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"419\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"386\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ud2lnr\" id=\"TextAnnotation_0ud2lnr_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"167\" x=\"348\" y=\"88\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i22lbk\" id=\"Association_1i22lbk_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@example.com",
      "description": "Search incidents based on filtering fields. Sort field are optional",
      "export_key": "example_search_incidents",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1623872969093,
      "name": "Example: Search Incidents",
      "object_type": "incident",
      "programmatic_name": "example_search_incidents",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "102016b8-3084-4b7d-810a-1c12c5206e68",
      "workflow_id": 86
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_close_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_close_incident\" isExecutable=\"true\" name=\"Example: Close Incident\"\u003e\u003cdocumentation\u003eAn example workflow which takes an incident_id and optional close_fields in order to close an Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1km8q9o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q692s2\" name=\"Incident Utils: Close Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7a1156f7-a00d-4f75-8035-a41f40ac980f\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = \\\"Result from Example: Close Incident on Incident {0}: \u0026lt;strong\u0026gt;{1}\u0026lt;/strong\u0026gt;\\\".format(results.inputs[\u0027incident_id\u0027], \\\\\\n\\\"success\\\" if results.success else \\\"failure.\u0026lt;br\u0026gt;Reason: {}\\\".format(results.reason))\\nincident.addNote(helper.createRichText(note_text))\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\niu_close_fields = rule.properties.incident_utils_close_fields.content\\ninputs.close_fields = u\\\"{}\\\".format(iu_close_fields)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1km8q9o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vycngo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1km8q9o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q692s2\"/\u003e\u003cendEvent id=\"EndEvent_06dl3od\"\u003e\u003cincoming\u003eSequenceFlow_0vycngo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vycngo\" sourceRef=\"ServiceTask_0q692s2\" targetRef=\"EndEvent_06dl3od\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1f5owg0\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\nincident_id, close_fields]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_027r5qp\" sourceRef=\"ServiceTask_0q692s2\" targetRef=\"TextAnnotation_1f5owg0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1jdoe1s\"\u003e\u003ctext\u003e\u003c![CDATA[Output:\nCloses the Incident should reflect the action after the function runs. A Note is created with the function results.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_00ycowm\" sourceRef=\"ServiceTask_0q692s2\" targetRef=\"TextAnnotation_1jdoe1s\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q692s2\" id=\"ServiceTask_0q692s2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"352\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1km8q9o\" id=\"SequenceFlow_1km8q9o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"290\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1f5owg0\" id=\"TextAnnotation_1f5owg0_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"98\" x=\"231\" y=\"33\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_027r5qp\" id=\"Association_027r5qp_di\"\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"305\" xsi:type=\"omgdc:Point\" y=\"91\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1jdoe1s\" id=\"TextAnnotation_1jdoe1s_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"221\" x=\"465\" y=\"12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_00ycowm\" id=\"Association_00ycowm_di\"\u003e\u003comgdi:waypoint x=\"445\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"533\" xsi:type=\"omgdc:Point\" y=\"92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06dl3od\" id=\"EndEvent_06dl3od_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"596.8037974683544\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"614.8037974683544\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vycngo\" id=\"SequenceFlow_0vycngo_di\"\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"597\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"524.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "a@example.com",
      "description": "An example workflow which takes an incident_id and optional close_fields in order to close an Incident.",
      "export_key": "example_close_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1621348643115,
      "name": "Example: Close Incident",
      "object_type": "incident",
      "programmatic_name": "example_close_incident",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "348d10f7-14e3-42bf-8ef8-5834faeb25b1",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "example_create_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_create_incident\" isExecutable=\"true\" name=\"Example: Create Incident\"\u003e\u003cdocumentation\u003eCreate an incident based on json field data. Artifacts and notes can be created at the same time.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dts2gk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0009aa3\" name=\"Incident Utils: Create Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"692045df-6155-44aa-99ca-f24ab4f59d5b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  link = u\u0027\u0026lt;a href=\\\"#incidents/{0}\\\"\u0026gt;{0}: {1}\u0026lt;/a\u0026gt;\u0027.format(results.content[\u0027id\u0027], results.content[\u0027name\u0027])\\n  incident.addNote(helper.createRichText(u\\\"Incident successfully created: {}\\\".format(link)))\\nelse:\\n  incident.addNote(u\\\"Incident creation failed: {}\\\".format(results.reason))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.inc_create_fields = rule.properties.inc_create_fields.content\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dts2gk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1chgj49\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dts2gk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0009aa3\"/\u003e\u003cendEvent id=\"EndEvent_0tkxmrt\"\u003e\u003cincoming\u003eSequenceFlow_1chgj49\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1chgj49\" sourceRef=\"ServiceTask_0009aa3\" targetRef=\"EndEvent_0tkxmrt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0e1evk3\"\u003e\u003ctext\u003e\u003c![CDATA[A note with the results is added\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17x4jrp\" sourceRef=\"ServiceTask_0009aa3\" targetRef=\"TextAnnotation_0e1evk3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0009aa3\" id=\"ServiceTask_0009aa3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"256\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dts2gk\" id=\"SequenceFlow_0dts2gk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"256\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"227\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tkxmrt\" id=\"EndEvent_0tkxmrt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"407\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"425\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1chgj49\" id=\"SequenceFlow_1chgj49_di\"\u003e\u003comgdi:waypoint x=\"356\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"407\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"381.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0e1evk3\" id=\"TextAnnotation_0e1evk3_di\"\u003e\u003comgdc:Bounds height=\"44\" width=\"203\" x=\"350\" y=\"74\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17x4jrp\" id=\"Association_17x4jrp_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "a@example.com",
      "description": "Create an incident based on json field data. Artifacts and notes can be created at the same time.",
      "export_key": "example_create_incident",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1623872836213,
      "name": "Example: Create Incident",
      "object_type": "incident",
      "programmatic_name": "example_create_incident",
      "tags": [
        {
          "tag_handle": "fn_incident_utils",
          "value": null
        }
      ],
      "uuid": "a5e2f053-4f72-4f72-a270-8e14f18090d8",
      "workflow_id": 87
    }
  ],
  "workspaces": []
}
