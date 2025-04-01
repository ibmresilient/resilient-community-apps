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
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Run rdap query against Artifact",
      "id": 480,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Run rdap query against Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "53c69fdd-a575-4ba7-86f1-6bd29970eb08",
      "view_items": [],
      "workflows": [
        "example_rdap_query"
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
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Run whois query against Artifact (RDAP)",
      "id": 481,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Run whois query against Artifact (RDAP)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "58cbc98c-66ab-47dc-95a9-74dd9df3427c",
      "view_items": [],
      "workflows": [
        "example_whois_query"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1743419508359,
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
      "export_key": "__function/rdap_depth",
      "hide_notification": false,
      "id": 3419,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "rdap_depth",
      "operation_perms": {},
      "operations": [],
      "placeholder": "0",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rdap_depth",
      "tooltip": "Can be 0, 1 or 2",
      "type_id": 11,
      "uuid": "85b2b2b8-a68b-4383-a004-ca060fd7c6a6",
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
      "export_key": "__function/whois_query",
      "hide_notification": false,
      "id": 2757,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "whois_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "ibm.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "whois_query",
      "tooltip": "IP, URL or DNS Artifact",
      "type_id": 11,
      "uuid": "94abbddb-6e44-4043-addf-b680576348f1",
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
      "export_key": "__function/rdap_query",
      "hide_notification": false,
      "id": 3420,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rdap_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "ibm.com",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rdap_query",
      "tooltip": "IP, URL or DNS Artifact",
      "type_id": 11,
      "uuid": "04edd19d-d008-4abc-a19b-731a9997320d",
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
      "created_date": 1743417887702,
      "description": {
        "content": "Using ipwhois library to make general queries in RDAP format",
        "format": "text"
      },
      "destination_handle": "fn_whois_rdap",
      "display_name": "RDAP: Query",
      "export_key": "rdap_query",
      "id": 324,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743417887702,
      "name": "rdap_query",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"nir\": null, \"asn_registry\": \"ripencc\", \"asn\": \"8075\", \"asn_cidr\": \"172.200.0.0/13\", \"asn_country_code\": \"GB\", \"asn_date\": \"2002-02-13\", \"asn_description\": \"MICROSOFT-CORP-MSN-AS-BLOCK, US\", \"query\": \"172.206.147.25\", \"network\": {\"handle\": \"172.128.0.0 - 172.215.255.255\", \"status\": [\"active\"], \"remarks\": null, \"notices\": [{\"title\": \"Filtered\", \"description\": \"This output has been filtered.\", \"links\": null}, {\"title\": \"Whois Inaccuracy Reporting\", \"description\": \"If you see inaccuracies in the results, please visit:\", \"links\": [\"https://www.ripe.net/contact-form?topic=ripe_dbm\u0026show_form=true\"]}, {\"title\": \"Source\", \"description\": \"Objects returned came from source\\nRIPE\", \"links\": null}, {\"title\": \"Terms and Conditions\", \"description\": \"This is the RIPE Database query service. The objects are in RDAP format.\", \"links\": [\"http://www.ripe.net/db/support/db-terms-conditions.pdf\"]}], \"links\": [\"https://rdap.db.ripe.net/ip/172.206.147.25\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": [{\"action\": \"registration\", \"timestamp\": \"2024-05-16T09:38:13Z\", \"actor\": null}, {\"action\": \"last changed\", \"timestamp\": \"2024-05-16T09:38:13Z\", \"actor\": null}], \"raw\": null, \"start_address\": \"172.128.0.0\", \"end_address\": \"172.215.255.255\", \"cidr\": \"172.128.0.0/10, 172.192.0.0/12, 172.208.0.0/13\", \"ip_version\": \"v4\", \"type\": \"ALLOCATED PA\", \"name\": \"UK-MICROSOFT-20000324\", \"country\": \"GB\", \"parent_handle\": \"0.0.0.0 - 255.255.255.255\"}, \"entities\": [\"DH5439-RIPE\", \"MICROSOFT-MAINT\", \"MRPA3-RIPE\", \"ORG-MA42-RIPE\", \"RIPE-NCC-HM-MNT\", \"MAC274-RIPE\"], \"objects\": {\"DH5439-RIPE\": {\"handle\": \"DH5439-RIPE\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": [\"https://rdap.db.ripe.net/entity/DH5439-RIPE\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": null, \"raw\": null, \"roles\": [\"administrative\"], \"contact\": {\"name\": \"Divya Quamara\", \"kind\": \"individual\", \"address\": [{\"type\": null, \"value\": \"One Microsoft Way\\nRedmond, WA 98052\"}], \"phone\": [{\"type\": \"voice\", \"value\": \"+1-425-882-8080\"}], \"email\": null, \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": null}, \"MICROSOFT-MAINT\": {\"handle\": \"MICROSOFT-MAINT\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": [\"https://rdap.db.ripe.net/entity/MICROSOFT-MAINT\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": null, \"raw\": null, \"roles\": [\"registrant\"], \"contact\": {\"name\": \"MICROSOFT-MAINT\", \"kind\": \"individual\", \"address\": null, \"phone\": null, \"email\": null, \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": null}, \"MRPA3-RIPE\": {\"handle\": \"MRPA3-RIPE\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": [\"https://rdap.db.ripe.net/entity/MRPA3-RIPE\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": null, \"raw\": null, \"roles\": [\"technical\"], \"contact\": {\"name\": \"Microsoft Routing, Peering, and DNS\", \"kind\": \"group\", \"address\": [{\"type\": null, \"value\": \"One Microsoft Way\\nRedmond, WA 98052\"}], \"phone\": null, \"email\": null, \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": null}, \"ORG-MA42-RIPE\": {\"handle\": \"ORG-MA42-RIPE\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": [\"https://rdap.db.ripe.net/entity/ORG-MA42-RIPE\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": null, \"raw\": null, \"roles\": [\"registrant\"], \"contact\": {\"name\": \"Microsoft Limited\", \"kind\": \"org\", \"address\": [{\"type\": null, \"value\": \"One Microsoft Way\\nWA 98052\\nRedmond\\nUNITED STATES\"}], \"phone\": [{\"type\": \"voice\", \"value\": \"+1 425 882 8080\"}, {\"type\": \"fax\", \"value\": \"+1 425 936 7329\"}], \"email\": null, \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": null}, \"RIPE-NCC-HM-MNT\": {\"handle\": \"RIPE-NCC-HM-MNT\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": [\"https://rdap.db.ripe.net/entity/RIPE-NCC-HM-MNT\", \"http://www.ripe.net/data-tools/support/documentation/terms\"], \"events\": null, \"raw\": null, \"roles\": [\"registrant\"], \"contact\": {\"name\": \"RIPE-NCC-HM-MNT\", \"kind\": \"individual\", \"address\": null, \"phone\": null, \"email\": null, \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": null}, \"MAC274-RIPE\": {\"handle\": \"MAC274-RIPE\", \"status\": null, \"remarks\": null, \"notices\": null, \"links\": null, \"events\": null, \"raw\": null, \"roles\": [\"abuse\"], \"contact\": {\"name\": \"Microsoft Abuse Contact\", \"kind\": \"group\", \"address\": [{\"type\": null, \"value\": \"One Microsoft Way\\nRedmond, WA 98052\"}], \"phone\": null, \"email\": [{\"type\": \"abuse\", \"value\": \"abuse@microsoft.com\"}], \"role\": null, \"title\": null}, \"events_actor\": null, \"entities\": [\"MICROSOFT-MAINT\"]}}, \"raw\": null, \"dns_zone\": \"25.147.206.172.origin.asn.cymru.com\", \"display_content\": \"{ \\\"dns_zone\\\":\\\"25.147.206.172.origin.asn.cymru.com\\\" }\"}, \"raw\": \"\", \"inputs\": {\"rdap_query\": \"172.206.147.25\", \"rdap_depth\": 0}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-whois-rdap\", \"package_version\": \"1.0.5\", \"host\": \"my.app.host\", \"execution_time_ms\": 1470, \"timestamp\": \"2024-09-24 13:56:32\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"nir\": {}, \"asn_registry\": {\"type\": \"string\"}, \"asn\": {\"type\": \"string\"}, \"asn_cidr\": {\"type\": \"string\"}, \"asn_country_code\": {\"type\": \"string\"}, \"asn_date\": {\"type\": \"string\"}, \"asn_description\": {\"type\": \"string\"}, \"query\": {\"type\": \"string\"}, \"network\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"remarks\": {}, \"notices\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"title\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"links\": {}}}}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"action\": {\"type\": \"string\"}, \"timestamp\": {\"type\": \"string\"}, \"actor\": {}}}}, \"raw\": {}, \"start_address\": {\"type\": \"string\"}, \"end_address\": {\"type\": \"string\"}, \"cidr\": {\"type\": \"string\"}, \"ip_version\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"country\": {\"type\": \"string\"}, \"parent_handle\": {\"type\": \"string\"}}}, \"entities\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"objects\": {\"type\": \"object\", \"properties\": {\"DH5439-RIPE\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {}, \"value\": {\"type\": \"string\"}}}}, \"phone\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}}, \"email\": {}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {}}}, \"MICROSOFT-MAINT\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {}, \"phone\": {}, \"email\": {}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {}}}, \"MRPA3-RIPE\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {}, \"value\": {\"type\": \"string\"}}}}, \"phone\": {}, \"email\": {}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {}}}, \"ORG-MA42-RIPE\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {}, \"value\": {\"type\": \"string\"}}}}, \"phone\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}}, \"email\": {}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {}}}, \"RIPE-NCC-HM-MNT\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {}, \"phone\": {}, \"email\": {}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {}}}, \"MAC274-RIPE\": {\"type\": \"object\", \"properties\": {\"handle\": {\"type\": \"string\"}, \"status\": {}, \"remarks\": {}, \"notices\": {}, \"links\": {}, \"events\": {}, \"raw\": {}, \"roles\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"contact\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"kind\": {\"type\": \"string\"}, \"address\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {}, \"value\": {\"type\": \"string\"}}}}, \"phone\": {}, \"email\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"value\": {\"type\": \"string\"}}}}, \"role\": {}, \"title\": {}}}, \"events_actor\": {}, \"entities\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}}, \"raw\": {}, \"dns_zone\": {\"type\": \"string\"}, \"display_content\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"rdap_query\": {\"type\": \"string\"}, \"rdap_depth\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "19b5bb37-9a4e-49ec-802a-fbc3006de117",
      "version": 0,
      "view_items": [
        {
          "content": "85b2b2b8-a68b-4383-a004-ca060fd7c6a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "04edd19d-d008-4abc-a19b-731a9997320d",
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
          "name": "Example: RDAP query",
          "object_type": "artifact",
          "programmatic_name": "example_rdap_query",
          "tags": [],
          "uuid": null,
          "workflow_id": 444
        }
      ]
    },
    {
      "created_date": 1743417887837,
      "description": {
        "content": "Using ipwhois library to make general queries in whois format",
        "format": "text"
      },
      "destination_handle": "fn_whois_rdap",
      "display_name": "WHOIS: query",
      "export_key": "whois_rdap_query",
      "id": 325,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743417887837,
      "name": "whois_rdap_query",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": \"1.0\", \"success\": true, \"reason\": null, \"content\": {\"nir\": null, \"asn_registry\": \"ripencc\", \"asn\": \"8075\", \"asn_cidr\": \"172.200.0.0/13\", \"asn_country_code\": \"GB\", \"asn_date\": \"2002-02-13\", \"asn_description\": \"MICROSOFT-CORP-MSN-AS-BLOCK, US\", \"query\": \"172.206.147.25\", \"nets\": [{\"cidr\": \"172.128.0.0/10, 172.192.0.0/12, 172.208.0.0/13\", \"name\": \"UK-MICROSOFT-20000324\", \"handle\": \"MRPA3-RIPE\", \"range\": \"172.128.0.0 - 172.215.255.255\", \"description\": \"Microsoft Corporation AS8075\\nTo report suspected security issues specific to\\ntraffic emanating from Microsoft online services,\\nincluding the distribution of malicious content\\nor other illicit or illegal material through a\\nMicrosoft online service, please submit reports\\nto:\\n* https://cert.microsoft.com\\nFor SPAM and other abuse issues, such as Microsoft\\nAccounts, please contact:\\n* abuse@microsoft.com\\nTo report security vulnerabilities in Microsoft\\nproducts and services, please contact:\\n* secure@microsoft.com\\nFor legal and law enforcement-related requests,\\nplease contact:\\n* msndcc@microsoft.com\\nFor routing, peering or DNS issues, please\\ncontact:\\n* IOC@microsoft.com\", \"country\": \"GB\", \"state\": null, \"city\": null, \"address\": \"One Microsoft Way\\nWA 98052\\nRedmond\\nUNITED STATES\", \"postal_code\": null, \"emails\": [\"abuse@microsoft.com\", \"secure@microsoft.com\", \"msndcc@microsoft.com\", \"IOC@microsoft.com\"], \"created\": \"2024-05-16T09:38:13Z\", \"updated\": \"2024-05-16T09:38:13Z\"}, {\"cidr\": \"172.200.0.0/13\", \"name\": null, \"handle\": null, \"range\": \"172.200.0.0 - 172.207.255.255\", \"description\": \"Microsoft\", \"country\": null, \"state\": null, \"city\": null, \"address\": null, \"postal_code\": null, \"emails\": null, \"created\": \"2022-07-08T19:11:00Z\", \"updated\": \"2022-07-08T19:11:00Z\"}], \"raw\": null, \"referral\": null, \"raw_referral\": null, \"dns_zone\": \"25.147.206.172.origin.asn.cymru.com\", \"display_content\": \"{ \\\"dns_zone\\\":\\\"25.147.206.172.origin.asn.cymru.com\\\" }\"}, \"raw\": \"\", \"inputs\": {\"whois_query\": \"172.206.147.25\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-whois-rdap\", \"package_version\": \"1.0.5\", \"host\": \"my.app.host\", \"execution_time_ms\": 1307, \"timestamp\": \"2024-09-24 13:57:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"nir\": {}, \"asn_registry\": {\"type\": \"string\"}, \"asn\": {\"type\": \"string\"}, \"asn_cidr\": {\"type\": \"string\"}, \"asn_country_code\": {\"type\": \"string\"}, \"asn_date\": {\"type\": \"string\"}, \"asn_description\": {\"type\": \"string\"}, \"query\": {\"type\": \"string\"}, \"nets\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"cidr\": {\"type\": \"string\"}, \"name\": {\"type\": [\"null\", \"string\"]}, \"handle\": {\"type\": [\"null\", \"string\"]}, \"range\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"country\": {\"type\": [\"null\", \"string\"]}, \"state\": {}, \"city\": {}, \"address\": {\"type\": [\"null\", \"string\"]}, \"postal_code\": {}, \"emails\": {}, \"created\": {\"type\": \"string\"}, \"updated\": {\"type\": \"string\"}}}}, \"raw\": {}, \"referral\": {}, \"raw_referral\": {}, \"dns_zone\": {\"type\": \"string\"}, \"display_content\": {\"type\": \"string\"}}}, \"raw\": {\"type\": \"string\"}, \"inputs\": {\"type\": \"object\", \"properties\": {\"whois_query\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "a040d3cd-d151-4c14-a622-26262ab6a9b9",
      "version": 0,
      "view_items": [
        {
          "content": "94abbddb-6e44-4043-addf-b680576348f1",
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
          "name": "Example: Whois query",
          "object_type": "artifact",
          "programmatic_name": "example_whois_query",
          "tags": [],
          "uuid": null,
          "workflow_id": 445
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 96,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1743419506532,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1743419506532,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0f3a4556-9302-485a-ad25-07a97bb51fd7"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_whois_rdap",
      "name": "fn_whois_rdap",
      "programmatic_name": "fn_whois_rdap",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "a13ff28e-5cde-4a52-a372-8f948483d32e"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [],
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
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_whois_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_whois_query\" isExecutable=\"true\" name=\"Example: Whois query\"\u003e\u003cdocumentation\u003eThis workflow generates RDAP formatted results from an IP, URL or DNS Artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tty0tn\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0f6uul4\"\u003e\u003cincoming\u003eSequenceFlow_1ev6m8m\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tty0tn\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_175ht7y\"/\u003e\u003cserviceTask id=\"ServiceTask_175ht7y\" name=\"WHOIS: query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a040d3cd-d151-4c14-a622-26262ab6a9b9\"\u003e{\"inputs\":{},\"post_processing_script\":\"def format_link(item):\\n  if item and (\\\"https://\\\" in item or \\\"http://\\\" in item):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        else:\\n          items.append(format_link(item))\\n      return separator.join(items)\\n    except:\\n        pass\\n    \\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n      \\n  return \\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n    \\n\\nnote = \\\"Whois for artifact: {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(artifact.value)\\nif results[\\\"success\\\"]:\\n  note = note + walk_dict(results[\\\"content\\\"])\\nelse:\\n  note = note + \\\"This Artifact has no whois information\\\"\\n\\nincident.addNote(helper.createRichText(note))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.whois_query = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tty0tn\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ev6m8m\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ev6m8m\" sourceRef=\"ServiceTask_175ht7y\" targetRef=\"EndEvent_0f6uul4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mzifei\"\u003e\u003ctext\u003eResults returned in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_076mvge\" sourceRef=\"ServiceTask_175ht7y\" targetRef=\"TextAnnotation_1mzifei\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0f6uul4\" id=\"EndEvent_0f6uul4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"522\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"540\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tty0tn\" id=\"SequenceFlow_1tty0tn_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"308\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"253\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_175ht7y\" id=\"ServiceTask_175ht7y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"308\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ev6m8m\" id=\"SequenceFlow_1ev6m8m_di\"\u003e\u003comgdi:waypoint x=\"408\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"522\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"465\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mzifei\" id=\"TextAnnotation_1mzifei_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"126\" x=\"408\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_076mvge\" id=\"Association_076mvge_di\"\u003e\u003comgdi:waypoint x=\"400\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"451\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "This workflow generates RDAP formatted results from an IP, URL or DNS Artifact",
      "export_key": "example_whois_query",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743418013028,
      "name": "Example: Whois query",
      "object_type": "artifact",
      "programmatic_name": "example_whois_query",
      "tags": [],
      "uuid": "d64df0b3-2a28-454a-8752-b1b1a4bde62b",
      "workflow_id": 445
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_rdap_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_rdap_query\" isExecutable=\"true\" name=\"Example: RDAP query\"\u003e\u003cdocumentation\u003eThis workflow generates RDAP formatted results from an IP, URL or DNS Artifact\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pz79gs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_06cg4dt\" name=\"RDAP: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"19b5bb37-9a4e-49ec-802a-fbc3006de117\"\u003e{\"inputs\":{},\"post_processing_script\":\"def format_link(item):\\n  if item and (\\\"https://\\\" in item or \\\"http://\\\" in item):\\n    return \\\"\u0026lt;a target=\u0027blank\u0027 href=\u0027{0}\u0027\u0026gt;{0}\u0026lt;/a\u0026gt;\\\".format(item)\\n  else:\\n    return item\\n\\ndef expand_list(list_value, separator=\\\"\u0026lt;br\u0026gt;\\\"):\\n  if not isinstance(list_value, list):\\n    return format_link(list_value)\\n  else:\\n    try:\\n      items = []\\n      for item in list_value:\\n        if isinstance(item, dict):\\n          items.append(\\\"\u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(walk_dict(item)))\\n        else:\\n          items.append(format_link(item))\\n      return separator.join(items)\\n    except:\\n        pass\\n    \\ndef walk_dict(sub_dict):\\n  notes = []\\n  for key, value in sub_dict.items():\\n    if key not in [\u0027display_content\u0027]:\\n      if isinstance(value, dict):\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: \u0026lt;div style=\u0027padding:10px\u0027\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(key, walk_dict(value)))\\n      else:\\n        notes.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;: {}\\\".format(key, expand_list(value)))\\n      \\n  return \\\"\u0026lt;br\u0026gt;\\\".join(notes)\\n    \\n\\nnote = \\\"RDAP Whois for artifact: {}\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\\\".format(artifact.value)\\nif results[\\\"success\\\"]:\\n  note = note + walk_dict(results[\\\"content\\\"])\\nelse:\\n  note = note + \\\"This Artifact has no ans accessible registry information\\\"\\n\\nincident.addNote(helper.createRichText(note))\\n\\n\\n\u0027\u0027\u0027\\n  for key.value in results[\\\"content\\\"].items():\\n    if isinstance\\n    if key not in [\u0027network\u0027]:\\n      item.append(\\\"\u0026lt;b\u0026gt;{}\u0026lt;/br\u0026gt;: {}\\\".format(key, expand_list)\\n  if des is None:\\n    note = note + \\\"\\\"\\\"\u0026lt;div\u0026gt;\u0026lt;p\u0026gt;\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;RDAP threat intelligence at {2}:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\\n\\\\n\\n    \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\u0026lt;/div\u0026gt;\u0026lt;/p\u0026gt;\\\\n\\\\n\\n    \u0026lt;div\u0026gt;\u0026lt;p\u0026gt;\u0026lt;br\u0026gt;\u0026lt;b\u0026gt; Possible accessible keys:\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\\n\\\\n\\n    \u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\\n\\\\n\\\"\\\"\\\".format(results[\\\"content\\\"][\\\"display_content\\\"],results[\\\"content\\\"].keys(),results[\\\"metrics\\\"][\\\"timestamp\\\"])\\n\u0027\u0027\u0027\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.rdap_query = artifact.value\\ninputs.rdap_depth = 0\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pz79gs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0pkk8jf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0ke3uqh\"\u003e\u003cincoming\u003eSequenceFlow_0pkk8jf\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pz79gs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_06cg4dt\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0pkk8jf\" sourceRef=\"ServiceTask_06cg4dt\" targetRef=\"EndEvent_0ke3uqh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ud6bnr\"\u003e\u003ctext\u003eResults returned in a Note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1196zgg\" sourceRef=\"ServiceTask_06cg4dt\" targetRef=\"TextAnnotation_0ud6bnr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"205\" y=\"199\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"200\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"207\" y=\"225\"/\u003e\u003comgdi:waypoint x=\"167\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_06cg4dt\" id=\"ServiceTask_06cg4dt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"348\" y=\"177\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ke3uqh\" id=\"EndEvent_0ke3uqh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"554\" y=\"199\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"527\" y=\"238\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pz79gs\" id=\"SequenceFlow_1pz79gs_di\"\u003e\u003comgdi:waypoint x=\"241\" y=\"217\"/\u003e\u003comgdi:waypoint x=\"348\" y=\"217\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"249.5\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0pkk8jf\" id=\"SequenceFlow_0pkk8jf_di\"\u003e\u003comgdi:waypoint x=\"448\" y=\"217\"/\u003e\u003comgdi:waypoint x=\"554\" y=\"217\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"456\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ud6bnr\" id=\"TextAnnotation_0ud6bnr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"122\" x=\"448\" y=\"86\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1196zgg\" id=\"Association_1196zgg_di\"\u003e\u003comgdi:waypoint x=\"437\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"491\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "This workflow generates RDAP formatted results from an IP, URL or DNS Artifact",
      "export_key": "example_rdap_query",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743419497045,
      "name": "Example: RDAP query",
      "object_type": "artifact",
      "programmatic_name": "example_rdap_query",
      "tags": [],
      "uuid": "cc1993f6-1cc4-489a-aa9c-3421cea342c6",
      "workflow_id": 444
    }
  ],
  "workspaces": []
}
