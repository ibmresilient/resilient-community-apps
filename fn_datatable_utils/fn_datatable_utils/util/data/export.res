{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Add Row",
      "id": 161,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Add Row",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e078c8fa-546d-4d24-8592-447d454de8ff",
      "view_items": [
        {
          "content": "0dd7ea75-2bad-4d91-a425-126a59eb993a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "900f6d29-9a9d-4af1-aa2e-78463cfc05ce",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e3bf7c9a-a1d2-49fd-93ae-9d8bdb36087a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fa5e939f-ce40-4498-a479-98a320da4492",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a05790cc-fd48-442b-a04c-2303ab72edd0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "689d93f8-58a3-4795-8a98-dd4222879b13",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66bc42be-70ad-432d-b239-22d83fb8ffed",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_data_table_utils_add_row"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Add Row to Datatable",
      "id": 162,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Add Row to Datatable",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7f89e72a-0334-46c8-bd7a-5fc5ba4512ec",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_add_row_to_datatable"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Clear Datatable",
      "id": 163,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Clear Datatable",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d090aaea-5c7b-4ae4-949d-0f8fb61914c0",
      "view_items": [
        {
          "content": "bdbb5bab-6625-4ef0-a5a9-3026aa531693",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_data_table_utils_clear_datatable"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Delete Current Row",
      "id": 164,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Delete Current Row",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2839d707-84a8-4622-adad-329b2ab3692f",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_delete_row_from_datatable"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Delete Data Table Row",
      "id": 165,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Delete Data Table Row",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f4d26cf4-999d-4e07-9bf4-776d379fe62a",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_delete_row"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Delete Data Table Rows",
      "id": 166,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Delete Data Table Rows",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "872d1190-54ec-4797-9a11-4d1d43e3fe45",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_delete_rows"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Delete Rows by Name",
      "id": 167,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Delete Rows by Name",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8888e08e-b440-4d7a-b3f9-896b381b99ea",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_delete_rows_from_datatable"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Create CSV Datatable",
      "id": 168,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Create CSV Datatable",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fbf95f1f-2ff5-47b2-9080-78a24e9c67db",
      "view_items": [],
      "workflows": [
        "example_create_csv_datatable"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get All Rows",
      "id": 169,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get All Rows",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "50afe059-ba5f-4059-9fa0-27b5e2cd41e6",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_get_all_data_table_rows"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get Current Row",
      "id": 170,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get Current Row",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8c2db262-5ba4-4482-986e-7b60cb047c1c",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_get_current_row"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get Data Table Row",
      "id": 171,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get Data Table Row",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "72438e7c-5c6e-4b1d-b9c8-fd6e6ef8d845",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_get_row"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get Data Table Rows",
      "id": 172,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get Data Table Rows",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "79515c29-290e-4ebf-94cf-3fddbd1d526a",
      "view_items": [
        {
          "content": "682aceff-2916-440e-9cf6-be00a17b2d9e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "23d69de0-6d53-4178-ac35-c81e132bc48e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ccf141bf-4137-47f8-96ed-35b83b72da58",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_data_table_utils_get_rows"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Update Current Row",
      "id": 173,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Update Current Row",
      "object_type": "dt_utils_test_data_table",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "034c60b1-a58f-45b6-9ecc-7be692a84d52",
      "view_items": [],
      "workflows": [
        "update_row"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Update Data Table Row",
      "id": 174,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Update Data Table Row",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a471f10b-333d-487d-8eb1-15e2ed638ec2",
      "view_items": [],
      "workflows": [
        "example_data_table_utils_update_row"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1684931495049,
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
      "id": 1757,
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
      "id": 1758,
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
      "id": 1759,
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
      "id": 1760,
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
      "id": 1761,
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
      "id": 1762,
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
      "id": 1763,
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
      "id": 1764,
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
      "id": 1765,
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
      "id": 1766,
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
      "id": 1767,
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
      "id": 1768,
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
      "id": 1769,
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
      "id": 1770,
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
      "id": 1771,
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
      "id": 1772,
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
      "id": 1773,
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
      "id": 1774,
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
          "value": 830
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DESC",
          "properties": null,
          "uuid": "4c223e4f-b70c-4957-9c7f-86761015b24c",
          "value": 831
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
      "id": 1775,
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
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/dt_number_field",
      "hide_notification": false,
      "id": 1746,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_number_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Number Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "900f6d29-9a9d-4af1-aa2e-78463cfc05ce",
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
      "export_key": "actioninvocation/dt_boolean_field",
      "hide_notification": false,
      "id": 1747,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "dt_boolean_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Boolean Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "a05790cc-fd48-442b-a04c-2303ab72edd0",
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
      "export_key": "actioninvocation/datatable_api_name",
      "hide_notification": false,
      "id": 1748,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "datatable_api_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "dt_utils_test_data_table",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Datatable API Name",
      "tooltip": "API name of the datatable to clear",
      "type_id": 6,
      "uuid": "bdbb5bab-6625-4ef0-a5a9-3026aa531693",
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
      "export_key": "actioninvocation/dt_utils_max_rows",
      "hide_notification": false,
      "id": 1749,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_max_rows",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Max Rows",
      "tooltip": "A number of max rows to return",
      "type_id": 6,
      "uuid": "ccf141bf-4137-47f8-96ed-35b83b72da58",
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
      "export_key": "actioninvocation/dt_text_field",
      "hide_notification": false,
      "id": 1750,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_text_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Text Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "e3bf7c9a-a1d2-49fd-93ae-9d8bdb36087a",
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
      "export_key": "actioninvocation/dt_datetime_field",
      "hide_notification": false,
      "id": 1751,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "dt_datetime_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Datetime Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "fa5e939f-ce40-4498-a479-98a320da4492",
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
      "export_key": "actioninvocation/dt_name_field",
      "hide_notification": false,
      "id": 1752,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_name_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Name Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "0dd7ea75-2bad-4d91-a425-126a59eb993a",
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
      "export_key": "actioninvocation/dt_utils_sort_direction",
      "hide_notification": false,
      "id": 1753,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_sort_direction",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Sort Direction",
      "tooltip": "Used with the Sort By API column name",
      "type_id": 6,
      "uuid": "23d69de0-6d53-4178-ac35-c81e132bc48e",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "ASC",
          "properties": null,
          "uuid": "2ee29ddc-cac4-47b4-aeb7-0c535eae7010",
          "value": 803
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DESC",
          "properties": null,
          "uuid": "479c72d7-8040-4f93-bf98-6266f3c49900",
          "value": 804
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
      "export_key": "actioninvocation/dt_multi_select_field",
      "hide_notification": false,
      "id": 1754,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "dt_multi_select_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Multi_Select Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "66bc42be-70ad-432d-b239-22d83fb8ffed",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "a",
          "properties": null,
          "uuid": "d97cf301-c44b-433d-ad3d-4f66ed280dae",
          "value": 805
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "b",
          "properties": null,
          "uuid": "0890688b-622d-4e49-a614-b514a1b1ce9f",
          "value": 806
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "c",
          "properties": null,
          "uuid": "5cb5d3ce-a7e9-4697-82f5-e446058c06e5",
          "value": 807
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "d",
          "properties": null,
          "uuid": "e00490d6-ff49-4cd7-b9f5-30fe20689117",
          "value": 808
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "e",
          "properties": null,
          "uuid": "61ef8c0f-b361-4394-b768-c333d1e91c52",
          "value": 809
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "f",
          "properties": null,
          "uuid": "86567cd3-59b6-4067-9c15-a61d5bd85a61",
          "value": 810
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "g",
          "properties": null,
          "uuid": "0bea5e06-7764-4d32-8030-8fba92006e9a",
          "value": 811
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "h",
          "properties": null,
          "uuid": "6bc78a07-d8cc-4549-8fe1-2fdd4cea6dfc",
          "value": 812
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "i",
          "properties": null,
          "uuid": "d6bf7af7-abef-4b0b-9417-039d2ec8aa72",
          "value": 813
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "j",
          "properties": null,
          "uuid": "2256f415-7e19-4d0d-b761-b49b3d7bbbfc",
          "value": 814
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "k",
          "properties": null,
          "uuid": "266ffb03-4dbd-4e6f-a3ca-1aee0736ced0",
          "value": 815
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "l",
          "properties": null,
          "uuid": "69c57e8c-e045-4a11-b869-6c0d7dad0628",
          "value": 816
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "m",
          "properties": null,
          "uuid": "5c113371-d5ca-4ad4-8202-8239d78275b6",
          "value": 817
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "n",
          "properties": null,
          "uuid": "016b354c-c367-4efc-b262-acb2e4af248f",
          "value": 818
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "o",
          "properties": null,
          "uuid": "5649da7c-33f0-468f-8c0a-8812eee28098",
          "value": 819
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "p",
          "properties": null,
          "uuid": "97326585-18c6-4e51-abae-d3e049dd154a",
          "value": 820
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
      "export_key": "actioninvocation/dt_utils_sort_by",
      "hide_notification": false,
      "id": 1755,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "dt_utils_sort_by",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Sort By",
      "tooltip": "The name of the API column",
      "type_id": 6,
      "uuid": "682aceff-2916-440e-9cf6-be00a17b2d9e",
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
      "export_key": "actioninvocation/dt_select_field",
      "hide_notification": false,
      "id": 1756,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "dt_select_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Select Field",
      "tooltip": "",
      "type_id": 6,
      "uuid": "689d93f8-58a3-4795-8a98-dd4222879b13",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "1",
          "properties": null,
          "uuid": "ff45ab7b-c795-493b-8619-e2cdbfaf49ca",
          "value": 821
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "2",
          "properties": null,
          "uuid": "6e356fcc-ef96-4d20-8082-25ede5ce3072",
          "value": 822
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "3",
          "properties": null,
          "uuid": "77899a0a-444f-4954-83a1-20c8bd864190",
          "value": 823
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "4",
          "properties": null,
          "uuid": "3d013415-45de-41de-a77c-0bcb1a909a7d",
          "value": 824
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "5",
          "properties": null,
          "uuid": "8118fb9e-1d58-4233-bcc2-8e635261939c",
          "value": 825
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "6",
          "properties": null,
          "uuid": "525bf401-3d27-4db7-a33d-40ab1cd61532",
          "value": 826
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "7",
          "properties": null,
          "uuid": "c852cc6b-2660-4e83-8a57-845d22063c64",
          "value": 827
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "8",
          "properties": null,
          "uuid": "cb703b7a-d070-43a8-b3cd-dd662850eb27",
          "value": 828
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "9",
          "properties": null,
          "uuid": "fb477141-6ad9-4da0-bf38-d47390eeda76",
          "value": 829
        }
      ]
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
      "created_date": 1683278090057,
      "description": {
        "content": "Add a row to a given datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Add Row",
      "export_key": "dt_utils_add_row",
      "id": 118,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090089,
      "name": "dt_utils_add_row",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"select\": \"1\", \"number\": 1, \"datetime\": 1654019149216, \"boolean\": true, \"multi_select\": [\"a\", \"b\"], \"dt_col_name\": \"fGzfdhgxj\", \"text\": \"example add row\"}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_cells_to_update\": \"{ \\\"select\\\":\\\"1\\\",\\\"number\\\":1,\\\"datetime\\\":1654019149216,\\\"boolean\\\":true,\\\"multi_select\\\":[\u0027a\u0027, \u0027b\u0027],\\\"dt_col_name\\\":\\\"fGzfdhgxj\\\",\\\"text\\\":\\\"example add row\\\" }\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 546, \"timestamp\": \"2022-05-31 13:45:50\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"select\": {\"type\": \"string\"}, \"number\": {\"type\": \"integer\"}, \"datetime\": {\"type\": \"integer\"}, \"boolean\": {\"type\": \"boolean\"}, \"multi_select\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"dt_col_name\": {\"type\": \"string\"}, \"text\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_cells_to_update\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "88e45595-8f9b-4521-986c-22e53de7abf3",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Add Row",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "example_data_table_utils_add_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 107
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Add Row to Datatable",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_add_row_to_datatable",
          "tags": [],
          "uuid": null,
          "workflow_id": 116
        }
      ]
    },
    {
      "created_date": 1683278090102,
      "description": {
        "content": "Delete all the contents of a datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Clear Datatable",
      "export_key": "dt_utils_clear_datatable",
      "id": 119,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090125,
      "name": "dt_utils_clear_datatable",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"success\": true, \"title\": null, \"message\": null, \"hints\": []}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 626, \"timestamp\": \"2022-05-31 13:46:14\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"title\": {}, \"message\": {}, \"hints\": {\"type\": \"array\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "9149563c-8e72-4025-ab71-305cda30dcc7",
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
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
          "name": "Example: Data Table Utils: Clear Datatable",
          "object_type": "incident",
          "programmatic_name": "example_data_table_utils_clear_datatable",
          "tags": [],
          "uuid": null,
          "workflow_id": 109
        }
      ]
    },
    {
      "created_date": 1683278090136,
      "description": {
        "content": "Add CSV data to a named datatable.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Create CSV Datatable",
      "export_key": "dt_utils_create_csv_table",
      "id": 120,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090161,
      "name": "dt_utils_create_csv_table",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"data_source\": \"test_types_utf-8.csv\", \"rows_added\": 12, \"rows_with_errors\": 0}, \"raw\": null, \"inputs\": {\"dt_date_time_format\": \"%m/%d/%y %H:%M\", \"dt_mapping_table\": \"{\\n  \\\"hdr_number\\\": \\\"number\\\",\\n  \\\"hdr_text\\\": \\\"text\\\",\\n  \\\"hdr_boolean\\\": \\\"boolean\\\",\\n  \\\"hdr_datetime\\\": \\\"datetime\\\",\\n  \\\"hdr_select\\\": \\\"select\\\",\\n  \\\"hdr_multiselect\\\": \\\"multi_select\\\"\\n}\", \"incident_id\": 2269, \"attachment_id\": 12, \"dt_datable_name\": \"dt_utils_test_data_table\", \"dt_has_headers\": true}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 5471, \"timestamp\": \"2022-05-31 13:30:04\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"data_source\": {\"type\": \"string\"}, \"rows_added\": {\"type\": \"integer\"}, \"rows_with_errors\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_date_time_format\": {\"type\": \"string\"}, \"dt_mapping_table\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"attachment_id\": {\"type\": \"integer\"}, \"dt_datable_name\": {\"type\": \"string\"}, \"dt_has_headers\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "6edc80c4-e5ae-4c33-b1f1-f0c101918d7a",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Create CSV Datatable",
          "object_type": "attachment",
          "programmatic_name": "example_create_csv_datatable",
          "tags": [],
          "uuid": null,
          "workflow_id": 113
        }
      ]
    },
    {
      "created_date": 1683278090172,
      "description": {
        "content": "Function that deletes a row from a Data Table given the internal row ID.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Delete Row",
      "export_key": "dt_utils_delete_row",
      "id": 121,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090196,
      "name": "dt_utils_delete_row",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"success\": true, \"title\": null, \"message\": null, \"hints\": []}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_row_id\": 642}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 543, \"timestamp\": \"2022-05-31 13:44:54\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"success\": {\"type\": \"boolean\"}, \"title\": {}, \"message\": {}, \"hints\": {\"type\": \"array\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_row_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "50cf405e-aac1-43e7-961e-3894d38688ad",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Row",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_delete_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 117
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Row from Datatable",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "example_data_table_utils_delete_row_from_datatable",
          "tags": [],
          "uuid": null,
          "workflow_id": 115
        }
      ]
    },
    {
      "created_date": 1683278090207,
      "description": {
        "content": "Function that deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Delete Rows",
      "export_key": "dt_utils_delete_rows",
      "id": 122,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090231,
      "name": "dt_utils_delete_rows",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows_ids\": [643]}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_rows_ids\": \"[643]\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 759, \"timestamp\": \"2022-05-31 13:45:13\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows_ids\": {\"type\": \"array\", \"items\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_rows_ids\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "ef4ef5c0-5de2-4fbc-90c9-f7568451da95",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Rows",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_delete_rows",
          "tags": [],
          "uuid": null,
          "workflow_id": 105
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Rows from Datatable",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "example_data_table_utils_delete_rows_from_datatable",
          "tags": [],
          "uuid": null,
          "workflow_id": 108
        }
      ]
    },
    {
      "created_date": 1683278090241,
      "description": {
        "content": "Return all of the rows from a data table in SOAR.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get All Data Table Rows",
      "export_key": "dt_utils_get_all_data_table_rows",
      "id": 123,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090265,
      "name": "dt_utils_get_all_data_table_rows",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows\": [{\"id\": 641, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 641, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 641, \"value\": 1654018496000}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 641, \"value\": \"dgzsfhcjv\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 641, \"value\": [\"e\", \"g\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 641, \"value\": 4598}, \"select\": {\"id\": \"select\", \"row_id\": 641, \"value\": \"3\"}, \"text\": {\"id\": \"text\", \"row_id\": 641, \"value\": \"Update from datatable\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}, {\"id\": 644, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 644, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 644, \"value\": 1654019149216}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 644, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 644, \"value\": [\"b\", \"a\"]}, \"number\": {\"id\": \"number\", \"row_id\": 644, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 644, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 644, \"value\": \"example add row\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 1}]}, \"raw\": null, \"inputs\": {\"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"incident_id\": 2269}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 173, \"timestamp\": \"2022-05-31 13:45:59\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "8a56f5fb-1623-4039-bd80-ed5a5a1bf05b",
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
          "content": "f7f51c3f-1601-44df-bb83-f7ec9583da96",
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
          "name": "Example: Data Table Utils: Get All Data Table Rows",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "example_data_table_utils_get_all_data_table_rows",
          "tags": [],
          "uuid": null,
          "workflow_id": 114
        }
      ]
    },
    {
      "created_date": 1683278090275,
      "description": {
        "content": "Function that searches for a row using a internal row ID or a \u0027search_column and search_value\u0027 pair and returns the cells of the row that is found, if such a row exists.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get Row",
      "export_key": "dt_utils_get_row",
      "id": 124,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090299,
      "name": "dt_utils_get_row",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"id\": 642, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 642, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 642, \"value\": 1654018816842}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 642, \"value\": \"fgshdsgfjn\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 642, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 642, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 642, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 642, \"value\": \"example add row\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 1}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_search_value\": \"fgshdsgfjn\", \"dt_utils_search_column\": \"dt_col_name\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 329, \"timestamp\": \"2022-05-31 13:44:52\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_search_value\": {\"type\": \"string\"}, \"dt_utils_search_column\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "77e98bdb-2843-4cd6-8294-5a9dbef6a08e",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Row",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_delete_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 117
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Get Current Row",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "example_data_table_utils_get_current_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 106
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Get Row",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_get_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 118
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Update Row",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_update_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 111
        }
      ]
    },
    {
      "created_date": 1683278090310,
      "description": {
        "content": "Function that returns the full unsorted list of JSON objects which contain all information regarding each row found, if no searching/sorting criteria were provided.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Get Rows",
      "export_key": "dt_utils_get_rows",
      "id": 125,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090335,
      "name": "dt_utils_get_rows",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"rows\": [{\"id\": 643, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 643, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 643, \"value\": 1654019072126}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 643, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 643, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 643, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 643, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 643, \"value\": \"Updated from Artifact\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}]}, \"raw\": null, \"inputs\": {\"dt_utils_sort_direction\": \"ASC\", \"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_search_value\": \"fGzfdhgxj\", \"dt_utils_sort_by\": null, \"dt_utils_search_column\": \"dt_col_name\", \"dt_utils_max_rows\": 0}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 192, \"timestamp\": \"2022-05-31 13:45:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"rows\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"dt_utils_sort_direction\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_search_value\": {\"type\": \"string\"}, \"dt_utils_sort_by\": {}, \"dt_utils_search_column\": {\"type\": \"string\"}, \"dt_utils_max_rows\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "9f9d8570-c33f-4f30-ab32-9448c3ff8d67",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Delete Rows",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_delete_rows",
          "tags": [],
          "uuid": null,
          "workflow_id": 105
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Get Rows",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_get_rows",
          "tags": [],
          "uuid": null,
          "workflow_id": 110
        }
      ]
    },
    {
      "created_date": 1683278090347,
      "description": {
        "content": "Function that takes a JSON String of \u0027search_column and search_value\u0027 pairs to update a Data Table row.",
        "format": "text"
      },
      "destination_handle": "fn_datatable_utils",
      "display_name": "Data Table Utils: Update Row",
      "export_key": "dt_utils_update_row",
      "id": 126,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1683278090371,
      "name": "dt_utils_update_row",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"row\": {\"id\": 643, \"cells\": {\"boolean\": {\"id\": \"boolean\", \"row_id\": 643, \"value\": true}, \"datetime\": {\"id\": \"datetime\", \"row_id\": 643, \"value\": 1654019072126}, \"dt_col_name\": {\"id\": \"dt_col_name\", \"row_id\": 643, \"value\": \"fGzfdhgxj\"}, \"multi_select\": {\"id\": \"multi_select\", \"row_id\": 643, \"value\": [\"a\", \"b\"]}, \"number\": {\"id\": \"number\", \"row_id\": 643, \"value\": 1}, \"select\": {\"id\": \"select\", \"row_id\": 643, \"value\": \"1\"}, \"text\": {\"id\": \"text\", \"row_id\": 643, \"value\": \"Updated from Artifact\"}}, \"actions\": [{\"id\": 43, \"name\": \"Get Current Row\", \"enabled\": true}, {\"id\": 56, \"name\": \"Get All Rows\", \"enabled\": true}, {\"id\": 38, \"name\": \"Delete Current Row\", \"enabled\": true}, {\"id\": 41, \"name\": \"Delete Rows by Name\", \"enabled\": true}, {\"id\": 46, \"name\": \"Update Current Row\", \"enabled\": true}, {\"id\": 58, \"name\": \"Add Row\", \"enabled\": true}], \"type_id\": 1002, \"table_name\": \"Example CSV Datatable\", \"inc_id\": 2269, \"inc_name\": \"f\", \"inc_owner\": \"admin@example.com\", \"version\": 2}}, \"raw\": null, \"inputs\": {\"incident_id\": 2269, \"dt_utils_datatable_api_name\": \"dt_utils_test_data_table\", \"dt_utils_cells_to_update\": \"{ \\\"datetime\\\":1654019072126,\\\"text\\\":\\\"Updated from Artifact\\\" }\", \"dt_utils_row_id\": 643}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-datatable-utils\", \"package_version\": \"2.0.0\", \"host\": \"local\", \"execution_time_ms\": 598, \"timestamp\": \"2022-05-31 13:44:33\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"row\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"cells\": {\"type\": \"object\", \"properties\": {\"boolean\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"boolean\"}}}, \"datetime\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"dt_col_name\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"multi_select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"number\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"integer\"}}}, \"select\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}, \"text\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"row_id\": {\"type\": \"integer\"}, \"value\": {\"type\": \"string\"}}}}}, \"actions\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"enabled\": {\"type\": \"boolean\"}}}}, \"type_id\": {\"type\": \"integer\"}, \"table_name\": {\"type\": \"string\"}, \"inc_id\": {\"type\": \"integer\"}, \"inc_name\": {\"type\": \"string\"}, \"inc_owner\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"dt_utils_datatable_api_name\": {\"type\": \"string\"}, \"dt_utils_cells_to_update\": {\"type\": \"string\"}, \"dt_utils_row_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "77b8451e-3137-4362-840a-ac724b674b73",
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
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example Data Utils: Update Row",
          "object_type": "dt_utils_test_data_table",
          "programmatic_name": "update_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 112
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Data Table Utils: Update Row",
          "object_type": "artifact",
          "programmatic_name": "example_data_table_utils_update_row",
          "tags": [],
          "uuid": null,
          "workflow_id": 111
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 20,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1684931494146,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1684931494146,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "e9d4a3be-ed6b-4c4d-ba63-506f9831d212"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_datatable_utils",
      "name": "fn_datatable_utils",
      "programmatic_name": "fn_datatable_utils",
      "tags": [],
      "users": [],
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
        "content_version": 4,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_47daec86_3c48_43a0_b526_39461bb417fe\" isExecutable=\"true\" name=\"playbook_47daec86_3c48_43a0_b526_39461bb417fe\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0jn08p1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, str):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# Refer to the existing row (value: 0)\\ninputs.dt_utils_row_id = 0\\n\\n# The column api names and the value to update the cell to\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"name\\\": \\\"Updated Example\\\", \\\"text\\\": \\\"Update from datatable\\\", \\\"number\\\": 4598, \\\"multi_select\\\": [\\\"b\\\", \\\"e\\\", \\\"g\\\"], \\\"boolean\\\": True})\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0jn08p1\u003c/incoming\u003e\u003coutgoing\u003eFlow_17mhr36\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_17mhr36\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0jn08p1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_17mhr36\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_47daec86_3c48_43a0_b526_39461bb417fe\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17mhr36\" id=\"Flow_17mhr36_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jn08p1\" id=\"Flow_0jn08p1_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683619091736,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_47daec86_3c48_43a0_b526_39461bb417fe",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Update Row Function. It illustrates updating the current row with static values.",
        "format": "text"
      },
      "display_name": "Example Data Utils: Update Row (PB)",
      "export_key": "update_current_row_pb",
      "field_type_handle": "playbook_47daec86_3c48_43a0_b526_39461bb417fe",
      "fields_type": {
        "actions": [],
        "display_name": "Update Current Row (PB)",
        "export_key": "playbook_47daec86_3c48_43a0_b526_39461bb417fe",
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
        "type_name": "playbook_47daec86_3c48_43a0_b526_39461bb417fe",
        "uuid": "c62a8581-e69e-4dd9-ac13-5e2cbaf0bf90"
      },
      "has_logical_errors": false,
      "id": 41,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928289404,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "update_current_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_47daec86-3c48-43a0-b526-39461bb417fe",
        "id": 54,
        "name": "playbook_47daec86_3c48_43a0_b526_39461bb417fe",
        "type": "playbook",
        "uuid": "1debb24d-5d4e-4814-bd7f-e6e9e7f3650a"
      },
      "tags": [],
      "type": "default",
      "uuid": "47daec86-3c48-43a0-b526-39461bb417fe",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0\" isExecutable=\"true\" name=\"playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0zgcy0d\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Create CSV Datatable\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6edc80c4-e5ae-4c33-b1f1-f0c101918d7a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n# The api name of the Data Table to update\\ninputs.dt_datable_name = \\\"dt_utils_test_data_table\\\"\\n# uncomment attachment_id when reading csv data from an attachmennt\\ninputs.attachment_id = attachment.id\\n\\n# A boolean to determine if CSV headers are present\\ninputs.dt_has_headers = True\\n\\n## The mapping format should be \\\"csv_header\\\":\\\"dt_column_name\\\"\\nmapping = \u0027\u0027\u0027{\\n  \\\"hdr_number\\\": \\\"number\\\",\\n  \\\"hdr_text\\\": \\\"text\\\",\\n  \\\"hdr_boolean\\\": \\\"boolean\\\",\\n  \\\"hdr_datetime\\\": \\\"datetime\\\",\\n  \\\"hdr_select\\\": \\\"select\\\",\\n  \\\"hdr_multiselect\\\": \\\"multi_select\\\"\\n}\u0027\u0027\u0027\\n# mappings of csv data without headers will be a list of data_table column names. Use null to bypass a csv data column\\nmapping_no_headers = \u0027\u0027\u0027[\\\"number\\\",\\\"text\\\",\\\"boolean\\\",\\\"datetime\\\",\\\"select\\\",\\\"multi_select\\\",\\\"x\\\",\\\"y\\\",\\\"z\\\"]\u0027\u0027\u0027\\ninputs.dt_mapping_table = mapping\\n# year - %Y, month - %m, day - %d, hour - %H, minutes - %M, seconds - %S, milliseconds - %f, timezone offset - %z\u0027\\ninputs.dt_date_time_format = \\\"%m/%d/%y %H:%M\\\"\\n# optional start row csv data. The first data row = 1\\n##inputs.dt_start_row = 0\\n# optional max number of csv rows to add relative to dt_start_row\\n##inputs.dt_max_rows = 5\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_csv\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0zgcy0d\u003c/incoming\u003e\u003coutgoing\u003eFlow_1aewa6j\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0zgcy0d\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1y568cn\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Create CSV Datatable Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"fc920c39-f6b5-4419-8ec6-572954e4e631\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1aewa6j\u003c/incoming\u003e\u003coutgoing\u003eFlow_1y568cn\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1aewa6j\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_1y568cn\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1y568cn\" id=\"Flow_1y568cn_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"372\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"398\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"398\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"424\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1aewa6j\" id=\"Flow_1aewa6j_di\"\u003e\u003comgdi:waypoint x=\"800\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"265\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"265\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"288\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zgcy0d\" id=\"Flow_0zgcy0d_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"138\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"138\"/\u003e\u003comgdi:waypoint x=\"800\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.125\" x=\"617\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"664\" y=\"424\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"702\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"288\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683610774636,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0",
      "description": {
        "content": "Take CSV data and add the results to a named datatable. Results of the function are written to an incident note.",
        "format": "text"
      },
      "display_name": "Example: Create CSV Datatable (PB)",
      "export_key": "example_create_csv_datatable_pb",
      "field_type_handle": "playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Create CSV Datatable (PB)",
        "export_key": "playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0",
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
        "type_name": "playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0",
        "uuid": "05844ca0-dca3-4d77-bdde-9f1ef859d866"
      },
      "has_logical_errors": false,
      "id": 35,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684428725857,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683611604658,
          "description": "",
          "enabled": false,
          "export_key": "Create CSV Datatable Post-Process Script",
          "id": 56,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684409279997,
          "name": "Create CSV Datatable Post-Process Script",
          "object_type": "attachment",
          "playbook_handle": "example_create_csv_datatable_pb",
          "programmatic_name": "example_create_csv_datatable_pb_create_csv_datatable_post_process_script",
          "script_text": "results = playbook.functions.results.create_csv\n\nif results[\u0027success\u0027]:\n  note_text = u\"\"\"Results from Data Table Utils: Create CSV Datatable\\nData Source: {}\\nRows added: {}\\nRows not added: {}\"\"\".format(results.content[\"data_source\"], results.content[\"rows_added\"], results.content[\"rows_with_errors\"])\n  incident.addNote(note_text)\nelse:\n  incident.addNote(u\"Error: Failed to add rows\")",
          "tags": [],
          "uuid": "fc920c39-f6b5-4419-8ec6-572954e4e631"
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
        "display_name": "Playbook_df5554f9-752d-4b47-ba36-d2c0f8195cf0",
        "id": 48,
        "name": "playbook_df5554f9_752d_4b47_ba36_d2c0f8195cf0",
        "type": "playbook",
        "uuid": "5bd41439-2f6e-4f76-a3fe-68a636095190"
      },
      "tags": [],
      "type": "default",
      "uuid": "df5554f9-752d-4b47-ba36-d2c0f8195cf0",
      "version": 14
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_689d27d3_64dc_4ff6_b825_900971fe867e\" isExecutable=\"true\" name=\"playbook_689d27d3_64dc_4ff6_b825_900971fe867e\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_10v23qm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, str):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"dt_col_name\\\": playbook.inputs.dt_name_field, \\\"number\\\": playbook.inputs.dt_number_field, \\\"text\\\": playbook.inputs.dt_text_field, \\\"datetime\\\": playbook.inputs.dt_datetime_field, \\\"boolean\\\": playbook.inputs.dt_boolean_field, \\\"select\\\": playbook.inputs.dt_select_field, \\\"multi_select\\\": playbook.inputs.dt_multi_select_field})\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_10v23qm\u003c/incoming\u003e\u003coutgoing\u003eFlow_1rvl52g\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_10v23qm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1rvl52g\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1rvl52g\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_689d27d3_64dc_4ff6_b825_900971fe867e\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1rvl52g\" id=\"Flow_1rvl52g_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_10v23qm\" id=\"Flow_10v23qm_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"143\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"143\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"644\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683626830157,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
      "description": {
        "content": "Add a row to the given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Add Row (PB)",
      "export_key": "add_row_pb",
      "field_type_handle": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
      "fields_type": {
        "actions": [],
        "display_name": "Add Row (PB)",
        "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
        "fields": {
          "dt_boolean_field": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_boolean_field",
            "hide_notification": false,
            "id": 2130,
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
            "type_id": 1069,
            "uuid": "1e9b80c8-37f3-439a-8329-21fe622f5081",
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_datetime_field",
            "hide_notification": false,
            "id": 2131,
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
            "type_id": 1069,
            "uuid": "26e9a592-904e-43c4-99b6-84042d9d492b",
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_multi_select_field",
            "hide_notification": false,
            "id": 2132,
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
            "type_id": 1069,
            "uuid": "b86a01b2-6f7e-438c-8272-722cac8cc987",
            "values": [
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "a",
                "properties": null,
                "uuid": "395aeb56-e03a-4154-b0fc-9895ff8a65cd",
                "value": 934
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "b",
                "properties": null,
                "uuid": "20890991-4723-4a64-b893-aee34233aa15",
                "value": 935
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "c",
                "properties": null,
                "uuid": "c17dc3b8-8215-4084-8b8c-2c8f24c3ee58",
                "value": 936
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "d",
                "properties": null,
                "uuid": "362ff226-2c01-4c9e-b72c-d7a523e3dfea",
                "value": 937
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "e",
                "properties": null,
                "uuid": "e2941098-013c-42ad-bc0a-e68c98e4148a",
                "value": 938
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "f",
                "properties": null,
                "uuid": "4eab3502-4a3b-459a-a32b-fdafdb7d0f57",
                "value": 939
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "g",
                "properties": null,
                "uuid": "4e817d4d-be7a-4cbe-9003-11f28c63ce92",
                "value": 940
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "h",
                "properties": null,
                "uuid": "9ddc7ab0-3c28-4151-abda-13fba95d9d19",
                "value": 941
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "i",
                "properties": null,
                "uuid": "ba1be443-2fbb-4c3b-a55f-09419d82d660",
                "value": 942
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "j",
                "properties": null,
                "uuid": "1b876722-3b7b-4860-bad1-8e641db5af27",
                "value": 943
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "k",
                "properties": null,
                "uuid": "02905beb-61bc-4f11-b8d3-90f21dda657d",
                "value": 944
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "l",
                "properties": null,
                "uuid": "b2279c79-967a-4cd7-b916-debd3bb094cb",
                "value": 945
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "m",
                "properties": null,
                "uuid": "b7b6c351-d968-4dfa-ab20-82a8ad628ef3",
                "value": 946
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "n",
                "properties": null,
                "uuid": "d6cf3408-2422-4810-a5fb-c394a14056f3",
                "value": 947
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "o",
                "properties": null,
                "uuid": "c3c32753-d498-48bf-8e94-a83ab7600643",
                "value": 948
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "p",
                "properties": null,
                "uuid": "e95abe2c-f45c-45cb-a732-7dd3aa63210d",
                "value": 949
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_name_field",
            "hide_notification": false,
            "id": 2133,
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
            "type_id": 1069,
            "uuid": "6a9ffbb3-cbef-4eb5-a5e6-e1f3b4cad89f",
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_number_field",
            "hide_notification": false,
            "id": 2134,
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
            "type_id": 1069,
            "uuid": "73c3188d-4f51-467c-8044-dce6fd060a55",
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_select_field",
            "hide_notification": false,
            "id": 2135,
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
            "type_id": 1069,
            "uuid": "6b01a1ea-4758-4e7c-9115-4030ce8bef72",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "1",
                "properties": null,
                "uuid": "70c2a872-bc72-4376-a1b8-044f7bf8422f",
                "value": 950
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "2",
                "properties": null,
                "uuid": "0ee16a83-0095-4e38-b722-c92bb3263c6d",
                "value": 951
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "3",
                "properties": null,
                "uuid": "0df53146-0229-4cb5-a6ea-9bc8d8e78b95",
                "value": 952
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "4",
                "properties": null,
                "uuid": "083b534b-8e8b-4237-9b2a-09fef376aadc",
                "value": 953
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "5",
                "properties": null,
                "uuid": "75cd8908-c1d7-4db8-b943-33a6dc454143",
                "value": 954
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "6",
                "properties": null,
                "uuid": "465c5a25-08ad-4fdb-b6ad-4941087ca13a",
                "value": 955
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "7",
                "properties": null,
                "uuid": "0d6a7eeb-9284-4e60-8e9e-2c3254385d6d",
                "value": 956
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "8",
                "properties": null,
                "uuid": "ee6a4c09-ec25-4f69-b26e-84ab35c3ca2f",
                "value": 957
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "9",
                "properties": null,
                "uuid": "f4daa65c-6bbd-46c5-8e40-a8173d03deca",
                "value": 958
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
            "export_key": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e/dt_text_field",
            "hide_notification": false,
            "id": 2136,
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
            "type_id": 1069,
            "uuid": "d2677d34-1ca9-471b-a652-2c5cf50af68c",
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
        "type_name": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
        "uuid": "b8650dbf-308b-440f-96ee-f75bd11a3bd1"
      },
      "has_logical_errors": false,
      "id": 45,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684927872090,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "6a9ffbb3-cbef-4eb5-a5e6-e1f3b4cad89f",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "73c3188d-4f51-467c-8044-dce6fd060a55",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d2677d34-1ca9-471b-a652-2c5cf50af68c",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "26e9a592-904e-43c4-99b6-84042d9d492b",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "1e9b80c8-37f3-439a-8329-21fe622f5081",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6b01a1ea-4758-4e7c-9115-4030ce8bef72",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b86a01b2-6f7e-438c-8272-722cac8cc987",
            "element": "field_uuid",
            "field_type": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "add_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_689d27d3-64dc-4ff6-b825-900971fe867e",
        "id": 58,
        "name": "playbook_689d27d3_64dc_4ff6_b825_900971fe867e",
        "type": "playbook",
        "uuid": "f0be8136-fdc4-4c17-8a1e-fc1d334a9c4e"
      },
      "tags": [],
      "type": "default",
      "uuid": "689d27d3-64dc-4ff6-b825-900971fe867e",
      "version": 12
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 67,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb\" isExecutable=\"true\" name=\"playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1927v87\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\nfrom json import dumps\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ntmp = {\\\"dt_col_name\\\": str(artifact.value), \\\"number\\\": 1, \\\"text\\\": \\\"example add row\\\", \\\"datetime\\\": int(datetime.now().timestamp()*1000), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = f\u0027{dumps(tmp)}\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1927v87\u003c/incoming\u003e\u003coutgoing\u003eFlow_11gtz9d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1927v87\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_11gtz9d\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_11gtz9d\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_11gtz9d\" id=\"Flow_11gtz9d_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"283\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"283\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"304\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1927v87\" id=\"Flow_1927v87_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"634\" y=\"304\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683536854436,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb",
      "description": {
        "content": "Add a row to the given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Add Row to Datatable (PB)",
      "export_key": "add_row_to_datatable_pb",
      "field_type_handle": "playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Data Table Utils: Add Row to Datatable (PB)",
        "export_key": "playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb",
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
        "type_name": "playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb",
        "uuid": "af7e0aed-98c1-4dbb-9932-1f3035d6189c"
      },
      "has_logical_errors": false,
      "id": 28,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684927899953,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "add_row_to_datatable_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_5cf449a2-aa52-464a-92f3-d0bb7daab3bb",
        "id": 41,
        "name": "playbook_5cf449a2_aa52_464a_92f3_d0bb7daab3bb",
        "type": "playbook",
        "uuid": "a2760633-85c1-470b-8afe-dc739bfe3d83"
      },
      "tags": [],
      "type": "default",
      "uuid": "5cf449a2-aa52-464a-92f3-d0bb7daab3bb",
      "version": 75
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_1a49f130_0114_4941_b4d6_79307b4af8e9\" isExecutable=\"true\" name=\"playbook_1a49f130_0114_4941_b4d6_79307b4af8e9\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1r319ls\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Clear Datatable\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9149563c-8e72-4025-ab71-305cda30dcc7\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\nif playbook.inputs.datatable_api_name:\\n  inputs.dt_utils_datatable_api_name = playbook.inputs.datatable_api_name\\nelse:\\n  # Defaults to example data table\\n  inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"clear_datatable\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1r319ls\u003c/incoming\u003e\u003coutgoing\u003eFlow_069f89x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1r319ls\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1h7yrk3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Clear Datatable Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8ba5543a-7701-4729-b48f-12cae99cef84\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_069f89x\u003c/incoming\u003e\u003coutgoing\u003eFlow_1h7yrk3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_069f89x\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_1h7yrk3\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1a49f130_0114_4941_b4d6_79307b4af8e9\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1h7yrk3\" id=\"Flow_1h7yrk3_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"433\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"433\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"464\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_069f89x\" id=\"Flow_069f89x_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"262\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1r319ls\" id=\"Flow_1r319ls_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.188\" x=\"628\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"624\" y=\"464\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683540479638,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
      "description": {
        "content": "Clear the content of a given datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Clear Datatable (PB)",
      "export_key": "clear_datatable_pb",
      "field_type_handle": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
      "fields_type": {
        "actions": [],
        "display_name": "Clear Datatable (PB)",
        "export_key": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
        "fields": {
          "datatable_api_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9/datatable_api_name",
            "hide_notification": false,
            "id": 2123,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "datatable_api_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Datatable API Name",
            "tooltip": "API name of the datatable to clear",
            "type_id": 1053,
            "uuid": "380d29fb-57a2-4d19-a188-5dc3a7814493",
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
        "type_name": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
        "uuid": "6de6be6d-e459-42d6-9bec-4f9b26bf377e"
      },
      "has_logical_errors": false,
      "id": 29,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684927932498,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683540918538,
          "description": "",
          "enabled": false,
          "export_key": "Clear Datatable Post-Process Script",
          "id": 53,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1683704400050,
          "name": "Clear Datatable Post-Process Script",
          "object_type": "incident",
          "playbook_handle": "clear_datatable_pb",
          "programmatic_name": "clear_datatable_pb_example_data_table_utils_clear_datatable_post_process_script",
          "script_text": "results = playbook.functions.results.clear_datatable\nif results[\"success\"]:\n  incident.addNote(\"Data table: {} content has been removed.\".format(results[\"inputs\"][\"dt_utils_datatable_api_name\"]))",
          "tags": [],
          "uuid": "8ba5543a-7701-4729-b48f-12cae99cef84"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "380d29fb-57a2-4d19-a188-5dc3a7814493",
            "element": "field_uuid",
            "field_type": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "clear_datatable_pb",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_1a49f130-0114-4941-b4d6-79307b4af8e9",
        "id": 42,
        "name": "playbook_1a49f130_0114_4941_b4d6_79307b4af8e9",
        "type": "playbook",
        "uuid": "1c442a04-d485-4447-8c70-7b337756df8e"
      },
      "tags": [],
      "type": "default",
      "uuid": "1a49f130-0114-4941-b4d6-79307b4af8e9",
      "version": 12
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 58,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_d66308b8_c378_46aa_970f_806dee082350\" isExecutable=\"true\" name=\"playbook_d66308b8_c378_46aa_970f_806dee082350\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1jr1slg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"row_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1jr1slg\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ahm5iw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The ID of the row to delete [again, taken from previous Get Row Function]\\ninputs.dt_utils_row_id = playbook.functions.results.row_to_delete.content.row[\\\"id\\\"]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"delete_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1orgyh4\u003c/incoming\u003e\u003coutgoing\u003eFlow_00ozszx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1f8upf4\u003c/incoming\u003e\u003cincoming\u003eFlow_0rv4g7r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1jr1slg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_00ozszx\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_6\"/\u003e\u003cinclusiveGateway default=\"Flow_0rv4g7r\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0ahm5iw\u003c/incoming\u003e\u003coutgoing\u003eFlow_1orgyh4\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0rv4g7r\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0ahm5iw\" sourceRef=\"ServiceTask_1\" targetRef=\"ConditionPoint_2\"/\u003e\u003cscriptTask id=\"ScriptTask_6\" name=\"Delete Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"64fea358-e963-4b0f-99e5-b9fb92d5cf77\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_00ozszx\u003c/incoming\u003e\u003coutgoing\u003eFlow_1f8upf4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1f8upf4\" sourceRef=\"ScriptTask_6\" targetRef=\"EndPoint_4\"/\u003e\u003csequenceFlow id=\"Flow_1orgyh4\" name=\"success\" sourceRef=\"ConditionPoint_2\" targetRef=\"ServiceTask_3\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\n\\nresults = playbook.functions.results.row_to_delete\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0rv4g7r\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_d66308b8_c378_46aa_970f_806dee082350\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0rv4g7r\" id=\"Flow_0rv4g7r_di\"\u003e\u003comgdi:waypoint x=\"720\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"720\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"334\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"668\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1orgyh4\" id=\"Flow_1orgyh4_di\"\u003e\u003comgdi:waypoint x=\"627\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"208\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"513\" y=\"159\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1f8upf4\" id=\"Flow_1f8upf4_di\"\u003e\u003comgdi:waypoint x=\"458\" y=\"370\"/\u003e\u003comgdi:waypoint x=\"506\" y=\"370\"/\u003e\u003comgdi:waypoint x=\"506\" y=\"360\"/\u003e\u003comgdi:waypoint x=\"554\" y=\"360\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ahm5iw\" id=\"Flow_0ahm5iw_di\"\u003e\u003comgdi:waypoint x=\"627\" y=\"-8\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_00ozszx\" id=\"Flow_00ozszx_di\"\u003e\u003comgdi:waypoint x=\"440\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"440\" y=\"310\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"310\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jr1slg\" id=\"Flow_1jr1slg_di\"\u003e\u003comgdi:waypoint x=\"639\" y=\"-144\"/\u003e\u003comgdi:waypoint x=\"639\" y=\"-118\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"-118\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"-92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"548\" y=\"-196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"529\" y=\"-92\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"342\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"554\" y=\"334\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"500\" y=\"94\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_6\" id=\"ScriptTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"262\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683547220696,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_d66308b8_c378_46aa_970f_806dee082350",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Row (PB)",
      "export_key": "delete_data_table_row_pb",
      "field_type_handle": "playbook_d66308b8_c378_46aa_970f_806dee082350",
      "fields_type": {
        "actions": [],
        "display_name": "Delete Data Table Row (PB)",
        "export_key": "playbook_d66308b8_c378_46aa_970f_806dee082350",
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
        "type_name": "playbook_d66308b8_c378_46aa_970f_806dee082350",
        "uuid": "542593ed-8785-43ff-9552-876c871f83fb"
      },
      "has_logical_errors": false,
      "id": 32,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928062723,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1684141360719,
          "description": "",
          "enabled": false,
          "export_key": "Delete Row Post-Process Script",
          "id": 68,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684146139131,
          "name": "Delete Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "delete_data_table_row_pb",
          "programmatic_name": "delete_data_table_row_pb_delete_row_post_process_script",
          "script_text": "results = playbook.functions.results.delete_row\nif results.success:\n  note = u\"Row id: {} removed from datatable: {} for artifact: {}\".format(results.inputs[\u0027dt_utils_row_id\u0027], results.inputs[\u0027dt_utils_datatable_api_name\u0027], artifact.value)\nelse:\n  note = u\"Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\nincident.addNote(note)",
          "tags": [],
          "uuid": "64fea358-e963-4b0f-99e5-b9fb92d5cf77"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "delete_data_table_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_d66308b8-c378-46aa-970f-806dee082350",
        "id": 45,
        "name": "playbook_d66308b8_c378_46aa_970f_806dee082350",
        "type": "playbook",
        "uuid": "f1a0db23-4780-468f-a910-f5ca0eb50227"
      },
      "tags": [],
      "type": "default",
      "uuid": "d66308b8-c378-46aa-970f-806dee082350",
      "version": 67
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 5,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_64bd2415_5336_4676_b92c_0717709cd59b\" isExecutable=\"true\" name=\"playbook_64bd2415_5336_4676_b92c_0717709cd59b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1c1hbw6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1c1hbw6\u003c/incoming\u003e\u003coutgoing\u003eFlow_04u40qz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1c1hbw6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_04u40qz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_04u40qz\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_64bd2415_5336_4676_b92c_0717709cd59b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04u40qz\" id=\"Flow_04u40qz_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"364\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1c1hbw6\" id=\"Flow_1c1hbw6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"364\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683541829482,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_64bd2415_5336_4676_b92c_0717709cd59b",
      "description": {
        "content": "Delete a row from a datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Row from Datatable (PB)",
      "export_key": "delete_current_row_pb",
      "field_type_handle": "playbook_64bd2415_5336_4676_b92c_0717709cd59b",
      "fields_type": {
        "actions": [],
        "display_name": "Delete Current Row (PB)",
        "export_key": "playbook_64bd2415_5336_4676_b92c_0717709cd59b",
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
        "type_name": "playbook_64bd2415_5336_4676_b92c_0717709cd59b",
        "uuid": "a2b8877b-61c7-48ac-b9d4-e38bbc95cca2"
      },
      "has_logical_errors": false,
      "id": 31,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684927968470,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "delete_current_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_64bd2415-5336-4676-b92c-0717709cd59b",
        "id": 44,
        "name": "playbook_64bd2415_5336_4676_b92c_0717709cd59b",
        "type": "playbook",
        "uuid": "3fae7fa5-1254-40b4-9c1f-d1c5c54af2e0"
      },
      "tags": [],
      "type": "default",
      "uuid": "64bd2415-5336-4676-b92c-0717709cd59b",
      "version": 13
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 11,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa\" isExecutable=\"true\" name=\"playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_173fz9m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1f8upf4\u003c/incoming\u003e\u003cincoming\u003eFlow_0rv4g7r\u003c/incoming\u003e\u003c/endEvent\u003e\u003cinclusiveGateway default=\"Flow_0rv4g7r\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1n3vhv3\u003c/incoming\u003e\u003coutgoing\u003eFlow_0rv4g7r\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0nhkrcj\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003cscriptTask id=\"ScriptTask_6\" name=\"Delete Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f7f7f5aa-3e5e-4226-93c2-20a9fe98e700\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1rtnknt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1f8upf4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1f8upf4\" sourceRef=\"ScriptTask_6\" targetRef=\"EndPoint_4\"/\u003e\u003cserviceTask id=\"ServiceTask_7\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"f7f51c3f-1601-44df-bb83-f7ec9583da96\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"11e8aca8-05bd-467b-8071-9dd160d9e14a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}},\"c42f5cac-9e46-4ee3-bda4-6c9dbe17c516\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"2c359b58-e41e-4dd1-ac65-138e85a27363\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fca27f70-867b-4899-b7c5-f8bdf1bbec13\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"rows_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_173fz9m\u003c/incoming\u003e\u003coutgoing\u003eFlow_04bpvns\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_173fz9m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_7\"/\u003e\u003cscriptTask id=\"ScriptTask_8\" name=\"Get Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"34eebd0c-ab6b-4a25-b89a-bd56940ee506\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04bpvns\u003c/incoming\u003e\u003coutgoing\u003eFlow_1n3vhv3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_04bpvns\" sourceRef=\"ServiceTask_7\" targetRef=\"ScriptTask_8\"/\u003e\u003csequenceFlow id=\"Flow_1n3vhv3\" sourceRef=\"ScriptTask_8\" targetRef=\"ConditionPoint_2\"/\u003e\u003cserviceTask id=\"ServiceTask_9\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table, search column, search value [here it is taken from previous Get Rows Function inputs]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The internal IDs of the rows that will be deleted [again, taken from previous Get Rows Function]\\nif playbook.functions.results.rows_to_delete and playbook.functions.results.rows_to_delete.content.rows:\\n  rows_ids = []\\n  for row in playbook.functions.results.rows_to_delete.content.rows:\\n    rows_ids.append(row[\\\"id\\\"])\\n  inputs.dt_utils_rows_ids = str(rows_ids)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"delete_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0nhkrcj\u003c/incoming\u003e\u003coutgoing\u003eFlow_1rtnknt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1rtnknt\" sourceRef=\"ServiceTask_9\" targetRef=\"ScriptTask_6\"/\u003e\u003csequenceFlow id=\"Flow_0nhkrcj\" name=\"success\" sourceRef=\"ConditionPoint_2\" targetRef=\"ServiceTask_9\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\nresults = playbook.functions.results.rows_to_delete\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0rv4g7r\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0rv4g7r\" id=\"Flow_0rv4g7r_di\"\u003e\u003comgdi:waypoint x=\"720\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"720\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"344\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"704\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0nhkrcj\" id=\"Flow_0nhkrcj_di\"\u003e\u003comgdi:waypoint x=\"500\" y=\"120\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"120\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"400\" y=\"98\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1rtnknt\" id=\"Flow_1rtnknt_di\"\u003e\u003comgdi:waypoint x=\"360\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"310\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"310\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1n3vhv3\" id=\"Flow_1n3vhv3_di\"\u003e\u003comgdi:waypoint x=\"620\" y=\"72\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"83\"/\u003e\u003comgdi:waypoint x=\"619\" y=\"83\"/\u003e\u003comgdi:waypoint x=\"619\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04bpvns\" id=\"Flow_04bpvns_di\"\u003e\u003comgdi:waypoint x=\"639\" y=\"-48\"/\u003e\u003comgdi:waypoint x=\"639\" y=\"-30\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"-30\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"-12\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_173fz9m\" id=\"Flow_173fz9m_di\"\u003e\u003comgdi:waypoint x=\"639\" y=\"-164\"/\u003e\u003comgdi:waypoint x=\"639\" y=\"-132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1f8upf4\" id=\"Flow_1f8upf4_di\"\u003e\u003comgdi:waypoint x=\"448\" y=\"380\"/\u003e\u003comgdi:waypoint x=\"546\" y=\"380\"/\u003e\u003comgdi:waypoint x=\"546\" y=\"370\"/\u003e\u003comgdi:waypoint x=\"644\" y=\"370\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"548\" y=\"-216\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"644\" y=\"344\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"500\" y=\"94\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_6\" id=\"ScriptTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"252\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_7\" id=\"ServiceTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"541\" y=\"-132\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_8\" id=\"ScriptTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"522\" y=\"-12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_9\" id=\"ServiceTask_9_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"262\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1684147094335,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Rows (PB)",
      "export_key": "delete_data_table_rows_pb",
      "field_type_handle": "playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa",
      "fields_type": {
        "actions": [],
        "display_name": "Delete Data Table Rows (PB)",
        "export_key": "playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa",
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
        "type_name": "playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa",
        "uuid": "31796c7d-f83d-4e85-9e01-dc8c79179d73"
      },
      "has_logical_errors": false,
      "id": 56,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928357494,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1684147094394,
          "description": "",
          "enabled": false,
          "export_key": "Delete Rows Post-Process Script",
          "id": 69,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684147959141,
          "name": "Delete Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "delete_data_table_rows_pb",
          "programmatic_name": "delete_data_table_rows_pb_delete_row_post_process_script",
          "script_text": "results = playbook.functions.results.delete_row\n\nif results.success:\n  note = u\"\u003cb\u003eResult from Example: Data Table Utils: Artifact: {} Delete Rows\u003c/b\u003e\u003cbr\u003e {}\".format(artifact.value, str(results.content[\"rows_ids\"]))\nelse:\n  note = u\"\u003cb\u003eResult from Example: Data Table Utils: Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\n\nincident.addNote(helper.createRichText(note))",
          "tags": [],
          "uuid": "f7f7f5aa-3e5e-4226-93c2-20a9fe98e700"
        },
        {
          "actions": [],
          "created_date": 1684147367318,
          "description": "",
          "enabled": false,
          "export_key": "Get Rows Post-Process Script",
          "id": 70,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684147674593,
          "name": "Get Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "delete_data_table_rows_pb",
          "programmatic_name": "delete_data_table_rows_pb_get_rows_post_process_script",
          "script_text": "results = playbook.functions.results.rows_to_delete\n\nif not results[\u0027success\u0027]:\n  incident.addNote(helper.createRichText(\"\u003cb\u003eResult from Example: Data Table Utils: Delete Rows\u003c/b\u003e\u003cbr\u003eNo rows found.\"))",
          "tags": [],
          "uuid": "34eebd0c-ab6b-4a25-b89a-bd56940ee506"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "delete_data_table_rows_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_1cb7d1e7-ae88-4fc8-af0d-0b5753f430aa",
        "id": 71,
        "name": "playbook_1cb7d1e7_ae88_4fc8_af0d_0b5753f430aa",
        "type": "playbook",
        "uuid": "8b3f0f23-bcda-44ee-ad88-9a1ee9351af7"
      },
      "tags": [],
      "type": "default",
      "uuid": "1cb7d1e7-ae88-4fc8-af0d-0b5753f430aa",
      "version": 18
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1\" isExecutable=\"true\" name=\"playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0zhwtd3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"pre_processing_script\":\"if not row.dt_col_name:\\n  helper.fail(\\\"The data table column \u0027name\u0027 must contain a value\\\")\\n\\ninputs.incident_id = incident.id\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\ninputs.dt_utils_search_value = row.dt_col_name\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0zhwtd3\u003c/incoming\u003e\u003coutgoing\u003eFlow_18mudwe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_18mudwe\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0zhwtd3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_18mudwe\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18mudwe\" id=\"Flow_18mudwe_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"344\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0zhwtd3\" id=\"Flow_0zhwtd3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"344\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683609316236,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1",
      "description": {
        "content": "Deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Delete Rows from Datatable (PB)",
      "export_key": "delete_rows_by_name_pb",
      "field_type_handle": "playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1",
      "fields_type": {
        "actions": [],
        "display_name": "Delete Rows by Name (PB)",
        "export_key": "playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1",
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
        "type_name": "playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1",
        "uuid": "d4dbc41a-63ac-4e7f-97f2-da569e84ae69"
      },
      "has_logical_errors": false,
      "id": 34,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928098506,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "delete_rows_by_name_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a74ec0e9-8a83-42a7-a057-9ee1eeb140c1",
        "id": 47,
        "name": "playbook_a74ec0e9_8a83_42a7_a057_9ee1eeb140c1",
        "type": "playbook",
        "uuid": "4b1a92de-a9f7-407a-a68d-931b7523c979"
      },
      "tags": [],
      "type": "default",
      "uuid": "a74ec0e9-8a83-42a7-a057-9ee1eeb140c1",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 35,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_8894bebc_b55f_4859_9218_222680256e24\" isExecutable=\"true\" name=\"playbook_8894bebc_b55f_4859_9218_222680256e24\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0itntin\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get All Data Table Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8a56f5fb-1623-4039-bd80-ed5a5a1bf05b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_all_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0itntin\u003c/incoming\u003e\u003coutgoing\u003eFlow_1y71dap\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get All Data Table Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3c034472-99ba-4302-93ec-b3d726db2e47\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1y71dap\u003c/incoming\u003e\u003coutgoing\u003eFlow_1fhp02f\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1fhp02f\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0itntin\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1y71dap\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1fhp02f\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8894bebc_b55f_4859_9218_222680256e24\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1fhp02f\" id=\"Flow_1fhp02f_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"383\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"383\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"404\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1y71dap\" id=\"Flow_1y71dap_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0itntin\" id=\"Flow_0itntin_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"644\" y=\"404\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683611687153,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_8894bebc_b55f_4859_9218_222680256e24",
      "description": {
        "content": "Return all of the rows from a data table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get All Data Table Rows (PB)",
      "export_key": "get_all_rows_pb",
      "field_type_handle": "playbook_8894bebc_b55f_4859_9218_222680256e24",
      "fields_type": {
        "actions": [],
        "display_name": "Get All Rows (PB)",
        "export_key": "playbook_8894bebc_b55f_4859_9218_222680256e24",
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
        "type_name": "playbook_8894bebc_b55f_4859_9218_222680256e24",
        "uuid": "aec3d3b3-dcaf-4c07-bef8-2d50ac8661a1"
      },
      "has_logical_errors": false,
      "id": 36,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928129387,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683614612261,
          "description": "",
          "enabled": false,
          "export_key": "Get All Data Table Rows Post-Process Script",
          "id": 57,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1683702828058,
          "name": "Get All Data Table Rows Post-Process Script",
          "object_type": "dt_utils_test_data_table",
          "playbook_handle": "get_all_rows_pb",
          "programmatic_name": "get_all_rows_pb_get_all_data_table_rows_post_process_script",
          "script_text": "note_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get All Data Table Rows\u003c/b\u003e\u003cbr\u003e\"\nresults = playbook.functions.results.get_all_rows\n\nif results.success:\n  note_text = u\"{0} \u003cbr\u003e{1}\".format(note_text, str(results.content.rows))\nelse:\n  note_text = u\"{0} \u003cbr\u003eNo rows found.\".format(note_text)\n \n  \n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "3c034472-99ba-4302-93ec-b3d726db2e47"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "get_all_rows_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8894bebc-b55f-4859-9218-222680256e24",
        "id": 49,
        "name": "playbook_8894bebc_b55f_4859_9218_222680256e24",
        "type": "playbook",
        "uuid": "b2feae39-51b1-4971-9c84-895beb442a08"
      },
      "tags": [],
      "type": "default",
      "uuid": "8894bebc-b55f-4859-9218-222680256e24",
      "version": 41
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 7,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6\" isExecutable=\"true\" name=\"playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0hp8wja\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_current_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0hp8wja\u003c/incoming\u003e\u003coutgoing\u003eFlow_10xx1ye\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Current Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"4a867564-40ef-44c1-a744-7a10776b2dea\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_10xx1ye\u003c/incoming\u003e\u003coutgoing\u003eFlow_1wo0crc\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0hp8wja\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_10xx1ye\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1wo0crc\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1wo0crc\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1wo0crc\" id=\"Flow_1wo0crc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_10xx1ye\" id=\"Flow_10xx1ye_di\"\u003e\u003comgdi:waypoint x=\"700\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"280\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"280\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0hp8wja\" id=\"Flow_0hp8wja_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"138\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"138\"/\u003e\u003comgdi:waypoint x=\"700\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.766\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"602\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683626719301,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Row Function. Get the the current row of the datatable.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Current Row (PB)",
      "export_key": "get_current_row_pb",
      "field_type_handle": "playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6",
      "fields_type": {
        "actions": [],
        "display_name": "Get Current Row (PB)",
        "export_key": "playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6",
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
        "type_name": "playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6",
        "uuid": "948c7c27-0734-4fc5-8356-98e943cdf283"
      },
      "has_logical_errors": false,
      "id": 44,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928336416,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683626719346,
          "description": "",
          "enabled": false,
          "export_key": "Get Current Row Post-Process Script",
          "id": 62,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1683703169191,
          "name": "Get Current Row Post-Process Script",
          "object_type": "dt_utils_test_data_table",
          "playbook_handle": "get_current_row_pb",
          "programmatic_name": "get_current_row_pb_get_current_row_post_process_script",
          "script_text": "note_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Row\u003c/b\u003e\u003cbr\u003e\"\nresults = playbook.functions.results.get_current_row\nif results.success:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"row\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "4a867564-40ef-44c1-a744-7a10776b2dea"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "get_current_row_pb",
      "object_type": "dt_utils_test_data_table",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_ad5da2d6-2507-4ef9-b325-50e000f04db6",
        "id": 57,
        "name": "playbook_ad5da2d6_2507_4ef9_b325_50e000f04db6",
        "type": "playbook",
        "uuid": "631cbe46-e636-4327-925b-d8e11f69ec44"
      },
      "tags": [],
      "type": "default",
      "uuid": "ad5da2d6-2507-4ef9-b325-50e000f04db6",
      "version": 12
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2\" isExecutable=\"true\" name=\"playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_114xes8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_114xes8\u003c/incoming\u003e\u003coutgoing\u003eFlow_05ii8bi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_114xes8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"02b6df73-beb1-47a2-8007-35107891c331\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_05ii8bi\u003c/incoming\u003e\u003coutgoing\u003eFlow_1v5peca\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1v5peca\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_05ii8bi\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1v5peca\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1v5peca\" id=\"Flow_1v5peca_di\"\u003e\u003comgdi:waypoint x=\"740\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"424\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_05ii8bi\" id=\"Flow_05ii8bi_di\"\u003e\u003comgdi:waypoint x=\"740\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_114xes8\" id=\"Flow_114xes8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"143\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"143\"/\u003e\u003comgdi:waypoint x=\"740\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"642\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"642\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"674\" y=\"424\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683614936554,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then returns that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Row (PB)",
      "export_key": "get_data_table_row_pb",
      "field_type_handle": "playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2",
      "fields_type": {
        "actions": [],
        "display_name": "Get Data Table Row (PB)",
        "export_key": "playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2",
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
        "type_name": "playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2",
        "uuid": "125fdf26-bb4b-448e-90d8-06dfb071fe6e"
      },
      "has_logical_errors": false,
      "id": 38,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928189895,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683615022067,
          "description": "",
          "enabled": false,
          "export_key": "Get Row Post-Process Script",
          "id": 59,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684153908219,
          "name": "Get Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "get_data_table_row_pb",
          "programmatic_name": "get_data_table_row_pb_get_row_post_process_script",
          "script_text": "results = playbook.functions.results.get_row\nnote_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Row\u003c/b\u003e\u003cbr\u003e search value: {}\".format(results[\"inputs\"][\"dt_utils_search_value\"])\n\nif results[\"success\"]:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"row\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "02b6df73-beb1-47a2-8007-35107891c331"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "get_data_table_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_56c2e4eb-fab9-41ab-8de0-ca086cab81e2",
        "id": 51,
        "name": "playbook_56c2e4eb_fab9_41ab_8de0_ca086cab81e2",
        "type": "playbook",
        "uuid": "beb34181-927d-4910-8c8d-c2159bd63ac4"
      },
      "tags": [],
      "type": "default",
      "uuid": "56c2e4eb-fab9-41ab-8de0-ca086cab81e2",
      "version": 15
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0\" isExecutable=\"true\" name=\"playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_03elkwe\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"811e99d7-d194-4ce8-86cc-aff5e01ab85c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"f7f51c3f-1601-44df-bb83-f7ec9583da96\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"11e8aca8-05bd-467b-8071-9dd160d9e14a\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}},\"c42f5cac-9e46-4ee3-bda4-6c9dbe17c516\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"2c359b58-e41e-4dd1-ac65-138e85a27363\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"fca27f70-867b-4899-b7c5-f8bdf1bbec13\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The number of max rows to return\\nif playbook.inputs.dt_utils_max_rows:\\n  inputs.dt_utils_max_rows = playbook.inputs.dt_utils_max_rows\\nelse:\\n  inputs.dt_utils_max_rows = 0\\n\\n# The direction of the sort\\ninputs.dt_utils_sort_direction = playbook.inputs.dt_utils_sort_direction\\n\\n# The api name of the column to sort by\\nif playbook.inputs.dt_utils_sort_by:\\n  inputs.dt_utils_sort_by = playbook.inputs.dt_utils_sort_by\\nelse:\\n  inputs.dt_utils_sort_by = None\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_rows\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_03elkwe\u003c/incoming\u003e\u003coutgoing\u003eFlow_0d8jlo1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Get Rows Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"6a128295-0afd-4419-a0ce-296e90e934b9\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0d8jlo1\u003c/incoming\u003e\u003coutgoing\u003eFlow_0r7610r\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_03elkwe\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0d8jlo1\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0r7610r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0r7610r\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0r7610r\" id=\"Flow_0r7610r_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"414\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0d8jlo1\" id=\"Flow_0d8jlo1_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"265\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"265\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_03elkwe\" id=\"Flow_03elkwe_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"644\" y=\"414\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683619223545,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Get Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Get Rows (PB)",
      "export_key": "get_data_table_rows_pb",
      "field_type_handle": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
      "fields_type": {
        "actions": [],
        "display_name": "Get Data Table Rows (PB)",
        "export_key": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
        "fields": {
          "dt_utils_max_rows": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0/dt_utils_max_rows",
            "hide_notification": false,
            "id": 2127,
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
            "type_id": 1066,
            "uuid": "39198bfd-52aa-4cd1-b3c1-0fe38bc2f2c4",
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
            "export_key": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0/dt_utils_sort_by",
            "hide_notification": false,
            "id": 2128,
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
            "type_id": 1066,
            "uuid": "02546f94-b273-41f7-a645-f499e8f21032",
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
            "export_key": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0/dt_utils_sort_direction",
            "hide_notification": false,
            "id": 2129,
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
            "type_id": 1066,
            "uuid": "6153993f-1539-4670-919e-e5e95d27aa2d",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "ASC",
                "properties": null,
                "uuid": "51c10371-97ab-4a0f-9713-3ac4d942ec12",
                "value": 932
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "DESC",
                "properties": null,
                "uuid": "bd3978d5-5f5c-4a24-aee8-e17cdceabc8f",
                "value": 933
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
        "type_name": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
        "uuid": "455eea46-a784-4538-9f0f-42a6f63b20b5"
      },
      "has_logical_errors": false,
      "id": 42,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928223681,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683619223618,
          "description": "",
          "enabled": false,
          "export_key": "Get Rows Post-Process Script",
          "id": 61,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684153953437,
          "name": "Get Rows Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "get_data_table_rows_pb",
          "programmatic_name": "get_data_table_rows_pb_get_rows_post_process_script",
          "script_text": "results = playbook.functions.results.get_rows\nnote_text = u\"\u003cb\u003eResult from Example: Data Table Utils: Get Rows\u003c/b\u003e\u003cbr\u003e search value: {}\".format(results[\"inputs\"][\"dt_utils_search_value\"])\n\n\nif results[\"success\"]:\n  note_text = u\"{} \u003cbr\u003e{}\".format(note_text, str(results.content[\"rows\"]))\nelse:\n  note_text = u\"{} \u003cbr\u003eNo row found.\".format(note_text)\n\nincident.addNote(helper.createRichText(note_text))",
          "tags": [],
          "uuid": "6a128295-0afd-4419-a0ce-296e90e934b9"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "02546f94-b273-41f7-a645-f499e8f21032",
            "element": "field_uuid",
            "field_type": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6153993f-1539-4670-919e-e5e95d27aa2d",
            "element": "field_uuid",
            "field_type": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "39198bfd-52aa-4cd1-b3c1-0fe38bc2f2c4",
            "element": "field_uuid",
            "field_type": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "get_data_table_rows_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_9307b948-b7f0-44c1-8f43-e0744244dbc0",
        "id": 55,
        "name": "playbook_9307b948_b7f0_44c1_8f43_e0744244dbc0",
        "type": "playbook",
        "uuid": "6553c5ff-d5dd-4afa-a117-ac263e65ac76"
      },
      "tags": [],
      "type": "default",
      "uuid": "9307b948-b7f0-44c1-8f43-e0744244dbc0",
      "version": 14
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 17,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190\" isExecutable=\"true\" name=\"playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1jr1slg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"row_to_update\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1jr1slg\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ahm5iw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_4\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1f8upf4\u003c/incoming\u003e\u003cincoming\u003eFlow_0rv4g7r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1jr1slg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cinclusiveGateway default=\"Flow_0rv4g7r\" id=\"ConditionPoint_2\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0ahm5iw\u003c/incoming\u003e\u003coutgoing\u003eFlow_0rv4g7r\u003c/outgoing\u003e\u003coutgoing\u003eFlow_12e72s6\u003c/outgoing\u003e\u003c/inclusiveGateway\u003e\u003csequenceFlow id=\"Flow_0ahm5iw\" sourceRef=\"ServiceTask_1\" targetRef=\"ConditionPoint_2\"/\u003e\u003cscriptTask id=\"ScriptTask_6\" name=\"Delete Row Post-Process Script\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"8ccc4f79-d06a-49ea-b916-ac0d43fbd150\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qw92mg\u003c/incoming\u003e\u003coutgoing\u003eFlow_1f8upf4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1f8upf4\" sourceRef=\"ScriptTask_6\" targetRef=\"EndPoint_4\"/\u003e\u003cserviceTask id=\"ServiceTask_7\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"pre_processing_script\":\"from datetime import datetime\\nfrom json import dumps\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\ninputs.dt_utils_row_id = playbook.functions.results.row_to_update.content.row[\\\"id\\\"]\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ntmp = {\\\"datetime\\\": int(datetime.now().timestamp()*1000), \\\"text\\\": \\\"Updated from Artifact\\\"}\\ninputs.dt_utils_cells_to_update = f\u0027{dumps(tmp)}\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_row\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_12e72s6\u003c/incoming\u003e\u003coutgoing\u003eFlow_0qw92mg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qw92mg\" sourceRef=\"ServiceTask_7\" targetRef=\"ScriptTask_6\"/\u003e\u003csequenceFlow id=\"Flow_12e72s6\" name=\"success\" sourceRef=\"ConditionPoint_2\" targetRef=\"ServiceTask_7\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"success\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\n\\nresults = playbook.functions.results.row_to_update\\n\\nif results[\u0027success\u0027]:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0rv4g7r\" name=\"Else\" sourceRef=\"ConditionPoint_2\" targetRef=\"EndPoint_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0rv4g7r\" id=\"Flow_0rv4g7r_di\"\u003e\u003comgdi:waypoint x=\"720\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"720\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"240\"/\u003e\u003comgdi:waypoint x=\"620\" y=\"334\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"668\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_12e72s6\" id=\"Flow_12e72s6_di\"\u003e\u003comgdi:waypoint x=\"500\" y=\"120\"/\u003e\u003comgdi:waypoint x=\"390\" y=\"120\"/\u003e\u003comgdi:waypoint x=\"390\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"41\" x=\"404\" y=\"135\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qw92mg\" id=\"Flow_0qw92mg_di\"\u003e\u003comgdi:waypoint x=\"390\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"390\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"305\"/\u003e\u003comgdi:waypoint x=\"360\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1f8upf4\" id=\"Flow_1f8upf4_di\"\u003e\u003comgdi:waypoint x=\"458\" y=\"370\"/\u003e\u003comgdi:waypoint x=\"506\" y=\"370\"/\u003e\u003comgdi:waypoint x=\"506\" y=\"360\"/\u003e\u003comgdi:waypoint x=\"554\" y=\"360\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ahm5iw\" id=\"Flow_0ahm5iw_di\"\u003e\u003comgdi:waypoint x=\"627\" y=\"-8\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jr1slg\" id=\"Flow_1jr1slg_di\"\u003e\u003comgdi:waypoint x=\"639\" y=\"-144\"/\u003e\u003comgdi:waypoint x=\"639\" y=\"-118\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"-118\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"-92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"548\" y=\"-196\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"529\" y=\"-92\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_4\" id=\"EndPoint_4_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"554\" y=\"334\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_2\" id=\"ConditionPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"238.828\" x=\"500\" y=\"94\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_6\" id=\"ScriptTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"262\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_7\" id=\"ServiceTask_7_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"292\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1684154440962,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "deployment_id": "playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190",
      "description": {
        "content": "An example Playbook showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
        "format": "text"
      },
      "display_name": "Example: Data Table Utils: Update Row (PB)",
      "export_key": "update_data_table_row_pb",
      "field_type_handle": "playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190",
      "fields_type": {
        "actions": [],
        "display_name": "Update Data Table Row (PB)",
        "export_key": "playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190",
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
        "type_name": "playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190",
        "uuid": "70023864-264a-4e8b-b19e-8818aad1ecb8"
      },
      "has_logical_errors": false,
      "id": 57,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 30,
        "name": "datatable@ibm.com",
        "type": "user"
      },
      "last_modified_time": 1684928263650,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1684154441010,
          "description": "",
          "enabled": false,
          "export_key": "Delete Row Post-Process Script",
          "id": 71,
          "language": "python3",
          "last_modified_by": "datatable@ibm.com",
          "last_modified_time": 1684399441103,
          "name": "Delete Row Post-Process Script",
          "object_type": "artifact",
          "playbook_handle": "update_data_table_row_pb",
          "programmatic_name": "update_data_table_row_pb_delete_row_post_process_script",
          "script_text": "results = playbook.functions.results.update_row\nif results.success:\n  note = u\"Row id: {} removed from datatable: {} for artifact: {}\".format(results.inputs[\u0027dt_utils_row_id\u0027], results.inputs[\u0027dt_utils_datatable_api_name\u0027], artifact.value)\nelse:\n  note = u\"Artifact: {} not found in datatable: {}\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\nincident.addNote(note)",
          "tags": [],
          "uuid": "8ccc4f79-d06a-49ea-b916-ac0d43fbd150"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "update_data_table_row_pb",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_6d0caf1b-ec2c-4114-afbf-432f5db44190",
        "id": 72,
        "name": "playbook_6d0caf1b_ec2c_4114_afbf_432f5db44190",
        "type": "playbook",
        "uuid": "c6d7e81f-0c4e-4fbd-a887-f5a2dd5a4ece"
      },
      "tags": [],
      "type": "default",
      "uuid": "6d0caf1b-ec2c-4114-afbf-432f5db44190",
      "version": 23
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 8529,
    "major": 48,
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
          "id": 1739,
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
          "type_id": 1042,
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
          "id": 1740,
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
          "type_id": 1042,
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
          "id": 1741,
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
          "type_id": 1042,
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
          "id": 1742,
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
          "type_id": 1042,
          "uuid": "5686792a-79b8-4756-b0f2-f1ec085bc37a",
          "values": [
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "a",
              "properties": null,
              "uuid": "587c135e-2d39-4140-822e-7829b03d4a21",
              "value": 733
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "b",
              "properties": null,
              "uuid": "b5514bda-e2f8-41d1-bf39-a2d09f37214a",
              "value": 734
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "c",
              "properties": null,
              "uuid": "6282c55c-af54-4c98-b5d1-12db87a4c76a",
              "value": 735
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "d",
              "properties": null,
              "uuid": "29eaf525-205a-46a5-b591-e023157053b4",
              "value": 736
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "e",
              "properties": null,
              "uuid": "48f95069-25a8-4919-9004-7066543dbcd5",
              "value": 737
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "f",
              "properties": null,
              "uuid": "e11c6dc8-70cc-4448-917a-93ab16c864e0",
              "value": 738
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "g",
              "properties": null,
              "uuid": "ebcbf31c-f5b2-4d3a-b1fe-334ce7cdaa9b",
              "value": 739
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "h",
              "properties": null,
              "uuid": "3f2963b6-8e1b-44b5-ba59-32cfbe7bdf5b",
              "value": 740
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "I",
              "properties": null,
              "uuid": "484dc992-3526-4e06-a392-fe8647373913",
              "value": 741
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "j",
              "properties": null,
              "uuid": "28c16106-f096-4565-b601-3a03da496559",
              "value": 742
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "k",
              "properties": null,
              "uuid": "260a964d-63e7-483d-b4f8-6822206830d0",
              "value": 743
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
          "id": 1743,
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
          "type_id": 1042,
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
          "id": 1744,
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
          "type_id": 1042,
          "uuid": "e2239bee-9516-4c7f-852a-2a884bcbaf0f",
          "values": [
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "1",
              "properties": null,
              "uuid": "6559ac56-25a2-4015-a681-9e89328da0a3",
              "value": 744
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "2",
              "properties": null,
              "uuid": "bd341de4-c08e-4ba2-9179-04a28a32e22e",
              "value": 745
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "3",
              "properties": null,
              "uuid": "9d7a37be-a50a-4bdf-8478-63e4be6ec4bc",
              "value": 746
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "4",
              "properties": null,
              "uuid": "8ecdf624-0e32-46f7-8d8a-f183c8559032",
              "value": 747
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "5",
              "properties": null,
              "uuid": "653d3e8e-00c9-41f4-85f2-10addde4b1ba",
              "value": 748
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "6",
              "properties": null,
              "uuid": "b5746a1b-9404-4b9c-bb20-924682a3ad97",
              "value": 749
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "7",
              "properties": null,
              "uuid": "b3f95da8-12fb-44f0-9f89-9b1ee269762b",
              "value": 750
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "8",
              "properties": null,
              "uuid": "d6d40d79-d0c4-4122-b982-91114e4b801b",
              "value": 751
            },
            {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "9",
              "properties": null,
              "uuid": "ec4b97d4-b313-4ded-bb0d-eda35b6dc172",
              "value": 802
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
          "id": 1745,
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
          "type_id": 1042,
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
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_add_row_to_datatable",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_add_row_to_datatable\" isExecutable=\"true\" name=\"Example: Data Table Utils: Add Row to Datatable\"\u003e\u003cdocumentation\u003eAdd a row to the given datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1srju0b\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1xo418p\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"dt_col_name\\\": str(artifact.value), \\\"number\\\": 1, \\\"text\\\": \\\"example add row\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1srju0b\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ydtzhk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1srju0b\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1xo418p\"/\u003e\u003cendEvent id=\"EndEvent_0se873w\"\u003e\u003cincoming\u003eSequenceFlow_1ydtzhk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ydtzhk\" sourceRef=\"ServiceTask_1xo418p\" targetRef=\"EndEvent_0se873w\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1xo418p\" id=\"ServiceTask_1xo418p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"239\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1srju0b\" id=\"SequenceFlow_1srju0b_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"239\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0se873w\" id=\"EndEvent_0se873w_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"395\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"413\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ydtzhk\" id=\"SequenceFlow_1ydtzhk_di\"\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"395\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"367\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Add a row to the given datatable.",
      "export_key": "example_data_table_utils_add_row_to_datatable",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091873,
      "name": "Example: Data Table Utils: Add Row to Datatable",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_add_row_to_datatable",
      "tags": [],
      "uuid": "a5ffd9fb-2ef0-448e-81a9-5a5bce8d20e2",
      "workflow_id": 116
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_delete_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_delete_row\" isExecutable=\"true\" name=\"Example: Data Table Utils: Delete Row\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pptje3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0oj7gk8\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python\",\"result_name\":\"row_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pptje3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08hc529\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_18o72ll\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note = u\\\"Row id: {} removed from datatable: {} for artifact: {}\\\".format(results.inputs[\u0027dt_utils_row_id\u0027], results.inputs[\u0027dt_utils_datatable_api_name\u0027], artifact.value)\\nelse:\\n  note = u\\\"Artifact: {} not found in datatable: {}\\\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\\n\\nincident.addNote(note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = workflow.properties.row_to_delete.inputs.dt_utils_datatable_api_name\\n\\n# The ID of the row to delete [again, taken from previous Get Row Function]\\ninputs.dt_utils_row_id = workflow.properties.row_to_delete.content.row[\\\"id\\\"]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1r9312q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_135ais0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_13jtock\"\u003e\u003cincoming\u003eSequenceFlow_135ais0\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0uv7luk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_135ais0\" sourceRef=\"ServiceTask_18o72ll\" targetRef=\"EndEvent_13jtock\"/\u003e\u003csequenceFlow id=\"SequenceFlow_08hc529\" sourceRef=\"ServiceTask_0oj7gk8\" targetRef=\"ExclusiveGateway_177w6e8\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1pptje3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0oj7gk8\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_177w6e8\"\u003e\u003cincoming\u003eSequenceFlow_08hc529\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1r9312q\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0uv7luk\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1r9312q\" name=\"success\" sourceRef=\"ExclusiveGateway_177w6e8\" targetRef=\"ServiceTask_18o72ll\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"success = workflow.properties.row_to_delete.success\",\"final_expression_text\":\"success\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0uv7luk\" name=\"fail\" sourceRef=\"ExclusiveGateway_177w6e8\" targetRef=\"EndEvent_13jtock\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"fail = not workflow.properties.row_to_delete.success\",\"final_expression_text\":\"fail\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_053uwhv\"\u003e\u003ctext\u003eInputs: data_table_api_name, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0o1dkfq\" sourceRef=\"ServiceTask_0oj7gk8\" targetRef=\"TextAnnotation_053uwhv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12gmms9\"\u003e\u003ctext\u003eOutput: the data table row that contains its ID and Cells\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0o7jw8z\" sourceRef=\"ServiceTask_0oj7gk8\" targetRef=\"TextAnnotation_12gmms9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_178wajp\"\u003e\u003ctext\u003eIf we find a row, continue, else end\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0n41ldu\" sourceRef=\"ExclusiveGateway_177w6e8\" targetRef=\"TextAnnotation_178wajp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1oyy5lt\"\u003e\u003ctext\u003eInputs: data_table_api_name, row_id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0f4r6h7\" sourceRef=\"ServiceTask_18o72ll\" targetRef=\"TextAnnotation_1oyy5lt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_197xlxy\"\u003e\u003ctext\u003eOutput: a success flag if row deleted\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1wid1dq\" sourceRef=\"ServiceTask_18o72ll\" targetRef=\"TextAnnotation_197xlxy\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0oj7gk8\" id=\"ServiceTask_0oj7gk8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"297\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_18o72ll\" id=\"ServiceTask_18o72ll_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"621\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_13jtock\" id=\"EndEvent_13jtock_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"797\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"770\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_135ais0\" id=\"SequenceFlow_135ais0_di\"\u003e\u003comgdi:waypoint x=\"721\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"797\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"714\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08hc529\" id=\"SequenceFlow_08hc529_di\"\u003e\u003comgdi:waypoint x=\"397\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"394.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pptje3\" id=\"SequenceFlow_1pptje3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"297\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"247.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_177w6e8\" id=\"ExclusiveGateway_177w6e8_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"482\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"507\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1r9312q\" id=\"SequenceFlow_1r9312q_di\"\u003e\u003comgdi:waypoint x=\"532\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"621\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"43\" x=\"556\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uv7luk\" id=\"SequenceFlow_0uv7luk_di\"\u003e\u003comgdi:waypoint x=\"507\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"507\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003comgdi:waypoint x=\"815\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003comgdi:waypoint x=\"815\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"17\" x=\"653\" y=\"88\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_053uwhv\" id=\"TextAnnotation_053uwhv_di\"\u003e\u003comgdc:Bounds height=\"63\" width=\"151\" x=\"182\" y=\"51\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0o1dkfq\" id=\"Association_0o1dkfq_di\"\u003e\u003comgdi:waypoint x=\"318\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12gmms9\" id=\"TextAnnotation_12gmms9_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"125\" x=\"378\" y=\"43\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0o7jw8z\" id=\"Association_0o7jw8z_di\"\u003e\u003comgdi:waypoint x=\"375\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_178wajp\" id=\"TextAnnotation_178wajp_di\"\u003e\u003comgdc:Bounds height=\"47\" width=\"115\" x=\"449\" y=\"275\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0n41ldu\" id=\"Association_0n41ldu_di\"\u003e\u003comgdi:waypoint x=\"507\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"507\" xsi:type=\"omgdc:Point\" y=\"275\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1oyy5lt\" id=\"TextAnnotation_1oyy5lt_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"104\" x=\"555\" y=\"332\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0f4r6h7\" id=\"Association_0f4r6h7_di\"\u003e\u003comgdi:waypoint x=\"655\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"621\" xsi:type=\"omgdc:Point\" y=\"332\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_197xlxy\" id=\"TextAnnotation_197xlxy_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"147\" x=\"714\" y=\"341\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1wid1dq\" id=\"Association_1wid1dq_di\"\u003e\u003comgdi:waypoint x=\"700\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"770\" xsi:type=\"omgdc:Point\" y=\"341\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example Workflow showing how to use the Data Table Utils: Delete Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then deletes that row from the Data Table.",
      "export_key": "example_data_table_utils_delete_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091992,
      "name": "Example: Data Table Utils: Delete Row",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_delete_row",
      "tags": [],
      "uuid": "686db112-6f44-40bb-8d9a-f789b4fb5be9",
      "workflow_id": 117
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_get_current_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_get_current_row\" isExecutable=\"true\" name=\"Example: Data Table Utils: Get Current Row\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Get Row Function. Get the the current row of the datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0xlivfe\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ln9onu\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Get Row\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\"\\nif results.success:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;{}\\\".format(note_text, str(results.content[\\\"row\\\"]))\\nelse:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;No row found.\\\".format(note_text)\\n\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xlivfe\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0l8inf3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xlivfe\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ln9onu\"/\u003e\u003cendEvent id=\"EndEvent_0blnyk1\"\u003e\u003cincoming\u003eSequenceFlow_0l8inf3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0l8inf3\" sourceRef=\"ServiceTask_1ln9onu\" targetRef=\"EndEvent_0blnyk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ln9onu\" id=\"ServiceTask_1ln9onu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xlivfe\" id=\"SequenceFlow_0xlivfe_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0blnyk1\" id=\"EndEvent_0blnyk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"403\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"421\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l8inf3\" id=\"SequenceFlow_0l8inf3_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"375\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example Workflow showing how to use the Data Table Utils: Get Row Function. Get the the current row of the datatable.",
      "export_key": "example_data_table_utils_get_current_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278090703,
      "name": "Example: Data Table Utils: Get Current Row",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "example_data_table_utils_get_current_row",
      "tags": [],
      "uuid": "c2871c5a-1e0f-421e-b2af-02bc4a00c42e",
      "workflow_id": 106
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_get_all_data_table_rows",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_get_all_data_table_rows\" isExecutable=\"true\" name=\"Example: Data Table Utils: Get All Data Table Rows\"\u003e\u003cdocumentation\u003eReturn all of the rows from a data table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1i3q9vy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0vnhpte\" name=\"Data Table Utils: Get All Data Ta...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8a56f5fb-1623-4039-bd80-ed5a5a1bf05b\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Get All Data Table Rows\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\\"\\nif results.success:\\n  note_text = u\\\"{0} \u0026lt;br\u0026gt;{1}\\\".format(note_text, str(results.content.rows))\\nelse:\\n  note_text = u\\\"{0} \u0026lt;br\u0026gt;No rows found.\\\".format(note_text)\\n\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1i3q9vy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1m9bjz4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1i3q9vy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0vnhpte\"/\u003e\u003cendEvent id=\"EndEvent_09yrvy7\"\u003e\u003cincoming\u003eSequenceFlow_1m9bjz4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1m9bjz4\" sourceRef=\"ServiceTask_0vnhpte\" targetRef=\"EndEvent_09yrvy7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vnhpte\" id=\"ServiceTask_0vnhpte_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"249\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1i3q9vy\" id=\"SequenceFlow_1i3q9vy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"223.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09yrvy7\" id=\"EndEvent_09yrvy7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"402\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"420\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m9bjz4\" id=\"SequenceFlow_1m9bjz4_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"375.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Return all of the rows from a data table.",
      "export_key": "example_data_table_utils_get_all_data_table_rows",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091637,
      "name": "Example: Data Table Utils: Get All Data Table Rows",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "example_data_table_utils_get_all_data_table_rows",
      "tags": [],
      "uuid": "d10ff50b-da54-4325-81ce-f7e9dc0aa5f6",
      "workflow_id": 114
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_data_table_utils_delete_rows",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_delete_rows\" isExecutable=\"true\" name=\"Example: Data Table Utils: Delete Rows\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Delete Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0exjopw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_02dhv4b\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}}},\"post_processing_script\":\"if not results.success:\\n  incident.addNote(helper.createRichText(\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Delete Rows\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;No rows found.\\\"))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The number of max rows to return\\nif rule.properties.dt_utils_max_rows:\\n  inputs.dt_utils_max_rows = rule.properties.dt_utils_max_rows\\nelse:\\n  inputs.dt_utils_max_rows = 0\\n\\n# The direction of the sort\\nif rule.properties.dt_utils_sort_direction:\\n  inputs.dt_utils_sort_direction = rule.properties.dt_utils_sort_direction\\nelse:\\n  inputs.dt_utils_sort_direction = \\\"ASC\\\"\\n\\n# The api name of the column to sort by\\nif rule.properties.dt_utils_sort_by:\\n  inputs.dt_utils_sort_by = rule.properties.dt_utils_sort_by\\nelse:\\n  inputs.dt_utils_sort_by = None\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"rows_to_delete\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0exjopw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1faqnyq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0exjopw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_02dhv4b\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0kgufcz\"\u003e\u003cincoming\u003eSequenceFlow_1faqnyq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0wtnh17\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0wirvr3\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1faqnyq\" sourceRef=\"ServiceTask_02dhv4b\" targetRef=\"ExclusiveGateway_0kgufcz\"/\u003e\u003cserviceTask id=\"ServiceTask_04as9z2\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.success:\\n  note = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Artifact: {} Delete Rows\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; {}\\\".format(artifact.value, str(results.content[\\\"rows_ids\\\"]))\\nelse:\\n  note = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Artifact: {} not found in datatable: {}\\\".format(artifact.value, results.inputs[\u0027dt_utils_datatable_api_name\u0027])\\n\\nincident.addNote(helper.createRichText(note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table, search column, search value [here it is taken from previous Get Rows Function inputs]\\ninputs.dt_utils_datatable_api_name = workflow.properties.rows_to_delete.inputs.dt_utils_datatable_api_name\\n\\n# The internal IDs of the rows that will be deleted [again, taken from previous Get Rows Function]\\nif workflow.properties.rows_to_delete and workflow.properties.rows_to_delete.content.rows:\\n  rows_ids = []\\n  for row in workflow.properties.rows_to_delete.content.rows:\\n    rows_ids.append(row[\\\"id\\\"])\\n  inputs.dt_utils_rows_ids = str(rows_ids)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0wtnh17\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mgbnmy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0mkob5h\"\u003e\u003cincoming\u003eSequenceFlow_1mgbnmy\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0wirvr3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1mgbnmy\" sourceRef=\"ServiceTask_04as9z2\" targetRef=\"EndEvent_0mkob5h\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0wtnh17\" name=\"success\" sourceRef=\"ExclusiveGateway_0kgufcz\" targetRef=\"ServiceTask_04as9z2\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"success = workflow.properties.rows_to_delete.success\",\"final_expression_text\":\"success\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0wirvr3\" name=\"fail\" sourceRef=\"ExclusiveGateway_0kgufcz\" targetRef=\"EndEvent_0mkob5h\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"fail = not workflow.properties.rows_to_delete.success\",\"final_expression_text\":\"fail\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1s67jx1\"\u003e\u003ctext\u003eInputs: data_table_api_name, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0t3j0lc\" sourceRef=\"ServiceTask_04as9z2\" targetRef=\"TextAnnotation_1s67jx1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1uvroo6\"\u003e\u003ctext\u003eOutput: The list of internal row IDs of the Data Table that were deleted\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_08ijs43\" sourceRef=\"ServiceTask_04as9z2\" targetRef=\"TextAnnotation_1uvroo6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_18op32u\"\u003e\u003ctext\u003eIf we find a row/s, continue, else end\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1uib20x\" sourceRef=\"ExclusiveGateway_0kgufcz\" targetRef=\"TextAnnotation_18op32u\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0v1gl3d\"\u003e\u003ctext\u003eInputs: datatable_api_name, max_rows, sort_by, sort_direction, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02ineyw\" sourceRef=\"ServiceTask_02dhv4b\" targetRef=\"TextAnnotation_0v1gl3d\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_01d3tf0\"\u003e\u003ctext\u003eOutput: The Data Table rows\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1yje4os\" sourceRef=\"ServiceTask_02dhv4b\" targetRef=\"TextAnnotation_01d3tf0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_02dhv4b\" id=\"ServiceTask_02dhv4b_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"298\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0exjopw\" id=\"SequenceFlow_0exjopw_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"298\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"248\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0kgufcz\" id=\"ExclusiveGateway_0kgufcz_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"499.12462311557783\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"524.1246231155778\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1faqnyq\" id=\"SequenceFlow_1faqnyq_di\"\u003e\u003comgdi:waypoint x=\"398\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"499\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"448.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_04as9z2\" id=\"ServiceTask_04as9z2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"646.1246231155778\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0mkob5h\" id=\"EndEvent_0mkob5h_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"854.1246231155778\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"872.1246231155778\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mgbnmy\" id=\"SequenceFlow_1mgbnmy_di\"\u003e\u003comgdi:waypoint x=\"746\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"854\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"800\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1s67jx1\" id=\"TextAnnotation_1s67jx1_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"134\" x=\"526\" y=\"311\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0t3j0lc\" id=\"Association_0t3j0lc_di\"\u003e\u003comgdi:waypoint x=\"667\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"619\" y=\"311\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1uvroo6\" id=\"TextAnnotation_1uvroo6_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"128\" x=\"771\" y=\"311\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_08ijs43\" id=\"Association_08ijs43_di\"\u003e\u003comgdi:waypoint x=\"736\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"802\" y=\"311\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_18op32u\" id=\"TextAnnotation_18op32u_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"108\" x=\"470\" y=\"247\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1uib20x\" id=\"Association_1uib20x_di\"\u003e\u003comgdi:waypoint x=\"524\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"525\" y=\"247\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0v1gl3d\" id=\"TextAnnotation_0v1gl3d_di\"\u003e\u003comgdc:Bounds height=\"90\" width=\"125\" x=\"197\" y=\"0\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02ineyw\" id=\"Association_02ineyw_di\"\u003e\u003comgdi:waypoint x=\"326\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"285\" y=\"90\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_01d3tf0\" id=\"TextAnnotation_01d3tf0_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"100\" x=\"384\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1yje4os\" id=\"Association_1yje4os_di\"\u003e\u003comgdi:waypoint x=\"373\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"422\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wtnh17\" id=\"SequenceFlow_0wtnh17_di\"\u003e\u003comgdi:waypoint x=\"549\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"646\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"41\" x=\"578\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wirvr3\" id=\"SequenceFlow_0wirvr3_di\"\u003e\u003comgdi:waypoint x=\"524\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"524\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"872\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"872\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"17\" x=\"690\" y=\"93\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example Workflow showing how to use the Data Table Utils: Delete Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.",
      "export_key": "example_data_table_utils_delete_rows",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1684154319531,
      "name": "Example: Data Table Utils: Delete Rows",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_delete_rows",
      "tags": [],
      "uuid": "fa5793d9-3e18-428b-859e-3c4d517755f5",
      "workflow_id": 105
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "update_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"update_row\" isExecutable=\"true\" name=\"Example Data Utils: Update Row\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Update Row Function. It illustrates updating the current row with static values.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00npig6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1acobvs\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# Refer to the existing row (value: 0)\\ninputs.dt_utils_row_id = 0\\n\\n# The column api names and the value to update the cell to\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"name\\\": \\\"Updated Example\\\", \\\"text\\\": \\\"Update from datatable\\\", \\\"number\\\": 4598, \\\"multi_select\\\": [\\\"b\\\", \\\"e\\\", \\\"g\\\"], \\\"boolean\\\": True})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00npig6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16wasgm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_00npig6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1acobvs\"/\u003e\u003cendEvent id=\"EndEvent_09dndei\"\u003e\u003cincoming\u003eSequenceFlow_16wasgm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16wasgm\" sourceRef=\"ServiceTask_1acobvs\" targetRef=\"EndEvent_09dndei\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1acobvs\" id=\"ServiceTask_1acobvs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00npig6\" id=\"SequenceFlow_00npig6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"243.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09dndei\" id=\"EndEvent_09dndei_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"452\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"470\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16wasgm\" id=\"SequenceFlow_16wasgm_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"420.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example Workflow showing how to use the Data Table Utils: Update Row Function. It illustrates updating the current row with static values.",
      "export_key": "update_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091397,
      "name": "Example Data Utils: Update Row",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "update_row",
      "tags": [],
      "uuid": "a078edb6-1b2f-43ad-81e6-f809689ae1e1",
      "workflow_id": 112
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_delete_row_from_datatable",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_delete_row_from_datatable\" isExecutable=\"true\" name=\"Example: Data Table Utils: Delete Row from Datatable\"\u003e\u003cdocumentation\u003eDelete a row from a datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ja63g4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_05odd5l\" name=\"Data Table Utils: Delete Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"50cf405e-aac1-43e7-961e-3894d38688ad\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.incident_id = incident.id\\ninputs.dt_utils_row_id = 0 # 0 represents current row\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ja63g4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kz2way\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ja63g4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_05odd5l\"/\u003e\u003cendEvent id=\"EndEvent_0g2neqr\"\u003e\u003cincoming\u003eSequenceFlow_0kz2way\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0kz2way\" sourceRef=\"ServiceTask_05odd5l\" targetRef=\"EndEvent_0g2neqr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_05odd5l\" id=\"ServiceTask_05odd5l_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ja63g4\" id=\"SequenceFlow_1ja63g4_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0g2neqr\" id=\"EndEvent_0g2neqr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"346\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kz2way\" id=\"SequenceFlow_0kz2way_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"315\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Delete a row from a datatable.",
      "export_key": "example_data_table_utils_delete_row_from_datatable",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091756,
      "name": "Example: Data Table Utils: Delete Row from Datatable",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "example_data_table_utils_delete_row_from_datatable",
      "tags": [],
      "uuid": "6dd89604-21a4-4456-b07a-9258f55baedb",
      "workflow_id": 115
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_delete_rows_from_datatable",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_delete_rows_from_datatable\" isExecutable=\"true\" name=\"Example: Data Table Utils: Delete Rows from Datatable\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ckvg8u\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1d15de4\" name=\"Data Table Utils: Delete Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ef4ef5c0-5de2-4fbc-90c9-f7568451da95\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"if not row.dt_col_name:\\n  helper.fail(\\\"The data table column \u0027name\u0027 must contain a value\\\")\\n\\ninputs.incident_id = incident.id\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\ninputs.dt_utils_search_value = row.dt_col_name\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ckvg8u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03gm5d9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ckvg8u\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1d15de4\"/\u003e\u003cendEvent id=\"EndEvent_1t18ug2\"\u003e\u003cincoming\u003eSequenceFlow_03gm5d9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_03gm5d9\" sourceRef=\"ServiceTask_1d15de4\" targetRef=\"EndEvent_1t18ug2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1d15de4\" id=\"ServiceTask_1d15de4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"269\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ckvg8u\" id=\"SequenceFlow_1ckvg8u_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"269\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"233.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t18ug2\" id=\"EndEvent_1t18ug2_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"434.9815817984832\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452.9815817984832\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03gm5d9\" id=\"SequenceFlow_03gm5d9_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"402\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Deletes rows from a Data Table given a list of internal row IDs or a \u0027search_column and search_value\u0027 pair.",
      "export_key": "example_data_table_utils_delete_rows_from_datatable",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278090925,
      "name": "Example: Data Table Utils: Delete Rows from Datatable",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "example_data_table_utils_delete_rows_from_datatable",
      "tags": [],
      "uuid": "6539208d-0878-4e0e-a4d4-0da7e680ce19",
      "workflow_id": 108
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_update_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_update_row\" isExecutable=\"true\" name=\"Example: Data Table Utils: Update Row\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Update Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then updates that row with the given values.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1godxss\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1o82xsx\" name=\"Data Table Utils: Update Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77b8451e-3137-4362-840a-ac724b674b73\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update [here it is taken from previous Get Row Function]\\ninputs.dt_utils_datatable_api_name = workflow.properties.row_to_update.inputs.dt_utils_datatable_api_name\\n\\n# The ID of the row to update [again, taken from previous Get Row Function]\\ninputs.dt_utils_row_id = workflow.properties.row_to_update.content.row[\\\"id\\\"]\\n\\n# The column api names and the value to update the cell to\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"datetime\\\": Date().getTime(),\\\"text\\\": \\\"Updated from Artifact\\\"})\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ap5bmy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qwi15e\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_090gk4x\"\u003e\u003cincoming\u003eSequenceFlow_0qwi15e\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_129h6sa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0qwi15e\" sourceRef=\"ServiceTask_1o82xsx\" targetRef=\"EndEvent_090gk4x\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1godxss\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1yllp7s\"/\u003e\u003cserviceTask id=\"ServiceTask_1yllp7s\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"row_to_update\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1godxss\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zfsi47\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zfsi47\" sourceRef=\"ServiceTask_1yllp7s\" targetRef=\"ExclusiveGateway_0j87ouk\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0j87ouk\"\u003e\u003cincoming\u003eSequenceFlow_0zfsi47\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ap5bmy\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_129h6sa\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0ap5bmy\" name=\"success\" sourceRef=\"ExclusiveGateway_0j87ouk\" targetRef=\"ServiceTask_1o82xsx\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"success = workflow.properties.row_to_update.success\",\"final_expression_text\":\"success\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_129h6sa\" name=\"fail\" sourceRef=\"ExclusiveGateway_0j87ouk\" targetRef=\"EndEvent_090gk4x\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"fail = not workflow.properties.row_to_update.success\",\"final_expression_text\":\"fail\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_0pp938a\"\u003e\u003ctext\u003eInputs: data_table_api_name, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1lvlnky\" sourceRef=\"ServiceTask_1yllp7s\" targetRef=\"TextAnnotation_0pp938a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qb3o9g\"\u003e\u003ctext\u003eOutput: the data table row that contains its ID and Cells\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_115ahxc\" sourceRef=\"ServiceTask_1yllp7s\" targetRef=\"TextAnnotation_0qb3o9g\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1jqrzhf\"\u003e\u003ctext\u003eIf we find a row, continue, else end\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1spz4lt\" sourceRef=\"ExclusiveGateway_0j87ouk\" targetRef=\"TextAnnotation_1jqrzhf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04qvwbx\"\u003e\u003ctext\u003eInputs: data_table_api_name, row_id, cells_to_update\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rilri5\" sourceRef=\"ServiceTask_1o82xsx\" targetRef=\"TextAnnotation_04qvwbx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0vbm79s\"\u003e\u003ctext\u003eOutput: the updated row\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1t8i02h\" sourceRef=\"ServiceTask_1o82xsx\" targetRef=\"TextAnnotation_0vbm79s\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"122\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"117\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1o82xsx\" id=\"ServiceTask_1o82xsx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"545\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_090gk4x\" id=\"EndEvent_090gk4x_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"725\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"743\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qwi15e\" id=\"SequenceFlow_0qwi15e_di\"\u003e\u003comgdi:waypoint x=\"645\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"725\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"640\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1godxss\" id=\"SequenceFlow_1godxss_di\"\u003e\u003comgdi:waypoint x=\"158\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"152\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1yllp7s\" id=\"ServiceTask_1yllp7s_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zfsi47\" id=\"SequenceFlow_0zfsi47_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"324\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0j87ouk\" id=\"ExclusiveGateway_0j87ouk_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"402\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"427\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ap5bmy\" id=\"SequenceFlow_0ap5bmy_di\"\u003e\u003comgdi:waypoint x=\"452\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"545\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"43\" x=\"478\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_129h6sa\" id=\"SequenceFlow_129h6sa_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003comgdi:waypoint x=\"743\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003comgdi:waypoint x=\"743\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"17\" x=\"577\" y=\"106\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0pp938a\" id=\"TextAnnotation_0pp938a_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"138\" x=\"129\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1lvlnky\" id=\"Association_1lvlnky_di\"\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"223\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qb3o9g\" id=\"TextAnnotation_0qb3o9g_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"135\" x=\"348\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_115ahxc\" id=\"Association_115ahxc_di\"\u003e\u003comgdi:waypoint x=\"329\" xsi:type=\"omgdc:Point\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"384\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1jqrzhf\" id=\"TextAnnotation_1jqrzhf_di\"\u003e\u003comgdc:Bounds height=\"44\" width=\"120\" x=\"367\" y=\"249\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1spz4lt\" id=\"Association_1spz4lt_di\"\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"427\" xsi:type=\"omgdc:Point\" y=\"249\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04qvwbx\" id=\"TextAnnotation_04qvwbx_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"140\" x=\"416\" y=\"334\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rilri5\" id=\"Association_0rilri5_di\"\u003e\u003comgdi:waypoint x=\"567\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"506\" xsi:type=\"omgdc:Point\" y=\"334\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0vbm79s\" id=\"TextAnnotation_0vbm79s_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"152\" x=\"629\" y=\"335\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1t8i02h\" id=\"Association_1t8i02h_di\"\u003e\u003comgdi:waypoint x=\"625\" xsi:type=\"omgdc:Point\" y=\"246\"/\u003e\u003comgdi:waypoint x=\"690\" xsi:type=\"omgdc:Point\" y=\"335\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example Workflow showing how to use the Data Table Utils: Update Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then updates that row with the given values.",
      "export_key": "example_data_table_utils_update_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091279,
      "name": "Example: Data Table Utils: Update Row",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_update_row",
      "tags": [],
      "uuid": "22f49b83-8334-4e99-88cb-f80a934b529b",
      "workflow_id": 111
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_create_csv_datatable",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_create_csv_datatable\" isExecutable=\"true\" name=\"Example: Data Table Utils: Create CSV Datatable\"\u003e\u003cdocumentation\u003eTake CSV data and add the results to a named datatable. Results of the function are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_0pa0hsb\"\u003e\u003coutgoing\u003eSequenceFlow_0lumpz7\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1glg38k\" name=\"Data Table Utils: Create CSV Data...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6edc80c4-e5ae-4c33-b1f1-f0c101918d7a\"\u003e{\"inputs\":{\"ea2dc835-7451-4386-abae-73634223d991\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results.success:\\n  note_text = u\\\"\\\"\\\"Results from Data Table Utils: Create CSV Datatable\\\\nData Source: {}\\\\nRows added: {}\\\\nRows not added: {}\\\"\\\"\\\".format(results.content[\\\"data_source\\\"], results.content[\\\"rows_added\\\"], results.content[\\\"rows_with_errors\\\"])\\n  incident.addNote(note_text)\\nelse:\\n  incident.addNote(u\\\"Error: Failed to add rows\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n# The api name of the Data Table to update\\ninputs.dt_datable_name = \\\"dt_utils_test_data_table\\\"\\n# uncomment attachment_id when reading csv data from an attachmennt\\ninputs.attachment_id = attachment.id\\n\\n# A boolean to determine if CSV headers are present\\ninputs.dt_has_headers = True\\n\\n## The mapping format should be \\\"csv_header\\\":\\\"dt_column_name\\\"\\nmapping = \u0027\u0027\u0027{\\n  \\\"hdr_number\\\": \\\"number\\\",\\n  \\\"hdr_text\\\": \\\"text\\\",\\n  \\\"hdr_boolean\\\": \\\"boolean\\\",\\n  \\\"hdr_datetime\\\": \\\"datetime\\\",\\n  \\\"hdr_select\\\": \\\"select\\\",\\n  \\\"hdr_multiselect\\\": \\\"multi_select\\\"\\n}\u0027\u0027\u0027\\n# mappings of csv data without headers will be a list of data_table column names. Use null to bypass a csv data column\\nmapping_no_headers = \u0027\u0027\u0027[\\\"number\\\",\\\"text\\\",\\\"boolean\\\",\\\"datetime\\\",\\\"select\\\",\\\"multi_select\\\",\\\"x\\\",\\\"y\\\",\\\"z\\\"]\u0027\u0027\u0027\\ninputs.dt_mapping_table = mapping\\n# year - %Y, month - %m, day - %d, hour - %H, minutes - %M, seconds - %S, milliseconds - %f, timezone offset - %z\u0027\\ninputs.dt_date_time_format = \\\"%m/%d/%y %H:%M\\\"\\n# optional start row csv data. The first data row = 1\\n##inputs.dt_start_row = 0\\n# optional max number of csv rows to add relative to dt_start_row\\n##inputs.dt_max_rows = 5\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0lumpz7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13wtfwl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0lumpz7\" sourceRef=\"StartEvent_0pa0hsb\" targetRef=\"ServiceTask_1glg38k\"/\u003e\u003cendEvent id=\"EndEvent_0214dvu\"\u003e\u003cincoming\u003eSequenceFlow_13wtfwl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13wtfwl\" sourceRef=\"ServiceTask_1glg38k\" targetRef=\"EndEvent_0214dvu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_057c9ze\"\u003e\u003ctext\u003e\u003c![CDATA[Input:\ncsv file with mapping information\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02h3xuq\" sourceRef=\"ServiceTask_1glg38k\" targetRef=\"TextAnnotation_057c9ze\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0c1wjn8\"\u003e\u003ctext\u003e\u003c![CDATA[\nOutput:\nDatatable row is created\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ultasz\" sourceRef=\"ServiceTask_1glg38k\" targetRef=\"TextAnnotation_0c1wjn8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_0pa0hsb\" id=\"StartEvent_0pa0hsb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"406\" y=\"127\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"379\" y=\"166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1glg38k\" id=\"ServiceTask_1glg38k_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"535\" y=\"105\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lumpz7\" id=\"SequenceFlow_0lumpz7_di\"\u003e\u003comgdi:waypoint x=\"442\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"443.5\" y=\"123.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0214dvu\" id=\"EndEvent_0214dvu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"726\" y=\"127\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"699\" y=\"166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13wtfwl\" id=\"SequenceFlow_13wtfwl_di\"\u003e\u003comgdi:waypoint x=\"635\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003comgdi:waypoint x=\"726\" xsi:type=\"omgdc:Point\" y=\"145\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"635.5\" y=\"123.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_057c9ze\" id=\"TextAnnotation_057c9ze_di\"\u003e\u003comgdc:Bounds height=\"73\" width=\"156\" x=\"391\" y=\"-12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02h3xuq\" id=\"Association_02h3xuq_di\"\u003e\u003comgdi:waypoint x=\"547\" xsi:type=\"omgdc:Point\" y=\"105\"/\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"61\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0c1wjn8\" id=\"TextAnnotation_0c1wjn8_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"152\" x=\"668\" y=\"-13\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ultasz\" id=\"Association_1ultasz_di\"\u003e\u003comgdi:waypoint x=\"630\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"62\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Take CSV data and add the results to a named datatable. Results of the function are written to an incident note.",
      "export_key": "example_create_csv_datatable",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091516,
      "name": "Example: Data Table Utils: Create CSV Datatable",
      "object_type": "attachment",
      "programmatic_name": "example_create_csv_datatable",
      "tags": [],
      "uuid": "6564ccbf-868a-40c5-826c-422962be394f",
      "workflow_id": 113
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_get_rows",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_get_rows\" isExecutable=\"true\" name=\"Example: Data Table Utils: Get Rows\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Get Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0snajqt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_11a3ucp\" name=\"Data Table Utils: Get Rows\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9f9d8570-c33f-4f30-ab32-9448c3ff8d67\"\u003e{\"inputs\":{\"2fea7801-9ec6-4f95-812b-31aec2661fca\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"61729b10-cdab-48eb-bc8b-9f30af3afec5\"}}},\"post_processing_script\":\"note_text = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Get Rows\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; search value: {}\\\".format(results[\\\"inputs\\\"][\\\"dt_utils_search_value\\\"])\\n\\nif results[\\\"success\\\"]:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;{}\\\".format(note_text, str(results.content[\\\"rows\\\"]))\\nelse:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;No row found.\\\".format(note_text)\\n\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The number of max rows to return\\nif rule.properties.dt_utils_max_rows:\\n  inputs.dt_utils_max_rows = rule.properties.dt_utils_max_rows\\nelse:\\n  inputs.dt_utils_max_rows = 0\\n\\n# The direction of the sort\\ninputs.dt_utils_sort_direction = rule.properties.dt_utils_sort_direction\\n\\n# The api name of the column to sort by\\nif rule.properties.dt_utils_sort_by:\\n  inputs.dt_utils_sort_by = rule.properties.dt_utils_sort_by\\nelse:\\n  inputs.dt_utils_sort_by = None\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0snajqt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uiq22v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0snajqt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_11a3ucp\"/\u003e\u003cendEvent id=\"EndEvent_134am30\"\u003e\u003cincoming\u003eSequenceFlow_0uiq22v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0uiq22v\" sourceRef=\"ServiceTask_11a3ucp\" targetRef=\"EndEvent_134am30\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19045on\"\u003e\u003ctext\u003eInputs: datatable_api_name, max_rows, sort_by, sort_direction, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1e3e8y5\" sourceRef=\"ServiceTask_11a3ucp\" targetRef=\"TextAnnotation_19045on\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1i7b857\"\u003e\u003ctext\u003eOutput: The Data Table rows\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0366vx4\" sourceRef=\"ServiceTask_11a3ucp\" targetRef=\"TextAnnotation_1i7b857\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"215\" y=\"197\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"210\" y=\"232\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11a3ucp\" id=\"ServiceTask_11a3ucp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"332\" y=\"175\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0snajqt\" id=\"SequenceFlow_0snajqt_di\"\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"332\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"246.5\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19045on\" id=\"TextAnnotation_19045on_di\"\u003e\u003comgdc:Bounds height=\"87\" width=\"125\" x=\"154\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1e3e8y5\" id=\"Association_1e3e8y5_di\"\u003e\u003comgdi:waypoint x=\"332\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"279\" xsi:type=\"omgdc:Point\" y=\"153\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1i7b857\" id=\"TextAnnotation_1i7b857_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"452\" y=\"90\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0366vx4\" id=\"Association_0366vx4_di\"\u003e\u003comgdi:waypoint x=\"424\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_134am30\" id=\"EndEvent_134am30_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"501\" y=\"197\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"474\" y=\"236\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uiq22v\" id=\"SequenceFlow_0uiq22v_di\"\u003e\u003comgdi:waypoint x=\"432\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"501\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"421.5\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example Workflow showing how to use the Data Table Utils: Get Rows Function. It uses an Artifact value to search the Data Table and find rows containing that value and then deletes those rows from the Data Table. The results will be written in an Incident note.",
      "export_key": "example_data_table_utils_get_rows",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091160,
      "name": "Example: Data Table Utils: Get Rows",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_get_rows",
      "tags": [],
      "uuid": "6d10d2f4-78c8-4f66-a0fe-516467d75eb2",
      "workflow_id": 110
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_data_table_utils_get_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_get_row\" isExecutable=\"true\" name=\"Example: Data Table Utils: Get Row\"\u003e\u003cdocumentation\u003eAn example Workflow showing how to use the Data Table Utils: Get Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then returns that row from the Data Table.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1s0htur\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ofe1w4\" name=\"Data Table Utils: Get Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"77e98bdb-2843-4cd6-8294-5a9dbef6a08e\"\u003e{\"inputs\":{},\"post_processing_script\":\"note_text = u\\\"\u0026lt;b\u0026gt;Result from Example: Data Table Utils: Get Row\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt; search value: {}\\\".format(results[\\\"inputs\\\"][\\\"dt_utils_search_value\\\"])\\n\\nif results[\\\"success\\\"]:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;{}\\\".format(note_text, str(results.content[\\\"row\\\"]))\\nelse:\\n  note_text = u\\\"{} \u0026lt;br\u0026gt;No row found.\\\".format(note_text)\\n\\nincident.addNote(helper.createRichText(note_text))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api name to search for\\ninputs.dt_utils_search_column = \\\"dt_col_name\\\"\\n\\n# The cell value to search for\\ninputs.dt_utils_search_value = artifact.value\\n\\n## Alternatively you can get the row by its ID by defining this input:\\n# inputs.dt_utils_row_id = 3\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1s0htur\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1trskjl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1hda6wv\"\u003e\u003cincoming\u003eSequenceFlow_1trskjl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1trskjl\" sourceRef=\"ServiceTask_1ofe1w4\" targetRef=\"EndEvent_1hda6wv\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1s0htur\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ofe1w4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mjy1cb\"\u003e\u003ctext\u003eInputs: data_table_api_name, search_column, search_value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_06hw6vm\" sourceRef=\"ServiceTask_1ofe1w4\" targetRef=\"TextAnnotation_1mjy1cb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0jvzp3u\"\u003e\u003ctext\u003eOutput: the data table row that contains its ID and Cells\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1fgbieg\" sourceRef=\"ServiceTask_1ofe1w4\" targetRef=\"TextAnnotation_0jvzp3u\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"115\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"110\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ofe1w4\" id=\"ServiceTask_1ofe1w4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"276\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1hda6wv\" id=\"EndEvent_1hda6wv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"460\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"478\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1trskjl\" id=\"SequenceFlow_1trskjl_di\"\u003e\u003comgdi:waypoint x=\"376\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"460\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"418\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1s0htur\" id=\"SequenceFlow_1s0htur_di\"\u003e\u003comgdi:waypoint x=\"151\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"168.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mjy1cb\" id=\"TextAnnotation_1mjy1cb_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"143\" x=\"116\" y=\"93\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_06hw6vm\" id=\"Association_06hw6vm_di\"\u003e\u003comgdi:waypoint x=\"276\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"239\" y=\"154\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0jvzp3u\" id=\"TextAnnotation_0jvzp3u_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"149\" x=\"459\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1fgbieg\" id=\"Association_1fgbieg_di\"\u003e\u003comgdi:waypoint x=\"376\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"459\" y=\"150\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example Workflow showing how to use the Data Table Utils: Get Row Function. It uses an Artifact value to search the Data Table and find a row containing that value and then returns that row from the Data Table.",
      "export_key": "example_data_table_utils_get_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1684154322308,
      "name": "Example: Data Table Utils: Get Row",
      "object_type": "artifact",
      "programmatic_name": "example_data_table_utils_get_row",
      "tags": [],
      "uuid": "e6404900-768c-49e3-b5d1-b172d35a2113",
      "workflow_id": 118
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_clear_datatable",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_clear_datatable\" isExecutable=\"true\" name=\"Example: Data Table Utils: Clear Datatable\"\u003e\u003cdocumentation\u003eClear the content of a given datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0stdbd2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ldstqt\" name=\"Data Table Utils: Clear Datatable\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9149563c-8e72-4025-ab71-305cda30dcc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results[\\\"success\\\"]:\\n  incident.addNote(\\\"Data table: {} content has been removed.\\\".format(results[\\\"inputs\\\"][\\\"dt_utils_datatable_api_name\\\"]))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\nif rule.properties.datatable_api_name:\\n  inputs.dt_utils_datatable_api_name = rule.properties.datatable_api_name\\nelse:\\n  # Defaults to example data table\\n  inputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0stdbd2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nbdq3z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0stdbd2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ldstqt\"/\u003e\u003cendEvent id=\"EndEvent_0xr4ong\"\u003e\u003cincoming\u003eSequenceFlow_1nbdq3z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1nbdq3z\" sourceRef=\"ServiceTask_0ldstqt\" targetRef=\"EndEvent_0xr4ong\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ldstqt\" id=\"ServiceTask_0ldstqt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"244\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0stdbd2\" id=\"SequenceFlow_0stdbd2_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"218\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"218\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"244\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"188\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0xr4ong\" id=\"EndEvent_0xr4ong_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"381\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nbdq3z\" id=\"SequenceFlow_1nbdq3z_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"317.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Clear the content of a given datatable.",
      "export_key": "example_data_table_utils_clear_datatable",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278091040,
      "name": "Example: Data Table Utils: Clear Datatable",
      "object_type": "incident",
      "programmatic_name": "example_data_table_utils_clear_datatable",
      "tags": [],
      "uuid": "03b8b37a-897a-4c04-b9c0-76e02c3ca07b",
      "workflow_id": 109
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_data_table_utils_add_row",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"example_data_table_utils_add_row\" isExecutable=\"true\" name=\"Example: Data Table Utils: Add Row\"\u003e\u003cdocumentation\u003eAdd a row to the given datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tn67tf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0eoqu5r\" name=\"Data Table Utils: Add Row\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"88e45595-8f9b-4521-986c-22e53de7abf3\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"import java.util.Date as Date\\n\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, bool, int, nested dicts and lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if not value:\\n      value = False\\n\\n    elif isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(key, value))\\n\\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      entries.append(json_entry.format(key, value))\\n\\n  return \u0027{0} {1} {2}\u0027.format(\u0027{\u0027, \u0027,\u0027.join(entries), \u0027}\u0027)\\n\\n# The ID of this incident\\ninputs.incident_id = incident.id\\n\\n# The api name of the Data Table to update\\ninputs.dt_utils_datatable_api_name = \\\"dt_utils_test_data_table\\\"\\n\\n# The column api names and the value to update the cell to\\n# Example: {\\\"dt_col_name\\\": \\\"example\\\", \\\"number\\\": 1, \\\"text\\\": \\\"example\\\", \\\"datetime\\\": Date().getTime(), \\\"boolean\\\": True, \\\"select\\\": \\\"1\\\", \\\"multi_select\\\": [\\\"a\\\", \\\"b\\\"]}\\ninputs.dt_utils_cells_to_update = dict_to_json_str({\\\"dt_col_name\\\": rule.properties.dt_name_field, \\\"number\\\": rule.properties.dt_number_field, \\\"text\\\": rule.properties.dt_text_field, \\\"datetime\\\": rule.properties.dt_datetime_field, \\\"boolean\\\": rule.properties.dt_boolean_field, \\\"select\\\": rule.properties.dt_select_field, \\\"multi_select\\\": rule.properties.dt_multi_select_field})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tn67tf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_05vqewj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tn67tf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0eoqu5r\"/\u003e\u003cendEvent id=\"EndEvent_00xdvv0\"\u003e\u003cincoming\u003eSequenceFlow_05vqewj\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_05vqewj\" sourceRef=\"ServiceTask_0eoqu5r\" targetRef=\"EndEvent_00xdvv0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0eoqu5r\" id=\"ServiceTask_0eoqu5r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"241\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tn67tf\" id=\"SequenceFlow_1tn67tf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"241\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_00xdvv0\" id=\"EndEvent_00xdvv0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"396\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"414\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_05vqewj\" id=\"SequenceFlow_05vqewj_di\"\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"396\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"368.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Add a row to the given datatable.",
      "export_key": "example_data_table_utils_add_row",
      "last_modified_by": "datatable@ibm.com",
      "last_modified_time": 1683278090814,
      "name": "Example: Data Table Utils: Add Row",
      "object_type": "dt_utils_test_data_table",
      "programmatic_name": "example_data_table_utils_add_row",
      "tags": [],
      "uuid": "de288136-4e9b-4012-927e-eac41be3e60f",
      "workflow_id": 107
    }
  ],
  "workspaces": []
}
