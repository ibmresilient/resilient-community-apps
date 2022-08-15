{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Playbook Maker",
      "id": 721,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Playbook Maker",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6a740d6b-335d-40e3-b4b2-748136c24447",
      "view_items": [
        {
          "content": "c62b14d6-fcd1-459c-b823-b796daeffc96",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed66fce5-42bf-414a-a98c-452852c5fd17",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ad84d0a4-b33b-4d77-bd74-64ae93259925",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "44511cca-41a0-4efb-bda8-b86425c7eee9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4f4d124b-049a-41de-86ab-98a1066ba63a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b6f332b-b336-4502-99be-6ba2bdb8e24f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3c8e09d5-3597-4f86-92a7-26f2e1da95f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f952515c-04f7-41e0-b494-54df3f76b906",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "playbook_maker"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1656101542345,
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
      "export_key": "__function/pbm_activation_type",
      "hide_notification": false,
      "id": 2220,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_activation_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_activation_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "8c7b3199-45bd-47c5-aba4-be39a156633d",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Automatic",
          "properties": null,
          "uuid": "715cb83f-39ce-45cd-916e-4c48b5fb2bd2",
          "value": 2809
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Manual",
          "properties": null,
          "uuid": "54012560-39ec-4e0a-90c2-45a5479b2cc1",
          "value": 2810
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
      "export_key": "__function/pbm_playbook_type",
      "hide_notification": false,
      "id": 2221,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_playbook_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_playbook_type",
      "tooltip": "incident, artifact, attachment, comment, \u003cdatatable name\u003e",
      "type_id": 11,
      "uuid": "a0025552-9496-4c10-b5bb-123829dc68ef",
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
      "export_key": "__function/pbm_function_names",
      "hide_notification": false,
      "id": 2222,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_function_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_function_names",
      "tooltip": "Comma separated names of functions or blank for all",
      "type_id": 11,
      "uuid": "bc059cf1-5173-464a-992b-636577a6c85d",
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
      "export_key": "__function/pbm_activation_fields",
      "hide_notification": false,
      "id": 2223,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_activation_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_activation_fields",
      "tooltip": "Create activation fields for data input",
      "type_id": 11,
      "uuid": "f1dd6b4e-e94b-4098-8a97-7010b914ff84",
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
      "export_key": "__function/pbm_add_to_same_playbook",
      "hide_notification": false,
      "id": 2368,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_add_to_same_playbook",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_add_to_same_playbook",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fd171133-6f21-411a-a353-e4c5a7c920db",
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
      "export_key": "__function/pbm_playbook_name",
      "hide_notification": false,
      "id": 2224,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_playbook_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Playbook for \u003cfunction\u003e",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_playbook_name",
      "tooltip": "Name of playbook use \u003cfunction\u003e to replace with function name",
      "type_id": 11,
      "uuid": "304490ef-0bae-4ffd-a333-dde19874a49f",
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
      "export_key": "__function/pbm_app_name",
      "hide_notification": false,
      "id": 2225,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_app_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_app_name",
      "tooltip": "Name of app to associate to playbook(s)",
      "type_id": 11,
      "uuid": "35202141-7a35-4b4a-9acd-8e0b30c882a9",
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
      "export_key": "__function/pbm_script_names",
      "hide_notification": false,
      "id": 2369,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_script_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "script1,script2",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "pbm_script_names",
      "tooltip": "Comma separated list of global scripts to apply",
      "type_id": 11,
      "uuid": "780c84f8-ad4a-4599-b87a-4943e3a4e10f",
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
      "export_key": "actioninvocation/pbm_app_name",
      "hide_notification": false,
      "id": 2228,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_app_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "App Name",
      "tooltip": "API name of App. Leave empty if referencing specific functions",
      "type_id": 6,
      "uuid": "ad84d0a4-b33b-4d77-bd74-64ae93259925",
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
      "export_key": "actioninvocation/pbm_type",
      "hide_notification": false,
      "id": 2240,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Playbook Type",
      "tooltip": "Modify the selection list to include datatables",
      "type_id": 6,
      "uuid": "c62b14d6-fcd1-459c-b823-b796daeffc96",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "incident",
          "properties": null,
          "uuid": "d85e8ee0-a925-463d-ade7-af26c51bce9c",
          "value": 2817
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "artifact",
          "properties": null,
          "uuid": "aff07c8f-9f33-4c90-b83a-22f23d37768b",
          "value": 2818
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "task",
          "properties": null,
          "uuid": "44d1491d-317a-4e17-83b1-353371ea9f98",
          "value": 2819
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "note",
          "properties": null,
          "uuid": "6d4431e5-3b04-44f5-a9e0-97e998c21465",
          "value": 2820
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "attachment",
          "properties": null,
          "uuid": "444c8e1e-af65-4b4b-8fe6-d2fba531cd80",
          "value": 2821
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cchange for datatables\u003e",
          "properties": null,
          "uuid": "e0ae36eb-4d1e-4c77-b3a0-fbe7e9822e86",
          "value": 2822
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
      "export_key": "actioninvocation/pbm_name_prefix",
      "hide_notification": false,
      "id": 2226,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_name_prefix",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Playbook Name Prefix",
      "tooltip": "",
      "type_id": 6,
      "uuid": "ed66fce5-42bf-414a-a98c-452852c5fd17",
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
      "export_key": "actioninvocation/pbm_activation_fields",
      "hide_notification": false,
      "id": 2231,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_activation_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Enable Activation Fields",
      "tooltip": "Only used for \u0027Manual\u0027 Activation type",
      "type_id": 6,
      "uuid": "f952515c-04f7-41e0-b494-54df3f76b906",
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
      "export_key": "actioninvocation/pbm_add_to_same_playbook",
      "hide_notification": false,
      "id": 2366,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_add_to_same_playbook",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Add to same Playbook",
      "tooltip": "Added all functions to same Playbook",
      "type_id": 6,
      "uuid": "0b6f332b-b336-4502-99be-6ba2bdb8e24f",
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
      "export_key": "actioninvocation/pbm_activation_type",
      "hide_notification": false,
      "id": 2232,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_activation_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Playbook Activation Type",
      "tooltip": "",
      "type_id": 6,
      "uuid": "3c8e09d5-3597-4f86-92a7-26f2e1da95f3",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Automatic",
          "properties": null,
          "uuid": "58135cff-eeac-4fec-ab06-bc90269bca6c",
          "value": 2811
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Manual",
          "properties": null,
          "uuid": "079c3a49-5e77-44e8-9318-b1f439eb2f99",
          "value": 2812
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
      "export_key": "actioninvocation/pbm_function_names",
      "hide_notification": false,
      "id": 2227,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_function_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Function name(s)",
      "tooltip": "Comma separated function API names or empty. If specifying an App name, leave empty",
      "type_id": 6,
      "uuid": "44511cca-41a0-4efb-bda8-b86425c7eee9",
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
      "export_key": "actioninvocation/pbm_script_names",
      "hide_notification": false,
      "id": 2367,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "pbm_script_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "templates": [],
      "text": "Script Name(s)",
      "tooltip": "Comma separated global scripts to use",
      "type_id": 6,
      "uuid": "4f4d124b-049a-41de-86ab-98a1066ba63a",
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
      "created_date": 1653442620345,
      "description": {
        "content": "Create playbook(s) based on specific apps and functions",
        "format": "text"
      },
      "destination_handle": "fn_playbook_maker",
      "display_name": "Make Playbook",
      "export_key": "make_playbook",
      "id": 121,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 8,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1656099595893,
      "name": "make_playbook",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"playbook_name\": \"make-7 for make_playbook\", \"success\": true, \"id\": 85}], \"raw\": null, \"inputs\": {\"pbm_activation_fields\": false, \"pbm_app_name\": null, \"pbm_playbook_name\": \"make-7\", \"pbm_function_names\": \"make_playbook\", \"pbm_activation_type\": \"Manual\", \"pbm_playbook_type\": \"incident\", \"pbm_add_to_same_playbook\": false}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-playbook-maker\", \"package_version\": \"1.0.0\", \"host\": \"local\", \"execution_time_ms\": 5732, \"timestamp\": \"2022-06-09 15:12:28\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"playbook_name\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"id\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"pbm_activation_fields\": {\"type\": \"boolean\"}, \"pbm_app_name\": {}, \"pbm_playbook_name\": {\"type\": \"string\"}, \"pbm_function_names\": {\"type\": \"string\"}, \"pbm_activation_type\": {\"type\": \"string\"}, \"pbm_playbook_type\": {\"type\": \"string\"}, \"pbm_add_to_same_playbook\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "uuid": "927ccb1d-a537-4291-8fc6-d35b74cdcd7d",
      "version": 3,
      "view_items": [
        {
          "content": "a0025552-9496-4c10-b5bb-123829dc68ef",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "304490ef-0bae-4ffd-a333-dde19874a49f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "35202141-7a35-4b4a-9acd-8e0b30c882a9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bc059cf1-5173-464a-992b-636577a6c85d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "780c84f8-ad4a-4599-b87a-4943e3a4e10f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c7b3199-45bd-47c5-aba4-be39a156633d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f1dd6b4e-e94b-4098-8a97-7010b914ff84",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fd171133-6f21-411a-a353-e4c5a7c920db",
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
          "name": "Playbook Maker",
          "object_type": "incident",
          "programmatic_name": "playbook_maker",
          "tags": [
            {
              "tag_handle": "fn_playbook_maker",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 322
        }
      ]
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
      "create_date": 1656101540518,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1656101540518,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "2f52990c-7d97-4b23-b5d6-d7c0cdc0e004"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_playbook_maker",
      "name": "fn_playbook_maker",
      "programmatic_name": "fn_playbook_maker",
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "users": [
        "a@example.com"
      ],
      "uuid": "ed83cce2-78c3-4c6d-84e9-14a8cfede0de"
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
    "build_number": 0,
    "major": 45,
    "minor": 0,
    "version": "45.0.0"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "playbook_maker",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_maker\" isExecutable=\"true\" name=\"Playbook Maker\"\u003e\u003cdocumentation\u003eCreate playbook(s) based apps or functions to include.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0orag44\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00sr963\" name=\"Make Playbook\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"927ccb1d-a537-4291-8fc6-d35b74cdcd7d\"\u003e{\"inputs\":{\"8c7b3199-45bd-47c5-aba4-be39a156633d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"54012560-39ec-4e0a-90c2-45a5479b2cc1\"}}},\"post_processing_script\":\"if not results.success:\\n  incident.addNote(\\\"Playbook Maker failed: {} for playbook name prefix: {}\\\".format(results.reason, rule.properties.pbm_name_prefix))\\nelse:\\n  msg_list = []\\n  for pbk in results.content:\\n    msg = \\\"{}: {}\\\".format(pbk.get(\u0027playbook_name\u0027), \\\"Success\\\" if pbk.get(\u0027success\u0027, False) else \\\"Failure\\\")\\n    if pbk.get(\u0027success\u0027, False):\\n      msg = \\\"{} \u0026lt;a target=\u0027blank\u0027 href=\u0027#playbooks/designer/{}\u0027\u0026gt;Playbook link\u0026lt;/a\u0026gt;\\\".format(msg, pbk.get(\u0027id\u0027))\\n    else:\\n      msg = \\\"Creating playbook failed: {}\\\".format(pbk.get(\u0027playbook_name\u0027))\\n    msg_list.append(msg)\\n      \\n  incident.addNote(helper.createRichText(\\\"Playbook Maker results:\u0026lt;br\u0026gt;{}\\\".format(\\\"\u0026lt;br\u0026gt;\\\".join(msg_list))))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.pbm_playbook_type = rule.properties.pbm_type\\ninputs.pbm_playbook_name = rule.properties.pbm_name_prefix\\ninputs.pbm_app_name = rule.properties.pbm_app_name\\ninputs.pbm_function_names = rule.properties.pbm_function_names\\ninputs.pbm_script_names = rule.properties.pbm_script_names\\ninputs.pbm_activation_type = rule.properties.pbm_activation_type\\ninputs.pbm_activation_fields = rule.properties.pbm_activation_fields if rule.properties.pbm_activation_fields else False\\ninputs.pbm_add_to_same_playbook = rule.properties.pbm_add_to_same_playbook if rule.properties.pbm_add_to_same_playbook else False\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0orag44\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0poj1sd\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0orag44\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00sr963\"/\u003e\u003cendEvent id=\"EndEvent_1ha688c\"\u003e\u003cincoming\u003eSequenceFlow_0poj1sd\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0poj1sd\" sourceRef=\"ServiceTask_00sr963\" targetRef=\"EndEvent_1ha688c\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18yp1yz\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned in a note\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0akwfox\" sourceRef=\"ServiceTask_00sr963\" targetRef=\"TextAnnotation_18yp1yz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00sr963\" id=\"ServiceTask_00sr963_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"270\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0orag44\" id=\"SequenceFlow_0orag44_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"270\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"234\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ha688c\" id=\"EndEvent_1ha688c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"433\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"451\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0poj1sd\" id=\"SequenceFlow_0poj1sd_di\"\u003e\u003comgdi:waypoint x=\"370\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"401.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18yp1yz\" id=\"TextAnnotation_18yp1yz_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"142\" x=\"359\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0akwfox\" id=\"Association_0akwfox_di\"\u003e\u003comgdi:waypoint x=\"359\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"115\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "Create playbook(s) based apps or functions to include.",
      "export_key": "playbook_maker",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1656100100842,
      "name": "Playbook Maker",
      "object_type": "incident",
      "programmatic_name": "playbook_maker",
      "tags": [
        {
          "tag_handle": "fn_playbook_maker",
          "value": null
        }
      ],
      "uuid": "3be3ac70-c643-48a1-95df-71606c341d4a",
      "workflow_id": 322
    }
  ],
  "workspaces": []
}
