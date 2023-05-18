{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "REST API",
      "id": 45,
      "logic_type": "all",
      "message_destinations": [],
      "name": "REST API",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "358ff4b4-9046-4f92-aa36-5386d53b83ab",
      "view_items": [],
      "workflows": [
        "rest_api"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1684419730751,
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
      "export_key": "__function/rest_api_method",
      "hide_notification": false,
      "id": 446,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_method",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_method",
      "tooltip": "",
      "type_id": 11,
      "uuid": "984922d9-24f1-444f-8967-8199742c8bf9",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "GET",
          "properties": null,
          "uuid": "dbd52017-9fb5-430f-9791-90a86e0f8a7b",
          "value": 102
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "HEAD",
          "properties": null,
          "uuid": "b8cc8517-0d5f-4cd9-958e-30fe0d2822ec",
          "value": 103
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "POST",
          "properties": null,
          "uuid": "b4627fb2-de27-4776-b6e5-7cefb3823fad",
          "value": 104
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PUT",
          "properties": null,
          "uuid": "34e698d5-d533-4982-99ff-decc295efc77",
          "value": 105
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DELETE",
          "properties": null,
          "uuid": "9f0463a3-c12c-40a1-9add-4295566daea1",
          "value": 106
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "OPTIONS",
          "properties": null,
          "uuid": "e0b8ac0a-1f29-471b-9fca-3b6b7e5031ba",
          "value": 107
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "PATCH",
          "properties": null,
          "uuid": "e6857ebe-27f1-48bf-84b2-66481548306c",
          "value": 108
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
      "export_key": "__function/rest_api_timeout",
      "hide_notification": false,
      "id": 447,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_timeout",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_timeout",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a1f12637-495d-4de6-a332-130a497bda5c",
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
      "export_key": "__function/rest_api_cookies",
      "hide_notification": false,
      "id": 448,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_cookies",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 1,
          "name": "rest_api_cookie_example",
          "template": {
            "content": "cookie1: one\ncookie2: two",
            "format": "text"
          },
          "uuid": "ecd1463f-c60d-43f5-9437-f5dbb8d7ff71"
        }
      ],
      "text": "rest_api_cookies",
      "tooltip": "",
      "type_id": 11,
      "uuid": "c999b7b4-0638-4979-9676-043ea8550f52",
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
      "export_key": "__function/rest_api_allowed_status_codes",
      "hide_notification": false,
      "id": 449,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_allowed_status_codes",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_allowed_status_codes",
      "tooltip": "Comma separated list",
      "type_id": 11,
      "uuid": "d380e625-4828-4726-9f85-9d588aeeb159",
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
      "export_key": "__function/rest_api_verify",
      "hide_notification": false,
      "id": 450,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_verify",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_verify",
      "tooltip": "Verify SSL certificate",
      "type_id": 11,
      "uuid": "d978e98d-f0a9-407d-b797-e18f83d43e24",
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
      "export_key": "__function/rest_api_headers",
      "hide_notification": false,
      "id": 451,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_headers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_headers",
      "tooltip": "",
      "type_id": 11,
      "uuid": "db425783-b537-4b32-bd14-0aa247524857",
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
      "export_key": "__function/rest_api_body",
      "hide_notification": false,
      "id": 452,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_body",
      "tooltip": "",
      "type_id": 11,
      "uuid": "30a4cbd0-09bd-488e-bde6-f1765a14aa8d",
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
      "export_key": "__function/rest_api_url",
      "hide_notification": false,
      "id": 453,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "rest_api_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "rest_api_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7d537dd9-c07d-4bb8-8135-e09eb4fe7896",
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
      "created_date": 1683544797494,
      "description": {
        "content": "This function calls a REST web service. It supports the standard REST methods: GET, HEAD, POST, PUT, DELETE, PATCH and OPTIONS.\n\nThe function parameters determine the type of call, the URL, and optionally the headers and body. The results include the text or structured (JSON) result from the web service, and additional information including the elapsed time.",
        "format": "text"
      },
      "destination_handle": "fn_rest_api",
      "display_name": "REST API",
      "export_key": "rest_api",
      "id": 21,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1683544797541,
      "name": "rest_api",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"ok\": true, \"url\": \"https://postman-echo.com/get\", \"status_code\": 200, \"reason\": \"OK\", \"cookies\": {\"sails.sid\": \"s%3AC3qSgEkPLbzV-xtRnnqe-p7zt80yQSTm.SJf3XOyooMFo0wQ8wiWfCzlgieNUBQGRNtSo%2BRSXw54\"}, \"headers\": {\"Date\": \"Thu, 02 Mar 2023 23:47:12 GMT\", \"Content-Type\": \"application/json; charset=utf-8\", \"Content-Length\": \"486\", \"Connection\": \"close\", \"ETag\": \"W/\\\"1e6-/Slr9JmNLSHXgTt5sCvAphvtWyI\\\"\", \"set-cookie\": \"sails.sid=s%3AC3qSgEkPLbzV-xtRnnqe-p7zt80yQSTm.SJf3XOyooMFo0wQ8wiWfCzlgieNUBQGRNtSo%2BRSXw54; Path=/; HttpOnly\"}, \"elapsed\": 711, \"apparent_encoding\": \"ascii\", \"text\": \"{\\n  \\\"args\\\": {\\n    \\\"key\\\": \\\"8.8.8.8\\\"\\n  },\\n  \\\"headers\\\": {\\n    \\\"x-forwarded-proto\\\": \\\"https\\\",\\n    \\\"x-forwarded-port\\\": \\\"443\\\",\\n    \\\"host\\\": \\\"postman-echo.com\\\",\\n    \\\"x-amzn-trace-id\\\": \\\"Root=1-64013580-54708cb41d08344e2a8af58b\\\",\\n    \\\"content-length\\\": \\\"18\\\",\\n    \\\"user-agent\\\": \\\"python-requests/2.28.1\\\",\\n    \\\"accept-encoding\\\": \\\"gzip, deflate\\\",\\n    \\\"accept\\\": \\\"*/*\\\",\\n    \\\"content-type\\\": \\\"application/json\\\",\\n    \\\"x-frooble\\\": \\\"Baz\\\",\\n    \\\"authorization\\\": \\\"\\\"\\n  },\\n  \\\"url\\\": \\\"https://postman-echo.com/get\\\"\\n}\", \"json\": {\"args\": {\"key\": \"8.8.8.8\"}, \"headers\": {\"x-forwarded-proto\": \"https\", \"x-forwarded-port\": \"443\", \"host\": \"postman-echo.com\", \"x-amzn-trace-id\": \"Root=1-64013580-54708cb41d08344e2a8af58b\", \"content-length\": \"18\", \"user-agent\": \"python-requests/2.28.1\", \"accept-encoding\": \"gzip, deflate\", \"accept\": \"*/*\", \"content-type\": \"application/json\", \"x-frooble\": \"Baz\", \"authorization\": \"\"}, \"url\": \"https://postman-echo.com/get\"}, \"links\": {}}, \"raw\": null, \"inputs\": {\"rest_api_headers\": \"Content-Type: application/json\\nX-Frooble: Baz\\nAuthorization: {{auth_header}}\", \"rest_api_method\": \"GET\", \"rest_api_verify\": true, \"rest_api_allowed_status_codes\": \" 305,404,500\", \"rest_api_url\": \"https://postman-echo.com/get\", \"rest_api_body\": \"{\\\"key\\\": \\\"8.8.8.8\\\"}\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-rest-api\", \"package_version\": \"1.0.0\", \"host\": \"My Host\", \"execution_time_ms\": 731, \"timestamp\": \"2023-03-02 18:47:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"ok\": {\"type\": \"boolean\"}, \"url\": {\"type\": \"string\"}, \"status_code\": {\"type\": \"integer\"}, \"reason\": {\"type\": \"string\"}, \"cookies\": {\"type\": \"object\", \"properties\": {\"sails.sid\": {\"type\": \"string\"}}}, \"headers\": {\"type\": \"object\", \"properties\": {\"Date\": {\"type\": \"string\"}, \"Content-Type\": {\"type\": \"string\"}, \"Content-Length\": {\"type\": \"string\"}, \"Connection\": {\"type\": \"string\"}, \"ETag\": {\"type\": \"string\"}, \"set-cookie\": {\"type\": \"string\"}}}, \"elapsed\": {\"type\": \"integer\"}, \"apparent_encoding\": {\"type\": \"string\"}, \"text\": {\"type\": \"string\"}, \"json\": {\"type\": \"object\", \"properties\": {\"args\": {\"type\": \"object\", \"properties\": {\"key\": {\"type\": \"string\"}}}, \"headers\": {\"type\": \"object\", \"properties\": {\"x-forwarded-proto\": {\"type\": \"string\"}, \"x-forwarded-port\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"x-amzn-trace-id\": {\"type\": \"string\"}, \"content-length\": {\"type\": \"string\"}, \"user-agent\": {\"type\": \"string\"}, \"accept-encoding\": {\"type\": \"string\"}, \"accept\": {\"type\": \"string\"}, \"content-type\": {\"type\": \"string\"}, \"x-frooble\": {\"type\": \"string\"}, \"authorization\": {\"type\": \"string\"}}}, \"url\": {\"type\": \"string\"}}}, \"links\": {\"type\": \"object\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"rest_api_headers\": {\"type\": \"string\"}, \"rest_api_method\": {\"type\": \"string\"}, \"rest_api_verify\": {\"type\": \"boolean\"}, \"rest_api_allowed_status_codes\": {\"type\": \"string\"}, \"rest_api_url\": {\"type\": \"string\"}, \"rest_api_body\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "5f728e3d-a4a0-4c6f-9f09-04468edc4d10",
      "version": 1,
      "view_items": [
        {
          "content": "984922d9-24f1-444f-8967-8199742c8bf9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7d537dd9-c07d-4bb8-8135-e09eb4fe7896",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "db425783-b537-4b32-bd14-0aa247524857",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c999b7b4-0638-4979-9676-043ea8550f52",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "30a4cbd0-09bd-488e-bde6-f1765a14aa8d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d978e98d-f0a9-407d-b797-e18f83d43e24",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1f12637-495d-4de6-a332-130a497bda5c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d380e625-4828-4726-9f85-9d588aeeb159",
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
          "name": "REST API",
          "object_type": "artifact",
          "programmatic_name": "rest_api",
          "tags": [],
          "uuid": null,
          "workflow_id": 31
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 22,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1684419728354,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1684419728354,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "4ca9be46-9da9-4f24-8d14-d950cb932770",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "c77b2ac5-96a4-4408-a32f-ed1fcaa5aea7"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_rest_api",
      "name": "fn_rest_api",
      "programmatic_name": "fn_rest_api",
      "tags": [],
      "users": [],
      "uuid": "f48d3cce-8d24-4afe-a79f-28df9c4c5b19"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 55,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_1570b076_796d_44b2_b916_10a69b2ffee8\" isExecutable=\"true\" name=\"playbook_1570b076_796d_44b2_b916_10a69b2ffee8\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0c2h19h\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"REST API\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5f728e3d-a4a0-4c6f-9f09-04468edc4d10\"\u003e{\"inputs\":{\"d978e98d-f0a9-407d-b797-e18f83d43e24\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"984922d9-24f1-444f-8967-8199742c8bf9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"dbd52017-9fb5-430f-9791-90a86e0f8a7b\"}},\"7d537dd9-c07d-4bb8-8135-e09eb4fe7896\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"db425783-b537-4b32-bd14-0aa247524857\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"c999b7b4-0638-4979-9676-043ea8550f52\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"30a4cbd0-09bd-488e-bde6-f1765a14aa8d\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"\"}}},\"a1f12637-495d-4de6-a332-130a497bda5c\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[]}},\"d380e625-4828-4726-9f85-9d588aeeb159\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"pre_processing_script\":\"# SECRETS\\n# -------\\n# For sensitive information that may be included in the rest_header, rest_url, rest_body, or \\n# rest_cookies, you can substitute values from the app.conf. To do so simply create a Key\\n# and a value pair in app.conf and then directly reference the key here using\\n# double-curly brace.\\n#\\n#    Example:\\n#    --------\\n#\\n#      headers = \\\"\\\"\\\"\\n#      Content-Type: application/json\\n#      X-Frooble: Baz\\n#      Authorization: {{auth_header}}\\n#      \\\"\\\"\\\"\\n#\\n# INPUT FORMAT\\n# ------------\\n# rest_api_url, rest_api_method and rest_api_verify are mandatory fields.\\n# rest_api_headers, rest_api_cookies, rest_api_body can accept 2 different formats.\\n#\\n# 1. New-line separated (Legacy)\\n#    ---------------------------\\n#\\n#    This format allows for specifying inputs as key-value pairs, separated\\n#    by a new line. It let\u0027s us create quick and easy inputs that is properly\\n#    formatted for the request. The primary purpose of this format is to retain\\n#    backwards compatibility.\\n#\\n#    Note:  This format does not support complex data structures such as lists\\n#    -----  or nested Key-value pairs.\\n#\\n#    Example:\\n#    -------- \\n#      body = \\\"\\\"\\\"\\n#      name : user1\\n#      password : p@ssword1\\n#      role : admin\\n#      \\\"\\\"\\\"             \\n# \\n#      headers = \\\"\\\"\\\"\\n#      Content-Type: application/json\\n#      X-Frooble: Baz\\n#      Authorization: {{auth_header}}\\n#\\n#\\n#\\n# 2. JSON format:\\n#    ------------\\n#\\n#    Standard json file format. Supports complex data structures such as lists\\n#    or nested Key-value pairs.\\n#\\n#    Example:\\n#    --------\\n#      body = \\\"\\\"\\\"\\n#      \\\"name\\\" : \\\"user1\\\",\\n#      \\\"password\\\" : \\\"p@ssword1\\\",\\n#      \\\"role\\\" : \\\"admin\\\",\\n#      \\\"content\\\" : { \\\"site_url\\\" : \\\"www.example.com\\\", \\\"users\\\" : [\\\"user1\\\", \\\"user2\\\"] }\\n#      \\\"\\\"\\\"      \\n#\\n#\\n#    Hint:\\n#    -----\\n#\\n#    An easier way to feed inputs to the above mentioned fields would be using\\n#    python dictionaries. While the inputs don\u0027t directly support dict, the in-built \\n#    json package can be used to convert a python dict to json string.\\n#\\n#    Example:\\n#    --------\\n#      import json\\n#     \\n#      body = {\\n#       \\\"name\\\"     : \\\"user1\\\",\\n#       \\\"password\\\" : \\\"p@ssword1\\\",\\n#       \\\"role\\\"     : \\\"admin\\\",\\n#       \\\"content\\\"  : { \\n#          \\\"site_url\\\" : \\\"www.example.com\\\",\\n#          \\\"users\\\"    : [\\\"user1\\\", \\\"user2\\\"]\\n#          }\\n#      }\\n#     \\n#     inputs.rest_api_body = json.dumps(body) # this converts the dict to a json string\\n#\\n# \\\"\\\"\\\"\\n\\nmethod = \\\"POST\\\"\\n\\nurl = \\\"https://www.example.com\\\"\\n\\nheader = \\\"\\\"\\\"\\nAuthorization : {{auth_header}}\\nContent-type  : application/json\\n\\\"\\\"\\\"\\n\\nbody = \\\"\\\"\\\"\\n\\\"displayName\\\"  : \\\"Library Assist\\\",\\n\\\"mailEnabled\\\"  : true,\\n\\\"mailNickname\\\" : \\\"library\\\",\\n\\\"securityEnabled\\\" : true,\\n\\\"groupTypes\\\": [\\\"Unified\\\"]\\n\\\"\\\"\\\"\\n\\ncookie  = None\\nverify  = True\\ntimeout = 60\\nallowed_status_code = \\\"305, 400, 404, 500\\\"\\n\\ninputs.rest_api_url     = url                          # Endpoint url\\ninputs.rest_api_headers = header if header else None   # Request headers used for Authorization\\ninputs.rest_api_cookies = cookie if cookie else None   # Cookies for request\\ninputs.rest_api_body    = body if body else None       # Request body\\ninputs.rest_api_verify  = verify if verify else True   # (Boolean) indicates whether to verify SSL certificates.\\ninputs.rest_api_timeout = timeout if timeout else 600  # Request timeout\\ninputs.rest_api_allowed_status_codes = allowed_status_code if allowed_status_code else \\\"200\\\" # Status codes in a comma separated fashion\\ninputs.rest_api_method  = method if method and method in [\\\"GET\\\", \\\"HEAD\\\", \\\"POST\\\", \\\"PUT\\\", \\\"DELETE\\\", \\\"OPTIONS\\\"] else \\\"GET\\\" #REST methods: GET, HEAD, POST, PUT, DELETE and OPTIONS\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"rest_response\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0c2h19h\u003c/incoming\u003e\u003coutgoing\u003eFlow_08s6wnz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0c2h19h\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Process REST Response\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"aa0a4d4f-19f0-472b-8c0e-a4b271013452\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_08s6wnz\u003c/incoming\u003e\u003coutgoing\u003eFlow_150opgb\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_08s6wnz\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_150opgb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_150opgb\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1570b076_796d_44b2_b916_10a69b2ffee8\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_150opgb\" id=\"Flow_150opgb_di\"\u003e\u003comgdi:waypoint x=\"520\" y=\"432\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"484\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_08s6wnz\" id=\"Flow_08s6wnz_di\"\u003e\u003comgdi:waypoint x=\"520\" y=\"292\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"348\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0c2h19h\" id=\"Flow_0c2h19h_di\"\u003e\u003comgdi:waypoint x=\"520\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"208\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.4\" x=\"429\" y=\"114\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"422\" y=\"208\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"422\" y=\"348\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.15\" x=\"454\" y=\"484\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1683545830838,
      "creator_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_1570b076_796d_44b2_b916_10a69b2ffee8",
      "description": {
        "content": "This is a general-purpose function to call any REST API or other HTTP service.",
        "format": "text"
      },
      "display_name": "REST API (PB)",
      "export_key": "rest_api_pb",
      "field_type_handle": "playbook_1570b076_796d_44b2_b916_10a69b2ffee8",
      "fields_type": {
        "actions": [],
        "display_name": "REST API (PB)",
        "export_key": "playbook_1570b076_796d_44b2_b916_10a69b2ffee8",
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
        "type_name": "playbook_1570b076_796d_44b2_b916_10a69b2ffee8",
        "uuid": "8beb9082-8e46-4a00-8840-2c1fb31c6ef6"
      },
      "has_logical_errors": false,
      "id": 25,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1684418517451,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1683547528577,
          "description": "Script to process Endpoint response.",
          "enabled": false,
          "export_key": "Process REST Response",
          "id": 22,
          "language": "python3",
          "last_modified_by": "admin@example.com",
          "last_modified_time": 1683892472263,
          "name": "Process REST Response",
          "object_type": "artifact",
          "playbook_handle": "rest_api_pb",
          "programmatic_name": "rest_api_pb_process_rest_response",
          "script_text": "\u0027\u0027\u0027\nresults = {\n  \"ok\"      : response.ok,\n  \"url\"     : response.url,\n  \"reason\"  : response.reason,\n  \"cookies\" : dedup_dict(response.cookies),\n  \"headers\" : dedup_dict(response.headers),\n  \"elapsed\" : int(response.elapsed.total_seconds() * 1000.0),\n  \"text\"    : response.text,\n  \"json\"    : response_json,\n  \"links\"   : response.links,\n  \"status_code\": response.status_code,\n  \"apparent_encoding\": response.apparent_encoding,\n}\n\u0027\u0027\u0027\n\nresult = playbook.functions.results.rest_response\n\nif not result.success:\n  incident.addNote(helper.createRichText(result.reason))\n\nelse:\n  response_text = result.content.get(\"text\")\n  if artifact.description:\n    artifact.description = u\"{}\\n\\n{}\".format(artifact.description.content, response_text)\n  else:\n    artifact.description = response_text \n",
          "tags": [],
          "uuid": "aa0a4d4f-19f0-472b-8c0e-a4b271013452"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "rest_api_pb",
      "object_type": "artifact",
      "status": "disabled",
      "tag": {
        "display_name": "Playbook_1570b076-796d-44b2-b916-10a69b2ffee8",
        "id": 28,
        "name": "playbook_1570b076_796d_44b2_b916_10a69b2ffee8",
        "type": "playbook",
        "uuid": "c967a567-18ee-4258-a8f1-158662a2f30a"
      },
      "tags": [],
      "type": "default",
      "uuid": "1570b076-796d-44b2-b916-10a69b2ffee8",
      "version": 60
    }
  ],
  "regulators": null,
  "roles": [],
  "scripts": [],
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
        "version": 3,
        "workflow_id": "rest_api",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"rest_api\" isExecutable=\"true\" name=\"REST API\"\u003e\u003cdocumentation\u003eThis is a general-purpose function to call any REST API or other HTTP service.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1urcf3t\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0cdo3j1\"\u003e\u003cincoming\u003eSequenceFlow_1c7guvs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1urcf3t\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1c3e64q\"/\u003e\u003cserviceTask id=\"ServiceTask_1c3e64q\" name=\"REST API\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5f728e3d-a4a0-4c6f-9f09-04468edc4d10\"\u003e{\"inputs\":{\"984922d9-24f1-444f-8967-8199742c8bf9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"dbd52017-9fb5-430f-9791-90a86e0f8a7b\"}}},\"post_processing_script\":\"\u0027\u0027\u0027\\nSet the artifact description to the Response (in plain text) of the REST call\\n\\nresults = {\\n  \\\"ok\\\": response.ok,\\n  \\\"url\\\": response.url,\\n  \\\"status_code\\\": response.status_code,\\n  \\\"reason\\\": response.reason,\\n  \\\"cookies\\\": dedup_dict(response.cookies),\\n  \\\"headers\\\": dedup_dict(response.headers),\\n  \\\"elapsed\\\": int(response.elapsed.total_seconds() * 1000.0),\\n  \\\"apparent_encoding\\\": response.apparent_encoding,\\n  \\\"text\\\": response.text,\\n  \\\"json\\\": response_json,\\n  \\\"links\\\": response.links,\\n}\\n\u0027\u0027\u0027\\n\\nif not results.success:\\n  incident.addNote(helper.createRichText(results.reason))\\n\\nelse:\\n  response_text = results.content.get(\\\"text\\\")\\n  if artifact.description:\\n    artifact.description = u\\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, response_text)\\n  else:\\n    artifact.description = response_text\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# SECRETS\\n# -------\\n# For sensitive information that may be included in the rest_header, rest_url, rest_body, or \\n# rest_cookies, you can substitute values from the app.conf. To do so simply create a Key\\n# and a value pair in app.conf and then directly reference the key here using\\n# double-curly brace.\\n#\\n#    Example:\\n#    --------\\n#\\n#      headers = \\\"\\\"\\\"\\n#      Content-Type: application/json\\n#      X-Frooble: Baz\\n#      Authorization: {{auth_header}}\\n#      \\\"\\\"\\\"\\n#\\n# INPUT FORMAT\\n# ------------\\n# rest_api_url, rest_api_method and rest_api_verify are mandatory fields.\\n# rest_api_headers, rest_api_cookies, rest_api_body can accept 2 different formats.\\n#\\n# 1. New-line separated (Legacy)\\n#    ---------------------------\\n#\\n#    This format allows for specifying inputs as key-value pairs, separated\\n#    by a new line. It let\u0027s us create quick and easy inputs that is properly\\n#    formatted for the request. The primary purpose of this format is to retain\\n#    backwards compatibility.\\n#\\n#    Note:  This format does not support complex data structures such as lists\\n#    -----  or nested Key-value pairs.\\n#\\n#    Example:\\n#    -------- \\n#      body = \\\"\\\"\\\"\\n#      name : user1\\n#      password : p@ssword1\\n#      role : admin\\n#      \\\"\\\"\\\"             \\n# \\n#      headers = \\\"\\\"\\\"\\n#      Content-Type: application/json\\n#      X-Frooble: Baz\\n#      Authorization: {{auth_header}}\\n#\\n#\\n#\\n# 2. JSON format:\\n#    ------------\\n#\\n#    Standard json file format. Supports complex data structures such as lists\\n#    or nested Key-value pairs.\\n#\\n#    Example:\\n#    --------\\n#      body = \\\"\\\"\\\"\\n#      \\\"name\\\" : \\\"user1\\\",\\n#      \\\"password\\\" : \\\"p@ssword1\\\",\\n#      \\\"role\\\" : \\\"admin\\\",\\n#      \\\"content\\\" : { \\\"site_url\\\" : \\\"www.example.com\\\", \\\"users\\\" : [\\\"user1\\\", \\\"user2\\\"] }\\n#      \\\"\\\"\\\"      \\n#\\n#\\n#    Hint:\\n#    -----\\n#\\n#    An easier way to feed inputs to the above mentioned fields would be using\\n#    python dictionaries. While the inputs don\u0027t directly support dict, the in-built \\n#    json package can be used to convert a python dict to json string.\\n#\\n#    Example:\\n#    --------\\n#      import json\\n#     \\n#      body = {\\n#       \\\"name\\\"     : \\\"user1\\\",\\n#       \\\"password\\\" : \\\"p@ssword1\\\",\\n#       \\\"role\\\"     : \\\"admin\\\",\\n#       \\\"content\\\"  : { \\n#          \\\"site_url\\\" : \\\"www.example.com\\\",\\n#          \\\"users\\\"    : [\\\"user1\\\", \\\"user2\\\"]\\n#          }\\n#      }\\n#     \\n#     inputs.rest_api_body = json.dumps(body) # this converts the dict to a json string\\n#\\n# \\\"\\\"\\\"\\n\\nmethod = \\\"POST\\\"\\n\\nurl = \\\"https://www.example.com\\\"\\n\\nheader = \\\"\\\"\\\"\\nAuthorization : {{auth_header}}\\nContent-type  : application/json\\n\\\"\\\"\\\"\\n\\nbody = \\\"\\\"\\\"\\n\\\"displayName\\\"  : \\\"Library Assist\\\",\\n\\\"mailEnabled\\\"  : true,\\n\\\"mailNickname\\\" : \\\"library\\\",\\n\\\"securityEnabled\\\" : true,\\n\\\"groupTypes\\\": [\\\"Unified\\\"]\\n\\\"\\\"\\\"\\n\\ncookie  = None\\nverify  = True\\ntimeout = 60\\nallowed_status_code = \\\"305, 400, 404, 500\\\"\\n\\ninputs.rest_api_url     = url                          # Endpoint url\\ninputs.rest_api_headers = header if header else None   # Request headers used for Authorization\\ninputs.rest_api_cookies = cookie if cookie else None   # Cookies for request\\ninputs.rest_api_body    = body if body else None       # Request body\\ninputs.rest_api_verify  = verify if verify else True   # (Boolean) indicates whether to verify SSL certificates.\\ninputs.rest_api_timeout = timeout if timeout else 600  # Request timeout\\ninputs.rest_api_allowed_status_codes = allowed_status_code if allowed_status_code else \\\"200\\\" # Status codes in a comma separated fashion\\ninputs.rest_api_method  = method if method and method in [\\\"GET\\\", \\\"HEAD\\\", \\\"POST\\\", \\\"PUT\\\", \\\"DELETE\\\", \\\"OPTIONS\\\"] else \\\"GET\\\" #REST methods: GET, HEAD, POST, PUT, DELETE and OPTIONS\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1urcf3t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1c7guvs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1c7guvs\" sourceRef=\"ServiceTask_1c3e64q\" targetRef=\"EndEvent_0cdo3j1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13lun7v\"\u003e\u003ctext\u003eResults are appended to the artifact description\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10ck7zh\" sourceRef=\"ServiceTask_1c3e64q\" targetRef=\"TextAnnotation_13lun7v\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0cdo3j1\" id=\"EndEvent_0cdo3j1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"511\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"529\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1urcf3t\" id=\"SequenceFlow_1urcf3t_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"302\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"250\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1c3e64q\" id=\"ServiceTask_1c3e64q_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"302\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1c7guvs\" id=\"SequenceFlow_1c7guvs_di\"\u003e\u003comgdi:waypoint x=\"402\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"511\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"456.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13lun7v\" id=\"TextAnnotation_13lun7v_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"103\" x=\"436\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10ck7zh\" id=\"Association_10ck7zh_di\"\u003e\u003comgdi:waypoint x=\"398\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"450\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "This is a general-purpose function to call any REST API or other HTTP service.",
      "export_key": "rest_api",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1684419721263,
      "name": "REST API",
      "object_type": "artifact",
      "programmatic_name": "rest_api",
      "tags": [],
      "uuid": "27e9c285-c17b-49d0-98bb-421e58443f50",
      "workflow_id": 31
    }
  ],
  "workspaces": []
}
