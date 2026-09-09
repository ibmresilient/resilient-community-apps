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
          "value": "Threat CVE ID"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - CVE Lookup",
      "id": 451,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Alien Vault - CVE Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5c32c7b5-2c0a-4280-abe6-0c9cf1371603",
      "view_items": [
        {
          "content": "2b75664d-5236-48fd-a7c5-f26209d24cf4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_cve"
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
          "value": "DNS Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - DNS Name Lookup",
      "id": 452,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Alien Vault - DNS Name Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "aa2d3f20-5cc9-4dd6-99e0-cfc8509dd5bf",
      "view_items": [
        {
          "content": "516378d7-dd7e-412e-ac86-175a197ca06e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_dns_name"
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
          "value": "Malware MD5 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-1 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware SHA-256 Hash"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Malware Sample Fuzzy Hash"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - File Hash Lookup",
      "id": 453,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Alien Vault - File Hash Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c6dc5096-02c2-4e94-a8f4-b7d686307aa8",
      "view_items": [
        {
          "content": "42485cdb-2f72-4bae-87cf-ad8726991909",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_hash"
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
          "value": "System Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - Host Name Lookup",
      "id": 454,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Alien Vault - Host Name Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c1aa182e-6154-4d97-9158-9fdc023c18ec",
      "view_items": [
        {
          "content": "6d1aa009-82d0-4562-8fcd-4e9dd98b35ef",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_host_name"
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
          "value": "IP Address"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - IP Address Lookup",
      "id": 455,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Alien Vault - IP Address Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "23a98b5a-dc8a-4965-af5a-ed3b5b2eaf2f",
      "view_items": [
        {
          "content": "239f43eb-fe39-4fa0-9aca-ba57fca0c7fd",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_ip"
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
          "value": "URL"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL Referer"
        }
      ],
      "enabled": true,
      "export_key": "Example: Alien Vault - URL Lookup",
      "id": 456,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Alien Vault - URL Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a09dae81-994c-4182-8fda-f22731133ffd",
      "view_items": [
        {
          "content": "b1277e25-6ebc-464a-8af3-96557d628af2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_alien_vault_otx_url"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1743072986046,
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
      "export_key": "__function/alienvault_search_value",
      "hide_notification": false,
      "id": 3008,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "alienvault_search_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "alienvault_search_value",
      "tooltip": "An artifact value to be searched for alien vault for threat intelligence data, an artifact value could be - IP Address, DNS Name, Host Name, File Hash,URL,Threat CVE ID.",
      "type_id": 11,
      "uuid": "9e690477-88ad-4463-94c2-f8b7fcb6d817",
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
      "export_key": "__function/alienvault_search_type",
      "hide_notification": false,
      "id": 3006,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "alienvault_search_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "alienvault_search_type",
      "tooltip": "a type of search element in alien vault for an threat intelligence data",
      "type_id": 11,
      "uuid": "184af415-4aa6-4b13-b040-93cc2a740180",
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
      "export_key": "__function/alienvault_section",
      "hide_notification": false,
      "id": 3007,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "alienvault_section",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "alienvault_section",
      "tooltip": "Type of the Section in which given Artifact would be searched for threat intelligence data",
      "type_id": 11,
      "uuid": "70f97335-39a3-4998-81e8-26dbb4673e28",
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
      "export_key": "actioninvocation/alien_vault_search_section_url",
      "hide_notification": false,
      "id": 3002,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section URL",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "b1277e25-6ebc-464a-8af3-96557d628af2",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "5056601c-2a95-4f7a-8446-79cc3ef35a61",
          "value": 3437
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "url_list",
          "properties": null,
          "uuid": "0187e6ea-10ba-4e98-9fe7-8e602853c554",
          "value": 3438
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
      "export_key": "actioninvocation/alien_vault_search_section_ip",
      "hide_notification": false,
      "id": 3005,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_ip",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section IP Address",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "239f43eb-fe39-4fa0-9aca-ba57fca0c7fd",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "87de7823-5231-405c-9ace-86d8d05e2624",
          "value": 3447
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "reputation",
          "properties": null,
          "uuid": "4fe31cca-f6d4-454d-8776-9410ad2be251",
          "value": 3448
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "geo",
          "properties": null,
          "uuid": "c730305d-34b3-439b-9c63-396d2b94984b",
          "value": 3449
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "malware",
          "properties": null,
          "uuid": "ecb6b8ff-7fd3-41ee-8c33-f78ee3040b77",
          "value": 3450
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "url_list",
          "properties": null,
          "uuid": "e31c2825-e4a1-4d0f-8d1e-681907cf99c4",
          "value": 3451
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "passive_dns",
          "properties": null,
          "uuid": "d3a676a6-2141-4236-b33b-ee5061e19498",
          "value": 3452
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "http_scans",
          "properties": null,
          "uuid": "e536ed03-b5cc-4d05-b522-6b2b4cdf6863",
          "value": 3453
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
      "export_key": "actioninvocation/alien_vault_search_section_cve",
      "hide_notification": false,
      "id": 3003,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_cve",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section CVE",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "2b75664d-5236-48fd-a7c5-f26209d24cf4",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "58ef5268-3855-4862-a508-fdf9c4ac1639",
          "value": 3439
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
      "export_key": "actioninvocation/alien_vault_search_section_hash",
      "hide_notification": false,
      "id": 3000,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_hash",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section Hash",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "42485cdb-2f72-4bae-87cf-ad8726991909",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "b6cf624e-f2fa-4a55-9cf1-7dda302a901c",
          "value": 3429
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "analysis",
          "properties": null,
          "uuid": "06b80f7a-cc36-40cc-b66c-d6bc9f64fded",
          "value": 3430
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
      "export_key": "actioninvocation/alien_vault_search_section_dns_name",
      "hide_notification": false,
      "id": 3004,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_dns_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section DNS Name",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "516378d7-dd7e-412e-ac86-175a197ca06e",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "9d76994a-4817-44fe-b46a-18a84f47680b",
          "value": 3440
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "geo",
          "properties": null,
          "uuid": "e4e2947c-2754-4b74-9a27-6a935279bb93",
          "value": 3441
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "malware",
          "properties": null,
          "uuid": "571e6ac0-2cdd-4123-9ef8-a93e074a06ac",
          "value": 3442
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "url_list",
          "properties": null,
          "uuid": "1c0f7b6f-7ae8-4bf9-b1fa-a0b10bba28de",
          "value": 3443
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "passive_dns",
          "properties": null,
          "uuid": "878057f8-d2bd-48f7-944d-d4fb0e5ab13d",
          "value": 3444
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "whois",
          "properties": null,
          "uuid": "3809b325-0964-4b00-8cfb-3a509bc195ad",
          "value": 3445
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "http_scans",
          "properties": null,
          "uuid": "a7a7500d-aac5-42d5-beac-03e9cbc5fa04",
          "value": 3446
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
      "export_key": "actioninvocation/alien_vault_search_section_host_name",
      "hide_notification": false,
      "id": 3001,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "alien_vault_search_section_host_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Alien Vault Search Section Host Name",
      "tooltip": "*general: General information about the artifact, such as geo data, and a list of the other sections currently available for this artifact. *reputation: OTX data on malicious activity observed by AlienVault Labs. *geo: A more verbose listing of geographic data (Country code, coordinates, etc.). *malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this artifact. *url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this artifact. *passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this artifact. *http_scans:  Meta data for http(s) connections to the Artifact. ",
      "type_id": 6,
      "uuid": "6d1aa009-82d0-4562-8fcd-4e9dd98b35ef",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "general",
          "properties": null,
          "uuid": "a796ffa9-3a43-4280-bc93-d4b610319bae",
          "value": 3431
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "geo",
          "properties": null,
          "uuid": "9d5390be-c878-4c7b-957d-ecc8d079aefb",
          "value": 3432
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "malware",
          "properties": null,
          "uuid": "ec41f3b6-bd3c-4c31-89a8-8a1c469a0849",
          "value": 3433
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "url_list",
          "properties": null,
          "uuid": "c7a92b8f-4236-47c8-aec2-2e418e35bbb3",
          "value": 3434
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "passive_dns",
          "properties": null,
          "uuid": "9bfb8b53-8f87-490f-b20c-bdc10def8149",
          "value": 3435
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "http_scans",
          "properties": null,
          "uuid": "e624e982-058e-4bc7-ba87-1af6c46fb0a4",
          "value": 3436
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
      "created_date": 1743069349850,
      "description": {
        "content": "A function to lookup threat intelligence information from Alien Vault OTX for given artifact value.",
        "format": "text"
      },
      "destination_handle": "fn_alienvault_otx",
      "display_name": "Alien Vault OTX",
      "export_key": "fn_alienvault_otx_threat_lookup",
      "id": 307,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743069349850,
      "name": "fn_alienvault_otx_threat_lookup",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "41ac9f58-135f-46f8-98aa-0f862004ebc7",
      "version": 0,
      "view_items": [
        {
          "content": "9e690477-88ad-4463-94c2-f8b7fcb6d817",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "184af415-4aa6-4b13-b040-93cc2a740180",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70f97335-39a3-4998-81e8-26dbb4673e28",
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
          "name": "Example: Alien Vault OTX CVE",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_cve",
          "tags": [],
          "uuid": null,
          "workflow_id": 430
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Alien Vault OTX DNS Name",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_dns_name",
          "tags": [],
          "uuid": null,
          "workflow_id": 429
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Alien Vault OTX Hash",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_hash",
          "tags": [],
          "uuid": null,
          "workflow_id": 426
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Alien Vault OTX Host Name",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_host_name",
          "tags": [],
          "uuid": null,
          "workflow_id": 427
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Alien Vault OTX IP Address",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_ip",
          "tags": [],
          "uuid": null,
          "workflow_id": 425
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Alien Vault OTX URL",
          "object_type": "artifact",
          "programmatic_name": "example_alien_vault_otx_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 428
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 78,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1743072983752,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1743072983752,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "fa759041-5854-4b98-85bd-a89938186a6f"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_alienvault_otx",
      "name": "fn_alienvault_otx",
      "programmatic_name": "fn_alienvault_otx",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "1d9e1378-e01a-4dc3-a852-205f90c4a91c"
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
        "workflow_id": "example_alien_vault_otx_dns_name",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_dns_name\" isExecutable=\"true\" name=\"Example: Alien Vault OTX DNS Name\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact DNS Name.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rtnpd5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_056dkal\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_dns_name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rtnpd5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1lo28mh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1rtnpd5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_056dkal\"/\u003e\u003cendEvent id=\"EndEvent_0ldg1xs\"\u003e\u003cincoming\u003eSequenceFlow_1lo28mh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1lo28mh\" sourceRef=\"ServiceTask_056dkal\" targetRef=\"EndEvent_0ldg1xs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1msfrid\"\u003e\u003ctext\u003eA workflow\u00a0 to lookup threat intelligence information from Alien Vault OTX for given artifact DNS Name.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wayli3\" sourceRef=\"ServiceTask_056dkal\" targetRef=\"TextAnnotation_1msfrid\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_056dkal\" id=\"ServiceTask_056dkal_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"395\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rtnpd5\" id=\"SequenceFlow_1rtnpd5_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"395\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"296.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ldg1xs\" id=\"EndEvent_0ldg1xs_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"757\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"775\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lo28mh\" id=\"SequenceFlow_1lo28mh_di\"\u003e\u003comgdi:waypoint x=\"495\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"757\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"626\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1msfrid\" id=\"TextAnnotation_1msfrid_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"350\" x=\"467\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wayli3\" id=\"Association_0wayli3_di\"\u003e\u003comgdi:waypoint x=\"495\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"580\" y=\"125\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact DNS Name.",
      "export_key": "example_alien_vault_otx_dns_name",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069482199,
      "name": "Example: Alien Vault OTX DNS Name",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_dns_name",
      "tags": [],
      "uuid": "4cd1eb32-11f8-4b4f-b457-1c1e0af467a0",
      "workflow_id": 429
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_alien_vault_otx_hash",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_hash\" isExecutable=\"true\" name=\"Example: Alien Vault OTX Hash\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact File Hashes.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0py16cf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_18w1e4w\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_hash\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0py16cf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1t0odx3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0py16cf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_18w1e4w\"/\u003e\u003cendEvent id=\"EndEvent_0vzh13a\"\u003e\u003cincoming\u003eSequenceFlow_1t0odx3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1t0odx3\" sourceRef=\"ServiceTask_18w1e4w\" targetRef=\"EndEvent_0vzh13a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1v8st45\"\u003e\u003ctext\u003eA workflow to lookup threat intelligence information from Alien Vault OTX for given artifact hashes.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1v48ne4\" sourceRef=\"ServiceTask_18w1e4w\" targetRef=\"TextAnnotation_1v8st45\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_18w1e4w\" id=\"ServiceTask_18w1e4w_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"405\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0py16cf\" id=\"SequenceFlow_0py16cf_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"301.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0vzh13a\" id=\"EndEvent_0vzh13a_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"711\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"729\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t0odx3\" id=\"SequenceFlow_1t0odx3_di\"\u003e\u003comgdi:waypoint x=\"505\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"711\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"608\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1v8st45\" id=\"TextAnnotation_1v8st45_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"317\" x=\"497\" y=\"65\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1v48ne4\" id=\"Association_1v48ne4_di\"\u003e\u003comgdi:waypoint x=\"505\" y=\"178\"/\u003e\u003comgdi:waypoint x=\"604\" y=\"123\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact File Hashes.",
      "export_key": "example_alien_vault_otx_hash",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069505410,
      "name": "Example: Alien Vault OTX Hash",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_hash",
      "tags": [],
      "uuid": "8c8ca418-05ff-4fa2-8587-97375d803ff2",
      "workflow_id": 426
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_alien_vault_otx_ip",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_ip\" isExecutable=\"true\" name=\"Example: Alien Vault OTX IP Address\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact IP Address.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0vilaka\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0o5ibux\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_ip\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0vilaka\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1jb96lx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0vilaka\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0o5ibux\"/\u003e\u003cendEvent id=\"EndEvent_0vazgdh\"\u003e\u003cincoming\u003eSequenceFlow_1jb96lx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1jb96lx\" sourceRef=\"ServiceTask_0o5ibux\" targetRef=\"EndEvent_0vazgdh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1x7c0a8\"\u003e\u003ctext\u003eA workflow to lookup threat intelligence information from Alien Vault OTX for given artifact IP Address.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vtib6v\" sourceRef=\"ServiceTask_0o5ibux\" targetRef=\"TextAnnotation_1x7c0a8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0o5ibux\" id=\"ServiceTask_0o5ibux_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"376.74123711340206\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vilaka\" id=\"SequenceFlow_0vilaka_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"377\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"287.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0vazgdh\" id=\"EndEvent_0vazgdh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"695\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"713\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jb96lx\" id=\"SequenceFlow_1jb96lx_di\"\u003e\u003comgdi:waypoint x=\"477\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"695\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"586\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1x7c0a8\" id=\"TextAnnotation_1x7c0a8_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"362\" x=\"473\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vtib6v\" id=\"Association_1vtib6v_di\"\u003e\u003comgdi:waypoint x=\"477\" y=\"184\"/\u003e\u003comgdi:waypoint x=\"600\" y=\"129\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact IP Address.",
      "export_key": "example_alien_vault_otx_ip",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069542839,
      "name": "Example: Alien Vault OTX IP Address",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_ip",
      "tags": [],
      "uuid": "470cbf3d-8ffe-4dac-adc5-e83c9cd72c4f",
      "workflow_id": 425
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_alien_vault_otx_cve",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_cve\" isExecutable=\"true\" name=\"Example: Alien Vault OTX CVE\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact threat CVE ID.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p0bfaj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1lq04a3\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_cve\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p0bfaj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ung5vm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p0bfaj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1lq04a3\"/\u003e\u003cendEvent id=\"EndEvent_04hzlr8\"\u003e\u003cincoming\u003eSequenceFlow_1ung5vm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ung5vm\" sourceRef=\"ServiceTask_1lq04a3\" targetRef=\"EndEvent_04hzlr8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06kmv39\"\u003e\u003ctext\u003eA workflow to lookup threat intelligence information from Alien Vault OTX for given artifact Threat CVE ID .\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0barl9k\" sourceRef=\"ServiceTask_1lq04a3\" targetRef=\"TextAnnotation_06kmv39\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1lq04a3\" id=\"ServiceTask_1lq04a3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"359\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p0bfaj\" id=\"SequenceFlow_0p0bfaj_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"359\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"233.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04hzlr8\" id=\"EndEvent_04hzlr8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"669\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"687\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ung5vm\" id=\"SequenceFlow_1ung5vm_di\"\u003e\u003comgdi:waypoint x=\"459\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"633\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"633\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"669\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"603\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06kmv39\" id=\"TextAnnotation_06kmv39_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"342\" x=\"497\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0barl9k\" id=\"Association_0barl9k_di\"\u003e\u003comgdi:waypoint x=\"459\" y=\"186\"/\u003e\u003comgdi:waypoint x=\"577\" y=\"138\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact threat CVE ID.",
      "export_key": "example_alien_vault_otx_cve",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069458881,
      "name": "Example: Alien Vault OTX CVE",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_cve",
      "tags": [],
      "uuid": "edee0b44-5aa9-41b0-aef3-2d3fcc841d6a",
      "workflow_id": 430
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_alien_vault_otx_host_name",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_host_name\" isExecutable=\"true\" name=\"Example: Alien Vault OTX Host Name\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact Host Name.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1e7tzyw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1x2fhdw\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_host_name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1e7tzyw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1l5h9qi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1e7tzyw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1x2fhdw\"/\u003e\u003cendEvent id=\"EndEvent_0myr3mg\"\u003e\u003cincoming\u003eSequenceFlow_1l5h9qi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1l5h9qi\" sourceRef=\"ServiceTask_1x2fhdw\" targetRef=\"EndEvent_0myr3mg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ghqe0p\"\u003e\u003ctext\u003eA workflow to lookup threat intelligence information from Alien Vault OTX for given artifact Host Name.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nfvovw\" sourceRef=\"ServiceTask_1x2fhdw\" targetRef=\"TextAnnotation_0ghqe0p\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1x2fhdw\" id=\"ServiceTask_1x2fhdw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"459\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e7tzyw\" id=\"SequenceFlow_1e7tzyw_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"459\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"328.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0myr3mg\" id=\"EndEvent_0myr3mg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"768\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"786\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l5h9qi\" id=\"SequenceFlow_1l5h9qi_di\"\u003e\u003comgdi:waypoint x=\"559\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"665\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"665\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"768\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"680\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ghqe0p\" id=\"TextAnnotation_0ghqe0p_di\"\u003e\u003comgdc:Bounds height=\"66\" width=\"308\" x=\"536\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nfvovw\" id=\"Association_1nfvovw_di\"\u003e\u003comgdi:waypoint x=\"555\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"647\" y=\"104\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact Host Name.",
      "export_key": "example_alien_vault_otx_host_name",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069523980,
      "name": "Example: Alien Vault OTX Host Name",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_host_name",
      "tags": [],
      "uuid": "6b68b17b-baec-4ecb-9a7e-562b4bcce37e",
      "workflow_id": 427
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_alien_vault_otx_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_alien_vault_otx_url\" isExecutable=\"true\" name=\"Example: Alien Vault OTX URL\"\u003e\u003cdocumentation\u003eLookup threat intelligence data from Alient Vault OTX for artifact URL.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_01mpud5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bmu40d\" name=\"Alien Vault OTX\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"41ac9f58-135f-46f8-98aa-0f862004ebc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"rich_text_format = \\\"\u0026lt;p\u0026gt;\u0026lt;b\u0026gt;{}\u0026amp;ensp:\u0026amp;ensp\u0026lt;/b\u0026gt;{}\u0026amp;ensp\u0026amp;ensp\u0026lt;/p\u0026gt;\\\"\\nrich_text_tmp = \\\"\\\"\\nresult_data = results[\u0027content\u0027]\\nfor key_data,value_data in result_data.items():\\n               rich_text_tmp += rich_text_format.format(key_data.upper(),value_data)\\nbrowse_rich_text_final = helper.createRichText(rich_text_tmp)\\nincident.addNote(browse_rich_text_final)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.alienvault_search_value = artifact.value\\ninputs.alienvault_search_type = artifact.type\\ninputs.alienvault_section = rule.properties.alien_vault_search_section_url\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_01mpud5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o4zglt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_01mpud5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bmu40d\"/\u003e\u003cendEvent id=\"EndEvent_1mujvmt\"\u003e\u003cincoming\u003eSequenceFlow_0o4zglt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0o4zglt\" sourceRef=\"ServiceTask_1bmu40d\" targetRef=\"EndEvent_1mujvmt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1yd5r81\"\u003e\u003ctext\u003eA workflow to lookup threat intelligence information from Alien Vault OTX for given artifact URL.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0mj4ck4\" sourceRef=\"ServiceTask_1bmu40d\" targetRef=\"TextAnnotation_1yd5r81\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bmu40d\" id=\"ServiceTask_1bmu40d_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"462\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01mpud5\" id=\"SequenceFlow_01mpud5_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"462\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"330\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1mujvmt\" id=\"EndEvent_1mujvmt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"758\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"776\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o4zglt\" id=\"SequenceFlow_0o4zglt_di\"\u003e\u003comgdi:waypoint x=\"562\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"758\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"660\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1yd5r81\" id=\"TextAnnotation_1yd5r81_di\"\u003e\u003comgdc:Bounds height=\"73\" width=\"286\" x=\"564\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0mj4ck4\" id=\"Association_0mj4ck4_di\"\u003e\u003comgdi:waypoint x=\"562\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"635\" y=\"145\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Lookup threat intelligence data from Alient Vault OTX for artifact URL.",
      "export_key": "example_alien_vault_otx_url",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743069564901,
      "name": "Example: Alien Vault OTX URL",
      "object_type": "artifact",
      "programmatic_name": "example_alien_vault_otx_url",
      "tags": [],
      "uuid": "cbd84b39-8541-4baa-968d-438a932d785e",
      "workflow_id": 428
    }
  ],
  "workspaces": []
}
