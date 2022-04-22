{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Add User(s) to Group(s)",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Add User(s) to Group(s)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1d8ef10c-e543-4373-986f-a612ba05eafe",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_add_users_to_groups"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Remove User(s) from Group(s)",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Remove User(s) from Group(s)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7a8a2d1d-0174-449a-8461-ef6116002b65",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_remove_user_from_groups"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Recipient"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Sender"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Search",
      "id": 30,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Search",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a1a5f8ce-c5ee-4675-bc52-cf50ce349808",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_search"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Recipient"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Sender"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Set Password",
      "id": 31,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Set Password",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0d0d491b-5a6a-40f7-858b-3833f52e6c1c",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_set_password"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Recipient"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Sender"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Toggle Access",
      "id": 32,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Toggle Access",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8d314ba0-70e6-4054-978a-e3ad97a6324d",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_toggle_access"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Recipient"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Sender"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: LDAP Utilities: Update",
      "id": 33,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: LDAP Utilities: Update",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "656aa9e0-3939-43fc-9ee5-abdfe8467d27",
      "view_items": [],
      "workflows": [
        "example_ldap_utilities_update"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1650636319652,
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
      "export_key": "__function/ldap_new_auto_password_len",
      "hide_notification": false,
      "id": 319,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_new_auto_password_len",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_new_auto_password_len",
      "tooltip": "Length of password to generate",
      "type_id": 11,
      "uuid": "91b1cdc7-457b-4c8b-8f35-b9faffcb8c6d",
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
      "export_key": "__function/ldap_search_filter",
      "hide_notification": false,
      "id": 302,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_search_filter",
      "tooltip": "The filter of the LDAP search request",
      "type_id": 11,
      "uuid": "a550e011-318e-4b7c-a4ee-7ec011ee0447",
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
      "export_key": "__function/ldap_toggle_access",
      "hide_notification": false,
      "id": 304,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_toggle_access",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_toggle_access",
      "tooltip": "Either enable or disable the user",
      "type_id": 11,
      "uuid": "aa0f6b18-30f9-4e15-ac83-9fce34525947",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Enable",
          "properties": null,
          "uuid": "a9a1571e-b734-4cbe-84d7-277ce397c0de",
          "value": 102
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Disable",
          "properties": null,
          "uuid": "938bd462-d9e0-4887-8ef1-670120e419ad",
          "value": 103
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
      "export_key": "__function/ldap_attribute_name",
      "hide_notification": false,
      "id": 303,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_attribute_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_attribute_name",
      "tooltip": "The name of the LDAP attribute",
      "type_id": 11,
      "uuid": "ad229bf3-14fe-4f0d-aae1-ee339da733dc",
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
      "export_key": "__function/ldap_search_param",
      "hide_notification": false,
      "id": 300,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_search_param",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_search_param",
      "tooltip": "Parameter used in search filter",
      "type_id": 11,
      "uuid": "b85e3696-97b0-48b3-a7d6-b72728b11f45",
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
      "export_key": "__function/ldap_attribute_values",
      "hide_notification": false,
      "id": 296,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_attribute_values",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"[\u0027value1\u0027, \u0027value2\u0027, \u0027value3\u0027]\"",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_attribute_values",
      "tooltip": "List (as a string representation) of the new attribute values",
      "type_id": 11,
      "uuid": "bec44d02-2902-4619-a3ad-c5fe9fb9231c",
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
      "export_key": "__function/ldap_domain_name",
      "hide_notification": false,
      "id": 318,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_domain_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_domain_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
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
      "export_key": "__function/ldap_dn",
      "hide_notification": false,
      "id": 306,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_dn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_dn",
      "tooltip": "Distinguished Name of entry you want to access",
      "type_id": 11,
      "uuid": "c276dce4-c3c6-420e-8430-85ba7e388cf8",
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
      "export_key": "__function/ldap_return_new_password",
      "hide_notification": false,
      "id": 320,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_return_new_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_return_new_password",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c886d097-52d8-4281-a68a-988496f28d11",
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
      "export_key": "__function/ldap_search_attributes",
      "hide_notification": false,
      "id": 301,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_search_attributes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_search_attributes",
      "tooltip": "A single attribute or a list of attributes to be returned by the LDAP search ",
      "type_id": 11,
      "uuid": "d449aa53-20e8-4af0-bb61-525f4208b07b",
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
      "export_key": "__function/ldap_multiple_group_dn",
      "hide_notification": false,
      "id": 305,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_multiple_group_dn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"[\u0027dn=Accounts Group,dc=example,dc=com\u0027, \u0027dn=IT Group,dc=example,dc=com\u0027]\"",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_multiple_group_dn",
      "tooltip": "List (represented as a string) of each DN of the related groups",
      "type_id": 11,
      "uuid": "d862b2fe-1199-43d2-86ec-cff4b45e01f3",
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
      "export_key": "__function/ldap_search_base",
      "hide_notification": false,
      "id": 297,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_search_base",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_search_base",
      "tooltip": "The base of the LDAP search request.",
      "type_id": 11,
      "uuid": "e72e469e-342e-4ef9-8863-d84dee27758a",
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
      "export_key": "__function/ldap_new_password",
      "hide_notification": false,
      "id": 298,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_new_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_new_password",
      "tooltip": "The new password you want to set for the entry",
      "type_id": 11,
      "uuid": "ed5de6d6-1e81-4774-ab3a-033b05b2efc8",
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
      "export_key": "__function/ldap_multiple_user_dn",
      "hide_notification": false,
      "id": 299,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ldap_multiple_user_dn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"[\u0027dn=tom smith,dc=example,dc=com\u0027, \u0027dn=ted smith,dc=example,dc=com\u0027]\"",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ldap_multiple_user_dn",
      "tooltip": "List (represented as a string) of each DN of the users",
      "type_id": 11,
      "uuid": "463e020a-d36c-46d8-bcb5-dbd4d950b09d",
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
      "created_date": 1649688520744,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function that allows adding multiple users to multiple groups",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Add to Group(s)",
      "export_key": "ldap_utilities_add_to_groups",
      "id": 10,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649942917284,
      "name": "ldap_utilities_add_to_groups",
      "tags": [],
      "uuid": "b602d316-c3b6-4b36-8813-eb81fd381bba",
      "version": 3,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "463e020a-d36c-46d8-bcb5-dbd4d950b09d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d862b2fe-1199-43d2-86ec-cff4b45e01f3",
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
          "name": "Example: LDAP Utilities: Add User(s) to Group(s)",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_add_users_to_groups",
          "tags": [],
          "uuid": null,
          "workflow_id": 15
        }
      ]
    },
    {
      "created_date": 1649688520812,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function that allows you to remove multiple from multiple groups",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Remove from Group(s)",
      "export_key": "ldap_utilities_remove_from_groups",
      "id": 11,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649942924056,
      "name": "ldap_utilities_remove_from_groups",
      "tags": [],
      "uuid": "9ba21139-a5f0-4710-983d-83190f4bdc6c",
      "version": 3,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "463e020a-d36c-46d8-bcb5-dbd4d950b09d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d862b2fe-1199-43d2-86ec-cff4b45e01f3",
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
          "name": "Example: LDAP Utilities: Remove User(s) from Group(s)",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_remove_user_from_groups",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1649688520892,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "SOAR Function to do a search or query against an LDAP server.",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Search",
      "export_key": "ldap_utilities_search",
      "id": 12,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649948893941,
      "name": "ldap_utilities_search",
      "tags": [],
      "uuid": "892075c1-64ba-46c9-aba1-f1f1aa040bb7",
      "version": 4,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e72e469e-342e-4ef9-8863-d84dee27758a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a550e011-318e-4b7c-a4ee-7ec011ee0447",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d449aa53-20e8-4af0-bb61-525f4208b07b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b85e3696-97b0-48b3-a7d6-b72728b11f45",
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
          "name": "Example: LDAP Utilities: Search",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 20
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: LDAP Utilities: Set Password",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_set_password",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: LDAP Utilities: Toggle Access",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_toggle_access",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: LDAP Utilities: Update",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_update",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1649688520985,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function that allows you to set a new password for an LDAP entry given the entry\u0027s DN",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Set Password",
      "export_key": "ldap_utilities_set_password",
      "id": 13,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1650285186916,
      "name": "ldap_utilities_set_password",
      "tags": [],
      "uuid": "b75c2ee2-759b-4d01-9649-6ec46f6a646e",
      "version": 4,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c276dce4-c3c6-420e-8430-85ba7e388cf8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed5de6d6-1e81-4774-ab3a-033b05b2efc8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "91b1cdc7-457b-4c8b-8f35-b9faffcb8c6d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c886d097-52d8-4281-a68a-988496f28d11",
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
          "name": "Example: LDAP Utilities: Set Password",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_set_password",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1649688521052,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function that allows an LDAP user, with the correct privileges to enable or disable another account given their DN",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Toggle Access",
      "export_key": "ldap_utilities_toggle_access",
      "id": 14,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649942460373,
      "name": "ldap_utilities_toggle_access",
      "tags": [],
      "uuid": "b912c17d-5be2-4dfa-9c8d-2d2b5d9abb08",
      "version": 3,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c276dce4-c3c6-420e-8430-85ba7e388cf8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa0f6b18-30f9-4e15-ac83-9fce34525947",
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
          "name": "Example: LDAP Utilities: Toggle Access",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_toggle_access",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        }
      ]
    },
    {
      "created_date": 1649688521117,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function that updates the attribute of a DN with a new value",
        "format": "text"
      },
      "destination_handle": "fn_ldap_utilities",
      "display_name": "LDAP Utilities: Update",
      "export_key": "ldap_utilities_update",
      "id": 15,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1649942451995,
      "name": "ldap_utilities_update",
      "tags": [],
      "uuid": "dfe0fab8-c425-48fc-95ab-a23f722f77bc",
      "version": 3,
      "view_items": [
        {
          "content": "bf1fbfd3-3b2d-4919-a4e2-0a22449d0921",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c276dce4-c3c6-420e-8430-85ba7e388cf8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ad229bf3-14fe-4f0d-aae1-ee339da733dc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bec44d02-2902-4619-a3ad-c5fe9fb9231c",
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
          "name": "Example: LDAP Utilities: Update",
          "object_type": "artifact",
          "programmatic_name": "example_ldap_utilities_update",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 26,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1650636318411,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1650636318411,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_ldap_utilities",
      "name": "fn_ldap_utilities",
      "programmatic_name": "fn_ldap_utilities",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "253d5df1-2f84-4be2-97cb-1c43cada5a32"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6783,
    "major": 41,
    "minor": 0,
    "version": "41.0.6783"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "LDAP Query results",
      "export_key": "ldap_query_results",
      "fields": {
        "email_address": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "ldap_query_results/email_address",
          "hide_notification": false,
          "id": 291,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "email_address",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Email address",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "398592cb-4d52-473e-926f-32c7d12ca11c",
          "values": [],
          "width": 132
        },
        "fullname": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "ldap_query_results/fullname",
          "hide_notification": false,
          "id": 292,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "fullname",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Fullname",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "b469d0fe-ab32-4100-bba5-9d40212fd127",
          "values": [],
          "width": 113
        },
        "surname": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "ldap_query_results/surname",
          "hide_notification": false,
          "id": 293,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "surname",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Surname",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "595f9641-46c6-485d-8005-8af98eb2a96c",
          "values": [],
          "width": 113
        },
        "telephone_number": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "ldap_query_results/telephone_number",
          "hide_notification": false,
          "id": 294,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "telephone_number",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Telephone Number",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "26e46025-166c-4505-a051-dee46e16df98",
          "values": [],
          "width": 172
        },
        "uid": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "ldap_query_results/uid",
          "hide_notification": false,
          "id": 295,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "uid",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "UID",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "94595e20-41c8-4e37-adff-70e949aa8ddc",
          "values": [],
          "width": 113
        }
      },
      "for_actions": false,
      "for_custom_fields": false,
      "for_notifications": false,
      "for_workflows": false,
      "id": null,
      "parent_types": [
        "incident"
      ],
      "properties": {
        "can_create": false,
        "can_destroy": false,
        "for_who": []
      },
      "scripts": [],
      "tags": [],
      "type_id": 8,
      "type_name": "ldap_query_results",
      "uuid": "edf0fcb2-77d3-433d-8143-10588b6a3948"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "example_ldap_utilities_toggle_access",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_toggle_access\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Toggle Access\"\u003e\u003cdocumentation\u003eAn example workflow showing how to enable/disable an Active Directory user account\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0zt8blr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_19rq2c5\"\u003e\u003cincoming\u003eSequenceFlow_1dijgsh\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_04m0elt\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1qhd998\" name=\"LDAP Utilities: Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"892075c1-64ba-46c9-aba1-f1f1aa040bb7\"\u003e{\"inputs\":{},\"post_processing_script\":\"# No post-processing script here as output being passed into next function\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Set the ldap_search_base and ldap_search_filter\\n# using the ldap_param wildcard then get the email\\n# address the user you want to toggle access for from the artifact\u0027s value\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_search_base = \\\"dc=example,dc=com\\\"\\ninputs.ldap_search_filter = \\\"(\u0026amp;(mail=%ldap_param%))\\\"\\ninputs.ldap_search_param =  artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"search_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zt8blr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_00cs355\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zt8blr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qhd998\"/\u003e\u003cserviceTask id=\"ServiceTask_0be768x\" name=\"LDAP Utilities: Toggle Access\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b912c17d-5be2-4dfa-9c8d-2d2b5d9abb08\"\u003e{\"inputs\":{\"aa0f6b18-30f9-4e15-ac83-9fce34525947\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"938bd462-d9e0-4887-8ef1-670120e419ad\"}}},\"post_processing_script\":\"# If the function is successful in updating users access rights,\\n# a note is added to the incident\\n\\nif (results.success):\\n  color = \\\"#45bc27\\\" #green\\n  if (results.inputs.ldap_toggle_access.get(\\\"name\\\") == \\\"Disabled\\\"):\\n    color = \\\"#ff402b\\\" #red\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP Utilities: Toggle Access workflow \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                    \u0026lt;b\u0026gt;Email:\u0026lt;/b\u0026gt; \u0026lt;u style=\\\"color: #7fb0ff\\\"\u0026gt;{}\u0026lt;/u\u0026gt;\\n                    \u0026lt;b\u0026gt;Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {}\\\"\u0026gt;{}\u0026lt;/b\u0026gt;\\n                    \u0026lt;b\u0026gt;DN:\u0026lt;/b\u0026gt; \u0027{}\u0027\\\"\\\"\\\".format(artifact.value, color, results.inputs.ldap_toggle_access.name, results.inputs.ldap_dn)\\n\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Once the LDAP Utilities: Search completes, get the DN of the first entry\\n# which will be the DN of the account you want to set a Toggle Access for\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_dn = workflow.properties.search_output.content[0][\\\"dn\\\"]\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1r2dkc6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dijgsh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dijgsh\" sourceRef=\"ServiceTask_0be768x\" targetRef=\"EndEvent_19rq2c5\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0uz0mob\"\u003e\u003cincoming\u003eSequenceFlow_00cs355\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1r2dkc6\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_04m0elt\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_00cs355\" sourceRef=\"ServiceTask_1qhd998\" targetRef=\"ExclusiveGateway_0uz0mob\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1r2dkc6\" name=\"\" sourceRef=\"ExclusiveGateway_0uz0mob\" targetRef=\"ServiceTask_0be768x\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# if at least one entry is found, success will be True\\ndecision == workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_04m0elt\" name=\"\" sourceRef=\"ExclusiveGateway_0uz0mob\" targetRef=\"EndEvent_19rq2c5\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"decision != workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_15a70qt\"\u003e\u003ctext\u003eIf the search returns nothing, skip toggling access and end\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0r15w1a\" sourceRef=\"ExclusiveGateway_0uz0mob\" targetRef=\"TextAnnotation_15a70qt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0fgo0d9\"\u003e\u003ctext\u003eEnd\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nvst3c\" sourceRef=\"EndEvent_19rq2c5\" targetRef=\"TextAnnotation_0fgo0d9\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"50\" x=\"102\" y=\"147\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"165\" xsi:type=\"omgdc:Point\" y=\"196\"/\u003e\u003comgdi:waypoint x=\"143\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_19rq2c5\" id=\"EndEvent_19rq2c5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"704\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"722\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qhd998\" id=\"ServiceTask_1qhd998_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"279\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zt8blr\" id=\"SequenceFlow_0zt8blr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0be768x\" id=\"ServiceTask_0be768x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"543\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dijgsh\" id=\"SequenceFlow_1dijgsh_di\"\u003e\u003comgdi:waypoint x=\"643\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"704\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"673.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0uz0mob\" id=\"ExclusiveGateway_0uz0mob_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"436\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"461\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00cs355\" id=\"SequenceFlow_00cs355_di\"\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"407.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1r2dkc6\" id=\"SequenceFlow_1r2dkc6_di\"\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"543\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"470\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04m0elt\" id=\"SequenceFlow_04m0elt_di\"\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003comgdi:waypoint x=\"722\" xsi:type=\"omgdc:Point\" y=\"129\"/\u003e\u003comgdi:waypoint x=\"722\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"547\" y=\"108\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_15a70qt\" id=\"TextAnnotation_15a70qt_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"172\" x=\"434\" y=\"322\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0r15w1a\" id=\"Association_0r15w1a_di\"\u003e\u003comgdi:waypoint x=\"468\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"510\" xsi:type=\"omgdc:Point\" y=\"322\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0fgo0d9\" id=\"TextAnnotation_0fgo0d9_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"50\" x=\"767\" y=\"167\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nvst3c\" id=\"Association_1nvst3c_di\"\u003e\u003comgdi:waypoint x=\"739\" xsi:type=\"omgdc:Point\" y=\"200\"/\u003e\u003comgdi:waypoint x=\"767\" xsi:type=\"omgdc:Point\" y=\"191\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "admin@example.com",
      "description": "An example workflow showing how to enable/disable an Active Directory user account",
      "export_key": "example_ldap_utilities_toggle_access",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636305225,
      "name": "Example: LDAP Utilities: Toggle Access",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_toggle_access",
      "tags": [],
      "uuid": "cbb7719b-4d47-4d86-84c9-5001ac42637d",
      "workflow_id": 19
    },
    {
      "actions": [],
      "content": {
        "version": 24,
        "workflow_id": "example_ldap_utilities_update",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_update\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Update\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow that updates the value of a DN\u0027s attribute with the given value(s)]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0s8l4i1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_14rl1ih\"\u003e\u003cincoming\u003eSequenceFlow_15r9dza\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0hz51xf\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1923jeb\" name=\"LDAP Utilities: Update\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"dfe0fab8-c425-48fc-95ab-a23f722f77bc\"\u003e{\"inputs\":{},\"post_processing_script\":\"# If the function is successful in updating the value of the attribute,\\n# a note is added to the incident\\n\\nif (results.success):\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP Utilities: Update workflow \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                    An LDAP Attribute has been updated\\n                    \u0026lt;b\u0026gt;Attribute:\u0026lt;/b\u0026gt; {}\\n                    \u0026lt;b\u0026gt;New Value(s):\u0026lt;/b\u0026gt; {}\\n                    \u0026lt;b\u0026gt;DN:\u0026lt;/b\u0026gt; \u0027{}\u0027\\\"\\\"\\\".format(results.inputs.ldap_attribute_name, results.inputs.ldap_attribute_values, results.user_dn)\\n\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Once the LDAP Utilities: Search completes, get the DN of the first entry\\n# which will be the DN of the account you want to update. Then set\\n# the name of the attribute to update and list the values\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_dn = workflow.properties.search_output.content[0][\\\"dn\\\"]\\ninputs.ldap_attribute_name = \\\"homePhone\\\"\\ninputs.ldap_attribute_values = \\\"[\u0027081111111\u0027]\\\"\\n# inputs.ldap_attribute_values = \\\"[\u0027081111111\u0027, \u0027082222222\u0027]\\\"\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_18fei9y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_15r9dza\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0s8l4i1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1k2mvun\"/\u003e\u003csequenceFlow id=\"SequenceFlow_15r9dza\" sourceRef=\"ServiceTask_1923jeb\" targetRef=\"EndEvent_14rl1ih\"/\u003e\u003cserviceTask id=\"ServiceTask_1k2mvun\" name=\"LDAP Utilities: Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"892075c1-64ba-46c9-aba1-f1f1aa040bb7\"\u003e{\"inputs\":{},\"post_processing_script\":\"# No post-processing script here as output being passed into next function\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Set the ldap_search_base and ldap_search_filter\\n# using the ldap_param wildcard then get the email\\n# address the user you want to update from the artifact\u0027s value\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_search_base = \\\"dc=example,dc=com\\\"\\ninputs.ldap_search_filter = \\\"(\u0026amp;(mail=%ldap_param%))\\\"\\ninputs.ldap_search_param =  artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"search_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0s8l4i1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xussi6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xussi6\" sourceRef=\"ServiceTask_1k2mvun\" targetRef=\"ExclusiveGateway_0xk5bqy\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0xk5bqy\"\u003e\u003cincoming\u003eSequenceFlow_0xussi6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_18fei9y\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0hz51xf\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_18fei9y\" name=\"\" sourceRef=\"ExclusiveGateway_0xk5bqy\" targetRef=\"ServiceTask_1923jeb\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# if at least one entry is found, success will be True\\ndecision == workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0hz51xf\" name=\"\" sourceRef=\"ExclusiveGateway_0xk5bqy\" targetRef=\"EndEvent_14rl1ih\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"decision != workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19p2bfe\"\u003e\u003ctext\u003eEnd\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18f2kbb\" sourceRef=\"EndEvent_14rl1ih\" targetRef=\"TextAnnotation_19p2bfe\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"50\" x=\"97\" y=\"164\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"164\" xsi:type=\"omgdc:Point\" y=\"200\"/\u003e\u003comgdi:waypoint x=\"147\" xsi:type=\"omgdc:Point\" y=\"192\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_14rl1ih\" id=\"EndEvent_14rl1ih_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"685\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"703\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19p2bfe\" id=\"TextAnnotation_19p2bfe_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"757\" y=\"191\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18f2kbb\" id=\"Association_18f2kbb_di\"\u003e\u003comgdi:waypoint x=\"721\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"757\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1923jeb\" id=\"ServiceTask_1923jeb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"526\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0s8l4i1\" id=\"SequenceFlow_0s8l4i1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"260\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"184\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15r9dza\" id=\"SequenceFlow_15r9dza_di\"\u003e\u003comgdi:waypoint x=\"626\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"685\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"610.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1k2mvun\" id=\"ServiceTask_1k2mvun_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"260\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xussi6\" id=\"SequenceFlow_0xussi6_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"417\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"388.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0xk5bqy\" id=\"ExclusiveGateway_0xk5bqy_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"417\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"442\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18fei9y\" id=\"SequenceFlow_18fei9y_di\"\u003e\u003comgdi:waypoint x=\"467\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"526\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"452\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hz51xf\" id=\"SequenceFlow_0hz51xf_di\"\u003e\u003comgdi:waypoint x=\"442\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"442\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003comgdi:waypoint x=\"703\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003comgdi:waypoint x=\"703\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"528\" y=\"105\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 24,
      "creator_id": "admin@example.com",
      "description": "An example workflow that updates the value of a DN\u0027s attribute with the given value(s)",
      "export_key": "example_ldap_utilities_update",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636305488,
      "name": "Example: LDAP Utilities: Update",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_update",
      "tags": [],
      "uuid": "4e0cb06d-9c47-4996-8dfe-aed68869262f",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 29,
        "workflow_id": "example_ldap_utilities_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_search\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Search\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow which runs a person query against an LDAP server using the person\u0027s email address]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1p0pun3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1xv950w\" name=\"LDAP Utilities: Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"892075c1-64ba-46c9-aba1-f1f1aa040bb7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  LDAP Utilities: Search - post-processing script ##\\n# Example of expected results - OpenLdap\\n\\\"\\\"\\\"\\n\u0027entries\u0027: [{\\\"dn\\\": \\\"uid=newton,dc=example,dc=com\\\", \\\"telephoneNumber\\\": [], \\\"uid\\\": [\\\"newton\\\"],\\n    \\\"mail\\\": [\\\"newton@ldap.forumsys.com\\\"], \\\"sn\\\": [\\\"Newton\\\"], \\\"cn\\\": [\\\"Isaac Newton\\\"]},\\n    {\\\"dn\\\": \\\"uid=einstein,dc=example,dc=com\\\", \\\"telephoneNumber\\\": [\\\"314-159-2653\\\"], \\\"uid\\\": [\\\"einstein\\\"],\\n    \\\"mail\\\": [\\\"einstein@ldap.forumsys.com\\\"], \\\"sn\\\": [\\\"Einstein\\\"], \\\"cn\\\": [\\\"Albert Einstein\\\"]}]\\n\\\"\\\"\\\"\\n\\n# Example of expected results - ActiveDirectory\\n\\\"\\\"\\\"\\n\u0027entries\u0027: [{u\u0027dn\u0027: u\u0027CN=Isaac Newton,OU=IBMResilient,DC=ibm,DC=resilient,DC=com\u0027,\\n              u\u0027telephoneNumber\u0027: u\u0027314-159-2653\u0027, u\u0027cn\u0027: u\u0027Isaac Newton\u0027,\\n              u\u0027mail\u0027: u\u0027einstein@resilient.ibm.com\u0027, u\u0027sn\u0027: u\u0027Newton\u0027}]\\n\\\"\\\"\\\"\\n\\n#  Globals\\nENTRY_TO_DATATABLE_MAP = {\\n   \\\"uid\\\": \\\"uid\\\",\\n   \\\"cn\\\": \\\"fullname\\\",\\n   \\\"sn\\\": \\\"surname\\\",\\n   \\\"mail\\\": \\\"email_address\\\",\\n   \\\"telephoneNumber\\\": \\\"telephone_number\\\"\\n}\\n\\n# Processing if the function is a success\\nif(results.success):\\n  for entry in results.content:\\n    if not entry:\\n      break\\n    # Add Row\\n    row = incident.addRow(\\\"ldap_query_results\\\")\\n    for k in ENTRY_TO_DATATABLE_MAP:\\n      if not entry[k]:\\n        row[ENTRY_TO_DATATABLE_MAP[k]] = \\\"N/A\\\"\\n      else:\\n        try:\\n          # If \u0027entry[k]\u0027 is empty\\n          if not len(entry[k]):\\n            row[ENTRY_TO_DATATABLE_MAP[k]] = \\\"N/A\\\"\\n          # Handle for Active Directory\\n          elif isinstance(entry[k], unicode):\\n            row[ENTRY_TO_DATATABLE_MAP[k]] = entry[k]\\n          # Handle for OpenLdap\\n          else:\\n            row[ENTRY_TO_DATATABLE_MAP[k]] = entry[k][0]\\n        except IndexError:\\n          row[ENTRY_TO_DATATABLE_MAP[k]] = \\\"N/A\\\"\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  LDAP Utilities: Search - pre-processing script ##\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_search_base = \\\"dc=example,dc=com\\\"\\ninputs.ldap_search_filter = \\\"(\u0026amp;(objectClass=person)(mail=*%ldap_param%))\\\"\\ninputs.ldap_search_attributes = \\\"uid,cn,sn,mail,telephoneNumber\\\"\\ninputs.ldap_search_param = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1p0pun3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hxgtgx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_02v8j60\"\u003e\u003cincoming\u003eSequenceFlow_1hxgtgx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1hxgtgx\" sourceRef=\"ServiceTask_1xv950w\" targetRef=\"EndEvent_02v8j60\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1p0pun3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1xv950w\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1xv950w\" id=\"ServiceTask_1xv950w_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"351\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02v8j60\" id=\"EndEvent_02v8j60_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"639\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"657\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hxgtgx\" id=\"SequenceFlow_1hxgtgx_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"639\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"545\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1p0pun3\" id=\"SequenceFlow_1p0pun3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"274.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 29,
      "creator_id": "admin@example.com",
      "description": "An example workflow which runs a person query against an LDAP server using the person\u0027s email address",
      "export_key": "example_ldap_utilities_search",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636304766,
      "name": "Example: LDAP Utilities: Search",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_search",
      "tags": [],
      "uuid": "dd244e52-1072-418a-ac40-19c2ed8dc53d",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 41,
        "workflow_id": "example_ldap_utilities_add_users_to_groups",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_add_users_to_groups\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Add User(s) to Group(s)\"\u003e\u003cdocumentation\u003eAn example workflow showing how to add multiple users to multiple groups\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0snjctn\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1977eiw\" name=\"LDAP Utilities: Add to Group(s)\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b602d316-c3b6-4b36-8813-eb81fd381bba\"\u003e{\"inputs\":{},\"post_processing_script\":\"# If the function is successful in adding the users to said groups,\\n# a note is added to the incident\\n\\nif (results.success):\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP Utilities: Add User(s) to Group(s) \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                    \u0026lt;b\u0026gt;User(s):\u0026lt;/b\u0026gt; {}\\n                    \u0026lt;b\u0026gt;Group(s):\u0026lt;/b\u0026gt; {}\\\"\\\"\\\".format(results.inputs.ldap_multiple_user_dn, results.inputs.ldap_multiple_group_dn)\\n\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Both inputs must be a string representation of a List\\n\\n## Example of multiple entries\\n# inputs.ldap_multiple_user_dn = \\\"[\u0027dn=user1,dc=example,dc=com\u0027, \u0027dn=user2,dc=example,dc=com\u0027]\\\"\\n# inputs.ldap_multiple_group_dn = \\\"[\u0027dn=Accounts Group,dc=example,dc=com\u0027, \u0027dn=IT Group,dc=example,dc=com\u0027]\\\"\\n\\n## Note: You can use this handy function below, then not need to worry about the inputs formatting\\n\\ndef into_string_list_format(entries):\\n  \\\"\\\"\\\"Function that converts a list or single string into a \u0027string repersentation of a list\u0027\\\"\\\"\\\"\\n  string_list_to_return = \\\"[{}]\\\"\\n\\n  # If its a string, assume its one DN, one entry\\n  if isinstance(entries, basestring):\\n    return string_list_to_return.format(\u0027\\\"{}\\\"\u0027.format(entries))\\n\\n  # Else assume its a List, so multiple DNs, multiple entries\\n  else:\\n    entries_to_add = \\\"\\\"\\n    for e in entries:\\n      entries_to_add += \u0027\\\"{}\\\",\u0027.format(e)\\n    return string_list_to_return.format(entries_to_add)\\n\\nlist_of_users_dn = [\u0027cn=Breda User11,cn=Users,dc=example,dc=com\u0027, \u0027cn=Breda User10,cn=Users,dc=example,dc=com\u0027]\\n\\ninputs.ldap_domain_name = \\\"Domain1\\\"\\n# Both inputs must be a string representation of a List\\ninputs.ldap_multiple_user_dn = into_string_list_format(list_of_users_dn)\\ninputs.ldap_multiple_group_dn = into_string_list_format(\u0027cn=GroupA,cn=Users,dc=example,dc=com\u0027)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0snjctn\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11eb0c4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0snjctn\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1977eiw\"/\u003e\u003cendEvent id=\"EndEvent_0rlnblo\"\u003e\u003cincoming\u003eSequenceFlow_11eb0c4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_11eb0c4\" sourceRef=\"ServiceTask_1977eiw\" targetRef=\"EndEvent_0rlnblo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1977eiw\" id=\"ServiceTask_1977eiw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"399\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0snjctn\" id=\"SequenceFlow_0snjctn_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"298.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0rlnblo\" id=\"EndEvent_0rlnblo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"679\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"697\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11eb0c4\" id=\"SequenceFlow_11eb0c4_di\"\u003e\u003comgdi:waypoint x=\"499\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"679\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"589\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 41,
      "creator_id": "admin@example.com",
      "description": "An example workflow showing how to add multiple users to multiple groups",
      "export_key": "example_ldap_utilities_add_users_to_groups",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636304918,
      "name": "Example: LDAP Utilities: Add User(s) to Group(s)",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_add_users_to_groups",
      "tags": [],
      "uuid": "8bb8e545-0841-49ec-a2f0-9080337a5564",
      "workflow_id": 15
    },
    {
      "actions": [],
      "content": {
        "version": 32,
        "workflow_id": "example_ldap_utilities_set_password",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_set_password\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Set Password\"\u003e\u003cdocumentation\u003eAn example workflow that searches for a user using their email address, gets their DN and sets a new password for that user\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bbjw69\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0azie2d\"\u003e\u003cincoming\u003eSequenceFlow_1adifvp\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_193svjt\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_03tj4yh\" name=\"LDAP Utilities: Search\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"892075c1-64ba-46c9-aba1-f1f1aa040bb7\"\u003e{\"inputs\":{},\"post_processing_script\":\"# No post-processing script here as output being passed into next function\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Set the ldap_search_base and ldap_search_filter\\n# using the ldap_param wildcard then get the email\\n# address the user you want to set a new password for from the artifact\u0027s value\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_search_base = \\\"dc=example,dc=com\\\"\\ninputs.ldap_search_filter = \\\"(\u0026amp;(objectClass=person)(mail=%ldap_param%))\\\"\\ninputs.ldap_search_param =  artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"search_output\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bbjw69\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_04b8zyw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bbjw69\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03tj4yh\"/\u003e\u003cserviceTask id=\"ServiceTask_042e0nm\" name=\"LDAP Utilities: Set Password\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b75c2ee2-759b-4d01-9649-6ec46f6a646e\"\u003e{\"inputs\":{},\"post_processing_script\":\"# If the function is successful in changing the users password,\\n# a note is added to the incident\\n\\nif (results.success):\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP MultiDomain Utilities: Set Password workflow \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                    A New Password has been set for:\\n                    \u0026lt;b\u0026gt;Email:\u0026lt;/b\u0026gt; \u0026lt;u style=\\\"color: #7fb0ff\\\"\u0026gt;{}\u0026lt;/u\u0026gt;\\n                    \u0026lt;b\u0026gt;DN:\u0026lt;/b\u0026gt; \u0027{}\u0027\\n                    \u0026lt;b\u0026gt;New password:\u0026lt;/b\u0026gt; \u0027{}\u0027\\\"\\\"\\\".format(artifact.value, results.inputs.ldap_dn, results.inputs.ldap_new_password)\\n\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Once the LDAP Utilities: Search completes, get the DN of the first entry\\n# which will be the DN of the account you want to set a Set a New Password for\\ninputs.ldap_domain_name = \u0027Domain1\u0027\\ninputs.ldap_dn = workflow.properties.search_output.content[0][\\\"dn\\\"]\\ninputs.ldap_new_password = \\\"\\\"\\ninputs.ldap_new_auto_password_len = \u002712\u0027\\ninputs.ldap_return_new_password = True\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1d9kfki\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1adifvp\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1adifvp\" sourceRef=\"ServiceTask_042e0nm\" targetRef=\"EndEvent_0azie2d\"/\u003e\u003csequenceFlow id=\"SequenceFlow_04b8zyw\" sourceRef=\"ServiceTask_03tj4yh\" targetRef=\"ExclusiveGateway_1wqzksd\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1wqzksd\"\u003e\u003cincoming\u003eSequenceFlow_04b8zyw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1d9kfki\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_193svjt\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1d9kfki\" name=\"\" sourceRef=\"ExclusiveGateway_1wqzksd\" targetRef=\"ServiceTask_042e0nm\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# if at least one entry is found, success will be True\\ndecision == workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_193svjt\" name=\"\" sourceRef=\"ExclusiveGateway_1wqzksd\" targetRef=\"EndEvent_0azie2d\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"decision != workflow.properties.search_output[\\\"success\\\"]\",\"final_expression_text\":\"decision\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12ui9le\"\u003e\u003ctext\u003eIf the search returns nothing, skip Set Password and End\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hnn7g6\" sourceRef=\"ExclusiveGateway_1wqzksd\" targetRef=\"TextAnnotation_12ui9le\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0q69jso\"\u003e\u003ctext\u003eEnd\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0pek3d6\" sourceRef=\"EndEvent_0azie2d\" targetRef=\"TextAnnotation_0q69jso\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"50\" x=\"106\" y=\"153\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"165\" xsi:type=\"omgdc:Point\" y=\"197\"/\u003e\u003comgdi:waypoint x=\"148\" xsi:type=\"omgdc:Point\" y=\"183\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0azie2d\" id=\"EndEvent_0azie2d_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"843\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"816\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03tj4yh\" id=\"ServiceTask_03tj4yh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"282.1146881287726\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bbjw69\" id=\"SequenceFlow_1bbjw69_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"282\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"240\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_042e0nm\" id=\"ServiceTask_042e0nm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"583\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1adifvp\" id=\"SequenceFlow_1adifvp_di\"\u003e\u003comgdi:waypoint x=\"683\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"843\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"718\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04b8zyw\" id=\"SequenceFlow_04b8zyw_di\"\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"434\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"408\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1wqzksd\" id=\"ExclusiveGateway_1wqzksd_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"434\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"459\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1d9kfki\" id=\"SequenceFlow_1d9kfki_di\"\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"583\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"489\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_193svjt\" id=\"SequenceFlow_193svjt_di\"\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003comgdi:waypoint x=\"843\" xsi:type=\"omgdc:Point\" y=\"116\"/\u003e\u003comgdi:waypoint x=\"843\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"606\" y=\"95\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12ui9le\" id=\"TextAnnotation_12ui9le_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"181\" x=\"370\" y=\"301\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hnn7g6\" id=\"Association_0hnn7g6_di\"\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"459\" xsi:type=\"omgdc:Point\" y=\"301\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0q69jso\" id=\"TextAnnotation_0q69jso_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"915\" y=\"191\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0pek3d6\" id=\"Association_0pek3d6_di\"\u003e\u003comgdi:waypoint x=\"879\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"915\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 32,
      "creator_id": "admin@example.com",
      "description": "An example workflow that searches for a user using their email address, gets their DN and sets a new password for that user",
      "export_key": "example_ldap_utilities_set_password",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636305377,
      "name": "Example: LDAP Utilities: Set Password",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_set_password",
      "tags": [],
      "uuid": "ad15e9ce-3d17-4bbb-b99a-e6aa4eb5db62",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "example_ldap_utilities_remove_user_from_groups",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_ldap_utilities_remove_user_from_groups\" isExecutable=\"true\" name=\"Example: LDAP Utilities: Remove User(s) from Group(s)\"\u003e\u003cdocumentation\u003eAn example workflow showing how to remove multiple users from a group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00qp10i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1hkgt06\" name=\"LDAP Utilities: Remove from Group...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9ba21139-a5f0-4710-983d-83190f4bdc6c\"\u003e{\"inputs\":{},\"post_processing_script\":\"# If the function is successful in removing the users from said groups,\\n# a note is added to the incident\\n\\nif (results.success):\\n  if not results.users_dn:\\n    noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP Utilities: Remove User from Group(s) \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                  \u0026lt;b\u0026gt;No users found. Check inputted user DN\u0027s\u0026lt;/b\u0026gt;\\\"\\\"\\\"\\n  else:\\n    noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;i style=\\\"color: #979ca3\\\"\u0026gt; LDAP Utilities: Remove User from Group(s) \u0026lt;u\u0026gt;complete\u0026lt;/u\u0026gt;:\u0026lt;/i\u0026gt;\\n                    \u0026lt;b\u0026gt;User(s):\u0026lt;/b\u0026gt; {}\\n                    \u0026lt;b\u0026gt;Group(s):\u0026lt;/b\u0026gt; {}\\\"\\\"\\\".format(results.inputs.ldap_multiple_user_dn, results.inputs.ldap_multiple_group_dn)\\n\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Both inputs must be a string representation of a List\\n\\n## Example of multiple entries\\n# inputs.ldap_multiple_user_dn = \\\"[\u0027dn=user1,dc=example,dc=com\u0027, \u0027dn=user2,dc=example,dc=com\u0027]\\\"\\n# inputs.ldap_multiple_group_dn = \\\"[\u0027dn=Accounts Group,dc=example,dc=com\u0027, \u0027dn=IT Group,dc=example,dc=com\u0027]\\\"\\n\\n## Note: You can use this handy function below, then not need to worry about the inputs formatting\\n\\ndef into_string_list_format(entries):\\n  \\\"\\\"\\\"Function that converts a list or single string into a \u0027string repersentation of a list\u0027\\\"\\\"\\\"\\n  string_list_to_return = \\\"[{}]\\\"\\n\\n  # If its a string, assume its one DN, one entry\\n  if isinstance(entries, basestring):\\n    return string_list_to_return.format(\u0027\\\"{}\\\"\u0027.format(entries))\\n\\n  # Else assume its a List, so multiple DNs, multiple entries\\n  else:\\n    entries_to_add = \\\"\\\"\\n    for e in entries:\\n      entries_to_add += \u0027\\\"{}\\\",\u0027.format(e)\\n    return string_list_to_return.format(entries_to_add)\\n\\nlist_of_users_dn = [\u0027cn=Breda User11,cn=Users,dc=example,dc=com\u0027, \u0027cn=Breda User10,cn=Users,dc=example,dc=com\u0027]\\n\\ninputs.ldap_domain_name = \\\"Domain1\\\"\\n# Both inputs must be a string representation of a List\\ninputs.ldap_multiple_user_dn = into_string_list_format(list_of_users_dn)\\ninputs.ldap_multiple_group_dn = into_string_list_format(\u0027cn=GroupA,cn=Users,dc=example,dc=com\u0027)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00qp10i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xidaq7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_00qp10i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1hkgt06\"/\u003e\u003cendEvent id=\"EndEvent_0lyq5pj\"\u003e\u003cincoming\u003eSequenceFlow_0xidaq7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0xidaq7\" sourceRef=\"ServiceTask_1hkgt06\" targetRef=\"EndEvent_0lyq5pj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1hkgt06\" id=\"ServiceTask_1hkgt06_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"384\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00qp10i\" id=\"SequenceFlow_00qp10i_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"384\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"291\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lyq5pj\" id=\"EndEvent_0lyq5pj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"655\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"673\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xidaq7\" id=\"SequenceFlow_0xidaq7_di\"\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"655\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"569.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "creator_id": "admin@example.com",
      "description": "An example workflow showing how to remove multiple users from a group",
      "export_key": "example_ldap_utilities_remove_user_from_groups",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1650636305061,
      "name": "Example: LDAP Utilities: Remove User(s) from Group(s)",
      "object_type": "artifact",
      "programmatic_name": "example_ldap_utilities_remove_user_from_groups",
      "tags": [],
      "uuid": "f25af4ec-ae21-4ce6-a450-879a9295ae01",
      "workflow_id": 17
    }
  ],
  "workspaces": []
}
