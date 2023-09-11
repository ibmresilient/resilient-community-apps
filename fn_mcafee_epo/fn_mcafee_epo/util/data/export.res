{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Add Permission Set to User",
      "id": 66,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Add Permission Set to User",
      "object_type": "mcafee_epo_permission_sets",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c9b86ec0-9778-47aa-9395-8eeaca0e6bb9",
      "view_items": [
        {
          "content": "b3aec334-6f5d-47b3-8bd5-ac1bacbe32fb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_add_permission_sets_to_user"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Add System",
      "id": 67,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Add System",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9fde229f-832c-4d25-bd8a-2947bea10a5d",
      "view_items": [
        {
          "content": "Required",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8ceaf604-1d11-4a9b-b2c9-0b4b7df68b71",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "32dc9aa3-1de2-45a5-830c-90c21e0c8da4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Optional",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "109a50e8-4417-4581-ab9d-2a0170a2a36e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f0cde799-d8f6-4936-99d9-ffa303885b7a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "81f9dbf9-173d-4cc4-a9ca-f8138f9e24b2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9134908e-ea1f-460b-8905-f2c5df5d9110",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "00a6ab5d-aff1-42c7-ac26-0166996083aa",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c45557a-09c6-4cf5-9dc8-66e760650c0a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "adf29fa1-8128-4cd5-8b7a-ab879dadc892",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "001e5998-5059-44e0-99ea-a90716b36110",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a0dc6a4c-7085-4310-9344-051b2c99fd37",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "46c38281-5d33-48ee-8d88-13a2a8e8ef00",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "df7028fa-1949-435f-a03e-3f579bbb96c3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7b005ea4-0a51-4b0b-a840-9d688ed18db8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f0a646d7-2b2e-46fe-a488-2f83ae38a8d9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_add_system"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Add User",
      "id": 68,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Add User",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0474f687-f2c6-490b-8430-aad3e108ed26",
      "view_items": [
        {
          "content": "Required",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3aec334-6f5d-47b3-8bd5-ac1bacbe32fb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a40ff3d-49a3-4d63-bb39-bf0958216288",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Optional",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "301ee32d-b495-489f-82f5-a2bff778b282",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5d6cba75-8964-4264-b7f9-09d5883f72ce",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3bb0693a-ae8a-41d7-8473-c8c85af4856f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d453dbe-2ab0-4a96-bda0-81c49e791370",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b7195acb-98d9-4464-ab3b-6cd5a74aa24d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "174a3249-ef7e-45d5-84d8-2fa2ed8cd046",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab03c38d-209b-4fd1-9c1b-39f0bc2e040b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_add_user"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Apply a Tag",
      "id": 69,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Apply a Tag",
      "object_type": "mcafee_epo_tags",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4b83ab93-bdae-4f1b-8516-ad4b870c850e",
      "view_items": [
        {
          "content": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_apply_a_tag"
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
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO Apply Tags",
      "id": 70,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Apply Tags",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fb53f6ab-d562-4cb7-841e-23099694c171",
      "view_items": [
        {
          "content": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_apply_tags"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Assign Policy to Group from Group",
      "id": 71,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Assign Policy to Group from Group",
      "object_type": "mcafee_epo_groups",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "326c864a-5c91-4c1d-bbc7-7d566cfe5043",
      "view_items": [
        {
          "content": "433da847-7353-404d-b7f1-687a071b6872",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24dd804f-37d1-40a4-b77e-6d8bfcba2289",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_assign_policy_to_group_from_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Assign Policy to Group from Policy",
      "id": 72,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Assign Policy to Group from Policy",
      "object_type": "mcafee_epo_policies",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d5ebe732-e398-4448-93b2-e62c082a28a1",
      "view_items": [
        {
          "content": "32dc9aa3-1de2-45a5-830c-90c21e0c8da4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_assign_policy_to_group_from_policy"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Assign Policy to System from System",
      "id": 73,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Assign Policy to System from System",
      "object_type": "mcafee_epo_systems",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4bbe188a-6133-44cc-a98d-d1bfccf77300",
      "view_items": [
        {
          "content": "24dd804f-37d1-40a4-b77e-6d8bfcba2289",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3bc3b79-a17a-454d-a7b2-b72f48cc7250",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "433da847-7353-404d-b7f1-687a071b6872",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_assign_policy_to_system_from_system"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Assign Policy to Systems from Policy",
      "id": 74,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Assign Policy to Systems from Policy",
      "object_type": "mcafee_epo_policies",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fbf4d5f8-3106-423a-876a-0e503b558fac",
      "view_items": [
        {
          "content": "8ceaf604-1d11-4a9b-b2c9-0b4b7df68b71",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_assign_policy_to_systems_from_policy"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Create Issue",
      "id": 75,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Create Issue",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1caa9cb8-d552-4a13-8ec1-8b8c95cea15e",
      "view_items": [
        {
          "content": "Required",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a306a5f-b537-4633-b3e8-7340445f908c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b6ad135-5c88-4743-b1ce-99bbfbe61239",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Optional",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5e406024-d27a-4ce6-a232-44428fbc2a01",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "add51952-f6fe-4a51-860a-795bfa4a706d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c546e8d-c906-4a0a-b4ba-313d1676e36f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48c53d38-fa32-4be1-a1ec-88a5139bb882",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9a2d4ed3-93c2-4155-8962-378b3e7b6ffd",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ff4a55e8-1883-4028-821e-03cc4904d804",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2bcacb74-c60e-4441-89e6-e82ef93a3015",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "29a320ab-7cd1-482a-91e8-c0cb387cec47",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c5dc189f-b2d2-461c-aab5-d568e29e9132",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3940f8e-9bf5-4dbc-98d4-3791eca72116",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_create_issue"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Delete Issue",
      "id": 76,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Delete Issue",
      "object_type": "mcafee_epo_issues",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "da87adf7-7410-4d0a-8b51-b0fe25cc5f24",
      "view_items": [],
      "workflows": [
        "mcafee_epo_delete_issue"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Delete System",
      "id": 77,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Delete System",
      "object_type": "mcafee_epo_systems",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1439363f-d3c4-4d1f-920b-14f7b5f4253a",
      "view_items": [],
      "workflows": [
        "mcafee_epo_delete_system"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Find All Client Tasks",
      "id": 78,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Find All Client Tasks",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "43e61e08-37a4-4577-a3d3-e31fd7c2cb9f",
      "view_items": [],
      "workflows": [
        "mcafee_epo_find_all_client_tasks"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Find All Groups",
      "id": 79,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Find All Groups",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "35ca8fb3-519e-48ca-9d0a-b3ac7523be98",
      "view_items": [],
      "workflows": [
        "mcafee_epo_find_all_groups"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Find Policies",
      "id": 80,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Find Policies",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4a6ebe50-d903-4afc-b287-bda7a2f1b0a5",
      "view_items": [],
      "workflows": [
        "mcafee_epo_find_policies"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Get All Permission Sets",
      "id": 81,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get All Permission Sets",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "17add228-14cf-44a1-9ba7-957e813fcec6",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_all_permission_sets"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Get All Systems",
      "id": 82,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get All Systems",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e79d9f00-56c4-4b2d-a0e6-a3b8d6babf32",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_all_systems"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Get All Users",
      "id": 83,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get All Users",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d213e4d9-e5d4-4ab6-aba0-f4b611ac2b96",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_all_users"
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
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO Get System Info",
      "id": 84,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get System Info",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "58a2bcde-39cb-40e9-ab23-7f7da4c6cc26",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_system_info"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Get System Info from Property",
      "id": 85,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get System Info from Property",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e04ca929-5f3e-4b03-96ea-71f521726de1",
      "view_items": [
        {
          "content": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_get_system_info_from_property"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Get System Information",
      "id": 86,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Get System Information",
      "object_type": "mcafee_epo_systems",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a8788ea0-7738-4b93-a7c5-795d345ebd68",
      "view_items": [],
      "workflows": [
        "mcafee_epo_get_system_information"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO List Issues",
      "id": 87,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO List Issues",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "68338423-f38a-4980-ac66-d6be9cb9c03c",
      "view_items": [],
      "workflows": [
        "mcafee_epo_list_issues"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO List Tags",
      "id": 88,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO List Tags",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9567fff9-5b8a-4d12-8e83-cde96e8b3ec9",
      "view_items": [],
      "workflows": [
        "mcafee_epo_list_tags"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Remove Permission Set from User",
      "id": 89,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Remove Permission Set from User",
      "object_type": "mcafee_epo_permission_sets",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "7a32f213-8cc9-485c-8ce5-b5f0f197cc53",
      "view_items": [
        {
          "content": "b3aec334-6f5d-47b3-8bd5-ac1bacbe32fb",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_remove_permission_set_from_user"
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
            "System Name",
            "MAC Address"
          ]
        }
      ],
      "enabled": true,
      "export_key": "McAfee ePO Remove Tags",
      "id": 90,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Remove Tags",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fcd70bd0-931e-42d5-886a-db45920f2af5",
      "view_items": [
        {
          "content": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_remove_tag"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Remove User",
      "id": 91,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Remove User",
      "object_type": "mcafee_epo_users",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6481337c-0f0b-4842-ba22-6b090975174a",
      "view_items": [],
      "workflows": [
        "mcafee_epo_remove_user"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Run Client Task",
      "id": 92,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Run Client Task",
      "object_type": "mcafee_epo_client_tasks",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "08234ccc-5df3-4ec1-80af-9df49b1f562b",
      "view_items": [
        {
          "content": "8ceaf604-1d11-4a9b-b2c9-0b4b7df68b71",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_run_client_task"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Run Client Task on System",
      "id": 93,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Run Client Task on System",
      "object_type": "mcafee_epo_systems",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "21045083-0a63-4f16-9ec6-ddff17cda845",
      "view_items": [
        {
          "content": "26905d07-1e1e-4d43-a8c5-effd90b646c9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24dd804f-37d1-40a4-b77e-6d8bfcba2289",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_run_client_task_on_system"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Update Issue",
      "id": 94,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Update Issue",
      "object_type": "mcafee_epo_issues",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "23666d4f-fc4e-428d-bd13-f3a67cc2ac88",
      "view_items": [
        {
          "content": "3a306a5f-b537-4633-b3e8-7340445f908c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b6ad135-5c88-4743-b1ce-99bbfbe61239",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5e406024-d27a-4ce6-a232-44428fbc2a01",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "add51952-f6fe-4a51-860a-795bfa4a706d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c546e8d-c906-4a0a-b4ba-313d1676e36f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "48c53d38-fa32-4be1-a1ec-88a5139bb882",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9a2d4ed3-93c2-4155-8962-378b3e7b6ffd",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ff4a55e8-1883-4028-821e-03cc4904d804",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2bcacb74-c60e-4441-89e6-e82ef93a3015",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "29a320ab-7cd1-482a-91e8-c0cb387cec47",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c5dc189f-b2d2-461c-aab5-d568e29e9132",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b3940f8e-9bf5-4dbc-98d4-3791eca72116",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_update_issue"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Update User",
      "id": 95,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Update User",
      "object_type": "mcafee_epo_users",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b9176641-f1d5-49ca-a294-296c0444d98e",
      "view_items": [
        {
          "content": "3ab9b1d3-8771-4912-bf7b-00a9fa8ef3a0",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3a40ff3d-49a3-4d63-bb39-bf0958216288",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "301ee32d-b495-489f-82f5-a2bff778b282",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5d6cba75-8964-4264-b7f9-09d5883f72ce",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3bb0693a-ae8a-41d7-8473-c8c85af4856f",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d453dbe-2ab0-4a96-bda0-81c49e791370",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "174a3249-ef7e-45d5-84d8-2fa2ed8cd046",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b7195acb-98d9-4464-ab3b-6cd5a74aa24d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ab03c38d-209b-4fd1-9c1b-39f0bc2e040b",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "02ad3c3e-03a0-4c72-8d07-8ea42e6da262",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "853b773d-c2e0-4828-b0c3-21c6ee692b94",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f350a200-9b51-498a-88c5-d5750cb4d282",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_update_user"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "McAfee ePO Wake up Agent",
      "id": 96,
      "logic_type": "all",
      "message_destinations": [],
      "name": "McAfee ePO Wake up Agent",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f273f809-b8f7-4420-8c35-e8c00b767bb7",
      "view_items": [
        {
          "content": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "mcafee_epo_wake_up_agent"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1664811038584,
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
      "export_key": "__function/mcafee_epo_new_username",
      "hide_notification": false,
      "id": 1296,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_new_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_new_username",
      "tooltip": "Change the ePO users usernam",
      "type_id": 11,
      "uuid": "80101eb8-577d-4737-95ad-d7db6effcc57",
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
      "export_key": "__function/mcafee_epo_push_agent_skip_if_installed",
      "hide_notification": false,
      "id": 1297,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_skip_if_installed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_skip_if_installed",
      "tooltip": "Skip pushing agent if it is installed",
      "type_id": 11,
      "uuid": "82a76921-c341-4e72-a576-b2006c60f525",
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
      "export_key": "__function/mcafee_epo_use_all_agent_handlers",
      "hide_notification": false,
      "id": 1298,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_use_all_agent_handlers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_use_all_agent_handlers",
      "tooltip": "True or false to use all agent handers",
      "type_id": 11,
      "uuid": "8378be72-9fbd-40f0-813d-84acb6f8b478",
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
      "export_key": "__function/mcafee_epo_issue_due",
      "hide_notification": false,
      "id": 1299,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_due",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_due",
      "tooltip": "Due date of the issue",
      "type_id": 11,
      "uuid": "83a16190-0db4-4b8d-a247-e5918309ff9c",
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
      "export_key": "__function/mcafee_epo_fullname",
      "hide_notification": false,
      "id": 1300,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_fullname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_fullname",
      "tooltip": "Full name for the new user",
      "type_id": 11,
      "uuid": "83ad827d-a6bd-44d7-892b-fd28a3efa1d1",
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
      "export_key": "__function/mcafee_epo_push_agent",
      "hide_notification": false,
      "id": 1301,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent",
      "tooltip": "wiether to push the agent to the system or not",
      "type_id": 11,
      "uuid": "8609adcd-0aaa-4e81-88d0-80c9e461d289",
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
      "export_key": "__function/mcafee_epo_ticket_id",
      "hide_notification": false,
      "id": 1302,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_ticket_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_ticket_id",
      "tooltip": "ID of the ticket",
      "type_id": 11,
      "uuid": "8bf4d417-d784-4752-9862-1b3aed4e385d",
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
      "export_key": "__function/mcafee_epo_abort_after_minutes",
      "hide_notification": false,
      "id": 1303,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_abort_after_minutes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_abort_after_minutes",
      "tooltip": "Number of minutes to wait to abort a call that isnt responding",
      "type_id": 11,
      "uuid": "8fbb495a-2958-4929-b0b3-ae2b1072e695",
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
      "export_key": "__function/mcafee_epo_push_agent_password",
      "hide_notification": false,
      "id": 1304,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_password",
      "tooltip": "Password for system",
      "type_id": 11,
      "uuid": "90ba14ec-4730-4870-88f3-147291abf2d9",
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
      "export_key": "__function/mcafee_epo_issue_severity",
      "hide_notification": false,
      "id": 1305,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_severity",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_severity",
      "tooltip": "Severity of the issue",
      "type_id": 11,
      "uuid": "9477b98a-5618-40d3-aab3-3c0f2c56ff59",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "b5611556-6d46-4755-9aab-38c72c55ad8d",
          "value": 242
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Lowest",
          "properties": null,
          "uuid": "54900b0d-3fc1-48b0-aec3-1e99bc1cf400",
          "value": 243
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "202dcca4-df0f-4235-9a08-e755fa24fa42",
          "value": 244
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "926be454-c8e7-49db-bc7c-e3b93ac02e5f",
          "value": 245
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "c0088c8b-75bb-43d3-966f-5414cbe26266",
          "value": 246
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Highest",
          "properties": null,
          "uuid": "058df23b-a5d3-49b2-a4c6-496e63c77c89",
          "value": 247
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
      "export_key": "__function/datatable_name",
      "hide_notification": false,
      "id": 1306,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "datatable_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Name of the datatable being cleared",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "datatable_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "9767f563-47d2-4daf-b353-284342833db8",
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
      "export_key": "__function/mcafee_epo_user_disabled",
      "hide_notification": false,
      "id": 1307,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_user_disabled",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_user_disabled",
      "tooltip": "Should the new user be disabled when created?",
      "type_id": 11,
      "uuid": "9d0751be-e063-411c-b04a-57f1b9d24407",
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
      "export_key": "__function/mcafee_epo_push_agent_force_install",
      "hide_notification": false,
      "id": 1308,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_force_install",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_force_install",
      "tooltip": "force install if agent on new system",
      "type_id": 11,
      "uuid": "a2779c87-2309-44bb-a423-2930fb5f2a04",
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
      "export_key": "__function/mcafee_epo_retry_intervals_in_seconds",
      "hide_notification": false,
      "id": 1309,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_retry_intervals_in_seconds",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_retry_intervals_in_seconds",
      "tooltip": "Number of seconds to wait between retrys",
      "type_id": 11,
      "uuid": "ac9b2c42-34c8-44b7-96b9-753402af3ce8",
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
      "export_key": "__function/mcafee_epo_query_group",
      "hide_notification": false,
      "id": 1310,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_query_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_query_group",
      "tooltip": "List, seperated by a space, of properties to group together in the output",
      "type_id": 11,
      "uuid": "aecce0bd-d875-405a-8a82-3e3672983fd4",
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
      "export_key": "__function/mcafee_epo_issue_state",
      "hide_notification": false,
      "id": 1311,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_state",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_state",
      "tooltip": "State of the issue",
      "type_id": 11,
      "uuid": "b114ab6f-268c-496f-9fd6-64ae4fc96e10",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "10234f71-637e-4dd6-906a-19e32ef335ca",
          "value": 248
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "4c89f37f-b974-47da-a1d7-c42a9040c74e",
          "value": 249
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Assigned",
          "properties": null,
          "uuid": "e305315f-04c7-4368-bea1-373c5eea12a6",
          "value": 250
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "7f562e50-15d2-4a15-b5c1-82de0f633437",
          "value": 251
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Closed",
          "properties": null,
          "uuid": "d570c184-9c28-4cbb-a16f-9324ffbdbb4f",
          "value": 252
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
      "export_key": "__function/mcafee_epo_object_id",
      "hide_notification": false,
      "id": 1312,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_object_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_object_id",
      "tooltip": "ID if object",
      "type_id": 11,
      "uuid": "b300efa4-5c6e-4e6a-8e0d-4972137b51b5",
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
      "export_key": "__function/mcafee_epo_product_id",
      "hide_notification": false,
      "id": 1313,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_product_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_product_id",
      "tooltip": "The product ID for the task",
      "type_id": 11,
      "uuid": "b4248da5-f2ca-46fb-a389-e51b4caf2cb7",
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
      "export_key": "__function/mcafee_epo_push_agent_suppress_ui",
      "hide_notification": false,
      "id": 1314,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_suppress_ui",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_suppress_ui",
      "tooltip": "Push agent and suppress ui",
      "type_id": 11,
      "uuid": "b4323a7a-a96c-417c-a6ee-03e4e9a89c15",
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
      "export_key": "__function/mcafee_epo_delete_if_removed",
      "hide_notification": false,
      "id": 1315,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_delete_if_removed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_delete_if_removed",
      "tooltip": "Should system be deleted if removed",
      "type_id": 11,
      "uuid": "b9c2b3d5-9b60-4102-863f-deb038573084",
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
      "export_key": "__function/mcafee_epo_retry_attempts",
      "hide_notification": false,
      "id": 1316,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_retry_attempts",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_retry_attempts",
      "tooltip": "Number of times to retry call",
      "type_id": 11,
      "uuid": "bca01f8b-018c-4c48-bebb-b3826e06ee39",
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
      "export_key": "__function/mcafee_epo_notes",
      "hide_notification": false,
      "id": 1317,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_notes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_notes",
      "tooltip": "Notes to add to the new user",
      "type_id": 11,
      "uuid": "bd4da808-aeba-45a0-b327-f06dc90b9709",
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
      "export_key": "__function/mcafee_epo_systems",
      "hide_notification": false,
      "id": 1318,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_systems",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_systems",
      "tooltip": "Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO",
      "type_id": 11,
      "uuid": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
      "export_key": "__function/mcafee_epo_push_agent_username",
      "hide_notification": false,
      "id": 1319,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_username",
      "tooltip": "username for system",
      "type_id": 11,
      "uuid": "bf5c2d93-c137-4e69-a976-462f531e0c8d",
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
      "export_key": "__function/mcafee_epo_admin",
      "hide_notification": false,
      "id": 1320,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_admin",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_admin",
      "tooltip": "Should this user have admin privileges ",
      "type_id": 11,
      "uuid": "c591bd91-9f03-44e7-a012-c766f6df6715",
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
      "export_key": "__function/mcafee_epo_email",
      "hide_notification": false,
      "id": 1321,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_email",
      "tooltip": "Email for the new user",
      "type_id": 11,
      "uuid": "c659cdce-1d9e-4e19-8e4b-07eb3756960a",
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
      "export_key": "__function/mcafee_epo_push_agent_domain_name",
      "hide_notification": false,
      "id": 1322,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_domain_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_domain_name",
      "tooltip": "Domain name for system to push agent",
      "type_id": 11,
      "uuid": "c6e02222-d63e-4824-809e-9ebf556f1cff",
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
      "export_key": "__function/mcafee_epo_issue_name",
      "hide_notification": false,
      "id": 1323,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_name",
      "tooltip": "Name of the issue on the ePO server",
      "type_id": 11,
      "uuid": "cd420db2-85fa-4b36-836e-b84b08da53d0",
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
      "export_key": "__function/mcafee_epo_issue_assignee",
      "hide_notification": false,
      "id": 1324,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_assignee",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_assignee",
      "tooltip": "Username of person assigned to the issue",
      "type_id": 11,
      "uuid": "d20dd061-06ce-4daf-8942-92b9b5f745b0",
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
      "export_key": "__function/mcafee_epo_push_agent_package_path",
      "hide_notification": false,
      "id": 1325,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_package_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_package_path",
      "tooltip": "Path the package on the new system",
      "type_id": 11,
      "uuid": "d7375d24-21e6-457d-8b3e-fe72a5076b15",
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
      "export_key": "__function/mcafee_epo_random_minutes",
      "hide_notification": false,
      "id": 1326,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_random_minutes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_random_minutes",
      "tooltip": "number of random minutes",
      "type_id": 11,
      "uuid": "d8a5c6fd-0830-45f6-879f-8567ed73d00d",
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
      "export_key": "__function/mcafee_epo_stop_after_minutes",
      "hide_notification": false,
      "id": 1327,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_stop_after_minutes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_stop_after_minutes",
      "tooltip": "number of minutes to wait until stopping retry call",
      "type_id": 11,
      "uuid": "e152d90c-28a4-4480-89e4-a8e5fa3cc33c",
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
      "export_key": "__function/mcafee_epo_issue_description",
      "hide_notification": false,
      "id": 1328,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_description",
      "tooltip": "description of the issue ",
      "type_id": 11,
      "uuid": "e64b4847-576c-41fd-9ebe-30388463d740",
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
      "export_key": "__function/mcafee_epo_uninstall",
      "hide_notification": false,
      "id": 1329,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_uninstall",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_uninstall",
      "tooltip": "True or false to uninstall system",
      "type_id": 11,
      "uuid": "f3512f4f-b0fe-427f-9114-1fe12aaa9f04",
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
      "export_key": "__function/mcafee_epo_type_id",
      "hide_notification": false,
      "id": 1330,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_type_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_type_id",
      "tooltip": "Type ID",
      "type_id": 11,
      "uuid": "f77c2f40-35d7-4900-8b7b-4d0c0cc2d7d1",
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
      "export_key": "__function/mcafee_epo_allowed_ips",
      "hide_notification": false,
      "id": 1331,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_allowed_ips",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_allowed_ips",
      "tooltip": "A list of ips that can access the new user",
      "type_id": 11,
      "uuid": "f824010c-151e-4ff1-8062-6f770997f544",
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
      "export_key": "__function/mcafee_epo_pass",
      "hide_notification": false,
      "id": 1332,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_pass",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_pass",
      "tooltip": "Password for ePO user",
      "type_id": 11,
      "uuid": "f94eb163-9184-4f4b-97e3-8ca127b2a157",
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
      "export_key": "__function/mcafee_epo_query_order",
      "hide_notification": false,
      "id": 1333,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_query_order",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_query_order",
      "tooltip": "Starts with asc for ascending or des for descending order a space and then the property to sort by",
      "type_id": 11,
      "uuid": "fc273b98-b408-4b43-ae7b-118e7082bf63",
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
      "export_key": "__function/mcafee_epo_flatten_tree_structure",
      "hide_notification": false,
      "id": 1334,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_flatten_tree_structure",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_flatten_tree_structure",
      "tooltip": "Should flatten tree structure",
      "type_id": 11,
      "uuid": "03e74613-d3ee-4632-87c1-2f61ac7e3b3a",
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
      "export_key": "__function/mcafee_epo_issue_id",
      "hide_notification": false,
      "id": 1335,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_id",
      "tooltip": "ID of the issue",
      "type_id": 11,
      "uuid": "050a0e76-1842-47ef-9f3f-5132db7ebe86",
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
      "export_key": "__function/mcafee_epo_issue_properties",
      "hide_notification": false,
      "id": 1336,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_properties",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_properties",
      "tooltip": "Properties for the issue",
      "type_id": 11,
      "uuid": "06bece11-b70f-4205-9e67-37db3d3f5dda",
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
      "export_key": "__function/mcafee_epo_issue_priority",
      "hide_notification": false,
      "id": 1337,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_priority",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_priority",
      "tooltip": "The priority of the issue",
      "type_id": 11,
      "uuid": "079bf7ef-d3a9-4b0d-9e72-cdcbb4783d01",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "026f887f-61d5-4806-9c17-4fadddc2d58f",
          "value": 253
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Lowest",
          "properties": null,
          "uuid": "86511491-26f4-4353-baa5-d773536da011",
          "value": 254
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "356e7a8e-13be-4eaa-80f4-894d1505f2e8",
          "value": 255
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "2fa8bbb9-d020-425b-948f-eaffbc0fc430",
          "value": 256
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "6c78f5c3-fffb-49a2-bdbf-e2161eb394b0",
          "value": 257
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Highest",
          "properties": null,
          "uuid": "a5fe3e7f-37d8-4590-b809-b5507a731020",
          "value": 258
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
      "export_key": "__function/mcafee_epo_ticket_server_name",
      "hide_notification": false,
      "id": 1338,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_ticket_server_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_ticket_server_name",
      "tooltip": "Name of the server the issue should be on",
      "type_id": 11,
      "uuid": "0c19dd34-7797-48b2-b2c8-f6279da97148",
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
      "export_key": "__function/mcafee_epo_phone_number",
      "hide_notification": false,
      "id": 1339,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_phone_number",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_phone_number",
      "tooltip": "Phone number for the new user",
      "type_id": 11,
      "uuid": "0ff2c2b8-89ac-451c-bdb2-ecd83588e9f7",
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
      "export_key": "__function/mcafee_epo_tag",
      "hide_notification": false,
      "id": 1340,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_tag",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_tag",
      "tooltip": "Tag managed on ePO",
      "type_id": 11,
      "uuid": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
      "export_key": "__function/mcafee_epo_system_name_or_id",
      "hide_notification": false,
      "id": 1341,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_system_name_or_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_system_name_or_id",
      "tooltip": "Comma seperated list of systems name or system ids",
      "type_id": 11,
      "uuid": "1f6f5cd4-cccf-4d78-9cc6-84a6550152c6",
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
      "id": 1342,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "SOAR incident id",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "1f8b5186-4843-473e-a7ef-261488512aad",
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
      "export_key": "__function/mcafee_epo_uninstall_software",
      "hide_notification": false,
      "id": 1343,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_uninstall_software",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_uninstall_software",
      "tooltip": "True or false to uninstall software on system",
      "type_id": 11,
      "uuid": "21706c4d-8ec9-4d45-8650-03e4ad3604ad",
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
      "export_key": "__function/mcafee_epo_sub_group",
      "hide_notification": false,
      "id": 1344,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_sub_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_sub_group",
      "tooltip": "Sub group name",
      "type_id": 11,
      "uuid": "23690958-a914-48b2-acec-4362f9816641",
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
      "export_key": "__function/mcafee_epo_windowsdomain",
      "hide_notification": false,
      "id": 1345,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_windowsdomain",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_windowsdomain",
      "tooltip": "Add a windows domain to the ePO users info",
      "type_id": 11,
      "uuid": "29fe75c0-8120-42d4-b3e3-b1240754ddbd",
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
      "export_key": "__function/mcafee_epo_timeout_in_hours",
      "hide_notification": false,
      "id": 1346,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_timeout_in_hours",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_timeout_in_hours",
      "tooltip": "Number of hours to wait until timeout",
      "type_id": 11,
      "uuid": "3058b1a0-2f52-4f3c-a61a-7e8c758677f6",
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
      "export_key": "__function/mcafee_epo_allow_duplicates",
      "hide_notification": false,
      "id": 1347,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_allow_duplicates",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_allow_duplicates",
      "tooltip": "Weither to allow duplicates or not",
      "type_id": 11,
      "uuid": "313002e7-a3f0-46a8-a6af-befb9d65ecea",
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
      "export_key": "__function/mcafee_epo_push_agent_install_path",
      "hide_notification": false,
      "id": 1348,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_push_agent_install_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_push_agent_install_path",
      "tooltip": "path to where the agent should be installed on the system",
      "type_id": 11,
      "uuid": "34053585-8ade-487d-b9c0-9b909d6c4f8e",
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
      "export_key": "__function/mcafee_epo_subjectdn",
      "hide_notification": false,
      "id": 1349,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_subjectdn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_subjectdn",
      "tooltip": "Add a subject DN to the ePO users info",
      "type_id": 11,
      "uuid": "353a1329-c745-49ab-9178-ee94c279b2e7",
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
      "export_key": "__function/mcafee_epo_issue_resolution",
      "hide_notification": false,
      "id": 1350,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_resolution",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_resolution",
      "tooltip": "Resolution status of the issue",
      "type_id": 11,
      "uuid": "3561f86b-44c7-4c83-9fc5-962bf0231192",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "7a9a788f-93c6-4575-bdb0-d22f9823624f",
          "value": 259
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Fixed",
          "properties": null,
          "uuid": "51871e15-184d-4c05-b486-583e5e4d511d",
          "value": 260
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Waived",
          "properties": null,
          "uuid": "15685a92-a121-47f1-a065-a2a8803d0dc9",
          "value": 261
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Will Not Fix",
          "properties": null,
          "uuid": "924e3517-61dc-4478-9258-380ade7f8fc1",
          "value": 262
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
      "export_key": "__function/mcafee_epo_username",
      "hide_notification": false,
      "id": 1351,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_username",
      "tooltip": "User name for ePO user",
      "type_id": 11,
      "uuid": "38fb4df9-f658-48d9-9f41-594c053337e2",
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
      "export_key": "__function/mcafee_epo_target",
      "hide_notification": false,
      "id": 1352,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_target",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_target",
      "tooltip": "ePO data types target name",
      "type_id": 11,
      "uuid": "3b19d71b-890d-472c-bec7-40a035c1bca2",
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
      "export_key": "__function/mcafee_epo_issue_type",
      "hide_notification": false,
      "id": 1353,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_issue_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_issue_type",
      "tooltip": "Issue type",
      "type_id": 11,
      "uuid": "4daa5700-47bc-4a1d-9e4d-1d32fe202286",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Basic",
          "properties": null,
          "uuid": "fa68645e-e98b-4ba0-9ff6-f3bff26f20a4",
          "value": 263
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
      "export_key": "__function/mcafee_epo_search_text",
      "hide_notification": false,
      "id": 1354,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_search_text",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_search_text",
      "tooltip": "",
      "type_id": 11,
      "uuid": "4ebc533a-359e-486d-9355-6c2a45a52d02",
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
      "export_key": "__function/mcafee_epo_group_id",
      "hide_notification": false,
      "id": 1355,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_group_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_group_id",
      "tooltip": "Id for the group on the ePO server",
      "type_id": 11,
      "uuid": "53bbb755-1c65-48c2-a323-c64ca989de16",
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
      "export_key": "__function/mcafee_epo_reset_inheritance",
      "hide_notification": false,
      "id": 1356,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_reset_inheritance",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_reset_inheritance",
      "tooltip": "Boolean to reset inheritance",
      "type_id": 11,
      "uuid": "646a51c3-b515-4a74-8e55-561261de69ba",
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
      "export_key": "__function/mcafee_epo_task_id",
      "hide_notification": false,
      "id": 1357,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_task_id",
      "tooltip": "The ID of the client task",
      "type_id": 11,
      "uuid": "66fc3d02-6834-487e-b658-ff34c36104e6",
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
      "export_key": "__function/mcafee_epo_query_select",
      "hide_notification": false,
      "id": 1358,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_query_select",
      "operation_perms": {},
      "operations": [],
      "placeholder": "EPOAssignedPolicy.NodeName EPOAssignedPolicy.UserName",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_query_select",
      "tooltip": "List of fields to return seperated by a space",
      "type_id": 11,
      "uuid": "6b48880e-8669-483e-8c8c-effb63f5fc18",
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
      "export_key": "__function/mcafee_epo_queryid",
      "hide_notification": false,
      "id": 1359,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_queryid",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_queryid",
      "tooltip": "The ID of the query you want to run",
      "type_id": 11,
      "uuid": "71c94599-1aee-4b14-84ca-8bade00be741",
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
      "export_key": "__function/mcafee_epo_windowsusername",
      "hide_notification": false,
      "id": 1360,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_windowsusername",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_windowsusername",
      "tooltip": "Add a windows user name to the ePO users info",
      "type_id": 11,
      "uuid": "74a73043-5370-4b64-bdcc-182e6f445b67",
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
      "export_key": "__function/mcafee_epo_permsetname",
      "hide_notification": false,
      "id": 1361,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "mcafee_epo_permsetname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "mcafee_epo_permsetname",
      "tooltip": "Name of the permission set to add to the ePO user",
      "type_id": 11,
      "uuid": "750a2448-13cb-4204-a2ea-2a4e0f1d9dc5",
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
      "export_key": "actioninvocation/epo_push_agent",
      "hide_notification": false,
      "id": 1250,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent",
      "tooltip": "True or false push the agent to the system",
      "type_id": 6,
      "uuid": "81f9dbf9-173d-4cc4-a9ca-f8138f9e24b2",
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
      "export_key": "actioninvocation/epo_windows_domain",
      "hide_notification": false,
      "id": 1251,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_windows_domain",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Windows Domain",
      "tooltip": "A windows domain to add to ePO server",
      "type_id": 6,
      "uuid": "853b773d-c2e0-4828-b0c3-21c6ee692b94",
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
      "export_key": "actioninvocation/epo_issue_severity",
      "hide_notification": false,
      "id": 1252,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_severity",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Severity",
      "tooltip": "Severity of the issue",
      "type_id": 6,
      "uuid": "8c546e8d-c906-4a0a-b4ba-313d1676e36f",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "dc244905-b3a8-4c3e-b64a-d55b30ec622d",
          "value": 214
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Lowest",
          "properties": null,
          "uuid": "da63b7c3-a8dc-48da-ad41-77e4aa262d33",
          "value": 215
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "366de95d-2c38-4d72-ab22-e5fcfe30c25e",
          "value": 216
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "d5f0f865-25f2-4d1a-b5fa-2041341d50d5",
          "value": 217
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "9b2d529a-ae5c-45f1-b656-f5ee61a36123",
          "value": 218
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Highest",
          "properties": null,
          "uuid": "e15c21f8-7ebf-4e31-ba12-f2ae2fed1936",
          "value": 219
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
      "export_key": "actioninvocation/epo_system_names_or_ids",
      "hide_notification": false,
      "id": 1253,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_system_names_or_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO System Names or IDs",
      "tooltip": "Comma seperated list of system names or IDs",
      "type_id": 6,
      "uuid": "8ceaf604-1d11-4a9b-b2c9-0b4b7df68b71",
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
      "export_key": "actioninvocation/epo_push_agent_force_install",
      "hide_notification": false,
      "id": 1254,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_force_install",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Force Install",
      "tooltip": "True or false push agent and force install",
      "type_id": 6,
      "uuid": "9134908e-ea1f-460b-8905-f2c5df5d9110",
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
      "export_key": "actioninvocation/epo_issue_state",
      "hide_notification": false,
      "id": 1255,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_state",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue State",
      "tooltip": "State of the issue",
      "type_id": 6,
      "uuid": "9a2d4ed3-93c2-4155-8962-378b3e7b6ffd",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "3761fa02-8af9-4304-9929-e0a71c85bde0",
          "value": 220
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "82e4489f-61fa-426f-bbe3-f825ab1b89b9",
          "value": 221
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Assigned",
          "properties": null,
          "uuid": "bb9ce071-5536-4467-aada-f5d5c830f2be",
          "value": 222
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "0e034d44-2e6c-49c8-9911-3be10ebb2395",
          "value": 223
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Closed",
          "properties": null,
          "uuid": "931fda06-4e58-4690-97b3-cf83c4c2c9db",
          "value": 224
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
      "export_key": "actioninvocation/epo_notes",
      "hide_notification": false,
      "id": 1256,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_notes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Notes",
      "tooltip": "Notes to add to the ePO user",
      "type_id": 6,
      "uuid": "9d453dbe-2ab0-4a96-bda0-81c49e791370",
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
      "export_key": "actioninvocation/epo_push_agent_domain_name",
      "hide_notification": false,
      "id": 1257,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_domain_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Domain Name",
      "tooltip": "Domain name for system to push agent",
      "type_id": 6,
      "uuid": "a0dc6a4c-7085-4310-9344-051b2c99fd37",
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
      "export_key": "actioninvocation/epo_allowed_ips",
      "hide_notification": false,
      "id": 1258,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_allowed_ips",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Allowed IPs",
      "tooltip": "List if IPs allowed to access the user",
      "type_id": 6,
      "uuid": "ab03c38d-209b-4fd1-9c1b-39f0bc2e040b",
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
      "export_key": "actioninvocation/epo_issue_priority",
      "hide_notification": false,
      "id": 1259,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_priority",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Priority",
      "tooltip": "The  priority of the issue",
      "type_id": 6,
      "uuid": "add51952-f6fe-4a51-860a-795bfa4a706d",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unknown",
          "properties": null,
          "uuid": "1d52053f-a6d5-46d3-b06d-3a1290c5d583",
          "value": 225
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Lowest",
          "properties": null,
          "uuid": "a8b255bd-9c08-4b75-9072-0881116f9609",
          "value": 226
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Low",
          "properties": null,
          "uuid": "515db145-e6b6-49a8-a1b4-afee62282f5f",
          "value": 227
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Medium",
          "properties": null,
          "uuid": "4b360c97-a849-4afc-8031-47bd73e0bf7f",
          "value": 228
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "High",
          "properties": null,
          "uuid": "2dbab188-8a72-4d6f-98f3-a03ea3513fba",
          "value": 229
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Highest",
          "properties": null,
          "uuid": "92c141c8-7163-4119-9426-d4365cc8465e",
          "value": 230
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
      "export_key": "actioninvocation/epo_push_agent_install_path",
      "hide_notification": false,
      "id": 1260,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_install_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Install Path",
      "tooltip": "path to where the agent should be installed on the system",
      "type_id": 6,
      "uuid": "adf29fa1-8128-4cd5-8b7a-ab879dadc892",
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
      "export_key": "actioninvocation/epo_ticket_server_name",
      "hide_notification": false,
      "id": 1261,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_ticket_server_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Ticket Server Name",
      "tooltip": "Name of the ticket server",
      "type_id": 6,
      "uuid": "b3940f8e-9bf5-4dbc-98d4-3791eca72116",
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
      "export_key": "actioninvocation/epo_username",
      "hide_notification": false,
      "id": 1262,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Username",
      "tooltip": "User name of an ePO user",
      "type_id": 6,
      "uuid": "b3aec334-6f5d-47b3-8bd5-ac1bacbe32fb",
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
      "export_key": "actioninvocation/epo_policy_type_id",
      "hide_notification": false,
      "id": 1263,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "epo_policy_type_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Policy Type ID",
      "tooltip": "Policy type ID",
      "type_id": 6,
      "uuid": "b3bc3b79-a17a-454d-a7b2-b72f48cc7250",
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
      "export_key": "actioninvocation/epo_user_disbabled",
      "hide_notification": false,
      "id": 1264,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_user_disbabled",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO User Disbabled",
      "tooltip": "If the user should be diabled",
      "type_id": 6,
      "uuid": "b7195acb-98d9-4464-ab3b-6cd5a74aa24d",
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
      "export_key": "actioninvocation/epo_ticket_id",
      "hide_notification": false,
      "id": 1265,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "epo_ticket_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Ticket ID",
      "tooltip": "ID of the ticket",
      "type_id": 6,
      "uuid": "c5dc189f-b2d2-461c-aab5-d568e29e9132",
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
      "export_key": "actioninvocation/epo_push_agent_password",
      "hide_notification": false,
      "id": 1266,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Password",
      "tooltip": "Password for the system",
      "type_id": 6,
      "uuid": "df7028fa-1949-435f-a03e-3f579bbb96c3",
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
      "export_key": "actioninvocation/epo_system",
      "hide_notification": false,
      "id": 1267,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_system",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO System",
      "tooltip": "Comma seperated list of systems properties or one system ",
      "type_id": 6,
      "uuid": "e5b13796-c649-4b6f-b38c-4f65637e9fb2",
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
      "export_key": "actioninvocation/ss_tags",
      "hide_notification": false,
      "id": 1268,
      "input_type": "multiselect",
      "internal": false,
      "is_tracked": false,
      "name": "ss_tags",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "List of tags",
      "tooltip": "Multiselect tags. Edit the list for your system",
      "type_id": 6,
      "uuid": "ebbb5eed-7401-4712-b440-0e6fc331afa1",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Escalated",
          "properties": null,
          "uuid": "a6e80147-c8ac-4c7f-b8d1-ac68a8406a37",
          "value": 231
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Excluded from Compliance Check",
          "properties": null,
          "uuid": "cb328af4-0cf1-49a7-87c0-89e846125299",
          "value": 232
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Server",
          "properties": null,
          "uuid": "4a896abb-838a-4cb0-a501-4a3e296b6c7d",
          "value": 233
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Shut Down",
          "properties": null,
          "uuid": "2fae2f32-cf34-4494-8c2d-4b86896b815b",
          "value": 234
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Workstation",
          "properties": null,
          "uuid": "2a7a4656-6043-4bb6-9379-1f71a92ebd20",
          "value": 235
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u0100 \u0101 \u0102 \u0103 \u0104 \u0105",
          "properties": null,
          "uuid": "9bf8605d-5791-4ef8-9095-bb9866bfb010",
          "value": 236
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
      "export_key": "actioninvocation/epo_flatten_tree_structure",
      "hide_notification": false,
      "id": 1269,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_flatten_tree_structure",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Flatten Tree Structure",
      "tooltip": "Should flatten tree structure",
      "type_id": 6,
      "uuid": "f0a646d7-2b2e-46fe-a488-2f83ae38a8d9",
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
      "export_key": "actioninvocation/epo_uninstall_removed",
      "hide_notification": false,
      "id": 1270,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_uninstall_removed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Uninstall Removed",
      "tooltip": "True or false to uninstall system",
      "type_id": 6,
      "uuid": "f0cde799-d8f6-4936-99d9-ffa303885b7a",
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
      "export_key": "actioninvocation/epo_subject_dn",
      "hide_notification": false,
      "id": 1271,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_subject_dn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Subject DN",
      "tooltip": "Subject DN to add to ePO user",
      "type_id": 6,
      "uuid": "f350a200-9b51-498a-88c5-d5750cb4d282",
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
      "export_key": "actioninvocation/epo_issue_assignee",
      "hide_notification": false,
      "id": 1272,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_assignee",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Assignee",
      "tooltip": "Username of the user to assign to the issue",
      "type_id": 6,
      "uuid": "ff4a55e8-1883-4028-821e-03cc4904d804",
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
      "export_key": "actioninvocation/epo_push_agent_package_path",
      "hide_notification": false,
      "id": 1273,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_package_path",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Package Path",
      "tooltip": "Path the package on the new system",
      "type_id": 6,
      "uuid": "001e5998-5059-44e0-99ea-a90716b36110",
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
      "export_key": "actioninvocation/epo_push_agent_skip_if_installed",
      "hide_notification": false,
      "id": 1274,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_skip_if_installed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Skip If Installed",
      "tooltip": "Skip pushing agent if it is installed",
      "type_id": 6,
      "uuid": "00a6ab5d-aff1-42c7-ac26-0166996083aa",
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
      "export_key": "actioninvocation/epo_windows_username",
      "hide_notification": false,
      "id": 1275,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_windows_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Windows Username",
      "tooltip": "Windows username for ePO server ",
      "type_id": 6,
      "uuid": "02ad3c3e-03a0-4c72-8d07-8ea42e6da262",
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
      "export_key": "actioninvocation/epo_push_agent_suppress_ui",
      "hide_notification": false,
      "id": 1276,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_suppress_ui",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent Suppress UI",
      "tooltip": "Push agent and suppress ui",
      "type_id": 6,
      "uuid": "0c45557a-09c6-4cf5-9dc8-66e760650c0a",
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
      "export_key": "actioninvocation/epo_allow_duplicates",
      "hide_notification": false,
      "id": 1277,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_allow_duplicates",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Allow Duplicates",
      "tooltip": "Weither to allow duplicates or not",
      "type_id": 6,
      "uuid": "109a50e8-4417-4581-ab9d-2a0170a2a36e",
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
      "export_key": "actioninvocation/epo_admin",
      "hide_notification": false,
      "id": 1278,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_admin",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Admin",
      "tooltip": "If user should be admin",
      "type_id": 6,
      "uuid": "174a3249-ef7e-45d5-84d8-2fa2ed8cd046",
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
      "export_key": "actioninvocation/epo_product_id",
      "hide_notification": false,
      "id": 1279,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_product_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Product ID",
      "tooltip": "ID of the product the task is associated with",
      "type_id": 6,
      "uuid": "24dd804f-37d1-40a4-b77e-6d8bfcba2289",
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
      "export_key": "actioninvocation/epo_task_id",
      "hide_notification": false,
      "id": 1280,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "epo_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Task ID",
      "tooltip": "Id for the task to run on the system",
      "type_id": 6,
      "uuid": "26905d07-1e1e-4d43-a8c5-effd90b646c9",
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
      "export_key": "actioninvocation/epo_issue_properties",
      "hide_notification": false,
      "id": 1281,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_properties",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Properties",
      "tooltip": "Properties for the issue",
      "type_id": 6,
      "uuid": "29a320ab-7cd1-482a-91e8-c0cb387cec47",
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
      "export_key": "actioninvocation/epo_issue_due",
      "hide_notification": false,
      "id": 1282,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_due",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Due",
      "tooltip": "Due date of the issue",
      "type_id": 6,
      "uuid": "2bcacb74-c60e-4441-89e6-e82ef93a3015",
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
      "export_key": "actioninvocation/epo_full_name",
      "hide_notification": false,
      "id": 1283,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_full_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Full Name",
      "tooltip": "Full name of the ePO user",
      "type_id": 6,
      "uuid": "301ee32d-b495-489f-82f5-a2bff778b282",
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
      "export_key": "actioninvocation/epo_group_id",
      "hide_notification": false,
      "id": 1284,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "epo_group_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Group ID",
      "tooltip": "ID for the group",
      "type_id": 6,
      "uuid": "32dc9aa3-1de2-45a5-830c-90c21e0c8da4",
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
      "export_key": "actioninvocation/epo_issue_name",
      "hide_notification": false,
      "id": 1285,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Name",
      "tooltip": "Name of the issue",
      "type_id": 6,
      "uuid": "3a306a5f-b537-4633-b3e8-7340445f908c",
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
      "export_key": "actioninvocation/epo_user_password",
      "hide_notification": false,
      "id": 1286,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_user_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO User Password",
      "tooltip": "Password for the ePO user",
      "type_id": 6,
      "uuid": "3a40ff3d-49a3-4d63-bb39-bf0958216288",
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
      "export_key": "actioninvocation/epo_new_username",
      "hide_notification": false,
      "id": 1287,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_new_username",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO New Username",
      "tooltip": "Change ePO users username",
      "type_id": 6,
      "uuid": "3ab9b1d3-8771-4912-bf7b-00a9fa8ef3a0",
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
      "export_key": "actioninvocation/epo_issue_description",
      "hide_notification": false,
      "id": 1288,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Description",
      "tooltip": "Description of the issue",
      "type_id": 6,
      "uuid": "3b6ad135-5c88-4743-b1ce-99bbfbe61239",
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
      "export_key": "actioninvocation/epo_phone_number",
      "hide_notification": false,
      "id": 1289,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_phone_number",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Phone Number",
      "tooltip": "Phone number for the ePO user",
      "type_id": 6,
      "uuid": "3bb0693a-ae8a-41d7-8473-c8c85af4856f",
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
      "export_key": "actioninvocation/epo_policy_id",
      "hide_notification": false,
      "id": 1290,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "epo_policy_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "ID of the policy name",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Policy ID",
      "tooltip": "",
      "type_id": 6,
      "uuid": "433da847-7353-404d-b7f1-687a071b6872",
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
      "export_key": "actioninvocation/epo_push_agent_user_name",
      "hide_notification": false,
      "id": 1291,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_push_agent_user_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Push Agent User Name",
      "tooltip": "username for system",
      "type_id": 6,
      "uuid": "46c38281-5d33-48ee-8d88-13a2a8e8ef00",
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
      "export_key": "actioninvocation/epo_issue_resolution",
      "hide_notification": false,
      "id": 1292,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_resolution",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Resolution",
      "tooltip": "Resolution of the issue",
      "type_id": 6,
      "uuid": "48c53d38-fa32-4be1-a1ec-88a5139bb882",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "364fbf42-5e2e-4294-b7c0-07a74440d9db",
          "value": 237
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Fixed",
          "properties": null,
          "uuid": "2b0cfbad-7d90-45bd-84a1-70627dee7fca",
          "value": 238
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Waived",
          "properties": null,
          "uuid": "848afd9f-c383-4d73-b827-803e5ad8a2a0",
          "value": 239
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Will Not Fix",
          "properties": null,
          "uuid": "4e6421ec-f594-4eb1-86a6-386c9fe4f38c",
          "value": 240
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
      "export_key": "actioninvocation/epo_email",
      "hide_notification": false,
      "id": 1293,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "epo_email",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Email",
      "tooltip": "Email for the ePO user",
      "type_id": 6,
      "uuid": "5d6cba75-8964-4264-b7f9-09d5883f72ce",
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
      "export_key": "actioninvocation/epo_issue_type",
      "hide_notification": false,
      "id": 1294,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "epo_issue_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Issue Type",
      "tooltip": "Issue type",
      "type_id": 6,
      "uuid": "5e406024-d27a-4ce6-a232-44428fbc2a01",
      "values": [
        {
          "default": false,
          "enabled": false,
          "hidden": false,
          "label": "Basic",
          "properties": null,
          "uuid": "b88e9546-ee65-4a3f-900a-798192ab2e80",
          "value": 241
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "BASIC",
          "properties": null,
          "uuid": "cb8cff20-dc6d-48a5-989f-675b9b23469c",
          "value": 302
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
      "export_key": "actioninvocation/epo_delete_if_removed",
      "hide_notification": false,
      "id": 1295,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "epo_delete_if_removed",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "templates": [],
      "text": "ePO Delete If Removed",
      "tooltip": "Should system be deleted if removed",
      "type_id": 6,
      "uuid": "7b005ea4-0a51-4b0b-a840-9d688ed18db8",
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
      "created_date": 1664546132441,
      "description": {
        "content": "Add permission set(s) to an ePO user",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Add Permission sets to user",
      "export_key": "mcafee_epo_add_permission_sets_to_user",
      "id": 4,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132496,
      "name": "mcafee_epo_add_permission_sets_to_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_username\": \"test\", \"mcafee_epo_permsetname\": \"Global Reviewer\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 593, \"timestamp\": \"2022-08-02 12:48:58\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_username\": {\"type\": \"string\"}, \"mcafee_epo_permsetname\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "6492efd0-43f0-4078-943e-46e033ceccb6",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "750a2448-13cb-4204-a2ea-2a4e0f1d9dc5",
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
          "name": "McAfee ePO Add Permission Sets to user",
          "object_type": "mcafee_epo_permission_sets",
          "programmatic_name": "mcafee_epo_add_permission_sets_to_user",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 21
        }
      ]
    },
    {
      "created_date": 1664546132514,
      "description": {
        "content": "Add a system to the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Add System",
      "export_key": "mcafee_epo_add_system",
      "id": 5,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132567,
      "name": "mcafee_epo_add_system",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_push_agent_install_path\": null, \"mcafee_epo_push_agent_package_path\": null, \"mcafee_epo_push_agent_force_install\": null, \"mcafee_epo_group_id\": 2, \"mcafee_epo_push_agent\": null, \"mcafee_epo_push_agent_domain_name\": null, \"mcafee_epo_flatten_tree_structure\": null, \"mcafee_epo_allow_duplicates\": null, \"mcafee_epo_delete_if_removed\": null, \"mcafee_epo_push_agent_username\": null, \"mcafee_epo_uninstall\": null, \"mcafee_epo_push_agent_skip_if_installed\": null, \"mcafee_epo_system_name_or_id\": \"fffff\", \"mcafee_epo_push_agent_suppress_ui\": null, \"mcafee_epo_push_agent_password\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 176568, \"timestamp\": \"2022-08-16 14:16:44\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_push_agent_install_path\": {}, \"mcafee_epo_push_agent_package_path\": {}, \"mcafee_epo_push_agent_force_install\": {}, \"mcafee_epo_group_id\": {\"type\": \"integer\"}, \"mcafee_epo_push_agent\": {}, \"mcafee_epo_push_agent_domain_name\": {}, \"mcafee_epo_flatten_tree_structure\": {}, \"mcafee_epo_allow_duplicates\": {}, \"mcafee_epo_delete_if_removed\": {}, \"mcafee_epo_push_agent_username\": {}, \"mcafee_epo_uninstall\": {}, \"mcafee_epo_push_agent_skip_if_installed\": {}, \"mcafee_epo_system_name_or_id\": {\"type\": \"string\"}, \"mcafee_epo_push_agent_suppress_ui\": {}, \"mcafee_epo_push_agent_password\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "b30f5c25-c4f3-49ed-ba15-fe4d82c71249",
      "version": 1,
      "view_items": [
        {
          "content": "1f6f5cd4-cccf-4d78-9cc6-84a6550152c6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "53bbb755-1c65-48c2-a323-c64ca989de16",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "313002e7-a3f0-46a8-a6af-befb9d65ecea",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f3512f4f-b0fe-427f-9114-1fe12aaa9f04",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8609adcd-0aaa-4e81-88d0-80c9e461d289",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a2779c87-2309-44bb-a423-2930fb5f2a04",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "82a76921-c341-4e72-a576-b2006c60f525",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4323a7a-a96c-417c-a6ee-03e4e9a89c15",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "34053585-8ade-487d-b9c0-9b909d6c4f8e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d7375d24-21e6-457d-8b3e-fe72a5076b15",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c6e02222-d63e-4824-809e-9ebf556f1cff",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bf5c2d93-c137-4e69-a976-462f531e0c8d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "90ba14ec-4730-4870-88f3-147291abf2d9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b9c2b3d5-9b60-4102-863f-deb038573084",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03e74613-d3ee-4632-87c1-2f61ac7e3b3a",
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
          "name": "McAfee ePO Add System",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_add_system",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 18
        }
      ]
    },
    {
      "created_date": 1664546132586,
      "description": {
        "content": "Add a user to the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Add User",
      "export_key": "mcafee_epo_add_user",
      "id": 6,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132640,
      "name": "mcafee_epo_add_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_pass\": \"password\", \"mcafee_epo_allowed_ips\": null, \"mcafee_epo_phone_number\": \"534-452-0287\", \"mcafee_epo_email\": \"jeff@example.com\", \"mcafee_epo_username\": \"jeff\", \"mcafee_epo_notes\": \"jefferson notes\", \"mcafee_epo_user_disabled\": false, \"mcafee_epo_fullname\": \"jeff\", \"mcafee_epo_admin\": true}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 604, \"timestamp\": \"2022-08-10 12:55:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_pass\": {\"type\": \"string\"}, \"mcafee_epo_allowed_ips\": {}, \"mcafee_epo_phone_number\": {\"type\": \"string\"}, \"mcafee_epo_email\": {\"type\": \"string\"}, \"mcafee_epo_username\": {\"type\": \"string\"}, \"mcafee_epo_notes\": {\"type\": \"string\"}, \"mcafee_epo_user_disabled\": {\"type\": \"boolean\"}, \"mcafee_epo_fullname\": {\"type\": \"string\"}, \"mcafee_epo_admin\": {\"type\": \"boolean\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "0d34aa89-8ebf-4c17-9c7f-4ea851c37a82",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f94eb163-9184-4f4b-97e3-8ca127b2a157",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "83ad827d-a6bd-44d7-892b-fd28a3efa1d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c659cdce-1d9e-4e19-8e4b-07eb3756960a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0ff2c2b8-89ac-451c-bdb2-ecd83588e9f7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd4da808-aeba-45a0-b327-f06dc90b9709",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f824010c-151e-4ff1-8062-6f770997f544",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d0751be-e063-411c-b04a-57f1b9d24407",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c591bd91-9f03-44e7-a012-c766f6df6715",
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
          "name": "McAfee ePO Add User",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_add_user",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 14
        }
      ]
    },
    {
      "created_date": 1664546132661,
      "description": {
        "content": "Assigns policy to the specified group no ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Assign Policy to Group",
      "export_key": "mcafee_epo_assign_policy_to_group",
      "id": 7,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132715,
      "name": "mcafee_epo_assign_policy_to_group",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_product_id\": \"MARCOBA_META\", \"mcafee_epo_group_id\": 5, \"mcafee_epo_object_id\": 39}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 751, \"timestamp\": \"2022-08-22 12:05:01\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_product_id\": {\"type\": \"string\"}, \"mcafee_epo_group_id\": {\"type\": \"integer\"}, \"mcafee_epo_object_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4dc3b4db-1f72-4b4e-b7e0-c5996f743697",
      "version": 1,
      "view_items": [
        {
          "content": "53bbb755-1c65-48c2-a323-c64ca989de16",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b300efa4-5c6e-4e6a-8e0d-4972137b51b5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4248da5-f2ca-46fb-a389-e51b4caf2cb7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "646a51c3-b515-4a74-8e55-561261de69ba",
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
          "name": "McAfee ePO Assign Policy to Group from Group",
          "object_type": "mcafee_epo_groups",
          "programmatic_name": "mcafee_epo_assign_policy_to_group_from_group",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 24
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Assign Policy to Group from Policy",
          "object_type": "mcafee_epo_policies",
          "programmatic_name": "mcafee_epo_assign_policy_to_group_from_policy",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 39
        }
      ]
    },
    {
      "created_date": 1664546132732,
      "description": {
        "content": "Assigns the policy to a supplied list of systems on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Assign Policy to Systems",
      "export_key": "mcafee_epo_assign_policy_to_systems",
      "id": 8,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132788,
      "name": "mcafee_epo_assign_policy_to_systems",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"name\": \"SystemA\", \"id\": \"12\", \"message\": \"Assign policy succeeded\", \"status\": 0}], \"raw\": null, \"inputs\": {\"mcafee_epo_product_id\": \"MARCOBA_META\", \"mcafee_epo_system_name_or_id\": \"SystemA\", \"mcafee_epo_object_id\": 39, \"mcafee_epo_type_id\": 19}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 709, \"timestamp\": \"2022-08-22 12:13:29\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"message\": {\"type\": \"string\"}, \"status\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_product_id\": {\"type\": \"string\"}, \"mcafee_epo_system_name_or_id\": {\"type\": \"string\"}, \"mcafee_epo_object_id\": {\"type\": \"integer\"}, \"mcafee_epo_type_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "81575bf7-1c92-45d0-a674-4682f9e735c7",
      "version": 1,
      "view_items": [
        {
          "content": "1f6f5cd4-cccf-4d78-9cc6-84a6550152c6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b300efa4-5c6e-4e6a-8e0d-4972137b51b5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4248da5-f2ca-46fb-a389-e51b4caf2cb7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "646a51c3-b515-4a74-8e55-561261de69ba",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f77c2f40-35d7-4900-8b7b-4d0c0cc2d7d1",
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
          "name": "McAfee ePO Assign Policy to System from System",
          "object_type": "mcafee_epo_systems",
          "programmatic_name": "mcafee_epo_assign_policy_to_system_from_system",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 42
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Assign Policy to Systems from Policy",
          "object_type": "mcafee_epo_policies",
          "programmatic_name": "mcafee_epo_assign_policy_to_systems_from_policy",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 29
        }
      ]
    },
    {
      "created_date": 1664546132806,
      "description": {
        "content": "Create an issue on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Create Issue",
      "export_key": "mcafee_epo_create_issue",
      "id": 9,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132859,
      "name": "mcafee_epo_create_issue",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": 13, \"raw\": null, \"inputs\": {\"mcafee_epo_issue_name\": \"New issue\", \"mcafee_epo_issue_properties\": null, \"mcafee_epo_ticket_server_name\": null, \"mcafee_epo_issue_due\": 1661950852000, \"mcafee_epo_issue_state\": \"Assigned\", \"mcafee_epo_issue_severity\": \"Low\", \"mcafee_epo_issue_description\": \"Test issue creation\", \"mcafee_epo_issue_assignee\": \"Jefferson\", \"mcafee_epo_issue_type\": \"Basic\", \"mcafee_epo_ticket_id\": null, \"mcafee_epo_issue_priority\": \"Medium\", \"mcafee_epo_issue_resolution\": \"Will Not Fix\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 547, \"timestamp\": \"2022-08-19 09:00:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"integer\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_issue_name\": {\"type\": \"string\"}, \"mcafee_epo_issue_properties\": {}, \"mcafee_epo_ticket_server_name\": {}, \"mcafee_epo_issue_due\": {\"type\": \"integer\"}, \"mcafee_epo_issue_state\": {\"type\": \"string\"}, \"mcafee_epo_issue_severity\": {\"type\": \"string\"}, \"mcafee_epo_issue_description\": {\"type\": \"string\"}, \"mcafee_epo_issue_assignee\": {\"type\": \"string\"}, \"mcafee_epo_issue_type\": {\"type\": \"string\"}, \"mcafee_epo_ticket_id\": {}, \"mcafee_epo_issue_priority\": {\"type\": \"string\"}, \"mcafee_epo_issue_resolution\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "8bbcc714-05ce-4894-bd65-9f5daff302e5",
      "version": 1,
      "view_items": [
        {
          "content": "cd420db2-85fa-4b36-836e-b84b08da53d0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e64b4847-576c-41fd-9ebe-30388463d740",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4daa5700-47bc-4a1d-9e4d-1d32fe202286",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b114ab6f-268c-496f-9fd6-64ae4fc96e10",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "079bf7ef-d3a9-4b0d-9e72-cdcbb4783d01",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9477b98a-5618-40d3-aab3-3c0f2c56ff59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3561f86b-44c7-4c83-9fc5-962bf0231192",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d20dd061-06ce-4daf-8942-92b9b5f745b0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "83a16190-0db4-4b8d-a247-e5918309ff9c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c19dd34-7797-48b2-b2c8-f6279da97148",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8bf4d417-d784-4752-9862-1b3aed4e385d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06bece11-b70f-4205-9e67-37db3d3f5dda",
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
          "name": "McAfee ePO Create Issue",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_create_issue",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 22
        }
      ]
    },
    {
      "created_date": 1664546132876,
      "description": {
        "content": "Delete an issue from the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Delete Issue",
      "export_key": "mcafee_epo_delete_issue",
      "id": 10,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546132930,
      "name": "mcafee_epo_delete_issue",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": 1, \"raw\": null, \"inputs\": {\"mcafee_epo_issue_id\": 12}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 538, \"timestamp\": \"2022-08-19 09:01:12\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"integer\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_issue_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "9edf3f57-b79b-4a50-bc6b-632ea6406dfe",
      "version": 1,
      "view_items": [
        {
          "content": "050a0e76-1842-47ef-9f3f-5132db7ebe86",
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
          "name": "McAfee ePO Delete Issue",
          "object_type": "mcafee_epo_issues",
          "programmatic_name": "mcafee_epo_delete_issue",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 34
        }
      ]
    },
    {
      "created_date": 1664546132947,
      "description": {
        "content": "Delete a system from the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Delete System",
      "export_key": "mcafee_epo_delete_system",
      "id": 11,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133002,
      "name": "mcafee_epo_delete_system",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"name\": \"toDelete\", \"id\": \"15\", \"message\": \"Computer deleted successfully\", \"status\": 0}], \"raw\": null, \"inputs\": {\"mcafee_epo_system_name_or_id\": \"toDelete\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 615, \"timestamp\": \"2022-08-12 09:11:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"message\": {\"type\": \"string\"}, \"status\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_system_name_or_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4011b9c6-eeba-49da-b5f7-27fdce026c83",
      "version": 1,
      "view_items": [
        {
          "content": "1f6f5cd4-cccf-4d78-9cc6-84a6550152c6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f3512f4f-b0fe-427f-9114-1fe12aaa9f04",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "21706c4d-8ec9-4d45-8650-03e4ad3604ad",
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
          "name": "McAfee ePO Delete System",
          "object_type": "mcafee_epo_systems",
          "programmatic_name": "mcafee_epo_delete_system",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 35
        }
      ]
    },
    {
      "created_date": 1664546133020,
      "description": {
        "content": "Execute a query on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Execute Query",
      "export_key": "mcafee_epo_execute_query",
      "id": 12,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133075,
      "name": "mcafee_epo_execute_query",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"EPOLeafNode.Tags\": \"Intel(R) Xeon(R) CPU, Linux, Server\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": \"2022-08-12T06:10:31-07:00\", \"EPOLeafNode.os\": \"Linux|Server|4.9|227-1.mlos2.x86_64\", \"EPOLeafNode.NodeName\": \"int-mcafee-tie\", \"EPOLeafNode.ManagedState\": 1, \"EPOLeafNode.AgentVersion\": \"5.6.5.236\", \"EPOLeafNode.AgentGUID\": \"E1ABB618-09C4-11ED-2BBA-005056B43418\", \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"1\"}, {\"EPOLeafNode.Tags\": \"Intel Core Processor, Server, Windows server 2016\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": \"2022-08-12T05:42:46-07:00\", \"EPOLeafNode.os\": \"Windows Server 2016|Server|10.0|\", \"EPOLeafNode.NodeName\": \"MCAFEE-EPO-CLIE\", \"EPOLeafNode.ManagedState\": 1, \"EPOLeafNode.AgentVersion\": \"5.5.1.388\", \"EPOLeafNode.AgentGUID\": \"D770FEB6-3C1E-40A9-ACB2-B74E5FF66D5E\", \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"1\"}, {\"EPOLeafNode.Tags\": \"Intel(R) Xeon(R) CPU, Server, Windows server 2016\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": \"2022-08-12T06:00:08-07:00\", \"EPOLeafNode.os\": \"Windows Server 2016|Server|10.0|\", \"EPOLeafNode.NodeName\": \"WIN-MTHJTQ4ELBP\", \"EPOLeafNode.ManagedState\": 1, \"EPOLeafNode.AgentVersion\": \"5.6.6.232\", \"EPOLeafNode.AgentGUID\": \"B7E3C7E0-CDE7-11EB-3210-005056B41000\", \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"1\"}, {\"EPOLeafNode.Tags\": \"\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": null, \"EPOLeafNode.os\": \"|||\", \"EPOLeafNode.NodeName\": \"SystemA\", \"EPOLeafNode.ManagedState\": 0, \"EPOLeafNode.AgentVersion\": null, \"EPOLeafNode.AgentGUID\": null, \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"0\"}, {\"EPOLeafNode.Tags\": \"\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": null, \"EPOLeafNode.os\": \"|||\", \"EPOLeafNode.NodeName\": \"LostSystem\", \"EPOLeafNode.ManagedState\": 0, \"EPOLeafNode.AgentVersion\": null, \"EPOLeafNode.AgentGUID\": null, \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"0\"}, {\"EPOLeafNode.Tags\": \"\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": null, \"EPOLeafNode.os\": \"|||\", \"EPOLeafNode.NodeName\": \"toDelete\", \"EPOLeafNode.ManagedState\": 0, \"EPOLeafNode.AgentVersion\": null, \"EPOLeafNode.AgentGUID\": null, \"EPOLeafNode.ResortEnabled\": false, \"EPOLeafNode.TransferSiteListsID\": false, \"EPOLeafNode.SequenceErrorCount\": 0, \"EPOLeafNode.SequenceErrorCountLastUpdate\": null, \"EPOLeafNode.LastCommSecure\": \"0\"}], \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"datatable_name\": \"mcafee_epo_systems\", \"mcafee_epo_target\": \"EPOLeafNode\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 1252, \"timestamp\": \"2022-08-12 09:10:36\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"EPOLeafNode.Tags\": {\"type\": \"string\"}, \"EPOLeafNode.ExcludedTags\": {\"type\": \"string\"}, \"EPOLeafNode.LastUpdate\": {\"type\": [\"null\", \"string\"]}, \"EPOLeafNode.os\": {\"type\": \"string\"}, \"EPOLeafNode.NodeName\": {\"type\": \"string\"}, \"EPOLeafNode.ManagedState\": {\"type\": \"integer\"}, \"EPOLeafNode.AgentVersion\": {\"type\": [\"null\", \"string\"]}, \"EPOLeafNode.AgentGUID\": {\"type\": [\"null\", \"string\"]}, \"EPOLeafNode.ResortEnabled\": {\"type\": \"boolean\"}, \"EPOLeafNode.TransferSiteListsID\": {\"type\": \"boolean\"}, \"EPOLeafNode.SequenceErrorCount\": {\"type\": \"integer\"}, \"EPOLeafNode.SequenceErrorCountLastUpdate\": {}, \"EPOLeafNode.LastCommSecure\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"datatable_name\": {\"type\": \"string\"}, \"mcafee_epo_target\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "3a78912f-473f-4eaf-86b3-05dc87c5e14a",
      "version": 1,
      "view_items": [
        {
          "content": "71c94599-1aee-4b14-84ca-8bade00be741",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3b19d71b-890d-472c-bec7-40a035c1bca2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6b48880e-8669-483e-8c8c-effb63f5fc18",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aecce0bd-d875-405a-8a82-3e3672983fd4",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fc273b98-b408-4b43-ae7b-118e7082bf63",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
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
          "name": "McAfee ePO Find All Groups",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_find_all_groups",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 33
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Find Policies",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_find_policies",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 44
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Get all Permission Sets",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_all_permission_sets",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 31
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Get All Systems",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_all_systems",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 26
        }
      ]
    },
    {
      "created_date": 1664546133093,
      "description": {
        "content": "Find an ePO system based on a property such as system name, tag, IP address, MAC address, etc.",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Find a System",
      "export_key": "mcafee_epo_find_a_system",
      "id": 13,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133148,
      "name": "mcafee_epo_find_a_system",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"EPOComputerProperties.ParentID\": 13, \"EPOComputerProperties.ComputerName\": \"test_server\", \"EPOComputerProperties.Description\": null, \"EPOComputerProperties.ComputerDescription\": null, \"EPOComputerProperties.TimeZone\": \"\", \"EPOComputerProperties.DefaultLangID\": \"\", \"EPOComputerProperties.UserName\": \"\", \"EPOComputerProperties.DomainName\": \"\", \"EPOComputerProperties.IPHostName\": \"\", \"EPOComputerProperties.IPV6\": null, \"EPOComputerProperties.IPAddress\": \"\", \"EPOComputerProperties.IPSubnet\": null, \"EPOComputerProperties.IPSubnetMask\": null, \"EPOComputerProperties.IPV4x\": null, \"EPOComputerProperties.IPXAddress\": \"\", \"EPOComputerProperties.SubnetAddress\": \"\", \"EPOComputerProperties.SubnetMask\": \"\", \"EPOComputerProperties.NetAddress\": \"\", \"EPOComputerProperties.OSType\": \"\", \"EPOComputerProperties.OSVersion\": \"\", \"EPOComputerProperties.OSCsdVersion\": \"\", \"EPOComputerProperties.OSBuildNum\": 0, \"EPOComputerProperties.OSPlatform\": \"\", \"EPOComputerProperties.OSOEMID\": \"\", \"EPOComputerProperties.CPUType\": \"\", \"EPOComputerProperties.CPUSpeed\": 0, \"EPOComputerProperties.NumOfCPU\": 0, \"EPOComputerProperties.CPUSerialNumber\": \"\", \"EPOComputerProperties.TotalPhysicalMemory\": 0, \"EPOComputerProperties.FreeMemory\": 0, \"EPOComputerProperties.FreeDiskSpace\": 0, \"EPOComputerProperties.TotalDiskSpace\": 0, \"EPOComputerProperties.IsPortable\": -1, \"EPOComputerProperties.Vdi\": -1, \"EPOComputerProperties.OSBitMode\": -1, \"EPOComputerProperties.LastAgentHandler\": null, \"EPOComputerProperties.UserProperty1\": null, \"EPOComputerProperties.UserProperty2\": null, \"EPOComputerProperties.UserProperty3\": null, \"EPOComputerProperties.UserProperty4\": null, \"EPOComputerProperties.UserProperty5\": null, \"EPOComputerProperties.UserProperty6\": null, \"EPOComputerProperties.UserProperty7\": null, \"EPOComputerProperties.UserProperty8\": null, \"EPOComputerProperties.Free_Space_of_Drive_C\": 0, \"EPOComputerProperties.Total_Space_of_Drive_C\": 0, \"EPOLeafNode.Tags\": \"myTag, Server, SOAR\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": null, \"EPOLeafNode.ManagedState\": 0, \"EPOLeafNode.AgentGUID\": null, \"EPOLeafNode.AgentVersion\": null, \"EPOBranchNode.AutoID\": 2}], \"raw\": null, \"inputs\": {\"mcafee_epo_systems\": \"test_server\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 649, \"timestamp\": \"2022-07-01 12:40:10\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"EPOComputerProperties.ParentID\": {\"type\": \"integer\"}, \"EPOComputerProperties.ComputerName\": {\"type\": \"string\"}, \"EPOComputerProperties.Description\": {}, \"EPOComputerProperties.ComputerDescription\": {}, \"EPOComputerProperties.TimeZone\": {\"type\": \"string\"}, \"EPOComputerProperties.DefaultLangID\": {\"type\": \"string\"}, \"EPOComputerProperties.UserName\": {\"type\": \"string\"}, \"EPOComputerProperties.DomainName\": {\"type\": \"string\"}, \"EPOComputerProperties.IPHostName\": {\"type\": \"string\"}, \"EPOComputerProperties.IPV6\": {}, \"EPOComputerProperties.IPAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.IPSubnet\": {}, \"EPOComputerProperties.IPSubnetMask\": {}, \"EPOComputerProperties.IPV4x\": {}, \"EPOComputerProperties.IPXAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.SubnetAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.SubnetMask\": {\"type\": \"string\"}, \"EPOComputerProperties.NetAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.OSType\": {\"type\": \"string\"}, \"EPOComputerProperties.OSVersion\": {\"type\": \"string\"}, \"EPOComputerProperties.OSCsdVersion\": {\"type\": \"string\"}, \"EPOComputerProperties.OSBuildNum\": {\"type\": \"integer\"}, \"EPOComputerProperties.OSPlatform\": {\"type\": \"string\"}, \"EPOComputerProperties.OSOEMID\": {\"type\": \"string\"}, \"EPOComputerProperties.CPUType\": {\"type\": \"string\"}, \"EPOComputerProperties.CPUSpeed\": {\"type\": \"integer\"}, \"EPOComputerProperties.NumOfCPU\": {\"type\": \"integer\"}, \"EPOComputerProperties.CPUSerialNumber\": {\"type\": \"string\"}, \"EPOComputerProperties.TotalPhysicalMemory\": {\"type\": \"integer\"}, \"EPOComputerProperties.FreeMemory\": {\"type\": \"integer\"}, \"EPOComputerProperties.FreeDiskSpace\": {\"type\": \"integer\"}, \"EPOComputerProperties.TotalDiskSpace\": {\"type\": \"integer\"}, \"EPOComputerProperties.IsPortable\": {\"type\": \"integer\"}, \"EPOComputerProperties.Vdi\": {\"type\": \"integer\"}, \"EPOComputerProperties.OSBitMode\": {\"type\": \"integer\"}, \"EPOComputerProperties.LastAgentHandler\": {}, \"EPOComputerProperties.UserProperty1\": {}, \"EPOComputerProperties.UserProperty2\": {}, \"EPOComputerProperties.UserProperty3\": {}, \"EPOComputerProperties.UserProperty4\": {}, \"EPOComputerProperties.UserProperty5\": {}, \"EPOComputerProperties.UserProperty6\": {}, \"EPOComputerProperties.UserProperty7\": {}, \"EPOComputerProperties.UserProperty8\": {}, \"EPOComputerProperties.Free_Space_of_Drive_C\": {\"type\": \"integer\"}, \"EPOComputerProperties.Total_Space_of_Drive_C\": {\"type\": \"integer\"}, \"EPOLeafNode.Tags\": {\"type\": \"string\"}, \"EPOLeafNode.ExcludedTags\": {\"type\": \"string\"}, \"EPOLeafNode.LastUpdate\": {}, \"EPOLeafNode.ManagedState\": {\"type\": \"integer\"}, \"EPOLeafNode.AgentGUID\": {}, \"EPOLeafNode.AgentVersion\": {}, \"EPOBranchNode.AutoID\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_systems\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "0030078d-417f-4d92-9212-6853914b56af",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
          "name": "McAfee ePO Get System Info",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_get_system_info",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 27
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Get System Info from Property",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_system_info_from_property",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 15
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Get System Information",
          "object_type": "mcafee_epo_systems",
          "programmatic_name": "mcafee_epo_get_system_information",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 43
        }
      ]
    },
    {
      "created_date": 1664546133166,
      "description": {
        "content": "Find client tasks on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Find Client Tasks",
      "export_key": "mcafee_epo_find_client_tasks",
      "id": 14,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133220,
      "name": "mcafee_epo_find_client_tasks",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"productId\": \"EPOAGENTMETA\", \"typeName\": \"McAfee Agent: McAfee Agent Statistics\", \"objectName\": \"Collect All\", \"typeId\": 4, \"objectId\": 7, \"productName\": \"McAfee Agent \"}, {\"productId\": \"EPOAGENTMETA\", \"typeName\": \"McAfee Agent: McAfee Agent Wakeup\", \"objectName\": \"Get changed properties\", \"typeId\": 3, \"objectId\": 14, \"productName\": \"McAfee Agent \"}, {\"productId\": \"EPOAGENTMETA\", \"typeName\": \"McAfee Agent: Product Update\", \"objectName\": \"Update all packages\", \"typeId\": 1, \"objectId\": 15, \"productName\": \"McAfee Agent \"}], \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"datatable_name\": \"mcafee_epo_client_tasks\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 1088, \"timestamp\": \"2022-08-12 09:58:29\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"productId\": {\"type\": \"string\"}, \"typeName\": {\"type\": \"string\"}, \"objectName\": {\"type\": \"string\"}, \"typeId\": {\"type\": \"integer\"}, \"objectId\": {\"type\": \"integer\"}, \"productName\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"datatable_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "948b9c0a-1d8e-47c4-a277-1180ee5d3f5e",
      "version": 1,
      "view_items": [
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4ebc533a-359e-486d-9355-6c2a45a52d02",
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
          "name": "McAfee ePO Find All Client Tasks",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_find_all_client_tasks",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1664546133238,
      "description": {
        "content": "Find groups on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Find Groups",
      "export_key": "mcafee_epo_find_groups",
      "id": 15,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133293,
      "name": "mcafee_epo_find_groups",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"groupId\": 2, \"groupPath\": \"My Organization\"}, {\"groupId\": 3, \"groupPath\": \"My Organization\\\\Lost and Found\"}, {\"groupId\": 4, \"groupPath\": \"My Organization\\\\Lost and Found\\\\rtp.raleigh.ibm.com\"}, {\"groupId\": 5, \"groupPath\": \"My Organization\\\\Test\"}], \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"datatable_name\": \"mcafee_epo_groups\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 1217, \"timestamp\": \"2022-08-11 08:48:38\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"groupId\": {\"type\": \"integer\"}, \"groupPath\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"datatable_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "cec9d0f8-06bc-4168-9fec-554d2fef8a99",
      "version": 1,
      "view_items": [
        {
          "content": "4ebc533a-359e-486d-9355-6c2a45a52d02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
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
          "name": "McAfee ePO Find All Groups",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_find_all_groups",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    },
    {
      "created_date": 1664546133311,
      "description": {
        "content": "Finds all policies that match the given search text or find all policies if no search text is given",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Find Policies",
      "export_key": "mcafee_epo_find_policies",
      "id": 16,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133369,
      "name": "mcafee_epo_find_policies",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"productId\": \"MARCOBA_META\", \"featureName\": \"MARCOBA_META\", \"typeName\": \"General\", \"objectName\": \"McAfee Default\", \"typeId\": 19, \"featureId\": \"MARCOBA_META\", \"objectId\": 39, \"productName\": \"Active Response 2.4.4\", \"objectNotes\": \"\"}, {\"productId\": \"MARCOBA_META\", \"featureName\": \"MARCOBA_META\", \"typeName\": \"General\", \"objectName\": \"Full Visibility\", \"typeId\": 19, \"featureId\": \"MARCOBA_META\", \"objectId\": 40, \"productName\": \"Active Response 2.4.4\", \"objectNotes\": \"\"}, {\"productId\": \"MARCOBA_META\", \"featureName\": \"MARCOBA_META\", \"typeName\": \"General\", \"objectName\": \"Full Monitoring\", \"typeId\": 19, \"featureId\": \"MARCOBA_META\", \"objectId\": 41, \"productName\": \"Active Response 2.4.4\", \"objectNotes\": \"\"}, {\"productId\": \"MARCOBA_META\", \"featureName\": \"MARCOBA_META\", \"typeName\": \"General\", \"objectName\": \"My Default\", \"typeId\": 19, \"featureId\": \"MARCOBA_META\", \"objectId\": 42, \"productName\": \"Active Response 2.4.4\", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"General\", \"objectName\": \"McAfee Default\", \"typeId\": 3, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 4, \"productName\": \"McAfee Agent \", \"objectNotes\": \"The McAfee Default policy is configured with settings recommended by McAfee to protect many environments\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"General\", \"objectName\": \"Large Organization Default\", \"typeId\": 3, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 9, \"productName\": \"McAfee Agent \", \"objectNotes\": \"The Large Organization Default policy is configured with settings recommended by McAfee to protect large enterprise environments.\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"General\", \"objectName\": \"My Default\", \"typeId\": 3, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 11, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Repository\", \"objectName\": \"McAfee Default\", \"typeId\": 4, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 5, \"productName\": \"McAfee Agent \", \"objectNotes\": \"The McAfee Default policy is configured with settings recommended by McAfee to protect many environments\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Repository\", \"objectName\": \"My Default\", \"typeId\": 4, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 12, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Troubleshooting\", \"objectName\": \"McAfee Default\", \"typeId\": 5, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 6, \"productName\": \"McAfee Agent \", \"objectNotes\": \"The McAfee Default policy is configured with settings recommended by McAfee to protect many environments\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Troubleshooting\", \"objectName\": \"My Default\", \"typeId\": 5, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 13, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Custom Properties\", \"objectName\": \"McAfee Default\", \"typeId\": 6, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 7, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Custom Properties\", \"objectName\": \"My Default\", \"typeId\": 6, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 14, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Product Improvement Program\", \"objectName\": \"McAfee Default\", \"typeId\": 7, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 8, \"productName\": \"McAfee Agent \", \"objectNotes\": \"The McAfee Default policy is configured with settings recommended by McAfee to protect many environments\"}, {\"productId\": \"EPOAGENTMETA\", \"featureName\": \"McAfee Agent\", \"typeName\": \"Product Improvement Program\", \"objectName\": \"My Default\", \"typeId\": 7, \"featureId\": \"EPOAGENTMETA\", \"objectId\": 15, \"productName\": \"McAfee Agent \", \"objectNotes\": \"\"}, {\"productId\": \"DXLBROKRMETA\", \"featureName\": \"McAfee DXL Broker Management\", \"typeName\": \"General\", \"objectName\": \"McAfee Default\", \"typeId\": 13, \"featureId\": \"DXLBROKRMETA\", \"objectId\": 24, \"productName\": \"McAfee DXL Broker Management 6.0.0\", \"objectNotes\": \"\"}, {\"productId\": \"DXLBROKRMETA\", \"featureName\": \"McAfee DXL Broker Management\", \"typeName\": \"General\", \"objectName\": \"My Default\", \"typeId\": 13, \"featureId\": \"DXLBROKRMETA\", \"objectId\": 28, \"productName\": \"McAfee DXL Broker Management 6.0.0\", \"objectNotes\": \"\"}, {\"productId\": \"DXLCLNT_META\", \"featureName\": \"McAfee DXL Client\", \"typeName\": \"General\", \"objectName\": \"McAfee Default\", \"typeId\": 17, \"featureId\": \"DXLCLNT_META\", \"objectId\": 33, \"productName\": \"McAfee DXL Client 6.0.0\", \"objectNotes\": \"\"}, {\"productId\": \"DXLCLNT_META\", \"featureName\": \"McAfee DXL Client\", \"typeName\": \"General\", \"objectName\": \"My Default\", \"typeId\": 17, \"featureId\": \"DXLCLNT_META\", \"objectId\": 35, \"productName\": \"McAfee DXL Client 6.0.0\", \"objectNotes\": \"\"}], \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"datatable_name\": \"mcafee_epo_policies\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 620661, \"timestamp\": \"2022-08-22 11:43:00\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"productId\": {\"type\": \"string\"}, \"featureName\": {\"type\": \"string\"}, \"typeName\": {\"type\": \"string\"}, \"objectName\": {\"type\": \"string\"}, \"typeId\": {\"type\": \"integer\"}, \"featureId\": {\"type\": \"string\"}, \"objectId\": {\"type\": \"integer\"}, \"productName\": {\"type\": \"string\"}, \"objectNotes\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"datatable_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "a8259648-09cc-4d7f-a21a-3a6d455646d3",
      "version": 1,
      "view_items": [
        {
          "content": "4ebc533a-359e-486d-9355-6c2a45a52d02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
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
          "name": "McAfee ePO Find Policies",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_find_policies",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 44
        }
      ]
    },
    {
      "created_date": 1664546133387,
      "description": {
        "content": "Find systems in a specified group on ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Find Systems in Group",
      "export_key": "mcafee_epo_find_systems_in_group",
      "id": 17,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133441,
      "name": "mcafee_epo_find_systems_in_group",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"EPOComputerProperties.ParentID\": 12, \"EPOComputerProperties.ComputerName\": \"SystemA\", \"EPOComputerProperties.Description\": null, \"EPOComputerProperties.ComputerDescription\": null, \"EPOComputerProperties.TimeZone\": \"\", \"EPOComputerProperties.DefaultLangID\": \"\", \"EPOComputerProperties.UserName\": \"\", \"EPOComputerProperties.DomainName\": \"\", \"EPOComputerProperties.IPHostName\": \"\", \"EPOComputerProperties.IPV6\": null, \"EPOComputerProperties.IPAddress\": \"\", \"EPOComputerProperties.IPSubnet\": null, \"EPOComputerProperties.IPSubnetMask\": null, \"EPOComputerProperties.IPV4x\": null, \"EPOComputerProperties.IPXAddress\": \"\", \"EPOComputerProperties.SubnetAddress\": \"\", \"EPOComputerProperties.SubnetMask\": \"\", \"EPOComputerProperties.NetAddress\": \"\", \"EPOComputerProperties.OSType\": \"\", \"EPOComputerProperties.OSVersion\": \"\", \"EPOComputerProperties.OSCsdVersion\": \"\", \"EPOComputerProperties.OSBuildNum\": 0, \"EPOComputerProperties.OSPlatform\": \"\", \"EPOComputerProperties.OSOEMID\": \"\", \"EPOComputerProperties.CPUType\": \"\", \"EPOComputerProperties.CPUSpeed\": 0, \"EPOComputerProperties.NumOfCPU\": 0, \"EPOComputerProperties.CPUSerialNumber\": \"\", \"EPOComputerProperties.TotalPhysicalMemory\": 0, \"EPOComputerProperties.FreeMemory\": 0, \"EPOComputerProperties.FreeDiskSpace\": 0, \"EPOComputerProperties.TotalDiskSpace\": 0, \"EPOComputerProperties.IsPortable\": -1, \"EPOComputerProperties.Vdi\": -1, \"EPOComputerProperties.OSBitMode\": -1, \"EPOComputerProperties.LastAgentHandler\": null, \"EPOComputerProperties.UserProperty1\": null, \"EPOComputerProperties.UserProperty2\": null, \"EPOComputerProperties.UserProperty3\": null, \"EPOComputerProperties.UserProperty4\": null, \"EPOComputerProperties.UserProperty5\": null, \"EPOComputerProperties.UserProperty6\": null, \"EPOComputerProperties.UserProperty7\": null, \"EPOComputerProperties.UserProperty8\": null, \"EPOComputerProperties.Free_Space_of_Drive_C\": 0, \"EPOComputerProperties.Total_Space_of_Drive_C\": 0, \"EPOLeafNode.Tags\": \"\", \"EPOLeafNode.ExcludedTags\": \"\", \"EPOLeafNode.LastUpdate\": null, \"EPOLeafNode.ManagedState\": 0, \"EPOLeafNode.AgentGUID\": null, \"EPOLeafNode.AgentVersion\": null, \"EPOBranchNode.AutoID\": 5}], \"raw\": null, \"inputs\": {\"mcafee_epo_group_id\": 5}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 578, \"timestamp\": \"2022-08-22 11:45:56\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"EPOComputerProperties.ParentID\": {\"type\": \"integer\"}, \"EPOComputerProperties.ComputerName\": {\"type\": \"string\"}, \"EPOComputerProperties.Description\": {}, \"EPOComputerProperties.ComputerDescription\": {}, \"EPOComputerProperties.TimeZone\": {\"type\": \"string\"}, \"EPOComputerProperties.DefaultLangID\": {\"type\": \"string\"}, \"EPOComputerProperties.UserName\": {\"type\": \"string\"}, \"EPOComputerProperties.DomainName\": {\"type\": \"string\"}, \"EPOComputerProperties.IPHostName\": {\"type\": \"string\"}, \"EPOComputerProperties.IPV6\": {}, \"EPOComputerProperties.IPAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.IPSubnet\": {}, \"EPOComputerProperties.IPSubnetMask\": {}, \"EPOComputerProperties.IPV4x\": {}, \"EPOComputerProperties.IPXAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.SubnetAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.SubnetMask\": {\"type\": \"string\"}, \"EPOComputerProperties.NetAddress\": {\"type\": \"string\"}, \"EPOComputerProperties.OSType\": {\"type\": \"string\"}, \"EPOComputerProperties.OSVersion\": {\"type\": \"string\"}, \"EPOComputerProperties.OSCsdVersion\": {\"type\": \"string\"}, \"EPOComputerProperties.OSBuildNum\": {\"type\": \"integer\"}, \"EPOComputerProperties.OSPlatform\": {\"type\": \"string\"}, \"EPOComputerProperties.OSOEMID\": {\"type\": \"string\"}, \"EPOComputerProperties.CPUType\": {\"type\": \"string\"}, \"EPOComputerProperties.CPUSpeed\": {\"type\": \"integer\"}, \"EPOComputerProperties.NumOfCPU\": {\"type\": \"integer\"}, \"EPOComputerProperties.CPUSerialNumber\": {\"type\": \"string\"}, \"EPOComputerProperties.TotalPhysicalMemory\": {\"type\": \"integer\"}, \"EPOComputerProperties.FreeMemory\": {\"type\": \"integer\"}, \"EPOComputerProperties.FreeDiskSpace\": {\"type\": \"integer\"}, \"EPOComputerProperties.TotalDiskSpace\": {\"type\": \"integer\"}, \"EPOComputerProperties.IsPortable\": {\"type\": \"integer\"}, \"EPOComputerProperties.Vdi\": {\"type\": \"integer\"}, \"EPOComputerProperties.OSBitMode\": {\"type\": \"integer\"}, \"EPOComputerProperties.LastAgentHandler\": {}, \"EPOComputerProperties.UserProperty1\": {}, \"EPOComputerProperties.UserProperty2\": {}, \"EPOComputerProperties.UserProperty3\": {}, \"EPOComputerProperties.UserProperty4\": {}, \"EPOComputerProperties.UserProperty5\": {}, \"EPOComputerProperties.UserProperty6\": {}, \"EPOComputerProperties.UserProperty7\": {}, \"EPOComputerProperties.UserProperty8\": {}, \"EPOComputerProperties.Free_Space_of_Drive_C\": {\"type\": \"integer\"}, \"EPOComputerProperties.Total_Space_of_Drive_C\": {\"type\": \"integer\"}, \"EPOLeafNode.Tags\": {\"type\": \"string\"}, \"EPOLeafNode.ExcludedTags\": {\"type\": \"string\"}, \"EPOLeafNode.LastUpdate\": {}, \"EPOLeafNode.ManagedState\": {\"type\": \"integer\"}, \"EPOLeafNode.AgentGUID\": {}, \"EPOLeafNode.AgentVersion\": {}, \"EPOBranchNode.AutoID\": {\"type\": \"integer\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_group_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "0cbf4250-b833-421d-a9be-a36e0d236022",
      "version": 1,
      "view_items": [
        {
          "content": "53bbb755-1c65-48c2-a323-c64ca989de16",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "23690958-a914-48b2-acec-4362f9816641",
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
      "created_date": 1664546133459,
      "description": {
        "content": "Get all of the permission sets on an ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Get All Permission sets",
      "export_key": "mcafee_epo_get_all_permission_sets",
      "id": 18,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133515,
      "name": "mcafee_epo_get_all_permission_sets",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"id\": 4, \"name\": \"Executive Reviewer\"}, {\"id\": 1, \"name\": \"Global Reviewer\"}, {\"id\": 2, \"name\": \"Group Admin\"}, {\"id\": 3, \"name\": \"Group Reviewer\"}], \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 552, \"timestamp\": \"2022-08-02 09:43:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4c45547c-5c2f-4711-90c1-7715706605fc",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
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
          "name": "McAfee ePO Get all Permission Sets",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_all_permission_sets",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 31
        }
      ]
    },
    {
      "created_date": 1664546133534,
      "description": {
        "content": "Get all the users on a ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Get All Users",
      "export_key": "mcafee_epo_get_all_users",
      "id": 19,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133588,
      "name": "mcafee_epo_get_all_users",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [], \"raw\": null, \"inputs\": {\"mcafee_epo_permsetname\": \"Global Reviewer\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 566, \"timestamp\": \"2022-08-11 08:07:14\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_permsetname\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "6b9906aa-5409-44cb-b88b-192c49598d35",
      "version": 1,
      "view_items": [
        {
          "content": "750a2448-13cb-4204-a2ea-2a4e0f1d9dc5",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
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
          "name": "McAfee ePO Get All Users",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_get_all_users",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 28
        }
      ]
    },
    {
      "created_date": 1664546133605,
      "description": {
        "content": "List the issues on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO List Issues",
      "export_key": "mcafee_epo_list_issues",
      "id": 20,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133659,
      "name": "mcafee_epo_list_issues",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"severity\": \"LOW\", \"activityLog\": [{\"date\": \"2022-08-19T06:00:56-07:00\", \"dirty\": true, \"issueId\": 13, \"details\": \"\", \"id\": 17, \"title\": \"Issue Created\", \"username\": \"admin\"}], \"dueDate\": 1661965252000, \"creatorName\": \"admin\", \"description\": \"Test issue creation\", \"ticketServerName\": null, \"priority\": \"MEDIUM\", \"type\": \"issue.type.untyped\", \"resolution\": \"WILLNOTFIX\", \"createdDate\": \"2022-08-19T06:00:56-07:00\", \"assigneeName\": \"Jefferson\", \"subtype\": null, \"name\": \"New issue\", \"assignee\": null, \"id\": 13, \"state\": \"ASSIGNED\", \"ticketId\": null}], \"raw\": null, \"inputs\": {\"incident_id\": 2108, \"datatable_name\": \"mcafee_epo_issues\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 1434, \"timestamp\": \"2022-08-19 09:03:21\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"severity\": {\"type\": \"string\"}, \"activityLog\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"date\": {\"type\": \"string\"}, \"dirty\": {\"type\": \"boolean\"}, \"issueId\": {\"type\": \"integer\"}, \"details\": {\"type\": \"string\"}, \"id\": {\"type\": \"integer\"}, \"title\": {\"type\": \"string\"}, \"username\": {\"type\": \"string\"}}}}, \"dueDate\": {\"type\": \"integer\"}, \"creatorName\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"ticketServerName\": {}, \"priority\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"resolution\": {\"type\": \"string\"}, \"createdDate\": {\"type\": \"string\"}, \"assigneeName\": {\"type\": \"string\"}, \"subtype\": {}, \"name\": {\"type\": \"string\"}, \"assignee\": {}, \"id\": {\"type\": \"integer\"}, \"state\": {\"type\": \"string\"}, \"ticketId\": {}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"datatable_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "e271a8f5-9886-4c2a-8e05-cbca9ed1c632",
      "version": 1,
      "view_items": [
        {
          "content": "050a0e76-1842-47ef-9f3f-5132db7ebe86",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
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
          "name": "McAfee ePO List Issues",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_list_issues",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 20
        }
      ]
    },
    {
      "created_date": 1664546133678,
      "description": {
        "content": "Find all tags specified in ePO",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO List Tags",
      "export_key": "mcafee_epo_list_tags",
      "id": 21,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133733,
      "name": "mcafee_epo_list_tags",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"tagNotes\": \"Default tag for systems identified as a Server\", \"tagId\": 1, \"tagName\": \"Server\"}, {\"tagNotes\": \"Default tag for systems identified as a Workstation\", \"tagId\": 2, \"tagName\": \"Workstation\"}, {\"tagNotes\": \"\", \"tagId\": 3, \"tagName\": \"SOAR\"}, {\"tagNotes\": \"\", \"tagId\": 4, \"tagName\": \"Windows server 2016\"}, {\"tagNotes\": \"\", \"tagId\": 5, \"tagName\": \"Linux\"}, {\"tagNotes\": \"\", \"tagId\": 6, \"tagName\": \"Intel(R) Xeon(R) CPU\"}, {\"tagNotes\": \"\", \"tagId\": 7, \"tagName\": \"Intel Core Processor\"}, {\"tagNotes\": \"\", \"tagId\": 8, \"tagName\": \"Test\"}, {\"tagNotes\": \"\", \"tagId\": 9, \"tagName\": \"AA\"}, {\"tagNotes\": \"\", \"tagId\": 10, \"tagName\": \"123\"}], \"raw\": null, \"inputs\": {}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 580, \"timestamp\": \"2022-07-22 14:03:38\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"tagNotes\": {\"type\": \"string\"}, \"tagId\": {\"type\": \"integer\"}, \"tagName\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\"}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "b9d82be9-83b0-4b88-90ca-7e0d2fb09dc7",
      "version": 1,
      "view_items": [
        {
          "content": "9767f563-47d2-4daf-b353-284342833db8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1f8b5186-4843-473e-a7ef-261488512aad",
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
          "name": "McAfee ePO List Tags",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_list_tags",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 30
        }
      ]
    },
    {
      "created_date": 1664546133751,
      "description": {
        "content": "Remove permission set(s) from an ePO user",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Remove Permission sets from user",
      "export_key": "mcafee_epo_remove_permission_sets_from_user",
      "id": 22,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133807,
      "name": "mcafee_epo_remove_permission_sets_from_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_username\": \"test\", \"mcafee_epo_permsetname\": \"Executive Reviewer\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 584, \"timestamp\": \"2022-08-02 12:46:01\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_username\": {\"type\": \"string\"}, \"mcafee_epo_permsetname\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "85f46ad5-4275-4478-a0f9-1789729d39e5",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "750a2448-13cb-4204-a2ea-2a4e0f1d9dc5",
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
          "name": "McAfee ePO Remove Permission Set from User",
          "object_type": "mcafee_epo_permission_sets",
          "programmatic_name": "mcafee_epo_remove_permission_set_from_user",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 37
        }
      ]
    },
    {
      "created_date": 1664546133825,
      "description": {
        "content": "Remove a tag associated with an ePO system(s).",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Remove Tag",
      "export_key": "mcafee_epo_remove_tag",
      "id": 23,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133888,
      "name": "mcafee_epo_remove_tag",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": 1, \"raw\": null, \"inputs\": {\"mcafee_epo_systems\": \"test_server\", \"mcafee_epo_tag\": \"[u\u0027Workstation\u0027]\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 660, \"timestamp\": \"2022-07-01 12:43:15\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"integer\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_systems\": {\"type\": \"string\"}, \"mcafee_epo_tag\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "1cb1fd7a-0eeb-4230-9edb-c8f6f47b1ae9",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
          "name": "McAfee ePO Remove Tag",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_remove_tag",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 40
        }
      ]
    },
    {
      "created_date": 1664546133908,
      "description": {
        "content": "Delete a user from the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Remove User",
      "export_key": "mcafee_epo_remove_user",
      "id": 24,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546133965,
      "name": "mcafee_epo_remove_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_username\": \"testUser\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 597, \"timestamp\": \"2022-08-11 08:07:17\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_username\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "83c00069-064a-4f1b-b8e5-043d36cb79de",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
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
          "name": "McAfee ePO Remove User",
          "object_type": "mcafee_epo_users",
          "programmatic_name": "mcafee_epo_remove_user",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 23
        }
      ]
    },
    {
      "created_date": 1664546133984,
      "description": {
        "content": "Run a client task on specified system(s)",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Run Client Task",
      "export_key": "mcafee_epo_run_client_task",
      "id": 25,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546134040,
      "name": "mcafee_epo_run_client_task",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": \"Succeeded\", \"raw\": null, \"inputs\": {\"mcafee_epo_product_id\": \"EPOAGENTMETA\", \"mcafee_epo_task_id\": 7, \"mcafee_epo_system_name_or_id\": \"WIN-MTHJTQ4ELBP\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 615, \"timestamp\": \"2022-08-15 08:05:18\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"string\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_product_id\": {\"type\": \"string\"}, \"mcafee_epo_task_id\": {\"type\": \"integer\"}, \"mcafee_epo_system_name_or_id\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "c87c8e6f-71bf-40e4-af85-08d716ed25a1",
      "version": 1,
      "view_items": [
        {
          "content": "1f6f5cd4-cccf-4d78-9cc6-84a6550152c6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b4248da5-f2ca-46fb-a389-e51b4caf2cb7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66fc3d02-6834-487e-b658-ff34c36104e6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bca01f8b-018c-4c48-bebb-b3826e06ee39",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ac9b2c42-34c8-44b7-96b9-753402af3ce8",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8fbb495a-2958-4929-b0b3-ae2b1072e695",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8378be72-9fbd-40f0-813d-84acb6f8b478",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e152d90c-28a4-4480-89e4-a8e5fa3cc33c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d8a5c6fd-0830-45f6-879f-8567ed73d00d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3058b1a0-2f52-4f3c-a61a-7e8c758677f6",
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
          "name": "McAfee ePO Run Client Task",
          "object_type": "mcafee_epo_client_tasks",
          "programmatic_name": "mcafee_epo_run_client_task",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 19
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Run Client Task on System",
          "object_type": "mcafee_epo_systems",
          "programmatic_name": "mcafee_epo_run_client_task_on_system",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 32
        }
      ]
    },
    {
      "created_date": 1664546134059,
      "description": {
        "content": "Update an issue on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Update Issue",
      "export_key": "mcafee_epo_update_issue",
      "id": 26,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546134127,
      "name": "mcafee_epo_update_issue",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": 13, \"raw\": null, \"inputs\": {\"mcafee_epo_issue_name\": null, \"mcafee_epo_issue_properties\": null, \"mcafee_epo_ticket_server_name\": null, \"mcafee_epo_issue_due\": null, \"mcafee_epo_issue_state\": \"Resolved\", \"mcafee_epo_issue_id\": 13, \"mcafee_epo_issue_severity\": null, \"mcafee_epo_issue_description\": null, \"mcafee_epo_issue_assignee\": null, \"mcafee_epo_ticket_id\": null, \"mcafee_epo_issue_priority\": null, \"mcafee_epo_issue_resolution\": \"Fixed\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 576, \"timestamp\": \"2022-08-19 09:05:15\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"integer\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_issue_name\": {}, \"mcafee_epo_issue_properties\": {}, \"mcafee_epo_ticket_server_name\": {}, \"mcafee_epo_issue_due\": {}, \"mcafee_epo_issue_state\": {\"type\": \"string\"}, \"mcafee_epo_issue_id\": {\"type\": \"integer\"}, \"mcafee_epo_issue_severity\": {}, \"mcafee_epo_issue_description\": {}, \"mcafee_epo_issue_assignee\": {}, \"mcafee_epo_ticket_id\": {}, \"mcafee_epo_issue_priority\": {}, \"mcafee_epo_issue_resolution\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "d11a1d48-231a-4c2f-b9a9-f482d785aa23",
      "version": 1,
      "view_items": [
        {
          "content": "050a0e76-1842-47ef-9f3f-5132db7ebe86",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cd420db2-85fa-4b36-836e-b84b08da53d0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e64b4847-576c-41fd-9ebe-30388463d740",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b114ab6f-268c-496f-9fd6-64ae4fc96e10",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "079bf7ef-d3a9-4b0d-9e72-cdcbb4783d01",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9477b98a-5618-40d3-aab3-3c0f2c56ff59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3561f86b-44c7-4c83-9fc5-962bf0231192",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "83a16190-0db4-4b8d-a247-e5918309ff9c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d20dd061-06ce-4daf-8942-92b9b5f745b0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c19dd34-7797-48b2-b2c8-f6279da97148",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8bf4d417-d784-4752-9862-1b3aed4e385d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "06bece11-b70f-4205-9e67-37db3d3f5dda",
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
          "name": "McAfee ePO Update Issue",
          "object_type": "mcafee_epo_issues",
          "programmatic_name": "mcafee_epo_update_issue",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 41
        }
      ]
    },
    {
      "created_date": 1664546134149,
      "description": {
        "content": "Update a user on the ePO server",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Update User",
      "export_key": "mcafee_epo_update_user",
      "id": 27,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546134207,
      "name": "mcafee_epo_update_user",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": true, \"raw\": null, \"inputs\": {\"mcafee_epo_email\": \"jefferson@example.com\", \"mcafee_epo_user_disabled\": false, \"mcafee_epo_windowsdomain\": null, \"mcafee_epo_admin\": false, \"mcafee_epo_windowsusername\": null, \"mcafee_epo_allowed_ips\": null, \"mcafee_epo_pass\": null, \"mcafee_epo_phone_number\": \"7930445234\", \"mcafee_epo_username\": \"jeff\", \"mcafee_epo_new_username\": \"jefferson\", \"mcafee_epo_notes\": \"This is Jeffersons account\", \"mcafee_epo_fullname\": \"Jefferson Greg\", \"mcafee_epo_subjectdn\": null}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 609, \"timestamp\": \"2022-08-10 13:53:43\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"boolean\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_email\": {\"type\": \"string\"}, \"mcafee_epo_user_disabled\": {\"type\": \"boolean\"}, \"mcafee_epo_windowsdomain\": {}, \"mcafee_epo_admin\": {\"type\": \"boolean\"}, \"mcafee_epo_windowsusername\": {}, \"mcafee_epo_allowed_ips\": {}, \"mcafee_epo_pass\": {}, \"mcafee_epo_phone_number\": {\"type\": \"string\"}, \"mcafee_epo_username\": {\"type\": \"string\"}, \"mcafee_epo_new_username\": {\"type\": \"string\"}, \"mcafee_epo_notes\": {\"type\": \"string\"}, \"mcafee_epo_fullname\": {\"type\": \"string\"}, \"mcafee_epo_subjectdn\": {}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "a45c768a-d8d0-4666-a002-b7ddf6624fe6",
      "version": 1,
      "view_items": [
        {
          "content": "38fb4df9-f658-48d9-9f41-594c053337e2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f94eb163-9184-4f4b-97e3-8ca127b2a157",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "74a73043-5370-4b64-bdcc-182e6f445b67",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "29fe75c0-8120-42d4-b3e3-b1240754ddbd",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "353a1329-c745-49ab-9178-ee94c279b2e7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80101eb8-577d-4737-95ad-d7db6effcc57",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "83ad827d-a6bd-44d7-892b-fd28a3efa1d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c659cdce-1d9e-4e19-8e4b-07eb3756960a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0ff2c2b8-89ac-451c-bdb2-ecd83588e9f7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f824010c-151e-4ff1-8062-6f770997f544",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "bd4da808-aeba-45a0-b327-f06dc90b9709",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9d0751be-e063-411c-b04a-57f1b9d24407",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c591bd91-9f03-44e7-a012-c766f6df6715",
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
          "name": "McAfee ePO Update User",
          "object_type": "mcafee_epo_users",
          "programmatic_name": "mcafee_epo_update_user",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 38
        }
      ]
    },
    {
      "created_date": 1664546134227,
      "description": {
        "content": "Wake up an ePO agent",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee ePO Wake up agent",
      "export_key": "mcafee_epo_wake_up_agent",
      "id": 28,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546134293,
      "name": "mcafee_epo_wake_up_agent",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": \"completed: 1\\nfailed: 0\\nexpired: 0\", \"raw\": null, \"inputs\": {\"mcafee_epo_systems\": \"WIN-MTHJTQ4ELBP\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 25666, \"timestamp\": \"2022-07-25 08:43:47\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"string\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_systems\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "a8b3bef5-36fc-4d69-b366-6fd3def996d2",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
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
          "name": "McAfee ePO Wake up Agent",
          "object_type": "incident",
          "programmatic_name": "mcafee_epo_wake_up_agent",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 25
        }
      ]
    },
    {
      "created_date": 1664546134314,
      "description": {
        "content": "Applies tag to the systems in ePO. Inputs include:\n- mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.\n- mcafee_epo_tag: A tag managed on ePO.",
        "format": "text"
      },
      "destination_handle": "mcafee_epo_message_destination",
      "display_name": "McAfee Tag an ePO Asset",
      "export_key": "mcafee_tag_an_epo_asset",
      "id": 29,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 14,
        "name": "b@example.com",
        "type": "user"
      },
      "last_modified_time": 1664546134373,
      "name": "mcafee_tag_an_epo_asset",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": 1, \"raw\": null, \"inputs\": {\"mcafee_epo_systems\": \"test_server\", \"mcafee_epo_tag\": \"[u\u0027Workstation\u0027]\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-mcafee-epo\", \"package_version\": \"1.1.0\", \"host\": \"local\", \"execution_time_ms\": 596, \"timestamp\": \"2022-07-01 12:42:07\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"integer\"}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"mcafee_epo_systems\": {\"type\": \"string\"}, \"mcafee_epo_tag\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "67c5b852-f38f-40f7-8a68-1ae8e8a78549",
      "version": 1,
      "view_items": [
        {
          "content": "bf25606e-96aa-4328-aa15-1cd5a8b8dc02",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "134bfbe6-821d-4c29-9492-d594c38125d7",
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
          "name": "McAfee ePO Apply a Tag",
          "object_type": "mcafee_epo_tags",
          "programmatic_name": "mcafee_epo_apply_a_tag",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 17
        },
        {
          "actions": [],
          "description": null,
          "name": "McAfee ePO Apply Tags",
          "object_type": "artifact",
          "programmatic_name": "mcafee_epo_apply_tags",
          "tags": [
            {
              "tag_handle": "fn_mcafee_epo",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 36
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 7,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1664811037319,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1664811037319,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "a1993591-6f2f-4a09-9fc7-8eaf1945768c"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "mcafee_epo_message_destination",
      "name": "McAfee ePO Message Destination",
      "programmatic_name": "mcafee_epo_message_destination",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "users": [],
      "uuid": "b0a31bf9-305f-4120-a5e6-aab5a965cac6"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 7585,
    "major": 44,
    "minor": 0,
    "version": "44.0.7585"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "McAfee ePO Client Tasks",
      "export_key": "mcafee_epo_client_tasks",
      "fields": {
        "object_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_client_tasks/object_name",
          "hide_notification": false,
          "id": 1202,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "object_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Object Name",
          "tooltip": "Name of the client task",
          "type_id": 1009,
          "uuid": "93178ed6-513c-4c4d-b1e3-6359cce6d3b5",
          "values": [],
          "width": 175
        },
        "product_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_client_tasks/product_id",
          "hide_notification": false,
          "id": 1203,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "product_id",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Product ID",
          "tooltip": "ID for the product",
          "type_id": 1009,
          "uuid": "ca19a865-d1cc-4b07-bce6-7bbaa164c29c",
          "values": [],
          "width": 153
        },
        "product_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_client_tasks/product_name",
          "hide_notification": false,
          "id": 1204,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "product_name",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Product Name",
          "tooltip": "Name of the product associated with the client task",
          "type_id": 1009,
          "uuid": "e809fd12-a34a-4ece-870a-235b0d0d4964",
          "values": [],
          "width": 189
        },
        "task_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_client_tasks/task_id",
          "hide_notification": false,
          "id": 1205,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "task_id",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Task ID",
          "tooltip": "ID for the task",
          "type_id": 1009,
          "uuid": "b7915e57-dfbe-4140-b9b0-4a00ecb1b171",
          "values": [],
          "width": 50
        },
        "type_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_client_tasks/type_name",
          "hide_notification": false,
          "id": 1206,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type Name",
          "tooltip": "Type of client task",
          "type_id": 1009,
          "uuid": "9da657fd-ff26-42c6-8c75-63c5b48107d4",
          "values": [],
          "width": 157
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_client_tasks",
      "uuid": "59880177-40ca-43c7-9b0c-576377bad687"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Groups",
      "export_key": "mcafee_epo_groups",
      "fields": {
        "group_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_groups/group_id",
          "hide_notification": false,
          "id": 1207,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "group_id",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Group ID",
          "tooltip": "ID of the group",
          "type_id": 1010,
          "uuid": "2de87667-95f3-4320-a85a-da3c5b627f97",
          "values": [],
          "width": 218
        },
        "group_path": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_groups/group_path",
          "hide_notification": false,
          "id": 1208,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "group_path",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Group Path",
          "tooltip": "Path to the group on the ePO server",
          "type_id": 1010,
          "uuid": "db3dc49e-1ef6-45c3-a2ff-2410a30b06ae",
          "values": [],
          "width": 254
        },
        "systems": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_groups/systems",
          "hide_notification": false,
          "id": 1209,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "systems",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Systems",
          "tooltip": "Name of the systems in the group",
          "type_id": 1010,
          "uuid": "21d97c6d-690e-4ccf-8509-4988debe3d1a",
          "values": [],
          "width": 209
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_groups",
      "uuid": "93b7e7d5-e9b9-481c-8fc2-f923d311bb42"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Issues",
      "export_key": "mcafee_epo_issues",
      "fields": {
        "assignee_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/assignee_name",
          "hide_notification": false,
          "id": 1210,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "assignee_name",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Assignee Name",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "4a8f45ad-3965-4105-9e11-29d8d3491fbe",
          "values": [],
          "width": 121
        },
        "issue_deleted": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_deleted",
          "hide_notification": false,
          "id": 1211,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "issue_deleted",
          "operation_perms": {},
          "operations": [],
          "order": 12,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Deleted",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "64b21505-7a73-4e95-a689-d9ade553d6f5",
          "values": [],
          "width": 59
        },
        "issue_description": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_description",
          "hide_notification": false,
          "id": 1212,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "issue_description",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Description",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "4dd43761-38a6-475a-b8c3-c40f01f6e5a3",
          "values": [],
          "width": 121
        },
        "issue_due_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_due_date",
          "hide_notification": false,
          "id": 1213,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "issue_due_date",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Due Date",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "bfe6b839-dd5b-4a0d-b6e2-dbf991d5500a",
          "values": [],
          "width": 71
        },
        "issue_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_id",
          "hide_notification": false,
          "id": 1214,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "issue_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Issue ID",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "dea02fe3-a5a8-4d77-bbe4-90f2743e5af4",
          "values": [],
          "width": 70
        },
        "issue_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_name",
          "hide_notification": false,
          "id": 1215,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "issue_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Issue Name",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "dae3b587-0ece-4704-905b-e0562e18a8b6",
          "values": [],
          "width": 106
        },
        "issue_state": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/issue_state",
          "hide_notification": false,
          "id": 1216,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "issue_state",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "State",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "865c78bc-2cf2-46b3-86e3-28547729a579",
          "values": [],
          "width": 40
        },
        "priority": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/priority",
          "hide_notification": false,
          "id": 1217,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "priority",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Priority",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "b6ddf514-db11-47e1-98ec-54c9625c3bb6",
          "values": [],
          "width": 57
        },
        "resolution": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/resolution",
          "hide_notification": false,
          "id": 1218,
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
          "type_id": 1011,
          "uuid": "e0476262-9839-4cb1-9239-8e00b74ff0b4",
          "values": [],
          "width": 81
        },
        "severity": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/severity",
          "hide_notification": false,
          "id": 1219,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "severity",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Severity",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "22c28e9b-78cc-4f64-b209-29943f6e2554",
          "values": [],
          "width": 69
        },
        "ticket_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/ticket_id",
          "hide_notification": false,
          "id": 1220,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_id",
          "operation_perms": {},
          "operations": [],
          "order": 11,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket ID",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "7e9da847-7728-4d2e-a510-7322d23fa982",
          "values": [],
          "width": 70
        },
        "ticket_server_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/ticket_server_name",
          "hide_notification": false,
          "id": 1221,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ticket_server_name",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Ticket Server Name",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "65e95335-7ec2-456a-8db6-b77483571bbf",
          "values": [],
          "width": 151
        },
        "type": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_issues/type",
          "hide_notification": false,
          "id": 1222,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type",
          "tooltip": "",
          "type_id": 1011,
          "uuid": "88b48c83-1118-4c92-9973-3e0d1d73a96a",
          "values": [],
          "width": 36
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_issues",
      "uuid": "ff2050da-0a2f-4294-b916-60b24fb8f3df"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Permission sets",
      "export_key": "mcafee_epo_permission_sets",
      "fields": {
        "permission_set_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_permission_sets/permission_set_name",
          "hide_notification": false,
          "id": 1223,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "permission_set_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Permission Set Name",
          "tooltip": "",
          "type_id": 1012,
          "uuid": "5f787b3b-1acd-40f6-9268-a20f47bed288",
          "values": [],
          "width": 495
        },
        "users": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_permission_sets/users",
          "hide_notification": false,
          "id": 1224,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "users",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Users",
          "tooltip": "Users that have the permission set",
          "type_id": 1012,
          "uuid": "9fc75e0d-663d-4365-81f3-17d697664569",
          "values": [],
          "width": 151
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_permission_sets",
      "uuid": "4f73d778-eb04-466d-867b-717539383bce"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Policies",
      "export_key": "mcafee_epo_policies",
      "fields": {
        "object_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/object_id",
          "hide_notification": false,
          "id": 1225,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "object_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Object ID",
          "tooltip": "ID of the policy",
          "type_id": 1013,
          "uuid": "aa1bb5ed-dfd2-4218-bd80-4221d5fe4634",
          "values": [],
          "width": 74
        },
        "object_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/object_name",
          "hide_notification": false,
          "id": 1226,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "object_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Object Name",
          "tooltip": "Name of the policy",
          "type_id": 1013,
          "uuid": "61811680-b221-4f08-ad65-b9059352c740",
          "values": [],
          "width": 118
        },
        "object_notes": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/object_notes",
          "hide_notification": false,
          "id": 1227,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "object_notes",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Object Notes",
          "tooltip": "Notes for the policy",
          "type_id": 1013,
          "uuid": "435c7d4b-403d-43c4-90eb-27b3cf01dfd9",
          "values": [],
          "width": 500
        },
        "product_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/product_id",
          "hide_notification": false,
          "id": 1228,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "product_id",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Product ID",
          "tooltip": "ID of the product",
          "type_id": 1013,
          "uuid": "f78db4ae-b369-4af1-9eca-5e920879fe0f",
          "values": [],
          "width": 102
        },
        "systems": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/systems",
          "hide_notification": false,
          "id": 1229,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "systems",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Systems",
          "tooltip": "Systems assigned to the policy",
          "type_id": 1013,
          "uuid": "e3d77afc-5692-402c-a576-999c973c2296",
          "values": [],
          "width": 76
        },
        "type_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/type_id",
          "hide_notification": false,
          "id": 1230,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "type_id",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type ID",
          "tooltip": "ID of the type of policy",
          "type_id": 1013,
          "uuid": "16920895-82fd-41d9-a19a-8d4b7c62f34e",
          "values": [],
          "width": 61
        },
        "type_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_policies/type_name",
          "hide_notification": false,
          "id": 1231,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "type_name",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Type Name",
          "tooltip": "Name of the type of policy",
          "type_id": 1013,
          "uuid": "ac6b5e2b-05fa-44d5-8e39-094b568b07ce",
          "values": [],
          "width": 86
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_policies",
      "uuid": "2c794f33-998d-4dcd-8435-080342ef1a82"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Systems",
      "export_key": "mcafee_epo_systems",
      "fields": {
        "agent_guid": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/agent_guid",
          "hide_notification": false,
          "id": 1232,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "agent_guid",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Agent GUID",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "4a06727d-bb13-4420-a42a-05f1fa2233fc",
          "values": [],
          "width": 205
        },
        "deleted": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/deleted",
          "hide_notification": false,
          "id": 1233,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "deleted",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Deleted",
          "tooltip": "If the System is deleted or not",
          "type_id": 1014,
          "uuid": "d88bd8b7-af58-42dd-bc4e-fa31bdab3a84",
          "values": [],
          "width": 59
        },
        "last_communication": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/last_communication",
          "hide_notification": false,
          "id": 1234,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "last_communication",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Last Communication",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "629ce5ec-9804-49f9-8258-e02d9f6b180e",
          "values": [],
          "width": 200
        },
        "operating_system": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/operating_system",
          "hide_notification": false,
          "id": 1235,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "operating_system",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Operating System",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "5fed4e04-aa48-4620-a7d1-efc767294217",
          "values": [],
          "width": 198
        },
        "system_name": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/system_name",
          "hide_notification": false,
          "id": 1236,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "system_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "System Name",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "2c589a6e-c182-4235-9653-7e88c1b2eac4",
          "values": [],
          "width": 152
        },
        "tags": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_systems/tags",
          "hide_notification": false,
          "id": 1237,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "tags",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tags",
          "tooltip": "",
          "type_id": 1014,
          "uuid": "0efaf908-600a-482b-ae10-8466a0488b74",
          "values": [],
          "width": 200
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_systems",
      "uuid": "7d08345f-56d9-4138-93bd-43c645e09a27"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO tags",
      "export_key": "mcafee_epo_tags",
      "fields": {
        "epo_id": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_id",
          "hide_notification": false,
          "id": 1238,
          "input_type": "number",
          "internal": false,
          "is_tracked": false,
          "name": "epo_id",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Id",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "565bbe14-2671-442e-9f9c-1fd9cdc82dd5",
          "values": [],
          "width": 35
        },
        "epo_notes": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_notes",
          "hide_notification": false,
          "id": 1239,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "epo_notes",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Notes",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "bf2dc924-ab97-40fe-abba-3e395d175323",
          "values": [],
          "width": 490
        },
        "epo_tag": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_tags/epo_tag",
          "hide_notification": false,
          "id": 1240,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "epo_tag",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "required": "always",
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tag",
          "tooltip": "",
          "type_id": 1015,
          "uuid": "033ee0aa-d253-47c1-976e-0bcfbce40f46",
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_tags",
      "uuid": "b40555f7-9353-447e-b4c3-2ac166936dfa"
    },
    {
      "actions": [],
      "display_name": "McAfee ePO Users",
      "export_key": "mcafee_epo_users",
      "fields": {
        "admin": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/admin",
          "hide_notification": false,
          "id": 1241,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "admin",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Admin",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "a93f7791-1434-4039-af77-5f168b277358",
          "values": [],
          "width": 49
        },
        "allowed_ips": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/allowed_ips",
          "hide_notification": false,
          "id": 1242,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "allowed_ips",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Allowed IPs",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "ccadefac-141f-467f-80f8-2f737f75f729",
          "values": [],
          "width": 111
        },
        "disabled": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/disabled",
          "hide_notification": false,
          "id": 1243,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "disabled",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Disabled",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "52f87819-f180-4c73-a9da-a9ee792d8106",
          "values": [],
          "width": 67
        },
        "email": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/email",
          "hide_notification": false,
          "id": 1244,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "email",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Email",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "f75d189b-54b1-4866-99ab-494d35fb5463",
          "values": [],
          "width": 82
        },
        "full_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/full_name",
          "hide_notification": false,
          "id": 1245,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "full_name",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Full Name",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "d907a966-84e5-44b4-b67d-68bd2a0b8984",
          "values": [],
          "width": 99
        },
        "notes": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/notes",
          "hide_notification": false,
          "id": 1246,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "notes",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Notes",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "063a6b3b-73ab-458b-8855-ed8aca82c7f9",
          "values": [],
          "width": 94
        },
        "phone_number": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/phone_number",
          "hide_notification": false,
          "id": 1247,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "phone_number",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Phone Number",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "c9638dca-a693-47f6-a616-cd31d8c4d366",
          "values": [],
          "width": 144
        },
        "user_deleted": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/user_deleted",
          "hide_notification": false,
          "id": 1248,
          "input_type": "boolean",
          "internal": false,
          "is_tracked": false,
          "name": "user_deleted",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User Deleted",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "3cbbe5b4-e52c-4b1f-89a1-197c86f3e16e",
          "values": [],
          "width": 59
        },
        "user_name": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "mcafee_epo_users/user_name",
          "hide_notification": false,
          "id": 1249,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "user_name",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User Name",
          "tooltip": "",
          "type_id": 1016,
          "uuid": "67c46a44-701f-4af9-b90c-14482e92415c",
          "values": [],
          "width": 179
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
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "mcafee_epo_users",
      "uuid": "53bbe7d2-f7e4-4fe7-9d6c-c3cb42410d24"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_add_system",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_add_system\" isExecutable=\"true\" name=\"McAfee ePO Add System\"\u003e\u003cdocumentation\u003eAdd a system to the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_111dlh8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_01a7t9n\" name=\"McAfee ePO Add System\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b30f5c25-c4f3-49ed-ba15-fe4d82c71249\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  row = incident.addRow(\\\"mcafee_epo_systems\\\")\\n  row[\\\"system_name\\\"] = rule.properties.epo_system_names_or_ids\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"# Required\\ninputs.mcafee_epo_group_id = rule.properties.epo_group_id\\ninputs.mcafee_epo_system_name_or_id = rule.properties.epo_system_names_or_ids\\n\\n# Optional\\ninputs.mcafee_epo_allow_duplicates = rule.properties.epo_allow_duplicates\\ninputs.mcafee_epo_delete_if_removed = rule.properties.epo_delete_if_removed\\ninputs.mcafee_epo_flatten_tree_structure = rule.properties.epo_flatten_tree_structure\\ninputs.mcafee_epo_push_agent = rule.properties.epo_push_agent\\ninputs.mcafee_epo_push_agent_domain_name = rule.properties.epo_push_agent_domain_name\\ninputs.mcafee_epo_push_agent_force_install = rule.properties.epo_push_agent_force_install\\ninputs.mcafee_epo_push_agent_package_path = rule.properties.epo_push_agent_package_path\\ninputs.mcafee_epo_push_agent_password = rule.properties.epo_push_agent_password\\ninputs.mcafee_epo_push_agent_skip_if_installed = rule.properties.epo_push_agent_skip_if_installed\\ninputs.mcafee_epo_push_agent_suppress_ui = rule.properties.epo_push_agent_suppress_ui\\ninputs.mcafee_epo_push_agent_username = rule.properties.epo_push_agent_user_name\\ninputs.mcafee_epo_uninstall = rule.properties.epo_uninstall_removed\\ninputs.mcafee_epo_push_agent_install_path = rule.properties.epo_push_agent_install_path\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_111dlh8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nh3lzk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_111dlh8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01a7t9n\"/\u003e\u003cendEvent id=\"EndEvent_0pomcxg\"\u003e\u003cincoming\u003eSequenceFlow_1nh3lzk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1nh3lzk\" sourceRef=\"ServiceTask_01a7t9n\" targetRef=\"EndEvent_0pomcxg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01a7t9n\" id=\"ServiceTask_01a7t9n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_111dlh8\" id=\"SequenceFlow_111dlh8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0pomcxg\" id=\"EndEvent_0pomcxg_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"377\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"395\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nh3lzk\" id=\"SequenceFlow_1nh3lzk_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"362\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Add a system to the ePO server",
      "export_key": "mcafee_epo_add_system",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546135211,
      "name": "McAfee ePO Add System",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_add_system",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "b9a75cbb-a2f5-438e-bc0f-960169957e26",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_assign_policy_to_group_from_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_assign_policy_to_group_from_group\" isExecutable=\"true\" name=\"McAfee ePO Assign Policy to Group from Group\"\u003e\u003cdocumentation\u003eAssign a policy to a specified group on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ghv1cj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_01m5snh\" name=\"McAfee ePO Assign Policy to Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4dc3b4db-1f72-4b4e-b7e0-c5996f743697\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"Policy: \u0027{}\u0027 Assigned to Group: \u0027{}\u0027\\\".format(rule.properties.epo_policy_id, row.group_id))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_group_id = row.group_id\\ninputs.mcafee_epo_object_id = rule.properties.epo_policy_id\\ninputs.mcafee_epo_product_id = rule.properties.epo_product_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ghv1cj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dwu680\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ghv1cj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_01m5snh\"/\u003e\u003cendEvent id=\"EndEvent_01u2wh9\"\u003e\u003cincoming\u003eSequenceFlow_1dwu680\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1dwu680\" sourceRef=\"ServiceTask_01m5snh\" targetRef=\"EndEvent_01u2wh9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_01m5snh\" id=\"ServiceTask_01m5snh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"244\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ghv1cj\" id=\"SequenceFlow_0ghv1cj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"244\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"221\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01u2wh9\" id=\"EndEvent_01u2wh9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"377\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"395\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dwu680\" id=\"SequenceFlow_1dwu680_di\"\u003e\u003comgdi:waypoint x=\"344\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"377\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"360.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Assign a policy to a specified group on the ePO server",
      "export_key": "mcafee_epo_assign_policy_to_group_from_group",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136124,
      "name": "McAfee ePO Assign Policy to Group from Group",
      "object_type": "mcafee_epo_groups",
      "programmatic_name": "mcafee_epo_assign_policy_to_group_from_group",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "23668311-532e-4115-a33c-28571437ef7d",
      "workflow_id": 24
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "mcafee_epo_create_issue",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_create_issue\" isExecutable=\"true\" name=\"McAfee ePO Create Issue\"\u003e\u003cdocumentation\u003eCreate an issue on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10o1umi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1cp3l20\" name=\"McAfee ePO Create Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8bbcc714-05ce-4894-bd65-9f5daff302e5\"\u003e{\"inputs\":{\"4daa5700-47bc-4a1d-9e4d-1d32fe202286\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"fa68645e-e98b-4ba0-9ff6-f3bff26f20a4\"}},\"b114ab6f-268c-496f-9fd6-64ae4fc96e10\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"10234f71-637e-4dd6-906a-19e32ef335ca\"}},\"079bf7ef-d3a9-4b0d-9e72-cdcbb4783d01\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"026f887f-61d5-4806-9c17-4fadddc2d58f\"}},\"9477b98a-5618-40d3-aab3-3c0f2c56ff59\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"b5611556-6d46-4755-9aab-38c72c55ad8d\"}},\"3561f86b-44c7-4c83-9fc5-962bf0231192\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7a9a788f-93c6-4575-bdb0-d22f9823624f\"}}},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  row = incident.addRow(\\\"mcafee_epo_issues\\\")\\n  row[\\\"issue_name\\\"] = rule.properties.epo_issue_name\\n  row[\\\"issue_id\\\"] = results.get(\\\"content\\\")\\n  row[\\\"severity\\\"] = rule.properties.epo_issue_severity\\n  row[\\\"issue_due_date\\\"] = rule.properties.epo_issue_due\\n  row[\\\"issue_description\\\"] = rule.properties.epo_issue_description\\n  row[\\\"ticket_server_name\\\"] = rule.properties.epo_ticket_server_name\\n  row[\\\"priority\\\"] = rule.properties.epo_issue_priority\\n  row[\\\"type\\\"] = rule.properties.epo_issue_type\\n  row[\\\"resolution\\\"] = rule.properties.epo_issue_resolution\\n  row[\\\"assignee_name\\\"] =rule.properties.epo_issue_assignee\\n  row[\\\"issue_state\\\"] = rule.properties.epo_issue_state\\n  row[\\\"ticket_id\\\"] = rule.properties.epo_ticket_id\\n  row[\\\"issue_deleted\\\"] = False\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_issue_assignee = rule.properties.epo_issue_assignee\\ninputs.mcafee_epo_issue_description = rule.properties.epo_issue_description\\ninputs.mcafee_epo_issue_due = rule.properties.epo_issue_due\\ninputs.mcafee_epo_issue_name = rule.properties.epo_issue_name\\ninputs.mcafee_epo_issue_priority = rule.properties.epo_issue_priority\\ninputs.mcafee_epo_issue_properties = rule.properties.epo_issue_properties\\ninputs.mcafee_epo_issue_resolution = rule.properties.epo_issue_resolution\\ninputs.mcafee_epo_issue_severity = rule.properties.epo_issue_severity\\ninputs.mcafee_epo_issue_state = rule.properties.epo_issue_state\\ninputs.mcafee_epo_ticket_id = rule.properties.epo_ticket_id\\ninputs.mcafee_epo_ticket_server_name = rule.properties.epo_ticket_server_name\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10o1umi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0223vif\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10o1umi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1cp3l20\"/\u003e\u003cendEvent id=\"EndEvent_1aztrov\"\u003e\u003cincoming\u003eSequenceFlow_0223vif\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0223vif\" sourceRef=\"ServiceTask_1cp3l20\" targetRef=\"EndEvent_1aztrov\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1cp3l20\" id=\"ServiceTask_1cp3l20_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"248\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10o1umi\" id=\"SequenceFlow_10o1umi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"220\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"220\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"248\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"235\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1aztrov\" id=\"EndEvent_1aztrov_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"367\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0223vif\" id=\"SequenceFlow_0223vif_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"357.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Create an issue on the ePO server",
      "export_key": "mcafee_epo_create_issue",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664808768099,
      "name": "McAfee ePO Create Issue",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_create_issue",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4d03c2a3-7a71-422a-b2a6-518c33bf885a",
      "workflow_id": 22
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_add_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_add_user\" isExecutable=\"true\" name=\"McAfee ePO Add User\"\u003e\u003cdocumentation\u003eAdd a user to the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dsuw3n\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1yyfkii\" name=\"McAfee ePO Add User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0d34aa89-8ebf-4c17-9c7f-4ea851c37a82\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"User: {} successfully created.\\\".format(rule.properties.epo_username))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_username = rule.properties.epo_username\\ninputs.mcafee_epo_pass = rule.properties.epo_user_password\\ninputs.mcafee_epo_admin = rule.properties.epo_admin\\ninputs.mcafee_epo_allowed_ips = rule.properties.epo_allowed_ips\\ninputs.mcafee_epo_email = rule.properties.epo_email\\ninputs.mcafee_epo_fullname = rule.properties.epo_full_name\\ninputs.mcafee_epo_notes = rule.properties.epo_notes\\ninputs.mcafee_epo_phone_number = rule.properties.epo_phone_number\\ninputs.mcafee_epo_user_disabled = rule.properties.epo_user_disbabled\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dsuw3n\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1945ef3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dsuw3n\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1yyfkii\"/\u003e\u003cendEvent id=\"EndEvent_09we1qu\"\u003e\u003cincoming\u003eSequenceFlow_1945ef3\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1945ef3\" sourceRef=\"ServiceTask_1yyfkii\" targetRef=\"EndEvent_09we1qu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1yyfkii\" id=\"ServiceTask_1yyfkii_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"243\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dsuw3n\" id=\"SequenceFlow_0dsuw3n_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09we1qu\" id=\"EndEvent_09we1qu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"380\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"398\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1945ef3\" id=\"SequenceFlow_1945ef3_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"380\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"361.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Add a user to the ePO server",
      "export_key": "mcafee_epo_add_user",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546134621,
      "name": "McAfee ePO Add User",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_add_user",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4cdec2ee-a728-47cd-9f64-d5bdcd1a16e1",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_assign_policy_to_system_from_system",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_assign_policy_to_system_from_system\" isExecutable=\"true\" name=\"McAfee ePO Assign Policy to System from System\"\u003e\u003cdocumentation\u003eAssign policy to system\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ekk3db\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cu6u4n\" name=\"McAfee ePO Assign Policy to Syste...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"81575bf7-1c92-45d0-a674-4682f9e735c7\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"Policy: \u0027{}\u0027 Assigned to system: \u0027{}\u0027\\\".format(rule.properties.epo_policy_id, row.system_name))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_system_name_or_id = row.system_name\\ninputs.mcafee_epo_product_id = rule.properties.epo_product_id\\ninputs.mcafee_epo_type_id = rule.properties.epo_policy_type_id\\ninputs.mcafee_epo_object_id = rule.properties.epo_policy_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ekk3db\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0l6rmtm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ekk3db\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cu6u4n\"/\u003e\u003cendEvent id=\"EndEvent_1goc8qo\"\u003e\u003cincoming\u003eSequenceFlow_0l6rmtm\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0l6rmtm\" sourceRef=\"ServiceTask_0cu6u4n\" targetRef=\"EndEvent_1goc8qo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cu6u4n\" id=\"ServiceTask_0cu6u4n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ekk3db\" id=\"SequenceFlow_1ekk3db_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1goc8qo\" id=\"EndEvent_1goc8qo_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"367\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l6rmtm\" id=\"SequenceFlow_0l6rmtm_di\"\u003e\u003comgdi:waypoint x=\"336\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"351.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Assign policy to system",
      "export_key": "mcafee_epo_assign_policy_to_system_from_system",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138844,
      "name": "McAfee ePO Assign Policy to System from System",
      "object_type": "mcafee_epo_systems",
      "programmatic_name": "mcafee_epo_assign_policy_to_system_from_system",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "5b385b2c-15f2-450f-92a8-e92b55aef183",
      "workflow_id": 42
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_remove_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_remove_user\" isExecutable=\"true\" name=\"McAfee ePO Remove User\"\u003e\u003cdocumentation\u003eDelete a user from the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dwph4o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0f1tt7g\" name=\"McAfee ePO Remove User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"83c00069-064a-4f1b-b8e5-043d36cb79de\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  row.user_deleted = True\\n  incident.addNote(\\\"User: {} removed  from ePO server\\\".format(row.user_name))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_username = row.user_name\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dwph4o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f5f6l1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dwph4o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0f1tt7g\"/\u003e\u003cendEvent id=\"EndEvent_048zj27\"\u003e\u003cincoming\u003eSequenceFlow_0f5f6l1\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0f5f6l1\" sourceRef=\"ServiceTask_0f1tt7g\" targetRef=\"EndEvent_048zj27\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0f1tt7g\" id=\"ServiceTask_0f1tt7g_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"234\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dwph4o\" id=\"SequenceFlow_0dwph4o_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"234\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_048zj27\" id=\"EndEvent_048zj27_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"360\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"378\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f5f6l1\" id=\"SequenceFlow_0f5f6l1_di\"\u003e\u003comgdi:waypoint x=\"334\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"347\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Delete a user from the ePO server",
      "export_key": "mcafee_epo_remove_user",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546135959,
      "name": "McAfee ePO Remove User",
      "object_type": "mcafee_epo_users",
      "programmatic_name": "mcafee_epo_remove_user",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "f2ae9b69-d635-4abf-8114-6999c38ca624",
      "workflow_id": 23
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_find_all_groups",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_find_all_groups\" isExecutable=\"true\" name=\"McAfee ePO Find All Groups\"\u003e\u003cdocumentation\u003eFind all the groups on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1ihnfbs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1qxadyp\" name=\"McAfee ePO Find Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"cec9d0f8-06bc-4168-9fec-554d2fef8a99\"\u003e{\"inputs\":{},\"post_processing_script\":\"# if results.get(\\\"success\\\"):\\n#   for x in results.get(\\\"content\\\"):\\n#     table = incident.addRow(\\\"mcafee_epo_groups\\\")\\n#     table[\\\"group_id\\\"] = int(x.get(\\\"groupId\\\"))\\n#     table[\\\"group_path\\\"] = x.get(\\\"groupPath\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"groupsresults\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ihnfbs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o0xami\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ihnfbs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qxadyp\"/\u003e\u003cserviceTask id=\"ServiceTask_1xcirqt\" name=\"McAfee ePO Execute Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a78912f-473f-4eaf-86b3-05dc87c5e14a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for groupInfo in workflow.properties.groupsresults.get(\\\"content\\\"):\\n    groupPath = groupInfo.get(\\\"groupPath\\\")\\n    table = incident.addRow(\\\"mcafee_epo_groups\\\")\\n    table[\\\"group_id\\\"] = int(groupInfo.get(\\\"groupId\\\"))\\n    table[\\\"group_path\\\"] = groupPath\\n    systems = \\\"\\\"\\n    for group in results.get(\\\"content\\\"):\\n      # EPOBranchNode.NodeTextPath2 only returns path after My Organization\\n      path2 = group.get(\\\"EPOBranchNode.NodeTextPath2\\\")\\n      # EPOBranchNode.NodeTextPath2 returns the path, Lost and Found, as, Lost\u0026amp;Found,\\n      # so it needs to be converted in order to compare paths.\\n      path2 = path2.replace(\\\"Lost\u0026amp;Found\\\", \\\"Lost and Found\\\")\\n      # Add, My Organization, to the begining of the path\\n      path2 = \\\"My Organization{}\\\".format(path2[:len(path2)-1])\\n\\n      if groupPath == path2:\\n        systems = \\\"{}, {}\\\".format(systems, group.get(\\\"EPOLeafNode.NodeName\\\"))\\n    table[\\\"systems\\\"] = systems[2:]\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_groups\\\"\\ninputs.incident_id = incident.id\\ninputs.mcafee_epo_target = \\\"EPOLeafNode\\\"\\ninputs.mcafee_epo_query_select = \\\"EPOLeafNode.NodeName EPOBranchNode.NodeName EPOBranchNode.NodeTextPath2\\\"\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0o0xami\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kdd4az\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0o0xami\" sourceRef=\"ServiceTask_1qxadyp\" targetRef=\"ServiceTask_1xcirqt\"/\u003e\u003cendEvent id=\"EndEvent_0xwl30s\"\u003e\u003cincoming\u003eSequenceFlow_0kdd4az\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0kdd4az\" sourceRef=\"ServiceTask_1xcirqt\" targetRef=\"EndEvent_0xwl30s\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qxadyp\" id=\"ServiceTask_1qxadyp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ihnfbs\" id=\"SequenceFlow_1ihnfbs_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1xcirqt\" id=\"ServiceTask_1xcirqt_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"390\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o0xami\" id=\"SequenceFlow_0o0xami_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"370\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0xwl30s\" id=\"EndEvent_0xwl30s_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"528\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"546\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kdd4az\" id=\"SequenceFlow_0kdd4az_di\"\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"528\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"509\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Find all the groups on the ePO server",
      "export_key": "mcafee_epo_find_all_groups",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137435,
      "name": "McAfee ePO Find All Groups",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_find_all_groups",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "0942dce8-758b-441f-87db-1743be5c086a",
      "workflow_id": 33
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_run_client_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_run_client_task\" isExecutable=\"true\" name=\"McAfee ePO Run Client Task\"\u003e\u003cdocumentation\u003eRun the client task on the specified system(s)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0vklh4g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13fqvcs\" name=\"McAfee ePO Run Client Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c87c8e6f-71bf-40e4-af85-08d716ed25a1\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"System(s): \u0027{}\u0027 ran client task: \u0027{}\u0027 successfully.\\\".format(rule.properties.epo_system_names_or_ids, row.object_name))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_system_name_or_id = rule.properties.epo_system_names_or_ids\\ninputs.mcafee_epo_product_id = row.product_id\\ninputs.mcafee_epo_task_id = int(row.task_id)\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0vklh4g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_054htr4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0vklh4g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13fqvcs\"/\u003e\u003cendEvent id=\"EndEvent_1sk4uo4\"\u003e\u003cincoming\u003eSequenceFlow_054htr4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_054htr4\" sourceRef=\"ServiceTask_13fqvcs\" targetRef=\"EndEvent_1sk4uo4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13fqvcs\" id=\"ServiceTask_13fqvcs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"248\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vklh4g\" id=\"SequenceFlow_0vklh4g_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"248\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"223\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1sk4uo4\" id=\"EndEvent_1sk4uo4_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"389\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"407\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_054htr4\" id=\"SequenceFlow_054htr4_di\"\u003e\u003comgdi:waypoint x=\"348\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"384\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Run the client task on the specified system(s)",
      "export_key": "mcafee_epo_run_client_task",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546135366,
      "name": "McAfee ePO Run Client Task",
      "object_type": "mcafee_epo_client_tasks",
      "programmatic_name": "mcafee_epo_run_client_task",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "ee49c394-372d-4c18-b8d1-f28144e6d597",
      "workflow_id": 19
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_update_issue",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_update_issue\" isExecutable=\"true\" name=\"McAfee ePO Update Issue\"\u003e\u003cdocumentation\u003eUpdate an issue on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1852ebw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0qt09xg\" name=\"McAfee ePO Update Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d11a1d48-231a-4c2f-b9a9-f482d785aa23\"\u003e{\"inputs\":{\"b114ab6f-268c-496f-9fd6-64ae4fc96e10\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"10234f71-637e-4dd6-906a-19e32ef335ca\"}},\"079bf7ef-d3a9-4b0d-9e72-cdcbb4783d01\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"026f887f-61d5-4806-9c17-4fadddc2d58f\"}},\"9477b98a-5618-40d3-aab3-3c0f2c56ff59\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"b5611556-6d46-4755-9aab-38c72c55ad8d\"}},\"3561f86b-44c7-4c83-9fc5-962bf0231192\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7a9a788f-93c6-4575-bdb0-d22f9823624f\"}}},\"post_processing_script\":\"note = \\\"\\\"\\nif results.get(\\\"success\\\"):\\n  inputs = results.get(\\\"inputs\\\")\\n  if inputs.get(\\\"mcafee_epo_issue_priority\\\"):\\n    row.priority = inputs.get(\\\"mcafee_epo_issue_priority\\\")\\n    note += \\\"Priority updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_priority\\\"))\\n  if inputs.get(\\\"mcafee_epo_ticket_server_name\\\"):\\n    row.ticket_server_name = inputs.get(\\\"mcafee_epo_ticket_server_name\\\")\\n    note += \\\"Ticket Server Name updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_ticket_server_name\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_resolution\\\"):\\n    row.resolution = inputs.get(\\\"mcafee_epo_issue_resolution\\\")\\n    note += \\\"Resolution updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_resolution\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_due\\\"):\\n    row.issue_due_date = inputs.get(\\\"mcafee_epo_issue_due\\\")\\n    note += \\\"Due Date updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_due\\\"))\\n  if inputs.get(\\\"mcafee_epo_ticket_id\\\"):\\n    row.ticket_id = inputs.get(\\\"mcafee_epo_ticket_id\\\")\\n    note += \\\"Ticket ID updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_ticket_id\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_severity\\\"):\\n    row.severity = inputs.get(\\\"mcafee_epo_issue_severity\\\")\\n    note += \\\"Severity updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_severity\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_state\\\"):\\n    row.issue_state = inputs.get(\\\"mcafee_epo_issue_state\\\")\\n    note += \\\"State updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_state\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_name\\\"):\\n    row.issue_name = inputs.get(\\\"mcafee_epo_issue_name\\\")\\n    note += \\\"Name updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_name\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_assignee\\\"):\\n    row.assignee_name = inputs.get(\\\"mcafee_epo_issue_assignee\\\")\\n    note += \\\"Assignee updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_assignee\\\"))\\n  if inputs.get(\\\"mcafee_epo_issue_description\\\"):\\n    row.issue_description = inputs.get(\\\"mcafee_epo_issue_description\\\")\\n    note += \\\"Description updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_issue_description\\\"))\\n  incident.addNote(\\\"Issue ID: \u0027{}\u0027 updated \\\\n{}\\\".format(row.issue_id, note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_issue_assignee = rule.properties.epo_issue_assignee\\ninputs.mcafee_epo_issue_description = rule.properties.epo_issue_description\\ninputs.mcafee_epo_issue_due = rule.properties.epo_issue_due\\ninputs.mcafee_epo_issue_id = row.issue_id\\ninputs.mcafee_epo_issue_name = rule.properties.epo_issue_name\\ninputs.mcafee_epo_issue_priority = rule.properties.epo_issue_priority\\ninputs.mcafee_epo_issue_properties = rule.properties.epo_issue_properties\\ninputs.mcafee_epo_issue_resolution = rule.properties.epo_issue_resolution\\ninputs.mcafee_epo_issue_severity = rule.properties.epo_issue_severity\\ninputs.mcafee_epo_issue_state = rule.properties.epo_issue_state\\ninputs.mcafee_epo_ticket_id = rule.properties.epo_ticket_id\\ninputs.mcafee_epo_ticket_server_name = rule.properties.epo_ticket_server_name\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1852ebw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0shtx8s\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1852ebw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0qt09xg\"/\u003e\u003cendEvent id=\"EndEvent_0amwqxf\"\u003e\u003cincoming\u003eSequenceFlow_0shtx8s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0shtx8s\" sourceRef=\"ServiceTask_0qt09xg\" targetRef=\"EndEvent_0amwqxf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0qt09xg\" id=\"ServiceTask_0qt09xg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"237\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1852ebw\" id=\"SequenceFlow_1852ebw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0amwqxf\" id=\"EndEvent_0amwqxf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0shtx8s\" id=\"SequenceFlow_0shtx8s_di\"\u003e\u003comgdi:waypoint x=\"337\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"355\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Update an issue on the ePO server",
      "export_key": "mcafee_epo_update_issue",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138698,
      "name": "McAfee ePO Update Issue",
      "object_type": "mcafee_epo_issues",
      "programmatic_name": "mcafee_epo_update_issue",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "7649d041-b118-4b4f-9707-ec98d4c1687c",
      "workflow_id": 41
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_system_information",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_system_information\" isExecutable=\"true\" name=\"McAfee ePO Get System Information\"\u003e\u003cdocumentation\u003eGet then information from a given system\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16fr39n\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1ndh1eg\" name=\"McAfee ePO Find a System\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0030078d-417f-4d92-9212-6853914b56af\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = \u0027\u0027\\nif results.get(\\\"success\\\"):\\n  for x in range(len(results[\u0027content\u0027])):\\n    content = dict((k, v) for k, v in results[\u0027content\u0027][x].iteritems() if v and \\\"N/A\\\" not in str(v))\\n    note += \\\"{}\\\\n{}\\\".format(results[\u0027content\u0027][x].get(\u0027EPOComputerProperties.ComputerName\u0027), str(content))\\n\\n  content = results[\u0027content\u0027][0]\\n  row.agent_guid = str(content.get(\u0027EPOLeafNode.AgentGUID\u0027))\\n  row.last_communication = str(content.get(\u0027EPOLeafNode.LastUpdate\u0027))\\n  row.tags = str(content.get(\u0027EPOLeafNode.Tags\u0027))\\n  row.operating_system = str(content.get(\\\"EPOLeafNode.os\\\")).replace(\\\"|\\\", \\\" | \\\")\\n  \\n  incident.addNote(note.replace(\\\"{\\\",\\\"\\\").replace(\\\"u\u0027\\\",\\\"\u0027\\\").replace(\\\"}\\\",\\\"\\\\n\\\\n\\\"))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = row.system_name\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16fr39n\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1p6wbsa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16fr39n\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1ndh1eg\"/\u003e\u003cendEvent id=\"EndEvent_1tettgp\"\u003e\u003cincoming\u003eSequenceFlow_1p6wbsa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1p6wbsa\" sourceRef=\"ServiceTask_1ndh1eg\" targetRef=\"EndEvent_1tettgp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1ndh1eg\" id=\"ServiceTask_1ndh1eg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"257\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16fr39n\" id=\"SequenceFlow_16fr39n_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"257\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"227.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1tettgp\" id=\"EndEvent_1tettgp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"406.633\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"424.633\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1p6wbsa\" id=\"SequenceFlow_1p6wbsa_di\"\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"407\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"382\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get then information from a given system",
      "export_key": "mcafee_epo_get_system_information",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138986,
      "name": "McAfee ePO Get System Information",
      "object_type": "mcafee_epo_systems",
      "programmatic_name": "mcafee_epo_get_system_information",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "46b700c3-c1c4-4936-8ef1-36d96a7cfdf5",
      "workflow_id": 43
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_apply_a_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_apply_a_tag\" isExecutable=\"true\" name=\"McAfee ePO Apply a Tag\"\u003e\u003cdocumentation\u003eApply a tag to an ePO system from a list of tags\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_141ihiy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1lbiutl\" name=\"McAfee Tag an ePO Asset\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"67c5b852-f38f-40f7-8a68-1ae8e8a78549\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  note = u\\\"ePO tags: {} applied to system(s): {}\\\".format(row.epo_tag, rule.properties.epo_system)\\nelse:\\n  note = u\\\"ePO system(s): {} either not found or tag already applied for tags: {}\\\".format(rule.properties.epo_system, row.epo_tag)\\n\\nincident.addNote(note)\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = rule.properties.epo_system\\ninputs.mcafee_epo_tag = row[\u0027epo_tag\u0027]\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_141ihiy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1pimmx0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_141ihiy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1lbiutl\"/\u003e\u003cendEvent id=\"EndEvent_10zkq01\"\u003e\u003cincoming\u003eSequenceFlow_1pimmx0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1pimmx0\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"EndEvent_10zkq01\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_143umko\"\u003e\u003ctext\u003e\u003c![CDATA[A note is written with the result\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1oemzei\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"TextAnnotation_143umko\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04zssm3\"\u003e\u003ctext\u003e\u003c![CDATA[The ePO asset is\u00a0 input through a rule dialog\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vgvj54\" sourceRef=\"ServiceTask_1lbiutl\" targetRef=\"TextAnnotation_04zssm3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1lbiutl\" id=\"ServiceTask_1lbiutl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_141ihiy\" id=\"SequenceFlow_141ihiy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10zkq01\" id=\"EndEvent_10zkq01_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"421\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pimmx0\" id=\"SequenceFlow_1pimmx0_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"421\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"386\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_143umko\" id=\"TextAnnotation_143umko_di\"\u003e\u003comgdc:Bounds height=\"55\" width=\"192\" x=\"338\" y=\"78\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1oemzei\" id=\"Association_1oemzei_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"398\" xsi:type=\"omgdc:Point\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04zssm3\" id=\"TextAnnotation_04zssm3_di\"\u003e\u003comgdc:Bounds height=\"44\" width=\"131\" x=\"130\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vgvj54\" id=\"Association_1vgvj54_di\"\u003e\u003comgdi:waypoint x=\"262\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"218\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Apply a tag to an ePO system from a list of tags",
      "export_key": "mcafee_epo_apply_a_tag",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546135063,
      "name": "McAfee ePO Apply a Tag",
      "object_type": "mcafee_epo_tags",
      "programmatic_name": "mcafee_epo_apply_a_tag",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "d8b90c47-57fa-43db-acb2-bcca4812fb2c",
      "workflow_id": 17
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_run_client_task_on_system",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_run_client_task_on_system\" isExecutable=\"true\" name=\"McAfee ePO Run Client Task on System\"\u003e\u003cdocumentation\u003eRun the client task on the specified system\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_13w1tcf\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1sfp7kl\" name=\"McAfee ePO Run Client Task\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c87c8e6f-71bf-40e4-af85-08d716ed25a1\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"content\\\") and results.get(\\\"content\\\") == \\\"Succeeded\\\":\\n  incident.addNote(\\\"System(s): \u0027{}\u0027 ran client task: \u0027{}\u0027 successfully.\\\".format(row.system_name, rule.properties.epo_task_id))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_system_name_or_id = row.system_name\\ninputs.mcafee_epo_product_id = rule.properties.epo_product_id\\ninputs.mcafee_epo_task_id = rule.properties.epo_task_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_13w1tcf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xsn7eb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_13w1tcf\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1sfp7kl\"/\u003e\u003cendEvent id=\"EndEvent_0tn77l3\"\u003e\u003cincoming\u003eSequenceFlow_0xsn7eb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0xsn7eb\" sourceRef=\"ServiceTask_1sfp7kl\" targetRef=\"EndEvent_0tn77l3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sfp7kl\" id=\"ServiceTask_1sfp7kl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13w1tcf\" id=\"SequenceFlow_13w1tcf_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0tn77l3\" id=\"EndEvent_0tn77l3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"388\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"406\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xsn7eb\" id=\"SequenceFlow_0xsn7eb_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"371.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Run the client task on the specified system",
      "export_key": "mcafee_epo_run_client_task_on_system",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137275,
      "name": "McAfee ePO Run Client Task on System",
      "object_type": "mcafee_epo_systems",
      "programmatic_name": "mcafee_epo_run_client_task_on_system",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "2718c9cd-0ffd-4d83-8c66-676a55659c02",
      "workflow_id": 32
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_apply_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_apply_tags\" isExecutable=\"true\" name=\"McAfee ePO Apply Tags\"\u003e\u003cdocumentation\u003eApply tag(s) to an ePO system. This workflow uses an artifact as representing the ePO system to tag.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mees7m\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_16nkdp9\" name=\"McAfee Tag an ePO Asset\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"67c5b852-f38f-40f7-8a68-1ae8e8a78549\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  note = u\\\"ePO tag(s) added: {}\\\".format(str(rule.properties.ss_tags))\\nelse:\\n  note = u\\\"ePO system not found or tag already applied: {}\\\".format(str(rule.properties.ss_tags))\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, note)\\nelse:\\n  artifact.description = note\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\\ninputs.mcafee_epo_tag = str(rule.properties.ss_tags)\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mees7m\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0jns448\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mees7m\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_16nkdp9\"/\u003e\u003cendEvent id=\"EndEvent_0ct39x5\"\u003e\u003cincoming\u003eSequenceFlow_0jns448\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0jns448\" sourceRef=\"ServiceTask_16nkdp9\" targetRef=\"EndEvent_0ct39x5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_15dsftr\"\u003e\u003ctext\u003e\u003c![CDATA[Results returned to artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17pn86l\" sourceRef=\"ServiceTask_16nkdp9\" targetRef=\"TextAnnotation_15dsftr\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_16nkdp9\" id=\"ServiceTask_16nkdp9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"264\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mees7m\" id=\"SequenceFlow_1mees7m_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"231\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ct39x5\" id=\"EndEvent_0ct39x5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"426\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"444\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jns448\" id=\"SequenceFlow_0jns448_di\"\u003e\u003comgdi:waypoint x=\"364\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"395\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_15dsftr\" id=\"TextAnnotation_15dsftr_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"137\" x=\"353\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17pn86l\" id=\"Association_17pn86l_di\"\u003e\u003comgdi:waypoint x=\"349\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Apply tag(s) to an ePO system. This workflow uses an artifact as representing the ePO system to tag.",
      "export_key": "mcafee_epo_apply_tags",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137913,
      "name": "McAfee ePO Apply Tags",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_apply_tags",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "23de1b1f-1cb8-4f97-95fa-bb2a8e657cfb",
      "workflow_id": 36
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_delete_issue",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_delete_issue\" isExecutable=\"true\" name=\"McAfee ePO Delete Issue\"\u003e\u003cdocumentation\u003eDelete the issue on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_00jnil9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ci8dag\" name=\"McAfee ePO Delete Issue\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9edf3f57-b79b-4a50-bc6b-632ea6406dfe\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  row.issue_deleted = True\\n  incident.addNote(\\\"Issue: \u0027{}\u0027 deleted successfully.\\\".format(row.issue_id))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_issue_id = row.issue_id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_00jnil9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03yy9bz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_00jnil9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ci8dag\"/\u003e\u003cendEvent id=\"EndEvent_1wzc31b\"\u003e\u003cincoming\u003eSequenceFlow_03yy9bz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_03yy9bz\" sourceRef=\"ServiceTask_0ci8dag\" targetRef=\"EndEvent_1wzc31b\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ci8dag\" id=\"ServiceTask_0ci8dag_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"233\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_00jnil9\" id=\"SequenceFlow_00jnil9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"233\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"215.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1wzc31b\" id=\"EndEvent_1wzc31b_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"360\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"378\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03yy9bz\" id=\"SequenceFlow_03yy9bz_di\"\u003e\u003comgdi:waypoint x=\"333\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"346.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Delete the issue on the ePO server",
      "export_key": "mcafee_epo_delete_issue",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137595,
      "name": "McAfee ePO Delete Issue",
      "object_type": "mcafee_epo_issues",
      "programmatic_name": "mcafee_epo_delete_issue",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "09cc49b9-12a6-47c1-ab39-1eddfa593405",
      "workflow_id": 34
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_assign_policy_to_group_from_policy",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_assign_policy_to_group_from_policy\" isExecutable=\"true\" name=\"McAfee ePO Assign Policy to Group from Policy\"\u003e\u003cdocumentation\u003eAssign a policy to a specified group on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p5hvx6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0a7fxx6\" name=\"McAfee ePO Assign Policy to Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4dc3b4db-1f72-4b4e-b7e0-c5996f743697\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"Policy: \u0027{}\u0027 Assigned to group: \u0027{}\u0027\\\".format(row.object_name, rule.properties.epo_group_id))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_group_id = rule.properties.epo_group_id\\ninputs.mcafee_epo_object_id = row.object_id\\ninputs.mcafee_epo_product_id = row.product_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p5hvx6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0njauw6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p5hvx6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0a7fxx6\"/\u003e\u003cendEvent id=\"EndEvent_1rl8isc\"\u003e\u003cincoming\u003eSequenceFlow_0njauw6\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0njauw6\" sourceRef=\"ServiceTask_0a7fxx6\" targetRef=\"EndEvent_1rl8isc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0a7fxx6\" id=\"ServiceTask_0a7fxx6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p5hvx6\" id=\"SequenceFlow_0p5hvx6_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1rl8isc\" id=\"EndEvent_1rl8isc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"373\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"391\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0njauw6\" id=\"SequenceFlow_0njauw6_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"362.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Assign a policy to a specified group on the ePO server",
      "export_key": "mcafee_epo_assign_policy_to_group_from_policy",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138350,
      "name": "McAfee ePO Assign Policy to Group from Policy",
      "object_type": "mcafee_epo_policies",
      "programmatic_name": "mcafee_epo_assign_policy_to_group_from_policy",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "69f4d215-1e0e-47dd-b4e4-1ffd86cee918",
      "workflow_id": 39
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_all_systems",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_all_systems\" isExecutable=\"true\" name=\"McAfee ePO Get All Systems\"\u003e\u003cdocumentation\u003eGet all of the systems in the system tree on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16y6xff\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0rrlpjh\" name=\"McAfee ePO Execute Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a78912f-473f-4eaf-86b3-05dc87c5e14a\"\u003e{\"inputs\":{\"3b19d71b-890d-472c-bec7-40a035c1bca2\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"EPOLeafNode\"}}},\"post_processing_script\":\"if results.get(\u0027success\u0027):\\n  for system in results[\u0027content\u0027]:\\n    table_row = incident.addRow(\\\"mcafee_epo_systems\\\")\\n    table_row[\\\"system_name\\\"] = system.get(\\\"EPOLeafNode.NodeName\\\")\\n    table_row[\\\"agent_guid\\\"] = system.get(\\\"EPOLeafNode.AgentGUID\\\")\\n    table_row[\\\"last_communication\\\"] = system.get(\\\"EPOLeafNode.LastUpdate\\\")\\n    table_row[\\\"tags\\\"] = system.get(\\\"EPOLeafNode.Tags\\\")\\n    table_row[\\\"operating_system\\\"] = system.get(\\\"EPOLeafNode.os\\\").replace(\\\"|\\\", \\\" | \\\")\\n    table_row[\\\"deleted\\\"] = False\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_target = \\\"EPOLeafNode\\\"\\ninputs.datatable_name = \\\"mcafee_epo_systems\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16y6xff\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_07jpeij\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16y6xff\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0rrlpjh\"/\u003e\u003cendEvent id=\"EndEvent_0eo73dv\"\u003e\u003cincoming\u003eSequenceFlow_07jpeij\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_07jpeij\" sourceRef=\"ServiceTask_0rrlpjh\" targetRef=\"EndEvent_0eo73dv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0rrlpjh\" id=\"ServiceTask_0rrlpjh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"232\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16y6xff\" id=\"SequenceFlow_16y6xff_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"232\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"215\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0eo73dv\" id=\"EndEvent_0eo73dv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"368\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"386\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07jpeij\" id=\"SequenceFlow_07jpeij_di\"\u003e\u003comgdi:waypoint x=\"332\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"350\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get all of the systems in the system tree on the ePO server",
      "export_key": "mcafee_epo_get_all_systems",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136411,
      "name": "McAfee ePO Get All Systems",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_get_all_systems",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "3e778eda-1193-40e1-bbd9-fefd9572dac5",
      "workflow_id": 26
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_remove_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_remove_tag\" isExecutable=\"true\" name=\"McAfee ePO Remove Tag\"\u003e\u003cdocumentation\u003eRemove tag(s) from an ePO system. This workflow use an artifact representing the system to tag.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1pzlzpj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1spfyme\" name=\"McAfee ePO remove tag\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"1cb1fd7a-0eeb-4230-9edb-c8f6f47b1ae9\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.get(\\\"success\\\"):\\n  note = u\\\"ePO system not found or tag not applied: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\nelse:\\n  note = u\\\"ePO tag(s) removed: {}\\\".format(results.inputs[\u0027mcafee_epo_tag\u0027])\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, note)\\nelse:\\n  artifact.description = note\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\\ninputs.mcafee_epo_tag = str(rule.properties.ss_tags)\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1pzlzpj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ygkcww\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1pzlzpj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1spfyme\"/\u003e\u003cendEvent id=\"EndEvent_1johhu0\"\u003e\u003cincoming\u003eSequenceFlow_1ygkcww\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ygkcww\" sourceRef=\"ServiceTask_1spfyme\" targetRef=\"EndEvent_1johhu0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1spfyme\" id=\"ServiceTask_1spfyme_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1pzlzpj\" id=\"SequenceFlow_1pzlzpj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1johhu0\" id=\"EndEvent_1johhu0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"400\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"418\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ygkcww\" id=\"SequenceFlow_1ygkcww_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"400\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"376\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Remove tag(s) from an ePO system. This workflow use an artifact representing the system to tag.",
      "export_key": "mcafee_epo_remove_tag",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138532,
      "name": "McAfee ePO Remove Tag",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_remove_tag",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "477b4168-74da-4c1a-b073-4e4be021b89a",
      "workflow_id": 40
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_system_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_system_info\" isExecutable=\"true\" name=\"McAfee ePO Get System Info\"\u003e\u003cdocumentation\u003eGet information on an ePO system\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ww09gi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_02avpdz\" name=\"McAfee ePO Find a System\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0030078d-417f-4d92-9212-6853914b56af\"\u003e{\"inputs\":{},\"post_processing_script\":\"if not results.get(\\\"success\\\"):\\n  info = u\\\"ePO system not found\\\"\\nelse:\\n  info = u\\\"ePO system info\\\\n\\\"\\n  for system in results.content:\\n    for setting in system:\\n      info = u\\\"{}\\\\n{}: {}\\\".format(info, setting, system.get(\\\"setting\\\"))\\n\\nif artifact.description:\\n  artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, info)\\nelse:\\n  artifact.description = info\\n\\nincident.addNote(info)\\n\\n\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = artifact.value\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ww09gi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11w64qz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ww09gi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_02avpdz\"/\u003e\u003cendEvent id=\"EndEvent_1shs028\"\u003e\u003cincoming\u003eSequenceFlow_11w64qz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_11w64qz\" sourceRef=\"ServiceTask_02avpdz\" targetRef=\"EndEvent_1shs028\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1p16xdz\"\u003e\u003ctext\u003e\u003c![CDATA[Return system info as the artifact description\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0v38vt5\" sourceRef=\"ServiceTask_02avpdz\" targetRef=\"TextAnnotation_1p16xdz\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_02avpdz\" id=\"ServiceTask_02avpdz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"252\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ww09gi\" id=\"SequenceFlow_0ww09gi_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"225\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1shs028\" id=\"EndEvent_1shs028_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"405\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"423\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11w64qz\" id=\"SequenceFlow_11w64qz_di\"\u003e\u003comgdi:waypoint x=\"352\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"405\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"378.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1p16xdz\" id=\"TextAnnotation_1p16xdz_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"178\" x=\"347\" y=\"66\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0v38vt5\" id=\"Association_0v38vt5_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"401\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get information on an ePO system",
      "export_key": "mcafee_epo_get_system_info",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136556,
      "name": "McAfee ePO Get System Info",
      "object_type": "artifact",
      "programmatic_name": "mcafee_epo_get_system_info",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "1498bc37-0695-4b96-9fa8-02fee0c06da4",
      "workflow_id": 27
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "mcafee_epo_list_issues",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_list_issues\" isExecutable=\"true\" name=\"McAfee ePO List Issues\"\u003e\u003cdocumentation\u003eList the issues found on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_018lvr8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1gm86kl\" name=\"McAfee ePO List Issues\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"e271a8f5-9886-4c2a-8e05-cbca9ed1c632\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for c in results.get(\\\"content\\\"):\\n    row = incident.addRow(\\\"mcafee_epo_issues\\\")\\n    row[\\\"issue_name\\\"] = c.get(\\\"name\\\")\\n    row[\\\"issue_id\\\"] = int(c.get(\\\"id\\\"))\\n    row[\\\"severity\\\"] = c.get(\\\"severity\\\")\\n    row[\\\"issue_due_date\\\"] = c.get(\\\"dueDate\\\")\\n    row[\\\"issue_description\\\"] = c.get(\\\"description\\\")\\n    row[\\\"ticket_server_name\\\"] = c.get(\\\"ticketServerName\\\")\\n    row[\\\"priority\\\"] = c.get(\\\"priority\\\")\\n    row[\\\"type\\\"] = c.get(\\\"type\\\")\\n    row[\\\"resolution\\\"] = c.get(\\\"resolution\\\")\\n    row[\\\"assignee_name\\\"] = c.get(\\\"assigneeName\\\")\\n    row[\\\"issue_state\\\"] = c.get(\\\"state\\\")\\n    row[\\\"ticket_id\\\"] = int(c.get(\\\"ticketId\\\")) if c.get(\\\"ticketId\\\") else None\\n    row[\\\"issue_deleted\\\"] = False\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_issues\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_018lvr8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0liif74\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_018lvr8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1gm86kl\"/\u003e\u003cendEvent id=\"EndEvent_09frq0n\"\u003e\u003cincoming\u003eSequenceFlow_0liif74\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0liif74\" sourceRef=\"ServiceTask_1gm86kl\" targetRef=\"EndEvent_09frq0n\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1gm86kl\" id=\"ServiceTask_1gm86kl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_018lvr8\" id=\"SequenceFlow_018lvr8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09frq0n\" id=\"EndEvent_09frq0n_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"386\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"359\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0liif74\" id=\"SequenceFlow_0liif74_di\"\u003e\u003comgdi:waypoint x=\"335\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"386\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"315.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "List the issues found on the ePO server",
      "export_key": "mcafee_epo_list_issues",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664808661393,
      "name": "McAfee ePO List Issues",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_list_issues",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "e2efe074-07a7-4a8a-9428-a558888e404d",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_all_users",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_all_users\" isExecutable=\"true\" name=\"McAfee ePO Get All Users\"\u003e\u003cdocumentation\u003eGet all of the users on an ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15b09rg\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_18zpd3n\" name=\"McAfee ePO Get All Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6b9906aa-5409-44cb-b88b-192c49598d35\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for user in results[\\\"content\\\"]:\\n    table_row = incident.addRow(\\\"mcafee_epo_users\\\")\\n    table_row[\\\"user_name\\\"] = user.get(\\\"name\\\")\\n    table_row[\\\"full_name\\\"] = user.get(\\\"fullName\\\")\\n    table_row[\\\"email\\\"] = user.get(\\\"email\\\")\\n    table_row[\\\"phone_number\\\"] = user.get(\\\"phoneNumber\\\")\\n    table_row[\\\"disabled\\\"] = bool(user.get(\\\"disabled\\\"))\\n    table_row[\\\"admin\\\"] = bool(user.get(\\\"admin\\\"))\\n    table_row[\\\"notes\\\"] = user.get(\\\"notes\\\")\\n    table_row[\\\"allowed_ips\\\"] = user.get(\\\"allowedIPs\\\")\\n    table_row[\\\"user_deleted\\\"] = False\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_users\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15b09rg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1sm0yak\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15b09rg\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_18zpd3n\"/\u003e\u003cendEvent id=\"EndEvent_1yzqlrq\"\u003e\u003cincoming\u003eSequenceFlow_1sm0yak\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1sm0yak\" sourceRef=\"ServiceTask_18zpd3n\" targetRef=\"EndEvent_1yzqlrq\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_18zpd3n\" id=\"ServiceTask_18zpd3n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15b09rg\" id=\"SequenceFlow_15b09rg_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1yzqlrq\" id=\"EndEvent_1yzqlrq_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"410\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"428\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1sm0yak\" id=\"SequenceFlow_1sm0yak_di\"\u003e\u003comgdi:waypoint x=\"350\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"410\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"400\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get all of the users on an ePO server",
      "export_key": "mcafee_epo_get_all_users",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136699,
      "name": "McAfee ePO Get All Users",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_get_all_users",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "98616f26-6b33-4808-bd74-b713d24b9e68",
      "workflow_id": 28
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_system_info_from_property",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_system_info_from_property\" isExecutable=\"true\" name=\"McAfee ePO Get System Info from Property\"\u003e\u003cdocumentation\u003eGet information about systems from a lit of system properties\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_10ab8pu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1yjbgrc\" name=\"McAfee ePO Find a System\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0030078d-417f-4d92-9212-6853914b56af\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = \u0027\u0027\\nif results.get(\\\"success\\\"):\\n  for x in range(len(results[\u0027content\u0027])):\\n    content = dict((k, v) for k, v in results[\u0027content\u0027][x].iteritems() if v and \\\"N/A\\\" not in str(v))\\n    note += \\\"{}\\\\n{}\\\".format(results[\u0027content\u0027][x].get(\u0027EPOComputerProperties.ComputerName\u0027), str(content))\\n    \\n  incident.addNote(note.replace(\\\"{\\\",\\\"\\\").replace(\\\"u\u0027\\\",\\\"\u0027\\\").replace(\\\"}\\\",\\\"\\\\n\\\\n\\\"))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = rule.properties.epo_system\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10ab8pu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1d76i4s\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10ab8pu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1yjbgrc\"/\u003e\u003cendEvent id=\"EndEvent_09bu20t\"\u003e\u003cincoming\u003eSequenceFlow_1d76i4s\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1d76i4s\" sourceRef=\"ServiceTask_1yjbgrc\" targetRef=\"EndEvent_09bu20t\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1yjbgrc\" id=\"ServiceTask_1yjbgrc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"245\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10ab8pu\" id=\"SequenceFlow_10ab8pu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"245\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"221.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_09bu20t\" id=\"EndEvent_09bu20t_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"383\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1d76i4s\" id=\"SequenceFlow_1d76i4s_di\"\u003e\u003comgdi:waypoint x=\"345\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"364\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get information about systems from a lit of system properties",
      "export_key": "mcafee_epo_get_system_info_from_property",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546134765,
      "name": "McAfee ePO Get System Info from Property",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_get_system_info_from_property",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "2cb0172a-f414-4c84-bc17-2b8180849877",
      "workflow_id": 15
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_find_all_client_tasks",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_find_all_client_tasks\" isExecutable=\"true\" name=\"McAfee ePO Find All Client Tasks\"\u003e\u003cdocumentation\u003eFind all of the client tasks on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1wzo119\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_13qnild\" name=\"McAfee ePO Find Client Tasks\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"948b9c0a-1d8e-47c4-a277-1180ee5d3f5e\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for x in results.get(\\\"content\\\"):\\n    table = incident.addRow(\\\"mcafee_epo_client_tasks\\\")\\n    table[\\\"object_name\\\"] = x.get(\\\"objectName\\\")\\n    table[\\\"type_name\\\"] = x.get(\\\"typeName\\\")\\n    table[\\\"product_name\\\"] = x.get(\\\"productName\\\")\\n    table[\\\"product_id\\\"] = x.get(\\\"productId\\\")\\n    table[\\\"task_id\\\"] = x.get(\\\"objectId\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_client_tasks\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1wzo119\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0l08t8q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wzo119\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_13qnild\"/\u003e\u003cendEvent id=\"EndEvent_0vkqeof\"\u003e\u003cincoming\u003eSequenceFlow_0l08t8q\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0l08t8q\" sourceRef=\"ServiceTask_13qnild\" targetRef=\"EndEvent_0vkqeof\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13qnild\" id=\"ServiceTask_13qnild_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"165\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wzo119\" id=\"SequenceFlow_1wzo119_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" xsi:type=\"omgdc:Point\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"173\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0vkqeof\" id=\"EndEvent_0vkqeof_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"367\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l08t8q\" id=\"SequenceFlow_0l08t8q_di\"\u003e\u003comgdi:waypoint x=\"338\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"367\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"307.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Find all of the client tasks on the ePO server",
      "export_key": "mcafee_epo_find_all_client_tasks",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546134912,
      "name": "McAfee ePO Find All Client Tasks",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_find_all_client_tasks",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "3674d301-6cab-46a1-adfa-ed4b06078efa",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_wake_up_agent",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_wake_up_agent\" isExecutable=\"true\" name=\"McAfee ePO Wake up Agent\"\u003e\u003cdocumentation\u003eWake up agent\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qn10xw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0wapcdn\" name=\"McAfee ePO Wake up agent\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a8b3bef5-36fc-4d69-b366-6fd3def996d2\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addNote(results.get(\\\"content\\\"))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_systems = rule.properties.epo_system\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qn10xw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0i01ddl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qn10xw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0wapcdn\"/\u003e\u003cendEvent id=\"EndEvent_0yc6dui\"\u003e\u003cincoming\u003eSequenceFlow_0i01ddl\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0i01ddl\" sourceRef=\"ServiceTask_0wapcdn\" targetRef=\"EndEvent_0yc6dui\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0wapcdn\" id=\"ServiceTask_0wapcdn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"283\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qn10xw\" id=\"SequenceFlow_1qn10xw_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"283\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"240.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0yc6dui\" id=\"EndEvent_0yc6dui_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"435\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"453\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0i01ddl\" id=\"SequenceFlow_0i01ddl_di\"\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"435\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"409\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Wake up agent",
      "export_key": "mcafee_epo_wake_up_agent",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136264,
      "name": "McAfee ePO Wake up Agent",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_wake_up_agent",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "902abf9a-af7b-47f5-9d3b-c567e0f3ae56",
      "workflow_id": 25
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_assign_policy_to_systems_from_policy",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_assign_policy_to_systems_from_policy\" isExecutable=\"true\" name=\"McAfee ePO Assign Policy to Systems from Policy\"\u003e\u003cdocumentation\u003eAssign a policy to system(s)\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0jjq5au\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ppy0xz\" name=\"McAfee ePO Assign Policy to Syste...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"81575bf7-1c92-45d0-a674-4682f9e735c7\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  incident.addNote(\\\"Policy: \u0027{}\u0027 Assigned to system: \u0027{}\u0027\\\".format(row.object_id, rule.properties.epo_system_names_or_ids))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_system_name_or_id = rule.properties.epo_system_names_or_ids\\ninputs.mcafee_epo_product_id = row.product_id\\ninputs.mcafee_epo_type_id = row.type_id\\ninputs.mcafee_epo_object_id = row.object_id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0jjq5au\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1aacxdv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0jjq5au\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ppy0xz\"/\u003e\u003cendEvent id=\"EndEvent_0yi911p\"\u003e\u003cincoming\u003eSequenceFlow_1aacxdv\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1aacxdv\" sourceRef=\"ServiceTask_0ppy0xz\" targetRef=\"EndEvent_0yi911p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ppy0xz\" id=\"ServiceTask_0ppy0xz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"253\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0jjq5au\" id=\"SequenceFlow_0jjq5au_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"225.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0yi911p\" id=\"EndEvent_0yi911p_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"376\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"394\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1aacxdv\" id=\"SequenceFlow_1aacxdv_di\"\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"364.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Assign a policy to system(s)",
      "export_key": "mcafee_epo_assign_policy_to_systems_from_policy",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136849,
      "name": "McAfee ePO Assign Policy to Systems from Policy",
      "object_type": "mcafee_epo_policies",
      "programmatic_name": "mcafee_epo_assign_policy_to_systems_from_policy",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "e50cc96a-fb35-4438-97c7-22a25a5c10e8",
      "workflow_id": 29
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_find_policies",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_find_policies\" isExecutable=\"true\" name=\"McAfee ePO Find Policies\"\u003e\u003cdocumentation\u003eFind policies in the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0j21lmc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xl7bzp\" name=\"McAfee ePO Find Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a8259648-09cc-4d7f-a21a-3a6d455646d3\"\u003e{\"inputs\":{},\"post_processing_script\":\"# if results.get(\\\"success\\\"):\\n#   for policy in results[\\\"content\\\"]:\\n#     table_row = incident.addRow(\\\"mcafee_epo_policies\\\")\\n#     table_row[\\\"object_name\\\"] = policy.get(\\\"objectName\\\")\\n#     table_row[\\\"object_id\\\"] = int(policy.get(\\\"objectId\\\"))\\n#     table_row[\\\"type_name\\\"] = policy.get(\\\"typeName\\\")\\n#     table_row[\\\"type_id\\\"] = int(policy.get(\\\"typeId\\\"))\\n#     table_row[\\\"product_id\\\"] = policy.get(\\\"productId\\\")\\n#     table_row[\\\"object_notes\\\"] = policy.get(\\\"objectNotes\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"policyresults\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0j21lmc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1499i96\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0j21lmc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xl7bzp\"/\u003e\u003cserviceTask id=\"ServiceTask_0xwxq1h\" name=\"McAfee ePO Execute Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a78912f-473f-4eaf-86b3-05dc87c5e14a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for policy in workflow.properties.policyresults[\\\"content\\\"]:\\n    policyId = int(policy.get(\\\"objectId\\\"))\\n    table_row = incident.addRow(\\\"mcafee_epo_policies\\\")\\n    table_row[\\\"object_name\\\"] = policy.get(\\\"objectName\\\")\\n    table_row[\\\"object_id\\\"] = policyId\\n    table_row[\\\"type_name\\\"] = policy.get(\\\"typeName\\\")\\n    table_row[\\\"type_id\\\"] = int(policy.get(\\\"typeId\\\"))\\n    table_row[\\\"product_id\\\"] = policy.get(\\\"productId\\\")\\n    table_row[\\\"object_notes\\\"] = policy.get(\\\"objectNotes\\\")\\n    systems = \\\"\\\"\\n    for assigned in results.get(\\\"content\\\"):\\n      if assigned.get(\\\"EPOAssignedPolicy.PolicyObjectID\\\") == policyId:\\n        systems = \\\"{}, {}\\\".format(systems, assigned.get(\\\"EPOAssignedPolicy.NodeName\\\"))\\n\\n    table_row[\\\"systems\\\"] = systems[2:]\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_target = \\\"EPOAssignedPolicy\\\"\\ninputs.mcafee_epo_query_select = \\\"EPOAssignedPolicy.NodeName EPOAssignedPolicy.PolicyObjectID\\\"\\ninputs.datatable_name = \\\"mcafee_epo_policies\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1499i96\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_036g865\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0hp8uyl\"\u003e\u003cincoming\u003eSequenceFlow_036g865\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_036g865\" sourceRef=\"ServiceTask_0xwxq1h\" targetRef=\"EndEvent_0hp8uyl\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1499i96\" sourceRef=\"ServiceTask_0xl7bzp\" targetRef=\"ServiceTask_0xwxq1h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xl7bzp\" id=\"ServiceTask_0xl7bzp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"231\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0j21lmc\" id=\"SequenceFlow_0j21lmc_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xwxq1h\" id=\"ServiceTask_0xwxq1h_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"373\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hp8uyl\" id=\"EndEvent_0hp8uyl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"523\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"496\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_036g865\" id=\"SequenceFlow_036g865_di\"\u003e\u003comgdi:waypoint x=\"473\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"523\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"453\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1499i96\" id=\"SequenceFlow_1499i96_di\"\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"373\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"307\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Find policies in the ePO server",
      "export_key": "mcafee_epo_find_policies",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546139118,
      "name": "McAfee ePO Find Policies",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_find_policies",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "bb1c82ad-0404-4537-b5cf-0fd372502d89",
      "workflow_id": 44
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_list_tags",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_list_tags\" isExecutable=\"true\" name=\"McAfee ePO List Tags\"\u003e\u003cdocumentation\u003eList available tags defined in ePO. Results are displayed in a datatable.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0a2179k\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1734ypy\" name=\"McAfee ePO List Tags\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b9d82be9-83b0-4b88-90ca-7e0d2fb09dc7\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for tag in sorted(results.content, key = lambda i: i[\u0027tagName\u0027].lower()):\\n    row = incident.addRow(\\\"mcafee_epo_tags\\\")\\n    row[\u0027epo_id\u0027] = tag[\u0027tagId\u0027]\\n    row[\u0027epo_tag\u0027] = tag[\u0027tagName\u0027]\\n    row[\u0027epo_notes\u0027] = tag[\u0027tagNotes\u0027]\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_tags\\\"\\ninputs.incident_id = incident.id\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0a2179k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_081gl9p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0a2179k\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1734ypy\"/\u003e\u003cendEvent id=\"EndEvent_1sd36bh\"\u003e\u003cincoming\u003eSequenceFlow_081gl9p\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_081gl9p\" sourceRef=\"ServiceTask_1734ypy\" targetRef=\"EndEvent_1sd36bh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ryo4jh\"\u003e\u003ctext\u003e\u003c![CDATA[Display results in a datatable\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0qxjkvx\" sourceRef=\"ServiceTask_1734ypy\" targetRef=\"TextAnnotation_1ryo4jh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1734ypy\" id=\"ServiceTask_1734ypy_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"255\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0a2179k\" id=\"SequenceFlow_0a2179k_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"255\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"226.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1sd36bh\" id=\"EndEvent_1sd36bh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"411.8027906976744\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"429.8027906976744\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_081gl9p\" id=\"SequenceFlow_081gl9p_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"383.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ryo4jh\" id=\"TextAnnotation_1ryo4jh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"349\" y=\"91\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0qxjkvx\" id=\"Association_0qxjkvx_di\"\u003e\u003comgdi:waypoint x=\"343\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "List available tags defined in ePO. Results are displayed in a datatable.",
      "export_key": "mcafee_epo_list_tags",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546136989,
      "name": "McAfee ePO List Tags",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_list_tags",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "50099f17-2f9a-4b2d-91d2-63625065cfee",
      "workflow_id": 30
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_get_all_permission_sets",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_get_all_permission_sets\" isExecutable=\"true\" name=\"McAfee ePO Get all Permission Sets\"\u003e\u003cdocumentation\u003eGet all of the permission sets on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1wqcqhu\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1g1o5nz\" name=\"McAfee ePO Get All Permission set...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4c45547c-5c2f-4711-90c1-7715706605fc\"\u003e{\"inputs\":{},\"post_processing_script\":\"# if results.get(\\\"success\\\"):\\n#   for permset in results[\\\"content\\\"]:\\n#     table_row = incident.addRow(\\\"mcafee_epo_permission_sets\\\")\\n#     table_row[\\\"permission_set_name\\\"] = permset.get(\\\"name\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script_language\":\"python\",\"result_name\":\"permsets\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1wqcqhu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_15ninxr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wqcqhu\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1g1o5nz\"/\u003e\u003cserviceTask id=\"ServiceTask_0ozhxzq\" name=\"McAfee ePO Execute Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3a78912f-473f-4eaf-86b3-05dc87c5e14a\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  for permset in workflow.properties.permsets.get(\\\"content\\\"):\\n    permsetName = permset.get(\\\"name\\\")\\n    table_row = incident.addRow(\\\"mcafee_epo_permission_sets\\\")\\n    table_row[\\\"permission_set_name\\\"] = permsetName\\n    users = \\\"\\\"\\n    for perm in results.get(\\\"content\\\"):\\n      user = perm.get(\\\"EntitlementView.PrincipalName\\\")\\n      if user and permsetName.lower() == perm.get(\\\"EntitlementView.GroupName\\\").lower() and user not in users:\\n        users = \\\"{}, {}\\\".format(users, user)\\n    table_row[\\\"users\\\"] = users[2:]\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.datatable_name = \\\"mcafee_epo_permission_sets\\\"\\ninputs.incident_id = incident.id\\ninputs.mcafee_epo_target = \\\"EntitlementView\\\"\\ninputs.mcafee_epo_query_select = \\\"EntitlementView.PrincipalName EntitlementView.GroupName\\\"\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15ninxr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t385gy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15ninxr\" sourceRef=\"ServiceTask_1g1o5nz\" targetRef=\"ServiceTask_0ozhxzq\"/\u003e\u003cendEvent id=\"EndEvent_0lqwxk6\"\u003e\u003cincoming\u003eSequenceFlow_0t385gy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0t385gy\" sourceRef=\"ServiceTask_0ozhxzq\" targetRef=\"EndEvent_0lqwxk6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1g1o5nz\" id=\"ServiceTask_1g1o5nz_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"247\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wqcqhu\" id=\"SequenceFlow_1wqcqhu_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ozhxzq\" id=\"ServiceTask_0ozhxzq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"409\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15ninxr\" id=\"SequenceFlow_15ninxr_di\"\u003e\u003comgdi:waypoint x=\"347\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"409\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"378\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0lqwxk6\" id=\"EndEvent_0lqwxk6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"540\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"558\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t385gy\" id=\"SequenceFlow_0t385gy_di\"\u003e\u003comgdi:waypoint x=\"509\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"540\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"524.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Get all of the permission sets on the ePO server",
      "export_key": "mcafee_epo_get_all_permission_sets",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137132,
      "name": "McAfee ePO Get all Permission Sets",
      "object_type": "incident",
      "programmatic_name": "mcafee_epo_get_all_permission_sets",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "67fbc2e0-e4b0-422e-bef5-421e9b7c760d",
      "workflow_id": 31
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_remove_permission_set_from_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_remove_permission_set_from_user\" isExecutable=\"true\" name=\"McAfee ePO Remove Permission Set from User\"\u003e\u003cdocumentation\u003eRemove a permission set from an ePO user\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_03mip5s\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0it7rag\" name=\"McAfee ePO Remove Permission sets...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"85f46ad5-4275-4478-a0f9-1789729d39e5\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\u0027success\u0027):\\n  incident.addNote(\\\"Permissions set: {} was removed from user: {}\\\".format(row.permission_set_name, rule.properties.epo_username))\\n  if row.users:\\n    usersList = list(row.users.split(\\\", \\\"))\\n    usersList.remove(rule.properties.epo_username)\\n    row.users = str(usersList).replace(\\\"[\\\",\\\"\\\").replace(\\\"]\\\",\\\"\\\").replace(\\\"\u0027\\\",\\\"\\\")\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_permsetname = row.permission_set_name\\ninputs.mcafee_epo_username = rule.properties.epo_username\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_03mip5s\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0z3jzci\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_03mip5s\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0it7rag\"/\u003e\u003cendEvent id=\"EndEvent_0d7fawb\"\u003e\u003cincoming\u003eSequenceFlow_0z3jzci\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0z3jzci\" sourceRef=\"ServiceTask_0it7rag\" targetRef=\"EndEvent_0d7fawb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0it7rag\" id=\"ServiceTask_0it7rag_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"231\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03mip5s\" id=\"SequenceFlow_03mip5s_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"231\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0d7fawb\" id=\"EndEvent_0d7fawb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"382.6877729257642\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"400.6877729257642\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0z3jzci\" id=\"SequenceFlow_0z3jzci_di\"\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"383\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"357\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Remove a permission set from an ePO user",
      "export_key": "mcafee_epo_remove_permission_set_from_user",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138065,
      "name": "McAfee ePO Remove Permission Set from User",
      "object_type": "mcafee_epo_permission_sets",
      "programmatic_name": "mcafee_epo_remove_permission_set_from_user",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "c8345121-5828-42b7-aa76-d86c191a941c",
      "workflow_id": 37
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_update_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_update_user\" isExecutable=\"true\" name=\"McAfee ePO Update User\"\u003e\u003cdocumentation\u003eUpdate a user on the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mecdzt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1trazkd\" name=\"McAfee ePO Update User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a45c768a-d8d0-4666-a002-b7ddf6624fe6\"\u003e{\"inputs\":{},\"post_processing_script\":\"note = \\\"\\\"\\nif results.get(\\\"success\\\"):\\n  inputs = results.get(\\\"inputs\\\")\\n  if inputs.get(\\\"mcafee_epo_new_username\\\"):\\n    row.user_name = inputs.get(\\\"mcafee_epo_new_username\\\")\\n    note += \\\"Username updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_new_username\\\"))\\n  if inputs.get(\\\"mcafee_epo_fullname\\\"):\\n    row.full_name = inputs.get(\\\"mcafee_epo_fullname\\\")\\n    note += \\\"Full name updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_fullname\\\"))\\n  if inputs.get(\\\"mcafee_epo_email\\\"):\\n    row.email = inputs.get(\\\"mcafee_epo_email\\\")\\n    note += \\\"Email updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_email\\\"))\\n  if inputs.get(\\\"mcafee_epo_phone_number\\\"):\\n    row.phone_number = inputs.get(\\\"mcafee_epo_phone_number\\\")\\n    note += \\\"Phone number updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_phone_number\\\"))\\n  if inputs.get(\\\"mcafee_epo_user_disabled\\\") != None:\\n    row.disabled = bool(inputs.get(\\\"mcafee_epo_user_disabled\\\"))\\n    note += \\\"User disbaled updated: {}\\\\n\\\".format(bool(inputs.get(\\\"mcafee_epo_user_disabled\\\")))\\n  if inputs.get(\\\"mcafee_epo_admin\\\") != None:\\n    row.admin = bool(inputs.get(\\\"mcafee_epo_admin\\\"))\\n    note += \\\"Admin updated: {}\\\\n\\\".format(bool(inputs.get(\\\"mcafee_epo_admin\\\")))\\n  if inputs.get(\\\"mcafee_epo_notes\\\"):\\n    row.notes = inputs.get(\\\"mcafee_epo_notes\\\")\\n    note += \\\"Notes updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_notes\\\"))\\n  if inputs.get(\\\"mcafee_epo_allowed_ips\\\"):\\n    row.allowed_ips = inputs.get(\\\"mcafee_epo_allowed_ips\\\")\\n    note += \\\"Allowed IPs updated: {}\\\\n\\\".format(inputs.get(\\\"mcafee_epo_allowed_ips\\\"))\\n  incident.addNote(\\\"User: {} updated \\\\n{}\\\".format(row.user_name, note))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_admin = rule.properties.epo_admin\\ninputs.mcafee_epo_allowed_ips = rule.properties.epo_allowed_ips\\ninputs.mcafee_epo_email = rule.properties.epo_email\\ninputs.mcafee_epo_fullname = rule.properties.epo_full_name\\ninputs.mcafee_epo_notes = rule.properties.epo_notes\\ninputs.mcafee_epo_pass = rule.properties.epo_user_password\\ninputs.mcafee_epo_phone_number = rule.properties.epo_phone_number\\ninputs.mcafee_epo_user_disabled = rule.properties.epo_user_disbabled\\ninputs.mcafee_epo_username = row.user_name\\ninputs.mcafee_epo_new_username = rule.properties.epo_new_username\\ninputs.mcafee_epo_subjectdn = rule.properties.epo_subject_dn\\ninputs.mcafee_epo_windowsdomain = rule.properties.epo_windows_domain\\ninputs.mcafee_epo_windowsusername = rule.properties.epo_windows_username\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mecdzt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vq8hdo\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1mecdzt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1trazkd\"/\u003e\u003cendEvent id=\"EndEvent_18pse67\"\u003e\u003cincoming\u003eSequenceFlow_1vq8hdo\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vq8hdo\" sourceRef=\"ServiceTask_1trazkd\" targetRef=\"EndEvent_18pse67\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1trazkd\" id=\"ServiceTask_1trazkd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"246\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mecdzt\" id=\"SequenceFlow_1mecdzt_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"246\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"222\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_18pse67\" id=\"EndEvent_18pse67_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"387\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"405\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vq8hdo\" id=\"SequenceFlow_1vq8hdo_di\"\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"387\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"366.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Update a user on the ePO server",
      "export_key": "mcafee_epo_update_user",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546138208,
      "name": "McAfee ePO Update User",
      "object_type": "mcafee_epo_users",
      "programmatic_name": "mcafee_epo_update_user",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "cee811c6-4dda-459f-b1a0-ebdfef3bd932",
      "workflow_id": 38
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_delete_system",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_delete_system\" isExecutable=\"true\" name=\"McAfee ePO Delete System\"\u003e\u003cdocumentation\u003eDelete a system from the ePO server\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1naoxaz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_11n97ur\" name=\"McAfee ePO Delete System\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4011b9c6-eeba-49da-b5f7-27fdce026c83\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  row.deleted = True\\n  incident.addNote(\\\"System: {} deleted\\\".format(row.system_name))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_system_name_or_id = row.system_name\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1naoxaz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1uesimp\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1naoxaz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_11n97ur\"/\u003e\u003cendEvent id=\"EndEvent_170sr3p\"\u003e\u003cincoming\u003eSequenceFlow_1uesimp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1uesimp\" sourceRef=\"ServiceTask_11n97ur\" targetRef=\"EndEvent_170sr3p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_11n97ur\" id=\"ServiceTask_11n97ur_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"241\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1naoxaz\" id=\"SequenceFlow_1naoxaz_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"241\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_170sr3p\" id=\"EndEvent_170sr3p_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"372\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"390\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uesimp\" id=\"SequenceFlow_1uesimp_di\"\u003e\u003comgdi:waypoint x=\"341\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"372\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"356.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Delete a system from the ePO server",
      "export_key": "mcafee_epo_delete_system",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546137757,
      "name": "McAfee ePO Delete System",
      "object_type": "mcafee_epo_systems",
      "programmatic_name": "mcafee_epo_delete_system",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "802f6b84-79ab-4cfc-9bfd-391b0cc668d8",
      "workflow_id": 35
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "mcafee_epo_add_permission_sets_to_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"mcafee_epo_add_permission_sets_to_user\" isExecutable=\"true\" name=\"McAfee ePO Add Permission Sets to user\"\u003e\u003cdocumentation\u003eAdd permission set(s) to a ePO user\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1qai4av\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1agj64n\" name=\"McAfee ePO Add Permission sets to...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6492efd0-43f0-4078-943e-46e033ceccb6\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results[\u0027success\u0027]:\\n  if rule.properties.epo_username not in row.users:\\n    if row.users:\\n      row.users = \\\"{}, {}\\\".format(row.users, rule.properties.epo_username)\\n    else:\\n      row.users = rule.properties.epo_username\\n    incident.addNote(\\\"Permissions set: {} was added to user: {}\\\".format(row.permission_set_name, rule.properties.epo_username))\\n  else:\\n    incident.addNote(\\\"User: {} already has permission set: {}\\\".format(rule.properties.epo_username, row.permission_set_name))\",\"post_processing_script_language\":\"python\",\"pre_processing_script\":\"inputs.mcafee_epo_username = rule.properties.epo_username\\ninputs.mcafee_epo_permsetname = row.permission_set_name\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1qai4av\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vzs8pb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1qai4av\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1agj64n\"/\u003e\u003cendEvent id=\"EndEvent_0hq0pnj\"\u003e\u003cincoming\u003eSequenceFlow_1vzs8pb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vzs8pb\" sourceRef=\"ServiceTask_1agj64n\" targetRef=\"EndEvent_0hq0pnj\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1agj64n\" id=\"ServiceTask_1agj64n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"240\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qai4av\" id=\"SequenceFlow_1qai4av_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"240\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hq0pnj\" id=\"EndEvent_0hq0pnj_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"403\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"421\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vzs8pb\" id=\"SequenceFlow_1vzs8pb_di\"\u003e\u003comgdi:waypoint x=\"340\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"403\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"371.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Add permission set(s) to a ePO user",
      "export_key": "mcafee_epo_add_permission_sets_to_user",
      "last_modified_by": "b@example.com",
      "last_modified_time": 1664546135663,
      "name": "McAfee ePO Add Permission Sets to user",
      "object_type": "mcafee_epo_permission_sets",
      "programmatic_name": "mcafee_epo_add_permission_sets_to_user",
      "tags": [
        {
          "tag_handle": "fn_mcafee_epo",
          "value": null
        }
      ],
      "uuid": "4bc06720-11c4-4486-939a-092d3d27cd3d",
      "workflow_id": 21
    }
  ],
  "workspaces": []
}
