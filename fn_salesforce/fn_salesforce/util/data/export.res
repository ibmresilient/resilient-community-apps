{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1704805272645,
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
      "export_key": "__function/task_sync_direction",
      "hide_notification": false,
      "id": 1637,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "task_sync_direction",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "task_sync_direction",
      "tooltip": "Direction to push tasks",
      "type_id": 11,
      "uuid": "91991ce4-0ef6-488f-9b28-01b99f8fa5c7",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "SOAR",
          "properties": null,
          "uuid": "74078907-7127-4500-bae5-5fe1973e2afd",
          "value": 1361
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Salesforce",
          "properties": null,
          "uuid": "c63e10cb-3517-4b4f-959f-02df04c92bcb",
          "value": 1362
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Both",
          "properties": null,
          "uuid": "326b5d59-3cb1-4de8-8dc2-2aa22e1885ad",
          "value": 1363
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 612,
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
      "uuid": "bee6fc4d-440c-484d-a37e-2090fd8e4eae",
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
      "export_key": "__function/salesforce_case_id",
      "hide_notification": false,
      "id": 1638,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_case_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "cdbb2fab-1d25-4140-8041-14a2c495f262",
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
      "export_key": "__function/artifact_id",
      "hide_notification": false,
      "id": 611,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "cfe97ace-78c6-416d-8feb-db3ec95a53c4",
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
      "export_key": "__function/salesforce_case_comment",
      "hide_notification": false,
      "id": 1639,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_comment",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_case_comment",
      "tooltip": "",
      "type_id": 11,
      "uuid": "d1a65e41-07c4-4c66-bdae-4639739eaa08",
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
      "export_key": "__function/salesforce_task_payload",
      "hide_notification": false,
      "id": 1640,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_task_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_task_payload",
      "tooltip": "task data in json format converted to a string",
      "type_id": 11,
      "uuid": "d98e9ebd-735b-4cf7-bd42-79146545cb9a",
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
      "export_key": "__function/salesforce_user_id",
      "hide_notification": false,
      "id": 1641,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_user_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_user_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "da3dad32-8a0a-4b84-8c82-5ec7a670f27b",
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
      "export_key": "__function/salesforce_comment_text",
      "hide_notification": false,
      "id": 1642,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_comment_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_comment_text",
      "tooltip": "",
      "type_id": 11,
      "uuid": "dcf61b94-b095-4cae-8293-b2c4ee4409e6",
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
      "export_key": "__function/salesforce_contact_id",
      "hide_notification": false,
      "id": 1643,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_contact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "de33f782-0597-4064-a533-91c6e8aec5bd",
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
      "id": 616,
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
      "uuid": "fcf2276c-054e-4f3a-83fa-aaefa06379a7",
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
      "export_key": "__function/salesforce_account_id",
      "hide_notification": false,
      "id": 1644,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_account_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_account_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "351b44c4-e47c-4f63-9486-d584a197d228",
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
      "export_key": "__function/salesforce_case_status",
      "hide_notification": false,
      "id": 1645,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_case_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "66b74c32-5542-4ce2-a18a-aea872d86d5b",
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
      "export_key": "__function/salesforce_case_payload",
      "hide_notification": false,
      "id": 1646,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "salesforce_case_payload",
      "tooltip": "",
      "type_id": 11,
      "uuid": "70f56caf-384e-4a84-81c2-b5a80eda6ad5",
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
      "id": 608,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
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
      "export_key": "incident/salesforce_case_link",
      "hide_notification": false,
      "id": 1618,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Link to Case in Salesforce",
      "tooltip": "",
      "type_id": 0,
      "uuid": "9e051a5f-7235-4956-9f30-c2439c618017",
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
      "export_key": "incident/salesforce_case_owner",
      "hide_notification": false,
      "id": 1619,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_owner",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Owner",
      "tooltip": "",
      "type_id": 0,
      "uuid": "a0539681-abf3-4209-a126-ccca5430b0d3",
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
      "export_key": "incident/salesforce_contact_email",
      "hide_notification": false,
      "id": 1620,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Contact Email",
      "tooltip": "Email address for the contact. The Case.ContactEmail field displays the Email field on the contact that is referenced by Case.ContactId. Label is Contact Email. This field is available in API version 38.0 and later.",
      "type_id": 0,
      "uuid": "b55e10a5-1ae6-4a61-94cb-fcf3373b79f7",
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
      "export_key": "incident/salesforce_contact_phone",
      "hide_notification": false,
      "id": 1621,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_phone",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Contact Phone",
      "tooltip": "Telephone number for the contact. Label is Contact Phone. This field is available in API version 38.0 and later.",
      "type_id": 0,
      "uuid": "c1ea39bb-673a-4259-ba4e-4633c33d0808",
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
      "export_key": "incident/salesforce_account_name",
      "hide_notification": false,
      "id": 1622,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_account_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Account Name",
      "tooltip": "",
      "type_id": 0,
      "uuid": "d7459e7b-edf9-4bd1-a0bf-95fbe679f478",
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
      "export_key": "incident/salesforce_owner_id",
      "hide_notification": false,
      "id": 1623,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_owner_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Owner Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "d9a22595-b270-4bb0-aa0b-00b1c6f9b5d5",
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
      "export_key": "incident/salesforce_case_type",
      "hide_notification": false,
      "id": 1624,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Type",
      "tooltip": "The type of case, such as Feature Request or Question.",
      "type_id": 0,
      "uuid": "e38018c4-3caa-4cad-af91-57d237c18643",
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
      "export_key": "incident/salesforce_contact_id",
      "hide_notification": false,
      "id": 1625,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Contact Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "f29c5b0f-71f8-4753-a629-2960f63caf05",
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
      "export_key": "incident/salesforce_supplied_name",
      "hide_notification": false,
      "id": 1626,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_supplied_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Name",
      "tooltip": "The name that was entered when the case was created. Label is Name.",
      "type_id": 0,
      "uuid": "f4598327-077a-43f6-8142-f16e952c4372",
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
      "export_key": "incident/salesforce_supplied_phone",
      "hide_notification": false,
      "id": 1627,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_supplied_phone",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Phone",
      "tooltip": "The phone number that was entered when the case was created. Label is Phone.",
      "type_id": 0,
      "uuid": "0bd08fbd-5e19-4fd6-9cbe-3e043f997088",
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
      "export_key": "incident/salesforce_case_id",
      "hide_notification": false,
      "id": 1628,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Id",
      "tooltip": "",
      "type_id": 0,
      "uuid": "20b495a6-c3dd-4230-8a81-8b6f57e8e65a",
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
      "export_key": "incident/salesforce_origin",
      "hide_notification": false,
      "id": 1629,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_origin",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Origin",
      "tooltip": "The source of the case, such as Email, Phone, or Web. Label is Case Origin.",
      "type_id": 0,
      "uuid": "230a2d3d-d2d3-486a-8cfe-515014f92ea6",
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
      "export_key": "incident/salesforce_account_id",
      "hide_notification": false,
      "id": 1630,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_account_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Account Id",
      "tooltip": "ID of the account associated with this case. ",
      "type_id": 0,
      "uuid": "27810db1-bf23-493e-9cf3-960b8355b324",
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
      "export_key": "incident/salesforce_supplied_email",
      "hide_notification": false,
      "id": 1631,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_supplied_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Email",
      "tooltip": "The email address that was entered when the case was created. Label is Email.  If your organization has an active auto-response rule, SuppliedEmail is required when creating a case via the API. Auto-response rules use the email in the contact specified by ContactId. If no email address is in the contact record, the email specified here is used.",
      "type_id": 0,
      "uuid": "3414a921-b526-44de-8084-64e95cd91788",
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
      "export_key": "incident/salesforce_contact_name",
      "hide_notification": false,
      "id": 1632,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Contact Name",
      "tooltip": "",
      "type_id": 0,
      "uuid": "38a9b89f-48bf-41fe-b4ab-57eb5dabe3c9",
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
      "export_key": "incident/salesforce_contact_fax",
      "hide_notification": false,
      "id": 1633,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_contact_fax",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Contact FAX",
      "tooltip": "Fax number for the contact. Label is Contact Fax. This field is available in API version 38.0 and later.",
      "type_id": 0,
      "uuid": "3aaef76b-840d-4a29-9de6-600cfb949ddf",
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
      "export_key": "incident/salesforce_status",
      "hide_notification": false,
      "id": 1634,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "63be189d-aeac-44d5-8a7e-6ff703d68026",
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
      "export_key": "incident/salesforce_supplied_company",
      "hide_notification": false,
      "id": 1635,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_supplied_company",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Company",
      "tooltip": "The company name that was entered when the case was created. Label is Company.",
      "type_id": 0,
      "uuid": "7039377c-e0e7-48fd-9895-f2c3144447b8",
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
      "export_key": "incident/salesforce_case_number",
      "hide_notification": false,
      "id": 1636,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "salesforce_case_number",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Case Number",
      "tooltip": "",
      "type_id": 0,
      "uuid": "7427c896-62d8-45c8-b566-a852aa9b93a3",
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
      "created_date": 1704785790576,
      "description": {
        "content": "Add a comment to a Salesforce case.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Add Comment to Salesforce Case",
      "export_key": "salesforce_add_comment_to_salesforce_case",
      "id": 213,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785790744,
      "name": "salesforce_add_comment_to_salesforce_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"salesforce_case_id\": \"500Hr00001X8WykIAF\", \"salesforce_comment_text\": \"Created by IBM SOAR: Case 2357 created in IBM SOAR\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 1824, \"timestamp\": \"2023-07-18 15:29:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_case_id\": {\"type\": \"string\"}, \"salesforce_comment_text\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "c13836c0-4432-4cb3-81ed-146422c3939c",
      "version": 1,
      "view_items": [
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dcf61b94-b095-4cae-8293-b2c4ee4409e6",
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
      "created_date": 1704785790826,
      "description": {
        "content": "Create a Salesforce case in Salesforce using the specified JSON case data.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Create Case in Salesforce",
      "export_key": "salesforce_create_case_in_salesforce",
      "id": 214,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785790999,
      "name": "salesforce_create_case_in_salesforce",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_case\": {\"id\": \"500Hr00001X906jIAB\", \"success\": true, \"errors\": []}}, \"raw\": null, \"inputs\": {\"salesforce_case_data\": \"{\\\"Origin\\\": \\\"Web\\\", \\\"Status\\\": \\\"In Progress\\\", \\\"Description\\\": \\\"My Description\\\", \\\"Subject\\\": \\\"My Subject testing\\\", \\\"Reason\\\": \\\"Installation\\\"}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 12850, \"timestamp\": \"2023-07-20 11:18:51\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_case\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"errors\": {\"type\": \"array\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_case_data\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "74337648-8bfe-4aa6-9cdd-34dd819a2bdd",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70f56caf-384e-4a84-81c2-b5a80eda6ad5",
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
      "created_date": 1704785791051,
      "description": {
        "content": "Create a SOAR task in a Salesforce case.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Create Task in Salesforce Case",
      "export_key": "salesforce_create_task_in_salesforce_case",
      "id": 215,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785791216,
      "name": "salesforce_create_task_in_salesforce_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_task\": {\"id\": \"00THr00008eYnBkMAK\", \"success\": true, \"errors\": []}}, \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"salesforce_case_id\": \"500Hr00001Wthb4IAB\", \"task_id\": 14, \"salesforce_task_data\": \"{\\\"WhatId\\\": \\\"500Hr00001Wthb4IAB\\\", \\\"Description\\\": \\\"Task from IBM SOAR case\\\", \\\"Subject\\\": \\\"Investigate Exposure of Personal Information/Data\\\", \\\"Priority\\\": \\\"Normal\\\", \\\"Status\\\": \\\"In Progress\\\"}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 7112, \"timestamp\": \"2023-08-02 17:17:32\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_task\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"errors\": {\"type\": \"array\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"salesforce_case_id\": {\"type\": \"string\"}, \"task_id\": {\"type\": \"integer\"}, \"salesforce_task_data\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "aa8d86b1-e94d-4906-b175-6889001f67c6",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bee6fc4d-440c-484d-a37e-2090fd8e4eae",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d98e9ebd-735b-4cf7-bd42-79146545cb9a",
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
      "created_date": 1704785791270,
      "description": {
        "content": "Get the Salesforce account information for the specified Salesforce AccountId.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get Account",
      "export_key": "salesforce_get_account",
      "id": 216,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785791442,
      "name": "salesforce_get_account",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_account\": {\"attributes\": {\"type\": \"Account\", \"url\": \"/services/data/v58.0/sobjects/Account/001Hr00001kFBihIAG\"}, \"Id\": \"001Hr00001kFBihIAG\", \"IsDeleted\": false, \"MasterRecordId\": null, \"Name\": \"IBM SOAR\", \"Type\": null, \"ParentId\": null, \"BillingStreet\": null, \"BillingCity\": null, \"BillingState\": null, \"BillingPostalCode\": null, \"BillingCountry\": null, \"BillingLatitude\": null, \"BillingLongitude\": null, \"BillingGeocodeAccuracy\": null, \"BillingAddress\": null, \"ShippingStreet\": null, \"ShippingCity\": null, \"ShippingState\": null, \"ShippingPostalCode\": null, \"ShippingCountry\": null, \"ShippingLatitude\": null, \"ShippingLongitude\": null, \"ShippingGeocodeAccuracy\": null, \"ShippingAddress\": null, \"Phone\": null, \"Fax\": null, \"AccountNumber\": null, \"Website\": null, \"PhotoUrl\": null, \"Sic\": null, \"Industry\": null, \"AnnualRevenue\": null, \"NumberOfEmployees\": null, \"Ownership\": null, \"TickerSymbol\": null, \"Description\": null, \"Rating\": \"Hot\", \"Site\": null, \"OwnerId\": \"005Hr00000COneZIAT\", \"CreatedDate\": \"2023-06-16T18:28:22.000+0000\", \"CreatedById\": \"005Hr00000COneZIAT\", \"LastModifiedDate\": \"2023-06-16T18:28:22.000+0000\", \"LastModifiedById\": \"005Hr00000COneZIAT\", \"SystemModstamp\": \"2023-06-16T18:28:22.000+0000\", \"LastActivityDate\": null, \"LastViewedDate\": \"2023-07-17T19:04:52.000+0000\", \"LastReferencedDate\": \"2023-07-17T19:04:52.000+0000\", \"Jigsaw\": null, \"JigsawCompanyId\": null, \"AccountSource\": null, \"DunsNumber\": null, \"Tradestyle\": null, \"NaicsCode\": null, \"NaicsDesc\": null, \"YearStarted\": null, \"SicDesc\": null, \"DandbCompanyId\": null, \"CustomerPriority__c\": null, \"SLA__c\": null, \"Active__c\": null, \"NumberofLocations__c\": null, \"UpsellOpportunity__c\": null, \"SLASerialNumber__c\": null, \"SLAExpirationDate__c\": null}}, \"raw\": null, \"inputs\": {\"salesforce_account_id\": \"001Hr00001kFBihIAG\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 262, \"timestamp\": \"2023-07-17 15:08:09\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_account\": {\"type\": \"object\", \"properties\": {\"attributes\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}}}, \"Id\": {\"type\": \"string\"}, \"IsDeleted\": {\"type\": \"boolean\"}, \"MasterRecordId\": {}, \"Name\": {\"type\": \"string\"}, \"Type\": {}, \"ParentId\": {}, \"BillingStreet\": {}, \"BillingCity\": {}, \"BillingState\": {}, \"BillingPostalCode\": {}, \"BillingCountry\": {}, \"BillingLatitude\": {}, \"BillingLongitude\": {}, \"BillingGeocodeAccuracy\": {}, \"BillingAddress\": {}, \"ShippingStreet\": {}, \"ShippingCity\": {}, \"ShippingState\": {}, \"ShippingPostalCode\": {}, \"ShippingCountry\": {}, \"ShippingLatitude\": {}, \"ShippingLongitude\": {}, \"ShippingGeocodeAccuracy\": {}, \"ShippingAddress\": {}, \"Phone\": {}, \"Fax\": {}, \"AccountNumber\": {}, \"Website\": {}, \"PhotoUrl\": {}, \"Sic\": {}, \"Industry\": {}, \"AnnualRevenue\": {}, \"NumberOfEmployees\": {}, \"Ownership\": {}, \"TickerSymbol\": {}, \"Description\": {}, \"Rating\": {\"type\": \"string\"}, \"Site\": {}, \"OwnerId\": {\"type\": \"string\"}, \"CreatedDate\": {\"type\": \"string\"}, \"CreatedById\": {\"type\": \"string\"}, \"LastModifiedDate\": {\"type\": \"string\"}, \"LastModifiedById\": {\"type\": \"string\"}, \"SystemModstamp\": {\"type\": \"string\"}, \"LastActivityDate\": {}, \"LastViewedDate\": {\"type\": \"string\"}, \"LastReferencedDate\": {\"type\": \"string\"}, \"Jigsaw\": {}, \"JigsawCompanyId\": {}, \"AccountSource\": {}, \"DunsNumber\": {}, \"Tradestyle\": {}, \"NaicsCode\": {}, \"NaicsDesc\": {}, \"YearStarted\": {}, \"SicDesc\": {}, \"DandbCompanyId\": {}, \"CustomerPriority__c\": {}, \"SLA__c\": {}, \"Active__c\": {}, \"NumberofLocations__c\": {}, \"UpsellOpportunity__c\": {}, \"SLASerialNumber__c\": {}, \"SLAExpirationDate__c\": {}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_account_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "ce27c1d7-8c77-45a4-ba6b-209c79f44192",
      "version": 1,
      "view_items": [
        {
          "content": "351b44c4-e47c-4f63-9486-d584a197d228",
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
      "created_date": 1704785791495,
      "description": {
        "content": "Get attachments associated with a Salesforce case and add the attachments in the corresponding SOAR case.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get Attachments from Salesforce",
      "export_key": "salesforce_get_attachments_from_salesforce",
      "id": 217,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785791673,
      "name": "salesforce_get_attachments_from_salesforce",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_attachments\": [\"test.txt\"]}, \"raw\": null, \"inputs\": {\"incident_id\": 2522, \"salesforce_case_id\": \"500Hr00001X98NnIAJ\", \"task_id\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 6912, \"timestamp\": \"2023-07-25 12:50:08\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_attachments\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"salesforce_case_id\": {\"type\": \"string\"}, \"task_id\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "ae3237f6-af1f-4b0f-a39f-73f35dd3208d",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bee6fc4d-440c-484d-a37e-2090fd8e4eae",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
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
      "created_date": 1704785791734,
      "description": {
        "content": "Get Case information from a specified Salesforce CaseId.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get Case",
      "export_key": "salesforce_get_case",
      "id": 218,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785791912,
      "name": "salesforce_get_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_case\": {\"attributes\": {\"type\": \"Case\", \"url\": \"/services/data/v58.0/sobjects/Case/500Hr00001VhyicIAB\"}, \"Id\": \"500Hr00001VhyicIAB\", \"IsDeleted\": false, \"MasterRecordId\": null, \"CaseNumber\": \"00001064\", \"ContactId\": null, \"AccountId\": \"001Hr00001kFBihIAG\", \"AssetId\": null, \"ParentId\": null, \"SuppliedName\": null, \"SuppliedEmail\": \"user@qradar.dev\", \"SuppliedPhone\": \"444-444-4444\", \"SuppliedCompany\": null, \"Type\": \"Mechanical\", \"Status\": \"New\", \"Reason\": \"Equipment Complexity\", \"Origin\": \"Web\", \"Subject\": \"SOAR Test Case\", \"Priority\": \"Medium\", \"Description\": \"Testing SOAR poller for new cases\", \"IsClosed\": false, \"ClosedDate\": null, \"IsEscalated\": false, \"OwnerId\": \"005Hr00000COneZIAT\", \"CreatedDate\": \"2023-07-07T21:40:12.000+0000\", \"CreatedById\": \"005Hr00000COneZIAT\", \"LastModifiedDate\": \"2023-07-17T19:04:23.000+0000\", \"LastModifiedById\": \"005Hr00000COneZIAT\", \"SystemModstamp\": \"2023-07-17T19:04:23.000+0000\", \"ContactPhone\": null, \"ContactMobile\": null, \"ContactEmail\": null, \"ContactFax\": null, \"Comments\": null, \"LastViewedDate\": \"2023-07-17T19:04:39.000+0000\", \"LastReferencedDate\": \"2023-07-17T19:04:39.000+0000\", \"EngineeringReqNumber__c\": null, \"SLAViolation__c\": null, \"Product__c\": null, \"PotentialLiability__c\": null, \"entity_url\": \"https://dev-ed.develop.lightning.force.com/lightning/r/Case/500Hr00001VhyicIAB/view\"}}, \"raw\": null, \"inputs\": {\"salesforce_case_id\": \"500Hr00001VhyicIAB\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 265, \"timestamp\": \"2023-07-17 15:07:07\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_case\": {\"type\": \"object\", \"properties\": {\"attributes\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}}}, \"Id\": {\"type\": \"string\"}, \"IsDeleted\": {\"type\": \"boolean\"}, \"MasterRecordId\": {}, \"CaseNumber\": {\"type\": \"string\"}, \"ContactId\": {\"type\": \"string\"}, \"AccountId\": {\"type\": \"string\"}, \"AssetId\": {}, \"ParentId\": {}, \"SuppliedName\": {\"type\": \"string\"}, \"SuppliedEmail\": {\"type\": \"string\"}, \"SuppliedPhone\": {\"type\": \"string\"}, \"SuppliedCompany\": {\"type\": \"string\"}, \"Type\": {\"type\": \"string\"}, \"Status\": {\"type\": \"string\"}, \"Reason\": {\"type\": \"string\"}, \"Origin\": {\"type\": \"string\"}, \"Subject\": {}, \"Priority\": {\"type\": \"string\"}, \"Description\": {}, \"IsClosed\": {\"type\": \"boolean\"}, \"ClosedDate\": {}, \"IsEscalated\": {\"type\": \"boolean\"}, \"OwnerId\": {\"type\": \"string\"}, \"CreatedDate\": {\"type\": \"string\"}, \"CreatedById\": {\"type\": \"string\"}, \"LastModifiedDate\": {\"type\": \"string\"}, \"LastModifiedById\": {\"type\": \"string\"}, \"SystemModstamp\": {\"type\": \"string\"}, \"ContactPhone\": {}, \"ContactMobile\": {}, \"ContactEmail\": {}, \"ContactFax\": {}, \"Comments\": {}, \"LastViewedDate\": {\"type\": \"string\"}, \"LastReferencedDate\": {\"type\": \"string\"}, \"EngineeringReqNumber__c\": {}, \"SLAViolation__c\": {}, \"Product__c\": {}, \"PotentialLiability__c\": {}, \"entity_url\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_case_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "055485d3-e8ab-434a-9500-3b8ae61680b2",
      "version": 1,
      "view_items": [
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
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
      "created_date": 1704785791969,
      "description": {
        "content": "Get the comments from the Salesforce case.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get Case Comments",
      "export_key": "salesforce_get_case_comments",
      "id": 219,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785792144,
      "name": "salesforce_get_case_comments",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"count\": 1}, \"raw\": null, \"inputs\": {\"incident_id\": 2312, \"salesforce_case_id\": \"500Hr00001VhyicIAB\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 4220, \"timestamp\": \"2023-07-17 15:09:28\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"count\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"salesforce_case_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "8e4f5ac0-996d-400f-b84d-0e2e5cd9fe4c",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
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
      "created_date": 1704785792223,
      "description": {
        "content": "Get the detailed information on the specified Salesforce Contact, give the ContactId.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get Contact",
      "export_key": "salesforce_get_contact",
      "id": 220,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785792399,
      "name": "salesforce_get_contact",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_contact\": {\"attributes\": {\"type\": \"Contact\", \"url\": \"/services/data/v58.0/sobjects/Contact/003Hr00002REwc8IAD\"}, \"Id\": \"003Hr00002REwc8IAD\", \"IsDeleted\": false, \"MasterRecordId\": null, \"AccountId\": null, \"LastName\": \"Doe\", \"FirstName\": \"John\", \"Salutation\": \"Mr.\", \"Name\": \"John Doe\", \"OtherStreet\": null, \"OtherCity\": null, \"OtherState\": null, \"OtherPostalCode\": null, \"OtherCountry\": null, \"OtherLatitude\": null, \"OtherLongitude\": null, \"OtherGeocodeAccuracy\": null, \"OtherAddress\": null, \"MailingStreet\": null, \"MailingCity\": null, \"MailingState\": null, \"MailingPostalCode\": null, \"MailingCountry\": null, \"MailingLatitude\": null, \"MailingLongitude\": null, \"MailingGeocodeAccuracy\": null, \"MailingAddress\": null, \"Phone\": null, \"Fax\": null, \"MobilePhone\": null, \"HomePhone\": null, \"OtherPhone\": null, \"AssistantPhone\": null, \"ReportsToId\": null, \"Email\": null, \"Title\": null, \"Department\": null, \"AssistantName\": null, \"LeadSource\": null, \"Birthdate\": null, \"Description\": null, \"OwnerId\": \"005Hr00000COneZIAT\", \"CreatedDate\": \"2023-06-16T18:29:41.000+0000\", \"CreatedById\": \"005Hr00000COneZIAT\", \"LastModifiedDate\": \"2023-06-16T18:29:41.000+0000\", \"LastModifiedById\": \"005Hr00000COneZIAT\", \"SystemModstamp\": \"2023-06-16T18:29:41.000+0000\", \"LastActivityDate\": null, \"LastCURequestDate\": null, \"LastCUUpdateDate\": null, \"LastViewedDate\": \"2023-07-17T18:58:39.000+0000\", \"LastReferencedDate\": \"2023-07-17T18:58:39.000+0000\", \"EmailBouncedReason\": null, \"EmailBouncedDate\": null, \"IsEmailBounced\": false, \"PhotoUrl\": null, \"Jigsaw\": null, \"JigsawContactId\": null, \"IndividualId\": null, \"Level__c\": null, \"Languages__c\": null}}, \"raw\": null, \"inputs\": {\"salesforce_contact_id\": \"003Hr00002REwc8IAD\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 308, \"timestamp\": \"2023-07-17 15:04:52\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_contact\": {\"type\": \"object\", \"properties\": {\"attributes\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}}}, \"Id\": {\"type\": \"string\"}, \"IsDeleted\": {\"type\": \"boolean\"}, \"MasterRecordId\": {}, \"AccountId\": {}, \"LastName\": {\"type\": \"string\"}, \"FirstName\": {\"type\": \"string\"}, \"Salutation\": {\"type\": \"string\"}, \"Name\": {\"type\": \"string\"}, \"OtherStreet\": {}, \"OtherCity\": {}, \"OtherState\": {}, \"OtherPostalCode\": {}, \"OtherCountry\": {}, \"OtherLatitude\": {}, \"OtherLongitude\": {}, \"OtherGeocodeAccuracy\": {}, \"OtherAddress\": {}, \"MailingStreet\": {}, \"MailingCity\": {}, \"MailingState\": {}, \"MailingPostalCode\": {}, \"MailingCountry\": {}, \"MailingLatitude\": {}, \"MailingLongitude\": {}, \"MailingGeocodeAccuracy\": {}, \"MailingAddress\": {}, \"Phone\": {}, \"Fax\": {}, \"MobilePhone\": {}, \"HomePhone\": {}, \"OtherPhone\": {}, \"AssistantPhone\": {}, \"ReportsToId\": {}, \"Email\": {}, \"Title\": {}, \"Department\": {}, \"AssistantName\": {}, \"LeadSource\": {}, \"Birthdate\": {}, \"Description\": {}, \"OwnerId\": {\"type\": \"string\"}, \"CreatedDate\": {\"type\": \"string\"}, \"CreatedById\": {\"type\": \"string\"}, \"LastModifiedDate\": {\"type\": \"string\"}, \"LastModifiedById\": {\"type\": \"string\"}, \"SystemModstamp\": {\"type\": \"string\"}, \"LastActivityDate\": {}, \"LastCURequestDate\": {}, \"LastCUUpdateDate\": {}, \"LastViewedDate\": {\"type\": \"string\"}, \"LastReferencedDate\": {\"type\": \"string\"}, \"EmailBouncedReason\": {}, \"EmailBouncedDate\": {}, \"IsEmailBounced\": {\"type\": \"boolean\"}, \"PhotoUrl\": {}, \"Jigsaw\": {}, \"JigsawContactId\": {}, \"IndividualId\": {}, \"Level__c\": {}, \"Languages__c\": {}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_contact_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "777154b4-dc0c-4d8d-ac3b-7a3cd9523255",
      "version": 1,
      "view_items": [
        {
          "content": "de33f782-0597-4064-a533-91c6e8aec5bd",
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
      "created_date": 1704785792453,
      "description": {
        "content": "Get the detailed information of a Salesforce User, given the UserId.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Get User",
      "export_key": "salesforce_get_user",
      "id": 221,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785792620,
      "name": "salesforce_get_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_user\": {\"attributes\": {\"type\": \"User\", \"url\": \"/services/data/v58.0/sobjects/User/005Hr00000COneZIAT\"}, \"Id\": \"005Hr00000COneZIAT\", \"Username\": \"user@qradar.dev\", \"LastName\": \"MyLastName\", \"FirstName\": \"Joe\", \"Name\": \"Joe MyLastName\", \"CompanyName\": null, \"Division\": null, \"Department\": null, \"Title\": null, \"Street\": null, \"City\": null, \"State\": null, \"PostalCode\": null, \"Country\": null, \"Latitude\": null, \"Longitude\": null, \"GeocodeAccuracy\": null, \"Address\": null, \"Email\": \"user@example.com\", \"EmailPreferencesAutoBcc\": true, \"EmailPreferencesAutoBccStayInTouch\": false, \"EmailPreferencesStayInTouchReminder\": true, \"SenderEmail\": null, \"SenderName\": null, \"Signature\": null, \"StayInTouchSubject\": null, \"StayInTouchSignature\": null, \"StayInTouchNote\": null, \"Phone\": null, \"Fax\": null, \"MobilePhone\": null, \"Alias\": \"anorc\", \"CommunityNickname\": \"User1686331325735812\", \"BadgeText\": \"\", \"IsActive\": true, \"TimeZoneSidKey\": \"America/Los_Angeles\", \"UserRoleId\": \"00EHr000002MWZLMA4\", \"LocaleSidKey\": \"en_US\", \"ReceivesInfoEmails\": true, \"ReceivesAdminInfoEmails\": true, \"EmailEncodingKey\": \"UTF-8\", \"ProfileId\": \"00eHr000001gfgwIAA\", \"UserType\": \"Standard\", \"LanguageLocaleKey\": \"en_US\", \"EmployeeNumber\": null, \"DelegatedApproverId\": null, \"ManagerId\": null, \"LastLoginDate\": \"2023-07-18T20:46:26.000+0000\", \"LastPasswordChangeDate\": \"2023-07-06T12:55:58.000+0000\", \"CreatedDate\": \"2023-06-09T17:22:47.000+0000\", \"CreatedById\": \"005Hr00000COnUsIAL\", \"LastModifiedDate\": \"2023-07-11T18:40:31.000+0000\", \"LastModifiedById\": \"005Hr00000COneZIAT\", \"SystemModstamp\": \"2023-07-17T15:13:07.000+0000\", \"NumberOfFailedLogins\": 0, \"OfflineTrialExpirationDate\": null, \"OfflinePdaTrialExpirationDate\": null, \"UserPermissionsMarketingUser\": false, \"UserPermissionsOfflineUser\": false, \"UserPermissionsCallCenterAutoLogin\": false, \"UserPermissionsSFContentUser\": true, \"UserPermissionsKnowledgeUser\": false, \"UserPermissionsInteractionUser\": false, \"UserPermissionsSupportUser\": false, \"UserPermissionsJigsawProspectingUser\": false, \"UserPermissionsLiveAgentUser\": false, \"UserPermissionsSiteforceContributorUser\": false, \"UserPermissionsSiteforcePublisherUser\": false, \"UserPermissionsWorkDotComUserFeature\": false, \"ForecastEnabled\": false, \"UserPreferencesActivityRemindersPopup\": true, \"UserPreferencesEventRemindersCheckboxDefault\": true, \"UserPreferencesTaskRemindersCheckboxDefault\": true, \"UserPreferencesReminderSoundOff\": false, \"UserPreferencesDisableAllFeedsEmail\": false, \"UserPreferencesContentNoEmail\": false, \"UserPreferencesContentEmailAsAndWhen\": false, \"UserPreferencesApexPagesDeveloperMode\": false, \"UserPreferencesReceiveNoNotificationsAsApprover\": false, \"UserPreferencesReceiveNotificationsAsDelegatedApprover\": false, \"UserPreferencesHideCSNGetChatterMobileTask\": false, \"UserPreferencesHideCSNDesktopTask\": false, \"UserPreferencesHideChatterOnboardingSplash\": false, \"UserPreferencesHideSecondChatterOnboardingSplash\": false, \"UserPreferencesJigsawListUser\": false, \"UserPreferencesShowTitleToExternalUsers\": true, \"UserPreferencesShowManagerToExternalUsers\": false, \"UserPreferencesShowEmailToExternalUsers\": false, \"UserPreferencesShowWorkPhoneToExternalUsers\": false, \"UserPreferencesShowMobilePhoneToExternalUsers\": false, \"UserPreferencesShowFaxToExternalUsers\": false, \"UserPreferencesShowStreetAddressToExternalUsers\": false, \"UserPreferencesShowCityToExternalUsers\": false, \"UserPreferencesShowStateToExternalUsers\": false, \"UserPreferencesShowPostalCodeToExternalUsers\": false, \"UserPreferencesShowCountryToExternalUsers\": false, \"UserPreferencesShowProfilePicToGuestUsers\": false, \"UserPreferencesShowTitleToGuestUsers\": false, \"UserPreferencesShowCityToGuestUsers\": false, \"UserPreferencesShowStateToGuestUsers\": false, \"UserPreferencesShowPostalCodeToGuestUsers\": false, \"UserPreferencesShowCountryToGuestUsers\": false, \"UserPreferencesShowForecastingChangeSignals\": false, \"UserPreferencesHideS1BrowserUI\": true, \"UserPreferencesPathAssistantCollapsed\": false, \"UserPreferencesCacheDiagnostics\": false, \"UserPreferencesShowEmailToGuestUsers\": false, \"UserPreferencesShowManagerToGuestUsers\": false, \"UserPreferencesShowWorkPhoneToGuestUsers\": false, \"UserPreferencesShowMobilePhoneToGuestUsers\": false, \"UserPreferencesShowFaxToGuestUsers\": false, \"UserPreferencesShowStreetAddressToGuestUsers\": false, \"UserPreferencesLightningExperiencePreferred\": true, \"UserPreferencesPreviewLightning\": false, \"UserPreferencesHideEndUserOnboardingAssistantModal\": false, \"UserPreferencesHideLightningMigrationModal\": false, \"UserPreferencesHideSfxWelcomeMat\": true, \"UserPreferencesHideBiggerPhotoCallout\": false, \"UserPreferencesGlobalNavBarWTShown\": false, \"UserPreferencesGlobalNavGridMenuWTShown\": false, \"UserPreferencesCreateLEXAppsWTShown\": false, \"UserPreferencesFavoritesWTShown\": false, \"UserPreferencesRecordHomeSectionCollapseWTShown\": false, \"UserPreferencesRecordHomeReservedWTShown\": false, \"UserPreferencesFavoritesShowTopFavorites\": false, \"UserPreferencesExcludeMailAppAttachments\": false, \"UserPreferencesSuppressTaskSFXReminders\": false, \"UserPreferencesSuppressEventSFXReminders\": false, \"UserPreferencesPreviewCustomTheme\": false, \"UserPreferencesHasCelebrationBadge\": false, \"UserPreferencesUserDebugModePref\": false, \"UserPreferencesSRHOverrideActivities\": false, \"UserPreferencesNewLightningReportRunPageEnabled\": false, \"UserPreferencesReverseOpenActivitiesView\": false, \"UserPreferencesHasSentWarningEmail\": false, \"UserPreferencesHasSentWarningEmail238\": false, \"UserPreferencesHasSentWarningEmail240\": false, \"UserPreferencesNativeEmailClient\": false, \"ContactId\": null, \"AccountId\": null, \"CallCenterId\": null, \"Extension\": null, \"FederationIdentifier\": null, \"AboutMe\": null, \"FullPhotoUrl\": \"https://ibmc4s-qradar-dev-dev-ed.develop.file.force.com/profilephoto/005/F\", \"SmallPhotoUrl\": \"https://ibmc4s-qradar-dev-dev-ed.develop.file.force.com/profilephoto/005/T\", \"IsExtIndicatorVisible\": false, \"OutOfOfficeMessage\": \"\", \"MediumPhotoUrl\": \"https://ibmc4s-qradar-dev-dev-ed.develop.file.force.com/profilephoto/005/M\", \"DigestFrequency\": \"D\", \"DefaultGroupNotificationFrequency\": \"D\", \"JigsawImportLimitOverride\": 300, \"LastViewedDate\": \"2023-07-18T20:46:37.000+0000\", \"LastReferencedDate\": \"2023-07-18T20:46:37.000+0000\", \"BannerPhotoUrl\": \"/profilephoto/005/B\", \"SmallBannerPhotoUrl\": \"/profilephoto/005/D\", \"MediumBannerPhotoUrl\": \"/profilephoto/005/E\", \"IsProfilePhotoActive\": false, \"IndividualId\": null}}, \"raw\": null, \"inputs\": {\"salesforce_user_id\": \"005Hr00000COneZIAT\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 225, \"timestamp\": \"2023-07-18 16:46:43\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_user\": {\"type\": \"object\", \"properties\": {\"attributes\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}}}, \"Id\": {\"type\": \"string\"}, \"Username\": {\"type\": \"string\"}, \"LastName\": {\"type\": \"string\"}, \"FirstName\": {\"type\": \"string\"}, \"Name\": {\"type\": \"string\"}, \"CompanyName\": {}, \"Division\": {}, \"Department\": {}, \"Title\": {}, \"Street\": {}, \"City\": {}, \"State\": {}, \"PostalCode\": {}, \"Country\": {}, \"Latitude\": {}, \"Longitude\": {}, \"GeocodeAccuracy\": {}, \"Address\": {}, \"Email\": {\"type\": \"string\"}, \"EmailPreferencesAutoBcc\": {\"type\": \"boolean\"}, \"EmailPreferencesAutoBccStayInTouch\": {\"type\": \"boolean\"}, \"EmailPreferencesStayInTouchReminder\": {\"type\": \"boolean\"}, \"SenderEmail\": {}, \"SenderName\": {}, \"Signature\": {}, \"StayInTouchSubject\": {}, \"StayInTouchSignature\": {}, \"StayInTouchNote\": {}, \"Phone\": {}, \"Fax\": {}, \"MobilePhone\": {}, \"Alias\": {\"type\": \"string\"}, \"CommunityNickname\": {\"type\": \"string\"}, \"BadgeText\": {\"type\": \"string\"}, \"IsActive\": {\"type\": \"boolean\"}, \"TimeZoneSidKey\": {\"type\": \"string\"}, \"UserRoleId\": {\"type\": \"string\"}, \"LocaleSidKey\": {\"type\": \"string\"}, \"ReceivesInfoEmails\": {\"type\": \"boolean\"}, \"ReceivesAdminInfoEmails\": {\"type\": \"boolean\"}, \"EmailEncodingKey\": {\"type\": \"string\"}, \"ProfileId\": {\"type\": \"string\"}, \"UserType\": {\"type\": \"string\"}, \"LanguageLocaleKey\": {\"type\": \"string\"}, \"EmployeeNumber\": {}, \"DelegatedApproverId\": {}, \"ManagerId\": {}, \"LastLoginDate\": {\"type\": \"string\"}, \"LastPasswordChangeDate\": {\"type\": \"string\"}, \"CreatedDate\": {\"type\": \"string\"}, \"CreatedById\": {\"type\": \"string\"}, \"LastModifiedDate\": {\"type\": \"string\"}, \"LastModifiedById\": {\"type\": \"string\"}, \"SystemModstamp\": {\"type\": \"string\"}, \"NumberOfFailedLogins\": {\"type\": \"integer\"}, \"OfflineTrialExpirationDate\": {}, \"OfflinePdaTrialExpirationDate\": {}, \"UserPermissionsMarketingUser\": {\"type\": \"boolean\"}, \"UserPermissionsOfflineUser\": {\"type\": \"boolean\"}, \"UserPermissionsCallCenterAutoLogin\": {\"type\": \"boolean\"}, \"UserPermissionsSFContentUser\": {\"type\": \"boolean\"}, \"UserPermissionsKnowledgeUser\": {\"type\": \"boolean\"}, \"UserPermissionsInteractionUser\": {\"type\": \"boolean\"}, \"UserPermissionsSupportUser\": {\"type\": \"boolean\"}, \"UserPermissionsJigsawProspectingUser\": {\"type\": \"boolean\"}, \"UserPermissionsLiveAgentUser\": {\"type\": \"boolean\"}, \"UserPermissionsSiteforceContributorUser\": {\"type\": \"boolean\"}, \"UserPermissionsSiteforcePublisherUser\": {\"type\": \"boolean\"}, \"UserPermissionsWorkDotComUserFeature\": {\"type\": \"boolean\"}, \"ForecastEnabled\": {\"type\": \"boolean\"}, \"UserPreferencesActivityRemindersPopup\": {\"type\": \"boolean\"}, \"UserPreferencesEventRemindersCheckboxDefault\": {\"type\": \"boolean\"}, \"UserPreferencesTaskRemindersCheckboxDefault\": {\"type\": \"boolean\"}, \"UserPreferencesReminderSoundOff\": {\"type\": \"boolean\"}, \"UserPreferencesDisableAllFeedsEmail\": {\"type\": \"boolean\"}, \"UserPreferencesContentNoEmail\": {\"type\": \"boolean\"}, \"UserPreferencesContentEmailAsAndWhen\": {\"type\": \"boolean\"}, \"UserPreferencesApexPagesDeveloperMode\": {\"type\": \"boolean\"}, \"UserPreferencesReceiveNoNotificationsAsApprover\": {\"type\": \"boolean\"}, \"UserPreferencesReceiveNotificationsAsDelegatedApprover\": {\"type\": \"boolean\"}, \"UserPreferencesHideCSNGetChatterMobileTask\": {\"type\": \"boolean\"}, \"UserPreferencesHideCSNDesktopTask\": {\"type\": \"boolean\"}, \"UserPreferencesHideChatterOnboardingSplash\": {\"type\": \"boolean\"}, \"UserPreferencesHideSecondChatterOnboardingSplash\": {\"type\": \"boolean\"}, \"UserPreferencesJigsawListUser\": {\"type\": \"boolean\"}, \"UserPreferencesShowTitleToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowManagerToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowEmailToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowWorkPhoneToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowMobilePhoneToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowFaxToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowStreetAddressToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowCityToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowStateToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowPostalCodeToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowCountryToExternalUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowProfilePicToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowTitleToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowCityToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowStateToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowPostalCodeToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowCountryToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowForecastingChangeSignals\": {\"type\": \"boolean\"}, \"UserPreferencesHideS1BrowserUI\": {\"type\": \"boolean\"}, \"UserPreferencesPathAssistantCollapsed\": {\"type\": \"boolean\"}, \"UserPreferencesCacheDiagnostics\": {\"type\": \"boolean\"}, \"UserPreferencesShowEmailToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowManagerToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowWorkPhoneToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowMobilePhoneToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowFaxToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesShowStreetAddressToGuestUsers\": {\"type\": \"boolean\"}, \"UserPreferencesLightningExperiencePreferred\": {\"type\": \"boolean\"}, \"UserPreferencesPreviewLightning\": {\"type\": \"boolean\"}, \"UserPreferencesHideEndUserOnboardingAssistantModal\": {\"type\": \"boolean\"}, \"UserPreferencesHideLightningMigrationModal\": {\"type\": \"boolean\"}, \"UserPreferencesHideSfxWelcomeMat\": {\"type\": \"boolean\"}, \"UserPreferencesHideBiggerPhotoCallout\": {\"type\": \"boolean\"}, \"UserPreferencesGlobalNavBarWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesGlobalNavGridMenuWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesCreateLEXAppsWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesFavoritesWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesRecordHomeSectionCollapseWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesRecordHomeReservedWTShown\": {\"type\": \"boolean\"}, \"UserPreferencesFavoritesShowTopFavorites\": {\"type\": \"boolean\"}, \"UserPreferencesExcludeMailAppAttachments\": {\"type\": \"boolean\"}, \"UserPreferencesSuppressTaskSFXReminders\": {\"type\": \"boolean\"}, \"UserPreferencesSuppressEventSFXReminders\": {\"type\": \"boolean\"}, \"UserPreferencesPreviewCustomTheme\": {\"type\": \"boolean\"}, \"UserPreferencesHasCelebrationBadge\": {\"type\": \"boolean\"}, \"UserPreferencesUserDebugModePref\": {\"type\": \"boolean\"}, \"UserPreferencesSRHOverrideActivities\": {\"type\": \"boolean\"}, \"UserPreferencesNewLightningReportRunPageEnabled\": {\"type\": \"boolean\"}, \"UserPreferencesReverseOpenActivitiesView\": {\"type\": \"boolean\"}, \"UserPreferencesHasSentWarningEmail\": {\"type\": \"boolean\"}, \"UserPreferencesHasSentWarningEmail238\": {\"type\": \"boolean\"}, \"UserPreferencesHasSentWarningEmail240\": {\"type\": \"boolean\"}, \"UserPreferencesNativeEmailClient\": {\"type\": \"boolean\"}, \"ContactId\": {}, \"AccountId\": {}, \"CallCenterId\": {}, \"Extension\": {}, \"FederationIdentifier\": {}, \"AboutMe\": {}, \"FullPhotoUrl\": {\"type\": \"string\"}, \"SmallPhotoUrl\": {\"type\": \"string\"}, \"IsExtIndicatorVisible\": {\"type\": \"boolean\"}, \"OutOfOfficeMessage\": {\"type\": \"string\"}, \"MediumPhotoUrl\": {\"type\": \"string\"}, \"DigestFrequency\": {\"type\": \"string\"}, \"DefaultGroupNotificationFrequency\": {\"type\": \"string\"}, \"JigsawImportLimitOverride\": {\"type\": \"integer\"}, \"LastViewedDate\": {\"type\": \"string\"}, \"LastReferencedDate\": {\"type\": \"string\"}, \"BannerPhotoUrl\": {\"type\": \"string\"}, \"SmallBannerPhotoUrl\": {\"type\": \"string\"}, \"MediumBannerPhotoUrl\": {\"type\": \"string\"}, \"IsProfilePhotoActive\": {\"type\": \"boolean\"}, \"IndividualId\": {}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_user_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "e7bafb91-836b-4aa4-b8b9-1b167d9fc96b",
      "version": 1,
      "view_items": [
        {
          "content": "da3dad32-8a0a-4b84-8c82-5ec7a670f27b",
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
      "created_date": 1704785792673,
      "description": {
        "content": "Post the SOAR attachment to the corresponding Case in Salesforce.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Post Attachment to Salesforce Case",
      "export_key": "salesforce_post_attachment_to_salesforce_case",
      "id": 222,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785792846,
      "name": "salesforce_post_attachment_to_salesforce_case",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"salesforce_attachment\": \"temp.txt\", \"content_document_link\": {\"id\": \"06AHr00000R0Rl0MAF\", \"success\": true, \"errors\": []}}, \"raw\": null, \"inputs\": {\"incident_id\": 2522, \"salesforce_case_id\": \"500Hr00001X98NnIAJ\", \"attachment_id\": 50, \"task_id\": null, \"artifact_id\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 13321, \"timestamp\": \"2023-07-25 16:15:49\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"salesforce_attachment\": {\"type\": \"string\"}, \"content_document_link\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"errors\": {\"type\": \"array\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"salesforce_case_id\": {\"type\": \"string\"}, \"attachment_id\": {\"type\": \"integer\"}, \"task_id\": {}, \"artifact_id\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "ecdac742-4e8a-4b9e-9ec9-4734d48ab62d",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fcf2276c-054e-4f3a-83fa-aaefa06379a7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bee6fc4d-440c-484d-a37e-2090fd8e4eae",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cfe97ace-78c6-416d-8feb-db3ec95a53c4",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
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
      "created_date": 1704785792903,
      "description": {
        "content": "Synchronize tasks between Salesforce case and SOAR case. If the SOAR case name matches the Salesforce case Subject and the Description field contains the SOAR header text (indicating it was already sent from SOAR), then the task is not sent to Salesforce.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Sync Tasks Between Cases",
      "export_key": "salesforce_sync_tasks_between_cases",
      "id": 223,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785793074,
      "name": "salesforce_sync_tasks_between_cases",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"task_count_to_salesforce\": 1, \"task_count_to_soar\": 0}, \"raw\": null, \"inputs\": {\"task_sync_direction\": \"Salesforce\", \"incident_id\": 2199, \"salesforce_case_id\": \"500Hr00001Wu3EtIAJ\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"MacBook-Pro.local\", \"execution_time_ms\": 914, \"timestamp\": \"2023-08-08 16:12:06\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"task_count_to_salesforce\": {\"type\": \"integer\"}, \"task_count_to_soar\": {\"type\": \"integer\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"task_sync_direction\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"salesforce_case_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "f9907018-0770-4e2c-9620-cb623b5a43f1",
      "version": 1,
      "view_items": [
        {
          "content": "780d2cdb-f5d8-4be5-81d6-93927c72eb34",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "91991ce4-0ef6-488f-9b28-01b99f8fa5c7",
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
      "created_date": 1704785793126,
      "description": {
        "content": "Update the Status field of a case in Salesforce.",
        "format": "text"
      },
      "destination_handle": "fn_salesforce",
      "display_name": "Salesforce: Update Case Status",
      "export_key": "salesforce_update_case_status",
      "id": 224,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785793289,
      "name": "salesforce_update_case_status",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"salesforce_case_id\": \"500Hr00001X8WykIAF\", \"salesforce_case_status\": \"Working\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-salesforce\", \"package_version\": \"1.0.0\", \"host\": \"My-MBP\", \"execution_time_ms\": 8467, \"timestamp\": \"2023-07-14 12:43:49\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"salesforce_case_id\": {\"type\": \"string\"}, \"salesforce_case_status\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "5639e9ca-ac5f-421e-9f87-5d9638a8cf67",
      "version": 1,
      "view_items": [
        {
          "content": "cdbb2fab-1d25-4140-8041-14a2c495f262",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66b74c32-5542-4ce2-a18a-aea872d86d5b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d1a65e41-07c4-4c66-bdae-4639739eaa08",
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
  "id": 101,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1704805269753,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1704805269753,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "38a77888-d751-4bcd-ab75-2dc1c168b5b2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_salesforce",
      "name": "Salesforce",
      "programmatic_name": "fn_salesforce",
      "tags": [],
      "users": [],
      "uuid": "12093dd1-73b0-4f43-b97a-3d8505db408e"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
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
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7e933741_7c74_4711_96d7_0b8d31d67343\" isExecutable=\"true\" name=\"playbook_7e933741_7c74_4711_96d7_0b8d31d67343\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0id8d9e\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_0id8d9e\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_3\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_17fsmpd\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Salesforce: Get Case Comments\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8e4f5ac0-996d-400f-b84d-0e2e5cd9fe4c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_comment_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0id8d9e\u003c/incoming\u003e\u003coutgoing\u003eFlow_0he6g1o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0he6g1o\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Salesforce: Check function results to add Salesforce comments to case\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"202e8dcc-9ab8-41ef-be29-9acbdc5a7a0c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0he6g1o\u003c/incoming\u003e\u003coutgoing\u003eFlow_17fsmpd\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_17fsmpd\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7e933741_7c74_4711_96d7_0b8d31d67343\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17fsmpd\" id=\"Flow_17fsmpd_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0he6g1o\" id=\"Flow_0he6g1o_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0id8d9e\" id=\"Flow_0id8d9e_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"167.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"307.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785794141,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7e933741_7c74_4711_96d7_0b8d31d67343",
      "description": {
        "content": "Add the specified text as a comment to the specified case.",
        "format": "text"
      },
      "display_name": "Salesforce: Add Comment to Salesforce Case",
      "export_key": "salesforce_add_comment_to_salesforce_case",
      "field_type_handle": "playbook_7e933741_7c74_4711_96d7_0b8d31d67343",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Add Comment to Salesforce Case",
        "export_key": "playbook_7e933741_7c74_4711_96d7_0b8d31d67343",
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
        "type_name": "playbook_7e933741_7c74_4711_96d7_0b8d31d67343",
        "uuid": "2199389d-ea89-4a13-9a29-d844022fe548"
      },
      "has_logical_errors": false,
      "id": 115,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785795195,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785794365,
          "description": "Check the status of function to add new comments to case",
          "enabled": false,
          "export_key": "Salesforce: Check function results to add Salesforce comments to case",
          "id": 92,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785794419,
          "name": "Salesforce: Check function results to add Salesforce comments to case",
          "object_type": "incident",
          "playbook_handle": "salesforce_add_comment_to_salesforce_case",
          "programmatic_name": "salesforce_add_comment_to_salesforce_case_salesforce_check_function_results_to_add_salesforce_comments_to_case",
          "script_text": "results  = playbook.functions.results.get_comment_results\n\nif results.success:\n  incident.addNote(\"Salesforce: automatic playbook added {} notes from Salesforce\".format(results.content.count))\nelse:\n  incident.addNote(\"Salesforce: ERROR in automatic playbook to get Salesforce case comments - function not successful.\")",
          "tags": [],
          "uuid": "202e8dcc-9ab8-41ef-be29-9acbdc5a7a0c"
        }
      ],
      "name": "salesforce_add_comment_to_salesforce_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7e933741-7c74-4711-96d7-0b8d31d67343",
        "id": 132,
        "name": "playbook_7e933741_7c74_4711_96d7_0b8d31d67343",
        "type": "playbook",
        "uuid": "f47a277b-c5cf-482c-a8e3-72c73f06cc82"
      },
      "tags": [],
      "type": "default",
      "uuid": "7e933741-7c74-4711-96d7-0b8d31d67343",
      "version": 4
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.resolution_id",
              "method": "changed",
              "type": null,
              "value": null
            },
            {
              "evaluation_id": null,
              "field_name": "incident.resolution_summary",
              "method": "not_contains",
              "type": null,
              "value": "Closed by Salesforce"
            }
          ],
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb\" isExecutable=\"true\" name=\"playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0scl7xm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Update Case Status\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5639e9ca-ac5f-421e-9f87-5d9638a8cf67\"\u003e{\"inputs\":{},\"pre_processing_script\":\"STATUS_LOOKUP = {\\n  \\\"Unresolved\\\": \\\"Closed\\\",   # Unresolved\\n  \\\"Duplicate\\\": \\\"Closed\\\",    # Duplicate\\n  \\\"Not an Issue\\\": \\\"Closed\\\", # Not an Issue\\n  \\\"Resolved\\\": \\\"Closed\\\"      # Resolved\\n}\\n\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.salesforce_case_comment = incident.resolution_summary.content\\ninputs.salesforce_case_status = STATUS_LOOKUP.get(incident.resolution_id, \\\"Closed\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_status\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0scl7xm\u003c/incoming\u003e\u003coutgoing\u003eFlow_1x8452o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0scl7xm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update Case Status\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e74dd1e7-b78d-4729-9a9f-e36b755f864a\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1x8452o\u003c/incoming\u003e\u003coutgoing\u003eFlow_0sl4qha\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1x8452o\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0sl4qha\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0sl4qha\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0sl4qha\" id=\"Flow_0sl4qha_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1x8452o\" id=\"Flow_1x8452o_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0scl7xm\" id=\"Flow_0scl7xm_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785795143,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb",
      "description": {
        "content": "Automatic playbook to close a case in Salesforce. ",
        "format": "text"
      },
      "display_name": "Salesforce: Close Case",
      "export_key": "salesforce_close_case",
      "field_type_handle": "playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Close Case",
        "export_key": "playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb",
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
        "type_name": "playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb",
        "uuid": "1e677377-3a07-4b7e-8bca-ed277a5dfdfb"
      },
      "has_logical_errors": false,
      "id": 116,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785796195,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785795367,
          "description": "",
          "enabled": false,
          "export_key": "Salesforce: Update Case Status",
          "id": 93,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785795448,
          "name": "Salesforce: Update Case Status",
          "object_type": "incident",
          "playbook_handle": "salesforce_close_case",
          "programmatic_name": "salesforce_close_case_salesforce_update_case_status",
          "script_text": "update_status = playbook.functions.results.update_status\n\nif not update_status.success:\n  incident.addNote(\"ERROR: unable to update case status in Salesforce\")\nelse:\n  incident.properties.salesforce_status = update_status.inputs.salesforce_case_status\n  incident.addNote(\"Case closed in IBM SOAR by playbook \u0027Salesforce: Close Case\u0027\")",
          "tags": [],
          "uuid": "e74dd1e7-b78d-4729-9a9f-e36b755f864a"
        }
      ],
      "name": "salesforce_close_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_bb44618a-c4be-47fe-a367-2f8bcdd5fbeb",
        "id": 133,
        "name": "playbook_bb44618a_c4be_47fe_a367_2f8bcdd5fbeb",
        "type": "playbook",
        "uuid": "521b3aad-31ee-49d4-b6ba-5a84abfb3048"
      },
      "tags": [],
      "type": "default",
      "uuid": "bb44618a-c4be-47fe-a367-2f8bcdd5fbeb",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa\" isExecutable=\"true\" name=\"playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_09qrncb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Create Case in Salesforce\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74337648-8bfe-4aa6-9cdd-34dd819a2bdd\"\u003e{\"inputs\":{},\"pre_processing_script\":\"import json\\n\\n# Form the payload from input in the activation form and custom fields to create a Salesforce case from SOAR. \\ncase_json = {}\\ncase_json[\u0027Origin\u0027] = \\\"Web\\\"\\n\\nif playbook.inputs.salesforce_case_status:\\n  case_json[\u0027Status\u0027] = playbook.inputs.salesforce_case_status\\nelse: \\n  case_json[\u0027Status\u0027] = \\\"New\\\"\\n  \\nif playbook.inputs.salesforce_case_type:\\n  case_json[\u0027Type\u0027] = playbook.inputs.salesforce_case_type\\n  \\nif playbook.inputs.salesforce_case_description:\\n  case_json[\u0027Description\u0027] = playbook.inputs.salesforce_case_description\\n\\nif playbook.inputs.salesforce_case_subject:\\n  case_json[\u0027Subject\u0027] = playbook.inputs.salesforce_case_subject\\n\\nif playbook.inputs.salesforce_case_internal_comments:\\n  case_json[\u0027Comments\u0027] = playbook.inputs.salesforce_case_internal_comments\\n\\nif incident.properties.salesforce_account_id and incident.properties.salesforce_account_id.lower() != \\\"none\\\":\\n  case_json[\u0027AccountId\u0027] = incident.properties.salesforce_account_id\\n\\nif incident.properties.salesforce_owner_id and incident.properties.salesforce_owner_id.lower() != \\\"none\\\":\\n  case_json[\u0027OwnerId\u0027] = incident.properties.salesforce_owner_id\\n  \\nif incident.properties.salesforce_contact_id and incident.properties.salesforce_contact_id.lower() != \\\"none\\\":\\n  case_json[\u0027ContactId\u0027] = incident.properties.salesforce_contact_id\\n  \\ninputs.salesforce_case_payload = json.dumps(case_json)\\ninputs.incident_id = incident.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_salesforce_case_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09qrncb\u003c/incoming\u003e\u003coutgoing\u003eFlow_0eyyvr2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09qrncb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write results of Create Salesforce Case function\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"295aaaa0-6cc9-4e54-b426-8bf585223f67\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0eyyvr2\u003c/incoming\u003e\u003coutgoing\u003eFlow_1dmb1fs\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0eyyvr2\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0g3b0di\u003c/incoming\u003e\u003cincoming\u003eFlow_1etib8x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1dmb1fs\" sourceRef=\"ScriptTask_2\" targetRef=\"ConditionPoint_4\"/\u003e\u003cexclusiveGateway default=\"Flow_0g3b0di\" id=\"ConditionPoint_4\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1dmb1fs\u003c/incoming\u003e\u003coutgoing\u003eFlow_0f72l4g\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0g3b0di\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"Salesforce: Sync Tasks Between Cases\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f9907018-0770-4e2c-9620-cb623b5a43f1\"\u003e{\"inputs\":{\"cdbb2fab-1d25-4140-8041-14a2c495f262\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"91991ce4-0ef6-488f-9b28-01b99f8fa5c7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"74078907-7127-4500-bae5-5fe1973e2afd\"}}},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.task_sync_direction = \\\"Salesforce\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"sync_task_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0f72l4g\u003c/incoming\u003e\u003coutgoing\u003eFlow_0eeigkq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_6\" name=\"Salesforce: Write sync task results to a note \"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"0b355962-6d5f-4269-ae8c-b86832246bf8\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0eeigkq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1etib8x\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0eeigkq\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_6\"/\u003e\u003csequenceFlow id=\"Flow_1etib8x\" sourceRef=\"ScriptTask_6\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_0f72l4g\" name=\"Test if Tasks should be added to the Salesforce case\" sourceRef=\"ConditionPoint_4\" targetRef=\"ServiceTask_5\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Test if Tasks should be added to the Salesforce case\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"if incident.properties.salesforce_case_id and playbook.inputs.include_soar_tasks:\\n  result = True\\nelse:\\n  result = False\\n\\n# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0g3b0di\" name=\"Else\" sourceRef=\"ConditionPoint_4\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0g3b0di\" id=\"Flow_0g3b0di_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"-14\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"284\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"554\" y=\"132\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0f72l4g\" id=\"Flow_0f72l4g_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"-14\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"58\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"53\" width=\"86\" x=\"407\" y=\"4\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1etib8x\" id=\"Flow_1etib8x_di\"\u003e\u003comgdi:waypoint x=\"448\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"466\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"466\" y=\"310\"/\u003e\u003comgdi:waypoint x=\"484\" y=\"310\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0eeigkq\" id=\"Flow_0eeigkq_di\"\u003e\u003comgdi:waypoint x=\"350\" y=\"142\"/\u003e\u003comgdi:waypoint x=\"350\" y=\"178\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dmb1fs\" id=\"Flow_1dmb1fs_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"-88\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"-66\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0eyyvr2\" id=\"Flow_0eyyvr2_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"-208\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"-172\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09qrncb\" id=\"Flow_09qrncb_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"-314\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"-292\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"456\" y=\"-366\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"452\" y=\"-292\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"452\" y=\"-172\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"484\" y=\"284\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_4\" id=\"ConditionPoint_4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"428\" y=\"-66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"252\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_6\" id=\"ScriptTask_6_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"252\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785796142,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
      "description": {
        "content": "Create a case in Salesforce. Activation form input and custom field data are used in function input script to create the JSON format payload used to create the case in Salesforce.",
        "format": "text"
      },
      "display_name": "Salesforce: Create Another Salesforce Case",
      "export_key": "salesforce_create_salesforce_case",
      "field_type_handle": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Create Another Salesforce Case",
        "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
        "fields": {
          "include_soar_tasks": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/include_soar_tasks",
            "hide_notification": false,
            "id": 1647,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "include_soar_tasks",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Include SOAR Tasks",
            "tooltip": "Select whether  SOAR tasks are included in the Salesforce case",
            "type_id": 1136,
            "uuid": "4a13602f-fab7-40d1-b68d-3f43de2680d6",
            "values": []
          },
          "salesforce_case_description": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_description",
            "hide_notification": false,
            "id": 1648,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_description",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Description",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "16463964-9292-4fe9-9d8b-4a3334d30bc9",
            "values": []
          },
          "salesforce_case_internal_comments": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_internal_comments",
            "hide_notification": false,
            "id": 1649,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_internal_comments",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Internal Comments",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "dba854fc-d8da-47f8-abaf-09241cdbfbf9",
            "values": []
          },
          "salesforce_case_priority": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_priority",
            "hide_notification": false,
            "id": 1650,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_priority",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Priority",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "5d21b1c3-5a6c-42dd-927d-bceeb7a83550",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "High",
                "properties": null,
                "uuid": "3a1bb84f-1930-4a97-b696-6087b05ce37f",
                "value": 1364
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Medium",
                "properties": null,
                "uuid": "1954a776-1753-46c6-9dec-b7bf6e2569af",
                "value": 1365
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Low",
                "properties": null,
                "uuid": "8a8d2d81-6a17-48bb-9022-986e00e6e77f",
                "value": 1366
              }
            ]
          },
          "salesforce_case_status": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_status",
            "hide_notification": false,
            "id": 1651,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_status",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Status",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "a0d8fbb7-4172-40d8-ac33-20d0ffa357e0",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "New",
                "properties": null,
                "uuid": "6174c220-215d-4273-8d96-27d06ccc537c",
                "value": 1367
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Working",
                "properties": null,
                "uuid": "b55d4690-2a7d-45b3-9c9d-0e5ef80c4779",
                "value": 1368
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Escalated",
                "properties": null,
                "uuid": "8cd6331f-719b-4e2b-9802-8c9bb524be87",
                "value": 1369
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "In Progress",
                "properties": null,
                "uuid": "980c6096-58b7-40f6-9225-d435f891845f",
                "value": 1370
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "On Hold",
                "properties": null,
                "uuid": "c845dc78-9654-49b8-bd2e-624a9cecb86b",
                "value": 1371
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Waiting for Customer",
                "properties": null,
                "uuid": "c05e63e7-d965-4d12-8dae-892ef5a020cf",
                "value": 1372
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Response Received",
                "properties": null,
                "uuid": "943f3113-1b68-46ba-9974-ed447b692434",
                "value": 1373
              }
            ]
          },
          "salesforce_case_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_subject",
            "hide_notification": false,
            "id": 1652,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Subject",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "60a4a55b-80d9-43c5-8093-e4b044b6a48f",
            "values": []
          },
          "salesforce_case_type": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa/salesforce_case_type",
            "hide_notification": false,
            "id": 1653,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_type",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Type",
            "tooltip": "",
            "type_id": 1136,
            "uuid": "d88cdc49-85d5-431d-84f6-a1a4b0ce60d7",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Communication error (fax; email)",
                "properties": null,
                "uuid": "70b82986-4030-4f89-ade2-00d13e598634",
                "value": 1374
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Customization Packages (internal)",
                "properties": null,
                "uuid": "8260c36c-0caa-4a52-9776-0c3ed6c9d099",
                "value": 1375
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Denial of Service",
                "properties": null,
                "uuid": "96b26a24-7bc2-4f07-9440-bdd6a24c8c3d",
                "value": 1376
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Improper disposal: digital assets",
                "properties": null,
                "uuid": "3e640e1c-a8b2-4931-988c-928eb4943749",
                "value": 1377
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Improper disposal: documents / files / records",
                "properties": null,
                "uuid": "d0000238-49e4-4d6e-b297-4db146d3c298",
                "value": 1378
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Lost documents / files / records",
                "properties": null,
                "uuid": "e8c6ff29-7df3-4d06-b621-b8d8355d89ae",
                "value": 1379
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Lost PC / laptop / tablet",
                "properties": null,
                "uuid": "996bdb00-c35b-4f73-9426-ae692e83a390",
                "value": 1380
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Lost storage device / media",
                "properties": null,
                "uuid": "deaa25a4-40e1-40d8-a371-1d8fc061636e",
                "value": 1381
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Malware",
                "properties": null,
                "uuid": "f6adf257-10ea-4d10-b87b-c7d3334ae1ad",
                "value": 1382
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not an Issue",
                "properties": null,
                "uuid": "e7d72181-f212-4d5c-a6de-da2744139cb4",
                "value": 1383
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Other",
                "properties": null,
                "uuid": "a59f8832-e4f9-488c-8aef-2db46c7466b8",
                "value": 1384
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Phishing",
                "properties": null,
                "uuid": "86098bbc-d75b-44d2-8e8a-b5c92eb722fc",
                "value": 1385
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Stolen documents / files / records",
                "properties": null,
                "uuid": "91a4d8b3-52d6-44fb-81c2-b44acd655c23",
                "value": 1386
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Stolen PC / laptop / tablet",
                "properties": null,
                "uuid": "1caf95cc-9675-49e7-b4c1-fb75a420aa1d",
                "value": 1387
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Stolen PDA / smartphone",
                "properties": null,
                "uuid": "4dabba55-e167-4b6d-b0f6-b340caa3d87a",
                "value": 1388
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Stolen storage device / media",
                "properties": null,
                "uuid": "7991638e-16a7-4d4d-abf2-61d67c4df3ce",
                "value": 1389
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "System Intrusion",
                "properties": null,
                "uuid": "d0ecdfd1-3b60-4b9f-99dd-72d4a824c43b",
                "value": 1390
              },
              {
                "default": true,
                "enabled": true,
                "hidden": false,
                "label": "TBD / Unknown",
                "properties": null,
                "uuid": "ba167ad6-329d-4d98-b68c-893e68ffd98c",
                "value": 1391
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Vendor / 3rd party error",
                "properties": null,
                "uuid": "52fa6873-b501-4e6a-aa81-9ba87bdc725d",
                "value": 1392
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
        "type_name": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
        "uuid": "4762252d-9096-4dac-9358-890d0e3e0a4d"
      },
      "has_logical_errors": false,
      "id": 117,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704786233027,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785796845,
          "description": "Write results of Create Salesforce Create Case function to a note",
          "enabled": false,
          "export_key": "Salesforce: Write results of Create Salesforce Case function",
          "id": 94,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704786160834,
          "name": "Salesforce: Write results of Create Salesforce Case function",
          "object_type": "incident",
          "playbook_handle": "salesforce_create_salesforce_case",
          "programmatic_name": "salesforce_create_salesforce_case_salesforce_write_results_of_create_salesforce_case_function",
          "script_text": "results = playbook.functions.results.create_salesforce_case_results\ncontent = results.get(\"content\")\nsalesforce_case = content.get(\"salesforce_case\")\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Create Case in Salesforce\u003c/b\u003e created Case with CaseId: {}\".format(salesforce_case.get(\"id\", None))\n  if salesforce_case.get(\"entity_url\", None):\n    note_text = note_text + \"   \u003ca target=\u0027_blank\u0027 href=\u0027{0}\u0027\u003eLink\u003c/a\u003e\".format(salesforce_case.get(\"entity_url\"))\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Create Case in Salesforce\u003c/b\u003e failed:\u003cbr\u003e{}\".format(salesforce_case.get(\"error\", None))\n  \nincident.addNote(note_text)",
          "tags": [],
          "uuid": "295aaaa0-6cc9-4e54-b426-8bf585223f67"
        },
        {
          "actions": [],
          "created_date": 1704785796899,
          "description": "Write results of sync task function to a note.",
          "enabled": false,
          "export_key": "Salesforce: Write sync task results to a note ",
          "id": 95,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785796957,
          "name": "Salesforce: Write sync task results to a note ",
          "object_type": "incident",
          "playbook_handle": "salesforce_create_salesforce_case",
          "programmatic_name": "salesforce_create_salesforce_case_salesforce_write_sync_task_results_to_a_note_",
          "script_text": "results = playbook.functions.results.sync_task_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks\u003c/b\u003e added:\u003cbr\u003e {0} tasks in Salesforce\u003cbr\u003e {1} tasks in SOAR\".format(results.content.task_count_to_salesforce, results.content.task_count_to_soar)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks\u003c/b\u003e FAILED and was unable to add tasks\"\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "0b355962-6d5f-4269-ae8c-b86832246bf8"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "Case Information",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "a0d8fbb7-4172-40d8-ac33-20d0ffa357e0",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "5d21b1c3-5a6c-42dd-927d-bceeb7a83550",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d88cdc49-85d5-431d-84f6-a1a4b0ce60d7",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "4a13602f-fab7-40d1-b68d-3f43de2680d6",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Description Information",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "60a4a55b-80d9-43c5-8093-e4b044b6a48f",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "16463964-9292-4fe9-9d8b-4a3334d30bc9",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "dba854fc-d8da-47f8-abaf-09241cdbfbf9",
            "element": "field_uuid",
            "field_type": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "salesforce_create_salesforce_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_53b2cb7f-7d97-4da5-acbf-89fdee65baaa",
        "id": 134,
        "name": "playbook_53b2cb7f_7d97_4da5_acbf_89fdee65baaa",
        "type": "playbook",
        "uuid": "e5b897d4-695d-4e06-9511-87d2da684993"
      },
      "tags": [],
      "type": "default",
      "uuid": "53b2cb7f-7d97-4da5-acbf-89fdee65baaa",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b\" isExecutable=\"true\" name=\"playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_17mzlly\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_17mzlly\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_4\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update SOAR Case with Salesforce Case Details\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"361b2f7a-5938-45d6-9d54-2410aadf9f15\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0nmmye0\u003c/incoming\u003e\u003coutgoing\u003eFlow_0axyoi4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0fx92y3\u003c/incoming\u003e\u003cincoming\u003eFlow_1hej2ug\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0axyoi4\" sourceRef=\"ScriptTask_2\" targetRef=\"ServiceTask_10\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Salesforce: Create Case in Salesforce\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74337648-8bfe-4aa6-9cdd-34dd819a2bdd\"\u003e{\"inputs\":{},\"pre_processing_script\":\"import json\\n\\ncase_json = {}\\ncase_json[\u0027Origin\u0027] = \\\"Web\\\"\\ncase_json[\u0027Status\u0027] = \\\"New\\\"\\ncase_json[\u0027Priority\u0027] = incident.severity_code \\nif incident.description:\\n  case_json[\u0027Description\u0027] = incident.description.content\\nelse:\\n  case_json[\u0027Description\u0027] = \\\"Case created from SOAR case {}\\\".format(incident.id)\\ncase_json[\u0027Subject\u0027] = incident.name\\n\\n# Need to make incident type multi-select in Salesforce to support multi-select in SOAR\\n# For now just take the first incident type in the list.\\nif incident.incident_type_ids != []:\\n  case_json[\u0027Type\u0027] = incident.incident_type_ids[0]\\n\\ninputs.salesforce_case_payload = json.dumps(case_json)\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"salesforce_case_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_17mzlly\u003c/incoming\u003e\u003coutgoing\u003eFlow_0nmmye0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0nmmye0\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_2\"/\u003e\u003cexclusiveGateway default=\"Flow_0fx92y3\" id=\"ConditionPoint_5\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_1ogpsjr\u003c/incoming\u003e\u003coutgoing\u003eFlow_1u0fchy\u003c/outgoing\u003e\u003coutgoing\u003eFlow_0fx92y3\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_8\" name=\"Salesforce: Sync Tasks Between Cases\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f9907018-0770-4e2c-9620-cb623b5a43f1\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.task_sync_direction = \\\"Salesforce\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"sync_task_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1u0fchy\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ve9jxo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0ve9jxo\" sourceRef=\"ServiceTask_8\" targetRef=\"ScriptTask_9\"/\u003e\u003cscriptTask id=\"ScriptTask_9\" name=\"Salesforce: Write sync task results to a note \"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"41a8cbe5-2350-4188-ae41-40763eada20a\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ve9jxo\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hej2ug\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1hej2ug\" sourceRef=\"ScriptTask_9\" targetRef=\"EndPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_10\" name=\"Salesforce: Add Comment to Salesforce Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c13836c0-4432-4cb3-81ed-146422c3939c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_case_id = incident.properties.salesforce_case_id\\nresults = playbook.functions.results.salesforce_case_results\\ninputs.salesforce_comment_text = \\\"This Salesforce case created from SOAR case {0} URL: {1}\\\".format(incident.id, playbook.functions.results.salesforce_case_results.content.salesforce_case.soar_case_url)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_comment_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0axyoi4\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ogpsjr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1ogpsjr\" sourceRef=\"ServiceTask_10\" targetRef=\"ConditionPoint_5\"/\u003e\u003csequenceFlow id=\"Flow_1u0fchy\" name=\"Test if Tasks should be added to the case\" sourceRef=\"ConditionPoint_5\" targetRef=\"ServiceTask_8\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Test if Tasks should be added to the case\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"if incident.properties.salesforce_case_id and playbook.inputs.include_soar_tasks:\\n  result = True\\nelse:\\n  result = False\\n\\n# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_0fx92y3\" name=\"Else\" sourceRef=\"ConditionPoint_5\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fx92y3\" id=\"Flow_0fx92y3_di\"\u003e\u003comgdi:waypoint x=\"730\" y=\"446\"/\u003e\u003comgdi:waypoint x=\"730\" y=\"704\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"720\" y=\"530\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1u0fchy\" id=\"Flow_1u0fchy_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"446\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"520\"/\u003e\u003comgdi:waypoint x=\"578\" y=\"520\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"84\" x=\"628\" y=\"445\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ogpsjr\" id=\"Flow_1ogpsjr_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"394\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hej2ug\" id=\"Flow_1hej2ug_di\"\u003e\u003comgdi:waypoint x=\"578\" y=\"643\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"643\"/\u003e\u003comgdi:waypoint x=\"690\" y=\"704\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ve9jxo\" id=\"Flow_0ve9jxo_di\"\u003e\u003comgdi:waypoint x=\"469\" y=\"562\"/\u003e\u003comgdi:waypoint x=\"469\" y=\"575\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"575\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"588\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0nmmye0\" id=\"Flow_0nmmye0_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"132\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0axyoi4\" id=\"Flow_0axyoi4_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_17mzlly\" id=\"Flow_17mzlly_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"26\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"48\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"616\" y=\"-26\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"644\" y=\"704\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"48\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_5\" id=\"ConditionPoint_5_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"588\" y=\"394\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_8\" id=\"ServiceTask_8_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"382\" y=\"478\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_9\" id=\"ScriptTask_9_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"382\" y=\"588\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10\" id=\"ServiceTask_10_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785797639,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
      "description": {
        "content": "Create a Salesforce case from the SOAR case which activated the playbook.  This playbook is only available to SOAR cases that are not associated with a Salesforce case.",
        "format": "text"
      },
      "display_name": "Salesforce: Create Salesforce Case from This SOAR Case",
      "export_key": "salesforce_create_salesforce_case_from_this_soar_case",
      "field_type_handle": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Create Salesforce Case from This SOAR Case",
        "export_key": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
        "fields": {
          "include_soar_tasks": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b/include_soar_tasks",
            "hide_notification": false,
            "id": 1654,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "include_soar_tasks",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Include SOAR Tasks",
            "tooltip": "",
            "type_id": 1137,
            "uuid": "ce7e186e-390d-4477-91fb-ec8e99a3e6eb",
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
        "type_name": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
        "uuid": "22981e16-5ba1-42cf-a64b-96502cdc6204"
      },
      "has_logical_errors": false,
      "id": 118,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704786231383,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785797943,
          "description": "Salesforce: Update SOAR Case with Salesforce Case Details",
          "enabled": false,
          "export_key": "Salesforce: Update SOAR Case with Salesforce Case Details",
          "id": 96,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704786144002,
          "name": "Salesforce: Update SOAR Case with Salesforce Case Details",
          "object_type": "incident",
          "playbook_handle": "salesforce_create_salesforce_case_from_this_soar_case",
          "programmatic_name": "salesforce_create_salesforce_case_from_this_soar_case_salesforce_update_soar_case_with_salesforce_case_details",
          "script_text": "results = playbook.functions.results.salesforce_case_results\ncontent = results.get(\"content\")\nsalesforce_case = content.get(\"salesforce_case\")\n\nif results.success:\n  incident.properties.salesforce_case_id = salesforce_case.get(\"id\")  \n  incident.properties.salesforce_case_number = salesforce_case.get(\"CaseNumber\")\n  note_text = \"\u003cb\u003eSalesforce: Created Case in Salesforce\u003c/b\u003e created Case with CaseId: {}\".format(salesforce_case.get(\"id\", None))\n  if salesforce_case.get(\"entity_url\", None):\n    note_text = note_text + \"   \u003ca target=\u0027_blank\u0027 href=\u0027{0}\u0027\u003eLink\u003c/a\u003e\".format(salesforce_case.get(\"entity_url\"))\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Create Case in Salesforce\u003c/b\u003e failed:\u003cbr\u003e{}\".format(salesforce_case.get(\"error\", None))\n  \nincident.addNote(note_text)",
          "tags": [],
          "uuid": "361b2f7a-5938-45d6-9d54-2410aadf9f15"
        },
        {
          "actions": [],
          "created_date": 1704785798000,
          "description": "Write the results of sending SOAR Tasks to Salesforce case",
          "enabled": false,
          "export_key": "Salesforce: Write results of Send Tasks to Salesforce case",
          "id": 97,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785798061,
          "name": "Salesforce: Write results of Send Tasks to Salesforce case",
          "object_type": "incident",
          "playbook_handle": "salesforce_create_salesforce_case_from_this_soar_case",
          "programmatic_name": "salesforce_create_salesforce_case_from_this_soar_case_salesforce_write_results_of_send_tasks_to_salesforce_case",
          "script_text": "results = playbook.functions.results.send_task_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Send SOAR Tasks to Salesforce Case\u003c/b\u003e added {} task(s)\".format(results.task_count)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Send SOAR Tasks to Salesforce Case\u003c/b\u003e FAILED and was unable to add tasks\"\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "ffb95327-d0d4-4382-af14-6c8c279efd98"
        },
        {
          "actions": [],
          "created_date": 1704785798063,
          "description": "Write results of sync task function to a note.",
          "enabled": false,
          "export_key": "Salesforce: Write sync task results to a note ",
          "id": 98,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785798122,
          "name": "Salesforce: Write sync task results to a note ",
          "object_type": "incident",
          "playbook_handle": "salesforce_create_salesforce_case_from_this_soar_case",
          "programmatic_name": "salesforce_create_salesforce_case_from_this_soar_case_salesforce_write_sync_task_results_to_a_note_",
          "script_text": "results = playbook.functions.results.sync_task_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks\u003c/b\u003e added:\u003cbr\u003e {0} tasks in Salesforce\u003cbr\u003e {1} tasks in SOAR\".format(results.content.task_count_to_salesforce, results.content.task_count_to_soar)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks\u003c/b\u003e FAILED and was unable to add tasks\"\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "41a8cbe5-2350-4188-ae41-40763eada20a"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "not_has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "ce7e186e-390d-4477-91fb-ec8e99a3e6eb",
            "element": "field_uuid",
            "field_type": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "salesforce_create_salesforce_case_from_this_soar_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a9666b4d-02ff-47be-a8c7-719b9b51541b",
        "id": 135,
        "name": "playbook_a9666b4d_02ff_47be_a8c7_719b9b51541b",
        "type": "playbook",
        "uuid": "92710b4b-0b0d-47d6-89b0-261eaf000f41"
      },
      "tags": [],
      "type": "default",
      "uuid": "a9666b4d-02ff-47be-a8c7-719b9b51541b",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815\" isExecutable=\"true\" name=\"playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0bchg87\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Attachments from Salesforce\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ae3237f6-af1f-4b0f-a39f-73f35dd3208d\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.task_id = None\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_attachments_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0bchg87\u003c/incoming\u003e\u003coutgoing\u003eFlow_0xmivdt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0bchg87\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Get Attachments write results to a note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e081b66b-c20a-43e3-ba90-c3e88861db98\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0xmivdt\u003c/incoming\u003e\u003coutgoing\u003eFlow_19rxtya\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0xmivdt\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_19rxtya\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_19rxtya\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_19rxtya\" id=\"Flow_19rxtya_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"404\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0xmivdt\" id=\"Flow_0xmivdt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0bchg87\" id=\"Flow_0bchg87_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"404\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785798823,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815",
      "description": {
        "content": "Get attachments from Salesforce case and add them to the SOAR case.",
        "format": "text"
      },
      "display_name": "Salesforce: Get Attachments from Salesforce Case",
      "export_key": "salesforce_get_attachments_from_salesforce_case",
      "field_type_handle": "playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Get Attachments from Salesforce Case",
        "export_key": "playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815",
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
        "type_name": "playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815",
        "uuid": "f55f418c-c05a-4198-8a1f-d695c0591873"
      },
      "has_logical_errors": false,
      "id": 119,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785799894,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785799061,
          "description": "Write the results of Get Attachments function to a note.",
          "enabled": false,
          "export_key": "Salesforce: Get Attachments write results to a note",
          "id": 99,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785799119,
          "name": "Salesforce: Get Attachments write results to a note",
          "object_type": "incident",
          "playbook_handle": "salesforce_get_attachments_from_salesforce_case",
          "programmatic_name": "salesforce_get_attachments_from_salesforce_case_salesforce_get_attachments_write_results_to_a_note",
          "script_text": "results = playbook.functions.results.get_attachments_results\n\nif results.success:\n  salesforce_attachments = results.content.salesforce_attachments\n  note_text = \"\u003cb\u003eSalesforce: Get Attachments:\u003c/b\u003e added {} attachments to incident:\u003cbr\u003e\".format(len(salesforce_attachments))\n  for attachment_name in salesforce_attachments:\n    note_text = note_text + \"\u003cbr\u003e{}\".format(attachment_name)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Get Attachments\u003c/b\u003e failed to get attachments from Salesforce.\"\nincident.addNote(note_text)\n",
          "tags": [],
          "uuid": "e081b66b-c20a-43e3-ba90-c3e88861db98"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_get_attachments_from_salesforce_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_e43fa5c0-2ea2-4965-abc7-c5525e3c7815",
        "id": 136,
        "name": "playbook_e43fa5c0_2ea2_4965_abc7_c5525e3c7815",
        "type": "playbook",
        "uuid": "9bc12c5f-be3f-4b5f-9e09-00126c565279"
      },
      "tags": [],
      "type": "default",
      "uuid": "e43fa5c0-2ea2-4965-abc7-c5525e3c7815",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6\" isExecutable=\"true\" name=\"playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0vaelh5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Post Attachment to Salesforce Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ecdac742-4e8a-4b9e-9ec9-4734d48ab62d\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.attachment_id = None\\ninputs.task_id = None\\ninputs.artifact_id = artifact.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"post_artifact_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0vaelh5\u003c/incoming\u003e\u003coutgoing\u003eFlow_15v5is0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0vaelh5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0qr2uq0\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Salesforce: Post Artifact File to Salesforce Case\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"c6e996e2-47ab-4da6-b6ef-0498e9177708\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_15v5is0\u003c/incoming\u003e\u003coutgoing\u003eFlow_0qr2uq0\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_15v5is0\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_0qr2uq0\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0vaelh5\" id=\"Flow_0vaelh5_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_15v5is0\" id=\"Flow_15v5is0_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"298\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qr2uq0\" id=\"Flow_0qr2uq0_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"382\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"298\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785799842,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6",
      "description": {
        "content": "Post a SOAR artifact file to a Salesforce cases as an attachment.",
        "format": "text"
      },
      "display_name": "Salesforce: Post Artifact File to Salesforce Case",
      "export_key": "salesforce_post_artifact_file_to_salesforce_case",
      "field_type_handle": "playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Post Artifact File to Salesforce Case",
        "export_key": "playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6",
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
        "type_name": "playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6",
        "uuid": "8750eac5-289c-4753-a4f2-ecd500f38f59"
      },
      "has_logical_errors": false,
      "id": 120,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785801172,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785800070,
          "description": "Write the results of posting an artifact file to a Salesforce case as an attachment.",
          "enabled": false,
          "export_key": "Salesforce: Post Artifact File to Salesforce Case",
          "id": 100,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785800121,
          "name": "Salesforce: Post Artifact File to Salesforce Case",
          "object_type": "artifact",
          "playbook_handle": "salesforce_post_artifact_file_to_salesforce_case",
          "programmatic_name": "salesforce_post_artifact_file_to_salesforce_case_salesforce_post_artifact_file_to_salesforce_case",
          "script_text": "results = playbook.functions.results.post_artifact_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Post Artifact File to Salesforce Case\u003c/b\u003e post attachment to case:\u003cbr\u003e{}\".format(results.content.salesforce_attachment)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Post Artifact File to Salesforce Case\u003c/b\u003e was NOT successful.\"\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "c6e996e2-47ab-4da6-b6ef-0498e9177708"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": 2,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Email Attachment"
            },
            {
              "evaluation_id": 3,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Malware Sample"
            },
            {
              "evaluation_id": 1,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "custom_condition": "(1 AND 2) OR (1 AND 3)",
          "logic_type": "advanced"
        },
        "view_items": []
      },
      "name": "salesforce_post_artifact_file_to_salesforce_case",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_05ce7276-b7fc-4e8c-afcf-41831acab3d6",
        "id": 137,
        "name": "playbook_05ce7276_b7fc_4e8c_afcf_41831acab3d6",
        "type": "playbook",
        "uuid": "b211c0dd-5da7-4a31-b862-226688ccd144"
      },
      "tags": [],
      "type": "default",
      "uuid": "05ce7276-b7fc-4e8c-afcf-41831acab3d6",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df\" isExecutable=\"true\" name=\"playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1191hgv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Post Attachment to Salesforce Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ecdac742-4e8a-4b9e-9ec9-4734d48ab62d\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.attachment_id = attachment.id\\ninputs.task_id = task.id if attachment.type == \u0027task\u0027 else None\\ninputs.artifact_id = None\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"post_attachment_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1191hgv\u003c/incoming\u003e\u003coutgoing\u003eFlow_06yoptt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1191hgv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write Results of Post Attachment to Salesforce case \"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"6f85e283-5988-4a28-a61a-1b7c729e54b2\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_06yoptt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1l04h11\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_06yoptt\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1l04h11\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1l04h11\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1l04h11\" id=\"Flow_1l04h11_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"152\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"204\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_06yoptt\" id=\"Flow_06yoptt_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"68\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1191hgv\" id=\"Flow_1191hgv_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"-124\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"-62\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.017\" x=\"605\" y=\"-176\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612.008\" y=\"-62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"612.008\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"644.008\" y=\"204\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785801114,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df",
      "description": {
        "content": "Post the SOAR attachment to the corresponding case in Salesforce.",
        "format": "text"
      },
      "display_name": "Salesforce: Post Attachment to Salesforce Case",
      "export_key": "salesforce_post_attachment_to_salesforce_case",
      "field_type_handle": "playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Post Attachment to Salesforce Case",
        "export_key": "playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df",
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
        "type_name": "playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df",
        "uuid": "5f49777e-12b3-4c69-ab4e-177557cf79d4"
      },
      "has_logical_errors": false,
      "id": 121,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785802310,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785801357,
          "description": "Write the results of posting a SOAR attachment to case in Salesforce",
          "enabled": false,
          "export_key": "Salesforce: Write Results of Post Attachment to Salesforce case ",
          "id": 101,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785801410,
          "name": "Salesforce: Write Results of Post Attachment to Salesforce case ",
          "object_type": "attachment",
          "playbook_handle": "salesforce_post_attachment_to_salesforce_case",
          "programmatic_name": "salesforce_post_attachment_to_salesforce_case_salesforce_write_results_of_post_attachment_to_salesforce_case_",
          "script_text": "results = playbook.functions.results.post_attachment_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Post Attachment to Salesforce Case\u003c/b\u003e post attachment to case:\u003cbr\u003e{}\".format(results.content.salesforce_attachment)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Post Attachment to Salesforce Case\u003c/b\u003e was NOT successful.\"\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "6f85e283-5988-4a28-a61a-1b7c729e54b2"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_post_attachment_to_salesforce_case",
      "object_type": "attachment",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_c9b4fe8b-8d4a-4e1f-a3cd-6cf4204f70df",
        "id": 138,
        "name": "playbook_c9b4fe8b_8d4a_4e1f_a3cd_6cf4204f70df",
        "type": "playbook",
        "uuid": "345302a7-3350-434f-b963-e2e56905dde6"
      },
      "tags": [],
      "type": "default",
      "uuid": "c9b4fe8b-8d4a-4e1f-a3cd-6cf4204f70df",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16\" isExecutable=\"true\" name=\"playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_029fukv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Add Comment to Salesforce Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c13836c0-4432-4cb3-81ed-146422c3939c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.salesforce_comment_text = note.text.content\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"add_comment_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_029fukv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1sjf3va\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_029fukv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1sjf3va\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1sjf3va\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sjf3va\" id=\"Flow_1sjf3va_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"334\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_029fukv\" id=\"Flow_029fukv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.5667\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"334\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785802258,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16",
      "description": {
        "content": "Send the specified SOAR case note as a comment in the corresponding Salesforce case.",
        "format": "text"
      },
      "display_name": "Salesforce: Send Note to Salesforce Case",
      "export_key": "salesforce_send_note_to_salesforce_case",
      "field_type_handle": "playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Send Note to Salesforce Case",
        "export_key": "playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16",
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
        "type_name": "playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16",
        "uuid": "938f4fa6-ce40-459f-b8aa-e18c805aad81"
      },
      "has_logical_errors": false,
      "id": 122,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785803210,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_send_note_to_salesforce_case",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_2e3e51f7-d0a9-42e0-b863-3e8b5c096c16",
        "id": 139,
        "name": "playbook_2e3e51f7_d0a9_42e0_b863_3e8b5c096c16",
        "type": "playbook",
        "uuid": "30c92484-f065-46c9-b3ec-b54aec14ae78"
      },
      "tags": [],
      "type": "default",
      "uuid": "2e3e51f7-d0a9-42e0-b863-3e8b5c096c16",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_7aaf3494_d064_4357_b92e_095fc9c740a7\" isExecutable=\"true\" name=\"playbook_7aaf3494_d064_4357_b92e_095fc9c740a7\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0uavjhb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Create Task in Salesforce Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"aa8d86b1-e94d-4906-b175-6889001f67c6\"\u003e{\"inputs\":{},\"pre_processing_script\":\"import json\\n\\ninputs.incident_id = incident.id\\ninputs.task_id = task.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\\ntask_json = {}\\n\\ntask_json[\u0027WhatId\u0027] = inputs.salesforce_case_id\\n\\ndescription = \\\"Task from IBM SOAR case {}\\\".format(incident.id)\\nif task.instructions:\\n  description = description + \\\": {}\\\".format(task.instructions.content)\\n\\ntask_json[\u0027Description\u0027] = description\\n\\nif task.due_date:\\n  task_json[\u0027ActivityDate\u0027] = task.due_date\\n  \\nif task.name:\\n  task_json[\u0027Subject\u0027] = task.name\\n\\nif playbook.inputs.task_priority:\\n  task_json[\u0027Priority\u0027] = playbook.inputs.task_priority\\n  \\nif playbook.inputs.task_status:\\n  task_json[\u0027Status\u0027] = playbook.inputs.task_status\\n  \\ninputs.salesforce_task_payload = json.dumps(task_json)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"create_task_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0uavjhb\u003c/incoming\u003e\u003coutgoing\u003eFlow_1qvkqjc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0uavjhb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write Create Task to Note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"9a5d6c5e-2d67-4f2f-b171-699e7a032e9b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1qvkqjc\u003c/incoming\u003e\u003coutgoing\u003eFlow_1sm5iud\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1qvkqjc\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1sm5iud\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1sm5iud\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_7aaf3494_d064_4357_b92e_095fc9c740a7\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sm5iud\" id=\"Flow_1sm5iud_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qvkqjc\" id=\"Flow_1qvkqjc_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0uavjhb\" id=\"Flow_0uavjhb_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"161.48329999999999\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785803158,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
      "description": {
        "content": "Send the task to corresponding Salesforce case.",
        "format": "text"
      },
      "display_name": "Salesforce: Send Task to Salesforce Case",
      "export_key": "salesforce_send_task_to_salesforce_case",
      "field_type_handle": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Send Task to Salesforce Case",
        "export_key": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
        "fields": {
          "task_priority": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7/task_priority",
            "hide_notification": false,
            "id": 1655,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "task_priority",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Priority",
            "tooltip": "",
            "type_id": 1142,
            "uuid": "77dbbf3a-1f6b-43e9-9db6-8b848c4b67fd",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "High",
                "properties": null,
                "uuid": "78969fde-c0db-4f60-93fd-98feeb59cd14",
                "value": 1393
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Normal",
                "properties": null,
                "uuid": "5ee985f8-5a7c-4a83-bc8d-4da139b8ec9d",
                "value": 1394
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Low",
                "properties": null,
                "uuid": "65b32557-56e6-4864-8d86-6842c2f56fd3",
                "value": 1395
              }
            ]
          },
          "task_status": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7/task_status",
            "hide_notification": false,
            "id": 1656,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "task_status",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Status",
            "tooltip": "",
            "type_id": 1142,
            "uuid": "b59fefbc-4709-4722-b372-c985e87f7ca6",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Not Started",
                "properties": null,
                "uuid": "461cfdf6-39dd-450a-987e-d78d9bb224e8",
                "value": 1396
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "In Progress",
                "properties": null,
                "uuid": "42afd1d4-8e21-4b06-a6f2-4f9a4c1e33b8",
                "value": 1397
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Completed",
                "properties": null,
                "uuid": "96b7613d-4ff2-45df-a00a-b81eb134abb6",
                "value": 1398
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Waiting on someone else",
                "properties": null,
                "uuid": "f6935373-aa57-4cdd-aca1-a533e75a0b08",
                "value": 1399
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Deferred",
                "properties": null,
                "uuid": "58a3b0b2-6547-4212-a038-57b63c99e7f1",
                "value": 1400
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
        "type_name": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
        "uuid": "9437aa9e-c26c-4070-b17d-6d452619f22c"
      },
      "has_logical_errors": false,
      "id": 123,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785804443,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785803522,
          "description": "Write the results of creating a task in Salesforce to a note",
          "enabled": false,
          "export_key": "Salesforce: Write Create Task to Note",
          "id": 102,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785803575,
          "name": "Salesforce: Write Create Task to Note",
          "object_type": "task",
          "playbook_handle": "salesforce_send_task_to_salesforce_case",
          "programmatic_name": "salesforce_send_task_to_salesforce_case_salesforce_write_create_task_to_note",
          "script_text": "results = playbook.functions.results.create_task_results\ncontent = results.get(\"content\")\nsalesforce_task = content.get(\"salesforce_task\")\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Create Task in Salesforce\u003c/b\u003e created with TaskId: {}\".format(salesforce_task.get(\"id\", None))\nelse:\n    note_text = \"\u003cb\u003eSalesforce: Create Task in Salesforce\u003c/b\u003e failed:\u003cbr\u003e{}\".format(salesforce_task.get(\"error\", None))\n  \nincident.addNote(note_text)",
          "tags": [],
          "uuid": "9a5d6c5e-2d67-4f2f-b171-699e7a032e9b"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "b59fefbc-4709-4722-b372-c985e87f7ca6",
            "element": "field_uuid",
            "field_type": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "77dbbf3a-1f6b-43e9-9db6-8b848c4b67fd",
            "element": "field_uuid",
            "field_type": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "salesforce_send_task_to_salesforce_case",
      "object_type": "task",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_7aaf3494-d064-4357-b92e-095fc9c740a7",
        "id": 140,
        "name": "playbook_7aaf3494_d064_4357_b92e_095fc9c740a7",
        "type": "playbook",
        "uuid": "2f57f4d7-0150-4439-8460-d8f29e6a39ac"
      },
      "tags": [],
      "type": "default",
      "uuid": "7aaf3494-d064-4357-b92e-095fc9c740a7",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568\" isExecutable=\"true\" name=\"playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0jniqug\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_0jniqug\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_4\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1sz571p\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"Salesforce: Write results of task sync to note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"7ce3de1b-7858-4116-aebc-9055c2560cfd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0drzqdl\u003c/incoming\u003e\u003coutgoing\u003eFlow_1sz571p\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1sz571p\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"Salesforce: Sync Tasks Between Cases\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f9907018-0770-4e2c-9620-cb623b5a43f1\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.task_sync_direction = playbook.inputs.task_sync_direction\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"sync_task_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0jniqug\u003c/incoming\u003e\u003coutgoing\u003eFlow_0drzqdl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0drzqdl\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0drzqdl\" id=\"Flow_0drzqdl_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1sz571p\" id=\"Flow_1sz571p_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jniqug\" id=\"Flow_0jniqug_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"307.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"167.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785804387,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Salesforce: Sync Tasks Between SOAR and Salesforce",
      "export_key": "salesforce_sync_tasks_between_soar_and_salesforce",
      "field_type_handle": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Sync Tasks Between SOAR and Salesforce",
        "export_key": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
        "fields": {
          "task_sync_direction": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568/task_sync_direction",
            "hide_notification": false,
            "id": 1657,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "task_sync_direction",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Task Sync Direction",
            "tooltip": "Select direction to push tasks: Push to Salesforce, Push to SOAR, Push to both Salesforce and SOAR ",
            "type_id": 1143,
            "uuid": "8d17b08d-67e6-46a2-a5ec-93db19f9ecdd",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Salesforce",
                "properties": null,
                "uuid": "93111665-b185-403d-8271-34277be7c523",
                "value": 1401
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "SOAR",
                "properties": null,
                "uuid": "0e41ca6d-2edd-492f-9e4d-3af845adfeae",
                "value": 1402
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Both",
                "properties": null,
                "uuid": "7a8b253c-4127-4c4f-a2fd-509608e7aec8",
                "value": 1403
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
        "type_name": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
        "uuid": "6d7c0559-c80b-4cdf-978a-221aa9e4d99c"
      },
      "has_logical_errors": false,
      "id": 124,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785805558,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785804715,
          "description": "Write results of task sync to note.",
          "enabled": false,
          "export_key": "Salesforce: Write results of task sync to note",
          "id": 103,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785804772,
          "name": "Salesforce: Write results of task sync to note",
          "object_type": "incident",
          "playbook_handle": "salesforce_sync_tasks_between_soar_and_salesforce",
          "programmatic_name": "salesforce_sync_tasks_between_soar_and_salesforce_salesforce_write_results_of_task_sync_to_note",
          "script_text": "results = playbook.functions.results.sync_task_results\n\nif results.success:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks Between SOAR and Salesforce\u003c/b\u003e\u003cbr\u003e sync direction to {0} added:\u003cbr\u003e {1} tasks in Salesforce\u003cbr\u003e {2} tasks in SOAR\".format(playbook.inputs.task_sync_direction, results.content.task_count_to_salesforce, results.content.task_count_to_soar)\nelse:\n  note_text = \"\u003cb\u003eSalesforce: Sync Tasks Between SOAR and Salesforce\u003c/b\u003e\u003cbr\u003e sync direction to {0} FAILED and was unable to add tasks\".format(playbook.inputs.task_sync_direction)\n\nincident.addNote(note_text)",
          "tags": [],
          "uuid": "7ce3de1b-7858-4116-aebc-9055c2560cfd"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "8d17b08d-67e6-46a2-a5ec-93db19f9ecdd",
            "element": "field_uuid",
            "field_type": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "salesforce_sync_tasks_between_soar_and_salesforce",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a0042da4-5e03-462a-b3dd-ebc7b67f6568",
        "id": 141,
        "name": "playbook_a0042da4_5e03_462a_b3dd_ebc7b67f6568",
        "type": "playbook",
        "uuid": "c031a094-4461-498c-af71-fe6677e40cb1"
      },
      "tags": [],
      "type": "default",
      "uuid": "a0042da4-5e03-462a-b3dd-ebc7b67f6568",
      "version": 4
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_account_id",
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
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_e81303a8_e109_4418_88df_424d8ea764d5\" isExecutable=\"true\" name=\"playbook_e81303a8_e109_4418_88df_424d8ea764d5\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_103l0pq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Account\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ce27c1d7-8c77-45a4-ba6b-209c79f44192\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_account_id = incident.properties.salesforce_account_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"account_details\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1u4f9pj\u003c/incoming\u003e\u003coutgoing\u003eFlow_0v6bcaj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_103l0pq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ConditionPoint_4\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update Account details in SOAR\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a63daeaa-bba8-429c-bb8b-0dc67ad10eb2\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0v6bcaj\u003c/incoming\u003e\u003coutgoing\u003eFlow_05lkdcm\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0v6bcaj\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_05lkdcm\u003c/incoming\u003e\u003cincoming\u003eFlow_08hyg7x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_05lkdcm\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003cexclusiveGateway default=\"Flow_1o6qozh\" id=\"ConditionPoint_4\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_103l0pq\u003c/incoming\u003e\u003coutgoing\u003eFlow_1u4f9pj\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1o6qozh\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"Salesforce: Set Account fields to None\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a1bcc55e-b858-4d6e-ac97-edec0e7482c4\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1o6qozh\u003c/incoming\u003e\u003coutgoing\u003eFlow_08hyg7x\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_08hyg7x\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_1u4f9pj\" name=\"Test if AccountId is not null\" sourceRef=\"ConditionPoint_4\" targetRef=\"ServiceTask_1\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Test if AccountId is not null\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\nif incident.properties.salesforce_account_id:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1o6qozh\" name=\"Else\" sourceRef=\"ConditionPoint_4\" targetRef=\"ScriptTask_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e81303a8_e109_4418_88df_424d8ea764d5\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1o6qozh\" id=\"Flow_1o6qozh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"142\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"142\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"784\" y=\"124\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1u4f9pj\" id=\"Flow_1u4f9pj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"137\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"137\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"158\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"84\" x=\"609\" y=\"119\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08hyg7x\" id=\"Flow_08hyg7x_di\"\u003e\u003comgdi:waypoint x=\"870\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"870\" y=\"333\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"333\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"394\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_05lkdcm\" id=\"Flow_05lkdcm_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"378\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"378\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"394\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0v6bcaj\" id=\"Flow_0v6bcaj_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_103l0pq\" id=\"Flow_103l0pq_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"6\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"44\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"-46\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"482\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"482\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"394\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_4\" id=\"ConditionPoint_4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"599\" y=\"44\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"772\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785805506,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_e81303a8_e109_4418_88df_424d8ea764d5",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Salesforce: Update Account Details in SOAR",
      "export_key": "salesforce_update_account_details_in_soar",
      "field_type_handle": "playbook_e81303a8_e109_4418_88df_424d8ea764d5",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Account Details in SOAR",
        "export_key": "playbook_e81303a8_e109_4418_88df_424d8ea764d5",
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
        "type_name": "playbook_e81303a8_e109_4418_88df_424d8ea764d5",
        "uuid": "cc3f22d2-34d6-4b6a-9cfb-38dd59475b0f"
      },
      "has_logical_errors": false,
      "id": 125,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785806596,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785805734,
          "description": " Set Account fields to None",
          "enabled": false,
          "export_key": "Salesforce: Set Account fields to None",
          "id": 104,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785805788,
          "name": "Salesforce: Set Account fields to None",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_account_details_in_soar",
          "programmatic_name": "salesforce_update_account_details_in_soar_salesforce_set_account_fields_to_none",
          "script_text": "incident.properties.salesforce_account_name = None",
          "tags": [],
          "uuid": "a1bcc55e-b858-4d6e-ac97-edec0e7482c4"
        },
        {
          "actions": [],
          "created_date": 1704785805790,
          "description": "Update the custom fields in SOAR related to the Salesforce Account.",
          "enabled": false,
          "export_key": "Salesforce: Update Account details in SOAR",
          "id": 105,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785805848,
          "name": "Salesforce: Update Account details in SOAR",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_account_details_in_soar",
          "programmatic_name": "salesforce_update_account_details_in_soar_salesforce_update_account_details_in_soar",
          "script_text": "results = playbook.functions.results.account_details\n\nif results.success:\n  content = results.get(\"content\", {})\n  if content:\n    account = content.get(\"salesforce_account\", None)\n    if account:\n      incident.properties.salesforce_account_name = account.get(\"Name\", None)\nelse:\n  incident.addNote(\"Salesforce: unable to get account details for Account Id \")",
          "tags": [],
          "uuid": "a63daeaa-bba8-429c-bb8b-0dc67ad10eb2"
        }
      ],
      "name": "salesforce_update_account_details_in_soar",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_e81303a8-e109-4418-88df-424d8ea764d5",
        "id": 142,
        "name": "playbook_e81303a8_e109_4418_88df_424d8ea764d5",
        "type": "playbook",
        "uuid": "56210d2a-fdb1-4b1d-9160-65ec3968e8ed"
      },
      "tags": [],
      "type": "default",
      "uuid": "e81303a8-e109-4418-88df-424d8ea764d5",
      "version": 4
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.plan_status",
              "method": "equals",
              "type": null,
              "value": "Active"
            },
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
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
          "logic_type": "all"
        }
      },
      "activation_type": "automatic",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_a6db8735_3d90_4c38_866d_2f91ca038490\" isExecutable=\"true\" name=\"playbook_a6db8735_3d90_4c38_866d_2f91ca038490\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qwx89d\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Case\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"055485d3-e8ab-434a-9500-3b8ae61680b2\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"salesforce_case_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qwx89d\u003c/incoming\u003e\u003coutgoing\u003eFlow_1xv3h3v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qwx89d\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update case in SOAR\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"322f86b9-0a67-4ad1-a53c-97dac97b17fb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1xv3h3v\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ajzbls\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0ajzbls\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1xv3h3v\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_0ajzbls\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a6db8735_3d90_4c38_866d_2f91ca038490\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ajzbls\" id=\"Flow_0ajzbls_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"364\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1xv3h3v\" id=\"Flow_1xv3h3v_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"192\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qwx89d\" id=\"Flow_0qwx89d_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"76\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"24\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"108\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"364\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785806542,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_a6db8735_3d90_4c38_866d_2f91ca038490",
      "description": {
        "content": "Automatic playbook to update the SOAR case with information from Salesforce.",
        "format": "text"
      },
      "display_name": "Salesforce: Update Case in SOAR",
      "export_key": "salesforce_update_case",
      "field_type_handle": "playbook_a6db8735_3d90_4c38_866d_2f91ca038490",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Case in SOAR",
        "export_key": "playbook_a6db8735_3d90_4c38_866d_2f91ca038490",
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
        "type_name": "playbook_a6db8735_3d90_4c38_866d_2f91ca038490",
        "uuid": "1346233d-247b-4bf3-8843-241983196d3a"
      },
      "has_logical_errors": false,
      "id": 126,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785807846,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785806781,
          "description": "Update the salesforce account name custom field with the information from salesforce.",
          "enabled": false,
          "export_key": "Salesforce: Update Account Name",
          "id": 106,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785806836,
          "name": "Salesforce: Update Account Name",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case",
          "programmatic_name": "salesforce_update_case_salesforce_update_account_name",
          "script_text": "results = playbook.functions.results.account_details\n\nif results.success:\n  content = results.get(\"content\", {})\n  if content:\n    account = content.get(\"salesforce_account\", None)\n    if account:\n      incident.properties.salesforce_account_name = account.get(\"Name\")\n    else:\n      incident.addNote(\"Salesforce: unable to get account details for Account Id\")\n  else:\n      incident.addNote(\"Salesforce: unable to get account details for Account Id\")\nelse:\n  incident.addNote(\"Salesforce: unable to get account details for Account Id \")",
          "tags": [],
          "uuid": "99316570-4aa7-4d81-b6c5-e42b05ea7b2f"
        },
        {
          "actions": [],
          "created_date": 1704785806839,
          "description": "Update the case in SOAR with the data from the case in Salesforce.",
          "enabled": false,
          "export_key": "Salesforce: Update case in SOAR",
          "id": 107,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785806901,
          "name": "Salesforce: Update case in SOAR",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case",
          "programmatic_name": "salesforce_update_case_salesforce_update_case_in_soar",
          "script_text": "results = playbook.functions.results.salesforce_case_results\n\nTYPE_LOOKUP = {\n  \u0027None\u0027: \"TBD / Unknown\",\n  \u0027Communication error (fax; email)\u0027 : \u0027Communication error (fax; email)\u0027,\n  \u0027Customization Packages (internal)\u0027: \u0027Customization Packages (internal)\u0027,\n  \u0027Denial of Service\u0027:                 \u0027Denial of Service\u0027,\n  \u0027Improper disposal: digital assets\u0027: \u0027Improper disposal: digital assets\u0027,\n  \u0027Improper disposal: documents / files / records\u0027: \u0027Improper disposal: documents / files / records\u0027,\n  \u0027Lost documents / files / records\u0027:  \u0027Lost documents / files / records\u0027,\n  \u0027Lost PC / laptop / tablet\u0027:         \u0027Lost PC / laptop / tablet\u0027,\n  \u0027Lost storage device / media\u0027:       \u0027Lost storage device / media\u0027,\n  \u0027Malware\u0027:                           \u0027Malware\u0027,\n  \u0027Not an Issue\u0027:                      \u0027Not an Issue\u0027,\n  \u0027Other\u0027:                             \u0027Other\u0027,\n  \u0027Phishing\u0027:                          \u0027Phishing\u0027,\n  \u0027Stolen documents / files / records\u0027:\u0027Stolen documents / files / records\u0027,\n  \u0027Stolen PC / laptop / tablet\u0027:       \u0027Stolen PC / laptop / tablet\u0027,\n  \u0027Stolen PDA / smartphone\u0027:           \u0027Stolen PDA / smartphone\u0027,\n  \u0027Stolen storage device / media\u0027:     \u0027Stolen storage device / media\u0027,\n  \u0027System Intrusion\u0027:                  \u0027System Intrusion\u0027,\n  \u0027TBD / Unknown\u0027:                     \u0027TBD / Unknown\u0027,\n  \u0027Vendor / 3rd party error\u0027:          \u0027Vendor / 3rd party error\u0027\n}\n\n\nif not results.success:\n    incident.addNote(\"Salesforce: Update custom fields: Unable to get case data to update custom fields.\")\nelse:\n    content = results.get(\"content\", {})\n    sf_case =content.get(\"salesforce_case\")\n    incident.properties.salesforce_account_id = sf_case.get(\"AccountId\")\n    incident.properties.salesforce_contact_id = sf_case.get(\"ContactId\")\n    incident.properties.salesforce_owner_id = sf_case.get(\"OwnerId\")\n    incident.properties.salesforce_case_number = sf_case.get(\"CaseNumber\")\n    incident.properties.salesforce_case_type = TYPE_LOOKUP.get(sf_case.get(\"Type\"), \"None\")\n    incident.properties.salesforce_contact_phone = sf_case.get(\"ContactPhone\")\n    incident.properties.salesforce_contact_email = sf_case.get(\"ContactEmail\")    \n    incident.properties.salesforce_contact_fax = sf_case.get(\"ContactFax\")\n    incident.properties.salesforce_supplied_name = sf_case.get(\"SuppliedName\")\n    incident.properties.salesforce_supplied_phone = sf_case.get(\"SuppliedPhone\")\n    incident.properties.salesforce_supplied_email = sf_case.get(\"SuppliedEmail\")    \n    incident.properties.salesforce_supplied_company = sf_case.get(\"SuppliedCompany\")\n    incident.properties.salesforce_origin = sf_case.get(\"Origin\")\n    incident.properties.salesforce_status = sf_case.get(\"Status\")\n    entity_url = sf_case.get(\"entity_url\", None)\n    if entity_url:\n      incident.properties.salesforce_case_link = \"\u003ca target=\u0027_blank\u0027 href=\u0027{0}\u0027\u003e{1}\u003c/a\u003e\".format(entity_url, sf_case.get(\"CaseNumber\"))\n      \n    # Add Salesforce case Comments as a note\n    sf_case_comments = sf_case.get(\"Comments\", None)\n    if sf_case_comments:\n        incident.addNote(helper.createRichText(\"\u003cb\u003eCreated by Salesforce:\u003c/b\u003e\u003cbr\u003e {}\".format(sf_case_comments)))",
          "tags": [],
          "uuid": "322f86b9-0a67-4ad1-a53c-97dac97b17fb"
        },
        {
          "actions": [],
          "created_date": 1704785806903,
          "description": "Update the Contact Name in SOAR custom field",
          "enabled": false,
          "export_key": "Salesforce: Update Contact",
          "id": 108,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785806963,
          "name": "Salesforce: Update Contact",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case",
          "programmatic_name": "salesforce_update_case_salesforce_update_contact",
          "script_text": "results = playbook.functions.results.contact_results\n\nif results.success:\n    content = results.get(\"content\", {})\n    contact = content.get(\"salesforce_contact\")\n    if contact:\n        incident.properties.salesforce_contact_name = contact.get(\"Name\", \"\")\n    else:\n        incident.addNote(\"Unable to get Contact information from ContactId\")\nelse:\n  incident.addNote(\"Unable to get Contact information from ContactId\")\n  ",
          "tags": [],
          "uuid": "f0a27b7a-8f37-43f7-8b07-4d9be6fcb977"
        },
        {
          "actions": [],
          "created_date": 1704785806966,
          "description": "Update the user custom field with information from the function results.",
          "enabled": false,
          "export_key": "Salesforce: Update User information",
          "id": 109,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785807029,
          "name": "Salesforce: Update User information",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case",
          "programmatic_name": "salesforce_update_case_salesforce_update_user_information",
          "script_text": "results = playbook.functions.results.user_results\n\nif results.success:\n    content = results.get(\"content\", {})\n    sf_user = content.get(\"salesforce_user\")\n    incident.properties.salesforce_user_name = sf_user.get(\"Name\", \"\")\nelse:\n  incident.addNote(\"Unable to get User information from  UserId: {}\".format(playbook.functions.results.inputs.salesforce_user_id))",
          "tags": [],
          "uuid": "234cc375-a5c1-4e7a-b78f-7b49ffb16273"
        }
      ],
      "name": "salesforce_update_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a6db8735-3d90-4c38-866d-2f91ca038490",
        "id": 143,
        "name": "playbook_a6db8735_3d90_4c38_866d_2f91ca038490",
        "type": "playbook",
        "uuid": "8d8b0014-f023-4b05-9ec8-b511c035cadf"
      },
      "tags": [],
      "type": "default",
      "uuid": "a6db8735-3d90-4c38-866d-2f91ca038490",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_c53f6cfd_04c9_4713_9806_7758148cba62\" isExecutable=\"true\" name=\"playbook_c53f6cfd_04c9_4713_9806_7758148cba62\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_134aeuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Update Case Status\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5639e9ca-ac5f-421e-9f87-5d9638a8cf67\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_case_id = incident.properties.salesforce_case_id\\ninputs.salesforce_case_status = playbook.inputs.salesforce_case_status\\ninputs.salesforce_case_comment = playbook.inputs.salesforce_case_comment\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_status\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_134aeuk\u003c/incoming\u003e\u003coutgoing\u003eFlow_1bwxtiz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_134aeuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update Status write results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"d952e676-eba0-4b83-8bb4-dfd032366308\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1bwxtiz\u003c/incoming\u003e\u003coutgoing\u003eFlow_09cg46s\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1bwxtiz\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_09cg46s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_09cg46s\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_c53f6cfd_04c9_4713_9806_7758148cba62\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09cg46s\" id=\"Flow_09cg46s_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"32\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"64\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1bwxtiz\" id=\"Flow_1bwxtiz_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"-78\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"-52\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_134aeuk\" id=\"Flow_134aeuk_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"-184\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"-162\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"-236\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"-162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"-52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785807789,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
      "description": {
        "content": "Manual playbook to update the case Status field in Salesforce",
        "format": "text"
      },
      "display_name": "Salesforce: Update Case Status in Salesforce",
      "export_key": "salesforce_update_case_status_manual",
      "field_type_handle": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Case Status in Salesforce",
        "export_key": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
        "fields": {
          "salesforce_case_comment": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62/salesforce_case_comment",
            "hide_notification": false,
            "id": 1658,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_comment",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Comment",
            "tooltip": "Optional: Comment sent to Salesforce case.",
            "type_id": 1146,
            "uuid": "5f474f5c-8285-4ad7-8d1a-b5e17fb417c3",
            "values": []
          },
          "salesforce_case_status": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62/salesforce_case_status",
            "hide_notification": false,
            "id": 1659,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "salesforce_case_status",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Status",
            "tooltip": "",
            "type_id": 1146,
            "uuid": "ebf31fae-9de5-47da-bd82-e8e6553d98de",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "New",
                "properties": null,
                "uuid": "b9b34135-aa12-4116-b503-86f000069164",
                "value": 1404
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Working",
                "properties": null,
                "uuid": "234d68ee-ad37-4751-a921-f79d73131194",
                "value": 1405
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Escalated",
                "properties": null,
                "uuid": "6b566249-d08a-4c8d-bb23-f3044a005da3",
                "value": 1406
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "In Progress",
                "properties": null,
                "uuid": "03432e3b-65f0-4ad1-a264-0d24ef0f0042",
                "value": 1407
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "On Hold",
                "properties": null,
                "uuid": "e079db15-21d2-4d30-95cc-d76b36182211",
                "value": 1408
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Waiting for Customer",
                "properties": null,
                "uuid": "c825f499-edda-44af-b70f-9ae65131357d",
                "value": 1409
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Response Received",
                "properties": null,
                "uuid": "8a236f88-5c61-45d8-bf27-c4776caf867e",
                "value": 1410
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Closed",
                "properties": null,
                "uuid": "50d86072-de33-4894-9797-655c0219d893",
                "value": 1411
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
        "type_name": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
        "uuid": "83cd18f8-8a34-40a0-be7f-911b92fc736d"
      },
      "has_logical_errors": false,
      "id": 127,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785809066,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785808180,
          "description": "",
          "enabled": false,
          "export_key": "Salesforce: Update Account Name",
          "id": 110,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785808235,
          "name": "Salesforce: Update Account Name",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case_status_manual",
          "programmatic_name": "salesforce_update_case_status_manual_salesforce_update_account_name",
          "script_text": "results = playbook.functions.account_details\n\nif results.success:\n  content = results.get(\"content\", {})\n  if content:\n    account = content.get(\"salesforce_account\", None)\n    incident.properties.account_name = account.get(\"Name\")\nelse:\n  incident.addNote(\"Salesforce unable to get account details for Account Id {0}\".format(playbook.functions.inputs.salesforce_account_id))",
          "tags": [],
          "uuid": "2564a146-28bb-4fe5-85ec-baf03b0559ea"
        },
        {
          "actions": [],
          "created_date": 1704785808237,
          "description": "Write the results from Update Status to a note",
          "enabled": false,
          "export_key": "Salesforce: Update Status write results",
          "id": 111,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785808296,
          "name": "Salesforce: Update Status write results",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_case_status_manual",
          "programmatic_name": "salesforce_update_case_status_manual_salesforce_update_status_write_results",
          "script_text": "update_status = playbook.functions.results.update_status\n\nif not update_status.success:\n  incident.addNote(\"Salesforce: ERROR: Unable to Update Case Status to \u003cb\u003e{}\u003c/b\u003e\".format(update_status.inputs.salesforce_case_status))\nelse:\n  incident.properties.salesforce_status = update_status.inputs.salesforce_case_status\n  incident.addNote(\"Salesforce: Updated Case Status to \u003cb\u003e{}\u003c/b\u003e in Salesforce\".format(incident.properties.salesforce_status))",
          "tags": [],
          "uuid": "d952e676-eba0-4b83-8bb4-dfd032366308"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "ebf31fae-9de5-47da-bd82-e8e6553d98de",
            "element": "field_uuid",
            "field_type": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "5f474f5c-8285-4ad7-8d1a-b5e17fb417c3",
            "element": "field_uuid",
            "field_type": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "salesforce_update_case_status_manual",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_c53f6cfd-04c9-4713-9806-7758148cba62",
        "id": 144,
        "name": "playbook_c53f6cfd_04c9_4713_9806_7758148cba62",
        "type": "playbook",
        "uuid": "239b96be-de34-49f4-8ff8-d7546dacf5fe"
      },
      "tags": [],
      "type": "default",
      "uuid": "c53f6cfd-04c9-4713-9806-7758148cba62",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1\" isExecutable=\"true\" name=\"playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1rqvbwk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Case Comments\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8e4f5ac0-996d-400f-b84d-0e2e5cd9fe4c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\ninputs.salesforce_case_id = incident.properties.salesforce_case_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_comments_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1rqvbwk\u003c/incoming\u003e\u003coutgoing\u003eFlow_0wl6ab0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1rqvbwk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0wl6ab0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0wl6ab0\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0wl6ab0\" id=\"Flow_0wl6ab0_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"232\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1rqvbwk\" id=\"Flow_1rqvbwk_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"148\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"148\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785809006,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1",
      "description": {
        "content": "Get the comments from the specified Salesforce case and update the notes in corresponding  SOAR case.",
        "format": "text"
      },
      "display_name": "Salesforce: Update Comments from Salesforce Case",
      "export_key": "salesforce_update_comments_from_salesforce_case",
      "field_type_handle": "playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Comments from Salesforce Case",
        "export_key": "playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1",
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
        "type_name": "playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1",
        "uuid": "44d1bc72-7ac0-41bc-a68f-eecedef4ced2"
      },
      "has_logical_errors": false,
      "id": 128,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785809907,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_update_comments_from_salesforce_case",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_c9f4a766-2b98-4676-a125-15af20ebdfe1",
        "id": 145,
        "name": "playbook_c9f4a766_2b98_4676_a125_15af20ebdfe1",
        "type": "playbook",
        "uuid": "aa6e30ed-46aa-487d-9f34-2cac79f1b523"
      },
      "tags": [],
      "type": "default",
      "uuid": "c9f4a766-2b98-4676-a125-15af20ebdfe1",
      "version": 4
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_contact_id",
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
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746\" isExecutable=\"true\" name=\"playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0fg8fwm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Contact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"777154b4-dc0c-4d8d-ac3b-7a3cd9523255\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_contact_id = incident.properties.salesforce_contact_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"contact_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ovnkma\u003c/incoming\u003e\u003coutgoing\u003eFlow_145slnd\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0fg8fwm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ConditionPoint_4\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Update Contact details when ContactId changes\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"f4a8a543-1cd0-43be-890a-78758acc70b5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_145slnd\u003c/incoming\u003e\u003coutgoing\u003eFlow_18t471j\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_145slnd\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_18t471j\u003c/incoming\u003e\u003cincoming\u003eFlow_1hujm7t\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_18t471j\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003cexclusiveGateway default=\"Flow_1r4y1o9\" id=\"ConditionPoint_4\" resilient:documentation=\"Condition point\"\u003e\u003cextensionElements/\u003e\u003cincoming\u003eFlow_0fg8fwm\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ovnkma\u003c/outgoing\u003e\u003coutgoing\u003eFlow_1r4y1o9\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cscriptTask id=\"ScriptTask_5\" name=\"Salesforce: Set Contact custom fields to None\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3f7ca671-2968-451c-8f43-70345114bb9c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1r4y1o9\u003c/incoming\u003e\u003coutgoing\u003eFlow_1hujm7t\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1hujm7t\" sourceRef=\"ScriptTask_5\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_0ovnkma\" name=\"Test for ContactId for not null\" sourceRef=\"ConditionPoint_4\" targetRef=\"ServiceTask_1\"\u003e\u003cextensionElements\u003e\u003cresilient:condition label=\"Test for ContactId for not null\" order=\"0\"/\u003e\u003c/extensionElements\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":null,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"script_text\":\"# One line example:\\n#\\n# result = incident.employee_involved = True\\n#\\n# Multi-line example:\\n#\\n# certificate_expired = playbook.functions.results.certificate_results.is_expired\\n# if (incident.employee_involved == True and certificate_expired):\\n#     result = True\\n# else:\\n#     result = False\\nif incident.properties.salesforce_contact_id:\\n  result = True\\nelse:\\n  result = False\",\"final_expression_text\":\"result\",\"final_expression_only_boolean\":true,\"language\":\"python3\"}}],\"logic_type\":\"all\",\"script_language\":null}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"Flow_1r4y1o9\" name=\"Else\" sourceRef=\"ConditionPoint_4\" targetRef=\"ScriptTask_5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1r4y1o9\" id=\"Flow_1r4y1o9_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"-134\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"-50\"/\u003e\u003comgdi:waypoint x=\"880\" y=\"-50\"/\u003e\u003comgdi:waypoint x=\"880\" y=\"-22\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"23\" x=\"798\" y=\"-79\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ovnkma\" id=\"Flow_0ovnkma_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"-134\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"-103\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"-103\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"-62\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"90\" x=\"590\" y=\"-123\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1hujm7t\" id=\"Flow_1hujm7t_di\"\u003e\u003comgdi:waypoint x=\"880\" y=\"62\"/\u003e\u003comgdi:waypoint x=\"880\" y=\"150\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"150\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"184\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_18t471j\" id=\"Flow_18t471j_di\"\u003e\u003comgdi:waypoint x=\"648\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"184\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_145slnd\" id=\"Flow_145slnd_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fg8fwm\" id=\"Flow_0fg8fwm_di\"\u003e\u003comgdi:waypoint x=\"710\" y=\"-224\"/\u003e\u003comgdi:waypoint x=\"710\" y=\"-186\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"616\" y=\"-276\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"452\" y=\"-62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"452\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"643.542\" y=\"183.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ConditionPoint_4\" id=\"ConditionPoint_4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"52\" width=\"243.6\" x=\"588\" y=\"-186.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_5\" id=\"ScriptTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"782\" y=\"-22.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785809855,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746",
      "description": {
        "content": "Automatic playbook to update the Contact details in SOAR when the ContactId has changed.",
        "format": "text"
      },
      "display_name": "Salesforce: Update Contact Details in SOAR",
      "export_key": "salesforce_update_contact_details_in_soar",
      "field_type_handle": "playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Contact Details in SOAR",
        "export_key": "playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746",
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
        "type_name": "playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746",
        "uuid": "09978786-1bfd-4d71-a492-20e3baf06889"
      },
      "has_logical_errors": false,
      "id": 129,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785811094,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785810090,
          "description": "Set contact custom fields to None when ContactId is null ",
          "enabled": false,
          "export_key": "Salesforce: Set Contact custom fields to None",
          "id": 112,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785810148,
          "name": "Salesforce: Set Contact custom fields to None",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_contact_details_in_soar",
          "programmatic_name": "salesforce_update_contact_details_in_soar_salesforce_set_account_fields_to_none",
          "script_text": "incident.properties.salesforce_contact_name = None\nincident.properties.salesforce_contact_email = None\nincident.properties.salesforce_contact_fax = None\nincident.properties.salesforce_contact_phone = None",
          "tags": [],
          "uuid": "3f7ca671-2968-451c-8f43-70345114bb9c"
        },
        {
          "actions": [],
          "created_date": 1704785810150,
          "description": "Update the Salesforce custom fields in SOAR when the ContactId is changed.",
          "enabled": false,
          "export_key": "Salesforce: Update Contact details when ContactId changes",
          "id": 113,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785810240,
          "name": "Salesforce: Update Contact details when ContactId changes",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_contact_details_in_soar",
          "programmatic_name": "salesforce_update_contact_details_in_soar_salesforce_update_contact_details_when_contactid_changes",
          "script_text": "results = playbook.functions.results.contact_results\n\nif results.success:\n    content = results.get(\"content\", {})\n    contact = content.get(\"salesforce_contact\")\n    if contact:\n        incident.properties.salesforce_contact_name = contact.get(\"Name\")\n        incident.properties.salesforce_contact_phone = contact.get(\"Phone\")\n        incident.properties.salesforce_contact_email = contact.get(\"Email\")\n        incident.properties.salesforce_contact_fax = contact.get(\"Fax\")\nelse:\n  incident.addNote(\"Unable to get Contact information from ContactId\")\n  ",
          "tags": [],
          "uuid": "f4a8a543-1cd0-43be-890a-78758acc70b5"
        }
      ],
      "name": "salesforce_update_contact_details_in_soar",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_cc4762df-970f-45b8-9fdd-bae6e9ee4746",
        "id": 146,
        "name": "playbook_cc4762df_970f_45b8_9fdd_bae6e9ee4746",
        "type": "playbook",
        "uuid": "1e2e5168-cc2f-41d6-a91b-afa5ed4fc27d"
      },
      "tags": [],
      "type": "default",
      "uuid": "cc4762df-970f-45b8-9fdd-bae6e9ee4746",
      "version": 4
    },
    {
      "activation_details": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_owner_id",
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
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9\" isExecutable=\"true\" name=\"playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_09z0qqd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1agz6pw\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_3\" name=\"Salesforce: Get User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7bafb91-836b-4aa4-b8b9-1b167d9fc96b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_user_id = incident.properties.salesforce_owner_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_user_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_09z0qqd\u003c/incoming\u003e\u003coutgoing\u003eFlow_1tbn0n7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_09z0qqd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"Salesforce: Update Case Owner details in SOAR\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a2965e45-a6a9-4dd6-a9a7-d82c00ff315e\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tbn0n7\u003c/incoming\u003e\u003coutgoing\u003eFlow_1agz6pw\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1tbn0n7\" sourceRef=\"ServiceTask_3\" targetRef=\"ScriptTask_4\"/\u003e\u003csequenceFlow id=\"Flow_1agz6pw\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1agz6pw\" id=\"Flow_1agz6pw_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"334\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tbn0n7\" id=\"Flow_1tbn0n7_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"142\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_09z0qqd\" id=\"Flow_09z0qqd_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"6\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"-46\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"334\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_3\" id=\"ServiceTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623.484\" y=\"57.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623.484\" y=\"197.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785811037,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9",
      "description": {
        "content": "Get the Case Owner details and update the Case Owner field in the SOAR case.",
        "format": "text"
      },
      "display_name": "Salesforce: Update Owner Details in SOAR",
      "export_key": "salesforce_update_owner_details_in_soar",
      "field_type_handle": "playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Update Owner Details in SOAR",
        "export_key": "playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9",
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
        "type_name": "playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9",
        "uuid": "3c1f3b6d-b504-4bab-aa59-0569cafe1c61"
      },
      "has_logical_errors": false,
      "id": 130,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785812120,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785811287,
          "description": "Update the Case Owner custom field in SOAR with information from the User in Salesforce.",
          "enabled": false,
          "export_key": "Salesforce: Update Case Owner details in SOAR",
          "id": 114,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785811342,
          "name": "Salesforce: Update Case Owner details in SOAR",
          "object_type": "incident",
          "playbook_handle": "salesforce_update_owner_details_in_soar",
          "programmatic_name": "salesforce_update_owner_details_in_soar_salesforce_update_case_owner_details_in_soar",
          "script_text": "results = playbook.functions.results.get_user_results\n\nif results.success:\n    content = results.get(\"content\", {})\n    user = content.get(\"salesforce_user\")\n    if user:\n        incident.properties.salesforce_case_owner = user.get(\"Name\", \"\")\nelse:\n  incident.addNote(\"Unable to get User information from OwnerId\")\n  ",
          "tags": [],
          "uuid": "a2965e45-a6a9-4dd6-a9a7-d82c00ff315e"
        }
      ],
      "name": "salesforce_update_owner_details_in_soar",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_25e0244c-c93a-44bd-a0f2-5922c14699a9",
        "id": 147,
        "name": "playbook_25e0244c_c93a_44bd_a0f2_5922c14699a9",
        "type": "playbook",
        "uuid": "3c88695f-38b4-4cb5-9489-f9a95fd72bd4"
      },
      "tags": [],
      "type": "default",
      "uuid": "25e0244c-c93a-44bd-a0f2-5922c14699a9",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537\" isExecutable=\"true\" name=\"playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1ydckvs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Account\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ce27c1d7-8c77-45a4-ba6b-209c79f44192\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_account_id = incident.properties.salesforce_account_id if incident.properties.salesforce_account_id else helper.fail(\\\"Error: AccountId is None\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"account_details\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ydckvs\u003c/incoming\u003e\u003coutgoing\u003eFlow_0l348n5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_1ydckvs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write Account information\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dd5cbb4d-6cb3-425a-9b66-30f24f7c0060\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0l348n5\u003c/incoming\u003e\u003coutgoing\u003eFlow_1cmimnu\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1cmimnu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0l348n5\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1cmimnu\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1cmimnu\" id=\"Flow_1cmimnu_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"372\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"434\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0l348n5\" id=\"Flow_0l348n5_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"288\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ydckvs\" id=\"Flow_1ydckvs_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"288\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"434\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785812064,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537",
      "description": {
        "content": "Get information on the Salesforce account associated with a case and write to a SOAR note.",
        "format": "text"
      },
      "display_name": "Salesforce: Write Account Details to Note",
      "export_key": "salesforce_get_account",
      "field_type_handle": "playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Write Account Details to Note",
        "export_key": "playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537",
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
        "type_name": "playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537",
        "uuid": "ba9d0749-22c8-4716-a10e-c37d7f0f7d0e"
      },
      "has_logical_errors": false,
      "id": 131,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785813064,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785812308,
          "description": "Write account information to a note.",
          "enabled": false,
          "export_key": "Salesforce: Write Account information",
          "id": 115,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785812363,
          "name": "Salesforce: Write Account information",
          "object_type": "incident",
          "playbook_handle": "salesforce_get_account",
          "programmatic_name": "salesforce_get_account_salesforce_write_account_information",
          "script_text": "import json\n\nresults = playbook.functions.results.account_details\n\nif results.success:\n  content = results.get(\"content\", {})\n  account = content.get(\"salesforce_account\", {})\n  note_text = \"Account Details: \u003cbr\u003e{0}\".format(json.dumps(account, indent=4))\n  incident.addNote(helper.createRichText(note_text))\nelse:\n  incident.addNote(\"Unable to get Account details from Salesforce.\")",
          "tags": [],
          "uuid": "dd5cbb4d-6cb3-425a-9b66-30f24f7c0060"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_get_account",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_43b42c04-a20e-4b8c-813d-4869ad5c7537",
        "id": 148,
        "name": "playbook_43b42c04_a20e_4b8c_813d_4869ad5c7537",
        "type": "playbook",
        "uuid": "13b3e8d2-04c7-41d3-a0e5-e4c9c653795e"
      },
      "tags": [],
      "type": "default",
      "uuid": "43b42c04-a20e-4b8c-813d-4869ad5c7537",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a\" isExecutable=\"true\" name=\"playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0rjwdyh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get Contact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"777154b4-dc0c-4d8d-ac3b-7a3cd9523255\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_contact_id = incident.properties.salesforce_contact_id if incident.properties.salesforce_contact_id else helper.fail(\\\"Error: ContactId is None\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"contact_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0rjwdyh\u003c/incoming\u003e\u003coutgoing\u003eFlow_1f4x8qf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0rjwdyh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write Contact details to a note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"edc2d7a4-9ffe-474d-af0c-b4076b97aa84\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1f4x8qf\u003c/incoming\u003e\u003coutgoing\u003eFlow_01hrj53\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1f4x8qf\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_01hrj53\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_01hrj53\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_01hrj53\" id=\"Flow_01hrj53_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"404\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1f4x8qf\" id=\"Flow_1f4x8qf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0rjwdyh\" id=\"Flow_0rjwdyh_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"404\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785813010,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a",
      "description": {
        "content": "Manual playbook to get the Contact information associated with the Salesforce case.  Write the details to a note in SOAR.",
        "format": "text"
      },
      "display_name": "Salesforce: Write Contact Details to Note",
      "export_key": "salesforce_get_contact",
      "field_type_handle": "playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Write Contact Details to Note",
        "export_key": "playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a",
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
        "type_name": "playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a",
        "uuid": "5916c9d4-426a-4fe1-bb52-34dee36624ed"
      },
      "has_logical_errors": false,
      "id": 132,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785814039,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785813250,
          "description": "Write the JSON results from call to Get Contact function to a note in SOAR.",
          "enabled": false,
          "export_key": "Salesforce: Write Contact details to a note",
          "id": 116,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785813305,
          "name": "Salesforce: Write Contact details to a note",
          "object_type": "incident",
          "playbook_handle": "salesforce_get_contact",
          "programmatic_name": "salesforce_get_contact_salesforce_write_contact_details_to_a_note",
          "script_text": "import json\n\nresults = playbook.functions.results.contact_results\n\nif results.success:\n  content = results.get(\"content\", {})\n  contact = content.get(\"salesforce_contact\", {})\n  note_text = \"Contact Details: \u003cbr\u003e{0}\".format(json.dumps(contact, indent=4))\n  incident.addNote(helper.createRichText(note_text))\nelse:\n  incident.addNote(\"Unable to get Contact details from Salesforce.\")",
          "tags": [],
          "uuid": "edc2d7a4-9ffe-474d-af0c-b4076b97aa84"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_get_contact",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_9096e28f-a667-43f0-8f87-a1f6e37db51a",
        "id": 149,
        "name": "playbook_9096e28f_a667_43f0_8f87_a1f6e37db51a",
        "type": "playbook",
        "uuid": "a048505e-ae21-4d54-9adb-44b714a53e46"
      },
      "tags": [],
      "type": "default",
      "uuid": "9096e28f-a667-43f0-8f87-a1f6e37db51a",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f\" isExecutable=\"true\" name=\"playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0ax2b41\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Salesforce: Get User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7bafb91-836b-4aa4-b8b9-1b167d9fc96b\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.salesforce_user_id = incident.properties.salesforce_owner_id if incident.properties.salesforce_owner_id else helper.fail(\\\"Error: OwnerId is None\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"get_user_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ax2b41\u003c/incoming\u003e\u003coutgoing\u003eFlow_0enqke2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0ax2b41\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Salesforce: Write Owner (User) details to an SOAR note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"e912625b-5e8e-44d0-b4ee-3cf3c969a81c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0enqke2\u003c/incoming\u003e\u003coutgoing\u003eFlow_1x4sgmw\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0enqke2\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1x4sgmw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1x4sgmw\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1x4sgmw\" id=\"Flow_1x4sgmw_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"362\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"414\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0enqke2\" id=\"Flow_0enqke2_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"232\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"278\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ax2b41\" id=\"Flow_0ax2b41_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"148\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"148\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"278\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"414\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1704785813985,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f",
      "description": {
        "content": "Write the User details of the Case Owner in Salesforce to a SOAR incident Note.",
        "format": "text"
      },
      "display_name": "Salesforce: Write Owner Details to Note",
      "export_key": "salesforce_write_owner_details_to_note",
      "field_type_handle": "playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f",
      "fields_type": {
        "actions": [],
        "display_name": "Salesforce: Write Owner Details to Note",
        "export_key": "playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f",
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
        "type_name": "playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f",
        "uuid": "0a5a8023-91a4-4b7e-b5e6-f03732606da4"
      },
      "has_logical_errors": false,
      "id": 133,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1704785815021,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1704785814232,
          "description": "Write the JSON results from Get User function to a SOAR note.",
          "enabled": false,
          "export_key": "Salesforce: Write Owner (User) details to an SOAR note",
          "id": 117,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1704785814290,
          "name": "Salesforce: Write Owner (User) details to an SOAR note",
          "object_type": "incident",
          "playbook_handle": "salesforce_write_owner_details_to_note",
          "programmatic_name": "salesforce_write_owner_details_to_note_salesforce_write_owner_user_details_to_an_soar_note",
          "script_text": "import json\n\nresults = playbook.functions.results.get_user_results\n\nif results.success:\n  content = results.get(\"content\", {})\n  user = content.get(\"salesforce_user\", {})\n  note_text = \"Owner Details: \u003cbr\u003e{0}\".format(json.dumps(user, indent=4))\n  incident.addNote(helper.createRichText(note_text))\nelse:\n  incident.addNote(\"Unable to get User details from Salesforce.\")",
          "tags": [],
          "uuid": "e912625b-5e8e-44d0-b4ee-3cf3c969a81c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "incident.properties.salesforce_case_id",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "salesforce_write_owner_details_to_note",
      "object_type": "incident",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_35a6e1dd-f0fe-4773-bfa4-6335ee30b84f",
        "id": 150,
        "name": "playbook_35a6e1dd_f0fe_4773_bfa4_6335ee30b84f",
        "type": "playbook",
        "uuid": "91a795a7-8eee-4399-a92a-ce6365f75a4f"
      },
      "tags": [],
      "type": "default",
      "uuid": "35a6e1dd-f0fe-4773-bfa4-6335ee30b84f",
      "version": 4
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
  "types": [],
  "workflows": [],
  "workspaces": []
}
