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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Add Artifact To Allowlist",
      "id": 103,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Add Artifact To Allowlist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac4df0a9-09f6-411a-8613-9e2be980d2e4",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_artifact_to_allowlist"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Add Artifact To Blocklist",
      "id": 104,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Add Artifact To Blocklist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f1e3550c-3d13-46ee-ba8b-1179b991ee34",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_artifact_to_blocklist"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Add Artifact To Customlist",
      "id": 105,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Add Artifact To Customlist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8b33456c-2ee1-41a7-ae2b-a198c1498654",
      "view_items": [
        {
          "content": "c92ca054-2751-4579-b0f9-5682ab358138",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_artifact_to_customlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Add Custom Category",
      "id": 106,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Add Custom Category",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1e34e038-c2f9-4956-bffd-0e88570a1e81",
      "view_items": [
        {
          "content": "a43d0fec-4081-4a05-8866-bde580cd8106",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "22b4d6a5-6acb-4126-af93-71184392d051",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c064411-c875-4675-8a79-bf025c297022",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_custom_category"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Add URLs To AllowList",
      "id": 107,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Add URLs To AllowList",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e8757948-2945-4c94-9a22-aeaee2b5293c",
      "view_items": [
        {
          "content": "8c064411-c875-4675-8a79-bf025c297022",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_urls_to_allowlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Add URLs To BlockList",
      "id": 108,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Add URLs To BlockList",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "49df2a90-9210-4dd5-b8c5-e6dbfd3948d0",
      "view_items": [
        {
          "content": "8c064411-c875-4675-8a79-bf025c297022",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_urls_to_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Add URLs To CustomList",
      "id": 109,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Add URLs To CustomList",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d8061df9-1465-4a1f-b1a5-7f80b419a765",
      "view_items": [
        {
          "content": "c92ca054-2751-4579-b0f9-5682ab358138",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c064411-c875-4675-8a79-bf025c297022",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_add_urls_to_customlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Get Allowlist",
      "id": 110,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Get Allowlist",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "861a4120-b643-4715-a06f-f9ea8db7bbbb",
      "view_items": [
        {
          "content": "62de6078-fd7a-4b19-8b95-4627e3193faf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_get_allowlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Get Blocklist",
      "id": 111,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Get Blocklist",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f758382d-0f15-471d-9a8e-68b87dc7b8ea",
      "view_items": [
        {
          "content": "62de6078-fd7a-4b19-8b95-4627e3193faf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_get_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Get Customlist",
      "id": 112,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Get Customlist",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a7bcae78-ead5-430e-abad-5368ecb74bbe",
      "view_items": [
        {
          "content": "35303301-4222-4a79-a252-08c1cb9a6bad",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "62de6078-fd7a-4b19-8b95-4627e3193faf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_get_customlist"
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
        }
      ],
      "enabled": true,
      "export_key": "ZIA: Get Sandbox Report",
      "id": 113,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Get Sandbox Report",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9e63f30e-71fb-47bf-b6b8-74a5bce667a0",
      "view_items": [
        {
          "content": "ce790b2a-2191-4f0f-bf9a-e479434b2b39",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_get_sandbox_report"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "ZIA: Get URL Categories",
      "id": 114,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Get URL Categories",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "87ae570d-4082-4f41-a9f0-1db6f259afad",
      "view_items": [
        {
          "content": "35303301-4222-4a79-a252-08c1cb9a6bad",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "62de6078-fd7a-4b19-8b95-4627e3193faf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0ec4b02c-611e-4466-b84b-766f00fe9440",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_get_url_categories"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Remove Artifact From Allowlist",
      "id": 115,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Remove Artifact From Allowlist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "717951da-de2a-4c4c-9c7a-9a976baa9eb8",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_artifact_from_allowlist"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Remove Artifact From Blocklist",
      "id": 116,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Remove Artifact From Blocklist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "15e06655-8c4d-4877-8745-b3f11bb2616f",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_artifact_from_blocklist"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: Remove Artifact From Customlist",
      "id": 117,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: Remove Artifact From Customlist",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6553ea58-0c13-41b1-83d5-31e97f307d4e",
      "view_items": [
        {
          "content": "c92ca054-2751-4579-b0f9-5682ab358138",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_artifact_from_customlist"
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
      "export_key": "ZIA: Remove From Allowlist",
      "id": 118,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Remove From Allowlist",
      "object_type": "zia_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e87a967c-d364-4046-97db-0abe89202405",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_from_allowlist"
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
      "export_key": "ZIA: Remove From Blocklist",
      "id": 119,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Remove From Blocklist",
      "object_type": "zia_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "93b1a3e9-24ec-4063-8a0f-c2ab6fbc5b83",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_from_blocklist"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "zia_customlists.cat_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "zia_customlists.configuredName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "ZIA: Remove From Customlist",
      "id": 120,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ZIA: Remove From Customlist",
      "object_type": "zia_customlists",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c21d54db-3c63-4e6c-8837-8be020332303",
      "view_items": [
        {
          "content": "69495cc1-492c-481f-a61d-1e3c8989a608",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_zia_remove_from_customlist"
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
          "value": "URI Path"
        },
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
      "export_key": "ZIA: URL Lookup",
      "id": 121,
      "logic_type": "any",
      "message_destinations": [],
      "name": "ZIA: URL Lookup",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e5d2615f-d35a-4c32-8ada-cc4fb81b8b10",
      "view_items": [],
      "workflows": [
        "wf_zia_url_lookup"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1623863866666,
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
      "export_key": "__function/zia_url_filter",
      "hide_notification": false,
      "id": 580,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_url_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\u003cREGEX\u003e|\u003cSTRING\u003e",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_url_filter",
      "tooltip": "Filter by URL. Can be a string or regular expression. e.g. host.ibm.com, ^host.*\u0027 or ^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$. Leaving the filter blank will return the full list.",
      "type_id": 11,
      "uuid": "894aa263-8ee8-4fdd-b559-01db32d1dd52",
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
      "export_key": "__function/zia_md5",
      "hide_notification": false,
      "id": 581,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_md5",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_md5",
      "tooltip": "MD5 hash value.",
      "type_id": 11,
      "uuid": "93153999-2154-4dbf-a99e-d5174ba8c278",
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
      "export_key": "__function/zia_custom_category",
      "hide_notification": false,
      "id": 582,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_custom_category",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_custom_category",
      "tooltip": "Indicates whether category is custom type. Valid values are \"true\", \"false\"\"",
      "type_id": 11,
      "uuid": "e10f6083-6c31-48a1-8d81-fb6162a81007",
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
      "export_key": "__function/zia_full_report",
      "hide_notification": false,
      "id": 583,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "zia_full_report",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_full_report",
      "tooltip": "Boolean True if a full report required",
      "type_id": 11,
      "uuid": "e422a86e-7b22-4b2c-b560-eb11a6ec1dc3",
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
      "export_key": "__function/zia_custom_only",
      "hide_notification": false,
      "id": 584,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_custom_only",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_custom_only",
      "tooltip": "Parameter to get only Custom Categories.Options \u0027true\u0027 or \u0027false\u0027",
      "type_id": 11,
      "uuid": "edcfe7e5-70ca-4cc9-8c5e-bee34f19f0dc",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/zia_activate",
      "hide_notification": false,
      "id": 585,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "zia_activate",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_activate",
      "tooltip": "Activate the configuration on ZIA.",
      "type_id": 11,
      "uuid": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
      "export_key": "__function/zia_keyword_filter",
      "hide_notification": false,
      "id": 586,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_keyword_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_keyword_filter",
      "tooltip": "Filter by keyword. Can be a string or regular expression. e.g. gambling or ^gambling.*\u0027 . Leaving the filter blank will return the full list.",
      "type_id": 11,
      "uuid": "121fe4e9-cfa2-4ff5-82ff-ad9d337d972f",
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
      "export_key": "__function/zia_keywords",
      "hide_notification": false,
      "id": 587,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_keywords",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_keywords",
      "tooltip": "Keyword string.",
      "type_id": 11,
      "uuid": "158e9fb8-776c-4d0c-a314-299be8e13116",
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
      "export_key": "__function/zia_blocklisturls",
      "hide_notification": false,
      "id": 588,
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
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_blocklisturls",
      "tooltip": "The URLs, URIs, DNS hostnames or IP addresses to add to the blocklist. See following for URL guidelines  https://help.zscaler.com/zia/url-format-guidelines",
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
      "export_key": "__function/zia_configured_name",
      "hide_notification": false,
      "id": 589,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_configured_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_configured_name",
      "tooltip": "Configured name of a custom URL category.",
      "type_id": 11,
      "uuid": "46a20c4a-ef04-4808-9a63-c06437445077",
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
      "id": 590,
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
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_allowlisturls",
      "tooltip": "The URLs, URIs, DNS hostnames or IP addresses to the allowlist. See following for URL guidelines  https://help.zscaler.com/zia/url-format-guidelines",
      "type_id": 11,
      "uuid": "49fed504-d765-4ace-8dff-9bbf356649cf",
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
      "export_key": "__function/zia_super_category",
      "hide_notification": false,
      "id": 591,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_super_category",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_super_category",
      "tooltip": "Super category of a custom URL category.",
      "type_id": 11,
      "uuid": "596a1620-0c8c-42e9-a1f3-5eee7c48f378",
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
      "export_key": "__function/zia_urls",
      "hide_notification": false,
      "id": 592,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_urls",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_urls",
      "tooltip": "Entries of type DNS hostname, IP Address, URL or URI. Wildcard is a \u0027.\u0027   Entries will be parsed to extract a format suitable for ZIA to add to a list. URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "type_id": 11,
      "uuid": "5f561591-9124-4524-8d8c-0737f7a2ec90",
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
      "export_key": "__function/zia_category_id",
      "hide_notification": false,
      "id": 593,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_category_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_category_id",
      "tooltip": "Category ID of a  URL category.",
      "type_id": 11,
      "uuid": "6dbdf189-eb7f-4043-a441-50a25a7871ff",
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
      "export_key": "__function/zia_name_filter",
      "hide_notification": false,
      "id": 594,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_name_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\u003cREGEX\u003e|\u003cSTRING\u003e",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "zia_name_filter",
      "tooltip": "Filter by category name. Can be a string or regular expression. e.g. \u0027Custom category\u0027, \u0027^CAT.*\u0027 or ^(List 1|LIST_2)$. Leaving the filter blank will return the full list. ",
      "type_id": 11,
      "uuid": "7393691c-ab20-4986-83c1-81420f80cab3",
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
      "export_key": "actioninvocation/zia_urls",
      "hide_notification": false,
      "id": 571,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "zia_urls",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "URLs",
      "tooltip": "Entries of type DNS hostname, IP Address, URL or URI. Wildcard is a \u0027.\u0027   Entries will be parsed to extract a format suitable for ZIA to add to a list. URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "type_id": 6,
      "uuid": "8c064411-c875-4675-8a79-bf025c297022",
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
      "export_key": "actioninvocation/zia_super_category",
      "hide_notification": false,
      "id": 572,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "zia_super_category",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Super category",
      "tooltip": "Super category of a custom URL category.",
      "type_id": 6,
      "uuid": "a43d0fec-4081-4a05-8866-bde580cd8106",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "BLOG",
          "properties": null,
          "uuid": "fec59731-4b52-4a6c-b57a-78204afb9c19",
          "value": 365
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "USER_DEFINED",
          "properties": null,
          "uuid": "1e203720-6e0c-4fd6-82dd-773cc64d513e",
          "value": 366
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ADULT_MATERIAL",
          "properties": null,
          "uuid": "24b552ce-2d6a-4e23-9b2e-cae4cc763241",
          "value": 367
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ADVANCED_SECURITY",
          "properties": null,
          "uuid": "fcd2747a-af95-448c-a302-00cb6fe6793b",
          "value": 368
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ANY",
          "properties": null,
          "uuid": "98374bb6-5e76-4390-99ed-fbaccc184492",
          "value": 369
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BUSINESS_AND_ECONOMY",
          "properties": null,
          "uuid": "e23cffdf-3893-49db-96d9-b232eb4cdc39",
          "value": 370
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CUSTOM_BP",
          "properties": null,
          "uuid": "34377ed2-1c93-4a4b-a274-a4673301d71d",
          "value": 371
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CUSTOM_BW",
          "properties": null,
          "uuid": "a7f14f2c-b009-48a8-94d2-8a84d9143732",
          "value": 372
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CUSTOM_SUPERCATEGORY",
          "properties": null,
          "uuid": "6ac3a662-f2a8-4cba-9951-0acd7811d69b",
          "value": 373
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DRUGS",
          "properties": null,
          "uuid": "6d6e79b7-304f-4d10-9bce-34f6bb287544",
          "value": 374
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "EDUCATION",
          "properties": null,
          "uuid": "6a9bfbeb-795f-4537-bda9-5ab8c8da50aa",
          "value": 375
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ENTERTAINMENT_AND_RECREATION",
          "properties": null,
          "uuid": "fc3c7e26-d529-42b6-8439-818101d23624",
          "value": 376
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GAMBLING",
          "properties": null,
          "uuid": "f7829f11-b174-4740-a45a-14e87577e021",
          "value": 377
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GAMES",
          "properties": null,
          "uuid": "6bf01a26-b6a0-441e-a8d2-9df8a16739a8",
          "value": 378
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GLOBAL_INT",
          "properties": null,
          "uuid": "c75babe4-990f-49c2-9d90-8dad656393ff",
          "value": 379
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GLOBAL_INT_BP",
          "properties": null,
          "uuid": "05101f93-4a75-4ae4-8df0-4655057e6cc0",
          "value": 380
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GLOBAL_INT_BW",
          "properties": null,
          "uuid": "fec263c9-6094-4651-b05d-d4d8c286926a",
          "value": 381
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "GOVERNMENT_AND_POLITICS",
          "properties": null,
          "uuid": "2a01d036-bf86-45b8-baa3-b02c50d157fe",
          "value": 382
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HEALTH",
          "properties": null,
          "uuid": "cca5434e-b255-4568-baa2-0fb4d48da673",
          "value": 383
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ILLEGAL_OR_QUESTIONABLE",
          "properties": null,
          "uuid": "a498d9cc-bf4e-4b0e-8aff-6183dce2c723",
          "value": 384
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "INFORMATION_TECHNOLOGY",
          "properties": null,
          "uuid": "641e1e3a-9d85-47b4-8672-f77c769b0006",
          "value": 385
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "INTERNET_COMMUNICATION",
          "properties": null,
          "uuid": "b0f1be74-0cf2-4748-9c27-988574ec581a",
          "value": 386
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "JOB_SEARCH",
          "properties": null,
          "uuid": "a2b9f678-85d2-4d10-8a70-ba06673f8265",
          "value": 387
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MILITANCY_HATE_AND_EXTREMISM",
          "properties": null,
          "uuid": "70dfc139-fc64-4b91-87b3-ac31a5bd6002",
          "value": 388
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MISCELLANEOUS",
          "properties": null,
          "uuid": "4af73458-70e3-47a7-97c3-76f68e806c31",
          "value": 389
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NEWS_AND_MEDIA",
          "properties": null,
          "uuid": "176d4907-ef7e-4656-9162-476c8a6d04a1",
          "value": 390
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NONE",
          "properties": null,
          "uuid": "2eba7419-6f98-4433-9f31-25b40f577b0f",
          "value": 391
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "OFFICE_365",
          "properties": null,
          "uuid": "421624ad-c1e0-4e96-891e-32bd3e6f8219",
          "value": 392
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RELIGION",
          "properties": null,
          "uuid": "c41f0e59-f09a-418b-bfeb-3b4c1927fb81",
          "value": 393
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SHOPPING_AND_AUCTIONS",
          "properties": null,
          "uuid": "2ec6936c-ceee-42c8-a9cb-7ef6b5243238",
          "value": 394
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SOCIAL_AND_FAMILY_ISSUES",
          "properties": null,
          "uuid": "79eb2d9a-5583-4cf8-bc0c-508f9be23f7f",
          "value": 395
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SOCIETY_AND_LIFESTYLE",
          "properties": null,
          "uuid": "a0dbc6f1-85cc-45ec-a581-10ffe2ace42c",
          "value": 396
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPECIAL_INTERESTS_SOCIAL_ORGANIZATIONS",
          "properties": null,
          "uuid": "04514ca9-8d5b-4c4a-ab59-3f2dc39f59c9",
          "value": 397
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SPORTS",
          "properties": null,
          "uuid": "471d1ade-f8ff-48cf-af79-c5017263095a",
          "value": 398
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TASTELESS",
          "properties": null,
          "uuid": "8a373f66-1bf9-4301-80a3-25e3956b11de",
          "value": 399
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TRAVEL",
          "properties": null,
          "uuid": "23cb284f-328a-4770-b2b5-6f21f7287dfe",
          "value": 400
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VEHICLES",
          "properties": null,
          "uuid": "c0f6522a-de7d-4a55-b508-c29b60c23fa2",
          "value": 401
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VIOLENCE",
          "properties": null,
          "uuid": "ce8f765a-a288-4c3e-b496-6e5ab2fc9d3e",
          "value": 402
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "WEAPONS_AND_BOMBS",
          "properties": null,
          "uuid": "786cc9cb-7db9-4a28-87b6-ea93a051e5e3",
          "value": 403
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SECURITY",
          "properties": null,
          "uuid": "ef8fda1a-0066-475f-8803-a0e679c02506",
          "value": 404
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
      "export_key": "actioninvocation/zia_configured_name",
      "hide_notification": false,
      "id": 573,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "zia_configured_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Configured name",
      "tooltip": "Custom category configured name. ",
      "type_id": 6,
      "uuid": "c92ca054-2751-4579-b0f9-5682ab358138",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "TEST_CAT_1",
          "properties": null,
          "uuid": "bceb16cc-bf51-4d88-a3b2-efc5e6b95551",
          "value": 405
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cEDIT THIS LIST\u003e",
          "properties": null,
          "uuid": "64ec262b-f188-4f2e-980b-845546771647",
          "value": 406
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
      "export_key": "actioninvocation/zia_report_type",
      "hide_notification": false,
      "id": 574,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "zia_report_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Report type",
      "tooltip": "",
      "type_id": 6,
      "uuid": "ce790b2a-2191-4f0f-bf9a-e479434b2b39",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "True",
          "properties": null,
          "uuid": "ab01981a-4b39-4dc4-ab3f-df2cc80a0b6a",
          "value": 407
        },
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "False",
          "properties": null,
          "uuid": "84eefb07-dc80-4bd2-8d28-8ee8574f29d6",
          "value": 408
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "SUMMARY",
          "properties": null,
          "uuid": "98415ead-5769-4993-9c7a-18a0732e723a",
          "value": 409
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FULL",
          "properties": null,
          "uuid": "718c363d-4f45-4461-8c40-aeab3051e139",
          "value": 410
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
      "export_key": "actioninvocation/zia_custom_only",
      "hide_notification": false,
      "id": 575,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "zia_custom_only",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Custom only",
      "tooltip": "Get information for custom categories only.",
      "type_id": 6,
      "uuid": "0ec4b02c-611e-4466-b84b-766f00fe9440",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "true",
          "properties": null,
          "uuid": "a176b965-7701-45b1-92c1-196badee23f4",
          "value": 411
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "false",
          "properties": null,
          "uuid": "7b043413-0408-4e94-a868-d8893c420c93",
          "value": 412
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
      "export_key": "actioninvocation/zia_configured_name_input",
      "hide_notification": false,
      "id": 576,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_configured_name_input",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Configured name",
      "tooltip": "Configured name of the custom category.  e.g. \u0027Custom blocklist\u0027, \u0027CUSTOM_ALLOWLIST\u0027 etc\u0027",
      "type_id": 6,
      "uuid": "22b4d6a5-6acb-4126-af93-71184392d051",
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
      "export_key": "actioninvocation/zia_name_filter",
      "hide_notification": false,
      "id": 577,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_name_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\u003cREGEX\u003e|\u003cSTRING\u003e",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Category name filter",
      "tooltip": "Filter by category name. Can be a string or regular expression. e.g. \u0027Custom category\u0027, \u0027^CAT.*\u0027 or ^(List 1|LIST_2)$. Leaving the filter blank will return the full list. ",
      "type_id": 6,
      "uuid": "35303301-4222-4a79-a252-08c1cb9a6bad",
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
      "export_key": "actioninvocation/zia_url_filter",
      "hide_notification": false,
      "id": 578,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "zia_url_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\u003cREGEX\u003e|\u003cSTRING\u003e",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "URL filter",
      "tooltip": "Filter by URL. Can be a string or regular expression. e.g. host.ibm.com, ^host.*\u0027 or ^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$. Leaving the filter blank will return the full list.",
      "type_id": 6,
      "uuid": "62de6078-fd7a-4b19-8b95-4627e3193faf",
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
      "export_key": "actioninvocation/zia_activate",
      "hide_notification": false,
      "id": 579,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "zia_activate",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "templates": [],
      "text": "Activate configuration",
      "tooltip": "Activate configuration changes.",
      "type_id": 6,
      "uuid": "69495cc1-492c-481f-a61d-1e3c8989a608",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "true",
          "properties": null,
          "uuid": "25d5867e-636d-4feb-8679-1b85f62a1664",
          "value": 413
        },
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "false",
          "properties": null,
          "uuid": "154896fb-eeac-4d0a-8868-62fe968116dd",
          "value": 414
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "True",
          "properties": null,
          "uuid": "8d1cc564-1faa-4e58-a9ba-d3cea57f76bc",
          "value": 415
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "False",
          "properties": null,
          "uuid": "52584a47-8cbe-46f7-8f1f-7e4342ab8e5e",
          "value": 416
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
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add URLs, DNS hostnames or IP addresses to the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add To Allowlist",
      "export_key": "funct_zia_add_to_allowlist",
      "id": 49,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775655909,
      "name": "funct_zia_add_to_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "1f0a1aaa-477e-4ed8-afa2-13cb049e47d7",
      "version": 1,
      "view_items": [
        {
          "content": "49fed504-d765-4ace-8dff-9bbf356649cf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Add Artifact To Allowlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_artifact_to_allowlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 89
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Add URLs To AllowList",
          "object_type": "incident",
          "programmatic_name": "wf_zia_add_urls_to_allowlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 78
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
        "content": "Add URLs, DNS hostnames or IP addresses to the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add To Blocklist",
      "export_key": "funct_zia_add_to_blocklist",
      "id": 50,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775655987,
      "name": "funct_zia_add_to_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "d02e8977-6437-4093-8e19-422f3ba315f7",
      "version": 1,
      "view_items": [
        {
          "content": "3a967529-342d-4803-b5f6-cc5a39568878",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Add Artifact To Blocklist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_artifact_to_blocklist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 84
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Add URLs To BlockList",
          "object_type": "incident",
          "programmatic_name": "wf_zia_add_urls_to_blocklist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
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
        "content": "Add URLs, DNS hostnames or IP addresses to a custom category. Artifacts of type URL will be parsed to extract format suitable for ZIA. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add To URL Category",
      "export_key": "funct_zia_add_to_url_category",
      "id": 51,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656077,
      "name": "funct_zia_add_to_url_category",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "73e8d2a4-79ca-4896-a022-c895de32762b",
      "version": 1,
      "view_items": [
        {
          "content": "5f561591-9124-4524-8d8c-0737f7a2ec90",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6dbdf189-eb7f-4043-a441-50a25a7871ff",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46a20c4a-ef04-4808-9a63-c06437445077",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Add Artifact To Customlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_artifact_to_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 91
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Add URLs To CustomList",
          "object_type": "incident",
          "programmatic_name": "wf_zia_add_urls_to_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
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
        "content": "Add a new custom URL category.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Add URL Category",
      "export_key": "funct_zia_add_url_category",
      "id": 52,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656164,
      "name": "funct_zia_add_url_category",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "197a1156-a58e-417f-9e60-71923a030c2c",
      "version": 1,
      "view_items": [
        {
          "content": "46a20c4a-ef04-4808-9a63-c06437445077",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e10f6083-6c31-48a1-8d81-fb6162a81007",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "596a1620-0c8c-42e9-a1f3-5eee7c48f378",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "158e9fb8-776c-4d0c-a314-299be8e13116",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5f561591-9124-4524-8d8c-0737f7a2ec90",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Add Custom Category",
          "object_type": "incident",
          "programmatic_name": "wf_zia_add_custom_category",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 86
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
        "content": "Gets a list of allow-listed URLs. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get Allowlist",
      "export_key": "funct_zia_get_allowlist",
      "id": 53,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656243,
      "name": "funct_zia_get_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "afef84ad-f288-4a0c-a8e1-7c22ffcf1261",
      "version": 1,
      "view_items": [
        {
          "content": "894aa263-8ee8-4fdd-b559-01db32d1dd52",
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
          "name": "ZIA: Get Allowlist",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_allowlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 83
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
        "content": "Get a list of black-listed URLs. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get Blocklist",
      "export_key": "funct_zia_get_blocklist",
      "id": 54,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656324,
      "name": "funct_zia_get_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "c24a73f2-6ef7-4b12-9b39-ad345ffe0b7f",
      "version": 1,
      "view_items": [
        {
          "content": "894aa263-8ee8-4fdd-b559-01db32d1dd52",
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
          "name": "ZIA: Get Blocklist",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_blocklist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 77
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
        "content": "Query an MD5 to see if it was run through the ZIA Sandbox.\nGet a full (i.e., complete) or summary detail report for a file that was analyzed.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get Sandbox Report",
      "export_key": "funct_zia_get_sandbox_report",
      "id": 55,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656405,
      "name": "funct_zia_get_sandbox_report",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "775a93c4-2eb2-41c1-938c-fcb10311b3d6",
      "version": 1,
      "view_items": [
        {
          "content": "93153999-2154-4dbf-a99e-d5174ba8c278",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e422a86e-7b22-4b2c-b560-eb11a6ec1dc3",
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
          "name": "ZIA: Get Sandbox Report",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_get_sandbox_report",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 88
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
        "content": "Get information about URL categories.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Get URL Categories",
      "export_key": "funct_zia_get_url_categories",
      "id": 56,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656475,
      "name": "funct_zia_get_url_categories",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "a50d525c-96cf-4006-9f1d-1dd6cd21c9f4",
      "version": 1,
      "view_items": [
        {
          "content": "edcfe7e5-70ca-4cc9-8c5e-bee34f19f0dc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6dbdf189-eb7f-4043-a441-50a25a7871ff",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "894aa263-8ee8-4fdd-b559-01db32d1dd52",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7393691c-ab20-4986-83c1-81420f80cab3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "121fe4e9-cfa2-4ff5-82ff-ad9d337d972f",
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
          "name": "ZIA: Add Artifact To Customlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_add_artifact_to_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 91
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Add URLs To CustomList",
          "object_type": "incident",
          "programmatic_name": "wf_zia_add_urls_to_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 94
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Get Customlist",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Get URL Categories.",
          "object_type": "incident",
          "programmatic_name": "wf_zia_get_url_categories",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 93
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Remove Artifact From Customlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_artifact_from_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
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
        "content": "Remove  URLs, DNS hostnames or IP addresses from the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Remove From Allowlist",
      "export_key": "funct_zia_remove_from_allowlist",
      "id": 57,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656557,
      "name": "funct_zia_remove_from_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
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
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Remove Artifact From Allowlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_artifact_from_allowlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 85
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Remove From Allowlist",
          "object_type": "zia_allowlist",
          "programmatic_name": "wf_zia_remove_from_allowlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 80
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
        "content": "Remove  URLs, DNS hostnames or IP addresses from the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA.  See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Remove From Blocklist",
      "export_key": "funct_zia_remove_from_blocklist",
      "id": 58,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656634,
      "name": "funct_zia_remove_from_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "eafc0196-f4bd-4654-8b7c-90e2a67ccac7",
      "version": 1,
      "view_items": [
        {
          "content": "3a967529-342d-4803-b5f6-cc5a39568878",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Remove Artifact From Blocklist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_artifact_from_blocklist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 87
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Remove From Blocklist",
          "object_type": "zia_blocklist",
          "programmatic_name": "wf_zia_remove_from_blocklist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 79
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
        "content": "Remove URLs, DNS hostnames or IP addresses  from a URL Category. Artifacts of type URL will be parsed to extract format suitable for ZIA. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: Remove From URL Category",
      "export_key": "funct_zia_remove_from_url_category",
      "id": 59,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656697,
      "name": "funct_zia_remove_from_url_category",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "83fb337f-b065-4e2f-9a07-705e33121c57",
      "version": 1,
      "view_items": [
        {
          "content": "5f561591-9124-4524-8d8c-0737f7a2ec90",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46a20c4a-ef04-4808-9a63-c06437445077",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6dbdf189-eb7f-4043-a441-50a25a7871ff",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f5bc624e-4149-4835-ab26-8266c54312bf",
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
          "name": "ZIA: Remove Artifact From Customlist",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_remove_artifact_from_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        },
        {
          "actions": [],
          "description": null,
          "name": "ZIA: Remove From Customlist",
          "object_type": "zia_customlists",
          "programmatic_name": "wf_zia_remove_from_customlist",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 90
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
        "content": "Look up the categorization of a URL or set of URLs, e.g., [\u0027abc.com\u0027, \u0027xyz.com\u0027].  See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
        "format": "text"
      },
      "destination_handle": "zia",
      "display_name": "ZIA: URL Lookup",
      "export_key": "funct_zia_url_lookup",
      "id": 60,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1623775656774,
      "name": "funct_zia_url_lookup",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "c4d74e5f-b75c-44cc-ae33-3e37a5c2e917",
      "version": 1,
      "view_items": [
        {
          "content": "5f561591-9124-4524-8d8c-0737f7a2ec90",
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
          "name": "ZIA: URL Lookup",
          "object_type": "artifact",
          "programmatic_name": "wf_zia_url_lookup",
          "tags": [
            {
              "tag_handle": "fn_zia",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 81
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 5,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1623863822102,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1623863822102,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "b4ace6e4-a5e0-4f3f-8d4a-6b13f3ba8e71"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "zia",
      "name": "zia",
      "programmatic_name": "zia",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
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
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_allowlist/allowlist_url",
          "hide_notification": false,
          "id": 434,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "allowlist_url",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Allowlist URL",
          "tooltip": "A URL which is on the allowlist",
          "type_id": 1000,
          "uuid": "f9b4cb08-86ff-4f39-a3af-d8992d8cc329",
          "values": [],
          "width": 339
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_allowlist/query_execution_date",
          "hide_notification": false,
          "id": 435,
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
          "tooltip": "Date and time when query was run.",
          "type_id": 1000,
          "uuid": "037eb7d8-1d26-440c-b814-69d89b44c2ed",
          "values": [],
          "width": 157
        },
        "query_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_allowlist/query_filter",
          "hide_notification": false,
          "id": 436,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_filter",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URL filter",
          "tooltip": "Filter, if any, used in query.",
          "type_id": 1000,
          "uuid": "58e361b5-4f2d-442a-a967-c94e7c9aa12e",
          "values": [],
          "width": 174
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
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
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
          "id": 437,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "blocklist_url",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Blocklist URL",
          "tooltip": "A URL which is on the blocklist.",
          "type_id": 1001,
          "uuid": "b227eee6-0fc0-4352-8975-53d7b1b393b7",
          "values": [],
          "width": 361
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
          "id": 438,
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
          "tooltip": "Date and time when query was run.",
          "type_id": 1001,
          "uuid": "f8a3ddba-bd77-4179-91ec-0d73b440ed63",
          "values": [],
          "width": 154
        },
        "query_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_blocklist/query_filter",
          "hide_notification": false,
          "id": 439,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "query_filter",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URL filter",
          "tooltip": "Filter, if any, used in query.",
          "type_id": 1001,
          "uuid": "0c8d95fe-1b9d-49e4-b23a-69f08144d958",
          "values": [],
          "width": 170
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
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "zia_blocklist",
      "uuid": "d2f1f7e6-5220-4e30-aed3-e1e0f0c99b83"
    },
    {
      "actions": [],
      "display_name": "Zscaler Internet Access - Custom lists",
      "export_key": "zia_customlists",
      "fields": {
        "cat_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/cat_id",
          "hide_notification": false,
          "id": 440,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cat_id",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category ID",
          "tooltip": "Category ID of custom list.",
          "type_id": 1002,
          "uuid": "58bae690-90b6-48ac-9fc3-ff82b35298dd",
          "values": [],
          "width": 167
        },
        "configuredName": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/configuredName",
          "hide_notification": false,
          "id": 441,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "configuredName",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category configured name",
          "tooltip": "configured name of the custom list.",
          "type_id": 1002,
          "uuid": "629f32a3-e679-427a-8d8d-4cc5fa3d670a",
          "values": [],
          "width": 153
        },
        "name_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/name_filter",
          "hide_notification": false,
          "id": 442,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "name_filter",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category name filter",
          "tooltip": "Configured name filter, if any, used in the query.",
          "type_id": 1002,
          "uuid": "bf5b3856-deae-431c-b9e5-4d92c9391b36",
          "values": [],
          "width": 98
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/query_execution_date",
          "hide_notification": false,
          "id": 443,
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
          "tooltip": "Date and time when query was run.",
          "type_id": 1002,
          "uuid": "ee640694-00bb-4e64-98a8-1072567804ba",
          "values": [],
          "width": 149
        },
        "url": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/url",
          "hide_notification": false,
          "id": 444,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "url",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URL",
          "tooltip": "A URL on the custom list.",
          "type_id": 1002,
          "uuid": "05d7e8f1-d744-4f1a-b12f-f075dbc58a9d",
          "values": [],
          "width": 295
        },
        "url_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_customlists/url_filter",
          "hide_notification": false,
          "id": 445,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "url_filter",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URL filter",
          "tooltip": "URL filter, if any, used in the query.",
          "type_id": 1002,
          "uuid": "f0fa99f7-bae2-4f3a-bc3f-f49406e9a66c",
          "values": [],
          "width": 108
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
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "zia_customlists",
      "uuid": "ae9da2db-3f49-4c68-a68f-ca3778704e52"
    },
    {
      "actions": [],
      "display_name": "Zscaler Internet Access - Sandbox Report Summary",
      "export_key": "zia_sandbox_report_summary",
      "fields": {
        "Category": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Category",
          "hide_notification": false,
          "id": 446,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Category",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Classification category",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "fab298f6-8b94-49a0-834d-3e2d8772c0a7",
          "values": [],
          "width": 104
        },
        "DetectedMalware": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/DetectedMalware",
          "hide_notification": false,
          "id": 447,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "DetectedMalware",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Detected malware",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "2bdc7b30-6690-4c18-a7ad-2892c0f909ed",
          "values": [],
          "width": 69
        },
        "DigitalCerificate": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/DigitalCerificate",
          "hide_notification": false,
          "id": 448,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "DigitalCerificate",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Digital certificate",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "c107641a-9c1c-489b-bd21-1552c749588f",
          "values": [],
          "width": 120
        },
        "FileSize": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/FileSize",
          "hide_notification": false,
          "id": 449,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "FileSize",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "File size",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "ed42cf5f-ced6-4371-b982-8a1d9db6f2a6",
          "values": [],
          "width": 30
        },
        "FileType": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/FileType",
          "hide_notification": false,
          "id": 450,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "FileType",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "File type",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "c8ffbbf0-07d4-4819-9f40-83f7ce16b4cf",
          "values": [],
          "width": 59
        },
        "Issuer": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Issuer",
          "hide_notification": false,
          "id": 451,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Issuer",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Issuer",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "efcb5370-a19a-4160-b43f-85ce9e54da56",
          "values": [],
          "width": 48
        },
        "MD5": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/MD5",
          "hide_notification": false,
          "id": 452,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "MD5",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "MD5",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "ce4e67a7-e554-4257-9618-6076ae0c28eb",
          "values": [],
          "width": 140
        },
        "RootCA": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/RootCA",
          "hide_notification": false,
          "id": 453,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "RootCA",
          "operation_perms": {},
          "operations": [],
          "order": 15,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "RootCA",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "00ac7383-1afb-4792-9d80-41f4884aaa7c",
          "values": [],
          "width": 56
        },
        "SHA1": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/SHA1",
          "hide_notification": false,
          "id": 454,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "SHA1",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "SHA1",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "cd7d0c76-8d9b-4cb0-8002-e8ffe1f48d09",
          "values": [],
          "width": 150
        },
        "SSDeep": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/SSDeep",
          "hide_notification": false,
          "id": 455,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "SSDeep",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "SSDeep",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "fbfa1920-0c8e-49a9-b0bc-a3251be2ea4c",
          "values": [],
          "width": 59
        },
        "Score": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Score",
          "hide_notification": false,
          "id": 456,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Score",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Score",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "f64620cb-13eb-4eee-8610-08c2618c224f",
          "values": [],
          "width": 43
        },
        "Sha256": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Sha256",
          "hide_notification": false,
          "id": 457,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Sha256",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "SHA256",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "26eed72a-67f2-4ea8-972d-adf15df3b422",
          "values": [],
          "width": 168
        },
        "Status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Status",
          "hide_notification": false,
          "id": 458,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Status",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report status",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "ab4e86d7-5a92-418c-96a1-625a22448ca5",
          "values": [],
          "width": 51
        },
        "Type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/Type",
          "hide_notification": false,
          "id": 459,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Type",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Classification type",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "6debe44b-c43f-4731-a04a-e616bf4fc993",
          "values": [],
          "width": 104
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/query_execution_date",
          "hide_notification": false,
          "id": 460,
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
          "type_id": 1003,
          "uuid": "fc17debd-1bbb-49d0-a71f-1ceddbddcdb3",
          "values": [],
          "width": 158
        },
        "report_Category": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_sandbox_report_summary/report_Category",
          "hide_notification": false,
          "id": 461,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "report_Category",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Report category",
          "tooltip": "",
          "type_id": 1003,
          "uuid": "e08b6d91-6cb8-47a1-a07b-b84a3d5c55fb",
          "values": [],
          "width": 68
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
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "zia_sandbox_report_summary",
      "uuid": "41c5ec9f-549b-4280-8e44-54fe47098cbe"
    },
    {
      "actions": [],
      "display_name": "Zscaler Internet Access - URL Categories",
      "export_key": "zia_url_categories",
      "fields": {
        "cat_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/cat_description",
          "hide_notification": false,
          "id": 462,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cat_description",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "32d5528b-af58-480e-a2ea-162da1ee1ead",
          "values": [],
          "width": 88
        },
        "cat_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/cat_id",
          "hide_notification": false,
          "id": 463,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "cat_id",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category ID",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "133bbe54-06ef-4c73-97c6-76a4af04f8e8",
          "values": [],
          "width": 84
        },
        "configuredName": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/configuredName",
          "hide_notification": false,
          "id": 464,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "configuredName",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Configured name",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "71b285f2-db92-4ce4-9e8c-03410a4c2013",
          "values": [],
          "width": 117
        },
        "customCategory": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/customCategory",
          "hide_notification": false,
          "id": 465,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "customCategory",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Custom category",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "6cce2020-d6d3-4f6d-b5d2-0633999789ea",
          "values": [],
          "width": 69
        },
        "customUrlsCount": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/customUrlsCount",
          "hide_notification": false,
          "id": 466,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "customUrlsCount",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Custom URLs count",
          "tooltip": "Total custom URL count before any results filtering.",
          "type_id": 1004,
          "uuid": "c102cf4f-02b5-495a-af00-689a3439f82a",
          "values": [],
          "width": 72
        },
        "editable": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/editable",
          "hide_notification": false,
          "id": 467,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "editable",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Editable",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "4e7c9909-f6b1-4283-a822-3fcc18baddcb",
          "values": [],
          "width": 63
        },
        "name_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/name_filter",
          "hide_notification": false,
          "id": 469,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "name_filter",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Category name filter",
          "tooltip": "Configured name filter, if any, used in the query.",
          "type_id": 1004,
          "uuid": "9e185e5f-3c68-49b2-8a66-54ce938b4bea",
          "values": [],
          "width": 68
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/query_execution_date",
          "hide_notification": false,
          "id": 470,
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
          "tooltip": "Date and time when query was run.",
          "type_id": 1004,
          "uuid": "2e8f71da-f58a-473b-b259-8224dbc3d3e7",
          "values": [],
          "width": 153
        },
        "type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/type",
          "hide_notification": false,
          "id": 472,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "0e1d4093-5a90-479d-914a-8815468adbec",
          "values": [],
          "width": 36
        },
        "url_filter": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/url_filter",
          "hide_notification": false,
          "id": 473,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "url_filter",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URL filter",
          "tooltip": "URL filter, if any, used in the query.",
          "type_id": 1004,
          "uuid": "b5d2f985-0374-41b4-879e-008f4cf0359c",
          "values": [],
          "width": 37
        },
        "urls": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "zia_url_categories/urls",
          "hide_notification": false,
          "id": 474,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "urls",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "URLs",
          "tooltip": "",
          "type_id": 1004,
          "uuid": "2ebd5d0d-7929-41cd-a69c-b24a8582e519",
          "values": [],
          "width": 273
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
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "zia_url_categories",
      "uuid": "958497b7-5414-4d23-b85d-b5a9d9e71016"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "wf_zia_remove_artifact_from_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_artifact_from_customlist\" isExecutable=\"true\" name=\"ZIA: Remove Artifact From Customlist\"\u003e\u003cdocumentation\u003eRemove artifact of type URL, URI , DNS hostname or IP address from a custom list. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from a custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15c70lp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_15uxgj3\" name=\"ZIA: Remove From URL Category\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"83fb337f-b065-4e2f-9a07-705e33121c57\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_artifact_from_customlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_url_category\\\"\\nWF_NAME = \\\"ZIA: Remove Artifact From Customlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    category_id = INPUTS.get(\\\"zia_category_id\\\")\\n    configured_name = INPUTS.get(\\\"zia_configured_name\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        customlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_customlist = response.get(\\\"urls\\\")\\n        if not any(a in updated_customlist for a in customlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist \\\"\\\\\\n                        u\\\"with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, category_id, configured_name, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all URLs were removed while attempting \\\"\\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; \\\"\\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, category_id, configured_name, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist of category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, category_id, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"content = workflow.properties.get_categories_results.content\\nconfigured_name = rule.properties.zia_configured_name\\ncats = content.get(\\\"categories\\\")\\ninputs.zia_category_id = [c[\\\"id\\\"] for c in cats if configured_name == c[\\\"configuredName\\\"]][0]\\ninputs.zia_urls = artifact.value\\ninputs.zia_configured_name = rule.properties.zia_configured_name\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0abntm1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hmsiex\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0swngga\"\u003e\u003cincoming\u003eSequenceFlow_0hmsiex\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0hmsiex\" sourceRef=\"ServiceTask_15uxgj3\" targetRef=\"EndEvent_0swngga\"/\u003e\u003cserviceTask id=\"ServiceTask_1kevxl3\" name=\"ZIA: Get URL Categories\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a50d525c-96cf-4006-9f1d-1dd6cd21c9f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_customlist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_url_categories\\\"\\nWF_NAME = \\\"ZIA: Remove Artifact From Customlist@\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\n\\n# Processing\\ndef main():\\n    catname_exists = False\\n    note_text = u\u0027\u0027\\n    name_filter = INPUTS.get(\\\"zia_name_filter\\\")\\n    if CONTENT:\\n        cats = CONTENT.get(\\\"categories\\\")\\n        if any(name_filter == c[\\\"configuredName\\\"] for c in cats):\\n            catname_exists = True\\n    if catname_exists:\\n        workflow.addProperty(\\\"catname_exists\\\", {})\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The category nmae  \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was not found \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, name_filter, FN_NAME)\\n        incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_categories_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15c70lp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13kan0u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15c70lp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kevxl3\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0w17j9r\"\u003e\u003cincoming\u003eSequenceFlow_13kan0u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0abntm1\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_13c07q3\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_13kan0u\" sourceRef=\"ServiceTask_1kevxl3\" targetRef=\"ExclusiveGateway_0w17j9r\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0abntm1\" name=\"Category name exists\" sourceRef=\"ExclusiveGateway_0w17j9r\" targetRef=\"ServiceTask_15uxgj3\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cendEvent id=\"EndEvent_0wa862s\"\u003e\u003cincoming\u003eSequenceFlow_13c07q3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13c07q3\" name=\"Category name does not exist\" sourceRef=\"ExclusiveGateway_0w17j9r\" targetRef=\"EndEvent_0wa862s\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1qvngl2\"\u003e\u003ctext\u003eGet category id for the configured name if it exists.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0v7vxu6\" sourceRef=\"ServiceTask_1kevxl3\" targetRef=\"TextAnnotation_1qvngl2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_15uxgj3\" id=\"ServiceTask_15uxgj3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"614\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0swngga\" id=\"EndEvent_0swngga_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"775\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"748\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hmsiex\" id=\"SequenceFlow_0hmsiex_di\"\u003e\u003comgdi:waypoint x=\"714\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"775\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"699.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kevxl3\" id=\"ServiceTask_1kevxl3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"243\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15c70lp\" id=\"SequenceFlow_15c70lp_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0w17j9r\" id=\"ExclusiveGateway_0w17j9r_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"413\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"438\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13kan0u\" id=\"SequenceFlow_13kan0u_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"413\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"378\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0abntm1\" id=\"SequenceFlow_0abntm1_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"80\" x=\"499\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wa862s\" id=\"EndEvent_0wa862s_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"420\" y=\"346\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"438\" y=\"385\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13c07q3\" id=\"SequenceFlow_13c07q3_di\"\u003e\u003comgdi:waypoint x=\"438\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"438\" xsi:type=\"omgdc:Point\" y=\"346\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"80\" x=\"413\" y=\"282\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1qvngl2\" id=\"TextAnnotation_1qvngl2_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"136\" x=\"225\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0v7vxu6\" id=\"Association_0v7vxu6_di\"\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"293\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@a.com",
      "description": "Remove artifact of type URL, URI , DNS hostname or IP address from a custom list. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from a custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_remove_artifact_from_customlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623859927938,
      "name": "ZIA: Remove Artifact From Customlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_remove_artifact_from_customlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "58160cbf-f4f5-4433-836c-c9949d53cdf8",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_add_urls_to_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_urls_to_blocklist\" isExecutable=\"true\" name=\"ZIA: Add URLs To BlockList\"\u003e\u003cdocumentation\u003eAdd URLS to the blocklist. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the blocklist.  See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1p44jzc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0anwat3\" name=\"ZIA: Add To Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d02e8977-6437-4093-8e19-422f3ba315f7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA -wf_zia_add_urls_to_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_blocklist\\\"\\nWF_NAME = \\\"ZIA: Add URLs To BlockList\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        status = response.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_activate = rule.properties.zia_activate\\ninputs.zia_blocklisturls = rule.properties.zia_urls.content\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1p44jzc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1pm93w4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1p44jzc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0anwat3\"/\u003e\u003cendEvent id=\"EndEvent_005xi4k\"\u003e\u003cincoming\u003eSequenceFlow_1pm93w4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pm93w4\" sourceRef=\"ServiceTask_0anwat3\" targetRef=\"EndEvent_005xi4k\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0anwat3\" id=\"ServiceTask_0anwat3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"229\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1p44jzc\" id=\"SequenceFlow_1p44jzc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"229\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_005xi4k\" id=\"EndEvent_005xi4k_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"370\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"388\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pm93w4\" id=\"SequenceFlow_1pm93w4_di\"\u003e\u003comgdi:waypoint x=\"329\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"370\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"349.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Add URLS to the blocklist. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the blocklist.  See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_add_urls_to_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775658502,
      "name": "ZIA: Add URLs To BlockList",
      "object_type": "incident",
      "programmatic_name": "wf_zia_add_urls_to_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "761782ae-0adc-4946-8a85-f2f8a8b434ec",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_get_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_blocklist\" isExecutable=\"true\" name=\"ZIA: Get Blocklist\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get a list of block-listed URLs. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The data table \"Zscaler Internet Access - Blocklist\" will be updated if the result \u003c 50, otherwise the result will be added to a note.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0s9avfm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tf8yli\" name=\"ZIA: Get Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c24a73f2-6ef7-4b12-9b39-ad345ffe0b7f\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_blocklist\\\"\\nWF_NAME = \\\"ZIA: Get Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    url_filter = INPUTS.get(\\\"zia_url_filter\\\")\\n    if CONTENT:\\n        blocklist_urls = CONTENT.blacklistUrls\\n        url_counts = CONTENT.url_counts\\n        note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; blocklist URLS(s) out of a total of \\\"\\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; using URL filter \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; returned for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, url_counts[\\\"filtered\\\"], url_counts[\\\"total\\\"], url_filter, FN_NAME)\\n        if blocklist_urls:\\n            if url_counts[\\\"filtered\\\"] \u0026lt;= 50:\\n                note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Zscaler Internet Access - Blocklist\\\")\\n                for url in blocklist_urls:\\n                    newrow = incident.addRow(\\\"zia_blocklist\\\")\\n                    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                    newrow.blocklist_url = url\\n                    newrow.query_filter = url_filter\\n            else:\\n                note_text += \\\"\u0026lt;br\u0026gt;Blocklisted URLS: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\".format(\\\", \\\".join(blocklist_urls))\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results using URL filter \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\"\\\\\\n                     u\\\"returned for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, url_filter, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ZIA - wf_zia_get_blocklist pre processing script ##\\nimport re\\n\\nURL_FILTER = rule.properties.zia_url_filter\\n\\ndef is_regex(regex_str):\\n    \\\"\\\"\\\"\\\"Test if sting is a correctly formed regular expression.\\n\\n    :param regex_str: Regular expression string.\\n    :return: Boolean.\\n    \\\"\\\"\\\"\\n    try:\\n        re.compile(regex_str)\\n        return True\\n    except (re.error, TypeError):\\n        return False\\n\\n\\ndef main():\\n    # Test filter to ensure it is a valid regular expressions.\\n    if URL_FILTER and not is_regex(URL_FILTER):\\n        raise ValueError(\\\"The query filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(URL_FILTER)))\\n\\n    inputs.zia_url_filter = rule.properties.zia_url_filter\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0s9avfm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_18cyza4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0s9avfm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tf8yli\"/\u003e\u003cendEvent id=\"EndEvent_0skpuhv\"\u003e\u003cincoming\u003eSequenceFlow_18cyza4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_18cyza4\" sourceRef=\"ServiceTask_1tf8yli\" targetRef=\"EndEvent_0skpuhv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tf8yli\" id=\"ServiceTask_1tf8yli_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0s9avfm\" id=\"SequenceFlow_0s9avfm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0skpuhv\" id=\"EndEvent_0skpuhv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18cyza4\" id=\"SequenceFlow_18cyza4_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Get a list of block-listed URLs. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The data table \"Zscaler Internet Access - Blocklist\" will be updated if the result \u003c 50, otherwise the result will be added to a note.",
      "export_key": "wf_zia_get_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775657243,
      "name": "ZIA: Get Blocklist",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "87dfa86f-ee6e-4cdb-a54d-116b5e8f82eb",
      "workflow_id": 77
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_url_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_url_lookup\" isExecutable=\"true\" name=\"ZIA: URL Lookup\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Look up the categorization of an artifact of type URL or IP Address e.g., [\u0027abc.com\u0027, \u0027xyz.com\u0027]]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0bibnqz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1trkalw\" name=\"ZIA: URL Lookup\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c4d74e5f-b75c-44cc-ae33-3e37a5c2e917\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_url_lookup post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_url_lookup\\\"\\nWF_NAME = \\\"Example: ZIA: URL Lookup\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    if CONTENT:\\n        note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Results (s) returned for \\\" \\\\\\n                        u\\\"URL \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), urls, FN_NAME)\\n        note_text += u\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt;\\\".format(CONTENT)\\n\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_urls = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0bibnqz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10wfpe9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0bibnqz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1trkalw\"/\u003e\u003cendEvent id=\"EndEvent_1oq0v7l\"\u003e\u003cincoming\u003eSequenceFlow_10wfpe9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_10wfpe9\" sourceRef=\"ServiceTask_1trkalw\" targetRef=\"EndEvent_1oq0v7l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1trkalw\" id=\"ServiceTask_1trkalw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bibnqz\" id=\"SequenceFlow_0bibnqz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1oq0v7l\" id=\"EndEvent_1oq0v7l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"361\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"379\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10wfpe9\" id=\"SequenceFlow_10wfpe9_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"361\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"348.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Look up the categorization of an artifact of type URL or IP Address e.g., [\u0027abc.com\u0027, \u0027xyz.com\u0027]",
      "export_key": "wf_zia_url_lookup",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775658245,
      "name": "ZIA: URL Lookup",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_url_lookup",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "e9a60225-0990-4af3-bbd3-4981d24bf417",
      "workflow_id": 81
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_remove_artifact_from_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_artifact_from_blocklist\" isExecutable=\"true\" name=\"ZIA: Remove Artifact From Blocklist\"\u003e\u003cdocumentation\u003eRemove artifact of type URL, URI , DNS hostname or IP address from the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rp90ut\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0kcy4vx\" name=\"ZIA: Remove From Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"eafc0196-f4bd-4654-8b7c-90e2a67ccac7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_artifact_from_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_blocklist\\\"\\nWF_NAME = \\\"ZIA: Remove Artifact From Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        status = response.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; from blocklist by SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, status, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = artifact.value\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rp90ut\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0i9mxjf\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0rp90ut\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0kcy4vx\"/\u003e\u003cendEvent id=\"EndEvent_00a2ggx\"\u003e\u003cincoming\u003eSequenceFlow_0i9mxjf\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0i9mxjf\" sourceRef=\"ServiceTask_0kcy4vx\" targetRef=\"EndEvent_00a2ggx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kcy4vx\" id=\"ServiceTask_0kcy4vx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"225\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rp90ut\" id=\"SequenceFlow_0rp90ut_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"225\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"211.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_00a2ggx\" id=\"EndEvent_00a2ggx_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"347\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"365\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0i9mxjf\" id=\"SequenceFlow_0i9mxjf_di\"\u003e\u003comgdi:waypoint x=\"325\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"336\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Remove artifact of type URL, URI , DNS hostname or IP address from the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_remove_artifact_from_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775659719,
      "name": "ZIA: Remove Artifact From Blocklist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_remove_artifact_from_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "51b314d7-65a7-47d7-8f9b-6f1037218251",
      "workflow_id": 87
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "wf_zia_add_artifact_to_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_artifact_to_allowlist\" isExecutable=\"true\" name=\"ZIA: Add Artifact To Allowlist\"\u003e\u003cdocumentation\u003eAdd artifact of type URL, URI , DNS hostname or IP address to the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_04n57x1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xikvmi\" name=\"ZIA: Add To Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1f0a1aaa-477e-4ed8-afa2-13cb049e47d7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - zia_add_artifact_to_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_allowlist\\\"\\nWF_NAME = \\\"ZIA: Add Artifact To Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        allowlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_allowlist = response.get(\\\"whitelistUrls\\\")\\n        if all(a in updated_allowlist for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        \\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all URLss added while attempting \\\" \\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.zia_allowlisturls = artifact.value\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_04n57x1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ov0tce\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_04n57x1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xikvmi\"/\u003e\u003cendEvent id=\"EndEvent_1gsxe6a\"\u003e\u003cincoming\u003eSequenceFlow_1ov0tce\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ov0tce\" sourceRef=\"ServiceTask_0xikvmi\" targetRef=\"EndEvent_1gsxe6a\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xikvmi\" id=\"ServiceTask_0xikvmi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04n57x1\" id=\"SequenceFlow_04n57x1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1gsxe6a\" id=\"EndEvent_1gsxe6a_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"366\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"384\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ov0tce\" id=\"SequenceFlow_1ov0tce_di\"\u003e\u003comgdi:waypoint x=\"338\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"352\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@a.com",
      "description": "Add artifact of type URL, URI , DNS hostname or IP address to the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_add_artifact_to_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623834849526,
      "name": "ZIA: Add Artifact To Allowlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_add_artifact_to_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "309d0766-cf12-4a16-ad7a-35fcb59b7df6",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_add_urls_to_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_urls_to_customlist\" isExecutable=\"true\" name=\"ZIA: Add URLs To CustomList\"\u003e\u003cdocumentation\u003eAdd URLS to a custom list. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0clckk6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ypki88\" name=\"ZIA: Add To URL Category\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"73e8d2a4-79ca-4896-a022-c895de32762b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_urls_to_customlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_url_category\\\"\\nWF_NAME = \\\"ZIA: Add URLs To CustomList\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    category_id = INPUTS.get(\\\"zia_category_id\\\")\\n    configured_name = INPUTS.get(\\\"zia_configured_name\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        customlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_customlist = response.get(\\\"urls\\\")\\n        if all(a in updated_customlist for a in customlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to customlist \\\"\\\\\\n                        u\\\"with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                        .format(WF_NAME, urls, category_id, configured_name, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls added while attempting \\\"\\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to customlist with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; \\\"\\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, category_id,  FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\"\\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to to customlist of category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, category_id,  FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"content = workflow.properties.get_categories_results.content\\nconfigured_name = rule.properties.zia_configured_name\\ncats = content.get(\\\"categories\\\")\\ninputs.zia_category_id = [c[\\\"id\\\"] for c in cats if configured_name == c[\\\"configuredName\\\"]][0]\\ninputs.zia_configured_name = configured_name\\ninputs.zia_urls = rule.properties.zia_urls.content\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_url_categories_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1uwi5b8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0dxp22q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1xp8ibg\"\u003e\u003cincoming\u003eSequenceFlow_0dxp22q\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0dxp22q\" sourceRef=\"ServiceTask_0ypki88\" targetRef=\"EndEvent_1xp8ibg\"/\u003e\u003cserviceTask id=\"ServiceTask_1okue8v\" name=\"ZIA: Get URL Categories\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a50d525c-96cf-4006-9f1d-1dd6cd21c9f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_customlist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_url_categories\\\"\\nWF_NAME = \\\"ZIA: Add URLs To CustomList\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\n\\n# Processing\\ndef main():\\n    catname_exists = False\\n    note_text = u\u0027\u0027\\n    name_filter = INPUTS.get(\\\"zia_name_filter\\\")\\n    if CONTENT:\\n        cats = CONTENT.get(\\\"categories\\\")\\n        if any(name_filter == c[\\\"configuredName\\\"] for c in cats):\\n            catname_exists = True\\n    if catname_exists:\\n        workflow.addProperty(\\\"catname_exists\\\", {})\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The category nmae  \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was not found \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, name_filter, FN_NAME)\\n        incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_categories_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0clckk6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1f23yzu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0clckk6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1okue8v\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_09xual6\"\u003e\u003cincoming\u003eSequenceFlow_1f23yzu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17fe4bw\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1uwi5b8\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1f23yzu\" sourceRef=\"ServiceTask_1okue8v\" targetRef=\"ExclusiveGateway_09xual6\"/\u003e\u003cendEvent id=\"EndEvent_1327axc\"\u003e\u003cincoming\u003eSequenceFlow_17fe4bw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17fe4bw\" name=\"Category name does not exist\" sourceRef=\"ExclusiveGateway_09xual6\" targetRef=\"EndEvent_1327axc\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1uwi5b8\" name=\"Category name exists\" sourceRef=\"ExclusiveGateway_09xual6\" targetRef=\"ServiceTask_0ypki88\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rf1xw8\"\u003e\u003ctext\u003e\u003c![CDATA[Get category id for the configured name if it exists.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h67t0q\" sourceRef=\"ServiceTask_1okue8v\" targetRef=\"TextAnnotation_1rf1xw8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ypki88\" id=\"ServiceTask_0ypki88_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"516\" y=\"161\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1xp8ibg\" id=\"EndEvent_1xp8ibg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"666\" y=\"183\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"639\" y=\"222\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dxp22q\" id=\"SequenceFlow_0dxp22q_di\"\u003e\u003comgdi:waypoint x=\"616\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"640\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"640\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"666\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"610\" y=\"194.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1okue8v\" id=\"ServiceTask_1okue8v_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"226\" y=\"161\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0clckk6\" id=\"SequenceFlow_0clckk6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"212\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"212\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"226\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"182\" y=\"197\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_09xual6\" id=\"ExclusiveGateway_09xual6_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"360\" y=\"176\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"340\" y=\"229\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f23yzu\" id=\"SequenceFlow_1f23yzu_di\"\u003e\u003comgdi:waypoint x=\"326\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"298\" y=\"179.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1327axc\" id=\"EndEvent_1327axc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"367\" y=\"318\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"340\" y=\"357\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17fe4bw\" id=\"SequenceFlow_17fe4bw_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"226\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"318\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"80\" x=\"360\" y=\"264\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uwi5b8\" id=\"SequenceFlow_1uwi5b8_di\"\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003comgdi:waypoint x=\"516\" xsi:type=\"omgdc:Point\" y=\"201\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"80\" x=\"404\" y=\"179\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rf1xw8\" id=\"TextAnnotation_1rf1xw8_di\"\u003e\u003comgdc:Bounds height=\"41\" width=\"133\" x=\"209\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h67t0q\" id=\"Association_0h67t0q_di\"\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"161\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"90\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Add URLS to a custom list. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_add_urls_to_customlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623834744259,
      "name": "ZIA: Add URLs To CustomList",
      "object_type": "incident",
      "programmatic_name": "wf_zia_add_urls_to_customlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "5d5b5feb-048d-4f19-a9c5-c4419afba3d3",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_get_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_customlist\" isExecutable=\"true\" name=\"ZIA: Get Customlist\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get a list of URLs on a custom list. The result can be filtered by URL and Custom list name using a regex or string. The filters are case-insensitive. The data table \"Zscaler Internet Access - Custom lists\" will be updated for each list if the result \u003c 50, otherwise the result will be added to a note.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bkbuxi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13g8k04\" name=\"ZIA: Get URL Categories\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a50d525c-96cf-4006-9f1d-1dd6cd21c9f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_customlist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_url_categories\\\"\\nWF_NAME = \\\"ZIA: Get Customlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\nDATA_TBL_FIELDS = [\\\"cat_id\\\", \\\"configuredName\\\", \\\"url\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    url_filter = INPUTS.get(\\\"zia_url_filter\\\")\\n    if CONTENT:\\n        categories = CONTENT.get(\\\"categories\\\")\\n        cat_counts = CONTENT.get(\\\"category_counts\\\")\\n        name_filter = INPUTS.get(\\\"zia_name_filter\\\")\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Custom lists out of a total of \\\"\\\\\\n                     u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; using category name filter \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; and URL filter \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; returned for SOAR \\\"\\\\\\n                     u\\\"function \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, cat_counts[\\\"filtered\\\"], cat_counts[\\\"total\\\"], name_filter, url_filter, FN_NAME)\\n        for cat in categories:\\n            url_counts = cat.get(\\\"url_counts\\\")\\n            cat_id = cat.get(\\\"id\\\")\\n            configured_name = cat.get(\\\"configuredName\\\")\\n            customlist_urls = cat.get(\\\"urls\\\")\\n            note_text += u\\\"\u0026lt;br\u0026gt;There were \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; URLS(s) out of a total of \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned using URL filter \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\"\\\\\\n                         u\\\"for Custom list \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; \\\"\\\\\\n            .format(url_counts[\\\"filtered\\\"], url_counts[\\\"total\\\"], url_filter, cat_id, configured_name)\\n            if customlist_urls:\\n                if url_counts[\\\"filtered\\\"] \u0026lt;= 50:\\n                    note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Zscaler Internet Access - Custom lists\\\")\\n                    for url in customlist_urls:\\n                        newrow = incident.addRow(\\\"zia_customlists\\\")\\n                        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                        newrow.cat_id = cat_id\\n                        newrow.configuredName = configured_name\\n                        newrow.url = url\\n                        newrow.url_filter = url_filter\\n                        newrow.name_filter = name_filter\\n                else:\\n                    note_text += \\\"\u0026lt;br\u0026gt;Custom list URLS for Category ID \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; : \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;\\\".format(\\\", \\\".join(customlist_urls))\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned using configured name filter \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\"\\\\\\n                     u\\\"and URL filter \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, url_filter, name_filter, url_filter, FN_NAME)\\n    \\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ZIA - wf_zia_get_customlist pre processing script ##\\ninputs.zia_custom_only = \\\"true\\\"\\nimport re\\n\\nURL_FILTER = rule.properties.zia_url_filter\\nNAME_FILTER = rule.properties.zia_name_filter\\n\\ndef is_regex(regex_str):\\n    \\\"\\\"\\\"\\\"Test if sting is a correctly formed regular expression.\\n\\n    :param regex_str: Regular expression string.\\n    :return: Boolean.\\n    \\\"\\\"\\\"\\n    try:\\n        re.compile(regex_str)\\n        return True\\n    except (re.error, TypeError):\\n        return False\\n\\n\\ndef main():\\n    # Test filters to ensure they are valid regular expressions.\\n    for query_filter in [URL_FILTER, NAME_FILTER]:\\n        if query_filter and not is_regex(query_filter):\\n            raise ValueError(\\\"The filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(repr(query_filter))))\\n    \\n    inputs.zia_url_filter = URL_FILTER\\n    inputs.zia_name_filter = NAME_FILTER\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bkbuxi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13jy8qo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bkbuxi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13g8k04\"/\u003e\u003cendEvent id=\"EndEvent_0fxdk6v\"\u003e\u003cincoming\u003eSequenceFlow_13jy8qo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13jy8qo\" sourceRef=\"ServiceTask_13g8k04\" targetRef=\"EndEvent_0fxdk6v\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13g8k04\" id=\"ServiceTask_13g8k04_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bkbuxi\" id=\"SequenceFlow_1bkbuxi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fxdk6v\" id=\"EndEvent_0fxdk6v_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"383\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13jy8qo\" id=\"SequenceFlow_13jy8qo_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"359.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Get a list of URLs on a custom list. The result can be filtered by URL and Custom list name using a regex or string. The filters are case-insensitive. The data table \"Zscaler Internet Access - Custom lists\" will be updated for each list if the result \u003c 50, otherwise the result will be added to a note.",
      "export_key": "wf_zia_get_customlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775661706,
      "name": "ZIA: Get Customlist",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_customlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "28172655-1e5b-407d-ba19-3b6e4e930c6b",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "wf_zia_remove_from_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_from_customlist\" isExecutable=\"true\" name=\"ZIA: Remove From Customlist\"\u003e\u003cdocumentation\u003eRemove  URL from a custom list. URLs will be parsed to extract format suitable for ZIA which will be removed from a custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0k4wj56\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08qihbu\" name=\"ZIA: Remove From URL Category\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"83fb337f-b065-4e2f-9a07-705e33121c57\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_from_customlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_url_category\\\"\\nWF_NAME = \\\"ZIA: Remove From Customlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    category_id = INPUTS.get(\\\"zia_category_id\\\")\\n    configured_name = INPUTS.get(\\\"zia_configured_name\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        customlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_customlist = response.get(\\\"urls\\\")\\n        if not any(a in updated_customlist for a in customlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist \\\"\\\\\\n                        u\\\"with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                        .format(WF_NAME, urls, category_id, configured_name, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls removed while attempting \\\"\\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; \\\"\\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, category_id,  FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from customlist of category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, category_id, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_urls = row.url\\ninputs.zia_category_id = row.cat_id\\ninputs.zia_configured_name = row.configuredName\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0k4wj56\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gvxwo3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0k4wj56\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08qihbu\"/\u003e\u003cendEvent id=\"EndEvent_140f49t\"\u003e\u003cincoming\u003eSequenceFlow_1gvxwo3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1gvxwo3\" sourceRef=\"ServiceTask_08qihbu\" targetRef=\"EndEvent_140f49t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08qihbu\" id=\"ServiceTask_08qihbu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"237\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0k4wj56\" id=\"SequenceFlow_0k4wj56_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_140f49t\" id=\"EndEvent_140f49t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"357\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"375\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gvxwo3\" id=\"SequenceFlow_1gvxwo3_di\"\u003e\u003comgdi:waypoint x=\"337\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"347\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@a.com",
      "description": "Remove  URL from a custom list. URLs will be parsed to extract format suitable for ZIA which will be removed from a custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_from_customlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623859778340,
      "name": "ZIA: Remove From Customlist",
      "object_type": "zia_customlists",
      "programmatic_name": "wf_zia_remove_from_customlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "651522cc-f50e-439f-8019-c93048e326be",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_get_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_allowlist\" isExecutable=\"true\" name=\"ZIA: Get Allowlist\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get a list of allow-listed URLs. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The data table \"Zscaler Internet Access - Allowlist\" will be updated if the result \u003c 50, otherwise the result will be added to a note.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_061sgnf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1u727i8\" name=\"ZIA: Get Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"afef84ad-f288-4a0c-a8e1-7c22ffcf1261\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_allowlist post processing script ##\\n\\n#  Globals\\n\\nFN_NAME = \\\"funct_zia_get_allowlist\\\"\\nWF_NAME = \\\"ZIA: Get Allowlist\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    url_filter = INPUTS.get(\\\"zia_url_filter\\\")\\n    if CONTENT:\\n        allowlist_urls = CONTENT.whitelistUrls\\n        url_counts = CONTENT.url_counts\\n        note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; allowlist URLS (s) out of a total of \\\"\\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; using URL filter \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; returned for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, url_counts[\\\"filtered\\\"], url_counts[\\\"total\\\"], url_filter, FN_NAME)\\n        if allowlist_urls:\\n            if url_counts[\\\"filtered\\\"] \u0026lt;= 50:\\n                note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Zscaler Internet Access - Allowlist\\\")\\n                for url in allowlist_urls:\\n                    newrow = incident.addRow(\\\"zia_allowlist\\\")\\n                    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                    newrow.allowlist_url = url\\n                    newrow.query_filter = url_filter\\n            else:\\n                note_text += \\\"\u0026lt;br\u0026gt;Allow list URLS: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\".format(\\\", \\\".join(allowlist_urls))\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results using URL filter \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\"\\\\\\n                     u\\\"returned for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, url_filter, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ZIA - wf_zia_get_allowlist post processing script ##\\nimport re\\n\\nURL_FILTER = rule.properties.zia_url_filter\\n\\ndef is_regex(regex_str):\\n    \\\"\\\"\\\"\\\"Test if sting is a correctly formed regular expression.\\n\\n    :param regex_str: Regular expression string.\\n    :return: Boolean.\\n    \\\"\\\"\\\"\\n    try:\\n        re.compile(regex_str)\\n        return True\\n    except (re.error, TypeError):\\n        return False\\n\\n\\ndef main():\\n    # Test filter to ensure it is a valid regular expressions.\\n    if URL_FILTER and not is_regex(URL_FILTER):\\n        raise ValueError(\\\"The query filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(URL_FILTER)))\\n\\n    inputs.zia_url_filter = rule.properties.zia_url_filter\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_061sgnf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1intjjs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_061sgnf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1u727i8\"/\u003e\u003cendEvent id=\"EndEvent_01p3u33\"\u003e\u003cincoming\u003eSequenceFlow_1intjjs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1intjjs\" sourceRef=\"ServiceTask_1u727i8\" targetRef=\"EndEvent_01p3u33\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1u727i8\" id=\"ServiceTask_1u727i8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"228\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_061sgnf\" id=\"SequenceFlow_061sgnf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"228\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01p3u33\" id=\"EndEvent_01p3u33_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"381\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1intjjs\" id=\"SequenceFlow_1intjjs_di\"\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Get a list of allow-listed URLs. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The data table \"Zscaler Internet Access - Allowlist\" will be updated if the result \u003c 50, otherwise the result will be added to a note.",
      "export_key": "wf_zia_get_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775658750,
      "name": "ZIA: Get Allowlist",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "88a31f09-9615-4a74-819d-3cb428d32840",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_remove_artifact_from_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_artifact_from_allowlist\" isExecutable=\"true\" name=\"ZIA: Remove Artifact From Allowlist\"\u003e\u003cdocumentation\u003eRemove artifact of type URL, URI , DNS hostname or IP address from the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1doni36\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1fi6bw5\" name=\"ZIA: Remove From Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e642b020-f7b1-4e65-aa18-8f05e28ae07e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_artifact_from_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_allowlist\\\"\\nWF_NAME = \\\"ZIA: Remove Artifact From Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        allowlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_allowlist_urls = response.get(\\\"whitelistUrls\\\")\\n        if not any(a in updated_allowlist_urls for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls removed while attempting \\\" \\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist by SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_allowlisturls = artifact.value\\ninputs.zia_activate = rule.properties.zia_activate\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1doni36\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ptbho9\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1doni36\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1fi6bw5\"/\u003e\u003cendEvent id=\"EndEvent_121o9de\"\u003e\u003cincoming\u003eSequenceFlow_0ptbho9\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0ptbho9\" sourceRef=\"ServiceTask_1fi6bw5\" targetRef=\"EndEvent_121o9de\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1fi6bw5\" id=\"ServiceTask_1fi6bw5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"239\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1doni36\" id=\"SequenceFlow_1doni36_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"239\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_121o9de\" id=\"EndEvent_121o9de_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"368\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"386\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ptbho9\" id=\"SequenceFlow_0ptbho9_di\"\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"353.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Remove artifact of type URL, URI , DNS hostname or IP address from the allowlist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be removed from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_remove_artifact_from_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623835125420,
      "name": "ZIA: Remove Artifact From Allowlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_remove_artifact_from_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "a1a55e5f-b9d6-4e2c-b1a0-c7810dbcd91c",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_remove_from_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_from_blocklist\" isExecutable=\"true\" name=\"ZIA: Remove From Blocklist\"\u003e\u003cdocumentation\u003eRemove  URL from the blocklist.  URLs will be parsed to extract format suitable for ZIA which will be removed from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0utralu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0qgmbeh\" name=\"ZIA: Remove From Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"eafc0196-f4bd-4654-8b7c-90e2a67ccac7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_from_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_blocklist\\\"\\nWF_NAME = \\\"ZIA: Remove From Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        status = response.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; from blocklist by SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, status, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = row.blocklist_url\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0utralu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0lc40f6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0utralu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qgmbeh\"/\u003e\u003cendEvent id=\"EndEvent_015l4tv\"\u003e\u003cincoming\u003eSequenceFlow_0lc40f6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0lc40f6\" sourceRef=\"ServiceTask_0qgmbeh\" targetRef=\"EndEvent_015l4tv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qgmbeh\" id=\"ServiceTask_0qgmbeh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"237\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0utralu\" id=\"SequenceFlow_0utralu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_015l4tv\" id=\"EndEvent_015l4tv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"372\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"390\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lc40f6\" id=\"SequenceFlow_0lc40f6_di\"\u003e\u003comgdi:waypoint x=\"337\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"354.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Remove  URL from the blocklist.  URLs will be parsed to extract format suitable for ZIA which will be removed from the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_from_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775657729,
      "name": "ZIA: Remove From Blocklist",
      "object_type": "zia_blocklist",
      "programmatic_name": "wf_zia_remove_from_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "3e067240-9a42-44e4-b339-1d5539bf8119",
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_zia_get_sandbox_report",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_sandbox_report\" isExecutable=\"true\" name=\"ZIA: Get Sandbox Report\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Gets a full (i.e., complete) or summary detail report for an MD5 hash of a file that was analyzed by Sandbox. A summary report will update a data table \"Zscaler Internet Access - Sandbox Report Summary\". A full list will be added as a note in raw JSON format.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1oow3wc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0rwdnn8\" name=\"ZIA: Get Sandbox Report\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"775a93c4-2eb2-41c1-938c-fcb10311b3d6\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_sandbox_report post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_sandbox_report\\\"\\nWF_NAME = \\\"ZIA: Get Sandbox Report\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\nSUMM_HEADERS = [\\\"Summary\\\", \\\"Classification\\\", \\\"FileProperties\\\"]\\nDATA_TBL_FIELDS = {\\n    \\\"Summary\\\": [\\\"Status\\\", \\\"report_Category\\\"],\\n    \\\"Classification\\\": [\\\"Type\\\", \\\"Category\\\", \\\"Score\\\", \\\"DetectedMalware\\\"],\\n    \\\"FileProperties\\\":  [\\\"FileType\\\", \\\"FileSize\\\", \\\"MD5\\\", \\\"SHA1\\\", \\\"Sha256\\\", \\\"Issuer\\\", \\\"DigitalCerificate\\\", \\n                        \\\"SSDeep\\\", \\\"RootCA\\\"]\\n}\\n\\n#Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    bad_summary = u\u0027\u0027\\n    bad_report_status = False\\n    unknown_md5_str = \\\"md5 is unknown or analysis has yet not been completed\\\"\\n    md5 = INPUTS.get(\\\"zia_md5\\\")\\n    report_type = \\\"Full\\\" if INPUTS.get(\\\"zia_full_report\\\") else \\\"Summary\\\"\\n    if CONTENT:\\n        full = CONTENT.get(\\\"Full Details\\\")\\n        summary = CONTENT.get(\\\"Summary\\\")\\n        for r in list(filter(None, [full, summary])):\\n            if  not isinstance(r, dict) and r.find(unknown_md5_str) \u0026gt; -1:\\n                bad_summary = r\\n                bad_report_status = True\\n        if bad_report_status:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; report was not returned for MD5 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n                .format(WF_NAME, report_type, md5, FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\".format(bad_summary)      \\n        elif summary:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; report was returned for MD5 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;. \\\" \\\\\\n                        u\\\"The data table \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; has been updated for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, report_type, md5, \\\"Zscaler Internet Access - Sandbox Report Summary\\\", FN_NAME)\\n            \\n            newrow = incident.addRow(\\\"zia_sandbox_report_summary\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            \\n            for header in SUMM_HEADERS:\\n                section = summary.get(header)\\n                for field in DATA_TBL_FIELDS[header]:\\n                    try:\\n                        f = field.split(\u0027_\u0027)[1]\\n                    except IndexError:\\n                        f = field\\n                    newrow[field]  = \\\"{}\\\".format(section[f])\\n        elif full:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; report was returned for MD5 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;. \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, report_type, md5, FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\".format(full)\\n        else:\\n            note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was an unknown report type returned for MD5 \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\" \\\\\\n                         u\\\" for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, md5, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for MD5 \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\" \\\\\\n                     u\\\" for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, md5, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_md5 =  artifact.value\\nif rule.properties.zia_report_type.lower() == \\\"full\\\":\\n    inputs.zia_full_report = True\\nelse:\\n    inputs.zia_full_report = False\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1oow3wc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zq13oj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1oow3wc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rwdnn8\"/\u003e\u003cendEvent id=\"EndEvent_0ypkg8z\"\u003e\u003cincoming\u003eSequenceFlow_0zq13oj\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0zq13oj\" sourceRef=\"ServiceTask_0rwdnn8\" targetRef=\"EndEvent_0ypkg8z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rwdnn8\" id=\"ServiceTask_0rwdnn8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"231\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1oow3wc\" id=\"SequenceFlow_1oow3wc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ypkg8z\" id=\"EndEvent_0ypkg8z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"366\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"384\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zq13oj\" id=\"SequenceFlow_0zq13oj_di\"\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"366\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"348.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Gets a full (i.e., complete) or summary detail report for an MD5 hash of a file that was analyzed by Sandbox. A summary report will update a data table \"Zscaler Internet Access - Sandbox Report Summary\". A full list will be added as a note in raw JSON format.",
      "export_key": "wf_zia_get_sandbox_report",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623775659964,
      "name": "ZIA: Get Sandbox Report",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_get_sandbox_report",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "40cfaf78-54f9-4e94-b887-d35fcbea6371",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_remove_from_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_remove_from_allowlist\" isExecutable=\"true\" name=\"ZIA: Remove From Allowlist\"\u003e\u003cdocumentation\u003eRemove URL from the allowlist. URLs will be parsed to extract format suitable for ZIA which will be removed from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0pdpsvb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0y3z974\" name=\"ZIA: Remove From Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e642b020-f7b1-4e65-aa18-8f05e28ae07e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_remove_from_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_remove_from_allowlist\\\"\\nWF_NAME = \\\"ZIA: Remove From Allowlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        allowlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_allowlist = response.get(\\\"whitelistUrls\\\")\\n        if not any(a in updated_allowlist for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully removed URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls removed while attempting \\\" \\\\\\n                        u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist by SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    elif isinstance(content, dict):\\n        note_text += u\\\"Is a dict\\\"\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to remove URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; from allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_allowlisturls = row.allowlist_url\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0pdpsvb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1motbxw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0pdpsvb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0y3z974\"/\u003e\u003cendEvent id=\"EndEvent_1dzgan7\"\u003e\u003cincoming\u003eSequenceFlow_1motbxw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1motbxw\" sourceRef=\"ServiceTask_0y3z974\" targetRef=\"EndEvent_1dzgan7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0y3z974\" id=\"ServiceTask_0y3z974_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"240\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0pdpsvb\" id=\"SequenceFlow_0pdpsvb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"240\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1dzgan7\" id=\"EndEvent_1dzgan7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"380\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1motbxw\" id=\"SequenceFlow_1motbxw_di\"\u003e\u003comgdi:waypoint x=\"340\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"380\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"360\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Remove URL from the allowlist. URLs will be parsed to extract format suitable for ZIA which will be removed from the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_remove_from_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623835192655,
      "name": "ZIA: Remove From Allowlist",
      "object_type": "zia_allowlist",
      "programmatic_name": "wf_zia_remove_from_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "a97f0a5f-dfa9-4ad3-a261-185f1504f01c",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "wf_zia_add_artifact_to_customlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_artifact_to_customlist\" isExecutable=\"true\" name=\"ZIA: Add Artifact To Customlist\"\u003e\u003cdocumentation\u003eAdd artifact of type to a custom list. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0aeqtok\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0aa9gvg\" name=\"ZIA: Add To URL Category\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"73e8d2a4-79ca-4896-a022-c895de32762b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_to_customlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_url_category\\\"\\nWF_NAME = \\\"ZIA: Add Artifact To Customlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    category_id = INPUTS.get(\\\"zia_category_id\\\")\\n    configured_name = INPUTS.get(\\\"zia_configured_name\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        customlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_customlist = response.get(\\\"urls\\\")\\n        if all(a in updated_customlist for a in customlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to customlist \\\"\\\\\\n                        u\\\"with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                        .format(WF_NAME, urls, category_id, configured_name, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all urls added while attempting \\\"\\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to customlist with category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and configured name \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; \\\"\\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, category_id,  FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\"\\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to to customlist of category ID \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, category_id,  FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"content = workflow.properties.get_categories_results.content\\nconfigured_name = rule.properties.zia_configured_name\\ncats = content.get(\\\"categories\\\")\\ninputs.zia_category_id = [c[\\\"id\\\"] for c in cats if configured_name == c[\\\"configuredName\\\"]][0]\\ninputs.zia_configured_name = configured_name\\ninputs.zia_urls = artifact.value\\ninputs.zia_activate = rule.properties.zia_activate\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0vebtis\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q55te1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0rjvdlw\"\u003e\u003cincoming\u003eSequenceFlow_0q55te1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0q55te1\" sourceRef=\"ServiceTask_0aa9gvg\" targetRef=\"EndEvent_0rjvdlw\"/\u003e\u003cserviceTask id=\"ServiceTask_13t89bp\" name=\"ZIA: Get URL Categories\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a50d525c-96cf-4006-9f1d-1dd6cd21c9f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_customlist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_url_categories\\\"\\nWF_NAME = \\\"ZIA: Add Artifact To Customlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\n\\n# Processing\\ndef main():\\n    catname_exists = False\\n    note_text = u\u0027\u0027\\n    name_filter = INPUTS.get(\\\"zia_name_filter\\\")\\n    if CONTENT:\\n        cats = CONTENT.get(\\\"categories\\\")\\n        if any(name_filter == c[\\\"configuredName\\\"] for c in cats):\\n            catname_exists = True\\n    if catname_exists:\\n        workflow.addProperty(\\\"catname_exists\\\", {})\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The category nmae  \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was not found \\\" \\\\\\n                     u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, name_filter, FN_NAME)\\n        incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_categories_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0aeqtok\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ktl7mx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0aeqtok\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13t89bp\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0qq6xn0\"\u003e\u003cincoming\u003eSequenceFlow_1ktl7mx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vebtis\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0kmpotg\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1ktl7mx\" sourceRef=\"ServiceTask_13t89bp\" targetRef=\"ExclusiveGateway_0qq6xn0\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0vebtis\" name=\"Category ID exists\" sourceRef=\"ExclusiveGateway_0qq6xn0\" targetRef=\"ServiceTask_0aa9gvg\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cendEvent id=\"EndEvent_1vw7cqt\"\u003e\u003cincoming\u003eSequenceFlow_0kmpotg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0kmpotg\" name=\"Category name does not exist\" sourceRef=\"ExclusiveGateway_0qq6xn0\" targetRef=\"EndEvent_1vw7cqt\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"catname_exists\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ynf6i6\"\u003e\u003ctext\u003eGet category id for the configured name if it exists.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1qgttbe\" sourceRef=\"ServiceTask_13t89bp\" targetRef=\"TextAnnotation_0ynf6i6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0aa9gvg\" id=\"ServiceTask_0aa9gvg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"587\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0rjvdlw\" id=\"EndEvent_0rjvdlw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"767\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"740\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q55te1\" id=\"SequenceFlow_0q55te1_di\"\u003e\u003comgdi:waypoint x=\"687\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"767\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"682\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13t89bp\" id=\"ServiceTask_13t89bp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0aeqtok\" id=\"SequenceFlow_0aeqtok_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0qq6xn0\" id=\"ExclusiveGateway_0qq6xn0_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"412\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"437\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ktl7mx\" id=\"SequenceFlow_1ktl7mx_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"381.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vebtis\" id=\"SequenceFlow_0vebtis_di\"\u003e\u003comgdi:waypoint x=\"462\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"587\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"63\" x=\"494\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1vw7cqt\" id=\"EndEvent_1vw7cqt_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"419\" y=\"334\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"437\" y=\"373\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kmpotg\" id=\"SequenceFlow_0kmpotg_di\"\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"437\" xsi:type=\"omgdc:Point\" y=\"334\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"80\" x=\"413\" y=\"276\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ynf6i6\" id=\"TextAnnotation_0ynf6i6_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"129\" x=\"236\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1qgttbe\" id=\"Association_1qgttbe_di\"\u003e\u003comgdi:waypoint x=\"301\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"301\" xsi:type=\"omgdc:Point\" y=\"99\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "creator_id": "a@a.com",
      "description": "Add artifact of type to a custom list. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the custom list. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_add_artifact_to_customlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623834810858,
      "name": "ZIA: Add Artifact To Customlist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_add_artifact_to_customlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "0d2888a7-246e-4645-8bd8-6dd21a09e8e7",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_get_url_categories",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_get_url_categories\" isExecutable=\"true\" name=\"ZIA: Get URL Categories.\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Get information about URL categories. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The query by default will query for  custom lists only,  query for all can also be selected. The data table \"Zscaler Internet Access - URL Categories\" will be updated.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_09yuw8h\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00b72q2\" name=\"ZIA: Get URL Categories\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a50d525c-96cf-4006-9f1d-1dd6cd21c9f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_get_url_categories post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_get_url_categories\\\"\\nWF_NAME = \\\"ZIA: Get URL Categories\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\nDATA_TBL_FIELDS = [\\\"configuredName\\\", \\\"urls\\\", \\\"customCategory\\\", \\\"editable\\\", \\\"type\\\", \\\"customUrlsCount\\\"]\\n#Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        categories = CONTENT.get(\\\"categories\\\")\\n        cat_counts = CONTENT.get(\\\"category_counts\\\")\\n        custom_only = INPUTS.get(\\\"zia_custom_only\\\")\\n        name_filter = INPUTS.get(\\\"zia_name_filter\\\")\\n        url_filter = INPUTS.get(\\\"zia_url_filter\\\")\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; URL categories out of a total of \\\"\\\\\\n                     u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; returned with \u0027custom_only\u0027 set to \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;, category name filter \\\"\\\\\\n                     u\\\"\u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; and URL filter \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{6}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, cat_counts[\\\"filtered\\\"], cat_counts[\\\"total\\\"], custom_only, name_filter, url_filter, FN_NAME)\\n        if categories:\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Zscaler Internet Access - URL Categories\\\")\\n        for cat in categories:\\n            newrow = incident.addRow(\\\"zia_url_categories\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.cat_id = cat[\\\"id\\\"]\\n            for f in DATA_TBL_FIELDS:\\n              if cat[f] is None:\\n                  newrow[f]  = cat[f]\\n              if isinstance(cat[f], list):\\n                  newrow[f]  = \\\"{}\\\".format(\\\", \\\".join(cat[f]))\\n              elif isinstance(cat[f], bool):\\n                  newrow[f]  = str(cat[f])\\n              else:\\n                  newrow[f]  = \\\"{}\\\".format(cat[f])\\n            newrow.url_filter = url_filter\\n            newrow.name_filter = name_filter\\n            \\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned with \u0027custom_only\u0027 set to \\\" \\\\\\n                     u\\\"\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; configured name filter \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and url filter \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, custom_only, url_filter, name_filter, FN_NAME)\\n\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ZIA - wf_zia_get_url_categories pre processing script ##\\ninputs.zia_custom_only = rule.properties.zia_custom_only\\ninputs.zia_category_id = rule.properties.zia_category_id_input\\nimport re\\n\\nURL_FILTER = rule.properties.zia_url_filter\\nNAME_FILTER = rule.properties.zia_name_filter\\n\\ndef is_regex(regex_str):\\n    \\\"\\\"\\\"\\\"Test if sting is a correctly formed regular expression.\\n\\n    :param regex_str: Regular expression string.\\n    :return: Boolean.\\n    \\\"\\\"\\\"\\n    try:\\n        re.compile(regex_str)\\n        return True\\n    except (re.error, TypeError):\\n        return False\\n\\n\\ndef main():\\n    # Test filter to ensure it is a valid regular expressions.\\n\\n    if URL_FILTER and not is_regex(URL_FILTER):\\n        raise ValueError(\\\"The url filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(URL_FILTER)))\\n    \\n    if NAME_FILTER and not is_regex(NAME_FILTER):\\n        raise ValueError(\\\"The category name filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(NAME_FILTER)))\\n    \\n    inputs.zia_url_filter = URL_FILTER\\n    inputs.zia_name_filter = NAME_FILTER\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_09yuw8h\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_141hh7j\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_09yuw8h\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00b72q2\"/\u003e\u003cendEvent id=\"EndEvent_0gwkfc8\"\u003e\u003cincoming\u003eSequenceFlow_141hh7j\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_141hh7j\" sourceRef=\"ServiceTask_00b72q2\" targetRef=\"EndEvent_0gwkfc8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00b72q2\" id=\"ServiceTask_00b72q2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"223\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09yuw8h\" id=\"SequenceFlow_09yuw8h_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"223\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"210.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gwkfc8\" id=\"EndEvent_0gwkfc8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"345\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_141hh7j\" id=\"SequenceFlow_141hh7j_di\"\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"345\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"334\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Get information about URL categories. The result can be filtered by URL using a regex or string. The filter is case-insensitive. The query by default will query for  custom lists only,  query for all can also be selected. The data table \"Zscaler Internet Access - URL Categories\" will be updated.",
      "export_key": "wf_zia_get_url_categories",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623852353887,
      "name": "ZIA: Get URL Categories.",
      "object_type": "incident",
      "programmatic_name": "wf_zia_get_url_categories",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "68256f21-b1f2-469d-9755-184e431f9807",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_add_urls_to_allowlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_urls_to_allowlist\" isExecutable=\"true\" name=\"ZIA: Add URLs To AllowList\"\u003e\u003cdocumentation\u003eAdd URLS to the allowlist. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dquv84\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1fksf4s\" name=\"ZIA: Add To Allowlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1f0a1aaa-477e-4ed8-afa2-13cb049e47d7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_urls_to_allowlist post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_allowlist\\\"\\nWF_NAME = \\\"ZIA: Add URLs To AllowList\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_allowlisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        allowlist_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        updated_allowlist = response.get(\\\"whitelistUrls\\\")\\n        if all(a in updated_allowlist for a in allowlist_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        \\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Not all URIs added while attempting \\\" \\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to allowlist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_activate = rule.properties.zia_activate\\ninputs.zia_allowlisturls = rule.properties.zia_urls.content\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dquv84\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1b87zlo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dquv84\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1fksf4s\"/\u003e\u003cendEvent id=\"EndEvent_1ebtwgr\"\u003e\u003cincoming\u003eSequenceFlow_1b87zlo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1b87zlo\" sourceRef=\"ServiceTask_1fksf4s\" targetRef=\"EndEvent_1ebtwgr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1fksf4s\" id=\"ServiceTask_1fksf4s_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"226\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dquv84\" id=\"SequenceFlow_0dquv84_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"226\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"212\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ebtwgr\" id=\"EndEvent_1ebtwgr_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"349\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"367\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1b87zlo\" id=\"SequenceFlow_1b87zlo_di\"\u003e\u003comgdi:waypoint x=\"326\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"337.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Add URLS to the allowlist. Entries of type URL will be parsed to extract format suitable for ZIA which will be added to the allowlist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines",
      "export_key": "wf_zia_add_urls_to_allowlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623834884917,
      "name": "ZIA: Add URLs To AllowList",
      "object_type": "incident",
      "programmatic_name": "wf_zia_add_urls_to_allowlist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "3ebbd3f9-8d0d-41b6-89e4-39f5c8cedba1",
      "workflow_id": 78
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "wf_zia_add_artifact_to_blocklist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_artifact_to_blocklist\" isExecutable=\"true\" name=\"ZIA: Add Artifact To Blocklist\"\u003e\u003cdocumentation\u003eAdd artifact of type URL, URI , DNS hostname or IP address to the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_11faor5\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16xg70t\" name=\"ZIA: Add To Blocklist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d02e8977-6437-4093-8e19-422f3ba315f7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_artifact_to_blocklist post processing script ##\\n\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_to_blocklist\\\"\\nWF_NAME = \\\"ZIA: Add Artifact To Blocklist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    urls = INPUTS.get(\\\"zia_blocklisturls\\\")\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        status = response.get(\\\"status\\\")\\n        if status == \\\"OK\\\":\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist \\\" \\\\\\n                        u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, urls, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned while attempting \\\" \\\\\\n                        u\\\"to add URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add URLs \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; to blocklist for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_blocklisturls = artifact.value\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11faor5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01oljus\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11faor5\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16xg70t\"/\u003e\u003cendEvent id=\"EndEvent_01x5bt3\"\u003e\u003cincoming\u003eSequenceFlow_01oljus\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01oljus\" sourceRef=\"ServiceTask_16xg70t\" targetRef=\"EndEvent_01x5bt3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16xg70t\" id=\"ServiceTask_16xg70t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"241\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11faor5\" id=\"SequenceFlow_11faor5_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"241\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01x5bt3\" id=\"EndEvent_01x5bt3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"371\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"389\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01oljus\" id=\"SequenceFlow_01oljus_di\"\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"356\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@a.com",
      "description": "Add artifact of type URL, URI , DNS hostname or IP address to the blocklist. Artifacts of type URL will be parsed to extract format suitable for ZIA which will be added to the blocklist. See following for URL guidelines https://help.zscaler.com/zia/url-format-guidelines.",
      "export_key": "wf_zia_add_artifact_to_blocklist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623862044280,
      "name": "ZIA: Add Artifact To Blocklist",
      "object_type": "artifact",
      "programmatic_name": "wf_zia_add_artifact_to_blocklist",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "42e6bd4b-fed4-4a14-9f53-a8cd10bc0bcc",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_zia_add_custom_category",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_zia_add_custom_category\" isExecutable=\"true\" name=\"ZIA: Add Custom Category\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Add a new custom URL category. The super category  defaults to \"USER_DEFINED\".]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_11p6qvq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03e4w5z\" name=\"ZIA: Add URL Category\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"197a1156-a58e-417f-9e60-71923a030c2c\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ZIA - wf_zia_add_url_category post processing script ##\\nimport re\\n#  Globals\\nFN_NAME = \\\"funct_zia_add_url_category\\\"\\nWF_NAME = \\\"ZIA: Add Custom Category\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    \\n    urls = INPUTS.get(\\\"zia_urls\\\")\\n    configured_name = INPUTS.get(\\\"zia_configured_name\\\")\\n\\n    if CONTENT:\\n        response = CONTENT.get(\\\"response\\\")\\n        activation = CONTENT.get(\\\"activation\\\")\\n        id = response.get(\\\"id\\\")\\n        super_cat = response.get(\\\"superCategory\\\")\\n        # In order to test all urls have been successfully added, convert string of urls\\n        # to a list and convert urls to the format used by ZIA. e.g. https://user:password@domain.com:port/index.html -\u0026gt;\\n        # domain.com:port/index.html\\n        list_urls = [re.sub(r\u0027^.*\\\\/\\\\/(.*@)*(.*)\u0027, r\u0027\\\\2\u0027, u) for u in re.split(\\\"\\\\s+|,\\\", urls)]\\n        category_list = response.get(\\\"urls\\\")\\n        if all(a in category_list for a in list_urls):\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully Created category \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with id \\\"\\\\\\n                        u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; and with urls \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; in super category \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, configured_name, id, urls, super_cat, FN_NAME)\\n            note_text += u\\\" Activation status: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\".format(activation[\\\"status\\\"])\\n        \\n        else:\\n            note_text = u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Category \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; creation not successfull \\\" \\\\\\n                        u\\\"with URLs \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;  for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, configured_name, urls, FN_NAME)\\n    else:\\n        note_text += u\\\"ZIA Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to create category \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with URLS \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, configured_name, urls, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\\n\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.zia_configured_name = rule.properties.zia_configured_name_input\\ninputs.zia_custom_category = \\\"true\\\"\\ninputs.zia_super_category = rule.properties.zia_super_category\\ninputs.zia_urls = rule.properties.zia_urls.content\\ninputs.zia_activate = rule.properties.zia_activate\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11p6qvq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17j1gfe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11p6qvq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03e4w5z\"/\u003e\u003cendEvent id=\"EndEvent_1wtibk9\"\u003e\u003cincoming\u003eSequenceFlow_17j1gfe\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17j1gfe\" sourceRef=\"ServiceTask_03e4w5z\" targetRef=\"EndEvent_1wtibk9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03e4w5z\" id=\"ServiceTask_03e4w5z_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"243\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11p6qvq\" id=\"SequenceFlow_11p6qvq_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wtibk9\" id=\"EndEvent_1wtibk9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"374\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"392\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17j1gfe\" id=\"SequenceFlow_17j1gfe_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"358.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@a.com",
      "description": "Add a new custom URL category. The super category  defaults to \"USER_DEFINED\".",
      "export_key": "wf_zia_add_custom_category",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1623834787873,
      "name": "ZIA: Add Custom Category",
      "object_type": "incident",
      "programmatic_name": "wf_zia_add_custom_category",
      "tags": [
        {
          "tag_handle": "fn_zia",
          "value": null
        }
      ],
      "uuid": "3717ff63-21f3-4ff3-83cb-3ba02aa7e98e",
      "workflow_id": 86
    }
  ],
  "workspaces": []
}
