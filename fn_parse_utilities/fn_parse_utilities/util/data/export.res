{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "RFC 822 Email Message File",
            "Email Attachment",
            "Other File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Parse Utilities Email Parsing (Artifact)",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities Email Parsing (Artifact)",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e224640f-3124-42f8-82cf-0caa9ec6d6dd",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_email_parsing_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Parse Utilities Email Parsing (Attachment)",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities Email Parsing (Attachment)",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9ae0ece9-481d-4d8b-babc-b71f8aa0bf9a",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_email_parsing_attachment"
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
          "value": "X509 Certificate File"
        }
      ],
      "enabled": true,
      "export_key": "Example: Parse Utilities Parse SSL Certificate",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities Parse SSL Certificate",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7e5d6ded-9ca8-4dc8-816b-ea9f175b2112",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_parse_ssl_certificate"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.attachment",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Parse Utilities PDFID (Artifact)",
      "id": 17,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities PDFID (Artifact)",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "007f4aff-3ba6-4a8e-865c-c408ff561132",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_pdfid"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Parse Utilities PDFID (Attachment)",
      "id": 18,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities PDFID (Attachment)",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "88be7682-2ba0-45b1-8b7c-335ad718f3aa",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_pdfid_attachment"
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
            "Log File",
            "Other File"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Parse Utilities XML Transformation",
      "id": 19,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities XML Transformation",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "cc5d1e56-27e7-4430-9b14-b53762463289",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_xml_transformation"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Parse Utilities XML Transformation (Attachment)",
      "id": 20,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Parse Utilities XML Transformation (Attachment)",
      "object_type": "attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "98c30341-c3f4-4d16-8ad7-284a586aee5f",
      "view_items": [],
      "workflows": [
        "example_parse_utilities_xml_attachment"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1667854579474,
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
      "export_key": "__function/parse_utilities_xml_source",
      "hide_notification": false,
      "id": 273,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_xml_source",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_xml_source",
      "tooltip": "xml document to transform or empty when using attachments",
      "type_id": 11,
      "uuid": "c7a516a1-8d59-4ed1-870d-6e71dd632ea2",
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
      "export_key": "__function/parse_utilities_filename",
      "hide_notification": false,
      "id": 274,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_filename",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_filename",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ee6c2353-c93c-4fc4-a555-db5a115ec0a7",
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
      "export_key": "__function/parse_utilities_task_id",
      "hide_notification": false,
      "id": 275,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f021ba2d-49d9-4a87-9f5b-84d743618a6d",
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
      "export_key": "__function/parse_utilities_certificate",
      "hide_notification": false,
      "id": 276,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_certificate",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_certificate",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f81ec445-590c-4ef4-8d8b-821a57e01207",
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
      "export_key": "__function/parse_utilities_incident_id",
      "hide_notification": false,
      "id": 277,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "02cba5bf-7a97-4eff-9c39-8935eebd8835",
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
      "export_key": "__function/parse_utilities_attachment_id",
      "hide_notification": false,
      "id": 278,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "095c2f0a-7eb3-4822-ab88-2fb614ecca44",
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
      "export_key": "__function/parse_utilities_artifact_id",
      "hide_notification": false,
      "id": 279,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
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
      "export_key": "__function/parse_utilities_xml_stylesheet",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_xml_stylesheet",
      "operation_perms": {},
      "operations": [],
      "placeholder": "transform.xslt",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_xml_stylesheet",
      "tooltip": "name of stylesheet to use for the transformation",
      "type_id": 11,
      "uuid": "32241685-5dc0-48a2-8b07-c72776cd2730",
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
      "export_key": "__function/parse_utilities_base64content",
      "hide_notification": false,
      "id": 281,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_base64content",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_base64content",
      "tooltip": "",
      "type_id": 11,
      "uuid": "559e9e98-7ee6-447b-a723-e4446293e192",
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
      "export_key": "__function/parse_utilities_email_attachments",
      "hide_notification": false,
      "id": 282,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "parse_utilities_email_attachments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "parse_utilities_email_attachments",
      "tooltip": "If set to True, attachments found in the email file will be attached as Artifacts",
      "type_id": 11,
      "uuid": "71585139-062b-4c5f-a0f9-bbc41b62b2da",
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
      "created_date": 1667328221257,
      "description": {
        "content": "Extracts message headers and body parts from an email message (.eml or .msg).\n\nAny attachments found are added to the incident as artifacts if `parse_utilities_parse_email_attachments` is set to True.",
        "format": "text"
      },
      "destination_handle": "fn_parse_utilities",
      "display_name": "Parse Utilities: Email Parse",
      "export_key": "parse_utilities_email_parse",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667328221299,
      "name": "parse_utilities_email_parse",
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"received\": [{\"from\": \"www-data@localhost\", \"by\": \"example.fyre.ibm.com 8.15.2/8.15.2/Submit\", \"id\": \"29AJsIaP1141965\", \"date\": \"Mon, 10 Oct 2022 12:54:18 -0700\", \"hop\": 1, \"date_utc\": \"2022-10-10T19:54:18\", \"delay\": 0}, {\"from\": \"example.fyre.ibm.com localhost 127.0.0.1\", \"by\": \"example.fyre.ibm.com 8.15.2/8.15.2/Debian-10\", \"with\": \"ESMTP\", \"id\": \"29AJsIxo1141966\", \"for\": \"\u003cexample@ibm.com\u003e\", \"date\": \"Mon, 10 Oct 2022 12:54:18 -0700\", \"hop\": 2, \"date_utc\": \"2022-10-10T19:54:18\", \"delay\": 0.0}, {\"from\": \"example.fyre.ibm.com unknown 9.30.166.9\", \"by\": \"b01ledav005.gho.pok.ibm.com Postfix\", \"with\": \"ESMTPS\", \"for\": \"\u003cexample@ibm.com\u003e\", \"date\": \"Mon, 10 Oct 2022 19:54:18 +0000 GMT\", \"hop\": 3, \"date_utc\": \"2022-10-10T19:54:18\", \"delay\": 0.0}, {\"from\": \"b01ledav005.gho.pok.ibm.com unknown 127.0.0.1\", \"by\": \"IMSVA Postfix\", \"with\": \"ESMTP\", \"id\": \"F0260AE060\", \"for\": \"\u003cexample@ibm.com\u003e\", \"date\": \"Mon, 10 Oct 2022 19:54:18 +0000 GMT\", \"hop\": 4, \"date_utc\": \"2022-10-10T19:54:18\", \"delay\": 0.0}, {\"from\": \"b01ledav005.gho.pok.ibm.com unknown 127.0.0.1\", \"by\": \"IMSVA Postfix\", \"with\": \"ESMTP\", \"id\": \"3203BAE066\", \"for\": \"\u003cexample@ibm.com\u003e\", \"date\": \"Mon, 10 Oct 2022 19:54:19 +0000 GMT\", \"hop\": 5, \"date_utc\": \"2022-10-10T19:54:19\", \"delay\": 1.0}, {\"from\": \"b01ledav005.gho.pok.ibm.com b01ledav005.gho.pok.ibm.com 9.57.199.110\", \"by\": \"b01cxnp23034.gho.pok.ibm.com 8.14.9/8.14.9/NCO v10.0\", \"with\": \"ESMTP\", \"id\": \"29AJsJhU4784872\\r version=TLSv1/SSLv3 cipher=DHE-RSA-AES256-GCM-SHA384 bits=256 verify=OK\", \"for\": \"\u003cexample@ibm.com\u003e\", \"date\": \"Mon, 10 Oct 2022 19:54:19 GMT\", \"hop\": 6, \"date_utc\": \"2022-10-10T19:54:19\", \"delay\": 0.0}, {\"from\": \"b01cxnp23034.gho.pok.ibm.com 9.57.198.29\", \"by\": \"m01ex002.gmx.ibm.com 10.148.53.59\", \"with\": \"Microsoft SMTP Server\\r version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\", \"id\": \"15.1.2507.12\", \"via\": \"Frontend Transport\", \"date\": \"Mon, 10 Oct 2022 15:54:19 -0400\", \"hop\": 7, \"date_utc\": \"2022-10-10T19:54:19\", \"delay\": 0.0}, {\"from\": \"m01ex002.gmx.ibm.com 10.148.53.59\", \"by\": \"m01ex004.gmx.ibm.com\\r 10.148.53.60\", \"with\": \"Microsoft SMTP Server version=TLS1_2,\\r cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\", \"id\": \"15.1.2507.12\", \"date\": \"Mon, 10 Oct\\r 2022 15:54:19 -0400\", \"hop\": 8, \"date_utc\": \"2022-10-10T19:54:19\", \"delay\": 0.0}, {\"from\": \"gmx.mail.ibm.com 169.55.84.251\", \"by\": \"MW2NAM12FT057.mail.protection.outlook.com 10.13.181.5\", \"with\": \"Microsoft SMTP\\r Server version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\", \"id\": \"15.20.5723.11\", \"via\": \"Frontend Transport\", \"date\": \"Mon, 10 Oct 2022 19:54:24 +0000\", \"hop\": 9, \"date_utc\": \"2022-10-10T19:54:24\", \"delay\": 5.0}, {\"from\": \"MW2NAM12FT057.eop-nam12.prod.protection.outlook.com\\r 2603:10b6:303:8c:cafe::42\", \"by\": \"MW4PR03CA0145.outlook.office365.com\\r 2603:10b6:303:8c::30\", \"with\": \"Microsoft SMTP Server version=TLS1_2,\\r cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384\", \"id\": \"15.20.5709.19\", \"via\": \"Frontend\\r Transport\", \"date\": \"Mon, 10 Oct 2022 19:54:24 +0000\", \"hop\": 10, \"date_utc\": \"2022-10-10T19:54:24\", \"delay\": 0.0}, {\"from\": \"MW4PR03CA0145.namprd03.prod.outlook.com 2603:10b6:303:8c::30\", \"by\": \"MN2PR15MB2877.namprd15.prod.outlook.com 2603:10b6:208:ee::17\", \"with\": \"Microsoft SMTP Server version=TLS1_2,\\r cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384\", \"id\": \"15.20.5709.15\", \"date\": \"Mon, 10 Oct\\r 2022 19:54:24 +0000\", \"hop\": 11, \"date_utc\": \"2022-10-10T19:54:24\", \"delay\": 0.0}, {\"from\": \"MN2PR15MB2877.namprd15.prod.outlook.com 2603:10b6:208:ee::17\", \"by\": \"BYAPR15MB2296.namprd15.prod.outlook.com\", \"with\": \"HTTPS\", \"date\": \"Mon, 10 Oct 2022\\r 19:54:38 +0000\", \"hop\": 12, \"date_utc\": \"2022-10-10T19:54:38\", \"delay\": 14.0}], \"x-originatororg\": \"mail.ibm.com\", \"x-ms-exchange-organization-expirationstarttimereason\": \"OriginalSubmit\", \"x-crosspremisesheadersfiltered\": \"MW2NAM12FT057.eop-nam12.prod.protection.outlook.com\", \"x-ms-exchange-organization-scl\": \"-1\", \"body\": \"\u003cmeta http-equiv=\\\"Content-Type\\\" content=\\\"text/html; charset=utf-8\\\"\u003e\u003ctable cellpadding=\\\"4\\\"\u003e\u003ctr\u003e\u003ctd align=\\\"left\\\" colspan=\\\"4\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003eCongratulations, you\u0027re all ready to go!!\\r\\n\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd align=\\\"left\\\" colspan=\\\"4\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003eYour cluster \u003cb\u003elead\u003c/b\u003e has been built with the following\\r\\nconfiguration :\u003c/b\u003e\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr bgcolor=\\\"orange\\\"\u003e\u003cth\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003eEmbers\u003c/th\u003e\u003cth\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003ePublic\\r\\nIP\u003c/th\u003e\u003cth\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003ePrivate IP \u003c/th\u003e\u003cth\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003eAdditional Disks\u003c/th\u003e\u003ctr\u003e\u003ctr\u003e\u003ctd align=\\\"left\\\" bgcolor=\\\"#f0f0f0\\\"\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\u003cb\u003elead1\u003c/b\u003e.fyre.ibm.com \u003c/td\u003e\u003ctd bgcolor=\\\"#f0f0f0\\\"\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e9.30.211.110\u003c/td\u003e\u003ctd bgcolor=\\\"#f0f0f0\\\"\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e10.11.38.164\u003c/td\u003e\u003ctd bgcolor=\\\"#f0f0f0\\\"\u003e\u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e--\u003c/td\u003e\u003ctr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\u003cbr\u003e\u003cbr\u003e\u003cb\u003eLogin Credentials:\u003c/b\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e You can now log\\r\\ninto the node(s) of your cluster with the following credentials:\\r\\n\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e Username: root\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e Password: Your personal root password that you\\r\\nset on the Fyre webpage. \u003cbr\u003e\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\u003cbr\u003e\u003cb\u003eSecurity schedule\u003cb\u003e:\\r\\n\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\\r\\nYour cluster will be kept compliant automatically and will be patched\\r\\nand rebooted on the 1st weekend of each month.  You can change this\\r\\nschedule or disable it on a per-cluster basis from the Fyre\\r\\nGUI.\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\u003cbr\u003e\u003cb\u003eTerms of Use\u003cb\u003e: \u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003eBy using Fyre and/or Fyre resources\\r\\n(vms, clusters, etc), you agree to always abide by the Fyre Terms of\\r\\nUse.  \u003cbr\u003e\\r\\n\\tThese terms can be found here: \u003ca href=\\\"https://fyre.ibm.com/help#fyre-termsofuse\\\"\u003ehttps://fyre.ibm.com/help#fyre-termsofuse\u003c/a\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e\\r\\n\u003cbr\u003e\u003cbr\u003eThanks!\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\"4\\\" align=\\\"left\\\"\u003e \u003cfont face=\\\"verdana\\\" size=\\\"2\\\"\u003e ~ The Fyre Team\u003c/td\u003e\u003c/tr\u003e\u003c/table\u003e\\r\\n\", \"x-ms-exchange-organization-network-message-id\": \"467954c2-54fc-491f-6f45-08daaaf93b34\", \"x-ms-exchange-crosstenant-fromentityheader\": \"HybridOnPrem\", \"date\": \"2022-10-10T19:54:18\", \"subject\": \"Fyre stack : \u0027lead\u0027 ready\", \"x-eopattributedmessage\": \"0\", \"x-ms-exchange-processed-by-bccfoldering\": \"15.20.5709.018\", \"authentication-results\": \"spf=none (sender IP is 169.55.84.251)\\r\\n smtp.mailfrom=example.fyre.ibm.com; dkim=none (message not signed)\\r\\n header.d=none;dmarc=fail action=none header.from=us.ibm.com;\", \"x-ms-exchange-organization-authas\": \"Anonymous\", \"content-type\": \"text/html; charset=\\\"UTF-8\\\"\", \"x-ms-exchange-crosstenant-network-message-id\": \"467954c2-54fc-491f-6f45-08daaaf93b34\", \"x-ms-exchange-organization-authsource\": \"m01ex002.gmx.ibm.com\", \"x-ms-exchange-crosstenant-authsource\": \"m01ex002.gmx.ibm.com\", \"x-tm-as-gconf\": \"00\", \"message-id\": \"\u003c202210101954.29AJsIaP1141965@example.fyre.ibm.com\u003e\", \"received-spf\": \"None (protection.outlook.com: example.fyre.ibm.com does not\\r\\n designate permitted sender hosts)\", \"timezone\": \"-7.0\", \"x-ms-exchange-organization-messagedirectionality\": \"Originating\", \"x-ms-exchange-crosstenant-id\": \"fcf67057-50c9-4ad4-98f3-ffca64add9e9\", \"x-organizationheaderspreserved\": \"m01ex004.gmx.ibm.com\", \"x-ms-exchange-crosstenant-originalarrivaltime\": \"10 Oct 2022 19:54:24.1967\\r\\n (UTC)\", \"to\": [[\"\", \"example@ibm.com\"]], \"x-ms-exchange-organization-expirationstarttime\": \"10 Oct 2022 19:54:24.3217\\r\\n (UTC)\", \"x-ms-traffictypediagnostic\": \"MW2NAM12FT057:EE_|MN2PR15MB2877:EE_\", \"x-ms-exchange-transport-endtoendlatency\": \"00:00:14.1482542\", \"x-ms-exchange-organization-expirationinterval\": \"1:00:00:00.0000000\", \"x-ms-exchange-crosstenant-originalattributedtenantconnectingip\": \"TenantId=fcf67057-50c9-4ad4-98f3-ffca64add9e9;Ip=[169.55.84.251];Helo=[gmx.mail.ibm.com]\", \"x-ms-exchange-transport-crosstenantheadersstamped\": \"MN2PR15MB2877\", \"x-ms-office365-filtering-correlation-id\": \"467954c2-54fc-491f-6f45-08daaaf93b34\", \"x-forefront-antispam-report\": \"CIP:169.55.84.251;CTRY:US;LANG:en;SCL:-1;SRV:;IPV:NLI;SFV:NSPM;H:gmx.mail.ibm.com;PTR:fb.54.37a9.ip4.static.sl-reverse.com;CAT:NONE;SFS:;DIR:INB;\", \"x-ms-exchange-organization-expirationintervalreason\": \"OriginalSubmit\", \"x-ms-publictraffictype\": \"Email\", \"to_domains\": [\"ibm.com\"], \"x-crosspremisesheaderspromoted\": \"MW2NAM12FT057.eop-nam12.prod.protection.outlook.com\", \"x-microsoft-antispam-mailbox-delivery\": \"ucf:0;jmr:0;auth:0;dest:I;ENG:(910001)(944506478)(944626604)(920097)(930097);\", \"x-ms-exchange-crosstenant-authas\": \"Anonymous\", \"x-microsoft-antispam-message-info\": \"FxHn9SLBjgFF4dnkfttJCPKsph9Xn/sEQCFV3yiLJGtgKZtqncl8KfT/dUhKZ0/gsMGuWHSea0qfzrAZ8+JHELx2xhOikG7lgDFxpsHiT9xi6/rannm53Ur5JqbUAGkXzJGXDA/BAUb1pjGogswkrl3NyGAq3+QSJ0XGJfOok63/Pa3ua6sCwzRjdEtzV0wK4YiTcMCMdhedpFPWf01iBcQPezd6aEHOg5EdMEnSFPFjSVfixP3nIqOsMSQLPS72ubUMz8JDhXycm1XennS6cGMb/WwByYS9YhfpFIiJqE3jFFLRnmzucI6msgFHRgQAS7nx2KYUZnnjJZbN1kS6bICVaRh4h2BrRhjb3G4b+HkkoW2Cqrhn4p+VnYIFH/hBPWuuophaKvQt/lJ0gIfR/svy0WBVtx1iRHY+lGgW8temE8vG4CS0oTgbztcMlMTmU5MNMszcSGHgeZZODkyeQPzi84QmpJdmiowkQqYynyv6yoYugLy3iIQfzv3XI0GChyctAVEzL34SAxwn+FCojNM/VYTp9XiZN3GSuqgvgwDpQNJpK6fxxdXhRsF6UG4eJpiQjHpCTYAg1y5njTGekjCqVsLkMeI5XYFdwOXKtceUos0vVCnUNVZxnEVxS2vJQWPZHziRd2tv8n/sMxdnIfXkQIDUSnby6M+X86IIYJYtf6vGPbTFaaYy8d8TVeHeEQNbnkyLuCmpKNek9xHHXBkz/5SSJ2JYb7/P6hzcVAXiIL2zlfLeUygHwl5yIupHY5QgqGOapnypnY4AfJWbIjpUL/EiB3aO0Mu+spvWoGZp3alMeYkvTTMmZcJrPOUJjY8Mgo4nhmJ+SWOo7VbAyoHwuJQrnfokBs3YCfHAHtub8WPcWDmimJ8mXViuT65QrPDc56ygK2NaCX6e++zOI/XKPTTbql4f1lsVoD8BFhmCfXZow1YDjsIwpn9ON5nWW86F7QveWQABZj0dGZb6OR/240k2FreC4u2H0l1X+Sa4H/bPVMwmJF6OEyKXVRWez4qdwfPw92kKLm3wD1kAOx/XTo0nJnrtrnOS+T+6BtLy+3m3u1Hehem6mDete3v3UJAWaZB0ofTJKzlrteo9/UCG3pwwYfLD9NHP0QsPUuD4qQmSee8TZO5XTZ3wkGEglIVs0lA9guRiVYMnX9kEFWrOcIAZYHpUMJDmY9YEc9tzJ9cRPVv/4WR1Gmf96p2s1tc5WkvYUXXotr+uyKp1d82lseuiW0fnVM2cfHD39URVCYJ7Jqmf2pnXRGuldbaWd/RFmyYBDHzeOX0jiZ+1cQLcn5kmOfowBxmDgBNKv4MPPvanY0jEkCqxM6YerTsJGs2fMN8JlUH5ToKMdk87JX8BEHYBuCHiGZWG/Zk6hdTL6QrfVL7gYwXOuhB+mBZYORylMH5SlNbNUzco0P2UwSHndiHBS/alLU9pzKPpCWaotNrvy3u9o0F0bBSHLqFoqjzhcwuY559ScjzUaAC7ASAS9G9Puy7d9PIl1UNH5Po8rvxmlkXlSv+YVHynHOsHo+2w/rkJP21IDz1Y6OT6SDoCBBU6vnuIkcmdKo+c4QyuOmmKnjf1gK3lRUOssWPEglg/2guLzVunyzpiafNeWoQZ6nGGE7pDHT24FzXjvi3X7zJLQiS+dkIjOYPEWABN140mLxbIODzhJ9MpsLMH1mh9ZQq3z3KELEtpXvlltJnf9lgcnZKDxv7R5L7ApHHvcRz3hyoJXc7PoQ1eBdwRi0bCA9aY+Q3m74Rmq+VEGRj7QpJS+fm7ALEdSqJw1f+HHKxtnMzdGSMMkXdOgSM4lW+y7wndHdXrqGXS+52z0Fhd4bzMLDKSSa/6HjdZtEjDQy2J8wLhrXK8e5sPaJgPPOpf+VIW1Xg/Qj968zigOEWb87TDN0NUM+WBF/t4QnebfQCnFCRiA8ZajnnlDa8dZA==\", \"return-path\": \"www-data@example.fyre.ibm.com\", \"x-microsoft-antispam\": \"BCL:0;\", \"mime-version\": \"1.0\", \"from\": [[\"Fyre Admin\", \"fyre@us.ibm.com\"]], \"has_defects\": false, \"plain_body\": \"\", \"html_body\": \"[\\\"\u003cmeta http-equiv=\\\\\\\"Content-Type\\\\\\\" content=\\\\\\\"text/html; charset=utf-8\\\\\\\"\u003e\u003ctable cellpadding=\\\\\\\"4\\\\\\\"\u003e\u003ctr\u003e\u003ctd align=\\\\\\\"left\\\\\\\" colspan=\\\\\\\"4\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003eCongratulations, you\u0027re all ready to go!!\\\\r\\\\n\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd align=\\\\\\\"left\\\\\\\" colspan=\\\\\\\"4\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003eYour cluster \u003cb\u003elead\u003c/b\u003e has been built with the following\\\\r\\\\nconfiguration :\u003c/b\u003e\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr bgcolor=\\\\\\\"orange\\\\\\\"\u003e\u003cth\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003eEmbers\u003c/th\u003e\u003cth\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003ePublic\\\\r\\\\nIP\u003c/th\u003e\u003cth\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003ePrivate IP \u003c/th\u003e\u003cth\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003eAdditional Disks\u003c/th\u003e\u003ctr\u003e\u003ctr\u003e\u003ctd align=\\\\\\\"left\\\\\\\" bgcolor=\\\\\\\"#f0f0f0\\\\\\\"\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\u003cb\u003elead1\u003c/b\u003e.fyre.ibm.com \u003c/td\u003e\u003ctd bgcolor=\\\\\\\"#f0f0f0\\\\\\\"\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e9.30.211.110\u003c/td\u003e\u003ctd bgcolor=\\\\\\\"#f0f0f0\\\\\\\"\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e10.11.38.164\u003c/td\u003e\u003ctd bgcolor=\\\\\\\"#f0f0f0\\\\\\\"\u003e\u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e--\u003c/td\u003e\u003ctr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\u003cbr\u003e\u003cbr\u003e\u003cb\u003eLogin Credentials:\u003c/b\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e You can now log\\\\r\\\\ninto the node(s) of your cluster with the following credentials:\\\\r\\\\n\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e Username: root\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e Password: Your personal root password that you\\\\r\\\\nset on the Fyre webpage. \u003cbr\u003e\u003cbr\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\u003cbr\u003e\u003cb\u003eSecurity schedule\u003cb\u003e:\\\\r\\\\n\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\\\\r\\\\nYour cluster will be kept compliant automatically and will be patched\\\\r\\\\nand rebooted on the 1st weekend of each month.  You can change this\\\\r\\\\nschedule or disable it on a per-cluster basis from the Fyre\\\\r\\\\nGUI.\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\u003cbr\u003e\u003cb\u003eTerms of Use\u003cb\u003e: \u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003eBy using Fyre and/or Fyre resources\\\\r\\\\n(vms, clusters, etc), you agree to always abide by the Fyre Terms of\\\\r\\\\nUse.  \u003cbr\u003e\\\\r\\\\n\\\\tThese terms can be found here: \u003ca href=\\\\\\\"https://fyre.ibm.com/help#fyre-termsofuse\\\\\\\"\u003ehttps://fyre.ibm.com/help#fyre-termsofuse\u003c/a\u003e\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e\\\\r\\\\n\u003cbr\u003e\u003cbr\u003eThanks!\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd colspan=\\\\\\\"4\\\\\\\" align=\\\\\\\"left\\\\\\\"\u003e \u003cfont face=\\\\\\\"verdana\\\\\\\" size=\\\\\\\"2\\\\\\\"\u003e ~ The Fyre Team\u003c/td\u003e\u003c/tr\u003e\u003c/table\u003e\\\\r\\\\n\\\"]\"}, \"raw\": \"{\\\"received\\\": [{\\\"from\\\": \\\"www-data@localhost\\\", \\\"by\\\": \\\"example.fyre.ibm.com 8.15.2/8.15.2/Submit\\\", \\\"FxHn9SLBjgFF4dnkfttJCPKsph9Xn/sEQCFV3yiLJGtgKZtqncl8KfT/dUhKZ0/gsMGuWHSea0qfzrAZ8+JHELx2xhOikG7lgDFxpsHiT9xi6/rannm53Ur5JqbUAGkXzJGXDA/BAUb1pjGogswkrl3NyGAq3+QSJ0XGJfOok63/Pa3ua6sCwzRjdEtzV0wK4YiTcMCMdhedpFPWf01iBcQPezd6aEHOg5EdMEnSFPFjSVfixP3nIqOsMSQLPS72ubUMz8JDhXycm1XennS6cGMb/WwByYS9YhfpFIiJqE3jFFLRnmzucI6msgFHRgQAS7nx2KYUZnnjJZbN1kS6bICVaRh4h2BrRhjb3G4b+HkkoW2Cqrhn4p+VnYIFH/hBPWuuophaKvQt/lJ0gIfR/svy0WBVtx1iRHY+lGgW8temE8vG4CS0oTgbztcMlMTmU5MNMszcSGHgeZZODkyeQPzi84QmpJdmiowkQqYynyv6yoYugLy3iIQfzv3XI0GChyctAVEzL34SAxwn+FCojNM/VYTp9XiZN3GSuqgvgwDpQNJpK6fxxdXhRsF6UG4eJpiQjHpCTYAg1y5njTGekjCqVsLkMeI5XYFdwOXKtceUos0vVCnUNVZxnEVxS2vJQWPZHziRd2tv8n/sMxdnIfXkQIDUSnby6M+X86IIYJYtf6vGPbTFaaYy8d8TVeHeEQNbnkyLuCmpKNek9xHHXBkz/5SSJ2JYb7/P6hzcVAXiIL2zlfLeUygHwl5yIupHY5QgqGOapnypnY4AfJWbIjpUL/EiB3aO0Mu+spvWoGZp3alMeYkvTTMmZcJrPOUJjY8Mgo4nhmJ+SWOo7VbAyoHwuJQrnfokBs3YCfHAHtub8WPcWDmimJ8mXViuT65QrPDc56ygK2NaCX6e++zOI/XKPTTbql4f1lsVoD8BFhmCfXZow1YDjsIwpn9ON5nWW86F7QveWQABZj0dGZb6OR/240k2FreC4u2H0l1X+Sa4H/bPVMwmJF6OEyKXVRWez4qdwfPw92kKLm3wD1kAOx/XTo0nJnrtrnOS+T+6BtLy+3m3u1Hehem6mDete3v3UJAWaZB0ofTJKzlrteo9/UCG3pwwYfLD9NHP0QsPUuD4qQmSee8TZO5XTZ3wkGEglIVs0lA9guRiVYMnX9kEFWrOcIAZYHpUMJDmY9YEc9tzJ9cRPVv/4WR1Gmf96p2s1tc5WkvYUXXotr+uyKp1d82lseuiW0fnVM2cfHD39URVCYJ7Jqmf2pnXRGuldbaWd/RFmyYBDHzeOX0jiZ+1cQLcn5kmOfowBxmDgBNKv4MPPvanY0jEkCqxM6YerTsJGs2fMN8JlUH5ToKMdk87JX8BEHYBuCHiGZWG/Zk6hdTL6QrfVL7gYwXOuhB+mBZYORylMH5SlNbNUzco0P2UwSHndiHBS/alLU9pzKPpCWaotNrvy3u9o0F0bBSHLqFoqjzhcwuY559ScjzUaAC7ASAS9G9Puy7d9PIl1UNH5Po8rvxmlkXlSv+YVHynHOsHo+2w/rkJP21IDz1Y6OT6SDoCBBU6vnuIkcmdKo+c4QyuOmmKnjf1gK3lRUOssWPEglg/2guLzVunyzpiafNeWoQZ6nGGE7pDHT24FzXjvi3X7zJLQiS+dkIjOYPEWABN140mLxbIODzhJ9MpsLMH1mh9ZQq3z3KELEtpXvlltJnf9lgcnZKDxv7R5L7ApHHvcRz3hyoJXc7PoQ1eBdwRi0bCA9aY+Q3m74Rmq+VEGRj7QpJS+fm7ALEdSqJw1f+HHKxtnMzdGSMMkXdOgSM4lW+y7wndHdXrqGXS+52z0Fhd4bzMLDKSSa/6HjdZtEjDQy2J8wLhrXK8e5sPaJgPPOpf+VIW1Xg/Qj968zigOEWb87TDN0NUM+WBF/t4QnebfQCnFCRiA8ZajnnlDa8dZA==\\\", \\\"return-path\\\": \\\"www-data@example.fyre.ibm.com\\\"}\", \"inputs\": {\"incident_id\": 2125, \"parse_utilities_email_attachments\": true, \"attachment_id\": 88}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-utilities\", \"package_version\": \"2.1.1\", \"host\": \"My Host\", \"execution_time_ms\": 1347, \"timestamp\": \"2022-10-13 15:50:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"received\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"from\": {\"type\": \"string\"}, \"by\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"date\": {\"type\": \"string\"}, \"hop\": {\"type\": \"integer\"}, \"date_utc\": {\"type\": \"string\"}, \"delay\": {\"type\": \"number\"}, \"with\": {\"type\": \"string\"}, \"for\": {\"type\": \"string\"}, \"via\": {\"type\": \"string\"}}}}, \"x-originatororg\": {\"type\": \"string\"}, \"x-ms-exchange-organization-expirationstarttimereason\": {\"type\": \"string\"}, \"x-crosspremisesheadersfiltered\": {\"type\": \"string\"}, \"x-ms-exchange-organization-scl\": {\"type\": \"string\"}, \"body\": {\"type\": \"string\"}, \"x-ms-exchange-organization-network-message-id\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-fromentityheader\": {\"type\": \"string\"}, \"date\": {\"type\": \"string\"}, \"subject\": {\"type\": \"string\"}, \"x-eopattributedmessage\": {\"type\": \"string\"}, \"x-ms-exchange-processed-by-bccfoldering\": {\"type\": \"string\"}, \"authentication-results\": {\"type\": \"string\"}, \"x-ms-exchange-organization-authas\": {\"type\": \"string\"}, \"content-type\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-network-message-id\": {\"type\": \"string\"}, \"x-ms-exchange-organization-authsource\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-authsource\": {\"type\": \"string\"}, \"x-tm-as-gconf\": {\"type\": \"string\"}, \"message-id\": {\"type\": \"string\"}, \"received-spf\": {\"type\": \"string\"}, \"timezone\": {\"type\": \"string\"}, \"x-ms-exchange-organization-messagedirectionality\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-id\": {\"type\": \"string\"}, \"x-organizationheaderspreserved\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-originalarrivaltime\": {\"type\": \"string\"}, \"to\": {\"type\": \"array\", \"items\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"x-ms-exchange-organization-expirationstarttime\": {\"type\": \"string\"}, \"x-ms-traffictypediagnostic\": {\"type\": \"string\"}, \"x-ms-exchange-transport-endtoendlatency\": {\"type\": \"string\"}, \"x-ms-exchange-organization-expirationinterval\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-originalattributedtenantconnectingip\": {\"type\": \"string\"}, \"x-ms-exchange-transport-crosstenantheadersstamped\": {\"type\": \"string\"}, \"x-ms-office365-filtering-correlation-id\": {\"type\": \"string\"}, \"x-forefront-antispam-report\": {\"type\": \"string\"}, \"x-ms-exchange-organization-expirationintervalreason\": {\"type\": \"string\"}, \"x-ms-publictraffictype\": {\"type\": \"string\"}, \"to_domains\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"x-crosspremisesheaderspromoted\": {\"type\": \"string\"}, \"x-microsoft-antispam-mailbox-delivery\": {\"type\": \"string\"}, \"x-ms-exchange-crosstenant-authas\": {\"type\": \"string\"}, \"x-microsoft-antispam-message-info\": {\"type\": \"string\"}, \"return-path\": {\"type\": \"string\"}, \"x-microsoft-antispam\": {\"type\": \"string\"}, \"mime-version\": {\"type\": \"string\"}, \"from\": {\"type\": \"array\", \"items\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}, \"has_defects\": {\"type\": \"boolean\"}, \"plain_body\": {\"type\": \"string\"}, \"html_body\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"parse_utilities_email_attachments\": {\"type\": \"boolean\"}, \"attachment_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "b8d57d19-a21e-42d4-9dba-06154084ca7e",
      "version": 1,
      "view_items": [
        {
          "content": "559e9e98-7ee6-447b-a723-e4446293e192",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "71585139-062b-4c5f-a0f9-bbc41b62b2da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "095c2f0a-7eb3-4822-ab88-2fb614ecca44",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "02cba5bf-7a97-4eff-9c39-8935eebd8835",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f021ba2d-49d9-4a87-9f5b-84d743618a6d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "095c2f0a-7eb3-4822-ab88-2fb614ecca44",
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
          "name": "Example: Parse Utilities Email Parsing (Artifact)",
          "object_type": "artifact",
          "programmatic_name": "example_parse_utilities_email_parsing_artifact",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 5
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Parse Utilities Email Parsing (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_parse_utilities_email_parsing_attachment",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1667328221309,
      "description": {
        "content": "This function produces the structured data from a provided SSL certificate. Three inputs are accepted by the function. There are 2 defined ways to use this function for parsing certificates.",
        "format": "text"
      },
      "destination_handle": "fn_parse_utilities",
      "display_name": "Parse Utilities: Parse SSL Certificate",
      "export_key": "parse_utilities_parse_ssl_certificate",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667328221342,
      "name": "parse_utilities_parse_ssl_certificate",
      "output_json_example": "{\"subject\": \"\\\"[(b\u0027C\u0027, b\u0027US\u0027), (b\u0027ST\u0027, b\u0027California\u0027), (b\u0027L\u0027, b\u0027San Francisco\u0027), (b\u0027O\u0027, b\u0027Cloudflare, Inc.\u0027), (b\u0027CN\u0027, b\u0027sni.cloudflaressl.com\u0027)]\\\"\", \"notBefore\": \"2022-03-29 00:00:00\", \"notAfter\": \"2023-03-29 23:59:59\", \"issuer\": \"\\\"[(b\u0027C\u0027, b\u0027US\u0027), (b\u0027O\u0027, b\u0027Cloudflare, Inc.\u0027), (b\u0027CN\u0027, b\u0027Cloudflare Inc ECC CA-3\u0027)]\\\"\", \"version\": 2, \"expiration_status\": \"Valid\", \"signature_algorithm\": \"b\u0027ecdsa-with-SHA256\u0027\", \"public_key\": \"b\u0027-----BEGIN PUBLIC KEY-----\\\\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEXLHljT47vFyTH/0A6YqZhypEhVok\\\\n6OsRv++OwcB5tcAQmnTF58RgamcQ8rOEiEDhavOcbBeX/xsus397BgBGmQ==\\\\n-----END PUBLIC KEY-----\\\\n\u0027\", \"extensions\": {\"subjectAltNames\": \"[\\\"sni.cloudflaressl.com\\\", \\\"*.adamtheautomator.com\\\", \\\"adamtheautomator.com\\\"]\", \"basicConstraints\": \"false\", \"issuerAltNames\": \"[]\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"subject\": {\"type\": \"string\"}, \"notBefore\": {\"type\": \"string\"}, \"notAfter\": {\"type\": \"string\"}, \"issuer\": {\"type\": \"string\"}, \"version\": {\"type\": \"integer\"}, \"expiration_status\": {\"type\": \"string\"}, \"signature_algorithm\": {\"type\": \"string\"}, \"public_key\": {\"type\": \"string\"}, \"extensions\": {\"type\": \"object\", \"properties\": {\"subjectAltNames\": {\"type\": \"string\"}, \"basicConstraints\": {\"type\": \"string\"}, \"issuerAltNames\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "0e09a520-544a-4f0f-8990-d2475b43ba04",
      "version": 1,
      "view_items": [
        {
          "content": "f81ec445-590c-4ef4-8d8b-821a57e01207",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "02cba5bf-7a97-4eff-9c39-8935eebd8835",
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
          "name": "Example: Parse Utilities Parse SSL Certificate",
          "object_type": "artifact",
          "programmatic_name": "example_parse_utilities_parse_ssl_certificate",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    },
    {
      "created_date": 1667328221350,
      "description": {
        "content": "Produces summary information about the structure of a PDF file, using Didier Stevens\u0027 PDFID (https://blog.didierstevens.com/programs/pdf-tools/).",
        "format": "text"
      },
      "destination_handle": "fn_parse_utilities",
      "display_name": "Parse Utilities: PDFID",
      "export_key": "parse_utilities_pdfid",
      "id": 3,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667328221381,
      "name": "parse_utilities_pdfid",
      "output_json_example": "{\"filename\": \"README.pdf\", \"header\": \"%PDF-1.4\", \"isPdf\": \"True\", \"obj\": 570, \"endobj\": 570, \"stream\": 398, \"endstream\": 398, \"xref\": 1, \"trailer\": 1, \"startxref\": 1, \"/Page\": 85, \"/Encrypt\": 0, \"/ObjStm\": 0, \"/JS\": 0, \"/JavaScript\": 0, \"/AA\": 0, \"/OpenAction\": 0, \"/AcroForm\": 0, \"/JBIG2Decode\": 0, \"/RichMedia\": 0, \"/Launch\": 0, \"/EmbeddedFile\": 0, \"/XFA\": 0, \"/Colors \u003e 2^24\": 0}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"filename\": {\"type\": \"string\"}, \"header\": {\"type\": \"string\"}, \"isPdf\": {\"type\": \"string\"}, \"obj\": {\"type\": \"integer\"}, \"endobj\": {\"type\": \"integer\"}, \"stream\": {\"type\": \"integer\"}, \"endstream\": {\"type\": \"integer\"}, \"xref\": {\"type\": \"integer\"}, \"trailer\": {\"type\": \"integer\"}, \"startxref\": {\"type\": \"integer\"}, \"/Page\": {\"type\": \"integer\"}, \"/Encrypt\": {\"type\": \"integer\"}, \"/ObjStm\": {\"type\": \"integer\"}, \"/JS\": {\"type\": \"integer\"}, \"/JavaScript\": {\"type\": \"integer\"}, \"/AA\": {\"type\": \"integer\"}, \"/OpenAction\": {\"type\": \"integer\"}, \"/AcroForm\": {\"type\": \"integer\"}, \"/JBIG2Decode\": {\"type\": \"integer\"}, \"/RichMedia\": {\"type\": \"integer\"}, \"/Launch\": {\"type\": \"integer\"}, \"/EmbeddedFile\": {\"type\": \"integer\"}, \"/XFA\": {\"type\": \"integer\"}, \"/Colors \u003e 2^24\": {\"type\": \"integer\"}}}",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "c4b919f7-f943-405e-86fd-640f79e3ee8e",
      "version": 1,
      "view_items": [
        {
          "content": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "02cba5bf-7a97-4eff-9c39-8935eebd8835",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "095c2f0a-7eb3-4822-ab88-2fb614ecca44",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f021ba2d-49d9-4a87-9f5b-84d743618a6d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ee6c2353-c93c-4fc4-a555-db5a115ec0a7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "559e9e98-7ee6-447b-a723-e4446293e192",
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
          "name": "Example: Parse Utilities PDFID (Artifact)",
          "object_type": "artifact",
          "programmatic_name": "example_parse_utilities_pdfid",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 2
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Parse Utilities PDFID (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_parse_utilities_pdfid_attachment",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1667328221389,
      "description": {
        "content": "Transforms an XML document using a preexisting `xsl` stylesheet. The resulting content is returned.",
        "format": "text"
      },
      "destination_handle": "fn_parse_utilities",
      "display_name": "Parse Utilities: XML Transformation",
      "export_key": "parse_utilities_xml_transformation",
      "id": 4,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1667328221419,
      "name": "parse_utilities_xml_transformation",
      "output_json_example": "{\"content\": \"\u003chtml\u003e\u003cbody\u003e\u003ch2\u003eMy CD Collection\u003c/h2\u003e\u003ctable border=\\\"1\\\"\u003e\u003ctr bgcolor=\\\"#9acd32\\\"\u003e\u003cth style=\\\"text-align:left\\\"\u003eTitle\u003c/th\u003e\u003cth style=\\\"text-align:left\\\"\u003eArtist\u003c/th\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd\u003eEmpire Burlesque\u003c/td\u003e\u003ctd\u003eBob Dylan\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd\u003eHide your heart\u003c/td\u003e\u003ctd\u003eBonnie Tyler\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd\u003eGreatest Hits\u003c/td\u003e\u003ctd\u003eDolly Parton\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003ctd\u003eStill got the blues\u003c/td\u003e\u003ctd\u003eGary Moore\u003c/td\u003e\u003c/tr\u003e\u003c/table\u003e\u003c/body\u003e\u003c/html\u003e\"}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"content\": {\"type\": \"string\"}}}",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "fb731c0f-f0ee-4a66-8cc5-ab98495a92ca",
      "version": 1,
      "view_items": [
        {
          "content": "2e64afbd-cea3-4e6c-b936-89d80e9083da",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "32241685-5dc0-48a2-8b07-c72776cd2730",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "095c2f0a-7eb3-4822-ab88-2fb614ecca44",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "02cba5bf-7a97-4eff-9c39-8935eebd8835",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f021ba2d-49d9-4a87-9f5b-84d743618a6d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c7a516a1-8d59-4ed1-870d-6e71dd632ea2",
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
          "name": "Example Parse Utilities XML (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "example_parse_utilities_xml_attachment",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Parse Utilities XML Transformation",
          "object_type": "artifact",
          "programmatic_name": "example_parse_utilities_xml_transformation",
          "tags": [
            {
              "tag_handle": "fn_parse_utilities",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 1,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1667854577764,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1667854577764,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3242c47c-8fff-457d-962a-330324af0060",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_parse_utilities",
      "name": "fn_parse_utilities",
      "programmatic_name": "fn_parse_utilities",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "users": [],
      "uuid": "218ce2bf-074b-4320-adc9-67da29b465a2"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1667328220760,
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion.\nTypically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys (sorted if specified) as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.0",
      "id": 2,
      "language": "python",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328220783,
      "name": "Convert JSON to rich text v1.0",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text_v10",
      "script_text": "# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.\nVERSION = 1.0\n\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to define the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, { \n    \"version\": 1.0,\n    \"header\": \"Artifact scan results for\".format(artifact.value),\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr /\u003e\",\n    \"sort\": True,\n    \"json\": results.content,\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.0, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr /\u003e\"|list such as [\u0027\u003cspan\u003e\u0027,\u0027\u003c/span\u003e\u0027], [html separator between json keys and lists or defaults to html break: \u0027\u003cbr /\u003e\u0027. \n                                                If a list, then the data is brackets by the pair specified]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\"\"\"\n\nimport re\n\n# needed for python 3\ntry:\n    unicode(\"abc\")\nexcept:\n    unicode = str\n\n\nrc = re.compile(r\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#\\?]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n    \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n\n    def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr /\u003e\", sort_keys=False):\n        self.omit_keys = omit_keys\n        self.padding = padding\n        self.separator = separator\n        self.sort_keys = sort_keys\n\n\n    def format_link(self, item):\n        \"\"\"[summary]\n          Find embedded urls (http(s)) and add html anchor tags to display as links\n          Args:\n              item ([string])\n\n          Returns:\n              [str]: None|original text if no links|text with html links\n        \"\"\"\n        formatted_item = item\n        if item and not isinstance(item, (int, bool, float)):\n            list = rc.findall(item)\n            if list:\n                for link in list:\n                    formatted_item = formatted_item.replace(link, u\"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n        return formatted_item\n\n    def expand_list(self, list_value, is_list=False):\n        \"\"\"[summary]\n          convert items to html, adding indents to nested dictionaries.\n          Args:\n              list_value ([dict|list]): json element\n\n          Returns:\n              [str]: html converted code\n        \"\"\"\n        if not isinstance(list_value, list):\n            return self.format_link(list_value)\n        elif not list_value:\n            return u\"None\u003cbr\u003e\"\n\n        try:\n            items_list = []  # this will ensure list starts on second line of key label\n            for item in list_value:\n                if isinstance(item, dict):\n                    result = self.convert_json_to_rich_text(item)\n                    if is_list:\n                        items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(result))\n                    else:\n                        items_list.append(result)\n                elif isinstance(item, list):\n                    items_list.append(self.expand_list(item, is_list=True))\n                elif is_list:\n                    items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(self.format_link(unicode(item))))\n                else:\n                    items_list.append(self.format_link(unicode(item)))\n\n            expand_list_result = self.add_separator(self.separator if not is_list else u\"\",\n                                                    items_list,\n                                                    is_list=is_list)\n\n            if is_list:\n                return u\"\u003cul\u003e{}\u003c/ul\u003e\".format(expand_list_result)\n            else:\n                return u\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(expand_list_result)\n        except Exception as err:\n            return str(err)\n\n    def convert_json_to_rich_text(self, sub_dict):\n        \"\"\"[summary]\n          Walk dictionary tree and convert to html for better display\n          Args:\n              sub_dict ([type]): [description]\n\n          Returns:\n              [type]: [description]\n        \"\"\"\n        notes = []\n        if sub_dict:\n            keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n            for key in keys:\n                if key not in self.omit_keys:\n                    value = sub_dict[key]\n                    is_list = isinstance(value, list)\n                    item_list = [u\"\u003cstrong\u003e{0}\u003c/strong\u003e: \".format(key)]\n                    if isinstance(value, dict):\n                        convert_result = self.convert_json_to_rich_text(value)\n                        if convert_result:\n                            item_list.append(u\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, convert_result))\n                        else:\n                            item_list.append(u\"None\u003cbr\u003e\")\n                    else:\n                        item_list.append(self.expand_list(value, is_list=is_list))\n                    notes.append(self.add_separator(self.separator, u\"\".join(unicode(v) for v in item_list), is_list=is_list))\n\n        result_notes = u\"\".join(notes)\n        if isinstance(self.separator, list):\n            return result_notes\n        else:\n            return result_notes.replace(\n                u\"\u003c/div\u003e{0}\".format(self.separator), u\"\u003c/div\u003e\").replace(\n                u\"{0}\u003c/div\u003e\".format(self.separator), u\"\u003c/div\u003e\"\n            )  # tighten up result\n\n    def add_separator(self, separator, items, is_list=False):\n        \"\"\"\n        apply the separator to the data\n        :param separator: None, str or list such as [\u0027\u003cspan\u003e\u0027, \u0027\u003c/span\u003e\u0027]\n        :param items: str or list to add separator\n        :return: text with separator applied\n        \"\"\"\n        _items = items\n\n        if not _items:\n            return \"\u003cbr\u003e\"\n\n        if not isinstance(_items, list):\n            _items = [_items]\n\n        if isinstance(separator, list):\n            return u\"\".join([u\"{}{}{}\".format(separator[0], item, separator[1]) for item in _items])\n\n        return u\"{}{}\".format(separator.join(_items), separator if not is_list else u\"\")\n\ndef get_properties(property_name):\n    \"\"\"\n    Logic to collect the json and parameters from a workflow property.\n    Args:\n      property_name: workflow property to reference\n    Returns:\n      padding, separator, header, json_omit_list, incident_field, json, sort_keys\n    \"\"\"\n    if not workflow.properties.get(property_name):\n        helper.fail(\"workflow.properties.{} undefined\".format(property_name))\n    if not workflow.properties[property_name].get(\u0027json\u0027):\n        helper.fail(\"workflow.properties.{}.json undefined\".format(property_name))\n\n    padding = int(workflow.properties[property_name].get(\"padding\", 10))\n    separator = workflow.properties[property_name].get(\"separator\", u\"\u003cbr /\u003e\")\n    if isinstance(separator, list) and len(separator) != 2:\n        helper.fail(\"list of separators should be specified as a pair such as [\u0027\u003cdiv\u003e\u0027, \u0027\u003c/div\u003e\u0027]: {}\".format(separator))\n\n    header = workflow.properties[property_name].get(\"header\")\n    json_omit_list = workflow.properties[property_name].get(\"json_omit_list\")\n    if not json_omit_list:\n        json_omit_list = []\n    incident_field = workflow.properties[property_name].get(\"incident_field\")\n    json = workflow.properties[property_name].get(\"json\")\n    if not isinstance(json, dict):\n        helper.fail(\"json element is not formatted correctly: {}\".format(json))\n    sort_keys = bool(workflow.properties[property_name].get(\"sort\", False))\n\n    return padding, separator, header, json_omit_list, incident_field, json, sort_keys\n\n\n## S T A R T\nif \u0027workflow\u0027 in globals():\n    padding, separator, header, json_omit_list, incident_field, json, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\n\n    if header:\n        if isinstance(separator, list):\n            hdr = u\"{0}{1}{2}\".format(separator[0], header, separator[1])\n        else:\n            hdr = u\"{0}{1}\".format(header, separator)\n    else:\n        hdr = u\"\"\n\n    convert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\n    converted_json = convert.convert_json_to_rich_text(json)\n    result = u\"{}{}\".format(hdr, converted_json)\n\n    rich_text_note = helper.createRichText(result)\n    if incident_field:\n        incident[incident_field] = rich_text_note\n    else:\n        incident.addNote(rich_text_note)\n",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "f7276ff0-1770-4058-9e89-40ee79c6e41b"
    }
  ],
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
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_email_parsing_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_email_parsing_attachment\" isExecutable=\"true\" name=\"Example: Parse Utilities Email Parsing (Attachment)\"\u003e\u003cdocumentation\u003eExample Workflow showing to parse an Email File (.eml or .msg) from Incident/Task Attachments. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1647a4o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0ypytjn\"\u003e\u003cincoming\u003eSequenceFlow_19h66px\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1647a4o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kb4551\"/\u003e\u003cserviceTask id=\"ServiceTask_1kb4551\" name=\"Parse Utilities: Email Parse\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8d57d19-a21e-42d4-9dba-06154084ca7e\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\nif not results.success:\\n  note_text = u\\\"\\\"\\\"Workflow \u0027Example: Email Parsing (Attachment)\u0027 Failed\u0026lt;br\u0026gt;\\n                  \u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(str(results.reason))\\n  \\n  incident.addNote(helper.createRichText(note_text))\\n\\nelse:\\n  email = results.content\\n  \\n  # Get Email Subject\\n  eml_subject = email.get(\\\"subject\\\", \\\"BLANK SUBJECT LINE\\\")\\n\\n  #########################################\\n  # Add Artifacts for Email Recipient: to #\\n  #########################################\\n  for eml_addr in email.get(\\\"to\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  #########################################\\n  # Add Artifacts for Email Recipient: cc #\\n  #########################################\\n  for eml_addr in email.get(\\\"cc\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  ########################################\\n  # Add Artifacts for Email Sender: from #\\n  ########################################\\n  for eml_addr in email.get(\\\"from\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Sender\\\", eml_addr[1], eml_addr[0])\\n\\n  ################################################\\n  # Add Artifacts for IPs found in Email Headers #\\n  ################################################\\n  for eml_header in email.get(\\\"received\\\", []):\\n    \\n    the_header = eml_header.get(\\\"from\\\", None)\\n    \\n    if the_header:\\n      ips = re.findall(\u0027(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\u0027, the_header)\\n      unique_ips = set(ips)\\n  \\n      for an_ip in unique_ips:\\n        if an_ip:\\n          incident.addArtifact(\\\"IP Address\\\", an_ip, u\\\"Hop {0} at {1}\\\\n\\\\nHeader: {2}\\\".format(eml_header.get(\\\"hop\\\", \\\"\\\"), eml_header.get(\\\"date_utc\\\", \\\"\\\"), the_header))\\n\\n  ##############################################\\n  # Add Artifacts for URLs found in Email Body #\\n  ##############################################\\n  urls = []\\n  for eml_body_content in [email.get(\\\"plain_body\\\", \\\"\\\"), email.get(\\\"html_body\\\", \\\"\\\")]:\\n    urls.extend(re.findall(\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026amp;+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027, eml_body_content))\\n\\n  uniq_urls = set(urls)\\n\\n  for a_url in uniq_urls:\\n    # Remove any backslash as regex can add\\n    a_url = a_url.replace(\u0027\\\\\\\\\u0027,\\\"\\\")\\n    if a_url:\\n      incident.addArtifact(\\\"URL\\\", a_url, \\\"Found in parsed Email\\\")\\n  \\n  ################################################\\n  # Add the Email Body as a Note to the Incident #\\n  ################################################\\n  if email.get(\\\"body\\\"):\\n    note_text = u\\\"\\\"\\\"\u0026lt;b\u0026gt;Parsed Email::\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Subject:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;From:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;To:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{2}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Body:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{3}\\\"\\\"\\\".format(str(eml_subject),\\n                                  str(email.get(\\\"from\\\", \\\"N/A\\\")),\\n                                  str(email.get(\\\"to\\\", \\\"N/A\\\")), \\n                                  str(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n  \\n  \u0027\u0027\u0027Uncomment this if you would like to add a (safer) plain_text only Note\\n  if email.get(\\\"plain_body\\\"):\\n    note_text = u\\\"\\\"\\\"Parsed Email::\\\\n\\\\nSubject:\\\\n{0}\\\\n\\\\nFrom:\\\\n{1}\\\\n\\\\nTo:\\\\n{2}\\\\n\\\\nBody:\\\\n{3}\\\"\\\"\\\".format(str(eml_subject),\\n      str(email.get(\\\"from\\\", \\\"N/A\\\")), str(email.get(\\\"to\\\", \\\"N/A\\\")), str(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createPlainText(note_text))\\n  \u0027\u0027\u0027\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Define incident_id and attachment_id\\ninputs.parse_utilities_incident_id = incident.id\\ninputs.parse_utilities_attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.parse_utilities_task_id = task.id\\n\\n# Setting this to True will add any found attachments as an Email Attachment Artifact\\ninputs.parse_utilities_email_attachments = True\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1647a4o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19h66px\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_19h66px\" sourceRef=\"ServiceTask_1kb4551\" targetRef=\"EndEvent_0ypytjn\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qbegrw\"\u003e\u003ctext\u003eAdditional artifacts created based on the email message\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0y1gtam\" sourceRef=\"ServiceTask_1kb4551\" targetRef=\"TextAnnotation_0qbegrw\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ypytjn\" id=\"EndEvent_0ypytjn_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"580\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"598\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1647a4o\" id=\"SequenceFlow_1647a4o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"322\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"260\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kb4551\" id=\"ServiceTask_1kb4551_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"322\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19h66px\" id=\"SequenceFlow_19h66px_di\"\u003e\u003comgdi:waypoint x=\"422\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"580\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"501\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qbegrw\" id=\"TextAnnotation_0qbegrw_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"192\" x=\"423\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0y1gtam\" id=\"Association_0y1gtam_di\"\u003e\u003comgdi:waypoint x=\"420\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"497\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example Workflow showing to parse an Email File (.eml or .msg) from Incident/Task Attachments. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.",
      "export_key": "example_parse_utilities_email_parsing_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328222539,
      "name": "Example: Parse Utilities Email Parsing (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "example_parse_utilities_email_parsing_attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "b68c24f3-3310-4af5-b87c-49466da8a138",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_parse_ssl_certificate",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_parse_ssl_certificate\" isExecutable=\"true\" name=\"Example: Parse Utilities Parse SSL Certificate\"\u003e\u003cdocumentation\u003eAn example workflow that takes a PEM encoded SSL certificate as input and returns structured information about the certificate.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_107bu4j\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0jfyo39\"\u003e\u003cincoming\u003eSequenceFlow_08w2ck9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_107bu4j\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ngo3c8\"/\u003e\u003cserviceTask id=\"ServiceTask_0ngo3c8\" name=\"Parse Utilities: Parse SSL Certif...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0e09a520-544a-4f0f-8990-d2475b43ba04\"\u003e{\"inputs\":{},\"post_processing_script\":\"color = \\\"#45bc27\\\"\\n\\nif (results.expiration_status != \\\"Valid\\\"):\\n  color = \\\"#ff402b\\\"\\nnoteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Certificate Subject :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n              \u0026lt;b\u0026gt;Certificate Expiry After :\u0026lt;/b\u0026gt;{1}\u0026lt;/a\u0026gt;\\n              \u0026lt;b\u0026gt;Expiration Status:\u0026lt;/b\u0026gt; \u0026lt;b style=\\\"color: {2}\\\"\u0026gt;{3}\u0026lt;/b\u0026gt;\\n              \u0026lt;br\u0026gt;Issuer Details :\u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.subject, results.notAfter, color, results.expiration_status,results.issuer)\\n\\nincident.addNote(helper.createRichText(noteText))\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, { \\n    \\\"version\\\": 1.0,\\n    \\\"header\\\": None,\\n    \\\"padding\\\": 10,\\n    \\\"separator\\\": u\\\"\u0026lt;br\u0026gt;\\\",\\n    \\\"json\\\": results,\\n    \\\"json_omit_list\\\": [],\\n    \\\"incident_field\\\": None\\n  })\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.parse_utilities_certificate = artifact.value\\ninputs.parse_utilities_artifact_id = artifact.id\\ninputs.parse_utilities_incident_id = incident.id\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_107bu4j\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tyaklj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tyaklj\" sourceRef=\"ServiceTask_0ngo3c8\" targetRef=\"ScriptTask_0zh0h71\"/\u003e\u003cscriptTask id=\"ScriptTask_0zh0h71\" name=\"Convert JSON to rich text v1.0\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v10\" uuid=\"f7276ff0-1770-4058-9e89-40ee79c6e41b\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tyaklj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08w2ck9\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_08w2ck9\" sourceRef=\"ScriptTask_0zh0h71\" targetRef=\"EndEvent_0jfyo39\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0f3nwzq\"\u003e\u003ctext\u003eInputs: certificate OR artifact_id AND incident_id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_12v8n38\" sourceRef=\"ServiceTask_0ngo3c8\" targetRef=\"TextAnnotation_0f3nwzq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0q2dpdp\"\u003e\u003ctext\u003eOutputs: certificate data as a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0lgdmx3\" sourceRef=\"ServiceTask_0ngo3c8\" targetRef=\"TextAnnotation_0q2dpdp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0jfyo39\" id=\"EndEvent_0jfyo39_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"606\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"624\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_107bu4j\" id=\"SequenceFlow_107bu4j_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"269\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"233.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ngo3c8\" id=\"ServiceTask_0ngo3c8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"269\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tyaklj\" id=\"SequenceFlow_1tyaklj_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"433\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0zh0h71\" id=\"ScriptTask_0zh0h71_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"432.64411027568923\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08w2ck9\" id=\"SequenceFlow_08w2ck9_di\"\u003e\u003comgdi:waypoint x=\"533\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"606\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"569.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0f3nwzq\" id=\"TextAnnotation_0f3nwzq_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"159\" x=\"149\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_12v8n38\" id=\"Association_12v8n38_di\"\u003e\u003comgdi:waypoint x=\"284\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0q2dpdp\" id=\"TextAnnotation_0q2dpdp_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"154\" x=\"392\" y=\"88\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0lgdmx3\" id=\"Association_0lgdmx3_di\"\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"447\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example workflow that takes a PEM encoded SSL certificate as input and returns structured information about the certificate.",
      "export_key": "example_parse_utilities_parse_ssl_certificate",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328222337,
      "name": "Example: Parse Utilities Parse SSL Certificate",
      "object_type": "artifact",
      "programmatic_name": "example_parse_utilities_parse_ssl_certificate",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "4d2b8fd5-61fd-4a88-bfe8-febd37df76b2",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_pdfid",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_pdfid\" isExecutable=\"true\" name=\"Example: Parse Utilities PDFID (Artifact)\"\u003e\u003cdocumentation\u003eAn example of using the PDFiD function to get summary information about a PDF file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00kletc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1tq9c9t\"\u003e\u003cincoming\u003eSequenceFlow_14nu8l0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_00kletc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1xmweyh\"/\u003e\u003cserviceTask id=\"ServiceTask_1xmweyh\" name=\"Parse Utilities: PDFID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4b919f7-f943-405e-86fd-640f79e3ee8e\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output of PDFiD is a dictionary with the fundamental elements of the PDF file.\\n# These include,\\n#  - \\\"isPdf\\\" (True or False)\\n#  - \\\"header\\\" (the PDF version header)\\n#  - \\\"obj\\\", \\\"endobj\\\" and so on: the count of each element.\\n# More documentation can be found at https://blog.didierstevens.com/programs/pdf-tools/\\n\\n# Some sections of interest\\ninteresting_sections = [\\n  \u0027obj\u0027, \u0027endobj\u0027, \u0027stream\u0027, \u0027endstream\u0027, \u0027startxref\u0027, \u0027xref\u0027, \u0027trailer\u0027,\\n  \u0027/AA\u0027, \u0027/AcroForm\u0027, \u0027/EmbeddedFile\u0027, \u0027/Encrypt\u0027, \u0027/JBIG2Decode\u0027, \u0027/JS\u0027, \u0027/JavaScript\u0027, \u0027/Launch\u0027, \u0027/ObjStm\u0027, \u0027/OpenAction\u0027, \u0027/Page\u0027, \u0027/RichMedia\u0027, \u0027/XFA\u0027\\n  ]\\n\\nif not results.isPdf:\\n  incident.addNote(helper.createRichText(u\\\"Not a PDF file: {}\\\".format(results.get(\\\"filename\\\"))))\\nelse:\\n  # In this example we just write them to a note in the incident\\n  note_data = [u\\\"PDFID report for {} ({}):\\\".format(results.get(\\\"filename\\\"), results.header)]\\n\\n  for section in interesting_sections:\\n    value = results.get(section)\\n    if value is not None:\\n      note_data.append(\\\"{}: {}\\\".format(section, value))\\n\\n  text = helper.createPlainText(\\\"\\\\n\\\".join(note_data))\\n  incident.addNote(text)\\n  \\n  # Maybe extend this to alert if (/JS or /JavaScript) and (/AA or /OpenAction)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: incident_id artifact_id\\ninputs.parse_utilities_incident_id = incident.id\\ninputs.parse_utilities_artifact_id = artifact.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00kletc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14nu8l0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14nu8l0\" sourceRef=\"ServiceTask_1xmweyh\" targetRef=\"EndEvent_1tq9c9t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1bggj6z\"\u003e\u003ctext\u003eInput to the PDFiD function is base64-encoded content.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_04w90cd\" sourceRef=\"ServiceTask_1xmweyh\" targetRef=\"TextAnnotation_1bggj6z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1n8kxa0\"\u003e\u003ctext\u003ePerforms a quick analysis of the structure of the PDF file.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02fa1mz\" sourceRef=\"ServiceTask_1xmweyh\" targetRef=\"TextAnnotation_1n8kxa0\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tq9c9t\" id=\"EndEvent_1tq9c9t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"601\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"619\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00kletc\" id=\"SequenceFlow_00kletc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"267\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1xmweyh\" id=\"ServiceTask_1xmweyh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"336\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14nu8l0\" id=\"SequenceFlow_14nu8l0_di\"\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"601\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"518.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1bggj6z\" id=\"TextAnnotation_1bggj6z_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"178\" x=\"146\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_04w90cd\" id=\"Association_04w90cd_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1n8kxa0\" id=\"TextAnnotation_1n8kxa0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"186\" x=\"469\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02fa1mz\" id=\"Association_02fa1mz_di\"\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"171\"/\u003e\u003comgdi:waypoint x=\"542\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example of using the PDFiD function to get summary information about a PDF file attachment.",
      "export_key": "example_parse_utilities_pdfid",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328222101,
      "name": "Example: Parse Utilities PDFID (Artifact)",
      "object_type": "artifact",
      "programmatic_name": "example_parse_utilities_pdfid",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "bb67e6cd-843c-4fbb-b14b-83a35db60ca8",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_pdfid_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_pdfid_attachment\" isExecutable=\"true\" name=\"Example: Parse Utilities PDFID (Attachment)\"\u003e\u003cdocumentation\u003eAn example of using the PDFiD function to get summary information about a PDF file attachment.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0l8aigp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_16uamej\"\u003e\u003cincoming\u003eSequenceFlow_1s5gf7u\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0l8aigp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ctjpik\"/\u003e\u003cserviceTask id=\"ServiceTask_1ctjpik\" name=\"Parse Utilities: PDFID\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4b919f7-f943-405e-86fd-640f79e3ee8e\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The output of PDFiD is a dictionary with the fundamental elements of the PDF file.\\n# These include,\\n#  - \\\"isPdf\\\" (True or False)\\n#  - \\\"header\\\" (the PDF version header)\\n#  - \\\"obj\\\", \\\"endobj\\\" and so on: the count of each element.\\n# More documentation can be found at https://blog.didierstevens.com/programs/pdf-tools/\\n\\n# Some sections of interest\\ninteresting_sections = [\\n  \u0027obj\u0027, \u0027endobj\u0027, \u0027stream\u0027, \u0027endstream\u0027, \u0027startxref\u0027, \u0027xref\u0027, \u0027trailer\u0027,\\n  \u0027/AA\u0027, \u0027/AcroForm\u0027, \u0027/EmbeddedFile\u0027, \u0027/Encrypt\u0027, \u0027/JBIG2Decode\u0027, \u0027/JS\u0027, \u0027/JavaScript\u0027, \u0027/Launch\u0027, \u0027/ObjStm\u0027, \u0027/OpenAction\u0027, \u0027/Page\u0027, \u0027/RichMedia\u0027, \u0027/XFA\u0027\\n  ]\\n\\nif not results.isPdf:\\n  incident.addNote(helper.createRichText(u\\\"Not a PDF file: {}\\\".format(results.get(\\\"filename\\\"))))\\nelse:\\n  # In this example we just write them to a note in the incident\\n  note_data = [u\\\"PDFID report for {} ({}):\\\".format(results.get(\\\"filename\\\"), results.header)]\\n\\n  for section in interesting_sections:\\n    value = results.get(section)\\n    if value is not None:\\n      note_data.append(\\\"{}: {}\\\".format(section, value))\\n\\n  text = helper.createPlainText(\\\"\\\\n\\\".join(note_data))\\n  incident.addNote(text)\\n  \\n  # Maybe extend this to alert if (/JS or /JavaScript) and (/AA or /OpenAction)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Required inputs are: incident_id attachment_id\\ninputs.parse_utilities_incident_id = incident.id\\ninputs.parse_utilities_attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.parse_utilities_task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0l8aigp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1s5gf7u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1s5gf7u\" sourceRef=\"ServiceTask_1ctjpik\" targetRef=\"EndEvent_16uamej\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16uamej\" id=\"EndEvent_16uamej_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"568\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"586\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l8aigp\" id=\"SequenceFlow_0l8aigp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"260.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ctjpik\" id=\"ServiceTask_1ctjpik_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"323\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1s5gf7u\" id=\"SequenceFlow_1s5gf7u_di\"\u003e\u003comgdi:waypoint x=\"423\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"568\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"495.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "An example of using the PDFiD function to get summary information about a PDF file attachment.",
      "export_key": "example_parse_utilities_pdfid_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328221904,
      "name": "Example: Parse Utilities PDFID (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "example_parse_utilities_pdfid_attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "d6f12ac2-0ca2-4831-8a93-298c05e21fad",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_xml_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_xml_attachment\" isExecutable=\"true\" name=\"Example Parse Utilities XML (Attachment)\"\u003e\u003cdocumentation\u003eExample workflow to transform an XML document attachment using a defined xsl transform file\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1a8triy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0a0lwe3\"\u003e\u003cincoming\u003eSequenceFlow_10mbfg7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1a8triy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ewa6xd\"/\u003e\u003cserviceTask id=\"ServiceTask_0ewa6xd\" name=\"Parse Utilities: XML Transformati...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fb731c0f-f0ee-4a66-8cc5-ab98495a92ca\"\u003e{\"inputs\":{\"32241685-5dc0-48a2-8b07-c72776cd2730\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"cdcatalog.xslt\"}}},\"post_processing_script\":\"# results.content is the string representation of the transformed xml document\\ncontent = helper.createPlainText(results.content)\\nincident.addNote(content)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.parse_utilities_incident_id = incident.id\\ninputs.parse_utilities_attachment_id = attachment.id\\n\\n# If this is a \\\"task attachment\\\" then we will additionally have a task-id\\nif task is not None:\\n  inputs.parse_utilities_task_id = task.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1a8triy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10mbfg7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10mbfg7\" sourceRef=\"ServiceTask_0ewa6xd\" targetRef=\"EndEvent_0a0lwe3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0a0lwe3\" id=\"EndEvent_0a0lwe3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"505\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1a8triy\" id=\"SequenceFlow_1a8triy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"245.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ewa6xd\" id=\"ServiceTask_0ewa6xd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"293\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10mbfg7\" id=\"SequenceFlow_10mbfg7_di\"\u003e\u003comgdi:waypoint x=\"393\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"449\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to transform an XML document attachment using a defined xsl transform file",
      "export_key": "example_parse_utilities_xml_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328222891,
      "name": "Example Parse Utilities XML (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "example_parse_utilities_xml_attachment",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "620e21da-88dc-42e1-9006-094abcdc0b26",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_parse_utilities_xml_transformation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_xml_transformation\" isExecutable=\"true\" name=\"Example: Parse Utilities XML Transformation\"\u003e\u003cdocumentation\u003eExample workflow to transform an XML document artifact using a defined xsl transform file\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_08prnsm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08b2bd4\" name=\"Parse Utilities: XML Transformati...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fb731c0f-f0ee-4a66-8cc5-ab98495a92ca\"\u003e{\"inputs\":{\"32241685-5dc0-48a2-8b07-c72776cd2730\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"cdcatalog.xslt\"}}},\"post_processing_script\":\"# results.content is the string representation of the transformed xml document\\ncontent = helper.createPlainText(results.content)\\nincident.addNote(content)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.parse_utilities_artifact_id = artifact.id\\ninputs.parse_utilities_incident_id = incident.id\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_08prnsm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0k2e7mt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_01q3kn4\"\u003e\u003cincoming\u003eSequenceFlow_0k2e7mt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_08prnsm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08b2bd4\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0k2e7mt\" sourceRef=\"ServiceTask_08b2bd4\" targetRef=\"EndEvent_01q3kn4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ss1hld\"\u003e\u003ctext\u003einput: xml document to transform and xsl transform file\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1otzqzx\" sourceRef=\"ServiceTask_08b2bd4\" targetRef=\"TextAnnotation_0ss1hld\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1oqliv7\"\u003e\u003ctext\u003eOutput: results.content\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0zxfud4\" sourceRef=\"ServiceTask_08b2bd4\" targetRef=\"TextAnnotation_1oqliv7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08b2bd4\" id=\"ServiceTask_08b2bd4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"319\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ss1hld\" id=\"TextAnnotation_0ss1hld_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"162\" x=\"179\" y=\"69\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1otzqzx\" id=\"Association_1otzqzx_di\"\u003e\u003comgdi:waypoint x=\"333\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"274\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1oqliv7\" id=\"TextAnnotation_1oqliv7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"502\" y=\"70\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0zxfud4\" id=\"Association_0zxfud4_di\"\u003e\u003comgdi:waypoint x=\"417\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"529\" xsi:type=\"omgdc:Point\" y=\"100\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01q3kn4\" id=\"EndEvent_01q3kn4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"534\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"552\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08prnsm\" id=\"SequenceFlow_08prnsm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"319\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"258.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0k2e7mt\" id=\"SequenceFlow_0k2e7mt_di\"\u003e\u003comgdi:waypoint x=\"419\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"534\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"476.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to transform an XML document artifact using a defined xsl transform file",
      "export_key": "example_parse_utilities_xml_transformation",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667328223031,
      "name": "Example: Parse Utilities XML Transformation",
      "object_type": "artifact",
      "programmatic_name": "example_parse_utilities_xml_transformation",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "7c9adcb5-68e8-475c-bd0b-14ea88eae664",
      "workflow_id": 7
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_parse_utilities_email_parsing_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_parse_utilities_email_parsing_artifact\" isExecutable=\"true\" name=\"Example: Parse Utilities Email Parsing (Artifact)\"\u003e\u003cdocumentation\u003eExample Workflow showing to parse an Email File (.eml or .msg) from an Artifact File. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_000vypy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_11br5ck\"\u003e\u003cincoming\u003eSequenceFlow_0jkxrkh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_000vypy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0yztm4o\"/\u003e\u003cserviceTask id=\"ServiceTask_0yztm4o\" name=\"Parse Utilities: Email Parse\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8d57d19-a21e-42d4-9dba-06154084ca7e\"\u003e{\"inputs\":{},\"post_processing_script\":\"import re\\n\\nif not results.success:\\n  note_text = u\\\"\\\"\\\"Workflow \u0027Example: Parse Utilities Email Parsing (Artifact)\u0027 Failed\u0026lt;br\u0026gt;\\n                  \u0026lt;b\u0026gt;Reason:\u0026lt;/b\u0026gt; {0}\\\"\\\"\\\".format(str(results.reason))\\n  \\n  incident.addNote(helper.createRichText(note_text))\\n\\nelse:\\n  email = results.content\\n  \\n  # Get Email Subject\\n  eml_subject = email.get(\\\"subject\\\", \\\"BLANK SUBJECT LINE\\\")\\n\\n  #########################################\\n  # Add Artifacts for Email Recipient: to #\\n  #########################################\\n  for eml_addr in email.get(\\\"to\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  #########################################\\n  # Add Artifacts for Email Recipient: cc #\\n  #########################################\\n  for eml_addr in email.get(\\\"cc\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Recipient\\\", eml_addr[1], eml_addr[0])\\n  \\n  ########################################\\n  # Add Artifacts for Email Sender: from #\\n  ########################################\\n  for eml_addr in email.get(\\\"from\\\", []):\\n    if eml_addr[1]:\\n      incident.addArtifact(\\\"Email Sender\\\", eml_addr[1], eml_addr[0])\\n\\n  ################################################\\n  # Add Artifacts for IPs found in Email Headers #\\n  ################################################\\n  for eml_header in email.get(\\\"received\\\", []):\\n    \\n    the_header = eml_header.get(\\\"from\\\", None)\\n    \\n    if the_header:\\n      ips = re.findall(\u0027(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\u0027, the_header)\\n      unique_ips = set(ips)\\n  \\n      for an_ip in unique_ips:\\n        if an_ip:\\n          incident.addArtifact(\\\"IP Address\\\", an_ip, u\\\"Hop {0} at {1}\\\\n\\\\nHeader: {2}\\\".format(eml_header.get(\\\"hop\\\", \\\"\\\"), eml_header.get(\\\"date_utc\\\", \\\"\\\"), the_header))\\n\\n  ##############################################\\n  # Add Artifacts for URLs found in Email Body #\\n  ##############################################\\n  urls = []\\n  for eml_body_content in [email.get(\\\"plain_body\\\", \\\"\\\"), email.get(\\\"html_body\\\", \\\"\\\")]:\\n    urls.extend(re.findall(\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026amp;+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027, eml_body_content))\\n\\n  uniq_urls = set(urls)\\n\\n  for a_url in uniq_urls:\\n    # Remove any backslash as regex can add\\n    a_url = a_url.replace(\u0027\\\\\\\\\u0027,\\\"\\\")\\n    if a_url:\\n      incident.addArtifact(\\\"URL\\\", a_url, \\\"Found in parsed Email\\\")\\n  \\n  ################################################\\n  # Add the Email Body as a Note to the Incident #\\n  ################################################\\n  if email.get(\\\"body\\\"):\\n    note_text = u\\\"\\\"\\\"\u0026lt;b\u0026gt;Parsed Email::\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Subject:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;From:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{1}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;To:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{2}\u0026lt;br\u0026gt;\\n                    \u0026lt;b\u0026gt;Body:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{3}\\\"\\\"\\\".format(str(eml_subject),\\n                                  str(email.get(\\\"from\\\", \\\"N/A\\\")),\\n                                  str(email.get(\\\"to\\\", \\\"N/A\\\")), \\n                                  str(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n  \\n  \u0027\u0027\u0027Uncomment this if you would like to add a (safer) plain_text only Note\\n  if email.get(\\\"plain_body\\\"):\\n    note_text = u\\\"\\\"\\\"Parsed Email::\\\\n\\\\nSubject:\\\\n{0}\\\\n\\\\nFrom:\\\\n{1}\\\\n\\\\nTo:\\\\n{2}\\\\n\\\\nBody:\\\\n{3}\\\"\\\"\\\".format(str(eml_subject),\\n      str(email.get(\\\"from\\\", \\\"N/A\\\")), unicode(email.get(\\\"to\\\", \\\"N/A\\\")), str(email.get(\\\"body\\\", \\\"N/A\\\")))\\n\\n    incident.addNote(helper.createPlainText(note_text))\\n  \u0027\u0027\u0027\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Define incident_id and artifact_id\\ninputs.parse_utilities_incident_id = incident.id\\ninputs.parse_utilities_artifact_id = artifact.id\\n\\n# Setting this to True will add any found attachments as an Email Attachment Artifact\\ninputs.parse_utilities_email_attachments = True\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_000vypy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jkxrkh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0jkxrkh\" sourceRef=\"ServiceTask_0yztm4o\" targetRef=\"EndEvent_11br5ck\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_167jdg2\"\u003e\u003ctext\u003eResults returned as additional artifacts\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_13adgis\" sourceRef=\"ServiceTask_0yztm4o\" targetRef=\"TextAnnotation_167jdg2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_11br5ck\" id=\"EndEvent_11br5ck_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"635\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"653\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_000vypy\" id=\"SequenceFlow_000vypy_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"372\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"285\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0yztm4o\" id=\"ServiceTask_0yztm4o_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"372\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jkxrkh\" id=\"SequenceFlow_0jkxrkh_di\"\u003e\u003comgdi:waypoint x=\"472\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"635\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"553.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_167jdg2\" id=\"TextAnnotation_167jdg2_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"232\" x=\"482\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_13adgis\" id=\"Association_13adgis_di\"\u003e\u003comgdi:waypoint x=\"471\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"574\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Example Workflow showing to parse an Email File (.eml or .msg) from an Artifact File. Sender and recipient email addresses are added as Artifacts. URLs and IPs found in the email headers or body are also added as Artifacts. The body of the email is added as a Note to the Incident. If attachments are found in the parsed email message, they are added as Email Attachment Artifacts.",
      "export_key": "example_parse_utilities_email_parsing_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1667854357608,
      "name": "Example: Parse Utilities Email Parsing (Artifact)",
      "object_type": "artifact",
      "programmatic_name": "example_parse_utilities_email_parsing_artifact",
      "tags": [
        {
          "tag_handle": "fn_parse_utilities",
          "value": null
        }
      ],
      "uuid": "bf325fa1-c1a6-4367-acbf-88cfe5ad472d",
      "workflow_id": 5
    }
  ],
  "workspaces": []
}
