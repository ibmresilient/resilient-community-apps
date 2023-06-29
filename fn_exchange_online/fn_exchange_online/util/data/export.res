{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1688018678565,
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
      "export_key": "__function/exo_email_address_sender",
      "hide_notification": false,
      "id": 670,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_email_address_sender",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user@example.com",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_email_address_sender",
      "tooltip": "Search messages sent from this email address; leave blank to ignore sender attribute",
      "type_id": 11,
      "uuid": "8dd46926-b1dc-4d1e-ab6a-4239510b199d",
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
      "export_key": "__function/exo_meeting_email_address",
      "hide_notification": false,
      "id": 678,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_email_address",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user@example.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_email_address",
      "tooltip": "Email address of meeting coordinator",
      "type_id": 11,
      "uuid": "97ddc0f2-0b9f-478b-8c2b-21f9f92d3c8f",
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
      "export_key": "__function/exo_query_output_format",
      "hide_notification": false,
      "id": 677,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "exo_query_output_format",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_query_output_format",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9e58d3a3-c54b-4a9b-9164-e6cc0832f644",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Exchange Online data table",
          "properties": null,
          "uuid": "68133b08-816e-4c03-a50d-c68af1b6b205",
          "value": 206
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Incident attachment",
          "properties": null,
          "uuid": "29fa8b3f-4fe5-419c-bda7-223af2c259cb",
          "value": 207
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Incident note",
          "properties": null,
          "uuid": "172c46ba-f424-42eb-b44d-9f66fb7190cd",
          "value": 208
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
      "export_key": "__function/exo_meeting_start_time",
      "hide_notification": false,
      "id": 655,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_start_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_start_time",
      "tooltip": "Meeting start date and time",
      "type_id": 11,
      "uuid": "a37feeea-a655-477c-a52d-9aa63d381a75",
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
      "export_key": "__function/exo_destination_mailfolder_id",
      "hide_notification": false,
      "id": 657,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "exo_destination_mailfolder_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_destination_mailfolder_id",
      "tooltip": "Destination folder to which message is moved",
      "type_id": 11,
      "uuid": "b9765902-10bb-4a92-819e-25d3e346c3b3",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "archive",
          "properties": null,
          "uuid": "f95a7ba4-7026-47fe-ad12-fbcc7ae0bb48",
          "value": 191
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "clutter",
          "properties": null,
          "uuid": "50d01161-eeb1-4ecf-8461-2071ba2e91d9",
          "value": 192
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "conflicts",
          "properties": null,
          "uuid": "85acaa9c-c0c2-4905-bc97-dab8d16f5ff0",
          "value": 193
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "conversationhistory",
          "properties": null,
          "uuid": "d0bfcaa3-c096-4a18-86a2-3c72f53b830f",
          "value": 194
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "deleteditems",
          "properties": null,
          "uuid": "67303ab0-25b2-4f22-ac3b-c7527b01cec9",
          "value": 195
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "drafts",
          "properties": null,
          "uuid": "3b2eb160-f417-4de4-aca2-247e2f2649ac",
          "value": 196
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "inbox",
          "properties": null,
          "uuid": "90830c93-6889-47b4-a57b-c03c942f0064",
          "value": 197
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "junkemail",
          "properties": null,
          "uuid": "9c20f34a-363a-4e70-8d68-2f0a3cadfc44",
          "value": 198
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "localfailures",
          "properties": null,
          "uuid": "4518d80f-fe86-463f-b64f-7e52de04938b",
          "value": 199
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "msgfolderroot",
          "properties": null,
          "uuid": "3ca0f058-855d-49ef-b3c6-9d8f279ae0c2",
          "value": 200
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "outbox",
          "properties": null,
          "uuid": "eb14de74-882f-429b-bb28-bd21a476a1ad",
          "value": 201
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "recoverableitemsdeletions",
          "properties": null,
          "uuid": "20dee080-43d5-423c-85ea-8b2f7b73768a",
          "value": 202
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "scheduled",
          "properties": null,
          "uuid": "7382a392-4576-41b5-a09e-54f8c6d0fa4b",
          "value": 203
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "searchfolders",
          "properties": null,
          "uuid": "5a356a79-f091-4ca0-8b5b-e3084db013b4",
          "value": 204
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "sentitems",
          "properties": null,
          "uuid": "0d797e5c-03a2-4c63-91b7-d6d538171b68",
          "value": 205
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
      "export_key": "__function/exo_meeting_optional_attendees",
      "hide_notification": false,
      "id": 662,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_optional_attendees",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user1@example.com, user2@example.com",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_optional_attendees",
      "tooltip": "Comma separated list of optional attendee email addresses",
      "type_id": 11,
      "uuid": "dd894f14-46f7-4561-85be-d2817613575a",
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
      "id": 676,
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
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "the id of the incident",
      "type_id": 11,
      "uuid": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "export_key": "__function/exo_query_messages_results",
      "hide_notification": false,
      "id": 659,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_query_messages_results",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_query_messages_results",
      "tooltip": "String containing JSON data results from Query Messages function",
      "type_id": 11,
      "uuid": "ebc9fc5a-bcb6-415c-bd23-795df84f93fc",
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
      "export_key": "__function/exo_has_attachments",
      "hide_notification": false,
      "id": 658,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "exo_has_attachments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_has_attachments",
      "tooltip": "True to include attachments, False to exclude attachments, Unknown to get all",
      "type_id": 11,
      "uuid": "ec20a9f0-1e29-490b-871b-57b05ffbac2e",
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
      "id": 671,
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
      "tags": [
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
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
      "export_key": "__function/exo_meeting_body",
      "hide_notification": false,
      "id": 653,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_body",
      "tooltip": "Meeting message body",
      "type_id": 11,
      "uuid": "feaa5784-5830-482b-9406-da9f9ef2b65a",
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
      "export_key": "__function/exo_messages_id",
      "hide_notification": false,
      "id": 672,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_messages_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_messages_id",
      "tooltip": "The message ID of the message to be deleted",
      "type_id": 11,
      "uuid": "00ca7e22-f9fa-4477-a056-602139d0dbd0",
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
      "export_key": "__function/exo_message_body",
      "hide_notification": false,
      "id": 675,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_message_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "message body text",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_message_body",
      "tooltip": "message body",
      "type_id": 11,
      "uuid": "06391a1a-0c2c-4bcd-832a-1f39a3ba77b8",
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
      "export_key": "__function/exo_email_address",
      "hide_notification": false,
      "id": 663,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_email_address",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user@example.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_email_address",
      "tooltip": "User email account",
      "type_id": 11,
      "uuid": "092a752f-1297-46a4-bae6-e75d1a9b4804",
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
      "export_key": "__function/exo_start_date",
      "hide_notification": false,
      "id": 673,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "exo_start_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_start_date",
      "tooltip": "Query messages received starting at this date/time.",
      "type_id": 11,
      "uuid": "1c9b3b95-ca24-484c-ad72-f5d64be87402",
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
      "export_key": "__function/exo_attachment_name",
      "hide_notification": false,
      "id": 656,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_attachment_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_attachment_name",
      "tooltip": "The attachment file to which message is written",
      "type_id": 11,
      "uuid": "1f8ead74-4649-4179-9dbd-3e8cf029e3d7",
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
      "export_key": "__function/exo_recipients",
      "hide_notification": false,
      "id": 669,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_recipients",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_recipients",
      "tooltip": "Comma separated list of message recipients",
      "type_id": 11,
      "uuid": "43a3d370-9043-44e8-b54a-7296f805edf8",
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
      "export_key": "__function/exo_meeting_required_attendees",
      "hide_notification": false,
      "id": 661,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_required_attendees",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user1@example.com, user2@example.com",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_required_attendees",
      "tooltip": "Comma separated list of required attendee email addresses",
      "type_id": 11,
      "uuid": "4c789e57-5316-4dae-bfac-bb195fd005c1",
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
      "export_key": "__function/exo_meeting_end_time",
      "hide_notification": false,
      "id": 665,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_end_time",
      "tooltip": "End date and time for meeting",
      "type_id": 11,
      "uuid": "4fba855a-d15c-407f-854e-6cbcd84801ec",
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
      "export_key": "__function/exo_mail_folders",
      "hide_notification": false,
      "id": 664,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_mail_folders",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Inbox",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_mail_folders",
      "tooltip": "The folder to search in the users mailbox",
      "type_id": 11,
      "uuid": "4ff86946-a8cf-4ae1-804b-87cab7d9dac1",
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
      "export_key": "__function/exo_message_subject",
      "hide_notification": false,
      "id": 660,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_message_subject",
      "operation_perms": {},
      "operations": [],
      "placeholder": "message subject",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_message_subject",
      "tooltip": "message subject",
      "type_id": 11,
      "uuid": "51a9c433-07bc-4f04-9932-99211726b9b7",
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
      "export_key": "__function/exo_attachment_names",
      "hide_notification": false,
      "id": 654,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_attachment_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_attachment_names",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5615f985-78ce-418b-a09d-4bdd73c4bd2e",
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
      "export_key": "__function/exo_meeting_subject",
      "hide_notification": false,
      "id": 666,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_subject",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_subject",
      "tooltip": "Meeting Subject",
      "type_id": 11,
      "uuid": "5e38ad9b-0580-4a23-b0d1-e749e29d5b41",
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
      "export_key": "__function/exo_mailfolders_id",
      "hide_notification": false,
      "id": 674,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_mailfolders_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_mailfolders_id",
      "tooltip": "MailFolders ID",
      "type_id": 11,
      "uuid": "669df159-68fd-419f-8678-ad3b93514f8c",
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
      "export_key": "__function/exo_meeting_location",
      "hide_notification": false,
      "id": 667,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "exo_meeting_location",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_meeting_location",
      "tooltip": "",
      "type_id": 11,
      "uuid": "67c027ff-02af-4eb9-98ec-ce23f5eead04",
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
      "export_key": "__function/exo_end_date",
      "hide_notification": false,
      "id": 668,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "exo_end_date",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "templates": [],
      "text": "exo_end_date",
      "tooltip": "Query messages received ending at this date/time",
      "type_id": 11,
      "uuid": "7354f758-b9ea-4029-835d-66d293a22b5d",
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
      "created_date": 1686811440076,
      "description": {
        "content": "This function creates a meeting event in the organizer\u0027s Outlook calendar and sends a calendar event mail message to the meeting participants inviting them to the meeting.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Create Meeting",
      "export_key": "exchange_online_create_meeting",
      "id": 5,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440126,
      "name": "exchange_online_create_meeting",
      "tags": [
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "40e56303-027d-4e27-9865-10ca18d267b3",
      "version": 1,
      "view_items": [
        {
          "content": "97ddc0f2-0b9f-478b-8c2b-21f9f92d3c8f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a37feeea-a655-477c-a52d-9aa63d381a75",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4fba855a-d15c-407f-854e-6cbcd84801ec",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5e38ad9b-0580-4a23-b0d1-e749e29d5b41",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "feaa5784-5830-482b-9406-da9f9ef2b65a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4c789e57-5316-4dae-bfac-bb195fd005c1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dd894f14-46f7-4561-85be-d2817613575a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "67c027ff-02af-4eb9-98ec-ce23f5eead04",
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
      "created_date": 1686811440155,
      "description": {
        "content": "Delete a message in the specified user\u0027s email address mailbox.  The email address of the mailbox and the message id are required input parameters.  The mail folder is an optional parameter.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Delete Message",
      "export_key": "exchange_online_delete_email",
      "id": 6,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440197,
      "name": "exchange_online_delete_email",
      "tags": [
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "e4a2073e-46cf-48a6-b3be-f0f99b05c472",
      "version": 1,
      "view_items": [
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "669df159-68fd-419f-8678-ad3b93514f8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "00ca7e22-f9fa-4477-a056-602139d0dbd0",
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
      "created_date": 1686811440226,
      "description": {
        "content": "This Exchange Online function deletes a list of messages returned from the Query Message function.  The input to the function is a string containing the JSON results from the Query Messages function.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Delete Messages From Query Results",
      "export_key": "exchange_online_delete_messages_from_query_results",
      "id": 7,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440277,
      "name": "exchange_online_delete_messages_from_query_results",
      "tags": [
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "af142c3a-3c38-4352-9bca-fa82d53c61af",
      "version": 1,
      "view_items": [
        {
          "content": "ebc9fc5a-bcb6-415c-bd23-795df84f93fc",
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
      "created_date": 1686811440306,
      "description": {
        "content": "This function gets Exchange Online user profile for a given email address.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Get User Profile",
      "export_key": "exchange_online_get_email_user_profile",
      "id": 8,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440350,
      "name": "exchange_online_get_email_user_profile",
      "tags": [
        {
          "tag_handle": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "f7af9277-dea6-4825-9279-09594d8e0770",
      "version": 1,
      "view_items": [
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
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
      "created_date": 1686811440376,
      "description": {
        "content": "This function returns the contents of an Exchange Online message in JSON format.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Get Message",
      "export_key": "exchange_online_get_message",
      "id": 9,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440419,
      "name": "exchange_online_get_message",
      "tags": [
        {
          "tag_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "c4748898-439e-496a-bbba-93fbc51582c3",
      "version": 1,
      "view_items": [
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "00ca7e22-f9fa-4477-a056-602139d0dbd0",
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
      "created_date": 1686811440446,
      "description": {
        "content": "This function moves an Exchange Online message to the specified folder in the users mailbox.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Move Message to Folder",
      "export_key": "exchange_online_move_message_to_folder",
      "id": 10,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440489,
      "name": "exchange_online_move_message_to_folder",
      "tags": [
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "ec89e514-34f6-4fe3-98ea-85398bb04dd9",
      "version": 1,
      "view_items": [
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "669df159-68fd-419f-8678-ad3b93514f8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "00ca7e22-f9fa-4477-a056-602139d0dbd0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9765902-10bb-4a92-819e-25d3e346c3b3",
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
      "created_date": 1686811440516,
      "description": {
        "content": "This function queries Exchange Online to find messages matching the specified input parameters.  A list of messages is returned from the function.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Query Messages",
      "export_key": "exchange_online_query_emails",
      "id": 11,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440558,
      "name": "exchange_online_query_emails",
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "6f09fab2-2176-4c27-ab39-cc19568e08e5",
      "version": 1,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4ff86946-a8cf-4ae1-804b-87cab7d9dac1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8dd46926-b1dc-4d1e-ab6a-4239510b199d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1c9b3b95-ca24-484c-ad72-f5d64be87402",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7354f758-b9ea-4029-835d-66d293a22b5d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "51a9c433-07bc-4f04-9932-99211726b9b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06391a1a-0c2c-4bcd-832a-1f39a3ba77b8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ec20a9f0-1e29-490b-871b-57b05ffbac2e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9e58d3a3-c54b-4a9b-9164-e6cc0832f644",
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
      "created_date": 1686811440584,
      "description": {
        "content": "This function creates a message and sends it to the specified recipients.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Send Message",
      "export_key": "exchange_online_send_message",
      "id": 12,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440627,
      "name": "exchange_online_send_message",
      "tags": [
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "6256b03b-03ae-4972-bba2-63fe629fbb65",
      "version": 1,
      "view_items": [
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "43a3d370-9043-44e8-b54a-7296f805edf8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "51a9c433-07bc-4f04-9932-99211726b9b7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06391a1a-0c2c-4bcd-832a-1f39a3ba77b8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5615f985-78ce-418b-a09d-4bdd73c4bd2e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
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
      "created_date": 1686811440655,
      "description": {
        "content": "This function gets the mime content of an Exchange Online message and writes it as an incident attachment.",
        "format": "text"
      },
      "destination_handle": "fn_exchange_online",
      "display_name": "Exchange Online: Write Message as Attachment",
      "export_key": "exchange_online_write_message_as_attachment",
      "id": 13,
      "last_modified_by": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686811440697,
      "name": "exchange_online_write_message_as_attachment",
      "tags": [
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "dbb5e3de-0f43-4c7e-b09f-5d50f0ce426c",
      "version": 1,
      "view_items": [
        {
          "content": "ead214c2-13fe-43f6-a3c7-676a88338dbb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "092a752f-1297-46a4-bae6-e75d1a9b4804",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "00ca7e22-f9fa-4477-a056-602139d0dbd0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8ead74-4649-4179-9dbd-3e8cf029e3d7",
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
  "id": 69,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1688018675500,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1688018675500,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "c3be9c35-c18c-4fac-bae5-9a7d483f1db2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_exchange_online",
      "name": "fn_exchange_online",
      "programmatic_name": "fn_exchange_online",
      "tags": [
        {
          "tag_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
          "value": "Playbook Tag"
        }
      ],
      "users": [],
      "uuid": "ef11c871-6784-4101-b7a0-bbfbe5574aaf"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f\" isExecutable=\"true\" name=\"playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1dkenar\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cscriptTask id=\"ScriptTask_1\" name=\"Exchange Online Create Artifacts from Message\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"ddc0513f-fcbc-4582-a4b3-b80a6bd3ff52\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1dkenar\u003c/incoming\u003e\u003coutgoing\u003eFlow_0mk2xb6\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0mk2xb6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1dkenar\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0mk2xb6\" sourceRef=\"ScriptTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1dkenar\" id=\"Flow_1dkenar_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"-84\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"18\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0mk2xb6\" id=\"Flow_0mk2xb6_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"102\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"194\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"480\" y=\"-136\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1\" id=\"ScriptTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"481.984\" y=\"17.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"513.9839999999999\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812124974,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Create Artifacts (PB)",
      "export_key": "example_exchange_online_create_artifacts",
      "field_type_handle": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Create Artifacts (PB)",
        "export_key": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
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
        "type_name": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
        "uuid": "bf76644b-3596-4ce3-ad42-49b4ceba6d0b"
      },
      "has_logical_errors": false,
      "id": 8,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1687333927021,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_exchange_online_create_artifacts",
      "object_type": "exo_message_query_results_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_45f7d606-5f20-4a3b-8bdb-1b9dc501650f",
        "id": 8,
        "name": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
        "type": "playbook",
        "uuid": "e71db3a8-c729-4e0e-8108-f4743680918e"
      },
      "tags": [],
      "type": "default",
      "uuid": "45f7d606-5f20-4a3b-8bdb-1b9dc501650f",
      "version": 6
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be\" isExecutable=\"true\" name=\"playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0j3j0st\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Create Meeting\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"40e56303-027d-4e27-9865-10ca18d267b3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_meeting_email_address = playbook.inputs.exchange_online_meeting_organizer_email_address  \\ninputs.exo_meeting_start_time = playbook.inputs.exchange_online_meeting_start_time\\ninputs.exo_meeting_end_time = playbook.inputs.exchange_online_meeting_end_time\\ninputs.exo_meeting_subject = playbook.inputs.exchange_online_meeting_subject\\ninputs.exo_meeting_body = playbook.inputs.exchange_online_meeting_body.content\\ninputs.exo_meeting_required_attendees = playbook.inputs.exchange_online_required_attendees\\ninputs.exo_meeting_optional_attendees = playbook.inputs.exchange_online_meeting_optional_attendees\\ninputs.exo_meeting_location = playbook.inputs.exchange_online_meeting_location\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_onlne_creating_meeting_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0j3j0st\u003c/incoming\u003e\u003coutgoing\u003eFlow_0x66ova\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0snbvqy\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"exchange_online_create_meeting_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"c095e48f-c02b-4120-a29d-db6e3e221d78\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0x66ova\u003c/incoming\u003e\u003coutgoing\u003eFlow_0snbvqy\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0j3j0st\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0x66ova\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_0snbvqy\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0snbvqy\" id=\"Flow_0snbvqy_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"442\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"504\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0x66ova\" id=\"Flow_0x66ova_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"358\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0j3j0st\" id=\"Flow_0j3j0st_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"504\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"358\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812125438,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Create Meeting (PB)",
      "export_key": "example_exchange_online_create_meeting",
      "field_type_handle": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Create Meeting (PB)",
        "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
        "fields": {
          "exchange_online_meeting_body": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_body",
            "hide_notification": false,
            "id": 679,
            "input_type": "textarea",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_body",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting Body",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "f68171ec-6528-44bd-a0eb-5c8915ab713d",
            "values": []
          },
          "exchange_online_meeting_end_time": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_end_time",
            "hide_notification": false,
            "id": 680,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_end_time",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting End Time",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "7ea76d16-d685-4a53-8d06-fd7414a0c1d5",
            "values": []
          },
          "exchange_online_meeting_location": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_location",
            "hide_notification": false,
            "id": 681,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_location",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting Location",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "ec6fc2d6-e320-4996-93b1-337a1fd371df",
            "values": []
          },
          "exchange_online_meeting_optional_attendees": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_optional_attendees",
            "hide_notification": false,
            "id": 682,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_optional_attendees",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user1@example.com, user2@example.com",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Optional Attendees",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "abf4608b-bf46-4aa4-864a-c03121dada72",
            "values": []
          },
          "exchange_online_meeting_organizer_email_address": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_organizer_email_address",
            "hide_notification": false,
            "id": 683,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_organizer_email_address",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user@example.com",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting Organizer Email Address",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "35f9f3b8-7553-4e7b-b588-cb757bc93ea7",
            "values": []
          },
          "exchange_online_meeting_start_time": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_start_time",
            "hide_notification": false,
            "id": 684,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_start_time",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting Start Time",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "98be31fa-a2b3-412c-9a4f-ed810d88f4d6",
            "values": []
          },
          "exchange_online_meeting_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_meeting_subject",
            "hide_notification": false,
            "id": 685,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_meeting_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Meeting Subject",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "eec63000-98b1-4d47-90d2-3be19d560bdd",
            "values": []
          },
          "exchange_online_required_attendees": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be/exchange_online_required_attendees",
            "hide_notification": false,
            "id": 686,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_required_attendees",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user1@example.com, user2@example.co",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Required Attendees",
            "tooltip": "",
            "type_id": 1011,
            "uuid": "ef31795e-6a56-4bd3-a444-3bab8108de77",
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
        "type_name": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
        "uuid": "9d00917c-096e-43a9-9bc3-b48cdd51d789"
      },
      "has_logical_errors": false,
      "id": 9,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686814684820,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812125775,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_create_meeting_post_process",
          "id": 10,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812125797,
          "name": "exchange_online_create_meeting_post_process",
          "object_type": "incident",
          "playbook_handle": "example_exchange_online_create_meeting",
          "programmatic_name": "example_exchange_online_create_meeting_exchange_online_create_meeting",
          "script_text": "results=playbook.functions.results.exchange_onlne_creating_meeting_result\n\nif results.success:\n  noteText = u\"Exchange Online created meeting\\n   From: {0}\\n{1}\".format(results.inputs[\"exo_meeting_email_address\"],results.pretty_string)\nelse:\n  noteText = u\"Exchange Online meeting was NOT created\\n   From: {0}\\n{1}\".format(results.inputs[\"exo_meeting_email_address\"], results.pretty_string)\n\nincident.addNote(noteText)",
          "tags": [],
          "uuid": "c095e48f-c02b-4120-a29d-db6e3e221d78"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "35f9f3b8-7553-4e7b-b588-cb757bc93ea7",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "98be31fa-a2b3-412c-9a4f-ed810d88f4d6",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "7ea76d16-d685-4a53-8d06-fd7414a0c1d5",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "eec63000-98b1-4d47-90d2-3be19d560bdd",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "f68171ec-6528-44bd-a0eb-5c8915ab713d",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "ec6fc2d6-e320-4996-93b1-337a1fd371df",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "ef31795e-6a56-4bd3-a444-3bab8108de77",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "abf4608b-bf46-4aa4-864a-c03121dada72",
            "element": "field_uuid",
            "field_type": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_create_meeting",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_eefd2b32-40c0-4dfa-a9a7-6954d45a83be",
        "id": 9,
        "name": "playbook_eefd2b32_40c0_4dfa_a9a7_6954d45a83be",
        "type": "playbook",
        "uuid": "01e22809-24f7-48c3-9420-0f3deb659fe1"
      },
      "tags": [],
      "type": "default",
      "uuid": "eefd2b32-40c0-4dfa-a9a7-6954d45a83be",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_2dca7324_8232_49aa_8029_3cf955c689b0\" isExecutable=\"true\" name=\"playbook_2dca7324_8232_49aa_8029_3cf955c689b0\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0y4m5em\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Delete Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e4a2073e-46cf-48a6-b3be-f0f99b05c472\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_email_address = row.exo_dt_email_address\\ninputs.exo_messages_id = row.exo_dt_message_id\\ninputs.exo_mailfolders_id = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_delete_message_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0y4m5em\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ridshg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0fv3op6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0y4m5em\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1ridshg\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"exchange_online_delete_message_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"c79c7a1c-eb02-4737-bde1-0a2b9d07a152\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ridshg\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fv3op6\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0fv3op6\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_2dca7324_8232_49aa_8029_3cf955c689b0\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fv3op6\" id=\"Flow_0fv3op6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"544\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ridshg\" id=\"Flow_1ridshg_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0y4m5em\" id=\"Flow_0y4m5em_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"544\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623.25\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812126151,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Delete Message (PB)",
      "export_key": "example_exchange_online_delete_message",
      "field_type_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Delete Message (PB)",
        "export_key": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
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
        "type_name": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
        "uuid": "ef23d709-cb17-4035-b009-bc1844129e9a"
      },
      "has_logical_errors": false,
      "id": 10,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1686815059676,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812126249,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_delete_message_post_process",
          "id": 11,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812126272,
          "name": "exchange_online_delete_message_post_process",
          "object_type": "exo_message_query_results_dt",
          "playbook_handle": "example_exchange_online_delete_message",
          "programmatic_name": "example_exchange_online_delete_message_exchange_online_delete_message",
          "script_text": "results=playbook.functions.results.exchange_online_delete_message_result\n\nif results.success:\n  # The message was deleted, so update \"status\" column in data table.\n  text = u\"\"\"\u003cp style= \"color:{color}\"\u003e{status} \u003c/p\u003e\"\"\".format(color=\"red\", status=\"Deleted\")\n  row[\u0027exo_dt_status\u0027] = helper.createRichText(text)\n  row[\u0027exo_dt_web_link\u0027] = \"\"\nelif results.content[\"error\"] is not None: \n  # There is an \"item not found\" error mostly likely here\n  row[\u0027exo_dt_status\u0027] = helper.createRichText(results.content[\"error\"][\"code\"])\n  row[\u0027exo_dt_web_link\u0027] = \"\"",
          "tags": [],
          "uuid": "c79c7a1c-eb02-4737-bde1-0a2b9d07a152"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "exo_message_query_results_dt.exo_dt_status",
              "method": "equals",
              "type": null,
              "value": "Active"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_exchange_online_delete_message",
      "object_type": "exo_message_query_results_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_2dca7324-8232-49aa-8029-3cf955c689b0",
        "id": 10,
        "name": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
        "type": "playbook",
        "uuid": "447c02a7-a2a4-4dd1-9bb0-dd49584294c3"
      },
      "tags": [],
      "type": "default",
      "uuid": "2dca7324-8232-49aa-8029-3cf955c689b0",
      "version": 5
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 9,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89\" isExecutable=\"true\" name=\"playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0r6camt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Query Messages\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6f09fab2-2176-4c27-ab39-cc19568e08e5\"\u003e{\"inputs\":{\"ead214c2-13fe-43f6-a3c7-676a88338dbb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"092a752f-1297-46a4-bae6-e75d1a9b4804\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"9e58d3a3-c54b-4a9b-9164-e6cc0832f644\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"68133b08-816e-4c03-a50d-c68af1b6b205\"]}},\"4ff86946-a8cf-4ae1-804b-87cab7d9dac1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"8dd46926-b1dc-4d1e-ab6a-4239510b199d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"1c9b3b95-ca24-484c-ad72-f5d64be87402\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"7354f758-b9ea-4029-835d-66d293a22b5d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"51a9c433-07bc-4f04-9932-99211726b9b7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"06391a1a-0c2c-4bcd-832a-1f39a3ba77b8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"ec20a9f0-1e29-490b-871b-57b05ffbac2e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"\\n\\ninputs.incident_id = incident.id\\n\\n# Get the email address of the user whose mailbox will be queried.\\ninputs.exo_email_address = playbook.inputs.exchange_online_email_address_list\\n\\n# Get the search criteria from the activity rules if available. \\n\\n\\ninputs.exo_mail_folders         = playbook.inputs.exchange_online_mail_folder_id\\ninputs.exo_email_address_sender = playbook.inputs.exchange_online_sender_email_address\\ninputs.exo_message_subject      = playbook.inputs.exchange_online_message_subject\\ninputs.exo_message_body         = playbook.inputs.exchange_online_message_body\\ninputs.exo_start_date           = playbook.inputs.exchange_online_start_datetime\\ninputs.exo_end_date             = playbook.inputs.exchange_online_end_datetime\\ninputs.exo_has_attachments      = playbook.inputs.exchange_online_has_attachments\\n\\n    \\nif hasattr(playbook.inputs, \\\"exchange_online_query_results_output\\\"):\\n    inputs.exo_query_output_format = [d for d in playbook.inputs.exchange_online_query_results_output]\\n\\n\\n\\n\\n\\n\\n\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_query_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0r6camt\u003c/incoming\u003e\u003coutgoing\u003eFlow_1vnwyn3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_2\" name=\"Exchange Online: Delete Messages From Query Results\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"af142c3a-3c38-4352-9bca-fa82d53c61af\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_query_messages_results = playbook.functions.results.exchange_online_query_results[\u0027raw\u0027]\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_delete_messages_from_query_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1vnwyn3\u003c/incoming\u003e\u003coutgoing\u003eFlow_1turkjv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0t7a98f\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0r6camt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1vnwyn3\" sourceRef=\"ServiceTask_1\" targetRef=\"ServiceTask_2\"/\u003e\u003csequenceFlow id=\"Flow_1turkjv\" sourceRef=\"ServiceTask_2\" targetRef=\"ScriptTask_4\"/\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"exchange_online_delete_messages_from_query_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"af90b5de-2584-4359-b13f-fd9c5cfc2b85\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1turkjv\u003c/incoming\u003e\u003coutgoing\u003eFlow_0t7a98f\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0t7a98f\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0t7a98f\" id=\"Flow_0t7a98f_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"682\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"744\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1turkjv\" id=\"Flow_1turkjv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"522\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"598\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1vnwyn3\" id=\"Flow_1vnwyn3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"332\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"438\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0r6camt\" id=\"Flow_0r6camt_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"248\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"248\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_2\" id=\"ServiceTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"438\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"654.5\" y=\"743.75\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623.25\" y=\"598.25\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812126662,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Delete Messages from Query Results (PB)",
      "export_key": "example_exchange_online_delete_messages_from_query_results",
      "field_type_handle": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Delete Messages from Query Results (PB)",
        "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
        "fields": {
          "exchange_online_email_address_list": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_email_address_list",
            "hide_notification": false,
            "id": 687,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_email_address_list",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Email Address",
            "tooltip": "Email addresses to search: a single email address, a comma separated list of email addresses, or \"ALL\" to search all users",
            "type_id": 1013,
            "uuid": "8a722d51-a347-4868-af95-e386d5b1bf52",
            "values": []
          },
          "exchange_online_end_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_end_datetime",
            "hide_notification": false,
            "id": 688,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_end_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "End date/time",
            "tooltip": "Query messages received ending at this date/time.",
            "type_id": 1013,
            "uuid": "457787e1-29d1-44bd-bf56-1645a6bc77bd",
            "values": []
          },
          "exchange_online_has_attachments": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_has_attachments",
            "hide_notification": false,
            "id": 689,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_has_attachments",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Has attachments",
            "tooltip": "Return messages which have attachments (Yes) or do not have attachments (No)",
            "type_id": 1013,
            "uuid": "7e5423cd-e7f8-4f99-973f-081eb3a293e0",
            "values": []
          },
          "exchange_online_mail_folder_id": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_mail_folder_id",
            "hide_notification": false,
            "id": 690,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_mail_folder_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Mail Folder",
            "tooltip": "The mailfolder to search. If none is selected, all mail folders are searched.",
            "type_id": 1013,
            "uuid": "58bdadf6-00f9-46c6-a862-04f76509dfba",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "archive",
                "properties": null,
                "uuid": "ec02e1dd-8a43-48cc-94fe-7bee4ba9ba17",
                "value": 209
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "clutter",
                "properties": null,
                "uuid": "af082915-de65-48e5-8b1c-59cc515c376d",
                "value": 210
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conflicts",
                "properties": null,
                "uuid": "302225ac-1225-4471-b4c7-70e2ec49687d",
                "value": 211
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conversationhistory",
                "properties": null,
                "uuid": "f73606bb-aed0-4e72-afbe-00c14b1841aa",
                "value": 212
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "deleteditems",
                "properties": null,
                "uuid": "3ca37e3a-88d1-4139-ac12-d2441678dd29",
                "value": 213
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "drafts",
                "properties": null,
                "uuid": "715516c0-93f5-4bc4-bb91-0216adf6d2fb",
                "value": 214
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "inbox",
                "properties": null,
                "uuid": "ce6b8a26-7b2b-4753-83c4-7b5d76350f3f",
                "value": 215
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "junkemail",
                "properties": null,
                "uuid": "6be92169-1591-4b5d-b6e3-d8cd4a6e45ef",
                "value": 216
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "localfailures",
                "properties": null,
                "uuid": "4203298d-93fe-4128-9d5c-f667f86dc8e6",
                "value": 217
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "msgfolderroot",
                "properties": null,
                "uuid": "7f711031-84fe-4554-8d2a-9061e9e58401",
                "value": 218
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "outbox",
                "properties": null,
                "uuid": "0b877eaa-9307-4e13-9f0c-270723a0451a",
                "value": 219
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "recoverableitemsdeletions",
                "properties": null,
                "uuid": "1d0652a3-bd30-4330-8f7a-a5f71f2739a1",
                "value": 220
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "scheduled",
                "properties": null,
                "uuid": "3a87685a-60ba-49b1-a3d7-1d0b732120b1",
                "value": 221
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "searchfolders",
                "properties": null,
                "uuid": "d8a58b2b-3c74-4907-8942-2667f4d8e1cb",
                "value": 222
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "sentitems",
                "properties": null,
                "uuid": "22f2efab-5035-436d-9131-2610c95fcb11",
                "value": 223
              }
            ]
          },
          "exchange_online_message_body": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_message_body",
            "hide_notification": false,
            "id": 691,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_body",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Body",
            "tooltip": "",
            "type_id": 1013,
            "uuid": "828cef69-7e78-42c3-a277-c654ba55fc49",
            "values": []
          },
          "exchange_online_message_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_message_subject",
            "hide_notification": false,
            "id": 692,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Subject",
            "tooltip": "Text for the message subject to query",
            "type_id": 1013,
            "uuid": "72a4f565-eba2-400d-aad7-5ba137d438c7",
            "values": []
          },
          "exchange_online_query_results_output": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_query_results_output",
            "hide_notification": false,
            "id": 693,
            "input_type": "multiselect",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_query_results_output",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Query results output",
            "tooltip": "",
            "type_id": 1013,
            "uuid": "b9043432-0a06-44fc-9948-6c8b3d879bea",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Exchange Online data table",
                "properties": null,
                "uuid": "b5773230-8a84-4105-93f0-3f654da156b7",
                "value": 224
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident attachment",
                "properties": null,
                "uuid": "5b521459-c937-4c7e-9b1a-52b9799c42a3",
                "value": 225
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident note",
                "properties": null,
                "uuid": "c860d303-4436-4f93-8ebb-18a726c2b40a",
                "value": 226
              }
            ]
          },
          "exchange_online_sender_email_address": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_sender_email_address",
            "hide_notification": false,
            "id": 694,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_sender_email_address",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user@example.com",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sender email address",
            "tooltip": "Enter the email address of the sender",
            "type_id": 1013,
            "uuid": "26132344-1763-4923-8aa6-d880240f57db",
            "values": []
          },
          "exchange_online_start_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89/exchange_online_start_datetime",
            "hide_notification": false,
            "id": 695,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_start_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Start date/time",
            "tooltip": "Query messages received starting at this date/time.",
            "type_id": 1013,
            "uuid": "424fcb0e-406e-475e-8271-b69ef21e30b1",
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
        "type_name": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
        "uuid": "f73307cb-6e24-4ef1-a60f-ea0226d45b21"
      },
      "has_logical_errors": false,
      "id": 11,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1687940769195,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812127025,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_delete_messages_from_query_post_process",
          "id": 12,
          "language": "python3",
          "last_modified_by": "hychuang@tw.ibm.com",
          "last_modified_time": 1687939676371,
          "name": "exchange_online_delete_messages_from_query_post_process",
          "object_type": "incident",
          "playbook_handle": "example_exchange_online_delete_messages_from_query_results",
          "programmatic_name": "example_exchange_online_delete_messages_from_query_results_exchange_online_delete_messages_from_query_results",
          "script_text": "from datetime import datetime\nresults=playbook.functions.results.exchange_online_delete_messages_from_query_results\ncontent = results.get(\"content\")\noutput_format = content.get(\"exo_query_output_format\")\n\n\n# Write to the data table if the user requested it.\nif \"Exchange Online data table\" in output_format:\n  \n  user_list = content.get(\"delete_results\")\n  # Add each email as a row in the query results data table\n  for user in user_list:\n    \n    for email in user[\"deleted_list\"]:\n      message_row = incident.addRow(\"exo_message_query_results_dt\")\n      message_row.exo_dt_query_date = datetime.now()\n      message_row.exo_dt_message_id = email.get(\"id\", \"\")\n      message_row.exo_dt_received_date   = email.get(\"receivedDateTime\")\n      message_row.exo_dt_email_address = user.get(\"email_address\")\n      if email.get(\"sender\"):\n        message_row.exo_dt_sender_email = email[\"sender\"][\"emailAddress\"][\"address\"]\n      else:\n        message_row.exo_dt_sender_email = \"\"\n      message_row.exo_dt_message_subject = email.get(\"subject\")\n      message_row.exo_dt_has_attachments = email.get(\"hasAttachments\")\n      message_row.exo_dt_web_link = \"\"\n      \n      text = u\"\"\"\u003cp style= \"color:{color}\"\u003e{status} \u003c/p\u003e\"\"\".format(color=\"red\", status=\"Deleted\")\n      message_row.exo_dt_status = helper.createRichText(text)\n",
          "tags": [],
          "uuid": "af90b5de-2584-4359-b13f-fd9c5cfc2b85"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "8a722d51-a347-4868-af95-e386d5b1bf52",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "58bdadf6-00f9-46c6-a862-04f76509dfba",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose from a least one of the search criteria below:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "26132344-1763-4923-8aa6-d880240f57db",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "424fcb0e-406e-475e-8271-b69ef21e30b1",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "457787e1-29d1-44bd-bf56-1645a6bc77bd",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "72a4f565-eba2-400d-aad7-5ba137d438c7",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "828cef69-7e78-42c3-a277-c654ba55fc49",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "7e5423cd-e7f8-4f99-973f-081eb3a293e0",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose query results output format:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b9043432-0a06-44fc-9948-6c8b3d879bea",
            "element": "field_uuid",
            "field_type": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_delete_messages_from_query_results",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_85dc2249-0372-458b-87bd-8ac9efdf3c89",
        "id": 11,
        "name": "playbook_85dc2249_0372_458b_87bd_8ac9efdf3c89",
        "type": "playbook",
        "uuid": "1a428b1b-4b15-4825-8e77-b1241587987c"
      },
      "tags": [],
      "type": "default",
      "uuid": "85dc2249-0372-458b-87bd-8ac9efdf3c89",
      "version": 11
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b\" isExecutable=\"true\" name=\"playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1qjnvue\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Get User Profile\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f7af9277-dea6-4825-9279-09594d8e0770\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_email_address = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_get_user_profile_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1qjnvue\u003c/incoming\u003e\u003coutgoing\u003eFlow_0epbqgv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"exchange_online_get_user_profile_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dc993933-d7b7-47df-be45-e0b42f06fefc\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0epbqgv\u003c/incoming\u003e\u003coutgoing\u003eFlow_131kgf8\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_131kgf8\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_1qjnvue\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_0epbqgv\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_131kgf8\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_131kgf8\" id=\"Flow_131kgf8_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"512\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"594\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0epbqgv\" id=\"Flow_0epbqgv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"322\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"428\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qjnvue\" id=\"Flow_1qjnvue_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"238\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"238\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"428\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812127472,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Get User Profile (PB)",
      "export_key": "example_exchange_online_get_user_profile",
      "field_type_handle": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Get User Profile (PB)",
        "export_key": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
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
        "type_name": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
        "uuid": "8cfb1717-086a-4230-bccd-1d88ec64eb0d"
      },
      "has_logical_errors": false,
      "id": 12,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686812128198,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812127582,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_get_user_profile_post_process",
          "id": 13,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812127607,
          "name": "exchange_online_get_user_profile_post_process",
          "object_type": "artifact",
          "playbook_handle": "example_exchange_online_get_user_profile",
          "programmatic_name": "example_exchange_online_get_user_profile_exchange_online_get_user_profile",
          "script_text": "results=playbook.functions.results.exchange_online_get_user_profile_result\n\nif results.content[\"error\"] is not None:\n  noteText = u\"Exchange Online user profile NOT FOUND: {0}\\n{1}\".format(results.inputs[\"exo_email_address\"], results.pretty_string)\nelse:\n  noteText = u\"Exchange Online user profile: {0}\\n{1}\".format(results.inputs[\"exo_email_address\"], results.pretty_string)\n\nincident.addNote(noteText)",
          "tags": [],
          "uuid": "dc993933-d7b7-47df-be45-e0b42f06fefc"
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
              "value": "Email Sender Name"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "User Account"
            }
          ],
          "logic_type": "any"
        },
        "view_items": []
      },
      "name": "example_exchange_online_get_user_profile",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_e7448d95-4104-4ff2-9d78-a3923a20b30b",
        "id": 12,
        "name": "playbook_e7448d95_4104_4ff2_9d78_a3923a20b30b",
        "type": "playbook",
        "uuid": "06721b34-a504-4ff6-8f80-09ff6eebe616"
      },
      "tags": [],
      "type": "default",
      "uuid": "e7448d95-4104-4ff2-9d78-a3923a20b30b",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_8685fa14_9e7f_4140_a974_886711daf91d\" isExecutable=\"true\" name=\"playbook_8685fa14_9e7f_4140_a974_886711daf91d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_156z2cs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Move Message to Folder\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ec89e514-34f6-4fe3-98ea-85398bb04dd9\"\u003e{\"inputs\":{\"092a752f-1297-46a4-bae6-e75d1a9b4804\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"00ca7e22-f9fa-4477-a056-602139d0dbd0\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"b9765902-10bb-4a92-819e-25d3e346c3b3\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9c20f34a-363a-4e70-8d68-2f0a3cadfc44\"}},\"669df159-68fd-419f-8678-ad3b93514f8c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"results=playbook.functions.results.exchange_online_move_nessage_to_folder_result\\n\\n\\ninputs.exo_email_address = row.exo_dt_email_address\\ninputs.exo_mailfolders_id = None\\ninputs.exo_messages_id = row.exo_dt_message_id\\ninputs.exo_destination_mailfolder_id = playbook.inputs.exchnange_online_wellknown_folders_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_move_nessage_to_folder_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_156z2cs\u003c/incoming\u003e\u003coutgoing\u003eFlow_1v6kpfe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_1qo3lfe\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"exchange_online_move_message_to_folder_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"618f493c-5a10-471d-bc8a-877086ff6ddb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1v6kpfe\u003c/incoming\u003e\u003coutgoing\u003eFlow_1qo3lfe\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_156z2cs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1v6kpfe\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_1qo3lfe\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_8685fa14_9e7f_4140_a974_886711daf91d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qo3lfe\" id=\"Flow_1qo3lfe_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"482\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"554\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1v6kpfe\" id=\"Flow_1v6kpfe_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"322\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"398\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_156z2cs\" id=\"Flow_156z2cs_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"238\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"238\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"554\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.75\" y=\"398\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812128174,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Move Message to Folder (PB)",
      "export_key": "example_exchange_online_move_message_to_folder",
      "field_type_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Move Message to Folder (PB)",
        "export_key": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
        "fields": {
          "exchnange_online_wellknown_folders_id": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_8685fa14_9e7f_4140_a974_886711daf91d/exchnange_online_wellknown_folders_id",
            "hide_notification": false,
            "id": 696,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "exchnange_online_wellknown_folders_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Well-known Folders",
            "tooltip": "Destination folder to which message will be moved",
            "type_id": 1015,
            "uuid": "f9cddb38-ccfa-4af2-8e22-44a3e2a88391",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "archive",
                "properties": null,
                "uuid": "bc07037a-ad51-4377-b09e-9fd2d681d07f",
                "value": 227
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "clutter",
                "properties": null,
                "uuid": "69b281c7-9356-42ad-936f-7683b1b403b0",
                "value": 228
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conflicts",
                "properties": null,
                "uuid": "18bf4f45-1f49-49f2-94cf-b608ee69343a",
                "value": 229
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conversationhistory",
                "properties": null,
                "uuid": "1da6d140-c711-4012-8599-79d6a2dd0ed9",
                "value": 230
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "deleteditems",
                "properties": null,
                "uuid": "f8f05861-2d62-42ef-8b2f-4492041b67a7",
                "value": 231
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "drafts",
                "properties": null,
                "uuid": "ed5340c8-d38d-4269-8c3a-bef663180108",
                "value": 232
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "inbox",
                "properties": null,
                "uuid": "3949f49c-015e-430b-ab06-72b4479c0f0a",
                "value": 233
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "junkemail",
                "properties": null,
                "uuid": "ef641dae-d39b-448b-9fbf-7a6cee3fd547",
                "value": 234
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "localfailures",
                "properties": null,
                "uuid": "a2c5b888-337d-4ff0-bf0f-ca7d2228daa2",
                "value": 235
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "msgfolderroot",
                "properties": null,
                "uuid": "39a02312-c3f6-4cb7-afb2-a8d38bec0396",
                "value": 236
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "outbox",
                "properties": null,
                "uuid": "0bf60c2c-877f-4d3e-b466-10869d6f7935",
                "value": 237
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "recoverableitemsdeletions",
                "properties": null,
                "uuid": "078b21e0-d5ae-401b-b296-44b022f2cfbe",
                "value": 238
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "scheduled",
                "properties": null,
                "uuid": "e5647752-0a04-4ce1-bdde-6f444f1992dd",
                "value": 239
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "searchfolders",
                "properties": null,
                "uuid": "9e199761-9cdb-481d-9bb3-0dd66a537ad6",
                "value": 240
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "sentitems",
                "properties": null,
                "uuid": "09bc53bf-ac82-461e-8259-7dfac6e678ad",
                "value": 241
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
        "type_name": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
        "uuid": "83df778a-4633-4dde-93e6-8112b1299818"
      },
      "has_logical_errors": false,
      "id": 13,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686812128716,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812128302,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_move_message_to_folder_post_process",
          "id": 14,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812128324,
          "name": "exchange_online_move_message_to_folder_post_process",
          "object_type": "exo_message_query_results_dt",
          "playbook_handle": "example_exchange_online_move_message_to_folder",
          "programmatic_name": "example_exchange_online_move_message_to_folder_exchange_online_move_message_to_folder",
          "script_text": "results=playbook.functions.results.exchange_online_move_nessage_to_folder_result\nif results.content[\"error\"] is not None:\n  # Print the message to an incident note if it is found, otherwise update the status as Not Found in the datatable.\n  noteText = u\"Exchange Online message NOT FOUND: \\n email address: {0}\\n message ID: {1}\".format(results.inputs[\"exo_email_address\"], results.inputs[\"exo_messages_id\"])\n  status_text = u\"\"\"\u003cp style= \"color:{color}\"\u003e{status} \u003c/p\u003e\"\"\".format(color=\"red\", status=\"Not Found\")\n  row[\u0027exo_dt_status\u0027] = helper.createRichText(status_text)\n  row[\u0027exo_dt_web_link\u0027] = \"\"\nelse:\n  # When a message is moved it\u0027s ID changes, so update the new message ID into the data table\n  # The message status is still \"Active\" but the weblink is no longer valid, so make is empty string.\n  noteText = u\"Exchange Online email address: {0}\\n\\n  Message has been moved to folder: {1}\\n\\n  Old message ID: {2} \\n\\n  New message ID: {3}\".format(results.inputs[\"exo_email_address\"], results.inputs[\"exo_destination_mailfolder_id\"][\"name\"], results.inputs[\"exo_messages_id\"], results.content[\"new_message_id\"])\n  row[\u0027exo_dt_message_id\u0027] = results.content[\"new_message_id\"]\n  row[\u0027exo_dt_web_link\u0027] = ref_html = u\"\"\"\u003ca href=\u0027{0}\u0027\u003eLink\u003c/a\u003e\"\"\".format(results.content[\"new_web_link\"])\nincident.addNote(noteText)",
          "tags": [],
          "uuid": "618f493c-5a10-471d-bc8a-877086ff6ddb"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "exo_message_query_results_dt.exo_dt_status",
              "method": "equals",
              "type": null,
              "value": "Active"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "f9cddb38-ccfa-4af2-8e22-44a3e2a88391",
            "element": "field_uuid",
            "field_type": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_move_message_to_folder",
      "object_type": "exo_message_query_results_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_8685fa14-9e7f-4140-a974-886711daf91d",
        "id": 13,
        "name": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
        "type": "playbook",
        "uuid": "f99853d6-2cf3-456a-8436-93c1bf4c1419"
      },
      "tags": [],
      "type": "default",
      "uuid": "8685fa14-9e7f-4140-a974-886711daf91d",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 18,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a\" isExecutable=\"true\" name=\"playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0tw5igv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Query Messages\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6f09fab2-2176-4c27-ab39-cc19568e08e5\"\u003e{\"inputs\":{\"ead214c2-13fe-43f6-a3c7-676a88338dbb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"092a752f-1297-46a4-bae6-e75d1a9b4804\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"9e58d3a3-c54b-4a9b-9164-e6cc0832f644\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"68133b08-816e-4c03-a50d-c68af1b6b205\"]}},\"4ff86946-a8cf-4ae1-804b-87cab7d9dac1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"8dd46926-b1dc-4d1e-ab6a-4239510b199d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"1c9b3b95-ca24-484c-ad72-f5d64be87402\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"7354f758-b9ea-4029-835d-66d293a22b5d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"51a9c433-07bc-4f04-9932-99211726b9b7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"06391a1a-0c2c-4bcd-832a-1f39a3ba77b8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"ec20a9f0-1e29-490b-871b-57b05ffbac2e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"\\n\\ninputs.incident_id = incident.id\\n\\n# Get the email address of the user whose mailbox will be queried.\\ninputs.exo_email_address = playbook.inputs.exchange_online_email_address_list\\n\\n# Get the search criteria from the activity rules if available. \\n\\n\\ninputs.exo_mail_folders         = playbook.inputs.exchange_online_mail_folder_id\\ninputs.exo_email_address_sender = playbook.inputs.exchange_online_sender_email_address\\ninputs.exo_message_subject      = playbook.inputs.exchange_online_message_subject\\ninputs.exo_message_body         = playbook.inputs.exchange_online_message_body\\ninputs.exo_start_date           = playbook.inputs.exchange_online_start_datetime\\ninputs.exo_end_date             = playbook.inputs.exchange_online_end_datetime\\ninputs.exo_has_attachments      = playbook.inputs.exchange_online_has_attachments\\n\\n    \\nif hasattr(playbook.inputs, \\\"exchange_online_query_results_output_format\\\"):\\n    inputs.exo_query_output_format = [d for d in playbook.inputs.exchange_online_query_results_output_format]\\n\\n\\n\\n\\n\\n\\n\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_query_messages_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0tw5igv\u003c/incoming\u003e\u003coutgoing\u003eFlow_1qox18v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_037maog\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0tw5igv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"exchange_online_query_message_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"3c970c09-2637-46b8-af5b-24ecb129c984\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1qox18v\u003c/incoming\u003e\u003coutgoing\u003eFlow_037maog\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1qox18v\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_037maog\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_037maog\" id=\"Flow_037maog_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"492\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"584\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1qox18v\" id=\"Flow_1qox18v_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"322\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"408\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0tw5igv\" id=\"Flow_0tw5igv_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"238\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"238\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"584\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.5\" y=\"408\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812128690,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
      "description": {
        "content": "This workflow will query the Exchange Online messages for a list of email address and write a row entry into the Exchange Message Query Results data table for each email that matches the search criteria.  If the string \"ALL\" or \"all\" is specified, all user mailboxes of the tenant are queried for the specified messages. The user can also specify the all users starting with specific characters.  For example: \"all:r\" will search all users whose email address begins with the letter \"r\".",
        "format": "text"
      },
      "display_name": "Example: Exchange Online Query Messages (PB)",
      "export_key": "example_exchange_online_query_messages",
      "field_type_handle": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Query Messages (PB)",
        "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
        "fields": {
          "exchange_online_email_address_list": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_email_address_list",
            "hide_notification": false,
            "id": 697,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_email_address_list",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Email Address",
            "tooltip": "Email addresses to search: a single email address, a comma separated list of email addresses, or \"ALL\" to search all users",
            "type_id": 1016,
            "uuid": "9c6a335f-8b3b-4d90-809a-f7379b684cc1",
            "values": []
          },
          "exchange_online_end_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_end_datetime",
            "hide_notification": false,
            "id": 698,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_end_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "End date/time",
            "tooltip": "Query messages received ending at this date/time.",
            "type_id": 1016,
            "uuid": "d50b37e2-6112-4375-8026-92111c33f73a",
            "values": []
          },
          "exchange_online_has_attachments": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_has_attachments",
            "hide_notification": false,
            "id": 699,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_has_attachments",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Has attachments",
            "tooltip": "Return messages which have attachments (Yes) or do not have attachments (No)",
            "type_id": 1016,
            "uuid": "6074334c-b1fd-456f-9720-8f773f21f533",
            "values": []
          },
          "exchange_online_mail_folder_id": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_mail_folder_id",
            "hide_notification": false,
            "id": 700,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_mail_folder_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Mail Folder",
            "tooltip": "The mailfolder to search. If none is selected, all mail folders are searched.",
            "type_id": 1016,
            "uuid": "5d59d485-0829-4162-a6df-9447d125c363",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "archive",
                "properties": null,
                "uuid": "fbafa1dd-4c40-46e7-8687-2018d764affb",
                "value": 242
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "clutter",
                "properties": null,
                "uuid": "066437f9-b6ab-4b30-b190-801e7ccd5101",
                "value": 243
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conflicts",
                "properties": null,
                "uuid": "c0c91bf1-4eb4-4de8-adae-25ee4c623c25",
                "value": 244
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conversationhistory",
                "properties": null,
                "uuid": "735205bf-6766-420d-b9e4-2f07e802463c",
                "value": 245
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "deleteditems",
                "properties": null,
                "uuid": "f3b829a7-93b5-462a-a9f4-45ae91aa1743",
                "value": 246
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "drafts",
                "properties": null,
                "uuid": "424403b9-b7dd-415f-a62e-70a10d3ea05d",
                "value": 247
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "inbox",
                "properties": null,
                "uuid": "506c0766-bf70-4cc1-a45f-677c0d7d19a6",
                "value": 248
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "junkemail",
                "properties": null,
                "uuid": "2950c03f-a5e0-4b8c-be56-1b57cb7c86e8",
                "value": 249
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "localfailures",
                "properties": null,
                "uuid": "b5273a5c-3747-474b-bd4d-ef7e3dd68a7c",
                "value": 250
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "msgfolderroot",
                "properties": null,
                "uuid": "6c9a64a4-da2d-46aa-8d32-b9e792f5b10b",
                "value": 251
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "outbox",
                "properties": null,
                "uuid": "0452e428-6ada-4488-98c0-c6cd269a83cc",
                "value": 252
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "recoverableitemsdeletions",
                "properties": null,
                "uuid": "b286394f-e97c-41b2-9527-a79279c7e792",
                "value": 253
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "scheduled",
                "properties": null,
                "uuid": "be769b82-0aae-4270-93d2-39763625e1e0",
                "value": 254
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "searchfolders",
                "properties": null,
                "uuid": "3fe1f743-027a-4dfd-98f2-2981d4fdb04e",
                "value": 255
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "sentitems",
                "properties": null,
                "uuid": "07103b14-0a35-4f18-9c63-ff2898cae8f8",
                "value": 256
              }
            ]
          },
          "exchange_online_message_body": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_message_body",
            "hide_notification": false,
            "id": 701,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_body",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Body",
            "tooltip": "",
            "type_id": 1016,
            "uuid": "336bc4b7-d24f-440a-a8d7-dfbd6a9a27af",
            "values": []
          },
          "exchange_online_message_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_message_subject",
            "hide_notification": false,
            "id": 702,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Subject",
            "tooltip": "Text for the message subject to query",
            "type_id": 1016,
            "uuid": "07f1c611-e5aa-4915-9702-2e72b4ffc2db",
            "values": []
          },
          "exchange_online_query_results_output_format": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_query_results_output_format",
            "hide_notification": false,
            "id": 703,
            "input_type": "multiselect",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_query_results_output_format",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Query results output",
            "tooltip": "",
            "type_id": 1016,
            "uuid": "01b728d7-79c7-4549-a151-6810249c887f",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Exchange Online data table",
                "properties": null,
                "uuid": "7807827f-e0cd-45e3-8252-b663525c3a9a",
                "value": 257
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident attachment",
                "properties": null,
                "uuid": "476ac302-0ce4-428a-b8e6-ae84624bd14e",
                "value": 258
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident note",
                "properties": null,
                "uuid": "bdc69783-df32-4541-9d9a-d375ed781449",
                "value": 259
              }
            ]
          },
          "exchange_online_sender_email_address": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_sender_email_address",
            "hide_notification": false,
            "id": 704,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_sender_email_address",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user@example.com",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sender email address",
            "tooltip": "Enter the email address of the sender",
            "type_id": 1016,
            "uuid": "8741e0d1-6079-4230-963c-2d7b827021b1",
            "values": []
          },
          "exchange_online_start_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a/exchange_online_start_datetime",
            "hide_notification": false,
            "id": 705,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_start_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Start date/time",
            "tooltip": "Query messages received starting at this date/time.",
            "type_id": 1016,
            "uuid": "4014d6e1-2506-4511-ba7a-2d53cefd6635",
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
        "type_name": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
        "uuid": "9e0a0906-d9c2-454e-9dd8-3e183d817509"
      },
      "has_logical_errors": false,
      "id": 14,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1688018066112,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812129033,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_query_message_post_process",
          "id": 15,
          "language": "python3",
          "last_modified_by": "hychuang@tw.ibm.com",
          "last_modified_time": 1688018038093,
          "name": "exchange_online_query_message_post_process",
          "object_type": "incident",
          "playbook_handle": "example_exchange_online_query_messages",
          "programmatic_name": "example_exchange_online_query_messages_exchange_online_query_message_post_process",
          "script_text": "\nfrom datetime import datetime\nresults=playbook.functions.results.exchange_online_query_messages_result\ncontent = results.get(\"content\")\noutput_format = content.get(\"exo_query_output_format\")\n\n\n# Write to the data table if the user requested it.\nif \"Exchange Online data table\" in output_format:\n  user_list = content.get(\"email_results\")\n  \n  # Add each email as a row in the query results data table\n  for user in user_list:\n    \n    \n    for email in user.get(\"email_list\"):\n      message_row = incident.addRow(\"exo_message_query_results_dt\")\n      message_row.exo_dt_query_date = datetime.now()\n      message_row.exo_dt_message_id = email.get(\"id\")\n      message_row.exo_dt_received_date   = email.get(\"receivedDateTime\")\n      message_row.exo_dt_email_address = user.get(\"email_address\")\n      if email.get(\"sender\"):\n        message_row.exo_dt_sender_email = email[\"sender\"][\"emailAddress\"][\"address\"]\n      else:\n        message_row.exo_dt_sender_email = \"\"\n      message_row.exo_dt_message_subject = email.get(\"subject\")\n      message_row.exo_dt_message_folder = playbook.inputs.exchange_online_mail_folder_id\n      message_row.exo_dt_has_attachments = email.get(\"hasAttachments\")\n      if email.get(\"webLink\"):\n        ref_html = u\"\"\"\u003ca href=\u0027{0}\u0027\u003eLink\u003c/a\u003e\"\"\".format(email[\"webLink\"])\n        message_row.exo_dt_web_link = helper.createRichText(ref_html)\n      else:\n        message_row.exo_dt_web_link = \"\"\n \n      message_row.exo_dt_status = helper.createRichText(\"Active\")\n\n",
          "tags": [],
          "uuid": "3c970c09-2637-46b8-af5b-24ecb129c984"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "9c6a335f-8b3b-4d90-809a-f7379b684cc1",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "5d59d485-0829-4162-a6df-9447d125c363",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose at least one of the search criteria below:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "8741e0d1-6079-4230-963c-2d7b827021b1",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "4014d6e1-2506-4511-ba7a-2d53cefd6635",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "d50b37e2-6112-4375-8026-92111c33f73a",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "07f1c611-e5aa-4915-9702-2e72b4ffc2db",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "336bc4b7-d24f-440a-a8d7-dfbd6a9a27af",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6074334c-b1fd-456f-9720-8f773f21f533",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose query results output format:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "01b728d7-79c7-4549-a151-6810249c887f",
            "element": "field_uuid",
            "field_type": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_query_messages",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_2cb0995b-534b-4bb3-a669-0e60e2db870a",
        "id": 14,
        "name": "playbook_2cb0995b_534b_4bb3_a669_0e60e2db870a",
        "type": "playbook",
        "uuid": "ba94581f-7485-4f6e-9c21-3dbe38dfdb76"
      },
      "tags": [],
      "type": "default",
      "uuid": "2cb0995b-534b-4bb3-a669-0e60e2db870a",
      "version": 21
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_07e7c993_f998_4f42_a365_c76422425b61\" isExecutable=\"true\" name=\"playbook_07e7c993_f998_4f42_a365_c76422425b61\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0m3tyxe\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Query Messages\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6f09fab2-2176-4c27-ab39-cc19568e08e5\"\u003e{\"inputs\":{\"ead214c2-13fe-43f6-a3c7-676a88338dbb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"092a752f-1297-46a4-bae6-e75d1a9b4804\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"9e58d3a3-c54b-4a9b-9164-e6cc0832f644\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"68133b08-816e-4c03-a50d-c68af1b6b205\"]}},\"4ff86946-a8cf-4ae1-804b-87cab7d9dac1\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"8dd46926-b1dc-4d1e-ab6a-4239510b199d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"1c9b3b95-ca24-484c-ad72-f5d64be87402\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"7354f758-b9ea-4029-835d-66d293a22b5d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"51a9c433-07bc-4f04-9932-99211726b9b7\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"06391a1a-0c2c-4bcd-832a-1f39a3ba77b8\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"ec20a9f0-1e29-490b-871b-57b05ffbac2e\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}}},\"pre_processing_script\":\"inputs.incident_id = incident.id\\n\\n# Get the email address of the user whose mailbox will be queried.\\ninputs.exo_email_address = artifact.value\\n\\n# Get the search criteria from the activity rules if available. \\ninputs.exo_email_address_sender = playbook.inputs.exchange_online_sender_email_address\\ninputs.exo_mail_folders         = playbook.inputs.exchange_online_mail_folder_id\\ninputs.exo_message_subject      = playbook.inputs.exchange_online_message_subject\\ninputs.exo_message_body         = playbook.inputs.exchange_online_message_body\\ninputs.exo_start_date           = playbook.inputs.exchange_online_start_datetime\\ninputs.exo_end_date             = playbook.inputs.exchange_online_end_datetime\\ninputs.exo_has_attachments      = playbook.inputs.exchange_online_has_attachments\\n\\nif hasattr(playbook.inputs, \\\"exchange_online_query_results_output_format\\\"):\\n    inputs.exo_query_output_format = [d for d in playbook.inputs.exchange_online_query_results_output_format]\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_query_message_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0m3tyxe\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ndpwum\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"exchange_online_query_message_on_artifact_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"2f4c3d79-5d9b-4ba7-9f2b-f17559bef84f\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ndpwum\u003c/incoming\u003e\u003coutgoing\u003eFlow_0m9equj\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0m9equj\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0m3tyxe\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1ndpwum\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_0m9equj\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_07e7c993_f998_4f42_a365_c76422425b61\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0m9equj\" id=\"Flow_0m9equj_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"462\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"564\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ndpwum\" id=\"Flow_1ndpwum_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"282\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"378\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0m3tyxe\" id=\"Flow_0m3tyxe_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"198\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"630\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"198\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"622.75\" y=\"378\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"654.75\" y=\"564\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812129384,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Query Messages on Artifact (PB)",
      "export_key": "example_exchange_online_query_messages_on_artifact",
      "field_type_handle": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Query Messages on Artifact (PB)",
        "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
        "fields": {
          "exchange_online_end_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_end_datetime",
            "hide_notification": false,
            "id": 706,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_end_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "End date/time",
            "tooltip": "Query messages received ending at this date/time.",
            "type_id": 1017,
            "uuid": "c5f5e092-c171-4d3a-b6ff-d19fbaedff92",
            "values": []
          },
          "exchange_online_has_attachments": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_has_attachments",
            "hide_notification": false,
            "id": 707,
            "input_type": "boolean",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_has_attachments",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Has attachments",
            "tooltip": "Return messages which have attachments (Yes) or do not have attachments (No)",
            "type_id": 1017,
            "uuid": "fa426a48-d9ea-44cd-bdbe-cda05a850c45",
            "values": []
          },
          "exchange_online_mail_folder_id": {
            "allow_default_value": false,
            "blank_option": true,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_mail_folder_id",
            "hide_notification": false,
            "id": 708,
            "input_type": "select",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_mail_folder_id",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Mail Folder",
            "tooltip": "The mailfolder to search. If none is selected, all mail folders are searched.",
            "type_id": 1017,
            "uuid": "b47e90e5-8da7-40b1-b342-1a8fa09e7ff7",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "archive",
                "properties": null,
                "uuid": "f3577867-3c42-44c8-8e8d-ff993bee15c2",
                "value": 260
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "clutter",
                "properties": null,
                "uuid": "8be3a42d-a253-41e9-b6f6-0988dac28370",
                "value": 261
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conflicts",
                "properties": null,
                "uuid": "62c68053-6dc5-4740-896d-3c1132262b3e",
                "value": 262
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "conversationhistory",
                "properties": null,
                "uuid": "9e0b0029-cdae-40c7-9bf4-0b3804a73aa0",
                "value": 263
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "deleteditems",
                "properties": null,
                "uuid": "68c9609a-d9ea-4778-915d-1cdcbb8d8aba",
                "value": 264
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "drafts",
                "properties": null,
                "uuid": "98823fdb-91d7-4759-bb52-f6c3e24f060b",
                "value": 265
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "inbox",
                "properties": null,
                "uuid": "2e55dcc0-0306-47c0-9609-43ad8eb571b2",
                "value": 266
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "junkemail",
                "properties": null,
                "uuid": "989b33c5-8dff-456c-9ea3-d7c15e210f31",
                "value": 267
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "localfailures",
                "properties": null,
                "uuid": "771477f4-6b64-4ce3-867f-7f5583453e00",
                "value": 268
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "msgfolderroot",
                "properties": null,
                "uuid": "ee54514a-e1b0-426a-8f67-47d5483dc11f",
                "value": 269
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "outbox",
                "properties": null,
                "uuid": "25a45751-b3b7-41d1-a926-c851383badda",
                "value": 270
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "recoverableitemsdeletions",
                "properties": null,
                "uuid": "0463bf79-fe76-4d55-a7c2-79856bd960b2",
                "value": 271
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "scheduled",
                "properties": null,
                "uuid": "9c105a25-a333-43cb-8c7a-1eb185cc79b4",
                "value": 272
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "searchfolders",
                "properties": null,
                "uuid": "b2f12045-6673-436d-b4b0-1e772cd541dc",
                "value": 273
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "sentitems",
                "properties": null,
                "uuid": "09202160-066e-4301-a519-2a47e7a736e4",
                "value": 274
              }
            ]
          },
          "exchange_online_message_body": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_message_body",
            "hide_notification": false,
            "id": 709,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_body",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Body",
            "tooltip": "",
            "type_id": 1017,
            "uuid": "6d82f344-d460-4c6a-9e42-8f5e6dd389a7",
            "values": []
          },
          "exchange_online_message_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_message_subject",
            "hide_notification": false,
            "id": 710,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Subject",
            "tooltip": "Text for the message subject to query",
            "type_id": 1017,
            "uuid": "ff84b50a-5713-486a-829f-a9cbf45ef876",
            "values": []
          },
          "exchange_online_query_results_output_format": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_query_results_output_format",
            "hide_notification": false,
            "id": 711,
            "input_type": "multiselect",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_query_results_output_format",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Query results output",
            "tooltip": "",
            "type_id": 1017,
            "uuid": "8fa48a8c-cd32-4d78-a73d-f3bb857e63c4",
            "values": [
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Exchange Online data table",
                "properties": null,
                "uuid": "a89e391b-2cc0-4058-88b3-282394b65a98",
                "value": 275
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident attachment",
                "properties": null,
                "uuid": "72773670-9236-46ff-ac41-b5aa81bb3c56",
                "value": 276
              },
              {
                "default": false,
                "enabled": true,
                "hidden": false,
                "label": "Incident note",
                "properties": null,
                "uuid": "0e697ac5-1788-49ea-bfa7-03547914f8b8",
                "value": 277
              }
            ]
          },
          "exchange_online_sender_email_address": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_sender_email_address",
            "hide_notification": false,
            "id": 712,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_sender_email_address",
            "operation_perms": {},
            "operations": [],
            "placeholder": "user@example.com",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sender email address",
            "tooltip": "Enter the email address of the sender",
            "type_id": 1017,
            "uuid": "4a532220-5bed-4cdb-b9e0-5866ef139fb4",
            "values": []
          },
          "exchange_online_start_datetime": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_07e7c993_f998_4f42_a365_c76422425b61/exchange_online_start_datetime",
            "hide_notification": false,
            "id": 713,
            "input_type": "datetimepicker",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_start_datetime",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Start date/time",
            "tooltip": "Query messages received starting at this date/time.",
            "type_id": 1017,
            "uuid": "fcee825c-dc59-4838-9f31-58e48dba6a66",
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
        "type_name": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
        "uuid": "650b9df6-98d5-4eae-bec6-aa66a2a0c2b7"
      },
      "has_logical_errors": false,
      "id": 15,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1688018249387,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812129728,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_query_message_on_artifact_post_process",
          "id": 16,
          "language": "python3",
          "last_modified_by": "hychuang@tw.ibm.com",
          "last_modified_time": 1688018245678,
          "name": "exchange_online_query_message_on_artifact_post_process",
          "object_type": "artifact",
          "playbook_handle": "example_exchange_online_query_messages_on_artifact",
          "programmatic_name": "example_exchange_online_query_messages_on_artifact_exchange_online_query_message_on_artifact_post_process",
          "script_text": "\nfrom datetime import datetime\nresults=playbook.functions.results.exchange_online_query_message_result\ncontent = results.get(\"content\")\noutput_format = content.get(\"exo_query_output_format\")\n\n\n# Write to the data table if the user requested it.\nif \"Exchange Online data table\" in output_format:\n  user_list = content.get(\"email_results\")\n  \n  # Add each email as a row in the query results data table\n  for user in user_list:\n    \n    \n    for email in user.get(\"email_list\"):\n      message_row = incident.addRow(\"exo_message_query_results_dt\")\n      message_row.exo_dt_query_date = datetime.now()\n      message_row.exo_dt_message_id = email.get(\"id\")\n      message_row.exo_dt_received_date   = email.get(\"receivedDateTime\")\n      message_row.exo_dt_email_address = user.get(\"email_address\")\n      if email.get(\"sender\"):\n        message_row.exo_dt_sender_email = email[\"sender\"][\"emailAddress\"][\"address\"]\n      else:\n        message_row.exo_dt_sender_email = \"\"\n      message_row.exo_dt_message_subject = email.get(\"subject\")\n      message_row.exo_dt_message_folder = playbook.inputs.exchange_online_mail_folder_id\n      message_row.exo_dt_has_attachments = email.get(\"hasAttachments\")\n      if email.get(\"webLink\"):\n        ref_html = u\"\"\"\u003ca href=\u0027{0}\u0027\u003eLink\u003c/a\u003e\"\"\".format(email[\"webLink\"])\n        message_row.exo_dt_web_link = helper.createRichText(ref_html)\n      else:\n        message_row.exo_dt_web_link = \"\"\n \n      message_row.exo_dt_status = helper.createRichText(\"Active\")\n\n",
          "tags": [],
          "uuid": "2f4c3d79-5d9b-4ba7-9f2b-f17559bef84f"
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
              "value": "Email Recipient"
            },
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "Email Sender"
            }
          ],
          "logic_type": "any"
        },
        "view_items": [
          {
            "content": "b47e90e5-8da7-40b1-b342-1a8fa09e7ff7",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose from at least one of the search criteria below:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "4a532220-5bed-4cdb-b9e0-5866ef139fb4",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "fcee825c-dc59-4838-9f31-58e48dba6a66",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "c5f5e092-c171-4d3a-b6ff-d19fbaedff92",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "ff84b50a-5713-486a-829f-a9cbf45ef876",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6d82f344-d460-4c6a-9e42-8f5e6dd389a7",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "fa426a48-d9ea-44cd-bdbe-cda05a850c45",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "Choose query results output format:",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "8fa48a8c-cd32-4d78-a73d-f3bb857e63c4",
            "element": "field_uuid",
            "field_type": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_query_messages_on_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_07e7c993-f998-4f42-a365-c76422425b61",
        "id": 15,
        "name": "playbook_07e7c993_f998_4f42_a365_c76422425b61",
        "type": "playbook",
        "uuid": "9355d5b2-caee-4699-97fc-208833051ea1"
      },
      "tags": [],
      "type": "default",
      "uuid": "07e7c993-f998-4f42-a365-c76422425b61",
      "version": 9
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 6,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_a6e61054_fd2e_4ade_86fc_693442bd6688\" isExecutable=\"true\" name=\"playbook_a6e61054_fd2e_4ade_86fc_693442bd6688\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1px5lbw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Send Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6256b03b-03ae-4972-bba2-63fe629fbb65\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_email_address   = playbook.inputs.exchange_online_sender_address\\ninputs.exo_recipients      = playbook.inputs.exchange_online_recipient_addresses\\ninputs.exo_message_subject = playbook.inputs.exchange_online_message_subject\\ninputs.exo_message_body    = playbook.inputs.exchange_online_message_body\\ninputs.exo_attachment_names = playbook.inputs.exchange_online_attachment_names\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_send_message_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1px5lbw\u003c/incoming\u003e\u003coutgoing\u003eFlow_05drtat\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0fbhro3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_3\" name=\"exchange_online_send_message_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"508b968d-cfd5-4a7c-9182-1220f7538dae\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_05drtat\u003c/incoming\u003e\u003coutgoing\u003eFlow_0fbhro3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1px5lbw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_05drtat\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_3\"/\u003e\u003csequenceFlow id=\"Flow_0fbhro3\" sourceRef=\"ScriptTask_3\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_a6e61054_fd2e_4ade_86fc_693442bd6688\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0fbhro3\" id=\"Flow_0fbhro3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"512\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"624\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_05drtat\" id=\"Flow_05drtat_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"332\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"428\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1px5lbw\" id=\"Flow_1px5lbw_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"248\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.083\" x=\"627\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"248\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"624\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_3\" id=\"ScriptTask_3_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"428\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812130255,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Send Message (PB)",
      "export_key": "example_exchange_online_send_message",
      "field_type_handle": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Send Message (PB)",
        "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
        "fields": {
          "exchange_online_attachment_names": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688/exchange_online_attachment_names",
            "hide_notification": false,
            "id": 714,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_attachment_names",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Attachment Names",
            "tooltip": "comma separated attachment names to attach to the message",
            "type_id": 1018,
            "uuid": "7bfa0bca-f886-4140-ab02-84d85b0fbfcb",
            "values": []
          },
          "exchange_online_message_body": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688/exchange_online_message_body",
            "hide_notification": false,
            "id": 715,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_body",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Body",
            "tooltip": "",
            "type_id": 1018,
            "uuid": "6c1707eb-8cd2-4030-ae75-5e2963ad5a5c",
            "values": []
          },
          "exchange_online_message_subject": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688/exchange_online_message_subject",
            "hide_notification": false,
            "id": 716,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_message_subject",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Message Subject",
            "tooltip": "Text for the message subject to query",
            "type_id": 1018,
            "uuid": "a752b520-1380-42b0-8851-6fee284dc442",
            "values": []
          },
          "exchange_online_recipient_addresses": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688/exchange_online_recipient_addresses",
            "hide_notification": false,
            "id": 717,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_recipient_addresses",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Recipient Addresses",
            "tooltip": "Comma separated list of message recipients",
            "type_id": 1018,
            "uuid": "b9b4a3be-cb80-40e4-8fa2-5f91a8b6e9d5",
            "values": []
          },
          "exchange_online_sender_address": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688/exchange_online_sender_address",
            "hide_notification": false,
            "id": 718,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_sender_address",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "required": "always",
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Sender Address",
            "tooltip": "",
            "type_id": 1018,
            "uuid": "c3847b8d-a57a-4050-b5c8-004f6e595172",
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
        "type_name": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
        "uuid": "4356c59c-ed36-42b9-9862-21bf8c6f65dd"
      },
      "has_logical_errors": false,
      "id": 16,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "hychuang@tw.ibm.com",
        "type": "user"
      },
      "last_modified_time": 1687851544158,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812130501,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_send_message_post_process",
          "id": 17,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812130527,
          "name": "exchange_online_send_message_post_process",
          "object_type": "incident",
          "playbook_handle": "example_exchange_online_send_message",
          "programmatic_name": "example_exchange_online_send_message_exchange_online_send_message_post_process",
          "script_text": "results=playbook.functions.results.exchange_online_send_message_result\n\nif results.success:\n  noteText = u\"Exchange Online message sent\\n   From: {0}\\n   To: {1}\\n   Subject: {2}\\n   Body: {3}\".format(results.inputs[\"exo_email_address\"], results.inputs[\"exo_recipients\"], results.inputs[\"exo_message_subject\"], results.inputs[\"exo_message_body\"])\nelse:\n  noteText = u\"Exchange Online message NOT sent\\n   From: {0}\\n  To: {1}\".format(results.inputs[\"exo_email_address\"], results.inputs[\"exo_recipients\"])\n  \nif results.content.get(\"failed_attachments\"):\n  noteText += u\"\"\"\\nWarning: Exchange Online send message - One or more attachments failed to attach to the message. \nUnable to find a matching attachment name on incident for the following names. Are they spelled correctly and was the extension included?\nFailed attachment names: {}\"\"\".format(\", \".join(results.content[\"failed_attachments\"]))\n\nincident.addNote(noteText)",
          "tags": [],
          "uuid": "508b968d-cfd5-4a7c-9182-1220f7538dae"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "c3847b8d-a57a-4050-b5c8-004f6e595172",
            "element": "field_uuid",
            "field_type": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "b9b4a3be-cb80-40e4-8fa2-5f91a8b6e9d5",
            "element": "field_uuid",
            "field_type": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "a752b520-1380-42b0-8851-6fee284dc442",
            "element": "field_uuid",
            "field_type": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "6c1707eb-8cd2-4030-ae75-5e2963ad5a5c",
            "element": "field_uuid",
            "field_type": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          },
          {
            "content": "7bfa0bca-f886-4140-ab02-84d85b0fbfcb",
            "element": "field_uuid",
            "field_type": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_send_message",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_a6e61054-fd2e-4ade-86fc-693442bd6688",
        "id": 16,
        "name": "playbook_a6e61054_fd2e_4ade_86fc_693442bd6688",
        "type": "playbook",
        "uuid": "c1324529-22fd-49c3-b462-22860541f042"
      },
      "tags": [],
      "type": "default",
      "uuid": "a6e61054-fd2e-4ade-86fc-693442bd6688",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d\" isExecutable=\"true\" name=\"playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0qamyww\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Write Message as Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"dbb5e3de-0f43-4c7e-b09f-5d50f0ce426c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.incident_id = incident.id\\n#inputs.task_id = task.id\\ninputs.exo_attachment_name = playbook.inputs.exchange_online_attachment_name\\ninputs.exo_email_address = row.exo_dt_email_address\\ninputs.exo_messages_id = row.exo_dt_message_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_write_message_as_attachment_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0qamyww\u003c/incoming\u003e\u003coutgoing\u003eFlow_0sua2p7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0qamyww\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cendEvent id=\"EndPoint_2\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0sua2p7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0sua2p7\" sourceRef=\"ServiceTask_1\" targetRef=\"EndPoint_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0qamyww\" id=\"Flow_0qamyww_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"248\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0sua2p7\" id=\"Flow_0sua2p7_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"332\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"484\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"248\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_2\" id=\"EndPoint_2_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"654.5\" y=\"483.5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812130892,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Write Message EML as Attachment (PB)",
      "export_key": "example_exchange_online_write_message_eml_as_attachment",
      "field_type_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Write Message EML as Attachment (PB)",
        "export_key": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
        "fields": {
          "exchange_online_attachment_name": {
            "allow_default_value": false,
            "blank_option": false,
            "calculated": false,
            "changeable": true,
            "chosen": false,
            "default_chosen_by_server": false,
            "deprecated": false,
            "export_key": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d/exchange_online_attachment_name",
            "hide_notification": false,
            "id": 719,
            "input_type": "text",
            "internal": false,
            "is_tracked": false,
            "name": "exchange_online_attachment_name",
            "operation_perms": {},
            "operations": [],
            "placeholder": "",
            "prefix": null,
            "read_only": false,
            "rich_text": false,
            "tags": [],
            "templates": [],
            "text": "Attachment Name",
            "tooltip": "",
            "type_id": 1019,
            "uuid": "8d7bc3e3-8e54-4273-ac25-999908c80763",
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
        "type_name": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
        "uuid": "d4e81545-a39c-43f3-ad96-79f339527b50"
      },
      "has_logical_errors": false,
      "id": 17,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686812131425,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "exo_message_query_results_dt.exo_dt_status",
              "method": "equals",
              "type": null,
              "value": "Active"
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "8d7bc3e3-8e54-4273-ac25-999908c80763",
            "element": "field_uuid",
            "field_type": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "example_exchange_online_write_message_eml_as_attachment",
      "object_type": "exo_message_query_results_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_79bda643-c6bb-4d10-82a6-f894fd982d2d",
        "id": 17,
        "name": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
        "type": "playbook",
        "uuid": "34dca8cc-a9a4-419a-b34f-b17a8421493c"
      },
      "tags": [],
      "type": "default",
      "uuid": "79bda643-c6bb-4d10-82a6-f894fd982d2d",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 1,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"http://www.camunda.org/test\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\u003e\u003cprocess id=\"playbook_ac12d839_f46a_4252_901f_77862961e1f6\" isExecutable=\"true\" name=\"playbook_ac12d839_f46a_4252_901f_77862961e1f6\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0238nai\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"Exchange Online: Get Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4748898-439e-496a-bbba-93fbc51582c3\"\u003e{\"inputs\":{},\"pre_processing_script\":\"inputs.exo_email_address = row.exo_dt_email_address\\ninputs.exo_messages_id = row.exo_dt_message_id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"exchange_online_get_message_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0238nai\u003c/incoming\u003e\u003coutgoing\u003eFlow_1tlyv8k\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"exchange_online_write_message_json_as_note_post_process\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"a5f0e298-85e6-491b-af57-08b07ca70365\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tlyv8k\u003c/incoming\u003e\u003coutgoing\u003eFlow_160psfo\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_160psfo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0238nai\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003csequenceFlow id=\"Flow_1tlyv8k\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003csequenceFlow id=\"Flow_160psfo\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_ac12d839_f46a_4252_901f_77862961e1f6\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0238nai\" id=\"Flow_0238nai_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"218\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tlyv8k\" id=\"Flow_1tlyv8k_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"302\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"418\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_160psfo\" id=\"Flow_160psfo_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"502\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"594\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"199.65\" x=\"621\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"218\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"655\" y=\"594\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"418\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1686812131395,
      "creator_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "deployment_id": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "Example: Exchange Online Write Message JSON as Note (PB)",
      "export_key": "example_exchange_online_write_message_json_as_note",
      "field_type_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
      "fields_type": {
        "actions": [],
        "display_name": "Example: Exchange Online Write Message JSON as Note (PB)",
        "export_key": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
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
        "type_name": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
        "uuid": "d4682b24-9f47-42c5-9886-504d6800a752"
      },
      "has_logical_errors": false,
      "id": 18,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "dev-integration",
        "id": 9,
        "name": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
        "type": "apikey"
      },
      "last_modified_time": 1686812131946,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1686812131514,
          "description": "",
          "enabled": false,
          "export_key": "exchange_online_write_message_json_as_note_post_process",
          "id": 18,
          "language": "python3",
          "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
          "last_modified_time": 1686812131539,
          "name": "exchange_online_write_message_json_as_note_post_process",
          "object_type": "exo_message_query_results_dt",
          "playbook_handle": "example_exchange_online_write_message_json_as_note",
          "programmatic_name": "example_exchange_online_write_message_json_as_note_exchange_online_write_message_json_as_note_post_process",
          "script_text": "results=playbook.functions.results.exchange_online_get_message_result\n# Print the message to an incident note if it is found, otherwise update the status as Not Found in the datatable.\nif results.content[\"error\"] is not None:\n  noteText = u\"Exchange Online message NOT FOUND: \\n email address: {0}\\n message ID: {1}\\n{2}\".format(results.inputs[\"exo_email_address\"], results.inputs[\"exo_messages_id\"], results.pretty_string)\n  row.exo_dt_status = \"Not Found\"\n  row.exo_dt_web_link = \"\"\nelse:\n  noteText = u\"Exchange Online email address: {0} message:\\n{1}\".format(results.inputs[\"exo_email_address\"], results.pretty_string)\n\nincident.addNote(noteText)",
          "tags": [],
          "uuid": "a5f0e298-85e6-491b-af57-08b07ca70365"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "exo_message_query_results_dt.exo_dt_status",
              "method": "equals",
              "type": null,
              "value": "Active"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "example_exchange_online_write_message_json_as_note",
      "object_type": "exo_message_query_results_dt",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_ac12d839-f46a-4252-901f-77862961e1f6",
        "id": 18,
        "name": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
        "type": "playbook",
        "uuid": "9ce43e3c-6fff-415e-aeb9-7a06fbb682d2"
      },
      "tags": [],
      "type": "default",
      "uuid": "ac12d839-f46a-4252-901f-77862961e1f6",
      "version": 4
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1686811439007,
      "description": "Create \"Email Recipient\", \"Email Sender\" and \"Email Subject\" artifacts from a message row-entry in the Exchange Online Message Query Results data table.",
      "enabled": false,
      "export_key": "Exchange Online Create Artifacts from Message",
      "id": 9,
      "language": "python",
      "last_modified_by": "c3be9c35-c18c-4fac-bae5-9a7d483f1db2",
      "last_modified_time": 1686811439028,
      "name": "Exchange Online Create Artifacts from Message",
      "object_type": "exo_message_query_results_dt",
      "playbook_handle": null,
      "programmatic_name": "exchange_online_create_artifacts_from_message",
      "script_text": "artifact_description = u\"Created by Exchange Online Query Results for artifact value: {}\".format(row.exo_dt_email_address)\nartifact_type = \"Email Recipient\"\nartifact_value = row.exo_dt_email_address\nif artifact_value:\n  incident.addArtifact(artifact_type, artifact_value, artifact_description)\n  \nartifact_description = u\"Created by Exchange Online Query Results for artifact value: {}\".format(row.exo_dt_sender_email)\nartifact_type = \"Email Sender\"\nartifact_value = row.exo_dt_sender_email\nif artifact_value:\n  incident.addArtifact(artifact_type, artifact_value, artifact_description)\n  \nartifact_description = u\"Created by Exchange Online Query Results for artifact value: {}\".format(row.exo_dt_message_subject)\nartifact_type = \"Email Subject\"\nartifact_value = row.exo_dt_message_subject\nif artifact_value:\n  incident.addArtifact(artifact_type, artifact_value, artifact_description)\n\n",
      "tags": [
        {
          "tag_handle": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
          "value": "Playbook Tag"
        }
      ],
      "uuid": "ddc0513f-fcbc-4582-a4b3-b80a6bd3ff52"
    }
  ],
  "server_version": {
    "build_number": 8304,
    "major": 47,
    "minor": 0,
    "version": "47.0.8304"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Exchange Online Message Query Results",
      "export_key": "exo_message_query_results_dt",
      "fields": {
        "exo_dt_email_address": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_email_address",
          "hide_notification": false,
          "id": 621,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_email_address",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Queried Email Address",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "1430b4c0-c77e-429d-b698-62cb9a6c336b",
          "values": [],
          "width": 62
        },
        "exo_dt_has_attachments": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_has_attachments",
          "hide_notification": false,
          "id": 622,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_has_attachments",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Has Attachments",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "1818d9f2-ef0f-4981-821a-8b0e6b9f95a8",
          "values": [],
          "width": 98
        },
        "exo_dt_message_folder": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_message_folder",
          "hide_notification": false,
          "id": 793,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_message_folder",
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
          "text": "Folder",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "11dad6f2-6f90-47b9-8c5e-af24619471e4",
          "values": [],
          "width": 48
        },
        "exo_dt_message_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_message_id",
          "hide_notification": false,
          "id": 623,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_message_id",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Message ID",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "89c605ce-2aaf-4b13-acd6-db150f977a87",
          "values": [],
          "width": 66
        },
        "exo_dt_message_subject": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_message_subject",
          "hide_notification": false,
          "id": 624,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_message_subject",
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
          "text": "Message Subject",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "c67414a0-30bd-43bb-9b86-2cbdbee79bfa",
          "values": [],
          "width": 154
        },
        "exo_dt_query_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_query_date",
          "hide_notification": false,
          "id": 625,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_query_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Query Date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "90d213d4-6efe-4d31-85d2-dc668afb86be",
          "values": [],
          "width": 45
        },
        "exo_dt_received_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_received_date",
          "hide_notification": false,
          "id": 626,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_received_date",
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
          "text": "Received Date",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "6d199c33-e39c-4377-9a35-32343470d380",
          "values": [],
          "width": 69
        },
        "exo_dt_sender_email": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_sender_email",
          "hide_notification": false,
          "id": 627,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_sender_email",
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
          "text": "Sender Email",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "0244ca3e-a694-41a8-9ce3-569cad2d5be5",
          "values": [],
          "width": 147
        },
        "exo_dt_status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_status",
          "hide_notification": false,
          "id": 628,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_status",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": true,
          "short_text": "",
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "ee39ace4-a7de-434b-be20-37f8d1c89667",
          "values": [],
          "width": 49
        },
        "exo_dt_web_link": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "exo_message_query_results_dt/exo_dt_web_link",
          "hide_notification": false,
          "id": 629,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "exo_dt_web_link",
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
          "text": "Web Link",
          "tooltip": "",
          "type_id": 1009,
          "uuid": "e6975596-3553-4f9b-abc9-d8e18bf6f249",
          "values": [],
          "width": 88
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
      "tags": [
        {
          "tag_handle": "playbook_2dca7324_8232_49aa_8029_3cf955c689b0",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_45f7d606_5f20_4a3b_8bdb_1b9dc501650f",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_79bda643_c6bb_4d10_82a6_f894fd982d2d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_8685fa14_9e7f_4140_a974_886711daf91d",
          "value": "Playbook Tag"
        },
        {
          "tag_handle": "playbook_ac12d839_f46a_4252_901f_77862961e1f6",
          "value": "Playbook Tag"
        }
      ],
      "type_id": 8,
      "type_name": "exo_message_query_results_dt",
      "uuid": "977bd347-12f0-489a-b1a4-68287d63a367"
    }
  ],
  "workflows": [],
  "workspaces": []
}
