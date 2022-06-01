{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.dns_name",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.ipaddr4",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.macaddr",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) add artifact",
      "id": 96,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) add artifact",
      "object_type": "extrahop_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "21d3a3ea-cbd4-4301-bdfb-0e8976121887",
      "view_items": [
        {
          "content": "29e39e7a-56b3-4727-9b44-2af47e40f69b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_add_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.devs_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) assign tag",
      "id": 97,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) assign tag",
      "object_type": "extrahop_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "911c76f4-ea2e-4fef-9512-7bfd72117e67",
      "view_items": [
        {
          "content": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_assign_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) create tag",
      "id": 98,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) create tag",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "decd187f-500b-4eda-9ee1-d8a9ab298dae",
      "view_items": [
        {
          "content": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_create_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) get activitymaps",
      "id": 99,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) get activitymaps",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d4f01da3-6489-4314-a7c6-0898a8f5e4b5",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_activitymaps"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) get tags",
      "id": 101,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) get tags",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b3318147-5a01-40da-8187-ca9140c04797",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_tags"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) get watchlist",
      "id": 102,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) get watchlist",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6adc7665-89bd-4448-a0be-bc205fc385a1",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_get_watchlist"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) refresh incident",
      "id": 115,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) refresh incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6df920ba-b6b7-4651-b858-27607ee18dc0",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_refresh_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) search detections",
      "id": 103,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) search detections",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e09ea0e6-ec4d-4c03-804e-1420cdd10cd6",
      "view_items": [
        {
          "content": "9692d8f7-aa30-4057-b9bc-a9fa24e7a167",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d9ef56c-f0f8-4f5d-98d6-e432e8ca2ac2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d94e2a93-a192-4ba5-a653-fd5a0e30f5f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bcf2d8ba-1bd4-4b75-8566-5cead8f5a1d1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "87ae2dd2-17dc-4351-b41c-daf7fa89f821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f16fa55a-4d2d-4c64-89d1-15cc657e7752",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4fc1ab8f-a2d8-4da5-9cab-a217457d536d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c0e8942a-16c2-4eca-b171-3553b130b445",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d46ebaf8-c9c1-4ca6-9c6c-b13c33886362",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_detections"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) search devices",
      "id": 104,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) search devices",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "60bf1021-e9f0-4395-bdaf-08e9006c4db0",
      "view_items": [
        {
          "content": "117b1d04-cf13-45bb-b95a-9422ba450477",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b3a4740-50d4-45b2-8e5d-9ad245a5673d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7064c221-59b5-4ff9-b015-e3360d0bbbbb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4aba00eb-fe2e-4580-b7f1-72b5a3793c7c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_devices"
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
          "value": "MAC Address"
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) search packets",
      "id": 108,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) search packets",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "384f2f6d-4679-4017-b1ab-db26f09d59d3",
      "view_items": [
        {
          "content": "472c0398-165f-4543-a42e-e689031485a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "12902179-0671-4cd1-ae3d-299f0aa41a86",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1d9d2ede-fabe-48d3-9f7f-33b0bd13a426",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f53ed073-19f7-4e0a-8059-2d5d10c4fb58",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "31bfb391-2463-4b8a-9865-c2b27431387e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b1f1135a-d790-4ff2-ade3-064b8d4e4b54",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fb989c53-33df-4efb-a363-4fa6b070cd3d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3d7cb90-2673-4733-97ae-ee3e837f43c9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_search_packets"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "changed_to",
          "type": null,
          "value": "Closed"
        },
        {
          "evaluation_id": null,
          "field_name": "incident.resolution_summary",
          "method": "not_contains",
          "type": null,
          "value": "Closed by ExtraHop"
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) update detection",
      "id": 105,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) update detection",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "a2591bfb-c7bb-4fcd-8a00-9b3903a24abc",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_update_detection"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.extrahop_detection_id",
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
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) update incident",
      "id": 106,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) update incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "e5f23d43-4054-4070-8f3f-3f9a43e3fbcb",
      "view_items": [],
      "workflows": [
        "wf_extrahop_rx_update_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "extrahop_devices.devs_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Extrahop Reveal(x) update watchlist",
      "id": 95,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Extrahop Reveal(x) update watchlist",
      "object_type": "extrahop_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7f295522-9fbf-49bb-8cc0-0d27e00f1299",
      "view_items": [
        {
          "content": "f7e7aa61-a227-4545-bede-653afe438414",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_extrahop_rx_update_watchlist"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1654103751788,
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
      "export_key": "__function/soar_inc_owner_id",
      "hide_notification": false,
      "id": 888,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_owner_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_owner_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "88360341-cb95-4040-9f2c-920f41d138bf",
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
      "export_key": "__function/extrahop_tag_name",
      "hide_notification": false,
      "id": 889,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_tag_name",
      "tooltip": "The string value for an ExtraHop  tag name.",
      "type_id": 11,
      "uuid": "9274ccb1-cebb-4be8-b7f1-f768f0eabbcf",
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
      "export_key": "__function/extrahop_always_return_body",
      "hide_notification": false,
      "id": 890,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_always_return_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_always_return_body",
      "tooltip": "If True return an empty packet capture file and an HTTP status of 200.",
      "type_id": 11,
      "uuid": "980e64f8-1d36-4d58-a611-0d3c54a9bf02",
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
      "export_key": "__function/extrahop_unassign",
      "hide_notification": false,
      "id": 778,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_unassign",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_unassign",
      "tooltip": "Comma or newline seperated list of device ids to unassign from a watchlist.",
      "type_id": 11,
      "uuid": "a19c702d-206d-48a7-8b26-80d7d4aaa4b6",
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
      "export_key": "__function/extrahop_assign",
      "hide_notification": false,
      "id": 779,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_assign",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_assign",
      "tooltip": "Comma or newline seperated list of device ids to assign to a watchlist.",
      "type_id": 11,
      "uuid": "a4628ae7-81c6-4208-ba4f-e71295f3c117",
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
      "export_key": "__function/extrahop_active_from",
      "hide_notification": false,
      "id": 780,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_active_from",
      "tooltip": "(Optional) The beginning timestamp for the request. Return only devices active after this time. Time is expressed in milliseconds since the epoch. 0 indicates the time of the request.",
      "type_id": 11,
      "uuid": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
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
      "export_key": "__function/extrahop_update_time",
      "hide_notification": false,
      "id": 891,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_update_time",
      "tooltip": "(Optional) Return detections that were updated on or after the specified date, expressed in milliseconds since the epoch.",
      "type_id": 11,
      "uuid": "b175d32a-198e-403d-adcd-052b56876488",
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
      "export_key": "__function/extrahop_note",
      "hide_notification": false,
      "id": 940,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_note",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_note",
      "tooltip": "ExtraHop note object",
      "type_id": 11,
      "uuid": "b9311b73-c244-47be-ac17-5ada6595b3e9",
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
      "export_key": "__function/extrahop_port2",
      "hide_notification": false,
      "id": 892,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_port2",
      "tooltip": " Return packets sent from or received on the specified port.",
      "type_id": 11,
      "uuid": "bd451766-afc3-40d7-86c8-5c512586b7d0",
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
      "export_key": "__function/extrahop_offset",
      "hide_notification": false,
      "id": 783,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_offset",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_offset",
      "tooltip": "(Optional) Skip the specified number of devices. This parameter is often combined with the limit parameter to paginate result sets.",
      "type_id": 11,
      "uuid": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
      "export_key": "__function/soar_inc_resolution_id",
      "hide_notification": false,
      "id": 893,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_resolution_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_resolution_id",
      "tooltip": "SOAR incident resolution",
      "type_id": 11,
      "uuid": "ccbe84af-c0ae-4ae5-a280-c84d1bde5f4d",
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
      "export_key": "__function/extrahop_limit_search_duration",
      "hide_notification": false,
      "id": 894,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_search_duration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit_search_duration",
      "tooltip": "The maximum amount of time to run the packet search.",
      "type_id": 11,
      "uuid": "d265d66f-635b-4f5c-8aa5-d7146f65ac15",
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
      "export_key": "__function/soar_inc_plan_status",
      "hide_notification": false,
      "id": 895,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "soar_inc_plan_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "soar_inc_plan_status",
      "tooltip": "SOAR incident status",
      "type_id": 11,
      "uuid": "dce787c0-2575-4dde-b0fa-a453fff3c941",
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
      "export_key": "__function/extrahop_limit_bytes",
      "hide_notification": false,
      "id": 896,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_bytes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit_bytes",
      "tooltip": "The maximum number of bytes to return.",
      "type_id": 11,
      "uuid": "eef5fc53-d7d2-4711-9263-ccec47dacd13",
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
      "export_key": "__function/extrahop_activitymap_id",
      "hide_notification": false,
      "id": 897,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_activitymap_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_activitymap_id",
      "tooltip": "The unique identifier for the activity map.",
      "type_id": 11,
      "uuid": "f1d0366d-e216-4071-8070-c67fe27f834b",
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
      "export_key": "__function/extrahop_device_ids",
      "hide_notification": false,
      "id": 898,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_device_ids",
      "tooltip": "Comma or newline seperated list of device ids.",
      "type_id": 11,
      "uuid": "f7117970-a76c-4505-87b3-5dbcc35eabdc",
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
      "export_key": "__function/extrahop_ip1",
      "hide_notification": false,
      "id": 899,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_ip1",
      "tooltip": "Return packets sent to or received by the specified IP address.",
      "type_id": 11,
      "uuid": "f844555a-e911-4ea3-95c2-44ad4f8c5ef9",
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
      "export_key": "__function/extrahop_sort",
      "hide_notification": false,
      "id": 900,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_sort",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_sort",
      "tooltip": "Sorts returned detections by the specified fields. By default, detections are sorted by most recent update time and then ID in ascending order.",
      "type_id": 11,
      "uuid": "0b7aca53-b3b4-42b0-8386-3f19042acf55",
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
      "export_key": "__function/extrahop_search_filter",
      "hide_notification": false,
      "id": 901,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_search_filter",
      "tooltip": "The  filter criteria for Extrahop search results.",
      "type_id": 11,
      "uuid": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
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
      "export_key": "__function/extrahop_participants",
      "hide_notification": false,
      "id": 902,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_participants",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{ \"id\": 0, \"usernames\": [], \"origins\": [] }",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_participants",
      "tooltip": "A list of devices and applications associated with a detection. ",
      "type_id": 11,
      "uuid": "13f7dfc8-67b0-4ead-a5c7-191d915cf79b",
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
      "export_key": "__function/extrahop_bpf",
      "hide_notification": false,
      "id": 903,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_bpf",
      "operation_perms": {},
      "operations": [],
      "placeholder": "host 192.168.1.2  dst host 192.168.1.3",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_bpf",
      "tooltip": "Filter packets with Berkeley Packet Filter syntax.",
      "type_id": 11,
      "uuid": "19778340-0ca0-47af-bb7b-61d0d2be6fa1",
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
      "export_key": "__function/extrahop_detection_id",
      "hide_notification": false,
      "id": 904,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_detection_id",
      "tooltip": "Extrahop detection ID",
      "type_id": 11,
      "uuid": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
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
      "export_key": "__function/extrahop_search_type",
      "hide_notification": false,
      "id": 796,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_search_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_search_type",
      "tooltip": "Indicates the field to search.",
      "type_id": 11,
      "uuid": "3a2068f3-d76c-4dac-8776-819499720814",
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
      "id": 905,
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "The ID for the incident in Resilient",
      "type_id": 11,
      "uuid": "3eb56561-8f36-458f-845a-eb3923bd0073",
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
      "export_key": "__function/extrahop_ip2",
      "hide_notification": false,
      "id": 906,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_ip2",
      "tooltip": "Return packets sent to or received by the specified IP address.",
      "type_id": 11,
      "uuid": "4756201b-b5b0-4a90-934d-815e13644e5e",
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
      "export_key": "__function/extrahop_value",
      "hide_notification": false,
      "id": 799,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_value",
      "tooltip": "Indicates the vakue to search for.",
      "type_id": 11,
      "uuid": "5763430b-3c38-4873-aec3-df249773c52a",
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
      "export_key": "__function/extrahop_tag_id",
      "hide_notification": false,
      "id": 907,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_tag_id",
      "tooltip": "The unique identifier for the tag.",
      "type_id": 11,
      "uuid": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
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
      "export_key": "__function/extrahop_limit",
      "hide_notification": false,
      "id": 801,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_limit",
      "tooltip": "(Optional) Limit the number of devices returned to the specified maximum number.",
      "type_id": 11,
      "uuid": "64a89cad-9373-4017-ba04-d06f97a28e8c",
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
      "export_key": "__function/extrahop_active_until",
      "hide_notification": false,
      "id": 802,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_until",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_active_until",
      "tooltip": "(Optional) The ending timestamp for the request. Return only devices active before this time.",
      "type_id": 11,
      "uuid": "68a4691f-8609-4d19-9208-3a7589a37997",
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
      "export_key": "__function/extrahop_port1",
      "hide_notification": false,
      "id": 908,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_port1",
      "tooltip": "Return packets sent from or received on the specified port.",
      "type_id": 11,
      "uuid": "6aa0c2da-9841-4b51-9c22-bd8d245d9cc6",
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
      "export_key": "__function/extrahop_output",
      "hide_notification": false,
      "id": 909,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_output",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_output",
      "tooltip": "The output format. Valid values pcap , keylog_txt  and zip",
      "type_id": 11,
      "uuid": "70f63d36-2b02-4939-ad37-620659809eaa",
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
      "export_key": "__function/extrahop_device_id",
      "hide_notification": false,
      "id": 805,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "extrahop_device_id",
      "tooltip": "Extrahop device ID",
      "type_id": 11,
      "uuid": "77f58f54-c4a9-4720-ab05-34e2beb94521",
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
      "export_key": "actioninvocation/extrahop_active_until",
      "hide_notification": false,
      "id": 870,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_until",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Active until",
      "tooltip": " (Optional) The ending timestamp for the request. ",
      "type_id": 6,
      "uuid": "8230c857-e727-4b1d-825b-0a17fc5cc69a",
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
      "export_key": "actioninvocation/extrahop_detection_assignee",
      "hide_notification": false,
      "id": 871,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_assignee",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Assignee",
      "tooltip": "Optional: Detection search filter assignee.",
      "type_id": 6,
      "uuid": "87ae2dd2-17dc-4351-b41c-daf7fa89f821",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": ".none",
          "properties": null,
          "uuid": "a93a621d-62e0-43a7-bb56-a71e6707d1f5",
          "value": 2157
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": ".me",
          "properties": null,
          "uuid": "8e0aa174-400f-4e12-8abc-ab236d17c7e3",
          "value": 2158
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cAdd user here\u003e",
          "properties": null,
          "uuid": "23ebf1ae-2fd5-4ec3-b535-9f47305bc63a",
          "value": 2159
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
      "export_key": "actioninvocation/extrahop_tag_name",
      "hide_notification": false,
      "id": 872,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_tag_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Tag name",
      "tooltip": "The string value for an Etrahop  tag name.",
      "type_id": 6,
      "uuid": "8fc11a21-d45b-4324-a255-63c4e857ec4f",
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
      "export_key": "actioninvocation/extrahop_detection_id",
      "hide_notification": false,
      "id": 1238,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Detection ID",
      "tooltip": "ExtraHop Detection ID",
      "type_id": 6,
      "uuid": "9692d8f7-aa30-4057-b9bc-a9fa24e7a167",
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
      "export_key": "actioninvocation/extrahop_detection_risk_score_min",
      "hide_notification": false,
      "id": 873,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_risk_score_min",
      "operation_perms": {},
      "operations": [],
      "placeholder": "80",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Riskscore minimum",
      "tooltip": "Optional: Detection search filter riskscore minimum.",
      "type_id": 6,
      "uuid": "9d9ef56c-f0f8-4f5d-98d6-e432e8ca2ac2",
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
      "export_key": "actioninvocation/extrahop_limit",
      "hide_notification": false,
      "id": 874,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Limit",
      "tooltip": "(Optional) Limit the number of devices returned to the specified maximum number.",
      "type_id": 6,
      "uuid": "a734c1dd-38bc-4b9a-8df6-b6237af57cf8",
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
      "export_key": "actioninvocation/extrahop_port1",
      "hide_notification": false,
      "id": 931,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Port1",
      "tooltip": "(Optional) Return packets sent from or received on the specified port.",
      "type_id": 6,
      "uuid": "b1f1135a-d790-4ff2-ade3-064b8d4e4b54",
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
      "export_key": "actioninvocation/extrahop_port2",
      "hide_notification": false,
      "id": 932,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_port2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Port2",
      "tooltip": "(Optional)  Return packets sent from or received on the specified port.",
      "type_id": 6,
      "uuid": "b3d7cb90-2673-4733-97ae-ee3e837f43c9",
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
      "export_key": "actioninvocation/extrahop_detection_types",
      "hide_notification": false,
      "id": 943,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_types",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Types",
      "tooltip": "(Optional): Detection search filter types.",
      "type_id": 6,
      "uuid": "bcf2d8ba-1bd4-4b75-8566-5cead8f5a1d1",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "cobalt_strike_cd_http",
          "properties": null,
          "uuid": "f2ed837b-ab67-4e3e-91f5-4834047c6ba8",
          "value": 2357
        },
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "rdp_brute_force",
          "properties": null,
          "uuid": "e617f6d7-d802-4126-9f22-4b2089d191f1",
          "value": 2358
        },
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "ssh_brute_force",
          "properties": null,
          "uuid": "4f8fff21-a0c7-40af-ae69-d7ffa9a7458f",
          "value": 2359
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AAA Auth Errors",
          "properties": null,
          "uuid": "481f9f8d-ecf3-442c-ae53-d8bee32ab98c",
          "value": 2407
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in AAA Failed Login Attempts",
          "properties": null,
          "uuid": "5d8d4249-7ffe-46d5-b205-7598b9970c19",
          "value": 2408
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Data Staging",
          "properties": null,
          "uuid": "fc7444ed-c993-4e17-b602-1cd0700f1960",
          "value": 2409
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Data Exfiltration to S3 Bucket",
          "properties": null,
          "uuid": "f5892252-e66d-4d5e-bde4-a3a56372316c",
          "value": 2410
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual User Creation",
          "properties": null,
          "uuid": "5a247c77-e57d-4332-b8ec-eceaffb0647a",
          "value": 2411
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New Printer Driver Installation Request",
          "properties": null,
          "uuid": "b25fe3d9-9214-438e-8574-0384e80f25bb",
          "value": 2412
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Anonymous FTP Auth Enabled",
          "properties": null,
          "uuid": "73f3421e-a9c1-43c1-bd70-c33ba174d7f5",
          "value": 2413
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apache HTTP Server Path Traversal Exploit",
          "properties": null,
          "uuid": "b6e5fc8b-7ca0-4ead-afd9-afa41a86b486",
          "value": 2414
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apache Struts 2 Exploit Attempt",
          "properties": null,
          "uuid": "3461e48f-8adf-457d-9069-daa6f2728369",
          "value": 2415
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Attempted Connections Dropped",
          "properties": null,
          "uuid": "f3d56453-2477-4deb-b563-b1b5fdd4e90a",
          "value": 2416
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AWS Instance Metadata Service (IMDS) Proxy",
          "properties": null,
          "uuid": "e2bee76a-d816-4482-aa78-6b9e4c71f72e",
          "value": 2417
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AWS Cloud Service Enumeration",
          "properties": null,
          "uuid": "9127b8a1-a094-4e84-8642-aedb379ccd93",
          "value": 2418
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BitTorrent Activity",
          "properties": null,
          "uuid": "97717cc9-8142-4ad2-b175-a01b48006195",
          "value": 2419
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious SSL/TLS Certificates",
          "properties": null,
          "uuid": "8aa07619-64db-42fd-b24e-01942c4c3797",
          "value": 2420
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BloodHound Enumeration Activity",
          "properties": null,
          "uuid": "1ae48693-5efb-4f3f-85e6-29c5f3f93a75",
          "value": 2421
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Command-and-Control Beaconing",
          "properties": null,
          "uuid": "0b90ce9d-a8cc-4e5c-8e86-1a2b76fade1a",
          "value": 2422
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Call Does Not Exist Error",
          "properties": null,
          "uuid": "f5f5e56a-689f-49aa-b591-236263cd9278",
          "value": 2423
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Transaction Delays",
          "properties": null,
          "uuid": "471ee379-5bdc-4d2e-a9ed-788a7a7e4fef",
          "value": 2424
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cisco CDP Exploit Attempt",
          "properties": null,
          "uuid": "9a82db46-a320-4685-92bc-809f1ef3c57b",
          "value": 2425
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Citrix Issues",
          "properties": null,
          "uuid": "05c973ff-ef6c-474c-94b4-7f7ce7e9797e",
          "value": 2426
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cobalt Strike DNS Beaconing",
          "properties": null,
          "uuid": "2af3c767-0368-4768-8206-485e5621a8c3",
          "value": 2427
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cobalt Strike C\u0026C HTTP Connection",
          "properties": null,
          "uuid": "c771898e-23ce-4127-9be7-df232d1cc2e8",
          "value": 2428
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cobalt Strike C\u0026C SSL/TLS Connection",
          "properties": null,
          "uuid": "98b02e60-b478-4a47-9f00-d4dcd8bcec3c",
          "value": 2429
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious File Download on Critical Server",
          "properties": null,
          "uuid": "63bad438-bd59-4af9-b915-d7f75be27d88",
          "value": 2430
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cryptocurrency Mining",
          "properties": null,
          "uuid": "7e8aeca1-a1e3-4f23-9987-7f35e816f4a9",
          "value": 2431
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Request for a Cryptocurrency Mining Pool",
          "properties": null,
          "uuid": "78183aaf-0440-4262-9416-fc3cd4372ea3",
          "value": 2432
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SSL/TLS Connection to a Cryptocurrency Mining Pool",
          "properties": null,
          "uuid": "038d6b8d-3d74-4bd3-8301-f86c27e230b9",
          "value": 2433
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Custom",
          "properties": null,
          "uuid": "a52a44db-d3a4-470f-9bee-b865bf8c8b5d",
          "value": 2434
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2017-12635 Apache CouchDB Exploit Attempt",
          "properties": null,
          "uuid": "f147a7bd-8001-47ff-9a6e-a2326509da12",
          "value": 2435
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2018-1111 Red Hat DHCP Exploit Attempt",
          "properties": null,
          "uuid": "cb6c3c8c-cf2b-43c7-9684-0ae7de0a8dc3",
          "value": 2436
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2018-13379 Fortinet FortiOS Exploit",
          "properties": null,
          "uuid": "96605ef0-98da-4511-80e9-71a11d60c07b",
          "value": 2437
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2018-15961 Adobe ColdFusion Exploit Attempt",
          "properties": null,
          "uuid": "ca111f0e-0ef5-413f-8000-58feea4d8cf6",
          "value": 2438
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Drupal Exploit Attempt",
          "properties": null,
          "uuid": "6295ec45-f2ee-46e1-874e-2e70a4fd693c",
          "value": 2439
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-0193 Apache Solr Exploit Attempt",
          "properties": null,
          "uuid": "133569c0-8f00-48ca-8d54-04c2e9a0f352",
          "value": 2440
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-0604 Microsoft SharePoint Exploit Attempt",
          "properties": null,
          "uuid": "3dd1578d-a499-4f69-a127-69109b4273b2",
          "value": 2441
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-0708 RDP Exploit Attempt",
          "properties": null,
          "uuid": "7c087511-3112-484d-a5c8-405257bc4d07",
          "value": 2442
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-10149 Exim Exploit Attempt",
          "properties": null,
          "uuid": "f902fd94-63a2-40ac-b2ff-ba9d9ea0d410",
          "value": 2443
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-11510 Pulse Connect Secure Exploit Attempt",
          "properties": null,
          "uuid": "11a8acd4-1b22-4628-9299-6c085235d439",
          "value": 2444
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-11580: Atlassian Crowd Vulnerability",
          "properties": null,
          "uuid": "01b343ed-a426-4aa9-bd93-05eb110ffaf3",
          "value": 2445
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-15846 Exim Exploit Attempt",
          "properties": null,
          "uuid": "deeaad3e-f0f6-4345-a301-657b08fc68cc",
          "value": 2446
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-17558 Apache Solr Exploit",
          "properties": null,
          "uuid": "02354b81-7dc9-4240-b03e-48b7cf1cfb85",
          "value": 2447
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-19781 Citrix ADC and Gateway Exploit",
          "properties": null,
          "uuid": "eee84713-2b44-456a-8733-42aba58e20d1",
          "value": 2448
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-19781 Citrix ADC and Gateway Scan",
          "properties": null,
          "uuid": "b430ffa9-0504-45ac-9f2e-0443db5d5c85",
          "value": 2449
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Oracle WebLogic Exploit",
          "properties": null,
          "uuid": "c004a4fd-1a54-4385-9626-08017b32c4cd",
          "value": 2450
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-8394 Zoho ManageEngine Exploit Attempt",
          "properties": null,
          "uuid": "8c60c331-e8b7-4b5a-8ef9-0cf620ccbdb1",
          "value": 2451
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2019-9670 Synacor Zimbra Collaboration Suite Exploit Attempt",
          "properties": null,
          "uuid": "43216745-3127-48c6-b6b9-a5dec8af240e",
          "value": 2452
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-0601 Windows CryptoAPI ECC Validation Vulnerability",
          "properties": null,
          "uuid": "a0dfc07d-683e-4d91-9912-4dd48055b878",
          "value": 2453
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-0796 Windows 10 SMBv3 Exploit Attempt",
          "properties": null,
          "uuid": "5de589b9-2882-4016-a202-b337a3d14ab5",
          "value": 2454
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-10189 Zoho ManageEngine Exploit",
          "properties": null,
          "uuid": "7668a08d-7fda-4660-a5a6-e05e65e1769c",
          "value": 2455
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-11651 Salt Exploit Attempt",
          "properties": null,
          "uuid": "827d7b01-7fec-40e1-9113-4c16b0df3707",
          "value": 2456
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-12695 UPnP Exploit Attempt",
          "properties": null,
          "uuid": "d4c48c7c-65f7-409e-9d34-7035fb2c8935",
          "value": 2457
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-1301 SMBv1 Exploit",
          "properties": null,
          "uuid": "d1fcdf83-2e03-48a2-93fb-08c35f5e4664",
          "value": 2458
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-1350 SIGRed Exploit Attempt",
          "properties": null,
          "uuid": "5c8e6513-14d3-433d-a0cc-365849cf503b",
          "value": 2459
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-1472 Zerologon Scan",
          "properties": null,
          "uuid": "65643cac-82ee-48bc-a7c9-bb50c6bc19b0",
          "value": 2460
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-1472 Zerologon Exploit Attempt",
          "properties": null,
          "uuid": "474b1484-a230-448a-aebd-2e3331db5263",
          "value": 2461
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-15505 MobileIron Core and Connector Exploit Attempt",
          "properties": null,
          "uuid": "7c3d1c91-b091-4f9f-ae15-bd15eb71a0a0",
          "value": 2462
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-16898 Windows TCP/IP Stack Exploit Attempt",
          "properties": null,
          "uuid": "db33703a-ac3d-4e85-8f5e-268aae0eb662",
          "value": 2463
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-16899 Windows TCP/IP Stack Exploit Attempt",
          "properties": null,
          "uuid": "f562cebd-43a7-4aaf-82a6-2e4222ec1a9c",
          "value": 2464
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-17051 Windows NFS Exploit Attempt",
          "properties": null,
          "uuid": "b74aeec3-dab2-49c0-8473-e66f233daf3d",
          "value": 2465
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-1938 Ghostcat Exploit",
          "properties": null,
          "uuid": "9af372ee-9fc9-4f41-b279-2615ad1a2916",
          "value": 2466
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-25577 FreeBSD Exploit Attempt",
          "properties": null,
          "uuid": "896bb780-01d6-4980-9f55-b5a5becaf43e",
          "value": 2467
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-25583 FreeBSD Exploit Attempt",
          "properties": null,
          "uuid": "f47e190a-5df1-462f-a9b1-660f45e48b60",
          "value": 2468
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-3952 VMware vCenter Exploit",
          "properties": null,
          "uuid": "2aff2b91-e9d0-42a1-9571-dea66e9270ba",
          "value": 2469
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-5902 F5 BIG-IP Exploit",
          "properties": null,
          "uuid": "8c3e5867-df6d-4d0c-97a7-3acce6b545d8",
          "value": 2470
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-6207 SAP Solution Manager Exploit Attempt",
          "properties": null,
          "uuid": "82ceb047-be6e-4573-8420-9cb0e62f3d78",
          "value": 2471
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-6287 SAP RECON Vulnerability",
          "properties": null,
          "uuid": "89ab517d-56c8-4baa-8b2b-93d1947eeabb",
          "value": 2472
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-7247 OpenSMTPD Exploit Attempt",
          "properties": null,
          "uuid": "be70afe6-81dc-47cb-ab69-c681b9f32cd8",
          "value": 2473
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-1497 Cisco HyperFlex HX Exploit Attempt",
          "properties": null,
          "uuid": "1975e2f7-754d-4751-a443-117f553dd301",
          "value": 2474
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-1498 Cisco HyperFlex HX Exploit Attempt",
          "properties": null,
          "uuid": "a3559b2a-0729-4900-b9b5-85c79347d878",
          "value": 2475
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-21972 VMware vCenter Exploit",
          "properties": null,
          "uuid": "9068600d-828a-4c29-9a74-9aab4beb9314",
          "value": 2476
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-21972 VMware vCenter Scan",
          "properties": null,
          "uuid": "cb6f0850-0e15-4e1e-a4c5-cbc23944ee81",
          "value": 2477
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-21974 VMware ESXi OpenSLP Exploit Attempt",
          "properties": null,
          "uuid": "c486e93c-2d5b-495c-b85a-13551869a4d2",
          "value": 2478
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-21985 VMware vCenter Exploit",
          "properties": null,
          "uuid": "4993919d-e9b9-4422-886b-4594d458e753",
          "value": 2479
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22005 VMware vCenter Exploit",
          "properties": null,
          "uuid": "f822edd8-66ea-4672-a7b0-1a326786023c",
          "value": 2480
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22006 VMware vCenter Exploit",
          "properties": null,
          "uuid": "3ceec9fc-4872-4aa9-ad9f-83e550818edf",
          "value": 2481
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22205 GitLab CE and EE Exploit Attempt",
          "properties": null,
          "uuid": "3ff232b0-921d-4168-96f5-68efa647bcba",
          "value": 2482
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22893 Pulse Connect Secure Exploit Attempt",
          "properties": null,
          "uuid": "6997dbad-6e16-4b6a-8cda-07a0655f494a",
          "value": 2483
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22986 F5 BIG-IP and BIG-IQ Exploit",
          "properties": null,
          "uuid": "777b970e-4ba2-4b57-a05b-06cbc6118f21",
          "value": 2484
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-22991 F5 BIG-IP Exploit",
          "properties": null,
          "uuid": "1dcd461e-9546-4414-892a-f785c099a914",
          "value": 2485
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-26084 Atlassian Confluence Exploit Attempt",
          "properties": null,
          "uuid": "6d29fe79-7801-4e9f-a28a-5f9689b66b23",
          "value": 2486
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-26432 Windows NFS ONCRPC Exploit Attempt",
          "properties": null,
          "uuid": "bd2a55a6-8929-4533-a2e3-78e07b946869",
          "value": 2487
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-26877 Windows DNS Server Exploit Attempt",
          "properties": null,
          "uuid": "1584a462-98d0-413f-92d8-6bbbacdb45bf",
          "value": 2488
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-26897 Windows DNS Server Exploit Attempt",
          "properties": null,
          "uuid": "14cefe3a-964c-4591-a87b-10446d21bcf1",
          "value": 2489
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-28324 Windows 10 SMBv3 Exploit Attempt",
          "properties": null,
          "uuid": "3ef58857-984b-4bdf-b570-844f9349e331",
          "value": 2490
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-31166 Windows HTTP Stack Exploit Attempt",
          "properties": null,
          "uuid": "17362c94-8bec-4421-b2a4-1a745f507400",
          "value": 2491
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-31181 Microsoft SharePoint Exploit Attempt",
          "properties": null,
          "uuid": "d1be1c3c-a6bc-4cf4-9509-41dfa5f832c5",
          "value": 2492
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-34467 Microsoft SharePoint Exploit Attempt",
          "properties": null,
          "uuid": "6c955691-50c9-4e26-9d47-4a5dd8cd8238",
          "value": 2493
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-34473 Microsoft Exchange Server Exploit",
          "properties": null,
          "uuid": "08f1700a-9409-4f93-afb2-8f455014b1f4",
          "value": 2494
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-34527 Windows Print Spooler Exploit Attempt",
          "properties": null,
          "uuid": "e0f4faad-d0bc-4b9c-8d59-96561f6b010e",
          "value": 2495
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-35394 Realtek SDK Exploit Attempt",
          "properties": null,
          "uuid": "f094c415-05f1-43ed-9ab2-e726f75481e2",
          "value": 2496
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-35395 Realtek SDK Exploit Attempt",
          "properties": null,
          "uuid": "e1bfe9c1-6238-4bd0-8d3e-652bda277461",
          "value": 2497
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-38647 OMIGOD Exploit",
          "properties": null,
          "uuid": "d87c29f1-e1fd-4470-bfed-41b4dd5f8db9",
          "value": 2498
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-42321 Microsoft Exchange Exploit Attempt",
          "properties": null,
          "uuid": "5e2411f8-73a7-455b-b993-2fe1814b632a",
          "value": 2499
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2021-43798 Grafana Exploit Attempt",
          "properties": null,
          "uuid": "61672696-0e73-4424-aeb5-f059c3f79674",
          "value": 2500
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Log4Shell JNDI Injection Attempt",
          "properties": null,
          "uuid": "a166dfb5-c9dd-4e77-ba4f-0c547b6d40aa",
          "value": 2501
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Outbound Log4Shell Activity",
          "properties": null,
          "uuid": "f7794767-d800-4a01-955d-e28bb41779b5",
          "value": 2502
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-0543 Redis Exploit",
          "properties": null,
          "uuid": "5f52f645-a759-4b7a-a9c6-edd6026de8c8",
          "value": 2503
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-1388 F5 BIG-IP Exploit",
          "properties": null,
          "uuid": "ca45d55c-6461-4307-a164-8afef50dde52",
          "value": 2504
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-21907 Windows HTTP Stack Exploit Attempt",
          "properties": null,
          "uuid": "e3f035fc-6d0c-4c8a-b9ae-250226133b7b",
          "value": 2505
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-22947 Spring Cloud Gateway Exploit Attempt",
          "properties": null,
          "uuid": "3945e500-126c-4406-927b-b037b9cd5838",
          "value": 2506
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-22963 Spring Cloud Function Exploit Attempt",
          "properties": null,
          "uuid": "a53aab60-0236-4afe-94d3-94494d30936e",
          "value": 2507
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Brute Force",
          "properties": null,
          "uuid": "048c293f-4636-4f78-8055-f14a3cb5069c",
          "value": 2508
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Enumeration",
          "properties": null,
          "uuid": "7f7c22a9-43ad-407f-9f39-78f75fa5c225",
          "value": 2509
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Issues",
          "properties": null,
          "uuid": "5b10213b-5e7a-4258-a0e9-6a27e9e75c3b",
          "value": 2510
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Takeover Attack",
          "properties": null,
          "uuid": "1a8cacce-14d3-43ab-962e-d776183a1aae",
          "value": 2511
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Database Transaction Failures",
          "properties": null,
          "uuid": "ecd5c3cc-26e8-447e-8159-b2f584d05502",
          "value": 2512
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VPN Client Data Exfiltration",
          "properties": null,
          "uuid": "e83a55d5-dcab-4a61-82bc-550e7d4de4a6",
          "value": 2513
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Data Exfiltration",
          "properties": null,
          "uuid": "21967f48-608b-4416-be14-b704f808391f",
          "value": 2514
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Data Transfer Issues",
          "properties": null,
          "uuid": "7687fc73-692b-4982-9185-a8c86594cf32",
          "value": 2515
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Poor Database Performance",
          "properties": null,
          "uuid": "f9489d81-535d-487e-bdcd-036aef9eb4c5",
          "value": 2516
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DCOM Remote Command Launch",
          "properties": null,
          "uuid": "988cd110-b0f7-4c28-875d-854d3311bec4",
          "value": 2517
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DCShadow Attack",
          "properties": null,
          "uuid": "94a74f58-959e-4eea-8241-20f2e4b45fb5",
          "value": 2518
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DCSync Attack",
          "properties": null,
          "uuid": "8c761151-dd77-4e55-9337-e0eb11baad98",
          "value": 2519
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Citrix Data Transfer",
          "properties": null,
          "uuid": "18607c4e-6d49-4be9-a0bf-7281dd0ff05e",
          "value": 2520
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Database Data Transfer",
          "properties": null,
          "uuid": "9fdb0046-7bc5-4fdf-a801-e8c51799bda1",
          "value": 2521
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Data Transfer",
          "properties": null,
          "uuid": "aa0e06a8-e034-43e5-97e4-a9538cb8ccc0",
          "value": 2522
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Email Data Transfer",
          "properties": null,
          "uuid": "3ad40a60-6253-42d7-92a2-d762abd24c5b",
          "value": 2523
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed FTP Data Transfer",
          "properties": null,
          "uuid": "ef199948-7562-449e-a7ea-83ff48ba8c29",
          "value": 2524
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed HTTP Data Transfer",
          "properties": null,
          "uuid": "c1e99761-9d0d-4845-8a13-2bd1096bceb0",
          "value": 2525
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed IP Address Configuration",
          "properties": null,
          "uuid": "6a314f44-3c70-460a-9efb-390f92c7f47d",
          "value": 2526
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Kerberos Auth",
          "properties": null,
          "uuid": "e6518a67-0a1d-4637-9da4-38061eaec51c",
          "value": 2527
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Kerberos Data Transfer",
          "properties": null,
          "uuid": "7cd8906a-e5d1-41dd-b2e8-ba14ec03d50f",
          "value": 2528
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed LDAP Auth",
          "properties": null,
          "uuid": "5e5514ad-2410-4359-8caa-0d2eb8b840a8",
          "value": 2529
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed LDAP Data Transfer",
          "properties": null,
          "uuid": "08e481e0-0c3a-4f9d-92c8-980c7fbfb871",
          "value": 2530
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Memcache Data Transfer",
          "properties": null,
          "uuid": "042adccd-d55c-441a-9348-3c5870ab4aea",
          "value": 2531
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Redis Data Transfer",
          "properties": null,
          "uuid": "993b46f5-3f2b-4ffc-954b-80c9204375c7",
          "value": 2532
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed Web Services",
          "properties": null,
          "uuid": "d343f42f-125f-4fe5-a634-092129398450",
          "value": 2533
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Delayed WiFi Auth",
          "properties": null,
          "uuid": "7a01b1cb-938f-428d-93ee-0bc0272178d3",
          "value": 2534
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DHCP Decline Error",
          "properties": null,
          "uuid": "a740e9f8-22d2-4653-8fd3-3dffada9043a",
          "value": 2535
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DHCP Errors",
          "properties": null,
          "uuid": "9b09240c-0c0d-4d5d-98bb-14bb65c66ffd",
          "value": 2536
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DHCP Issues",
          "properties": null,
          "uuid": "ae15338f-48b2-4a73-8eed-12864655c20c",
          "value": 2537
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DHCP Restart Error",
          "properties": null,
          "uuid": "aebc1e57-d46f-4cc4-998e-201a538176a3",
          "value": 2538
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Brute Force",
          "properties": null,
          "uuid": "2b9c5200-ca7f-4d57-b49e-f05a71d01b68",
          "value": 2539
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Errors",
          "properties": null,
          "uuid": "bdd48d7a-5047-4be1-aae6-b819c2302154",
          "value": 2540
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Internal Reverse Lookup Scan",
          "properties": null,
          "uuid": "978a8261-53d2-4729-96b2-a84ab21dd253",
          "value": 2541
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Issues",
          "properties": null,
          "uuid": "4f61bd58-68c2-4457-9f6d-8c6e1962762f",
          "value": 2542
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Lookup Failures",
          "properties": null,
          "uuid": "c2a26140-81d4-4280-b0c4-92830711b5de",
          "value": 2543
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Rebinding",
          "properties": null,
          "uuid": "bafdb0b3-710f-4003-9579-075ef8799aca",
          "value": 2544
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Request Timeouts",
          "properties": null,
          "uuid": "e974946b-deeb-4210-8503-ccfbcfff720e",
          "value": 2545
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Timeouts",
          "properties": null,
          "uuid": "c39c1fa3-a988-4e9c-b7cc-82fc9c774686",
          "value": 2546
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Tunnel",
          "properties": null,
          "uuid": "8fd30811-a38f-48d4-85e4-14886625b3bd",
          "value": 2547
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Zone Transfer",
          "properties": null,
          "uuid": "5c9cdeca-45af-4664-a4cf-6f8208e985ff",
          "value": 2548
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Fronting",
          "properties": null,
          "uuid": "a7423aec-5167-4322-b2c9-197c499c91fb",
          "value": 2549
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Generation Algorithm",
          "properties": null,
          "uuid": "0c0160d1-b7e7-488f-a29e-712fd6a64c64",
          "value": 2550
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DGA Domain Resolution",
          "properties": null,
          "uuid": "67ed656c-dca4-41e7-909d-4507c89a8f68",
          "value": 2551
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DGA Domain Queries",
          "properties": null,
          "uuid": "a2ae7861-b0ac-4548-9985-5e8ad895cc48",
          "value": 2552
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Trust Enumeration",
          "properties": null,
          "uuid": "ea89babf-c08f-43c0-88cc-008a94552cf0",
          "value": 2553
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Trusts Enumeration",
          "properties": null,
          "uuid": "9e79d3df-3491-40aa-b5c2-60ec8707f8e4",
          "value": 2554
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DoublePulsar RDP Implant",
          "properties": null,
          "uuid": "6aa2233c-096c-47e8-81c6-e11c7aa88942",
          "value": 2555
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DoublePulsar RDP Scan",
          "properties": null,
          "uuid": "8234bcab-bfb9-4b45-bb0c-c2ddac3bf0e9",
          "value": 2556
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DoublePulsar SMB/CIFS Implant Activity",
          "properties": null,
          "uuid": "3fb12ffe-985d-460b-b425-16b1bff0bddb",
          "value": 2557
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DoublePulsar SMB/CIFS Scan",
          "properties": null,
          "uuid": "60c463fb-f7a9-488f-b8c2-7d8f5fb2c880",
          "value": 2558
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Errors",
          "properties": null,
          "uuid": "ff52b5bf-a57f-42ba-ba87-7e2558b13075",
          "value": 2559
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Issues",
          "properties": null,
          "uuid": "af8ab461-b546-4a2d-ac6f-d63d8c86f3f7",
          "value": 2560
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Mailbox Unavailable Error",
          "properties": null,
          "uuid": "00a1b087-f45a-4cfd-8e99-573b44214ed8",
          "value": 2561
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Service Unavailable Error",
          "properties": null,
          "uuid": "f149dd2a-be63-4d77-ba83-e87239366d34",
          "value": 2562
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Empire C\u0026C HTTP Connection",
          "properties": null,
          "uuid": "7187ff21-dc81-4c2a-95bb-f48e3988e697",
          "value": 2563
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Empire C\u0026C SSL/TLS Connection",
          "properties": null,
          "uuid": "fdadbc72-06bb-49b2-9b04-66e96d57ae10",
          "value": 2564
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "EternalBlue Exploit",
          "properties": null,
          "uuid": "bc7f2970-a8f3-4a64-a506-3356b2cecfaa",
          "value": 2565
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overlapping IP Fragmentation",
          "properties": null,
          "uuid": "bfff4bba-ce6f-427d-85f7-67d348b33501",
          "value": 2566
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Experimental Detection",
          "properties": null,
          "uuid": "c1bcfd3c-bcd2-4502-bfe2-653ae14805c0",
          "value": 2567
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Experimental Detection for Protocol Activity",
          "properties": null,
          "uuid": "d917dc0b-87b0-4077-b08e-7da6ad9e743c",
          "value": 2568
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Experimental Detection for a Single Metric",
          "properties": null,
          "uuid": "4d882f7c-5f5e-4409-a9bd-7ed055661e73",
          "value": 2569
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Experimental Detection for a Single Source",
          "properties": null,
          "uuid": "72262ea3-1ae7-45a6-b3dd-e7fdf8b6ee8e",
          "value": 2570
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Expired SSL Server Certificates",
          "properties": null,
          "uuid": "ab9ac255-ff96-4294-8806-a50632fa56d9",
          "value": 2571
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Request to External Database Server",
          "properties": null,
          "uuid": "98fccd31-698d-4c46-a7e0-4553fab3ee11",
          "value": 2572
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Executable File Download",
          "properties": null,
          "uuid": "ecba9dc6-ea5a-4895-ab6d-c09c635902a1",
          "value": 2573
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Request to External LDAP Server",
          "properties": null,
          "uuid": "8681ef54-d0c7-4ca2-bc3d-a8df3a807520",
          "value": 2574
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Request to External NFS Server",
          "properties": null,
          "uuid": "a3f874d4-cc1b-4b84-be73-fdb20d8acf31",
          "value": 2575
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New SSH Device",
          "properties": null,
          "uuid": "ce580d3f-7026-4f9c-b362-6c1216353213",
          "value": 2576
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "File Access Failure",
          "properties": null,
          "uuid": "835b2520-f637-4ff9-b59d-17aa2bd88734",
          "value": 2577
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Access Denied Error",
          "properties": null,
          "uuid": "d65ff174-f4c1-4b64-96d8-120d70cfe8b2",
          "value": 2578
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Bad Syntax Error",
          "properties": null,
          "uuid": "c6181711-f4c5-4c5b-9ed1-8708a80553b8",
          "value": 2579
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Brute Force",
          "properties": null,
          "uuid": "01822d6c-400e-460d-960b-49635277d1bc",
          "value": 2580
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Errors",
          "properties": null,
          "uuid": "cf97f1ee-12ad-493d-9fb6-b54d780d2c31",
          "value": 2581
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP File Transfer Issues",
          "properties": null,
          "uuid": "a7c8b90e-8dbf-48c6-a2e5-d5f97fae0947",
          "value": 2582
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Not Logged in Error",
          "properties": null,
          "uuid": "23ffc049-7526-4408-812c-a08a915e20d3",
          "value": 2583
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Hacking Tool Domain Access",
          "properties": null,
          "uuid": "e232011a-c076-406d-9fdc-f0f98ea90bf8",
          "value": 2584
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High Citrix Latency",
          "properties": null,
          "uuid": "034a66d6-5cc5-48a9-8910-8cff8e6cbe36",
          "value": 2585
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP 400 Status Codes",
          "properties": null,
          "uuid": "d5d33f35-2e28-4e0d-bd53-22db868fe495",
          "value": 2586
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Bad Requests",
          "properties": null,
          "uuid": "bf7b7f76-f89a-4f95-bca1-7160289475b5",
          "value": 2587
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Desync Attack",
          "properties": null,
          "uuid": "0cf0918b-5f88-493c-89aa-272249efe17f",
          "value": 2588
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Errors",
          "properties": null,
          "uuid": "b3562d11-25df-49d0-a974-851866814961",
          "value": 2589
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Forbidden",
          "properties": null,
          "uuid": "f7c26a90-3a2c-49ba-b10e-d8a20528334e",
          "value": 2590
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Gateway Timeout Error",
          "properties": null,
          "uuid": "c503f81f-fc5e-457b-9b96-e737f9e65fe0",
          "value": 2591
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Internal Error",
          "properties": null,
          "uuid": "fd9f6bda-3d7b-4725-b3ed-34a02fd6dcd6",
          "value": 2592
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Method Scan",
          "properties": null,
          "uuid": "9a4601b9-cc6a-4616-95f9-8d8934b5882f",
          "value": 2593
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Not Found",
          "properties": null,
          "uuid": "8bbcc8fc-3aaf-41a6-b2b1-a5f5c20bb48a",
          "value": 2594
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Path Traversal",
          "properties": null,
          "uuid": "a7caac49-cc0f-4876-a9c5-aa482162281c",
          "value": 2595
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Credentials Sent over HTTP",
          "properties": null,
          "uuid": "e96db057-da3e-4b59-b59b-1d640920fe56",
          "value": 2596
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Credentials Received over HTTP",
          "properties": null,
          "uuid": "fbe3e095-b54e-4d7d-aeb2-019b8bb461bb",
          "value": 2597
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Service Unavailable Error",
          "properties": null,
          "uuid": "c50d2f6b-aec6-4c93-b2c4-08d837fa4946",
          "value": 2598
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ICMP Tunnel",
          "properties": null,
          "uuid": "7c311766-e266-4c4f-b4c9-1fc283b3d400",
          "value": 2599
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound Connection from a Cobalt Strike IP Address",
          "properties": null,
          "uuid": "d6ee4c8a-0de9-4567-9050-3b211fd3d6de",
          "value": 2600
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound Tor Node Connections",
          "properties": null,
          "uuid": "39adf841-aed0-4b55-83fe-8407e9d2018a",
          "value": 2601
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Interactive Traffic from a Remote Desktop",
          "properties": null,
          "uuid": "86747cb4-b4ef-40fb-8398-bd0e04910d95",
          "value": 2602
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Interactive Traffic from an External Endpoint",
          "properties": null,
          "uuid": "a08b110b-cf71-4c0d-8363-09dc63a81eec",
          "value": 2603
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Remote Control SSH Traffic",
          "properties": null,
          "uuid": "a4d15eea-e185-4587-b91d-726bd0cec04c",
          "value": 2604
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Interrupted Citrix Data Transfer",
          "properties": null,
          "uuid": "afce3381-23da-49b4-99f4-f783beb78b0c",
          "value": 2605
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Default Kali Linux SSH Keys",
          "properties": null,
          "uuid": "0cffc8a0-de7b-4ee8-870a-b51c7eb884bb",
          "value": 2606
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "REvil C\u0026C Activity (Kaseya Supply Chain)",
          "properties": null,
          "uuid": "6ae0848a-6d6f-4e30-8f14-ab259ca50904",
          "value": 2607
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "REvil Suspicious Connection (Kaseya Supply Chain)",
          "properties": null,
          "uuid": "a55adf6d-6c95-42a4-8366-4230b1ad3bc2",
          "value": 2608
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kaseya VSA Activity",
          "properties": null,
          "uuid": "50dec13e-5799-4198-a309-3cb03bf6eeaa",
          "value": 2609
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Attack Tool Activity",
          "properties": null,
          "uuid": "169e01ce-56c6-4ec3-a1cf-a8b8ca42bd69",
          "value": 2610
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Auth Errors",
          "properties": null,
          "uuid": "a2f372b2-e3b3-4a34-89f6-8afee6a26b08",
          "value": 2611
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Auth Issues",
          "properties": null,
          "uuid": "97c045f5-b8a1-4f1b-8c5b-2a873849c751",
          "value": 2612
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Brute Force",
          "properties": null,
          "uuid": "4c5e8e13-5718-4e8f-8b41-d0853944ed38",
          "value": 2613
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Duplicate Sessions Errors",
          "properties": null,
          "uuid": "5493a0eb-169b-42bc-9d5d-0a85499edecd",
          "value": 2614
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Expired Password Errors",
          "properties": null,
          "uuid": "1c202641-e5b6-47da-85d8-963f4c489e27",
          "value": 2615
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Golden Ticket Attack",
          "properties": null,
          "uuid": "48b72646-a158-4282-bfeb-69efed383b1c",
          "value": 2616
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Invalid Ticket Errors",
          "properties": null,
          "uuid": "f3583f15-0e04-4b5c-ae1f-6769c10efae6",
          "value": 2617
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Policy Errors",
          "properties": null,
          "uuid": "4a56b668-e729-4e95-b8bc-9a153499b82f",
          "value": 2618
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Revoked Credentials Errors",
          "properties": null,
          "uuid": "ebdeaf88-0241-44da-b4d2-a551d1fb48f0",
          "value": 2619
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Service Unknown Errors",
          "properties": null,
          "uuid": "47d8e326-c930-435b-a6a3-f5667aaa5be7",
          "value": 2620
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Silver Ticket Attack",
          "properties": null,
          "uuid": "c7a2c6f3-8c07-4263-bc61-3a2bcfd662e3",
          "value": 2621
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Sync Errors",
          "properties": null,
          "uuid": "2d04b5f4-48f7-4ad3-af7e-3e3c803c716d",
          "value": 2622
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Ticket Errors",
          "properties": null,
          "uuid": "7145ca7b-7768-4be3-82b7-421e715a746f",
          "value": 2623
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Unknown Service Errors",
          "properties": null,
          "uuid": "5214ea3c-99ba-49b5-98c2-f10108568a3e",
          "value": 2624
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos User Enumeration",
          "properties": null,
          "uuid": "a7dfe7b4-d9cb-4ac4-b8d4-5a54f052b98c",
          "value": 2625
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Kerberos Wrong Password Errors",
          "properties": null,
          "uuid": "7ee58334-455c-4c6f-a2c5-0f61b2420630",
          "value": 2626
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "AS-REP Roasting Activity",
          "properties": null,
          "uuid": "74f001c7-faa8-429b-9228-feb26682912f",
          "value": 2627
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Auth Error",
          "properties": null,
          "uuid": "b58a6fcd-950a-4d78-9cee-a9fcf9374602",
          "value": 2628
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Auth Errors",
          "properties": null,
          "uuid": "33221f34-71d3-46ad-81e3-48128a34b9a3",
          "value": 2629
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Auth Issues",
          "properties": null,
          "uuid": "b140725e-b214-45e9-8488-09df6d11d088",
          "value": 2630
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Wildcard Query",
          "properties": null,
          "uuid": "8633c425-073e-49a3-ad3f-c372bf8f2a38",
          "value": 2631
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Computer Enumeration",
          "properties": null,
          "uuid": "891a035f-6323-46bf-ac9a-bb994c1fade4",
          "value": 2632
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP GPO Enumeration",
          "properties": null,
          "uuid": "1d81decd-c688-40a8-8879-a7bcf458fe9c",
          "value": 2633
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Invalid Credentials Error",
          "properties": null,
          "uuid": "9544ac08-2cf5-40be-9d88-f0162d252edd",
          "value": 2634
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All Object Enumeration",
          "properties": null,
          "uuid": "e185497a-26d6-4b0a-a115-ccfd2703f0c3",
          "value": 2635
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Operational Error",
          "properties": null,
          "uuid": "e6920214-8f7c-4dc7-a063-c756155f13df",
          "value": 2636
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP Protocol Error",
          "properties": null,
          "uuid": "2bd18456-f6c7-4a38-87c4-bdef6052aab6",
          "value": 2637
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LDAP SPN Scan",
          "properties": null,
          "uuid": "f7282a5b-9a35-49e5-8afa-dbcca1791d1e",
          "value": 2638
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "LLMNR Poisoning",
          "properties": null,
          "uuid": "e439ef9a-c115-4b32-b6ef-d4a487d6b74e",
          "value": 2639
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Windows Account Enumeration",
          "properties": null,
          "uuid": "f9d61eb0-4315-4814-ba8a-372d29a5ea73",
          "value": 2640
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Memcache Errors",
          "properties": null,
          "uuid": "b5c44ca4-30c7-4385-b4af-12d186268285",
          "value": 2641
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Memcache Issues",
          "properties": null,
          "uuid": "dcb59bdc-493d-4327-b28a-cc143b589f60",
          "value": 2642
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Meterpreter C\u0026C Session",
          "properties": null,
          "uuid": "2a75eb9b-e958-402f-9488-59dc46f37196",
          "value": 2643
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Microsoft Exchange Server SSRF and RCE Exploit",
          "properties": null,
          "uuid": "29cd890d-5c80-4988-84db-432435166fba",
          "value": 2644
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Metasploit C\u0026C SSL/TLS Connection",
          "properties": null,
          "uuid": "d8e796ff-d37b-45a4-af6c-18d0630127f7",
          "value": 2645
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Remote Admin Connection Requests",
          "properties": null,
          "uuid": "e2224c46-3c42-4678-8bbb-b6fe53fa1555",
          "value": 2646
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Alias Member Enumeration",
          "properties": null,
          "uuid": "24f5e845-7440-4a83-b863-79b395ac6ed8",
          "value": 2647
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Controller Enumeration",
          "properties": null,
          "uuid": "1a7178ab-89af-488c-85bb-7e6fa0bdbd36",
          "value": 2648
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Group Member Enumeration",
          "properties": null,
          "uuid": "0ef518e7-1d73-4413-b6d2-24652c4ad9a8",
          "value": 2649
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Logged-On User Enumeration",
          "properties": null,
          "uuid": "d612e1d7-6b07-4be8-bad9-bffdcaf8baae",
          "value": 2650
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "User Session Enumeration",
          "properties": null,
          "uuid": "1d429e23-7fc4-47ab-b006-1ff87d87f00c",
          "value": 2651
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Network Share Enumeration",
          "properties": null,
          "uuid": "c72abc77-a0bf-4da6-b8e0-1adba7a9fefd",
          "value": 2652
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RDP Session Enumeration",
          "properties": null,
          "uuid": "cbd08dc2-94cb-4312-a128-53522c366035",
          "value": 2653
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Windows Registry Enumeration",
          "properties": null,
          "uuid": "cb4fae78-6664-4f7b-85c6-8a1ffd173d49",
          "value": 2654
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Scheduled Task Activity (ATSVC)",
          "properties": null,
          "uuid": "e2060a51-915f-42e9-a89d-27c697bb736a",
          "value": 2655
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Scheduled Task Activity (ITaskSchedulerService)",
          "properties": null,
          "uuid": "0fac77c2-d00b-4e62-8710-106673dd7232",
          "value": 2656
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Multiple Email Errors",
          "properties": null,
          "uuid": "ec599fa1-0279-4cfc-8442-ebe0b71cf83e",
          "value": 2657
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Multiple FTP Errors",
          "properties": null,
          "uuid": "feb0a16e-703c-4694-bd62-dd4139040e7f",
          "value": 2658
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Multiple Kerberos Authentication Errors",
          "properties": null,
          "uuid": "8d859db3-c548-445b-a24b-e5809819d6a6",
          "value": 2659
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Multiple LDAP Auth Errors",
          "properties": null,
          "uuid": "dd459718-3fd4-4a2e-91e8-f13a3a648415",
          "value": 2660
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Multiple SMB/CIFS Errors",
          "properties": null,
          "uuid": "b20b81e0-57b3-43ce-942a-cbb4f5a0c89b",
          "value": 2661
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NBT-NS Poisoning",
          "properties": null,
          "uuid": "66c31a4c-bcfd-48de-bcf9-12fcc5162d64",
          "value": 2662
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Network Privilege Escalation",
          "properties": null,
          "uuid": "d2828028-0c85-4682-9e2b-92e294d4db09",
          "value": 2663
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New Active Directory Web Service (ADWS) Activity",
          "properties": null,
          "uuid": "488766ab-fdec-406a-8d3c-fe58fb61a35d",
          "value": 2664
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New DHCP Activity",
          "properties": null,
          "uuid": "b99a3e25-f7d1-4dab-917b-7ead0d091ba7",
          "value": 2665
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New DNS over HTTPS (DoH) Activity",
          "properties": null,
          "uuid": "20fa3afb-3813-49e8-8ee4-a3592c345453",
          "value": 2666
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External Connection",
          "properties": null,
          "uuid": "4fe6800a-5391-4623-bad2-14fcdde4f1af",
          "value": 2667
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External Database Connection",
          "properties": null,
          "uuid": "8356bf1c-0a07-4605-bdaf-bb5dd33fa12e",
          "value": 2668
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External IIOP Connection",
          "properties": null,
          "uuid": "0b55600f-b01c-4eb0-9b05-e14869bce795",
          "value": 2669
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External LDAP Connection",
          "properties": null,
          "uuid": "b8c14732-33c9-4e9e-8081-2ab4c9030e6d",
          "value": 2670
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External NFS Connection",
          "properties": null,
          "uuid": "b88b7450-ff3e-4039-a022-c003b1e32b9a",
          "value": 2671
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External RDP Connection",
          "properties": null,
          "uuid": "c3184ce3-6392-4b59-b0a2-ee0babbd587e",
          "value": 2672
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External Java RMI Connection",
          "properties": null,
          "uuid": "576a9a78-bb99-416c-92de-ef2dfa0ab560",
          "value": 2673
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External SSH Connection",
          "properties": null,
          "uuid": "25862212-b580-4c55-9ec5-6bf570b889cc",
          "value": 2674
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External Telnet Connection",
          "properties": null,
          "uuid": "e622ebf4-60b9-4889-9cab-3bb2168319fb",
          "value": 2675
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External VNC Connection",
          "properties": null,
          "uuid": "94634bfe-95fe-4378-848f-8d3fec366352",
          "value": 2676
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New External IoT Connection",
          "properties": null,
          "uuid": "8dbb4146-13ee-4f80-91fa-3d8912ce3f80",
          "value": 2677
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New Local DNS Server Activity",
          "properties": null,
          "uuid": "591f4ad1-9383-46b0-a9e6-e52136912ba3",
          "value": 2678
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New SMB/CIFS Executable File Transfer",
          "properties": null,
          "uuid": "7bd5bb92-ec37-4e16-b461-60d2e32a6124",
          "value": 2679
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New Telnet Activity",
          "properties": null,
          "uuid": "010310ad-2fde-4a6c-ae22-a0a04da421e9",
          "value": 2680
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NFS File Access Failure",
          "properties": null,
          "uuid": "81970455-8a10-486e-9d6f-0ea643997c04",
          "value": 2681
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NTLM Relay Attack",
          "properties": null,
          "uuid": "ff6d582b-c72f-43d0-99b4-b6cf312c8d62",
          "value": 2682
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NTLMv1 Authentication",
          "properties": null,
          "uuid": "95ee98d8-ea98-4f33-908f-9e09f5e09d56",
          "value": 2683
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Numerous Emails",
          "properties": null,
          "uuid": "443f7fee-d0b3-47e5-813d-e8692caf6e7f",
          "value": 2684
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Confirmed OnePercent Group Ransomware IOC",
          "properties": null,
          "uuid": "14fabbfe-d896-4f50-b606-6516d6132631",
          "value": 2685
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Outbound Connection to a Cobalt Strike IP Address",
          "properties": null,
          "uuid": "fa366d03-95ba-499b-b2c5-ee28fbfcc44a",
          "value": 2686
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New Outbound SOCKS Connection",
          "properties": null,
          "uuid": "454ba31d-0210-48ce-bef0-881e4ce0a15a",
          "value": 2687
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Outbound Tor Node Connections",
          "properties": null,
          "uuid": "429ae7d5-5137-4a95-b6b2-9d04da38e1c5",
          "value": 2688
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Citrix Data Transfer",
          "properties": null,
          "uuid": "017824fc-6119-4fa5-a34e-bd081998f5e6",
          "value": 2689
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Database Data Transfer",
          "properties": null,
          "uuid": "d12f7c61-e907-4113-8f20-56de7415c2ec",
          "value": 2690
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Data Transfer",
          "properties": null,
          "uuid": "5062e898-f3f1-46d7-a41e-5c3f53915999",
          "value": 2691
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Email Data Transfer",
          "properties": null,
          "uuid": "9e9ea65d-3344-40bc-8390-7e519ac2c009",
          "value": 2692
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed FTP Data Transfer",
          "properties": null,
          "uuid": "3692dd16-765f-495f-86b7-0dd87ca8aff4",
          "value": 2693
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed HTTP Data Transfer",
          "properties": null,
          "uuid": "ff03e527-49cd-430e-bd2a-4471f47eb049",
          "value": 2694
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Kerberos Data Transfer",
          "properties": null,
          "uuid": "3fb86395-a454-40d9-9c84-1af6ec1a9b08",
          "value": 2695
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed LDAP Data Transfer",
          "properties": null,
          "uuid": "5b03e710-8056-4f57-8226-33ac9f9e8234",
          "value": 2696
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Memcache Data Transfer",
          "properties": null,
          "uuid": "34cff054-53c6-40c5-8c69-01b16d643d80",
          "value": 2697
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Overwhelmed Redis Data Transfer",
          "properties": null,
          "uuid": "ed85f08f-2a06-40c2-a452-9e0a5ea479f6",
          "value": 2698
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Ping Scan",
          "properties": null,
          "uuid": "59e7b87e-a18c-44c3-8621-58d3033e9203",
          "value": 2699
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Poor AAA Performance",
          "properties": null,
          "uuid": "f88472d3-ed01-48cf-bb11-99eb2ba5413d",
          "value": 2700
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Poor DHCP Performance",
          "properties": null,
          "uuid": "6d5f1581-1adf-4db5-ae18-3b20be64f09a",
          "value": 2701
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Poor HTTP Performance",
          "properties": null,
          "uuid": "f9ce5bda-f74e-4daf-a197-23a2d1db5b8b",
          "value": 2702
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Tunnel",
          "properties": null,
          "uuid": "5893a043-9eb2-4def-8441-3c40e394e8c6",
          "value": 2703
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Remote Service Launch",
          "properties": null,
          "uuid": "ebc80242-182c-4541-b831-25d4bc6f63dc",
          "value": 2704
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Ransomware Activity",
          "properties": null,
          "uuid": "f209f857-bafe-46c1-a1cb-3792589c2c04",
          "value": 2705
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Rare Database Table Access",
          "properties": null,
          "uuid": "355f89ea-7670-416a-a543-ef5eb4ca5e38",
          "value": 2706
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Rare SSH Port",
          "properties": null,
          "uuid": "87ddf421-c8e7-45e7-82a0-49b4988f55dd",
          "value": 2707
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RDP Brute Force",
          "properties": null,
          "uuid": "fd0778d2-6731-4379-b7f3-31d365889647",
          "value": 2708
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound Remote Desktop Traffic from an Unusual Location",
          "properties": null,
          "uuid": "7fe698c5-5ebe-49d2-a251-d37d431eec61",
          "value": 2709
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Redis Errors",
          "properties": null,
          "uuid": "fd2979f7-e9d8-4872-a0a7-68e323013731",
          "value": 2710
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Redis Issues",
          "properties": null,
          "uuid": "3b59d169-9f80-464d-8abe-732cfc02c105",
          "value": 2711
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Remote Registry Modification",
          "properties": null,
          "uuid": "fe7d42d9-2253-4510-a7d5-8e9421ae04a3",
          "value": 2712
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Reverse SSH Connection",
          "properties": null,
          "uuid": "6b7cfb9e-aaeb-49f2-815b-fefc24d571c8",
          "value": 2713
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VNC Brute Force",
          "properties": null,
          "uuid": "e4f86075-0eb5-4779-9dd7-ea3ec40ecdb4",
          "value": 2714
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2020-11901 Ripple20 Exploit Attempt",
          "properties": null,
          "uuid": "018e99e9-2a1a-4cad-8563-520e2d03085f",
          "value": 2715
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Ripple20 ICMP Scan",
          "properties": null,
          "uuid": "c1e1efa6-f571-4655-ac15-c715d97c2021",
          "value": 2716
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Treck TCP/IP Network Stack Detected",
          "properties": null,
          "uuid": "d7de5656-9f12-4258-b158-2849ce9a52c1",
          "value": 2717
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Ripple20 IP in IP Exploit Attempt",
          "properties": null,
          "uuid": "250c153a-a5c3-48c0-aed3-9b348557dae9",
          "value": 2718
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Remote Log Deletion",
          "properties": null,
          "uuid": "80bc31d1-a948-49c8-8524-f18cf498e550",
          "value": 2719
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Remote System Shutdown",
          "properties": null,
          "uuid": "8c83996c-6425-4dbb-aa11-6d147d2cba0d",
          "value": 2720
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Admin Enumeration",
          "properties": null,
          "uuid": "502eb440-8f55-461a-b360-98473269c188",
          "value": 2721
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Group Enumeration",
          "properties": null,
          "uuid": "00596926-c67f-4ed0-b393-4bd5a29256ec",
          "value": 2722
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain User Enumeration",
          "properties": null,
          "uuid": "fcd1b7d9-bccb-4415-aedd-189b9e9110f8",
          "value": 2723
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Workstation Enumeration",
          "properties": null,
          "uuid": "a0ebef3a-11cf-4c0d-a533-5cde0e837c18",
          "value": 2724
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Local Admin Enumeration",
          "properties": null,
          "uuid": "4f7a5106-bd9f-4c2a-9b2d-0eaab811b2e4",
          "value": 2725
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Local User Enumeration",
          "properties": null,
          "uuid": "642850ad-67ac-4224-a80e-a9237e695f66",
          "value": 2726
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Scheduled Task Enumeration",
          "properties": null,
          "uuid": "66b0614a-fc3c-4c1a-ad27-f9dd6f0ba7f3",
          "value": 2727
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Sensitive Data Transfer",
          "properties": null,
          "uuid": "6fceaa4c-47a0-4c0e-80fd-1883c754b4c8",
          "value": 2728
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Shellshock DHCP Exploit Attempt",
          "properties": null,
          "uuid": "2bf8f5a7-a3a8-44a3-906e-2930e7e73e75",
          "value": 2729
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Shellshock HTTP Exploit Attempt",
          "properties": null,
          "uuid": "2e097735-fa2f-4329-b2f7-fbd464a5297e",
          "value": 2730
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SIP Brute Force",
          "properties": null,
          "uuid": "e6ee89e2-db7a-46f8-8166-355cda54f25b",
          "value": 2731
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "File Transfer to Windows Autostart Path",
          "properties": null,
          "uuid": "4ff9c896-abb6-4287-ab8f-ff67d62f97b5",
          "value": 2732
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Access Denied Errors",
          "properties": null,
          "uuid": "2023800f-499a-41e2-9f4a-1c7a770caa41",
          "value": 2733
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Brute Force",
          "properties": null,
          "uuid": "c9ad3738-0ced-4d7c-859a-852a2fcb3a12",
          "value": 2734
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Errors",
          "properties": null,
          "uuid": "4ab0884a-1472-41cc-ac8f-7d1ff4f1ba2f",
          "value": 2735
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS File Access Failure",
          "properties": null,
          "uuid": "4447acbb-f0c5-4897-b096-9c71edd21e90",
          "value": 2736
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Privileged Pipe",
          "properties": null,
          "uuid": "0fc143dc-e7c1-472b-a8ad-a51b97176c52",
          "value": 2737
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Share Enumeration",
          "properties": null,
          "uuid": "ba6aee9d-8209-4df4-b0c4-b464dc747948",
          "value": 2738
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Account Errors",
          "properties": null,
          "uuid": "d6c4586b-58fb-4387-b8e2-9bc8bafdc4f8",
          "value": 2739
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Named Pipe Beaconing",
          "properties": null,
          "uuid": "80c75937-4a01-417a-a9bb-23230c6df528",
          "value": 2740
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Email Domain Length",
          "properties": null,
          "uuid": "1cbee7b3-22f8-4169-ad47-76fa868485c8",
          "value": 2741
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Poor SMTP Server Performance",
          "properties": null,
          "uuid": "b7f09851-4bd7-4ce9-b9cc-b7d09a125027",
          "value": 2742
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMTP Syntax Error",
          "properties": null,
          "uuid": "b1772b89-80c9-453f-9a34-b321a3caa8ed",
          "value": 2743
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in Email Traffic Volume",
          "properties": null,
          "uuid": "2d67cacc-c072-43c2-a07a-37907189b57c",
          "value": 2744
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in LDAP Requests",
          "properties": null,
          "uuid": "36f19923-d3be-4167-be13-d6691bff68f4",
          "value": 2745
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in RDP Sessions",
          "properties": null,
          "uuid": "f43e986c-4388-4e0d-890d-e53690433bd0",
          "value": 2746
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in VNC Sessions",
          "properties": null,
          "uuid": "76c2bde9-dfaf-41ad-8e9c-2e79e6bc7de7",
          "value": 2747
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Transaction Delays",
          "properties": null,
          "uuid": "1cbd5d57-a95c-4d06-8d9f-60fbf42f2ef4",
          "value": 2748
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in SSH Sessions",
          "properties": null,
          "uuid": "b1f045dc-ec76-4bc7-8bfd-d3a33622af81",
          "value": 2749
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spike in Telnet Connections",
          "properties": null,
          "uuid": "9e9f6f48-775c-45f3-a460-1a967d7fdba2",
          "value": 2750
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Spoofed SSL/TLS Certificate",
          "properties": null,
          "uuid": "2ae4ae91-7f58-4eb6-87b0-fbee3dedc37c",
          "value": 2751
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "CVE-2022-22965 Spring4Shell Exploit Attempt",
          "properties": null,
          "uuid": "3c5a7d00-89bb-4971-b2ba-cfa37bdb6e4a",
          "value": 2752
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SQL Injection (SQLi) Attack",
          "properties": null,
          "uuid": "9204a63e-a9a1-406d-97f7-bbc805c75dd7",
          "value": 2753
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SSH Brute Force",
          "properties": null,
          "uuid": "47a9ae7b-a6b3-4d9f-9175-00bea2546c9c",
          "value": 2754
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound SSH Traffic from an Unusual Location",
          "properties": null,
          "uuid": "c2f00f8c-d4c9-41dd-9039-f816cf78118f",
          "value": 2755
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Outbound SSH Traffic to an Unusual Location",
          "properties": null,
          "uuid": "04cd985b-3168-4c5c-bc0b-a6a88623b5e2",
          "value": 2756
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SSL Scan",
          "properties": null,
          "uuid": "97424d5b-10bc-47da-8bf7-b07e64885681",
          "value": 2757
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Stalled Data Transfer",
          "properties": null,
          "uuid": "cf74ae17-198a-4934-b943-1e5986ac90a7",
          "value": 2758
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Sudden Decrease in Application Bandwidth",
          "properties": null,
          "uuid": "661a28f7-3c04-4069-a7c6-60c777706528",
          "value": 2759
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Sudden Decrease in Device Bandwidth",
          "properties": null,
          "uuid": "21450449-2535-492a-ab70-59a5c6d25569",
          "value": 2760
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Sudden Decrease in Network Bandwidth",
          "properties": null,
          "uuid": "acfc9561-c6a4-4221-9c02-df4914ebc0e2",
          "value": 2761
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SUNBURST C\u0026C Activity",
          "properties": null,
          "uuid": "2e5d41c1-98d0-49b2-aaad-4e09d9425ab7",
          "value": 2762
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SUPERNOVA Web Shell",
          "properties": null,
          "uuid": "b71820ab-a8e9-45bd-b978-51bd3791750d",
          "value": 2763
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious SMB/CIFS Resource Accessed",
          "properties": null,
          "uuid": "f3205a35-6484-4fc8-96dd-14e826b2b99f",
          "value": 2764
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious External File Download",
          "properties": null,
          "uuid": "d6918155-6012-411f-9aa0-602cbaf739e4",
          "value": 2765
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious Internal File Download",
          "properties": null,
          "uuid": "bb9d02b1-f5e8-4aab-a850-5f8427fb1b7d",
          "value": 2766
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "FTP Data Staging",
          "properties": null,
          "uuid": "16956cf2-c773-42c5-990c-d4aab879ec95",
          "value": 2767
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious FTP Download",
          "properties": null,
          "uuid": "4f6cabf6-68e9-4766-b2d7-710cfc06fbb6",
          "value": 2768
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual HTML Application (HTA) File Download",
          "properties": null,
          "uuid": "8b8f201c-acb2-4038-acde-1f480ea747c4",
          "value": 2769
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious HTTP File Received",
          "properties": null,
          "uuid": "a05a9b6d-b9de-4f43-b587-c261dd537889",
          "value": 2770
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Non-standard HTTP Port",
          "properties": null,
          "uuid": "f9096cdd-16ab-4a08-bc98-3f7de0171ffc",
          "value": 2771
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious JA3 Fingerprint",
          "properties": null,
          "uuid": "d5a9ffb8-afb3-473c-9b00-2b438993f70a",
          "value": 2772
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious New Device Detected",
          "properties": null,
          "uuid": "8ce88e51-a9c2-4c80-b1f9-024519709790",
          "value": 2773
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "NFS Data Staging",
          "properties": null,
          "uuid": "56eec1f2-b3e2-4798-916d-94fa7538458b",
          "value": 2774
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious NFS File Reads",
          "properties": null,
          "uuid": "9cb34e00-dae3-4f08-a026-aca31dabd552",
          "value": 2775
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious NFS File Share Access",
          "properties": null,
          "uuid": "20722405-6315-48ad-beda-e103332a1c4d",
          "value": 2776
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "RDP Attack Tool Activity",
          "properties": null,
          "uuid": "da29777a-cf19-4048-81aa-2b5dd587e0b3",
          "value": 2777
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SMB/CIFS Data Staging",
          "properties": null,
          "uuid": "b72d299a-c64f-4832-a6c2-ce78887bcf31",
          "value": 2778
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious SMB/CIFS File Reads",
          "properties": null,
          "uuid": "e5f6fbb9-4790-4300-8b25-9b821c7da13f",
          "value": 2779
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious SMB/CIFS File Share Access",
          "properties": null,
          "uuid": "60eea1a3-ff4f-488b-b61b-1228fcd49a6c",
          "value": 2780
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual SMB/CIFS Executable File Transfer",
          "properties": null,
          "uuid": "ae3c5349-2063-41d7-b2e9-4763211ca89e",
          "value": 2781
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious SMB/CIFS Named Pipe",
          "properties": null,
          "uuid": "e62cb25b-67db-4405-af8c-aeea8f7495ec",
          "value": 2782
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious Top-level Domain",
          "properties": null,
          "uuid": "b50fb600-c66a-4fe4-b8c4-dab01f05037a",
          "value": 2783
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Suspicious User Agent",
          "properties": null,
          "uuid": "c5cb4ac5-dbc1-493f-b6e5-2e787b878a91",
          "value": 2784
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TCP NULL, FIN, or XMAS Scan",
          "properties": null,
          "uuid": "ab0b973c-0be5-4951-8366-9ca7b1610e8b",
          "value": 2785
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TCP SYN Scan",
          "properties": null,
          "uuid": "c68dce3b-567f-415e-878e-695777326b0c",
          "value": 2786
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TCP Stack Exploit Attempt (Client)",
          "properties": null,
          "uuid": "6c915fca-ae92-4e35-a465-a6e0be5d071c",
          "value": 2787
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "TCP Stack Exploit Attempt (Server)",
          "properties": null,
          "uuid": "bac29dab-1c82-4198-a2f1-6bf4e1cc816a",
          "value": 2788
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Telnet Password",
          "properties": null,
          "uuid": "ccccc001-69ac-40ea-9db4-a50e25c4e91a",
          "value": 2789
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Client Request to a Suspicious Host",
          "properties": null,
          "uuid": "58366b53-b2a7-49b1-b6d4-3cfba3e00714",
          "value": 2790
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Client Request to a Suspicious Host",
          "properties": null,
          "uuid": "ed61da09-786a-4d18-981e-a4273a600cea",
          "value": 2791
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HTTP Client Request to a Suspicious URI",
          "properties": null,
          "uuid": "bf4bff2f-aa49-4158-9639-174249ca21da",
          "value": 2792
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SSL/TLS Connection to a Suspicious Host",
          "properties": null,
          "uuid": "158a6218-0d1b-4e36-99c1-bb2db8d0eece",
          "value": 2793
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound Suspicious Connections",
          "properties": null,
          "uuid": "484c95c0-0183-42f7-9e86-aef8dbd82bd2",
          "value": 2794
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Outbound Suspicious Connection",
          "properties": null,
          "uuid": "5e708c6d-3f5c-4274-bd17-8114ebc0e460",
          "value": 2795
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Apache Tomcat JSP Exploit Attempt",
          "properties": null,
          "uuid": "42e58605-98e4-4d96-8dd3-296adc0ce920",
          "value": 2796
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "UDP Port Scan",
          "properties": null,
          "uuid": "04ea622a-3bc6-4cdb-9fa7-fb8308237aad",
          "value": 2797
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unapproved Cloud Service Access",
          "properties": null,
          "uuid": "1a4afd29-09d9-4ff7-8487-53c48b6b3f65",
          "value": 2798
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unauthorized Caller Error",
          "properties": null,
          "uuid": "3a079434-f6d0-4763-884a-ba283942f188",
          "value": 2799
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional Data Transfer",
          "properties": null,
          "uuid": "8fc6eb8e-01e2-454f-8ffa-b9b72ace5714",
          "value": 2800
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional External Connection",
          "properties": null,
          "uuid": "d88c580b-c3ab-4b26-becb-f901f1a376bf",
          "value": 2801
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional Internal Connection",
          "properties": null,
          "uuid": "acfe29f2-700b-4853-937d-dff62b2e64e0",
          "value": 2802
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional Protocol Communication",
          "properties": null,
          "uuid": "4f6a59b9-02a3-40a8-9040-49bfde7a0da7",
          "value": 2803
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional RDP Behavior",
          "properties": null,
          "uuid": "d27a69e5-f2f2-4aa8-821b-d6ca16b197fe",
          "value": 2804
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional RDP Data Transfer",
          "properties": null,
          "uuid": "372ccc17-b56b-4fa4-9192-d935f4a753d5",
          "value": 2805
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional VNC Behavior",
          "properties": null,
          "uuid": "7476947a-e83f-4c6d-b036-845d5c4c7120",
          "value": 2806
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional VNC Data Transfer",
          "properties": null,
          "uuid": "bd695024-8d69-45d5-9f34-2584ae67d6e1",
          "value": 2807
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional SMB/CIFS Data Transfer",
          "properties": null,
          "uuid": "7c3d4e4c-6e66-4ccf-b519-77a3f2e5e1bc",
          "value": 2808
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional SSH Behavior",
          "properties": null,
          "uuid": "a582406d-1f8e-4820-a489-8ca59cc62fac",
          "value": 2809
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional SSH Data Transfer",
          "properties": null,
          "uuid": "10286a6b-41ec-4862-a998-c90866bcd7c5",
          "value": 2810
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unconventional Telnet Data Transfer",
          "properties": null,
          "uuid": "598a13c6-2f24-4996-a583-5520a22060ab",
          "value": 2811
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unencrypted Zoom Data",
          "properties": null,
          "uuid": "df3720ad-35a4-4189-ae7c-36c26b6d38c3",
          "value": 2812
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unexpected Dropped Connections",
          "properties": null,
          "uuid": "82feab42-6e2f-4201-b05c-7e2f0bcddf72",
          "value": 2813
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unexpected Service Access",
          "properties": null,
          "uuid": "97a0c86b-195f-421e-8710-61e12deedcc5",
          "value": 2814
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown Public DNS Server",
          "properties": null,
          "uuid": "3e08cb63-685e-488d-8426-bb2e7681b7e2",
          "value": 2815
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Data Exfiltration to Unknown S3 Bucket",
          "properties": null,
          "uuid": "f92af0d2-93ab-41a9-a64c-46ae018dacf9",
          "value": 2816
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unsafe LDAP Authentication",
          "properties": null,
          "uuid": "906d3ea3-240b-4b6e-bd32-b7e71eeb76cb",
          "value": 2817
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual IoT Protocol Activity",
          "properties": null,
          "uuid": "a8c886c1-3266-4724-bc74-098410590861",
          "value": 2818
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Kerberos Fingerprint",
          "properties": null,
          "uuid": "b1b6c4e1-b930-4161-b6bd-e8a62365072f",
          "value": 2819
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Protocol for Enterprise Software",
          "properties": null,
          "uuid": "b9f050c2-c642-45db-96ff-8d36f79cc974",
          "value": 2820
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Download from S3 Bucket",
          "properties": null,
          "uuid": "21c98ad4-c5eb-4f14-b9e7-51b312244b2f",
          "value": 2821
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unusual Login Time",
          "properties": null,
          "uuid": "dbc2b52f-ba50-418d-93d0-1e6e756f8a60",
          "value": 2822
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Inbound VNC Traffic from an Unusual Location",
          "properties": null,
          "uuid": "b950c5fe-a401-40a5-a4cf-2d8ed221bb98",
          "value": 2823
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VoIP Call Failure",
          "properties": null,
          "uuid": "e8d062d3-ff50-47a8-bb96-3088d0795431",
          "value": 2824
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VoIP Unavailability Error",
          "properties": null,
          "uuid": "64f79fa5-facf-48b6-af77-954fa7f1f2fe",
          "value": 2825
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "VPN Gateway Access from an Unusual Location",
          "properties": null,
          "uuid": "78438c59-29c1-4c4c-ba07-1ec7dd766037",
          "value": 2826
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Weak Cipher Suites",
          "properties": null,
          "uuid": "9a415dce-f840-44ad-8a6d-1256e22d3966",
          "value": 2827
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Weak Kerberos Encryption",
          "properties": null,
          "uuid": "075deb42-1132-4017-af40-843b1574fa36",
          "value": 2828
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Web Directory Scan",
          "properties": null,
          "uuid": "90475749-65d4-44b1-9eb9-b61cab260df4",
          "value": 2829
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Web Issues",
          "properties": null,
          "uuid": "bfd1a52e-6ee3-460d-b18a-5cbb45df155b",
          "value": 2830
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Oracle WebLogic Administration Console Exploit Attempt",
          "properties": null,
          "uuid": "1fe5c36d-2902-4f19-9917-e6498b77e70c",
          "value": 2831
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Oracle WebLogic Deserialization Exploit Attempt",
          "properties": null,
          "uuid": "68c80c81-2020-4ae1-a3a3-c88e829b2ab2",
          "value": 2832
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Web Service Issues",
          "properties": null,
          "uuid": "e1d48410-9a86-4902-be72-b7ec0df346f4",
          "value": 2833
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "WiFi Auth Issues",
          "properties": null,
          "uuid": "88cfdf3e-d0d4-440f-b9ca-89ccadbd5095",
          "value": 2834
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New WMI Method Launch",
          "properties": null,
          "uuid": "24c7c8d5-1e17-4d14-a553-03a8c5fd6843",
          "value": 2835
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New WMI Process Creation",
          "properties": null,
          "uuid": "5f2a63f7-9246-4ae6-bc4b-2e34daf5b5e4",
          "value": 2836
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New WMI Enumeration Query",
          "properties": null,
          "uuid": "62371e04-bfb6-437e-af9c-3bdc7334eafd",
          "value": 2837
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "WordPress Brute Force",
          "properties": null,
          "uuid": "8ae85975-5ec1-4ae0-a3df-9d53e409f627",
          "value": 2838
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PowerShell Remoting Activity",
          "properties": null,
          "uuid": "85c51dd0-a409-40dc-a7e4-676e01470023",
          "value": 2839
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cross-Site Scripting (XSS) Attack",
          "properties": null,
          "uuid": "cd041ee3-2143-4ab3-8072-cc95d815f6e3",
          "value": 2840
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
      "export_key": "actioninvocation/extrahop_offset",
      "hide_notification": false,
      "id": 875,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_offset",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Offset",
      "tooltip": "(Optional) Skip the specified number of devices. This parameter is often combined with the limit parameter to paginate result sets.",
      "type_id": 6,
      "uuid": "c08fdfe6-3ae5-4b28-854d-7fe4aed3f848",
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
      "export_key": "actioninvocation/extrahop_detection_resolution",
      "hide_notification": false,
      "id": 876,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_resolution",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Resolution",
      "tooltip": "Optional: Detection search filter resolution.",
      "type_id": 6,
      "uuid": "c0e8942a-16c2-4eca-b171-3553b130b445",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": ".none",
          "properties": null,
          "uuid": "2802166b-39b1-4828-a527-48ae376a40a0",
          "value": 2160
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "action_taken",
          "properties": null,
          "uuid": "8ce7fe8e-400f-4ea0-ac17-8213eff39f28",
          "value": 2161
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "no_action_taken",
          "properties": null,
          "uuid": "4abc9b23-db57-436b-9bf8-b5dd23c084de",
          "value": 2162
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
      "export_key": "actioninvocation/extrahop_update_time",
      "hide_notification": false,
      "id": 878,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Update time",
      "tooltip": "(Optional) Return detections that were updated on or after the specified date, expressed in milliseconds since the epoch.",
      "type_id": 6,
      "uuid": "d46ebaf8-c9c1-4ca6-9c6c-b13c33886362",
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
      "export_key": "actioninvocation/extrahop_detection_category",
      "hide_notification": false,
      "id": 879,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_category",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Category",
      "tooltip": "Optional:  Detection search filter category. Note: Performance categories not included in the selection list.",
      "type_id": 6,
      "uuid": "d94e2a93-a192-4ba5-a653-fd5a0e30f5f3",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "sec.exploit",
          "properties": null,
          "uuid": "24a1fac1-ae61-4d65-bd9e-8f441c1d3eaa",
          "value": 2170
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Security",
          "properties": null,
          "uuid": "2d1923f3-cfd2-44bf-a5a9-a5da54c4f69f",
          "value": 2841
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Actions on Objective",
          "properties": null,
          "uuid": "a8e7b092-a7de-46f0-9de9-91327cf6033e",
          "value": 2842
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Botnet",
          "properties": null,
          "uuid": "c784cfdd-4e84-4279-96d8-55909fe9203d",
          "value": 2843
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Caution",
          "properties": null,
          "uuid": "ed309347-d1c9-4293-a228-be3c9991b608",
          "value": 2844
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Command \u0026 Control",
          "properties": null,
          "uuid": "0c4e1ab3-3b05-4de8-b22d-1e0f95dc2887",
          "value": 2845
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cryptocurrency Mining",
          "properties": null,
          "uuid": "0005874f-04e2-48fe-855f-78b9b9970338",
          "value": 2846
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Denial of Service",
          "properties": null,
          "uuid": "4b0f5d14-9bb4-4aee-bfcb-850256b747b5",
          "value": 2847
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Exfiltration",
          "properties": null,
          "uuid": "7854db6a-1640-4dd7-a575-6e714d919c3b",
          "value": 2848
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Exploitation",
          "properties": null,
          "uuid": "1ae16ba0-3ec3-4583-8a29-199292bee985",
          "value": 2849
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Hardening",
          "properties": null,
          "uuid": "7dd3d2e6-33c7-4cf6-be46-2e76e681e7f5",
          "value": 2850
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Lateral Movement",
          "properties": null,
          "uuid": "8f3a4d14-573a-45b0-83ca-5fdd914b51cd",
          "value": 2851
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Ransomware",
          "properties": null,
          "uuid": "05fb5989-d5b0-45be-8569-76fb1772ceb6",
          "value": 2852
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Reconnaissance",
          "properties": null,
          "uuid": "34beae94-189d-483a-9572-12eec054be5c",
          "value": 2853
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
      "export_key": "actioninvocation/extrahop_detection_ticket_id",
      "hide_notification": false,
      "id": 880,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_ticket_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Ticket ID",
      "tooltip": "Optional: Detection search filter ticket ID.",
      "type_id": 6,
      "uuid": "f16fa55a-4d2d-4c64-89d1-15cc657e7752",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": ".none",
          "properties": null,
          "uuid": "89968a23-0b83-4a17-b3cf-8817e7e1143e",
          "value": 2175
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cAdd SOAR incident ID here\u003e",
          "properties": null,
          "uuid": "e36c1cb9-e23d-4b86-b121-e13f6848f39b",
          "value": 2176
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
      "export_key": "actioninvocation/extrahop_output",
      "hide_notification": false,
      "id": 910,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_output",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Output",
      "tooltip": "(Optional) The output format. * `pcap` - .pcap file * `keylog_txt` - A keylog.txt file that can be loaded in wireshark to decode ssl packets. * `zip` - A zip file containing both a packets.pcap and keylog.txt.",
      "type_id": 6,
      "uuid": "f53ed073-19f7-4e0a-8059-2d5d10c4fb58",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "pcap",
          "properties": null,
          "uuid": "43f9c667-6491-40a2-a0eb-5033a421c450",
          "value": 2234
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "keylog_txt",
          "properties": null,
          "uuid": "848b5822-d325-43d0-9132-569b99f0132f",
          "value": 2235
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "zip",
          "properties": null,
          "uuid": "b56d5860-0000-4d6c-80ac-1f6936a8b108",
          "value": 2236
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
      "export_key": "actioninvocation/extrahop_watchlist_action",
      "hide_notification": false,
      "id": 767,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_watchlist_action",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Watchlist action",
      "tooltip": "Add or remove device to or from the watchlist.",
      "type_id": 6,
      "uuid": "f7e7aa61-a227-4545-bede-653afe438414",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "add",
          "properties": null,
          "uuid": "1907ca01-4f6e-4ed4-b6e8-f99b8404ec6d",
          "value": 1906
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "remove",
          "properties": null,
          "uuid": "302c895f-5535-4ac6-ab4c-7bd6de4294b1",
          "value": 1907
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
      "export_key": "actioninvocation/extrahop_ip2",
      "hide_notification": false,
      "id": 934,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip2",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Ip2",
      "tooltip": "(Optional) Return packets sent to or received by the specified IP address.",
      "type_id": 6,
      "uuid": "fb989c53-33df-4efb-a363-4fa6b070cd3d",
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
      "export_key": "actioninvocation/extrahop_device_field",
      "hide_notification": false,
      "id": 882,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_field",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Field",
      "tooltip": "Optional:  Device search filter field.",
      "type_id": 6,
      "uuid": "0b3a4740-50d4-45b2-8e5d-9ad245a5673d",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "discovery_id",
          "properties": null,
          "uuid": "2730f40e-b05b-4d84-9c42-ef6131b64c72",
          "value": 2189
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ipaddr",
          "properties": null,
          "uuid": "0f5c90a2-50e2-42d9-9f76-09fe1f9e2363",
          "value": 2190
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "macaddr",
          "properties": null,
          "uuid": "4190648b-c34e-4e38-af86-c2b161ed1bc9",
          "value": 2191
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vendor",
          "properties": null,
          "uuid": "a16c1db3-43bc-4aea-afec-d1ecf031cbd3",
          "value": 2192
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "tag",
          "properties": null,
          "uuid": "8f7d8ec9-ae78-46f6-b81d-91a6c44b9590",
          "value": 2193
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "activity",
          "properties": null,
          "uuid": "dd2b7013-2202-4b01-8d88-cd8f7460f1c4",
          "value": 2194
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "node",
          "properties": null,
          "uuid": "4f1aa3df-8531-4e42-a778-f7c1a22de1c8",
          "value": 2195
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vlan",
          "properties": null,
          "uuid": "6c13996a-49a1-4a7a-9940-40bf0fcafeec",
          "value": 2196
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "discover_time",
          "properties": null,
          "uuid": "0d1f23e5-5346-4e43-80e4-efd7cbfb6f37",
          "value": 2197
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "role",
          "properties": null,
          "uuid": "6044bc54-440e-4469-8b7e-6dd6870ec0c0",
          "value": 2198
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "dns_name",
          "properties": null,
          "uuid": "61b1b210-3a30-4eaa-a89e-ec5375e22931",
          "value": 2199
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "dhcp_name",
          "properties": null,
          "uuid": "097e0c85-1044-439e-9f77-306643eb9fcb",
          "value": 2200
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "netbios_name",
          "properties": null,
          "uuid": "a9ae1a7d-009a-4660-b12b-27424bd52ca7",
          "value": 2201
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "cdp_name",
          "properties": null,
          "uuid": "6a567a0d-64a4-41cc-a81b-ecf291f239a2",
          "value": 2202
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "custom_name",
          "properties": null,
          "uuid": "ef474d05-0503-4db5-ae0e-443df1f68971",
          "value": 2203
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "software",
          "properties": null,
          "uuid": "c450d794-c786-42e5-9d98-d6d3c45aec58",
          "value": 2204
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "model",
          "properties": null,
          "uuid": "101aae35-0531-438d-a023-83d66de357dc",
          "value": 2205
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "is_critical",
          "properties": null,
          "uuid": "177a48cc-4b20-438f-ba55-aa11961616ed",
          "value": 2206
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "instance_id",
          "properties": null,
          "uuid": "5cb4370e-dd3b-4781-b31b-70e25c6b2bd0",
          "value": 2207
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "instance_name",
          "properties": null,
          "uuid": "0938494c-92d3-4d3f-bbbf-d646bab57ad1",
          "value": 2208
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "instance_type",
          "properties": null,
          "uuid": "10afbf66-8cd9-4d51-94f3-44648237a858",
          "value": 2209
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "cloud_account",
          "properties": null,
          "uuid": "cfa4d607-67ba-4194-9184-bc71286f9056",
          "value": 2210
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "vpc_id",
          "properties": null,
          "uuid": "03f945a4-4a9a-4cbe-82f9-b1d8a5615f21",
          "value": 2211
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "subnet_id",
          "properties": null,
          "uuid": "7a0a016c-744e-478a-a111-c20dbb97e42a",
          "value": 2212
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "is_active",
          "properties": null,
          "uuid": "1f119129-1f37-4c14-bf43-f2ec6ba0d6d5",
          "value": 2213
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
      "export_key": "actioninvocation/extrahop_device_id",
      "hide_notification": false,
      "id": 1236,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Device ID",
      "tooltip": "ExtraHop Device REST api ID.",
      "type_id": 6,
      "uuid": "117b1d04-cf13-45bb-b95a-9422ba450477",
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
      "export_key": "actioninvocation/extrahop_limit_search_duration",
      "hide_notification": false,
      "id": 911,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_search_duration",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Limit search duration",
      "tooltip": "The maximum amount of time to run the packet search.The default unit is milliseconds, but other units can be specified with a unit suffix. ",
      "type_id": 6,
      "uuid": "12902179-0671-4cd1-ae3d-299f0aa41a86",
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
      "export_key": "actioninvocation/extrahop_limit_bytes",
      "hide_notification": false,
      "id": 912,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_limit_bytes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Limit bytes",
      "tooltip": "The maximum number of bytes to return.",
      "type_id": 6,
      "uuid": "1d9d2ede-fabe-48d3-9f7f-33b0bd13a426",
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
      "export_key": "actioninvocation/extrahop_artifact_type",
      "hide_notification": false,
      "id": 807,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Artifact type",
      "tooltip": "SOAR artifact type.",
      "type_id": 6,
      "uuid": "29e39e7a-56b3-4727-9b44-2af47e40f69b",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "IP Address",
          "properties": null,
          "uuid": "9391d6c1-3d70-4eaf-8eeb-d27dce1b9adb",
          "value": 2007
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "IP Address (v4)",
          "properties": null,
          "uuid": "5bcc3d96-30e2-4ccd-8baa-75ccfa1f9801",
          "value": 2307
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "IP Address (v6)",
          "properties": null,
          "uuid": "b053929a-319d-45ca-a385-23fc0da23074",
          "value": 2857
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Name",
          "properties": null,
          "uuid": "47dc03bf-4931-4e9d-81b3-060576f4eca9",
          "value": 2008
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "MAC Address",
          "properties": null,
          "uuid": "db5e257e-be57-4266-8f41-d4934600cd3d",
          "value": 2009
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
      "export_key": "actioninvocation/extrahop_ip1",
      "hide_notification": false,
      "id": 933,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ip1",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Ip1",
      "tooltip": "(Optional) Return packets sent to or received by the specified IP address.",
      "type_id": 6,
      "uuid": "31bfb391-2463-4b8a-9865-c2b27431387e",
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
      "export_key": "actioninvocation/extrahop_active_from",
      "hide_notification": false,
      "id": 884,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_active_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Active from",
      "tooltip": "(Optional) The beginning timestamp for the request.",
      "type_id": 6,
      "uuid": "472c0398-165f-4543-a42e-e689031485a0",
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
      "export_key": "actioninvocation/extrahop_device_operand",
      "hide_notification": false,
      "id": 885,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_operand",
      "operation_perms": {},
      "operations": [],
      "placeholder": "\u003cOperand string value\u003e",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Operand",
      "tooltip": "Optional:  Device search filter operand. String or Number or Object",
      "type_id": 6,
      "uuid": "4aba00eb-fe2e-4580-b7f1-72b5a3793c7c",
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
      "export_key": "actioninvocation/extrahop_detection_status",
      "hide_notification": false,
      "id": 886,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Status",
      "tooltip": "Optional: Detection search filter status.",
      "type_id": 6,
      "uuid": "4fc1ab8f-a2d8-4da5-9cab-a217457d536d",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "in_prog",
          "properties": null,
          "uuid": "87555e4f-33cd-4feb-a3ed-08ab0af48d61",
          "value": 2214
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": ".none",
          "properties": null,
          "uuid": "eb27e6c5-591f-4079-a13d-ece052da2454",
          "value": 2215
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "new",
          "properties": null,
          "uuid": "dccce03e-a76d-435e-a5bf-b92c995ecd24",
          "value": 2216
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "in_progress",
          "properties": null,
          "uuid": "94693fd9-c2cd-4023-a484-0dba4786dc7a",
          "value": 2217
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "closed",
          "properties": null,
          "uuid": "fc0515ab-6db1-40fd-85d2-c8712c2e7d1e",
          "value": 2218
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "acknowledged",
          "properties": null,
          "uuid": "eb135393-3563-4892-a374-0ac05a960f1c",
          "value": 2219
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": true,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "actioninvocation/extrahop_device_operator",
      "hide_notification": false,
      "id": 887,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_device_operator",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Operator",
      "tooltip": "Optional:  Device search filter operator",
      "type_id": 6,
      "uuid": "7064c221-59b5-4ff9-b015-e3360d0bbbbb",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003e",
          "properties": null,
          "uuid": "8a139075-72c8-4943-9201-a4e5a05ecb07",
          "value": 2220
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003c",
          "properties": null,
          "uuid": "a2aa575a-482b-4d48-a37d-77a243b15acd",
          "value": 2221
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003c=",
          "properties": null,
          "uuid": "3646ac86-6567-46e6-9373-4c6bb4b28e48",
          "value": 2222
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003e=",
          "properties": null,
          "uuid": "f3d656d2-b9ba-45ef-bbc0-02c32c5d8a2b",
          "value": 2223
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "=",
          "properties": null,
          "uuid": "2075cd22-340a-47da-859c-efa5089cb62c",
          "value": 2224
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "!=",
          "properties": null,
          "uuid": "0628d67d-53d3-47bc-8762-e87b53553a6a",
          "value": 2225
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "startswith",
          "properties": null,
          "uuid": "4ea81c01-fbd9-41be-a867-5c1d80ae2077",
          "value": 2226
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "and",
          "properties": null,
          "uuid": "da76852e-9b7f-4d7f-bfaa-2eb84ae87ecf",
          "value": 2227
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "or",
          "properties": null,
          "uuid": "25d76027-4435-490b-a80f-cd1d16f59e1c",
          "value": 2228
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "not",
          "properties": null,
          "uuid": "05ba4f6a-a4c9-48ad-83f5-fe237ffc0c54",
          "value": 2229
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "exists",
          "properties": null,
          "uuid": "24995edf-8e15-49b2-939a-c8e15b38a078",
          "value": 2230
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "not_exists",
          "properties": null,
          "uuid": "32e77a93-9ae1-435f-b3ca-adb3cc112043",
          "value": 2231
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "~",
          "properties": null,
          "uuid": "e510fb35-0655-41e5-a327-6b2d04ca656e",
          "value": 2232
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "!~",
          "properties": null,
          "uuid": "311e239d-a020-4721-88f0-7c8e10317090",
          "value": 2233
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
      "export_key": "incident/extrahop_site_name",
      "hide_notification": false,
      "id": 935,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_site_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop site name",
      "tooltip": "The name of the ExtraHop appliance.",
      "type_id": 0,
      "uuid": "9011273d-bb9b-4b7a-b65d-3d1fe362fc47",
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
      "export_key": "incident/extrahop_update_time",
      "hide_notification": false,
      "id": 635,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop Update Time",
      "tooltip": "",
      "type_id": 0,
      "uuid": "9961a920-85af-49f3-a0f2-029fc673b884",
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
      "export_key": "incident/extrahop_detection_link",
      "hide_notification": false,
      "id": 636,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_link",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Detection Link",
      "tooltip": "Link back to ExtraHop detection",
      "type_id": 0,
      "uuid": "9ebbe669-25c7-4669-9eab-122113403cc4",
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
      "export_key": "incident/extrahop_site_uuid",
      "hide_notification": false,
      "id": 936,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_site_uuid",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop site UUID",
      "tooltip": "The uuidof the ExtraHop appliance.",
      "type_id": 0,
      "uuid": "c0996450-adb7-4921-8309-1317cb5e95d9",
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
      "export_key": "incident/extrahop_update_notification",
      "hide_notification": false,
      "id": 939,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_update_notification",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "ExtraHop Update Notification",
      "tooltip": "",
      "type_id": 0,
      "uuid": "c45e6f5f-7f3f-402b-ab02-5e242460b720",
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
      "export_key": "incident/extrahop_status",
      "hide_notification": false,
      "id": 637,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Status",
      "tooltip": "",
      "type_id": 0,
      "uuid": "c45eec21-2a76-479d-a164-172df939d760",
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
      "export_key": "incident/extrahop_console_url",
      "hide_notification": false,
      "id": 937,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_console_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop console URL",
      "tooltip": "ExtraHop base console url.",
      "type_id": 0,
      "uuid": "065f70e9-5dec-4a5d-93cc-8d7ece7dbf31",
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
      "export_key": "incident/extrahop_detection_updated",
      "hide_notification": false,
      "id": 638,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_updated",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Detection Updated",
      "tooltip": "Field to indicate detection has been updated",
      "type_id": 0,
      "uuid": "0921db00-b482-418f-a16b-9022d1f3ea68",
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
      "export_key": "incident/extrahop_ticket_id",
      "hide_notification": false,
      "id": 639,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_ticket_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Ticket ID",
      "tooltip": "",
      "type_id": 0,
      "uuid": "0a1a6146-2d5d-4cc6-b657-300e2768eb03",
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
      "export_key": "incident/extrahop_detection_id",
      "hide_notification": false,
      "id": 640,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_detection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Detection ID",
      "tooltip": "Extrahop detecion ID.",
      "type_id": 0,
      "uuid": "264154d1-778e-4fe8-afff-485d86020976",
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
      "export_key": "incident/extrahop_end_time",
      "hide_notification": false,
      "id": 641,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop End Time",
      "tooltip": "",
      "type_id": 0,
      "uuid": "551c0110-b5fd-4a55-9643-bb5684c2c1aa",
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
      "export_key": "incident/extrahop_risk_score",
      "hide_notification": false,
      "id": 642,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_risk_score",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Risk Score",
      "tooltip": "",
      "type_id": 0,
      "uuid": "638e8971-c0c7-436b-967f-ab3b8027be33",
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
      "export_key": "incident/extrahop_assignee",
      "hide_notification": false,
      "id": 643,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "extrahop_assignee",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "templates": [],
      "text": "Extrahop Assignee",
      "tooltip": "",
      "type_id": 0,
      "uuid": "72598a45-93b0-425f-b0b1-8bf9ead8d986",
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
      "created_date": 1652437247684,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add a note to an ExtraHop detection. Parameters detection_id, note. (Optional) update_time.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) add detection note",
      "export_key": "funct_extrahop_rx_add_detection_note",
      "id": 82,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1653920193853,
      "name": "funct_extrahop_rx_add_detection_note",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": \"success\"}, \"raw\": null, \"inputs\": {\"extrahop_update_time\": 0, \"extrahop_note\": \"\\nIBM SOAR 16/05/2022 15:13:37\\n[SOAR Case - 4305](https://127.0.0.1:1443/#incidents/4305)\\n[SOAR case - \u00274305\u0027](Closed with resolution summary: \u0027test closed.\u0027)\", \"extrahop_detection_id\": 3}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 892, \"timestamp\": \"2022-05-16 15:29:16\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_update_time\": {\"type\": \"integer\"}, \"extrahop_note\": {\"type\": \"string\"}, \"extrahop_detection_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "58307d38-9975-4209-a8af-e68cb85f59f4",
      "version": 8,
      "view_items": [
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9311b73-c244-47be-ac17-5ada6595b3e9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b175d32a-198e-403d-adcd-052b56876488",
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
          "name": "Example: Extrahop Reveal(x) update detection",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_detection",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "created_date": 1651162998409,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Assign a tag to a list of devices ids forExtrahop Reveal(x). Parameters tag_id. devices_ids.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) assign tag",
      "export_key": "funct_extrahop_rx_assign_tag",
      "id": 68,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162998568,
      "name": "funct_extrahop_rx_assign_tag",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": \"success\"}, \"raw\": null, \"inputs\": {\"extrahop_device_ids\": \"3\", \"extrahop_tag_id\": 5}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 810, \"timestamp\": \"2022-04-13 17:19:42\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_device_ids\": {\"type\": \"string\"}, \"extrahop_tag_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "f0d2fc8c-20ab-440c-b4f5-46776a0b561e",
      "version": 1,
      "view_items": [
        {
          "content": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f7117970-a76c-4505-87b3-5dbcc35eabdc",
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
          "name": "Example: Extrahop Reveal(x) assign tag",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_assign_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 83
        }
      ]
    },
    {
      "created_date": 1651162998652,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Create a new tag for  Extrahop Reveal(x).  Parameter tag_name.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) create tag",
      "export_key": "funct_extrahop_rx_create_tag",
      "id": 69,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162998804,
      "name": "funct_extrahop_rx_create_tag",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": \"success\"}, \"raw\": null, \"inputs\": {\"extrahop_tag_name\": \"TEST_TAG_1\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 798, \"timestamp\": \"2022-04-13 17:22:37\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_tag_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "d566e4b3-6692-4599-a351-7530cdb4874e",
      "version": 1,
      "view_items": [
        {
          "content": "9274ccb1-cebb-4be8-b7f1-f768f0eabbcf",
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
          "name": "Example: Extrahop Reveal(x) create tag",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_create_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 77
        }
      ]
    },
    {
      "created_date": 1651162998871,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get activitymap information from Extrahop Reveal(x) . Optional parameter activitymap_id.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get activitymaps",
      "export_key": "funct_extrahop_rx_get_activitymaps",
      "id": 70,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162999071,
      "name": "funct_extrahop_rx_get_activitymaps",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"id\": 1, \"name\": \"Test_activity_map_1\", \"short_code\": \"wGCGL\", \"description\": \"Test map 1\", \"weighting\": \"bytes\", \"owner\": \"setup\", \"mode\": \"2dforce\", \"mod_time\": 1644514002331, \"show_alert_status\": false, \"walks\": [{\"origins\": [{\"object_type\": \"device\", \"object_id\": 6}], \"steps\": [{\"relationships\": [{\"protocol\": \"any\", \"role\": \"any\"}]}]}], \"rights\": [\"delete\", \"edit\", \"share\", \"transfer\", \"view\"]}]}, \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 1063, \"timestamp\": \"2022-04-13 16:50:16\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}, \"short_code\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"weighting\": {\"type\": \"string\"}, \"owner\": {\"type\": \"string\"}, \"mode\": {\"type\": \"string\"}, \"mod_time\": {\"type\": \"integer\"}, \"show_alert_status\": {\"type\": \"boolean\"}, \"walks\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"origins\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"object_type\": {\"type\": \"string\"}, \"object_id\": {\"type\": \"integer\"}}}}, \"steps\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"relationships\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"protocol\": {\"type\": \"string\"}, \"role\": {\"type\": \"string\"}}}}}}}}}}, \"rights\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "18aa0964-745b-4329-a04b-a92f5f3fab40",
      "version": 1,
      "view_items": [
        {
          "content": "f1d0366d-e216-4071-8070-c67fe27f834b",
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
          "name": "Example: Extrahop Reveal(x) get activitymaps",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_activitymaps",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 81
        }
      ]
    },
    {
      "created_date": 1652450274331,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get a note from an ExtraHop detection. Parameter detection_id.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get detection note",
      "export_key": "funct_extrahop_rx_get_detection_note",
      "id": 83,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1653920193977,
      "name": "funct_extrahop_rx_get_detection_note",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": {\"author\": \"setup\", \"update_time\": 1652711350410, \"note\": \"\\nIBM SOAR 16/05/2022 15:13:37\\n[SOAR Case - 4305](https://127.0.0.1:1443/#incidents/4305)\"}}, \"raw\": null, \"inputs\": {\"extrahop_detection_id\": 3}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 780, \"timestamp\": \"2022-05-16 15:29:13\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"object\", \"properties\": {\"author\": {\"type\": \"string\"}, \"update_time\": {\"type\": \"integer\"}, \"note\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_detection_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "e5d62abb-bce4-46f6-a686-1b112a735219",
      "version": 5,
      "view_items": [
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
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
          "name": "Example: Extrahop Reveal(x) update detection",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_detection",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "created_date": 1651162999154,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get detections information from Extrahop Reveal(x) . Optional parameter extrahop_detection_id.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get detections",
      "export_key": "funct_extrahop_rx_get_detections",
      "id": 71,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162999308,
      "name": "funct_extrahop_rx_get_detections",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": {\"id\": 71, \"start_time\": 1646559540000, \"update_time\": 1647656040000, \"end_time\": 1647051270000, \"title\": \"Weekly Summary: Weak Cipher Suites\", \"description\": \"Over the past week, servers negotiated SSL/TLS sessions with a cipher suite that includes an encryption algorithm that is known to be vulnerable. Cipher suites that contain weak encryption algorithms such as CBC, 3DES, RC4, null, anonymous, and export should be removed from servers and replaced with stronger cipher suites.\", \"categories\": [\"sec\", \"sec.caution\"], \"risk_score\": 61, \"type\": \"weak_cipher\", \"participants\": [{\"object_type\": \"device\", \"object_id\": 3, \"role\": \"offender\", \"external\": false, \"id\": 175}, {\"object_type\": \"device\", \"object_id\": 6, \"role\": \"offender\", \"external\": false, \"id\": 179}], \"ticket_id\": \"3055\", \"assignee\": \"a@a.com\", \"status\": \"in_progress\", \"resolution\": null, \"properties\": {}, \"mitre_tactics\": [], \"mitre_techniques\": [], \"appliance_id\": 0, \"is_user_created\": false}}, \"raw\": null, \"inputs\": {\"extrahop_detection_id\": 71}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 1373, \"timestamp\": \"2022-04-13 17:01:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"start_time\": {\"type\": \"integer\"}, \"update_time\": {\"type\": \"integer\"}, \"end_time\": {\"type\": \"integer\"}, \"title\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"categories\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"risk_score\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"participants\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"object_type\": {\"type\": \"string\"}, \"object_id\": {\"type\": \"integer\"}, \"role\": {\"type\": \"string\"}, \"external\": {\"type\": \"boolean\"}, \"id\": {\"type\": \"integer\"}}}}, \"ticket_id\": {\"type\": \"string\"}, \"assignee\": {\"type\": \"string\"}, \"status\": {\"type\": \"string\"}, \"resolution\": {}, \"properties\": {\"type\": \"object\"}, \"mitre_tactics\": {\"type\": \"array\"}, \"mitre_techniques\": {\"type\": \"array\"}, \"appliance_id\": {\"type\": \"integer\"}, \"is_user_created\": {\"type\": \"boolean\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_detection_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "fc71fc68-991e-4825-bc07-2191e58745f3",
      "version": 1,
      "view_items": [
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
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
          "name": "Example: Extrahop Reveal(x) refresh incident",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_refresh_incident",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) search detections",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_detections",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 85
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) update detection",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_detection",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) update incident",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_incident",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 79
        }
      ]
    },
    {
      "created_date": 1649934557715,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get devices information from Extrahop Reveal(x) . Optional parameters  device_id, active_from, active_util, limit and offset.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get devices",
      "export_key": "funct_extrahop_rx_get_devices",
      "id": 50,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1649934557786,
      "name": "funct_extrahop_rx_get_devices",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"mod_time\": 1647052291076, \"node_id\": null, \"id\": 6, \"extrahop_id\": \"027437b63df40000\", \"discovery_id\": \"027437b63df40000\", \"display_name\": \"Device 027437b63df40000\", \"description\": null, \"user_mod_time\": 1646046972271, \"discover_time\": 1644418590000, \"vlanid\": 0, \"parent_id\": null, \"macaddr\": \"02:74:37:B6:3D:F4\", \"vendor\": null, \"is_l3\": false, \"ipaddr4\": \"192.168.1.2\", \"ipaddr6\": null, \"device_class\": \"node\", \"default_name\": \"Device 027437b63df40000\", \"custom_name\": null, \"cdp_name\": \"\", \"dhcp_name\": \"\", \"netbios_name\": \"\", \"dns_name\": \"\", \"custom_type\": \"\", \"auto_role\": \"http_server\", \"analysis_level\": 2, \"analysis\": \"advanced\", \"role\": \"http_server\", \"on_watchlist\": true, \"last_seen_time\": 1647052260000, \"model\": null, \"model_override\": null, \"custom_make\": null, \"custom_model\": null, \"critical\": false, \"custom_criticality\": null, \"cloud_instance_id\": null, \"cloud_instance_type\": null, \"cloud_instance_name\": null, \"cloud_account\": null, \"vpc_id\": null, \"subnet_id\": null}]}, \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 1558, \"timestamp\": \"2022-04-13 17:02:00\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"mod_time\": {\"type\": \"integer\"}, \"node_id\": {}, \"id\": {\"type\": \"integer\"}, \"extrahop_id\": {\"type\": \"string\"}, \"discovery_id\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}, \"description\": {}, \"user_mod_time\": {\"type\": \"integer\"}, \"discover_time\": {\"type\": \"integer\"}, \"vlanid\": {\"type\": \"integer\"}, \"parent_id\": {}, \"macaddr\": {\"type\": \"string\"}, \"vendor\": {}, \"is_l3\": {\"type\": \"boolean\"}, \"ipaddr4\": {\"type\": [\"null\", \"string\"]}, \"ipaddr6\": {}, \"device_class\": {\"type\": \"string\"}, \"default_name\": {\"type\": \"string\"}, \"custom_name\": {}, \"cdp_name\": {\"type\": \"string\"}, \"dhcp_name\": {\"type\": \"string\"}, \"netbios_name\": {\"type\": \"string\"}, \"dns_name\": {\"type\": \"string\"}, \"custom_type\": {\"type\": \"string\"}, \"auto_role\": {\"type\": \"string\"}, \"analysis_level\": {\"type\": \"integer\"}, \"analysis\": {\"type\": \"string\"}, \"role\": {\"type\": \"string\"}, \"on_watchlist\": {\"type\": \"boolean\"}, \"last_seen_time\": {\"type\": \"integer\"}, \"model\": {}, \"model_override\": {}, \"custom_make\": {}, \"custom_model\": {}, \"critical\": {\"type\": \"boolean\"}, \"custom_criticality\": {}, \"cloud_instance_id\": {}, \"cloud_instance_type\": {}, \"cloud_instance_name\": {}, \"cloud_account\": {}, \"vpc_id\": {}, \"subnet_id\": {}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "75447029-32ca-4363-b753-bc970cee66d5",
      "version": 1,
      "view_items": [
        {
          "content": "77f58f54-c4a9-4720-ab05-34e2beb94521",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a2068f3-d76c-4dac-8776-819499720814",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5763430b-3c38-4873-aec3-df249773c52a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
          "name": "Example: Extrahop Reveal(x) get devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_devices",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 75
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) refresh incident",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_refresh_incident",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 95
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) search devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_devices",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 76
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) update incident",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_incident",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 79
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) update watchlist",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_update_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 74
        }
      ]
    },
    {
      "created_date": 1651162999469,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Get tags information from Extrahop Reveal(x) . Optional parameter tag_id.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get tags",
      "export_key": "funct_extrahop_rx_get_tags",
      "id": 72,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162999621,
      "name": "funct_extrahop_rx_get_tags",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"mod_time\": 1646045416014, \"id\": 1, \"name\": \"TEST_TAG_1\"}, {\"mod_time\": 1646064909025, \"id\": 2, \"name\": \"TEST_TAG_2\"}]}, \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 969, \"timestamp\": \"2022-04-13 17:19:40\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"mod_time\": {\"type\": \"integer\"}, \"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "55ced5bd-cd23-4212-b661-956fed40722b",
      "version": 1,
      "view_items": [
        {
          "content": "5da7da21-5ae6-424a-9b37-c2d6eb0fc501",
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
          "name": "Example: Extrahop Reveal(x) assign tag",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_assign_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 83
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) create tag",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_create_tag",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 77
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) get tags",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_tags",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 84
        }
      ]
    },
    {
      "created_date": 1651162999698,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Retrieve all devices that are in the watchlist from Extrahop Reveal(x) .",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) get watchlist",
      "export_key": "funct_extrahop_rx_get_watchlist",
      "id": 73,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651162999906,
      "name": "funct_extrahop_rx_get_watchlist",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"mod_time\": 1647052291076, \"node_id\": null, \"id\": 6, \"extrahop_id\": \"027437b63df40000\", \"discovery_id\": \"027437b63df40000\", \"display_name\": \"Device 027437b63df40000\", \"description\": null, \"user_mod_time\": 1646046972271, \"discover_time\": 1644418590000, \"vlanid\": 0, \"parent_id\": null, \"macaddr\": \"02:74:37:B6:3D:F4\", \"vendor\": null, \"is_l3\": false, \"ipaddr4\": \"192.168.1.2\", \"ipaddr6\": null, \"device_class\": \"node\", \"default_name\": \"Device 027437b63df40000\", \"custom_name\": null, \"cdp_name\": \"\", \"dhcp_name\": \"\", \"netbios_name\": \"\", \"dns_name\": \"\", \"custom_type\": \"\", \"auto_role\": \"http_server\", \"analysis_level\": 2, \"analysis\": \"advanced\", \"role\": \"http_server\", \"on_watchlist\": true, \"last_seen_time\": 1647052260000, \"model\": null, \"model_override\": null, \"custom_make\": null, \"custom_model\": null, \"critical\": false, \"custom_criticality\": null, \"cloud_instance_id\": null, \"cloud_instance_type\": null, \"cloud_instance_name\": null, \"cloud_account\": null, \"vpc_id\": null, \"subnet_id\": null}]}, \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 739, \"timestamp\": \"2022-04-13 16:50:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"mod_time\": {\"type\": \"integer\"}, \"node_id\": {}, \"id\": {\"type\": \"integer\"}, \"extrahop_id\": {\"type\": \"string\"}, \"discovery_id\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}, \"description\": {}, \"user_mod_time\": {\"type\": \"integer\"}, \"discover_time\": {\"type\": \"integer\"}, \"vlanid\": {\"type\": \"integer\"}, \"parent_id\": {}, \"macaddr\": {\"type\": \"string\"}, \"vendor\": {}, \"is_l3\": {\"type\": \"boolean\"}, \"ipaddr4\": {\"type\": \"string\"}, \"ipaddr6\": {}, \"device_class\": {\"type\": \"string\"}, \"default_name\": {\"type\": \"string\"}, \"custom_name\": {}, \"cdp_name\": {\"type\": \"string\"}, \"dhcp_name\": {\"type\": \"string\"}, \"netbios_name\": {\"type\": \"string\"}, \"dns_name\": {\"type\": \"string\"}, \"custom_type\": {\"type\": \"string\"}, \"auto_role\": {\"type\": \"string\"}, \"analysis_level\": {\"type\": \"integer\"}, \"analysis\": {\"type\": \"string\"}, \"role\": {\"type\": \"string\"}, \"on_watchlist\": {\"type\": \"boolean\"}, \"last_seen_time\": {\"type\": \"integer\"}, \"model\": {}, \"model_override\": {}, \"custom_make\": {}, \"custom_model\": {}, \"critical\": {\"type\": \"boolean\"}, \"custom_criticality\": {}, \"cloud_instance_id\": {}, \"cloud_instance_type\": {}, \"cloud_instance_name\": {}, \"cloud_account\": {}, \"vpc_id\": {}, \"subnet_id\": {}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "4d5690ce-998c-4fbb-bf25-765800aaa246",
      "version": 1,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Extrahop Reveal(x) get watchlist",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_get_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 80
        }
      ]
    },
    {
      "created_date": 1651162999999,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for detections information from Extrahop Reveal(x). Optional parameters search_filter, active_from, active_util, limit , offset, update_time and sort.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) search detections",
      "export_key": "funct_extrahop_rx_search_detections",
      "id": 74,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651163000156,
      "name": "funct_extrahop_rx_search_detections",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"id\": 3, \"start_time\": 1644540480000, \"update_time\": 1644642690000, \"end_time\": 1644556530000, \"title\": \"Daily Summary: Inbound Suspicious Connections\", \"description\": \"Over the past day, servers received connections from devices with suspicious IP addresses. These IP addresses are considered suspicious based on threat intelligence found in your Reveal(x) system. Investigate to determine if the IP addresses are from malicious endpoints.\\n\\nSuspicious IP addresses linked to this detection:\\n* 109.237.103.9\\n* 45.83.65.214\\n* 45.83.67.186\\n* 185.220.101.63\\n* 185.220.101.191\\n* 130.211.54.158\\n* 192.241.212.103\", \"categories\": [\"sec\", \"sec.caution\"], \"risk_score\": 60, \"type\": \"ti_tcp_incoming\", \"participants\": [{\"object_type\": \"device\", \"object_id\": 2, \"role\": \"victim\", \"external\": false, \"id\": 8}, {\"object_type\": \"device\", \"object_id\": 6, \"role\": \"victim\", \"external\": false, \"id\": 11}], \"ticket_id\": null, \"assignee\": null, \"status\": \"in_progress\", \"resolution\": null, \"properties\": {\"suspicious_ipaddr\": {\"type\": \"ipaddr\", \"value\": [\"192.168.1.9\", \"192.168.1.214\", \"192.168.1.186\", \"192.168.1.63\", \"192.168.1.191\", \"192.168.1.158\", \"192.168.2.103\"]}}, \"mitre_tactics\": [], \"mitre_techniques\": [], \"appliance_id\": 0, \"is_user_created\": false}, {\"id\": 79, \"start_time\": 1646741073962, \"update_time\": 1646741073962, \"end_time\": 1646741073962, \"title\": \"CVE-2019-0708 RDP Exploit Attempt\", \"description\": \"[Device 02a1d541ff800000](#/metrics/devices/c708d037ae5a46b69ec4dcbf7e4555e5.02a1d541ff800000/overview?from=1646741073\u0026interval_type=DT\u0026until=1646741073) received a Remote Desktop Protocol (RDP) connection request that is consistent with a known vulnerability, also known as BlueKeep, in older versions of Microsoft Windows. This vulnerability allows an unauthenticated attacker to remotely run arbitrary code on an RDP server. The attacker can then tamper with data or install malware that could propagate to other Windows devices across the network. Investigate to determine if [Device 02a1d541ff800000](#/metrics/devices/c708d037ae5a46b69ec4dcbf7e4555e5.02a1d541ff800000/overview?from=1646741073\u0026interval_type=DT\u0026until=1646741073) is hosting a version affected by CVE-2019-0708: Windows 7, Windows XP, Windows Vista, Windows Server 2003, and Windows Server 2008.\", \"categories\": [\"sec\", \"sec.exploit\"], \"risk_score\": 98, \"type\": \"cve_2019_0708\", \"participants\": [{\"object_type\": \"device\", \"object_id\": 2, \"role\": \"victim\", \"external\": false, \"id\": 194}, {\"object_type\": \"ipaddr\", \"object_value\": \"216.218.206.66\", \"role\": \"offender\", \"external\": true, \"id\": 195}], \"ticket_id\": \"2529\", \"assignee\": \"a@a.com\", \"status\": \"in_progress\", \"resolution\": null, \"properties\": {\"client_port\": 45214, \"server_port\": 3389}, \"mitre_tactics\": [{\"id\": \"TA0008\", \"name\": \"Lateral Movement\", \"url\": \"https://attack.mitre.org/tactics/TA0008\"}], \"mitre_techniques\": [{\"id\": \"T1210\", \"name\": \"Exploitation of Remote Services\", \"url\": \"https://attack.mitre.org/techniques/T1210\", \"legacy_ids\": [\"T1210\"]}], \"appliance_id\": 0, \"is_user_created\": false}]}, \"raw\": null, \"inputs\": {\"extrahop_search_filter\": \"{\\\"filter\\\": {\\\"status\\\": [\\\"in_progress\\\"]}}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 948, \"timestamp\": \"2022-04-13 17:53:38\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"start_time\": {\"type\": \"integer\"}, \"update_time\": {\"type\": \"integer\"}, \"end_time\": {\"type\": \"integer\"}, \"title\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"categories\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"risk_score\": {\"type\": \"integer\"}, \"type\": {\"type\": \"string\"}, \"participants\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"object_type\": {\"type\": \"string\"}, \"object_id\": {\"type\": \"integer\"}, \"role\": {\"type\": \"string\"}, \"external\": {\"type\": \"boolean\"}, \"id\": {\"type\": \"integer\"}, \"object_value\": {\"type\": \"string\"}}}}, \"ticket_id\": {\"type\": [\"null\", \"string\"]}, \"assignee\": {\"type\": [\"null\", \"string\"]}, \"status\": {\"type\": [\"null\", \"string\"]}, \"resolution\": {}, \"properties\": {\"type\": \"object\", \"properties\": {\"client_port\": {\"type\": \"integer\"}, \"server_port\": {\"type\": \"integer\"}, \"jndi_strings\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"mitre_tactics\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}}}}, \"mitre_techniques\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"url\": {\"type\": \"string\"}, \"legacy_ids\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}, \"appliance_id\": {\"type\": \"integer\"}, \"is_user_created\": {\"type\": \"boolean\"}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_search_filter\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b70037a5-fcaf-4e78-a1e2-6acdc4dff239",
      "version": 1,
      "view_items": [
        {
          "content": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b175d32a-198e-403d-adcd-052b56876488",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0b7aca53-b3b4-42b0-8386-3f19042acf55",
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
          "name": "Example: Extrahop Reveal(x) search detections",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_detections",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 85
        }
      ]
    },
    {
      "created_date": 1651163000215,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for devices information from Extrahop Reveal(x). Optional parameters search_filter, active_from, active_util, limit and offset.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) search devices",
      "export_key": "funct_extrahop_rx_search_devices",
      "id": 75,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651163000364,
      "name": "funct_extrahop_rx_search_devices",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": [{\"mod_time\": 1649866540057, \"node_id\": null, \"id\": 3, \"extrahop_id\": \"02f6b87341f00000\", \"discovery_id\": \"02f6b87341f00000\", \"display_name\": \"Device 02f6b87341f00000\", \"description\": null, \"user_mod_time\": 1644418537403, \"discover_time\": 1644418320000, \"vlanid\": 0, \"parent_id\": null, \"macaddr\": \"02:F6:B8:73:41:F0\", \"vendor\": null, \"is_l3\": false, \"ipaddr4\": \"192.168.1.159\", \"ipaddr6\": null, \"device_class\": \"node\", \"default_name\": \"Device 02f6b87341f00000\", \"custom_name\": null, \"cdp_name\": \"\", \"dhcp_name\": \"\", \"netbios_name\": \"\", \"dns_name\": \"\", \"custom_type\": \"\", \"auto_role\": \"other\", \"analysis_level\": 2, \"analysis\": \"advanced\", \"role\": \"other\", \"on_watchlist\": true, \"last_seen_time\": 1647052200000, \"model\": null, \"model_override\": null, \"custom_make\": null, \"custom_model\": null, \"critical\": false, \"custom_criticality\": null, \"cloud_instance_id\": null, \"cloud_instance_type\": null, \"cloud_instance_name\": null, \"cloud_account\": null, \"vpc_id\": null, \"subnet_id\": null}]}, \"raw\": null, \"inputs\": {\"extrahop_search_filter\": \"{\\\"filter\\\": {\\\"operator\\\": \\\"=\\\", \\\"field\\\": \\\"ipaddr\\\", \\\"operand\\\": \\\"192.168.1.159\\\"}}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 965, \"timestamp\": \"2022-04-13 17:17:19\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"mod_time\": {\"type\": \"integer\"}, \"node_id\": {}, \"id\": {\"type\": \"integer\"}, \"extrahop_id\": {\"type\": \"string\"}, \"discovery_id\": {\"type\": \"string\"}, \"display_name\": {\"type\": \"string\"}, \"description\": {}, \"user_mod_time\": {\"type\": \"integer\"}, \"discover_time\": {\"type\": \"integer\"}, \"vlanid\": {\"type\": \"integer\"}, \"parent_id\": {}, \"macaddr\": {\"type\": \"string\"}, \"vendor\": {}, \"is_l3\": {\"type\": \"boolean\"}, \"ipaddr4\": {\"type\": \"string\"}, \"ipaddr6\": {}, \"device_class\": {\"type\": \"string\"}, \"default_name\": {\"type\": \"string\"}, \"custom_name\": {}, \"cdp_name\": {\"type\": \"string\"}, \"dhcp_name\": {\"type\": \"string\"}, \"netbios_name\": {\"type\": \"string\"}, \"dns_name\": {\"type\": \"string\"}, \"custom_type\": {\"type\": \"string\"}, \"auto_role\": {\"type\": \"string\"}, \"analysis_level\": {\"type\": \"integer\"}, \"analysis\": {\"type\": \"string\"}, \"role\": {\"type\": \"string\"}, \"on_watchlist\": {\"type\": \"boolean\"}, \"last_seen_time\": {\"type\": \"integer\"}, \"model\": {}, \"model_override\": {}, \"custom_make\": {}, \"custom_model\": {}, \"critical\": {\"type\": \"boolean\"}, \"custom_criticality\": {}, \"cloud_instance_id\": {}, \"cloud_instance_type\": {}, \"cloud_instance_name\": {}, \"cloud_account\": {}, \"vpc_id\": {}, \"subnet_id\": {}}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_search_filter\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "e7384abd-0046-4b46-97af-d34d8cc9c711",
      "version": 1,
      "view_items": [
        {
          "content": "0c8318d9-cc79-4f1b-b500-ea84d2b40371",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "64a89cad-9373-4017-ba04-d06f97a28e8c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cb078829-0c0e-426f-b1d6-850e9396f070",
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
          "name": "Example: Extrahop Reveal(x) search devices",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_search_devices",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 76
        }
      ]
    },
    {
      "created_date": 1651163000421,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Search for and download packets stored on the ExtraHop Reveal(x) system.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) search packets",
      "export_key": "funct_extrahop_rx_search_packets",
      "id": 76,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1653920194165,
      "name": "funct_extrahop_rx_search_packets",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": {\"attachment\": \"\u003cb\u003eextrahop 2022-05-11 16.00.00 to 2022-05-12 21.39.30 PDT.pcap\u003c/b\u003e\"}}, \"raw\": null, \"inputs\": {\"extrahop_port1\": null, \"extrahop_ip2\": null, \"extrahop_ip1\": null, \"extrahop_port2\": null, \"incident_id\": 4307, \"extrahop_limit_search_duration\": null, \"extrahop_active_from\": 1652310000000, \"extrahop_bpf\": \"host 192.168.1.2\", \"extrahop_output\": \"pcap\", \"extrahop_limit_bytes\": null, \"extrahop_active_until\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 20395, \"timestamp\": \"2022-05-17 11:24:39\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"object\", \"properties\": {\"attachment\": {\"type\": \"string\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_port1\": {}, \"extrahop_ip2\": {}, \"extrahop_ip1\": {}, \"extrahop_port2\": {}, \"incident_id\": {\"type\": \"integer\"}, \"extrahop_limit_search_duration\": {}, \"extrahop_active_from\": {\"type\": \"integer\"}, \"extrahop_bpf\": {\"type\": \"string\"}, \"extrahop_output\": {\"type\": \"string\"}, \"extrahop_limit_bytes\": {}, \"extrahop_active_until\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "f551a853-62d0-468d-9e36-df5904c5bf96",
      "version": 2,
      "view_items": [
        {
          "content": "3eb56561-8f36-458f-845a-eb3923bd0073",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70f63d36-2b02-4939-ad37-620659809eaa",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ae497dab-1605-4b71-b997-61b0e9a9ca46",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "68a4691f-8609-4d19-9208-3a7589a37997",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eef5fc53-d7d2-4711-9263-ccec47dacd13",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d265d66f-635b-4f5c-8aa5-d7146f65ac15",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "980e64f8-1d36-4d58-a611-0d3c54a9bf02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "19778340-0ca0-47af-bb7b-61d0d2be6fa1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f844555a-e911-4ea3-95c2-44ad4f8c5ef9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6aa0c2da-9841-4b51-9c22-bd8d245d9cc6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4756201b-b5b0-4a90-934d-815e13644e5e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd451766-afc3-40d7-86c8-5c512586b7d0",
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
          "name": "Example: Extrahop Reveal(x) search packets",
          "object_type": "artifact",
          "programmatic_name": "wf_extrahop_rx_search_packets",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 92
        }
      ]
    },
    {
      "created_date": 1651163000622,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Update a detection in Extrahop Reveal(x). Required parameter incident_id, detection_id, owner_id, plan_status, resolution. Optional parameters participants.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) update detection",
      "export_key": "funct_extrahop_rx_update_detection",
      "id": 77,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1651163000802,
      "name": "funct_extrahop_rx_update_detection",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": \"success\"}, \"raw\": null, \"inputs\": {\"incident_id\": 3235, \"soar_inc_owner_id\": \"a@a.com\", \"soar_inc_resolution_id\": \"Resolved\", \"extrahop_detection_id\": 71, \"soar_inc_plan_status\": \"C\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 1084, \"timestamp\": \"2022-04-13 17:21:32\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"soar_inc_owner_id\": {\"type\": \"string\"}, \"soar_inc_resolution_id\": {\"type\": \"string\"}, \"extrahop_detection_id\": {\"type\": \"integer\"}, \"soar_inc_plan_status\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "8ee5a0dc-d7d9-4d02-85a3-55d340a43aa0",
      "version": 1,
      "view_items": [
        {
          "content": "3eb56561-8f36-458f-845a-eb3923bd0073",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2cd40098-aebb-4efd-8b30-eca7edfb8438",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "dce787c0-2575-4dde-b0fa-a453fff3c941",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ccbe84af-c0ae-4ae5-a280-c84d1bde5f4d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "88360341-cb95-4040-9f2c-920f41d138bf",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13f7dfc8-67b0-4ead-a5c7-191d915cf79b",
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
          "name": "Example: Extrahop Reveal(x) update detection",
          "object_type": "incident",
          "programmatic_name": "wf_extrahop_rx_update_detection",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 82
        }
      ]
    },
    {
      "created_date": 1649934558375,
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "description": {
        "content": "Add or remove devices from the watchlist on Extrahop Reveal(x). Required parameter assign or unassign comma-seperated list of devices.",
        "format": "text"
      },
      "destination_handle": "fn_extrahop",
      "display_name": "Extrahop Reveal(x) update watchlist",
      "export_key": "funct_extrahop_rx_update_watchlist",
      "id": 57,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 4,
        "name": "a@a.com",
        "type": "user"
      },
      "last_modified_time": 1650621635304,
      "name": "funct_extrahop_rx_update_watchlist",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"result\": \"success\"}, \"raw\": null, \"inputs\": {\"extrahop_assign\": \"3\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-extrahop\", \"package_version\": \"1.0.0\", \"host\": \"myhost.ibm.com\", \"execution_time_ms\": 719, \"timestamp\": \"2022-04-13 17:17:23\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"extrahop_assign\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b8d33930-3417-436e-82a1-267a5dc9fa91",
      "version": 2,
      "view_items": [
        {
          "content": "a4628ae7-81c6-4208-ba4f-e71295f3c117",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a19c702d-206d-48a7-8b26-80d7d4aaa4b6",
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
          "name": "Example: Extrahop Reveal(x) update watchlist",
          "object_type": "extrahop_devices",
          "programmatic_name": "wf_extrahop_rx_update_watchlist",
          "tags": [
            {
              "tag_handle": "fn_extrahop",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 74
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 83,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1654103732605,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1654103732605,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "a0ece8a1-8c47-4e39-99af-1658e358df1f"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_extrahop",
      "name": "fn_extrahop",
      "programmatic_name": "fn_extrahop",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "users": [
        "a@a.com"
      ],
      "uuid": "f81b5729-e662-495a-8b49-b2c934b5c26e"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1652878835323,
      "creator_id": "a@a.com",
      "description": "Set ExtraHop detection properties as workflow property dicts.",
      "enabled": false,
      "export_key": "scr_extrahop_detection_property_helper",
      "id": 6,
      "language": "python",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654091969223,
      "name": "scr_extrahop_detection_property_helper",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "scr_extrahop_set_properties",
      "script_text": "##  ExtraHop - scr_extrahop_detection_property_helper script ##\n# Used to share data with several workflows.\n\n# Map of detection category  display name to name.\nCATEGORY_MAP = {\n    \"sec.action\": \"Actions on Objective\",\n    \"sec.botnet\": \"Botnet\",\n    \"sec.caution\": \"Caution\",\n    \"sec.command\": \"Command \u0026 Control\",\n    \"sec.cryptomining\": \"Cryptocurrency Mining\",\n    \"sec.dos\": \"Denial of Service\",\n    \"sec.exfil\": \"Exfiltration\",\n    \"sec.exploit\": \"Exploitation\",\n    \"sec.hardening\": \"Hardening\",\n    \"sec.lateral\": \"Lateral Movement\",\n    \"sec.ransomware\": \"Ransomware\",\n    \"sec.recon\": \"Reconnaissance\",\n    \"sec\": \"Security\"\n}\n# Map of detection type name to  display name.\nTYPE_MAP = {\n    \"aaa_auth_errors\": \"AAA Auth Errors\",\n    \"aaa_brute_force\": \"Spike in AAA Failed Login Attempts\",\n    \"abnormally_large_database_response\": \"Database Data Staging\",\n    \"abnormal_s3_upload\": \"Data Exfiltration to S3 Bucket\",\n    \"abnormal_user_creation\": \"Unusual User Creation\",\n    \"add_printer_driver\": \"New Printer Driver Installation Request\",\n    \"anonymous_ftp\": \"Anonymous FTP Auth Enabled\",\n    \"apache_http_server_path_traversal\": \"Apache HTTP Server Path Traversal Exploit\",\n    \"apache_struts2_exploit_attempt\": \"Apache Struts 2 Exploit Attempt\",\n    \"attempted_connections_dropped\": \"Attempted Connections Dropped\",\n    \"aws_imds_proxying\": \"AWS Instance Metadata Service (IMDS) Proxy\",\n    \"aws_services_enumeration\": \"AWS Cloud Service Enumeration\",\n    \"bittorrent_activity\": \"BitTorrent Activity\",\n    \"blacklisted_cert\": \"Suspicious SSL/TLS Certificates\",\n    \"bloodhound_enumeration_activity\": \"BloodHound Enumeration Activity\",\n    \"c2_web_beaconing\": \"Command-and-Control Beaconing\",\n    \"call_does_not_exist_error\": \"Call Does Not Exist Error\",\n    \"cifs_round_trip_time\": \"SMB/CIFS Transaction Delays\",\n    \"cisco_cdp_vulnerabilities\": \"Cisco CDP Exploit Attempt\",\n    \"citrix_issues\": \"Citrix Issues\",\n    \"cobalt_strike_c2_dns\": \"Cobalt Strike DNS Beaconing\",\n    \"cobalt_strike_c2_http\": \"Cobalt Strike C\u0026C HTTP Connection\",\n    \"cobalt_strike_c2_tls\": \"Cobalt Strike C\u0026C SSL/TLS Connection\",\n    \"crit_server_suspicious_download\": \"Suspicious File Download on Critical Server\",\n    \"cryptocurrency_mining\": \"Cryptocurrency Mining\",\n    \"cryptomining_pool_dns_request\": \"DNS Request for a Cryptocurrency Mining Pool\",\n    \"cryptomining_pool_ssl_connection\": \"SSL/TLS Connection to a Cryptocurrency Mining Pool\",\n    \"customer_detection_template\": \"Custom\",\n    \"cve_2017_12635\": \"CVE-2017-12635 Apache CouchDB Exploit Attempt\",\n    \"cve_2018_1111\": \"CVE-2018-1111 Red Hat DHCP Exploit Attempt\",\n    \"cve_2018_13379\": \"CVE-2018-13379 Fortinet FortiOS Exploit\",\n    \"cve_2018_15961\": \"CVE-2018-15961 Adobe ColdFusion Exploit Attempt\",\n    \"cve_2018_7600\": \"Drupal Exploit Attempt\",\n    \"cve_2019_0193\": \"CVE-2019-0193 Apache Solr Exploit Attempt\",\n    \"cve_2019_0604\": \"CVE-2019-0604 Microsoft SharePoint Exploit Attempt\",\n    \"cve_2019_0708\": \"CVE-2019-0708 RDP Exploit Attempt\",\n    \"cve_2019_10149\": \"CVE-2019-10149 Exim Exploit Attempt\",\n    \"cve_2019_11510\": \"CVE-2019-11510 Pulse Connect Secure Exploit Attempt\",\n    \"cve_2019_11580\": \"CVE-2019-11580: Atlassian Crowd Vulnerability\",\n    \"cve_2019_15846\": \"CVE-2019-15846 Exim Exploit Attempt\",\n    \"cve_2019_17558\": \"CVE-2019-17558 Apache Solr Exploit\",\n    \"cve_2019_19781_exploit\": \"CVE-2019-19781 Citrix ADC and Gateway Exploit\",\n    \"cve_2019_19781_scan\": \"CVE-2019-19781 Citrix ADC and Gateway Scan\",\n    \"cve_2019_2725\": \"Oracle WebLogic Exploit\",\n    \"cve_2019_8394\": \"CVE-2019-8394 Zoho ManageEngine Exploit Attempt\",\n    \"cve_2019_9670\": \"CVE-2019-9670 Synacor Zimbra Collaboration Suite Exploit Attempt\",\n    \"cve_2020_0601\": \"CVE-2020-0601 Windows CryptoAPI ECC Validation Vulnerability\",\n    \"cve_2020_0796\": \"CVE-2020-0796 Windows 10 SMBv3 Exploit Attempt\",\n    \"cve_2020_10189\": \"CVE-2020-10189 Zoho ManageEngine Exploit\",\n    \"cve_2020_11651\": \"CVE-2020-11651 Salt Exploit Attempt\",\n    \"cve_2020_12695\": \"CVE-2020-12695 UPnP Exploit Attempt\",\n    \"cve_2020_1301\": \"CVE-2020-1301 SMBv1 Exploit\",\n    \"cve_2020_1350\": \"CVE-2020-1350 SIGRed Exploit Attempt\",\n    \"cve_2020_1472\": \"CVE-2020-1472 Zerologon Scan\",\n    \"cve_2020_1472_exploit\": \"CVE-2020-1472 Zerologon Exploit Attempt\",\n    \"cve_2020_15505\": \"CVE-2020-15505 MobileIron Core and Connector Exploit Attempt\",\n    \"cve_2020_16898\": \"CVE-2020-16898 Windows TCP/IP Stack Exploit Attempt\",\n    \"cve_2020_16899\": \"CVE-2020-16899 Windows TCP/IP Stack Exploit Attempt\",\n    \"cve_2020_17051\": \"CVE-2020-17051 Windows NFS Exploit Attempt\",\n    \"cve_2020_1938\": \"CVE-2020-1938 Ghostcat Exploit\",\n    \"cve_2020_25577\": \"CVE-2020-25577 FreeBSD Exploit Attempt\",\n    \"cve_2020_25583\": \"CVE-2020-25583 FreeBSD Exploit Attempt\",\n    \"cve_2020_3952\": \"CVE-2020-3952 VMware vCenter Exploit\",\n    \"cve_2020_5902\": \"CVE-2020-5902 F5 BIG-IP Exploit\",\n    \"cve_2020_6207\": \"CVE-2020-6207 SAP Solution Manager Exploit Attempt\",\n    \"cve_2020_6287\": \"CVE-2020-6287 SAP RECON Vulnerability\",\n    \"cve_2020_7247\": \"CVE-2020-7247 OpenSMTPD Exploit Attempt\",\n    \"cve_2021_1497\": \"CVE-2021-1497 Cisco HyperFlex HX Exploit Attempt\",\n    \"cve_2021_1498\": \"CVE-2021-1498 Cisco HyperFlex HX Exploit Attempt\",\n    \"cve_2021_21972_exploit\": \"CVE-2021-21972 VMware vCenter Exploit\",\n    \"cve_2021_21972_scan\": \"CVE-2021-21972 VMware vCenter Scan\",\n    \"cve_2021_21974\": \"CVE-2021-21974 VMware ESXi OpenSLP Exploit Attempt\",\n    \"cve_2021_21985\": \"CVE-2021-21985 VMware vCenter Exploit\",\n    \"cve_2021_22005\": \"CVE-2021-22005 VMware vCenter Exploit\",\n    \"cve_2021_22006\": \"CVE-2021-22006 VMware vCenter Exploit\",\n    \"cve_2021_22205\": \"CVE-2021-22205 GitLab CE and EE Exploit Attempt\",\n    \"cve_2021_22893\": \"CVE-2021-22893 Pulse Connect Secure Exploit Attempt\",\n    \"cve_2021_22986\": \"CVE-2021-22986 F5 BIG-IP and BIG-IQ Exploit\",\n    \"cve_2021_22991\": \"CVE-2021-22991 F5 BIG-IP Exploit\",\n    \"cve_2021_26084\": \"CVE-2021-26084 Atlassian Confluence Exploit Attempt\",\n    \"cve_2021_26432\": \"CVE-2021-26432 Windows NFS ONCRPC Exploit Attempt\",\n    \"cve_2021_26877\": \"CVE-2021-26877 Windows DNS Server Exploit Attempt\",\n    \"cve_2021_26897\": \"CVE-2021-26897 Windows DNS Server Exploit Attempt\",\n    \"cve_2021_28324\": \"CVE-2021-28324 Windows 10 SMBv3 Exploit Attempt\",\n    \"cve_2021_31166\": \"CVE-2021-31166 Windows HTTP Stack Exploit Attempt\",\n    \"cve_2021_31181\": \"CVE-2021-31181 Microsoft SharePoint Exploit Attempt\",\n    \"cve_2021_34467\": \"CVE-2021-34467 Microsoft SharePoint Exploit Attempt\",\n    \"cve_2021_34473\": \"CVE-2021-34473 Microsoft Exchange Server Exploit\",\n    \"cve_2021_34527\": \"CVE-2021-34527 Windows Print Spooler Exploit Attempt\",\n    \"cve_2021_35394\": \"CVE-2021-35394 Realtek SDK Exploit Attempt\",\n    \"cve_2021_35395\": \"CVE-2021-35395 Realtek SDK Exploit Attempt\",\n    \"cve_2021_38647\": \"CVE-2021-38647 OMIGOD Exploit\",\n    \"cve_2021_42321\": \"CVE-2021-42321 Microsoft Exchange Exploit Attempt\",\n    \"cve_2021_43798\": \"CVE-2021-43798 Grafana Exploit Attempt\",\n    \"cve_2021_44228_jndi_injection_attempt\": \"Log4Shell JNDI Injection Attempt\",\n    \"cve_2021_44228_outbound_activity\": \"Outbound Log4Shell Activity\",\n    \"cve_2022_0543\": \"CVE-2022-0543 Redis Exploit\",\n    \"cve_2022_1388\": \"CVE-2022-1388 F5 BIG-IP Exploit\",\n    \"cve_2022_21907\": \"CVE-2022-21907 Windows HTTP Stack Exploit Attempt\",\n    \"cve_2022_22947\": \"CVE-2022-22947 Spring Cloud Gateway Exploit Attempt\",\n    \"cve_2022_22963\": \"CVE-2022-22963 Spring Cloud Function Exploit Attempt\",\n    \"database_brute_force\": \"Database Brute Force\",\n    \"database_enumeration\": \"Database Enumeration\",\n    \"database_issues\": \"Database Issues\",\n    \"database_takeover\": \"Database Takeover Attack\",\n    \"database_transaction_failures\": \"Database Transaction Failures\",\n    \"data_exfil_by_vpn\": \"VPN Client Data Exfiltration\",\n    \"data_exfiltration\": \"Data Exfiltration\",\n    \"data_transfer_issues\": \"Data Transfer Issues\",\n    \"db_processing_spike\": \"Poor Database Performance\",\n    \"dcom_lateral_movement\": \"DCOM Remote Command Launch\",\n    \"dcshadow\": \"DCShadow Attack\",\n    \"dcsync\": \"DCSync Attack\",\n    \"delayed_citrix_data_transfer\": \"Delayed Citrix Data Transfer\",\n    \"delayed_database_data_transfer\": \"Delayed Database Data Transfer\",\n    \"delayed_data_transfer\": \"Delayed Data Transfer\",\n    \"delayed_email_data_transfer\": \"Delayed Email Data Transfer\",\n    \"delayed_ftp_data_transfer\": \"Delayed FTP Data Transfer\",\n    \"delayed_http_data_transfer\": \"Delayed HTTP Data Transfer\",\n    \"delayed_ip_address_configuration\": \"Delayed IP Address Configuration\",\n    \"delayed_kerberos_auth\": \"Delayed Kerberos Auth\",\n    \"delayed_kerberos_data_transfer\": \"Delayed Kerberos Data Transfer\",\n    \"delayed_ldap_auth\": \"Delayed LDAP Auth\",\n    \"delayed_ldap_data_transfer\": \"Delayed LDAP Data Transfer\",\n    \"delayed_memcache_data_transfer\": \"Delayed Memcache Data Transfer\",\n    \"delayed_redis_data_transfer\": \"Delayed Redis Data Transfer\",\n    \"delayed_web_services\": \"Delayed Web Services\",\n    \"delayed_wifi_auth\": \"Delayed WiFi Auth\",\n    \"dhcp_decline_error\": \"DHCP Decline Error\",\n    \"dhcp_errors\": \"DHCP Errors\",\n    \"dhcp_issues\": \"DHCP Issues\",\n    \"dhcp_restart_error\": \"DHCP Restart Error\",\n    \"dns_brute_force\": \"DNS Brute Force\",\n    \"dns_errors\": \"DNS Errors\",\n    \"dns_internal_reverse_lookup_scan\": \"DNS Internal Reverse Lookup Scan\",\n    \"dns_issues\": \"DNS Issues\",\n    \"dns_lookup_failures\": \"DNS Lookup Failures\",\n    \"dns_rebind\": \"DNS Rebinding\",\n    \"dns_request_timeouts\": \"DNS Request Timeouts\",\n    \"dns_timeouts\": \"DNS Timeouts\",\n    \"dns_tunnel\": \"DNS Tunnel\",\n    \"dns_zone_transfer\": \"DNS Zone Transfer\",\n    \"domain_fronting\": \"Domain Fronting\",\n    \"domain_generation_algorithm\": \"Domain Generation Algorithm\",\n    \"domain_generation_algorithm_resolved\": \"DGA Domain Resolution\",\n    \"domain_generation_algorithm_unresolved\": \"DGA Domain Queries\",\n    \"domain_trust_enumeration\": \"Domain Trust Enumeration\",\n    \"domain_trusts_enumeration\": \"Domain Trusts Enumeration\",\n    \"doublepulsar_rdp_implant\": \"DoublePulsar RDP Implant\",\n    \"doublepulsar_rdp_scan\": \"DoublePulsar RDP Scan\",\n    \"doublepulsar_smb_implant\": \"DoublePulsar SMB/CIFS Implant Activity\",\n    \"doublepulsar_smb_scan\": \"DoublePulsar SMB/CIFS Scan\",\n    \"email_errors\": \"Email Errors\",\n    \"email_issues\": \"Email Issues\",\n    \"email_mailbox_unavailable_error\": \"Email Mailbox Unavailable Error\",\n    \"email_service_unavailable_error\": \"Email Service Unavailable Error\",\n    \"empire_c2_http\": \"Empire C\u0026C HTTP Connection\",\n    \"empire_c2_tls\": \"Empire C\u0026C SSL/TLS Connection\",\n    \"eternalblue_exploit\": \"EternalBlue Exploit\",\n    \"excessive_ip_fragmentation\": \"Overlapping IP Fragmentation\",\n    \"experimental\": \"Experimental Detection\",\n    \"experimentalMetric\": \"Experimental Detection for Protocol Activity\",\n    \"experimentalMetricAnomaly\": \"Experimental Detection for a Single Metric\",\n    \"experimentalSource\": \"Experimental Detection for a Single Source\",\n    \"expired_cert\": \"Expired SSL Server Certificates\",\n    \"external_db_req\": \"Request to External Database Server\",\n    \"external_exec_file_download\": \"Unusual Executable File Download\",\n    \"external_ldap_req\": \"Request to External LDAP Server\",\n    \"external_nfs_req\": \"Request to External NFS Server\",\n    \"external_ssh_new_device\": \"New SSH Device\",\n    \"file_access_failure\": \"File Access Failure\",\n    \"ftp_access_denied_error\": \"FTP Access Denied Error\",\n    \"ftp_bad_syntax_error\": \"FTP Bad Syntax Error\",\n    \"ftp_brute_force\": \"FTP Brute Force\",\n    \"ftp_errors\": \"FTP Errors\",\n    \"ftp_file_transfer_issues\": \"FTP File Transfer Issues\",\n    \"ftp_not_logged_in_error\": \"FTP Not Logged in Error\",\n    \"hacking_tools\": \"Hacking Tool Domain Access\",\n    \"high_citrix_latency\": \"High Citrix Latency\",\n    \"http_400_status_codes\": \"HTTP 400 Status Codes\",\n    \"http_bad_requests\": \"HTTP Bad Requests\",\n    \"http_desync_attack\": \"HTTP Desync Attack\",\n    \"http_errors\": \"HTTP Errors\",\n    \"http_forbidden\": \"HTTP Forbidden\",\n    \"http_gateway_timeout_error\": \"HTTP Gateway Timeout Error\",\n    \"http_internal_error\": \"HTTP Internal Error\",\n    \"http_method_scan\": \"HTTP Method Scan\",\n    \"http_not_found\": \"HTTP Not Found\",\n    \"http_path_traversal\": \"HTTP Path Traversal\",\n    \"http_plaintext_password_client\": \"Credentials Sent over HTTP\",\n    \"http_plaintext_password_server\": \"Credentials Received over HTTP\",\n    \"http_service_unavailable_error\": \"HTTP Service Unavailable Error\",\n    \"icmp_tunnel\": \"ICMP Tunnel\",\n    \"inbound_cobalt_strike_connection\": \"Inbound Connection from a Cobalt Strike IP Address\",\n    \"inbound_tor_connection\": \"Inbound Tor Node Connections\",\n    \"interactive_traffic_remote_desktop\": \"Unusual Interactive Traffic from a Remote Desktop\",\n    \"interactive_traffic_shell\": \"Unusual Interactive Traffic from an External Endpoint\",\n    \"interactive_traffic_ssh\": \"Remote Control SSH Traffic\",\n    \"interrupted_citrix_data_transfer\": \"Interrupted Citrix Data Transfer\",\n    \"kali_ssh_server_key\": \"Default Kali Linux SSH Keys\",\n    \"kaseya_ml\": \"REvil C\u0026C Activity (Kaseya Supply Chain)\",\n    \"kaseya_ml_ip\": \"REvil Suspicious Connection (Kaseya Supply Chain)\",\n    \"kaseya_vsa\": \"Kaseya VSA Activity\",\n    \"kerberos_attack_tool_activity\": \"Kerberos Attack Tool Activity\",\n    \"kerberos_auth_errors\": \"Kerberos Auth Errors\",\n    \"kerberos_auth_issues\": \"Kerberos Auth Issues\",\n    \"kerberos_brute_force\": \"Kerberos Brute Force\",\n    \"kerberos_duplicate_sessions_errors\": \"Kerberos Duplicate Sessions Errors\",\n    \"kerberos_expired_password_errors\": \"Kerberos Expired Password Errors\",\n    \"kerberos_golden_ticket_attack\": \"Kerberos Golden Ticket Attack\",\n    \"kerberos_invalid_ticket_errors\": \"Kerberos Invalid Ticket Errors\",\n    \"kerberos_policy_errors\": \"Kerberos Policy Errors\",\n    \"kerberos_revoked_credentials_errors\": \"Kerberos Revoked Credentials Errors\",\n    \"kerberos_service_unknown_errors\": \"Kerberos Service Unknown Errors\",\n    \"kerberos_silver_ticket_attack\": \"Kerberos Silver Ticket Attack\",\n    \"kerberos_sync_errors\": \"Kerberos Sync Errors\",\n    \"kerberos_ticket_errors\": \"Kerberos Ticket Errors\",\n    \"kerberos_unknown_service_errors\": \"Kerberos Unknown Service Errors\",\n    \"kerberos_user_enumeration\": \"Kerberos User Enumeration\",\n    \"kerberos_wrong_password_errors\": \"Kerberos Wrong Password Errors\",\n    \"ldap_all_workstation_enum\": \"Domain Workstation Enumeration\",\n    \"ldap_as_rep_activity\": \"AS-REP Roasting Activity\",\n    \"ldap_auth_error\": \"LDAP Auth Error\",\n    \"ldap_auth_errors\": \"LDAP Auth Errors\",\n    \"ldap_auth_issues\": \"LDAP Auth Issues\",\n    \"ldap_client_any_attribute_enum\": \"LDAP Wildcard Query\",\n    \"ldap_computer_enum\": \"LDAP Computer Enumeration\",\n    \"ldap_gpo_enumeration\": \"LDAP GPO Enumeration\",\n    \"ldap_invalid_credentials_error\": \"LDAP Invalid Credentials Error\",\n    \"ldap_object_enum\": \"All Object Enumeration\",\n    \"ldap_operational_error\": \"LDAP Operational Error\",\n    \"ldap_protocol_error\": \"LDAP Protocol Error\",\n    \"ldap_spn_scan\": \"LDAP SPN Scan\",\n    \"llmnr_poisoning\": \"LLMNR Poisoning\",\n    \"local_admin_enumeration\": \"Windows Account Enumeration\",\n    \"memcache_errors\": \"Memcache Errors\",\n    \"memcache_issues\": \"Memcache Issues\",\n    \"meterpreter_shell\": \"Meterpreter C\u0026C Session\",\n    \"ms_exchange_ssrf_rce\": \"Microsoft Exchange Server SSRF and RCE Exploit\",\n    \"msf_cert\": \"Metasploit C\u0026C SSL/TLS Connection\",\n    \"msrpc_admin_access_check\": \"Unusual Remote Admin Connection Requests\",\n    \"msrpc_alias_member_enum\": \"Alias Member Enumeration\",\n    \"msrpc_domain_controller_enumeration\": \"Domain Controller Enumeration\",\n    \"msrpc_group_member_enum\": \"Group Member Enumeration\",\n    \"msrpc_loggedon_user_enum\": \"Logged-On User Enumeration\",\n    \"msrpc_netsession_enum\": \"User Session Enumeration\",\n    \"msrpc_network_share_enum\": \"Network Share Enumeration\",\n    \"msrpc_rdp_session_enum\": \"RDP Session Enumeration\",\n    \"msrpc_registry_enumeration_via_winreg\": \"Windows Registry Enumeration\",\n    \"msrpc_scheduled_task_via_atsvc\": \"Scheduled Task Activity (ATSVC)\",\n    \"msrpc_scheduled_task_via_ITaskSchedulerService\": \"Scheduled Task Activity (ITaskSchedulerService)\",\n    \"multiple_email_errors\": \"Multiple Email Errors\",\n    \"multiple_ftp_errors\": \"Multiple FTP Errors\",\n    \"multiple_kerberos_auth_errors\": \"Multiple Kerberos Authentication Errors\",\n    \"multiple_ldap_auth_errors\": \"Multiple LDAP Auth Errors\",\n    \"multiple_smb_cifs_errors\": \"Multiple SMB/CIFS Errors\",\n    \"nbt_ns_poisoning\": \"NBT-NS Poisoning\",\n    \"network_privilege_escalation\": \"Network Privilege Escalation\",\n    \"new_adws_activity\": \"New Active Directory Web Service (ADWS) Activity\",\n    \"new_dhcp_activity\": \"New DHCP Activity\",\n    \"new_doh_activity\": \"New DNS over HTTPS (DoH) Activity\",\n    \"new_external_connection\": \"New External Connection\",\n    \"new_external_db_connection\": \"New External Database Connection\",\n    \"new_external_iiop_connection\": \"New External IIOP Connection\",\n    \"new_external_ldap_connection\": \"New External LDAP Connection\",\n    \"new_external_nfs_connection\": \"New External NFS Connection\",\n    \"new_external_rdp_connection\": \"New External RDP Connection\",\n    \"new_external_rmi_connection\": \"New External Java RMI Connection\",\n    \"new_external_ssh_connection\": \"New External SSH Connection\",\n    \"new_external_telnet_connection\": \"New External Telnet Connection\",\n    \"new_external_vnc_connection\": \"New External VNC Connection\",\n    \"new_iot_connection\": \"New External IoT Connection\",\n    \"new_local_dns_server\": \"New Local DNS Server Activity\",\n    \"new_smb_cifs_file_transfer\": \"New SMB/CIFS Executable File Transfer\",\n    \"new_telnet_activity\": \"New Telnet Activity\",\n    \"nfs_file_access_failure\": \"NFS File Access Failure\",\n    \"ntlm_relay\": \"NTLM Relay Attack\",\n    \"ntlmv1_authentication\": \"NTLMv1 Authentication\",\n    \"numerous_emails\": \"Numerous Emails\",\n    \"onepercent_ml\": \"Confirmed OnePercent Group Ransomware IOC\",\n    \"outbound_cobalt_strike_connection\": \"Outbound Connection to a Cobalt Strike IP Address\",\n    \"outbound_socks_connection\": \"New Outbound SOCKS Connection\",\n    \"outbound_tor_connection\": \"Outbound Tor Node Connections\",\n    \"overwhelmed_citrix_data_transfer\": \"Overwhelmed Citrix Data Transfer\",\n    \"overwhelmed_database_data_transfer\": \"Overwhelmed Database Data Transfer\",\n    \"overwhelmed_data_transfer\": \"Overwhelmed Data Transfer\",\n    \"overwhelmed_email_data_transfer\": \"Overwhelmed Email Data Transfer\",\n    \"overwhelmed_ftp_data_transfer\": \"Overwhelmed FTP Data Transfer\",\n    \"overwhelmed_http_data_transfer\": \"Overwhelmed HTTP Data Transfer\",\n    \"overwhelmed_kerberos_data_transfer\": \"Overwhelmed Kerberos Data Transfer\",\n    \"overwhelmed_ldap_data_transfer\": \"Overwhelmed LDAP Data Transfer\",\n    \"overwhelmed_memcache_data_transfer\": \"Overwhelmed Memcache Data Transfer\",\n    \"overwhelmed_redis_data_transfer\": \"Overwhelmed Redis Data Transfer\",\n    \"ping_scan\": \"Ping Scan\",\n    \"poor_aaa_performance\": \"Poor AAA Performance\",\n    \"poor_dhcp_performance\": \"Poor DHCP Performance\",\n    \"poor_http_performance\": \"Poor HTTP Performance\",\n    \"potential_covert_channel\": \"HTTP Tunnel\",\n    \"psexec_activity\": \"Remote Service Launch\",\n    \"ransomware_activity\": \"Ransomware Activity\",\n    \"rare_database_table_access\": \"Rare Database Table Access\",\n    \"rare_ssh_port\": \"Rare SSH Port\",\n    \"rdp_brute_force\": \"RDP Brute Force\",\n    \"rdp_unusual_location\": \"Inbound Remote Desktop Traffic from an Unusual Location\",\n    \"redis_errors\": \"Redis Errors\",\n    \"redis_issues\": \"Redis Issues\",\n    \"remote_reg_setvalue\": \"Remote Registry Modification\",\n    \"reverse_ssh_connection\": \"Reverse SSH Connection\",\n    \"rfb_brute_force\": \"VNC Brute Force\",\n    \"ripple20_dns_rce\": \"CVE-2020-11901 Ripple20 Exploit Attempt\",\n    \"ripple20_icmp_scan\": \"Ripple20 ICMP Scan\",\n    \"ripple20_icmp_treck\": \"Treck TCP/IP Network Stack Detected\",\n    \"ripple20_ip_in_ip\": \"Ripple20 IP in IP Exploit Attempt\",\n    \"ripple20_ip_in_ip_ipaddr\": \"Ripple20 IP in IP Exploit Attempt\",\n    \"rpc_log_deletion_srv\": \"Remote Log Deletion\",\n    \"rpc_remote_shutdown\": \"Remote System Shutdown\",\n    \"samr_domain_admin_enum\": \"Domain Admin Enumeration\",\n    \"samr_domain_computer_enum\": \"Domain Workstation Enumeration\",\n    \"samr_domain_group_enum\": \"Domain Group Enumeration\",\n    \"samr_domain_user_enum\": \"Domain User Enumeration\",\n    \"samr_domain_workstation_enum\": \"Domain Workstation Enumeration\",\n    \"samr_local_admin_enum\": \"Local Admin Enumeration\",\n    \"samr_local_user_enum\": \"Local User Enumeration\",\n    \"scheduled_task_enumeration\": \"Scheduled Task Enumeration\",\n    \"sensitive_data_transfer\": \"Unusual Sensitive Data Transfer\",\n    \"shellshock_dhcp\": \"Shellshock DHCP Exploit Attempt\",\n    \"shellshock_http\": \"Shellshock HTTP Exploit Attempt\",\n    \"sip_brute_force\": \"SIP Brute Force\",\n    \"smb_autostart_path\": \"File Transfer to Windows Autostart Path\",\n    \"smb_cifs_access_denied_errors\": \"SMB/CIFS Access Denied Errors\",\n    \"smb_cifs_brute_force\": \"SMB/CIFS Brute Force\",\n    \"smb_cifs_errors\": \"SMB/CIFS Errors\",\n    \"smb_cifs_file_access_failure\": \"SMB/CIFS File Access Failure\",\n    \"smb_cifs_privileged_pipe\": \"SMB/CIFS Privileged Pipe\",\n    \"smb_cifs_share_enumeration\": \"SMB/CIFS Share Enumeration\",\n    \"smb_cifs_valid_login_errors\": \"SMB/CIFS Account Errors\",\n    \"smb_named_pipe_beaconing\": \"SMB/CIFS Named Pipe Beaconing\",\n    \"smtp_helo_ehlo_buffer_overflow\": \"Unusual Email Domain Length\",\n    \"smtp_processing_spike\": \"Poor SMTP Server Performance\",\n    \"smtp_syntax_error\": \"SMTP Syntax Error\",\n    \"spike_in_email_traffic_volume\": \"Spike in Email Traffic Volume\",\n    \"spike_in_ldap_requests\": \"Spike in LDAP Requests\",\n    \"spike_in_rdp_sessions\": \"Spike in RDP Sessions\",\n    \"spike_in_rfb_sessions\": \"Spike in VNC Sessions\",\n    \"spike_in_round_trip_time\": \"Transaction Delays\",\n    \"spike_in_ssh_sessions\": \"Spike in SSH Sessions\",\n    \"spike_in_telnet_connections\": \"Spike in Telnet Connections\",\n    \"spoofed_self_signed_ssl_certificate\": \"Spoofed SSL/TLS Certificate\",\n    \"spring4shell\": \"CVE-2022-22965 Spring4Shell Exploit Attempt\",\n    \"sqli_attack\": \"SQL Injection (SQLi) Attack\",\n    \"ssh_brute_force\": \"SSH Brute Force\",\n    \"ssh_unusual_location\": \"Inbound SSH Traffic from an Unusual Location\",\n    \"ssh_unusual_location_c2\": \"Outbound SSH Traffic to an Unusual Location\",\n    \"ssl_scan\": \"SSL Scan\",\n    \"stalled_data_transfer\": \"Stalled Data Transfer\",\n    \"sudden_decrease_in_application_bandwidth\": \"Sudden Decrease in Application Bandwidth\",\n    \"sudden_decrease_in_device_bandwidth\": \"Sudden Decrease in Device Bandwidth\",\n    \"sudden_decrease_in_network_bandwidth\": \"Sudden Decrease in Network Bandwidth\",\n    \"sunburst\": \"SUNBURST C\u0026C Activity\",\n    \"supernova_web_shell_command\": \"SUPERNOVA Web Shell\",\n    \"suspicious_cifs\": \"Suspicious SMB/CIFS Resource Accessed\",\n    \"suspicious_file_download_external\": \"Suspicious External File Download\",\n    \"suspicious_file_download_internal\": \"Suspicious Internal File Download\",\n    \"suspicious_ftp_data_reads\": \"FTP Data Staging\",\n    \"suspicious_ftp_download\": \"Suspicious FTP Download\",\n    \"suspicious_hta_download\": \"Unusual HTML Application (HTA) File Download\",\n    \"suspicious_http_file\": \"Suspicious HTTP File Received\",\n    \"suspicious_http_port\": \"Non-standard HTTP Port\",\n    \"suspicious_ja3_fingerprint\": \"Suspicious JA3 Fingerprint\",\n    \"suspicious_new_device\": \"Suspicious New Device Detected\",\n    \"suspicious_nfs_data_reads\": \"NFS Data Staging\",\n    \"suspicious_nfs_file_reads\": \"Suspicious NFS File Reads\",\n    \"suspicious_nfs_file_share_access\": \"Suspicious NFS File Share Access\",\n    \"suspicious_rdp_client\": \"RDP Attack Tool Activity\",\n    \"suspicious_smb_cifs_data_reads\": \"SMB/CIFS Data Staging\",\n    \"suspicious_smb_cifs_file_reads\": \"Suspicious SMB/CIFS File Reads\",\n    \"suspicious_smb_cifs_file_share_access\": \"Suspicious SMB/CIFS File Share Access\",\n    \"suspicious_smb_cifs_file_transfer\": \"Unusual SMB/CIFS Executable File Transfer\",\n    \"suspicious_smb_named_pipe\": \"Suspicious SMB/CIFS Named Pipe\",\n    \"suspicious_tld\": \"Suspicious Top-level Domain\",\n    \"suspicious_user_agent\": \"Suspicious User Agent\",\n    \"tcp_null_fin_or_xmas_scan\": \"TCP NULL, FIN, or XMAS Scan\",\n    \"tcp_syn_scan\": \"TCP SYN Scan\",\n    \"tcp_urg_flag_client\": \"TCP Stack Exploit Attempt (Client)\",\n    \"tcp_urg_flag_server\": \"TCP Stack Exploit Attempt (Server)\",\n    \"telnet_password\": \"Telnet Password\",\n    \"ti_dns_host\": \"DNS Client Request to a Suspicious Host\",\n    \"ti_http_host\": \"HTTP Client Request to a Suspicious Host\",\n    \"ti_http_uri\": \"HTTP Client Request to a Suspicious URI\",\n    \"ti_ssl_sni\": \"SSL/TLS Connection to a Suspicious Host\",\n    \"ti_tcp_incoming\": \"Inbound Suspicious Connections\",\n    \"ti_tcp_outgoing\": \"Outbound Suspicious Connection\",\n    \"tomcat_jsp_upload\": \"Apache Tomcat JSP Exploit Attempt\",\n    \"udp_port_scan\": \"UDP Port Scan\",\n    \"unapproved_saas\": \"Unapproved Cloud Service Access\",\n    \"unauthorized_caller_error\": \"Unauthorized Caller Error\",\n    \"unconventional_data_transfer\": \"Unconventional Data Transfer\",\n    \"unconventional_new_external_host\": \"Unconventional External Connection\",\n    \"unconventional_new_internal_host\": \"Unconventional Internal Connection\",\n    \"unconventional_new_protocol\": \"Unconventional Protocol Communication\",\n    \"unconventional_rdp_behavior\": \"Unconventional RDP Behavior\",\n    \"unconventional_rdp_data_transfer\": \"Unconventional RDP Data Transfer\",\n    \"unconventional_rfb_behavior\": \"Unconventional VNC Behavior\",\n    \"unconventional_rfb_data_transfer\": \"Unconventional VNC Data Transfer\",\n    \"unconventional_smb_cifs_data_transfer\": \"Unconventional SMB/CIFS Data Transfer\",\n    \"unconventional_ssh_behavior\": \"Unconventional SSH Behavior\",\n    \"unconventional_ssh_data_transfer\": \"Unconventional SSH Data Transfer\",\n    \"unconventional_telnet_data_transfer\": \"Unconventional Telnet Data Transfer\",\n    \"unencrypted_zoom\": \"Unencrypted Zoom Data\",\n    \"unexpected_dropped_connections\": \"Unexpected Dropped Connections\",\n    \"unexpected_service_access\": \"Unexpected Service Access\",\n    \"unknown_public_dns_server\": \"Unknown Public DNS Server\",\n    \"unknown_s3_bucket_upload\": \"Data Exfiltration to Unknown S3 Bucket\",\n    \"unsafe_ldap_auth\": \"Unsafe LDAP Authentication\",\n    \"unusual_iot_protocol\": \"Unusual IoT Protocol Activity\",\n    \"unusual_kerberos_fingerprint\": \"Unusual Kerberos Fingerprint\",\n    \"unusual_protocol_for_enterprise_software\": \"Unusual Protocol for Enterprise Software\",\n    \"unusual_s3_download\": \"Unusual Download from S3 Bucket\",\n    \"unusual_user_login_time\": \"Unusual Login Time\",\n    \"vnc_unusual_location\": \"Inbound VNC Traffic from an Unusual Location\",\n    \"voip_call_failure\": \"VoIP Call Failure\",\n    \"voip_unavailability_error\": \"VoIP Unavailability Error\",\n    \"vpn_gateway_unusual_location\": \"VPN Gateway Access from an Unusual Location\",\n    \"weak_cipher\": \"Weak Cipher Suites\",\n    \"weak_kerberos_encryption_attempt\": \"Weak Kerberos Encryption\",\n    \"web_directory_scan\": \"Web Directory Scan\",\n    \"web_issues\": \"Web Issues\",\n    \"weblogic_admin_console_handle_rce\": \"Oracle WebLogic Administration Console Exploit Attempt\",\n    \"weblogic_xml_deserialization\": \"Oracle WebLogic Deserialization Exploit Attempt\",\n    \"web_service_issues\": \"Web Service Issues\",\n    \"wifi_auth_issues\": \"WiFi Auth Issues\",\n    \"wmi_activity\": \"New WMI Method Launch\",\n    \"wmi_create_process\": \"New WMI Process Creation\",\n    \"wmi_enumeration_query\": \"New WMI Enumeration Query\",\n    \"wordpress_brute_force\": \"WordPress Brute Force\",\n    \"wsman_activity\": \"PowerShell Remoting Activity\",\n    \"xss_attack\": \"Cross-Site Scripting (XSS) Attack\"\n}\n\nworkflow.addProperty(\"category_map\", CATEGORY_MAP)\nworkflow.addProperty(\"type_map\", TYPE_MAP)\n\nif rule.properties.extrahop_detection_id:\n    workflow.addProperty(\"det_id_set\", {})",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "e934b42f-f5c5-4117-97ba-e07cfbba59c5"
    },
    {
      "actions": [],
      "created_date": 1654099229198,
      "creator_id": "a@a.com",
      "description": "Set ExtraHop device properties as workflow property dicts.",
      "enabled": false,
      "export_key": "scr_extrahop_device_property_helper",
      "id": 14,
      "language": "python3",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654099328780,
      "name": "scr_extrahop_device_property_helper",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "dd",
      "script_text": "##  ExtraHop - scr_extrahop_device_property_helper script ##\n# Used to share data with other workflows.\nif rule.properties.extrahop_device_id:\n    workflow.addProperty(\"dev_id_set\", {})",
      "tags": [],
      "uuid": "49851abe-51dd-46da-9822-1cba3ee7d172"
    },
    {
      "actions": [],
      "created_date": 1649952719461,
      "creator_id": "a@a.com",
      "description": "Add Devices data table field as a SOAR artifact.",
      "enabled": false,
      "export_key": "scr_extrahop_rx_add_artifact_from_device",
      "id": 3,
      "language": "python",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654103563870,
      "name": "scr_extrahop_rx_add_artifact_from_device",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "scr_sep_add_artifact_from_scan_results",
      "script_text": "# Create a Resilient artifact based on a dropdown which selects the corresponding data-table field.\nARTIFACT_TYPE = rule.properties.extrahop_artifact_type.replace(\" (v4)\" ,\"\").replace(\" (v6)\" ,\"\")\n\nPARAMS = {\n    \"IP Address\": row.ipaddr4,\n    \"DNS Name\": row.dns_name,\n    \"MAC Address\": row.macaddr\n}\n# Both IP address V4 or V6 will be added as type \"IP Address\".\nif \"v6\" in rule.properties.extrahop_artifact_type:\n    PARAMS.update({\"IP Address\": row.ipaddr6})\n\ndef addArtifact(artifact_type, artifact_value, description):\n    \"\"\"This method adds new artifacts to the incident derived from matches of the the regular expression\n\n    :param artifact_type: The type of the artifact.\n    :param artifact_value: - The value of the artifact.\n    :param description: - the description of the artifact.\n    \"\"\"\n    incident.addArtifact(artifact_type, artifact_value, description)\n\ndef validate_fields(fields, params):\n    \"\"\"\n    Ensure required fields are present. Throw ValueError if not\n    :param fields: Required fields.\n    :param params: Data-table fields as parameters.\n    :return: no return\n    \"\"\"\n    for f in fields:\n        if f not in params or not params.get(f) or params.get(f) == \u0027\u0027:\n            raise ValueError(str(\u0027Required data-table field is missing or empty for artifact type: \u0027 + f))\n\n\ndef main():\n    desc = \u0027\u0027\n\n    validate_fields([ARTIFACT_TYPE], PARAMS)\n\n    desc = \"Artifact from Device detected in the ExtraHop environment. Device name \u0027{}\u0027, Device ID \u0027{}\u0027.\".format(row.default_name, row.devs_id)\n    addArtifact(ARTIFACT_TYPE, PARAMS[ARTIFACT_TYPE], desc)\n\n\n# Script execution starts here\nif __name__ == \"__main__\":\n    main()",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b22a440f-5bd8-4d14-a34e-9fe51dad99fb"
    }
  ],
  "server_version": {
    "build_number": 41,
    "major": 41,
    "minor": 2,
    "version": "41.2.41"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "ExtraHop Activitymaps",
      "export_key": "extrahop_activitymaps",
      "fields": {
        "ams_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_description",
          "hide_notification": false,
          "id": 645,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_description",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "c2b5859c-61be-4e53-9560-3677fe57c0ff",
          "values": [],
          "width": 88
        },
        "ams_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_id",
          "hide_notification": false,
          "id": 646,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "39022bfb-713f-43f7-ac47-f17d6a857f8a",
          "values": [],
          "width": 18
        },
        "ams_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/ams_name",
          "hide_notification": false,
          "id": 647,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ams_name",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Name",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "41121269-26c3-4cbd-8131-d65339a7455e",
          "values": [],
          "width": 44
        },
        "mod_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/mod_time",
          "hide_notification": false,
          "id": 648,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mod time",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "7467ba91-6d24-4d7e-9e8b-ca27877ad449",
          "values": [],
          "width": 34
        },
        "mode": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/mode",
          "hide_notification": false,
          "id": 649,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "mode",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mode",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "779f44c3-eb2d-41fe-b570-1b5195847dec",
          "values": [],
          "width": 41
        },
        "owner": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/owner",
          "hide_notification": false,
          "id": 650,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "owner",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Owner",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "309b4088-7cc0-4ff3-96f6-e9d9de24b965",
          "values": [],
          "width": 50
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/query_execution_date",
          "hide_notification": false,
          "id": 651,
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
          "type_id": 1033,
          "uuid": "cbe6cb23-7dbb-468b-a3ae-097fede6a055",
          "values": [],
          "width": 75
        },
        "rights": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/rights",
          "hide_notification": false,
          "id": 652,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "rights",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Rights",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "d0ee5116-6629-4ca4-b87b-89ac91240207",
          "values": [],
          "width": 48
        },
        "short_code": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/short_code",
          "hide_notification": false,
          "id": 653,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "short_code",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Short code",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "438e0eec-1608-462e-89c0-bcac47d1e2d4",
          "values": [],
          "width": 42
        },
        "show_alert_status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/show_alert_status",
          "hide_notification": false,
          "id": 654,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "show_alert_status",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Show alert status",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "ed6be14d-c73d-43ad-bcc0-22650a4811b2",
          "values": [],
          "width": 47
        },
        "walks": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/walks",
          "hide_notification": false,
          "id": 655,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "walks",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Walks",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "004aa07c-fcf4-40b8-93d5-3e9b965c092f",
          "values": [],
          "width": 98
        },
        "weighting": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_activitymaps/weighting",
          "hide_notification": false,
          "id": 656,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "weighting",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Weighting",
          "tooltip": "",
          "type_id": 1033,
          "uuid": "48a3c9a6-2502-40db-9dce-71a0715c48b4",
          "values": [],
          "width": 77
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_activitymaps",
      "uuid": "7ff13989-c3e2-4797-81cd-3766c947c452"
    },
    {
      "actions": [],
      "display_name": "Extrahop Detections",
      "export_key": "extrahop_detections",
      "fields": {
        "appliance_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/appliance_id",
          "hide_notification": false,
          "id": 657,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "appliance_id",
          "operation_perms": {},
          "operations": [],
          "order": 21,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Appliance id",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "e07d8028-42a2-4e38-8b55-06485e4aba47",
          "values": [],
          "width": 77
        },
        "assignee": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/assignee",
          "hide_notification": false,
          "id": 658,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "assignee",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Assignee",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "3ae88e4a-bed0-4120-9af0-908cb0cdb75a",
          "values": [],
          "width": 69
        },
        "categories": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/categories",
          "hide_notification": false,
          "id": 659,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "categories",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Categories",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "6ebb268c-f45a-4fc9-9259-d0e389302d76",
          "values": [],
          "width": 82
        },
        "det_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/det_description",
          "hide_notification": false,
          "id": 660,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "det_description",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "7a0898df-d4cb-4b2a-8270-97f08ebeab5a",
          "values": [],
          "width": 305
        },
        "det_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/det_id",
          "hide_notification": false,
          "id": 661,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "det_id",
          "operation_perms": {},
          "operations": [],
          "order": 20,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "337912b5-f97b-4746-b1c8-1b915d82b2d0",
          "values": [],
          "width": 18
        },
        "detection_url": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/detection_url",
          "hide_notification": false,
          "id": 1230,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "detection_url",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Detection URL",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "def6c0a2-9ccd-4efb-ba3f-2c4338c2f45f",
          "values": [],
          "width": 74
        },
        "end_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/end_time",
          "hide_notification": false,
          "id": 662,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "end_time",
          "operation_perms": {},
          "operations": [],
          "order": 16,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "End time",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "a5b713fc-f606-4f33-80e1-30faef26f6ae",
          "values": [],
          "width": 70
        },
        "is_user_created": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/is_user_created",
          "hide_notification": false,
          "id": 663,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "is_user_created",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Is user created",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "0b055da1-91f0-4437-be4b-3899ece4c732",
          "values": [],
          "width": 58
        },
        "mitre_tactics": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/mitre_tactics",
          "hide_notification": false,
          "id": 664,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "mitre_tactics",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Mitre tactics",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "dd7b464d-629f-4a6d-adb3-ce035dd1f7f4",
          "values": [],
          "width": 188
        },
        "mitre_techniques": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/mitre_techniques",
          "hide_notification": false,
          "id": 665,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "mitre_techniques",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Mitre techniques",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "feb16d57-13de-42c0-a9bd-78308de095de",
          "values": [],
          "width": 182
        },
        "participants": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/participants",
          "hide_notification": false,
          "id": 666,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "participants",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Participants",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "039c878d-c07e-440b-9bab-fc7d87de4921",
          "values": [],
          "width": 148
        },
        "properties": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/properties",
          "hide_notification": false,
          "id": 667,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "properties",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Properties",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "4a88b4aa-6141-4872-b5e5-4cd69c1b8506",
          "values": [],
          "width": 171
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/query_execution_date",
          "hide_notification": false,
          "id": 668,
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
          "type_id": 1034,
          "uuid": "c3476aba-a7e1-4f01-bfd0-8ab3fd6f98b1",
          "values": [],
          "width": 119
        },
        "resolution": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/resolution",
          "hide_notification": false,
          "id": 669,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "resolution",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Resolution",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "cbb2a8e0-b616-464a-a386-5eaa8cbeb151",
          "values": [],
          "width": 81
        },
        "risk_score": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/risk_score",
          "hide_notification": false,
          "id": 670,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "risk_score",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Risk score",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "2f42568a-0acd-449f-8ce0-0f6bd46c2712",
          "values": [],
          "width": 41
        },
        "start_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/start_time",
          "hide_notification": false,
          "id": 671,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "start_time",
          "operation_perms": {},
          "operations": [],
          "order": 15,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Start time",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "c775c66c-912e-4114-9074-8d34cdbb4b1a",
          "values": [],
          "width": 72
        },
        "status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/status",
          "hide_notification": false,
          "id": 672,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "fd8fa146-2f02-42a7-be7a-95d0ffaa1ccc",
          "values": [],
          "width": 49
        },
        "ticket_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/ticket_id",
          "hide_notification": false,
          "id": 673,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_id",
          "operation_perms": {},
          "operations": [],
          "order": 18,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket ID",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "2947aabf-4274-48cc-b5cb-76ec2816a5ad",
          "values": [],
          "width": 47
        },
        "ticket_url": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/ticket_url",
          "hide_notification": false,
          "id": 674,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_url",
          "operation_perms": {},
          "operations": [],
          "order": 19,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket URL",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "065d5317-5a89-4834-8a72-8ff9658d9563",
          "values": [],
          "width": 47
        },
        "title": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/title",
          "hide_notification": false,
          "id": 675,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "title",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Title",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "85a98923-5167-4f7b-8a6c-3d2c96c0cdf6",
          "values": [],
          "width": 95
        },
        "type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/type",
          "hide_notification": false,
          "id": 676,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "3e8d5dcd-2a86-47b0-bd51-8396d8404244",
          "values": [],
          "width": 120
        },
        "update_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_detections/update_time",
          "hide_notification": false,
          "id": 677,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "update_time",
          "operation_perms": {},
          "operations": [],
          "order": 17,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Update time",
          "tooltip": "",
          "type_id": 1034,
          "uuid": "39aae273-6425-4e18-8dbe-9c3ed08517c5",
          "values": [],
          "width": 70
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_detections",
      "uuid": "712e0e4e-8209-472d-8978-d72f18c2e583"
    },
    {
      "actions": [],
      "display_name": "ExtraHop Devices",
      "export_key": "extrahop_devices",
      "fields": {
        "activity": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/activity",
          "hide_notification": false,
          "id": 809,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "activity",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Activity",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "fb3dd873-04ee-4836-9a4e-e51408568069",
          "values": [],
          "width": 59
        },
        "default_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/default_name",
          "hide_notification": false,
          "id": 810,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "default_name",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Default name",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "e0a7c1d0-9c01-4f1f-8902-341c0bfcaee4",
          "values": [],
          "width": 80
        },
        "device_url": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/device_url",
          "hide_notification": false,
          "id": 938,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "device_url",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Device URL",
          "tooltip": "Linkback to  device on ExtraHop.",
          "type_id": 1038,
          "uuid": "0da6b049-e577-4395-8b95-a574ac532713",
          "values": [],
          "width": 79
        },
        "devs_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/devs_description",
          "hide_notification": false,
          "id": 811,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "devs_description",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "b2041256-ddea-4577-803b-a18389a4d876",
          "values": [],
          "width": 88
        },
        "devs_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/devs_id",
          "hide_notification": false,
          "id": 869,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "devs_id",
          "operation_perms": {},
          "operations": [],
          "order": 13,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "REST API ID",
          "type_id": 1038,
          "uuid": "66e37627-60ba-40f8-9535-103a05dae36f",
          "values": [],
          "width": 63
        },
        "discover_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/discover_time",
          "hide_notification": false,
          "id": 813,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "discover_time",
          "operation_perms": {},
          "operations": [],
          "order": 15,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Discovery time",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "ed736af9-e6ba-494a-b53a-379d9737e598",
          "values": [],
          "width": 151
        },
        "display_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/display_name",
          "hide_notification": false,
          "id": 814,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "display_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Display name",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "2afb30e5-422f-4663-810f-fe8b965a482c",
          "values": [],
          "width": 81
        },
        "dns_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/dns_name",
          "hide_notification": false,
          "id": 815,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "dns_name",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "DNS name",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "88e6cf47-4b8e-4dce-adde-206212ed97b9",
          "values": [],
          "width": 83
        },
        "extrahop_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/extrahop_id",
          "hide_notification": false,
          "id": 816,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "extrahop_id",
          "operation_perms": {},
          "operations": [],
          "order": 14,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ExtraHop  ID",
          "tooltip": "ExtraHop Discovery ID",
          "type_id": 1038,
          "uuid": "2ce02cd6-4559-42de-b65f-84f63237528f",
          "values": [],
          "width": 75
        },
        "ipaddr4": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/ipaddr4",
          "hide_notification": false,
          "id": 817,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr4",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr4",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "9c3eed4d-a6a6-40ac-bf9b-cf92a19c71e2",
          "values": [],
          "width": 83
        },
        "ipaddr6": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/ipaddr6",
          "hide_notification": false,
          "id": 818,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr6",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr6",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "61994faf-d774-4e3d-a2d7-51c0ace7a18a",
          "values": [],
          "width": 88
        },
        "last_seen_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/last_seen_time",
          "hide_notification": false,
          "id": 819,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "last_seen_time",
          "operation_perms": {},
          "operations": [],
          "order": 18,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Last seen time",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "9614750e-7922-4373-ae1f-92e4b514d677",
          "values": [],
          "width": 153
        },
        "macaddr": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/macaddr",
          "hide_notification": false,
          "id": 820,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "macaddr",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "MACaddr",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "c0a1d534-8346-4082-aec8-fbcbd4c01845",
          "values": [],
          "width": 79
        },
        "mod_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/mod_time",
          "hide_notification": false,
          "id": 821,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 17,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Modification time",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "116c7c43-0207-4303-9a1f-9cfb404cf08c",
          "values": [],
          "width": 148
        },
        "on_watchlist": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/on_watchlist",
          "hide_notification": false,
          "id": 822,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "on_watchlist",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "On watchlist",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "5b6864c2-5177-45d7-8a46-c85721e569f1",
          "values": [],
          "width": 71
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/query_execution_date",
          "hide_notification": false,
          "id": 823,
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
          "type_id": 1038,
          "uuid": "9100b462-eafd-4a19-9c0f-9380a168e8d7",
          "values": [],
          "width": 75
        },
        "role": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/role",
          "hide_notification": false,
          "id": 824,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "role",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Role",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "e337a0f0-19c9-461e-878d-0968c0a55260",
          "values": [],
          "width": 96
        },
        "user_mod_time": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/user_mod_time",
          "hide_notification": false,
          "id": 825,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "user_mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 16,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User modification time",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "db0e30a4-43ab-4845-abd2-1644b0170b43",
          "values": [],
          "width": 153
        },
        "vendor": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_devices/vendor",
          "hide_notification": false,
          "id": 826,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "vendor",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Vendor",
          "tooltip": "",
          "type_id": 1038,
          "uuid": "bb6fa4e4-6ea3-45b9-9a07-cd7096c78051",
          "values": [],
          "width": 54
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_devices",
      "uuid": "611de6ae-8b44-4bba-a2d9-9169ab0da2ec"
    },
    {
      "actions": [],
      "display_name": "Extrahop Tags",
      "export_key": "extrahop_tags",
      "fields": {
        "mod_time": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/mod_time",
          "hide_notification": false,
          "id": 1237,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "mod_time",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Mod time",
          "tooltip": "Tag modification time",
          "type_id": 1061,
          "uuid": "6c839252-80ed-4451-84a1-2a008a539f66",
          "values": [],
          "width": 145
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/query_execution_date",
          "hide_notification": false,
          "id": 1233,
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
          "type_id": 1061,
          "uuid": "ec8fcd62-3285-411d-abc2-6e0a92ec9a14",
          "values": [],
          "width": 167
        },
        "tag": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/tag",
          "hide_notification": false,
          "id": 1234,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "tag",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tag",
          "tooltip": "Tag name",
          "type_id": 1061,
          "uuid": "842086e3-6e1a-4d5c-bed6-5bd33f313c08",
          "values": [],
          "width": 137
        },
        "tag_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_tags/tag_id",
          "hide_notification": false,
          "id": 1235,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "tag_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ID",
          "tooltip": "Tag ID",
          "type_id": 1061,
          "uuid": "10a76105-22ed-4191-9154-30f37908f537",
          "values": [],
          "width": 98
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_tags",
      "uuid": "1bbbcc65-f200-4041-8445-da134d8eb6cb"
    },
    {
      "actions": [],
      "display_name": "ExtraHop Watchlist",
      "export_key": "extrahop_watchlist",
      "fields": {
        "display_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/display_name",
          "hide_notification": false,
          "id": 700,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "display_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Display name",
          "tooltip": "",
          "type_id": 1037,
          "uuid": "0da314e0-a21b-4022-be04-5f25dd66baad",
          "values": [],
          "width": 140
        },
        "extrahop_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/extrahop_id",
          "hide_notification": false,
          "id": 701,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "extrahop_id",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "ExtraHop ID",
          "tooltip": "",
          "type_id": 1037,
          "uuid": "ef6bdb00-9852-4c35-b06e-7b73233d5e61",
          "values": [],
          "width": 156
        },
        "ipaddr4": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/ipaddr4",
          "hide_notification": false,
          "id": 702,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr4",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr4",
          "tooltip": "",
          "type_id": 1037,
          "uuid": "db777ffc-8430-4b3c-a411-385320425bf7",
          "values": [],
          "width": 84
        },
        "ipaddr6": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/ipaddr6",
          "hide_notification": false,
          "id": 703,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ipaddr6",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "IPaddr6",
          "tooltip": "",
          "type_id": 1037,
          "uuid": "fcb8e407-4077-46d7-ba71-5ec6ec800d6e",
          "values": [],
          "width": 83
        },
        "macaddr": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/macaddr",
          "hide_notification": false,
          "id": 704,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "macaddr",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "MACaddr",
          "tooltip": "",
          "type_id": 1037,
          "uuid": "67a77a85-93b4-4fc5-a27c-0749d959ab15",
          "values": [],
          "width": 128
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "extrahop_watchlist/query_execution_date",
          "hide_notification": false,
          "id": 705,
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
          "type_id": 1037,
          "uuid": "a95bfd25-6f88-4193-8781-f3797e20c0e7",
          "values": [],
          "width": 147
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
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "extrahop_watchlist",
      "uuid": "224bf5b6-346d-455a-a949-b62be7e74b90"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 37,
        "workflow_id": "wf_extrahop_rx_update_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_incident\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) update incident\"\u003e\u003cdocumentation\u003eUpdate SOAR incident with detection information from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dag81c\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xe2t7x\" name=\"Extrahop Reveal(x) get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_incident post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detections\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update incident\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n# Read CATEGORY_MAP and TYPE_MAP dicts from workflow property.\\nCATEGORY_MAP = workflow.properties.category_map\\nTYPE_MAP = workflow.properties.type_map\\nLINKBACK_URL = \\\"/extrahop/#/detections/detail/{}\\\"\\n\\n# Processing\\ndef make_linkback_url(det_id):\\n    \\\"\\\"\\\"Create a url to link back to the detection.\\n\\n    Args:\\n        det_id (str/int): id representing the detection.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(det_id)\\n\\ndef addArtifact(artifact_type, artifact_value, description):\\n    \\\"\\\"\\\"Add new artifacts to the incident.\\n\\n    :param artifact_type: The type of the artifact.\\n    :param artifact_value: - The value of the artifact.\\n    :param description: - the description of the artifact.\\n    \\\"\\\"\\\"\\n    incident.addArtifact(artifact_type, artifact_value, description)\\n\\n# Processing\\ndef main():\\n    detection_id = INPUTS[\\\"extrahop_detection_id\\\"]\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        det = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A Detection was successfully returned for \\\" \\\\\\n                    u\\\"detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if det:\\n            detection_url = make_linkback_url(det[\\\"id\\\"])\\n            detection_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{0}\\\"\u0026gt;{1}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                         .format(detection_url, det[\\\"id\\\"])\\n            newrow = incident.addRow(DATA_TABLE)\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.detection_url = detection_url_html\\n            for f1 in DATA_TBL_FIELDS:\\n                f2 = f1\\n                if f1.startswith(\\\"det_\\\"):\\n                    f2 = f1.split(\u0027_\u0027, 1)[1]\\n                if det[f2] is None or isinstance(det[f2], long):\\n                    newrow[f1] = det[f2]\\n                elif isinstance(det[f1], list):\\n                    if f1 == \\\"categories\\\":\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(CATEGORY_MAP[c] if CATEGORY_MAP.get(c) else c for c in det[f2]))\\n                    elif f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                        if f1 == \\\"participants\\\":\\n                            for p in det[f2]:\\n                                if p[\\\"object_type\\\"] == \\\"ipaddr\\\":\\n                                    artifact_type = \\\"IP Address\\\"\\n                                    addArtifact(artifact_type, p[\\\"object_value\\\"],\\n                                                \\\"Participant IP address in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                                    if p[\\\"hostname\\\"]:\\n                                        artifact_type = \\\"DNS Name\\\"\\n                                        addArtifact(artifact_type, p[\\\"hostname\\\"],\\n                                                    \\\"Participant DNS name in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                    .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                        obj_cnt = 0\\n                        tbl = u\u0027\u0027\\n                        for i in det[f2]:\\n                            for k, v in i.items():\\n                                if k == \\\"legacy_ids\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, \u0027,\u0027.join(v))\\n                                elif k == \\\"url\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                                        .format(k, v, i[\\\"id\\\"])\\n                                else:\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, v)\\n                            tbl += u\\\"\u0026lt;br\u0026gt;\\\"\\n                            obj_cnt += 1\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                elif isinstance(det[f2], (bool, dict)):\\n                    if f1 in [\\\"properties\\\"]:\\n                        tbl = u\u0027\u0027\\n                        for i, j in det[f2].items():\\n                            if i == \\\"suspicious_ipaddr\\\":\\n                                artifact_type = \\\"IP Address\\\"\\n                                type = \\\"Suspicious IP Addresses\\\"\\n                                value = j[\\\"value\\\"]\\n                                for ip in value:\\n                                    addArtifact(artifact_type, ip, \\\"Suspicious IP address found by ExtraHop.\\\")\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0027.format(type)\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}\u0027.format(\\\", \\\".join(\\\"{}\\\".format(i) for i in value))\\n                            else:\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(i, j)\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = str(det[f2])\\n                else:\\n                    if f1 == \\\"type\\\":\\n                        newrow[f1] = TYPE_MAP[det[f2]] if TYPE_MAP.get(det[f2]) else det[f2]\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get detections for detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\" \\\\\\n                     u\\\" with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_detection_id = incident.properties.extrahop_detection_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_detections_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_199bvm4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tuc6op\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1y7yknm\"\u003e\u003cincoming\u003eSequenceFlow_1vgg24b\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1v7g0lj\" name=\"Extrahop Reveal(x) get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_devices\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update incident\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\", \\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\n                   \\\"last_seen_time\\\"]\\nLINKBACK_URL = \\\"/extrahop/#/metrics/devices/{}.{}\\\"\\n\\n\\ndef make_linkback_url(dev_id):\\n    \\\"\\\"\\\"Create a url to link back to the endpoint alert, case, etc.\\n\\n    Args:\\n        dev_id (str/int): id representing the device etc.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(incident.properties.extrahop_site_uuid, dev_id)\\n\\ndef process_devs(dev):\\n    # Process a device result.\\n    newrow = incident.addRow(DATA_TABLE)\\n    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n    for f1 in DATA_TBL_FIELDS:\\n        f2 = f1\\n        if f1.startswith(\\\"devs_\\\"):\\n            f2 = f1.split(\u0027_\u0027, 1)[1]\\n        if dev[f1] is None:\\n            newrow[f1] = dev[f2]\\n        elif isinstance(dev[f2], list):\\n            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n        elif isinstance(dev[f2], bool):\\n            newrow[f1] = str(dev[f2])\\n        elif f1 in [\\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\\"last_seen_time\\\"]:\\n            newrow[f1] = long(dev[f2])\\n        else:\\n            newrow[f1] = \\\"{}\\\".format(dev[f2])\\n    device_url = make_linkback_url(dev[\\\"extrahop_id\\\"])\\n    device_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n              .format(\\\"url\\\", device_url, dev[\\\"extrahop_id\\\"])\\n    newrow.device_url = device_url_html\\n\\ndef get_dev_ids():\\n    # Get participant dev ids    \\n    dev_ids = []\\n    get_devices_content = workflow.properties.get_detections_result.content\\n    devs = get_devices_content[\\\"result\\\"]\\n    participants = devs[\\\"participants\\\"]\\n    for p in participants:\\n        if p[\\\"object_type\\\"] == \\\"device\\\":\\n            dev_ids.append(p[\\\"object_id\\\"])\\n    return dev_ids\\n\\n\\n# Processing\\ndef main():\\n    participant_dev_ids = get_dev_ids()\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = [d for d in CONTENT.result if d[\\\"id\\\"] in participant_dev_ids]\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Devices returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME, \\\", \\\".join(\\n            \\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if devs:\\n            if isinstance(devs, list):\\n                for dev in devs:\\n                    process_devs(dev)\\n            else:\\n                process_devs(devs)\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get devices for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tuc6op\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vgg24b\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tuc6op\" sourceRef=\"ServiceTask_0xe2t7x\" targetRef=\"ServiceTask_1v7g0lj\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1vgg24b\" sourceRef=\"ServiceTask_1v7g0lj\" targetRef=\"EndEvent_1y7yknm\"/\u003e\u003cscriptTask id=\"ScriptTask_1pr9qu7\" name=\"scr_extrahop_detection_property_h...\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"scr_extrahop_set_properties\" uuid=\"e934b42f-f5c5-4117-97ba-e07cfbba59c5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dag81c\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_199bvm4\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dag81c\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_1pr9qu7\"/\u003e\u003csequenceFlow id=\"SequenceFlow_199bvm4\" sourceRef=\"ScriptTask_1pr9qu7\" targetRef=\"ServiceTask_0xe2t7x\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xe2t7x\" id=\"ServiceTask_0xe2t7x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"435\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1y7yknm\" id=\"EndEvent_1y7yknm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"834\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"807\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1v7g0lj\" id=\"ServiceTask_1v7g0lj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"635\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tuc6op\" id=\"SequenceFlow_1tuc6op_di\"\u003e\u003comgdi:waypoint x=\"535\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"635\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"540\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vgg24b\" id=\"SequenceFlow_1vgg24b_di\"\u003e\u003comgdi:waypoint x=\"735\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"834\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"739.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1pr9qu7\" id=\"ScriptTask_1pr9qu7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"248\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dag81c\" id=\"SequenceFlow_1dag81c_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"248\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"223\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_199bvm4\" id=\"SequenceFlow_199bvm4_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 37,
      "creator_id": "a@a.com",
      "description": "Update SOAR incident with detection information from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_update_incident",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653921189471,
      "name": "Example: Extrahop Reveal(x) update incident",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_update_incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "b0a2acd5-a6ac-431f-b4c4-e467ff4b3f85",
      "workflow_id": 79
    },
    {
      "actions": [],
      "content": {
        "version": 21,
        "workflow_id": "wf_extrahop_rx_refresh_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_refresh_incident\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) refresh incident\"\u003e\u003cdocumentation\u003eRefresh SOAR incident with detection information from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1rp32u8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0zhtitt\" name=\"Extrahop Reveal(x) get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_incident post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detections\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) refresh incident\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n# Read CATEGORY_MAP and TYPE_MAP from workflow property.\\nCATEGORY_MAP = workflow.properties.category_map\\nTYPE_MAP = workflow.properties.type_map\\nLINKBACK_URL = \\\"/extrahop/#/detections/detail/{}\\\"\\n\\n# Processing\\ndef make_linkback_url(det_id):\\n    \\\"\\\"\\\"Create a url to link back to the detection.\\n\\n    Args:\\n        det_id (str/int): id representing the detection.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(det_id)\\n\\ndef addArtifact(artifact_type, artifact_value, description):\\n    \\\"\\\"\\\"Add new artifacts to the incident.\\n\\n    :param artifact_type: The type of the artifact.\\n    :param artifact_value: - The value of the artifact.\\n    :param description: - the description of the artifact.\\n    \\\"\\\"\\\"\\n    incident.addArtifact(artifact_type, artifact_value, description)\\n\\n# Processing\\ndef main():\\n    detection_id = INPUTS[\\\"extrahop_detection_id\\\"]\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        det = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A Detection was successfully returned for \\\" \\\\\\n                    u\\\"detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if det:\\n            detection_url = make_linkback_url(det[\\\"id\\\"])\\n            detection_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{0}\\\"\u0026gt;{1}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                         .format(detection_url, det[\\\"id\\\"])\\n            newrow = incident.addRow(DATA_TABLE)\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.detection_url = detection_url_html\\n            for f1 in DATA_TBL_FIELDS:\\n                f2 = f1\\n                if f1.startswith(\\\"det_\\\"):\\n                    f2 = f1.split(\u0027_\u0027, 1)[1]\\n                if det[f2] is None or isinstance(det[f2], long):\\n                    newrow[f1] = det[f2]\\n                elif isinstance(det[f1], list):\\n                    if f1 == \\\"categories\\\":\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(CATEGORY_MAP[c] if CATEGORY_MAP.get(c) else c for c in det[f2]))\\n                    elif f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                        if f1 == \\\"participants\\\":\\n                            for p in det[f2]:\\n                                if p[\\\"object_type\\\"] == \\\"ipaddr\\\":\\n                                    artifact_type = \\\"IP Address\\\"\\n                                    addArtifact(artifact_type, p[\\\"object_value\\\"],\\n                                                \\\"Participant IP address in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                                    if p[\\\"hostname\\\"]:\\n                                        artifact_type = \\\"DNS Name\\\"\\n                                        addArtifact(artifact_type, p[\\\"hostname\\\"],\\n                                                    \\\"Participant DNS name in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                    .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                        obj_cnt = 0\\n                        tbl = u\u0027\u0027\\n                        for i in det[f2]:\\n                            for k, v in i.items():\\n                                if k == \\\"legacy_ids\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, \u0027,\u0027.join(v))\\n                                elif k == \\\"url\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                                        .format(k, v, i[\\\"id\\\"])\\n                                else:\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, v)\\n                            tbl += u\\\"\u0026lt;br\u0026gt;\\\"\\n                            obj_cnt += 1\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                elif isinstance(det[f2], (bool, dict)):\\n                    if f1 in [\\\"properties\\\"]:\\n                        tbl = u\u0027\u0027\\n                        for i, j in det[f2].items():\\n                            if i == \\\"suspicious_ipaddr\\\":\\n                                artifact_type = \\\"IP Address\\\"\\n                                type = \\\"Suspicious IP Addresses\\\"\\n                                value = j[\\\"value\\\"]\\n                                for ip in value:\\n                                    addArtifact(artifact_type, ip, \\\"Suspicious IP address found by ExtraHop.\\\")\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0027.format(type)\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}\u0027.format(\\\", \\\".join(\\\"{}\\\".format(i) for i in value))\\n                            else:\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(i, j)\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = str(det[f2])\\n                else:\\n                    if f1 == \\\"type\\\":\\n                        newrow[f1] = TYPE_MAP[det[f2]] if TYPE_MAP.get(det[f2]) else det[f2]\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get detections for detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\" \\\\\\n                     u\\\" with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_detection_id = incident.properties.extrahop_detection_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_detections_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1lm3sdb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10xajts\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_0gq0yy0\" name=\"Extrahop Reveal(x) get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_devices\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) refresh incident\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\", \\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\n                   \\\"last_seen_time\\\"]\\nLINKBACK_URL = \\\"/extrahop/#/metrics/devices/{}.{}\\\"\\n\\n\\ndef make_linkback_url(dev_id):\\n    \\\"\\\"\\\"Create a url to link back to the endpoint alert, case, etc.\\n\\n    Args:\\n        dev_id (str/int): id representing the device etc.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(incident.properties.extrahop_site_uuid, dev_id)\\n\\ndef process_devs(dev):\\n    # Process a device result.\\n    newrow = incident.addRow(DATA_TABLE)\\n    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n    for f1 in DATA_TBL_FIELDS:\\n        f2 = f1\\n        if f1.startswith(\\\"devs_\\\"):\\n            f2 = f1.split(\u0027_\u0027, 1)[1]\\n        if dev[f1] is None:\\n            newrow[f1] = dev[f2]\\n        elif isinstance(dev[f2], list):\\n            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n        elif isinstance(dev[f2], bool):\\n            newrow[f1] = str(dev[f2])\\n        elif f1 in [\\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\\"last_seen_time\\\"]:\\n            newrow[f1] = long(dev[f2])\\n        else:\\n            newrow[f1] = \\\"{}\\\".format(dev[f2])\\n    device_url = make_linkback_url(dev[\\\"extrahop_id\\\"])\\n    device_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n              .format(\\\"url\\\", device_url, dev[\\\"extrahop_id\\\"])\\n    newrow.device_url = device_url_html\\n\\ndef get_dev_ids():\\n    # Get participant dev ids    \\n    dev_ids = []\\n    get_devices_content = workflow.properties.get_detections_result.content\\n    devs = get_devices_content[\\\"result\\\"]\\n    participants = devs[\\\"participants\\\"]\\n    for p in participants:\\n        if p[\\\"object_type\\\"] == \\\"device\\\":\\n            dev_ids.append(p[\\\"object_id\\\"])\\n    return dev_ids\\n\\n\\n# Processing\\ndef main():\\n    participant_dev_ids = get_dev_ids()\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = [d for d in CONTENT.result if d[\\\"id\\\"] in participant_dev_ids]\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Devices returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME, \\\", \\\".join(\\n            \\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if devs:\\n            if isinstance(devs, list):\\n                for dev in devs:\\n                    process_devs(dev)\\n            else:\\n                process_devs(devs)\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get devices for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n    #Unset the Detection update notification. \\n    incident.properties.extrahop_update_notification = None\\n    \\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10xajts\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jzx3p1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10xajts\" sourceRef=\"ServiceTask_0zhtitt\" targetRef=\"ServiceTask_0gq0yy0\"/\u003e\u003cendEvent id=\"EndEvent_0vdxbjz\"\u003e\u003cincoming\u003eSequenceFlow_0jzx3p1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jzx3p1\" sourceRef=\"ServiceTask_0gq0yy0\" targetRef=\"EndEvent_0vdxbjz\"/\u003e\u003cscriptTask id=\"ScriptTask_1wk6h0x\" name=\"scr_extrahop_detection_property_h...\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"scr_extrahop_set_properties\" uuid=\"e934b42f-f5c5-4117-97ba-e07cfbba59c5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1rp32u8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1lm3sdb\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1rp32u8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_1wk6h0x\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1lm3sdb\" sourceRef=\"ScriptTask_1wk6h0x\" targetRef=\"ServiceTask_0zhtitt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0zhtitt\" id=\"ServiceTask_0zhtitt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"400\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gq0yy0\" id=\"ServiceTask_0gq0yy0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"559\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10xajts\" id=\"SequenceFlow_10xajts_di\"\u003e\u003comgdi:waypoint x=\"500\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"559\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"484.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0vdxbjz\" id=\"EndEvent_0vdxbjz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"704\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"677\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jzx3p1\" id=\"SequenceFlow_0jzx3p1_di\"\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"704\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"636.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1wk6h0x\" id=\"ScriptTask_1wk6h0x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"233\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rp32u8\" id=\"SequenceFlow_1rp32u8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"233\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"215.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1lm3sdb\" id=\"SequenceFlow_1lm3sdb_di\"\u003e\u003comgdi:waypoint x=\"333\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"366.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 21,
      "creator_id": "a@a.com",
      "description": "Refresh SOAR incident with detection information from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_refresh_incident",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654100739014,
      "name": "Example: Extrahop Reveal(x) refresh incident",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_refresh_incident",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "6b1c7212-5707-4aff-b579-d031e7c127d2",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 35,
        "workflow_id": "wf_extrahop_rx_search_devices",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_devices\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) search devices\"\u003e\u003cdocumentation\u003eSearch for devices information from Extrahop Reveal(x) using a filter.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ao1ref\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10yatj6\" name=\"Extrahop Reveal(x) search devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e7384abd-0046-4b46-97af-d34d8cc9c711\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_devices\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) search devices\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\", \\\"on_watchlist\\\", \\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\n                   \\\"last_seen_time\\\"]\\n\\nLINKBACK_URL = \\\"/extrahop/#/metrics/devices/{}.{}\\\"\\n\\n\\n# Processing\\ndef make_linkback_url(dev_id):\\n    \\\"\\\"\\\"Create a url to link back to the endpoint alert, case, etc.\\n\\n    Args:\\n        dev_id (str/int): id representing the device etc.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(incident.properties.extrahop_site_uuid, dev_id)\\n\\ndef process_devs(dev):\\n    # Process a device result.\\n    newrow = incident.addRow(DATA_TABLE)\\n    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n    for f1 in DATA_TBL_FIELDS:\\n        f2 = f1\\n        if f1.startswith(\\\"devs_\\\"):\\n            f2 = f1.split(\u0027_\u0027, 1)[1]\\n        if dev[f1] is None:\\n            newrow[f1] = dev[f2]\\n        elif isinstance(dev[f2], list):\\n            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n        elif isinstance(dev[f2], bool):\\n            newrow[f1] = str(dev[f2])\\n        elif f1 in [\\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\\"last_seen_time\\\"]:\\n            newrow[f1] = long(dev[f2])\\n        else:\\n            newrow[f1] = \\\"{}\\\".format(dev[f2])\\n    device_url = make_linkback_url(dev[\\\"extrahop_id\\\"])\\n    device_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n              .format(\\\"url\\\", device_url, dev[\\\"extrahop_id\\\"])\\n    newrow.device_url = device_url_html\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if CONTENT.get(\\\"error\\\", None):\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Search devices failed with error \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, CONTENT[\\\"error\\\"], FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n        else:\\n            devs = CONTENT.result\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Devices returned for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n            if devs:\\n                for dev in devs:\\n                    process_devs(dev)\\n                note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search devices for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_detections pre processing script ##\\n\\ndef get_prop(prop, type=None):\\n    if prop:\\n        return \u0027{}\u0027.format(prop)\\n    else:\\n        return None\\n\\n\\ndef main():\\n    filter = {}\\n    filter_props = {\\n        \\\"field\\\": get_prop(rule.properties.extrahop_device_field),\\n        \\\"operand\\\": get_prop(rule.properties.extrahop_device_operand),\\n        \\\"operator\\\": get_prop(rule.properties.extrahop_device_operator)\\n    }\\n    filter = {k: v for k, v in filter_props.items() if v}\\n    \\n    if filter and rule.properties.extrahop_device_id:\\n        raise ValueError(\\\"The device ID and search filter shouldn\u0027t be set at the same time.\\\")\\n\\n\\n\\n    if filter:\\n        missing_props = []\\n        for f in [\\\"field\\\", \\\"operand\\\", \\\"operator\\\"]:\\n            if not filter.get(f, None):\\n                missing_props.append(f)\\n        if missing_props:\\n            raise ValueError(\\\"The filter is missing properties: \u0027{}\u0027.\\\".format(\\\", \\\".join(missing_props)))\\n            \\n        search_filter = {\\n            \\\"filter\\\": filter\\n        }\\n\\n    if rule.properties.extrahop_device_id:\\n        search_filter = {\\n            \\\"filter\\\": {\\n                \\\"field\\\": \\\"discovery_id\\\",\\n                \\\"operator\\\": \\\"=\\\",\\n                \\\"operand\\\": str(rule.properties.extrahop_device_id)\\n            }\\n        }\\n\\n    inputs.extrahop_search_filter = str(search_filter).replace(\\\"\u0027\\\", \u0027\\\"\u0027)\\n    if rule.properties.extrahop_active_from:\\n        inputs.extrahop_active_from = rule.properties.extrahop_active_from\\n    if rule.properties.extrahop_active_until:\\n        inputs.extrahop_active_until = rule.properties.extrahop_active_until\\n    if rule.properties.extrahop_limit:\\n        inputs.extrahop_limit = rule.properties.extrahop_limit\\n    if rule.properties.extrahop_offset:\\n        inputs.extrahop_offset = rule.properties.extrahop_offset\\n\\n\\nmain()\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"search_devices_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1l1ytsi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081bn3v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0t2xr17\"\u003e\u003cincoming\u003eSequenceFlow_081bn3v\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_18nwf3h\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081bn3v\" sourceRef=\"ServiceTask_10yatj6\" targetRef=\"EndEvent_0t2xr17\"/\u003e\u003cscriptTask id=\"ScriptTask_0j8efc5\" name=\"scr_extrahop_device_property_help...\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"dd\" uuid=\"49851abe-51dd-46da-9822-1cba3ee7d172\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ao1ref\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ehho9d\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ao1ref\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_0j8efc5\"/\u003e\u003cserviceTask id=\"ServiceTask_1dpvtto\" name=\"Extrahop Reveal(x) get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_devices\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) search devices\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\", \\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\",\\n                   \\\"last_seen_time\\\"]\\nLINKBACK_URL = \\\"/extrahop/#/metrics/devices/{}.{}\\\"\\n\\n\\ndef make_linkback_url(dev_id):\\n    \\\"\\\"\\\"Create a url to link back to the endpoint alert, case, etc.\\n\\n    Args:\\n        dev_id (str/int): id representing the device etc.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(incident.properties.extrahop_site_uuid,\\n                                                                          dev_id)\\n\\n\\ndef process_devs(dev):\\n    # Process a device result.\\n    newrow = incident.addRow(DATA_TABLE)\\n    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n    for f1 in DATA_TBL_FIELDS:\\n        f2 = f1\\n        if f1.startswith(\\\"devs_\\\"):\\n            f2 = f1.split(\u0027_\u0027, 1)[1]\\n        if dev[f1] is None:\\n            newrow[f1] = dev[f2]\\n        elif isinstance(dev[f2], list):\\n            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n        elif isinstance(dev[f2], bool):\\n            newrow[f1] = str(dev[f2])\\n        elif f1 in [\\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\\"last_seen_time\\\"]:\\n            newrow[f1] = long(dev[f2])\\n        else:\\n            newrow[f1] = \\\"{}\\\".format(dev[f2])\\n    device_url = make_linkback_url(dev[\\\"extrahop_id\\\"])\\n    device_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n        .format(\\\"url\\\", device_url, dev[\\\"extrahop_id\\\"])\\n    newrow.device_url = device_url_html\\n\\n# Processing\\ndef main():\\n    device_id = INPUTS[\\\"extrahop_device_id\\\"]\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        dev = CONTENT.result\\n        if dev:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A Device was successfully returned for \\\" \\\\\\n                        u\\\"device ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n                .format(WF_NAME, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n            process_devs(dev)\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get device for device ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\" \\\\\\n                     u\\\" with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"search_filters =  [ \\n    rule.properties.extrahop_device_field,\\n    rule.properties.extrahop_device_operand,\\n    rule.properties.extrahop_device_operator\\n]\\nfor p in search_filters:\\n    if p:\\n        raise ValueError(\\\"A search filter and Device ID are not allowed at the same time.\\\")\\n\\ninputs.extrahop_device_id = rule.properties.extrahop_device_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0tj1tm9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_18nwf3h\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_08g3jxf\"\u003e\u003cincoming\u003eSequenceFlow_1ehho9d\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1l1ytsi\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0tj1tm9\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1ehho9d\" sourceRef=\"ScriptTask_0j8efc5\" targetRef=\"ExclusiveGateway_08g3jxf\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1l1ytsi\" name=\"Device ID not set\" sourceRef=\"ExclusiveGateway_08g3jxf\" targetRef=\"ServiceTask_10yatj6\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"dev_id_set\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0tj1tm9\" name=\"Device ID set\" sourceRef=\"ExclusiveGateway_08g3jxf\" targetRef=\"ServiceTask_1dpvtto\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"dev_id_set\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_18nwf3h\" sourceRef=\"ServiceTask_1dpvtto\" targetRef=\"EndEvent_0t2xr17\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10yatj6\" id=\"ServiceTask_10yatj6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"484\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0t2xr17\" id=\"EndEvent_0t2xr17_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"673\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"646\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081bn3v\" id=\"SequenceFlow_081bn3v_di\"\u003e\u003comgdi:waypoint x=\"584\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"673\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"599\" y=\"157.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0j8efc5\" id=\"ScriptTask_0j8efc5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ao1ref\" id=\"SequenceFlow_0ao1ref_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"224\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"224\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"239\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1dpvtto\" id=\"ServiceTask_1dpvtto_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"484\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_08g3jxf\" id=\"ExclusiveGateway_08g3jxf_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"379\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"404\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ehho9d\" id=\"SequenceFlow_1ehho9d_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"379\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1l1ytsi\" id=\"SequenceFlow_1l1ytsi_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"122\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"89\" x=\"375\" y=\"145\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tj1tm9\" id=\"SequenceFlow_0tj1tm9_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"294\"/\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"294\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"70\" x=\"384\" y=\"256\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_18nwf3h\" id=\"SequenceFlow_18nwf3h_di\"\u003e\u003comgdi:waypoint x=\"584\" xsi:type=\"omgdc:Point\" y=\"294\"/\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"294\"/\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"673\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"644\" y=\"243.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 35,
      "creator_id": "a@a.com",
      "description": "Search for devices information from Extrahop Reveal(x) using a filter.",
      "export_key": "wf_extrahop_rx_search_devices",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654101894405,
      "name": "Example: Extrahop Reveal(x) search devices",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_devices",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "7d82fa2a-339c-4306-9a2c-ab4886101e2e",
      "workflow_id": 76
    },
    {
      "actions": [],
      "content": {
        "version": 36,
        "workflow_id": "wf_extrahop_rx_create_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_create_tag\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) create tag\"\u003e\u003cdocumentation\u003eCreate a new tag for  Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dto6o1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1km27wt\" name=\"Extrahop Reveal(x) create tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d566e4b3-6692-4599-a351-7530cdb4874e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_create_tag post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_create_tag\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) create tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            workflow.addProperty(\\\"tag_exists\\\", {})\\n            tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully created tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, unicode(tag), FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to create tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, unicode(tag), FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n        elif result == \\\"exists\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A 422 (tag name exists) error was thrown while to create tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, unicode(tag), FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Create tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, unicode(tag), FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to create a tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt;for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; .\\\"\\\\\\n            .format(WF_NAME, unicode(tag), FN_NAME, \\\", \\\".join(unicode(\\\"{}:{}\\\").format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_tag_name = rule.properties.extrahop_tag_name\\nif inputs.extrahop_tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"create_tag_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dto6o1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t46923\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dto6o1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1km27wt\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_018en0v\"\u003e\u003cincoming\u003eSequenceFlow_0t46923\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kwg8z2\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1q240w3\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0t46923\" sourceRef=\"ServiceTask_1km27wt\" targetRef=\"ExclusiveGateway_018en0v\"/\u003e\u003cserviceTask id=\"ServiceTask_0vsh07p\" name=\"Extrahop Reveal(x) get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_tags post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_tags\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) create tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TBL_FIELDS = [\\\"am_description\\\", \\\"am_id\\\", \\\"mod_time\\\", \\\"mode\\\", \\\"name\\\", \\\"owner\\\", \\\"rights\\\", \\\"short_code\\\", \\\"show_alert_status\\\", \\\"walks\\\", \\\"weighting\\\"]\\n\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag_exists = False\\n    tag_name = rule.properties.extrahop_tag_name\\n    if CONTENT:\\n        tags = CONTENT.result\\n        if tags:\\n            for tag in tags:\\n                if tag_name == tag[\\\"name\\\"]:\\n                    note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;:  Tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; returned for returned \\\" \\\\\\n                                u\\\"for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                        .format(WF_NAME, tag_name, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n                    tag_exists = True\\n                    newrow = incident.addRow(\\\"extrahop_tags\\\")\\n                    newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                    newrow.tag = tag.name\\n                    newrow.mod_time = tag.mod_time\\n                    newrow.tag_id = tag.id\\n                    note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Tags\\\")\\n                    break\\n            if not tag_exists:\\n                note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt;not returned for SOAR function \\\" \\\\\\n                            u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                    .format(WF_NAME, tag_name, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get  Tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, tag_name, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0kwg8z2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qub2do\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0kwg8z2\" name=\"Tag exists\" sourceRef=\"ExclusiveGateway_018en0v\" targetRef=\"ServiceTask_0vsh07p\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"tag_exists\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cendEvent id=\"EndEvent_1xse1dz\"\u003e\u003cincoming\u003eSequenceFlow_0qub2do\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1q240w3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0qub2do\" sourceRef=\"ServiceTask_0vsh07p\" targetRef=\"EndEvent_1xse1dz\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1q240w3\" name=\"Tag doesn\u0027t exist\" sourceRef=\"ExclusiveGateway_018en0v\" targetRef=\"EndEvent_1xse1dz\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"tag_exists\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"103\" y=\"258\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"170\" xsi:type=\"omgdc:Point\" y=\"221\"/\u003e\u003comgdi:waypoint x=\"156\" xsi:type=\"omgdc:Point\" y=\"258\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1km27wt\" id=\"ServiceTask_1km27wt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dto6o1\" id=\"SequenceFlow_0dto6o1_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"198.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_018en0v\" id=\"ExclusiveGateway_018en0v_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"436\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"461\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t46923\" id=\"SequenceFlow_0t46923_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"436\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"412.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0vsh07p\" id=\"ServiceTask_0vsh07p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"582\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kwg8z2\" id=\"SequenceFlow_0kwg8z2_di\"\u003e\u003comgdi:waypoint x=\"486\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"582\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"53\" x=\"508\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1xse1dz\" id=\"EndEvent_1xse1dz_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"754\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"772\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qub2do\" id=\"SequenceFlow_0qub2do_di\"\u003e\u003comgdi:waypoint x=\"682\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"718\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1q240w3\" id=\"SequenceFlow_1q240w3_di\"\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"386\"/\u003e\u003comgdi:waypoint x=\"772\" xsi:type=\"omgdc:Point\" y=\"386\"/\u003e\u003comgdi:waypoint x=\"772\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"87\" x=\"573\" y=\"365\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 36,
      "creator_id": "a@a.com",
      "description": "Create a new tag for  Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_create_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653997427906,
      "name": "Example: Extrahop Reveal(x) create tag",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_create_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "ceb2ade6-72f4-490d-bae2-7824953d3c91",
      "workflow_id": 77
    },
    {
      "actions": [],
      "content": {
        "version": 48,
        "workflow_id": "wf_extrahop_rx_update_detection",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_detection\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) update detection\"\u003e\u003cdocumentation\u003eUpdate ExtraHop detection if the status is changed on the associated  SOAR incident. Add a resolution note to the  detection.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1bom7fb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_089q2t9\" name=\"Extrahop Reveal(x) update detecti...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8ee5a0dc-d7d9-4d02-85a3-55d340a43aa0\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_setection post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_update_detection\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update detection\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        result = CONTENT[\\\"result\\\"]\\n        if result == \\\"success\\\":\\n            tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully updated the detection status for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to update the detection status for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Update detection status failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to update the detection status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.extrahop_detection_id = incident.properties.extrahop_detection_id\\ninputs.incident_id = incident.id\\ninputs.soar_inc_owner_id = incident.owner_id\\ninputs.soar_inc_plan_status = incident.plan_status\\ninputs.soar_inc_resolution_id = incident.resolution_id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"update_detection_note_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1bom7fb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0nsb0z2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1bom7fb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_089q2t9\"/\u003e\u003cserviceTask id=\"ServiceTask_046hx85\" name=\"Extrahop Reveal(x) get detection ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e5d62abb-bce4-46f6-a686-1b112a735219\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_detection post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detection_note\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update detection\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if not CONTENT:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get a detection note for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_detection_id = incident.properties.extrahop_detection_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_detection_note_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0nsb0z2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ou6tb8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0nsb0z2\" sourceRef=\"ServiceTask_089q2t9\" targetRef=\"ServiceTask_046hx85\"/\u003e\u003cserviceTask id=\"ServiceTask_1tfebsg\" name=\"Extrahop Reveal(x) add detection ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"58307d38-9975-4209-a8af-e68cb85f59f4\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_detection post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_add_detection_note\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update detection\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully added closure resolution note to \\\" \\\\\\n                        u\\\"ExtraHop detection for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, tag, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to add closure resolution note to ExtraHop \\\" \\\\\\n                        u\\\"detection for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, tag, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to add closure resolution note to ExtraHop \\\" \\\\\\n                        u\\\"detection  with unexpected response for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, tag, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to add closure resolution note to ExtraHop detection for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters\\\" \\\\\\n                     u\\\" \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\"\\\\\\n            .format(WF_NAME, tag, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_detection pre processing script ##\\nimport re\\ninputs.extrahop_detection_id = incident.properties.extrahop_detection_id\\n\\nUPD_DET_DATETIME = workflow.properties.update_detection_note_result.metrics[\\\"timestamp\\\"]\\nSUMMARY = re.sub(\u0027\u0026lt;[^\u0026lt;]+?\u0026gt;\u0027, \u0027\u0027, incident.resolution_summary.content)\\n\\n\\ndef get_current_note():\\n    # Get old note\\n    note = u\u0027\u0027\\n    get_detection_note_content = workflow.properties.get_detection_note_result.content\\n    note_obj = get_detection_note_content[\\\"result\\\"]\\n    if not note_obj:\\n        raise ValueError(\\\"Existing ExtraHop detection note not found.\\\")\\n    note = note_obj[\\\"note\\\"]\\n    return note\\n\\n\\ndef make_summary_note():\\n    # Make a  note.\\n    summary_note = \\\"IBM SOAR {}\\\\n\\\".format(UPD_DET_DATETIME)\\n    summary_note += \\\"[SOAR case - \u0027{}\u0027](Closed with resolution summary: \u0027{}\u0027)\\\" \\\\\\n    .format(incident.id, SUMMARY)\\n    return summary_note\\n\\n# Processing\\ndef main():\\n    detection_note = get_current_note()\\n\\n    inputs.extrahop_note = \u0027\\\\n\u0027.join([detection_note if detection_note else \\\"\\\", make_summary_note()])\\n    inputs.extrahop_update_time = 0\\nmain()\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ou6tb8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zpd6qz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ou6tb8\" sourceRef=\"ServiceTask_046hx85\" targetRef=\"ServiceTask_1tfebsg\"/\u003e\u003cserviceTask id=\"ServiceTask_1cel146\" name=\"Extrahop Reveal(x) get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_incident post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detections\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update detection\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"assignee\\\",  \\\"status\\\", \\\"ticket_id\\\"]\\n\\n\\n# Processing\\ndef main():\\n    detection_id = INPUTS[\\\"extrahop_detection_id\\\"]\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        det = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A Detection was successfully returned for \\\" \\\\\\n                    u\\\"detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        note_text += u\\\"\u0026lt;br\u0026gt;Updated ExtraHop properties for SOAR incident.\\\"\\n        incident.properties.extrahop_status = det[\\\"status\\\"]\\n        incident.properties.extrahop_ticket_id = det[\\\"ticket_id\\\"]\\n        incident.properties.extrahop_assignee = det[\\\"assignee\\\"]\\n        incident.properties.extrahop_update_notification = \\\"\u0026lt;span style=\u0027color:red;\u0027\u0026gt;The ExtraHop Detection has been closed.\u0026lt;/span\u0026gt;\u0026lt;br\u0026gt;\u0026lt;div\u0026gt;To refresh the incident run the action: Example: Extrahop Reveal(x) refresh incident.\u0026lt;div/\u0026gt;\\\"\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get detections for detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\" \\\\\\n                     u\\\" with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_detection_id = incident.properties.extrahop_detection_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zpd6qz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19s8zub\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zpd6qz\" sourceRef=\"ServiceTask_1tfebsg\" targetRef=\"ServiceTask_1cel146\"/\u003e\u003cendEvent id=\"EndEvent_0182k2c\"\u003e\u003cincoming\u003eSequenceFlow_19s8zub\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_19s8zub\" sourceRef=\"ServiceTask_1cel146\" targetRef=\"EndEvent_0182k2c\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_089q2t9\" id=\"ServiceTask_089q2t9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"223\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bom7fb\" id=\"SequenceFlow_1bom7fb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"223\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"210.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_046hx85\" id=\"ServiceTask_046hx85_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"368\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0nsb0z2\" id=\"SequenceFlow_0nsb0z2_di\"\u003e\u003comgdi:waypoint x=\"323\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"345.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tfebsg\" id=\"ServiceTask_1tfebsg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"526\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ou6tb8\" id=\"SequenceFlow_1ou6tb8_di\"\u003e\u003comgdi:waypoint x=\"468\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"526\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"497\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cel146\" id=\"ServiceTask_1cel146_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"686\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zpd6qz\" id=\"SequenceFlow_0zpd6qz_di\"\u003e\u003comgdi:waypoint x=\"626\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"686\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"656\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0182k2c\" id=\"EndEvent_0182k2c_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"830\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"848\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19s8zub\" id=\"SequenceFlow_19s8zub_di\"\u003e\u003comgdi:waypoint x=\"786\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"830\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"808\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 48,
      "creator_id": "a@a.com",
      "description": "Update ExtraHop detection if the status is changed on the associated  SOAR incident. Add a resolution note to the  detection.",
      "export_key": "wf_extrahop_rx_update_detection",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653472366137,
      "name": "Example: Extrahop Reveal(x) update detection",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_update_detection",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "a2732fde-597d-420c-8749-cf9c198c8fc5",
      "workflow_id": 82
    },
    {
      "actions": [],
      "content": {
        "version": 17,
        "workflow_id": "wf_extrahop_rx_update_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_update_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) update watchlist\"\u003e\u003cdocumentation\u003eAdd or remove an ExtraHop device to or from the watchlist.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1aj2xl3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1xzsmrv\" name=\"Extrahop Reveal(x) update watchli...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b8d33930-3417-436e-82a1-267a5dc9fa91\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_watchlist post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_update_watchlist\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        result = CONTENT[\\\"result\\\"]\\n        if result == \\\"success\\\":\\n            workflow.addProperty(\\\"watchlist_updated\\\", {})\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully updated the watchlist for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for device \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()), row.devs_id)\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to update the watchlist for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for device \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        elif result == \\\"conflict\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A 409 (conflict) error was thrown while attempting  \\\" \\\\\\n                        u\\\"to update the watchlist for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for device \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()), row.devs_id)\\n            note_text += u\\\"\u0026lt;br\u0026gt;Check if the sensor is being managed from the cloud-based service.\\\"\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Update watchlist failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for device \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()), row.devs_id)\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to update the watchlist \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for device \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()), row.devs_id)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"dev_id = row.devs_id\\naction = rule.properties.extrahop_watchlist_action\\nif action == \\\"add\\\":\\n    inputs.extrahop_assign = str(dev_id)\\nelif action == \\\"remove\\\":\\n    inputs.extrahop_unassign = str(dev_id)\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1aj2xl3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03c15k1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1aj2xl3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1xzsmrv\"/\u003e\u003cserviceTask id=\"ServiceTask_03ldzqe\" name=\"Extrahop Reveal(x) get devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"75447029-32ca-4363-b753-bc970cee66d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_devices\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) update watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_devices\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"devs_description\\\", \\\"default_name\\\", \\\"dns_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\",\\n                   \\\"role\\\", \\\"vendor\\\", \\\"devs_id\\\", \\\"extrahop_id\\\", \\\"activity\\\", \\\"on_watchlist\\\", \\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\n                   \\\"last_seen_time\\\"]\\n\\ndef process_devs(dev):\\n    # Process a device result.\\n    row.query_execution_date = QUERY_EXECUTION_DATE\\n    for f1 in DATA_TBL_FIELDS:\\n        f2 = f1\\n        if f1.startswith(\\\"devs_\\\"):\\n            f2 = f1.split(\u0027_\u0027, 1)[1]\\n        if dev[f1] is None:\\n            row[f1] = dev[f2]\\n        elif isinstance(dev[f2], list):\\n            row[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n        elif isinstance(dev[f2], bool):\\n            row[f1] = str(dev[f2])\\n        elif f1 in [\\\"mod_time\\\", \\\"user_mod_time\\\", \\\"discover_time\\\", \\\"last_seen_time\\\"]:\\n            row[f1] = long(dev[f2])\\n        else:\\n           row[f1] = \\\"{}\\\".format(dev[f2])\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        dev = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was a Device returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME, \\\", \\\".join(\\n            \\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if dev:\\n            process_devs(dev)\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(DATA_TABLE)\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get devices for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.extrahop_device_id = row.devs_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rzr9om\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1clpsis\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0hqfkxo\"\u003e\u003cincoming\u003eSequenceFlow_1clpsis\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_03h7cfd\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1clpsis\" sourceRef=\"ServiceTask_03ldzqe\" targetRef=\"EndEvent_0hqfkxo\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1j7sde2\"\u003e\u003cincoming\u003eSequenceFlow_03c15k1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0rzr9om\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_03h7cfd\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_03c15k1\" sourceRef=\"ServiceTask_1xzsmrv\" targetRef=\"ExclusiveGateway_1j7sde2\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0rzr9om\" name=\"Watchlist_updated\" sourceRef=\"ExclusiveGateway_1j7sde2\" targetRef=\"ServiceTask_03ldzqe\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"watchlist_updated\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_03h7cfd\" name=\"Watchlist not updated\" sourceRef=\"ExclusiveGateway_1j7sde2\" targetRef=\"EndEvent_0hqfkxo\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"watchlist_updated\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1xzsmrv\" id=\"ServiceTask_1xzsmrv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"287\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1aj2xl3\" id=\"SequenceFlow_1aj2xl3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"287\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"242.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03ldzqe\" id=\"ServiceTask_03ldzqe_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"635\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hqfkxo\" id=\"EndEvent_0hqfkxo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"823\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"796\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1clpsis\" id=\"SequenceFlow_1clpsis_di\"\u003e\u003comgdi:waypoint x=\"735\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"823\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"734\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1j7sde2\" id=\"ExclusiveGateway_1j7sde2_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"428\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03c15k1\" id=\"SequenceFlow_03c15k1_di\"\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"407.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rzr9om\" id=\"SequenceFlow_0rzr9om_di\"\u003e\u003comgdi:waypoint x=\"478\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"635\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"83\" x=\"515\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03h7cfd\" id=\"SequenceFlow_03h7cfd_di\"\u003e\u003comgdi:waypoint x=\"453\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"453\" xsi:type=\"omgdc:Point\" y=\"367\"/\u003e\u003comgdi:waypoint x=\"841\" xsi:type=\"omgdc:Point\" y=\"367\"/\u003e\u003comgdi:waypoint x=\"841\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"67\" x=\"614\" y=\"346\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 17,
      "creator_id": "a@a.com",
      "description": "Add or remove an ExtraHop device to or from the watchlist.",
      "export_key": "wf_extrahop_rx_update_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653393463622,
      "name": "Example: Extrahop Reveal(x) update watchlist",
      "object_type": "extrahop_devices",
      "programmatic_name": "wf_extrahop_rx_update_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "d1ac6f70-c4d9-4bee-adac-dcdea587c38c",
      "workflow_id": 74
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_extrahop_rx_get_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_tags\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) get tags\"\u003e\u003cdocumentation\u003eGet tags information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1dns9ig\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_189ulsl\" name=\"Extrahop Reveal(x) get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_tags post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_tags\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) get tags\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TBL_FIELDS = [\\\"am_description\\\", \\\"am_id\\\", \\\"mod_time\\\", \\\"mode\\\", \\\"name\\\", \\\"owner\\\", \\\"rights\\\", \\\"short_code\\\", \\\"show_alert_status\\\", \\\"walks\\\", \\\"weighting\\\"]\\n\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        tags = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Tags returned for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\"\\\\\\n                     u\\\"with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n        .format(WF_NAME, len(tags), FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if tags:\\n            for tag in tags:\\n                newrow = incident.addRow(\\\"extrahop_tags\\\")\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                newrow.tag = tag.name\\n                newrow.mod_time = tag.mod_time\\n                newrow.tag_id = tag.id\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Tags\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get tags for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dns9ig\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vd5haa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dns9ig\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_189ulsl\"/\u003e\u003cendEvent id=\"EndEvent_0y9myii\"\u003e\u003cincoming\u003eSequenceFlow_0vd5haa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vd5haa\" sourceRef=\"ServiceTask_189ulsl\" targetRef=\"EndEvent_0y9myii\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_189ulsl\" id=\"ServiceTask_189ulsl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"244\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dns9ig\" id=\"SequenceFlow_1dns9ig_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"244\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"221\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0y9myii\" id=\"EndEvent_0y9myii_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"388\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"406\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vd5haa\" id=\"SequenceFlow_0vd5haa_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"366\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "creator_id": "a@a.com",
      "description": "Get tags information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_tags",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653934681091,
      "name": "Example: Extrahop Reveal(x) get tags",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_tags",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "3385d752-805c-4275-9092-4af1c3e9abe4",
      "workflow_id": 84
    },
    {
      "actions": [],
      "content": {
        "version": 23,
        "workflow_id": "wf_extrahop_rx_assign_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_assign_tag\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) assign tag\"\u003e\u003cdocumentation\u003eAssign a tag to a list of devices ids for Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0l449vv\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_04jmpas\" name=\"Extrahop Reveal(x) get tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"55ced5bd-cd23-4212-b661-956fed40722b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_tags post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_tags\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) assign tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag_name = rule.properties.extrahop_tag_name\\n    tag_id = None\\n    \\n    if CONTENT:\\n        tags = CONTENT.result\\n        if tags:\\n            for tag in tags:\\n                if tag_name == tag[\\\"name\\\"]:\\n                    tag_id = tag[\\\"id\\\"]\\n                    workflow.addProperty(\\\"tag_exists\\\", {})\\n                    break\\n            if not tag_id:\\n                note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt;not returned for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\"\\\\\\n                            u\\\"with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                    .format(WF_NAME, tag_name, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get tags for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"if rule.properties.extrahop_tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"get_tags_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0l449vv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0revep1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0l449vv\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_04jmpas\"/\u003e\u003cserviceTask id=\"ServiceTask_1hdcy5r\" name=\"Extrahop Reveal(x) assign tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f0d2fc8c-20ab-440c-b4f5-46776a0b561e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_assign_tag post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_assign_tag\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) assign tag\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    tag_name = rule.properties.extrahop_tag_name\\n    tag = INPUTS.get(\\\"extrahop_tag_name\\\")\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result == \\\"success\\\":\\n            device_id = INPUTS.get(\\\"extrahop_device_ids\\\")\\n            tag_id = INPUTS.get(\\\"extrahop_tag_id\\\")\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully assigned tag \u0026lt;b\u0026gt;\u0027{1}\u0027\u0026lt;/b\u0026gt; with id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_name, tag_id, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n        elif result == \\\"failed\\\":\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Failed to assign tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_name, tag_id, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        else:\\n            note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Assign tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; failed with unexpected \\\" \\\\\\n                        u\\\"response for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, tag_name, tag_id, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to assign tag \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with id  \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; to device id \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{5}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, tag_name, tag_id, device_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"tag_name = rule.properties.extrahop_tag_name\\nget_tags_content = workflow.properties.get_tags_result.content\\ninputs.extrahop_device_ids = str(row.devs_id)\\nif tag_name is None:\\n    raise ValueError(\\\"The tag name is not set\\\")\\ninputs.extrahop_tag_id = None\\nfor tag in get_tags_content[\\\"result\\\"]:\\n    if tag_name == tag[\\\"name\\\"]:\\n        inputs.extrahop_tag_id = tag[\\\"id\\\"]\\n        break\\nif not inputs.extrahop_tag_id:\\n    raise ValueError(\\\"Tag {} not found.\\\".format(tag_name))\\n\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pz1idf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1db2q7n\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0bh06jd\"\u003e\u003cincoming\u003eSequenceFlow_1db2q7n\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_01xzkxm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1db2q7n\" sourceRef=\"ServiceTask_1hdcy5r\" targetRef=\"EndEvent_0bh06jd\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0runlvf\"\u003e\u003cincoming\u003eSequenceFlow_0revep1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1pz1idf\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_01xzkxm\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0revep1\" sourceRef=\"ServiceTask_04jmpas\" targetRef=\"ExclusiveGateway_0runlvf\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1pz1idf\" name=\"Tag  exists\" sourceRef=\"ExclusiveGateway_0runlvf\" targetRef=\"ServiceTask_1hdcy5r\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"tag_exists\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_01xzkxm\" name=\"Tag does not exist\" sourceRef=\"ExclusiveGateway_0runlvf\" targetRef=\"EndEvent_0bh06jd\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"tag_exists\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_04jmpas\" id=\"ServiceTask_04jmpas_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"239\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l449vv\" id=\"SequenceFlow_0l449vv_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"239\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1hdcy5r\" id=\"ServiceTask_1hdcy5r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"558\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0bh06jd\" id=\"EndEvent_0bh06jd_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"745\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"718\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1db2q7n\" id=\"SequenceFlow_1db2q7n_di\"\u003e\u003comgdi:waypoint x=\"658\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"745\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"656.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0runlvf\" id=\"ExclusiveGateway_0runlvf_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"410\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"435\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0revep1\" id=\"SequenceFlow_0revep1_di\"\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"374.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pz1idf\" id=\"SequenceFlow_1pz1idf_di\"\u003e\u003comgdi:waypoint x=\"460\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"558\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"53\" x=\"483\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01xzkxm\" id=\"SequenceFlow_01xzkxm_di\"\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"343\"/\u003e\u003comgdi:waypoint x=\"763\" xsi:type=\"omgdc:Point\" y=\"343\"/\u003e\u003comgdi:waypoint x=\"763\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"67\" x=\"566\" y=\"322\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 23,
      "creator_id": "a@a.com",
      "description": "Assign a tag to a list of devices ids for Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_assign_tag",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653990703482,
      "name": "Example: Extrahop Reveal(x) assign tag",
      "object_type": "extrahop_devices",
      "programmatic_name": "wf_extrahop_rx_assign_tag",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "6ab655c4-a62d-43bc-b896-a198871aef15",
      "workflow_id": 83
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "wf_extrahop_rx_get_watchlist",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_watchlist\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) get watchlist\"\u003e\u003cdocumentation\u003eRetrieve all devices that are in the watchlist from Extrahop Reveal(x) .\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0j0orct\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03t8ciq\" name=\"Extrahop Reveal(x) get watchlist\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4d5690ce-998c-4fbb-bf25-765800aaa246\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_watchlist post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_watchlist\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) get watchlist\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n# Display subset of fields\\nDATA_TABLE = \\\"extrahop_watchlist\\\"\\nDATA_TBL_FIELDS = [\\\"display_name\\\", \\\"ipaddr4\\\", \\\"ipaddr6\\\", \\\"macaddr\\\", \\\"extrahop_id\\\"]\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        devs = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; devices returned in the Watchlist\\\" \\\\\\n                    u\\\" for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(devs), FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if devs:\\n            for dev in devs:\\n                newrow = incident.addRow(\\\"extrahop_watchlist\\\")\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                  f2 = f1\\n                  if dev[f1] is None:\\n                      newrow[f1] = dev[f2]\\n                  if isinstance(dev[f1], list):\\n                      newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(dev[f2]))\\n                  elif isinstance(dev[f1], bool):\\n                      newrow[f1] = str(dev[f2])\\n                  else:\\n                      newrow[f1] = \\\"{}\\\".format(dev[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get the watchlist for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0j0orct\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0u8wmby\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0j0orct\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03t8ciq\"/\u003e\u003cendEvent id=\"EndEvent_1nup12z\"\u003e\u003cincoming\u003eSequenceFlow_0u8wmby\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0u8wmby\" sourceRef=\"ServiceTask_03t8ciq\" targetRef=\"EndEvent_1nup12z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03t8ciq\" id=\"ServiceTask_03t8ciq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j0orct\" id=\"SequenceFlow_0j0orct_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1nup12z\" id=\"EndEvent_1nup12z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"391\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u8wmby\" id=\"SequenceFlow_0u8wmby_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"391\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "creator_id": "a@a.com",
      "description": "Retrieve all devices that are in the watchlist from Extrahop Reveal(x) .",
      "export_key": "wf_extrahop_rx_get_watchlist",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1651163008221,
      "name": "Example: Extrahop Reveal(x) get watchlist",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_watchlist",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "1a397ec4-4b9c-41fc-a4c3-a302ac7de149",
      "workflow_id": 80
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "wf_extrahop_rx_search_packets",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_packets\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) search packets\"\u003e\u003cdocumentation\u003eSearch for and download packets stored on the ExtraHop Reveal(x) system and add as an attachment. Valid output types are: pcap, keylog_txt or zip.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_08zi9sc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bqqxcs\" name=\"Extrahop Reveal(x) search packets\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f551a853-62d0-468d-9e36-df5904c5bf96\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_packets post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_packets\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) search packets\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        result = CONTENT.result\\n        if result.get(\\\"attachment\\\"):\\n            note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Successfully searched for packets for SOAR \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n            note_text += u\\\"\u0026lt;br\u0026gt;Attachment \u0026lt;b\u0026gt;{}\u0026lt;b\u0026gt; added.\\\".format(result.get(\\\"attachment\\\"))\\n        elif result.get(\\\"status\\\"):\\n            note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Search for packets returned no results for SOAR \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n            note_text += u\\\"\u0026lt;br\u0026gt;Status \u0026lt;b\u0026gt;{}\u0026lt;b\u0026gt;.\\\".format(result.get(\\\"status\\\"))\\n        elif result.get(\\\"error\\\"):\\n            note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Search for packets failed for \\\" \\\\\\n                        u\\\"SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n            note_text += u\\\"\u0026lt;br\u0026gt;Error \u0026lt;b\u0026gt;{}\u0026lt;b\u0026gt;.\\\".format(result.get(\\\"error\\\"))\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search packets for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.incident_id = incident.id\\nif artifact.type == \\\"IP Address\\\" or artifact.type == \\\"DNS Name\\\":\\n    inputs.extrahop_bpf = \\\"host {}\\\".format(artifact.value)\\nelif artifact.type == \\\"MAC Address\\\":\\n    inputs.extrahop_bpf = \\\"ether host {}\\\".format(artifact.value)\\ninputs.extrahop_active_from = rule.properties.extrahop_active_from\\ninputs.extrahop_active_until = rule.properties.extrahop_active_until\\ninputs.extrahop_output = rule.properties.extrahop_output\\ninputs.extrahop_limit_search_duration = rule.properties.extrahop_limit_search_duration\\ninputs.extrahop_limit_bytes = rule.properties.extrahop_limit_bytes\\ninputs.extrahop_ip1 = rule.properties.extrahop_ip1\\ninputs.extrahop_port1 = rule.properties.extrahop_port1\\ninputs.extrahop_ip2 = rule.properties.extrahop_ip2\\ninputs.extrahop_port2 = rule.properties.extrahop_port2\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_08zi9sc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t8ri2v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_08zi9sc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1bqqxcs\"/\u003e\u003cendEvent id=\"EndEvent_1hexrht\"\u003e\u003cincoming\u003eSequenceFlow_0t8ri2v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0t8ri2v\" sourceRef=\"ServiceTask_1bqqxcs\" targetRef=\"EndEvent_1hexrht\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bqqxcs\" id=\"ServiceTask_1bqqxcs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"227\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08zi9sc\" id=\"SequenceFlow_08zi9sc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"227\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"212.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1hexrht\" id=\"EndEvent_1hexrht_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t8ri2v\" id=\"SequenceFlow_0t8ri2v_di\"\u003e\u003comgdi:waypoint x=\"327\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"350\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "creator_id": "a@a.com",
      "description": "Search for and download packets stored on the ExtraHop Reveal(x) system and add as an attachment. Valid output types are: pcap, keylog_txt or zip.",
      "export_key": "wf_extrahop_rx_search_packets",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654098337003,
      "name": "Example: Extrahop Reveal(x) search packets",
      "object_type": "artifact",
      "programmatic_name": "wf_extrahop_rx_search_packets",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "d81106fc-ce08-464f-b4f2-af78b94d6846",
      "workflow_id": 92
    },
    {
      "actions": [],
      "content": {
        "version": 74,
        "workflow_id": "wf_extrahop_rx_search_detections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_search_detections\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) search detections\"\u003e\u003cdocumentation\u003eSearch for detections information from Extrahop Reveal(x).\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15pjwy9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1bnujpl\" name=\"Extrahop Reveal(x) search detecti...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b70037a5-fcaf-4e78-a1e2-6acdc4dff239\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_detections post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_search_detections\\\"\\nWF_NAME = \\\"Example: Extrahop revealx search detections\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n\\n# Read CATEGORY_MAP and TYPE_MAP from workflow property.\\nCATEGORY_MAP = workflow.properties.category_map\\nTYPE_MAP = workflow.properties.type_map\\n\\nLINKBACK_URL = \\\"/extrahop/#/detections/detail/{}\\\"\\n\\n# Processing\\ndef make_linkback_url(det_id):\\n    \\\"\\\"\\\"Create a url to link back to the detection.\\n\\n    Args:\\n        det_id (str/int): id representing the detection.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(det_id)\\n\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n\\n    if CONTENT:\\n        dets = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Detections returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(dets), FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if dets:\\n            for det in dets:\\n                detection_url = make_linkback_url(det[\\\"id\\\"])\\n                detection_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{0}\\\"\u0026gt;{1}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                             .format(detection_url, det[\\\"id\\\"])\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                newrow.detection_url = detection_url_html\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"det_\\\"):\\n                      f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if det[f2] is None or isinstance(det[f2], long):\\n                        newrow[f1] = det[f2]\\n                    elif isinstance(det[f1], list):\\n                        if f1 == \\\"categories\\\":\\n                            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(CATEGORY_MAP[c] if CATEGORY_MAP.get(c) else c for c in det[f2]))\\n                        elif f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                            obj_cnt = 0\\n                            tbl = u\u0027\u0027\\n                            for i in det[f2]:\\n                                for k, v in i.items():\\n                                    if k == \\\"legacy_ids\\\":\\n                                        tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, \u0027,\u0027.join(v))\\n                                    elif k == \\\"url\\\":\\n                                        tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/div\u0026gt;\u0027\\\\\\n                                            .format(k, v, i[\\\"id\\\"])\\n                                    else:\\n                                        tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, v)\\n                                tbl += u\\\"\u0026lt;br\u0026gt;\\\"\\n                                obj_cnt += 1\\n                            newrow[f1] = tbl\\n                        else:\\n                            newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                    elif isinstance(det[f2], (bool, dict)):\\n                        if f1 in [\\\"properties\\\"]:\\n                            suspect_ip = False\\n                            tbl = u\u0027\u0027\\n                            for i, j in det[f2].items():\\n                                if i == \\\"suspicious_ipaddr\\\":\\n                                    artifact_type = \\\"IP Address\\\"\\n                                    type = \\\"Suspicious IP Addresses\\\"\\n                                    value = j[\\\"value\\\"]\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0027.format(type)\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}\u0027.format(\\\", \\\".join(\\\"{}\\\".format(i) for i in value))\\n                                else:\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(i, j)\\n                            newrow[f1] = tbl\\n                        else:\\n                            newrow[f1] = str(det[f2])\\n                    else:\\n                        if f1 == \\\"type\\\":\\n                            newrow[f1] = TYPE_MAP[det[f2]] if TYPE_MAP.get(det[f2]) else det[f2]\\n                        else:\\n                            newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to search detections for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n    \\n# Start execution\\nmain()\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"##  ExtraHop - wf_extrahop_rx_search_detections pre processing script ##\\n# Read CATEGORY_MAP and TYPE_MAP from workflow propertyself. \\n# Reverse the dict keys and values\\nCATEGORY_MAP = {v: k for k, v in workflow.properties.category_map.items()}\\nTYPE_MAP = {v: k for k, v in workflow.properties.type_map.items()}\\n\\ndef get_prop(prop, type=None):\\n    if prop:\\n        if isinstance(prop, int):\\n            return prop\\n        elif isinstance(prop, list):\\n            return [\u0027{}\u0027.format(i) for i in prop]\\n        return \u0027{}\u0027.format(prop)\\n    else:\\n        return None\\n\\nfilter = {}\\ncategory = None\\ndetection_types = None\\nif rule.properties.extrahop_detection_category:\\n    category = CATEGORY_MAP[rule.properties.extrahop_detection_category]\\nif rule.properties.extrahop_detection_types:\\n    detection_types = [TYPE_MAP[d] for d in rule.properties.extrahop_detection_types]\\n\\n    \\nfilter_props = {\\n    \\\"risk_score_min\\\": get_prop(rule.properties.extrahop_detection_risk_score_min),\\n    \\\"types\\\": get_prop(detection_types),\\n    \\\"category\\\": get_prop(category),\\n    \\\"assignee\\\": get_prop(rule.properties.extrahop_detection_assignee),\\n    \\\"ticket_id\\\": get_prop(rule.properties.extrahop_detection_ticket_id),\\n    \\\"status\\\": get_prop(rule.properties.extrahop_detection_status),\\n    \\\"resolution\\\": get_prop(rule.properties.extrahop_detection_resolution)\\n}\\n\\nfilter = {k: v for k, v in filter_props.items() if v}\\n\\nif filter and rule.properties.extrahop_detection_id:\\n    raise ValueError(\\\"The search filter and Detecion ID are not allowed at the same time.\\\")\\n    \\nif not filter:\\n    raise ValueError(\\\"The search filter is empty.\\\")\\nelse:\\n    search_filter = {\\n        \\\"filter\\\": filter\\n    }\\n\\ninputs.extrahop_search_filter = str(search_filter).replace(\\\"\u0027\\\", \u0027\\\"\u0027)\\nif rule.properties.extrahop_active_from:\\n    inputs.extrahop_active_from = rule.properties.extrahop_active_from\\nif rule.properties.extrahop_active_until:\\n    inputs.extrahop_active_until = rule.properties.extrahop_active_until\\nif rule.properties.extrahop_limit:\\n    inputs.extrahop_limit = rule.properties.extrahop_limit\\nif rule.properties.extrahop_offset:\\n    inputs.extrahop_offset = rule.properties.extrahop_offset\\nif rule.properties.extrahop_update_time:\\n    inputs.extrahop_update_time = rule.properties.extrahop_update_time\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11b80db\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17ve9fh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0jhirff\"\u003e\u003cincoming\u003eSequenceFlow_17ve9fh\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1ggqezr\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17ve9fh\" sourceRef=\"ServiceTask_1bnujpl\" targetRef=\"EndEvent_0jhirff\"/\u003e\u003cscriptTask id=\"ScriptTask_0b3qvu2\" name=\"scr_extrahop_detection_property_h...\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"scr_extrahop_set_properties\" uuid=\"e934b42f-f5c5-4117-97ba-e07cfbba59c5\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15pjwy9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_00biv05\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_15pjwy9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_0b3qvu2\"/\u003e\u003csequenceFlow id=\"SequenceFlow_00biv05\" sourceRef=\"ScriptTask_0b3qvu2\" targetRef=\"ExclusiveGateway_1w91mxx\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1w91mxx\"\u003e\u003cincoming\u003eSequenceFlow_00biv05\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11b80db\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0xmysoo\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_11b80db\" name=\"Detection ID not set\" sourceRef=\"ExclusiveGateway_1w91mxx\" targetRef=\"ServiceTask_1bnujpl\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"det_id_set\\\", None) == None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0xtcn38\" name=\"Extrahop Reveal(x) get detections\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fc71fc68-991e-4825-bc07-2191e58745f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_update_incident post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_detections\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) search detections\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_detections\\\"\\nDATA_TBL_FIELDS = [\\\"appliance_id\\\", \\\"assignee\\\", \\\"categories\\\", \\\"det_description\\\", \\\"end_time\\\", \\\"det_id\\\", \\\"is_user_created\\\",\\n                   \\\"mitre_tactics\\\", \\\"mitre_techniques\\\", \\\"participants\\\", \\\"properties\\\", \\\"resolution\\\", \\\"risk_score\\\",\\n                   \\\"start_time\\\", \\\"status\\\", \\\"ticket_id\\\", \\\"ticket_url\\\", \\\"title\\\", \\\"type\\\", \\\"update_time\\\"]\\n# Read CATEGORY_MAP and TYPE_MAP from workflow property.\\nCATEGORY_MAP = workflow.properties.category_map\\nTYPE_MAP = workflow.properties.type_map\\nLINKBACK_URL = \\\"/extrahop/#/detections/detail/{}\\\"\\n\\n# Processing\\ndef make_linkback_url(det_id):\\n    \\\"\\\"\\\"Create a url to link back to the detection.\\n\\n    Args:\\n        det_id (str/int): id representing the detection.\\n\\n    Returns:\\n        str: completed url for linkback\\n    \\\"\\\"\\\"\\n    return incident.properties.extrahop_console_url + LINKBACK_URL.format(det_id)\\n\\ndef addArtifact(artifact_type, artifact_value, description):\\n    \\\"\\\"\\\"Add new artifacts to the incident.\\n\\n    :param artifact_type: The type of the artifact.\\n    :param artifact_value: - The value of the artifact.\\n    :param description: - the description of the artifact.\\n    \\\"\\\"\\\"\\n    incident.addArtifact(artifact_type, artifact_value, description)\\n\\n# Processing\\ndef main():\\n    detection_id = INPUTS[\\\"extrahop_detection_id\\\"]\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        det = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: A Detection was successfully returned for \\\" \\\\\\n                    u\\\"detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if det:\\n            detection_url = make_linkback_url(det[\\\"id\\\"])\\n            detection_url_html = u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;\u0026lt;a target=\\\"blank\\\" href=\\\"{0}\\\"\u0026gt;{1}\u0026lt;/a\u0026gt;\u0026lt;/b\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                         .format(detection_url, det[\\\"id\\\"])\\n            newrow = incident.addRow(DATA_TABLE)\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            newrow.detection_url = detection_url_html\\n            for f1 in DATA_TBL_FIELDS:\\n                f2 = f1\\n                if f1.startswith(\\\"det_\\\"):\\n                    f2 = f1.split(\u0027_\u0027, 1)[1]\\n                if det[f2] is None or isinstance(det[f2], long):\\n                    newrow[f1] = det[f2]\\n                elif isinstance(det[f1], list):\\n                    if f1 == \\\"categories\\\":\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(CATEGORY_MAP[c] if CATEGORY_MAP.get(c) else c for c in det[f2]))\\n                    elif f1 in [\\\"participants\\\", \\\"mitre_tactics\\\", \\\"mitre_techniques\\\"]:\\n                        if f1 == \\\"participants\\\":\\n                            for p in det[f2]:\\n                                if p[\\\"object_type\\\"] == \\\"ipaddr\\\":\\n                                    artifact_type = \\\"IP Address\\\"\\n                                    addArtifact(artifact_type, p[\\\"object_value\\\"],\\n                                                \\\"Participant IP address in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                                    if p[\\\"hostname\\\"]:\\n                                        artifact_type = \\\"DNS Name\\\"\\n                                        addArtifact(artifact_type, p[\\\"hostname\\\"],\\n                                                    \\\"Participant DNS name in ExtraHop detection \u0027{0}\u0027, role: \u0027{1}\u0027.\\\"\\n                                                    .format(det[\\\"id\\\"], p[\\\"role\\\"]))\\n                        obj_cnt = 0\\n                        tbl = u\u0027\u0027\\n                        for i in det[f2]:\\n                            for k, v in i.items():\\n                                if k == \\\"legacy_ids\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, \u0027,\u0027.join(v))\\n                                elif k == \\\"url\\\":\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;a target=\\\"blank\\\" href=\\\"{1}\\\"\u0026gt;{2}\u0026lt;/a\u0026gt;\u0026lt;/div\u0026gt;\u0027 \\\\\\n                                        .format(k, v, i[\\\"id\\\"])\\n                                else:\\n                                    tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(k, v)\\n                            tbl += u\\\"\u0026lt;br\u0026gt;\\\"\\n                            obj_cnt += 1\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(det[f2]))\\n                elif isinstance(det[f2], (bool, dict)):\\n                    if f1 in [\\\"properties\\\"]:\\n                        tbl = u\u0027\u0027\\n                        for i, j in det[f2].items():\\n                            if i == \\\"suspicious_ipaddr\\\":\\n                                artifact_type = \\\"IP Address\\\"\\n                                type = \\\"Suspicious IP Addresses\\\"\\n                                value = j[\\\"value\\\"]\\n                                for ip in value:\\n                                    addArtifact(artifact_type, ip, \\\"Suspicious IP address found by ExtraHop.\\\")\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0027.format(type)\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}\u0027.format(\\\", \\\".join(\\\"{}\\\".format(i) for i in value))\\n                            else:\\n                                tbl += u\u0027\u0026lt;div\u0026gt;\u0026lt;b\u0026gt;{0}:\u0026lt;/b\u0026gt;{1}\u0026lt;/div\u0026gt;\u0027.format(i, j)\\n                        newrow[f1] = tbl\\n                    else:\\n                        newrow[f1] = str(det[f2])\\n                else:\\n                    if f1 == \\\"type\\\":\\n                        newrow[f1] = TYPE_MAP[det[f2]] if TYPE_MAP.get(det[f2]) else det[f2]\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(det[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Detections\\\")\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get detections for detection ID \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for SOAR function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; .\\\" \\\\\\n                     u\\\" with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, detection_id, FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"search_filters =  [ \\n    rule.properties.extrahop_detection_risk_score_min, rule.properties.extrahop_detection_category, \\n    rule.properties.extrahop_detection_types, rule.properties.extrahop_detection_assignee, \\n    rule.properties.extrahop_detection_ticket_id, rule.properties.extrahop_detection_status, \\n    rule.properties.extrahop_detection_resolution\\n]\\nfor p in search_filters:\\n    if p:\\n        raise ValueError(\\\"A search filter and Detection ID are not allowed at the same time.\\\")\\n\\ninputs.extrahop_detection_id = rule.properties.extrahop_detection_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xmysoo\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ggqezr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xmysoo\" name=\"Detection ID set\" sourceRef=\"ExclusiveGateway_1w91mxx\" targetRef=\"ServiceTask_0xtcn38\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e\u003c![CDATA[{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"det_id_set\\\", None) != None\",\"language\":\"python\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python\"}]]\u003e\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1ggqezr\" sourceRef=\"ServiceTask_0xtcn38\" targetRef=\"EndEvent_0jhirff\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1bnujpl\" id=\"ServiceTask_1bnujpl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"558\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0jhirff\" id=\"EndEvent_0jhirff_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"736\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"709\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17ve9fh\" id=\"SequenceFlow_17ve9fh_di\"\u003e\u003comgdi:waypoint x=\"658\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"661\" y=\"74.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0b3qvu2\" id=\"ScriptTask_0b3qvu2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"234\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15pjwy9\" id=\"SequenceFlow_15pjwy9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"234\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00biv05\" id=\"SequenceFlow_00biv05_di\"\u003e\u003comgdi:waypoint x=\"334\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"438\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"341\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1w91mxx\" id=\"ExclusiveGateway_1w91mxx_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"438\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"418\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11b80db\" id=\"SequenceFlow_11b80db_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"558\" xsi:type=\"omgdc:Point\" y=\"96\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"26\" width=\"84\" x=\"437\" y=\"131.57142857142858\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xtcn38\" id=\"ServiceTask_0xtcn38_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"558\" y=\"275\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xmysoo\" id=\"SequenceFlow_0xmysoo_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"315\"/\u003e\u003comgdi:waypoint x=\"558\" xsi:type=\"omgdc:Point\" y=\"315\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"83\" x=\"437\" y=\"266.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ggqezr\" id=\"SequenceFlow_1ggqezr_di\"\u003e\u003comgdi:waypoint x=\"658\" xsi:type=\"omgdc:Point\" y=\"315\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"315\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"661\" y=\"293.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 74,
      "creator_id": "a@a.com",
      "description": "Search for detections information from Extrahop Reveal(x).",
      "export_key": "wf_extrahop_rx_search_detections",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1654101702997,
      "name": "Example: Extrahop Reveal(x) search detections",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_search_detections",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "7e68a246-23c6-40bd-8f0a-77217f69a01c",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_extrahop_rx_get_activitymaps",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_get_activitymaps\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) get activitymaps\"\u003e\u003cdocumentation\u003eGet activitymaps information from Extrahop Reveal(x)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_104u30s\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03b8xn3\" name=\"Extrahop Reveal(x) get activityma...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"18aa0964-745b-4329-a04b-a92f5f3fab40\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  ExtraHop - wf_extrahop_rx_get_activitymaps post processing script ##\\n#  Globals\\nFN_NAME = \\\"funct_extrahop_rx_get_activitymaps\\\"\\nWF_NAME = \\\"Example: Extrahop Reveal(x) get activitymaps\\\"\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDATA_TABLE = \\\"extrahop_activitymaps\\\"\\nDATA_TBL_FIELDS = [\\\"ams_description\\\", \\\"ams_id\\\", \\\"mod_time\\\", \\\"mode\\\", \\\"ams_name\\\", \\\"owner\\\", \\\"rights\\\", \\\"short_code\\\",\\n                   \\\"show_alert_status\\\", \\\"walks\\\", \\\"weighting\\\"]\\n# Processing\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        ams = CONTENT.result\\n        note_text = u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Activitymaps returned for SOAR \\\" \\\\\\n                    u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(ams), FN_NAME, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n        if ams:\\n            for am in ams:\\n                newrow = incident.addRow(DATA_TABLE)\\n                newrow.query_execution_date = QUERY_EXECUTION_DATE\\n                for f1 in DATA_TBL_FIELDS:\\n                    f2 = f1\\n                    if f1.startswith(\\\"ams_\\\"):\\n                        f2 = f1.split(\u0027_\u0027, 1)[1]\\n                    if am[f2] is None:\\n                        newrow[f1] = am[f2]\\n                    if isinstance(am[f2], list):\\n                      if f1 in [\\\"walks\\\",\\\"steps\\\"]:\\n                          newrow[f1] = \\\"{}\\\".format(am[f2])\\n                      else:\\n                          newrow[f1] = \\\"{}\\\".format(\\\", \\\".join(am[f2]))\\n                    elif isinstance(am[f2], (bool, dict)):\\n                        newrow[f1] = str(am[f2])\\n                    else:\\n                        newrow[f1] = \\\"{}\\\".format(am[f2])\\n            note_text += u\\\"\u0026lt;br\u0026gt;The data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; has been updated\\\".format(\\\"Extrahop Activitymaps\\\")\\n    else:\\n        note_text += u\\\"ExtraHop Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; result returned while attempting \\\" \\\\\\n                     u\\\"to get activitymaps for SOAR function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with parameters \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAM, \\\", \\\".join(\\\"{}:{}\\\".format(k, v) for k, v in INPUTS.items()))\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\nmain()\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_104u30s\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17yb9c4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_104u30s\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03b8xn3\"/\u003e\u003cendEvent id=\"EndEvent_03rpj82\"\u003e\u003cincoming\u003eSequenceFlow_17yb9c4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_17yb9c4\" sourceRef=\"ServiceTask_03b8xn3\" targetRef=\"EndEvent_03rpj82\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03b8xn3\" id=\"ServiceTask_03b8xn3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"254\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_104u30s\" id=\"SequenceFlow_104u30s_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_03rpj82\" id=\"EndEvent_03rpj82_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"399\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17yb9c4\" id=\"SequenceFlow_17yb9c4_di\"\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"399\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"376.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "creator_id": "a@a.com",
      "description": "Get activitymaps information from Extrahop Reveal(x)",
      "export_key": "wf_extrahop_rx_get_activitymaps",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1651163010170,
      "name": "Example: Extrahop Reveal(x) get activitymaps",
      "object_type": "incident",
      "programmatic_name": "wf_extrahop_rx_get_activitymaps",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "37240452-0a4d-478b-83c4-2b8965d9fcb4",
      "workflow_id": 81
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_extrahop_rx_add_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_extrahop_rx_add_artifact\" isExecutable=\"true\" name=\"Example: Extrahop Reveal(x) add artifact\"\u003e\u003cdocumentation\u003eCreate a SOAR incident artifact from ExtraHop device property. Valid types are IP Address, DNS Name or MAC Address.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p2jx04\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cscriptTask id=\"ScriptTask_06obwkv\" name=\"scr_extrahop_rx_add_artifact_from...\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"scr_sep_add_artifact_from_scan_results\" uuid=\"b22a440f-5bd8-4d14-a34e-9fe51dad99fb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p2jx04\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0chyplu\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p2jx04\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ScriptTask_06obwkv\"/\u003e\u003cendEvent id=\"EndEvent_070d7ng\"\u003e\u003cincoming\u003eSequenceFlow_0chyplu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0chyplu\" sourceRef=\"ScriptTask_06obwkv\" targetRef=\"EndEvent_070d7ng\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_06obwkv\" id=\"ScriptTask_06obwkv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"241\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p2jx04\" id=\"SequenceFlow_0p2jx04_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"241\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_070d7ng\" id=\"EndEvent_070d7ng_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"372\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"390\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0chyplu\" id=\"SequenceFlow_0chyplu_di\"\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"356.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "a@a.com",
      "description": "Create a SOAR incident artifact from ExtraHop device property. Valid types are IP Address, DNS Name or MAC Address.",
      "export_key": "wf_extrahop_rx_add_artifact",
      "last_modified_by": "a@a.com",
      "last_modified_time": 1653920618463,
      "name": "Example: Extrahop Reveal(x) add artifact",
      "object_type": "extrahop_devices",
      "programmatic_name": "wf_extrahop_rx_add_artifact",
      "tags": [
        {
          "tag_handle": "fn_extrahop",
          "value": null
        }
      ],
      "uuid": "9b17bae7-271d-4683-a58b-825cdaeb09bc",
      "workflow_id": 93
    }
  ],
  "workspaces": []
}
