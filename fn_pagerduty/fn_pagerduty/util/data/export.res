{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.pd_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "note.text",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": null,
          "method": "object_added",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Create PagerDuty Note",
      "id": 34,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Create PagerDuty Note",
      "object_type": "note",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "5e4a6216-38fc-4235-8fd1-ed87b2135000",
      "view_items": [],
      "workflows": [
        "pagerduty_create_note"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.pd_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_summary",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Resolve PagerDuty Incident",
      "id": 35,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Resolve PagerDuty Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "f70b5585-876e-42a2-9877-bd714c4ed50d",
      "view_items": [],
      "workflows": [
        "pagerduty_transition_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.pd_incident_id",
          "method": "not_has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Trigger PagerDuty Incident",
      "id": 36,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Trigger PagerDuty Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9f176a11-3160-4183-b19e-a824786931d4",
      "view_items": [],
      "workflows": [
        "pagerduty_create_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.pd_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "incident.severity_code",
          "method": "changed",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Update PagerDuty Incident",
      "id": 37,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Update PagerDuty Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "169c694a-6411-4fbf-a856-3dfb9e18b4ab",
      "view_items": [],
      "workflows": [
        "pagerduty_transition_incident"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1657914234136,
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
      "export_key": "__function/pd_service",
      "hide_notification": false,
      "id": 333,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_service",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_service",
      "tooltip": "service name from pagerduty",
      "type_id": 11,
      "uuid": "8982957c-9571-453b-9aae-77eae0be4113",
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
      "export_key": "__function/pd_priority",
      "hide_notification": false,
      "id": 330,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_priority",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_priority",
      "tooltip": "incident priority",
      "type_id": 11,
      "uuid": "b9bfdf7a-8216-4fbd-9d4e-8243767f7739",
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
      "export_key": "__function/pd_incident_id",
      "hide_notification": false,
      "id": 332,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_incident_id",
      "tooltip": "id of incident",
      "type_id": 11,
      "uuid": "116ceabb-9014-44b3-ad2a-7db477f01ee3",
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
      "export_key": "__function/pd_incident_key",
      "hide_notification": false,
      "id": 328,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_incident_key",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_incident_key",
      "tooltip": "used during acknowledge and resolve event actions",
      "type_id": 11,
      "uuid": "13f91ce2-3c5a-4724-b55c-b58d8b2aa4e2",
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
      "export_key": "__function/pd_status",
      "hide_notification": false,
      "id": 329,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "232c535c-8d4a-4fbc-be40-009eb1099abf",
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
      "export_key": "__function/pd_title",
      "hide_notification": false,
      "id": 327,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_title",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_title",
      "tooltip": "",
      "type_id": 11,
      "uuid": "3d7f37e8-38c6-4dfb-8d0d-36d34623533a",
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
      "export_key": "__function/pd_escalation_policy",
      "hide_notification": false,
      "id": 326,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_escalation_policy",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_escalation_policy",
      "tooltip": "escalation policy name from pagerduty",
      "type_id": 11,
      "uuid": "3fc76022-247a-4076-a1fb-9b564c9ebb0f",
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
      "export_key": "__function/incidentID",
      "hide_notification": false,
      "id": 325,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incidentID",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incidentID",
      "tooltip": "",
      "type_id": 11,
      "uuid": "47cd0f65-b766-47be-8735-f309851d1515",
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
      "export_key": "__function/pd_description",
      "hide_notification": false,
      "id": 331,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "pd_description",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6f29225a-7593-4fab-b81b-1a20b401a710",
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
      "export_key": "incident/pd_incident_id",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pd_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_pagerduty",
          "value": null
        }
      ],
      "templates": [],
      "text": "PagerDuty Incident ID",
      "tooltip": "field to contain the pagerduty incident Id created",
      "type_id": 0,
      "uuid": "e9ca1e45-845b-4117-942a-41074e9ee096",
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
      "export_key": "incident/pd_incident_url",
      "hide_notification": false,
      "id": 278,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "pd_incident_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_pagerduty",
          "value": null
        }
      ],
      "templates": [],
      "text": "PagerDuty Incident URL",
      "tooltip": "",
      "type_id": 0,
      "uuid": "15fbd365-9042-4eee-a322-4e49b07b5ce1",
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
      "created_date": 1657902999913,
      "description": {
        "content": "Create a PagerDuty Incident based on a Resilient Incident",
        "format": "text"
      },
      "destination_handle": "pagerduty",
      "display_name": "PagerDuty Create Incident",
      "export_key": "pagerduty_create_incident",
      "id": 17,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1657903685564,
      "name": "pagerduty_create_incident",
      "tags": [],
      "uuid": "dec7e0d3-fd7f-4f22-b74a-d825428eda34",
      "version": 3,
      "view_items": [
        {
          "content": "47cd0f65-b766-47be-8735-f309851d1515",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3d7f37e8-38c6-4dfb-8d0d-36d34623533a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6f29225a-7593-4fab-b81b-1a20b401a710",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8982957c-9571-453b-9aae-77eae0be4113",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3fc76022-247a-4076-a1fb-9b564c9ebb0f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9bfdf7a-8216-4fbd-9d4e-8243767f7739",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13f91ce2-3c5a-4724-b55c-b58d8b2aa4e2",
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
          "name": "PagerDuty Create Incident",
          "object_type": "incident",
          "programmatic_name": "pagerduty_create_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1657902999990,
      "description": {
        "content": "Create a PagerDuty Note based on a Resilient Incident\u0027s Note",
        "format": "text"
      },
      "destination_handle": "pagerduty",
      "display_name": "PagerDuty Create Note",
      "export_key": "pagerduty_create_note",
      "id": 18,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1657903685598,
      "name": "pagerduty_create_note",
      "tags": [],
      "uuid": "efdef5a6-796a-412a-bee7-5edd42ef92b3",
      "version": 3,
      "view_items": [
        {
          "content": "116ceabb-9014-44b3-ad2a-7db477f01ee3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6f29225a-7593-4fab-b81b-1a20b401a710",
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
          "name": "PagerDuty Create Note",
          "object_type": "note",
          "programmatic_name": "pagerduty_create_note",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1657903000047,
      "description": {
        "content": "Transition a PagerDuty Incident based on changes to a Resilient Incident (such as Closing the Incident)",
        "format": "text"
      },
      "destination_handle": "pagerduty",
      "display_name": "PagerDuty Transition Incident",
      "export_key": "pagerduty_transition_incident",
      "id": 19,
      "last_modified_by": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "last_modified_time": 1657903685632,
      "name": "pagerduty_transition_incident",
      "tags": [],
      "uuid": "1b89c0c8-91fc-407a-8ec0-1b63851eaa20",
      "version": 3,
      "view_items": [
        {
          "content": "116ceabb-9014-44b3-ad2a-7db477f01ee3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9bfdf7a-8216-4fbd-9d4e-8243767f7739",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "232c535c-8d4a-4fbc-be40-009eb1099abf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6f29225a-7593-4fab-b81b-1a20b401a710",
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
          "name": "PagerDuty Transition Incident",
          "object_type": "incident",
          "programmatic_name": "pagerduty_transition_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 11,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1657914232264,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1657914232264,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "pagerduty",
      "name": "pagerduty",
      "programmatic_name": "pagerduty",
      "tags": [],
      "users": [],
      "uuid": "988db4b3-27b6-46cf-a6e2-2180efd89d96"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "pagerduty_create_note",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pagerduty_create_note\" isExecutable=\"true\" name=\"PagerDuty Create Note\"\u003e\u003cdocumentation\u003eCreate a PagerDuty Note based on a Resilient Incident Note. The rule for this workflow should only trigger if a PagerDuty Incident has already been created.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0geppld\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0oipeed\" name=\"PagerDuty Create Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"efdef5a6-796a-412a-bee7-5edd42ef92b3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pd_incident_id = incident.properties.pd_incident_id\\ninputs.pd_description = note.text.content\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0geppld\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0gsdntz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0geppld\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0oipeed\"/\u003e\u003cendEvent id=\"EndEvent_1uo6e51\"\u003e\u003cincoming\u003eSequenceFlow_0gsdntz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0gsdntz\" sourceRef=\"ServiceTask_0oipeed\" targetRef=\"EndEvent_1uo6e51\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_036hwr5\"\u003e\u003ctext\u003eInput includes Resilient Incident Note description\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0opfhdj\" sourceRef=\"ServiceTask_0oipeed\" targetRef=\"TextAnnotation_036hwr5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0oipeed\" id=\"ServiceTask_0oipeed_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"262\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0geppld\" id=\"SequenceFlow_0geppld_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"230\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1uo6e51\" id=\"EndEvent_1uo6e51_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"434\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0gsdntz\" id=\"SequenceFlow_0gsdntz_di\"\u003e\u003comgdi:waypoint x=\"362\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_036hwr5\" id=\"TextAnnotation_036hwr5_di\"\u003e\u003comgdc:Bounds height=\"53\" width=\"166\" x=\"130\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0opfhdj\" id=\"Association_0opfhdj_di\"\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Create a PagerDuty Note based on a Resilient Incident Note. The rule for this workflow should only trigger if a PagerDuty Incident has already been created.",
      "export_key": "pagerduty_create_note",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1657903000613,
      "name": "PagerDuty Create Note",
      "object_type": "note",
      "programmatic_name": "pagerduty_create_note",
      "tags": [],
      "uuid": "f0069d34-6a3a-4cd0-934a-6dfc7a1c73ad",
      "workflow_id": 17
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "pagerduty_transition_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pagerduty_transition_incident\" isExecutable=\"true\" name=\"PagerDuty Transition Incident\"\u003e\u003cdocumentation\u003eTransition a PagerDuty Incident to either acknowledged or resolved. The rule for this workflow should only trigger if a PagerDuty Incident has already been created.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_05krtsc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"SequenceFlow_05krtsc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1praj43\"/\u003e\u003cendEvent id=\"EndEvent_0v4y1vv\"\u003e\u003cincoming\u003eSequenceFlow_089j3v9\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1praj43\" name=\"PagerDuty Transition Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1b89c0c8-91fc-407a-8ec0-1b63851eaa20\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.pd_incident_id = incident.properties.pd_incident_id\\nif incident.resolution_id:\\n  inputs.pd_status = \u0027resolved\u0027\\n  inputs.pd_description = incident.resolution_summary.content\\n#else:\\n#  inputs.pd_status = \u0027acknowledged\u0027\\n  \\npriority = { \u0027Low\u0027: \u0027p3\u0027, \u0027Medium\u0027: \u0027p2\u0027, \u0027High\u0027: \u0027p1\u0027 }\\nif incident.severity_code in priority:\\n  inputs.pd_priority = priority.get(incident.severity_code)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_05krtsc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_089j3v9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_089j3v9\" sourceRef=\"ServiceTask_1praj43\" targetRef=\"EndEvent_0v4y1vv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0mo7kai\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs include an Incident\u0027s priority and resolution summary (if present for closed Incidents). Choose the transition status (acknowledged or resolved) for the Incident\u00a0]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0r5a3pl\" sourceRef=\"ServiceTask_1praj43\" targetRef=\"TextAnnotation_0mo7kai\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05krtsc\" id=\"SequenceFlow_05krtsc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"242\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0v4y1vv\" id=\"EndEvent_0v4y1vv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"508\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"526\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1praj43\" id=\"ServiceTask_1praj43_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"286\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_089j3v9\" id=\"SequenceFlow_089j3v9_di\"\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"508\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"447\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0mo7kai\" id=\"TextAnnotation_0mo7kai_di\"\u003e\u003comgdc:Bounds height=\"62\" width=\"321\" x=\"113\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0r5a3pl\" id=\"Association_0r5a3pl_di\"\u003e\u003comgdi:waypoint x=\"316\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"115\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Transition a PagerDuty Incident to either acknowledged or resolved. The rule for this workflow should only trigger if a PagerDuty Incident has already been created.",
      "export_key": "pagerduty_transition_incident",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1657903000755,
      "name": "PagerDuty Transition Incident",
      "object_type": "incident",
      "programmatic_name": "pagerduty_transition_incident",
      "tags": [],
      "uuid": "ed9375ad-6616-4a9e-a2b7-b44dff57ce0e",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 12,
        "workflow_id": "pagerduty_create_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"pagerduty_create_incident\" isExecutable=\"true\" name=\"PagerDuty Create Incident\"\u003e\u003cdocumentation\u003eCreate a PagerDuty Incident based on a Resilient Incident.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0h5stck\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1sstkd3\" name=\"PagerDuty Create Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"dec7e0d3-fd7f-4f22-b74a-d825428eda34\"\u003e{\"inputs\":{\"8982957c-9571-453b-9aae-77eae0be4113\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"API Service\"}},\"3fc76022-247a-4076-a1fb-9b564c9ebb0f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"default\"}}},\"post_processing_script\":\"incident.properties.pd_incident_id  = results.pd[\u0027incident\u0027][\u0027id\u0027]\\nincident.properties.pd_incident_url = \\\"\u0026lt;a href=\u0027{}\u0027 target=\u0027blank\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\".format(results.pd[\u0027incident\u0027][\u0027html_url\u0027])\",\"pre_processing_script\":\"inputs.incidentID = incident.id\\ninputs.pd_title = \\\"Resilient: {}\\\".format(incident.name)\\ninputs.pd_incident_key = \u0027RES-\u0027+str(incident.id)\\n    \\npriority = { \u0027Low\u0027: \u0027p3\u0027, \u0027Medium\u0027: \u0027p2\u0027, \u0027High\u0027: \u0027p1\u0027 }\\nif incident.severity_code in priority:\\n  inputs.pd_priority = priority.get(incident.severity_code)\\nelse:\\n  inputs.pd_priority = \u0027p4\u0027 # lowest\\n    \\nif not incident.description is None:\\n  inputs.pd_description = incident.description.content\\n\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0h5stck\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0gfoeuc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0h5stck\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1sstkd3\"/\u003e\u003cendEvent id=\"EndEvent_18u16eg\"\u003e\u003cincoming\u003eSequenceFlow_0gfoeuc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0gfoeuc\" sourceRef=\"ServiceTask_1sstkd3\" targetRef=\"EndEvent_18u16eg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kit5qd\"\u003e\u003ctext\u003eChoose the PagerDuty Service and Escalation Policy to use. Incident input fields include: Name, Description, and Priority\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13auxhs\" sourceRef=\"ServiceTask_1sstkd3\" targetRef=\"TextAnnotation_1kit5qd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05vu4uo\"\u003e\u003ctext\u003eSuccessful PagerDuty incident creation will populate a Link back to PagerDuty\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0oob4vf\" sourceRef=\"ServiceTask_1sstkd3\" targetRef=\"TextAnnotation_05vu4uo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sstkd3\" id=\"ServiceTask_1sstkd3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"257\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0h5stck\" id=\"SequenceFlow_0h5stck_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"257\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"227.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_18u16eg\" id=\"EndEvent_18u16eg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"435\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0gfoeuc\" id=\"SequenceFlow_0gfoeuc_di\"\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"396\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kit5qd\" id=\"TextAnnotation_1kit5qd_di\"\u003e\u003comgdc:Bounds height=\"76\" width=\"259\" x=\"-4\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13auxhs\" id=\"Association_13auxhs_di\"\u003e\u003comgdi:waypoint x=\"257\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"186\" xsi:type=\"omgdc:Point\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05vu4uo\" id=\"TextAnnotation_05vu4uo_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"246\" x=\"435\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0oob4vf\" id=\"Association_0oob4vf_di\"\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 12,
      "description": "Create a PagerDuty Incident based on a Resilient Incident.",
      "export_key": "pagerduty_create_incident",
      "last_modified_by": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "last_modified_time": 1657903685825,
      "name": "PagerDuty Create Incident",
      "object_type": "incident",
      "programmatic_name": "pagerduty_create_incident",
      "tags": [],
      "uuid": "2f328cd9-34d7-43b8-b8fe-b8ed7fae6743",
      "workflow_id": 16
    }
  ],
  "workspaces": []
}
