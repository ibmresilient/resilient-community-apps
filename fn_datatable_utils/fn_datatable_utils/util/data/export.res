{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1686560750489,
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
      "id": 1008,
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
      "export_key": "__function/dt_mapping_table",
      "hide_notification": false,
      "id": 1009,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_mapping_table",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\"\"\"{\"csv_hdr1\":\"datatable_column_name, ...}\"\"\"",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_mapping_table",
      "tooltip": "String-encoded JSON of csv header to datatable column mappings",
      "type_id": 11,
      "uuid": "85d4768e-32ac-4b27-8c4e-f338e41387fd",
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
      "export_key": "__function/dt_start_row",
      "hide_notification": false,
      "id": 1010,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_start_row",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_start_row",
      "tooltip": "Row to start adding to datatable. Use 1 if dt_has_headers = True for first data row",
      "type_id": 11,
      "uuid": "8e6c2730-0ecb-42d8-b0a0-b199677c6782",
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
      "export_key": "__function/dt_utils_cells_to_update",
      "hide_notification": false,
      "id": 1011,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_cells_to_update",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_cells_to_update",
      "tooltip": "A JSON String containing the column names and cell values to update",
      "type_id": 11,
      "uuid": "9e1fc0a5-7546-4c6a-814f-1fad878cd875",
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
      "export_key": "__function/dt_csv_data",
      "hide_notification": false,
      "id": 1012,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_csv_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "CSV Data",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_csv_data",
      "tooltip": "string of csv data consisting an optional header row followed by rows of comma separated data. each comma separated field may contain quotes to allow for embedded commas",
      "type_id": 11,
      "uuid": "a850ece1-e363-4044-94fa-a4ce63085f33",
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
      "export_key": "__function/dt_utils_rows_ids",
      "hide_notification": false,
      "id": 1013,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_rows_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_rows_ids",
      "tooltip": "The list of internal rows IDs of a Data Table to delete",
      "type_id": 11,
      "uuid": "bdccb36f-d1e2-45d4-9078-97c677895b8d",
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
      "export_key": "__function/dt_utils_max_rows",
      "hide_notification": false,
      "id": 1014,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_max_rows",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_max_rows",
      "tooltip": "The maximum number of rows to be returned",
      "type_id": 11,
      "uuid": "c42f5cac-9e46-4ee3-bda4-6c9dbe17c516",
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
      "export_key": "__function/dt_utils_delete_all_rows",
      "hide_notification": false,
      "id": 1015,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_delete_all_rows",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_delete_all_rows",
      "tooltip": "explicitly delete all rows",
      "type_id": 11,
      "uuid": "cdc77c39-75b9-498e-b4c6-fb2b19f9ff08",
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
      "export_key": "__function/dt_date_time_format",
      "hide_notification": false,
      "id": 1016,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_date_time_format",
      "operation_perms": {},
      "operations": [],
      "placeholder": "E.g. dd/mm/yyyy",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_date_time_format",
      "tooltip": "If you\u0027re data contains date entries, provide the format for the date",
      "type_id": 11,
      "uuid": "e2a22797-1440-4fb5-8e85-adead51f0448",
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
      "export_key": "__function/dt_has_headers",
      "hide_notification": false,
      "id": 1017,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "dt_has_headers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_has_headers",
      "tooltip": "boolean True if the csv_data contains header information to match with the column names of the datatable. If False, the data is added to the datatable in column order.",
      "type_id": 11,
      "uuid": "ea2dc835-7451-4386-abae-73634223d991",
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
      "export_key": "__function/dt_utils_datatable_api_name",
      "hide_notification": false,
      "id": 1018,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_datatable_api_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_datatable_api_name",
      "tooltip": "The API name of the Data Table",
      "type_id": 11,
      "uuid": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
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
      "export_key": "__function/dt_utils_search_value",
      "hide_notification": false,
      "id": 1019,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_search_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_search_value",
      "tooltip": "The cell value to search for within the search column",
      "type_id": 11,
      "uuid": "fca27f70-867b-4899-b7c5-f8bdf1bbec13",
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
      "export_key": "__function/dt_utils_sort_by",
      "hide_notification": false,
      "id": 1020,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_sort_by",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_sort_by",
      "tooltip": "The API name of the column to sort by",
      "type_id": 11,
      "uuid": "11e8aca8-05bd-467b-8071-9dd160d9e14a",
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
      "id": 1021,
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
      "uuid": "17c3e652-6559-4935-9f95-74374ca37a7b",
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
      "export_key": "__function/dt_datable_name",
      "hide_notification": false,
      "id": 1022,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_datable_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Datatable Name",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_datable_name",
      "tooltip": "string of api name of datatable",
      "type_id": 11,
      "uuid": "1ef31204-70b9-4f15-bfe1-7456f89a0ad4",
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
      "export_key": "__function/dt_utils_row_id",
      "hide_notification": false,
      "id": 1023,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_row_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_row_id",
      "tooltip": "The internal ID of the row to be retrieved",
      "type_id": 11,
      "uuid": "21f1e446-305a-4f03-a176-c064ca3283fe",
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
      "export_key": "__function/dt_utils_search_column",
      "hide_notification": false,
      "id": 1024,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_search_column",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_search_column",
      "tooltip": "The API name of the column to search",
      "type_id": 11,
      "uuid": "2c359b58-e41e-4dd1-ac65-138e85a27363",
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
      "export_key": "__function/dt_utils_sort_direction",
      "hide_notification": false,
      "id": 1025,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_sort_direction",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_utils_sort_direction",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2fea7801-9ec6-4f95-812b-31aec2661fca",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "ASC",
          "properties": null,
          "uuid": "61729b10-cdab-48eb-bc8b-9f30af3afec5",
          "value": 357
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DESC",
          "properties": null,
          "uuid": "4c223e4f-b70c-4957-9c7f-86761015b24c",
          "value": 358
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
      "export_key": "__function/dt_max_rows",
      "hide_notification": false,
      "id": 1026,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_max_rows",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "dt_max_rows",
      "tooltip": "limit the number of rows to include",
      "type_id": 11,
      "uuid": "4363abc4-1934-407a-bdbb-923ef968d44c",
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
      "created_date": 1685351004276,
      "description": {
        "content": "Add a row to a given datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Add Row",
      "export_key": "dt_utils_add_row",
      "id": 43,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601209,
      "name": "dt_utils_add_row",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"select\": \"1\", \"number\": 1, \"datetime\": 1654019149216, \"boolean\": true, \"multi_select\": [\"a\", \"b\"], \"dt_col_name\": \"fGzfdhgxj\", \"text\": \"example add row\"}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_cells_to_update\": \"{ \\\"select\\\":\\\"1\\\",\\\"number\\\":1,\\\"datetime\\\":1654019149216,\\\"boolean\\\":true,\\\"multi_select\\\":[\u0027a\u0027, \u0027b\u0027],\\\"dt_col_name\\\":\\\"fGzfdhgxj\\\",\\\"text\\\":\\\"example add row\\\" }\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 546, \"timestamp\": \"2022-05-31 13:45:50\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"select\": {\"type\": \"string\"}, \"number\": {\"type\": \"integer\"}, \"datetime\": {\"type\": \"integer\"}, \"boolean\": {\"type\": \"boolean\"}, \"multi_select\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"dt_col_name\": {\"type\": \"string\"}, \"text\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_cells_to_update\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "88e45595-8f9b-4521-986c-22e53de7abf3",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e1fc0a5-7546-4c6a-814f-1fad878cd875",
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
      "created_date": 1685351004312,
      "description": {
        "content": "Delete all the contents of a datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Clear Datatable",
      "export_key": "dt_utils_clear_datatable",
      "id": 44,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601245,
      "name": "dt_utils_clear_datatable",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"title\": null, \"message\": null, \"hints\": []}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 626, \"timestamp\": \"2022-05-31 13:46:14\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"title\": {}, \"message\": {}, \"hints\": {\"type\": \"array\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "9149563c-8e72-4025-ab71-305cda30dcc7",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
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
      "created_date": 1685351004350,
      "description": {
        "content": "Add CSV data to a named datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Create CSV Datatable",
      "export_key": "dt_utils_create_csv_table",
      "id": 45,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601278,
      "name": "dt_utils_create_csv_table",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"data_source\": \"test_types_utf-8.csv\", \"rows_added\": 12, \"rows_with_errors\": 0}, \"raw\": null, \"inputs\": {\"dt_date_time_format\": \"%m/%d/%y %H:%M\", \"dt_mapping_table\": \"{\\n  \\\"hdr_number\\\": \\\"number\\\",\\n  \\\"hdr_text\\\": \\\"text\\\",\\n  \\\"hdr_boolean\\\": \\\"boolean\\\",\\n  \\\"hdr_datetime\\\": \\\"datetime\\\",\\n  \\\"hdr_select\\\": \\\"select\\\",\\n  \\\"hdr_multiselect\\\": \\\"multi_select\\\"\\n}\", \"incident_id\": 2269, \"attachment_id\": 12, \"dt_datable_name\": \"dt_utils_test_data_table\", \"dt_has_headers\": true}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 5471, \"timestamp\": \"2022-05-31 13:30:04\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"data_source\": {\"type\": \"string\"}, \"rows_added\": {\"type\": \"integer\"}, \"rows_with_errors\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_date_time_format\": {\"type\": \"string\"}, \"dt_mapping_table\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"attachment_id\": {\"type\": \"integer\"}, \"dt_datable_name\": {\"type\": \"string\"}, \"dt_has_headers\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "6edc80c4-e5ae-4c33-b1f1-f0c101918d7a",
      "version": 7,
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
          "content": "17c3e652-6559-4935-9f95-74374ca37a7b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1ef31204-70b9-4f15-bfe1-7456f89a0ad4",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a850ece1-e363-4044-94fa-a4ce63085f33",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ea2dc835-7451-4386-abae-73634223d991",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "85d4768e-32ac-4b27-8c4e-f338e41387fd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e2a22797-1440-4fb5-8e85-adead51f0448",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8e6c2730-0ecb-42d8-b0a0-b199677c6782",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4363abc4-1934-407a-bdbb-923ef968d44c",
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
      "created_date": 1685351004388,
      "description": {
        "content": "Function that deletes a row from a Data Table given the internal row ID.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Delete Row",
      "export_key": "dt_utils_delete_row",
      "id": 46,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601311,
      "name": "dt_utils_delete_row",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"success\": true, \"title\": null, \"message\": null, \"hints\": []}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_row_id\": 642}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 543, \"timestamp\": \"2022-05-31 13:44:54\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"title\": {}, \"message\": {}, \"hints\": {\"type\": \"array\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_row_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "50cf405e-aac1-43e7-961e-3894d38688ad",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "21f1e446-305a-4f03-a176-c064ca3283fe",
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
      "created_date": 1685351004424,
      "description": {
        "content": "Function that deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Delete Rows",
      "export_key": "dt_utils_delete_rows",
      "id": 47,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601344,
      "name": "dt_utils_delete_rows",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows_ids\": [643]}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_rows_ids\": \"[643]\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 759, \"timestamp\": \"2022-05-31 13:45:13\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows_ids\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_rows_ids\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "ef4ef5c0-5de2-4fbc-90c9-f7568451da95",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bdccb36f-d1e2-45d4-9078-97c677895b8d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2c359b58-e41e-4dd1-ac65-138e85a27363",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fca27f70-867b-4899-b7c5-f8bdf1bbec13",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdc77c39-75b9-498e-b4c6-fb2b19f9ff08",
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
      "created_date": 1685351004463,
      "description": {
        "content": "Return all of the rows from a data table in SOAR.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get All Data Table Rows",
      "export_key": "dt_utils_get_all_data_table_rows",
      "id": 48,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601377,
      "name": "dt_utils_get_all_data_table_rows",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows\": [{\"id\": 641, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 641, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 641, \"value\": 1654018496000}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 641, \"value\": \"dgzsfhcjv\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 641, \"value\": [\"e\", \"g\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 641, \"value\": 4598}, \"select\": {\"id\": \"select\", \"row_id\": 641, \"value\": \"3\"}, \"text\": {\"id\": \"text\", \"row_id\": 641, \"value\": \"Update from datatable\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}, {\"id\": 644, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 644, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 644, \"value\": 1654019149216}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 644, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 644, \"value\": [\"b\", \"a\"]}, \"number\": {\"id\": \"number\", \"row_id\": 644, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 644, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 644, \"value\": \"example add row\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 1}]}, \"raw\": null, \"inputs\": {\"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"incident_id\": 2269}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 173, \"timestamp\": \"2022-05-31 13:45:59\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "8a56f5fb-1623-4039-bd80-ed5a5a1bf05b",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
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
      "created_date": 1685351004501,
      "description": {
        "content": "Function that searches for a row using a internal row ID or a \u0027search_column and search_value\u0027 pair and returns the cells of the row that is found, if such a row exists.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get Row",
      "export_key": "dt_utils_get_row",
      "id": 49,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601410,
      "name": "dt_utils_get_row",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"id\": 642, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 642, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 642, \"value\": 1654018816842}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 642, \"value\": \"fgshdsgfjn\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 642, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 642, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 642, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 642, \"value\": \"example add row\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 1}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_search_value\": \"fgshdsgfjn\", \"dt_utils_search_column\": \"dt_col_name\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 329, \"timestamp\": \"2022-05-31 13:44:52\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_search_value\": {\"type\": \"string\"}, \"dt_utils_search_column\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "77e98bdb-2843-4cd6-8294-5a9dbef6a08e",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "21f1e446-305a-4f03-a176-c064ca3283fe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2c359b58-e41e-4dd1-ac65-138e85a27363",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fca27f70-867b-4899-b7c5-f8bdf1bbec13",
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
      "created_date": 1685351004537,
      "description": {
        "content": "Function that returns the full unsorted list of JSON objects which contain all information regarding each row found, if no searching/sorting criteria were provided.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get Rows",
      "export_key": "dt_utils_get_rows",
      "id": 50,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601447,
      "name": "dt_utils_get_rows",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows\": [{\"id\": 643, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 643, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 643, \"value\": 1654019072126}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 643, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 643, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 643, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 643, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 643, \"value\": \"Updated from Artifact\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}]}, \"raw\": null, \"inputs\": {\"dt_utils_sort_direction\": \"ASC\", \"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_search_value\": \"fGzfdhgxj\", \"dt_utils_sort_by\": null, \"dt_utils_search_column\": \"dt_col_name\", \"dt_utils_max_rows\": 0}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 192, \"timestamp\": \"2022-05-31 13:45:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_utils_sort_direction\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_search_value\": {\"type\": \"string\"}, \"dt_utils_sort_by\": {}, \"dt_utils_search_column\": {\"type\": \"string\"}, \"dt_utils_max_rows\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "9f9d8570-c33f-4f30-ab32-9448c3ff8d67",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "11e8aca8-05bd-467b-8071-9dd160d9e14a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fea7801-9ec6-4f95-812b-31aec2661fca",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c42f5cac-9e46-4ee3-bda4-6c9dbe17c516",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2c359b58-e41e-4dd1-ac65-138e85a27363",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fca27f70-867b-4899-b7c5-f8bdf1bbec13",
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
      "created_date": 1685351004574,
      "description": {
        "content": "Function that takes a JSON String of \u0027search_column and search_value\u0027 pairs to update a Data Table row.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Update Row",
      "export_key": "dt_utils_update_row",
      "id": 51,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686205601485,
      "name": "dt_utils_update_row",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"id\": 643, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 643, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 643, \"value\": 1654019072126}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 643, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 643, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 643, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 643, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 643, \"value\": \"Updated from Artifact\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_cells_to_update\": \"{ \\\"datetime\\\":1654019072126,\\\"text\\\":\\\"Updated from Artifact\\\" }\", \"dt_utils_row_id\": 643}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 598, \"timestamp\": \"2022-05-31 13:44:33\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_cells_to_update\": {\"type\": \"string\"}, \"dt_utils_row_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "77b8451e-3137-4362-840a-ac724b674b73",
      "version": 7,
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "21f1e446-305a-4f03-a176-c064ca3283fe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e1fc0a5-7546-4c6a-814f-1fad878cd875",
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
  "id": 49,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1686560749513,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1686560749513,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "c89ba3f7-162e-4083-a056-918be0051a03"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_datatable_utils",
      "name": "fn_datatable_utils",
      "programmatic_name": "fn_datatable_utils",
      "tags": [],
      "users": [
        "datatable@ibm.com"
      ],
      "uuid": "32bd8ab8-3c32-4ec8-a5d9-0252477a0c3e"
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
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081\" isExecutable=\"true\" name=\"playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_16ogfqu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, str):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# Refer to the existing row (value: 0)\\ninputs.dt_utils_row_id = 0\\n\\n# The column api names and the value to update the cell to\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"name\\\": \\\"Updated Example\\\", \\\"text\\\": \\\"Update from datatable\\\", \\\"number\\\": 4598, \\\"multi_select\\\": [\\\"b\\\", \\\"e\\\", \\\"g\\\"], \\\"boolean\\\": True})\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_16ogfqu\u003c/incoming\u003e\u003coutgoing\u003eFlow_0w3vcm8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0w3vcm8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_16ogfqu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0w3vcm8\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_16ogfqu\" id=\"Flow_16ogfqu_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0w3vcm8\" id=\"Flow_0w3vcm8_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"318\"/\u003e\u003comgdi:waypoint x=\"670\" y=\"318\"/\u003e\u003comgdi:waypoint x=\"670\" y=\"354\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"602\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"604\" y=\"354\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685359396535,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Update Row Function. It illustrates updating the current row with static values.",
        "format": "text"
      },
      "display_name": "Example Data Utils: Update Row (PB)",
      "export_key": "example_data_utils_update_row_pb",
      "field_type_handle": "playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081",
      "fields_type": {
        "actions": [],
        "display_name": "Example Data Utils: Update Row (PB)",
        "export_key": "playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081",
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
        "type_name": "playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081",
        "uuid": "08b8f7f1-4c16-4d3b-ae95-a924e8a4fb23"
      },
      "has_logical_errors": false,
      "id": 22,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685359463194,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_utils_update_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_55c36624-35fe-4f2d-bb71-ab62f4d51081",
        "id": 25,
        "name": "playbook_55c36624_35fe_4f2d_bb71_ab62f4d51081",
        "type": "playbook",
        "uuid": "53fee2be-21b1-4438-82a6-0eaeb0339840"
      },
      "tags": [],
      "type": "default",
      "uuid": "55c36624-35fe-4f2d-bb71-ab62f4d51081",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8b654e16_001f_42c1_a283_28cd56c84dba\" isExecutable=\"true\" name=\"playbook_8b654e16_001f_42c1_a283_28cd56c84dba\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0oqf1jy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Create CSV Datatable\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6edc80c4-e5ae-4c33-b1f1-f0c101918d7a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n# The api name of the Data Table to update\\ninputs.dt_datable_name = \\\"dt_utils_test_data_table\\\"\\n# uncomment attachment_id when reading csv data from an attachmennt\\ninputs.attachment_id = attachment.id\\n\\n# A boolean to determine if CSV headers are present\\ninputs.dt_has_headers = True\\n\\n## The mapping format should be \\\"csv_header\\\":\\\"dt_column_name\\\"\\nmapping = \u0027\u0027\u0027{\\n  \\\"hdr_number\\\": \\\"number\\\",\\n  \\\"hdr_text\\\": \\\"text\\\",\\n  \\\"hdr_boolean\\\": \\\"boolean\\\",\\n  \\\"hdr_datetime\\\": \\\"datetime\\\",\\n  \\\"hdr_select\\\": \\\"select\\\",\\n  \\\"hdr_multiselect\\\": \\\"multi_select\\\"\\n}\u0027\u0027\u0027\\n# mappings of csv data without headers will be a list of data_table column names. Use null to bypass a csv data column\\nmapping_no_headers = \u0027\u0027\u0027[\\\"number\\\",\\\"text\\\",\\\"boolean\\\",\\\"datetime\\\",\\\"select\\\",\\\"multi_select\\\",\\\"x\\\",\\\"y\\\",\\\"z\\\"]\u0027\u0027\u0027\\ninputs.dt_mapping_table = mapping\\n# year - %Y, month - %m, day - %d, hour - %H, minutes - %M, seconds - %S, milliseconds - %f, timezone offset - %z\u0027\\ninputs.dt_date_time_format = \\\"%m/%d/%y %H:%M\\\"\\n# optional start row csv data. The first data row = 1\\n##inputs.dt_start_row = 0\\n# optional max number of csv rows to add relative to dt_start_row\\n##inputs.dt_max_rows = 5\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_csv\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0oqf1jy\u003c/incoming\u003e\u003coutgoing\u003eFlow_0yqfaqh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Create CSV Datatable Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"d2400744-b8e5-4f18-ab2a-9a1a16cee3fc\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0yqfaqh\u003c/incoming\u003e\u003coutgoing\u003eFlow_08gr5ba\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0oqf1jy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0yqfaqh\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_08gr5ba\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_08gr5ba\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8b654e16_001f_42c1_a283_28cd56c84dba\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0oqf1jy\" id=\"Flow_0oqf1jy_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0yqfaqh\" id=\"Flow_0yqfaqh_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"295\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"295\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08gr5ba\" id=\"Flow_08gr5ba_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"443\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"443\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"464\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.125\" x=\"617\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"634\" y=\"464\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685356086615,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_8b654e16_001f_42c1_a283_28cd56c84dba",
      "description": {
        "content": "Take CSV data and add the results to a named datatable. Results of the function are written to an incident note.",
        "format": "text"
      },
      "display_name": "Example: Create CSV Datatable (PB)",
      "export_key": "example_create_csv_datatable_pb",
      "field_type_handle": "playbook_8b654e16_001f_42c1_a283_28cd56c84dba",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Create CSV Datatable (PB)",
        "export_key": "playbook_8b654e16_001f_42c1_a283_28cd56c84dba",
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
        "type_name": "playbook_8b654e16_001f_42c1_a283_28cd56c84dba",
        "uuid": "856f172c-62ed-4fa9-a82e-358e4ce55831"
      },
      "has_logical_errors": false,
      "id": 9,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685356718030,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685356692380,
          "description": "",
          "enabled": false,
          "export_key": "Create CSV Datatable Post-Process Script",
          "id": 11,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685356692393,
          "name": "Create CSV Datatable Post-Process Script",
          "object_type": "attachment",
          "playbook_handle": "example_create_csv_datatable_pb",
          "programmatic_name": "example_create_csv_datatable_pb_create_csv_datatable_post_process_script",
          "script_text": "results = playbook.functions.results.create_csv\n\nif results[\u0027success\u0027]:\n  note_text = u\"\"\"Results from Data Table Utils: Create CSV Datatable\\nData Source: {}\\nRows added: {}\\nRows not added: {}\"\"\".format(results.content[\"data_source\"], results.content[\"rows_added\"], results.content[\"rows_with_errors\"])\n  incident.addNote(note_text)\nelse:\n  incident.addNote(u\"Error: Failed to add rows\")",
          "tags": [],
          "uuid": "d2400744-b8e5-4f18-ab2a-9a1a16cee3fc"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_create_csv_datatable_pb",
      "object_type": "attachment",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8b654e16-001f-42c1-a283-28cd56c84dba",
        "id": 12,
        "name": "playbook_8b654e16_001f_42c1_a283_28cd56c84dba",
        "type": "playbook",
        "uuid": "38007b25-a5c9-4e0b-bce6-25afe06c0664"
      },
      "tags": [],
      "type": "default",
      "uuid": "8b654e16-001f-42c1-a283-28cd56c84dba",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b\" isExecutable=\"true\" name=\"playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1kfvs3g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, str):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"dt_col_name\\\": playbook.inputs.dt_name_field, \\\"number\\\": playbook.inputs.dt_number_field, \\\"text\\\": playbook.inputs.dt_text_field, \\\"datetime\\\": playbook.inputs.dt_datetime_field, \\\"boolean\\\": playbook.inputs.dt_boolean_field, \\\"select\\\": playbook.inputs.dt_select_field, \\\"multi_select\\\": playbook.inputs.dt_multi_select_field})\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1kfvs3g\u003c/incoming\u003e\u003coutgoing\u003eFlow_002kch5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1kfvs3g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_002kch5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_002kch5\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1kfvs3g\" id=\"Flow_1kfvs3g_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_002kch5\" id=\"Flow_002kch5_di\"\u003e\u003comgdi:waypoint x=\"730\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"384\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"632\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"664\" y=\"384\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685356826688,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
      "description": {
        "content": "Add a row to the given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Add Row (PB)",
      "export_key": "example_data_table_utils_add_row_pb",
      "field_type_handle": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Add Row (PB)",
        "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
        "fields": {
          "dt_boolean_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_boolean_field",
            "hide_notification": false,
            "id": 1027,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "dt_boolean_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Boolean Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "8b3cc34e-f797-4600-a9f9-39d9ae46c5df",
            "values": []
          },
          "dt_datetime_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_datetime_field",
            "hide_notification": false,
            "id": 1028,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "dt_datetime_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Datetime Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "5d65faed-6942-4dee-a898-ca72cfb32e5a",
            "values": []
          },
          "dt_multi_select_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_multi_select_field",
            "hide_notification": false,
            "id": 1029,
            "input_type": "multiselect",
            "internal": false,
            "is_tracked": false,
            "name": "dt_multi_select_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Multi_Select Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "5655c8ea-32a0-42b9-9e9c-82879a6d76a8",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "a",
                "properties": null,
                "uuid": "dc3caf70-713a-4f03-ac5f-49a1f1c120bb",
                "value": 359
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "b",
                "properties": null,
                "uuid": "a2bdb6bf-1ce0-4183-93e1-fbb0e79a84f3",
                "value": 360
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "c",
                "properties": null,
                "uuid": "895e2bcb-1c8c-4e33-a171-3351942d7cfa",
                "value": 361
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "d",
                "properties": null,
                "uuid": "b525f47c-a8ec-41ff-a8c8-9726a1cfed33",
                "value": 362
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "e",
                "properties": null,
                "uuid": "f9603017-7e80-4edc-81fb-561933754ab5",
                "value": 363
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "f",
                "properties": null,
                "uuid": "dd1f435f-7e17-48ad-971a-4f53db3bc7e7",
                "value": 364
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "g",
                "properties": null,
                "uuid": "4f1d5e96-f2a3-4043-aba0-7fca6352baf0",
                "value": 365
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "h",
                "properties": null,
                "uuid": "73b9c9dc-326c-4005-acac-fd64e7f51d68",
                "value": 366
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "i",
                "properties": null,
                "uuid": "0b1cee5c-db45-46c1-8ff1-ca6a01d70b87",
                "value": 367
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "j",
                "properties": null,
                "uuid": "cc600118-426b-41f4-bd8c-3f0662cc3b31",
                "value": 368
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "k",
                "properties": null,
                "uuid": "83c9dcd4-c91a-4332-9ebe-feafa3361ee5",
                "value": 369
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "l",
                "properties": null,
                "uuid": "13cf19bb-9ee3-485e-9fd0-cd8626cfefc4",
                "value": 370
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "m",
                "properties": null,
                "uuid": "ea52b01c-dc43-4f06-a947-2b050a5a37b2",
                "value": 371
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "n",
                "properties": null,
                "uuid": "89677db2-a38f-43cb-b0c1-8bdbf78fffd8",
                "value": 372
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "o",
                "properties": null,
                "uuid": "82b5dbf7-7f09-4528-9205-78e11e3105a5",
                "value": 373
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "p",
                "properties": null,
                "uuid": "244aceab-083e-4dc6-bf24-3d918e2956a6",
                "value": 374
              }
            ]
          },
          "dt_name_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_name_field",
            "hide_notification": false,
            "id": 1030,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "dt_name_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Name Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "a6a4d19d-9a55-4b7c-9f58-6c4f862b5f53",
            "values": []
          },
          "dt_number_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_number_field",
            "hide_notification": false,
            "id": 1031,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "dt_number_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Number Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "9bc7faa0-b6e7-4980-81b5-e65fe03648bc",
            "values": []
          },
          "dt_select_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_select_field",
            "hide_notification": false,
            "id": 1032,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "dt_select_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Select Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "a6716c38-f0dd-4ee3-bf7b-8c3ac3341c82",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1",
                "properties": null,
                "uuid": "e95187ca-3ddb-4ba3-b591-7e014ab4d849",
                "value": 375
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "2",
                "properties": null,
                "uuid": "ca883afb-a15f-499f-b835-58319ac8d1df",
                "value": 376
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "3",
                "properties": null,
                "uuid": "8f9e3eaa-5d8a-4259-93f4-bea1fe696d2b",
                "value": 377
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "4",
                "properties": null,
                "uuid": "6cf0be13-49d8-4630-a7be-562345764430",
                "value": 378
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "5",
                "properties": null,
                "uuid": "8d6eb000-8b5a-4e83-b4a5-0eb1e67157cf",
                "value": 379
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "6",
                "properties": null,
                "uuid": "9b57b95a-dd17-4e5a-b010-1d9d48a912c6",
                "value": 380
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "7",
                "properties": null,
                "uuid": "31448e6a-5591-46e2-ae6a-ad36be13ade5",
                "value": 381
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "8",
                "properties": null,
                "uuid": "2508a90e-79be-4c6f-912f-78b053318364",
                "value": 382
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "9",
                "properties": null,
                "uuid": "b89e30ee-4878-4bb5-ae6b-4069b3d3e36f",
                "value": 383
              }
            ]
          },
          "dt_text_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b/dt_text_field",
            "hide_notification": false,
            "id": 1033,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "dt_text_field",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Text Field",
            "tooltip": "",
            "type_id": 1012,
            "uuid": "28f9617f-68ce-45f1-b7f2-f56872683e17",
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
        "type_name": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
        "uuid": "c7d46677-ab8c-41dc-b573-2f6520065e6a"
      },
      "has_logical_errors": false,
      "id": 10,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685357285338,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "a6a4d19d-9a55-4b7c-9f58-6c4f862b5f53",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "9bc7faa0-b6e7-4980-81b5-e65fe03648bc",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "28f9617f-68ce-45f1-b7f2-f56872683e17",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "5d65faed-6942-4dee-a898-ca72cfb32e5a",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "8b3cc34e-f797-4600-a9f9-39d9ae46c5df",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "a6716c38-f0dd-4ee3-bf7b-8c3ac3341c82",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "5655c8ea-32a0-42b9-9e9c-82879a6d76a8",
            "element": "field_uuid",
            "field_type": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_data_table_utils_add_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_362842b9-ada1-4d5a-be0c-28c8fbb8b52b",
        "id": 13,
        "name": "playbook_362842b9_ada1_4d5a_be0c_28c8fbb8b52b",
        "type": "playbook",
        "uuid": "59774dfe-48e3-4792-9ac1-a855bd0a5d23"
      },
      "tags": [],
      "type": "default",
      "uuid": "362842b9-ada1-4d5a-be0c-28c8fbb8b52b",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3\" isExecutable=\"true\" name=\"playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0xhbnck\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\nfrom json import dumps\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ntmp = {\\\"dt_col_name\\\": str(artifact.value), \\\"number\\\": 1, \\\"text\\\": \\\"example add row\\\", \\\"datetime\\\": int(datetime.now().timestamp()*1000), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = f\u0027{dumps(tmp)}\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0xhbnck\u003c/incoming\u003e\u003coutgoing\u003eFlow_0et0m9d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0et0m9d\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0xhbnck\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0et0m9d\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xhbnck\" id=\"Flow_0xhbnck_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0et0m9d\" id=\"Flow_0et0m9d_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"304\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"655\" y=\"304\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685357320389,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3",
      "description": {
        "content": "Add a row to the given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Add Row to Datatable (PB)",
      "export_key": "example_data_table_utils_add_row_to_datatable_pb",
      "field_type_handle": "playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Add Row to Datatable (PB)",
        "export_key": "playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3",
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
        "type_name": "playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3",
        "uuid": "7ec90181-9aa5-48fe-93cd-2610eaa1a0b9"
      },
      "has_logical_errors": false,
      "id": 11,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685357415457,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_add_row_to_datatable_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_4b0bbbda-4e65-4341-a3d3-ad42a03474b3",
        "id": 14,
        "name": "playbook_4b0bbbda_4e65_4341_a3d3_ad42a03474b3",
        "type": "playbook",
        "uuid": "b11c4a82-fe88-49c2-a60b-1bf1a91f0c7e"
      },
      "tags": [],
      "type": "default",
      "uuid": "4b0bbbda-4e65-4341-a3d3-ad42a03474b3",
      "version": 9
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_646d920a_1548_489f_ab1c_2232d323227f\" isExecutable=\"true\" name=\"playbook_646d920a_1548_489f_ab1c_2232d323227f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0wj46yc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Clear Datatable\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9149563c-8e72-4025-ab71-305cda30dcc7\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\nif playbook.inputs.datatable_api_name:\\n  inputs.dt_utils_datatable_api_name = playbook.inputs.datatable_api_name\\nelse:\\n  # Defaults to example data table\\n  inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"clear_datatable\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0wj46yc\u003c/incoming\u003e\u003coutgoing\u003eFlow_15zqe0u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Clear Datatable Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"2438b0e5-db83-4abb-afe0-ebca4c291b43\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_15zqe0u\u003c/incoming\u003e\u003coutgoing\u003eFlow_1h68mky\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0wj46yc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_15zqe0u\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1h68mky\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1h68mky\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_646d920a_1548_489f_ab1c_2232d323227f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1h68mky\" id=\"Flow_1h68mky_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"433\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"433\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"454\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_15zqe0u\" id=\"Flow_15zqe0u_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wj46yc\" id=\"Flow_0wj46yc_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"158\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.188\" x=\"628\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"644\" y=\"454\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685357429927,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
      "description": {
        "content": "Clear the content of a given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Clear Datatable (PB)",
      "export_key": "example_data_table_utils_clear_datatable_pb",
      "field_type_handle": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Clear Datatable (PB)",
        "export_key": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
        "fields": {
          "datatable_api_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_646d920a_1548_489f_ab1c_2232d323227f/datatable_api_name",
            "hide_notification": false,
            "id": 1034,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "datatable_api_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "dt_utils_test_data_table",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Datatable API Name",
            "tooltip": "API name of the datatable to clear",
            "type_id": 1014,
            "uuid": "768a050c-446c-4c59-b110-85be6b171540",
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
        "type_name": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
        "uuid": "c8a0dd6d-9a57-4cfc-a75e-e8423641e175"
      },
      "has_logical_errors": false,
      "id": 12,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685435563388,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685357537918,
          "description": "",
          "enabled": false,
          "export_key": "Clear Datatable Post-Process Script",
          "id": 12,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685357537934,
          "name": "Clear Datatable Post-Process Script",
          "object_type": "incident",
          "playbook_handle": "example_data_table_utils_clear_datatable_pb",
          "programmatic_name": "example_data_table_utils_clear_datatable_pb_clear_datatable_post_process_script",
          "script_text": "results = playbook.functions.results.clear_datatable\nif results[\"success\"]:\n  incident.addNote(\"Data table: {} content has been removed.\".format(results[\"inputs\"][\"dt_utils_datatable_api_name\"]))",
          "tags": [],
          "uuid": "2438b0e5-db83-4abb-afe0-ebca4c291b43"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "768a050c-446c-4c59-b110-85be6b171540",
            "element": "field_uuid",
            "field_type": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_data_table_utils_clear_datatable_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_646d920a-1548-489f-ab1c-2232d323227f",
        "id": 15,
        "name": "playbook_646d920a_1548_489f_ab1c_2232d323227f",
        "type": "playbook",
        "uuid": "66aee9c7-73db-4fde-9dca-5c1823a0488d"
      },
      "tags": [],
      "type": "default",
      "uuid": "646d920a-1548-489f-ab1c-2232d323227f",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64\" isExecutable=\"true\" name=\"playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_01fdkfs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"row_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_01fdkfs\u003c/incoming\u003e\u003coutgoing\u003eFlow_06j00o3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cinclusiveGateway default=\"Flow_0ky4pb4\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_06j00o3\u003c/incoming\u003e\u003coutgoing\u003eFlow_0tq9jk7\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0ky4pb4\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The ID of the row to delete [again, taken from previous Get Row Function]\\ninputs.dt_utils_row_id = playbook.functions.results.row_to_delete.content.row[\\\"id\\\"]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"delete_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0tq9jk7\u003c/incoming\u003e\u003coutgoing\u003eFlow_0o6932b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Delete Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fe3ee2b9-19b5-4fa7-9941-1758a88da4a6\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0o6932b\u003c/incoming\u003e\u003coutgoing\u003eFlow_17c1fkk\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_17c1fkk\u003c/incoming\u003e\u003cincoming\u003eFlow_0ky4pb4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_01fdkfs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_06j00o3\" sourceRef=\"ServiceTask_1\" targetRef=\"ConditionPoint_2\"/\u003e\u003csequenceFlow id=\"Flow_0o6932b\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003csequenceFlow id=\"Flow_17c1fkk\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_0tq9jk7\" name=\"success\" sourceRef=\"ConditionPoint_2\" targetRef=\"ServiceTask_3\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\n\\nresults = playbook.functions.results.row_to_delete\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0ky4pb4\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ky4pb4\" id=\"Flow_0ky4pb4_di\"\u003e\u003comgdi:waypoint x=\"719\" y=\"366\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"465\"/\u003e\u003comgdi:waypoint x=\"780\" y=\"465\"/\u003e\u003comgdi:waypoint x=\"780\" y=\"564\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"738\" y=\"447\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0tq9jk7\" id=\"Flow_0tq9jk7_di\"\u003e\u003comgdi:waypoint x=\"719\" y=\"366\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"418\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"599\" y=\"374\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17c1fkk\" id=\"Flow_17c1fkk_di\"\u003e\u003comgdi:waypoint x=\"618\" y=\"590\"/\u003e\u003comgdi:waypoint x=\"714\" y=\"590\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0o6932b\" id=\"Flow_0o6932b_di\"\u003e\u003comgdi:waypoint x=\"520\" y=\"502\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"548\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06j00o3\" id=\"Flow_06j00o3_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"293\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"293\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_01fdkfs\" id=\"Flow_01fdkfs_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"153\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"153\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"600\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"422\" y=\"418\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"422\" y=\"548\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"714\" y=\"564\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685357732567,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64",
      "description": {
        "content": "\t\nAn example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Row (PB)",
      "export_key": "example_data_table_utils_delete_row_pb",
      "field_type_handle": "playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Delete Row (PB)",
        "export_key": "playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64",
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
        "type_name": "playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64",
        "uuid": "0a68436a-8691-4538-b940-3954c2b474e7"
      },
      "has_logical_errors": false,
      "id": 14,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685431381131,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685357859327,
          "description": "",
          "enabled": false,
          "export_key": "Delete Row Post-Process Script",
          "id": 13,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685430380513,
          "name": "Delete Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_delete_row_pb",
          "programmatic_name": "example_data_table_utils_delete_row_pb_delete_row_post_process_script",
          "script_text": "results = playbook.functions.results.delete_row\nif results[\u0027success\u0027]:\n  note = u\"Row id: {} removed from datatable: {} for artifact: {}\".format(results.inputs[\u0027dt_utils_row_id\u0027], results.inputs[\u0027dt_utils_datatable_api_name\u0027], artifact.value)\nelse:\n  note = u\"Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\nincident.addNote(note)",
          "tags": [],
          "uuid": "fe3ee2b9-19b5-4fa7-9941-1758a88da4a6"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_delete_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_44eeca2b-fa37-41d8-9a41-a8b8d02b7d64",
        "id": 17,
        "name": "playbook_44eeca2b_fa37_41d8_9a41_a8b8d02b7d64",
        "type": "playbook",
        "uuid": "4c155367-bade-480b-a2bf-2bebc829d2f2"
      },
      "tags": [],
      "type": "default",
      "uuid": "44eeca2b-fa37-41d8-9a41-a8b8d02b7d64",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97\" isExecutable=\"true\" name=\"playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_06hm4f5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_06hm4f5\u003c/incoming\u003e\u003coutgoing\u003eFlow_151dd2w\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_06hm4f5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_151dd2w\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_151dd2w\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06hm4f5\" id=\"Flow_06hm4f5_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_151dd2w\" id=\"Flow_151dd2w_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"288\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"288\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"644\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685357629382,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97",
      "description": {
        "content": "Delete a row from a datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Row from Datatable (PB)",
      "export_key": "example_data_table_utils_delete_row_from_datatable_pb",
      "field_type_handle": "playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Delete Row from Datatable (PB)",
        "export_key": "playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97",
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
        "type_name": "playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97",
        "uuid": "4c96c7d1-4da8-45cd-8447-873964f958c7"
      },
      "has_logical_errors": false,
      "id": 13,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685357707903,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_delete_row_from_datatable_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_1ab48fa8-3873-40d0-b9f8-f5b6ed693a97",
        "id": 16,
        "name": "playbook_1ab48fa8_3873_40d0_b9f8_f5b6ed693a97",
        "type": "playbook",
        "uuid": "72d65d23-2055-4df1-b3eb-d8bc7a496574"
      },
      "tags": [],
      "type": "default",
      "uuid": "1ab48fa8-3873-40d0-b9f8-f5b6ed693a97",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_8f7c422a_2d77_4a36_a211_4fe474881303\" isExecutable=\"true\" name=\"playbook_8f7c422a_2d77_4a36_a211_4fe474881303\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1lcjb7g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"f7f51c3f-1601-44df-bb83-f7ec9583da96\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"11e8aca8-05bd-467b-8071-9dd160d9e14a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}},\"c42f5cac-9e46-4ee3-bda4-6c9dbe17c516\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"2c359b58-e41e-4dd1-ac65-138e85a27363\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fca27f70-867b-4899-b7c5-f8bdf1bbec13\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"rows_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1lcjb7g\u003c/incoming\u003e\u003coutgoing\u003eFlow_12ipn3j\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1lcjb7g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3dbd1e67-96b6-4eab-9805-788e159a4f2f\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12ipn3j\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hkuwsq\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cinclusiveGateway default=\"Flow_1bpkcfz\" id=\"ConditionPoint_3\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1hkuwsq\u003c/incoming\u003e\u003coutgoing\u003eFlow_0qt09uh\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1bpkcfz\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table, search column, search value [here it is taken from previous Get Rows Function inputs]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The internal IDs of the rows that will be deleted [again, taken from previous Get Rows Function]\\nif playbook.functions.results.rows_to_delete and playbook.functions.results.rows_to_delete.content.rows:\\n  rows_ids = []\\n  for row in playbook.functions.results.rows_to_delete.content.rows:\\n    rows_ids.append(row[\\\"id\\\"])\\n  inputs.dt_utils_rows_ids = str(rows_ids)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"delete_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qt09uh\u003c/incoming\u003e\u003coutgoing\u003eFlow_19kwp5r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"Delete Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"0884170c-86bd-446f-a126-9e1950285b84\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_19kwp5r\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jl2xlf\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_12ipn3j\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1hkuwsq\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_19kwp5r\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_5\"/\u003e\u003cendEvent id=\"EndPoint_6\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jl2xlf\u003c/incoming\u003e\u003cincoming\u003eFlow_1bpkcfz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jl2xlf\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_6\"/\u003e\u003csequenceFlow id=\"Flow_0qt09uh\" name=\"success\" sourceRef=\"ConditionPoint_3\" targetRef=\"ServiceTask_4\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\nresults = playbook.functions.results.rows_to_delete\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1bpkcfz\" name=\"Else\" sourceRef=\"ConditionPoint_3\" targetRef=\"EndPoint_6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8f7c422a_2d77_4a36_a211_4fe474881303\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bpkcfz\" id=\"Flow_1bpkcfz_di\"\u003e\u003comgdi:waypoint x=\"760\" y=\"496\"/\u003e\u003comgdi:waypoint x=\"760\" y=\"590\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"590\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"684\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"758\" y=\"572\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qt09uh\" id=\"Flow_0qt09uh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"496\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"517\"/\u003e\u003comgdi:waypoint x=\"530\" y=\"517\"/\u003e\u003comgdi:waypoint x=\"530\" y=\"538\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"605\" y=\"499\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jl2xlf\" id=\"Flow_0jl2xlf_di\"\u003e\u003comgdi:waypoint x=\"448\" y=\"740\"/\u003e\u003comgdi:waypoint x=\"626\" y=\"740\"/\u003e\u003comgdi:waypoint x=\"626\" y=\"710\"/\u003e\u003comgdi:waypoint x=\"674\" y=\"710\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_19kwp5r\" id=\"Flow_19kwp5r_di\"\u003e\u003comgdi:waypoint x=\"432\" y=\"580\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"580\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"698\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hkuwsq\" id=\"Flow_1hkuwsq_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12ipn3j\" id=\"Flow_12ipn3j_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1lcjb7g\" id=\"Flow_1lcjb7g_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_3\" id=\"ConditionPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"602\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"432\" y=\"538\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"252\" y=\"698\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_6\" id=\"EndPoint_6_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"674\" y=\"684\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685358099429,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_8f7c422a_2d77_4a36_a211_4fe474881303",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Rows (PB)",
      "export_key": "example_data_table_utils_delete_rows_pb",
      "field_type_handle": "playbook_8f7c422a_2d77_4a36_a211_4fe474881303",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Delete Rows (PB)",
        "export_key": "playbook_8f7c422a_2d77_4a36_a211_4fe474881303",
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
        "type_name": "playbook_8f7c422a_2d77_4a36_a211_4fe474881303",
        "uuid": "fe08434f-ca74-4393-ab3c-126ffc6bf6cf"
      },
      "has_logical_errors": false,
      "id": 16,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685432360843,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685358197871,
          "description": "",
          "enabled": false,
          "export_key": "Delete Rows Post-Process Script",
          "id": 15,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685432070423,
          "name": "Delete Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_delete_rows_pb",
          "programmatic_name": "example_data_table_utils_delete_rows_pb_delete_rows_post_process_script",
          "script_text": "results = playbook.functions.results.delete_rows\n\nif results[\u0027success\u0027]:\n  note = u\"\u003cb\u003eResult from Example: Data Table Utils: Artifact: {} Delete Rows\u003c/b\u003e\u003cbr\u003e {}\".format(artifact.value, str(results.content[\"rows_ids\"]))\nelse:\n  note = u\"\u003cb\u003eResult from Example: Data Table Utils: Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\n\nincident.addNote(helper.createRichText(note))",
          "tags": [],
          "uuid": "0884170c-86bd-446f-a126-9e1950285b84"
        },
        {
          "actions": [],
          "created_date": 1685358175982,
          "description": "",
          "enabled": false,
          "export_key": "Get Rows Post-Process Script",
          "id": 14,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685358175991,
          "name": "Get Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_delete_rows_pb",
          "programmatic_name": "example_data_table_utils_delete_rows_pb_get_rows_post_process_script",
          "script_text": "results = playbook.functions.results.rows_to_delete\n\nif not results[\u0027success\u0027]:\n  incident.addNote(helper.createRichText(\"\u003cb\u003eResult from Example: Data Table Utils: Delete Rows\u003c/b\u003e\u003cbr\u003eNo rows found.\"))",
          "tags": [],
          "uuid": "3dbd1e67-96b6-4eab-9805-788e159a4f2f"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_delete_rows_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8f7c422a-2d77-4a36-a211-4fe474881303",
        "id": 19,
        "name": "playbook_8f7c422a_2d77_4a36_a211_4fe474881303",
        "type": "playbook",
        "uuid": "d983447c-e904-4fcf-aa81-23ec40fd9bd0"
      },
      "tags": [],
      "type": "default",
      "uuid": "8f7c422a-2d77-4a36-a211-4fe474881303",
      "version": 12
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_eefbfde1_691f_460d_b485_63f26aae936c\" isExecutable=\"true\" name=\"playbook_eefbfde1_691f_460d_b485_63f26aae936c\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1dsa4ou\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if not row.dt_col_name:\\n  helper.fail(\\\"The data table column \u0027name\u0027 must contain a value\\\")\\n\\ninputs.incident_id = incident.id\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\ninputs.dt_utils_search_value = row.dt_col_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1dsa4ou\u003c/incoming\u003e\u003coutgoing\u003eFlow_10jdwqa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1dsa4ou\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_10jdwqa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_10jdwqa\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_eefbfde1_691f_460d_b485_63f26aae936c\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dsa4ou\" id=\"Flow_1dsa4ou_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_10jdwqa\" id=\"Flow_10jdwqa_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"323\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"323\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"364\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"644\" y=\"364\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685357941578,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_eefbfde1_691f_460d_b485_63f26aae936c",
      "description": {
        "content": "Deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Rows from Datatable (PB)",
      "export_key": "example_data_table_utils_delete_rows_from_datatable_pb",
      "field_type_handle": "playbook_eefbfde1_691f_460d_b485_63f26aae936c",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Delete Rows from Datatable (PB)",
        "export_key": "playbook_eefbfde1_691f_460d_b485_63f26aae936c",
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
        "type_name": "playbook_eefbfde1_691f_460d_b485_63f26aae936c",
        "uuid": "802a1158-dba6-4b06-bfd8-dce7c3bdf964"
      },
      "has_logical_errors": false,
      "id": 15,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685358061200,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_delete_rows_from_datatable_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_eefbfde1-691f-460d-b485-63f26aae936c",
        "id": 18,
        "name": "playbook_eefbfde1_691f_460d_b485_63f26aae936c",
        "type": "playbook",
        "uuid": "f2547bb5-71c3-4973-8c10-d70a2c03019b"
      },
      "tags": [],
      "type": "default",
      "uuid": "eefbfde1-691f-460d-b485-63f26aae936c",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0\" isExecutable=\"true\" name=\"playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1gawkcj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get All Data Table Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8a56f5fb-1623-4039-bd80-ed5a5a1bf05b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_all_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1gawkcj\u003c/incoming\u003e\u003coutgoing\u003eFlow_0slr94v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get All Data Table Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a93254df-73f2-417f-80ea-79438ae27374\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0slr94v\u003c/incoming\u003e\u003coutgoing\u003eFlow_0w6apcm\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1gawkcj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0slr94v\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0w6apcm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0w6apcm\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1gawkcj\" id=\"Flow_1gawkcj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0slr94v\" id=\"Flow_0slr94v_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0w6apcm\" id=\"Flow_0w6apcm_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"424\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"655\" y=\"424\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685358357668,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0",
      "description": {
        "content": "Return all of the rows from a data table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get All Data Table Rows (PB)",
      "export_key": "example_data_table_utils_get_all_data_table_rows_pb",
      "field_type_handle": "playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Get All Data Table Rows (PB)",
        "export_key": "playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0",
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
        "type_name": "playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0",
        "uuid": "cd03b17e-e423-465a-b75f-49a588066eb6"
      },
      "has_logical_errors": false,
      "id": 17,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685358446894,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685358424417,
          "description": "",
          "enabled": false,
          "export_key": "Get All Data Table Rows Post-Process Script",
          "id": 16,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685358424426,
          "name": "Get All Data Table Rows Post-Process Script",
          "object_type": "dt_utils_test_data_table",
          "playbook_handle": "example_data_table_utils_get_all_data_table_rows_pb",
          "programmatic_name": "example_data_table_utils_get_all_data_table_rows_pb_get_all_data_table_rows_post_process_script",
          "script_text": "note_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get All Data Table Rows\u003c/b\u003e\u003cbr\u003e\"\nresults = playbook.functions.results.get_all_rows\n\nif results.success:\n  note_text = u\"{0} \u003cbr\u003e{1}\".format(note_text, str(results.content.rows))\nelse:\n  note_text = u\"{0} \u003cbr\u003eNo rows found.\".format(note_text)\n \n  \n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "a93254df-73f2-417f-80ea-79438ae27374"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_get_all_data_table_rows_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7e3edc59-0f64-4a28-8c64-d1d2375eb1d0",
        "id": 20,
        "name": "playbook_7e3edc59_0f64_4a28_8c64_d1d2375eb1d0",
        "type": "playbook",
        "uuid": "44d31ab9-08c2-4e08-95f3-85b4a767f5e9"
      },
      "tags": [],
      "type": "default",
      "uuid": "7e3edc59-0f64-4a28-8c64-d1d2375eb1d0",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698\" isExecutable=\"true\" name=\"playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_11fb9je\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_current_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_11fb9je\u003c/incoming\u003e\u003coutgoing\u003eFlow_0cv2qrq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_11fb9je\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Current Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"89b709aa-d31f-4aed-95d7-494d4ad6ef01\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0cv2qrq\u003c/incoming\u003e\u003coutgoing\u003eFlow_19uzvwq\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0cv2qrq\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_19uzvwq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_19uzvwq\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_11fb9je\" id=\"Flow_11fb9je_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0cv2qrq\" id=\"Flow_0cv2qrq_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"270\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"270\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"298\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_19uzvwq\" id=\"Flow_19uzvwq_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"382\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"403\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"403\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"424\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.758\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"298\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"634\" y=\"424\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685358466004,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Row Function. Get the the current row of the datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Current Row (PB)",
      "export_key": "example_data_table_utils_get_current_row_pb",
      "field_type_handle": "playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Get Current Row (PB)",
        "export_key": "playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698",
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
        "type_name": "playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698",
        "uuid": "2b35fc48-3607-4a67-9f0f-a8bb8af34424"
      },
      "has_logical_errors": false,
      "id": 18,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685358550149,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685358519522,
          "description": "",
          "enabled": false,
          "export_key": "Get Current Row Post-Process Script",
          "id": 17,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685358519532,
          "name": "Get Current Row Post-Process Script",
          "object_type": "dt_utils_test_data_table",
          "playbook_handle": "example_data_table_utils_get_current_row_pb",
          "programmatic_name": "example_data_table_utils_get_current_row_pb_get_current_row_post_process_script",
          "script_text": "note_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Row\u003c/b\u003e\u003cbr\u003e\"\nresults = playbook.functions.results.get_current_row\nif results.success:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"row\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "89b709aa-d31f-4aed-95d7-494d4ad6ef01"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_get_current_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_adfa4ae2-c29d-4eb1-92f5-64265808f698",
        "id": 21,
        "name": "playbook_adfa4ae2_c29d_4eb1_92f5_64265808f698",
        "type": "playbook",
        "uuid": "d46ff091-c292-410e-a02b-9dbefabd634a"
      },
      "tags": [],
      "type": "default",
      "uuid": "adfa4ae2-c29d-4eb1-92f5-64265808f698",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_b91648da_1ce0_41da_8876_a8f83447150d\" isExecutable=\"true\" name=\"playbook_b91648da_1ce0_41da_8876_a8f83447150d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1mu2344\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1mu2344\u003c/incoming\u003e\u003coutgoing\u003eFlow_13q1ilh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e850b28f-d3f2-4327-91a0-309ef3e562f9\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_13q1ilh\u003c/incoming\u003e\u003coutgoing\u003eFlow_0q9ysxq\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0q9ysxq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1mu2344\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_13q1ilh\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_0q9ysxq\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_b91648da_1ce0_41da_8876_a8f83447150d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1mu2344\" id=\"Flow_1mu2344_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_13q1ilh\" id=\"Flow_13q1ilh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"295\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"295\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0q9ysxq\" id=\"Flow_0q9ysxq_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"428\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"428\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"454\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"634\" y=\"454\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685358570079,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_b91648da_1ce0_41da_8876_a8f83447150d",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then returns that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Row (PB)",
      "export_key": "example_data_table_utils_get_row_pb",
      "field_type_handle": "playbook_b91648da_1ce0_41da_8876_a8f83447150d",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Get Row (PB)",
        "export_key": "playbook_b91648da_1ce0_41da_8876_a8f83447150d",
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
        "type_name": "playbook_b91648da_1ce0_41da_8876_a8f83447150d",
        "uuid": "7bca1e5c-4985-4462-bd22-74f2a945bada"
      },
      "has_logical_errors": false,
      "id": 19,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685358908267,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685358874020,
          "description": "",
          "enabled": false,
          "export_key": "Get Row Post-Process Script",
          "id": 18,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685358874029,
          "name": "Get Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_get_row_pb",
          "programmatic_name": "example_data_table_utils_get_row_pb_get_row_post_process_script",
          "script_text": "results = playbook.functions.results.get_row\nnote_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Row\u003c/b\u003e\u003cbr\u003e search value: {}\".format(results[\"inputs\"][\"dt_utils_search_value\"])\n\nif results[\"success\"]:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"row\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "e850b28f-d3f2-4327-91a0-309ef3e562f9"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_get_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_b91648da-1ce0-41da-8876-a8f83447150d",
        "id": 22,
        "name": "playbook_b91648da_1ce0_41da_8876_a8f83447150d",
        "type": "playbook",
        "uuid": "700d57cd-5f3b-4be9-ac37-a7af130cce81"
      },
      "tags": [],
      "type": "default",
      "uuid": "b91648da-1ce0-41da-8876-a8f83447150d",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_1c8044df_59e9_4f55_b823_67d0522c4a42\" isExecutable=\"true\" name=\"playbook_1c8044df_59e9_4f55_b823_67d0522c4a42\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_14a6t43\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"f7f51c3f-1601-44df-bb83-f7ec9583da96\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"11e8aca8-05bd-467b-8071-9dd160d9e14a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}},\"c42f5cac-9e46-4ee3-bda4-6c9dbe17c516\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"2c359b58-e41e-4dd1-ac65-138e85a27363\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fca27f70-867b-4899-b7c5-f8bdf1bbec13\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The number of max rows to return\\nif playbook.inputs.dt_utils_max_rows:\\n  inputs.dt_utils_max_rows = playbook.inputs.dt_utils_max_rows\\nelse:\\n  inputs.dt_utils_max_rows = 0\\n\\n# The direction of the sort\\ninputs.dt_utils_sort_direction = playbook.inputs.dt_utils_sort_direction\\n\\n# The api name of the column to sort by\\nif playbook.inputs.dt_utils_sort_by:\\n  inputs.dt_utils_sort_by = playbook.inputs.dt_utils_sort_by\\nelse:\\n  inputs.dt_utils_sort_by = None\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_14a6t43\u003c/incoming\u003e\u003coutgoing\u003eFlow_0c03m7w\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"66947e6c-6582-4880-8234-9d3f05e6efb0\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0c03m7w\u003c/incoming\u003e\u003coutgoing\u003eFlow_1a26xmy\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1a26xmy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_14a6t43\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0c03m7w\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1a26xmy\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1c8044df_59e9_4f55_b823_67d0522c4a42\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_14a6t43\" id=\"Flow_14a6t43_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0c03m7w\" id=\"Flow_0c03m7w_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"288\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1a26xmy\" id=\"Flow_1a26xmy_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"372\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"414\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"288\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"655\" y=\"414\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685358941824,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Rows (PB)",
      "export_key": "example_data_table_utils_get_rows_pb",
      "field_type_handle": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Get Rows (PB)",
        "export_key": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
        "fields": {
          "dt_utils_max_rows": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42/dt_utils_max_rows",
            "hide_notification": false,
            "id": 1035,
            "input_type": "number",
            "internal": false,
            "is_tracked": false,
            "name": "dt_utils_max_rows",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Max Rows",
            "tooltip": "A number of max rows to return",
            "type_id": 1022,
            "uuid": "b5e4b03e-e24e-4866-928b-23764285c0bf",
            "values": []
          },
          "dt_utils_sort_by": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42/dt_utils_sort_by",
            "hide_notification": false,
            "id": 1036,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "dt_utils_sort_by",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sort By",
            "tooltip": "The name of the API column",
            "type_id": 1022,
            "uuid": "e27380b1-2106-4a5c-863b-077ff0455ada",
            "values": []
          },
          "dt_utils_sort_direction": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42/dt_utils_sort_direction",
            "hide_notification": false,
            "id": 1037,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "dt_utils_sort_direction",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sort Direction",
            "tooltip": "Used with the Sort By API column name",
            "type_id": 1022,
            "uuid": "2a182307-e67e-4fa1-a8d9-caf0168a263c",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "ASC",
                "properties": null,
                "uuid": "aea640b3-7921-4f33-931c-1c31dba47235",
                "value": 384
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "DESC",
                "properties": null,
                "uuid": "36fb2a7b-a917-49f3-8f4f-7b75bff4daf0",
                "value": 385
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
        "type_name": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
        "uuid": "ffa9fae3-cf0a-4ac3-98cc-9a06cd505325"
      },
      "has_logical_errors": false,
      "id": 20,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685359125684,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685359101924,
          "description": "",
          "enabled": false,
          "export_key": "Get Rows Post-Process Script",
          "id": 19,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685359101932,
          "name": "Get Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_get_rows_pb",
          "programmatic_name": "example_data_table_utils_get_rows_pb_get_rows_post_process_script",
          "script_text": "results = playbook.functions.results.get_rows\nnote_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Rows\u003c/b\u003e\u003cbr\u003e search value: {}\".format(results[\"inputs\"][\"dt_utils_search_value\"])\n\n\nif results[\"success\"]:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"rows\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "66947e6c-6582-4880-8234-9d3f05e6efb0"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "e27380b1-2106-4a5c-863b-077ff0455ada",
            "element": "field_uuid",
            "field_type": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "2a182307-e67e-4fa1-a8d9-caf0168a263c",
            "element": "field_uuid",
            "field_type": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b5e4b03e-e24e-4866-928b-23764285c0bf",
            "element": "field_uuid",
            "field_type": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_data_table_utils_get_rows_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_1c8044df-59e9-4f55-b823-67d0522c4a42",
        "id": 23,
        "name": "playbook_1c8044df_59e9_4f55_b823_67d0522c4a42",
        "type": "playbook",
        "uuid": "2d5fdc42-bc80-4378-bdcb-37583b45d700"
      },
      "tags": [],
      "type": "default",
      "uuid": "1c8044df-59e9-4f55-b823-67d0522c4a42",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_fb922654_9fff_4452_87b7_bebcb3606d30\" isExecutable=\"true\" name=\"playbook_fb922654_9fff_4452_87b7_bebcb3606d30\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0g62n7n\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"row_to_update\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0g62n7n\u003c/incoming\u003e\u003coutgoing\u003eFlow_121xvw9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cinclusiveGateway default=\"Flow_1fu9la0\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_121xvw9\u003c/incoming\u003e\u003coutgoing\u003eFlow_0zyrg8v\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1fu9la0\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\nfrom json import dumps\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\ninputs.dt_utils_row_id = playbook.functions.results.row_to_update.content.row[\\\"id\\\"]\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ntmp = {\\\"datetime\\\": int(datetime.now().timestamp()*1000), \\\"text\\\": \\\"Updated from Artifact\\\"}\\ninputs.dt_utils_cells_to_update = f\u0027{dumps(tmp)}\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0zyrg8v\u003c/incoming\u003e\u003coutgoing\u003eFlow_1qv0pwk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Delete Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"1eb54c2d-1cbe-4886-9764-a27f9431cc2b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1qv0pwk\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jraktx\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_5\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jraktx\u003c/incoming\u003e\u003cincoming\u003eFlow_1fu9la0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0g62n7n\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_121xvw9\" sourceRef=\"ServiceTask_1\" targetRef=\"ConditionPoint_2\"/\u003e\u003csequenceFlow id=\"Flow_1qv0pwk\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003csequenceFlow id=\"Flow_0jraktx\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_0zyrg8v\" name=\"success\" sourceRef=\"ConditionPoint_2\" targetRef=\"ServiceTask_3\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\n\\nresults = playbook.functions.results.row_to_update\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1fu9la0\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"EndPoint_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_fb922654_9fff_4452_87b7_bebcb3606d30\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0g62n7n\" id=\"Flow_0g62n7n_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"153\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"153\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_121xvw9\" id=\"Flow_121xvw9_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"308\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"308\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"344\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zyrg8v\" id=\"Flow_0zyrg8v_di\"\u003e\u003comgdi:waypoint x=\"719\" y=\"396\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"437\"/\u003e\u003comgdi:waypoint x=\"530\" y=\"437\"/\u003e\u003comgdi:waypoint x=\"530\" y=\"478\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"604\" y=\"419\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qv0pwk\" id=\"Flow_1qv0pwk_di\"\u003e\u003comgdi:waypoint x=\"530\" y=\"562\"/\u003e\u003comgdi:waypoint x=\"530\" y=\"585\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"585\"/\u003e\u003comgdi:waypoint x=\"510\" y=\"608\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jraktx\" id=\"Flow_0jraktx_di\"\u003e\u003comgdi:waypoint x=\"608\" y=\"650\"/\u003e\u003comgdi:waypoint x=\"671\" y=\"650\"/\u003e\u003comgdi:waypoint x=\"671\" y=\"660\"/\u003e\u003comgdi:waypoint x=\"734\" y=\"660\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1fu9la0\" id=\"Flow_1fu9la0_di\"\u003e\u003comgdi:waypoint x=\"719\" y=\"396\"/\u003e\u003comgdi:waypoint x=\"719\" y=\"515\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"515\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"634\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"748\" y=\"497\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"600\" y=\"344\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"432\" y=\"478\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"412\" y=\"608\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_5\" id=\"EndPoint_5_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"734\" y=\"634\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1685359151772,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_fb922654_9fff_4452_87b7_bebcb3606d30",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Update Row (PB)",
      "export_key": "example_data_table_utils_update_row_pb",
      "field_type_handle": "playbook_fb922654_9fff_4452_87b7_bebcb3606d30",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Update Row (PB)",
        "export_key": "playbook_fb922654_9fff_4452_87b7_bebcb3606d30",
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
        "type_name": "playbook_fb922654_9fff_4452_87b7_bebcb3606d30",
        "uuid": "f42104de-9c0e-4b73-adf4-234930a5fb2e"
      },
      "has_logical_errors": false,
      "id": 21,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 15,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1685359364029,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1685359255072,
          "description": "",
          "enabled": false,
          "export_key": "Delete Row Post-Process Script",
          "id": 20,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1685359255081,
          "name": "Delete Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "example_data_table_utils_update_row_pb",
          "programmatic_name": "example_data_table_utils_update_row_pb_delete_row_post_process_script",
          "script_text": "results = playbook.functions.results.update_row\nif results.success:\n  note = u\"Row id: {} removed from datatable: {} for artifact: {}\".format(results.inputs[\u0027dt_utils_row_id\u0027], results.inputs[\u0027dt_utils_datatable_api_name\u0027], artifact.value)\nelse:\n  note = u\"Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\nincident.addNote(note)",
          "tags": [],
          "uuid": "1eb54c2d-1cbe-4886-9764-a27f9431cc2b"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_data_table_utils_update_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_fb922654-9fff-4452-87b7-bebcb3606d30",
        "id": 24,
        "name": "playbook_fb922654_9fff_4452_87b7_bebcb3606d30",
        "type": "playbook",
        "uuid": "c0ae2cff-a769-45fb-9855-e97380dec0b1"
      },
      "tags": [],
      "type": "default",
      "uuid": "fb922654-9fff-4452-87b7-bebcb3606d30",
      "version": 6
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 8131,
    "major": 46,
    "minor": 0,
    "version": "46.0.8131"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Example CSV Datatable",
      "export_key": "dt_utils_test_data_table",
      "fields": {
        "boolean": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/boolean",
          "hide_notification": false,
          "id": 930,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "boolean",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "boolean",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "8fe94e4d-e591-41e9-af15-18fc2cf96a96",
          "values": [],
          "width": 87
        },
        "datetime": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/datetime",
          "hide_notification": false,
          "id": 931,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "datetime",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "datetime",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "bf9e6153-abe6-40e7-bcb0-f45024804eef",
          "values": [],
          "width": 225
        },
        "dt_col_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/dt_col_name",
          "hide_notification": false,
          "id": 932,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "dt_col_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "name",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "b167a766-24fc-4c68-a865-b44f19b53b97",
          "values": [],
          "width": 68
        },
        "multi_select": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/multi_select",
          "hide_notification": false,
          "id": 933,
          "input_type": "multiselect",
          "internal": false,
          "is_tracked": false,
          "name": "multi_select",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "multi_select",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "5686792a-79b8-4756-b0f2-f1ec085bc37a",
          "values": [
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "a",
              "properties": null,
              "uuid": "587c135e-2d39-4140-822e-7829b03d4a21",
              "value": 252
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "b",
              "properties": null,
              "uuid": "b5514bda-e2f8-41d1-bf39-a2d09f37214a",
              "value": 253
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "c",
              "properties": null,
              "uuid": "6282c55c-af54-4c98-b5d1-12db87a4c76a",
              "value": 254
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "d",
              "properties": null,
              "uuid": "29eaf525-205a-46a5-b591-e023157053b4",
              "value": 255
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "e",
              "properties": null,
              "uuid": "48f95069-25a8-4919-9004-7066543dbcd5",
              "value": 256
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "f",
              "properties": null,
              "uuid": "e11c6dc8-70cc-4448-917a-93ab16c864e0",
              "value": 257
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "g",
              "properties": null,
              "uuid": "ebcbf31c-f5b2-4d3a-b1fe-334ce7cdaa9b",
              "value": 258
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "h",
              "properties": null,
              "uuid": "3f2963b6-8e1b-44b5-ba59-32cfbe7bdf5b",
              "value": 259
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "I",
              "properties": null,
              "uuid": "484dc992-3526-4e06-a392-fe8647373913",
              "value": 260
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "j",
              "properties": null,
              "uuid": "28c16106-f096-4565-b601-3a03da496559",
              "value": 261
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "k",
              "properties": null,
              "uuid": "260a964d-63e7-483d-b4f8-6822206830d0",
              "value": 262
            }
          ],
          "width": 64
        },
        "number": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/number",
          "hide_notification": false,
          "id": 934,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "number",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "number",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "97a819fd-cbcf-4eda-a245-c1d50ce27ae6",
          "values": [],
          "width": 84
        },
        "select": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/select",
          "hide_notification": false,
          "id": 935,
          "input_type": "select",
          "internal": false,
          "is_tracked": false,
          "name": "select",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "select",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "e2239bee-9516-4c7f-852a-2a884bcbaf0f",
          "values": [
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "1",
              "properties": null,
              "uuid": "6559ac56-25a2-4015-a681-9e89328da0a3",
              "value": 263
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "2",
              "properties": null,
              "uuid": "bd341de4-c08e-4ba2-9179-04a28a32e22e",
              "value": 264
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "3",
              "properties": null,
              "uuid": "9d7a37be-a50a-4bdf-8478-63e4be6ec4bc",
              "value": 265
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "4",
              "properties": null,
              "uuid": "8ecdf624-0e32-46f7-8d8a-f183c8559032",
              "value": 266
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "5",
              "properties": null,
              "uuid": "653d3e8e-00c9-41f4-85f2-10addde4b1ba",
              "value": 267
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "6",
              "properties": null,
              "uuid": "b5746a1b-9404-4b9c-bb20-924682a3ad97",
              "value": 268
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "7",
              "properties": null,
              "uuid": "b3f95da8-12fb-44f0-9f89-9b1ee269762b",
              "value": 269
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "8",
              "properties": null,
              "uuid": "d6d40d79-d0c4-4122-b982-91114e4b801b",
              "value": 270
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "9",
              "properties": null,
              "uuid": "ec4b97d4-b313-4ded-bb0d-eda35b6dc172",
              "value": 271
            }
          ],
          "width": 32
        },
        "text": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "dt_utils_test_data_table/text",
          "hide_notification": false,
          "id": 936,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "text",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "text",
          "tooltip": "",
          "type_id": 1010,
          "uuid": "3be7be3d-9931-4386-a845-a62bfe26f017",
          "values": [],
          "width": 123
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
      "type_name": "dt_utils_test_data_table",
      "uuid": "0b69525c-fbed-42d9-b368-81e06759ed90"
    }
  ],
  "workflows": [],
  "workspaces": []
}
