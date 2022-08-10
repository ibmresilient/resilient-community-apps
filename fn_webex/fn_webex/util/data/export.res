{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1660130749681,
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
      "export_key": "__function/webex_team_id",
      "hide_notification": false,
      "id": 294,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_team_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8dc95f18-ff66-4ac4-a29e-a35c7ad3730f",
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
      "export_key": "__function/webex_incident_id",
      "hide_notification": false,
      "id": 289,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Leave this field blank",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9aa23a09-3fd0-4f44-8932-729d1edff840",
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
      "export_key": "__function/webex_meeting_end_time",
      "hide_notification": false,
      "id": 281,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_end_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
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
      "export_key": "__function/webex_room_name",
      "hide_notification": false,
      "id": 290,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_room_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_room_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ae2a9043-96f5-4ab8-915c-52d898dfdd0b",
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
      "export_key": "__function/webex_meeting_attendees",
      "hide_notification": false,
      "id": 286,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_attendees",
      "operation_perms": {},
      "operations": [],
      "placeholder": "If only specific members are to be added, specify their email addresses in a comma-separated manner and set add_all_members to NO",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_meeting_attendees",
      "tooltip": "The list of email address of the attendees in a space-seperated format. Leave blank to select all attendees",
      "type_id": 11,
      "uuid": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
      "export_key": "__function/webex_meeting_password",
      "hide_notification": false,
      "id": 278,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_password",
      "tooltip": "Meeting password",
      "type_id": 11,
      "uuid": "03dd1531-acbb-4db8-9950-53520eabbb5c",
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
      "export_key": "__function/webex_add_all_members",
      "hide_notification": false,
      "id": 288,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "webex_add_all_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_add_all_members",
      "tooltip": "Select this option to add all members to the webex meeting. If only selected members are to be added, specify their email address below.",
      "type_id": 11,
      "uuid": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
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
      "export_key": "__function/webex_meeting_name",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_name",
      "tooltip": "Meeting name",
      "type_id": 11,
      "uuid": "14438dc7-4874-4971-9aa7-5596b13276a1",
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
      "export_key": "__function/webex_meeting_agenda",
      "hide_notification": false,
      "id": 279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_agenda",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_agenda",
      "tooltip": "Meeting agenda",
      "type_id": 11,
      "uuid": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
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
      "export_key": "__function/webex_meeting_start_time",
      "hide_notification": false,
      "id": 282,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "webex_meeting_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "templates": [],
      "text": "webex_meeting_start_time",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5706ac62-97ee-4b54-9807-9f4b124ececc",
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
      "export_key": "__function/webex_team_name",
      "hide_notification": false,
      "id": 292,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "webex_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "webex_team_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "6f5a8140-bebb-45a5-b639-6d581fc49f3e",
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
      "created_date": 1659727541157,
      "description": {
        "content": "A function to create meetings",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Meeting",
      "export_key": "webex_create_meeting",
      "id": 4,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1659727541179,
      "name": "webex_create_meeting",
      "tags": [],
      "uuid": "674a0970-dab8-4bd1-8e67-4ac8d5068b38",
      "version": 1,
      "view_items": [
        {
          "content": "9d368a2f-edf4-4353-a8ba-37f86c5a84e7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5706ac62-97ee-4b54-9807-9f4b124ececc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "14438dc7-4874-4971-9aa7-5596b13276a1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03dd1531-acbb-4db8-9950-53520eabbb5c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b179897-3cfc-4a98-8864-d9c09e685d5a",
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
          "name": "WebEx Platform",
          "object_type": "incident",
          "programmatic_name": "webex_platform",
          "tags": [
            {
              "tag_handle": "fn_webex",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1656947489905,
      "description": {
        "content": "Creates a WebEx meeting and returns the Host URL and Attendee URL.",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Room",
      "export_key": "webex_create_room",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1660043631805,
      "name": "webex_create_room",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "ab9bd63a-728e-4c80-aa36-27e288813c34",
      "version": 53,
      "view_items": [
        {
          "content": "8dc95f18-ff66-4ac4-a29e-a35c7ad3730f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9aa23a09-3fd0-4f44-8932-729d1edff840",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae2a9043-96f5-4ab8-915c-52d898dfdd0b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
          "name": "Webex: Create Room",
          "object_type": "incident",
          "programmatic_name": "workflow_create_room",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        },
        {
          "actions": [],
          "description": null,
          "name": "Webex: Create Team with Room",
          "object_type": "incident",
          "programmatic_name": "create_webex_team_with_room",
          "tags": [],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    },
    {
      "created_date": 1659727464787,
      "description": {
        "content": "A function to create Webex teams",
        "format": "text"
      },
      "destination_handle": "fn_webex",
      "display_name": "Webex: Create Team",
      "export_key": "webex_create_team",
      "id": 3,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1659968954998,
      "name": "webex_create_team",
      "tags": [],
      "uuid": "7e202188-beda-403c-b0e8-0b626c201382",
      "version": 5,
      "view_items": [
        {
          "content": "9aa23a09-3fd0-4f44-8932-729d1edff840",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6f5a8140-bebb-45a5-b639-6d581fc49f3e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0bc70659-40ad-4178-9174-c7841eb3c9b3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9a26148-b7ad-480a-9a61-b39061df91e5",
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
          "name": "Webex: Create Team",
          "object_type": "incident",
          "programmatic_name": "webex_create_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Webex: Create Team with Room",
          "object_type": "incident",
          "programmatic_name": "create_webex_team_with_room",
          "tags": [],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 17,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1660130747240,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1660130747240,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "d26fee39-8a4f-4845-afa3-701a5786c30a",
        "e14b8f3e-6652-408c-8abf-448093f7f4ea"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_webex",
      "name": "fn_webex",
      "programmatic_name": "fn_webex",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "users": [],
      "uuid": "7fc77005-9552-4cbe-90c6-d9b6037c937c"
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
        "version": 86,
        "workflow_id": "webex_platform",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"webex_platform\" isExecutable=\"true\" name=\"WebEx Platform\"\u003e\u003cdocumentation\u003eA platform to create a meeting with team members\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1jvh0lg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cp3aej\" name=\"Webex: Create Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"674a0970-dab8-4bd1-8e67-4ac8d5068b38\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Cisco WebEx Meeting\\\"\\n\\n  fail_reason = content.get(\\\"fail_reason\\\")\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\nelse:\\n  ref_html_room = u\\\"\\\"\\\"\u0026lt;a href=\u0027{0}\u0027\u0026gt;Link\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(content.get(\\\"meetingLink\\\"))\\n\\n  text = u\\\"\u0026lt;b\u0026gt;Cisco WebEx Meeting Links:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;Webex Room URL: {0}\\\".format(ref_html_room)\\n  for key in content:\\n      text += u\\\"\u0026lt;br /\u0026gt;{} : {}\\\".format(key, content.get(key))\\n  \\nnote = helper.createRichText(text)\\nincident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# To set meeting name to the workflow inputs, uncomment the following lines\\ninputs.webex_meeting_name = incident.name\\ninputs.webex_incident_id = str(incident.id)\\n\\n# Get the agenda from the activity field or the incident description\\nif rule.properties.webex_meeting_agenda is None:\\n  if incident.description is not None and incident.description.content is not None:\\n    inputs.webex_meeting_agenda = incident.description.content\\n  else:\\n    inputs.webex_meeting_agenda = \\\"\\\"\\nelse:\\n  inputs.webex_meeting_agenda = rule.properties.webex_meeting_agenda\\n\\ninputs.webex_meeting_password = inputs.webex_meeting_password if rule.properties.webex_meeting_password is None else rule.properties.webex_meeting_password\\n\\nif rule.properties.webex_meeting_attendee:\\n    inputs.webex_meeting_attendee = rule.properties.webex_meeting_attendee\\n    \\nif rule.properties.webex_add_all_members is not None:\\n    inputs.webex_add_all_members = rule.properties.webex_add_all_members\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1jvh0lg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_12scroy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_04gd8py\"\u003e\u003cincoming\u003eSequenceFlow_12scroy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1jvh0lg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cp3aej\"/\u003e\u003csequenceFlow id=\"SequenceFlow_12scroy\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"EndEvent_04gd8py\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_172tdgi\"\u003e\u003ctext\u003eInputs:\u00a0webex_meeting_name, webex_meeting_agenda, and webex_meeting_password\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0nvlnia\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"TextAnnotation_172tdgi\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01xqm6h\"\u003e\u003ctext\u003eOutputs: host_url and attendee_url written to incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1aeawdv\" sourceRef=\"ServiceTask_0cp3aej\" targetRef=\"TextAnnotation_01xqm6h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_121irbg\"\u003e\u003ctext\u003e\u003c![CDATA[Workflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1kqsb5m\" sourceRef=\"EndEvent_04gd8py\" targetRef=\"TextAnnotation_121irbg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"175\" y=\"251\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"170\" y=\"286\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"65\" y=\"347\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"280\"/\u003e\u003comgdi:waypoint x=\"124\" xsi:type=\"omgdc:Point\" y=\"347\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cp3aej\" id=\"ServiceTask_0cp3aej_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"614\" y=\"229\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_172tdgi\" id=\"TextAnnotation_172tdgi_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"433\" x=\"44\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0nvlnia\" id=\"Association_0nvlnia_di\"\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"248\"/\u003e\u003comgdi:waypoint x=\"296\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01xqm6h\" id=\"TextAnnotation_01xqm6h_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"378\" x=\"854\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1aeawdv\" id=\"Association_1aeawdv_di\"\u003e\u003comgdi:waypoint x=\"714\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"1010\" xsi:type=\"omgdc:Point\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04gd8py\" id=\"EndEvent_04gd8py_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1113.2577962577961\" y=\"251\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"1131.2577962577961\" y=\"290\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_121irbg\" id=\"TextAnnotation_121irbg_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"1249\" y=\"347\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1kqsb5m\" id=\"Association_1kqsb5m_di\"\u003e\u003comgdi:waypoint x=\"1147\" xsi:type=\"omgdc:Point\" y=\"278\"/\u003e\u003comgdi:waypoint x=\"1272\" xsi:type=\"omgdc:Point\" y=\"347\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jvh0lg\" id=\"SequenceFlow_1jvh0lg_di\"\u003e\u003comgdi:waypoint x=\"211\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"412.5\" y=\"247\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12scroy\" id=\"SequenceFlow_12scroy_di\"\u003e\u003comgdi:waypoint x=\"714\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"1113\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"913.5\" y=\"247\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 86,
      "description": "A platform to create a meeting with team members",
      "export_key": "webex_platform",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1659727979652,
      "name": "WebEx Platform",
      "object_type": "incident",
      "programmatic_name": "webex_platform",
      "tags": [
        {
          "tag_handle": "fn_webex",
          "value": null
        }
      ],
      "uuid": "8c7a52f8-0dfc-4e8c-ba3e-d0207cb906c2",
      "workflow_id": 4
    }
  ],
  "workspaces": []
}
