{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1745591590869,
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
      "export_key": "__function/fn_watsonx_analyst_arguments",
      "hide_notification": false,
      "id": 341,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_arguments",
      "operation_perms": {},
      "operations": [],
      "placeholder": "foo,bar,foobar",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_arguments",
      "tooltip": "Comma-separated arguments to replace \u0027{}\u0027s in the prompt",
      "type_id": 11,
      "uuid": "af6262f7-170e-415d-b4ae-1246d35b4471",
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
      "export_key": "__function/fn_watsonx_analyst_attachment_id",
      "hide_notification": false,
      "id": 333,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_attachment_id",
      "tooltip": "You can use data navigator to set this field.",
      "type_id": 11,
      "uuid": "afeb37ea-774a-4f57-8429-ada6cd754fae",
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
      "export_key": "__function/fn_watsonx_analyst_task_id",
      "hide_notification": false,
      "id": 334,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "task.id",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_task_id",
      "tooltip": "Optional Task ID. If this is set to a non-null value, the attachment will be assumed to belong to a task.",
      "type_id": 11,
      "uuid": "cecff544-3780-4902-adaa-0fc3c510af43",
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
      "export_key": "__function/fn_watsonx_analyst_model_id",
      "hide_notification": false,
      "id": 335,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_model_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_model_id",
      "tooltip": "Which watsonx.ai generative AI model to use to perform the task?",
      "type_id": 11,
      "uuid": "d76f1086-f760-4edb-915d-c96732276b8d",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-3-2b-instruct",
          "properties": null,
          "uuid": "7d026b4a-4950-407f-af3e-a37d9d74c0b3",
          "value": 59
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-3-8b-instruct",
          "properties": null,
          "uuid": "bc839b03-48b7-456a-910e-05e5ac66acb8",
          "value": 60
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-3-2-8b-instruct",
          "properties": null,
          "uuid": "f7880d06-57ea-4950-bb9b-4fe3cd080cfc",
          "value": 66
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-3-3-8b-instruct",
          "properties": null,
          "uuid": "594887db-64bd-4f59-ba55-4225fb5b5cf0",
          "value": 67
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-8b-code-instruct",
          "properties": null,
          "uuid": "934cd609-5eae-49f0-89e0-4d3bc8af4911",
          "value": 68
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "meta-llama/llama-3-405b-instruct",
          "properties": null,
          "uuid": "71477844-51a9-4f5e-b22c-854e822e9a92",
          "value": 70
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "meta-llama/llama-3-2-90b-vision-instruct",
          "properties": null,
          "uuid": "da04d545-15e9-4b5a-9efd-226eeb59b638",
          "value": 72
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "meta-llama/llama-3-3-70b-instruct",
          "properties": null,
          "uuid": "c49da377-ca16-42d4-91f0-1e3e914a42cb",
          "value": 73
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "mistralai/mistral-large",
          "properties": null,
          "uuid": "c26a6745-205a-4f17-a00e-cae905b0f26d",
          "value": 64
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "mistralai/mixtral-8x7b-instruct-v01",
          "properties": null,
          "uuid": "7536082d-3212-404f-95a0-15d2d4118d56",
          "value": 65
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
      "export_key": "__function/fn_watsonx_analyst_incident_id",
      "hide_notification": false,
      "id": 336,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "2095",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_incident_id",
      "tooltip": "You can use Data Navigator for this",
      "type_id": 11,
      "uuid": "e31918e0-c67b-44a7-9f40-760a08cb95d1",
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
      "export_key": "__function/fn_watsonx_analyst_artifact_id",
      "hide_notification": false,
      "id": 337,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_artifact_id",
      "tooltip": "You can use data navigator to add this.",
      "type_id": 11,
      "uuid": "4e3aa3c0-0168-4644-a4e6-cf0f81bc5e59",
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
      "export_key": "__function/fn_watsonx_analyst_note_id",
      "hide_notification": false,
      "id": 338,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_note_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_note_id",
      "tooltip": "ID for the Incident note to respond to. You can use Data Navigator.",
      "type_id": 11,
      "uuid": "538595f0-6797-4c1c-8bf7-b2e2f9947af2",
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
      "export_key": "__function/fn_watsonx_analyst_prompt",
      "hide_notification": false,
      "id": 342,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_prompt",
      "operation_perms": {},
      "operations": [],
      "placeholder": "Tell me about this incident.",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_prompt",
      "tooltip": "What you are asking the LLM",
      "type_id": 11,
      "uuid": "5ed1a15d-cb99-4b1e-98dc-1b215e95a291",
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
      "export_key": "__function/fn_watsonx_analyst_system_prompt",
      "hide_notification": false,
      "id": 343,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "fn_watsonx_analyst_system_prompt",
      "operation_perms": {},
      "operations": [],
      "placeholder": "You are a helpful AI assistant knowledgeable in cyber security. You are inoffensive, and respond clearly, and concisely.",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "fn_watsonx_analyst_system_prompt",
      "tooltip": "Optional grounding prompt",
      "type_id": 11,
      "uuid": "791d44e9-2ad1-4c18-9e00-c03d9e6a794c",
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
      "created_date": 1744877429361,
      "description": {
        "content": "Allow conversation in an incident\u0027s Notes tab. Will take previous notes as context.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx.ai Converse via Notes",
      "export_key": "fn_watsonx_analyst_converse_via_notes",
      "id": 5,
      "last_modified_by": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1744877429361,
      "name": "fn_watsonx_analyst_converse_via_notes",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"generated_text\": \"\u003cp\u003eText from watsonx.ai\u003c/p\u003e\", \"raw_output\": \"Text from watsonx.ai\", \"tag\": \"HTML model tag to be prefixed before any AI-generated content\", \"metadata\": {\"model_id\": \"ibm/granite-3-2b-instruct\", \"stop_reason\": \"EOS token\", \"created_at\": \"2023-07-21T16:52:32.190Z\", \"generated_token_count\": 8, \"input_token_count\": 10}}",
      "output_json_schema": "{\"type\": \"object\", \"properties\": {\"generated_text\": {\"type\": \"string\"}, \"raw_output\": {\"type\": \"string\"}, \"tag\": {\"type\": \"string\"}, \"metadata\": {\"type\": \"object\", \"properties\": {\"model_id\": {\"type\": \"string\"}, \"stop_reason\": {\"type\": \"string\"}, \"created_at\": {\"type\": \"string\"}, \"generated_token_count\": {\"type\": \"number\"}, \"input_token_count\": {\"type\": \"number\"}}}}}",
      "tags": [],
      "uuid": "74f46f9b-364a-4884-b7ad-418bd9a7ac9a",
      "version": 0,
      "view_items": [
        {
          "content": "e31918e0-c67b-44a7-9f40-760a08cb95d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "538595f0-6797-4c1c-8bf7-b2e2f9947af2",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d76f1086-f760-4edb-915d-c96732276b8d",
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
      "created_date": 1744877429479,
      "description": {
        "content": "Use watsonx.ai to scan an artifact, and assess whether the artifact indicates any malicious activity.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx.ai Scan Artifact",
      "export_key": "fn_watsonx_analyst_scan_artifact",
      "id": 6,
      "last_modified_by": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1744877429479,
      "name": "fn_watsonx_analyst_scan_artifact",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"generated_text\": \"\u003cp\u003eText from watsonx.ai\u003c/p\u003e\", \"raw_output\": \"Text from watsonx.ai\", \"tag\": \"HTML model tag to be prefixed before any AI-generated content\", \"metadata\": {\"model_id\": \"ibm/granite-3-2b-instruct\", \"stop_reason\": \"EOS token\", \"created_at\": \"2023-07-21T16:52:32.190Z\", \"generated_token_count\": 8, \"input_token_count\": 10}}",
      "output_json_schema": "{\"type\": \"object\", \"properties\": {\"generated_text\": {\"type\": \"string\"}, \"raw_output\": {\"type\": \"string\"}, \"tag\": {\"type\": \"string\"}, \"metadata\": {\"type\": \"object\", \"properties\": {\"model_id\": {\"type\": \"string\"}, \"stop_reason\": {\"type\": \"string\"}, \"created_at\": {\"type\": \"string\"}, \"generated_token_count\": {\"type\": \"number\"}, \"input_token_count\": {\"type\": \"number\"}}}}}",
      "tags": [],
      "uuid": "7df11ea0-1613-4b45-89b7-e15335a60889",
      "version": 0,
      "view_items": [
        {
          "content": "e31918e0-c67b-44a7-9f40-760a08cb95d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4e3aa3c0-0168-4644-a4e6-cf0f81bc5e59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d76f1086-f760-4edb-915d-c96732276b8d",
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
      "created_date": 1744877429598,
      "description": {
        "content": "Use watsonx.ai to scan an attachment, and assess whether it indicates any malicious activity. This function will treat the attachment as an artifact, and as such will assume some level of danger or malicious activity.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx.ai Scan Attachment",
      "export_key": "fn_watsonx_analyst_scan_attachment",
      "id": 7,
      "last_modified_by": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1744877429598,
      "name": "fn_watsonx_analyst_scan_attachment",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"generated_text\": \"\u003cp\u003eText from watsonx.ai\u003c/p\u003e\", \"raw_output\": \"Text from watsonx.ai\", \"tag\": \"HTML model tag to be prefixed before any AI-generated content\", \"metadata\": {\"model_id\": \"ibm/granite-3-2b-instruct\", \"stop_reason\": \"EOS token\", \"created_at\": \"2023-07-21T16:52:32.190Z\", \"generated_token_count\": 8, \"input_token_count\": 10}}",
      "output_json_schema": "{\"type\": \"object\", \"properties\": {\"generated_text\": {\"type\": \"string\"}, \"raw_output\": {\"type\": \"string\"}, \"tag\": {\"type\": \"string\"}, \"metadata\": {\"type\": \"object\", \"properties\": {\"model_id\": {\"type\": \"string\"}, \"stop_reason\": {\"type\": \"string\"}, \"created_at\": {\"type\": \"string\"}, \"generated_token_count\": {\"type\": \"number\"}, \"input_token_count\": {\"type\": \"number\"}}}}}",
      "tags": [],
      "uuid": "6d06f8cb-af62-4ce0-9d78-b8d29a1b2c28",
      "version": 0,
      "view_items": [
        {
          "content": "e31918e0-c67b-44a7-9f40-760a08cb95d1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cecff544-3780-4902-adaa-0fc3c510af43",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "afeb37ea-774a-4f57-8429-ada6cd754fae",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d76f1086-f760-4edb-915d-c96732276b8d",
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
      "created_date": 1745582541475,
      "description": {
        "content": "Perform Text Generation using watsonx.ai. Can replace \u0027{}\u0027 in prompts with comma-separated strings in `fn_watsonx_analyst_arguments`.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx.ai Text Generation",
      "export_key": "fn_watsonx_analyst_text_generation",
      "id": 9,
      "last_modified_by": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1745582541475,
      "name": "fn_watsonx_analyst_text_generation",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"generated_text\": \"\u003cp\u003eText from watsonx.ai\u003c/p\u003e\", \"raw_output\": \"Text from watsonx.ai\", \"tag\": \"HTML model tag to be prefixed before any AI-generated content\", \"metadata\": {\"model_id\": \"ibm/granite-3-2b-instruct\", \"stop_reason\": \"EOS token\", \"created_at\": \"2023-07-21T16:52:32.190Z\", \"generated_token_count\": 8, \"input_token_count\": 10}}",
      "output_json_schema": "{\"type\": \"object\", \"properties\": {\"generated_text\": {\"type\": \"string\"}, \"raw_output\": {\"type\": \"string\"}, \"tag\": {\"type\": \"string\"}, \"metadata\": {\"type\": \"object\", \"properties\": {\"model_id\": {\"type\": \"string\"}, \"stop_reason\": {\"type\": \"string\"}, \"created_at\": {\"type\": \"string\"}, \"generated_token_count\": {\"type\": \"number\"}, \"input_token_count\": {\"type\": \"number\"}}}}}",
      "tags": [],
      "uuid": "011baa28-1a1d-490c-8e6d-05dfb71740e7",
      "version": 0,
      "view_items": [
        {
          "content": "791d44e9-2ad1-4c18-9e00-c03d9e6a794c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5ed1a15d-cb99-4b1e-98dc-1b215e95a291",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "af6262f7-170e-415d-b4ae-1246d35b4471",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d76f1086-f760-4edb-915d-c96732276b8d",
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
  "id": 2,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1745591588502,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1745591588502,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "d2785e8a-5cb2-4be4-a739-b561196fb439"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_watsonx_analyst",
      "name": "watsonx.ai Message Destination",
      "programmatic_name": "fn_watsonx_analyst",
      "tags": [],
      "users": [],
      "uuid": "b5f677d6-9f6f-488f-8591-3fb17faba5b8"
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
              "field_name": "note.text",
              "method": "contains",
              "type": null,
              "value": "@watsonx"
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
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\" isExecutable=\"true\" name=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_04063g6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_04063g6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_5\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jcyraf\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"watsonx.ai Respond to note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dd832d95-76f5-4da4-b6bf-e73c471a22dd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_018f7pl\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jcyraf\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0jcyraf\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"watsonx.ai Converse via Notes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74f46f9b-364a-4884-b7ad-418bd9a7ac9a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.fn_watsonx_analyst_incident_id = incident.id\\ninputs.fn_watsonx_analyst_model_id = \\\"ibm/granite-3-2b-instruct\\\"\\ninputs.fn_watsonx_analyst_note_id = note.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04063g6\u003c/incoming\u003e\u003coutgoing\u003eFlow_018f7pl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_018f7pl\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_018f7pl\" id=\"Flow_018f7pl_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jcyraf\" id=\"Flow_0jcyraf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04063g6\" id=\"Flow_04063g6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.6328\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744877430549,
      "creator_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "deployment_id": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
      "description": {
        "content": "This Playbook is triggered when a user writes a note that contains \"@watsonx\" at the start of the note. \n\nA reply will be generated by IBM watsonx.ai generative AI, and added as a reply to the first note.",
        "format": "text"
      },
      "display_name": "watsonx.ai Note Conversation",
      "export_key": "fn_watsonx_analyst_note_conversation",
      "field_type_handle": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
      "fields_type": {
        "actions": [],
        "display_name": "watsonx.ai Note Conversation",
        "export_key": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
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
        "type_name": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
        "uuid": "b39a7275-eb78-4328-aacb-9089e0ffe4bf"
      },
      "has_logical_errors": false,
      "id": 5,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1745582542661,
      "local_scripts": [],
      "name": "fn_watsonx_analyst_note_conversation",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_75573cee-9116-46ef-8924-c89260100fe8",
        "id": 6,
        "name": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
        "type": "playbook",
        "uuid": "32510d2d-15b5-4772-bf51-cce41ea4592f"
      },
      "tags": [],
      "type": "default",
      "uuid": "75573cee-9116-46ef-8924-c89260100fe8",
      "version": 5
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\" isExecutable=\"true\" name=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1tvpqhi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"watsonx.ai Respond to note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dd832d95-76f5-4da4-b6bf-e73c471a22dd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0of5sbk\u003c/incoming\u003e\u003coutgoing\u003eFlow_0te23h2\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0te23h2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0te23h2\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_1tvpqhi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_4\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"watsonx.ai Converse via Notes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74f46f9b-364a-4884-b7ad-418bd9a7ac9a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.fn_watsonx_analyst_incident_id = incident.id\\ninputs.fn_watsonx_analyst_model_id = \\\"ibm/granite-3-2b-instruct\\\"\\ninputs.fn_watsonx_analyst_note_id = note.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tvpqhi\u003c/incoming\u003e\u003coutgoing\u003eFlow_0of5sbk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0of5sbk\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0of5sbk\" id=\"Flow_0of5sbk_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tvpqhi\" id=\"Flow_1tvpqhi_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0te23h2\" id=\"Flow_0te23h2_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"474\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.6406\" x=\"640\" y=\"94\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744877431350,
      "creator_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "deployment_id": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
      "description": {
        "content": "If a response fails to be generated, you can use this playbook on a note with a query for `@watsonx` to try again.",
        "format": "text"
      },
      "display_name": "watsonx.ai Retry Note Conversation",
      "export_key": "fn_watsonx_analyst_retry_note_conversation",
      "field_type_handle": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
      "fields_type": {
        "actions": [],
        "display_name": "watsonx.ai Retry Note Conversation",
        "export_key": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
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
        "type_name": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
        "uuid": "95636cb0-f871-49fc-ad21-0f8f08cbfd83"
      },
      "has_logical_errors": false,
      "id": 6,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1745582543724,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "note.text",
              "method": "contains",
              "type": null,
              "value": "@watsonx"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "fn_watsonx_analyst_retry_note_conversation",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_d59ecd99-5b7a-49ae-8854-488792b9b231",
        "id": 7,
        "name": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
        "type": "playbook",
        "uuid": "27cbbcf1-818b-4b93-8787-f538d6a68168"
      },
      "tags": [],
      "type": "default",
      "uuid": "d59ecd99-5b7a-49ae-8854-488792b9b231",
      "version": 5
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 2,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\" isExecutable=\"true\" name=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0mi3un1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_0mi3un1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_5\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0c1pci3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"watsonx.ai Add Artifact Report to Notes\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"789d1193-b7f9-4401-9829-59bd4830d350\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_16e8jb6\u003c/incoming\u003e\u003coutgoing\u003eFlow_0c1pci3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0c1pci3\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"watsonx.ai Scan Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7df11ea0-1613-4b45-89b7-e15335a60889\"\u003e{\"inputs\":{\"d76f1086-f760-4edb-915d-c96732276b8d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7d026b4a-4950-407f-af3e-a37d9d74c0b3\"}},\"e31918e0-c67b-44a7-9f40-760a08cb95d1\":{\"expression_input\":{\"expression\":\"incident.id\"},\"input_type\":\"expression\"},\"4e3aa3c0-0168-4644-a4e6-cf0f81bc5e59\":{\"expression_input\":{\"expression\":\"artifact.id\"},\"input_type\":\"expression\"}},\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0mi3un1\u003c/incoming\u003e\u003coutgoing\u003eFlow_16e8jb6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_16e8jb6\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_16e8jb6\" id=\"Flow_16e8jb6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0c1pci3\" id=\"Flow_0c1pci3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0mi3un1\" id=\"Flow_0mi3un1_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"54\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744877432116,
      "creator_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "deployment_id": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
      "description": {
        "content": "Watsonx reads the contents of the provided artifact if an attachment is supplied. \nThen, Watsonx gives a summary of the contents, and threat scores.",
        "format": "text"
      },
      "display_name": "watsonx.ai Scan Artifact",
      "export_key": "fn_watsonx_analyst_scan_artifact",
      "field_type_handle": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
      "fields_type": {
        "actions": [],
        "display_name": "watsonx.ai Scan Artifact",
        "export_key": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
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
        "type_name": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
        "uuid": "132dd4fa-6097-4926-a60b-ff0ff49527f0"
      },
      "has_logical_errors": false,
      "id": 7,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1744877432945,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.attachment",
              "method": "has_a_value",
              "type": null,
              "value": null
            }
          ],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "\u003cdiv style=\"max-width: 750.0px;\"\u003e\n  \u003cp\u003e\n    This playbook shows the contents of this artifact to an LLM on watsonx.ai,\n    which will give a summary of the contents, and indicate whether\n    the artifact may be malicious or not.\n  \u003c/p\u003e\n  \u003cbr /\u003e\n  \u003cp\u003e\n    Large artifacts will take a long time, and will take many watsonx.ai tokens to generate.\n  \u003c/p\u003e\n\n  \u003cp style=\"margin: 1.0em 0;\"\u003e\n    \u003cstrong\u003e\n      The output of this summarization will be added to the Incident\u0027s\n      notes.\n    \u003c/strong\u003e\n  \u003c/p\u003e\n\u003c/div\u003e",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "fn_watsonx_analyst_scan_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_86ace61c-324b-44fc-8c07-795f7f47827b",
        "id": 8,
        "name": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
        "type": "playbook",
        "uuid": "ebc6e8a3-701c-41dd-adbb-4c8617827686"
      },
      "tags": [],
      "type": "default",
      "uuid": "86ace61c-324b-44fc-8c07-795f7f47827b",
      "version": 4
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 3,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_6d973c7c_318b_4be6_bf6a_277caacde397\" isExecutable=\"true\" name=\"playbook_6d973c7c_318b_4be6_bf6a_277caacde397\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0ra6mvx\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"watsonx.ai Scan Attachment\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6d06f8cb-af62-4ce0-9d78-b8d29a1b2c28\"\u003e{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.fn_watsonx_analyst_model_id = \\\"ibm/granite-3-2b-instruct\\\"\\ninputs.fn_watsonx_analyst_incident_id = incident.id\\ninputs.fn_watsonx_analyst_attachment_id = attachment.id\\nif task:\\n  inputs.fn_watsonx_analyst_task_id = task.id\\nelse:\\n  inputs.fn_watsonx_analyst_task_id = None\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0ra6mvx\u003c/incoming\u003e\u003coutgoing\u003eFlow_0mw9b6l\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0ra6mvx\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"watsonx.ai Add Attatchment Report to Notes\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"72655ae1-5d6c-47dd-ab45-883cc02d87eb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0mw9b6l\u003c/incoming\u003e\u003coutgoing\u003eFlow_0ioa0oi\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0mw9b6l\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0ioa0oi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0ioa0oi\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_6d973c7c_318b_4be6_bf6a_277caacde397\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ioa0oi\" id=\"Flow_0ioa0oi_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"402\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"464\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0mw9b6l\" id=\"Flow_0mw9b6l_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"272\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"318\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0ra6mvx\" id=\"Flow_0ra6mvx_di\"\u003e\u003comgdi:waypoint x=\"722\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"722\" y=\"188\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"209.125\" x=\"617\" y=\"94\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"188\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"624\" y=\"318\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"656\" y=\"464\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744877432900,
      "creator_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "deployment_id": "playbook_6d973c7c_318b_4be6_bf6a_277caacde397",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "watsonx.ai Scan Attachment",
      "export_key": "fn_watsonx_analyst_scan_attachment",
      "field_type_handle": "playbook_6d973c7c_318b_4be6_bf6a_277caacde397",
      "fields_type": {
        "actions": [],
        "display_name": "watsonx.ai Scan Attachment",
        "export_key": "playbook_6d973c7c_318b_4be6_bf6a_277caacde397",
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
        "type_name": "playbook_6d973c7c_318b_4be6_bf6a_277caacde397",
        "uuid": "dd3c3a29-09c4-4faa-a4f0-625254d78984"
      },
      "has_logical_errors": false,
      "id": 8,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Admin",
        "id": 4,
        "name": "admin@co3sys.com",
        "type": "user"
      },
      "last_modified_time": 1745582544286,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1744877433054,
          "description": "",
          "enabled": false,
          "export_key": "watsonx.ai Add Attatchment Report to Notes",
          "id": 7,
          "language": "python3",
          "last_modified_by": "admin@co3sys.com",
          "last_modified_time": 1744877433054,
          "name": "watsonx.ai Add Attatchment Report to Notes",
          "object_type": "attachment",
          "playbook_handle": "fn_watsonx_analyst_scan_attachment",
          "programmatic_name": "fn_watsonx_analyst_scan_attachment_6d973c7c_318b_4be6_bf6a_277caacde397_watsonxai_add_attatchment_report_to_notes",
          "script_text": "\ngenerated_text = playbook.functions.results.ai_response[\"content\"][\"generated_text\"]\ntag = playbook.functions.results.ai_response[\"content\"][\"tag\"]\n\nif generated_text:\n  generated_text = generated_text.strip()\n  incident.addNote(tag + generated_text)\n",
          "tags": [],
          "uuid": "72655ae1-5d6c-47dd-ab45-883cc02d87eb"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "\u003cdiv style=\"max-width: 750.0px;\"\u003e\n  \u003cp\u003e\n    This playbook shows the contents of this attachment to an LLM on watsonx.ai,\n    which will give a summary of the contents, and may indicate whether\n    the attachment may be malicious or not.\n  \u003c/p\u003e\n  \u003cbr /\u003e\n  \u003cp\u003e\n    Large attachments will take a long time, and will take many watsonx.ai tokens to generate.\n  \u003c/p\u003e\n\n  \u003cp style=\"margin: 1.0em 0;\"\u003e\n    \u003cstrong\u003e\n      The output of this summarization will be added to the Incident\u0027s\n      notes.\n    \u003c/strong\u003e\n  \u003c/p\u003e\n\u003c/div\u003e",
            "element": "html",
            "field_type": null,
            "show_if": null,
            "show_link_header": false,
            "step_label": null
          }
        ]
      },
      "name": "fn_watsonx_analyst_scan_attachment",
      "object_type": "attachment",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_6d973c7c-318b-4be6-bf6a-277caacde397",
        "id": 9,
        "name": "playbook_6d973c7c_318b_4be6_bf6a_277caacde397",
        "type": "playbook",
        "uuid": "33934c7c-f4cc-4391-83be-6d0ace193d6f"
      },
      "tags": [],
      "type": "default",
      "uuid": "6d973c7c-318b-4be6-bf6a-277caacde397",
      "version": 5
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1744877428087,
      "description": "",
      "enabled": false,
      "export_key": "watsonx.ai Add Artifact Report to Notes",
      "id": 5,
      "language": "python3",
      "last_modified_by": "admin@co3sys.com",
      "last_modified_time": 1744877428087,
      "name": "watsonx.ai Add Artifact Report to Notes",
      "object_type": "artifact",
      "playbook_handle": null,
      "programmatic_name": "watsonx_add_note_to_artifact",
      "script_text": "\ngenerated_text = playbook.functions.results.ai_response[\"content\"][\"generated_text\"]\ntag = playbook.functions.results.ai_response[\"content\"][\"tag\"]\n\nif generated_text:\n  generated_text = generated_text.strip()\n  incident.addNote(tag + generated_text)\n",
      "tags": [],
      "uuid": "789d1193-b7f9-4401-9829-59bd4830d350"
    },
    {
      "actions": [],
      "created_date": 1744877428145,
      "description": "",
      "enabled": false,
      "export_key": "watsonx.ai Respond to note",
      "id": 6,
      "language": "python3",
      "last_modified_by": "admin@co3sys.com",
      "last_modified_time": 1744877428145,
      "name": "watsonx.ai Respond to note",
      "object_type": "note",
      "playbook_handle": null,
      "programmatic_name": "watsonx_respond_to_note",
      "script_text": "\ngenerated_text = playbook.functions.results.ai_response[\"content\"][\"generated_text\"]\ntag = playbook.functions.results.ai_response[\"content\"][\"tag\"]\n\nif generated_text != \"\":\n  note.addNote(tag + generated_text)\n",
      "tags": [],
      "uuid": "dd832d95-76f5-4da4-b6bf-e73c471a22dd"
    }
  ],
  "server_version": {
    "build_number": 0,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.0"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
