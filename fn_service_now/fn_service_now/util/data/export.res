{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1744121747380,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 4949,
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
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
      "export_key": "__function/sn_add_soar_link_on_snow",
      "hide_notification": false,
      "id": 5850,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "sn_add_soar_link_on_snow",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_add_soar_link_on_snow",
      "tooltip": "To add a link to the SOAR incident to the SNOW incident note. Defaults to True.",
      "type_id": 11,
      "uuid": "8efbcee8-df71-4b6b-87c8-33c1200e7610",
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
      "export_key": "__function/sn_parent_ref_id",
      "hide_notification": false,
      "id": 4950,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_parent_ref_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_parent_ref_id",
      "tooltip": "If creating a child incident, give the parent reference ID from SNOW. Be sure also to set the \"parent\" field in the sn_optional_fields to the appropriate sys_id for the parent",
      "type_id": 11,
      "uuid": "8fb8fdc3-caab-4916-b247-6c01ab2c77a6",
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
      "export_key": "__function/sn_note_text",
      "hide_notification": false,
      "id": 4951,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_note_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_note_text",
      "tooltip": "The text of the Comment",
      "type_id": 11,
      "uuid": "908e2bd1-d682-44e1-9240-efb5c2bf23a1",
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
      "export_key": "__function/sn_close_work_note",
      "hide_notification": false,
      "id": 4952,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_close_work_note",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_close_work_note",
      "tooltip": "A optional note to add to the ServiceNow Record when it is closed from within IBM SOAR",
      "type_id": 11,
      "uuid": "9939f061-85a2-42ac-875a-46168998f3b6",
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
      "export_key": "__function/sn_init_work_note",
      "hide_notification": false,
      "id": 4953,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_init_work_note",
      "operation_perms": {},
      "operations": [],
      "placeholder": "This Incident originated from our Cyber Security Team using the IBM SOAR platform",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_init_work_note",
      "tooltip": "A custom string of text to be added as initial work_note in ServiceNow",
      "type_id": 11,
      "uuid": "9fb070d7-fc5a-4ca1-8e2e-fc940e53c857",
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
      "export_key": "__function/sn_query_field",
      "hide_notification": false,
      "id": 4954,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_query_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "state",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_query_field",
      "tooltip": "The name of the ServiceNow Field to query",
      "type_id": 11,
      "uuid": "a483a5fb-0064-4760-9fe8-7d8312ed1dd2",
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
      "export_key": "__function/sn_query_value",
      "hide_notification": false,
      "id": 4955,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_query_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"In Progress\"",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_query_value",
      "tooltip": "The value to be compared",
      "type_id": 11,
      "uuid": "ad37c004-da73-4b49-9575-a33093897343",
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 4956,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
      "export_key": "__function/sn_close_code",
      "hide_notification": false,
      "id": 4957,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_close_code",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Solved (Permanently)",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_close_code",
      "tooltip": "The ServiceNow close_code i.e. \"Solved (Permanently)\"",
      "type_id": 11,
      "uuid": "bffdd765-d0c1-42bd-8b93-798436cfab93",
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
      "export_key": "__function/sn_record_state",
      "hide_notification": false,
      "id": 4958,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sn_record_state",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_record_state",
      "tooltip": "The numeric value of the state of the record in ServiceNow",
      "type_id": 11,
      "uuid": "f0eb15f5-fb36-4c6d-b489-352befbe3ea3",
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
      "export_key": "__function/sn_close_notes",
      "hide_notification": false,
      "id": 4959,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_close_notes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Incident resolved in SOAR. No further action needed",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_close_notes",
      "tooltip": "The reason for resolving this record",
      "type_id": 11,
      "uuid": "f234db2f-dfe8-401f-a3b9-f5f87921e21f",
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
      "export_key": "__function/sn_optional_fields",
      "hide_notification": false,
      "id": 4960,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_optional_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"\"\"{\"assignment_group\": \"IT Security\"}\"\"\"",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_optional_fields",
      "tooltip": "JSON string containing the api_name and value of the fields you want to set within ServiceNow after creating the record",
      "type_id": 11,
      "uuid": "0b739213-0896-4ee8-bd5a-fd26286185ba",
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
      "export_key": "__function/sn_table_name",
      "hide_notification": false,
      "id": 4961,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_table_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "incident",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_table_name",
      "tooltip": "Name of the table in ServiceNow",
      "type_id": 11,
      "uuid": "107edc5d-e444-4398-a596-00d61db4c3fd",
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
      "export_key": "__function/attachment_id",
      "hide_notification": false,
      "id": 4962,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "1677716a-a95e-4f55-8e3e-5399e6d3bd96",
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
      "export_key": "__function/sn_note_type",
      "hide_notification": false,
      "id": 4963,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "sn_note_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_note_type",
      "tooltip": "When sending a Note, should it be added as a \"work_note\" or \"additional_comment\" in ServiceNow. Default: \"work_note\"",
      "type_id": 11,
      "uuid": "19d5e854-dc64-43d4-9a39-7be914920ad6",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "work_note",
          "properties": null,
          "uuid": "c65de77d-f6b2-4c19-94eb-cdfa5cf5037f",
          "value": 1993
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "additional_comment",
          "properties": null,
          "uuid": "3cb448e0-48d2-4afb-b509-59e9dc19168e",
          "value": 1994
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
      "export_key": "__function/sn_res_id",
      "hide_notification": false,
      "id": 4964,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_res_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_res_id",
      "tooltip": "The res_id of a SNOW record in sn_records_dt Data Table",
      "type_id": 11,
      "uuid": "33155d23-83f5-4a2b-b013-0baa7866c62d",
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
      "export_key": "__function/sn_update_fields",
      "hide_notification": false,
      "id": 4965,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_update_fields",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_update_fields",
      "tooltip": "A JSON String of SNOW field names and values to update",
      "type_id": 11,
      "uuid": "4bf00b16-c289-4a96-9066-7422fc18b78a",
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
      "export_key": "__function/sn_resilient_status",
      "hide_notification": false,
      "id": 4966,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_resilient_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sn_resilient_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "72a4e5ad-6df7-4839-a114-f081d4c00973",
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
      "export_key": "incident/sn_snow_table_name",
      "hide_notification": false,
      "id": 4935,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_snow_table_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "incident",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "ServiceNow Table Name",
      "tooltip": "The name of the table in ServiceNow for the corresponding record",
      "type_id": 0,
      "uuid": "9efe2671-dfd9-4ab5-8f97-d9baa3beabef",
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
      "export_key": "incident/sn_snow_record_id",
      "hide_notification": false,
      "id": 4936,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sn_snow_record_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "ServiceNow Record ID",
      "tooltip": "ID of ServiceNow Record",
      "type_id": 0,
      "uuid": "ec65fd4d-b4c5-4632-a504-d390f45be715",
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
      "export_key": "incident/sn_snow_record_link",
      "hide_notification": false,
      "id": 4937,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sn_snow_record_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "ServiceNow Record",
      "tooltip": "Link to ServiceNow Record",
      "type_id": 0,
      "uuid": "6e69a025-6597-4994-9b1b-557ef736d45e",
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
      "created_date": 1739375038053,
      "description": {
        "content": "Function that adds a SOAR Attachment to a ServiceNow Record.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Add Attachment to Record",
      "export_key": "fn_snow_add_attachment_to_record",
      "id": 5,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706477,
      "name": "fn_snow_add_attachment_to_record",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "975b1809-2110-4208-8c37-4b8ba9ad331a",
      "version": 1,
      "view_items": [
        {
          "content": "1677716a-a95e-4f55-8e3e-5399e6d3bd96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
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
      "created_date": 1739375038131,
      "description": {
        "content": "Function that adds a Note to a ServiceNow Record. Option to add the note as a \u0027Work Note\u0027 or \u0027Additional Comment\u0027.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Add Note to Record",
      "export_key": "fn_snow_add_note_to_record",
      "id": 6,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706477,
      "name": "fn_snow_add_note_to_record",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c43f8cc1-5cdc-41a6-a6b0-fa59dd32df36",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "908e2bd1-d682-44e1-9240-efb5c2bf23a1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "19d5e854-dc64-43d4-9a39-7be914920ad6",
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
      "created_date": 1739375038216,
      "description": {
        "content": "Function that uses the \u0027/close_record\u0027 custom endpoint in ServiceNow to change the state of a ServiceNow Record and add Close Notes and a Close Code to the Record.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Close Record",
      "export_key": "fn_snow_close_record",
      "id": 7,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706478,
      "name": "fn_snow_close_record",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "edadf951-4652-48a9-8068-9b719bf4bfe4",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "33155d23-83f5-4a2b-b013-0baa7866c62d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f0eb15f5-fb36-4c6d-b489-352befbe3ea3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f234db2f-dfe8-401f-a3b9-f5f87921e21f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bffdd765-d0c1-42bd-8b93-798436cfab93",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9939f061-85a2-42ac-875a-46168998f3b6",
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
      "created_date": 1739375038300,
      "description": {
        "content": "Function that uses the \u0027/create\u0027 custom endpoint in ServiceNow to create a ServiceNow Record from a SOAR Incident or Task.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Create Record",
      "export_key": "fn_snow_create_record",
      "id": 8,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706477,
      "name": "fn_snow_create_record",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "041fa8ca-70bb-44b1-996b-88f61a8a0671",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9fb070d7-fc5a-4ca1-8e2e-fc940e53c857",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b739213-0896-4ee8-bd5a-fd26286185ba",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "107edc5d-e444-4398-a596-00d61db4c3fd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8fb8fdc3-caab-4916-b247-6c01ab2c77a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8efbcee8-df71-4b6b-87c8-33c1200e7610",
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
      "created_date": 1739375038381,
      "description": {
        "content": "A helper function to add a Note to a Task from a Workflow with a different parent object type.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW Helper: Add Task Note",
      "export_key": "fn_snow_helper_add_task_note",
      "id": 9,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706476,
      "name": "fn_snow_helper_add_task_note",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "f02d65f0-f19a-414a-828d-5c35de5270b1",
      "version": 1,
      "view_items": [
        {
          "content": "33155d23-83f5-4a2b-b013-0baa7866c62d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "908e2bd1-d682-44e1-9240-efb5c2bf23a1",
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
      "created_date": 1739375038461,
      "description": {
        "content": "A helper function that updates the ServiceNow Records Data Table when the status of an Incident/Task is changed.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW Helper: Update Data Table",
      "export_key": "fn_snow_helper_update_datatable",
      "id": 10,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706477,
      "name": "fn_snow_helper_update_datatable",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "6130c083-17ea-4262-986b-8d073d3f7328",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "72a4e5ad-6df7-4839-a114-f081d4c00973",
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
      "created_date": 1739375038547,
      "description": {
        "content": "Function that gets the \u0027sys_id\u0027 of a ServiceNow Record.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Lookup sys_id",
      "export_key": "fn_snow_lookup_sysid",
      "id": 11,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706477,
      "name": "fn_snow_lookup_sysid",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "e5abf91c-57f6-4d01-bd5a-50bfe261cb01",
      "version": 1,
      "view_items": [
        {
          "content": "107edc5d-e444-4398-a596-00d61db4c3fd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a483a5fb-0064-4760-9fe8-7d8312ed1dd2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ad37c004-da73-4b49-9575-a33093897343",
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
      "created_date": 1739375038631,
      "description": {
        "content": "Function that uses the \u0027/update\u0027 custom endpoint in ServiceNow to update a ServiceNow Record with a given dictionary of field name/value pairs.",
        "format": "text"
      },
      "destination_handle": "fn_service_now",
      "display_name": "SNOW: Update Record",
      "export_key": "fn_snow_update_record",
      "id": 12,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743421706478,
      "name": "fn_snow_update_record",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "95d7d4df-0ec8-4dbd-bbcf-9759b23930eb",
      "version": 1,
      "view_items": [
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba318261-ed6a-4a38-a187-9e0b68d1604f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "33155d23-83f5-4a2b-b013-0baa7866c62d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4bf00b16-c289-4a96-9066-7422fc18b78a",
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
  "id": 41,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1744121745266,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1744121745266,
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
      "export_key": "fn_service_now",
      "name": "fn_service_now",
      "programmatic_name": "fn_service_now",
      "tags": [],
      "users": [
        "a@example.com"
      ],
      "uuid": "59c41f3d-8a93-4205-a23d-1706c1e48f61"
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
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_57237674_6459_4940_a146_9daf73c2f87a\" isExecutable=\"true\" name=\"playbook_57237674_6459_4940_a146_9daf73c2f87a\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1pwcmsj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1pwcmsj\u003c/incoming\u003e\u003coutgoing\u003eFlow_09gn2pv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1pwcmsj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09gn2pv\u003c/incoming\u003e\u003coutgoing\u003eFlow_160bxct\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09gn2pv\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Map IBM SOAR severity values to ServiceNow severity values\\nsn_severity_map = {\\n  \\\"High\\\": 1,\\n  \\\"Medium\\\": 2,\\n  \\\"Low\\\": 3\\n}\\n\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Record created from a IBM SOAR Incident ID: {incident.id}.\\n                          Severity: {incident.severity_code}\\n                          Incident Type(s): {\u0027, \u0027.join(incident.incident_type_ids)}\\\"\\\"\\\"\\n\\n# If the user adds a comment when they invoke the rule, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = getattr(playbook.inputs, \\\"sn_initial_note\\\", None).content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# Initial work note to attach to created ServiceNow Record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\n# For SIR tables it is recommended to map \\\"business_criticality\\\" to sn_severity_map as that is visible in the SNOW query_builder\\n# (see the example commented out below)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}: {incident.name}\\\",\\n  \\\"impact\\\": sn_severity_map[incident.severity_code],\\n  #\\\"business_criticality\\\": sn_severity_map[incident.severity_code],\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\")\\n})\\n\\n# to override the table name set in app.config, set inputs.sn_table_name=\u0026lt;table_name_to_send_to\u0026gt;\\n# inputs.sn_table_name = \\\"incident\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_160bxct\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vytx9i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_160bxct\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"73be698f-53dc-4937-a232-852291f15bd5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vytx9i\u003c/incoming\u003e\u003coutgoing\u003eFlow_0owltkx\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1vytx9i\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0owltkx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0owltkx\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_57237674_6459_4940_a146_9daf73c2f87a\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0owltkx\" id=\"Flow_0owltkx_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"722\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"784\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vytx9i\" id=\"Flow_1vytx9i_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"592\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_160bxct\" id=\"Flow_160bxct_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"508\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09gn2pv\" id=\"Flow_09gn2pv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1pwcmsj\" id=\"Flow_1pwcmsj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"508\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"784\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375039169,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
      "description": {
        "content": "Deprecated as of v2.3.0. Please use \"SNOW: Create New Incident (PB)\" to create \"incident\" records and \"SNOW: Create New Security Incident (PB)\" to create \"sn_si_incident\" records.\n\nThis playbook is used to create a new record in ServiceNow from this case in SOAR. It reads the sn_table_name config to determine the table in which to create the record.",
        "format": "text"
      },
      "display_name": "[DEPRECATED] SNOW: Create New Record (PB)",
      "export_key": "snow_create_record_incident_pb",
      "field_type_handle": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
      "fields_type": {
        "actions": [],
        "display_name": "[DEPRECATED] SNOW: Create New Record (PB)",
        "export_key": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
        "fields": {
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_57237674_6459_4940_a146_9daf73c2f87a/sn_assignment_group",
            "hide_notification": false,
            "id": 4967,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1005,
            "uuid": "e66e5ba7-8e3d-4633-b143-a477337c2145",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "7aa0c8aa-ab53-4a18-aa64-4fb29a97abe8",
                "value": 1995
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "94926972-d9c2-4852-8bc6-0625b32b947e",
                "value": 1996
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "09fa796f-5657-4ba4-b41b-99fdcaeb8e6a",
                "value": 1997
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "8d2434e7-1961-417d-a272-d31b6ac52c54",
                "value": 1998
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "9bec94cd-ac5a-4a9e-a9b1-f27f0e619080",
                "value": 1999
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "2dee7af0-b270-4c66-b8a0-535a3bcf158f",
                "value": 2000
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_57237674_6459_4940_a146_9daf73c2f87a/sn_initial_note",
            "hide_notification": false,
            "id": 4968,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1005,
            "uuid": "83475f17-1707-4aac-9f92-f6400cdc1076",
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
        "type_name": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
        "uuid": "30af54bc-38fd-4648-9a46-e7fadeed1cc8"
      },
      "has_logical_errors": false,
      "id": 5,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509532722,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375039356,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 20,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375039356,
          "name": "SNOW post-process",
          "object_type": "incident",
          "playbook_handle": "snow_create_record_incident_pb",
          "programmatic_name": "snow_create_record_incident_pb_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n  # Set incident fields sn_snow_record_id, sn_snow_record_link, and sn_snow_table_name\n  incident.sn_snow_record_id = results.get(\"sn_ref_id\")\n  incident.sn_snow_record_link = f\"\"\"\u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003eLink\u003c/a\u003e\"\"\"\n  incident.sn_snow_table_name = results.get(\"sn_table_name\")\n\n  noteText = f\"\"\"\u003cbr\u003eThis Incident has been created in \u003cb\u003eServiceNow\u003c/b\u003e in the {results.get(\u0027sn_table_name\u0027)} table.\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  incident.addNote(helper.createRichText(noteText))\n",
          "tags": [],
          "uuid": "73be698f-53dc-4937-a232-852291f15bd5"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "not_has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "e66e5ba7-8e3d-4633-b143-a477337c2145",
            "element": "field_uuid",
            "field_type": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "83475f17-1707-4aac-9f92-f6400cdc1076",
            "element": "field_uuid",
            "field_type": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_record_incident_pb",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_57237674-6459-4940-a146-9daf73c2f87a",
        "id": 7,
        "name": "playbook_57237674_6459_4940_a146_9daf73c2f87a",
        "type": "playbook",
        "uuid": "8f073d8b-43a0-4ae4-8f20-52c29ecfc417"
      },
      "tags": [],
      "type": "default",
      "uuid": "57237674-6459-4940-a146-9daf73c2f87a",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 5,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423\" isExecutable=\"true\" name=\"playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_18kx1xj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\n# Codes prepended with [SIR] are specific to Security Incident Response incidents\\nmap_sn_record_states = {\\n  \\\"New\\\": 1,\\n  \\\"In Progress\\\": 2,\\n  \\\"On Hold\\\": 3,\\n  \\\"[INC] Resolved\\\": 6,\\n  \\\"[INC] Closed\\\": 7,\\n  \\\"[INC] Canceled\\\": 8,\\n\\t\\\"[SIR] Analysis\\\": 16,\\n\\t\\\"[SIR] Contain\\\": 18,\\n\\t\\\"[SIR] Eradicate\\\": 19,\\n\\t\\\"[SIR] Recover\\\": 20,\\n\\t\\\"[SIR] Review\\\": 100,\\n\\t\\\"[SIR] Closed\\\": 3,\\n\\t\\\"[SIR] Canceled\\\": 7\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this task\\ninputs.task_id = task.id\\n\\n# The state to change the record to\\n# inputs.sn_record_state = map_sn_record_states[\\\"Closed\\\"]\\ninputs.sn_record_state = map_sn_record_states[getattr(playbook.inputs, \\\"sn_record_state\\\", None)]\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\n# inputs.sn_close_notes = \\\"This incident has been resolved in IBM SOAR. No further action required\\\"\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# The ServiceNow \u0027close_code\u0027 that you normally select when closing a ServiceNow record\\n# inputs.sn_close_code = \\\"Solved (Permanently)\\\"\\nif getattr(playbook.inputs, \\\"sn_close_code\\\", None):\\n  inputs.sn_close_code = getattr(playbook.inputs, \\\"sn_close_code\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_18kx1xj\u003c/incoming\u003e\u003coutgoing\u003eFlow_1q6qsnc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_18kx1xj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"787488cb-b82d-4925-83d4-75ac5eefbe85\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1q6qsnc\u003c/incoming\u003e\u003coutgoing\u003eFlow_1rpv64c\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1q6qsnc\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1rpv64c\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1rpv64c\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1rpv64c\" id=\"Flow_1rpv64c_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"454\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1q6qsnc\" id=\"Flow_1q6qsnc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18kx1xj\" id=\"Flow_18kx1xj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"454\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375040167,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
      "description": {
        "content": "Deprecated as of v2.3.0 because tasks don\u0027t contain enough information to distinguish between Security Incidents, Security Response Tasks, and Incidents. This playbook is now disabled by default. Please use the associated playbook for the record from the datatable.",
        "format": "text"
      },
      "display_name": "[DEPRECATED] SNOW: Update/Close Record [Task] (PB)",
      "export_key": "snow_updateclose_record_task_pb",
      "field_type_handle": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
      "fields_type": {
        "actions": [],
        "display_name": "[DEPRECATED] SNOW: Update/Close Record [Task] (PB)",
        "export_key": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
        "fields": {
          "sn_close_code": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423/sn_close_code",
            "hide_notification": false,
            "id": 4969,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_code",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Code",
            "tooltip": "Optional. Sets the close code only when Record State is CLOSED",
            "type_id": 1006,
            "uuid": "aa8a86c5-8980-475e-8383-9fe0704f4cb2",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Work Around)",
                "properties": null,
                "uuid": "de767ea9-8214-4654-a553-1b6ba44ea494",
                "value": 2001
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Permanently)",
                "properties": null,
                "uuid": "8fc18dad-8399-4d0a-bcf7-32d4f559dbaf",
                "value": 2002
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Not Reproducible)",
                "properties": null,
                "uuid": "6c495ca9-3abe-4208-b7d9-24ccb2afe096",
                "value": 2003
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Too Costly)",
                "properties": null,
                "uuid": "d233d03f-7bdf-4ba6-a17d-7923c7c25e9f",
                "value": 2004
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed/Resolved by Caller",
                "properties": null,
                "uuid": "7347bbf3-7517-4e77-b041-06b18367486d",
                "value": 2005
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Investigation completed",
                "properties": null,
                "uuid": "11e9cabd-d4f1-47ff-bfdc-79af168bc7e3",
                "value": 2006
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Threat mitigated",
                "properties": null,
                "uuid": "42bd5afd-7471-4b37-8b97-de4f3b444cda",
                "value": 2007
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Patched vulnerability",
                "properties": null,
                "uuid": "10863819-a1c6-41c7-9890-cce3cc008bfa",
                "value": 2008
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Invalid vulnerability",
                "properties": null,
                "uuid": "c57dce4c-86d0-470e-8cfb-41913c9dab07",
                "value": 2009
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not resolved",
                "properties": null,
                "uuid": "0f5eb06b-0d7f-479c-97c2-30dd5bbc9b3f",
                "value": 2010
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "False positive",
                "properties": null,
                "uuid": "32d0b824-f227-4daa-974d-436cc4078182",
                "value": 2011
              }
            ]
          },
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423/sn_close_notes",
            "hide_notification": false,
            "id": 4970,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1006,
            "uuid": "e2b0868b-0596-47cd-918d-54f03e59c541",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423/sn_record_state",
            "hide_notification": false,
            "id": 4971,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "Use INC state for SNOW Incident tables and SIR States for Security Incident Response tables",
            "type_id": 1006,
            "uuid": "76bc3ddf-e62f-4479-a549-92d9ecd75cab",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[INC] Resolved",
                "properties": null,
                "uuid": "8e3e8c9c-388b-4495-812d-68f9b4482375",
                "value": 2012
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[INC] Closed",
                "properties": null,
                "uuid": "64df972d-9c3a-464e-8a85-f6e99a25424e",
                "value": 2013
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[INC] Canceled",
                "properties": null,
                "uuid": "b7994a00-2f79-48ba-8167-6207913cf539",
                "value": 2014
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Analysis",
                "properties": null,
                "uuid": "05b48c98-7b59-4c12-87a4-840f974e006a",
                "value": 2015
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Contain",
                "properties": null,
                "uuid": "a7a930f2-eba2-4df0-a722-e75d5bd3f804",
                "value": 2016
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Eradicate",
                "properties": null,
                "uuid": "6e143172-c622-4f61-9970-b7d9bbedcc70",
                "value": 2017
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Recover",
                "properties": null,
                "uuid": "77d2b513-fdfe-4fc2-af76-7c823c22cc5b",
                "value": 2018
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Review",
                "properties": null,
                "uuid": "1514abfe-03b0-44a1-aa3b-a64aed84a3cc",
                "value": 2019
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Closed",
                "properties": null,
                "uuid": "3a778ad2-8f01-4ca0-9365-1bc98a64af8b",
                "value": 2020
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "[SIR] Canceled",
                "properties": null,
                "uuid": "c028da6b-3f50-4eea-a89c-00ee4f1b60bb",
                "value": 2021
              }
            ]
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
        "type_name": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
        "uuid": "877d0656-a09b-412a-b418-4cc7a820ec76"
      },
      "has_logical_errors": false,
      "id": 6,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509533392,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375040433,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 21,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375040433,
          "name": "SNOW post-process",
          "object_type": "task",
          "playbook_handle": "snow_updateclose_record_task_pb",
          "programmatic_name": "snow_updateclose_record_task_pb_post_process",
          "script_text": "results = playbook.functions.results.close_record\nif results.get(\"success\"):\n  note_text = f\"\"\"\u003cbr\u003eThis Task has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\nelse:\n  note_text = f\"\"\"\u003cbr\u003eFailed to close this Task in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\ntask.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "787488cb-b82d-4925-83d4-75ac5eefbe85"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "76bc3ddf-e62f-4479-a549-92d9ecd75cab",
            "element": "field_uuid",
            "field_type": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "aa8a86c5-8980-475e-8383-9fe0704f4cb2",
            "element": "field_uuid",
            "field_type": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "e2b0868b-0596-47cd-918d-54f03e59c541",
            "element": "field_uuid",
            "field_type": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_record_task_pb",
      "object_type": "task",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_c21d4c8d-d49b-4c41-92c4-ddd0e60b3423",
        "id": 8,
        "name": "playbook_c21d4c8d_d49b_4c41_92c4_ddd0e60b3423",
        "type": "playbook",
        "uuid": "132e9fe1-ddf3-4406-9f29-bc1eaf5c0837"
      },
      "tags": [],
      "type": "default",
      "uuid": "c21d4c8d-d49b-4c41-92c4-ddd0e60b3423",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_098e7385_a5bf_4c11_91f1_d04490e3b791\" isExecutable=\"true\" name=\"playbook_098e7385_a5bf_4c11_91f1_d04490e3b791\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1qqywrr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Add Attachment to Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"975b1809-2110-4208-8c37-4b8ba9ad331a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The id of this attachment\\ninputs.attachment_id = attachment.id\\n\\n# The id of this incident\\ninputs.incident_id = incident.id\\n\\n# If this is a task attachment, get the taskId\\nif attachment.type == \u0027task\u0027:\\n  inputs.task_id = task.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_attachment\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1qqywrr\u003c/incoming\u003e\u003coutgoing\u003eFlow_1aka46t\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1qqywrr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"db033a24-6341-4183-82b6-6002efb796c3\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1aka46t\u003c/incoming\u003e\u003coutgoing\u003eFlow_1quzyar\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1aka46t\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1quzyar\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1quzyar\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_098e7385_a5bf_4c11_91f1_d04490e3b791\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1quzyar\" id=\"Flow_1quzyar_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"464\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1aka46t\" id=\"Flow_1aka46t_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qqywrr\" id=\"Flow_1qqywrr_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.017\" x=\"616\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"464\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375041144,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_098e7385_a5bf_4c11_91f1_d04490e3b791",
      "description": {
        "content": "Send this attachment to the associated record in ServiceNow.",
        "format": "text"
      },
      "display_name": "SNOW: Add Attachment to Record (PB)",
      "export_key": "snow_add_attachment_to_record",
      "field_type_handle": "playbook_098e7385_a5bf_4c11_91f1_d04490e3b791",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Add Attachment to Record (PB)",
        "export_key": "playbook_098e7385_a5bf_4c11_91f1_d04490e3b791",
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
        "type_name": "playbook_098e7385_a5bf_4c11_91f1_d04490e3b791",
        "uuid": "c802bdd7-2413-486a-baac-12e6271c1256"
      },
      "has_logical_errors": false,
      "id": 7,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509534117,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375041277,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 22,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375041277,
          "name": "SNOW post-process",
          "object_type": "attachment",
          "playbook_handle": "snow_add_attachment_to_record",
          "programmatic_name": "snow_add_attachment_to_record_post_process",
          "script_text": "results = playbook.functions.results.add_attachment\nif results.get(\"success\"):\n\n  noteText = f\"\"\"\u003cbr\u003e{principal.display_name} has added an attachment to \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eAttachment Name:\u003c/b\u003e  {results.attachment_name}\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\"\"\"\n\n  # If this is a task attachment, add a note to the Task\n  if task:\n    task.addNote(helper.createRichText(noteText))\n  # Else add the note to the Incident\n  else:\n    incident.addNote(helper.createRichText(noteText))",
          "tags": [],
          "uuid": "db033a24-6341-4183-82b6-6002efb796c3"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "snow_add_attachment_to_record",
      "object_type": "attachment",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_098e7385-a5bf-4c11-91f1-d04490e3b791",
        "id": 9,
        "name": "playbook_098e7385_a5bf_4c11_91f1_d04490e3b791",
        "type": "playbook",
        "uuid": "9373fa16-0859-4d02-a4e4-119bef653c43"
      },
      "tags": [],
      "type": "default",
      "uuid": "098e7385-a5bf-4c11-91f1-d04490e3b791",
      "version": 6
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": 1,
              "field_name": "sn_records_dt.sn_records_dt_snow_status",
              "method": "contains",
              "type": null,
              "value": "Closed"
            },
            {
              "evaluation_id": 2,
              "field_name": "sn_records_dt.sn_records_dt_snow_status",
              "method": "contains",
              "type": null,
              "value": "Resolved"
            },
            {
              "evaluation_id": 3,
              "field_name": "sn_records_dt.sn_records_dt_type",
              "method": "equals",
              "type": null,
              "value": "Incident"
            }
          ],
          "custom_condition": "(1 OR 2) AND 3 ",
          "logic_type": "advanced"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d\" isExecutable=\"true\" name=\"playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1oygik1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cscriptTask id=\"ScriptTask_1\" name=\"Close SOAR case on SNOW closure if row SN ID matches\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"ec551512-03cd-4462-bcc4-7639e2ef3496\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1oygik1\u003c/incoming\u003e\u003coutgoing\u003eFlow_06craps\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1oygik1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_06craps\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_06craps\" sourceRef=\"ScriptTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06craps\" id=\"Flow_06craps_di\"\u003e\u003comgdi:waypoint x=\"638\" y=\"52\"/\u003e\u003comgdi:waypoint x=\"638\" y=\"148\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"148\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"244\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1oygik1\" id=\"Flow_1oygik1_di\"\u003e\u003comgdi:waypoint x=\"640\" y=\"-174\"/\u003e\u003comgdi:waypoint x=\"640\" y=\"-103\"/\u003e\u003comgdi:waypoint x=\"638\" y=\"-103\"/\u003e\u003comgdi:waypoint x=\"638\" y=\"-32\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"540\" y=\"-226\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"574\" y=\"244\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1\" id=\"ScriptTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"540\" y=\"-32\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375042054,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d",
      "description": {
        "content": "Automatically closes the case/incident in SOAR when the status of the record in ServiceNow is changed to \"Closed\" or \"Resolved.\"",
        "format": "text"
      },
      "display_name": "SNOW: Close Incident on Datatable Value Change (PB)",
      "export_key": "snow_close_on_datatable_value_change_incident_pb",
      "field_type_handle": "playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Close Incident on Datatable Value Change (PB)",
        "export_key": "playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d",
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
        "type_name": "playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d",
        "uuid": "9f8b922a-d999-4337-a2e8-f770911b6f88"
      },
      "has_logical_errors": false,
      "id": 8,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1744121686672,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375042186,
          "description": "",
          "enabled": false,
          "export_key": "Close SOAR case on SNOW closure if row SN ID matches",
          "id": 23,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375042186,
          "name": "Close SOAR case on SNOW closure if row SN ID matches",
          "object_type": "sn_records_dt",
          "playbook_handle": "snow_close_on_datatable_value_change_incident_pb",
          "programmatic_name": "snow_close_on_datatable_value_change_incident_pb_close_soar_case_on_snow_closure",
          "script_text": "# only closes the case when the row with the same ID as the incident is closed\nif str(row.sn_records_dt_sn_ref_id) == str(incident.properties.sn_snow_record_id):\n  \n  \n  incident.plan_status = \"C\"\n  incident.resolution_id = \"Resolved\"\n  incident.resolution_summary = \"Closed from ServiceNow automatically when ServiceNow status changed to \" + str(row.sn_records_dt_snow_status.content)\n  \n  # NOTE: Make sure to also set any other required close fields that you may have in your SOAR system\n",
          "tags": [],
          "uuid": "ec551512-03cd-4462-bcc4-7639e2ef3496"
        }
      ],
      "name": "snow_close_on_datatable_value_change_incident_pb",
      "object_type": "sn_records_dt",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_d6feffc1-f9c6-4766-be54-d1a33f9ef20d",
        "id": 10,
        "name": "playbook_d6feffc1_f9c6_4766_be54_d1a33f9ef20d",
        "type": "playbook",
        "uuid": "bae2acd8-dc94-4d57-8dd2-be27ff888fc3"
      },
      "tags": [],
      "type": "default",
      "uuid": "d6feffc1-f9c6-4766-be54-d1a33f9ef20d",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_aaedaadd_54f4_44ac_a087_2556a15597b1\" isExecutable=\"true\" name=\"playbook_aaedaadd_54f4_44ac_a087_2556a15597b1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1uwk90m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1uwk90m\u003c/incoming\u003e\u003coutgoing\u003eFlow_04wlg33\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1uwk90m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04wlg33\u003c/incoming\u003e\u003coutgoing\u003eFlow_0chwcrv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_04wlg33\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Child Incident created from IBM SOAR Task ID: {task.id}. Associated IBM SOAR Incident ID: {incident.id}. Parent incident in SerivceNow: {incident.properties.sn_snow_record_id}\\\"\\\"\\\"\\n\\n# This can be true or false. True will add a link to the SOAR incident in a note on the ServiceNow incident.\\ninputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, \\\"sn_add_soar_link_on_snow\\\", True)\\n\\n# If the user adds a comment when they invoke the playbook, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = playbook.inputs.sn_initial_note.content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this task\\ninputs.task_id = task.id\\n\\n# Initial work note to attach to created ServiceNow record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Parse the urgency and impact numbers value from the text input\\nimpact = int(playbook.inputs.sn_impact[0])\\nurgency = int(playbook.inputs.sn_urgency[0])\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}-{task.id}: {task.name}\\\",\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\"),\\n  \\\"parent_incident\\\": playbook.functions.results.parent_inc_sys_id.get(\\\"sys_id\\\"),\\n  \\\"impact\\\": impact,\\n  \\\"urgency\\\": urgency\\n})\\n\\n# this specifc Playbook only will run to create recrods as child incidents, so use the same incident table as the parent\\ninputs.sn_table_name = incident.properties.sn_snow_table_name\\n\\n# because we\u0027re creating a child incident here, set the parent REF ID\\ninputs.sn_parent_ref_id = incident.properties.sn_snow_record_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0olhihg\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vyyekt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0chwcrv\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_6\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"4d3ba1e4-88b2-428b-a179-5f134b89d3ca\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vyyekt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1oz0idp\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1vyyekt\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1oz0idp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1oz0idp\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"incident\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"number\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = incident.properties.sn_snow_record_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"parent_inc_sys_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0chwcrv\u003c/incoming\u003e\u003coutgoing\u003eFlow_0olhihg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0olhihg\" sourceRef=\"ServiceTask_6\" targetRef=\"ServiceTask_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_aaedaadd_54f4_44ac_a087_2556a15597b1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0olhihg\" id=\"Flow_0olhihg_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"582\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"648\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1oz0idp\" id=\"Flow_1oz0idp_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"892\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"974\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vyyekt\" id=\"Flow_1vyyekt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"732\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"808\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0chwcrv\" id=\"Flow_0chwcrv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"498\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04wlg33\" id=\"Flow_04wlg33_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1uwk90m\" id=\"Flow_1uwk90m_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"156\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"104\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"648\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"808\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"974\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"497.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375042948,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
      "description": {
        "content": "Create a new \u0027incident\u0027 record in ServiceNow based off of the linked parent incident.",
        "format": "text"
      },
      "display_name": "SNOW: Create Child Incident (PB)",
      "export_key": "snow_create_child_incident_task_pb",
      "field_type_handle": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Create Child Incident (PB)",
        "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
        "fields": {
          "sn_add_soar_link_on_snow": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1/sn_add_soar_link_on_snow",
            "hide_notification": false,
            "id": 5852,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "sn_add_soar_link_on_snow",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Add SOAR link to ServiceNow incident",
            "tooltip": "Add SOAR incident link to ServiceNow incident in a note. Defaults to True.",
            "type_id": 1009,
            "uuid": "960a55ab-2d68-4335-b148-d88131763996",
            "values": []
          },
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1/sn_assignment_group",
            "hide_notification": false,
            "id": 4972,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1009,
            "uuid": "d32df65f-a077-4883-8d0f-7d267f8282d0",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "12ca895f-15ea-4440-85d1-811e198cc62a",
                "value": 2022
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "8b78cbd9-5455-4d89-8d29-2001add11745",
                "value": 2023
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "61e6145e-4d88-454b-8cc1-e15262762879",
                "value": 2024
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "3272dcaf-3ab5-4700-96f0-9734aed68b9f",
                "value": 2025
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "21a7dc88-2074-4e15-b7a6-ea90471a5183",
                "value": 2026
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "9f7957e2-92f7-4090-98df-b9021c655e3c",
                "value": 2027
              }
            ]
          },
          "sn_impact": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1/sn_impact",
            "hide_notification": false,
            "id": 4973,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_impact",
            "operation_perms": {},
            "operations": [],
            "placeholder": "3 - Low",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Impact",
            "tooltip": "Impact to set for this record in ServiceNow. Defaults to \"3 - Low\"",
            "type_id": 1009,
            "uuid": "d13dd92f-0e52-4bdf-9956-82c270bfa2c6",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1 - High",
                "properties": null,
                "uuid": "088390d8-3d98-401e-a262-20f81dcfea6d",
                "value": 2028
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "2 - Medium",
                "properties": null,
                "uuid": "e761d7a6-a4f9-4754-b849-de028eb87583",
                "value": 2029
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "3 - Low",
                "properties": null,
                "uuid": "6f3028e8-7d00-4c87-89f0-dca205cf6771",
                "value": 2030
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1/sn_initial_note",
            "hide_notification": false,
            "id": 4974,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1009,
            "uuid": "50a9a40b-0b79-430f-9285-5e2f16210701",
            "values": []
          },
          "sn_urgency": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1/sn_urgency",
            "hide_notification": false,
            "id": 4975,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_urgency",
            "operation_perms": {},
            "operations": [],
            "placeholder": "3 - Low",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Urgency",
            "tooltip": "Urgency to set for this record in ServiceNow. Defaults to \"3 - Low\"",
            "type_id": 1009,
            "uuid": "d6db1ec3-7f0e-4e16-91f5-bbdae3af38bc",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1 - High",
                "properties": null,
                "uuid": "cbdab111-110b-4009-9550-324c4bfe3a20",
                "value": 2031
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "2 - Medium",
                "properties": null,
                "uuid": "5506e1e2-0ff5-423f-a8df-1b2fe7529361",
                "value": 2032
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "3 - Low",
                "properties": null,
                "uuid": "fe23bf3d-0c16-4c61-a05f-fcb4a326cfe6",
                "value": 2033
              }
            ]
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
        "type_name": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
        "uuid": "fc801ad3-bd2e-46de-9835-aca1dabfac35"
      },
      "has_logical_errors": false,
      "id": 9,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743527717428,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375043241,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 24,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1743421711247,
          "name": "SNOW post-process",
          "object_type": "task",
          "playbook_handle": "snow_create_child_incident_task_pb",
          "programmatic_name": "snow_create_child_incident_task_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n\n  note_text = f\"\"\"\u003cbr\u003eThis Task has been created in \u003cb\u003eServiceNow\u003c/b\u003e with Impact \u0027{playbook.inputs.sn_impact}\u0027 and Urgency \u0027{playbook.inputs.sn_urgency}\u0027 in the {results.get(\u0027sn_table_name\u0027)} table as a Child Incident of {incident.properties.sn_snow_record_id} ({incident.properties.sn_snow_record_link.content}).\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  task.addNote(helper.createRichText(note_text))\n\nelif results.get(\"reason\"):\n  task.addNote(results.get(\"reason\"))",
          "tags": [],
          "uuid": "4d3ba1e4-88b2-428b-a179-5f134b89d3ca"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_table_name",
              "method": "equals",
              "type": null,
              "value": "incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "\u003cb\u003eCreate task as child incident of parent incident in SNOW\u003c/b\u003e\u003cbr /\u003e\n\nThis playbook will run to create this task as a record in ServiceNow with a \u0026quot;parent incident\u0026quot; link\nset to the linked record of this incident.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "960a55ab-2d68-4335-b148-d88131763996",
            "element": "field_uuid",
            "field_type": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d32df65f-a077-4883-8d0f-7d267f8282d0",
            "element": "field_uuid",
            "field_type": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "50a9a40b-0b79-430f-9285-5e2f16210701",
            "element": "field_uuid",
            "field_type": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Optional Impact and Urgency scores.\nThese two factors together will be used by ServiceNow to determine the \u0026quot;Priority\u0026quot; score for the incident.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d13dd92f-0e52-4bdf-9956-82c270bfa2c6",
            "element": "field_uuid",
            "field_type": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d6db1ec3-7f0e-4e16-91f5-bbdae3af38bc",
            "element": "field_uuid",
            "field_type": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_child_incident_task_pb",
      "object_type": "task",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_aaedaadd-54f4-44ac-a087-2556a15597b1",
        "id": 11,
        "name": "playbook_aaedaadd_54f4_44ac_a087_2556a15597b1",
        "type": "playbook",
        "uuid": "57b073ff-84a9-4804-a393-4f196add2475"
      },
      "tags": [],
      "type": "default",
      "uuid": "aaedaadd-54f4-44ac-a087-2556a15597b1",
      "version": 12
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885\" isExecutable=\"true\" name=\"playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1pwcmsj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1pwcmsj\u003c/incoming\u003e\u003coutgoing\u003eFlow_09gn2pv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1pwcmsj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09gn2pv\u003c/incoming\u003e\u003coutgoing\u003eFlow_160bxct\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09gn2pv\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Map IBM SOAR severity values to ServiceNow severity values\\nsn_severity_map = {\\n  \\\"High\\\": 1,\\n  \\\"Medium\\\": 2,\\n  \\\"Low\\\": 3\\n}\\n\\ninputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, \\\"sn_add_soar_link_on_snow\\\", None)\\n\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Record created from a IBM SOAR Incident ID: {incident.id}.\\n                          Severity: {incident.severity_code}\\n                          Incident Type(s): {\u0027, \u0027.join(incident.incident_type_ids)}\\\"\\\"\\\"\\n\\n# If the user adds a comment when they invoke the rule, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = getattr(playbook.inputs, \\\"sn_initial_note\\\", None).content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# Initial work note to attach to created ServiceNow Record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Parse the urgency and impact numbers value from the text input and incident severity, respectively\\nimpact = sn_severity_map[incident.severity_code]\\nurgency = int(playbook.inputs.sn_urgency[0])\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}: {incident.name}\\\",\\n  \\\"impact\\\": impact,\\n  \\\"urgency\\\": urgency,\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\")\\n})\\n\\n# This makes sure this creates this record in the \\\"incident\\\" table\\ninputs.sn_table_name = \\\"incident\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_160bxct\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vytx9i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_160bxct\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"333d91bc-9b43-41f6-ba98-22bf2ef71475\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vytx9i\u003c/incoming\u003e\u003coutgoing\u003eFlow_0owltkx\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1vytx9i\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0owltkx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0owltkx\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0owltkx\" id=\"Flow_0owltkx_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"722\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"784\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vytx9i\" id=\"Flow_1vytx9i_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"592\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_160bxct\" id=\"Flow_160bxct_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"508\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09gn2pv\" id=\"Flow_09gn2pv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1pwcmsj\" id=\"Flow_1pwcmsj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"508\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"784\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375043957,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
      "description": {
        "content": "Creates a new record in the Incident (incident) table in ServiceNow.",
        "format": "text"
      },
      "display_name": "SNOW: Create New Incident (PB)",
      "export_key": "snow_create_new_incident_pb",
      "field_type_handle": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Create New Incident (PB)",
        "export_key": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
        "fields": {
          "sn_add_soar_link_on_snow": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885/sn_add_soar_link_on_snow",
            "hide_notification": false,
            "id": 5851,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "sn_add_soar_link_on_snow",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Add SOAR link to ServiceNow incident",
            "tooltip": "Add SOAR incident link to ServiceNow incident in a note.",
            "type_id": 1010,
            "uuid": "48d23e2a-539c-4aff-ad91-a5b32d7f3546",
            "values": []
          },
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885/sn_assignment_group",
            "hide_notification": false,
            "id": 4976,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1010,
            "uuid": "9d13e561-6f8f-4fc1-9e8b-1544b41ee6ef",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "7aa0c8aa-ab53-4a18-aa64-4fb29a97abe8",
                "value": 2034
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "94926972-d9c2-4852-8bc6-0625b32b947e",
                "value": 2035
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "09fa796f-5657-4ba4-b41b-99fdcaeb8e6a",
                "value": 2036
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "8d2434e7-1961-417d-a272-d31b6ac52c54",
                "value": 2037
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "9bec94cd-ac5a-4a9e-a9b1-f27f0e619080",
                "value": 2038
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "2dee7af0-b270-4c66-b8a0-535a3bcf158f",
                "value": 2039
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885/sn_initial_note",
            "hide_notification": false,
            "id": 4977,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1010,
            "uuid": "6292437c-c716-4052-a155-ff3b5383999c",
            "values": []
          },
          "sn_urgency": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885/sn_urgency",
            "hide_notification": false,
            "id": 4978,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_urgency",
            "operation_perms": {},
            "operations": [],
            "placeholder": "3 - Low",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Urgency",
            "tooltip": "Urgency to set for this record in ServiceNow. Defaults to \"3 - Low\"",
            "type_id": 1010,
            "uuid": "6ad7b450-2005-4722-a494-040235fab517",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1 - High",
                "properties": null,
                "uuid": "25329a0e-46a1-4279-8d07-8a779867e08c",
                "value": 2040
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "2 - Medium",
                "properties": null,
                "uuid": "652c87e9-0cc2-4a09-8b08-0efeb1ae3393",
                "value": 2041
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "3 - Low",
                "properties": null,
                "uuid": "75cb81e3-4f4c-4f0d-ac33-b4a90fcf1bdc",
                "value": 2042
              }
            ]
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
        "type_name": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
        "uuid": "ba6b6423-a789-4abd-937f-b1e4ef4ba0ce"
      },
      "has_logical_errors": false,
      "id": 10,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743510784059,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375044180,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 25,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375044180,
          "name": "SNOW post-process",
          "object_type": "incident",
          "playbook_handle": "snow_create_new_incident_pb",
          "programmatic_name": "snow_create_new_incident_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n  # Set incident fields sn_snow_record_id, sn_snow_record_link, and sn_snow_table_name\n  incident.sn_snow_record_id = results.get(\"sn_ref_id\")\n  incident.sn_snow_record_link = f\"\"\"\u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003eLink\u003c/a\u003e\"\"\"\n  incident.sn_snow_table_name = results.get(\"sn_table_name\")\n\n  noteText = f\"\"\"\u003cbr\u003eThis Incident has been created in \u003cb\u003eServiceNow\u003c/b\u003e with Urgency \u0027{playbook.inputs.sn_urgency}\u0027in the {results.get(\u0027sn_table_name\u0027)} table.\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  incident.addNote(helper.createRichText(noteText))\n",
          "tags": [],
          "uuid": "333d91bc-9b43-41f6-ba98-22bf2ef71475"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "not_has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "48d23e2a-539c-4aff-ad91-a5b32d7f3546",
            "element": "field_uuid",
            "field_type": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "9d13e561-6f8f-4fc1-9e8b-1544b41ee6ef",
            "element": "field_uuid",
            "field_type": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6292437c-c716-4052-a155-ff3b5383999c",
            "element": "field_uuid",
            "field_type": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose the optional \u0026quot;urgency\u0026quot; value for this incident in ServiceNow. \nThe \u0026quot;impact\u0026quot; value in ServiceNow is set automatically and synced with the severity of the SOAR case.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6ad7b450-2005-4722-a494-040235fab517",
            "element": "field_uuid",
            "field_type": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_new_incident_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7118b3ee-519d-43c1-af78-2ac9bc71e885",
        "id": 12,
        "name": "playbook_7118b3ee_519d_43c1_af78_2ac9bc71e885",
        "type": "playbook",
        "uuid": "d5f8725f-cf6b-4cf9-b326-56f0074bda85"
      },
      "tags": [],
      "type": "default",
      "uuid": "7118b3ee-519d-43c1-af78-2ac9bc71e885",
      "version": 11
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea\" isExecutable=\"true\" name=\"playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1uwk90m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1uwk90m\u003c/incoming\u003e\u003coutgoing\u003eFlow_04wlg33\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1uwk90m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04wlg33\u003c/incoming\u003e\u003coutgoing\u003eFlow_0chwcrv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_04wlg33\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Record created from IBM SOAR Task ID: {task.id}. Associated IBM SOAR Incident ID: {incident.id}.\\\"\\\"\\\"\\n# This can be true or false. True will add a link to the SOAR incident in a note on the ServiceNow incident.\\ninputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, \\\"sn_add_soar_link_on_snow\\\", False)\\n\\n# If the user adds a comment when they invoke the playbook, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = playbook.inputs.sn_initial_note.content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this task\\ninputs.task_id = task.id\\n\\n# Initial work note to attach to created ServiceNow record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}-{task.id}: {task.name}\\\",\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\")\\n})\\n\\n# if the incident for this task has already been synced,\\n# send this task to the same table in ServiceNow\\n# if not set, defaults to the value set in app.config\\ninputs.sn_table_name = incident.properties.sn_snow_table_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0chwcrv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vyyekt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0chwcrv\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"604b080a-1625-45dc-bca3-52f9a4abe8fe\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vyyekt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1oz0idp\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1vyyekt\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1oz0idp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1oz0idp\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1oz0idp\" id=\"Flow_1oz0idp_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"742\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"824\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vyyekt\" id=\"Flow_1vyyekt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"582\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"658\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0chwcrv\" id=\"Flow_0chwcrv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"498\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04wlg33\" id=\"Flow_04wlg33_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1uwk90m\" id=\"Flow_1uwk90m_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"498\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"658\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"824\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375044767,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
      "description": {
        "content": "NOTE: Since v2.3.0, consider using \"Create Child Incident\" or \"Create Security Response Task\" playbooks which maintain the relationship of the task to the case better than this playbook does.\n\nCreate a new record from the selected task. This will create the new record in the same ServiceNow table (incident vs sn_si_incident) that the SOAR case is associated with. If the case in SOAR isn\u0027t linked to a record in ServiceNow, the table will default to the value set by sn_table_name in the app.config.",
        "format": "text"
      },
      "display_name": "SNOW: Create New Record from Task (PB)",
      "export_key": "snow_create_record_task_pb",
      "field_type_handle": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Create New Record from Task (PB)",
        "export_key": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
        "fields": {
          "sn_add_soar_link_on_snow": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea/sn_add_soar_link_on_snow",
            "hide_notification": false,
            "id": 5853,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "sn_add_soar_link_on_snow",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Add SOAR link to ServiceNow incident",
            "tooltip": "Add SOAR incident link to ServiceNow incident in a note. Defaults to True.",
            "type_id": 1011,
            "uuid": "f5940080-ac48-46fc-b88d-72ce1aa85b94",
            "values": []
          },
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea/sn_assignment_group",
            "hide_notification": false,
            "id": 4979,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1011,
            "uuid": "251d072f-2087-474c-bc74-d079f6d6142d",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "12ca895f-15ea-4440-85d1-811e198cc62a",
                "value": 2043
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "8b78cbd9-5455-4d89-8d29-2001add11745",
                "value": 2044
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "61e6145e-4d88-454b-8cc1-e15262762879",
                "value": 2045
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "3272dcaf-3ab5-4700-96f0-9734aed68b9f",
                "value": 2046
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "21a7dc88-2074-4e15-b7a6-ea90471a5183",
                "value": 2047
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "9f7957e2-92f7-4090-98df-b9021c655e3c",
                "value": 2048
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea/sn_initial_note",
            "hide_notification": false,
            "id": 4980,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "8a89384f-5cfd-4a95-ad9b-cd865d367c1e",
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
        "type_name": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
        "uuid": "1cb65283-9449-4b59-9c3a-338081a5c14f"
      },
      "has_logical_errors": false,
      "id": 11,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743527704007,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375044962,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 26,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375044962,
          "name": "SNOW post-process",
          "object_type": "task",
          "playbook_handle": "snow_create_record_task_pb",
          "programmatic_name": "snow_create_record_task_pb_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n\n  note_text = f\"\"\"\u003cbr\u003eThis Task has been created in \u003cb\u003eServiceNow\u003c/b\u003e in the {results.get(\u0027sn_table_name\u0027)} table.\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  task.addNote(helper.createRichText(note_text))\n\nelif results.get(\"reason\"):\n  task.addNote(results.get(\"reason\"))",
          "tags": [],
          "uuid": "604b080a-1625-45dc-bca3-52f9a4abe8fe"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "Create a new record from the selected task. This will create the new record in the same \nServiceNow table (incident vs sn_si_incident) that the SOAR case is associated with. \nIf the case in SOAR isn\u0027t linked to a record in ServiceNow, \nthe table will default to the value set by sn_table_name in the app.config.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "f5940080-ac48-46fc-b88d-72ce1aa85b94",
            "element": "field_uuid",
            "field_type": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "251d072f-2087-474c-bc74-d079f6d6142d",
            "element": "field_uuid",
            "field_type": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "8a89384f-5cfd-4a95-ad9b-cd865d367c1e",
            "element": "field_uuid",
            "field_type": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_record_task_pb",
      "object_type": "task",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_c1e69c29-d812-47e5-acc1-0c6879a9cfea",
        "id": 13,
        "name": "playbook_c1e69c29_d812_47e5_acc1_0c6879a9cfea",
        "type": "playbook",
        "uuid": "ad23d53f-3ada-4725-886f-cd8cfc23ec81"
      },
      "tags": [],
      "type": "default",
      "uuid": "c1e69c29-d812-47e5-acc1-0c6879a9cfea",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 14,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_3ae0447d_d753_4502_b405_bc15d71c7634\" isExecutable=\"true\" name=\"playbook_3ae0447d_d753_4502_b405_bc15d71c7634\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1pwcmsj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1pwcmsj\u003c/incoming\u003e\u003coutgoing\u003eFlow_09gn2pv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1pwcmsj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09gn2pv\u003c/incoming\u003e\u003coutgoing\u003eFlow_160bxct\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09gn2pv\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003csequenceFlow id=\"Flow_160bxct\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_6\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"5f9be06e-1074-4148-b1c3-6d95cd1d11fd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1hnt7sf\u003c/incoming\u003e\u003coutgoing\u003eFlow_0owltkx\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0owltkx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0owltkx\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Map IBM SOAR severity values to ServiceNow severity values\\nsn_severity_map = {\\n  \\\"High\\\": 1,\\n  \\\"Medium\\\": 2,\\n  \\\"Low\\\": 3\\n}\\n# This can be true or false. True will add a link to the SOAR incident in a note on the ServiceNow incident.\\ninputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, \\\"sn_add_soar_link_on_snow\\\", False)\\n\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Record created from a IBM SOAR Incident ID: {incident.id}.\\n                          Severity: {incident.severity_code}\\n                          Incident Type(s): {\u0027, \u0027.join(incident.incident_type_ids)}\\\"\\\"\\\"\\n\\n# If the user adds a comment when they invoke the rule, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = getattr(playbook.inputs, \\\"sn_initial_note\\\", None).content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# Initial work note to attach to created ServiceNow Record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Map severity for SIR table\\nseverity = sn_severity_map[incident.severity_code]\\n\\n# Parse the priority number value from the priority text input\\npriority = int(playbook.inputs.sn_priority[0])\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}: {incident.name}\\\",\\n  \\\"business_criticality\\\": severity,\\n  \\\"priority\\\": priority,\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\")\\n})\\n\\n# This makes sure this creates this record in the \\\"sn_si_incident\\\" table\\ninputs.sn_table_name = \\\"sn_si_incident\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_160bxct\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hnt7sf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1hnt7sf\" sourceRef=\"ServiceTask_6\" targetRef=\"ScriptTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_3ae0447d_d753_4502_b405_bc15d71c7634\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hnt7sf\" id=\"Flow_1hnt7sf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"572\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0owltkx\" id=\"Flow_0owltkx_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"722\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"784\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_160bxct\" id=\"Flow_160bxct_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"488\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09gn2pv\" id=\"Flow_09gn2pv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1pwcmsj\" id=\"Flow_1pwcmsj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"784\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"488\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375045605,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
      "description": {
        "content": "Creates a new record in the Security Incident (sn_si_incident) table in ServiceNow. Note that this option is only available if your ServiceNow instance is configured with the Security Response module.",
        "format": "text"
      },
      "display_name": "SNOW: Create New Security Incident (PB)",
      "export_key": "snow_create_new_security_incident_pb",
      "field_type_handle": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Create New Security Incident (PB)",
        "export_key": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
        "fields": {
          "sn_add_soar_link_on_snow": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634/sn_add_soar_link_on_snow",
            "hide_notification": false,
            "id": 5854,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "sn_add_soar_link_on_snow",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Add SOAR link to ServiceNow incident",
            "tooltip": "Add SOAR incident link to ServiceNow incident in a note. Defaults to True.",
            "type_id": 1012,
            "uuid": "4ccfa810-4778-4cbc-98c1-2d187ef6f470",
            "values": []
          },
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634/sn_assignment_group",
            "hide_notification": false,
            "id": 4981,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1012,
            "uuid": "e9116013-f50d-4a22-a110-6ba426998d14",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "7aa0c8aa-ab53-4a18-aa64-4fb29a97abe8",
                "value": 2049
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "94926972-d9c2-4852-8bc6-0625b32b947e",
                "value": 2050
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "09fa796f-5657-4ba4-b41b-99fdcaeb8e6a",
                "value": 2051
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "8d2434e7-1961-417d-a272-d31b6ac52c54",
                "value": 2052
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "9bec94cd-ac5a-4a9e-a9b1-f27f0e619080",
                "value": 2053
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "2dee7af0-b270-4c66-b8a0-535a3bcf158f",
                "value": 2054
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634/sn_initial_note",
            "hide_notification": false,
            "id": 4982,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "2f07c329-98cb-4b5c-b058-7b5465d4c9f7",
            "values": []
          },
          "sn_priority": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634/sn_priority",
            "hide_notification": false,
            "id": 4983,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_priority",
            "operation_perms": {},
            "operations": [],
            "placeholder": "4 - Low",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Priority",
            "tooltip": "Priority to set for this record in ServiceNow. Defaults to \"4 - Low\"",
            "type_id": 1012,
            "uuid": "b42de12f-64fe-4615-9ab8-670830daef9e",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1 - Critical",
                "properties": null,
                "uuid": "b9c9b1c6-bc63-486b-a072-2c7982188177",
                "value": 2055
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "2 - High",
                "properties": null,
                "uuid": "a5c768dd-7d3d-4f49-9634-eefae3547599",
                "value": 2056
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "3 - Moderate",
                "properties": null,
                "uuid": "34959670-fb95-47b6-a150-ae31f636281e",
                "value": 2057
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "4 - Low",
                "properties": null,
                "uuid": "acb114eb-400c-4d4c-aa6a-63ceeebf81a4",
                "value": 2058
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "5 - Planning",
                "properties": null,
                "uuid": "ebf8fa93-3c65-47ff-b0fa-7410f1b54d69",
                "value": 2059
              }
            ]
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
        "type_name": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
        "uuid": "d36a72ee-3dfa-4186-8630-ad981dbd5917"
      },
      "has_logical_errors": false,
      "id": 12,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743527737075,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375045842,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 27,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375045842,
          "name": "SNOW post-process",
          "object_type": "incident",
          "playbook_handle": "snow_create_new_security_incident_pb",
          "programmatic_name": "snow_create_new_security_incident_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n  # Set incident fields sn_snow_record_id, sn_snow_record_link, and sn_snow_table_name\n  incident.sn_snow_record_id = results.get(\"sn_ref_id\")\n  incident.sn_snow_record_link = f\"\"\"\u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003eLink\u003c/a\u003e\"\"\"\n  incident.sn_snow_table_name = results.get(\"sn_table_name\")\n\n  noteText = f\"\"\"\u003cbr\u003eThis Incident has been created in \u003cb\u003eServiceNow\u003c/b\u003e with Priority \u0027{playbook.inputs.sn_priority}\u0027 in the {results.get(\u0027sn_table_name\u0027)} table.\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  incident.addNote(helper.createRichText(noteText))\n",
          "tags": [],
          "uuid": "5f9be06e-1074-4148-b1c3-6d95cd1d11fd"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "not_has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "Creates a new record in the Security Incident (sn_si_incident) table in ServiceNow. \nNote that this option is only available if your ServiceNow instance is configured \nwith the Security Response module.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "4ccfa810-4778-4cbc-98c1-2d187ef6f470",
            "element": "field_uuid",
            "field_type": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "e9116013-f50d-4a22-a110-6ba426998d14",
            "element": "field_uuid",
            "field_type": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "2f07c329-98cb-4b5c-b058-7b5465d4c9f7",
            "element": "field_uuid",
            "field_type": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose the optional \u0026quot;Priority\u0026quot; value for this incident in ServiceNow. \nThe \u0026quot;Business Impact\u0026quot; value in ServiceNow is set automatically and \nsynced with the severity of the SOAR case.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b42de12f-64fe-4615-9ab8-670830daef9e",
            "element": "field_uuid",
            "field_type": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_new_security_incident_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_3ae0447d-d753-4502-b405-bc15d71c7634",
        "id": 14,
        "name": "playbook_3ae0447d_d753_4502_b405_bc15d71c7634",
        "type": "playbook",
        "uuid": "56dcf18c-c897-428c-a352-b77334fefaaf"
      },
      "tags": [],
      "type": "default",
      "uuid": "3ae0447d-d753-4502-b405-bc15d71c7634",
      "version": 17
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a323b37c_940b_40bb_8833_84da0340ecb8\" isExecutable=\"true\" name=\"playbook_a323b37c_940b_40bb_8833_84da0340ecb8\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1uwk90m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user_group\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"name\\\"\\n\\n# The value to equate the cell to\\n# Get the group name from the Rule Activity Field with:\\ninputs.sn_query_value = getattr(playbook.inputs, \\\"sn_assignment_group\\\", None)\\n\\n## OR Set group name statically with:\\n## inputs.sn_query_value = \\\"IT Securities\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"assignment_group\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1uwk90m\u003c/incoming\u003e\u003coutgoing\u003eFlow_04wlg33\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1uwk90m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sys_user\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"user_name\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = \\\"ibmresilient\\\" #our integrations user in ServiceNow\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"caller_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04wlg33\u003c/incoming\u003e\u003coutgoing\u003eFlow_0chwcrv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_04wlg33\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Create Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"041fa8ca-70bb-44b1-996b-88f61a8a0671\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Default text of the initial note added to the ServiceNow Record\\ninit_snow_note_text = f\\\"\\\"\\\"Response Task created from IBM SOAR Task ID: {task.id}. Associated IBM SOAR Incident ID: {incident.id}. Parent incident in SerivceNow: {incident.properties.sn_snow_record_id}\\\"\\\"\\\"\\n# This can be true or false. True will add a link to the SOAR incident in a note on the ServiceNow incident.\\ninputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, \\\"sn_add_soar_link_on_snow\\\", None)\\n\\n# If the user adds a comment when they invoke the playbook, that comment gets concatenated here\\ninitial_note = None\\nif getattr(playbook.inputs, \\\"sn_initial_note\\\", None):\\n  initial_note = playbook.inputs.sn_initial_note.content\\nif initial_note:\\n  init_snow_note_text = f\\\"{init_snow_note_text}\\\\n\\\\n{initial_note}\\\"\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# ID of this task\\ninputs.task_id = task.id\\n\\n# Initial work note to attach to created ServiceNow record\\ninputs.sn_init_work_note = init_snow_note_text\\n\\n# Parse the priority number value from the priority text input\\npriority = int(playbook.inputs.sn_priority[0])\\n\\n# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.\\n# ServiceNow Example: setValue(\u0027assignment_group\u0027, request.body.data.sn_optional_fields.assignment_group)\\ninputs.sn_optional_fields = dumps({\\n  \\\"short_description\\\": f\\\"RES-{incident.id}-{task.id}: {task.name}\\\",\\n  \\\"assignment_group\\\": playbook.functions.results.assignment_group.get(\\\"sys_id\\\"),\\n  \\\"caller_id\\\": playbook.functions.results.caller_id.get(\\\"sys_id\\\"),\\n  \\\"parent\\\": playbook.functions.results.parent_inc_sys_id.get(\\\"sys_id\\\"),\\n  \\\"priority\\\": priority\\n})\\n\\n# this specifc Playbook only will run to create recrods in the sn_si_task table\\ninputs.sn_table_name = \\\"sn_si_task\\\"\\n\\n# because we\u0027re creating a child incident here, set the parent REF ID\\ninputs.sn_parent_ref_id = incident.properties.sn_snow_record_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0olhihg\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vyyekt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0chwcrv\" sourceRef=\"ServiceTask_2\" targetRef=\"ServiceTask_6\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"75cbabd1-610f-47d4-a2f9-d20da1571be1\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vyyekt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1oz0idp\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1vyyekt\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1oz0idp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1oz0idp\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003cserviceTask id=\"ServiceTask_6\" name=\"SNOW: Lookup sys_id\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5abf91c-57f6-4d01-bd5a-50bfe261cb01\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The table in ServiceNow to query\\ninputs.sn_table_name = \\\"sn_si_incident\\\"\\n\\n# The name of the field/table column to query\\ninputs.sn_query_field = \\\"number\\\"\\n\\n# The value to equate the cell to\\ninputs.sn_query_value = incident.properties.sn_snow_record_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"parent_inc_sys_id\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0chwcrv\u003c/incoming\u003e\u003coutgoing\u003eFlow_0olhihg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0olhihg\" sourceRef=\"ServiceTask_6\" targetRef=\"ServiceTask_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a323b37c_940b_40bb_8833_84da0340ecb8\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0olhihg\" id=\"Flow_0olhihg_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"582\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"648\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1oz0idp\" id=\"Flow_1oz0idp_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"892\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"974\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vyyekt\" id=\"Flow_1vyyekt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"732\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"808\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0chwcrv\" id=\"Flow_0chwcrv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"498\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04wlg33\" id=\"Flow_04wlg33_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1uwk90m\" id=\"Flow_1uwk90m_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"648\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"808\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"974\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_6\" id=\"ServiceTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"497.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375046453,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
      "description": {
        "content": "Create a Security Response Task linked to the parent Security Incident of this task\u0027s parent incident.",
        "format": "text"
      },
      "display_name": "SNOW: Create Security Response Task (PB)",
      "export_key": "snow_create_security_response_task_pb",
      "field_type_handle": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Create Security Response Task (PB)",
        "export_key": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
        "fields": {
          "sn_add_soar_link_on_snow": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8/sn_add_soar_link_on_snow",
            "hide_notification": false,
            "id": 5855,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "sn_add_soar_link_on_snow",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Add SOAR link to ServiceNow incident",
            "tooltip": "Add SOAR incident link to ServiceNow incident in a note.",
            "type_id": 1013,
            "uuid": "66fbf2cd-6b97-4aaa-a3ec-45627f7d21c8",
            "values": []
          },
          "sn_assignment_group": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8/sn_assignment_group",
            "hide_notification": false,
            "id": 4984,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_assignment_group",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Assignment Group",
            "tooltip": "The group this record will be assigned to in ServiceNow",
            "type_id": 1013,
            "uuid": "517a0d61-ae0f-41fd-b3a5-f1478cac031a",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "IT Securities",
                "properties": null,
                "uuid": "12ca895f-15ea-4440-85d1-811e198cc62a",
                "value": 2060
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Network",
                "properties": null,
                "uuid": "8b78cbd9-5455-4d89-8d29-2001add11745",
                "value": 2061
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Hardware",
                "properties": null,
                "uuid": "61e6145e-4d88-454b-8cc1-e15262762879",
                "value": 2062
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Software",
                "properties": null,
                "uuid": "3272dcaf-3ab5-4700-96f0-9734aed68b9f",
                "value": 2063
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Database",
                "properties": null,
                "uuid": "21a7dc88-2074-4e15-b7a6-ea90471a5183",
                "value": 2064
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "Incident Management",
                "properties": null,
                "uuid": "9f7957e2-92f7-4090-98df-b9021c655e3c",
                "value": 2065
              }
            ]
          },
          "sn_initial_note": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8/sn_initial_note",
            "hide_notification": false,
            "id": 4985,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "sn_initial_note",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Initial Note",
            "tooltip": "",
            "type_id": 1013,
            "uuid": "1bd25ab3-b4ca-4700-b3c0-38da94e33c16",
            "values": []
          },
          "sn_priority": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8/sn_priority",
            "hide_notification": false,
            "id": 4986,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_priority",
            "operation_perms": {},
            "operations": [],
            "placeholder": "4 - Low",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Priority",
            "tooltip": "Priority to set for this record in ServiceNow. Defaults to \"4 - Low\"",
            "type_id": 1013,
            "uuid": "e6f4d15e-b95f-4f43-8b53-b239ee960063",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1 - Critical",
                "properties": null,
                "uuid": "b2f1a8b4-3d9b-4fc9-9e58-2ed4ed5f3400",
                "value": 2066
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "2 - High",
                "properties": null,
                "uuid": "d0ecbcf3-70a0-4865-897b-ac3b1d605cab",
                "value": 2067
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "3 - Moderate",
                "properties": null,
                "uuid": "72a74a84-be59-42ef-b563-7394c61c655f",
                "value": 2068
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "4 - Low",
                "properties": null,
                "uuid": "a33df8d5-1f2d-426a-b205-32864879c7e4",
                "value": 2069
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "5 - Planning",
                "properties": null,
                "uuid": "f1fb8586-c5e8-4057-b7a5-f31c28a729e3",
                "value": 2070
              }
            ]
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
        "type_name": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
        "uuid": "7b1206f3-9734-4458-8954-b89a745956de"
      },
      "has_logical_errors": false,
      "id": 13,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743527752100,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375046767,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 28,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375046767,
          "name": "SNOW post-process",
          "object_type": "task",
          "playbook_handle": "snow_create_security_response_task_pb",
          "programmatic_name": "snow_create_security_response_task_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.create_record\nif results.get(\"success\"):\n\n  note_text = f\"\"\"\u003cbr\u003eThis Task has been created in \u003cb\u003eServiceNow\u003c/b\u003e with Priority \u0027{playbook.inputs.sn_priority}\u0027 in the {results.get(\u0027sn_table_name\u0027)} table as a Security Response Task for parent Security Incident {incident.properties.sn_snow_record_id} ({incident.properties.sn_snow_record_link.content}).\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e  {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Link:\u003c/b\u003e \u003ca href=\u0027{results.get(\u0027sn_record_link\u0027)}\u0027\u003e{results.get(\u0027sn_record_link\u0027)}\u003c/a\u003e\"\"\"\n\n  task.addNote(helper.createRichText(note_text))\n\nelif results.get(\"reason\"):\n  task.addNote(results.get(\"reason\"))\n",
          "tags": [],
          "uuid": "75cbabd1-610f-47d4-a2f9-d20da1571be1"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_table_name",
              "method": "equals",
              "type": null,
              "value": "sn_si_incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "\u003cb\u003eCreate security response task off parent record in SNOW\u003c/b\u003e\u003cbr /\u003e\n\nThis playbook will run to create this task as a record in ServiceNow with a \u0026quot;parent incident\u0026quot; link\nset to the linked record of this incident.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "66fbf2cd-6b97-4aaa-a3ec-45627f7d21c8",
            "element": "field_uuid",
            "field_type": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "517a0d61-ae0f-41fd-b3a5-f1478cac031a",
            "element": "field_uuid",
            "field_type": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "1bd25ab3-b4ca-4700-b3c0-38da94e33c16",
            "element": "field_uuid",
            "field_type": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "e6f4d15e-b95f-4f43-8b53-b239ee960063",
            "element": "field_uuid",
            "field_type": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_create_security_response_task_pb",
      "object_type": "task",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a323b37c-940b-40bb-8833-84da0340ecb8",
        "id": 15,
        "name": "playbook_a323b37c_940b_40bb_8833_84da0340ecb8",
        "type": "playbook",
        "uuid": "f33e56cd-45df-4230-a90b-cfdc5578226c"
      },
      "tags": [],
      "type": "default",
      "uuid": "a323b37c-940b-40bb-8833-84da0340ecb8",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c\" isExecutable=\"true\" name=\"playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1k8fj92\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Add Note to Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c43f8cc1-5cdc-41a6-a6b0-fa59dd32df36\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"908e2bd1-d682-44e1-9240-efb5c2bf23a1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"19d5e854-dc64-43d4-9a39-7be914920ad6\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"c65de77d-f6b2-4c19-94eb-cdfa5cf5037f\"}},\"ba318261-ed6a-4a38-a187-9e0b68d1604f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.sn_note_type = \\\"additional_comment\\\"\\n# The id of this incident\\ninputs.incident_id = incident.id\\n\\n# If this is a task note, get the taskId\\nif note.type == \u0027task\u0027:\\n  # Set the task_id\\n  inputs.task_id = task.id\\n\\n# Get the text of the note\\ninputs.sn_note_text = note.text.content\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1k8fj92\u003c/incoming\u003e\u003coutgoing\u003eFlow_1dk6y8d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1k8fj92\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"60fecb55-7cbb-4ade-803f-d75bf5fa98b5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1dk6y8d\u003c/incoming\u003e\u003coutgoing\u003eFlow_1urnpky\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1dk6y8d\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1urnpky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1urnpky\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1urnpky\" id=\"Flow_1urnpky_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"382\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dk6y8d\" id=\"Flow_1dk6y8d_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"298\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1k8fj92\" id=\"Flow_1k8fj92_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.5667\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"298\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375047474,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "SNOW: Send as Additional Comment (PB)",
      "export_key": "snow_send_as_additional_comment_pb",
      "field_type_handle": "playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Send as Additional Comment (PB)",
        "export_key": "playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c",
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
        "type_name": "playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c",
        "uuid": "52d68bef-f011-49f0-a16f-3e9f64d7dc27"
      },
      "has_logical_errors": false,
      "id": 14,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509539498,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375047628,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 29,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375047628,
          "name": "SNOW post-process",
          "object_type": "note",
          "playbook_handle": "snow_send_as_additional_comment_pb",
          "programmatic_name": "snow_send_as_additional_comment_pb_post_process",
          "script_text": "from datetime import datetime\nnote.text = f\"\u003cb\u003eSent to ServiceNow at {datetime.now()}\u003c/b\u003e\u003cbr\u003e{note.text.content}\"",
          "tags": [],
          "uuid": "60fecb55-7cbb-4ade-803f-d75bf5fa98b5"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "note.text",
              "method": "not_contains",
              "type": null,
              "value": "Sent to ServiceNow at"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "snow_send_as_additional_comment_pb",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_fae27efd-55f8-4473-b9f2-c044a0b6a97c",
        "id": 16,
        "name": "playbook_fae27efd_55f8_4473_b9f2_c044a0b6a97c",
        "type": "playbook",
        "uuid": "13eda8cc-3269-46f0-bfb9-9b1c1cc7516e"
      },
      "tags": [],
      "type": "default",
      "uuid": "fae27efd-55f8-4473-b9f2-c044a0b6a97c",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06\" isExecutable=\"true\" name=\"playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1el4yjo\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Add Note to Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c43f8cc1-5cdc-41a6-a6b0-fa59dd32df36\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"908e2bd1-d682-44e1-9240-efb5c2bf23a1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"19d5e854-dc64-43d4-9a39-7be914920ad6\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"c65de77d-f6b2-4c19-94eb-cdfa5cf5037f\"}},\"ba318261-ed6a-4a38-a187-9e0b68d1604f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.sn_note_type = \\\"work_note\\\"\\n# The id of this incident\\ninputs.incident_id = incident.id\\n\\n# If this is a task note, get the taskId\\nif note.type == \u0027task\u0027:\\n  # Set the task_id\\n  inputs.task_id = task.id\\n\\n# Get the text of the note\\ninputs.sn_note_text = note.text.content\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1el4yjo\u003c/incoming\u003e\u003coutgoing\u003eFlow_12cxyxn\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1el4yjo\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f3e64ae6-3ba9-406b-ab9a-5a2b8b013abc\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12cxyxn\u003c/incoming\u003e\u003coutgoing\u003eFlow_06e0j7j\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_12cxyxn\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_06e0j7j\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_06e0j7j\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06e0j7j\" id=\"Flow_06e0j7j_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"382\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"454\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12cxyxn\" id=\"Flow_12cxyxn_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"298\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1el4yjo\" id=\"Flow_1el4yjo_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.5667\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"298\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"454\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375048319,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "SNOW: Send as Work Note (PB)",
      "export_key": "snow_send_as_work_note_pb",
      "field_type_handle": "playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Send as Work Note (PB)",
        "export_key": "playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06",
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
        "type_name": "playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06",
        "uuid": "cee26ce2-c81f-46ed-a249-e415c5e9df96"
      },
      "has_logical_errors": false,
      "id": 15,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509540320,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375048470,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 30,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375048470,
          "name": "SNOW post-process",
          "object_type": "note",
          "playbook_handle": "snow_send_as_work_note_pb",
          "programmatic_name": "snow_send_as_work_note_pb_post_process",
          "script_text": "from datetime import datetime\nnote.text = f\"\u003cb\u003eSent to ServiceNow at {datetime.now()}\u003c/b\u003e\u003cbr\u003e{note.text.content}\"",
          "tags": [],
          "uuid": "f3e64ae6-3ba9-406b-ab9a-5a2b8b013abc"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "note.text",
              "method": "not_contains",
              "type": null,
              "value": "Sent to ServiceNow at"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "snow_send_as_work_note_pb",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_64920ab3-7a3f-49a4-bfd0-eaac83149e06",
        "id": 17,
        "name": "playbook_64920ab3_7a3f_49a4_bfd0_eaac83149e06",
        "type": "playbook",
        "uuid": "3ddf7aac-d0a3-4d85-83c4-b5c36f64e7d9"
      },
      "tags": [],
      "type": "default",
      "uuid": "64920ab3-7a3f-49a4-bfd0-eaac83149e06",
      "version": 6
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.plan_status",
              "method": "changed",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1\" isExecutable=\"true\" name=\"playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0fr6c68\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW Helper: Update Data Table\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6130c083-17ea-4262-986b-8d073d3f7328\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# Get the incident id\\ninputs.incident_id = incident.id\\n\\n# Get the new status of the incident\\ninputs.sn_resilient_status = incident.plan_status\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_data_table\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0fr6c68\u003c/incoming\u003e\u003coutgoing\u003eFlow_08aob7k\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0fr6c68\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_08aob7k\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_08aob7k\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08aob7k\" id=\"Flow_08aob7k_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"294\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fr6c68\" id=\"Flow_0fr6c68_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"294\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375049246,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "SNOW: Update Data Table on Status Change [Incident] (PB)",
      "export_key": "snow_update_data_table_on_status_change_incident_pb",
      "field_type_handle": "playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update Data Table on Status Change [Incident] (PB)",
        "export_key": "playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1",
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
        "type_name": "playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1",
        "uuid": "84b5995f-5b06-4a7d-83c4-6f3ef9721e62"
      },
      "has_logical_errors": false,
      "id": 16,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1744121687650,
      "local_scripts": [],
      "name": "snow_update_data_table_on_status_change_incident_pb",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_220a34cb-6f4e-4cd4-8feb-854fed31bea1",
        "id": 18,
        "name": "playbook_220a34cb_6f4e_4cd4_8feb_854fed31bea1",
        "type": "playbook",
        "uuid": "47219148-db2e-4d05-a001-49a241e8f2f4"
      },
      "tags": [],
      "type": "default",
      "uuid": "220a34cb-6f4e-4cd4-8feb-854fed31bea1",
      "version": 8
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "task.status",
              "method": "changed",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc\" isExecutable=\"true\" name=\"playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_14kgw9i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW Helper: Update Data Table\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6130c083-17ea-4262-986b-8d073d3f7328\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# Get the incident id\\ninputs.incident_id = incident.id\\n\\n# Get the task id\\ninputs.task_id = task.id\\n\\n# Get the new status of the task\\ninputs.sn_resilient_status = task.status\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_data_table\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14kgw9i\u003c/incoming\u003e\u003coutgoing\u003eFlow_0c6uea7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_14kgw9i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0c6uea7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0c6uea7\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0c6uea7\" id=\"Flow_0c6uea7_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"324\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14kgw9i\" id=\"Flow_14kgw9i_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"324\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375050137,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "SNOW: Update Data Table on Status Change [Task] (PB)",
      "export_key": "snow_update_data_table_on_status_change_task_pb",
      "field_type_handle": "playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update Data Table on Status Change [Task] (PB)",
        "export_key": "playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc",
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
        "type_name": "playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc",
        "uuid": "164b7808-1750-4033-ad58-d44e1defc1db"
      },
      "has_logical_errors": false,
      "id": 17,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1744121688691,
      "local_scripts": [],
      "name": "snow_update_data_table_on_status_change_task_pb",
      "object_type": "task",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_e6abcf71-4c86-44fd-82e2-f72fcf64d6dc",
        "id": 19,
        "name": "playbook_e6abcf71_4c86_44fd_82e2_f72fcf64d6dc",
        "type": "playbook",
        "uuid": "24c8c172-652f-46cd-b2b4-5261e973e498"
      },
      "tags": [],
      "type": "default",
      "uuid": "e6abcf71-4c86-44fd-82e2-f72fcf64d6dc",
      "version": 8
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
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
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_26e860aa_1826_44cd_8108_3d468e98cd87\" isExecutable=\"true\" name=\"playbook_26e860aa_1826_44cd_8108_3d468e98cd87\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0wwhag2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Update Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"95d7d4df-0ec8-4dbd-bbcf-9759b23930eb\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from json import dumps\\n# Map IBM SOAR severity values to ServiceNow severity values\\nsn_severity_map = {\\n  \\\"High\\\": 1,\\n  \\\"Medium\\\": 2,\\n  \\\"Low\\\": 3\\n}\\n\\n# Get the id of this incident\\ninputs.incident_id = incident.id\\n\\n# in INC table, severity is called \u0027impact\u0027; in SIR table, it is called \u0027business_criticality\u0027\\nseverity_field_name = \\\"business_criticality\\\" if incident.properties.sn_snow_table_name == \\\"sn_si_incident\\\" else \\\"impact\\\"\\n\\n# List all the fields you want to update in the ServiceNow Record here with the ServiceNow field_name being the key\\ninputs.sn_update_fields = dumps({\\n  severity_field_name: sn_severity_map[incident.severity_code]\\n})\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wwhag2\u003c/incoming\u003e\u003coutgoing\u003eFlow_0g99ya7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0wwhag2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process update\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a7f6904f-29d0-4fa0-a338-0ca4fe49e393\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0g99ya7\u003c/incoming\u003e\u003coutgoing\u003eFlow_05exjux\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0g99ya7\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"SNOW: Add Note to Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c43f8cc1-5cdc-41a6-a6b0-fa59dd32df36\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"908e2bd1-d682-44e1-9240-efb5c2bf23a1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"19d5e854-dc64-43d4-9a39-7be914920ad6\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"c65de77d-f6b2-4c19-94eb-cdfa5cf5037f\"}},\"ba318261-ed6a-4a38-a187-9e0b68d1604f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.sn_note_text = f\\\"The Severity of this Incident was updated to {incident.severity_code} in IBM SOAR\\\"\\ninputs.sn_note_type = \\\"work_note\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_05exjux\u003c/incoming\u003e\u003coutgoing\u003eFlow_0psgqgq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_05exjux\" sourceRef=\"ScriptTask_2\" targetRef=\"ServiceTask_3\"/\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0psgqgq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0psgqgq\" sourceRef=\"ServiceTask_3\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_26e860aa_1826_44cd_8108_3d468e98cd87\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0psgqgq\" id=\"Flow_0psgqgq_di\"\u003e\u003comgdi:waypoint x=\"1420\" y=\"622\"/\u003e\u003comgdi:waypoint x=\"1420\" y=\"684\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_05exjux\" id=\"Flow_05exjux_di\"\u003e\u003comgdi:waypoint x=\"1420\" y=\"462\"/\u003e\u003comgdi:waypoint x=\"1420\" y=\"538\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0g99ya7\" id=\"Flow_0g99ya7_di\"\u003e\u003comgdi:waypoint x=\"1420\" y=\"332\"/\u003e\u003comgdi:waypoint x=\"1420\" y=\"378\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wwhag2\" id=\"Flow_0wwhag2_di\"\u003e\u003comgdi:waypoint x=\"1420\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"1420\" y=\"248\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"1326\" y=\"134\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1322\" y=\"248\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1322\" y=\"378\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"1322\" y=\"538\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"1354\" y=\"684\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375050838,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_26e860aa_1826_44cd_8108_3d468e98cd87",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "SNOW: Update Record on Severity Change (PB)",
      "export_key": "snow_inc_update_record_on_severity_change_pb",
      "field_type_handle": "playbook_26e860aa_1826_44cd_8108_3d468e98cd87",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update Record on Severity Change (PB)",
        "export_key": "playbook_26e860aa_1826_44cd_8108_3d468e98cd87",
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
        "type_name": "playbook_26e860aa_1826_44cd_8108_3d468e98cd87",
        "uuid": "565a8c94-4123-4e22-86e7-8a36f2cf4364"
      },
      "has_logical_errors": false,
      "id": 18,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1744121689724,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375051021,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process update",
          "id": 31,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375051021,
          "name": "SNOW post-process update",
          "object_type": "incident",
          "playbook_handle": "snow_inc_update_record_on_severity_change_pb",
          "programmatic_name": "snow_inc_update_record_on_severity_change_pb_post_process_update",
          "script_text": "# Add a Note to the Incident\nincident.addNote(f\"The Severity of this Incident was updated to {incident.severity_code} in IBM SOAR\")",
          "tags": [],
          "uuid": "a7f6904f-29d0-4fa0-a338-0ca4fe49e393"
        }
      ],
      "name": "snow_inc_update_record_on_severity_change_pb",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_26e860aa-1826-44cd-8108-3d468e98cd87",
        "id": 20,
        "name": "playbook_26e860aa_1826_44cd_8108_3d468e98cd87",
        "type": "playbook",
        "uuid": "1a30ce9c-d9a2-4a91-8161-dc8650ed4677"
      },
      "tags": [],
      "type": "default",
      "uuid": "26e860aa-1826-44cd-8108-3d468e98cd87",
      "version": 10
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 5,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f\" isExecutable=\"true\" name=\"playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_030xauf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\n# Codes prepended with [SIR] are specific to Security Incident Response incidents\\nmap_sn_record_states = {\\n  \\\"New\\\": 1,\\n  \\\"In Progress\\\": 2,\\n  \\\"On Hold\\\": 3,\\n  \\\"Resolved\\\": 6,\\n  \\\"Closed\\\": 7,\\n  \\\"Canceled\\\": 8,\\n  \\\"Cancelled\\\": 8 # servicenow has inconsistent spellings of this word...\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The state to change the record to\\n# inputs.sn_record_state = map_sn_record_states[\\\"Closed\\\"]\\ninputs.sn_record_state = map_sn_record_states[getattr(playbook.inputs, \\\"sn_record_state\\\", None)]\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\n# inputs.sn_close_notes = \\\"This incident has been resolved in IBM SOAR. No further action required\\\"\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# The ServiceNow \u0027close_code\u0027 that you normally select when closing a ServiceNow record\\n# inputs.sn_close_code = \\\"Solved (Permanently)\\\"\\nif getattr(playbook.inputs, \\\"sn_close_code\\\", None):\\n  inputs.sn_close_code = getattr(playbook.inputs, \\\"sn_close_code\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_030xauf\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wztaau\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_030xauf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"82a425ab-8d3e-48a0-8672-e12b9b498585\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wztaau\u003c/incoming\u003e\u003coutgoing\u003eFlow_085mkuv\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0wztaau\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_085mkuv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_085mkuv\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_085mkuv\" id=\"Flow_085mkuv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wztaau\" id=\"Flow_0wztaau_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_030xauf\" id=\"Flow_030xauf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375051700,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
      "description": {
        "content": "Update the state of this record in the incident table in ServiceNow",
        "format": "text"
      },
      "display_name": "SNOW: Update/Close Incident (PB)",
      "export_key": "snow_updateclose_record_incident_pb",
      "field_type_handle": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update/Close Incident (PB)",
        "export_key": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
        "fields": {
          "sn_close_code": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f/sn_close_code",
            "hide_notification": false,
            "id": 4987,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_code",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Code",
            "tooltip": "Optional. Sets the close code only when Record State is CLOSED",
            "type_id": 1019,
            "uuid": "6cb1f7f0-6f52-428a-8150-d9c8c80f38e8",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Work Around)",
                "properties": null,
                "uuid": "6246c121-b899-4de6-bbc0-fd9ab17b519f",
                "value": 2071
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Permanently)",
                "properties": null,
                "uuid": "456aaad5-e5c6-4277-a45e-c763a6ed14e2",
                "value": 2072
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Not Reproducible)",
                "properties": null,
                "uuid": "4c6c687c-f7c5-4c32-b82c-7da832816648",
                "value": 2073
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Too Costly)",
                "properties": null,
                "uuid": "9a83ffb2-48b8-4878-aa86-9374f31a5ee1",
                "value": 2074
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed/Resolved by Caller",
                "properties": null,
                "uuid": "478b2383-cd13-454e-8e62-af786e502697",
                "value": 2075
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Investigation completed",
                "properties": null,
                "uuid": "5f721fba-73c4-4d8f-a0fc-eca2cd76a61d",
                "value": 2076
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Threat mitigated",
                "properties": null,
                "uuid": "4e98ad83-5d6f-44ac-ac39-6298d0b23ff5",
                "value": 2077
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Patched vulnerability",
                "properties": null,
                "uuid": "397905a1-b60a-4be1-9905-10339e7796f9",
                "value": 2078
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Invalid vulnerability",
                "properties": null,
                "uuid": "3222705e-b4b4-425a-bee7-df4ce396b938",
                "value": 2079
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not resolved",
                "properties": null,
                "uuid": "2acee495-0ea0-4422-a9d3-97138a1661c7",
                "value": 2080
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "False positive",
                "properties": null,
                "uuid": "ed73ffd2-1ca9-4315-8363-0ec44704c902",
                "value": 2081
              }
            ]
          },
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f/sn_close_notes",
            "hide_notification": false,
            "id": 4988,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1019,
            "uuid": "99faf2a3-bd94-42b2-9c9d-54815f154016",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f/sn_record_state",
            "hide_notification": false,
            "id": 4989,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "",
            "type_id": 1019,
            "uuid": "e1e3ccb6-8f31-4416-87b4-1778210de08f",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "In Progress",
                "properties": null,
                "uuid": "9dd792dc-445a-4fbf-a800-d2cbfa513f30",
                "value": 2082
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "On Hold",
                "properties": null,
                "uuid": "8f951b6d-ca82-432e-ac3c-831eb890c045",
                "value": 2083
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Resolved",
                "properties": null,
                "uuid": "2e74025e-1752-4abf-98b3-9260b6cb1a1b",
                "value": 2084
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "0b8ab77e-9aa8-4022-b35d-e7dac6b78b07",
                "value": 2086
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Canceled",
                "properties": null,
                "uuid": "3fb10eb3-f5c3-4c7b-927a-434dc2fea2a0",
                "value": 2087
              }
            ]
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
        "type_name": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
        "uuid": "628e0198-3bc9-4e42-b54e-2bef6f3d569a"
      },
      "has_logical_errors": false,
      "id": 19,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509541762,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375051975,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 32,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375051975,
          "name": "SNOW post-process",
          "object_type": "incident",
          "playbook_handle": "snow_updateclose_record_incident_pb",
          "programmatic_name": "snow_updateclose_record_incident_pb_post_process",
          "script_text": "results = playbook.functions.results.close_record\nif results.get(\"success\"):\n  note_text = f\"\"\"\u003cbr\u003eThis Incident has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\nelse:\n  note_text = f\"\"\"\u003cbr\u003eFailed to close this Incident in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "82a425ab-8d3e-48a0-8672-e12b9b498585"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_table_name",
              "method": "equals",
              "type": null,
              "value": "incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "If closing the SNOW record all tasks on the SNOW record must be closed in order to close the SNOW record.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "e1e3ccb6-8f31-4416-87b4-1778210de08f",
            "element": "field_uuid",
            "field_type": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6cb1f7f0-6f52-428a-8150-d9c8c80f38e8",
            "element": "field_uuid",
            "field_type": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "99faf2a3-bd94-42b2-9c9d-54815f154016",
            "element": "field_uuid",
            "field_type": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_record_incident_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_536adc5b-6286-4ff2-ae36-72ef17ffc20f",
        "id": 21,
        "name": "playbook_536adc5b_6286_4ff2_ae36_72ef17ffc20f",
        "type": "playbook",
        "uuid": "b5c0ccfe-696e-4c30-b75d-739dad73fa85"
      },
      "tags": [],
      "type": "default",
      "uuid": "536adc5b-6286-4ff2-ae36-72ef17ffc20f",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_edcd1bb4_0249_4a25_bcca_e17347857277\" isExecutable=\"true\" name=\"playbook_edcd1bb4_0249_4a25_bcca_e17347857277\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_077rlcc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\n# Codes prepended with [SIR] are specific to Security Incident Response incidents\\nmap_sn_record_states = {\\n  \\\"New\\\": 1,\\n  \\\"In Progress\\\": 2,\\n  \\\"On Hold\\\": 3,\\n  \\\"Resolved\\\": 6,\\n  \\\"Closed\\\": 7,\\n  \\\"Canceled\\\": 8,\\n  \\\"Cancelled\\\": 8 # servicenow has inconsistent spellings of this word...\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# RES ID of this SNOW record from the Data Table row\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# The state to change the record to\\ninputs.sn_record_state = map_sn_record_states.get(getattr(playbook.inputs, \\\"sn_record_state\\\", None))\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# The ServiceNow \u0027close_code\u0027 that you normally select when closing a ServiceNow record\\nif getattr(playbook.inputs, \\\"sn_close_code\\\", None):\\n  inputs.sn_close_code = getattr(playbook.inputs, \\\"sn_close_code\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_in_sn\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_077rlcc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0vwiu22\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_077rlcc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"488a18f2-a7fd-47c8-9a6b-fc2f367bc634\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vwiu22\u003c/incoming\u003e\u003coutgoing\u003eFlow_103hgzz\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0vwiu22\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_0zqn8dv\" id=\"ConditionPoint_3\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_103hgzz\u003c/incoming\u003e\u003coutgoing\u003eFlow_0b4bf5c\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0zqn8dv\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_103hgzz\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"SNOW Helper: Add Task Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f02d65f0-f19a-414a-828d-5c35de5270b1\"\u003e{\"inputs\":{},\"pre_processing_script\":\"note_text = None\\nresults = playbook.functions.results.close_in_sn\\nif results.get(\\\"success\\\"):\\n  # If successfully closed the record, set below note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;This Task has been updated in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow ID:\u0026lt;/b\u0026gt; {results.get(\u0027sn_ref_id\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Record State:\u0026lt;/b\u0026gt; {results.get(\u0027sn_record_state\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Notes:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Code:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\\\"\\\"\\\"\\nelse:\\n  # Else, it failed, so set this note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;Failed to close this Task in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {results.get(\\\"reason\\\")}\\\"\\\"\\\"\\n\\n# Get sn_res_id from the Data Table\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# Set the sn_note_text input\\ninputs.sn_note_text = note_text\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_task_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0b4bf5c\u003c/incoming\u003e\u003coutgoing\u003eFlow_1nozhak\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1nozhak\u003c/incoming\u003e\u003cincoming\u003eFlow_0zqn8dv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1nozhak\" sourceRef=\"ServiceTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_0b4bf5c\" name=\"do_continue\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"do_continue\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = row.sn_records_dt_type == \\\"Task\\\"\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0zqn8dv\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_edcd1bb4_0249_4a25_bcca_e17347857277\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zqn8dv\" id=\"Flow_0zqn8dv_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"654\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"948.9999999999999\" y=\"523\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0b4bf5c\" id=\"Flow_0b4bf5c_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"556\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"62\" x=\"690\" y=\"583\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nozhak\" id=\"Flow_1nozhak_di\"\u003e\u003comgdi:waypoint x=\"819\" y=\"680\"/\u003e\u003comgdi:waypoint x=\"894\" y=\"680\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_103hgzz\" id=\"Flow_103hgzz_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"504\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vwiu22\" id=\"Flow_0vwiu22_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_077rlcc\" id=\"Flow_077rlcc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"250\" x=\"598\" y=\"504\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"894\" y=\"654\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375052559,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
      "description": {
        "content": "Update the state of this record in the \"incident\" table in ServiceNow",
        "format": "text"
      },
      "display_name": "SNOW: Update/Close Record (PB)",
      "export_key": "snow_updateclose_record_pb",
      "field_type_handle": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update/Close Record (PB)",
        "export_key": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
        "fields": {
          "sn_close_code": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277/sn_close_code",
            "hide_notification": false,
            "id": 4990,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_code",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Code",
            "tooltip": "Optional. Sets the close code only when Record State is CLOSED",
            "type_id": 1020,
            "uuid": "3eca123e-cf0c-4ece-af6b-4c2d87382213",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Work Around)",
                "properties": null,
                "uuid": "56070ec6-50df-41df-ac2b-9771dffabb59",
                "value": 2088
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Permanently)",
                "properties": null,
                "uuid": "b5d4c881-3a1d-4bba-8bb4-839c2fc8817e",
                "value": 2089
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Not Reproducible)",
                "properties": null,
                "uuid": "6df00d88-ff9d-44c3-ac40-0baafea8c517",
                "value": 2090
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Too Costly)",
                "properties": null,
                "uuid": "b9ea1766-1ddc-45d7-bfd1-c9ed3f2237ad",
                "value": 2091
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed/Resolved by Caller",
                "properties": null,
                "uuid": "0df2c9c7-a3c5-469c-9236-6938cf0fa2ad",
                "value": 2092
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Investigation completed",
                "properties": null,
                "uuid": "c72df9f4-1f59-481a-9f16-b8556fd384d2",
                "value": 2093
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Threat mitigated",
                "properties": null,
                "uuid": "7ecb1479-bf7f-41e9-b59d-2d3d9b016737",
                "value": 2094
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Patched vulnerability",
                "properties": null,
                "uuid": "aca5ed90-05a7-466c-9592-2f25e7195288",
                "value": 2095
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Invalid vulnerability",
                "properties": null,
                "uuid": "6cd0fdc3-17bd-4a7c-9dfa-c1d289f0f961",
                "value": 2096
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not resolved",
                "properties": null,
                "uuid": "8bfc2a73-4176-4f74-8514-ffbfb0b0f0ff",
                "value": 2097
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "False positive",
                "properties": null,
                "uuid": "108a8f26-39ed-45a3-b2a1-9099b15faa9b",
                "value": 2098
              }
            ]
          },
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277/sn_close_notes",
            "hide_notification": false,
            "id": 4991,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1020,
            "uuid": "41b3f8e4-53fd-4566-a02d-4b22dfaff152",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277/sn_record_state",
            "hide_notification": false,
            "id": 4992,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "",
            "type_id": 1020,
            "uuid": "93655d2e-3e26-4046-93cd-19cb4903a91a",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "In Progress",
                "properties": null,
                "uuid": "df6a2fcc-8b15-4adc-a699-7c465d92c63b",
                "value": 2100
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "On Hold",
                "properties": null,
                "uuid": "f5fda5e7-1711-4ae2-a5d3-916f515ea2a2",
                "value": 2101
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Resolved",
                "properties": null,
                "uuid": "221e4b37-67fb-4222-8784-805645d537ff",
                "value": 2102
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "630a5021-8d55-46d0-ad9d-8e99229ee356",
                "value": 2103
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Canceled",
                "properties": null,
                "uuid": "e2d77043-a7dd-4619-9770-102b2fa8f59e",
                "value": 2105
              }
            ]
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
        "type_name": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
        "uuid": "b809ad39-4159-46c1-9091-598d542c315e"
      },
      "has_logical_errors": false,
      "id": 20,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509542617,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375052859,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 33,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375052859,
          "name": "SNOW post-process",
          "object_type": "sn_records_dt",
          "playbook_handle": "snow_updateclose_record_pb",
          "programmatic_name": "snow_updateclose_record_pb_post_process",
          "script_text": "results = playbook.functions.results.close_in_sn\n# If the SOAR item type is Incident (if it is Task, we run the SNOW Helper: Add Task Note function)\nif row.sn_records_dt_type == \"Incident\":\n  note_text = None\n\n  # If it was a success, set below note_text\n  if results.get(\"success\"):\n    note_text = f\"\"\"\u003cbr\u003eThis Incident has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\n\n  # Else, it failed, so set below note_text\n  else:\n    note_text = f\"\"\"\u003cbr\u003eFailed to close this Incident in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\n  incident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "488a18f2-a7fd-47c8-9a6b-fc2f367bc634"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "sn_records_dt.sn_records_dt_snow_table",
              "method": "equals",
              "type": null,
              "value": "incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "If closing the SNOW record all tasks on the SNOW record must be closed in order to close the SNOW record.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "93655d2e-3e26-4046-93cd-19cb4903a91a",
            "element": "field_uuid",
            "field_type": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "3eca123e-cf0c-4ece-af6b-4c2d87382213",
            "element": "field_uuid",
            "field_type": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "41b3f8e4-53fd-4566-a02d-4b22dfaff152",
            "element": "field_uuid",
            "field_type": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_record_pb",
      "object_type": "sn_records_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_edcd1bb4-0249-4a25-bcca-e17347857277",
        "id": 22,
        "name": "playbook_edcd1bb4_0249_4a25_bcca_e17347857277",
        "type": "playbook",
        "uuid": "16ec98ec-b569-4e84-8e29-4521a54ecafe"
      },
      "tags": [],
      "type": "default",
      "uuid": "edcd1bb4-0249-4a25-bcca-e17347857277",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb\" isExecutable=\"true\" name=\"playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_077rlcc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\nmap_sn_record_states = {\\n\\t\\\"Draft\\\": 1,\\n\\t\\\"Ready\\\": 18,\\n\\t\\\"Assigned\\\": 16,\\n\\t\\\"Work in Progress\\\": 18,\\n\\t\\\"Closed\\\": 3\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# RES ID of this SNOW record from the Data Table row\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# The state to change the record to\\ninputs.sn_record_state = map_sn_record_states.get(getattr(playbook.inputs, \\\"sn_record_state\\\", None))\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_in_sn\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_077rlcc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0vwiu22\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_077rlcc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dfd3c8ff-c44a-4806-bb80-b29da07b63d4\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vwiu22\u003c/incoming\u003e\u003coutgoing\u003eFlow_103hgzz\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0vwiu22\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_0zqn8dv\" id=\"ConditionPoint_3\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_103hgzz\u003c/incoming\u003e\u003coutgoing\u003eFlow_0b4bf5c\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0zqn8dv\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_103hgzz\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"SNOW Helper: Add Task Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f02d65f0-f19a-414a-828d-5c35de5270b1\"\u003e{\"inputs\":{},\"pre_processing_script\":\"note_text = None\\nresults = playbook.functions.results.close_in_sn\\nif results.get(\\\"success\\\"):\\n  # If successfully closed the record, set below note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;This Task has been updated in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow ID:\u0026lt;/b\u0026gt; {results.get(\u0027sn_ref_id\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Record State:\u0026lt;/b\u0026gt; {results.get(\u0027sn_record_state\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Notes:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Code:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\\\"\\\"\\\"\\nelse:\\n  # Else, it failed, so set this note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;Failed to close this Task in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {results.get(\\\"reason\\\")}\\\"\\\"\\\"\\n\\n# Get sn_res_id from the Data Table\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# Set the sn_note_text input\\ninputs.sn_note_text = note_text\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_task_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0b4bf5c\u003c/incoming\u003e\u003coutgoing\u003eFlow_1nozhak\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1nozhak\u003c/incoming\u003e\u003cincoming\u003eFlow_0zqn8dv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1nozhak\" sourceRef=\"ServiceTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_0b4bf5c\" name=\"do_continue\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"do_continue\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = row.sn_records_dt_type == \\\"Task\\\"\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0zqn8dv\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zqn8dv\" id=\"Flow_0zqn8dv_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"654\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"948.9999999999999\" y=\"523\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0b4bf5c\" id=\"Flow_0b4bf5c_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"556\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"62\" x=\"690\" y=\"583\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nozhak\" id=\"Flow_1nozhak_di\"\u003e\u003comgdi:waypoint x=\"819\" y=\"680\"/\u003e\u003comgdi:waypoint x=\"894\" y=\"680\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_103hgzz\" id=\"Flow_103hgzz_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"504\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vwiu22\" id=\"Flow_0vwiu22_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_077rlcc\" id=\"Flow_077rlcc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"504\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"894\" y=\"654\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375053765,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
      "description": {
        "content": "Update the state of this record in the \"sn_si_task\" table in ServiceNow",
        "format": "text"
      },
      "display_name": "SNOW: Update/Close Response Task (PB)",
      "export_key": "snow_updateclose_response_task_pb",
      "field_type_handle": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update/Close Response Task (PB)",
        "export_key": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
        "fields": {
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb/sn_close_notes",
            "hide_notification": false,
            "id": 4993,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1021,
            "uuid": "196ec424-7fe4-46cb-afab-1981f57602e2",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb/sn_record_state",
            "hide_notification": false,
            "id": 4994,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "",
            "type_id": 1021,
            "uuid": "47db28ca-707f-43c0-9461-f886517f9e28",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Draft",
                "properties": null,
                "uuid": "5af87d46-5763-415a-94e1-2f1511e47920",
                "value": 2106
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Ready",
                "properties": null,
                "uuid": "b642fd6f-c3d4-4ed2-b254-fcdffe461c44",
                "value": 2107
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Assigned",
                "properties": null,
                "uuid": "a6b10da0-83f0-478c-8ea2-f88c954167a3",
                "value": 2108
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Work in Progress",
                "properties": null,
                "uuid": "69534620-93b0-42f1-81e7-1695475c9a79",
                "value": 2109
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "f3d7af59-76fc-446b-92cb-5e35f3e45a18",
                "value": 2110
              }
            ]
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
        "type_name": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
        "uuid": "3eeacb8f-0b02-4a6a-8b1c-6db99b253ea0"
      },
      "has_logical_errors": false,
      "id": 21,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509543497,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375054024,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 34,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375054024,
          "name": "SNOW post-process",
          "object_type": "sn_records_dt",
          "playbook_handle": "snow_updateclose_response_task_pb",
          "programmatic_name": "snow_updateclose_response_task_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.close_in_sn\n# If the SOAR item type is Incident (if it is Task, we run the SNOW Helper: Add Task Note function)\nif row.sn_records_dt_type == \"Incident\":\n  note_text = None\n\n  # If it was a success, set below note_text\n  if results.get(\"success\"):\n    note_text = f\"\"\"\u003cbr\u003eThis Incident has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\n\n  # Else, it failed, so set below note_text\n  else:\n    note_text = f\"\"\"\u003cbr\u003eFailed to close this Incident in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\n  incident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "dfd3c8ff-c44a-4806-bb80-b29da07b63d4"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "sn_records_dt.sn_records_dt_snow_table",
              "method": "equals",
              "type": null,
              "value": "sn_si_task"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "47db28ca-707f-43c0-9461-f886517f9e28",
            "element": "field_uuid",
            "field_type": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "196ec424-7fe4-46cb-afab-1981f57602e2",
            "element": "field_uuid",
            "field_type": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_response_task_pb",
      "object_type": "sn_records_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_41ab7f41-a85b-4a0b-a6f6-e2b1b248f6fb",
        "id": 23,
        "name": "playbook_41ab7f41_a85b_4a0b_a6f6_e2b1b248f6fb",
        "type": "playbook",
        "uuid": "f9c29fa6-0c55-49b7-8673-f25655ad48eb"
      },
      "tags": [],
      "type": "default",
      "uuid": "41ab7f41-a85b-4a0b-a6f6-e2b1b248f6fb",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_b24adedf_5e85_429a_a181_72fce0de1523\" isExecutable=\"true\" name=\"playbook_b24adedf_5e85_429a_a181_72fce0de1523\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_077rlcc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\n# Codes prepended with [SIR] are specific to Security Incident Response incidents\\nmap_sn_record_states = {\\n  \\\"New\\\": 1,\\n  \\\"In Progress\\\": 2,\\n  \\\"On Hold\\\": 3,\\n\\t\\\"Analysis\\\": 16,\\n\\t\\\"Contain\\\": 18,\\n\\t\\\"Eradicate\\\": 19,\\n\\t\\\"Recover\\\": 20,\\n\\t\\\"Review\\\": 100,\\n\\t\\\"Closed\\\": 3,\\n\\t\\\"Canceled\\\": 7,\\n  \\\"Cancelled\\\": 7 # servicenow has inconsistent spellings of this word...\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# RES ID of this SNOW record from the Data Table row\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# The state to change the record to\\ninputs.sn_record_state = map_sn_record_states.get(getattr(playbook.inputs, \\\"sn_record_state\\\", None))\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# The ServiceNow \u0027close_code\u0027 that you normally select when closing a ServiceNow record\\nif getattr(playbook.inputs, \\\"sn_close_code\\\", None):\\n  inputs.sn_close_code = getattr(playbook.inputs, \\\"sn_close_code\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_in_sn\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_077rlcc\u003c/incoming\u003e\u003coutgoing\u003eFlow_0vwiu22\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_077rlcc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e1a0d8ac-0364-45fc-9f38-77c8c622712f\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vwiu22\u003c/incoming\u003e\u003coutgoing\u003eFlow_103hgzz\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0vwiu22\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_0zqn8dv\" id=\"ConditionPoint_3\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_103hgzz\u003c/incoming\u003e\u003coutgoing\u003eFlow_0b4bf5c\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0zqn8dv\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"Flow_103hgzz\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"SNOW Helper: Add Task Note\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f02d65f0-f19a-414a-828d-5c35de5270b1\"\u003e{\"inputs\":{},\"pre_processing_script\":\"note_text = None\\nresults = playbook.functions.results.close_in_sn\\nif results.get(\\\"success\\\"):\\n  # If successfully closed the record, set below note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;This Task has been updated in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow ID:\u0026lt;/b\u0026gt; {results.get(\u0027sn_ref_id\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Record State:\u0026lt;/b\u0026gt; {results.get(\u0027sn_record_state\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Notes:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\\n              \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;ServiceNow Closing Code:\u0026lt;/b\u0026gt; {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\\\"\\\"\\\"\\nelse:\\n  # Else, it failed, so set this note_text\\n  note_text = f\\\"\\\"\\\"\u0026lt;br\u0026gt;Failed to close this Task in \u0026lt;b\u0026gt;ServiceNow\u0026lt;/b\u0026gt;\\n            \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {results.get(\\\"reason\\\")}\\\"\\\"\\\"\\n\\n# Get sn_res_id from the Data Table\\ninputs.sn_res_id = row.sn_records_dt_res_id\\n\\n# Set the sn_note_text input\\ninputs.sn_note_text = note_text\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_task_note\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0b4bf5c\u003c/incoming\u003e\u003coutgoing\u003eFlow_1nozhak\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1nozhak\u003c/incoming\u003e\u003cincoming\u003eFlow_0zqn8dv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1nozhak\" sourceRef=\"ServiceTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_0b4bf5c\" name=\"do_continue\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"do_continue\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"result = row.sn_records_dt_type == \\\"Task\\\"\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0zqn8dv\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_b24adedf_5e85_429a_a181_72fce0de1523\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zqn8dv\" id=\"Flow_0zqn8dv_di\"\u003e\u003comgdi:waypoint x=\"843\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"530\"/\u003e\u003comgdi:waypoint x=\"960\" y=\"654\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"948.9999999999999\" y=\"523\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0b4bf5c\" id=\"Flow_0b4bf5c_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"556\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"638\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"62\" x=\"690\" y=\"583\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1nozhak\" id=\"Flow_1nozhak_di\"\u003e\u003comgdi:waypoint x=\"819\" y=\"680\"/\u003e\u003comgdi:waypoint x=\"894\" y=\"680\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_103hgzz\" id=\"Flow_103hgzz_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"452\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"504\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vwiu22\" id=\"Flow_0vwiu22_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"368\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_077rlcc\" id=\"Flow_077rlcc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"368\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"504\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"638\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"894\" y=\"654\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375054792,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
      "description": {
        "content": "Update the state of this record in the \"sn_si_incident\" table in ServiceNow",
        "format": "text"
      },
      "display_name": "SNOW: Update/Close Security Incident (PB)",
      "export_key": "snow_updateclose_sir_incident_from_datatable_pb",
      "field_type_handle": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update/Close Security Incident (PB)",
        "export_key": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
        "fields": {
          "sn_close_code": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_b24adedf_5e85_429a_a181_72fce0de1523/sn_close_code",
            "hide_notification": false,
            "id": 4995,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_code",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Code",
            "tooltip": "Optional. Sets the close code only when Record State is CLOSED",
            "type_id": 1022,
            "uuid": "b3e3e938-0e97-4622-8416-085c1eb87016",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Work Around)",
                "properties": null,
                "uuid": "56070ec6-50df-41df-ac2b-9771dffabb59",
                "value": 2111
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Permanently)",
                "properties": null,
                "uuid": "b5d4c881-3a1d-4bba-8bb4-839c2fc8817e",
                "value": 2112
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Not Reproducible)",
                "properties": null,
                "uuid": "6df00d88-ff9d-44c3-ac40-0baafea8c517",
                "value": 2113
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Too Costly)",
                "properties": null,
                "uuid": "b9ea1766-1ddc-45d7-bfd1-c9ed3f2237ad",
                "value": 2114
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed/Resolved by Caller",
                "properties": null,
                "uuid": "0df2c9c7-a3c5-469c-9236-6938cf0fa2ad",
                "value": 2115
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Investigation completed",
                "properties": null,
                "uuid": "c72df9f4-1f59-481a-9f16-b8556fd384d2",
                "value": 2116
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Threat mitigated",
                "properties": null,
                "uuid": "7ecb1479-bf7f-41e9-b59d-2d3d9b016737",
                "value": 2117
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Patched vulnerability",
                "properties": null,
                "uuid": "aca5ed90-05a7-466c-9592-2f25e7195288",
                "value": 2118
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Invalid vulnerability",
                "properties": null,
                "uuid": "6cd0fdc3-17bd-4a7c-9dfa-c1d289f0f961",
                "value": 2119
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not resolved",
                "properties": null,
                "uuid": "8bfc2a73-4176-4f74-8514-ffbfb0b0f0ff",
                "value": 2120
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "False positive",
                "properties": null,
                "uuid": "108a8f26-39ed-45a3-b2a1-9099b15faa9b",
                "value": 2121
              }
            ]
          },
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_b24adedf_5e85_429a_a181_72fce0de1523/sn_close_notes",
            "hide_notification": false,
            "id": 4996,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1022,
            "uuid": "684df6e4-a5bd-4517-8d0c-758dfd58aaab",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_b24adedf_5e85_429a_a181_72fce0de1523/sn_record_state",
            "hide_notification": false,
            "id": 4997,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "",
            "type_id": 1022,
            "uuid": "c19fdb96-f777-449a-be07-27678783a88b",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Analysis",
                "properties": null,
                "uuid": "86fcd607-b05d-4d55-8c49-6dea73261178",
                "value": 2122
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Contain",
                "properties": null,
                "uuid": "227278d0-72bd-462f-b865-3db07ee4c3f8",
                "value": 2123
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Eradicate",
                "properties": null,
                "uuid": "414cf2e5-ef23-423d-8296-ee1dc051cbc7",
                "value": 2124
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Recover",
                "properties": null,
                "uuid": "cf7e6b27-5fed-44cb-9f39-7fa61cfc01dc",
                "value": 2125
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Review",
                "properties": null,
                "uuid": "81d47b4a-24b4-4fc4-a1f9-05aefe64ab55",
                "value": 2126
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "f3d7af59-76fc-446b-92cb-5e35f3e45a18",
                "value": 2127
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Canceled",
                "properties": null,
                "uuid": "17edf5cd-f312-49bf-bf47-d336c46bae74",
                "value": 2128
              }
            ]
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
        "type_name": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
        "uuid": "64f58396-83ea-44af-bb8d-26dcfcab3e30"
      },
      "has_logical_errors": false,
      "id": 22,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509544361,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375055129,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 35,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375055129,
          "name": "SNOW post-process",
          "object_type": "sn_records_dt",
          "playbook_handle": "snow_updateclose_sir_incident_from_datatable_pb",
          "programmatic_name": "snow_updateclose_sir_incident_from_datatable_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.close_in_sn\n# If the SOAR item type is Incident (if it is Task, we run the SNOW Helper: Add Task Note function)\nif row.sn_records_dt_type == \"Incident\":\n  note_text = None\n\n  # If it was a success, set below note_text\n  if results.get(\"success\"):\n    note_text = f\"\"\"\u003cbr\u003eThis Incident has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n                \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\n\n  # Else, it failed, so set below note_text\n  else:\n    note_text = f\"\"\"\u003cbr\u003eFailed to close this Incident in \u003cb\u003eServiceNow\u003c/b\u003e\n                \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\n  incident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "e1a0d8ac-0364-45fc-9f38-77c8c622712f"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "sn_records_dt.sn_records_dt_snow_table",
              "method": "equals",
              "type": null,
              "value": "sn_si_incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "If closing the SNOW record all tasks on the SNOW record must be closed in order to close the SNOW record.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "c19fdb96-f777-449a-be07-27678783a88b",
            "element": "field_uuid",
            "field_type": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b3e3e938-0e97-4622-8416-085c1eb87016",
            "element": "field_uuid",
            "field_type": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "684df6e4-a5bd-4517-8d0c-758dfd58aaab",
            "element": "field_uuid",
            "field_type": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_sir_incident_from_datatable_pb",
      "object_type": "sn_records_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_b24adedf-5e85-429a-a181-72fce0de1523",
        "id": 24,
        "name": "playbook_b24adedf_5e85_429a_a181_72fce0de1523",
        "type": "playbook",
        "uuid": "e7cbf2ad-3462-4881-a758-afd90380d654"
      },
      "tags": [],
      "type": "default",
      "uuid": "b24adedf-5e85-429a-a181-72fce0de1523",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925\" isExecutable=\"true\" name=\"playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_030xauf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"SNOW: Close Record\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"edadf951-4652-48a9-8068-9b719bf4bfe4\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# A Dictionary that maps Record States to their corresponding codes\\n# These codes are defined in ServiceNow and may be different for each ServiceNow configuration\\n# Codes prepended with [SIR] are specific to Security Incident Response incidents\\nmap_sn_record_states = {\\n  \\\"New\\\": 1,\\n  \\\"In Progress\\\": 2,\\n  \\\"On Hold\\\": 3,\\n\\t\\\"Analysis\\\": 16,\\n\\t\\\"Contain\\\": 18,\\n\\t\\\"Eradicate\\\": 19,\\n\\t\\\"Recover\\\": 20,\\n\\t\\\"Review\\\": 100,\\n\\t\\\"Closed\\\": 3,\\n\\t\\\"Canceled\\\": 7,\\n  \\\"Cancelled\\\": 7 # servicenow has inconsistent spellings of this word...\\n}\\n\\n# ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The state to change the record to\\n# inputs.sn_record_state = map_sn_record_states[\\\"Closed\\\"]\\ninputs.sn_record_state = map_sn_record_states[getattr(playbook.inputs, \\\"sn_record_state\\\", None)]\\n\\n# The resolution notes that are normally required when you close a ServiceNow record\\n# inputs.sn_close_notes = \\\"This incident has been resolved in IBM SOAR. No further action required\\\"\\nif getattr(playbook.inputs, \\\"sn_close_notes\\\", None):\\n  inputs.sn_close_notes = getattr(playbook.inputs, \\\"sn_close_notes\\\", None)\\n\\n# The ServiceNow \u0027close_code\u0027 that you normally select when closing a ServiceNow record\\n# inputs.sn_close_code = \\\"Solved (Permanently)\\\"\\nif getattr(playbook.inputs, \\\"sn_close_code\\\", None):\\n  inputs.sn_close_code = getattr(playbook.inputs, \\\"sn_close_code\\\", None)\\n\\n# Add a Work Note to the Record in ServiceNow\\ninputs.sn_close_work_note = f\\\"This record\u0027s state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR\\\"\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"close_record\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_030xauf\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wztaau\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_030xauf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"SNOW post-process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"33bf2913-fd82-45c7-9937-4685c210f22c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wztaau\u003c/incoming\u003e\u003coutgoing\u003eFlow_085mkuv\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0wztaau\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_085mkuv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_085mkuv\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_085mkuv\" id=\"Flow_085mkuv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wztaau\" id=\"Flow_0wztaau_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_030xauf\" id=\"Flow_030xauf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1739375056009,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
      "description": {
        "content": "Update the state of this record in the \"sn_si_incident\" table in ServiceNow",
        "format": "text"
      },
      "display_name": "SNOW: Update/Close SIR Incident (PB)",
      "export_key": "snow_updateclose_sir_incident_pb",
      "field_type_handle": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
      "fields_type": {
        "actions": [],
        "display_name": "SNOW: Update/Close SIR Incident (PB)",
        "export_key": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
        "fields": {
          "sn_close_code": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925/sn_close_code",
            "hide_notification": false,
            "id": 4998,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_code",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Code",
            "tooltip": "Optional. Sets the close code only when Record State is CLOSED",
            "type_id": 1023,
            "uuid": "60b9d3d9-cb21-4773-a15e-0761f6eb4861",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Work Around)",
                "properties": null,
                "uuid": "6246c121-b899-4de6-bbc0-fd9ab17b519f",
                "value": 2129
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Solved (Permanently)",
                "properties": null,
                "uuid": "456aaad5-e5c6-4277-a45e-c763a6ed14e2",
                "value": 2130
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Not Reproducible)",
                "properties": null,
                "uuid": "4c6c687c-f7c5-4c32-b82c-7da832816648",
                "value": 2131
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Solved (Too Costly)",
                "properties": null,
                "uuid": "9a83ffb2-48b8-4878-aa86-9374f31a5ee1",
                "value": 2132
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed/Resolved by Caller",
                "properties": null,
                "uuid": "478b2383-cd13-454e-8e62-af786e502697",
                "value": 2133
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Investigation completed",
                "properties": null,
                "uuid": "5f721fba-73c4-4d8f-a0fc-eca2cd76a61d",
                "value": 2134
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Threat mitigated",
                "properties": null,
                "uuid": "4e98ad83-5d6f-44ac-ac39-6298d0b23ff5",
                "value": 2135
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Patched vulnerability",
                "properties": null,
                "uuid": "397905a1-b60a-4be1-9905-10339e7796f9",
                "value": 2136
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Invalid vulnerability",
                "properties": null,
                "uuid": "3222705e-b4b4-425a-bee7-df4ce396b938",
                "value": 2137
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not resolved",
                "properties": null,
                "uuid": "2acee495-0ea0-4422-a9d3-97138a1661c7",
                "value": 2138
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "False positive",
                "properties": null,
                "uuid": "ed73ffd2-1ca9-4315-8363-0ec44704c902",
                "value": 2139
              }
            ]
          },
          "sn_close_notes": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925/sn_close_notes",
            "hide_notification": false,
            "id": 4999,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "sn_close_notes",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Close Notes",
            "tooltip": "Optional. Note to be added to record when state is CLOSED",
            "type_id": 1023,
            "uuid": "d753e42a-8a49-441f-913e-689c9b34a8ca",
            "values": []
          },
          "sn_record_state": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925/sn_record_state",
            "hide_notification": false,
            "id": 5000,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "sn_record_state",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "SN Record State",
            "tooltip": "",
            "type_id": 1023,
            "uuid": "1ce4d188-2a07-4eb8-9095-493d25d91e76",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Analysis",
                "properties": null,
                "uuid": "75bd520f-ec13-4aac-98ee-46ba4769422b",
                "value": 2140
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Contain",
                "properties": null,
                "uuid": "4110cfab-67e5-4bee-a899-1db1a1ce04e8",
                "value": 2141
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Eradicate",
                "properties": null,
                "uuid": "b70f6eb5-481c-4f8e-b859-aa7bf5f9d6a6",
                "value": 2142
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Recover",
                "properties": null,
                "uuid": "b811652f-bc95-4a99-828a-e97b9d216c0d",
                "value": 2143
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Review",
                "properties": null,
                "uuid": "68428c65-fb27-49de-a7ee-1d722f336af9",
                "value": 2144
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "3288959c-7053-4e1f-962c-505feb74c551",
                "value": 2145
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Canceled",
                "properties": null,
                "uuid": "a1d832e4-a26a-4d6c-bbf5-119da4706fdb",
                "value": 2146
              }
            ]
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
        "type_name": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
        "uuid": "a64b6f29-6a49-45c0-97e9-1247edd7ba65"
      },
      "has_logical_errors": false,
      "id": 23,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 33,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1743509544921,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1739375056296,
          "description": "",
          "enabled": false,
          "export_key": "SNOW post-process",
          "id": 36,
          "language": "python3",
          "last_modified_by": "a@example.com",
          "last_modified_time": 1739375056296,
          "name": "SNOW post-process",
          "object_type": "incident",
          "playbook_handle": "snow_updateclose_sir_incident_pb",
          "programmatic_name": "snow_updateclose_sir_incident_pb_snow_post_process",
          "script_text": "results = playbook.functions.results.close_record\nif results.get(\"success\"):\n  note_text = f\"\"\"\u003cbr\u003eThis Incident has been updated in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eServiceNow ID:\u003c/b\u003e {results.get(\u0027sn_ref_id\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Record State:\u003c/b\u003e {results.get(\u0027sn_record_state\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Notes:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_notes\u0027)}\n              \u003cbr\u003e\u003cb\u003eServiceNow Closing Code:\u003c/b\u003e {results.get(\u0027inputs\u0027, {}).get(\u0027sn_close_code\u0027)}\"\"\"\nelse:\n  note_text = f\"\"\"\u003cbr\u003eFailed to close this Incident in \u003cb\u003eServiceNow\u003c/b\u003e\n              \u003cbr\u003e\u003cb\u003eReason:\u003c/b\u003e {results.get(\u0027reason\u0027)}\"\"\"\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "33bf2913-fd82-45c7-9937-4685c210f22c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_record_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.properties.sn_snow_table_name",
              "method": "equals",
              "type": null,
              "value": "sn_si_incident"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "If closing the SNOW record all tasks on the SNOW record must be closed in order to close the SNOW record.",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "1ce4d188-2a07-4eb8-9095-493d25d91e76",
            "element": "field_uuid",
            "field_type": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "60b9d3d9-cb21-4773-a15e-0761f6eb4861",
            "element": "field_uuid",
            "field_type": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d753e42a-8a49-441f-913e-689c9b34a8ca",
            "element": "field_uuid",
            "field_type": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "snow_updateclose_sir_incident_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_ec07cc7a-61c2-4537-b5e7-d30b6923a925",
        "id": 25,
        "name": "playbook_ec07cc7a_61c2_4537_b5e7_d30b6923a925",
        "type": "playbook",
        "uuid": "723df679-832d-4a91-9edd-0d290afe62b0"
      },
      "tags": [],
      "type": "default",
      "uuid": "ec07cc7a-61c2-4537-b5e7-d30b6923a925",
      "version": 7
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
  "types": [
    {
      "actions": [],
      "display_name": "ServiceNow Records",
      "export_key": "sn_records_dt",
      "fields": {
        "sn_records_dt_links": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_links",
          "hide_notification": false,
          "id": 4939,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_links",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Links",
          "tooltip": "Opens the record in a new tab in either IBM SOAR or SNOW",
          "type_id": 1004,
          "uuid": "7fafcc23-1b8d-44e0-a192-336bdd4137b2",
          "values": [],
          "width": 64
        },
        "sn_records_dt_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_name",
          "hide_notification": false,
          "id": 4940,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Name",
          "tooltip": "The name of the record",
          "type_id": 1004,
          "uuid": "b81b6dd1-78c0-4e35-9fc0-2883b0037890",
          "values": [],
          "width": 110
        },
        "sn_records_dt_res_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_res_id",
          "hide_notification": false,
          "id": 4941,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_res_id",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SOAR ID",
          "tooltip": "Unique ID of IBM SOAR Incident or Task",
          "type_id": 1004,
          "uuid": "7709e2b5-f66c-403d-a8ba-c438837b78c9",
          "values": [],
          "width": 167
        },
        "sn_records_dt_res_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_res_status",
          "hide_notification": false,
          "id": 4942,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_res_status",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SOAR Status",
          "tooltip": "The current status of the Incident/Task in IBM SOAR",
          "type_id": 1004,
          "uuid": "c99d25f2-8066-412a-ba89-4f1226b6af5e",
          "values": [],
          "width": 181
        },
        "sn_records_dt_sn_parent_ref_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_sn_parent_ref_id",
          "hide_notification": false,
          "id": 4943,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_sn_parent_ref_id",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SNOW Parent ID",
          "tooltip": "ID of record\u0027s parent in SNOW if the record is a \"child\" record",
          "type_id": 1004,
          "uuid": "6db39fa5-3a99-4ce8-aca6-bece69d55f5f",
          "values": [],
          "width": 148
        },
        "sn_records_dt_sn_ref_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_sn_ref_id",
          "hide_notification": false,
          "id": 4944,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_sn_ref_id",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SNOW ID",
          "tooltip": "ID of record in SNOW, unique to its table in SNOW",
          "type_id": 1004,
          "uuid": "cd9c9e13-ebbf-4b5e-a438-a7a969c1f9fd",
          "values": [],
          "width": 121
        },
        "sn_records_dt_snow_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_snow_status",
          "hide_notification": false,
          "id": 4945,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_snow_status",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SNOW Status",
          "tooltip": "The current status of the record in SNOW",
          "type_id": 1004,
          "uuid": "fa7159db-73e4-464e-8bbd-5e7ef99f54e9",
          "values": [],
          "width": 181
        },
        "sn_records_dt_snow_table": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_snow_table",
          "hide_notification": false,
          "id": 4946,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_snow_table",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "incident",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "SNOW Table",
          "tooltip": "The table in ServiceNow where this record exists",
          "type_id": 1004,
          "uuid": "37e8cc80-294f-464f-801c-7666afb2531b",
          "values": [],
          "width": 116
        },
        "sn_records_dt_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_time",
          "hide_notification": false,
          "id": 4947,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_time",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Last Updated",
          "tooltip": "The time this row was last updated",
          "type_id": 1004,
          "uuid": "3da0c0bb-b1fa-40c9-9859-aa8458211ba6",
          "values": [],
          "width": 157
        },
        "sn_records_dt_type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "sn_records_dt/sn_records_dt_type",
          "hide_notification": false,
          "id": 4948,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "sn_records_dt_type",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Type in SOAR",
          "tooltip": "Type of the linked object in SOAR. Either Incident or Task",
          "type_id": 1004,
          "uuid": "9fd786bb-cc8d-49c8-8df1-f02921e36578",
          "values": [],
          "width": 124
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
      "type_name": "sn_records_dt",
      "uuid": "8d34ee77-4c54-4034-b68b-23cbf9088e11"
    }
  ],
  "workflows": [],
  "workspaces": []
}
