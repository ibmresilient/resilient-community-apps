{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "task.status",
          "method": "changed_to",
          "type": null,
          "value": "Closed"
        }
      ],
      "enabled": true,
      "export_key": "Remedy Close Incident from Task",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Remedy Close Incident from Task",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "0f48b579-f54b-42a8-832e-0cfe2d3178d4",
      "view_items": [],
      "workflows": [
        "close_a_remedy_incident_from_task"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "task.status",
          "method": "equals",
          "type": null,
          "value": "Open"
        }
      ],
      "enabled": true,
      "export_key": "Remedy Create Incident from Task",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Remedy Create Incident from Task",
      "object_type": "task",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "edeb2d07-4321-493a-930d-b04d479d61fa",
      "view_items": [
        {
          "content": "c29d5daa-1a0f-4cc7-882c-f5a2eebab296",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3946b0f6-0e2b-447f-a613-5661c444b9e7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5d0908ad-a469-49f1-bf41-7640323b5797",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "244b09b4-8d97-4197-86e3-08ee195c5f88",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a977f7a7-ef06-4d38-a4ed-f293b5066989",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3ac24106-39a2-4843-9ba0-a92da2f453cf",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "209f2896-2427-48ae-a6e8-45803160ebc5",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8ae7377f-d799-4ad9-af81-9ffece3b29a6",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "076bf9ea-79be-471e-82d4-cc27de3f3ab7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f9831ec1-c511-455f-a142-2c1155c9130d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ba597730-d2f3-4476-b131-0d5b0ee8de7e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "create_a_remedy_incident_from_task"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1619813732960,
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
      "export_key": "__function/incident_id",
      "hide_notification": false,
      "id": 230,
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
          "tag_handle": "fn_remedy",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "incident_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
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
      "export_key": "__function/task_id",
      "hide_notification": false,
      "id": 229,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "task_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        },
        {
          "tag_handle": "fn_utilities",
          "value": null
        }
      ],
      "templates": [],
      "text": "task_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
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
      "export_key": "__function/remedy_payload",
      "hide_notification": false,
      "id": 231,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "remedy_payload",
      "tooltip": "",
      "type_id": 11,
      "uuid": "69575a0b-9ca7-4d57-be72-d7596f1942e1",
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
      "export_key": "__function/remedy_incident_name",
      "hide_notification": false,
      "id": 232,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_incident_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "remedy_incident_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7377a061-c4eb-4008-9822-710b5d2f2248",
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
      "export_key": "actioninvocation/remedy_urgency",
      "hide_notification": false,
      "id": 218,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_urgency",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Urgency",
      "tooltip": "Urgency to assign to the Remedy form",
      "type_id": 6,
      "uuid": "8ae7377f-d799-4ad9-af81-9ffece3b29a6",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "1-Critical",
          "properties": null,
          "uuid": "a84342c0-8084-4457-8ea4-1d40f6738409",
          "value": 52
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "2-High",
          "properties": null,
          "uuid": "e571569c-5c7a-48ca-bea0-a2719bc2e541",
          "value": 53
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "3-Medium",
          "properties": null,
          "uuid": "05c6e6c2-62f4-4d50-9946-49a97ace3dd2",
          "value": 54
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "4-Low",
          "properties": null,
          "uuid": "598471fb-2b98-432c-ab6f-54ed8b454a06",
          "value": 55
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
      "export_key": "actioninvocation/remedy_note",
      "hide_notification": false,
      "id": 219,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_note",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Summary",
      "tooltip": "Optionally, define the note/description of the Remedy form",
      "type_id": 6,
      "uuid": "a977f7a7-ef06-4d38-a4ed-f293b5066989",
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
      "export_key": "actioninvocation/remedy_additional_data",
      "hide_notification": false,
      "id": 220,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_additional_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{\"first_name2\":\"Allen\", \"last_name2\":\"Allbrook\"}",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Additional Data",
      "tooltip": "Addtional key value pairs to send to Remedy. Keys must match the incident schema in the Remedy system",
      "type_id": 6,
      "uuid": "ba597730-d2f3-4476-b131-0d5b0ee8de7e",
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
      "export_key": "actioninvocation/remedy_template",
      "hide_notification": false,
      "id": 221,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_template",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Template",
      "tooltip": "Template to apply to the incident to prefill values",
      "type_id": 6,
      "uuid": "c29d5daa-1a0f-4cc7-882c-f5a2eebab296",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Issue",
          "properties": null,
          "uuid": "2e684665-b725-412c-a797-b71c5e368fcd",
          "value": 56
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
      "export_key": "actioninvocation/remedy_reported_source",
      "hide_notification": false,
      "id": 222,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_reported_source",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Reported Source",
      "tooltip": "The originating source of this Incident. Must be configured with values present in your remedy system.",
      "type_id": 6,
      "uuid": "f9831ec1-c511-455f-a142-2c1155c9130d",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Direct Input",
          "properties": null,
          "uuid": "22d89ff3-db61-4c32-81f7-867772c69c4e",
          "value": 57
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email",
          "properties": null,
          "uuid": "a08b4372-1c1f-412a-bcef-92f78b2dca44",
          "value": 58
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "External Escalation",
          "properties": null,
          "uuid": "fb132e77-f1bd-424e-b652-d6830ab30935",
          "value": 59
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Fax",
          "properties": null,
          "uuid": "dae4c261-9743-4f66-ac16-224ea537e1a0",
          "value": 60
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Self Service",
          "properties": null,
          "uuid": "fd910d74-cb45-4aef-99e7-c9cb30cce6bd",
          "value": 61
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Systems Management",
          "properties": null,
          "uuid": "157c3ab1-568f-4908-8e78-e7728943f6a3",
          "value": 62
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Phone",
          "properties": null,
          "uuid": "684c7a18-f6f1-44e6-9a09-0d92bf7d6be1",
          "value": 63
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Voice Mail",
          "properties": null,
          "uuid": "43056ab2-c3aa-4466-afe0-f7de900c679f",
          "value": 64
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Walk In",
          "properties": null,
          "uuid": "581abf4e-7942-493c-9577-188ecb3f33cf",
          "value": 65
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Web",
          "properties": null,
          "uuid": "9d024012-25e0-464c-8e2c-9eff33d9312d",
          "value": 66
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Other",
          "properties": null,
          "uuid": "fdbbce1d-0f2c-4306-9f39-849100e0f4f8",
          "value": 67
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "BMC Impact Manager Event",
          "properties": null,
          "uuid": "0a4b1301-2064-4694-b88e-b2fefcda91d0",
          "value": 68
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
      "export_key": "actioninvocation/remedy_service_type",
      "hide_notification": false,
      "id": 223,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_service_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Service Type",
      "tooltip": "Service type to assign to the Remedy form",
      "type_id": 6,
      "uuid": "076bf9ea-79be-471e-82d4-cc27de3f3ab7",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "User Service Restoration",
          "properties": null,
          "uuid": "0f0716a5-dd16-46f5-ba69-c0ef3c16245d",
          "value": 69
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "User Service Request",
          "properties": null,
          "uuid": "c54c7389-7298-4481-8e12-194e2aec1467",
          "value": 70
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Infrastructure Restoration",
          "properties": null,
          "uuid": "ea38f484-a8b1-490a-9b81-8f8a706b96ca",
          "value": 71
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Infrastructure Event",
          "properties": null,
          "uuid": "92f32723-f65f-4816-b15c-a80f3f6c0596",
          "value": 72
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Security Incident",
          "properties": null,
          "uuid": "ef5aad57-a740-41dd-8210-0997a4441549",
          "value": 73
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
      "export_key": "actioninvocation/remedy_impact",
      "hide_notification": false,
      "id": 224,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_impact",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Impact",
      "tooltip": "Impact to assign to the Remedy form",
      "type_id": 6,
      "uuid": "209f2896-2427-48ae-a6e8-45803160ebc5",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "1-Extensive/Widespread",
          "properties": null,
          "uuid": "a43a4b7a-54df-4dfe-aea9-dd85e23625d9",
          "value": 74
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "2-Significant/Large",
          "properties": null,
          "uuid": "b84e3042-32ef-41c0-b961-924412a6ffff",
          "value": 75
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "3-Moderate/Limited",
          "properties": null,
          "uuid": "b4d2ffae-2502-4ac3-a175-b1371c5055f5",
          "value": 76
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "4-Minor/Localized",
          "properties": null,
          "uuid": "138d917d-7bcf-4be6-9a6b-5fa979b37176",
          "value": 77
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
      "export_key": "actioninvocation/remedy_support_group",
      "hide_notification": false,
      "id": 225,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_support_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Support Group",
      "tooltip": "Support Organization to assign the incident to",
      "type_id": 6,
      "uuid": "244b09b4-8d97-4197-86e3-08ee195c5f88",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Service Desk",
          "properties": null,
          "uuid": "9e743552-446f-462b-9fa7-5f09be9057cb",
          "value": 78
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SOC",
          "properties": null,
          "uuid": "35deabf9-33cc-45d6-b839-aec131fea4de",
          "value": 79
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
      "export_key": "actioninvocation/remedy_first_name",
      "hide_notification": false,
      "id": 226,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_first_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Customer First Name",
      "tooltip": "First name of the affected customer",
      "type_id": 6,
      "uuid": "3946b0f6-0e2b-447f-a613-5661c444b9e7",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Allen",
          "properties": null,
          "uuid": "a708b165-371b-469b-85f3-f8dc22312de0",
          "value": 80
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
      "export_key": "actioninvocation/remedy_status",
      "hide_notification": false,
      "id": 227,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Status",
      "tooltip": "The status to assign to the Remedy form",
      "type_id": 6,
      "uuid": "3ac24106-39a2-4843-9ba0-a92da2f453cf",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "New",
          "properties": null,
          "uuid": "c8e5ce2b-1081-439b-8db2-ef7d86401e85",
          "value": 81
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Assigned",
          "properties": null,
          "uuid": "0c19bd7b-8bd6-4592-b7ac-bad12f581c68",
          "value": 82
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "In Progress",
          "properties": null,
          "uuid": "0b09fe1c-eba9-4dd9-a8a0-f8260fe56ee7",
          "value": 83
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Pending",
          "properties": null,
          "uuid": "a49f9b73-6b99-4825-aaa8-3656a21bc1e3",
          "value": 84
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Resolved",
          "properties": null,
          "uuid": "aa0b8bc0-943b-415b-84e7-3322d83a38cc",
          "value": 85
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Closed",
          "properties": null,
          "uuid": "916379e0-d4c1-45a5-b383-181367b42050",
          "value": 86
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Cancelled",
          "properties": null,
          "uuid": "3f5c9627-6e3f-429f-b7ac-6a24a6b46e03",
          "value": 87
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
      "export_key": "actioninvocation/remedy_last_name",
      "hide_notification": false,
      "id": 228,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "remedy_last_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "templates": [],
      "text": "Customer Last Name",
      "tooltip": "Last name of the affected customer",
      "type_id": 6,
      "uuid": "5d0908ad-a469-49f1-bf41-7640323b5797",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Allbrook",
          "properties": null,
          "uuid": "a6088a9a-8c00-4ec8-9545-9e1a62b22d46",
          "value": 88
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
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Close an incident ticket in Remedy",
        "format": "text"
      },
      "destination_handle": "fn_remedy",
      "display_name": "Remedy: Close Incident",
      "export_key": "remedy_close_incident",
      "id": 1,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1619535376318,
      "name": "remedy_close_incident",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "uuid": "92d5714d-4d38-485e-82af-cce278830a3e",
      "version": 2,
      "view_items": [
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69575a0b-9ca7-4d57-be72-d7596f1942e1",
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
          "name": "Close a Remedy Incident from Task",
          "object_type": "task",
          "programmatic_name": "close_a_remedy_incident_from_task",
          "tags": [
            {
              "tag_handle": "fn_remedy",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 2
        }
      ]
    },
    {
      "creator": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "description": {
        "content": "Create a new incident in Remedy from a Resilient task.",
        "format": "text"
      },
      "destination_handle": "fn_remedy",
      "display_name": "Remedy: Create Incident",
      "export_key": "remedy_create_incident",
      "id": 2,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 3,
        "name": "a@example.com",
        "type": "user"
      },
      "last_modified_time": 1619535376318,
      "name": "remedy_create_incident",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "uuid": "914c7f97-8d48-4cfb-a411-0da2957950c4",
      "version": 2,
      "view_items": [
        {
          "content": "f934cf75-e9f3-4d1c-bf64-9e4f66f16d7f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "811e99d7-d194-4ce8-86cc-aff5e01ab85c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7377a061-c4eb-4008-9822-710b5d2f2248",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "69575a0b-9ca7-4d57-be72-d7596f1942e1",
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
          "name": "Create a Remedy Incident from Task",
          "object_type": "task",
          "programmatic_name": "create_a_remedy_incident_from_task",
          "tags": [
            {
              "tag_handle": "fn_remedy",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 2,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1619813732529,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1619813732529,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ce056b7d-3e2f-4452-ba8c-f6996926ebcf"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_remedy",
      "name": "fn_remedy",
      "programmatic_name": "fn_remedy",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "users": [],
      "uuid": "251c5949-0bcb-4db3-bbbd-cd2832d7d550"
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
      "display_name": "Remedy Linked Incidents Reference Table",
      "export_key": "remedy_linked_incidents_reference_table",
      "fields": {
        "extra": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "remedy_linked_incidents_reference_table/extra",
          "hide_notification": false,
          "id": 213,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "extra",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Extra",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "a187d2ef-afa1-4fd4-acd3-20ddd53366b6",
          "values": [],
          "width": 50
        },
        "remedy_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "remedy_linked_incidents_reference_table/remedy_id",
          "hide_notification": false,
          "id": 214,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "remedy_id",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Remedy ID",
          "tooltip": "Request ID of the Remedy form entry",
          "type_id": 1000,
          "uuid": "1870ab95-e280-412b-9235-71db10529a6e",
          "values": [],
          "width": 203
        },
        "status": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "remedy_linked_incidents_reference_table/status",
          "hide_notification": false,
          "id": 215,
          "input_type": "textarea",
          "internal": false,
          "is_tracked": false,
          "name": "status",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": true,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "Last status applied to the Remedy Incident",
          "type_id": 1000,
          "uuid": "845c1ce2-88e3-4874-a460-b47ac52cc0fc",
          "values": [],
          "width": 79
        },
        "taskincident_id": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "remedy_linked_incidents_reference_table/taskincident_id",
          "hide_notification": false,
          "id": 216,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "taskincident_id",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Task ID",
          "tooltip": "ID of the Task and its description",
          "type_id": 1000,
          "uuid": "6f1ec8eb-aaec-4b47-b032-1f8f7c901e47",
          "values": [],
          "width": 108
        },
        "timestamp": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "remedy_linked_incidents_reference_table/timestamp",
          "hide_notification": false,
          "id": 217,
          "input_type": "datetimepicker",
          "internal": false,
          "is_tracked": false,
          "name": "timestamp",
          "operation_perms": {},
          "operations": [],
          "order": 0,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Timestamp",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "fb2b36a0-d5e1-4df2-88ae-9da71cab2d95",
          "values": [],
          "width": 138
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
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "type_id": 8,
      "type_name": "remedy_linked_incidents_reference_table",
      "uuid": "b25bfda0-295d-49a1-8a08-99f2e2b8163e"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "close_a_remedy_incident_from_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"close_a_remedy_incident_from_task\" isExecutable=\"true\" name=\"Close a Remedy Incident from Task\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Close an existing incident in Remedy from a task by updating it\u0027s status.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0p0a2oy\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0j4wj9n\" name=\"Remedy: Close Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"92d5714d-4d38-485e-82af-cce278830a3e\"\u003e{\"inputs\":{},\"post_processing_script\":\"noteText = \\\"\u0026lt;h5\u0026gt;Remedy Close Incident:\u0026lt;/h5\u0026gt;\\\"\\n\\nif results[\\\"success\\\"]:\\n  if not results[\\\"content\\\"][\\\"closed\\\"] and not results[\\\"content\\\"][\\\"skipped\\\"]:\\n    \\\"\u0026lt;p\u0026gt;No record of task ID {0} in Remedy. Nothing was updated.\u0026lt;/p\u0026gt;\\\".format(task.id)\\n  else:\\n    if results[\\\"content\\\"][\\\"closed\\\"]:\\n      noteText += \\\"\u0026lt;p\u0026gt;The following incidents were matched in Remedy and the successfully closed:\u0026lt;/p\u0026gt;\\\"\\n      for item in results[\\\"content\\\"][\\\"closed\\\"]:\\n        noteText += \\\"\u0026lt;p\u0026gt;    Incident Number {0}, Request ID: {1}\u0026lt;/p\u0026gt;\\\".format(item[\\\"values\\\"][\\\"Incident Number\\\"], item[\\\"values\\\"][\\\"Request ID\\\"])\\n    if results[\\\"content\\\"][\\\"skipped\\\"]:\\n      noteText += \\\"\u0026lt;p\u0026gt;The following incidents were not able to be closed. Common reasons include that the incident has been previously closed, \\\" \\\\\\n      \\\"the incident has been deleted, or the payload sent to Remedy was incomplete according to the requirements of your specific system:\u0026lt;/p\u0026gt;\\\"\\n      for item in results[\\\"content\\\"][\\\"skipped\\\"]:\\n        noteText += \\\"\u0026lt;p\u0026gt;    Incident Number {0}, Request ID: {1}\u0026lt;/p\u0026gt;\\\".format(item[\\\"values\\\"][\\\"Incident Number\\\"], item[\\\"values\\\"][\\\"Request ID\\\"])\\nelse:\\n  noteText += \\\"\u0026lt;p\u0026gt;Function failed to complete.\u0026lt;/p\u0026gt;\\\"\\n\\nrichText = helper.createRichText(noteText)\\nincident.addNote(richText)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Python 2 compatibility for CP4S 1.6\\ndef mk_str(value, quotes=u\u0027\\\"\u0027):\\n    if value is None:\\n        return \\\"null\\\"\\n    else:\\n        esc_value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n        if quotes:\\n            return u\u0027{0}{1}{0}\u0027.format(quotes, esc_value)\\n        else:\\n            return esc_value\\n\\n\\ninputs.task_id = task.id\\ninputs.incident_id = incident.id\\n\\n# Use this section to add key, value pairs to send to Remedy\\n# These values will be added/updated on the target Remedy incident,\\n# so they must conform with the \\\"HPD:IncidentInterface_Create\\\" schema\\npayload = \\\"\\\"\\\"{\\\"Status_Reason\\\": \\\"foo\\\"}\\\"\\\"\\\"\\n\\ninputs.remedy_payload = payload if payload else \u0027\u0027\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0p0a2oy\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_087loyw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0p0a2oy\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0j4wj9n\"/\u003e\u003cendEvent id=\"EndEvent_1bene68\"\u003e\u003cincoming\u003eSequenceFlow_087loyw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_087loyw\" sourceRef=\"ServiceTask_0j4wj9n\" targetRef=\"EndEvent_1bene68\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_04y1g33\"\u003e\u003ctext\u003e\u003c![CDATA[Create a note reflecting the operation success\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0yah6uc\" sourceRef=\"ServiceTask_0j4wj9n\" targetRef=\"TextAnnotation_04y1g33\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0j4wj9n\" id=\"ServiceTask_0j4wj9n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"285\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0p0a2oy\" id=\"SequenceFlow_0p0a2oy_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"285\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"196.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1bene68\" id=\"EndEvent_1bene68_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"466\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"439\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_087loyw\" id=\"SequenceFlow_087loyw_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"466\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"380.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_04y1g33\" id=\"TextAnnotation_04y1g33_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"278\" x=\"394\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0yah6uc\" id=\"Association_0yah6uc_di\"\u003e\u003comgdi:waypoint x=\"385\" xsi:type=\"omgdc:Point\" y=\"179\"/\u003e\u003comgdi:waypoint x=\"496\" xsi:type=\"omgdc:Point\" y=\"118\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "creator_id": "a@example.com",
      "description": "Close an existing incident in Remedy from a task by updating it\u0027s status.",
      "export_key": "close_a_remedy_incident_from_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1619806685770,
      "name": "Close a Remedy Incident from Task",
      "object_type": "task",
      "programmatic_name": "close_a_remedy_incident_from_task",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "uuid": "f15e4054-1aa8-43d8-8e28-4addfc607117",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "create_a_remedy_incident_from_task",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"create_a_remedy_incident_from_task\" isExecutable=\"true\" name=\"Create a Remedy Incident from Task\"\u003e\u003cdocumentation\u003eCreate a new Incident in Remedy from a Task\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16gpxlj\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0herueu\" name=\"Remedy: Create Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"914c7f97-8d48-4cfb-a411-0da2957950c4\"\u003e{\"inputs\":{},\"post_processing_script\":\"noteText = \\\"\u0026lt;h5\u0026gt; Remedy Create Incident\u0026lt;/h5\u0026gt;\\\"\\n\\ntask_id = task.id\\ntask_name = task.name\\n\\nif results[\\\"success\\\"]:\\n  noteText += \\\"\u0026lt;p\u0026gt;Successfully sent task {0} \\\\\\\"{1}\\\\\\\" to Remedy as Incident Number {2} (UI name) and Request ID {3} (API name).\u0026lt;/p\u0026gt;\\\"\\\\\\n  \\\"\\\".format(task_id, task_name, \\\\\\n  results[\\\"content\\\"][\\\"values\\\"][\\\"Incident Number\\\"], results[\\\"content\\\"][\\\"values\\\"][\\\"Request ID\\\"])\\nelse:\\n  noteText += \\\"\u0026lt;p\u0026gt;Unable to send task {0} \\\\\\\"{1}\\\\\\\" to Remedy\u0026lt;/p\u0026gt;\\\".format(task_id, task_name)\\n  noteText += \\\"\u0026lt;p\u0026gt;Ensure the activity fields and payload you provide meet the minimum requirements in your system for incident creation and routing.\\\"\\n\\nrichText = helper.createRichText(noteText)\\nincident.addNote(richText)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Python 2 compatibility for CP4S 1.6\\ndef mk_str(value, quotes=u\u0027\\\"\u0027):\\n    if value is None:\\n        return \\\"null\\\"\\n    else:\\n        esc_value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n        if quotes:\\n            return u\u0027{0}{1}{0}\u0027.format(quotes, esc_value)\\n        else:\\n            return esc_value\\n\\n\\npayload = u\\\"\\\"\\\"{{ \\\"ApplyTemplate\\\": {},\\n  \\\"First_Name\\\": {},\\n  \\\"Last_Name\\\": {},\\n  \\\"Impact\\\": {},\\n  \\\"Urgency\\\": {},\\n  \\\"Service_Type\\\": {},\\n  \\\"Status\\\": {},\\n  \\\"Reported Source\\\": {},\\n  \\\"Description\\\": {},\\n  \\\"Assigned Support Organization\\\": {},\\n  \\\"additional_data\\\": {}\\n}}\\\"\\\"\\\".format(mk_str(rule.properties.remedy_template),\\n  mk_str(rule.properties.remedy_first_name),\\n  mk_str(rule.properties.remedy_last_name),\\n  mk_str(rule.properties.remedy_impact),\\n  mk_str(rule.properties.remedy_urgency),\\n  mk_str(rule.properties.remedy_service_type),\\n  mk_str(rule.properties.remedy_status),\\n  mk_str(rule.properties.remedy_reported_source),\\n  mk_str(rule.properties.remedy_note),\\n  mk_str(rule.properties.remedy_support_group),\\n  rule.properties.remedy_additional_data.content if rule.properties.remedy_additional_data.content else \\\"null\\\"\\n)\\n\\n# set inputs\\ninputs.task_id = task.id \\ninputs.incident_id = incident.id\\ninputs.remedy_incident_name = task.name\\ninputs.remedy_payload = payload\\n\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16gpxlj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_104rfpk\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_16gpxlj\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0herueu\"/\u003e\u003cendEvent id=\"EndEvent_07o8z3v\"\u003e\u003cincoming\u003eSequenceFlow_104rfpk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_104rfpk\" sourceRef=\"ServiceTask_0herueu\" targetRef=\"EndEvent_07o8z3v\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_048yfkp\"\u003e\u003ctext\u003e\u003c![CDATA[Create a note reflecting the operation success\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cozu34\" sourceRef=\"ServiceTask_0herueu\" targetRef=\"TextAnnotation_048yfkp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0herueu\" id=\"ServiceTask_0herueu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"304\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16gpxlj\" id=\"SequenceFlow_16gpxlj_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"304\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"206\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07o8z3v\" id=\"EndEvent_07o8z3v_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"483\" y=\"180\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"456\" y=\"219\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_104rfpk\" id=\"SequenceFlow_104rfpk_di\"\u003e\u003comgdi:waypoint x=\"404\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"483\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"398.5\" y=\"176.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_048yfkp\" id=\"TextAnnotation_048yfkp_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"278\" x=\"390\" y=\"74\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cozu34\" id=\"Association_1cozu34_di\"\u003e\u003comgdi:waypoint x=\"402\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"505\" xsi:type=\"omgdc:Point\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "creator_id": "a@example.com",
      "description": "Create a new Incident in Remedy from a Task",
      "export_key": "create_a_remedy_incident_from_task",
      "last_modified_by": "a@example.com",
      "last_modified_time": 1619811495703,
      "name": "Create a Remedy Incident from Task",
      "object_type": "task",
      "programmatic_name": "create_a_remedy_incident_from_task",
      "tags": [
        {
          "tag_handle": "fn_remedy",
          "value": null
        }
      ],
      "uuid": "cafb745a-f842-4c43-a4a4-c07b0589ee71",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
