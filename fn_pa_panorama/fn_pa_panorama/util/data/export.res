{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1741278932805,
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
      "export_key": "__function/panorama_users_list",
      "hide_notification": false,
      "id": 5245,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_users_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_users_list",
      "tooltip": "List of panorama users",
      "type_id": 11,
      "uuid": "88fff54c-9d70-43bc-beb6-568e1ba504c6",
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
      "export_key": "__function/panorama_commit_without_default_template",
      "hide_notification": false,
      "id": 5246,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_commit_without_default_template",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_commit_without_default_template",
      "tooltip": "True - commit all without including default device/network template changes.",
      "type_id": 11,
      "uuid": "92c379c1-a974-4240-8a49-89944a3a02fc",
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
      "export_key": "__function/panorama_job_id",
      "hide_notification": false,
      "id": 5247,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_job_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_job_id",
      "tooltip": "The job ID to get the status of.",
      "type_id": 11,
      "uuid": "9edfccae-3371-4860-b913-2d8fc7a69585",
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
      "export_key": "__function/panorama_user_group_name",
      "hide_notification": false,
      "id": 5248,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_user_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_user_group_name",
      "tooltip": "Name of the user group",
      "type_id": 11,
      "uuid": "a195023e-ed73-436e-ab3f-675a539e538e",
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
      "export_key": "__function/panorama_request_body",
      "hide_notification": false,
      "id": 5249,
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
          "id": 1,
          "name": "Edit Address Group Body",
          "template": {
            "content": "{\n  \"entry\": {\n    \"@name\": \"string\",\n    \"description\": \"string\",\n    \"static\": {\n      \"member\": [\n        \"string\"\n      ]\n    },\n    \"dynamic\": {\n      \"filter\": \"string\"\n    },\n    \"tag\": {\n      \"member\": [\n        \"string\"\n      ]\n    }\n  }\n}",
            "format": "text"
          },
          "uuid": "87c12460-0355-40ee-8fef-302a9bf1e808"
        },
        {
          "id": 2,
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
      "id": 5250,
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
      "id": 5251,
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
      "id": 5252,
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
          "value": 2257
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vsys",
          "properties": null,
          "uuid": "4910f3d6-367d-4e6f-b6d3-f15ff394773e",
          "value": 2258
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "panorama-pushed",
          "properties": null,
          "uuid": "2ac1f5a8-1d28-4d41-b65d-a701f9ef471b",
          "value": 2259
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "device-group",
          "properties": null,
          "uuid": "54ebb86a-669b-4fba-9144-f9f06d7f0c52",
          "value": 2260
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
      "id": 5253,
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
      "export_key": "__function/panorama_device_group",
      "hide_notification": false,
      "id": 5254,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "panorama_device_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "panorama_device_group",
      "tooltip": "The name of the device-group when location type is \u0027device-group\u0027",
      "type_id": 11,
      "uuid": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
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
      "id": 5255,
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
          "id": 3,
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
      "id": 5256,
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
      "created_date": 1741027804112,
      "description": {
        "content": "Commit changes that have been made on the Panorama server",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Commit",
      "export_key": "panorama_commit",
      "id": 56,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027804112,
      "name": "panorama_commit",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "938412d2-1552-4d55-a8e0-234fc73f959b",
      "version": 0,
      "view_items": [
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e9aa03fe-166f-4ebc-b783-0bfa367a963b",
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
      "created_date": 1741027804406,
      "description": {
        "content": "Commit and push changes to panorama firewall",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Commit All",
      "export_key": "panorama_commit_all",
      "id": 57,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027804406,
      "name": "panorama_commit_all",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "3366b084-8a3d-4631-834d-9124a5e57614",
      "version": 0,
      "view_items": [
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "92c379c1-a974-4240-8a49-89944a3a02fc",
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
      "created_date": 1741027804713,
      "description": {
        "content": "Creates a new address object in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Create Address",
      "export_key": "panorama_create_address",
      "id": 58,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027804713,
      "name": "panorama_create_address",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "8450551a-7da1-48b1-929f-798d4ef923ee",
      "version": 0,
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
          "content": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
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
      "created_date": 1741027804997,
      "description": {
        "content": "Edits an address group in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Edit Address Group",
      "export_key": "panorama_edit_address_group",
      "id": 59,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027804997,
      "name": "panorama_edit_address_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c8336bd1-1a63-4662-9b04-eb74e9de7510",
      "version": 0,
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
          "content": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
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
      "created_date": 1741027805306,
      "description": {
        "content": "Edits users in a group in Panorama. This only works with Panorama and does not work with PanOS.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Edit Users in a Group",
      "export_key": "panorama_edit_users_in_a_group",
      "id": 60,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027805306,
      "name": "panorama_edit_users_in_a_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "e89ee2fa-3983-417e-9e69-f8a5ac9961cd",
      "version": 0,
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
        },
        {
          "content": "a195023e-ed73-436e-ab3f-675a539e538e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "88fff54c-9d70-43bc-beb6-568e1ba504c6",
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
      "created_date": 1741027805749,
      "description": {
        "content": "List address groups in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Address Groups",
      "export_key": "panorama_get_address_groups",
      "id": 61,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027805749,
      "name": "panorama_get_address_groups",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "4b233153-426e-456d-83cd-c133c6e05429",
      "version": 0,
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
          "content": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
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
      "created_date": 1741027806110,
      "description": {
        "content": "List addresses in Panorama.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Addresses",
      "export_key": "panorama_get_addresses",
      "id": 62,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027806110,
      "name": "panorama_get_addresses",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "50a9c249-ffaa-4280-92ff-4d5c9eca94cc",
      "version": 0,
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
          "content": "39f05d50-d87a-4a1b-a2ef-fbb3579e3af6",
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
      "created_date": 1741027806536,
      "description": {
        "content": "Get panorama job status from job ID.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Job Status",
      "export_key": "panorama_get_job_status",
      "id": 63,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027806536,
      "name": "panorama_get_job_status",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "1150149f-550c-4388-9f44-fd64b327197b",
      "version": 0,
      "view_items": [
        {
          "content": "d3a29851-1be8-4c24-ad15-34e247fdbf9d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9edfccae-3371-4860-b913-2d8fc7a69585",
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
      "created_date": 1741027806842,
      "description": {
        "content": "Lists users part of a group in Panorama. This only works with Panorama and does not work with PanOS.",
        "format": "text"
      },
      "destination_handle": "palo_alto_panorama",
      "display_name": "Panorama Get Users in a Group",
      "export_key": "panorama_get_users_in_a_group",
      "id": 64,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741027806842,
      "name": "panorama_get_users_in_a_group",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "85a6dc33-8f88-4bb5-9e21-3daa253d4a6c",
      "version": 0,
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
  "id": 17,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1741278930776,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1741278930776,
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
        "admin@example.com"
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
        "content_version": 20,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\" isExecutable=\"true\" name=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_17ese3i\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1sl7qel\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_17ese3i\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ktna8q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1sl7qel\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fj9g69\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_17ese3i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1sl7qel\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_1canimf\" id=\"ConditionPoint_3\" resilient:documentation=\"Check if address exists\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0fj9g69\u003c/incoming\u003e\u003coutgoing\u003eFlow_1canimf\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0e8wgg1\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Panorama Create Address\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8450551a-7da1-48b1-929f-798d4ef923ee\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = artifact.value\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": artifact.value,\\n    \\\"description\\\": artifact.value,\\n    \\\"fqdn\\\": artifact.value\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_address_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1canimf\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hunjc9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"from json import dumps\\n\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ndns_name = \\\"\\\"\\ngroup = playbook.functions.results.groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\nif group:\\n  group = group[0]\\n\\n# If new address was created\\nif playbook.functions.results.create_address_results:\\n  dns_name = artifact.value\\n# Else find it in the list of addresses\\nelse:\\n  addresses = playbook.functions.results.addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\")\\n  for address in addresses:\\n    if address.get(\\\"fqdn\\\") == artifact.value:\\n      dns_name = address.get(\\\"@name\\\")\\n      break\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nif group.get(\\\"static\\\", {}).get(\\\"member\\\"):\\n  member_list = group.get(\\\"static\\\", {}).get(\\\"member\\\", [])\\nelse:\\n  member_list = []\\nif dns_name not in member_list:\\n  member_list.append(dns_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\n# If using api version 9.0 or before uncomment below for the body\\n# body = {\\n#   \\\"entry\\\": {\\n#     \\\"@name\\\": group_name,\\n#     \\\"description\\\": des,\\n#     \\\"static\\\": {\\n#       \\\"member\\\": dumps(member_list)\\n#     }\\n#   }\\n# }\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": group_name,\\n    \\\"description\\\": des,\\n    \\\"static\\\": {\\n      \\\"member\\\": member_list\\n    }\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_group_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0fot35v\u003c/incoming\u003e\u003coutgoing\u003eFlow_1cask2u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_7\" name=\"Panorama Block DNS Name post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a8431d31-1223-4d29-bd15-193218de4827\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vmfh17\u003c/incoming\u003e\u003coutgoing\u003eFlow_1djmatv\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_8\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1djmatv\u003c/incoming\u003e\u003cincoming\u003eFlow_19ic6tk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1djmatv\" sourceRef=\"ScriptTask_7\" targetRef=\"EndPoint_8\"/\u003e\u003cexclusiveGateway default=\"Flow_0xgjir5\" id=\"ConditionPoint_9\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1hunjc9\u003c/incoming\u003e\u003cincoming\u003eFlow_0e8wgg1\u003c/incoming\u003e\u003coutgoing\u003eFlow_02irm2s\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0xgjir5\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_1hunjc9\" sourceRef=\"ServiceTask_4\" targetRef=\"ConditionPoint_9\"/\u003e\u003cparallelGateway id=\"CollectionPoint_10\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_1ktna8q\u003c/incoming\u003e\u003cincoming\u003eFlow_02irm2s\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fot35v\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_1ktna8q\" sourceRef=\"ServiceTask_1\" targetRef=\"CollectionPoint_10\"/\u003e\u003csequenceFlow id=\"Flow_0fot35v\" sourceRef=\"CollectionPoint_10\" targetRef=\"ServiceTask_6\"/\u003e\u003cendEvent id=\"EndPoint_11\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0xgjir5\u003c/incoming\u003e\u003c/endEvent\u003e\u003cexclusiveGateway default=\"Flow_1vmfh17\" id=\"ConditionPoint_12\" resilient:documentation=\"Check if edit address was successful\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1cask2u\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vmfh17\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0tm6f8v\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_13\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0tm6f8v\u003c/incoming\u003e\u003coutgoing\u003eFlow_0guhhgo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_14\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dc223973-47f1-42d9-8163-2f5a1f60f730\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0guhhgo\u003c/incoming\u003e\u003coutgoing\u003eFlow_19ic6tk\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0guhhgo\" sourceRef=\"ServiceTask_13\" targetRef=\"ScriptTask_14\"/\u003e\u003csequenceFlow id=\"Flow_19ic6tk\" sourceRef=\"ScriptTask_14\" targetRef=\"EndPoint_8\"/\u003e\u003csequenceFlow id=\"Flow_1cask2u\" sourceRef=\"ServiceTask_6\" targetRef=\"ConditionPoint_12\"/\u003e\u003csequenceFlow id=\"Flow_0fj9g69\" sourceRef=\"ServiceTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_02irm2s\" name=\"If finished running\" sourceRef=\"ConditionPoint_9\" targetRef=\"CollectionPoint_10\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"If finished running\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.addresses_results else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0xgjir5\" name=\"Else\" sourceRef=\"ConditionPoint_9\" targetRef=\"EndPoint_11\"/\u003e\u003csequenceFlow id=\"Flow_0e8wgg1\" name=\"address to block is present\" sourceRef=\"ConditionPoint_3\" targetRef=\"ConditionPoint_9\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"address to block is present\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.addresses_results\\n\\ncreated_addresses = []\\nfor address in results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\"):\\n  if \\\"ip-netmask\\\" in address:\\n    created_addresses.append(address.get(\\\"ip-netmask\\\"))\\n  if \\\"fqdn\\\" in address:\\n    created_addresses.append(address.get(\\\"fqdn\\\"))\\n\\nif artifact.value in created_addresses:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1canimf\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"/\u003e\u003csequenceFlow id=\"Flow_0tm6f8v\" name=\"Successful edit group\" sourceRef=\"ConditionPoint_12\" targetRef=\"ServiceTask_13\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Successful edit group\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_group_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1vmfh17\" name=\"Else\" sourceRef=\"ConditionPoint_12\" targetRef=\"ScriptTask_7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_20761e90_81df_4c9a_a13e_872c6c5fed85\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xgjir5\" id=\"Flow_0xgjir5_di\"\u003e\u003comgdi:waypoint x=\"1573\" y=\"780\"/\u003e\u003comgdi:waypoint x=\"1724\" y=\"780\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1641\" y=\"762\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02irm2s\" id=\"Flow_02irm2s_di\"\u003e\u003comgdi:waypoint x=\"1451\" y=\"806\"/\u003e\u003comgdi:waypoint x=\"1451\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"1358\" y=\"870\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1396\" y=\"833\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1canimf\" id=\"Flow_1canimf_di\"\u003e\u003comgdi:waypoint x=\"1525\" y=\"546\"/\u003e\u003comgdi:waypoint x=\"1525\" y=\"587\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"587\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"628\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1582\" y=\"593\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0e8wgg1\" id=\"Flow_0e8wgg1_di\"\u003e\u003comgdi:waypoint x=\"1375\" y=\"546\"/\u003e\u003comgdi:waypoint x=\"1375\" y=\"650\"/\u003e\u003comgdi:waypoint x=\"1381\" y=\"650\"/\u003e\u003comgdi:waypoint x=\"1381\" y=\"754\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"86\" x=\"1332\" y=\"589\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vmfh17\" id=\"Flow_1vmfh17_di\"\u003e\u003comgdi:waypoint x=\"1220\" y=\"1126\"/\u003e\u003comgdi:waypoint x=\"1220\" y=\"1192\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"1192\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"1218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1440\" y=\"1153\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0tm6f8v\" id=\"Flow_0tm6f8v_di\"\u003e\u003comgdi:waypoint x=\"1220\" y=\"1126\"/\u003e\u003comgdi:waypoint x=\"1220\" y=\"1192\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"1192\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"1218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"80\" x=\"1102\" y=\"1166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fj9g69\" id=\"Flow_0fj9g69_di\"\u003e\u003comgdi:waypoint x=\"1470\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"494\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1cask2u\" id=\"Flow_1cask2u_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"1052\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"1074\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_19ic6tk\" id=\"Flow_19ic6tk_di\"\u003e\u003comgdi:waypoint x=\"1110\" y=\"1442\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"1530\"/\u003e\u003comgdi:waypoint x=\"1224\" y=\"1530\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0guhhgo\" id=\"Flow_0guhhgo_di\"\u003e\u003comgdi:waypoint x=\"1110\" y=\"1302\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"1358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fot35v\" id=\"Flow_0fot35v_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"896\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"968\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ktna8q\" id=\"Flow_1ktna8q_di\"\u003e\u003comgdi:waypoint x=\"1110\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"1221\" y=\"870\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hunjc9\" id=\"Flow_1hunjc9_di\"\u003e\u003comgdi:waypoint x=\"1590\" y=\"712\"/\u003e\u003comgdi:waypoint x=\"1590\" y=\"733\"/\u003e\u003comgdi:waypoint x=\"1451\" y=\"733\"/\u003e\u003comgdi:waypoint x=\"1451\" y=\"754\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1djmatv\" id=\"Flow_1djmatv_di\"\u003e\u003comgdi:waypoint x=\"1470\" y=\"1302\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"1428\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"1428\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"1504\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sl7qel\" id=\"Flow_1sl7qel_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1470\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17ese3i\" id=\"Flow_17ese3i_di\"\u003e\u003comgdi:waypoint x=\"1290\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"1290\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"247\"/\u003e\u003comgdi:waypoint x=\"1110\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1199\" y=\"164\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1012\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1372\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"293.83299999999997\" x=\"1323\" y=\"494\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1492\" y=\"628\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1192\" y=\"968\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_7\" id=\"ScriptTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1372\" y=\"1218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_8\" id=\"EndPoint_8_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1224\" y=\"1504\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_9\" id=\"ConditionPoint_9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1329\" y=\"754\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_10\" id=\"CollectionPoint_10_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1221\" y=\"844\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_11\" id=\"EndPoint_11_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1724\" y=\"754\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_12\" id=\"ConditionPoint_12_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"383.75\" x=\"1098\" y=\"1074\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13\" id=\"ServiceTask_13_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1012.425392670157\" y=\"1217.9895287958116\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_14\" id=\"ScriptTask_14_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1012.425392670157\" y=\"1357.9895287958116\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027808649,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
      "description": {
        "content": "Given a DNS Name artifact, adds the DNS Name to the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Panorama: Block DNS Name - Example (PB)",
      "export_key": "example_panorama_block_dns_name",
      "field_type_handle": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Block DNS Name - Example (PB)",
        "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
        "fields": {
          "panorama_device_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85/panorama_device_group",
            "hide_notification": false,
            "id": 5272,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "group1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Device Group",
            "tooltip": "Name of the device group to use",
            "type_id": 1080,
            "uuid": "d30b5120-bc78-4e54-aa1a-1a451339bd3a",
            "values": []
          },
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
            "id": 5257,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config. ",
            "type_id": 1080,
            "uuid": "1d9faeac-0b24-4bfd-a5c7-f9eaf74b9858",
            "values": []
          },
          "panorama_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85/panorama_location",
            "hide_notification": false,
            "id": 5273,
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
            "text": "Panorama Location",
            "tooltip": "Panorama location to use",
            "type_id": 1080,
            "uuid": "b07f48f7-38b3-48ea-a73a-520e09bb2998",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "vsys",
                "properties": null,
                "uuid": "8b260770-9429-48f9-a68f-6b18a1b07b75",
                "value": 2264
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "panorama-pushed",
                "properties": null,
                "uuid": "a9f321e9-0213-4a4c-9663-1066a45fa7cf",
                "value": 2265
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "shared",
                "properties": null,
                "uuid": "d6789195-d6c5-4218-ba6f-adbf7e932991",
                "value": 2268
              },
              {
                "default": false,
                "enabled": false,
                "hidden": false,
                "label": "device-group",
                "properties": null,
                "uuid": "67623fc6-3383-4bf5-8060-114de62060aa",
                "value": 2266
              }
            ]
          },
          "panorama_vsys": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85/panorama_vsys",
            "hide_notification": false,
            "id": 5274,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_vsys",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama vsys",
            "tooltip": "Name of the vsys to use",
            "type_id": 1080,
            "uuid": "cf4d56cd-5a60-48bc-95b5-085397560d7f",
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
      "id": 66,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741198225343,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027809098,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 76,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027809098,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_dns_name",
          "programmatic_name": "example_panorama_block_dns_name_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_group = playbook.functions.results.edit_group_results\nif edit_group.get(\"success\"):\n  note += f\"Panorama DNS name: {artifact.value} was blocked.\\n\"\nelse:\n  note += f\"Panorama Block DNS failed with reason: {edit_group.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "dc223973-47f1-42d9-8163-2f5a1f60f730"
        },
        {
          "actions": [],
          "created_date": 1741027809170,
          "description": "",
          "enabled": false,
          "export_key": "Panorama Block DNS Name post-process",
          "id": 77,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027809170,
          "name": "Panorama Block DNS Name post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_dns_name",
          "programmatic_name": "example_panorama_block_dns_name_block_dns_name_post_process",
          "script_text": "results = playbook.functions.results.edit_group_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama DNS name: {artifact.value} was blocked.\")\nelse:\n  incident.addNote(f\"Panorama Block DNS failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "b07f48f7-38b3-48ea-a73a-520e09bb2998",
            "element": "field_uuid",
            "field_type": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is vsys or panorama-pushed, then panorama_vsys must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "cf4d56cd-5a60-48bc-95b5-085397560d7f",
            "element": "field_uuid",
            "field_type": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is device-group, then panorama_device_group must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d30b5120-bc78-4e54-aa1a-1a451339bd3a",
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
        "id": 68,
        "name": "playbook_20761e90_81df_4c9a_a13e_872c6c5fed85",
        "type": "playbook",
        "uuid": "24cc2e03-b8f9-4a37-be57-f63bb2d4f247"
      },
      "tags": [],
      "type": "default",
      "uuid": "20761e90-81df-4c9a-a13e-872c6c5fed85",
      "version": 23
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\" isExecutable=\"true\" name=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1ioa0ju\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1umtp27\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cexclusiveGateway default=\"Flow_0uq42j3\" id=\"ConditionPoint_4\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1xq4igl\u003c/incoming\u003e\u003coutgoing\u003eFlow_0uq42j3\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0ajrv54\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cparallelGateway id=\"CollectionPoint_5\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_1bm214o\u003c/incoming\u003e\u003cincoming\u003eFlow_0bbxhdj\u003c/incoming\u003e\u003coutgoing\u003eFlow_1bopayq\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ioa0ju\u003c/incoming\u003e\u003coutgoing\u003eFlow_1xq4igl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1ioa0ju\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_6\"/\u003e\u003csequenceFlow id=\"Flow_1xq4igl\" sourceRef=\"ServiceTask_6\" targetRef=\"ConditionPoint_4\"/\u003e\u003cserviceTask id=\"ServiceTask_7\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1umtp27\u003c/incoming\u003e\u003coutgoing\u003eFlow_1bm214o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1umtp27\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_7\"/\u003e\u003csequenceFlow id=\"Flow_1bm214o\" sourceRef=\"ServiceTask_7\" targetRef=\"CollectionPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_8\" name=\"Panorama Create Address\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8450551a-7da1-48b1-929f-798d4ef923ee\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"from json import dumps\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = artifact.value\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": artifact.value,\\n    \\\"description\\\": artifact.value,\\n    \\\"ip-netmask\\\": artifact.value\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_address_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0uq42j3\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ik3izc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cexclusiveGateway default=\"Flow_1nowzes\" id=\"ConditionPoint_9\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0ajrv54\u003c/incoming\u003e\u003cincoming\u003eFlow_0ik3izc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0bbxhdj\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1nowzes\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0ik3izc\" sourceRef=\"ServiceTask_8\" targetRef=\"ConditionPoint_9\"/\u003e\u003cendEvent id=\"EndPoint_10\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1nowzes\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_11\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"from json import dumps\\n\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nip_name = \\\"\\\"\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\nif group:\\n  group = group[0]\\n\\n# If new address was created\\nif playbook.functions.results.create_address_results:\\n  ip_name = artifact.value\\n# Else find it in the list of addresses\\nelse:\\n  addresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\")\\n  for address in addresses:\\n    if address.get(\\\"ip-netmask\\\") == artifact.value:\\n      ip_name = address.get(\\\"@name\\\")\\n      break\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\", [])\\nif ip_name not in member_list:\\n  member_list.append(ip_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\n# If using api version 9.0 or before uncomment below for the body\\n# body = {\\n#   \\\"entry\\\": {\\n#     \\\"@name\\\": group_name,\\n#     \\\"static\\\": {\\n#       \\\"member\\\": dumps(member_list)\\n#     }\\n#   }\\n# }\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": group_name,\\n    \\\"static\\\": {\\n      \\\"member\\\": member_list\\n    }\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1bopayq\u003c/incoming\u003e\u003coutgoing\u003eFlow_130y1vm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1bopayq\" sourceRef=\"CollectionPoint_5\" targetRef=\"ServiceTask_11\"/\u003e\u003cscriptTask id=\"ScriptTask_12\" name=\"Panorama Block IP post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"b12cfc5c-8649-4a55-bb00-7535c14fe4f7\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09ug8as\u003c/incoming\u003e\u003coutgoing\u003eFlow_1wxjccx\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_13\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1wxjccx\u003c/incoming\u003e\u003cincoming\u003eFlow_1az73h3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_14\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14ntf1r\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fd6ofw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cexclusiveGateway default=\"Flow_09ug8as\" id=\"ConditionPoint_15\" resilient:documentation=\"Group edited\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_130y1vm\u003c/incoming\u003e\u003coutgoing\u003eFlow_14ntf1r\u003c/outgoing\u003e\u003coutgoing\u003eFlow_09ug8as\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_130y1vm\" sourceRef=\"ServiceTask_11\" targetRef=\"ConditionPoint_15\"/\u003e\u003csequenceFlow id=\"Flow_1wxjccx\" sourceRef=\"ScriptTask_12\" targetRef=\"EndPoint_13\"/\u003e\u003cscriptTask id=\"ScriptTask_16\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"841e10cf-a50f-4b7e-a7c0-d457f272d077\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0fd6ofw\u003c/incoming\u003e\u003coutgoing\u003eFlow_1az73h3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0fd6ofw\" sourceRef=\"ServiceTask_14\" targetRef=\"ScriptTask_16\"/\u003e\u003csequenceFlow id=\"Flow_1az73h3\" sourceRef=\"ScriptTask_16\" targetRef=\"EndPoint_13\"/\u003e\u003csequenceFlow id=\"Flow_14ntf1r\" name=\"Edited group successfully\" sourceRef=\"ConditionPoint_15\" targetRef=\"ServiceTask_14\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Edited group successfully\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_groups_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_09ug8as\" name=\"Else\" sourceRef=\"ConditionPoint_15\" targetRef=\"ScriptTask_12\"/\u003e\u003csequenceFlow id=\"Flow_0bbxhdj\" name=\"If finished running\" sourceRef=\"ConditionPoint_9\" targetRef=\"CollectionPoint_5\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"If finished running\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.get_addresses_results else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1nowzes\" name=\"Else\" sourceRef=\"ConditionPoint_9\" targetRef=\"EndPoint_10\"/\u003e\u003csequenceFlow id=\"Flow_0ajrv54\" name=\"Address to block is present\" sourceRef=\"ConditionPoint_4\" targetRef=\"ConditionPoint_9\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Address to block is present\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"results = playbook.functions.results.get_addresses_results\\ncreated_addresses = []\\nfor address in results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\"):\\n  if \\\"ip-netmask\\\" in address:\\n    created_addresses.append(address.get(\\\"ip-netmask\\\"))\\n  if \\\"fqdn\\\" in address:\\n    created_addresses.append(address.get(\\\"fqdn\\\"))\\n\\nif artifact.value in created_addresses:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0uq42j3\" name=\"Else\" sourceRef=\"ConditionPoint_4\" targetRef=\"ServiceTask_8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09ug8as\" id=\"Flow_09ug8as_di\"\u003e\u003comgdi:waypoint x=\"1854\" y=\"970\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"970\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"1078\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1898\" y=\"983\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14ntf1r\" id=\"Flow_14ntf1r_di\"\u003e\u003comgdi:waypoint x=\"1626\" y=\"970\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"970\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"1078\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"68\" x=\"1556\" y=\"976\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nowzes\" id=\"Flow_1nowzes_di\"\u003e\u003comgdi:waypoint x=\"2052\" y=\"620\"/\u003e\u003comgdi:waypoint x=\"2154\" y=\"620\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"2092\" y=\"602\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bbxhdj\" id=\"Flow_0bbxhdj_di\"\u003e\u003comgdi:waypoint x=\"1930\" y=\"646\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1808\" y=\"710\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1865\" y=\"675\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0uq42j3\" id=\"Flow_0uq42j3_di\"\u003e\u003comgdi:waypoint x=\"2052\" y=\"390\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"390\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"458\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"2080\" y=\"403\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ajrv54\" id=\"Flow_0ajrv54_di\"\u003e\u003comgdi:waypoint x=\"1850\" y=\"416\"/\u003e\u003comgdi:waypoint x=\"1850\" y=\"594\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"84\" x=\"1808\" y=\"486\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1az73h3\" id=\"Flow_1az73h3_di\"\u003e\u003comgdi:waypoint x=\"1550\" y=\"1312\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"1370\"/\u003e\u003comgdi:waypoint x=\"1674\" y=\"1370\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fd6ofw\" id=\"Flow_0fd6ofw_di\"\u003e\u003comgdi:waypoint x=\"1550\" y=\"1162\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"1228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1wxjccx\" id=\"Flow_1wxjccx_di\"\u003e\u003comgdi:waypoint x=\"1930\" y=\"1162\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"1370\"/\u003e\u003comgdi:waypoint x=\"1806\" y=\"1370\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_130y1vm\" id=\"Flow_130y1vm_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"872\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"944\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bopayq\" id=\"Flow_1bopayq_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"736\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"788\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ik3izc\" id=\"Flow_0ik3izc_di\"\u003e\u003comgdi:waypoint x=\"2130\" y=\"542\"/\u003e\u003comgdi:waypoint x=\"2130\" y=\"568\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"568\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"594\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bm214o\" id=\"Flow_1bm214o_di\"\u003e\u003comgdi:waypoint x=\"1550\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1671\" y=\"710\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1umtp27\" id=\"Flow_1umtp27_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1550\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1xq4igl\" id=\"Flow_1xq4igl_di\"\u003e\u003comgdi:waypoint x=\"1930\" y=\"312\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"364\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ioa0ju\" id=\"Flow_1ioa0ju_di\"\u003e\u003comgdi:waypoint x=\"1740\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"1740\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"207\"/\u003e\u003comgdi:waypoint x=\"1930\" y=\"228\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1649\" y=\"134\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_4\" id=\"ConditionPoint_4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1808\" y=\"364\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_5\" id=\"CollectionPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1671\" y=\"684\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1832\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_7\" id=\"ServiceTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1452\" y=\"228\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_8\" id=\"ServiceTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"2032\" y=\"458\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_9\" id=\"ConditionPoint_9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1808\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_10\" id=\"EndPoint_10_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"2154\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11\" id=\"ServiceTask_11_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1642\" y=\"788\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_12\" id=\"ScriptTask_12_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1832\" y=\"1078\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_13\" id=\"EndPoint_13_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1674\" y=\"1344\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_14\" id=\"ServiceTask_14_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1452\" y=\"1078\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_15\" id=\"ConditionPoint_15_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"228.4\" x=\"1626\" y=\"944\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_16\" id=\"ScriptTask_16_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1451.7190860215055\" y=\"1228.0672043010752\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027811138,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
      "description": {
        "content": "Given an IP Address artifact, adds the IP Address to the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Panorama: Block IP Address - Example (PB)",
      "export_key": "example_panorama_block_ip_address",
      "field_type_handle": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Block IP Address - Example (PB)",
        "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
        "fields": {
          "panorama_device_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1/panorama_device_group",
            "hide_notification": false,
            "id": 5279,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "group1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Device Group",
            "tooltip": "Name of the device group to use",
            "type_id": 1081,
            "uuid": "c4a4a9ad-ae12-400f-b7df-46ad1550b336",
            "values": []
          },
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
            "id": 5258,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1081,
            "uuid": "5f1eea39-f8cf-4381-9a3e-810492e82296",
            "values": []
          },
          "panorama_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1/panorama_location",
            "hide_notification": false,
            "id": 5280,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_location",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Location",
            "tooltip": "Panorama location to use",
            "type_id": 1081,
            "uuid": "55d9076a-beb5-4fc6-a0d5-da59ddfe4a6b",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "vsys",
                "properties": null,
                "uuid": "99e52680-51bf-4c49-8e38-f7aeea0ce9e7",
                "value": 2304
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "panorama-pushed",
                "properties": null,
                "uuid": "cfdebb89-9448-4be2-93d1-cab45fe245e4",
                "value": 2305
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "shared",
                "properties": null,
                "uuid": "65ccc365-8dbf-403f-80a4-56aa61d04fb6",
                "value": 2306
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "device-group",
                "properties": null,
                "uuid": "fb862bd9-7759-4679-a7c4-59f9982f7316",
                "value": 2307
              }
            ]
          },
          "panorama_vsys": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1/panorama_vsys",
            "hide_notification": false,
            "id": 5281,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_vsys",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama vsys",
            "tooltip": "Name of the vsys to use",
            "type_id": 1081,
            "uuid": "71d5785c-17a6-4647-ab2c-124c4330aa44",
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
      "id": 67,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741198432802,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027811783,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 78,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027811783,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_ip_address",
          "programmatic_name": "example_panorama_block_ip_address_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_groups = playbook.functions.results.edit_groups_results\nif edit_groups.get(\"success\"):\n  note += f\"Panorama IP Address: {artifact.value} was blocked.\\n\"\nelse:\n  note += f\"Panorama Block IP failed with reason: {edit_groups.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "841e10cf-a50f-4b7e-a7c0-d457f272d077"
        },
        {
          "actions": [],
          "created_date": 1741027811905,
          "description": "",
          "enabled": false,
          "export_key": "Panorama Block IP post-process",
          "id": 79,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027811905,
          "name": "Panorama Block IP post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_ip_address",
          "programmatic_name": "example_panorama_block_ip_address_block_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_groups_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama IP Address: {artifact.value} was blocked.\")\nelse:\n  incident.addNote(f\"Panorama Block IP failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "55d9076a-beb5-4fc6-a0d5-da59ddfe4a6b",
            "element": "field_uuid",
            "field_type": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is vsys or panorama-pushed, then panorama_vsys must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "71d5785c-17a6-4647-ab2c-124c4330aa44",
            "element": "field_uuid",
            "field_type": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is device-group, then panorama_device_group must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "c4a4a9ad-ae12-400f-b7df-46ad1550b336",
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
        "id": 69,
        "name": "playbook_4f6ee7aa_22cc_4d4b_9696_dd1cac5e4de1",
        "type": "playbook",
        "uuid": "f5fce47d-a28f-4a71-8a5c-c08f3d0cb54d"
      },
      "tags": [],
      "type": "default",
      "uuid": "4f6ee7aa-22cc-4d4b-9696-dd1cac5e4de1",
      "version": 9
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 15,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\" isExecutable=\"true\" name=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qt9mg8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"85a6dc33-8f88-4bb5-9e21-3daa253d4a6c\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# Set this to the xpath of the group you are interested in\\nif getattr(playbook.inputs, \\\"panorama_template\\\", None):\\n  inputs.panorama_user_group_xpath = f\\\"/config/devices/entry[@name=\u0027localhost.localdomain\u0027]/template/entry[@name=\u0027{playbook.inputs.panorama_template}\u0027]/config/shared/local-user-database/user-group/entry[@name=\u0027Blocked_Users\u0027]\\\"\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_location = \\\"shared\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qt9mg8\u003c/incoming\u003e\u003coutgoing\u003eFlow_1lgsf39\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Edit Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e89ee2fa-3983-417e-9e69-f8a5ac9961cd\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"4c33528f-e008-4d22-9787-28f864c7456e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"shared\\\"\\n# Set this to the name of the user group you wish to add a user to\\ngroup_name = \\\"Blocked_Users\\\"\\n\\n# Set this to the xpath of the group you are interested in\\nif getattr(playbook.inputs, \\\"panorama_template\\\", None):\\n  inputs.panorama_user_group_xpath = f\\\"/config/devices/entry[@name=\u0027localhost.localdomain\u0027]/template/entry[@name=\u0027{playbook.inputs.panorama_template}\u0027]/config/shared/local-user-database/user-group/entry[@name=\u0027{group_name}\u0027]\\\"\\n\\nusers_list = playbook.functions.results.get_users_results.get(\\\"content\\\", {}).get(\\\"user_list\\\", [])\\n\\nblocked_users = []\\n\\nif len(users_list) == 1:\\n  # only one user was returned\\n  blocked_users.append(users_list[0])\\nelif len(users_list) \u0026gt; 1:\\n  # multiple users returned\\n  for user in users_list:\\n    blocked_users.append(user.get(\\\"#text\\\"))\\n\\n# Add the user to the blocked list if they are not already there\\nif artifact.value not in blocked_users:\\n  blocked_users.append(artifact.value)\\n\\n# Updated function creates the xml request body for you\\ninputs.panorama_users_list = str(blocked_users)\\ninputs.panorama_user_group_name = group_name\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\n\\n# Giving the xml request body as an input still works\\n# # Build xml which the function will send to Panorama\\n# panorama_xml = f\u0027\u0027\u0027\\n# \u0026lt;entry name=\\\"{str(group_name)}\\\"\u0026gt;\\n#     \u0026lt;user\u0026gt;\u0027\u0027\u0027\\n\\n# # Add member nodes with the username to the xml string\\n# for user in blocked_users:\\n#   panorama_xml += f\\\"\\\\n      \u0026lt;member\u0026gt;{user}\u0026lt;/member\u0026gt;\\\"\\n\\n# # Add the ending of the xml to the string\\n# panorama_xml += \\\"\\\"\\\"\\n#     \u0026lt;/user\u0026gt;\\n# \u0026lt;/entry\u0026gt;\\n# \\\"\\\"\\\"\\n# inputs.panorama_user_group_xml = panorama_xml\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1lgsf39\u003c/incoming\u003e\u003coutgoing\u003eFlow_0te9q5e\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Panorama block user post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"05f9f363-4dd6-41ad-b7fb-8d12286700b4\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1xowp5s\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wfegvd\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0qt9mg8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1lgsf39\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0wfegvd\u003c/incoming\u003e\u003cincoming\u003eFlow_0gkvkx0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0wfegvd\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_4\"/\u003e\u003cexclusiveGateway default=\"Flow_1xowp5s\" id=\"ConditionPoint_5\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0te9q5e\u003c/incoming\u003e\u003coutgoing\u003eFlow_1xowp5s\u003c/outgoing\u003e\u003coutgoing\u003eFlow_111cegq\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0te9q5e\" sourceRef=\"ServiceTask_2\" targetRef=\"ConditionPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_location = \\\"shared\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_111cegq\u003c/incoming\u003e\u003coutgoing\u003eFlow_0xqkc6a\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_7\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"163a9ca0-97d5-4987-a565-7cc29e5d3685\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0xqkc6a\u003c/incoming\u003e\u003coutgoing\u003eFlow_0gkvkx0\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0xqkc6a\" sourceRef=\"ServiceTask_6\" targetRef=\"ScriptTask_7\"/\u003e\u003csequenceFlow id=\"Flow_0gkvkx0\" sourceRef=\"ScriptTask_7\" targetRef=\"EndPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_111cegq\" name=\"successfully edit users\" sourceRef=\"ConditionPoint_5\" targetRef=\"ServiceTask_6\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"successfully edit users\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_users_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1xowp5s\" name=\"Else\" sourceRef=\"ConditionPoint_5\" targetRef=\"ScriptTask_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1xowp5s\" id=\"Flow_1xowp5s_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"500\"/\u003e\u003comgdi:waypoint x=\"930\" y=\"500\"/\u003e\u003comgdi:waypoint x=\"930\" y=\"608\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"875\" y=\"523\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_111cegq\" id=\"Flow_111cegq_di\"\u003e\u003comgdi:waypoint x=\"599\" y=\"500\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"500\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"608\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"87\" x=\"526\" y=\"516\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0gkvkx0\" id=\"Flow_0gkvkx0_di\"\u003e\u003comgdi:waypoint x=\"510\" y=\"832\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"940\"/\u003e\u003comgdi:waypoint x=\"655\" y=\"940\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xqkc6a\" id=\"Flow_0xqkc6a_di\"\u003e\u003comgdi:waypoint x=\"510\" y=\"692\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"748\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0te9q5e\" id=\"Flow_0te9q5e_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wfegvd\" id=\"Flow_0wfegvd_di\"\u003e\u003comgdi:waypoint x=\"930\" y=\"692\"/\u003e\u003comgdi:waypoint x=\"930\" y=\"940\"/\u003e\u003comgdi:waypoint x=\"787\" y=\"940\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1lgsf39\" id=\"Flow_1lgsf39_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qt9mg8\" id=\"Flow_0qt9mg8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"832\" y=\"608\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"914\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_5\" id=\"ConditionPoint_5_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"474\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"412\" y=\"608\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_7\" id=\"ScriptTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"411.5\" y=\"747.75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027813743,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
      "description": {
        "content": "Given a User Account artifact, adds the user to the \"Blocked_Users\" group in Panorama. This only works with Panorama and does not work with PanOS.",
        "format": "text"
      },
      "display_name": "Panorama: Block User - Example (PB)",
      "export_key": "example_panorama_block_user",
      "field_type_handle": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Block User - Example (PB)",
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
            "id": 5259,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1082,
            "uuid": "c5778bf4-13a6-4037-94de-96f47974cbef",
            "values": []
          },
          "panorama_template": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f/panorama_template",
            "hide_notification": false,
            "id": 5283,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_template",
            "operation_perms": {},
            "operations": [],
            "placeholder": "temp1",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Template",
            "tooltip": "Name of the Panorama template to use",
            "type_id": 1082,
            "uuid": "c3a6da57-0bfe-41ac-8f4d-fce73f64e1b6",
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
      "id": 68,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741204913729,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027814224,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 80,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027814224,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_user",
          "programmatic_name": "example_panorama_block_user_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_user = playbook.functions.results.edit_users_results\nif edit_user.get(\"success\"):\n  note += f\"Panorama User account: {artifact.value} was blocked.\\n\"\nelse:\n  if \"code 12\" in edit_user.get(\"reason\"):\n    note += \"Panorama Block User failed because the User you are trying to block does not exist.\\n\"\n  else:\n    note += f\"Panorama Block User failed with reason: {edit_user.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "163a9ca0-97d5-4987-a565-7cc29e5d3685"
        },
        {
          "actions": [],
          "created_date": 1741027814302,
          "description": "",
          "enabled": false,
          "export_key": "Panorama block user post-process",
          "id": 81,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027814302,
          "name": "Panorama block user post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_block_user",
          "programmatic_name": "example_panorama_block_user_block_user_post_process",
          "script_text": "results = playbook.functions.results.edit_users_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama User account: {artifact.value} was blocked.\")\nelse:\n  if \"code 12\" in results.get(\"reason\"):\n    incident.addNote(\"Panorama Block User failed because the User you are trying to block does not exist.\")\n  else:\n    incident.addNote(f\"Panorama Block User failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "c3a6da57-0bfe-41ac-8f4d-fce73f64e1b6",
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
        "id": 70,
        "name": "playbook_7bc7deb6_d0e0_434b_b25d_aaed1532ea9f",
        "type": "playbook",
        "uuid": "f303cb58-f571-4054-8a23-b0a43975b404"
      },
      "tags": [],
      "type": "default",
      "uuid": "7bc7deb6-d0e0-434b-b25d-aaed1532ea9f",
      "version": 19
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_af36d5fa_489f_4946_9ba0_bf8085943a73\" isExecutable=\"true\" name=\"playbook_af36d5fa_489f_4946_9ba0_bf8085943a73\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0agx1ze\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Commit All\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3366b084-8a3d-4631-834d-9124a5e57614\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.panorama_commit_without_default_template = getattr(playbook.inputs, \\\"panorama_commit_without_default_templates\\\", False)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group_name\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"panorama_commit_all_return\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0agx1ze\u003c/incoming\u003e\u003coutgoing\u003eFlow_12mxpk7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0agx1ze\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Panorama Commit all results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e8cf1513-f071-4dad-bf0c-7615f9b8cd71\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12mxpk7\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jri3r2\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_12mxpk7\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jri3r2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jri3r2\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_af36d5fa_489f_4946_9ba0_bf8085943a73\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jri3r2\" id=\"Flow_0jri3r2_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"432\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"524\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12mxpk7\" id=\"Flow_12mxpk7_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"348\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0agx1ze\" id=\"Flow_0agx1ze_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5419999999999\" y=\"347.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"524\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027815998,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
      "description": {
        "content": "Commit all and push",
        "format": "text"
      },
      "display_name": "Panorama: Commit All - Example (PB)",
      "export_key": "panorama_commit_all",
      "field_type_handle": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Commit All - Example (PB)",
        "export_key": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
        "fields": {
          "panorama_commit_without_default_templates": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73/panorama_commit_without_default_templates",
            "hide_notification": false,
            "id": 5260,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_commit_without_default_templates",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Commit without default templates",
            "tooltip": "Specific device group commit without including default device/network template changes.",
            "type_id": 1083,
            "uuid": "95576a91-a063-4263-980c-eadfed2fd288",
            "values": []
          },
          "panorama_device_group_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73/panorama_device_group_name",
            "hide_notification": false,
            "id": 5261,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Device Group Name",
            "tooltip": "Panorama device group name",
            "type_id": 1083,
            "uuid": "62208068-0d88-4668-8fd9-89fbca5c1fc7",
            "values": []
          },
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73/panorama_label",
            "hide_notification": false,
            "id": 5262,
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
            "text": "panorama label",
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1083,
            "uuid": "11619fe9-c23e-414c-94bc-4e9c9fd82fb7",
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
        "type_name": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
        "uuid": "7ea8e032-cf95-4231-b5a9-a2c1a7ef804b"
      },
      "has_logical_errors": false,
      "id": 69,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741273027482,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027816868,
          "description": "",
          "enabled": false,
          "export_key": "Panorama Commit all results",
          "id": 82,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027816868,
          "name": "Panorama Commit all results",
          "object_type": "incident",
          "playbook_handle": "panorama_commit_all",
          "programmatic_name": "panorama_commit_all_panorama_commit_all_results",
          "script_text": "from json import dumps\nresults = playbook.functions.results.panorama_commit_all_return\nif results.get(\"success\", None):\n  incident.addNote(f\"Panorama: Commit All returned\\n{dumps(results.get(\u0027content\u0027, {}), indent=4)}\")\nelse:\n  incident.addNote(f\"Panorama: Commit All failed with reason: {results.get(\u0027reason\u0027, None)}\")",
          "tags": [],
          "uuid": "e8cf1513-f071-4dad-bf0c-7615f9b8cd71"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "62208068-0d88-4668-8fd9-89fbca5c1fc7",
            "element": "field_uuid",
            "field_type": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "11619fe9-c23e-414c-94bc-4e9c9fd82fb7",
            "element": "field_uuid",
            "field_type": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "95576a91-a063-4263-980c-eadfed2fd288",
            "element": "field_uuid",
            "field_type": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "panorama_commit_all",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_af36d5fa-489f-4946-9ba0-bf8085943a73",
        "id": 71,
        "name": "playbook_af36d5fa_489f_4946_9ba0_bf8085943a73",
        "type": "playbook",
        "uuid": "f99a316c-7196-4860-b809-d8fd8820a4e4"
      },
      "tags": [],
      "type": "default",
      "uuid": "af36d5fa-489f-4946-9ba0-bf8085943a73",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532\" isExecutable=\"true\" name=\"playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0z59qd2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\n  \\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"address_groups\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0z59qd2\u003c/incoming\u003e\u003coutgoing\u003eFlow_07y3vq7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0z59qd2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Panorama post process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"ab4fbb5c-f777-4434-973f-1f24bab618f6\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_07y3vq7\u003c/incoming\u003e\u003coutgoing\u003eFlow_0q4h7z3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_07y3vq7\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0q4h7z3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0q4h7z3\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0q4h7z3\" id=\"Flow_0q4h7z3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_07y3vq7\" id=\"Flow_07y3vq7_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0z59qd2\" id=\"Flow_0z59qd2_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741190560406,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
      "description": {
        "content": "Get address groups on the Panorama server",
        "format": "text"
      },
      "display_name": "Panorama: Get Address Groups - Example (PB)",
      "export_key": "example_panorama_get_address_groups",
      "field_type_handle": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Get Address Groups - Example (PB)",
        "export_key": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
        "fields": {
          "panorama_device_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532/panorama_device_group",
            "hide_notification": false,
            "id": 5275,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "group1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Device Group",
            "tooltip": "Name of the device group to use",
            "type_id": 1089,
            "uuid": "930f37b7-b72f-4a0c-8135-b0b68efd82e2",
            "values": []
          },
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532/panorama_label",
            "hide_notification": false,
            "id": 5276,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1089,
            "uuid": "bafa45c4-232c-4810-8ab7-3a1e97cbd460",
            "values": []
          },
          "panorama_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532/panorama_location",
            "hide_notification": false,
            "id": 5277,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_location",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Location",
            "tooltip": "Panorama location to use",
            "type_id": 1089,
            "uuid": "b667c785-f9b6-49df-848f-44f8272b9144",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "vsys",
                "properties": null,
                "uuid": "bc8fcf3d-2420-4e3d-ac88-33d52374bd67",
                "value": 2269
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "panorama-pushed",
                "properties": null,
                "uuid": "7c689b13-1de9-4a3b-8b7f-8ea9543ec65f",
                "value": 2270
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "shared",
                "properties": null,
                "uuid": "188fdd4c-22e3-4a3a-ade1-f7ffab4aeed9",
                "value": 2302
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "device-group",
                "properties": null,
                "uuid": "01cf4b98-831f-49b3-8a0f-7e495ec9c19c",
                "value": 2303
              }
            ]
          },
          "panorama_vsys": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532/panorama_vsys",
            "hide_notification": false,
            "id": 5278,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_vsys",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama vsys",
            "tooltip": "Name of the vsys to use",
            "type_id": 1089,
            "uuid": "21b45a1f-196c-452e-a207-4bc41ce6c403",
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
        "type_name": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
        "uuid": "eb16b0ac-8581-4020-bc3b-92e8e2831454"
      },
      "has_logical_errors": false,
      "id": 75,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741199203318,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741190561260,
          "description": "",
          "enabled": false,
          "export_key": "Panorama post process",
          "id": 93,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741190561260,
          "name": "Panorama post process",
          "object_type": "incident",
          "playbook_handle": "example_panorama_get_address_groups",
          "programmatic_name": "example_panorama_get_address_groups_post_process",
          "script_text": "from json import dumps\nresults = playbook.functions.results.address_groups\n\nif results.get(\"success\"):\n  incident.addNote(f\u0027Panorama Get Address Groups\\n{dumps(results.get(\"content\", {}), indent=4)}\u0027)\nelse:\n  incident.addNote(f\"Panorama Get address groups failed with reason: {results.get(\u0027reason\u0027)}\")",
          "tags": [],
          "uuid": "ab4fbb5c-f777-4434-973f-1f24bab618f6"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "bafa45c4-232c-4810-8ab7-3a1e97cbd460",
            "element": "field_uuid",
            "field_type": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b667c785-f9b6-49df-848f-44f8272b9144",
            "element": "field_uuid",
            "field_type": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is vsys or panorama-pushed, then panorama_vsys must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "21b45a1f-196c-452e-a207-4bc41ce6c403",
            "element": "field_uuid",
            "field_type": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is device-group, then panorama_device_group must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "930f37b7-b72f-4a0c-8135-b0b68efd82e2",
            "element": "field_uuid",
            "field_type": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_panorama_get_address_groups",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_71e6da2e-4ed7-41b7-a185-e12b6a8b5532",
        "id": 77,
        "name": "playbook_71e6da2e_4ed7_41b7_a185_e12b6a8b5532",
        "type": "playbook",
        "uuid": "5feb36d3-7a54-4a1c-a300-e6b0bd6cb675"
      },
      "tags": [],
      "type": "default",
      "uuid": "71e6da2e-4ed7-41b7-a185-e12b6a8b5532",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a79484f4_a987_452e_ac58_14ad2fec0392\" isExecutable=\"true\" name=\"playbook_a79484f4_a987_452e_ac58_14ad2fec0392\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_08zcvul\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Job Status\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1150149f-550c-4388-9f44-fd64b327197b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_job_id = getattr(playbook.inputs, \\\"panorama_job_id\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"panorama_job_status_return\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_08zcvul\u003c/incoming\u003e\u003coutgoing\u003eFlow_1wrwqr3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_08zcvul\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Panorama: Get Job Status results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"91ed51d2-4905-46ae-8193-eda6d9f56087\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1wrwqr3\u003c/incoming\u003e\u003coutgoing\u003eFlow_1a6jpsb\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1wrwqr3\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1a6jpsb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1a6jpsb\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a79484f4_a987_452e_ac58_14ad2fec0392\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1a6jpsb\" id=\"Flow_1a6jpsb_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1wrwqr3\" id=\"Flow_1wrwqr3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08zcvul\" id=\"Flow_08zcvul_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027819659,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
      "description": {
        "content": "Get status of a Panorama job from the job ID",
        "format": "text"
      },
      "display_name": "Panorama: Get Job Status - Example (PB)",
      "export_key": "panorama_get_job_status",
      "field_type_handle": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Get Job Status - Example (PB)",
        "export_key": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
        "fields": {
          "panorama_job_id": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392/panorama_job_id",
            "hide_notification": false,
            "id": 5264,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_job_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Job ID",
            "tooltip": "Job ID of Panorama job.",
            "type_id": 1085,
            "uuid": "b18d8bcb-d9c9-4078-97fc-7623bad0c23a",
            "values": []
          },
          "panorama_label": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392/panorama_label",
            "hide_notification": false,
            "id": 5265,
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
            "text": "Panorama label",
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1085,
            "uuid": "3f868773-3797-4135-b01b-9e68b1ca0a4f",
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
        "type_name": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
        "uuid": "61e8d7c3-15b3-4658-8d95-d30f0daa9484"
      },
      "has_logical_errors": false,
      "id": 71,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741190564097,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027820270,
          "description": "",
          "enabled": false,
          "export_key": "Panorama: Get Job Status results",
          "id": 84,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027820270,
          "name": "Panorama: Get Job Status results",
          "object_type": "incident",
          "playbook_handle": "panorama_get_job_status",
          "programmatic_name": "panorama_get_job_status_panorama_get_job_status_results",
          "script_text": "from json import dumps\nresults = playbook.functions.results.panorama_job_status_return\nif results.get(\"success\", None):\n  incident.addNote(f\"Panorama: Get Job Status results:\\n{dumps(results.get(\u0027content\u0027, {}), indent=4)}\")\nelse:\n  incident.addNote(f\"Panorama: Get Job Status failed with reason:\\n{results.get(\u0027reason\u0027, None)}\")",
          "tags": [],
          "uuid": "91ed51d2-4905-46ae-8193-eda6d9f56087"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "3f868773-3797-4135-b01b-9e68b1ca0a4f",
            "element": "field_uuid",
            "field_type": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b18d8bcb-d9c9-4078-97fc-7623bad0c23a",
            "element": "field_uuid",
            "field_type": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "panorama_get_job_status",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a79484f4-a987-452e-ac58-14ad2fec0392",
        "id": 73,
        "name": "playbook_a79484f4_a987_452e_ac58_14ad2fec0392",
        "type": "playbook",
        "uuid": "eb6d59c2-3f6a-429e-884d-8325bb1c6822"
      },
      "tags": [],
      "type": "default",
      "uuid": "a79484f4-a987-452e-ac58-14ad2fec0392",
      "version": 5
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 5,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\" isExecutable=\"true\" name=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0j8llco\u003c/outgoing\u003e\u003coutgoing\u003eFlow_18x1t2k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0j8llco\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kjeon9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_18x1t2k\u003c/incoming\u003e\u003coutgoing\u003eFlow_0nizk7z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0j8llco\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_18x1t2k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cparallelGateway id=\"CollectionPoint_3\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_0kjeon9\u003c/incoming\u003e\u003cincoming\u003eFlow_0nizk7z\u003c/incoming\u003e\u003coutgoing\u003eFlow_14pnrmv\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_0kjeon9\" sourceRef=\"ServiceTask_1\" targetRef=\"CollectionPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_0nizk7z\" sourceRef=\"ServiceTask_2\" targetRef=\"CollectionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"from json import dumps\\n\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ndns_name = \\\"\\\"\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\nif group:\\n  group = group[0]\\n\\naddresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\nfor address in addresses:\\n  if address.get(\\\"fqdn\\\") == artifact.value:\\n    dns_name = address.get(\\\"@name\\\")\\n    break\\n\\nif not dns_name:\\n  helper.fail(f\\\"The DNS address {artifact.value} was not found in the specified address group.\\\")\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\")\\n\\n# Remove IP address from list\\nmember_list.remove(dns_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\n# If using api version 9.0 or before uncomment below for the body\\n# body = {\\n#   \\\"entry\\\": {\\n#     \\\"@name\\\": group_name,\\n#     \\\"description\\\": des,\\n#     \\\"static\\\": {\\n#       \\\"member\\\": dumps(member_list)\\n#     }\\n#   }\\n# }\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": group_name,\\n    \\\"description\\\": des,\\n    \\\"static\\\": {\\n      \\\"member\\\": member_list\\n    }\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14pnrmv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1h25vm3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"Panorama unblock dns post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f627d5f0-ce59-44a1-891c-56dc2ff1b127\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wo3z0j\u003c/incoming\u003e\u003coutgoing\u003eFlow_020ypio\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_6\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_020ypio\u003c/incoming\u003e\u003cincoming\u003eFlow_01kk2m1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_020ypio\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_6\"/\u003e\u003csequenceFlow id=\"Flow_14pnrmv\" sourceRef=\"CollectionPoint_3\" targetRef=\"ServiceTask_4\"/\u003e\u003cexclusiveGateway default=\"Flow_0wo3z0j\" id=\"ConditionPoint_7\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1h25vm3\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wo3z0j\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0u095b8\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_1h25vm3\" sourceRef=\"ServiceTask_4\" targetRef=\"ConditionPoint_7\"/\u003e\u003cserviceTask id=\"ServiceTask_8\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0u095b8\u003c/incoming\u003e\u003coutgoing\u003eFlow_1mo8c8r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_9\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a353d64c-4155-476d-a29d-1d2f7309a2e6\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1mo8c8r\u003c/incoming\u003e\u003coutgoing\u003eFlow_01kk2m1\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1mo8c8r\" sourceRef=\"ServiceTask_8\" targetRef=\"ScriptTask_9\"/\u003e\u003csequenceFlow id=\"Flow_01kk2m1\" sourceRef=\"ScriptTask_9\" targetRef=\"EndPoint_6\"/\u003e\u003csequenceFlow id=\"Flow_0u095b8\" name=\"Successfully edited address\" sourceRef=\"ConditionPoint_7\" targetRef=\"ServiceTask_8\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Successfully edited address\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_addresses_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0wo3z0j\" name=\"Else\" sourceRef=\"ConditionPoint_7\" targetRef=\"ScriptTask_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e891e702_52bf_437a_bc61_af36c715b5e6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wo3z0j\" id=\"Flow_0wo3z0j_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"570\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"570\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"688\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"845\" y=\"623\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0u095b8\" id=\"Flow_0u095b8_di\"\u003e\u003comgdi:waypoint x=\"599\" y=\"570\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"570\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"688\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"75\" x=\"522\" y=\"576\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_01kk2m1\" id=\"Flow_01kk2m1_di\"\u003e\u003comgdi:waypoint x=\"510\" y=\"912\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"960\"/\u003e\u003comgdi:waypoint x=\"655\" y=\"960\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1mo8c8r\" id=\"Flow_1mo8c8r_di\"\u003e\u003comgdi:waypoint x=\"510\" y=\"772\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"828\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1h25vm3\" id=\"Flow_1h25vm3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"492\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"544\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14pnrmv\" id=\"Flow_14pnrmv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"356\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"408\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_020ypio\" id=\"Flow_020ypio_di\"\u003e\u003comgdi:waypoint x=\"870\" y=\"772\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"960\"/\u003e\u003comgdi:waypoint x=\"787\" y=\"960\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0nizk7z\" id=\"Flow_0nizk7z_di\"\u003e\u003comgdi:waypoint x=\"870\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"789\" y=\"330\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kjeon9\" id=\"Flow_0kjeon9_di\"\u003e\u003comgdi:waypoint x=\"570\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"330\"/\u003e\u003comgdi:waypoint x=\"652\" y=\"330\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18x1t2k\" id=\"Flow_18x1t2k_di\"\u003e\u003comgdi:waypoint x=\"811\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0j8llco\" id=\"Flow_0j8llco_di\"\u003e\u003comgdi:waypoint x=\"630\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"91\"/\u003e\u003comgdi:waypoint x=\"570\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"472\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"772\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_3\" id=\"CollectionPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"652\" y=\"304\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"408\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"772\" y=\"688\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_6\" id=\"EndPoint_6_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"934\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_7\" id=\"ConditionPoint_7_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"544\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_8\" id=\"ServiceTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"412\" y=\"688\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_9\" id=\"ScriptTask_9_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"412.25\" y=\"827.75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027821426,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
      "description": {
        "content": "Given a DNS Name artifact, removes the DNS Name from the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Panorama: Unblock DNS Name - Example (PB)",
      "export_key": "example_panorama_unblock_dns_name",
      "field_type_handle": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Unblock DNS Name - Example (PB)",
        "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
        "fields": {
          "panorama_device_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6/panorama_device_group",
            "hide_notification": false,
            "id": 5285,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "group1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Device Group",
            "tooltip": "Name of the device group to use",
            "type_id": 1086,
            "uuid": "9f2e4919-4cb6-47b0-8804-e156c7230f04",
            "values": []
          },
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
            "id": 5266,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1086,
            "uuid": "b12bd4dd-0be0-478e-bae4-7d26c94dd46c",
            "values": []
          },
          "panorama_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6/panorama_location",
            "hide_notification": false,
            "id": 5286,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_location",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Location",
            "tooltip": "",
            "type_id": 1086,
            "uuid": "aa6481ff-f020-4652-9d09-e05020db86e4",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "vsys",
                "properties": null,
                "uuid": "3801b030-eb51-4c0b-a617-f310a3629cc4",
                "value": 2312
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "panorama-pushed",
                "properties": null,
                "uuid": "2c730847-7db8-42b4-8708-c04efe4c317d",
                "value": 2313
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "shared",
                "properties": null,
                "uuid": "f3e1dc2d-f905-4312-89d0-07f56caf63d2",
                "value": 2314
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "device-group",
                "properties": null,
                "uuid": "fa1be619-6478-4089-9c8b-5a6a39acc454",
                "value": 2315
              }
            ]
          },
          "panorama_vsys": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6/panorama_vsys",
            "hide_notification": false,
            "id": 5287,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_vsys",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama vsys",
            "tooltip": "Name of the vsys to use",
            "type_id": 1086,
            "uuid": "0465a57d-70e8-4f2d-a7a6-2768b887de65",
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
      "id": 72,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741201677467,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027821987,
          "description": "",
          "enabled": false,
          "export_key": "Address does not exist",
          "id": 85,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027821987,
          "name": "Address does not exist",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_dns_name",
          "programmatic_name": "example_panorama_unblock_dns_name_address_does_not_exist",
          "script_text": "incident.addNote(f\"Address {} does not exist.\")",
          "tags": [],
          "uuid": "a88914d9-cee3-4bdf-930c-bca92a78c02e"
        },
        {
          "actions": [],
          "created_date": 1741027822090,
          "description": "",
          "enabled": false,
          "export_key": "Address group does not exist",
          "id": 86,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027822090,
          "name": "Address group does not exist",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_dns_name",
          "programmatic_name": "example_panorama_unblock_dns_name_address_group_does_not_exist",
          "script_text": "results = playbook.functions.results.get_groups_results\nincident.addNote(f\"The address group {results.get(\u0027inputs\u0027, {}).get(\u0027panorama_name_parameter\u0027)} does not exist.\")",
          "tags": [],
          "uuid": "e9568d33-03f1-45e8-8fde-e3297196a9a4"
        },
        {
          "actions": [],
          "created_date": 1741027822204,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 87,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027822204,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_dns_name",
          "programmatic_name": "example_panorama_unblock_dns_name_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_addresses = playbook.functions.results.edit_addresses_results\nif edit_addresses.get(\"success\"):\n  note += f\"Panorama DNS name: {artifact.value} was unblocked.\\n\"\nelse:\n  note += f\"Panorama Unblock DNS failed with reason: {edit_addresses.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "a353d64c-4155-476d-a29d-1d2f7309a2e6"
        },
        {
          "actions": [],
          "created_date": 1741027822329,
          "description": "",
          "enabled": false,
          "export_key": "Panorama unblock dns post-process",
          "id": 88,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027822329,
          "name": "Panorama unblock dns post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_dns_name",
          "programmatic_name": "example_panorama_unblock_dns_name_unblock_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_addresses_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama DNS name: {artifact.value} was unblocked.\")\nelse:\n  incident.addNote(f\"Panorama Unblock DNS failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "aa6481ff-f020-4652-9d09-e05020db86e4",
            "element": "field_uuid",
            "field_type": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is vsys or panorama-pushed, then panorama_vsys must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "0465a57d-70e8-4f2d-a7a6-2768b887de65",
            "element": "field_uuid",
            "field_type": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is device-group, then panorama_device_group must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "9f2e4919-4cb6-47b0-8804-e156c7230f04",
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
        "id": 74,
        "name": "playbook_e891e702_52bf_437a_bc61_af36c715b5e6",
        "type": "playbook",
        "uuid": "bfa7e49f-9da4-46d2-8883-5f66792b0418"
      },
      "tags": [],
      "type": "default",
      "uuid": "e891e702-52bf-437a-bc61-af36c715b5e6",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\" isExecutable=\"true\" name=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0xjlnoc\u003c/outgoing\u003e\u003coutgoing\u003eFlow_02808cp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Edit Address Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8336bd1-1a63-4662-9b04-eb74e9de7510\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"a6a5a64c-8040-4d70-9213-96450e05f87e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"from json import dumps\\n\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nip_address_name = artifact.value\\ngroup = playbook.functions.results.get_groups_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])[0]\\naddresses = playbook.functions.results.get_addresses_results.get(\\\"content\\\", {}).get(\\\"result\\\", {}).get(\\\"entry\\\", [])\\n\\ngroup_name = group.get(\\\"@name\\\")\\ndes = group.get(\\\"description\\\")\\n\\nmember_list = group.get(\\\"static\\\", {}).get(\\\"member\\\")\\n\\n# Remove IP address from list if it\u0027s present\\nif ip_address_name in member_list:\\n  member_list.remove(ip_address_name)\\n\\ninputs.panorama_name_parameter = group_name\\n\\n# If using api version 9.0 or under uncomment the below to use as the body\\n# body = {\\n#   \\\"entry\\\": {\\n#     \\\"@name\\\": group_name,\\n#     \\\"description\\\": des,\\n#     \\\"static\\\": {\\n#       \\\"member\\\": dumps(member_list)\\n#     }\\n#   }\\n# }\\n\\nbody = {\\n  \\\"entry\\\": {\\n    \\\"@name\\\": group_name,\\n    \\\"description\\\": des,\\n    \\\"static\\\": {\\n      \\\"member\\\": member_list\\n    }\\n  }\\n}\\n\\ninputs.panorama_request_body = dumps(body)\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_082glnv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1kl9der\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Get Addresses\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50a9c249-ffaa-4280-92ff-4d5c9eca94cc\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_addresses_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_02808cp\u003c/incoming\u003e\u003coutgoing\u003eFlow_08eabn0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Panorama Get Address Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4b233153-426e-456d-83cd-c133c6e05429\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"c9f1bf5e-1c78-440a-bbe2-a373610200cf\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fb0e735b-6a43-461a-87a2-893edc92d24f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\\nif inputs.panorama_location in [\\\"vsys\\\", \\\"panorama-pushed\\\"]:\\n  if getattr(playbook.inputs, \\\"panorama_vsys\\\", None):\\n    inputs.panorama_vsys = getattr(playbook.inputs, \\\"panorama_vsys\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals vsys or panorama-pushed, then panorama_vsys must be given.\\\")\\nif inputs.panorama_location == \\\"device-group\\\":\\n  # If `panorama_location` equals \u0027device-group\u0027 then set `panorama_device_group`\\n  if getattr(playbook.inputs, \\\"panorama_device_group\\\", None):\\n    inputs.panorama_device_group = getattr(playbook.inputs, \\\"panorama_device_group\\\", None)\\n  else:\\n    helper.fail(\\\"If panorama_location equals device-group, then panorama_device_group must be given.\\\")\\n\\ninputs.panorama_name_parameter = \\\"Blocked Group\\\"\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0xjlnoc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ulvawt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cparallelGateway id=\"CollectionPoint_4\" resilient:documentation=\"Wait point\"\u003e\u003cincoming\u003eFlow_0ulvawt\u003c/incoming\u003e\u003cincoming\u003eFlow_08eabn0\u003c/incoming\u003e\u003coutgoing\u003eFlow_082glnv\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003csequenceFlow id=\"Flow_0ulvawt\" sourceRef=\"ServiceTask_3\" targetRef=\"CollectionPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_08eabn0\" sourceRef=\"ServiceTask_2\" targetRef=\"CollectionPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_082glnv\" sourceRef=\"CollectionPoint_4\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0xjlnoc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_3\"/\u003e\u003csequenceFlow id=\"Flow_02808cp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_2\"/\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"Panorama unblock ip post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8b544819-af40-4a0e-a324-631279825f49\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0peny83\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jz8otw\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_6\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jz8otw\u003c/incoming\u003e\u003cincoming\u003eFlow_1nun2jl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jz8otw\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_6\"/\u003e\u003cexclusiveGateway default=\"Flow_0peny83\" id=\"ConditionPoint_7\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1kl9der\u003c/incoming\u003e\u003coutgoing\u003eFlow_0peny83\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1mdkvzq\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_1kl9der\" sourceRef=\"ServiceTask_1\" targetRef=\"ConditionPoint_7\"/\u003e\u003cserviceTask id=\"ServiceTask_8\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\nif getattr(playbook.inputs, \\\"panorama_location\\\", None):\\n  inputs.panorama_location = getattr(playbook.inputs, \\\"panorama_location\\\", None)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1mdkvzq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1eleyfi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_9\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"271022e9-cb48-4229-8fc2-a2b29594fbed\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1eleyfi\u003c/incoming\u003e\u003coutgoing\u003eFlow_1nun2jl\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1eleyfi\" sourceRef=\"ServiceTask_8\" targetRef=\"ScriptTask_9\"/\u003e\u003csequenceFlow id=\"Flow_1nun2jl\" sourceRef=\"ScriptTask_9\" targetRef=\"EndPoint_6\"/\u003e\u003csequenceFlow id=\"Flow_1mdkvzq\" name=\"Successfully edited addresses\" sourceRef=\"ConditionPoint_7\" targetRef=\"ServiceTask_8\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Successfully edited addresses\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_addresses_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0peny83\" name=\"Else\" sourceRef=\"ConditionPoint_7\" targetRef=\"ScriptTask_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0peny83\" id=\"Flow_0peny83_di\"\u003e\u003comgdi:waypoint x=\"1462\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1540\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1540\" y=\"818\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"1498\" y=\"713\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1mdkvzq\" id=\"Flow_1mdkvzq_di\"\u003e\u003comgdi:waypoint x=\"1218\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1070\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"1070\" y=\"818\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"87\" x=\"1084\" y=\"716\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nun2jl\" id=\"Flow_1nun2jl_di\"\u003e\u003comgdi:waypoint x=\"1070\" y=\"1062\"/\u003e\u003comgdi:waypoint x=\"1070\" y=\"1110\"/\u003e\u003comgdi:waypoint x=\"1274\" y=\"1110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1eleyfi\" id=\"Flow_1eleyfi_di\"\u003e\u003comgdi:waypoint x=\"1070\" y=\"902\"/\u003e\u003comgdi:waypoint x=\"1070\" y=\"978\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1kl9der\" id=\"Flow_1kl9der_di\"\u003e\u003comgdi:waypoint x=\"1340\" y=\"652\"/\u003e\u003comgdi:waypoint x=\"1340\" y=\"684\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jz8otw\" id=\"Flow_0jz8otw_di\"\u003e\u003comgdi:waypoint x=\"1540\" y=\"902\"/\u003e\u003comgdi:waypoint x=\"1540\" y=\"1110\"/\u003e\u003comgdi:waypoint x=\"1406\" y=\"1110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_02808cp\" id=\"Flow_02808cp_di\"\u003e\u003comgdi:waypoint x=\"1430\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"268\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xjlnoc\" id=\"Flow_0xjlnoc_di\"\u003e\u003comgdi:waypoint x=\"1249\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"268\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_082glnv\" id=\"Flow_082glnv_di\"\u003e\u003comgdi:waypoint x=\"1340\" y=\"486\"/\u003e\u003comgdi:waypoint x=\"1340\" y=\"568\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08eabn0\" id=\"Flow_08eabn0_di\"\u003e\u003comgdi:waypoint x=\"1490\" y=\"352\"/\u003e\u003comgdi:waypoint x=\"1490\" y=\"460\"/\u003e\u003comgdi:waypoint x=\"1408\" y=\"460\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ulvawt\" id=\"Flow_0ulvawt_di\"\u003e\u003comgdi:waypoint x=\"1190\" y=\"352\"/\u003e\u003comgdi:waypoint x=\"1190\" y=\"460\"/\u003e\u003comgdi:waypoint x=\"1271\" y=\"460\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"1249\" y=\"154\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1242\" y=\"568\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1392\" y=\"268\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1092\" y=\"268\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"CollectionPoint_4\" id=\"CollectionPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"137.13330000000002\" x=\"1271\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1442\" y=\"818\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_6\" id=\"EndPoint_6_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1274\" y=\"1084\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_7\" id=\"ConditionPoint_7_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"1218\" y=\"684\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_8\" id=\"ServiceTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"972\" y=\"818\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_9\" id=\"ScriptTask_9_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"971.75\" y=\"977.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027824161,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
      "description": {
        "content": "Given an IP Address artifact, removes the IP Address from the \"Blocked Group\" in Panorama.",
        "format": "text"
      },
      "display_name": "Panorama: Unblock IP Address - Example (PB)",
      "export_key": "example_panorama_unblock_ip_address",
      "field_type_handle": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Unblock IP Address - Example (PB)",
        "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
        "fields": {
          "panorama_device_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c/panorama_device_group",
            "hide_notification": false,
            "id": 5288,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_device_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "group1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Device Group",
            "tooltip": "Name of the device group to use",
            "type_id": 1087,
            "uuid": "270d60fd-42c0-4084-a892-8ff238bb623a",
            "values": []
          },
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
            "id": 5267,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1087,
            "uuid": "1c91feb8-07f0-415d-8183-c39a547c27c3",
            "values": []
          },
          "panorama_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c/panorama_location",
            "hide_notification": false,
            "id": 5289,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_location",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Location",
            "tooltip": "Panorama location to use",
            "type_id": 1087,
            "uuid": "5d29a34c-13b6-43fa-8f58-7c0da604c646",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "vsys",
                "properties": null,
                "uuid": "e0c3d88c-a60e-4724-889e-d4f81a4730c0",
                "value": 2316
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "panorama-pushed",
                "properties": null,
                "uuid": "3cb07e8d-e134-41d0-b1b8-b8509541c985",
                "value": 2317
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "shared",
                "properties": null,
                "uuid": "b800bb0b-4654-40f4-8baa-757abe41ad81",
                "value": 2318
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "device-group",
                "properties": null,
                "uuid": "a7c7ca4a-4763-487d-98c0-245b6a3fa4cc",
                "value": 2319
              }
            ]
          },
          "panorama_vsys": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c/panorama_vsys",
            "hide_notification": false,
            "id": 5290,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_vsys",
            "operation_perms": {},
            "operations": [],
            "placeholder": "vsys1",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama vsys",
            "tooltip": "Name of the vsys to use",
            "type_id": 1087,
            "uuid": "7a89f1e4-8251-45cc-b5b5-fa540c7e47c1",
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
      "id": 73,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741201841097,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027824754,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 89,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027824754,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_ip_address",
          "programmatic_name": "example_panorama_unblock_ip_address_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_addresses = playbook.functions.results.edit_addresses_results\nif edit_addresses.get(\"success\"):\n  note += f\"Panorama IP Address: {artifact.value} was unblocked.\\n\"\nelse:\n  note += f\"Panorama Unblock IP address failed with reason: {edit_addresses.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "271022e9-cb48-4229-8fc2-a2b29594fbed"
        },
        {
          "actions": [],
          "created_date": 1741027824836,
          "description": "",
          "enabled": false,
          "export_key": "Panorama unblock ip post-process",
          "id": 90,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027824836,
          "name": "Panorama unblock ip post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_ip_address",
          "programmatic_name": "example_panorama_unblock_ip_address_unblock_ip_post_process",
          "script_text": "results = playbook.functions.results.edit_addresses_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama IP Address: {artifact.value} was unblocked.\")\nelse:\n  incident.addNote(f\"Panorama Unblock IP address failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "5d29a34c-13b6-43fa-8f58-7c0da604c646",
            "element": "field_uuid",
            "field_type": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is vsys or panorama-pushed, then panorama_vsys must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "7a89f1e4-8251-45cc-b5b5-fa540c7e47c1",
            "element": "field_uuid",
            "field_type": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "If panorama_location is device-group, then panorama_device_group must be given.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "270d60fd-42c0-4084-a892-8ff238bb623a",
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
        "id": 75,
        "name": "playbook_14264b30_9bed_4985_b6ce_cd34dd996b9c",
        "type": "playbook",
        "uuid": "9e587e05-f0b2-4c3b-a0c2-b82a23821420"
      },
      "tags": [],
      "type": "default",
      "uuid": "14264b30-9bed-4985-b6ce-cd34dd996b9c",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\" isExecutable=\"true\" name=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1g1nlkh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Panorama Get Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"85a6dc33-8f88-4bb5-9e21-3daa253d4a6c\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# Set this to the xpath of the group you are interested in\\nif getattr(playbook.inputs, \\\"panorama_template\\\", None):\\n  inputs.panorama_user_group_xpath = f\\\"/config/devices/entry[@name=\u0027localhost.localdomain\u0027]/template/entry[@name=\u0027{playbook.inputs.panorama_template}\u0027]/config/shared/local-user-database/user-group/entry[@name=\u0027Blocked_Users\u0027]\\\"\\n\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_location = \\\"shared\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1g1nlkh\u003c/incoming\u003e\u003coutgoing\u003eFlow_07lm4lf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Panorama Edit Users in a Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e89ee2fa-3983-417e-9e69-f8a5ac9961cd\"\u003e{\"inputs\":{\"e9aa03fe-166f-4ebc-b783-0bfa367a963b\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"799cc50b-a9b9-445f-8037-efd936b3cfee\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"4c33528f-e008-4d22-9787-28f864c7456e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"d3a29851-1be8-4c24-ad15-34e247fdbf9d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"inputs.panorama_location = \\\"shared\\\"\\n# Set this to the name of the user group you wish to add a user to\\ngroup_name = \\\"Blocked_Users\\\"\\n\\n# Set this to the xpath of the group you are interested in\\nif getattr(playbook.inputs, \\\"panorama_template\\\", None):\\n  inputs.panorama_user_group_xpath = f\\\"/config/devices/entry[@name=\u0027localhost.localdomain\u0027]/template/entry[@name=\u0027{playbook.inputs.panorama_template}\u0027]/config/shared/local-user-database/user-group/entry[@name=\u0027{group_name}\u0027]\\\"\\n\\nusers_list = playbook.functions.results.get_users_results.get(\\\"content\\\", {}).get(\\\"user_list\\\", [])\\n\\nblocked_users = users_list.copy()\\n\\n# Remove the user from the blocked list if they are there\\nif artifact.value in blocked_users:\\n  blocked_users.remove(artifact.value)\\nelse:\\n  helper.fail(f\\\"The Panorama user(s): {artifact.value} is not found in the group: {group_name} and can not be removed from it.\\\")\\n\\n# Updated function creates the xml request body for you\\ninputs.panorama_users_list = str(blocked_users)\\ninputs.panorama_user_group_name = group_name\\nif getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\n\\n# Giving the xml request body as an input still works\\n# panorama_xml = \\\"\\\"\\n# # Set xml to empty users if list is empty\\n# if len(users_list) == 0:\\n#   panorama_xml = f\u0027\u0026lt;entry name=\\\"{group_name}\\\"/\u0026gt;\u0027\\n\\n# # Multiple members, build xml which the function will send to Panorama\\n# else:\\n#   panorama_xml = f\\\"\u0026lt;entry name=\u0027{group_name}\u0027\u0026gt;\u0026lt;user\u0026gt;\\\"\\n\\n#   # Add member nodes with the username to the xml string\\n#   for user in blocked_users:\\n#     panorama_xml += f\\\"\u0026lt;member\u0026gt;{user}\u0026lt;/member\u0026gt;\\\"\\n\\n#   # Add the ending of the xml to the string\\n#   panorama_xml += \\\"\u0026lt;/user\u0026gt;\u0026lt;/entry\u0026gt;\\\"\\n\\n# inputs.panorama_user_group_xml = panorama_xml\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"edit_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_07lm4lf\u003c/incoming\u003e\u003coutgoing\u003eFlow_0j7s4kd\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Panorama unblock user post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"0faec4e9-f36a-4891-ae4d-c1d3be2da800\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0v7zuwj\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kog3tg\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1g1nlkh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_07lm4lf\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0kog3tg\u003c/incoming\u003e\u003cincoming\u003eFlow_1q4casg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0kog3tg\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_4\"/\u003e\u003cexclusiveGateway default=\"Flow_0v7zuwj\" id=\"ConditionPoint_5\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0j7s4kd\u003c/incoming\u003e\u003coutgoing\u003eFlow_0v7zuwj\u003c/outgoing\u003e\u003coutgoing\u003eFlow_08g4d7e\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0j7s4kd\" sourceRef=\"ServiceTask_2\" targetRef=\"ConditionPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"Panorama Commit\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"938412d2-1552-4d55-a8e0-234fc73f959b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if getattr(playbook.inputs, \\\"panorama_label\\\", None):\\n  inputs.panorama_label = getattr(playbook.inputs, \\\"panorama_label\\\", None)\\ninputs.panorama_location = \\\"shared\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"commit_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_08g4d7e\u003c/incoming\u003e\u003coutgoing\u003eFlow_0qxwdkj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_7\" name=\"commit output\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"4cbaf628-8341-4a7e-b68a-5bd297546257\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qxwdkj\u003c/incoming\u003e\u003coutgoing\u003eFlow_1q4casg\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0qxwdkj\" sourceRef=\"ServiceTask_6\" targetRef=\"ScriptTask_7\"/\u003e\u003csequenceFlow id=\"Flow_1q4casg\" sourceRef=\"ScriptTask_7\" targetRef=\"EndPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_08g4d7e\" name=\"Successfully edited users\" sourceRef=\"ConditionPoint_5\" targetRef=\"ServiceTask_6\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Successfully edited users\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = True if playbook.functions.results.edit_users_results.get(\\\"success\\\") else False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0v7zuwj\" name=\"Else\" sourceRef=\"ConditionPoint_5\" targetRef=\"ScriptTask_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0v7zuwj\" id=\"Flow_0v7zuwj_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"470\"/\u003e\u003comgdi:waypoint x=\"1000\" y=\"470\"/\u003e\u003comgdi:waypoint x=\"1000\" y=\"538\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"922\" y=\"448\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08g4d7e\" id=\"Flow_08g4d7e_di\"\u003e\u003comgdi:waypoint x=\"599\" y=\"470\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"470\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"568\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"67\" x=\"456\" y=\"476\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1q4casg\" id=\"Flow_1q4casg_di\"\u003e\u003comgdi:waypoint x=\"440\" y=\"822\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"655\" y=\"870\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qxwdkj\" id=\"Flow_0qxwdkj_di\"\u003e\u003comgdi:waypoint x=\"440\" y=\"652\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"738\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0j7s4kd\" id=\"Flow_0j7s4kd_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kog3tg\" id=\"Flow_0kog3tg_di\"\u003e\u003comgdi:waypoint x=\"1000\" y=\"622\"/\u003e\u003comgdi:waypoint x=\"1000\" y=\"870\"/\u003e\u003comgdi:waypoint x=\"787\" y=\"870\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_07lm4lf\" id=\"Flow_07lm4lf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1g1nlkh\" id=\"Flow_1g1nlkh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"902\" y=\"538\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"844\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_5\" id=\"ConditionPoint_5_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"342\" y=\"568\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_7\" id=\"ScriptTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"342\" y=\"737.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1741027826315,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
      "description": {
        "content": "Given a User Account artifact, removes the user from the \"Blocked_Users\" group in Panorama. This only works with Panorama and does not work with PanOS.",
        "format": "text"
      },
      "display_name": "Panorama: Unblock User - Example (PB)",
      "export_key": "example_panorama_unblock_user",
      "field_type_handle": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
      "fields_type": {
        "actions": [],
        "display_name": "Panorama: Unblock User - Example (PB)",
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
            "id": 5268,
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
            "tooltip": "Label given to the server to use. Only needed if configured in app.config.",
            "type_id": 1088,
            "uuid": "1ed52467-249c-4ce0-bbba-d27a488e8abe",
            "values": []
          },
          "panorama_template": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90/panorama_template",
            "hide_notification": false,
            "id": 5291,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "panorama_template",
            "operation_perms": {},
            "operations": [],
            "placeholder": "temp1",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Panorama Template",
            "tooltip": "Name of the Panorama template to use",
            "type_id": 1088,
            "uuid": "c43ef18e-4ccb-4ced-a390-f70e23f12a2d",
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
      "id": 74,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 32,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1741203994709,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1741027826826,
          "description": "",
          "enabled": false,
          "export_key": "commit output",
          "id": 91,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027826826,
          "name": "commit output",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_user",
          "programmatic_name": "example_panorama_unblock_user_commit_output",
          "script_text": "note = \"\"\nresults = playbook.functions.results.commit_output\nedit_user = playbook.functions.results.edit_users_results\nif edit_user.get(\"success\"):\n  note += f\"Panorama User account: {artifact.value} was unblocked.\\n\"\nelse:\n  note += f\"Panorama Unblock User failed with reason: {edit_user.get(\u0027reason\u0027)}\\n\"\n\nif results.get(\"success\"):\n  note += str(results.get(\"content\", {}).get(\"result\", {}).get(\"msg\", {}).get(\"line\"))\n\nincident.addNote(note)",
          "tags": [],
          "uuid": "4cbaf628-8341-4a7e-b68a-5bd297546257"
        },
        {
          "actions": [],
          "created_date": 1741027826912,
          "description": "",
          "enabled": false,
          "export_key": "Panorama unblock user post-process",
          "id": 92,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1741027826912,
          "name": "Panorama unblock user post-process",
          "object_type": "artifact",
          "playbook_handle": "example_panorama_unblock_user",
          "programmatic_name": "example_panorama_unblock_user_unblock_user_post_process",
          "script_text": "results = playbook.functions.results.edit_users_results\nif results.get(\"success\"):\n  incident.addNote(f\"Panorama User account: {artifact.value} was unblocked.\")\nelse:\n  incident.addNote(f\"Panorama Unblock User failed with reason: {results.get(\u0027reason\u0027)}\")",
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
          },
          {
            "content": "c43ef18e-4ccb-4ced-a390-f70e23f12a2d",
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
        "id": 76,
        "name": "playbook_68dd2c77_47b7_479a_ae1e_f5cb0cebce90",
        "type": "playbook",
        "uuid": "e4b0058e-6552-4db2-b1a0-f30abdea151e"
      },
      "tags": [],
      "type": "default",
      "uuid": "68dd2c77-47b7-479a-ae1e-f5cb0cebce90",
      "version": 11
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
