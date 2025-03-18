{
  "action_order": [],
  "actions": [],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1732203182162,
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
      "id": 3890,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "export_key": "__function/fn_watsonx_analyst_model_id",
      "hide_notification": false,
      "id": 3891,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "tooltip": "Which watsonx\u2122 generative AI model to use to perform the task?",
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
          "value": 3027
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-3-8b-instruct",
          "properties": null,
          "uuid": "bc839b03-48b7-456a-910e-05e5ac66acb8",
          "value": 3037
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-20b-code-instruct",
          "properties": null,
          "uuid": "02d19faf-9585-46bd-8bdf-2eddc8e25b97",
          "value": 3028
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-34b-code-instruct",
          "properties": null,
          "uuid": "29a5ba70-dc13-4901-90b0-b756721acef7",
          "value": 3029
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ibm/granite-20b-multilingual",
          "properties": null,
          "uuid": "7c2b45c2-9931-4a45-b955-46fd3fc5dc71",
          "value": 3036
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "meta-llama/llama-3-70b-instruct",
          "properties": null,
          "uuid": "debaa62d-5a49-4100-ae07-500d3f656823",
          "value": 3033
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "meta-llama/llama-3-1-70b-instruct",
          "properties": null,
          "uuid": "38363d45-2773-4639-a9ed-5b04d2bdf2bf",
          "value": 3038
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "mistralai/mistral-large",
          "properties": null,
          "uuid": "c26a6745-205a-4f17-a00e-cae905b0f26d",
          "value": 3030
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "mistralai/mixtral-8x7b-instruct-v01",
          "properties": null,
          "uuid": "7536082d-3212-404f-95a0-15d2d4118d56",
          "value": 3042
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
      "id": 3892,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "id": 3894,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "id": 3895,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "id": 3896,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "id": 3897,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "json_example": null,
      "json_schema": null,
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
      "created_date": 1732023985512,
      "description": {
        "content": "Allow conversation in an incident\u0027s Notes tab. Will take previous notes as context.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx\u2122 Converse via Notes",
      "export_key": "fn_watsonx_analyst_converse_via_notes",
      "id": 190,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732202778531,
      "name": "fn_watsonx_analyst_converse_via_notes",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\n  \"generated_text\": \"Text from watsonx.ai\",\n  \"tag\": \"HTML model tag to be prefixed before any AI-generated content\",\n  \"metadata\": {\n    \"model_id\": \"ibm/granite-3-2b-instruct\",\n    \"stop_reason\": \"EOS token\",\n    \"created_at\": \"2023-07-21T16:52:32.190Z\",\n    \"generated_token_count\": 8,\n    \"input_token_count\": 10\n  }\n}",
      "output_json_schema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"generated_text\": {\n      \"type\": \"string\"\n    },\n    \"tag\": {\n      \"type\": \"string\"\n    },\n    \"metadata\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"model_id\": {\n          \"type\": \"string\"\n        },\n        \"stop_reason\": {\n          \"type\": \"string\"\n        },\n        \"created_at\": {\n          \"type\": \"string\"\n        },\n        \"generated_token_count\": {\n          \"type\": \"number\"\n        },\n        \"input_token_count\": {\n          \"type\": \"number\"\n        }\n      }\n    }\n  }\n}",
      "tags": [],
      "uuid": "74f46f9b-364a-4884-b7ad-418bd9a7ac9a",
      "version": 3,
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
      "created_date": 1732023985571,
      "description": {
        "content": "Use watsonx\u2122 to scan an artifact, and assess whether the artifact indicates any malicious activity. Design to work with log files, scripts (e.g. Bash, Python, Lua, Powershell, Perl).",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx\u2122 Scan Artifact",
      "export_key": "fn_watsonx_analyst_scan_artifact",
      "id": 191,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732202769647,
      "name": "fn_watsonx_analyst_scan_artifact",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\n  \"generated_text\": \"Text from watsonx.ai\",\n  \"tag\": \"HTML model tag to be prefixed before any AI-generated content\",\n  \"metadata\": {\n    \"model_id\": \"ibm/granite-3-2b-instruct\",\n    \"stop_reason\": \"EOS token\",\n    \"created_at\": \"2023-07-21T16:52:32.190Z\",\n    \"generated_token_count\": 8,\n    \"input_token_count\": 10\n  }\n}",
      "output_json_schema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"generated_text\": {\n      \"type\": \"string\"\n    },\n    \"tag\": {\n      \"type\": \"string\"\n    },\n    \"metadata\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"model_id\": {\n          \"type\": \"string\"\n        },\n        \"stop_reason\": {\n          \"type\": \"string\"\n        },\n        \"created_at\": {\n          \"type\": \"string\"\n        },\n        \"generated_token_count\": {\n          \"type\": \"number\"\n        },\n        \"input_token_count\": {\n          \"type\": \"number\"\n        }\n      }\n    }\n  }\n}",
      "tags": [],
      "uuid": "7df11ea0-1613-4b45-89b7-e15335a60889",
      "version": 3,
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
          "content": "791d44e9-2ad1-4c18-9e00-c03d9e6a794c",
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
      "created_date": 1732023985628,
      "description": {
        "content": "Perform Text Generation using watsonx.ai. Can replace \u0027{}\u0027 in prompts with comma-separated strings in `fn_watsonx_analyst_arguments`.",
        "format": "text"
      },
      "destination_handle": "fn_watsonx_analyst",
      "display_name": "watsonx\u2122 Text Generation",
      "export_key": "fn_watsonx_analyst_text_generation",
      "id": 192,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732202718462,
      "name": "fn_watsonx_analyst_text_generation",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\n  \"generated_text\": \"Text from watsonx.ai\",\n  \"tag\": \"HTML model tag to be prefixed before any AI-generated content\",\n  \"metadata\":  {\n    \"model_id\": \"ibm/granite-3-2b-instruct\",\n    \"stop_reason\": \"EOS token\",\n    \"created_at\": \"2023-07-21T16:52:32.190Z\",\n    \"generated_token_count\": 8,\n    \"input_token_count\": 10\n  }\n}",
      "output_json_schema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"generated_text\": {\n      \"type\": \"string\"\n    },\n    \"tag\": {\n      \"type\": \"string\"\n    },\n    \"metadata\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"model_id\": {\n          \"type\": \"string\"\n        },\n        \"stop_reason\": {\n          \"type\": \"string\"\n        },\n        \"created_at\": {\n          \"type\": \"string\"\n        },\n        \"generated_token_count\": {\n          \"type\": \"number\"\n        },\n        \"input_token_count\": {\n          \"type\": \"number\"\n        }\n      }\n    }\n  }\n}",
      "tags": [],
      "uuid": "011baa28-1a1d-490c-8e6d-05dfb71740e7",
      "version": 2,
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
  "id": 32,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1732203180278,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1732203180278,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "6beee884-6969-4b12-82ad-7c5eb04bb92b"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_watsonx_analyst",
      "name": "watsonx\u2122 Message Desination",
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
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\" isExecutable=\"true\" name=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_04063g6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_04063g6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_5\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0jcyraf\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"watsonx.ai Respond to note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dd832d95-76f5-4da4-b6bf-e73c471a22dd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_018f7pl\u003c/incoming\u003e\u003coutgoing\u003eFlow_0jcyraf\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0jcyraf\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"watsonx\u2122 Converse via Notes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74f46f9b-364a-4884-b7ad-418bd9a7ac9a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.fn_watsonx_analyst_incident_id = incident.id\\ninputs.fn_watsonx_analyst_model_id = \\\"ibm/granite-3-2b-instruct\\\"\\ninputs.fn_watsonx_analyst_note_id = note.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_04063g6\u003c/incoming\u003e\u003coutgoing\u003eFlow_018f7pl\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_018f7pl\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_75573cee_9116_46ef_8924_c89260100fe8\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_018f7pl\" id=\"Flow_018f7pl_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0jcyraf\" id=\"Flow_0jcyraf_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_04063g6\" id=\"Flow_04063g6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"117\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.6328\" x=\"640\" y=\"65\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2109\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1732023985850,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
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
      "id": 193,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732202909142,
      "local_scripts": [],
      "name": "fn_watsonx_analyst_note_conversation",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_75573cee-9116-46ef-8924-c89260100fe8",
        "id": 234,
        "name": "playbook_75573cee_9116_46ef_8924_c89260100fe8",
        "type": "playbook",
        "uuid": "32510d2d-15b5-4772-bf51-cce41ea4592f"
      },
      "tags": [],
      "type": "default",
      "uuid": "75573cee-9116-46ef-8924-c89260100fe8",
      "version": 8
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 8,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\" isExecutable=\"true\" name=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_1tvpqhi\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"watsonx.ai Respond to note\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"dd832d95-76f5-4da4-b6bf-e73c471a22dd\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0of5sbk\u003c/incoming\u003e\u003coutgoing\u003eFlow_0te23h2\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0te23h2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0te23h2\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003csequenceFlow id=\"Flow_1tvpqhi\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_4\"/\u003e\u003cserviceTask id=\"ServiceTask_4\" name=\"watsonx\u2122 Converse via Notes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"74f46f9b-364a-4884-b7ad-418bd9a7ac9a\"\u003e{\"inputs\":{},\"pre_processing_script\":\"\\ninputs.fn_watsonx_analyst_incident_id = incident.id\\ninputs.fn_watsonx_analyst_model_id = \\\"ibm/granite-3-2b-instruct\\\"\\ninputs.fn_watsonx_analyst_note_id = note.id\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1tvpqhi\u003c/incoming\u003e\u003coutgoing\u003eFlow_0of5sbk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0of5sbk\" sourceRef=\"ServiceTask_4\" targetRef=\"ScriptTask_2\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_d59ecd99_5b7a_49ae_8854_488792b9b231\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0of5sbk\" id=\"Flow_0of5sbk_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"242\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"338\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1tvpqhi\" id=\"Flow_1tvpqhi_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"116\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"158\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0te23h2\" id=\"Flow_0te23h2_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"422\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"474\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"162.6406\" x=\"640\" y=\"64\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"338\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"474\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_4\" id=\"ServiceTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"158\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1732023986127,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
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
        "display_name": "watsonx\u2122 Retry Note Conversation",
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
      "id": 194,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732202902293,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "fn_watsonx_analyst_retry_note_conversation",
      "object_type": "note",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_d59ecd99-5b7a-49ae-8854-488792b9b231",
        "id": 235,
        "name": "playbook_d59ecd99_5b7a_49ae_8854_488792b9b231",
        "type": "playbook",
        "uuid": "27cbbcf1-818b-4b93-8787-f538d6a68168"
      },
      "tags": [],
      "type": "default",
      "uuid": "d59ecd99-5b7a-49ae-8854-488792b9b231",
      "version": 7
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 15,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\" isExecutable=\"true\" name=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0mi3un1\u003c/outgoing\u003e\u003c/startEvent\u003e\u003csequenceFlow id=\"Flow_0mi3un1\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_5\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0c1pci3\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_4\" name=\"watsonx.ai Add Artifact Report to Notes\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"789d1193-b7f9-4401-9829-59bd4830d350\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_16e8jb6\u003c/incoming\u003e\u003coutgoing\u003eFlow_0c1pci3\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_0c1pci3\" sourceRef=\"ScriptTask_4\" targetRef=\"EndPoint_3\"/\u003e\u003cserviceTask id=\"ServiceTask_5\" name=\"watsonx\u2122 Scan Artifact\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7df11ea0-1613-4b45-89b7-e15335a60889\"\u003e{\"inputs\":{\"d76f1086-f760-4edb-915d-c96732276b8d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7d026b4a-4950-407f-af3e-a37d9d74c0b3\"}},\"791d44e9-2ad1-4c18-9e00-c03d9e6a794c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"e31918e0-c67b-44a7-9f40-760a08cb95d1\":{\"expression_input\":{\"expression\":\"incident.id\"},\"input_type\":\"expression\"},\"4e3aa3c0-0168-4644-a4e6-cf0f81bc5e59\":{\"expression_input\":{\"expression\":\"artifact.id\"},\"input_type\":\"expression\"}},\"result_name\":\"ai_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0mi3un1\u003c/incoming\u003e\u003coutgoing\u003eFlow_16e8jb6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_16e8jb6\" sourceRef=\"ServiceTask_5\" targetRef=\"ScriptTask_4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_86ace61c_324b_44fc_8c07_795f7f47827b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_16e8jb6\" id=\"Flow_16e8jb6_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"252\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"308\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0c1pci3\" id=\"Flow_0c1pci3_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"392\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"444\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0mi3un1\" id=\"Flow_0mi3un1_di\"\u003e\u003comgdi:waypoint x=\"721\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"721\" y=\"168\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"630\" y=\"54\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"655\" y=\"444\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_4\" id=\"ScriptTask_4_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"308\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_5\" id=\"ServiceTask_5_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"623\" y=\"168\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1732023986446,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
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
      "id": 195,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 34,
        "name": "thomas@example.com",
        "type": "user"
      },
      "last_modified_time": 1732203160453,
      "local_scripts": [],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": [
          {
            "content": "\u003cdiv style=\"max-width: 750.0px;\"\u003e\n  \u003ch1\u003ewatsonx.ai Scan Artifact\u003c/h1\u003e\n\n  \u003cp\u003e\n    This playbook shows the contents of this artifact to an LLM on watsonx.ai,\n    which will give a summary of the contents, and indicate whether\n    the artifact may be malicious or not.\n  \u003c/p\u003e\n  \u003cbr /\u003e\n  \u003cp\u003e\n    Large artifacts will take a long time, and will take many watsonx.ai tokens to generate.\n  \u003c/p\u003e\n\n  \u003cp style=\"margin: 1.0em 0;\"\u003e\n    \u003cstrong\u003e\n      The output of this summarization will be added to the Incident\u0027s\n      notes.\n    \u003c/strong\u003e\n  \u003c/p\u003e\n\u003c/div\u003e",
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
        "id": 236,
        "name": "playbook_86ace61c_324b_44fc_8c07_795f7f47827b",
        "type": "playbook",
        "uuid": "ebc6e8a3-701c-41dd-adbb-4c8617827686"
      },
      "tags": [],
      "type": "default",
      "uuid": "86ace61c-324b-44fc-8c07-795f7f47827b",
      "version": 13
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1732023985040,
      "description": "",
      "enabled": false,
      "export_key": "watsonx.ai Add Artifact Report to Notes",
      "id": 153,
      "language": "python3",
      "last_modified_by": "thomas@example.com",
      "last_modified_time": 1732202873817,
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
      "created_date": 1732023985017,
      "description": "",
      "enabled": false,
      "export_key": "watsonx.ai Respond to note",
      "id": 152,
      "language": "python3",
      "last_modified_by": "thomas@example.com",
      "last_modified_time": 1732202900432,
      "name": "watsonx.ai Respond to note",
      "object_type": "note",
      "playbook_handle": null,
      "programmatic_name": "watsonx_respond_to_note",
      "script_text": "\ngenerated_text = playbook.functions.results.ai_response[\"content\"][\"generated_text\"]\ntag = playbook.functions.results.ai_response[\"content\"][\"tag\"]\n\nif generated_text != \"\":\n  note.addNote(tag + generated_text)\n",
      "tags": [],
      "uuid": "dd832d95-76f5-4da4-b6bf-e73c471a22dd"
    }
  ],
  "server_version" : {
    "build_number" : 0,
    "f" : 0,
    "m" : 0,
    "major" : 0,
    "minor" : 0,
    "r" : 0,
    "v" : 51,
    "version" : "51.0.0.0.0"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [],
  "workspaces": []
}
