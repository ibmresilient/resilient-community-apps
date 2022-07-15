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
          "value": "Other File"
        }
      ],
      "enabled": true,
      "export_key": "Parse Image (Artifact)",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [
        "fn_ocr"
      ],
      "name": "Parse Image (Artifact)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "277afaba-2fc0-4251-b787-097207f4b81c",
      "view_items": [
        {
          "content": "2e03ffd5-6398-4ff1-a064-7bfe83aa4afa",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "667fcdd2-53f2-4f47-814e-8bb36901dc4a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "parse_image"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Parse Image (Attachment)",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [
        "fn_ocr"
      ],
      "name": "Parse Image (Attachment)",
      "object_type": "attachment",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "c0862b14-5f9e-4af4-a532-b26592e3f802",
      "view_items": [
        {
          "content": "2e03ffd5-6398-4ff1-a064-7bfe83aa4afa",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "667fcdd2-53f2-4f47-814e-8bb36901dc4a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "parse_image_attachment"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Parse Image (Base64)",
      "id": 16,
      "logic_type": "all",
      "message_destinations": [
        "fn_ocr"
      ],
      "name": "Parse Image (Base64)",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b83af406-afb1-4df7-808f-d2cd58c56977",
      "view_items": [
        {
          "content": "2e03ffd5-6398-4ff1-a064-7bfe83aa4afa",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "667fcdd2-53f2-4f47-814e-8bb36901dc4a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aee46497-748b-4b70-ae7c-99697d1156f4",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "parse_image_base64"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1657825902089,
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
      "export_key": "__function/ocr_incident_id",
      "hide_notification": false,
      "id": 274,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "843f9fcc-5dcd-463e-975f-476b9d6e7aef",
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
      "export_key": "__function/ocr_attachment_id",
      "hide_notification": false,
      "id": 271,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_attachment_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_attachment_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "de40eefc-0ddd-434b-bd88-d52b9cf1ef88",
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
      "export_key": "__function/ocr_language",
      "hide_notification": false,
      "id": 275,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_language",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_language",
      "tooltip": "Language that the OCR should look for. If the wrong language is selected, the app may not return the best possible prediction",
      "type_id": 11,
      "uuid": "f68e397a-c89a-4d1c-ad3e-c4de71006d11",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "eng",
          "properties": null,
          "uuid": "35ce524f-3a34-40f9-ae46-bebb39f4c275",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ara",
          "properties": null,
          "uuid": "a259b707-2fd9-4edb-b4d2-eb9f43611a1a",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "chi_sim",
          "properties": null,
          "uuid": "7a292535-de23-488e-826a-16b5d5e3dcc2",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "chi_tra",
          "properties": null,
          "uuid": "37e5e550-24e7-460d-a366-09e911e75920",
          "value": 55
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "rus",
          "properties": null,
          "uuid": "86330af8-1ef0-4d03-b6b1-e736c3a26262",
          "value": 56
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "spa",
          "properties": null,
          "uuid": "81946a12-c119-4e84-92ba-9ad4c95982a4",
          "value": 57
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
      "export_key": "__function/ocr_base64",
      "hide_notification": false,
      "id": 272,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_base64",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_base64",
      "tooltip": "",
      "type_id": 11,
      "uuid": "166063ce-ba2c-44d8-b0d1-b4f23edfddec",
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
      "export_key": "__function/ocr_confidence_threshold",
      "hide_notification": false,
      "id": 273,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_confidence_threshold",
      "operation_perms": {},
      "operations": [],
      "placeholder": "50",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_confidence_threshold",
      "tooltip": "Lowest confidence to consider when returning predictions",
      "type_id": 11,
      "uuid": "1fd2afd8-9a4c-4fed-a949-57ca75f8bda1",
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
      "export_key": "__function/ocr_artifact_id",
      "hide_notification": false,
      "id": 270,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_artifact_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_artifact_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "3eb378b2-405f-4e05-a758-576f9a1e612b",
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
      "export_key": "__function/ocr_task_id",
      "hide_notification": false,
      "id": 276,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "templates": [],
      "text": "ocr_task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "52470066-4238-4d46-a6ab-51e38ed376c1",
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
      "export_key": "actioninvocation/ocr_base64",
      "hide_notification": false,
      "id": 280,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_base64",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Base 64 String",
      "tooltip": "The Base64 String of an Image to be Parsed",
      "type_id": 6,
      "uuid": "aee46497-748b-4b70-ae7c-99697d1156f4",
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
      "export_key": "actioninvocation/ocr_language",
      "hide_notification": false,
      "id": 278,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_language",
      "operation_perms": {},
      "operations": [],
      "placeholder": "eng",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "OCR Language",
      "tooltip": "Language that the OCR should look for. If the wrong language is selected, the app may not return the best possible prediction",
      "type_id": 6,
      "uuid": "2e03ffd5-6398-4ff1-a064-7bfe83aa4afa",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "eng",
          "properties": null,
          "uuid": "879a4905-5c0b-4101-99c3-26619aed1961",
          "value": 58
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ara",
          "properties": null,
          "uuid": "edd6fcae-ba2f-46c7-89b3-ff5a36c6dbba",
          "value": 59
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "chi_sim",
          "properties": null,
          "uuid": "86ac6e0d-f505-413f-bc98-45ef83eaa7eb",
          "value": 60
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "chi_tra",
          "properties": null,
          "uuid": "2f388d91-92da-45ef-a9c5-42a9d9d0cc1a",
          "value": 61
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "deu",
          "properties": null,
          "uuid": "711104a9-c11c-48b9-84ea-9bf336108260",
          "value": 64
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "fra",
          "properties": null,
          "uuid": "8b585b6e-aef6-4621-87a2-cb8960f12df9",
          "value": 65
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "jpn",
          "properties": null,
          "uuid": "7287d12d-c1db-44b0-b48f-b104517b4700",
          "value": 66
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "kor",
          "properties": null,
          "uuid": "7416594d-cbdf-46e0-82eb-6e63961bec29",
          "value": 67
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "rus",
          "properties": null,
          "uuid": "9f3eaf5d-6db4-487f-a9d2-d2f9cfdbf0e8",
          "value": 62
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "spa",
          "properties": null,
          "uuid": "9dc7d6b2-06c1-464b-8416-46e48956b040",
          "value": 63
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
      "export_key": "actioninvocation/ocr_confidence_threshold",
      "hide_notification": false,
      "id": 279,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "ocr_confidence_threshold",
      "operation_perms": {},
      "operations": [],
      "placeholder": "50",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Confidence Threshold",
      "tooltip": "Lowest confidence to consider when returning predictions",
      "type_id": 6,
      "uuid": "667fcdd2-53f2-4f47-814e-8bb36901dc4a",
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
      "created_date": 1656440792750,
      "description": {
        "content": "Runs OCR on an image in byte string format and returns the relevant results",
        "format": "text"
      },
      "destination_handle": "fn_ocr",
      "display_name": "Read Text From Image Bytes",
      "export_key": "fn_ocr",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656615849897,
      "name": "fn_ocr",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": [{\"text\": \"Description\", \"confidence\": 93.921173}], \"raw\": null, \"inputs\": {\"ocr_confidence_threshold\": 49, \"ocr_artifact_id\": 23, \"ocr_language\": \"eng\", \"ocr_task_id\": null, \"ocr_base64\": null, \"ocr_incident_id\": 2098}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-ocr\", \"package_version\": \"1.0.0\", \"host\": \"Host\", \"execution_time_ms\": 1161, \"timestamp\": \"2022-06-27 14:08:28\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"text\": {\"type\": \"string\"}, \"confidence\": {\"type\": \"number\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ocr_confidence_threshold\": {\"type\": \"integer\"}, \"ocr_artifact_id\": {\"type\": \"integer\"}, \"ocr_language\": {\"type\": \"string\"}, \"ocr_task_id\": {}, \"ocr_base64\": {\"type\": \"string\"}, \"ocr_incident_id\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "uuid": "c690d533-585f-4b9d-a6c8-9d570f2fac5c",
      "version": 4,
      "view_items": [
        {
          "content": "166063ce-ba2c-44d8-b0d1-b4f23edfddec",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "de40eefc-0ddd-434b-bd88-d52b9cf1ef88",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "52470066-4238-4d46-a6ab-51e38ed376c1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f68e397a-c89a-4d1c-ad3e-c4de71006d11",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "843f9fcc-5dcd-463e-975f-476b9d6e7aef",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1fd2afd8-9a4c-4fed-a949-57ca75f8bda1",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3eb378b2-405f-4e05-a758-576f9a1e612b",
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
          "name": "Parse Image (Artifact)",
          "object_type": "artifact",
          "programmatic_name": "parse_image",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        },
        {
          "actions": [],
          "description": null,
          "name": "Parse Image (Attachment)",
          "object_type": "attachment",
          "programmatic_name": "parse_image_attachment",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        },
        {
          "actions": [],
          "description": null,
          "name": "Parse Image (Base64)",
          "object_type": "incident",
          "programmatic_name": "parse_image_base64",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 12,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1657825900600,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1657825900600,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "9824db18-6759-417e-8e70-df0cda45dc68",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_ocr",
      "name": "fn_ocr",
      "programmatic_name": "fn_ocr",
      "tags": [
        {
          "tag_handle": "fn_ocr",
          "value": null
        }
      ],
      "users": [],
      "uuid": "0a542982-0f76-4624-8814-b4b0f814c3fe"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "parse_image",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"parse_image\" isExecutable=\"true\" name=\"Parse Image (Artifact)\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0lk1vog\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0x72p05\" name=\"Read Text From Image Bytes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c690d533-585f-4b9d-a6c8-9d570f2fac5c\"\u003e{\"inputs\":{\"166063ce-ba2c-44d8-b0d1-b4f23edfddec\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"None\"}},\"f68e397a-c89a-4d1c-ad3e-c4de71006d11\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"35ce524f-3a34-40f9-ae46-bebb39f4c275\"}}},\"post_processing_script\":\"content = workflow.properties.ocr_results[\\\"content\\\"]\\n\\nif content is not None:\\n  output_text = \\\"Below are the lines detected by OCR, as well as their confidence scores\\\\n\\\\n\\\"\\n  for line in content:\\n    output_text += \u0027\\\"\u0027 + line[\\\"text\\\"] + f\u0027\\\" \\\\t\\\\t Confidence Score: {round(line[\\\"confidence\\\"],2)}%\\\\n\\\\n\u0027\\n  \\n  \\n  incident.addNote(output_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ocr_incident_id = incident.id\\n# inputs.ocr_attachment_id = attachment.id if attachment.id else None\\ninputs.ocr_artifact_id = artifact.id if artifact.id else None\\ninputs.ocr_task_id = task.id if task and task.id else None\\ninputs.ocr_confidence_threshold = rule.properties.ocr_confidence_threshold\\ninputs.ocr_language = rule.properties.ocr_language\\ninputs.ocr_base64 = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ocr_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0lk1vog\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1m1h8th\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0lk1vog\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0x72p05\"/\u003e\u003cendEvent id=\"EndEvent_02vdjnl\"\u003e\u003cincoming\u003eSequenceFlow_1m1h8th\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1m1h8th\" sourceRef=\"ServiceTask_0x72p05\" targetRef=\"EndEvent_02vdjnl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"179\" y=\"167\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"174\" y=\"202\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"186\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"154\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0x72p05\" id=\"ServiceTask_0x72p05_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"339\" y=\"145\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0lk1vog\" id=\"SequenceFlow_0lk1vog_di\"\u003e\u003comgdi:waypoint x=\"215\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"287\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"287\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"339\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"257\" y=\"178.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02vdjnl\" id=\"EndEvent_02vdjnl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"505.2328638497653\" y=\"197\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"523.2328638497653\" y=\"236\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m1h8th\" id=\"SequenceFlow_1m1h8th_di\"\u003e\u003comgdi:waypoint x=\"439\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"479\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"479\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"494\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "description": "",
      "export_key": "parse_image",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656616404601,
      "name": "Parse Image (Artifact)",
      "object_type": "artifact",
      "programmatic_name": "parse_image",
      "tags": [],
      "uuid": "6e51d47d-0c15-4d81-8ad9-8bca9feeef2b",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "parse_image_attachment",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"parse_image_attachment\" isExecutable=\"true\" name=\"Parse Image (Attachment)\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0mww2ez\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0t2unnc\" name=\"Read Text From Image Bytes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c690d533-585f-4b9d-a6c8-9d570f2fac5c\"\u003e{\"inputs\":{\"f68e397a-c89a-4d1c-ad3e-c4de71006d11\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"35ce524f-3a34-40f9-ae46-bebb39f4c275\"}}},\"post_processing_script\":\"content = workflow.properties.ocr_results[\\\"content\\\"]\\n\\nif content is not None:\\n  output_text = \\\"Below are the lines detected by OCR, as well as their confidence scores\\\\n\\\\n\\\"\\n  for line in content:\\n    output_text += \u0027\\\"\u0027 + line[\\\"text\\\"] + f\u0027\\\" \\\\t\\\\t Confidence Score: {round(line[\\\"confidence\\\"],2)}%\\\\n\\\\n\u0027\\n  \\n  \\n  incident.addNote(output_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ocr_incident_id = incident.id\\ninputs.ocr_attachment_id = attachment.id if attachment.id else None\\n# inputs.ocr_artifact_id = artifact.id if artifact.id else None\\ninputs.ocr_task_id = task.id if task and task.id else None\\ninputs.ocr_confidence_threshold = rule.properties.ocr_confidence_threshold\\ninputs.ocr_language = rule.properties.ocr_language\\ninputs.ocr_base64 = None\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ocr_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0mww2ez\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0y8t2rp\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_04acwe7\"\u003e\u003cincoming\u003eSequenceFlow_0y8t2rp\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0y8t2rp\" sourceRef=\"ServiceTask_0t2unnc\" targetRef=\"EndEvent_04acwe7\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0mww2ez\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0t2unnc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"210\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"205\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"213\" xsi:type=\"omgdc:Point\" y=\"215\"/\u003e\u003comgdi:waypoint x=\"165\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0t2unnc\" id=\"ServiceTask_0t2unnc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"353\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_04acwe7\" id=\"EndEvent_04acwe7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"539.8955223880597\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"557.8955223880597\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0y8t2rp\" id=\"SequenceFlow_0y8t2rp_di\"\u003e\u003comgdi:waypoint x=\"453\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"540\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"496.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mww2ez\" id=\"SequenceFlow_0mww2ez_di\"\u003e\u003comgdi:waypoint x=\"246\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"353\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"299.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "",
      "export_key": "parse_image_attachment",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656616412816,
      "name": "Parse Image (Attachment)",
      "object_type": "attachment",
      "programmatic_name": "parse_image_attachment",
      "tags": [],
      "uuid": "518bfac5-043b-459c-9af4-08b3c4169d08",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "parse_image_base64",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"parse_image_base64\" isExecutable=\"true\" name=\"Parse Image (Base64)\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0u36jkn\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00lupd7\" name=\"Read Text From Image Bytes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c690d533-585f-4b9d-a6c8-9d570f2fac5c\"\u003e{\"inputs\":{\"f68e397a-c89a-4d1c-ad3e-c4de71006d11\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"35ce524f-3a34-40f9-ae46-bebb39f4c275\"}}},\"post_processing_script\":\"content = workflow.properties.ocr_results[\\\"content\\\"]\\n\\nif content is not None:\\n  output_text = \\\"Below are the lines detected by OCR, as well as their confidence scores\\\\n\\\\n\\\"\\n  for line in content:\\n    output_text += \u0027\\\"\u0027 + line[\\\"text\\\"] + f\u0027\\\" \\\\t\\\\t Confidence Score: {round(line[\\\"confidence\\\"],2)}%\\\\n\\\\n\u0027\\n  \\n  \\n  incident.addNote(output_text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ocr_incident_id = incident.id\\n# inputs.ocr_attachment_id = attachment.id if attachment.id else None\\n# inputs.ocr_artifact_id = artifact.id if artifact.id else None\\ninputs.ocr_task_id = task.id if task and task.id else None\\ninputs.ocr_confidence_threshold = rule.properties.ocr_confidence_threshold\\ninputs.ocr_language = rule.properties.ocr_language\\ninputs.ocr_base64 = rule.properties.ocr_base64\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"ocr_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0u36jkn\u003c/incoming\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0u36jkn\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00lupd7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00lupd7\" id=\"ServiceTask_00lupd7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"179\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0u36jkn\" id=\"SequenceFlow_0u36jkn_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"217\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"217\" xsi:type=\"omgdc:Point\" y=\"219\"/\u003e\u003comgdi:waypoint x=\"235\" xsi:type=\"omgdc:Point\" y=\"219\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"232\" y=\"205.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "",
      "export_key": "parse_image_base64",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656541621591,
      "name": "Parse Image (Base64)",
      "object_type": "incident",
      "programmatic_name": "parse_image_base64",
      "tags": [],
      "uuid": "1b8082e7-7e74-481e-9f90-9d7a847c9a74",
      "workflow_id": 3
    }
  ],
  "workspaces": []
}
