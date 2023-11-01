{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1698842246730,
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
      "export_key": "__function/panorama_request_body",
      "hide_notification": false,
      "id": 4679,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_request_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 4,
          "name": "Edit Address Group Body",
          "template": {
            "content": "{\n  \"entry\": {\n    \"@name\": \"string\",\n    \"description\": \"string\",\n    \"static\": {\n      \"member\": [\n        \"string\"\n      ]\n    },\n    \"dynamic\": {\n      \"filter\": \"string\"\n    },\n    \"tag\": {\n      \"member\": [\n        \"string\"\n      ]\n    }\n  }\n}",
            "format": "text"
          },
          "uuid": "87c12460-0355-40ee-8fef-302a9bf1e808"
        },
        {
          "id": 5,
          "name": "Add Address Body",
          "template": {
            "content": "{\n  \"entry\": {\n    \"@name\": \"string\",\n    \"description\": \"string\",\n    \"ip-netmask\": \"string\",\n    \"ip-range\": \"string\",\n    \"ip-wildcard\": \"string\",\n    \"fqdn\": \"string\",\n    \"tag\": {\n      \"member\": [\n        \"string\"\n      ]\n    }\n  }\n}",
            "format": "text"
          },
          "uuid": "4a74ca30-5fcb-418c-a44e-5446120884d8"
        }
      ],
      "text": "panorama_request_body",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a6a5a64c-8040-4d70-9213-96450e05f87e",
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
      "export_key": "__function/panorama_vsys",
      "hide_notification": false,
      "id": 4680,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_vsys",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_vsys",
      "tooltip": "The name of the vsys when location type is \u0027vsys\u0027 or \u0027panorama-pushed\u0027",
      "type_id": 11,
      "uuid": "c9f1bf5e-1c78-440a-bbe2-a373610200cf",
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
      "export_key": "__function/panorama_label",
      "hide_notification": false,
      "id": 4681,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_label",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_label",
      "tooltip": "Label of the server to use",
      "type_id": 11,
      "uuid": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "export_key": "__function/panorama_location",
      "hide_notification": false,
      "id": 4682,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_location",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_location",
      "tooltip": "The location of the entry",
      "type_id": 11,
      "uuid": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "shared",
          "properties": null,
          "uuid": "b3e3ef89-4dea-4375-86cb-3b3c8bf9d7f1",
          "value": 2211
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vsys",
          "properties": null,
          "uuid": "4910f3d6-367d-4e6f-b6d3-f15ff394773e",
          "value": 2212
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "panorama-pushed",
          "properties": null,
          "uuid": "2ac1f5a8-1d28-4d41-b65d-a701f9ef471b",
          "value": 2213
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
      "export_key": "__function/panorama_name_parameter",
      "hide_notification": false,
      "id": 4683,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_name_parameter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_name_parameter",
      "tooltip": "Useful to return back one item, ie: 1 Address Group",
      "type_id": 11,
      "uuid": "fb0e735b-6a43-461a-87a2-893edc92d24f",
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
      "export_key": "__function/panorama_user_group_xml",
      "hide_notification": false,
      "id": 4684,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_user_group_xml",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 6,
          "name": "example",
          "template": {
            "content": "\u003centry name=\"Blocked_Users\"\u003e\n    \u003cuser\u003e\n      \u003cmember\u003eBlocked_User\u003c/member\u003e\n    \u003c/user\u003e\n\u003c/entry\u003e",
            "format": "text"
          },
          "uuid": "1007c2fc-c069-491a-af92-685aba5f7f12"
        }
      ],
      "text": "panorama_user_group_xml",
      "tooltip": "xml structure indicating which users are members of the group",
      "type_id": 11,
      "uuid": "4c33528f-e008-4d22-9787-28f864c7456e",
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
      "export_key": "__function/panorama_user_group_xpath",
      "hide_notification": false,
      "id": 4685,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_user_group_xpath",
      "operation_perms": {},
      "operations": [],
      "placeholder": "/config/shared/local-user-database/user-group/entry[@name=\u0027Blocked_Users\u0027]",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_user_group_xpath",
      "tooltip": "xpath to the user group you want to use",
      "type_id": 11,
      "uuid": "799cc50b-a9b9-445f-8037-efd936b3cfee",
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
      "created_date": 1698842158943,
      "description": {
        "content": "Creates a new address object in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Create Address",
      "export_key": "panorama_create_address",
      "id": 59,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159011,
      "name": "panorama_create_address",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "8450551a-7da1-48b1-929f-798d4ef923ee",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c9f1bf5e-1c78-440a-bbe2-a373610200cf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb0e735b-6a43-461a-87a2-893edc92d24f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a6a5a64c-8040-4d70-9213-96450e05f87e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "created_date": 1698842159042,
      "description": {
        "content": "Edits an address group in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Edit Address Group",
      "export_key": "panorama_edit_address_group",
      "id": 60,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159111,
      "name": "panorama_edit_address_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c8336bd1-1a63-4662-9b04-eb74e9de7510",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c9f1bf5e-1c78-440a-bbe2-a373610200cf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb0e735b-6a43-461a-87a2-893edc92d24f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a6a5a64c-8040-4d70-9213-96450e05f87e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "created_date": 1698842159141,
      "description": {
        "content": "Edits users in a group in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Edit Users in a Group",
      "export_key": "panorama_edit_users_in_a_group",
      "id": 61,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159212,
      "name": "panorama_edit_users_in_a_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "e89ee2fa-3983-417e-9e69-f8a5ac9961cd",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "799cc50b-a9b9-445f-8037-efd936b3cfee",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4c33528f-e008-4d22-9787-28f864c7456e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "created_date": 1698842159241,
      "description": {
        "content": "List address groups in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Address Groups",
      "export_key": "panorama_get_address_groups",
      "id": 62,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159309,
      "name": "panorama_get_address_groups",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "4b233153-426e-456d-83cd-c133c6e05429",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c9f1bf5e-1c78-440a-bbe2-a373610200cf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb0e735b-6a43-461a-87a2-893edc92d24f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "created_date": 1698842159338,
      "description": {
        "content": "List addresses in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Addresses",
      "export_key": "panorama_get_addresses",
      "id": 63,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159408,
      "name": "panorama_get_addresses",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "50a9c249-ffaa-4280-92ff-4d5c9eca94cc",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c9f1bf5e-1c78-440a-bbe2-a373610200cf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
      "created_date": 1698842159439,
      "description": {
        "content": "Lists users part of a group in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Users in a Group",
      "export_key": "panorama_get_users_in_a_group",
      "id": 64,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842159510,
      "name": "panorama_get_users_in_a_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "85a6dc33-8f88-4bb5-9e21-3daa253d4a6c",
      "version": 1,
      "view_items": [
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "799cc50b-a9b9-445f-8037-efd936b3cfee",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
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
  "id": 9,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1698842245250,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1698842245250,
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
      "export_key": "palo_alto_panorama",
      "name": "Palo Alto Panorama",
      "programmatic_name": "palo_alto_panorama",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "1765df5c-37a7-4cd9-94ec-baa68d673329"
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
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\" isExecutable=\"true\" name=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_17ese3i\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1sl7qel\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_17ese3i\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ktna8q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1sl7qel\u003c/incoming\u003e\u003coutgoing\u003eFlow_0mbgvwc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_17ese3i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1sl7qel\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_1canimf\" id=\"ConditionPoint_3\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0mbgvwc\u003c/incoming\u003e\u003coutgoing\u003eFlow_1canimf\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0e8wgg1\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0mbgvwc\" sourceRef=\"ServiceTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Panorama Create Address\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8450551a-7da1-48b1-929f-798d4ef923ee\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = artifact.value\\n\\nbody = \u0027\u0027\u0027{{\\n\\\"entry\\\": {{\\n  \\\"@name\\\": \\\"{}\\\",\\n  \\\"description\\\": \\\"{}\\\",\\n  \\\"fqdn\\\": \\\"{}\\\"\\n}}\\n}}\u0027\u0027\u0027.format(artifact.value, artifact.value, artifact.value)\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_address_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1canimf\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hunjc9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"def list_to_json_str(l):\\n  string_list = \\\"[\\\"\\n  for item in l:\\n    string_list = string_list + \u0027\\\"\u0027 + item + \u0027\\\"\u0027\\n    if item != l[-1]:\\n      string_list = string_list + \\\", \\\"\\n  return string_list + \\\"]\\\"\\n\\ninputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\n\\ndns_name = \\\"\\\"\\ngroup = playbook.functions.results.groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])[0]\\n\\n# If new address was created\\nif playbook.functions.results.create_address_results:\\n  dns_name = artifact.value\\n# Else find it in the list of addresses\\nelse:\\n  addresses = playbook.functions.results.addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\")\\n  for address in addresses:\\n    if address.get(\\\"fqdn\\\") == artifact.value:\\n      dns_name = address.get(\\\"@name\\\")\\n      break\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nif group.get(\\\"static\\\", {}).get(\\\"member\\\"):\\n  member_list = group.get(\\\"static\\\", {}).get(\\\"member\\\", [])\\nelse:\\n  member_list = []\\nif dns_name not in member_list:\\n  member_list.append(dns_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\nbody = \u0027\u0027\u0027{{\\n  \\\"entry\\\": {{\\n    \\\"@name\\\": \\\"{}\\\",\\n    \\\"description\\\": \\\"{}\\\",\\n    \\\"static\\\": {{\\n      \\\"member\\\": {}\\n    }}\\n  }}\\n}}\u0027\u0027\u0027.format(group_name, des, list_to_json_str(member_list))\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_group_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0fot35v\u003c/incoming\u003e\u003coutgoing\u003eFlow_02q0k44\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_7\" name=\"Block DNS Name post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a8431d31-1223-4d29-bd15-193218de4827\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_02q0k44\u003c/incoming\u003e\u003coutgoing\u003eFlow_1djmatv\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_02q0k44\" sourceRef=\"ServiceTask_6\" targetRef=\"ScriptTask_7\"/\u003e\u003cendEvent id=\"EndPoint_8\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1djmatv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1djmatv\" sourceRef=\"ScriptTask_7\" targetRef=\"EndPoint_8\"/\u003e\u003cexclusiveGateway default=\"Flow_0xgjir5\" id=\"ConditionPoint_9\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1hunjc9\u003c/incoming\u003e\u003cincoming\u003eFlow_0e8wgg1\u003c/incoming\u003e\u003coutgoing\u003eFlow_02irm2s\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0xgjir5\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_1hunjc9\" sourceRef=\"ServiceTask_4\" targetRef=\"ConditionPoint_9\"/\u003e\u003cparallelGateway id=\"CollectionPoint_10\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_1ktna8q\u003c/incoming\u003e\u003cincoming\u003eFlow_02irm2s\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fot35v\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_1ktna8q\" sourceRef=\"ServiceTask_1\" targetRef=\"CollectionPoint_10\"/\u003e\u003csequenceFlow id=\"Flow_0fot35v\" sourceRef=\"CollectionPoint_10\" targetRef=\"ServiceTask_6\"/\u003e\u003cendEvent id=\"EndPoint_11\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0xgjir5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_02irm2s\" name=\"If finished running\" sourceRef=\"ConditionPoint_9\" targetRef=\"CollectionPoint_10\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"If finished running\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\nif playbook.functions.results.addresses_results:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0xgjir5\" name=\"Else\" sourceRef=\"ConditionPoint_9\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_0e8wgg1\" name=\"address to block is present\" sourceRef=\"ConditionPoint_3\" targetRef=\"ConditionPoint_9\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"address to block is present\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.addresses_results\\n\\ncreated_addresses = []\\nfor address in results.get(\\\"content\\\", {}).get(\\\"result\\\").get(\\\"entry\\\"):\\n  if \\\"ip-netmask\\\" in address:\\n    created_addresses.append(address.get(\\\"ip-netmask\\\"))\\n  if \\\"fqdn\\\" in address:\\n    created_addresses.append(address.get(\\\"fqdn\\\"))\\n\\nif artifact.value in created_addresses:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1canimf\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xgjir5\" id=\"Flow_0xgjir5_di\"\u003e\u003comgdi:waypoint x=\"1592\" y=\"780\"/\u003e\u003comgdi:waypoint x=\"1724\" y=\"780\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1647\" y=\"762\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02irm2s\" id=\"Flow_02irm2s_di\"\u003e\u003comgdi:waypoint x=\"1470\" y=\"806\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"1358\" y=\"870\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1415\" y=\"833\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1canimf\" id=\"Flow_1canimf_di\"\u003e\u003comgdi:waypoint x=\"1550\" y=\"546\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"587\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"587\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"628\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1558\" y=\"593\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0e8wgg1\" id=\"Flow_0e8wgg1_di\"\u003e\u003comgdi:waypoint x=\"1400\" y=\"546\"/\u003e\u003comgdi:waypoint x=\"1400\" y=\"754\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"83\" x=\"1358\" y=\"646\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fot35v\" id=\"Flow_0fot35v_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"896\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"948\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ktna8q\" id=\"Flow_1ktna8q_di\"\u003e\u003comgdi:waypoint x=\"1110\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"1221\" y=\"870\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hunjc9\" id=\"Flow_1hunjc9_di\"\u003e\u003comgdi:waypoint x=\"1590\" y=\"712\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"733\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"733\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"754\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1djmatv\" id=\"Flow_1djmatv_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"1142\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"1174\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02q0k44\" id=\"Flow_02q0k44_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"1032\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"1058\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0mbgvwc\" id=\"Flow_0mbgvwc_di\"\u003e\u003comgdi:waypoint x=\"1470\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"494\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sl7qel\" id=\"Flow_1sl7qel_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17ese3i\" id=\"Flow_17ese3i_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1199\" y=\"164\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1012\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1372\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1348\" y=\"494\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1492\" y=\"628\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1192\" y=\"948\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_7\" id=\"ScriptTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1192\" y=\"1058\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_8\" id=\"EndPoint_8_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1224\" y=\"1174\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_9\" id=\"ConditionPoint_9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1348\" y=\"754\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_10\" id=\"CollectionPoint_10_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1221\" y=\"844\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_11\" id=\"EndPoint_11_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1724\" y=\"754\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842159933,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
      "description": {
        "content": "Given a DNS Name artifact, adds the DNS Name to the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Block DNS Name (PB)",
      "export_key": "example_panorama_block_dns_name",
      "field_type_handle": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Block DNS Name (PB)",
        "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85/panorama_label",
            "hide_notification": false,
            "id": 4686,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1036,
            "uuid": "1d9faeac-0b24-4bfd-a5c7-f9eaf74b9858",
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
        "type_name": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
        "uuid": "a62e4b0b-dc82-4316-85a7-7bb109ca1b67"
      },
      "has_logical_errors": false,
      "id": 31,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842160645,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842160071,
          "description": "",
          "enabled": false,
          "export_key": "Block DNS Name post-process",
          "id": 44,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842160096,
          "name": "Block DNS Name post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_dns_name",
          "programmatic_name": "example_panorama_block_dns_name_block_dns_name_post_process",
          "script_text": "results = playbook.functions.results.edit_group_results\nif results.get(\"success\"):\n  incident.addNote(\"DNS name: {} was blocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "a8431d31-1223-4d29-bd15-193218de4827"
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
              "value": "DNS Name"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "1d9faeac-0b24-4bfd-a5c7-f9eaf74b9858",
            "element": "field_uuid",
            "field_type": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_block_dns_name",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_20761e90-81df-4c9a-a13e-872c6c5fed85",
        "id": 31,
        "name": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
        "type": "playbook",
        "uuid": "24cc2e03-b8f9-4a37-be57-f63bb2d4f247"
      },
      "tags": [],
      "type": "default",
      "uuid": "20761e90-81df-4c9a-a13e-872c6c5fed85",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\" isExecutable=\"true\" name=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1ioa0ju\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1umtp27\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cexclusiveGateway default=\"Flow_0uq42j3\" id=\"ConditionPoint_4\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1xq4igl\u003c/incoming\u003e\u003coutgoing\u003eFlow_0uq42j3\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0ajrv54\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cparallelGateway id=\"CollectionPoint_5\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_1bm214o\u003c/incoming\u003e\u003cincoming\u003eFlow_0bbxhdj\u003c/incoming\u003e\u003coutgoing\u003eFlow_1bopayq\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ioa0ju\u003c/incoming\u003e\u003coutgoing\u003eFlow_1xq4igl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1ioa0ju\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_6\"/\u003e\u003csequenceFlow id=\"Flow_1xq4igl\" sourceRef=\"ServiceTask_6\" targetRef=\"ConditionPoint_4\"/\u003e\u003cserviceTask id=\"ServiceTask_7\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1umtp27\u003c/incoming\u003e\u003coutgoing\u003eFlow_1bm214o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1umtp27\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_7\"/\u003e\u003csequenceFlow id=\"Flow_1bm214o\" sourceRef=\"ServiceTask_7\" targetRef=\"CollectionPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_8\" name=\"Panorama Create Address\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8450551a-7da1-48b1-929f-798d4ef923ee\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = artifact.value\\n\\nbody = \u0027\u0027\u0027{{\\n  \\\"entry\\\": {{\\n    \\\"@name\\\": \\\"{}\\\",\\n    \\\"description\\\": \\\"{}\\\",\\n    \\\"ip-netmask\\\": \\\"{}\\\"\\n  }}\\n}}\u0027\u0027\u0027.format(artifact.value, artifact.value, artifact.value)\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_address_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0uq42j3\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ik3izc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cexclusiveGateway default=\"Flow_1nowzes\" id=\"ConditionPoint_9\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0ajrv54\u003c/incoming\u003e\u003cincoming\u003eFlow_0ik3izc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0bbxhdj\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1nowzes\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0ik3izc\" sourceRef=\"ServiceTask_8\" targetRef=\"ConditionPoint_9\"/\u003e\u003cendEvent id=\"EndPoint_10\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1nowzes\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_11\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"def list_to_json_str(l):\\n  string_list = \\\"[\\\"\\n  for item in l:\\n    string_list = string_list + \u0027\\\"\u0027 + item + \u0027\\\"\u0027\\n    if item != l[-1]:\\n      string_list = string_list + \\\", \\\"\\n  return string_list + \\\"]\\\"\\n\\ninputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\n\\nip_name = \\\"\\\"\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])[0]\\n\\n# If new address was created\\nif playbook.functions.results.create_address_results:\\n  ip_name = artifact.value\\n# Else find it in the list of addresses\\nelse:\\n  addresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\")\\n  for address in addresses:\\n    if address.get(\\\"ip-netmask\\\") == artifact.value:\\n      ip_name = address.get(\\\"@name\\\")\\n      break\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\", [])\\nif ip_name not in member_list:\\n  member_list.append(ip_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\nbody = \u0027\u0027\u0027{{\\n  \\\"entry\\\": {{\\n    \\\"@name\\\": \\\"{}\\\",\\n    \\\"description\\\": \\\"{}\\\",\\n    \\\"static\\\": {{\\n      \\\"member\\\": {}\\n    }}\\n  }}\\n}}\u0027\u0027\u0027.format(group_name, des, list_to_json_str(member_list))\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1bopayq\u003c/incoming\u003e\u003coutgoing\u003eFlow_0s4ueot\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1bopayq\" sourceRef=\"CollectionPoint_5\" targetRef=\"ServiceTask_11\"/\u003e\u003cscriptTask id=\"ScriptTask_12\" name=\"Block IP post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"b12cfc5c-8649-4a55-bb00-7535c14fe4f7\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0s4ueot\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ouz7c4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0s4ueot\" sourceRef=\"ServiceTask_11\" targetRef=\"ScriptTask_12\"/\u003e\u003cendEvent id=\"EndPoint_13\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1ouz7c4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1ouz7c4\" sourceRef=\"ScriptTask_12\" targetRef=\"EndPoint_13\"/\u003e\u003csequenceFlow id=\"Flow_0bbxhdj\" name=\"If finished running\" sourceRef=\"ConditionPoint_9\" targetRef=\"CollectionPoint_5\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"If finished running\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"if playbook.functions.results.get_addresses_results:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1nowzes\" name=\"Else\" sourceRef=\"ConditionPoint_9\" targetRef=\"EndPoint_10\"/\u003e\u003csequenceFlow id=\"Flow_0ajrv54\" name=\"Address to block is present\" sourceRef=\"ConditionPoint_4\" targetRef=\"ConditionPoint_9\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Address to block is present\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.get_addresses_results\\ncreated_addresses = []\\nfor address in results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\"):\\n  if \\\"ip-netmask\\\" in address:\\n    created_addresses.append(address.get(\\\"ip-netmask\\\"))\\n  if \\\"fqdn\\\" in address:\\n    created_addresses.append(address.get(\\\"fqdn\\\"))\\n\\nif artifact.value in created_addresses:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0uq42j3\" name=\"Else\" sourceRef=\"ConditionPoint_4\" targetRef=\"ServiceTask_8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nowzes\" id=\"Flow_1nowzes_di\"\u003e\u003comgdi:waypoint x=\"2052\" y=\"620\"/\u003e\u003comgdi:waypoint x=\"2154\" y=\"620\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"2092\" y=\"602\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bbxhdj\" id=\"Flow_0bbxhdj_di\"\u003e\u003comgdi:waypoint x=\"1930\" y=\"646\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1808\" y=\"710\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1865\" y=\"675\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0uq42j3\" id=\"Flow_0uq42j3_di\"\u003e\u003comgdi:waypoint x=\"2052\" y=\"390\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"390\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"458\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"2080\" y=\"403\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ajrv54\" id=\"Flow_0ajrv54_di\"\u003e\u003comgdi:waypoint x=\"1850\" y=\"416\"/\u003e\u003comgdi:waypoint x=\"1850\" y=\"594\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"84\" x=\"1808\" y=\"486\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ouz7c4\" id=\"Flow_1ouz7c4_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"992\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"1034\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0s4ueot\" id=\"Flow_0s4ueot_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"872\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"908\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bopayq\" id=\"Flow_1bopayq_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"736\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"788\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ik3izc\" id=\"Flow_0ik3izc_di\"\u003e\u003comgdi:waypoint x=\"2130\" y=\"542\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"568\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"568\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"594\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bm214o\" id=\"Flow_1bm214o_di\"\u003e\u003comgdi:waypoint x=\"1550\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1671\" y=\"710\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1umtp27\" id=\"Flow_1umtp27_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1xq4igl\" id=\"Flow_1xq4igl_di\"\u003e\u003comgdi:waypoint x=\"1930\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"364\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ioa0ju\" id=\"Flow_1ioa0ju_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1649\" y=\"134\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_4\" id=\"ConditionPoint_4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1808\" y=\"364\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_5\" id=\"CollectionPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1671\" y=\"684\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1832\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_7\" id=\"ServiceTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1452\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_8\" id=\"ServiceTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"2032\" y=\"458\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_9\" id=\"ConditionPoint_9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1808\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_10\" id=\"EndPoint_10_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"2154\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11\" id=\"ServiceTask_11_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1642\" y=\"788\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_12\" id=\"ScriptTask_12_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1642.3\" y=\"908\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_13\" id=\"EndPoint_13_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1674\" y=\"1034\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842160619,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
      "description": {
        "content": "Given an IP Address artifact, adds the IP Address to the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Block IP Address (PB)",
      "export_key": "example_panorama_block_ip_address",
      "field_type_handle": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Block IP Address (PB)",
        "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1/panorama_label",
            "hide_notification": false,
            "id": 4687,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1037,
            "uuid": "5f1eea39-f8cf-4381-9a3e-810492e82296",
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
        "type_name": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
        "uuid": "b9cf6fa5-0647-4762-800f-a27d13bf9a7e"
      },
      "has_logical_errors": false,
      "id": 32,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842161281,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842160770,
          "description": "",
          "enabled": false,
          "export_key": "Block IP post-process",
          "id": 45,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842160793,
          "name": "Block IP post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_ip_address",
          "programmatic_name": "example_panorama_block_ip_address_block_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_groups_results\nif results.get(\"success\"):\n  incident.addNote(\"IP Address: {} was blocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "b12cfc5c-8649-4a55-bb00-7535c14fe4f7"
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
        "view_items": [
          {
            "content": "5f1eea39-f8cf-4381-9a3e-810492e82296",
            "element": "field_uuid",
            "field_type": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_block_ip_address",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_4f6ee7aa-22cc-4d4b-9696-dd1cac5e4de1",
        "id": 32,
        "name": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
        "type": "playbook",
        "uuid": "f5fce47d-a28f-4a71-8a5c-c08f3d0cb54d"
      },
      "tags": [],
      "type": "default",
      "uuid": "4f6ee7aa-22cc-4d4b-9696-dd1cac5e4de1",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\" isExecutable=\"true\" name=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qt9mg8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"85a6dc33-8f88-4bb5-9e21-3daa253d4a6c\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# Set this to the xpath of the group you are interested in\\ninputs.panorama_user_group_xpath = \\\"/config/shared/local-user-database/user-group/entry[@name=\u0027Blocked_Users\u0027]\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\\ninputs.panorama_location = \\\"vsys\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qt9mg8\u003c/incoming\u003e\u003coutgoing\u003eFlow_1lgsf39\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Edit Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e89ee2fa-3983-417e-9e69-f8a5ac9961cd\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"4c33528f-e008-4d22-9787-28f864c7456e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\n# Set this to the name of the user group you wish to add a user to\\ngroup_name = \\\"Blocked_Users\\\"\\n\\n# Set this to the xpath of the group you are interested in\\ninputs.panorama_user_group_xpath = \\\"/config/shared/local-user-database/user-group/entry[@name=\u0027{}\u0027]\\\".format(group_name)\\n\\nusers_list = playbook.functions.results.get_users_results.get(\\\"content\\\", {}).get(\\\"user_list\\\", [])\\n\\nblocked_users = []\\n\\nif len(users_list) == 1:\\n  # only one user was returned\\n  blocked_users.append(users_list[0])\\nelif len(users_list) \u0026gt; 1:\\n  # multiple users returned\\n  for user in users_list:\\n    blocked_users.append(user.get(\\\"#text\\\"))\\n\\n# Add the user to the blocked list if they are not already there\\nif artifact.value not in blocked_users:\\n  blocked_users.append(artifact.value)\\n\\n# Build xml which the function will send to Panorama\\npanorama_xml = u\u0027\u0027\u0027\\n\u0026lt;entry name=\\\"{}\\\"\u0026gt;\\n    \u0026lt;user\u0026gt;\u0027\u0027\u0027.format(str(group_name))\\n\\n# Add member nodes with the username to the xml string\\nfor user in blocked_users:\\n  panorama_xml += u\\\"\\\\n      \u0026lt;member\u0026gt;\\\" + user + \\\"\u0026lt;/member\u0026gt;\\\"\\n\\n# Add the ending of the xml to the string\\nxml_ending = \\\"\\\"\\\"\\n    \u0026lt;/user\u0026gt;\\n\u0026lt;/entry\u0026gt;\\n\\\"\\\"\\\"\\npanorama_xml += xml_ending\\n\\ninputs.panorama_user_group_xml = panorama_xml\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1lgsf39\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ukwy06\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"block user post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"05f9f363-4dd6-41ad-b7fb-8d12286700b4\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ukwy06\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wfegvd\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0qt9mg8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1lgsf39\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1ukwy06\" sourceRef=\"ServiceTask_2\" targetRef=\"ScriptTask_3\"/\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0wfegvd\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0wfegvd\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wfegvd\" id=\"Flow_0wfegvd_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"572\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"634\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ukwy06\" id=\"Flow_1ukwy06_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"488\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1lgsf39\" id=\"Flow_1lgsf39_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qt9mg8\" id=\"Flow_0qt9mg8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"488\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"634\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842161255,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
      "description": {
        "content": "Given a User Account artifact, adds the user to the \"Blocked_Users\" group in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Block User (PB)",
      "export_key": "example_panorama_block_user",
      "field_type_handle": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Block User (PB)",
        "export_key": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f/panorama_label",
            "hide_notification": false,
            "id": 4688,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1038,
            "uuid": "c5778bf4-13a6-4037-94de-96f47974cbef",
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
        "type_name": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
        "uuid": "a5a5f727-9ae5-4905-b91a-1c91076d9502"
      },
      "has_logical_errors": false,
      "id": 33,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842161911,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842161400,
          "description": "",
          "enabled": false,
          "export_key": "block user post-process",
          "id": 46,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842161423,
          "name": "block user post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_user",
          "programmatic_name": "example_panorama_block_user_block_user_post_process",
          "script_text": "results = playbook.functions.results.edit_users_results\nif results.get(\"success\"):\n  incident.addNote(\"User account: {} was blocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "05f9f363-4dd6-41ad-b7fb-8d12286700b4"
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
              "value": "User Account"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "c5778bf4-13a6-4037-94de-96f47974cbef",
            "element": "field_uuid",
            "field_type": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_block_user",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7bc7deb6-d0e0-434b-b25d-aaed1532ea9f",
        "id": 33,
        "name": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
        "type": "playbook",
        "uuid": "f303cb58-f571-4054-8a23-b0a43975b404"
      },
      "tags": [],
      "type": "default",
      "uuid": "7bc7deb6-d0e0-434b-b25d-aaed1532ea9f",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\" isExecutable=\"true\" name=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0j8llco\u003c/outgoing\u003e\u003coutgoing\u003eFlow_18x1t2k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0j8llco\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kjeon9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_18x1t2k\u003c/incoming\u003e\u003coutgoing\u003eFlow_0nizk7z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0j8llco\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_18x1t2k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cparallelGateway id=\"CollectionPoint_3\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_0kjeon9\u003c/incoming\u003e\u003cincoming\u003eFlow_0nizk7z\u003c/incoming\u003e\u003coutgoing\u003eFlow_0el5yi5\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_0kjeon9\" sourceRef=\"ServiceTask_1\" targetRef=\"CollectionPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_0nizk7z\" sourceRef=\"ServiceTask_2\" targetRef=\"CollectionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"def list_to_json_str(l):\\n  string_list = \\\"[\\\"\\n  for item in l:\\n    string_list = string_list + \u0027\\\"\u0027 + item + \u0027\\\"\u0027\\n    if item != l[-1]:\\n      string_list = string_list + \\\", \\\"\\n  return string_list + \\\"]\\\"\\n\\ninputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\n\\ndns_name = \\\"\\\"\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])[0]\\naddresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\nfor address in addresses:\\n  if address.get(\\\"fqdn\\\") == artifact.value:\\n    dns_name = address.get(\\\"@name\\\")\\n    break\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\")\\n\\n# Remove IP address from list\\nmember_list.remove(dns_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\nbody = \u0027\u0027\u0027{{\\n  \\\"entry\\\": {{\\n    \\\"@name\\\": \\\"{}\\\",\\n    \\\"description\\\": \\\"{}\\\",\\n    \\\"static\\\": {{\\n      \\\"member\\\": {}\\n    }}\\n  }}\\n}}\u0027\u0027\u0027.format(group_name, des, list_to_json_str(member_list))\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0el5yi5\u003c/incoming\u003e\u003coutgoing\u003eFlow_1u36swy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0el5yi5\" sourceRef=\"CollectionPoint_3\" targetRef=\"ServiceTask_4\"/\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"unblock dns post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f627d5f0-ce59-44a1-891c-56dc2ff1b127\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1u36swy\u003c/incoming\u003e\u003coutgoing\u003eFlow_020ypio\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1u36swy\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_5\"/\u003e\u003cendEvent id=\"EndPoint_6\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_020ypio\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_020ypio\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_020ypio\" id=\"Flow_020ypio_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"612\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"674\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1u36swy\" id=\"Flow_1u36swy_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"528\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0el5yi5\" id=\"Flow_0el5yi5_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"356\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0nizk7z\" id=\"Flow_0nizk7z_di\"\u003e\u003comgdi:waypoint x=\"870\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"789\" y=\"330\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kjeon9\" id=\"Flow_0kjeon9_di\"\u003e\u003comgdi:waypoint x=\"570\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"652\" y=\"330\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18x1t2k\" id=\"Flow_18x1t2k_di\"\u003e\u003comgdi:waypoint x=\"811\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0j8llco\" id=\"Flow_0j8llco_di\"\u003e\u003comgdi:waypoint x=\"630\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"472\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"772\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_3\" id=\"CollectionPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"652\" y=\"304\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"528\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_6\" id=\"EndPoint_6_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"674\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842161883,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
      "description": {
        "content": "Given a DNS Name artifact, removes the DNS Name from the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Unblock DNS Name (PB)",
      "export_key": "example_panorama_unblock_dns_name",
      "field_type_handle": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Unblock DNS Name (PB)",
        "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6/panorama_label",
            "hide_notification": false,
            "id": 4689,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1039,
            "uuid": "b12bd4dd-0be0-478e-bae4-7d26c94dd46c",
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
        "type_name": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
        "uuid": "9f022c28-d9aa-40b0-b922-0d421ad73e42"
      },
      "has_logical_errors": false,
      "id": 34,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842162551,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842162043,
          "description": "",
          "enabled": false,
          "export_key": "unblock dns post-process",
          "id": 47,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842162068,
          "name": "unblock dns post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_dns_name",
          "programmatic_name": "example_panorama_unblock_dns_name_unblock_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_addresses_results\nif results.get(\"success\"):\n  incident.addNote(\"DNS name: {} was unblocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "f627d5f0-ce59-44a1-891c-56dc2ff1b127"
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
              "value": "DNS Name"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "b12bd4dd-0be0-478e-bae4-7d26c94dd46c",
            "element": "field_uuid",
            "field_type": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_unblock_dns_name",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_e891e702-52bf-437a-bc61-af36c715b5e6",
        "id": 34,
        "name": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
        "type": "playbook",
        "uuid": "bfa7e49f-9da4-46d2-8883-5f66792b0418"
      },
      "tags": [],
      "type": "default",
      "uuid": "e891e702-52bf-437a-bc61-af36c715b5e6",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\" isExecutable=\"true\" name=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0xjlnoc\u003c/outgoing\u003e\u003coutgoing\u003eFlow_02808cp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"def list_to_json_str(l):\\n  string_list = \\\"[\\\"\\n  for item in l:\\n    string_list = string_list + \u0027\\\"\u0027 + item + \u0027\\\"\u0027\\n    if item != l[-1]:\\n      string_list = string_list + \\\", \\\"\\n  return string_list + \\\"]\\\"\\n\\ninputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\n\\nip_address_name = artifact.value\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])[0]\\naddresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\")\\n\\n# Remove IP address from list if it\u0027s present\\nif ip_address_name in member_list:\\n  member_list.remove(ip_address_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\nbody = \u0027\u0027\u0027{{\\n  \\\"entry\\\": {{\\n    \\\"@name\\\": \\\"{}\\\",\\n    \\\"description\\\": \\\"{}\\\",\\n    \\\"static\\\": {{\\n      \\\"member\\\": {}\\n    }}\\n  }}\\n}}\u0027\u0027\u0027.format(group_name, des, list_to_json_str(member_list))\\n\\ninputs.panorama_request_body = body\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_082glnv\u003c/incoming\u003e\u003coutgoing\u003eFlow_0lvnfj8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_02808cp\u003c/incoming\u003e\u003coutgoing\u003eFlow_08eabn0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\ninputs.panorama_vsys = \\\"vsys1\\\"\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0xjlnoc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ulvawt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cparallelGateway id=\"CollectionPoint_4\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_0ulvawt\u003c/incoming\u003e\u003cincoming\u003eFlow_08eabn0\u003c/incoming\u003e\u003coutgoing\u003eFlow_082glnv\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_0ulvawt\" sourceRef=\"ServiceTask_3\" targetRef=\"CollectionPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_08eabn0\" sourceRef=\"ServiceTask_2\" targetRef=\"CollectionPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_082glnv\" sourceRef=\"CollectionPoint_4\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0xjlnoc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_3\"/\u003e\u003csequenceFlow id=\"Flow_02808cp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"unblock ip post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8b544819-af40-4a0e-a324-631279825f49\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0lvnfj8\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jz8otw\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0lvnfj8\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_5\"/\u003e\u003cendEvent id=\"EndPoint_6\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jz8otw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jz8otw\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jz8otw\" id=\"Flow_0jz8otw_di\"\u003e\u003comgdi:waypoint x=\"1340\" y=\"782\"/\u003e\u003comgdi:waypoint x=\"1340\" y=\"824\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0lvnfj8\" id=\"Flow_0lvnfj8_di\"\u003e\u003comgdi:waypoint x=\"1340\" y=\"652\"/\u003e\u003comgdi:waypoint x=\"1340\" y=\"698\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02808cp\" id=\"Flow_02808cp_di\"\u003e\u003comgdi:waypoint x=\"1430\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"268\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xjlnoc\" id=\"Flow_0xjlnoc_di\"\u003e\u003comgdi:waypoint x=\"1249\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"268\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_082glnv\" id=\"Flow_082glnv_di\"\u003e\u003comgdi:waypoint x=\"1340\" y=\"486\"/\u003e\u003comgdi:waypoint x=\"1340\" y=\"568\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08eabn0\" id=\"Flow_08eabn0_di\"\u003e\u003comgdi:waypoint x=\"1490\" y=\"352\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"460\"/\u003e\u003comgdi:waypoint x=\"1408\" y=\"460\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ulvawt\" id=\"Flow_0ulvawt_di\"\u003e\u003comgdi:waypoint x=\"1190\" y=\"352\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"460\"/\u003e\u003comgdi:waypoint x=\"1271\" y=\"460\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1249\" y=\"154\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1242\" y=\"568\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1392\" y=\"268\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1092\" y=\"268\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_4\" id=\"CollectionPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1271\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1242\" y=\"698\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_6\" id=\"EndPoint_6_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1274\" y=\"824\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842162525,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
      "description": {
        "content": "Given an IP Address artifact, removes the IP Address from the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Unblock IP Address (PB)",
      "export_key": "example_panorama_unblock_ip_address",
      "field_type_handle": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Unblock IP Address (PB)",
        "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c/panorama_label",
            "hide_notification": false,
            "id": 4690,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1040,
            "uuid": "1c91feb8-07f0-415d-8183-c39a547c27c3",
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
        "type_name": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
        "uuid": "3914f6dc-661d-4ed6-9733-0309bb39c5c6"
      },
      "has_logical_errors": false,
      "id": 35,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842163171,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842162680,
          "description": "",
          "enabled": false,
          "export_key": "unblock ip post-process",
          "id": 48,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842162704,
          "name": "unblock ip post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_ip_address",
          "programmatic_name": "example_panorama_unblock_ip_address_unblock_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_addresses_results\nif results.get(\"success\"):\n  incident.addNote(\"IP Address: {} was unblocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "8b544819-af40-4a0e-a324-631279825f49"
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
        "view_items": [
          {
            "content": "1c91feb8-07f0-415d-8183-c39a547c27c3",
            "element": "field_uuid",
            "field_type": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_unblock_ip_address",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_14264b30-9bed-4985-b6ce-cd34dd996b9c",
        "id": 35,
        "name": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
        "type": "playbook",
        "uuid": "9e587e05-f0b2-4c3b-a0c2-b82a23821420"
      },
      "tags": [],
      "type": "default",
      "uuid": "14264b30-9bed-4985-b6ce-cd34dd996b9c",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\" isExecutable=\"true\" name=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1g1nlkh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"85a6dc33-8f88-4bb5-9e21-3daa253d4a6c\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# Set this to the xpath of the group you are interested in\\ninputs.panorama_user_group_xpath = \\\"/config/shared/local-user-database/user-group/entry[@name=\u0027Blocked_Users\u0027]\\\"\\ninputs.panorama_label = playbook.inputs.panorama_label\\ninputs.panorama_location = \\\"vsys\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1g1nlkh\u003c/incoming\u003e\u003coutgoing\u003eFlow_07lm4lf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Edit Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e89ee2fa-3983-417e-9e69-f8a5ac9961cd\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"4c33528f-e008-4d22-9787-28f864c7456e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"vsys\\\"\\n# Set this to the name of the user group you wish to add a user to\\ngroup_name = \\\"Blocked_Users\\\"\\n\\n# Set this to the xpath of the group you are interested in\\ninputs.panorama_user_group_xpath = u\\\"/config/shared/local-user-database/user-group/entry[@name=\u0027{}\u0027]\\\".format(group_name)\\n\\nusers_list = playbook.functions.results.get_users_results.get(\\\"content\\\", {}).get(\\\"user_list\\\")\\n\\nblocked_users = []\\n\\nif len(users_list) == 1:\\n  # only one user was returned\\n  blocked_users.append(users_list[0])\\nelif len(users_list) \u0026gt; 1:\\n  # multiple users returned\\n  for user in users_list:\\n    blocked_users.append(str(user.get(\\\"#text\\\")))\\n\\n# Remove the user from the blocked list if they are there\\nif artifact.value in blocked_users:\\n  blocked_users.remove(artifact.value)\\n\\npanorama_xml = \\\"\\\"\\n# Set xml to empty users if list is empty\\nif len(users_list) == 0:\\n  panorama_xml = u\u0027\u0026lt;entry name=\\\"{}\\\"/\u0026gt;\u0027.format(group_name)\\n\\n# Multiple members, build xml which the function will send to Panorama\\nelse:\\n  panorama_xml = u\u0027\u0027\u0027\\n  \u0026lt;entry name=\\\"{}\\\"\u0026gt;\\n      \u0026lt;user\u0026gt;\u0027\u0027\u0027.format(group_name)\\n\\n  # Add member nodes with the username to the xml string\\n  for user in blocked_users:\\n    panorama_xml += u\\\"\\\\n      \u0026lt;member\u0026gt;\\\" + user + \\\"\u0026lt;/member\u0026gt;\\\"\\n\\n  # Add the ending of the xml to the string\\n  xml_ending = u\\\"\\\"\\\"\\n      \u0026lt;/user\u0026gt;\\n  \u0026lt;/entry\u0026gt;\\n  \\\"\\\"\\\"\\n  panorama_xml += xml_ending\\n\\ninputs.panorama_user_group_xml = panorama_xml\\ninputs.panorama_label = playbook.inputs.panorama_label\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_07lm4lf\u003c/incoming\u003e\u003coutgoing\u003eFlow_1slq0wt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"unblock user post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"0faec4e9-f36a-4891-ae4d-c1d3be2da800\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1slq0wt\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kog3tg\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1slq0wt\" sourceRef=\"ServiceTask_2\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_1g1nlkh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_07lm4lf\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0kog3tg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0kog3tg\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kog3tg\" id=\"Flow_0kog3tg_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"612\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"674\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_07lm4lf\" id=\"Flow_07lm4lf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"378\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1g1nlkh\" id=\"Flow_1g1nlkh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1slq0wt\" id=\"Flow_1slq0wt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"462\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"528\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"378\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"528\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"674\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1698842163143,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
      "description": {
        "content": "Given a User Account artifact, removes the user from the \"Blocked_Users\" group in Panorama.",
        "format": "text"
      },
      "display_name": "Example: Panorama Unblock User (PB)",
      "export_key": "example_panorama_unblock_user",
      "field_type_handle": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Panorama Unblock User (PB)",
        "export_key": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
        "fields": {
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90/panorama_label",
            "hide_notification": false,
            "id": 4691,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_label",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "panorama_label",
            "tooltip": "Label given to the server to use",
            "type_id": 1041,
            "uuid": "1ed52467-249c-4ce0-bbba-d27a488e8abe",
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
        "type_name": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
        "uuid": "5c366a4e-01dc-4970-9f46-8417702e5fc0"
      },
      "has_logical_errors": false,
      "id": 36,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 35,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1698842163783,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1698842163294,
          "description": "",
          "enabled": false,
          "export_key": "unblock user post-process",
          "id": 49,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1698842163324,
          "name": "unblock user post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_user",
          "programmatic_name": "example_panorama_unblock_user_unblock_user_post_process",
          "script_text": "results = playbook.functions.results.edit_users_results\nif results.get(\"success\"):\n  incident.addNote(\"User account: {} was unblocked.\".format(artifact.value))",
          "tags": [],
          "uuid": "0faec4e9-f36a-4891-ae4d-c1d3be2da800"
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
              "value": "User Account"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "1ed52467-249c-4ce0-bbba-d27a488e8abe",
            "element": "field_uuid",
            "field_type": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_unblock_user",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_68dd2c77-47b7-479a-ae1e-f5cb0cebce90",
        "id": 36,
        "name": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
        "type": "playbook",
        "uuid": "e4b0058e-6552-4db2-b1a0-f30abdea151e"
      },
      "tags": [],
      "type": "default",
      "uuid": "68dd2c77-47b7-479a-ae1e-f5cb0cebce90",
      "version": 4
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 16,
    "major": 48,
    "minor": 2,
    "version": "48.2.16"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
