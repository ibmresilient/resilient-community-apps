{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Google Cloud - Inspect Attachment for PII",
      "id": 34,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Google Cloud - Inspect Attachment for PII",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "35ecc5d3-b63d-44c7-b4aa-27df01a8a15c",
      "view_items": [],
      "workflows": [
        "gcp_dlp_inspect_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Google Cloud - Remove PII from Attachment",
      "id": 35,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Google Cloud - Remove PII from Attachment",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "79923e7e-deae-41d9-9080-acb3435e2a9d",
      "view_items": [],
      "workflows": [
        "gcp_dlp_deidentify_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "Email Attachment",
            "Malware Sample",
            "Other File",
            "String",
            "X509 Certificate File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Google Cloud - Remove PII from String",
      "id": 36,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Google Cloud - Remove PII from String",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "46a67a64-d12d-4bdf-8f8b-14b9a3102c3f",
      "view_items": [],
      "workflows": [
        "gcp_dlp_deidentify_artifact"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1655926718803,
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
      "id": 289,
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
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_urlscanio",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
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
      "export_key": "__function/artifact_id",
      "hide_notification": false,
      "id": 290,
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
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
      "templates": [],
      "text": "artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
      "export_key": "__function/gcp_dlp_info_types",
      "hide_notification": false,
      "id": 297,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "gcp_dlp_info_types",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "templates": [],
      "text": "gcp_dlp_info_types",
      "tooltip": "Which types of PII do you want to de-identify.",
      "type_id": 11,
      "uuid": "dac1b61a-dc30-403e-804c-079398551459",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AMERICAN_BANKERS_CUSIP_ID",
          "properties": null,
          "uuid": "53feb186-add8-411b-821a-4533a9516a50",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AUSTRALIA_MEDICARE_NUMBER",
          "properties": null,
          "uuid": "0d25e9ae-9385-4553-b0df-c4162673af9c",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AUSTRALIA_TAX_FILE_NUMBER",
          "properties": null,
          "uuid": "c4744f0a-5822-4f39-bb56-9c8a86f38cb5",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BRAZIL_CPF_NUMBER",
          "properties": null,
          "uuid": "fd3ad059-07ff-4ac2-b3b1-a20006367653",
          "value": 55
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_BC_PHN",
          "properties": null,
          "uuid": "385f06c2-a235-48ab-845b-8467ec4b8d48",
          "value": 56
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_DRIVERS_LICENSE_NUMBER",
          "properties": null,
          "uuid": "6f3241ef-da68-474e-8575-e87a8342d086",
          "value": 57
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_OHIP",
          "properties": null,
          "uuid": "840f946f-7a8a-464f-a351-fb164a66a54e",
          "value": 58
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_PASSPORT",
          "properties": null,
          "uuid": "b95ca022-e50f-4bab-bbcf-c1e3709b861f",
          "value": 59
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_QUEBEC_HIN",
          "properties": null,
          "uuid": "c545c601-563f-4c87-a69a-b343f8689881",
          "value": 60
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CANADA_SOCIAL_INSURANCE_NUMBER",
          "properties": null,
          "uuid": "4cdad83e-c2fe-4cb7-bd0e-d0e130e94056",
          "value": 61
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CHINA_PASSPORT",
          "properties": null,
          "uuid": "2fb2f392-8afc-4324-af14-338aacc7fc04",
          "value": 62
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "CREDIT_CARD_NUMBER",
          "properties": null,
          "uuid": "e37d895d-fed3-4a7e-8f30-a33ff6903968",
          "value": 63
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "EMAIL_ADDRESS",
          "properties": null,
          "uuid": "6c6b51dc-88f0-4f1d-bae8-3c01daf4a46d",
          "value": 64
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ETHNIC_GROUP",
          "properties": null,
          "uuid": "79368d0f-d76f-496d-ab2c-60ca5e6e41a6",
          "value": 65
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FEMALE_NAME",
          "properties": null,
          "uuid": "fe664b7b-a713-47d3-9b1d-dcd7e5c80026",
          "value": 66
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "FIRST_NAME",
          "properties": null,
          "uuid": "00a4bbe7-c3b1-4a4d-adfe-0e0eeb9696ca",
          "value": 67
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FRANCE_CNI",
          "properties": null,
          "uuid": "7957a965-0e28-4dcb-b353-f7d3d78da775",
          "value": 68
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FRANCE_NIR",
          "properties": null,
          "uuid": "5c09b4b9-f6d1-44bf-ae7b-fec607802233",
          "value": 69
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FRANCE_PASSPORT",
          "properties": null,
          "uuid": "c32a8bba-5689-4741-8b29-6f6e85696383",
          "value": 70
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GCP_CREDENTIALS",
          "properties": null,
          "uuid": "993aed01-86d8-420b-91bb-0aa449ee925f",
          "value": 71
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GERMANY_PASSPORT",
          "properties": null,
          "uuid": "1ecfe406-c3e3-46b5-aada-6df600e9d3c4",
          "value": 72
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "IBAN_CODE",
          "properties": null,
          "uuid": "9e96cde2-9496-40f5-a408-96b42199f320",
          "value": 73
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "IMEI_HARDWARE_ID",
          "properties": null,
          "uuid": "7ab92b4a-d4dc-4cb1-bab9-b0e24076d82f",
          "value": 74
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "INDIA_PAN_INDIVIDUAL",
          "properties": null,
          "uuid": "c6a17cc8-66c3-4f1e-a94c-0243e1b38fc8",
          "value": 75
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "IP_ADDRESS",
          "properties": null,
          "uuid": "7cf7ad56-3469-485f-aea8-509c4679790b",
          "value": 76
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "JAPAN_INDIVIDUAL_NUMBER",
          "properties": null,
          "uuid": "258b3210-b6a1-4214-bf11-3f0a798acd80",
          "value": 77
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "JAPAN_PASSPORT",
          "properties": null,
          "uuid": "52eab8df-4dfe-4257-967f-581377af5c4c",
          "value": 78
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "KOREA_PASSPORT",
          "properties": null,
          "uuid": "bc4909f7-9520-4b31-b8ef-915e73a6ee9c",
          "value": 79
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "KOREA_RRN",
          "properties": null,
          "uuid": "5e375b41-5646-438b-9ca3-6df80b91435a",
          "value": 80
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "LAST_NAME",
          "properties": null,
          "uuid": "ebd94a3b-2a44-47cf-bec6-503424ab7a6c",
          "value": 81
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MAC_ADDRESS_LOCAL",
          "properties": null,
          "uuid": "7691f7da-8bad-4eb2-8808-c78be8bccdc5",
          "value": 82
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "MAC_ADDRESS",
          "properties": null,
          "uuid": "06a86258-ea5e-431d-ba80-b991b0e317e8",
          "value": 83
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MALE_NAME",
          "properties": null,
          "uuid": "30d03e3d-24f3-4b38-9907-5bd45f847e89",
          "value": 84
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MEXICO_CURP_NUMBER",
          "properties": null,
          "uuid": "1cddbd5f-5c86-4d54-8913-78a97a55ae97",
          "value": 85
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MEXICO_PASSPORT",
          "properties": null,
          "uuid": "a263fd06-6cd2-4b66-b6ac-a531a4d243c9",
          "value": 86
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NETHERLANDS_BSN_NUMBER",
          "properties": null,
          "uuid": "d2c6c6d7-cb3e-4999-a0ae-8209cc97417e",
          "value": 87
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NORWAY_NI_NUMBER",
          "properties": null,
          "uuid": "b208068c-86c3-49d1-b9e8-918c7a99be83",
          "value": 88
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "PHONE_NUMBER",
          "properties": null,
          "uuid": "473e24d1-5835-42a4-a13c-f97ba236b4e9",
          "value": 89
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPAIN_NIE_NUMBER",
          "properties": null,
          "uuid": "06b42df7-d644-4c1f-a613-3b04ef2f2f38",
          "value": 90
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPAIN_NIF_NUMBER",
          "properties": null,
          "uuid": "149e6a22-3e17-43d3-b283-84316414312c",
          "value": 91
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPAIN_PASSPORT",
          "properties": null,
          "uuid": "21e3514f-8321-47eb-b927-629bf90f7c48",
          "value": 92
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SWIFT_CODE",
          "properties": null,
          "uuid": "ebf9fb9f-376d-41b8-bc39-cb0065ee1ee9",
          "value": 93
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UK_DRIVERS_LICENSE_NUMBER",
          "properties": null,
          "uuid": "01044402-0435-49d8-990f-c0e167576cf7",
          "value": 94
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
          "properties": null,
          "uuid": "74511bee-2deb-4ad6-aade-2ae139c202e5",
          "value": 95
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UK_NATIONAL_INSURANCE_NUMBER",
          "properties": null,
          "uuid": "d5b73310-17bf-41d6-967f-248b7dd1cbef",
          "value": 96
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UK_PASSPORT",
          "properties": null,
          "uuid": "4fa9e3b5-95db-4925-b095-faebe711a385",
          "value": 97
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UK_TAXPAYER_REFERENCE",
          "properties": null,
          "uuid": "650109ee-1c33-4907-9db3-1df3b1620563",
          "value": 98
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_ADOPTION_TAXPAYER_IDENTIFICATION_NUMBER",
          "properties": null,
          "uuid": "40f79122-2a05-4d01-8b58-a2eb17e0d9be",
          "value": 99
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_BANK_ROUTING_MICR",
          "properties": null,
          "uuid": "27279a30-b9cd-4b6e-9414-fda7d9d216ed",
          "value": 100
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_DEA_NUMBER",
          "properties": null,
          "uuid": "346c41ab-d773-4fcf-930d-5905542544b6",
          "value": 101
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_DRIVERS_LICENSE_NUMBER",
          "properties": null,
          "uuid": "9b0a4731-38fc-44d0-9e01-6c267ba9ebda",
          "value": 102
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_HEALTHCARE_NPI",
          "properties": null,
          "uuid": "1b58a29f-22d8-4467-8712-0225be70ee20",
          "value": 103
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER",
          "properties": null,
          "uuid": "7b9ac7ef-9241-4b0e-a149-2d730cb6f149",
          "value": 104
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_PASSPORT",
          "properties": null,
          "uuid": "0a90ad49-480d-4ce6-93f0-b7842576f477",
          "value": 105
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_PREPARER_TAXPAYER_IDENTIFICATION_NUMBER",
          "properties": null,
          "uuid": "803168c4-a2e0-4936-b6dc-ae5dccdb1216",
          "value": 106
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_SOCIAL_SECURITY_NUMBER",
          "properties": null,
          "uuid": "46b361b5-0852-49d2-9160-32fdb6d118eb",
          "value": 107
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_TOLLFREE_PHONE_NUMBER",
          "properties": null,
          "uuid": "ed7aa1ac-1fea-4f75-9f33-52c336fa0446",
          "value": 108
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_VEHICLE_IDENTIFICATION_NUMBER",
          "properties": null,
          "uuid": "75528b91-58d7-498a-b9e7-5a237dacc51f",
          "value": 109
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_STATE",
          "properties": null,
          "uuid": "30728572-057d-4576-a0e6-4a7a306610ba",
          "value": 110
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FDA_CODE",
          "properties": null,
          "uuid": "334600b8-e3ce-4add-b2a5-ed8f942c3d5b",
          "value": 111
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ICD9_CODE",
          "properties": null,
          "uuid": "a8af58ea-8825-4293-99d0-0fb445cc1f45",
          "value": 112
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ICD10_CODE",
          "properties": null,
          "uuid": "128f9381-54f8-48ac-942f-50fd4c7cdf6a",
          "value": 113
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "US_EMPLOYER_IDENTIFICATION_NUMBER",
          "properties": null,
          "uuid": "ad1cc8a9-e9b5-458f-8d3a-4c668652f844",
          "value": 114
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LOCATION",
          "properties": null,
          "uuid": "0c1e18b6-827a-4bf7-90e3-c53305b318fb",
          "value": 115
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "DATE",
          "properties": null,
          "uuid": "8228a825-bdde-437b-9b62-3fce9330f235",
          "value": 116
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "DATE_OF_BIRTH",
          "properties": null,
          "uuid": "1f486b27-1b3d-42eb-aca2-56e256200a4b",
          "value": 117
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TIME",
          "properties": null,
          "uuid": "1b728d9f-5e07-4094-a7b5-df4a0e5531d4",
          "value": 118
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "PERSON_NAME",
          "properties": null,
          "uuid": "f0b19eee-24b0-4dff-9d5f-8f8136fba7e8",
          "value": 119
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "AGE",
          "properties": null,
          "uuid": "c31de861-11a1-4f51-b081-8d7763921515",
          "value": 120
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GENDER",
          "properties": null,
          "uuid": "979c6684-4377-4456-bf72-806e4660f447",
          "value": 121
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ARGENTINA_DNI_NUMBER",
          "properties": null,
          "uuid": "8fadea4b-bdc8-4170-a8d9-a7b9eccdd7a3",
          "value": 122
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CHILE_CDI_NUMBER",
          "properties": null,
          "uuid": "e8303d25-807e-44aa-9ba2-c74b1b4f850e",
          "value": 123
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "COLOMBIA_CDC_NUMBER",
          "properties": null,
          "uuid": "a992a906-0920-4c31-bd33-fce5c7bd2597",
          "value": 124
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NETHERLANDS_PASSPORT",
          "properties": null,
          "uuid": "5bcac13c-f826-4ac0-b134-94ad65ec41be",
          "value": 125
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PARAGUAY_CIC_NUMBER",
          "properties": null,
          "uuid": "d6173ad1-081a-4bae-bfa4-31e9368215a2",
          "value": 126
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PERU_DNI_NUMBER",
          "properties": null,
          "uuid": "1f187d34-bff0-42f9-a3ae-c215a9e80d17",
          "value": 127
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PORTUGAL_CDC_NUMBER",
          "properties": null,
          "uuid": "b723a172-02fc-4136-8358-3b83f075738c",
          "value": 128
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "URUGUAY_CDI_NUMBER",
          "properties": null,
          "uuid": "757f1bab-60e4-477a-8cd5-bc3a6f37f850",
          "value": 129
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VENEZUELA_CDI_NUMBER",
          "properties": null,
          "uuid": "bc84b498-96e8-4caf-9b3f-693255d5ded3",
          "value": 130
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "DOMAIN_NAME",
          "properties": null,
          "uuid": "a7dfc1b4-49eb-478d-a30f-40e2bfdc13aa",
          "value": 131
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CHINA_RESIDENT_ID_NUMBER",
          "properties": null,
          "uuid": "3a44a228-ae4a-47cf-b49c-a7300aadce39",
          "value": 132
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "POLAND_PESEL_NUMBER",
          "properties": null,
          "uuid": "3699cbeb-1605-470f-9c19-3cbcdf3161c1",
          "value": 133
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "POLAND_NATIONAL_ID_NUMBER",
          "properties": null,
          "uuid": "d05cc508-6d3b-4545-8917-c299062b47d1",
          "value": 134
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "POLAND_PASSPORT",
          "properties": null,
          "uuid": "1425484d-0af3-4955-bb5b-183571cd3f4f",
          "value": 135
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SWEDEN_PASSPORT",
          "properties": null,
          "uuid": "e1dae86a-a93c-4018-9072-ee6395e3b08b",
          "value": 136
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SWEDEN_NATIONAL_ID_NUMBER",
          "properties": null,
          "uuid": "114792dd-8771-4d89-a91c-ecc5a71598ab",
          "value": 137
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FINLAND_NATIONAL_ID_NUMBER",
          "properties": null,
          "uuid": "84399e2d-9677-4793-9304-a4e717de933a",
          "value": 138
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "JAPAN_BANK_ACCOUNT",
          "properties": null,
          "uuid": "4263a5ab-d5fe-47f7-b753-62b900235d4b",
          "value": 139
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "JAPAN_DRIVERS_LICENSE_NUMBER",
          "properties": null,
          "uuid": "28955f89-7977-4eda-b2cf-805e88b16461",
          "value": 140
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPAIN_DRIVERS_LICENSE_NUMBER",
          "properties": null,
          "uuid": "f0720d56-0d48-4927-904f-40d1327f3e71",
          "value": 141
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "URL",
          "properties": null,
          "uuid": "0f0ba9bc-a573-4385-bcff-05e71e2b3772",
          "value": 142
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DENMARK_CPR_NUMBER",
          "properties": null,
          "uuid": "a213301d-99ca-4c4e-a1d4-e0691d68ef00",
          "value": 143
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
      "id": 298,
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
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
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
      "export_key": "__function/attachment_id",
      "hide_notification": false,
      "id": 291,
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
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        },
        {
          "tag_handle": "fn_virustotal",
          "value": null
        }
      ],
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
      "export_key": "__function/gcp_artifact_input",
      "hide_notification": false,
      "id": 299,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "gcp_artifact_input",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "templates": [],
      "text": "gcp_artifact_input",
      "tooltip": "A optional input to be used when the function is ran from an artifact and is used to capture the artifacts value.",
      "type_id": 11,
      "uuid": "73ccbbd1-7050-433e-97a3-321d8d52e35e",
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
      "created_date": 1655912150258,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "fn_google_cloud_dlp",
      "display_name": "Google Cloud DLP: De-Identify Content",
      "export_key": "google_cloud_dlp_deidentify_content",
      "id": 14,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1655923947711,
      "name": "google_cloud_dlp_deidentify_content",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"de_identified_text\": \"My email is ############################\"}, \"raw\": \"{\\\"de_identified_text\\\": \\\"My email is ############################\\\"}\", \"inputs\": {\"gcp_dlp_info_types\": [{\"id\": 63, \"name\": \"CREDIT_CARD_NUMBER\"}, {\"id\": 64, \"name\": \"EMAIL_ADDRESS\"}, {\"id\": 67, \"name\": \"FIRST_NAME\"}, {\"id\": 73, \"name\": \"IBAN_CODE\"}, {\"id\": 76, \"name\": \"IP_ADDRESS\"}, {\"id\": 81, \"name\": \"LAST_NAME\"}, {\"id\": 83, \"name\": \"MAC_ADDRESS\"}, {\"id\": 89, \"name\": \"PHONE_NUMBER\"}, {\"id\": 116, \"name\": \"DATE\"}, {\"id\": 117, \"name\": \"DATE_OF_BIRTH\"}, {\"id\": 119, \"name\": \"PERSON_NAME\"}, {\"id\": 120, \"name\": \"AGE\"}, {\"id\": 131, \"name\": \"DOMAIN_NAME\"}, {\"id\": 142, \"name\": \"URL\"}], \"incident_id\": 2103, \"gcp_artifact_input\": \"My email is johnsmith@gmail.com\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-google-cloud-dlp\", \"package_version\": \"1.2.0\", \"host\": \"christohersmbp2.cambridge.ibm.com\", \"execution_time_ms\": 26887, \"timestamp\": \"2022-06-22 13:11:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"de_identified_text\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"gcp_dlp_info_types\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}}}}, \"incident_id\": {\"type\": \"integer\"}, \"gcp_artifact_input\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "uuid": "1dd74d85-887d-4d5c-beda-640630d317c1",
      "version": 2,
      "view_items": [
        {
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "content": "73ccbbd1-7050-433e-97a3-321d8d52e35e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dac1b61a-dc30-403e-804c-079398551459",
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
          "name": "Example: Google Cloud DLP - De-Identify Artifact",
          "object_type": "artifact",
          "programmatic_name": "gcp_dlp_deidentify_artifact",
          "tags": [
            {
              "tag_handle": "fn_google_cloud_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 30
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Google Cloud DLP - De-Identify Attachment",
          "object_type": "attachment",
          "programmatic_name": "gcp_dlp_deidentify_attachment",
          "tags": [
            {
              "tag_handle": "fn_google_cloud_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 29
        }
      ]
    },
    {
      "created_date": 1655912150377,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "fn_google_cloud_dlp",
      "display_name": "Google Cloud DLP: Inspect Content",
      "export_key": "google_cloud_dlp_inspect_content",
      "id": 15,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1655923947757,
      "name": "google_cloud_dlp_inspect_content",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "uuid": "eca925ca-bea4-4f76-9afd-cc4b02a2083a",
      "version": 2,
      "view_items": [
        {
          "content": "da8b8ba4-28a3-4ad0-b35a-354b1bc59fd6",
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
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
          "content": "73ccbbd1-7050-433e-97a3-321d8d52e35e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dac1b61a-dc30-403e-804c-079398551459",
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
          "name": "Example: Google Cloud DLP - Inspect Attachment for PII",
          "object_type": "attachment",
          "programmatic_name": "gcp_dlp_inspect_attachment",
          "tags": [
            {
              "tag_handle": "fn_google_cloud_dlp",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 28
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 105,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1655926717232,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1655926717232,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea",
        "23b46b1b-bd7a-4e23-9f54-21f71c97020b"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_google_cloud_dlp",
      "name": "Google Cloud DLP: Message Destination",
      "programmatic_name": "fn_google_cloud_dlp",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "users": [],
      "uuid": "473e731c-c19c-4d92-ac61-809cd3a923ab"
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
        "version": 8,
        "workflow_id": "gcp_dlp_deidentify_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"gcp_dlp_deidentify_attachment\" isExecutable=\"true\" name=\"Example: Google Cloud DLP - De-Identify Attachment\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow ran at an attachment level that sends the attachment data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. The return result is a new attachment with the PII removed.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1u824h5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0k4g9bu\" name=\"Google Cloud DLP: De-Identify Con...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1dd74d85-887d-4d5c-beda-640630d317c1\"\u003e{\"inputs\":{\"dac1b61a-dc30-403e-804c-079398551459\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"e37d895d-fed3-4a7e-8f30-a33ff6903968\",\"6c6b51dc-88f0-4f1d-bae8-3c01daf4a46d\",\"9e96cde2-9496-40f5-a408-96b42199f320\",\"ebd94a3b-2a44-47cf-bec6-503424ab7a6c\",\"06a86258-ea5e-431d-ba80-b991b0e317e8\",\"473e24d1-5835-42a4-a13c-f97ba236b4e9\",\"46b361b5-0852-49d2-9160-32fdb6d118eb\",\"8228a825-bdde-437b-9b62-3fce9330f235\",\"1f486b27-1b3d-42eb-aca2-56e256200a4b\",\"f0b19eee-24b0-4dff-9d5f-8f8136fba7e8\",\"c31de861-11a1-4f51-b081-8d7763921515\",\"a7dfc1b4-49eb-478d-a30f-40e2bfdc13aa\",\"0f0ba9bc-a573-4385-bcff-05e71e2b3772\"]}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.incident_id = incident.id \\n\\n# If this workflow has the task_id available, gather it incase we need it.\\nif task:\\n  inputs.task_id = task.id\\n# If this workflow has the attachment_id available, gather it incase we need it.\\nif attachment:\\n  inputs.attachment_id = attachment.id\\n\\n# If this workflow has the artifact_id available, gather it incase we need it.\\ntry: \\n  if artifact:\\n    inputs.artifact_id = artifact.id\\nexcept:\\n  pass\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1u824h5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c53ji1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_10gh3ua\"\u003e\u003cincoming\u003eSequenceFlow_0c53ji1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c53ji1\" sourceRef=\"ServiceTask_0k4g9bu\" targetRef=\"EndEvent_10gh3ua\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1u824h5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0k4g9bu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0k4g9bu\" id=\"ServiceTask_0k4g9bu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"463\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10gh3ua\" id=\"EndEvent_10gh3ua_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"781\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"799\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c53ji1\" id=\"SequenceFlow_0c53ji1_di\"\u003e\u003comgdi:waypoint x=\"563\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"672\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1u824h5\" id=\"SequenceFlow_1u824h5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"330.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "0228e00e-2c47-43e6-a736-550f104c94ea",
      "description": "An example workflow ran at an attachment level that sends the attachment data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. The return result is a new attachment with the PII removed.",
      "export_key": "gcp_dlp_deidentify_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1655926686533,
      "name": "Example: Google Cloud DLP - De-Identify Attachment",
      "object_type": "attachment",
      "programmatic_name": "gcp_dlp_deidentify_attachment",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "uuid": "82dedecb-172c-492e-8b8e-619a5a070a5b",
      "workflow_id": 29
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "gcp_dlp_inspect_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"gcp_dlp_inspect_attachment\" isExecutable=\"true\" name=\"Example: Google Cloud DLP - Inspect Attachment for PII\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow ran at an attachment level that sends the attachment data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. Returned results include a list of findings generated from the input including the finding itself, what type of info it was matched against and the likelihood that the match is accurate.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1u824h5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0k4g9bu\" name=\"Google Cloud DLP: Inspect Content\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"eca925ca-bea4-4f76-9afd-cc4b02a2083a\"\u003e{\"inputs\":{\"dac1b61a-dc30-403e-804c-079398551459\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"e37d895d-fed3-4a7e-8f30-a33ff6903968\",\"6c6b51dc-88f0-4f1d-bae8-3c01daf4a46d\",\"00a4bbe7-c3b1-4a4d-adfe-0e0eeb9696ca\",\"9e96cde2-9496-40f5-a408-96b42199f320\",\"7cf7ad56-3469-485f-aea8-509c4679790b\",\"ebd94a3b-2a44-47cf-bec6-503424ab7a6c\",\"06a86258-ea5e-431d-ba80-b991b0e317e8\",\"473e24d1-5835-42a4-a13c-f97ba236b4e9\",\"8228a825-bdde-437b-9b62-3fce9330f235\",\"1f486b27-1b3d-42eb-aca2-56e256200a4b\",\"f0b19eee-24b0-4dff-9d5f-8f8136fba7e8\",\"c31de861-11a1-4f51-b081-8d7763921515\",\"a7dfc1b4-49eb-478d-a30f-40e2bfdc13aa\",\"0f0ba9bc-a573-4385-bcff-05e71e2b3772\"]}}},\"post_processing_script\":\"if results.success:\\n  \\\"\\\"\\\"Print all the findings as a richtext note. This note may be very long if you run the integration on a large file with lots of PII. In these cases you may want to limit how many findings are put into the note.\\\"\\\"\\\"\\n  if results.content[\u0027findings\u0027] != None:\\n    note_text = u\\\"\\\"\\\"Findings were found from attachment \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\u0026lt;br\u0026gt; Findings: \u0026lt;br\u0026gt;\\\"\\\"\\\".format(results.content[\\\"attachment_name\\\"])\\n    for finding in results.content[\u0027findings\u0027]:\\n      note_text += u\\\"\\\"\\\"Text Quote: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\n                      \u0026lt;br\u0026gt; Information Type Suspected: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\n                      \u0026lt;br\u0026gt; Likelihood / Confidence: \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\"\\\"\\\".format(finding[\\\"quote\\\"],finding[\\\"info_type\\\"],finding[\\\"likelihood\\\"])\\n                      \\n    incident.addNote(helper.createRichText(note_text))\",\"pre_processing_script\":\"inputs.incident_id = incident.id \\n\\n# If this workflow has the task_id available, gather it incase we need it.\\nif task:\\n  inputs.task_id = task.id\\n# If this workflow has the attachment_id available, gather it incase we need it.\\nif attachment:\\n  inputs.attachment_id = attachment.id\\n\\n# If this workflow has the artifact_id available, gather it incase we need it.\\ntry: \\n  if artifact:\\n    inputs.artifact_id = artifact.id\\nexcept:\\n  pass\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1u824h5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c53ji1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_10gh3ua\"\u003e\u003cincoming\u003eSequenceFlow_0c53ji1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c53ji1\" sourceRef=\"ServiceTask_0k4g9bu\" targetRef=\"EndEvent_10gh3ua\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1u824h5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0k4g9bu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0k4g9bu\" id=\"ServiceTask_0k4g9bu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"463\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10gh3ua\" id=\"EndEvent_10gh3ua_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"781\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"799\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c53ji1\" id=\"SequenceFlow_0c53ji1_di\"\u003e\u003comgdi:waypoint x=\"563\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"781\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"672\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1u824h5\" id=\"SequenceFlow_1u824h5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"330.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "0228e00e-2c47-43e6-a736-550f104c94ea",
      "description": "An example workflow ran at an attachment level that sends the attachment data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. Returned results include a list of findings generated from the input including the finding itself, what type of info it was matched against and the likelihood that the match is accurate.",
      "export_key": "gcp_dlp_inspect_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1655923948061,
      "name": "Example: Google Cloud DLP - Inspect Attachment for PII",
      "object_type": "attachment",
      "programmatic_name": "gcp_dlp_inspect_attachment",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "uuid": "bcc81226-69fa-457f-8853-a1961de9e8e1",
      "workflow_id": 28
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "gcp_dlp_deidentify_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"gcp_dlp_deidentify_artifact\" isExecutable=\"true\" name=\"Example: Google Cloud DLP - De-Identify Artifact\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example workflow ran at an attachment level that sends the artifact data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. The return result is a new note with the PII removed.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ilcc5g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zpzzxc\" name=\"Google Cloud DLP: De-Identify Con...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1dd74d85-887d-4d5c-beda-640630d317c1\"\u003e{\"inputs\":{\"dac1b61a-dc30-403e-804c-079398551459\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[\"e37d895d-fed3-4a7e-8f30-a33ff6903968\",\"6c6b51dc-88f0-4f1d-bae8-3c01daf4a46d\",\"00a4bbe7-c3b1-4a4d-adfe-0e0eeb9696ca\",\"9e96cde2-9496-40f5-a408-96b42199f320\",\"7cf7ad56-3469-485f-aea8-509c4679790b\",\"ebd94a3b-2a44-47cf-bec6-503424ab7a6c\",\"06a86258-ea5e-431d-ba80-b991b0e317e8\",\"473e24d1-5835-42a4-a13c-f97ba236b4e9\",\"8228a825-bdde-437b-9b62-3fce9330f235\",\"1f486b27-1b3d-42eb-aca2-56e256200a4b\",\"f0b19eee-24b0-4dff-9d5f-8f8136fba7e8\",\"c31de861-11a1-4f51-b081-8d7763921515\",\"a7dfc1b4-49eb-478d-a30f-40e2bfdc13aa\",\"0f0ba9bc-a573-4385-bcff-05e71e2b3772\"]}}},\"post_processing_script\":\"\\\"\\\"\\\"\\nIf the integration was successful in operation, return a note with the now de-identified text. \\n\\\"\\\"\\\"\\nif results.success:\\n  incident.addNote(u\\\"\\\"\\\"De-Identified using Google Cloud DLP\u0026lt;b\u0026gt;{}\u0026lt;b\u0026gt;\\\"\\\"\\\".format(results.content[\\\"de_identified_text\\\"]))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\nif artifact.type == \\\"String\\\":\\n  inputs.gcp_artifact_input = artifact.value\\nelse:\\n  inputs.artifact_id = artifact.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ilcc5g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ewcngu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ilcc5g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0zpzzxc\"/\u003e\u003cendEvent id=\"EndEvent_1636vpj\"\u003e\u003cincoming\u003eSequenceFlow_1ewcngu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ewcngu\" sourceRef=\"ServiceTask_0zpzzxc\" targetRef=\"EndEvent_1636vpj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zpzzxc\" id=\"ServiceTask_0zpzzxc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"456\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ilcc5g\" id=\"SequenceFlow_0ilcc5g_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"327\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1636vpj\" id=\"EndEvent_1636vpj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"769\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"787\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ewcngu\" id=\"SequenceFlow_1ewcngu_di\"\u003e\u003comgdi:waypoint x=\"556\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"769\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"662.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "0228e00e-2c47-43e6-a736-550f104c94ea",
      "description": "An example workflow ran at an attachment level that sends the artifact data to Google Cloud\u0027s DLP Service and aims to de-identify the types of  personal information specified. By default 14 types are selected out of 50+ types. The return result is a new note with the PII removed.",
      "export_key": "gcp_dlp_deidentify_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1655926234506,
      "name": "Example: Google Cloud DLP - De-Identify Artifact",
      "object_type": "artifact",
      "programmatic_name": "gcp_dlp_deidentify_artifact",
      "tags": [
        {
          "tag_handle": "fn_google_cloud_dlp",
          "value": null
        }
      ],
      "uuid": "735701cc-a569-4589-afdb-7d6f6a97e0bc",
      "workflow_id": 30
    }
  ],
  "workspaces": []
}
