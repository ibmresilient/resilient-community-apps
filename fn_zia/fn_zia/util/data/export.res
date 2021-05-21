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
          "value": "DNS Name"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Add To Allowlist",
      "id": 56,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: ZIA: Add To Allowlist",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac4df0a9-09f6-411a-8613-9e2be980d2e4",
      "view_items": [],
      "workflows": [
        "wf_zia_add_to_allowlist"
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
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Add To Blocklist",
      "id": 28,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: ZIA: Add To Blocklist",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f1e3550c-3d13-46ee-ba8b-1179b991ee34",
      "view_items": [],
      "workflows": [
        "wf_zia_add_to_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: ZIA: Get Allowlist",
      "id": 55,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ZIA: Get Allowlist",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "861a4120-b643-4715-a06f-f9ea8db7bbbb",
      "view_items": [],
      "workflows": [
        "wf_zia_get_allowlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: ZIA: Get Blocklist",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ZIA: Get Blocklist",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f758382d-0f15-471d-9a8e-68b87dc7b8ea",
      "view_items": [],
      "workflows": [
        "wf_zia_get_blocklist"
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
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Remove From Allowlist",
      "id": 57,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: ZIA: Remove From Allowlist",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "717951da-de2a-4c4c-9c7a-9a976baa9eb8",
      "view_items": [],
      "workflows": [
        "wf_zia_remove_from_allowlist"
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
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "IP Address"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Remove From Blocklist",
      "id": 53,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: ZIA: Remove From Blocklist",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "15e06655-8c4d-4877-8745-b3f11bb2616f",
      "view_items": [],
      "workflows": [
        "wf_zia_remove_from_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "zia_allowlist.allowlist_url",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Remove URL From Allowlist",
      "id": 58,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ZIA: Remove URL From Allowlist",
      "object_type": "zia_allowlist",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e87a967c-d364-4046-97db-0abe89202405",
      "view_items": [],
      "workflows": [
        "wf_zia_remove_url_from_allowlist"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "zia_blocklist.blocklist_url",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: ZIA: Remove URL From Blocklist",
      "id": 54,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ZIA: Remove URL From Blocklist",
      "object_type": "zia_blocklist",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "93b1a3e9-24ec-4063-8a0f-c2ab6fbc5b83",
      "view_items": [],
      "workflows": [
        "wf_zia_remove_url_from_blocklist"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1621596072807,
  "export_format_version": 2,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/zia_blocklisturls",
      "hide_notification": false,
      "id": 433,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_blocklisturls",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "zia_blocklisturls",
      "tooltip": "Add  URLs or IP addresses to the blocklist. See following for URL guidelines  https://help.zscaler.com/zia/url-format-guidelines",
      "type_id": 11,
      "uuid": "3a967529-342d-4803-b5f6-cc5a39568878",
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
      "export_key": "__function/zia_allowlisturls",
      "hide_notification": false,
      "id": 553,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_allowlisturls",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "zia_allowlisturls",
      "tooltip": "Add  URLs or IP addresses to the allowlist. See following for URL guidelines  https://help.zscaler.com/zia/url-format-guidelines",
      "type_id": 11,
      "uuid": "49fed504-d765-4ace-8dff-9bbf356649cf",
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
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add URLs or IP addresses to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add To Allowlist",
      "export_key": "funct_zia_add_to_allowlist",
      "id": 19,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1621421963479,
      "name": "funct_zia_add_to_allowlist",
      "tags": [],
      "uuid": "1f0a1aaa-477e-4ed8-afa2-13cb049e47d7",
      "version": 4,
      "view_items": [
        {
          "content": "49fed504-d765-4ace-8dff-9bbf356649cf",
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
          "name": "Example: ZIA: Add To Allowlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_to_allowlist",
          "tags": [],
          "uuid": null,
          "workflow_id": 31
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add URLs or IP addresses to the blocklist.\nSee following for URL guidelines  https://help.zscaler.com/zia/url-format-guidelines",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add To Blocklist",
      "export_key": "funct_zia_add_to_blocklist",
      "id": 2,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1620916717355,
      "name": "funct_zia_add_to_blocklist",
      "tags": [],
      "uuid": "d02e8977-6437-4093-8e19-422f3ba315f7",
      "version": 7,
      "view_items": [
        {
          "content": "3a967529-342d-4803-b5f6-cc5a39568878",
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
          "name": "Example: ZIA: Add To Blocklist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_to_blocklist",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Gets a list of allow-listed URLs",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get Allowlist",
      "export_key": "funct_zia_get_allowlist",
      "id": 18,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1620926973576,
      "name": "funct_zia_get_allowlist",
      "tags": [],
      "uuid": "afef84ad-f288-4a0c-a8e1-7c22ffcf1261",
      "version": 3,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: ZIA: Get Allowlist",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_allowlist",
          "tags": [],
          "uuid": null,
          "workflow_id": 29
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get a list of black-listed URLs",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get Blocklist",
      "export_key": "funct_zia_get_blocklist",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1621421982298,
      "name": "funct_zia_get_blocklist",
      "tags": [],
      "uuid": "c24a73f2-6ef7-4b12-9b39-ad345ffe0b7f",
      "version": 4,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: ZIA: Get Blocklist",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_blocklist",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Remove  URLs or IP addresses from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Remove From Allowlist",
      "export_key": "funct_zia_remove_from_allowlist",
      "id": 20,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1620998465244,
      "name": "funct_zia_remove_from_allowlist",
      "tags": [],
      "uuid": "e642b020-f7b1-4e65-aa18-8f05e28ae07e",
      "version": 1,
      "view_items": [
        {
          "content": "49fed504-d765-4ace-8dff-9bbf356649cf",
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
          "name": "Example: ZIA: Remove From Allowlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_from_allowlist",
          "tags": [],
          "uuid": null,
          "workflow_id": 32
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: ZIA: Remove URL From Allowlist",
          "object_type": "zia_allowlist",
          "programmatic_name": "wf_zia_remove_url_from_allowlist",
          "tags": [],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Remove  URLs or IP addresses from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Remove From Blocklist",
      "export_key": "funct_zia_remove_from_blocklist",
      "id": 17,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1620650611194,
      "name": "funct_zia_remove_from_blocklist",
      "tags": [],
      "uuid": "eafc0196-f4bd-4654-8b7c-90e2a67ccac7",
      "version": 3,
      "view_items": [
        {
          "content": "3a967529-342d-4803-b5f6-cc5a39568878",
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
          "name": "Example: ZIA: Remove From Blocklist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_from_blocklist",
          "tags": [],
          "uuid": null,
          "workflow_id": 26
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: ZIA: Remove URL From Blocklist",
          "object_type": "zia_blocklist",
          "programmatic_name": "wf_zia_remove_url_from_blocklist",
          "tags": [],
          "uuid": null,
          "workflow_id": 27
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 122,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1621596073843,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1621596073843,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "zia",
      "name": "zia",
      "programmatic_name": "zia",
      "tags": [],
      "users": [
        "a@a.com"
      ],
      "uuid": "bcaa4221-77d7-4b5f-a538-aff82236d457"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6328,
    "major": 39,
    "minor": 0,
    "version": "39.0.6328"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "Zscaler Internet Access - Allowlist",
      "export_key": "zia_allowlist",
      "fields": {
        "allowlist_url": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_allowlist/allowlist_url",
          "hide_notification": false,
          "id": 551,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "allowlist_url",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Allowlist url",
          "tooltip": "A url  or  ip address which is on allowlist",
          "type_id": 1007,
          "uuid": "f9b4cb08-86ff-4f39-a3af-d8992d8cc329",
          "values": [],
          "width": 271
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_allowlist/query_execution_date",
          "hide_notification": false,
          "id": 552,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query execution date",
          "tooltip": "",
          "type_id": 1007,
          "uuid": "037eb7d8-1d26-440c-b814-69d89b44c2ed",
          "values": [],
          "width": 427
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
      "type_name": "zia_allowlist",
      "uuid": "6172469d-1a8d-4898-911d-817cb93c9198"
    },
    {
      "actions": [],
      "display_name": "Zscaler Internet Access - Blocklist",
      "export_key": "zia_blocklist",
      "fields": {
        "blocklist_url": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_blocklist/blocklist_url",
          "hide_notification": false,
          "id": 550,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "blocklist_url",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Blocklist url",
          "tooltip": "A url  or  ip address which is on blocklist",
          "type_id": 1006,
          "uuid": "b227eee6-0fc0-4352-8975-53d7b1b393b7",
          "values": [],
          "width": 321
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_blocklist/query_execution_date",
          "hide_notification": false,
          "id": 549,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_execution_date",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Query Execution Date",
          "tooltip": "",
          "type_id": 1006,
          "uuid": "f8a3ddba-bd77-4179-91ec-0d73b440ed63",
          "values": [],
          "width": 351
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
      "type_name": "zia_blocklist",
      "uuid": "d2f1f7e6-5220-4e30-aed3-e1e0f0c99b83"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "wf_zia_get_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_allowlist\" isExecutable=\"true\" name=\"Example: ZIA: Get Allowlist\"\u003e\u003cdocumentation\u003eGet a list of allow-listed URLs\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_061sgnf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1u727i8\" name=\"ZIA: Get Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"afef84ad-f288-4a0c-a8e1-7c22ffcf1261\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_allowlist post processing script ##\\n\\n#  Globals\\n\\nFN_NAME = \\\"funct_zia_get_allowlist\\\"\\nWF_NAME = \\\"Example: ZIA: Get Allowlist\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    if CONTENT:\\n        allowlist_urls = CONTENT.whitelistUrls\\n        note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; allowlist URLS (s) returned for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(allowlist_urls), FN_NAME)\\n        for url in allowlist_urls:\\n            newrow = incident.addRow(\\\"zia_allowlist\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.allowlist_url = url\\n\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_061sgnf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1intjjs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_061sgnf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1u727i8\"/\u003e\u003cendEvent id=\"EndEvent_01p3u33\"\u003e\u003cincoming\u003eSequenceFlow_1intjjs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1intjjs\" sourceRef=\"ServiceTask_1u727i8\" targetRef=\"EndEvent_01p3u33\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1u727i8\" id=\"ServiceTask_1u727i8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"228\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_061sgnf\" id=\"SequenceFlow_061sgnf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"228\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01p3u33\" id=\"EndEvent_01p3u33_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"381\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1intjjs\" id=\"SequenceFlow_1intjjs_di\"\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "creator_id": "a@a.com",
      "description": "Get a list of allow-listed URLs",
      "export_key": "wf_zia_get_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621336617238,
      "name": "Example: ZIA: Get Allowlist",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_allowlist",
      "tags": [],
      "uuid": "88a31f09-9615-4a74-819d-3cb428d32840",
      "workflow_id": 29
    },
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "wf_zia_remove_url_from_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_url_from_blocklist\" isExecutable=\"true\" name=\"Example: ZIA: Remove URL From Blocklist\"\u003e\u003cdocumentation\u003eRemove  URL addresses from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_03fnd7q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_11a94r8\" name=\"ZIA: Remove From Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"eafc0196-f4bd-4654-8b7c-90e2a67ccac7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_url_from_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_blocklist\\\"\\nWF_NAME = \\\"Example: ZIA: Remove URL From Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        status = CONTENT.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to remove URLS \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; from blocklist by SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, status, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = row.blocklist_url\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_03fnd7q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q3bepe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_03fnd7q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_11a94r8\"/\u003e\u003cendEvent id=\"EndEvent_0lfafre\"\u003e\u003cincoming\u003eSequenceFlow_0q3bepe\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0q3bepe\" sourceRef=\"ServiceTask_11a94r8\" targetRef=\"EndEvent_0lfafre\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11a94r8\" id=\"ServiceTask_11a94r8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"229\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03fnd7q\" id=\"SequenceFlow_03fnd7q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"229\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lfafre\" id=\"EndEvent_0lfafre_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"370.9348958333333\" y=\"187.58246527777777\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"388.9348958333333\" y=\"226.58246527777777\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q3bepe\" id=\"SequenceFlow_0q3bepe_di\"\u003e\u003comgdi:waypoint x=\"329\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"365\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "creator_id": "a@a.com",
      "description": "Remove  URL addresses from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_url_from_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621525664375,
      "name": "Example: ZIA: Remove URL From Blocklist",
      "object_type": "zia_blocklist",
      "programmatic_name": "wf_zia_remove_url_from_blocklist",
      "tags": [],
      "uuid": "b39c8394-086b-4cca-a7aa-9e9e3b4539f8",
      "workflow_id": 27
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "wf_zia_remove_url_from_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_url_from_allowlist\" isExecutable=\"true\" name=\"Example: ZIA: Remove URL From Allowlist\"\u003e\u003cdocumentation\u003eRemove  URL  from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0bz8qi8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_05mv6rt\" name=\"ZIA: Remove From Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e642b020-f7b1-4e65-aa18-8f05e28ae07e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_url_from_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_allowlist\\\"\\nWF_NAME = \\\"Example: ZIA: Remove URL From Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        allowlist_urls = re.split(\\\"\\\\s+|,\\\", urls)\\n        updated_allowlist = CONTENT.whitelistUrls\\n        if not any(a in updated_allowlist for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls removed while attempting \\\" \\\\\\n                        u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist by SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    elif isinstance(content, dict):\\n        note_text += u\\\"Is a dict\\\"\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_allowlisturls = row.allowlist_url\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0bz8qi8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1b5xl77\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0bz8qi8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_05mv6rt\"/\u003e\u003cendEvent id=\"EndEvent_1c8874e\"\u003e\u003cincoming\u003eSequenceFlow_1b5xl77\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1b5xl77\" sourceRef=\"ServiceTask_05mv6rt\" targetRef=\"EndEvent_1c8874e\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_05mv6rt\" id=\"ServiceTask_05mv6rt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"221\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bz8qi8\" id=\"SequenceFlow_0bz8qi8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"221\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"209.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1c8874e\" id=\"EndEvent_1c8874e_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"365\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"383\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1b5xl77\" id=\"SequenceFlow_1b5xl77_di\"\u003e\u003comgdi:waypoint x=\"321\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"365\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"343\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "creator_id": "a@a.com",
      "description": "Remove  URL  from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_url_from_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621525686326,
      "name": "Example: ZIA: Remove URL From Allowlist",
      "object_type": "zia_allowlist",
      "programmatic_name": "wf_zia_remove_url_from_allowlist",
      "tags": [],
      "uuid": "78929f6c-da9f-4dc4-805e-829653f1993e",
      "workflow_id": 33
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "wf_zia_remove_from_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_from_allowlist\" isExecutable=\"true\" name=\"Example: ZIA: Remove From Allowlist\"\u003e\u003cdocumentation\u003eRemove artifact of type URLs or IP addresses from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1cgipae\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0v5bypi\" name=\"ZIA: Remove From Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e642b020-f7b1-4e65-aa18-8f05e28ae07e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_from_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_allowlist\\\"\\nWF_NAME = \\\"Example: ZIA: Remove From Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        allowlist_urls = re.split(\\\"\\\\s+|,\\\", urls)\\n        updated_allowlist_urls = CONTENT.whitelistUrls\\n        if not any(a in updated_allowlist_urls for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls removed while attempting \\\" \\\\\\n                        u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist by SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_allowlisturls = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1cgipae\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_043lg16\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1cgipae\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0v5bypi\"/\u003e\u003cendEvent id=\"EndEvent_1uqizf1\"\u003e\u003cincoming\u003eSequenceFlow_043lg16\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_043lg16\" sourceRef=\"ServiceTask_0v5bypi\" targetRef=\"EndEvent_1uqizf1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0v5bypi\" id=\"ServiceTask_0v5bypi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"221\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cgipae\" id=\"SequenceFlow_1cgipae_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"221\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"209.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1uqizf1\" id=\"EndEvent_1uqizf1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"358\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"376\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_043lg16\" id=\"SequenceFlow_043lg16_di\"\u003e\u003comgdi:waypoint x=\"321\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"358\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"339.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@a.com",
      "description": "Remove artifact of type URLs or IP addresses from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_from_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621595139726,
      "name": "Example: ZIA: Remove From Allowlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_remove_from_allowlist",
      "tags": [],
      "uuid": "af251397-fd63-4eb6-8d62-b524b0e9ee28",
      "workflow_id": 32
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_add_to_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_to_allowlist\" isExecutable=\"true\" name=\"Example: ZIA: Add To Allowlist\"\u003e\u003cdocumentation\u003eAdd artifact of type URLs or IP addresses URLs to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1arfy0q\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0msrva9\" name=\"ZIA: Add To Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1f0a1aaa-477e-4ed8-afa2-13cb049e47d7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_to_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_allowlist\\\"\\nWF_NAME = \\\"Example: ZIA: Add To Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        allowlist_urls = re.split(\\\"\\\\s+|,\\\", urls)\\n        updated_allowlist = CONTENT.whitelistUrls\\n        if all(a in updated_allowlist for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls added while attempting \\\" \\\\\\n                        u\\\"to add URLS \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_allowlisturls = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1arfy0q\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_164ld5w\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1arfy0q\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0msrva9\"/\u003e\u003cendEvent id=\"EndEvent_0nkhs0p\"\u003e\u003cincoming\u003eSequenceFlow_164ld5w\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_164ld5w\" sourceRef=\"ServiceTask_0msrva9\" targetRef=\"EndEvent_0nkhs0p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0msrva9\" id=\"ServiceTask_0msrva9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"231\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1arfy0q\" id=\"SequenceFlow_1arfy0q_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nkhs0p\" id=\"EndEvent_0nkhs0p_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"378\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"396\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_164ld5w\" id=\"SequenceFlow_164ld5w_di\"\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"368\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Add artifact of type URLs or IP addresses URLs to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_add_to_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621014562770,
      "name": "Example: ZIA: Add To Allowlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_add_to_allowlist",
      "tags": [],
      "uuid": "c021f589-a8ae-455b-93b6-a36b71e0d0ec",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 21,
        "workflow_id": "wf_zia_add_to_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_to_blocklist\" isExecutable=\"true\" name=\"Example: ZIA: Add To Blocklist\"\u003e\u003cdocumentation\u003eAdd  artifact of type URLs or IP addresses URLs to the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0qa2n4m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17951my\" name=\"ZIA: Add To Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d02e8977-6437-4093-8e19-422f3ba315f7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_to_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_blocklist\\\"\\nWF_NAME = \\\"Example: ZIA: Add To Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        status = CONTENT.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to add URLS \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qa2n4m\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1v6etyi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0qa2n4m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17951my\"/\u003e\u003cendEvent id=\"EndEvent_07u7fcb\"\u003e\u003cincoming\u003eSequenceFlow_1v6etyi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1v6etyi\" sourceRef=\"ServiceTask_17951my\" targetRef=\"EndEvent_07u7fcb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17951my\" id=\"ServiceTask_17951my_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"228\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qa2n4m\" id=\"SequenceFlow_0qa2n4m_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"228\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07u7fcb\" id=\"EndEvent_07u7fcb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"371\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"389\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1v6etyi\" id=\"SequenceFlow_1v6etyi_di\"\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"349.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 21,
      "creator_id": "a@a.com",
      "description": "Add  artifact of type URLs or IP addresses URLs to the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_add_to_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1620913136072,
      "name": "Example: ZIA: Add To Blocklist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_add_to_blocklist",
      "tags": [],
      "uuid": "487aa42c-5a9e-4cc6-81cc-fa5116b66428",
      "workflow_id": 4
    },
    {
      "actions": [],
      "content": {
        "version": 33,
        "workflow_id": "wf_zia_get_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_blocklist\" isExecutable=\"true\" name=\"Example: ZIA: Get Blocklist\"\u003e\u003cdocumentation\u003eGet a list of block-listed URLs\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0s9avfm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tf8yli\" name=\"ZIA: Get Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c24a73f2-6ef7-4b12-9b39-ad345ffe0b7f\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_blocklist\\\"\\nWF_NAME = \\\"Example: ZIA: Get Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    if CONTENT:\\n        blocklist_urls = CONTENT.blacklistUrls\\n        note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; blocklist URLS (s) returned for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(blocklist_urls), FN_NAME)\\n        for url in blocklist_urls:\\n            newrow = incident.addRow(\\\"zia_blocklist\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.blocklist_url = url\\n\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0s9avfm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_18cyza4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0s9avfm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tf8yli\"/\u003e\u003cendEvent id=\"EndEvent_0skpuhv\"\u003e\u003cincoming\u003eSequenceFlow_18cyza4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_18cyza4\" sourceRef=\"ServiceTask_1tf8yli\" targetRef=\"EndEvent_0skpuhv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tf8yli\" id=\"ServiceTask_1tf8yli_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0s9avfm\" id=\"SequenceFlow_0s9avfm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0skpuhv\" id=\"EndEvent_0skpuhv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18cyza4\" id=\"SequenceFlow_18cyza4_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 33,
      "creator_id": "a@a.com",
      "description": "Get a list of block-listed URLs",
      "export_key": "wf_zia_get_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1621247560926,
      "name": "Example: ZIA: Get Blocklist",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_blocklist",
      "tags": [],
      "uuid": "87dfa86f-ee6e-4cdb-a54d-116b5e8f82eb",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "wf_zia_remove_from_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_from_blocklist\" isExecutable=\"true\" name=\"Example: ZIA: Remove From Blocklist\"\u003e\u003cdocumentation\u003eRemove artifact of type URLs or IP addresses from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ve5ojq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ow3cn8\" name=\"ZIA: Remove From Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"eafc0196-f4bd-4654-8b7c-90e2a67ccac7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_from_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_blocklist\\\"\\nWF_NAME = \\\"Example: ZIA: Remove From Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        status = CONTENT.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to remove URLS \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; from blocklist by SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, status, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLS \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ve5ojq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z5p1br\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ve5ojq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ow3cn8\"/\u003e\u003cendEvent id=\"EndEvent_134lofm\"\u003e\u003cincoming\u003eSequenceFlow_0z5p1br\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0z5p1br\" sourceRef=\"ServiceTask_1ow3cn8\" targetRef=\"EndEvent_134lofm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ow3cn8\" id=\"ServiceTask_1ow3cn8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"234\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ve5ojq\" id=\"SequenceFlow_0ve5ojq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"234\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_134lofm\" id=\"EndEvent_134lofm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"366\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"384\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z5p1br\" id=\"SequenceFlow_0z5p1br_di\"\u003e\u003comgdi:waypoint x=\"334\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"350\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "creator_id": "a@a.com",
      "description": "Remove artifact of type URLs or IP addresses from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_from_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1620913187677,
      "name": "Example: ZIA: Remove From Blocklist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_remove_from_blocklist",
      "tags": [],
      "uuid": "c03200dc-3a09-4e54-b38e-047719d79814",
      "workflow_id": 26
    }
  ],
  "workspaces": []
}
