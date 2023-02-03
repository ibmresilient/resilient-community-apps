{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Archive Team",
      "id": 113,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Archive Team",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9f2c0101-5bd5-42e4-8376-32a68521f67d",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for archiving an existing MS team or unarchiving a previously archived team\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a8fc9e48-df3e-4bee-bd54-256a5da62903",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eArchiving a Team for a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_archive_unarchive_a_microsoft_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Archive Team From Task",
      "id": 114,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Archive Team From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6602d0d9-de95-4c75-82f6-482976f95602",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for archiving an existing MS team or unarchiving a previously archived team\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a8fc9e48-df3e-4bee-bd54-256a5da62903",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eEnabling Teams for a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_archive_unarchive_a_microsoft_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Channel",
      "id": 115,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Channel",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "57ff737e-8ef6-441c-862d-314ca998e5b4",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for creating a Channel for an existing Team\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eCreating a Channel for a Team using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the Group or Team name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_teams_channel"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Channel From Task",
      "id": 116,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Channel From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5902308a-0c29-4fda-b07f-f1ea5f09d046",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for creating a Channel for an existing Team\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eCreating a Channel for a Team using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the Group or Team name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_teams_channel"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Group",
      "id": 117,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Group",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f63657ce-d1d9-4459-bb26-e8ee61eb71cf",
      "view_items": [
        {
          "content": "Required attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Additional attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9e46e44-a4db-4190-8e31-f4b959a2568d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Group From Task",
      "id": 118,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Group From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1452ff67-bf9c-41ed-930b-a126783f0eed",
      "view_items": [
        {
          "content": "\u003ch5\u003eRequired\u003c/h5\u003e \n\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003ch5\u003eOptional\u003c/h5\u003e \n\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d0e04cd2-57f9-4a93-a919-b84adb5ff7ac",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Team",
      "id": 119,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Team",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2f6e7c88-8159-422e-8db0-17de597b1ac9",
      "view_items": [
        {
          "content": "Required attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a23555de-b881-45fb-84e8-5094a89e404d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Additional attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d9e46e44-a4db-4190-8e31-f4b959a2568d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_create_a_microsoft_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Create Team From Task",
      "id": 120,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Create Team From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "98b5468c-fba1-4da7-acb3-44d826fa4e99",
      "view_items": [
        {
          "content": "Required attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a23555de-b881-45fb-84e8-5094a89e404d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Additional attributes",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d0e04cd2-57f9-4a93-a919-b84adb5ff7ac",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_create_a_microsoft_team"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Delete Channel",
      "id": 121,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Delete Channel",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0dfe8c3e-cb62-4b74-a632-703806c2d698",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for deleting an existing Microsoft Channel from a Team\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eDeleting a Channel using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_delete_a_teams_channel"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Delete Channel From Task",
      "id": 122,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Delete Channel From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "443e3a8c-f408-49d8-98bd-f16b98ba902c",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for deleting an existing Microsoft Channel from a Team\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eDeleting a Channel using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_delete_a_teams_channel"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Delete Group",
      "id": 123,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Delete Group",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a7581e16-da65-48c3-a21f-8a55a949ceaa",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for deleting an existing Microsoft Group\u003c/p\u003e \u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "371c7b60-656c-4592-a429-dc2408b9b222",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eDeleting a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_delete_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Delete Group From Task",
      "id": 124,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Delete Group From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "0ffc17b8-69d2-4e66-9529-5370607edb5e",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action allows for deleting an existing Microsoft Group\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "371c7b60-656c-4592-a429-dc2408b9b222",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eEnabling Teams for a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_delete_a_microsoft_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Enable Teams for Group",
      "id": 125,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Enable Teams for Group",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9ebf076e-df68-42a4-875b-bf8443834975",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action enables Microsoft Teams functionality for an existing Microsoft Group\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "371c7b60-656c-4592-a429-dc2408b9b222",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eEnabling Teams for a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_enable_microsoft_team_for_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Enable Teams for Group From Task",
      "id": 126,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Enable Teams for Group From Task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4641f200-280b-4f8f-860d-5fbf8d23a5d0",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003eThis action enables Microsoft Teams functionality for an existing Microsoft Group\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "371c7b60-656c-4592-a429-dc2408b9b222",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "27cd3210-769a-4443-b25e-947b4270ebc8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eEnabling Teams for a Group using the \u003cb\u003eGroup Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups with the same name. Use this option if you are sure that the Group name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_enable_microsoft_team_for_group"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Post Incident Information",
      "id": 127,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Post Incident Information",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ab423457-6a80-43e1-ba72-24d7729359dd",
      "view_items": [],
      "workflows": [
        "incident_post_message_to_teams"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Post Task Information",
      "id": 128,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Post Task Information",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a4ea172e-6103-4db1-87a0-17a5e2e27a97",
      "view_items": [],
      "workflows": [
        "task_post_message_to_teams"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Read Channel Messages",
      "id": 129,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Read Channel Messages",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6f8fbeba-f784-48de-bd8e-52eed9c2ead4",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003eImportant!\u003c/span\u003e\u003c/b\u003e  This function allows for access to sensitive data and so it falls under Microsoft\u0027s \u003cb\u003eprotected APIs\u003c/b\u003e . Therefore it requires delegated permission. More information on this can be found in the documentation. \u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Read Message Replies",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cp style=\"font-size: 14.0px;\"\u003eRead each response to a specific message. For effective message extraction, all three values must be present.\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a5070192-c64c-4e92-a571-0c1d200923d8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f08897a2-31aa-4d22-aa7e-82bbe299e7f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Read All Messages",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cp style=\"font-size: 14.0px;\"\u003eRead all messages posted in a Microsoft Channel. The channel name is mandatory and any one of the group attribute must be present.\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eRetrieving messages from a Channel using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "incident_read_a_channels_messages"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "MS Teams: Read Channel Messages From task",
      "id": 130,
      "logic_type": "all",
      "message_destinations": [],
      "name": "MS Teams: Read Channel Messages From task",
      "object_type": "task",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "551966ff-4832-46c2-b0d2-25b775ec7603",
      "view_items": [
        {
          "content": "\u003cp style=\"font-size: 15.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003eImportant!\u003c/span\u003e\u003c/b\u003e  This function allows for access to sensitive data and so it falls under Microsoft\u0027s \u003cb\u003eprotected APIs\u003c/b\u003e . Therefore it requires delegated permission. More information on this can be found in the documentation. \u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Read Message Replies",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cp style=\"font-size: 14.0px;\"\u003eRead each response to a specific message. For effective message extraction, all three values must be present.\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a5070192-c64c-4e92-a571-0c1d200923d8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f08897a2-31aa-4d22-aa7e-82bbe299e7f3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "Read All Messages",
          "element": "header",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cp style=\"font-size: 14.0px;\"\u003eRead all messages posted in a Microsoft Channel. The channel name is mandatory and any one of the group attribute must be present.\u003c/p\u003e\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "80a3cfc0-209d-45d2-a422-54531b7123a8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cdiv style=\"text-align: center;\"\u003e\n\u003ch5\u003e -- OR -- \u003c/h5\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "\u003cbr /\u003e\n\u003cp style=\"font-size: 12.0px;\"\u003e\u003cb\u003e\u003cspan style=\"color: red;\"\u003e*\u003c/span\u003e\u003cu\u003eNote\u003c/u\u003e: \u003c/b\u003eRetrieving messages from a Channel using the \u003cb\u003eGroup/Team Name\u003c/b\u003e attribute is not recommended, as there can exist multiple Groups or Teams with the same name. Use this option if you are sure that the name is unique.\u003c/p\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "task_read_a_channels_messages"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1675436479165,
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
      "export_key": "__function/ms_group_mail_nickname",
      "hide_notification": false,
      "id": 489,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_mail_nickname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_mail_nickname",
      "tooltip": "Unique value, as no two MS Objects can have the same email ID. The mail address need not include the domain suffix (i.e. @example.com)",
      "type_id": 11,
      "uuid": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
      "export_key": "__function/ms_team_name",
      "hide_notification": false,
      "id": 581,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_team_name",
      "tooltip": "Name of the Microsoft Team",
      "type_id": 11,
      "uuid": "8c740ee5-6b2d-4555-be2e-e0dce0fe93fc",
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
      "id": 582,
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
      "tags": [],
      "templates": [],
      "text": "task_id",
      "tooltip": "Unique id of a task assigned while being created",
      "type_id": 11,
      "uuid": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
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
      "export_key": "__function/ms_group_id",
      "hide_notification": false,
      "id": 583,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_id",
      "tooltip": "Unique id assigned to a team while being created",
      "type_id": 11,
      "uuid": "9cefbe23-f9c0-4276-9d61-934a2273e7a9",
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
      "export_key": "__function/add_members_from",
      "hide_notification": false,
      "id": 584,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_from",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "add_members_from",
      "tooltip": "Allows for adding incident or task members to Team/Group",
      "type_id": 11,
      "uuid": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "9602467c-8872-4fe0-9992-20498e6b076e",
          "value": 209
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Task",
          "properties": null,
          "uuid": "40b72b22-9485-47ac-9ade-ee2f97a38515",
          "value": 210
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Incident",
          "properties": null,
          "uuid": "054edd56-3fd2-4068-8779-bcc24e8e2c5d",
          "value": 211
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
      "export_key": "__function/additional_members",
      "hide_notification": false,
      "id": 585,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "additional_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "additional_members",
      "tooltip": "Add members who are not members of this incident or task",
      "type_id": 11,
      "uuid": "caa4ac0d-4869-46bb-b0f5-e585c43b396e",
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
      "export_key": "__function/ms_owners_list",
      "hide_notification": false,
      "id": 586,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_owners_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_owners_list",
      "tooltip": "A list of owners for the group or team",
      "type_id": 11,
      "uuid": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
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
      "export_key": "__function/ms_group_name",
      "hide_notification": false,
      "id": 587,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_group_name",
      "tooltip": "Name of the MS Group",
      "type_id": 11,
      "uuid": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
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
      "export_key": "__function/ms_channel_id",
      "hide_notification": false,
      "id": 509,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_channel_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_channel_id",
      "tooltip": "Unique Id assigned to a channel while being created",
      "type_id": 11,
      "uuid": "da40f919-c1cc-4088-9839-b5e0bd6ae1e3",
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
      "export_key": "__function/teams_mrkdown",
      "hide_notification": false,
      "id": 588,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "teams_mrkdown",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "teams_mrkdown",
      "tooltip": "",
      "type_id": 11,
      "uuid": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
      "export_key": "__function/teams_payload",
      "hide_notification": false,
      "id": 589,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "teams_payload",
      "tooltip": "json of teams conversation message: sections, title, text, facts",
      "type_id": 11,
      "uuid": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
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
      "export_key": "__function/ms_message_id",
      "hide_notification": false,
      "id": 506,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_message_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_message_id",
      "tooltip": "Each message has a unique ID",
      "type_id": 11,
      "uuid": "188e6fd5-670c-469a-832d-81763a065291",
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
      "export_key": "__function/ms_channel_name",
      "hide_notification": false,
      "id": 499,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_channel_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_channel_name",
      "tooltip": "Name of the Microsoft Teams channel",
      "type_id": 11,
      "uuid": "24d9ba06-510e-46fc-b03f-7093e1a07ac7",
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
      "export_key": "__function/ms_groupteam_name",
      "hide_notification": false,
      "id": 500,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_groupteam_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_groupteam_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "31e87c41-6cc5-4a48-809b-69fc8a1d9671",
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
      "id": 590,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "incident_id",
      "tooltip": "Unique id assigned to an incident while being created ",
      "type_id": 11,
      "uuid": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
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
      "export_key": "__function/ms_groupteam_id",
      "hide_notification": false,
      "id": 502,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_groupteam_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_groupteam_id",
      "tooltip": "Unique id assigned to a MS Group or Team while being created",
      "type_id": 11,
      "uuid": "4b0f234f-0474-4334-b146-a42f8b941d59",
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
      "export_key": "__function/archive_operation",
      "hide_notification": false,
      "id": 591,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "archive_operation",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "archive_operation",
      "tooltip": "Specify the operation to be performed",
      "type_id": 11,
      "uuid": "5bc4e7ce-8aa4-42b9-af61-7a9a1c51de1f",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Archive",
          "properties": null,
          "uuid": "11cbdf5e-aa22-4b99-85d3-98790f9de82e",
          "value": 212
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unarchive",
          "properties": null,
          "uuid": "7fd9bd61-5f26-4063-8436-5b686ea4d817",
          "value": 213
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
      "export_key": "__function/ms_description",
      "hide_notification": false,
      "id": 592,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "ms_description",
      "tooltip": "Description for the MS Graph Object (Group / Team / Channel) that is being created",
      "type_id": 11,
      "uuid": "6c7730f3-4872-4709-b60a-cabee7e5a208",
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
      "export_key": "__function/teams_channel",
      "hide_notification": false,
      "id": 593,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "teams_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "teams_channel",
      "tooltip": "Lookup value to channel to post a message",
      "type_id": 11,
      "uuid": "76023ce3-fc17-41d1-9002-2392283ce315",
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
      "export_key": "actioninvocation/ms_group_mail_nickname",
      "hide_notification": false,
      "id": 568,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_mail_nickname",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Mail nickname",
      "tooltip": "This value must be a unique value as no two MS Objects can have the same email ID. The mail address need not include the domain suffix (i.e. @example.com)",
      "type_id": 6,
      "uuid": "80a3cfc0-209d-45d2-a422-54531b7123a8",
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
      "export_key": "actioninvocation/ms_groupteam_id",
      "hide_notification": false,
      "id": 569,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_groupteam_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Group/Team ID",
      "tooltip": "Unique ID assigned to the Group or Team object while being created",
      "type_id": 6,
      "uuid": "955147c1-a5a0-4c6c-ac2a-387bfcb65af9",
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
      "export_key": "actioninvocation/additional_members",
      "hide_notification": false,
      "id": 570,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "additional_members",
      "operation_perms": {},
      "operations": [],
      "placeholder": "user1@example.com, user2@example.com",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Additional members",
      "tooltip": "Add members who are not members of this incident or task",
      "type_id": 6,
      "uuid": "a1cdb642-ebc7-4546-9788-c0f3e973fda7",
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
      "export_key": "actioninvocation/ms_team_name",
      "hide_notification": false,
      "id": 571,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_team_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Team Name",
      "tooltip": "A name for the team.",
      "type_id": 6,
      "uuid": "a23555de-b881-45fb-84e8-5094a89e404d",
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
      "export_key": "actioninvocation/ms_message_id",
      "hide_notification": false,
      "id": 507,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_message_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Message Id",
      "tooltip": "The unique id assigned to a message posted in the Teams channel",
      "type_id": 6,
      "uuid": "a5070192-c64c-4e92-a571-0c1d200923d8",
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
      "export_key": "actioninvocation/archive_operation",
      "hide_notification": false,
      "id": 572,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "archive_operation",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Operation",
      "tooltip": "Specify the operation to be performed",
      "type_id": 6,
      "uuid": "a8fc9e48-df3e-4bee-bd54-256a5da62903",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Archive",
          "properties": null,
          "uuid": "63e99580-094b-4359-ba03-35696f524696",
          "value": 202
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Unarchive",
          "properties": null,
          "uuid": "159d81b7-aae7-44db-a5fb-4b1d1a5a775b",
          "value": 203
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
      "export_key": "actioninvocation/ms_channel_name",
      "hide_notification": false,
      "id": 573,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_channel_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Channel Name",
      "tooltip": "Name of the Microsoft Teams Channel",
      "type_id": 6,
      "uuid": "aa6a0aca-bdd1-4142-89ad-2f467dc395e3",
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
      "export_key": "actioninvocation/ms_owners_list",
      "hide_notification": false,
      "id": 574,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_owners_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "owner1@example.com, owner2@example.com",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Owners",
      "tooltip": "Email addresses of the MS Team/Group Owners.",
      "type_id": 6,
      "uuid": "befdf4d5-dfc1-4763-907a-54ed7fec6821",
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
      "export_key": "actioninvocation/ms_description",
      "hide_notification": false,
      "id": 575,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_description",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Description",
      "tooltip": "Description for the MS Graph Object (Group / Team / Channel) that is being created",
      "type_id": 6,
      "uuid": "c2417b6b-f7bc-4714-9cd9-5266015ac629",
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
      "export_key": "actioninvocation/add_members_task",
      "hide_notification": false,
      "id": 576,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_task",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Add members",
      "tooltip": "Allows for adding incident or task members to Team/Group",
      "type_id": 6,
      "uuid": "d0e04cd2-57f9-4a93-a919-b84adb5ff7ac",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "e54c978e-266e-4c8d-9c09-5de4d5d0f70d",
          "value": 204
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All task members",
          "properties": null,
          "uuid": "97c9273e-5c12-45fc-ae17-c077cf44e25b",
          "value": 205
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All incident members",
          "properties": null,
          "uuid": "3bf0cc9d-09fe-4536-950d-22c47c29ff64",
          "value": 206
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
      "export_key": "actioninvocation/add_members_incident",
      "hide_notification": false,
      "id": 577,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "add_members_incident",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Add members",
      "tooltip": "Allows for adding incident members to Team/Group",
      "type_id": 6,
      "uuid": "d9e46e44-a4db-4190-8e31-f4b959a2568d",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "None",
          "properties": null,
          "uuid": "ab334806-2665-4498-bd3a-e9ff05d62c50",
          "value": 207
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "All incident members",
          "properties": null,
          "uuid": "6ba20604-b094-4fcf-ae8b-6e3141f63d9b",
          "value": 208
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
      "export_key": "actioninvocation/ms_channel_id",
      "hide_notification": false,
      "id": 508,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_channel_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Channel Id",
      "tooltip": "Unique Id assigned to a channel while being created",
      "type_id": 6,
      "uuid": "f08897a2-31aa-4d22-aa7e-82bbe299e7f3",
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
      "export_key": "actioninvocation/ms_group_name",
      "hide_notification": false,
      "id": 578,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Group name",
      "tooltip": "Name of the Group to be created",
      "type_id": 6,
      "uuid": "27cd3210-769a-4443-b25e-947b4270ebc8",
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
      "export_key": "actioninvocation/ms_groupteam_name",
      "hide_notification": false,
      "id": 579,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_groupteam_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Group/Team Name",
      "tooltip": "Name of the Microsoft Group or Team",
      "type_id": 6,
      "uuid": "2fa3eaf4-8500-4a97-91b1-94966fe89b3a",
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
      "export_key": "actioninvocation/ms_group_id",
      "hide_notification": false,
      "id": 580,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "ms_group_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "Microsoft Group Id",
      "tooltip": "If a Microsoft Group already exists, it\u0027s Group ID can be specified to create a team",
      "type_id": 6,
      "uuid": "371c7b60-656c-4592-a429-dc2408b9b222",
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
      "created_date": 1674638830627,
      "description": {
        "content": "Function to archive a MS Team",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Archive Team",
      "export_key": "ms_teams_archive_team",
      "id": 80,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830663,
      "name": "ms_teams_archive_team",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"4dfde5ae-4c27-4461-955d-e90791504987\", \"deletedDateTime\": null, \"classification\": null, \"createdDateTime\": \"2022-11-17T19:38:40Z\", \"creationOptions\": [\"Team\", \"ExchangeProvisioningFlags:3552\"], \"description\": \"Sample\", \"displayName\": \"Admin\", \"expirationDateTime\": null, \"groupTypes\": [\"Unified\"], \"isAssignableToRole\": null, \"mail\": \"Admin@5rf2xs.onmicrosoft.com\", \"mailEnabled\": true, \"mailNickname\": \"Admin\", \"membershipRule\": null, \"membershipRuleProcessingState\": null, \"onPremisesDomainName\": null, \"onPremisesLastSyncDateTime\": null, \"onPremisesNetBiosName\": null, \"onPremisesSamAccountName\": null, \"onPremisesSecurityIdentifier\": null, \"onPremisesSyncEnabled\": null, \"preferredDataLocation\": null, \"preferredLanguage\": null, \"proxyAddresses\": [\"SPO:SPO_6a9b33c4-5b75-4854-8cd8-***********_1d8a5928-8678-408e-ab06-50ca7e01766a\", \"SMTP:Admin@5rf2xs.onmicrosoft.com\"], \"renewedDateTime\": \"2022-11-17T19:38:40Z\", \"resourceBehaviorOptions\": [\"HideGroupInOutlook\", \"SubscribeMembersToCalendarEventsDisabled\", \"WelcomeEmailDisabled\"], \"resourceProvisioningOptions\": [\"Team\"], \"securityEnabled\": false, \"securityIdentifier\": \"S-1-12-1-********-1147227175-132734357-2269728913\", \"theme\": null, \"visibility\": \"Public\", \"onPremisesProvisioningErrors\": [], \"message\": \"Successfully archived Team: Admin\", \"teamsEnabled\": \"Archived\"}, \"raw\": null, \"inputs\": {\"ms_team_name\": \"Admin\", \"archive_operation\": \"Archive\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"appHost\", \"execution_time_ms\": 5367, \"timestamp\": \"2022-11-22 11:21:47\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"deletedDateTime\": {}, \"classification\": {}, \"createdDateTime\": {\"type\": \"string\"}, \"creationOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"description\": {\"type\": \"string\"}, \"displayName\": {\"type\": \"string\"}, \"expirationDateTime\": {}, \"groupTypes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"isAssignableToRole\": {}, \"mail\": {\"type\": \"string\"}, \"mailEnabled\": {\"type\": \"boolean\"}, \"mailNickname\": {\"type\": \"string\"}, \"membershipRule\": {}, \"membershipRuleProcessingState\": {}, \"onPremisesDomainName\": {}, \"onPremisesLastSyncDateTime\": {}, \"onPremisesNetBiosName\": {}, \"onPremisesSamAccountName\": {}, \"onPremisesSecurityIdentifier\": {}, \"onPremisesSyncEnabled\": {}, \"preferredDataLocation\": {}, \"preferredLanguage\": {}, \"proxyAddresses\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"renewedDateTime\": {\"type\": \"string\"}, \"resourceBehaviorOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"resourceProvisioningOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"securityEnabled\": {\"type\": \"boolean\"}, \"securityIdentifier\": {\"type\": \"string\"}, \"theme\": {}, \"visibility\": {\"type\": \"string\"}, \"onPremisesProvisioningErrors\": {\"type\": \"array\"}, \"message\": {\"type\": \"string\"}, \"teamsEnabled\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_team_name\": {\"type\": \"string\"}, \"archive_operation\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "553efbec-00dc-4205-8845-fbda91742028",
      "version": 1,
      "view_items": [
        {
          "content": "5bc4e7ce-8aa4-42b9-af61-7a9a1c51de1f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b0f234f-0474-4334-b146-a42f8b941d59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "31e87c41-6cc5-4a48-809b-69fc8a1d9671",
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
          "name": "Incident: Archive Unarchive A Microsoft Team",
          "object_type": "incident",
          "programmatic_name": "incident_archive_unarchive_a_microsoft_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 88
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Archive Unarchive a Microsoft Team",
          "object_type": "task",
          "programmatic_name": "task_archive_unarchive_a_microsoft_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 102
        }
      ]
    },
    {
      "created_date": 1674638830673,
      "description": {
        "content": "Function to create a MS Channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create Channel",
      "export_key": "ms_teams_create_channel",
      "id": 81,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830700,
      "name": "ms_teams_create_channel",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"@odata.context\": \"https://graph.microsoft.com/v1.0/$metadata#teams(\u00274e8349d3-a5e1-****-****-3d81f5252b7f\u0027)/channels/$entity\", \"id\": \"19:8d4fbf7358174021ae16374572797fce@thread.tacv2\", \"createdDateTime\": \"2022-11-22T12:21:20.4305814Z\", \"displayName\": \"Engineering Team\", \"description\": \"Engineering 2 subteam\", \"isFavoriteByDefault\": false, \"email\": \"\", \"webUrl\": \"https://teams.microsoft.com/l/channel/19%3a8d4fbf7************72797fce%40thread.tacv2/Engineering Team?groupId=4e8349d3-a5e1-****-*****-3d81f5252b7f\u0026tenantId=1d8a5928-8678-408e-ab06-50ca7e01766a\", \"membershipType\": \"standard\", \"status_code\": 201, \"message\": \"Successfully created channel: Engineering Team\"}, \"raw\": null, \"inputs\": {\"ms_channel_name\": \"Engineering Team\", \"ms_group_description\": \"Engineering 2 subteam\", \"ms_groupteam_name\": \"Engineering Team\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"appHost\", \"execution_time_ms\": 9106, \"timestamp\": \"2022-11-22 12:21:20\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"@odata.context\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"createdDateTime\": {\"type\": \"string\"}, \"displayName\": {\"type\": \"string\"}, \"description\": {\"type\": \"string\"}, \"isFavoriteByDefault\": {\"type\": \"boolean\"}, \"email\": {\"type\": \"string\"}, \"webUrl\": {\"type\": \"string\"}, \"membershipType\": {\"type\": \"string\"}, \"status_code\": {\"type\": \"integer\"}, \"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_channel_name\": {\"type\": \"string\"}, \"ms_group_description\": {\"type\": \"string\"}, \"ms_groupteam_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "d89ac27e-9c8b-4383-a4da-3c5f901a74cb",
      "version": 1,
      "view_items": [
        {
          "content": "24d9ba06-510e-46fc-b03f-7093e1a07ac7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6c7730f3-4872-4709-b60a-cabee7e5a208",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b0f234f-0474-4334-b146-a42f8b941d59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "31e87c41-6cc5-4a48-809b-69fc8a1d9671",
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
          "name": "Incident: Create a Teams Channel",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_teams_channel",
          "tags": [],
          "uuid": null,
          "workflow_id": 93
        },
        {
          "actions": [],
          "description": null,
          "name": "task: Create a Teams Channel",
          "object_type": "task",
          "programmatic_name": "task_create_a_teams_channel",
          "tags": [],
          "uuid": null,
          "workflow_id": 99
        }
      ]
    },
    {
      "created_date": 1674638830705,
      "description": {
        "content": "A function to create a Microsoft Group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create group",
      "export_key": "ms_teams_create_group",
      "id": 82,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830731,
      "name": "ms_teams_create_group",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"489acc09-3bac-4c43-a168-544df4bf40ff\", \"deletedDateTime\": null, \"classification\": null, \"createdDateTime\": \"2022-11-15T16:30:37Z\", \"creationOptions\": [], \"description\": \"Incident 2095: MS Teams This is a sample incident created for MS teams in SOAR v45\", \"displayName\": \"SOAR\", \"expirationDateTime\": null, \"groupTypes\": [\"Unified\"], \"isAssignableToRole\": null, \"mail\": \"SOAR@****.onmicrosoft.com\", \"mailEnabled\": true, \"mailNickname\": \"SOAR\", \"membershipRule\": null, \"membershipRuleProcessingState\": null, \"onPremisesDomainName\": null, \"onPremisesLastSyncDateTime\": null, \"onPremisesNetBiosName\": null, \"onPremisesSamAccountName\": null, \"onPremisesSecurityIdentifier\": null, \"onPremisesSyncEnabled\": null, \"preferredDataLocation\": null, \"preferredLanguage\": null, \"proxyAddresses\": [\"SMTP:SOAR@****.onmicrosoft.com\"], \"renewedDateTime\": \"2022-11-15T16:30:37Z\", \"resourceBehaviorOptions\": [], \"resourceProvisioningOptions\": [], \"securityEnabled\": false, \"securityIdentifier\": \"S-1-12-1-1218104329-1279474604-1297377441-4282433524\", \"theme\": null, \"visibility\": \"Public\", \"onPremisesProvisioningErrors\": [], \"teamsEnabled\": false, \"unfoundUsers\": []}, \"raw\": null, \"inputs\": {\"incident_id\": 2095, \"ms_group_description\": \"Incident 2095: MS Teams This is a sample incident created for MS teams in SOAR v45\", \"ms_owners_list\": \"AdminSoarMS@****.onmicrosoft.com\", \"ms_group_name\": \"SOAR\", \"ms_group_mail_nickname\": \"SOAR\", \"add_members_from\": \"Incident\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"Apphost\", \"execution_time_ms\": 20595, \"timestamp\": \"2022-11-15 16:30:46\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"deletedDateTime\": {}, \"classification\": {}, \"createdDateTime\": {\"type\": \"string\"}, \"creationOptions\": {\"type\": \"array\"}, \"description\": {\"type\": \"string\"}, \"displayName\": {\"type\": \"string\"}, \"expirationDateTime\": {}, \"groupTypes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"isAssignableToRole\": {}, \"mail\": {\"type\": \"string\"}, \"mailEnabled\": {\"type\": \"boolean\"}, \"mailNickname\": {\"type\": \"string\"}, \"membershipRule\": {}, \"membershipRuleProcessingState\": {}, \"onPremisesDomainName\": {}, \"onPremisesLastSyncDateTime\": {}, \"onPremisesNetBiosName\": {}, \"onPremisesSamAccountName\": {}, \"onPremisesSecurityIdentifier\": {}, \"onPremisesSyncEnabled\": {}, \"preferredDataLocation\": {}, \"preferredLanguage\": {}, \"proxyAddresses\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"renewedDateTime\": {\"type\": \"string\"}, \"resourceBehaviorOptions\": {\"type\": \"array\"}, \"resourceProvisioningOptions\": {\"type\": \"array\"}, \"securityEnabled\": {\"type\": \"boolean\"}, \"securityIdentifier\": {\"type\": \"string\"}, \"theme\": {}, \"visibility\": {\"type\": \"string\"}, \"onPremisesProvisioningErrors\": {\"type\": \"array\"}, \"teamsEnabled\": {\"type\": \"boolean\"}, \"unfoundUsers\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"incident_id\": {\"type\": \"integer\"}, \"ms_group_description\": {\"type\": \"string\"}, \"ms_owners_list\": {\"type\": \"string\"}, \"ms_group_name\": {\"type\": \"string\"}, \"ms_group_mail_nickname\": {\"type\": \"string\"}, \"add_members_from\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "120d2055-a0de-413b-b5d7-444d289dd469",
      "version": 1,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "caa4ac0d-4869-46bb-b0f5-e585c43b396e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6c7730f3-4872-4709-b60a-cabee7e5a208",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
          "name": "Incident: Create a Microsoft Group",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 86
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Microsoft Group",
          "object_type": "task",
          "programmatic_name": "task_create_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 90
        }
      ]
    },
    {
      "created_date": 1674638830736,
      "description": {
        "content": "Create a Microsoft Team",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Create team",
      "export_key": "ms_teams_create_team",
      "id": 83,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830763,
      "name": "ms_teams_create_team",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"@odata.context\": \"https://graph.microsoft.com/v1.0/$metadata#groups/$entity\", \"id\": \"db7350fc-b6df-4041-b6cd-2cd7588fa7da\", \"deletedDateTime\": null, \"classification\": null, \"createdDateTime\": \"2022-11-16T12:11:47Z\", \"creationOptions\": [\"Team\", \"ExchangeProvisioningFlags:3552\"], \"description\": \"SOARAPPS\", \"displayName\": \"SOARGROUP\", \"expirationDateTime\": null, \"groupTypes\": [\"Unified\"], \"isAssignableToRole\": null, \"mail\": \"soargroup@****.onmicrosoft.com\", \"mailEnabled\": true, \"mailNickname\": \"soargroup\", \"membershipRule\": null, \"membershipRuleProcessingState\": null, \"onPremisesDomainName\": null, \"onPremisesLastSyncDateTime\": null, \"onPremisesNetBiosName\": null, \"onPremisesSamAccountName\": null, \"onPremisesSecurityIdentifier\": null, \"onPremisesSyncEnabled\": null, \"preferredDataLocation\": null, \"preferredLanguage\": null, \"proxyAddresses\": [\"SMTP:soargroup@****.onmicrosoft.com\"], \"renewedDateTime\": \"2022-11-16T12:11:47Z\", \"resourceBehaviorOptions\": [\"HideGroupInOutlook\", \"SubscribeMembersToCalendarEventsDisabled\", \"WelcomeEmailDisabled\"], \"resourceProvisioningOptions\": [\"Team\"], \"securityEnabled\": false, \"securityIdentifier\": \"S-1-12-1-3681767676-1078048479-3610037686-3668414296\", \"theme\": null, \"visibility\": \"Public\", \"onPremisesProvisioningErrors\": [], \"status_code\": 200, \"teamsEnabled\": true, \"unfoundUsers\": null}, \"raw\": null, \"inputs\": {\"ms_team_name\": \"SOARAPPS\", \"incident_id\": 2095, \"ms_owners_list\": \"AdminSoarMS@****.onmicrosoft.com\", \"add_members_from\": \"Incident\", \"ms_team_description\": \"soargroup\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"AppHost\", \"execution_time_ms\": 18257, \"timestamp\": \"2022-11-16 12:11:53\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"@odata.context\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"deletedDateTime\": {}, \"classification\": {}, \"createdDateTime\": {\"type\": \"string\"}, \"creationOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"description\": {\"type\": \"string\"}, \"displayName\": {\"type\": \"string\"}, \"expirationDateTime\": {}, \"groupTypes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"isAssignableToRole\": {}, \"mail\": {\"type\": \"string\"}, \"mailEnabled\": {\"type\": \"boolean\"}, \"mailNickname\": {\"type\": \"string\"}, \"membershipRule\": {}, \"membershipRuleProcessingState\": {}, \"onPremisesDomainName\": {}, \"onPremisesLastSyncDateTime\": {}, \"onPremisesNetBiosName\": {}, \"onPremisesSamAccountName\": {}, \"onPremisesSecurityIdentifier\": {}, \"onPremisesSyncEnabled\": {}, \"preferredDataLocation\": {}, \"preferredLanguage\": {}, \"proxyAddresses\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"renewedDateTime\": {\"type\": \"string\"}, \"resourceBehaviorOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"resourceProvisioningOptions\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"securityEnabled\": {\"type\": \"boolean\"}, \"securityIdentifier\": {\"type\": \"string\"}, \"theme\": {}, \"visibility\": {\"type\": \"string\"}, \"onPremisesProvisioningErrors\": {\"type\": \"array\"}, \"status_code\": {\"type\": \"integer\"}, \"teamsEnabled\": {\"type\": \"boolean\"}, \"unfoundUsers\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_team_name\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"ms_owners_list\": {\"type\": \"string\"}, \"add_members_from\": {\"type\": \"string\"}, \"ms_team_description\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "9acc046d-60f3-4be8-97cf-c966436e6f9b",
      "version": 1,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8c740ee5-6b2d-4555-be2e-e0dce0fe93fc",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d2f9e887-fd44-4b64-98f8-a642b4b1738c",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b246d664-7c89-47a7-bdce-e7bb6cf47321",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "6c7730f3-4872-4709-b60a-cabee7e5a208",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "caa4ac0d-4869-46bb-b0f5-e585c43b396e",
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
          "name": "Incident: Create a Microsoft Team",
          "object_type": "incident",
          "programmatic_name": "incident_create_a_microsoft_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 91
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Create a Microsoft Team",
          "object_type": "task",
          "programmatic_name": "task_create_a_microsoft_team",
          "tags": [],
          "uuid": null,
          "workflow_id": 98
        }
      ]
    },
    {
      "created_date": 1674638830768,
      "description": {
        "content": "Function to create a MS Channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Delete Channel",
      "export_key": "ms_teams_delete_channel",
      "id": 84,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830800,
      "name": "ms_teams_delete_channel",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"status_code\": 204, \"message\": \"Successfully deleted channel: Engineering Team\"}, \"raw\": null, \"inputs\": {\"ms_channel_name\": \"Engineering Team\", \"ms_groupteam_name\": \"Engineering Team\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"appHost\", \"execution_time_ms\": 6253, \"timestamp\": \"2022-11-22 12:31:03\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"status_code\": {\"type\": \"integer\"}, \"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_channel_name\": {\"type\": \"string\"}, \"ms_groupteam_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "2ea7a99c-b4df-4e5d-860f-d2d4d841f3d9",
      "version": 1,
      "view_items": [
        {
          "content": "24d9ba06-510e-46fc-b03f-7093e1a07ac7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b0f234f-0474-4334-b146-a42f8b941d59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "31e87c41-6cc5-4a48-809b-69fc8a1d9671",
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
          "name": "Incident: Delete a Teams Channel",
          "object_type": "incident",
          "programmatic_name": "incident_delete_a_teams_channel",
          "tags": [],
          "uuid": null,
          "workflow_id": 94
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Delete a Teams Channel",
          "object_type": "task",
          "programmatic_name": "task_delete_a_teams_channel",
          "tags": [],
          "uuid": null,
          "workflow_id": 89
        }
      ]
    },
    {
      "created_date": 1674638830808,
      "description": {
        "content": "Delete a Microsoft Group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Delete Group",
      "export_key": "ms_teams_delete_group",
      "id": 85,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830836,
      "name": "ms_teams_delete_group",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"status_code\": 204, \"message\": \"Successfully deleted Group: Production Team\"}, \"raw\": null, \"inputs\": {\"ms_group_mail_nickname\": \"ProductionTeamm@******.onmicrosoft.com\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"AppHost\", \"execution_time_ms\": 2996, \"timestamp\": \"2022-11-22 12:14:11\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"status_code\": {\"type\": \"integer\"}, \"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_group_mail_nickname\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "c710fb72-c934-45ce-9205-e36794fee376",
      "version": 1,
      "view_items": [
        {
          "content": "9cefbe23-f9c0-4276-9d61-934a2273e7a9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
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
          "name": "Incident: Delete a Microsoft Group",
          "object_type": "incident",
          "programmatic_name": "incident_delete_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 101
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Delete a Microsoft Group",
          "object_type": "task",
          "programmatic_name": "task_delete_a_microsoft_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 100
        }
      ]
    },
    {
      "created_date": 1674638830841,
      "description": {
        "content": "Allows for enabling a team for an existing Group",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Enable Team",
      "export_key": "ms_teams_enable_team",
      "id": 86,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830867,
      "name": "ms_teams_enable_team",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"id\": \"764a62f2-b759-4dd9-86e7-1a4949e4b77d\", \"deletedDateTime\": null, \"classification\": null, \"createdDateTime\": \"2022-11-17T15:35:29Z\", \"creationOptions\": [], \"description\": \"This is a sample group\", \"displayName\": \"Engineering Team\", \"expirationDateTime\": null, \"groupTypes\": [\"Unified\"], \"isAssignableToRole\": null, \"mail\": \"example@******.onmicrosoft.com\", \"mailEnabled\": true, \"mailNickname\": \"example\", \"membershipRule\": null, \"membershipRuleProcessingState\": null, \"onPremisesDomainName\": null, \"onPremisesLastSyncDateTime\": null, \"onPremisesNetBiosName\": null, \"onPremisesSamAccountName\": null, \"onPremisesSecurityIdentifier\": null, \"onPremisesSyncEnabled\": null, \"preferredDataLocation\": null, \"preferredLanguage\": null, \"proxyAddresses\": [\"SMTP:example@******.onmicrosoft.com\"], \"renewedDateTime\": \"2022-11-17T15:35:29Z\", \"resourceBehaviorOptions\": [], \"resourceProvisioningOptions\": [], \"securityEnabled\": false, \"securityIdentifier\": \"S-1-12-1-1984586482-1306113881-1226499974-2109203529\", \"theme\": null, \"visibility\": \"Public\", \"onPremisesProvisioningErrors\": [], \"message\": \"Successfully enabled Teams for Group: Engineering Team\", \"teamsEnabled\": true}, \"raw\": null, \"inputs\": {\"ms_group_mail_nickname\": \"EngineeringTeam@******.onmicrosoft.com\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"AppHost\", \"execution_time_ms\": 5220, \"timestamp\": \"2022-11-17 15:37:00\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"deletedDateTime\": {}, \"classification\": {}, \"createdDateTime\": {\"type\": \"string\"}, \"creationOptions\": {\"type\": \"array\"}, \"description\": {\"type\": \"string\"}, \"displayName\": {\"type\": \"string\"}, \"expirationDateTime\": {}, \"groupTypes\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"isAssignableToRole\": {}, \"mail\": {\"type\": \"string\"}, \"mailEnabled\": {\"type\": \"boolean\"}, \"mailNickname\": {\"type\": \"string\"}, \"membershipRule\": {}, \"membershipRuleProcessingState\": {}, \"onPremisesDomainName\": {}, \"onPremisesLastSyncDateTime\": {}, \"onPremisesNetBiosName\": {}, \"onPremisesSamAccountName\": {}, \"onPremisesSecurityIdentifier\": {}, \"onPremisesSyncEnabled\": {}, \"preferredDataLocation\": {}, \"preferredLanguage\": {}, \"proxyAddresses\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"renewedDateTime\": {\"type\": \"string\"}, \"resourceBehaviorOptions\": {\"type\": \"array\"}, \"resourceProvisioningOptions\": {\"type\": \"array\"}, \"securityEnabled\": {\"type\": \"boolean\"}, \"securityIdentifier\": {\"type\": \"string\"}, \"theme\": {}, \"visibility\": {\"type\": \"string\"}, \"onPremisesProvisioningErrors\": {\"type\": \"array\"}, \"message\": {\"type\": \"string\"}, \"teamsEnabled\": {\"type\": \"boolean\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_group_mail_nickname\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "0e597a9e-7ce0-4580-86fa-11204e2f1caf",
      "version": 1,
      "view_items": [
        {
          "content": "d6f67e8d-3562-48a3-8164-c2440b2c70f0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9cefbe23-f9c0-4276-9d61-934a2273e7a9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
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
          "name": "Incident: Enable Microsoft Team for Group",
          "object_type": "incident",
          "programmatic_name": "incident_enable_microsoft_team_for_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 96
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Enable Microsoft Team for Group",
          "object_type": "task",
          "programmatic_name": "task_enable_microsoft_team_for_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 87
        }
      ]
    },
    {
      "created_date": 1674638830872,
      "description": {
        "content": "Post a message to a Microsoft Teams channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Post Message",
      "export_key": "ms_teams_post_message",
      "id": 87,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830914,
      "name": "ms_teams_post_message",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"message\": \"Information successfully posted in channel Engineering\"}, \"raw\": null, \"inputs\": {\"teams_channel\": \"resilient\", \"incident_id\": 2096, \"task_id\": 78, \"teams_mrkdown\": true, \"teams_payload\": \"{ \\\"summary\\\": \\\"SOAR Incident\\\", \\\"sections\\\": [ \\n  { \\\"facts\\\": [ \\n    { \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"Gootloader\\\" }, \\n    { \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"\u003cdiv class=\\\\\\\"rte\\\\\\\"\u003e\u003cdiv\u003eDelivery method: Distributed via web download\u003c/div\u003e\u003cdiv\u003eDropped by: Gootloader\u003c/div\u003e\u003cdiv\u003eLink: \u003ca href=\\\\\\\"https://example.com/gootloadersites\\\\\\\" target=\\\\\\\"_blank\\\\\\\"\u003ehttps://example.com/gootloadersites\u003c/a\u003e\u003c/div\u003e\u003c/div\u003e\\\" }, \\n    { \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"2096\\\" }, \\n    { \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"adminsoarms@5rf2xs.onmicrosoft.com\\\" }, \\n    { \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"Malware\\\" }, \\n    { \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"\\\" }, \\n    { \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"Wed Nov 16 14:35:03 GMT 2022\\\" }, \\n    { \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"Wed Oct 26 00:00:00 IST 2022\\\" }, \\n    { \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"Wed Oct 26 14:25:12 IST 2022\\\" }, \\n    { \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"True\\\" }, \\n    { \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"High\\\" } \\n   ]\\n  },\\n  { \\\"text\\\": \\\"Task\\\", \\\"facts\\\": [ \\n    { \\\"name\\\": \\\"Task\\\", \\\"value\\\": \\\"Research AV vendor databases\\\" }, \\n    { \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"-\\\" },\\n    { \\\"name\\\": \\\"Instructions\\\", \\\"value\\\": \\\"Research AV vendor databases for recent outbreaks, symptoms and remediation guidance based on observed symptoms and findings. Possible source for intelligence include the following.\\n\u003cul\u003e\\n\u003cli\u003eKaspersky: http://www.securelist.com/en/threats/detect \u003c/li\u003e\\n\u003cli\u003eMicrosoft: http://www.microsoft.com/security/portal/threat/threats.aspx \u003c/li\u003e\\n\u003cli\u003eSymantec:  http://example.com/security_response/landing/azlisting.jsp\u003c/li\u003e\\n\u003cli\u003eTrend Micro: http://example.com/us/threatencyclopedia#malware \u003c/li\u003e\\n\u003c/ul\u003e\\\" },\\n    { \\\"name\\\": \\\"Due Date\\\", \\\"value\\\": \\\"-\\\" }\\n    ]\\n  }\\n ] \\n} \\n\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"host\": \"Apphost\", \"execution_time_ms\": 25451, \"timestamp\": \"2022-11-23 12:22:20\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"message\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"teams_channel\": {\"type\": \"string\"}, \"incident_id\": {\"type\": \"integer\"}, \"task_id\": {\"type\": \"integer\"}, \"teams_mrkdown\": {\"type\": \"boolean\"}, \"teams_payload\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "0c8e4497-c131-4d5d-bdf3-3153d30b9bbc",
      "version": 1,
      "view_items": [
        {
          "content": "958f0953-8b6f-4472-b786-b9ae4351ddfe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3f35f1a9-f5d6-440a-a825-66a340aeaefe",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "76023ce3-fc17-41d1-9002-2392283ce315",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "13a24eb1-1c04-4009-a80e-857a5c8dc41f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fa64a099-f3d4-4caa-bd64-72ffdb46414f",
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
          "name": "Incident: Post message to Teams",
          "object_type": "incident",
          "programmatic_name": "incident_post_message_to_teams",
          "tags": [],
          "uuid": null,
          "workflow_id": 95
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Post message to Teams",
          "object_type": "task",
          "programmatic_name": "task_post_message_to_teams",
          "tags": [],
          "uuid": null,
          "workflow_id": 85
        }
      ]
    },
    {
      "created_date": 1670845125280,
      "description": {
        "content": "Read messages from a Teams Channel",
        "format": "text"
      },
      "destination_handle": "fn_teams",
      "display_name": "MS Teams: Read Message",
      "export_key": "ms_teams_read_message",
      "id": 65,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1674638830967,
      "name": "ms_teams_read_message",
      "output_json_example": "{\"raw\": null, \"reason\": null, \"success\": true, \"version\": 2.0, \"content\": [{\"attachments\": [{\"content\": {\"value\": \"It begins with a user searching for specific information in a search engine. In this case, the user had searched for the keywords \\u201cdisclosure agreement real estate transaction\\u201d. A website compromised by Gootkit operators was among the results, meaning that the user did not open this compromised website by chance. Indeed, the operators had tweaked the odds in their favor by using Search Engine Optimization (SEO) poisoning to make this website rank high in the search results, leading the user to visit the compromised website. This also means that the website\\u2019s URL will not be available for long and that a full analysis would be difficult to conduct if not done immediately\"}, \"contentType\": \"application/vnd.microsoft.teams.card.o365connector\", \"contentUrl\": null, \"id\": \"7c0997dc1b1f481ab4cacf3da1ad76ac\", \"name\": null, \"thumbnailUrl\": null}], \"body\": {\"content\": \"\u003cattachment id=\\\"7c0997dc1b1f481ab4cacf3da1ad76ac\\\"\u003e\u003c/attachment\u003e\", \"contentType\": \"html\"}, \"channelIdentity\": {\"channelId\": \"19:2bcae5884bd4439788c6f6639000e7f5@thread.tacv2\", \"teamId\": \"66475ea6-d085-461b-8d25-7818274b6cf0\"}, \"chatId\": null, \"createdDateTime\": \"2022-12-12T21:06:16.484Z\", \"deletedDateTime\": null, \"etag\": \"1670879176484\", \"eventDetail\": null, \"from\": {\"application\": {\"applicationIdentityType\": \"office365Connector\", \"displayName\": \"SOAR\", \"id\": \"203a1e2c-26cc-47ca-83ae-be98f960b6b2\"}, \"device\": null, \"user\": null}, \"id\": \"1670879176484\", \"importance\": \"normal\", \"lastEditedDateTime\": null, \"lastModifiedDateTime\": \"2022-12-12T21:06:16.484Z\", \"locale\": \"en-us\", \"mentions\": [], \"messageType\": \"message\", \"policyViolation\": null, \"reactions\": [], \"replyToId\": null, \"subject\": null, \"summary\": null, \"webUrl\": \"https://teams.microsoft.com/l/message/******\"}, {\"attachments\": [{\"content\": \"{\\r\\n  \\\"summary\\\": \\\"Incoming Webhook is now connected to soarmessages\\\",\\r\\n  \\\"sections\\\": [\\r\\n    {\\r\\n      \\\"activitySubtitle\\\": \\\"\u003cp\u003eMiriam Graham has set up a connection to Incoming Webhook so group members will be notified for this configuration with name \u003cstrong\u003eSOAR\u003c/strong\u003e\u003c/p\u003e\\\",\\r\\n      \\\"activityText\\\": \\\"\\\",\\r\\n      \\\"markdown\\\": true,\\r\\n      \\\"startGroup\\\": false\\r\\n    }\\r\\n  ]\\r\\n}\", \"contentType\": \"application/vnd.microsoft.teams.card.o365connector\", \"contentUrl\": null, \"id\": \"2afcb94fd474482484883803d78a22e1\", \"name\": null, \"thumbnailUrl\": null}], \"body\": {\"content\": \"\u003cattachment id=\\\"2afcb94fd474482484883803d78a22e1\\\"\u003e\u003c/attachment\u003e\", \"contentType\": \"html\"}, \"channelIdentity\": {\"channelId\": \"19:2bcae5884bd4439788c6f6639000e7f5@thread.tacv2\", \"teamId\": \"66475ea6-d085-461b-8d25-7818274b6cf0\"}, \"chatId\": null, \"createdDateTime\": \"2022-12-08T17:27:53.277Z\", \"deletedDateTime\": null, \"etag\": \"1670520473277\", \"eventDetail\": null, \"from\": {\"application\": {\"applicationIdentityType\": \"office365Connector\", \"displayName\": \"SOAR\", \"id\": \"203a1e2c-26cc-47ca-83ae-be98f960b6b2\"}, \"device\": null, \"user\": null}, \"id\": \"1670520473277\", \"importance\": \"normal\", \"lastEditedDateTime\": null, \"lastModifiedDateTime\": \"2022-12-08T17:27:53.277Z\", \"locale\": \"en-us\", \"mentions\": [], \"messageType\": \"message\", \"policyViolation\": null, \"reactions\": [], \"replyToId\": null, \"subject\": null, \"summary\": \"Incoming Webhook is now connected to soarmessages\", \"webUrl\": \"https://teams.microsoft.com/l/messages****\"}, {\"attachments\": [], \"body\": {\"content\": \"Hello!\", \"contentType\": \"text\"}, \"channelIdentity\": {\"channelId\": \"19:2bcae5884bd4439788c6f6639000e7f5@thread.tacv2\", \"teamId\": \"66475ea6-d085-461b-8d25-7818274b6cf0\"}, \"chatId\": null, \"createdDateTime\": \"2022-12-08T11:53:30.188Z\", \"deletedDateTime\": null, \"etag\": \"1670500410188\", \"eventDetail\": null, \"from\": {\"application\": null, \"device\": null, \"user\": {\"displayName\": \"user2\", \"id\": \"6c259569-f2c0-430b-af73-40081b5de19d\", \"tenantId\": \"1d8a5928-8678-408e-ab06-50ca7e01766a\", \"userIdentityType\": \"aadUser\"}}, \"id\": \"1670500410188\", \"importance\": \"normal\", \"lastEditedDateTime\": null, \"lastModifiedDateTime\": \"2022-12-08T11:53:30.188Z\", \"locale\": \"en-us\", \"mentions\": [], \"messageType\": \"message\", \"policyViolation\": null, \"reactions\": [], \"replyToId\": null, \"subject\": null, \"summary\": null, \"webUrl\": \"https://teams.microsoft.com/l/message/******\"}, {\"attachments\": [], \"body\": {\"content\": \"Message 1\", \"contentType\": \"text\"}, \"channelIdentity\": {\"channelId\": \"19:2bcae5884bd4439788c6f6639000e7f5@thread.tacv2\", \"teamId\": \"66475ea6-d085-461b-8d25-7818274b6cf0\"}, \"chatId\": null, \"createdDateTime\": \"2022-12-08T11:15:26.534Z\", \"deletedDateTime\": null, \"etag\": \"1670498126534\", \"eventDetail\": null, \"from\": {\"application\": null, \"device\": null, \"user\": {\"displayName\": \"user1\", \"id\": \"a27544ce-79dc-4d26-a277-d7d4a7cd19cc\", \"tenantId\": \"1d8a5928-8678-408e-ab06-50ca7e01766a\", \"userIdentityType\": \"aadUser\"}}, \"id\": \"1670498126534\", \"importance\": \"normal\", \"lastEditedDateTime\": null, \"lastModifiedDateTime\": \"2022-12-08T11:15:26.534Z\", \"locale\": \"en-us\", \"mentions\": [], \"messageType\": \"message\", \"policyViolation\": null, \"reactions\": [], \"replyToId\": null, \"subject\": null, \"summary\": null, \"webUrl\": \"https://teams.microsoft.com/l/message/*****\"}], \"inputs\": {\"ms_channel_name\": \"ychannel\", \"ms_groupteam_name\": \"soarmessages\"}, \"metrics\": {\"execution_time_ms\": 5030, \"host\": \"apphost\", \"package\": \"fn-teams\", \"package_version\": \"2.0.0\", \"timestamp\": \"2022-12-13 16:56:51\", \"version\": \"1.0\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"replyToId\": {}, \"etag\": {\"type\": \"string\"}, \"messageType\": {\"type\": \"string\"}, \"createdDateTime\": {\"type\": \"string\"}, \"lastModifiedDateTime\": {\"type\": \"string\"}, \"lastEditedDateTime\": {}, \"deletedDateTime\": {}, \"subject\": {}, \"summary\": {\"type\": [\"null\", \"string\"]}, \"chatId\": {}, \"importance\": {\"type\": \"string\"}, \"locale\": {\"type\": \"string\"}, \"webUrl\": {\"type\": \"string\"}, \"policyViolation\": {}, \"eventDetail\": {}, \"from\": {\"type\": \"object\", \"properties\": {\"device\": {}, \"user\": {}, \"application\": {}}}, \"body\": {\"type\": \"object\", \"properties\": {\"contentType\": {\"type\": \"string\"}, \"content\": {\"type\": \"string\"}}}, \"channelIdentity\": {\"type\": \"object\", \"properties\": {\"teamId\": {\"type\": \"string\"}, \"channelId\": {\"type\": \"string\"}}}, \"attachments\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"id\": {\"type\": \"string\"}, \"contentType\": {\"type\": \"string\"}, \"contentUrl\": {}, \"content\": {\"type\": \"string\"}, \"name\": {}, \"thumbnailUrl\": {}}}}, \"mentions\": {\"type\": \"array\"}, \"reactions\": {\"type\": \"array\"}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"ms_channel_name\": {\"type\": \"string\"}, \"ms_groupteam_name\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "789a5606-7fcf-407e-a218-d96aabf5e543",
      "version": 6,
      "view_items": [
        {
          "content": "188e6fd5-670c-469a-832d-81763a065291",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "da40f919-c1cc-4088-9839-b5e0bd6ae1e3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "24d9ba06-510e-46fc-b03f-7093e1a07ac7",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4b0f234f-0474-4334-b146-a42f8b941d59",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "86fbad8b-a5dd-45b8-a7e8-f3f19afce0a6",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "31e87c41-6cc5-4a48-809b-69fc8a1d9671",
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
          "name": "Incident: Read a Channel Messages",
          "object_type": "incident",
          "programmatic_name": "incident_read_a_channels_messages",
          "tags": [],
          "uuid": null,
          "workflow_id": 97
        },
        {
          "actions": [],
          "description": null,
          "name": "Task: Read a Channel Messages",
          "object_type": "task",
          "programmatic_name": "task_read_a_channels_messages",
          "tags": [],
          "uuid": null,
          "workflow_id": 92
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 23,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1675436476401,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1675436476401,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "9fdc0f25-0fa7-4c6c-8fbd-11a02961ab3a",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_teams",
      "name": "fn_teams",
      "programmatic_name": "fn_teams",
      "tags": [],
      "users": [],
      "uuid": "44d59a45-1647-438d-ba45-0bbf0c7506f7"
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
    "build_number": 7899,
    "major": 45,
    "minor": 0,
    "version": "45.0.7899"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_delete_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_delete_a_microsoft_group\" isExecutable=\"true\" name=\"Task: Delete a Microsoft Group\"\u003e\u003cdocumentation\u003eExample workflow to delete a MS Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_07l5bga\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tk0xvp\" name=\"MS Teams: Delete Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c710fb72-c934-45ce-9205-e36794fee376\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text = u\\\"\u0026lt;b\u0026gt;Microsoft Groups:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(content.get(\\\"message\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_group_id:\\n    inputs.ms_group_id = rule.properties.ms_group_id\\n\\nelif rule.properties.ms_group_mail_nickname:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\\nelif rule.properties.ms_group_name:\\n    inputs.ms_group_name = rule.properties.ms_group_name\\n\\nelse:\\n    helper.fail(\\\"Atleast one option must be specified to delete a group\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_07l5bga\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1q6a4wt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1eb2hkm\"\u003e\u003cincoming\u003eSequenceFlow_1q6a4wt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1q6a4wt\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"EndEvent_1eb2hkm\"/\u003e\u003csequenceFlow id=\"SequenceFlow_07l5bga\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tk0xvp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1se85ex\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1p7fhja\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_1se85ex\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10kzg48\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1m6api6\" sourceRef=\"EndEvent_1eb2hkm\" targetRef=\"TextAnnotation_10kzg48\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_142txyo\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nConfirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0lc1nip\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_142txyo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"169\" x=\"95\" y=\"312\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"174\" xsi:type=\"omgdc:Point\" y=\"312\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tk0xvp\" id=\"ServiceTask_1tk0xvp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"363\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1eb2hkm\" id=\"EndEvent_1eb2hkm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"631\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"649\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1q6a4wt\" id=\"SequenceFlow_1q6a4wt_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"502\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07l5bga\" id=\"SequenceFlow_07l5bga_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"235.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1se85ex\" id=\"TextAnnotation_1se85ex_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"144\" x=\"108\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1p7fhja\" id=\"Association_1p7fhja_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"225\" xsi:type=\"omgdc:Point\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10kzg48\" id=\"TextAnnotation_10kzg48_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"143\" x=\"577\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1m6api6\" id=\"Association_1m6api6_di\"\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_142txyo\" id=\"TextAnnotation_142txyo_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"143\" x=\"577\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0lc1nip\" id=\"Association_0lc1nip_di\"\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"593\" xsi:type=\"omgdc:Point\" y=\"89\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to delete a MS Group",
      "export_key": "task_delete_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638833364,
      "name": "Task: Delete a Microsoft Group",
      "object_type": "task",
      "programmatic_name": "task_delete_a_microsoft_group",
      "tags": [],
      "uuid": "77d567ba-50ab-4663-aee4-26c7f90d7b0f",
      "workflow_id": 100
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "task_create_a_microsoft_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_microsoft_team\" isExecutable=\"true\" name=\"Task: Create a Microsoft Team\"\u003e\u003cdocumentation\u003eExample workflow to create a MS Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1oiq2cc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0gte7jh\" name=\"MS Teams: Create team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9acc046d-60f3-4be8-97cf-c966436e6f9b\"\u003e{\"inputs\":{\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"\\nif task:\\n  inputs.task_id = task.id\\n\\ninputs.incident_id = str(incident.id)\\ninputs.ms_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_team_name is None else rule.properties.ms_team_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_task is not None:\\n  _value = rule.properties.add_members_task.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  elif _value == \\\"all task members\\\":\\n    inputs.add_members_from = \\\"Task\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1oiq2cc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vvaq5z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0dph6pf\"\u003e\u003cincoming\u003eSequenceFlow_1vvaq5z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vvaq5z\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"EndEvent_0dph6pf\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1oiq2cc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gte7jh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qchpws\"\u003e\u003ctext\u003e\u003c![CDATA[Outpus:\n----------\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0e2dtli\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"TextAnnotation_0qchpws\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19ww9ld\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e team_name\n-\u003e owners_list\n-\u003e members_list\n-\u003e group_description\n-\u003e additional_members]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18j4hck\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"TextAnnotation_19ww9ld\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1lpcw80\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ak25sa\" sourceRef=\"EndEvent_0dph6pf\" targetRef=\"TextAnnotation_1lpcw80\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"236\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"231\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"191\" x=\"158\" y=\"332\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"247\" xsi:type=\"omgdc:Point\" y=\"332\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gte7jh\" id=\"ServiceTask_0gte7jh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"469\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0dph6pf\" id=\"EndEvent_0dph6pf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"764\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"737\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vvaq5z\" id=\"SequenceFlow_1vvaq5z_di\"\u003e\u003comgdi:waypoint x=\"569\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"670\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"670\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"764\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"640\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1oiq2cc\" id=\"SequenceFlow_1oiq2cc_di\"\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"374\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"344\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qchpws\" id=\"TextAnnotation_0qchpws_di\"\u003e\u003comgdc:Bounds height=\"143\" width=\"186\" x=\"689\" y=\"-41\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0e2dtli\" id=\"Association_0e2dtli_di\"\u003e\u003comgdi:waypoint x=\"569\" xsi:type=\"omgdc:Point\" y=\"185\"/\u003e\u003comgdi:waypoint x=\"754\" xsi:type=\"omgdc:Point\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19ww9ld\" id=\"TextAnnotation_19ww9ld_di\"\u003e\u003comgdc:Bounds height=\"112\" width=\"153\" x=\"194\" y=\"-25\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18j4hck\" id=\"Association_18j4hck_di\"\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"283\" xsi:type=\"omgdc:Point\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1lpcw80\" id=\"TextAnnotation_1lpcw80_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"152\" x=\"706\" y=\"330\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ak25sa\" id=\"Association_0ak25sa_di\"\u003e\u003comgdi:waypoint x=\"782\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"782\" xsi:type=\"omgdc:Point\" y=\"330\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "description": "Example workflow to create a MS Team",
      "export_key": "task_create_a_microsoft_team",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638833123,
      "name": "Task: Create a Microsoft Team",
      "object_type": "task",
      "programmatic_name": "task_create_a_microsoft_team",
      "tags": [],
      "uuid": "ea822586-8b16-48d3-9193-1ad8e9fe8904",
      "workflow_id": 98
    },
    {
      "actions": [],
      "content": {
        "version": 15,
        "workflow_id": "incident_create_a_microsoft_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_microsoft_team\" isExecutable=\"true\" name=\"Incident: Create a Microsoft Team\"\u003e\u003cdocumentation\u003eExample workflow to create a MS Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1oiq2cc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0gte7jh\" name=\"MS Teams: Create team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"9acc046d-60f3-4be8-97cf-c966436e6f9b\"\u003e{\"inputs\":{\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if task:\\n    inputs.task_id = task.id\\n  \\ninputs.incident_id = str(incident.id)\\ninputs.ms_team_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_team_name is None else rule.properties.ms_team_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_incident is not None:\\n  _value = rule.properties.add_members_incident.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1oiq2cc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vvaq5z\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0dph6pf\"\u003e\u003cincoming\u003eSequenceFlow_1vvaq5z\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vvaq5z\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"EndEvent_0dph6pf\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1oiq2cc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gte7jh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qchpws\"\u003e\u003ctext\u003e\u003c![CDATA[Outpus:\n----------\n-\u003e Confirmation message\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0e2dtli\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"TextAnnotation_0qchpws\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_19ww9ld\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e team_name\n-\u003e owners_list\n-\u003e members_list\n-\u003e description\n-\u003e additional_members]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18j4hck\" sourceRef=\"ServiceTask_0gte7jh\" targetRef=\"TextAnnotation_19ww9ld\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1lpcw80\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ak25sa\" sourceRef=\"EndEvent_0dph6pf\" targetRef=\"TextAnnotation_1lpcw80\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"236\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"231\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"177\" x=\"165\" y=\"327\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"327\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gte7jh\" id=\"ServiceTask_0gte7jh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"470\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0dph6pf\" id=\"EndEvent_0dph6pf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"764\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"737\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vvaq5z\" id=\"SequenceFlow_1vvaq5z_di\"\u003e\u003comgdi:waypoint x=\"570\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"764\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"622\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1oiq2cc\" id=\"SequenceFlow_1oiq2cc_di\"\u003e\u003comgdi:waypoint x=\"272\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"470\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"326\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qchpws\" id=\"TextAnnotation_0qchpws_di\"\u003e\u003comgdc:Bounds height=\"167\" width=\"178\" x=\"693\" y=\"-92\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0e2dtli\" id=\"Association_0e2dtli_di\"\u003e\u003comgdi:waypoint x=\"570\" xsi:type=\"omgdc:Point\" y=\"183\"/\u003e\u003comgdi:waypoint x=\"783\" xsi:type=\"omgdc:Point\" y=\"85\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_19ww9ld\" id=\"TextAnnotation_19ww9ld_di\"\u003e\u003comgdc:Bounds height=\"119\" width=\"146\" x=\"181\" y=\"-43\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18j4hck\" id=\"Association_18j4hck_di\"\u003e\u003comgdi:waypoint x=\"470\" xsi:type=\"omgdc:Point\" y=\"182\"/\u003e\u003comgdi:waypoint x=\"254\" xsi:type=\"omgdc:Point\" y=\"81\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1lpcw80\" id=\"TextAnnotation_1lpcw80_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"135\" x=\"714\" y=\"325\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ak25sa\" id=\"Association_0ak25sa_di\"\u003e\u003comgdi:waypoint x=\"782\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"782\" xsi:type=\"omgdc:Point\" y=\"325\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 15,
      "description": "Example workflow to create a MS Team",
      "export_key": "incident_create_a_microsoft_team",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832257,
      "name": "Incident: Create a Microsoft Team",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_microsoft_team",
      "tags": [],
      "uuid": "4dbd2397-ab9d-465e-a7e0-28de2df30f73",
      "workflow_id": 91
    },
    {
      "actions": [],
      "content": {
        "version": 18,
        "workflow_id": "incident_create_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_microsoft_group\" isExecutable=\"true\" name=\"Incident: Create a Microsoft Group\"\u003e\u003cdocumentation\u003eExample workflow to create a MS Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rhfah8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0xcbxw8\" name=\"MS Teams: Create group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"120d2055-a0de-413b-b5d7-444d289dd469\"\u003e{\"inputs\":{\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if task:\\n    inputs.task_id = task.id\\n  \\ninputs.incident_id = str(incident.id)\\ninputs.ms_group_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_group_name is None else rule.properties.ms_group_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_incident is not None:\\n  _value = rule.properties.add_members_incident.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\\n  \\nif rule.properties.ms_group_mail_nickname is not None:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rhfah8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19sx12p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_00djqtl\"\u003e\u003cincoming\u003eSequenceFlow_19sx12p\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_19sx12p\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"EndEvent_00djqtl\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0rhfah8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0xcbxw8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17bn2hx\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group_name\n-\u003e group_mailNickname\n-\u003e owners_list\n-\u003e members_list\n-\u003e group_description\n-\u003e additional_members]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14jwjkk\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"TextAnnotation_17bn2hx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0so7w7l\"\u003e\u003ctext\u003e\u003c![CDATA[Outpus:\n----------\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1wzfeh6\" sourceRef=\"ServiceTask_0xcbxw8\" targetRef=\"TextAnnotation_0so7w7l\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1cot0pb\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1nzxqcp\" sourceRef=\"EndEvent_00djqtl\" targetRef=\"TextAnnotation_1cot0pb\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"145\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"140\" y=\"233\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"160\" x=\"88\" y=\"326\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"163\" xsi:type=\"omgdc:Point\" y=\"238\"/\u003e\u003comgdi:waypoint x=\"163\" xsi:type=\"omgdc:Point\" y=\"326\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0xcbxw8\" id=\"ServiceTask_0xcbxw8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"381\" y=\"176\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_00djqtl\" id=\"EndEvent_00djqtl_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"681\" y=\"198\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"699\" y=\"237\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19sx12p\" id=\"SequenceFlow_19sx12p_di\"\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"681\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"581\" y=\"194\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rhfah8\" id=\"SequenceFlow_0rhfah8_di\"\u003e\u003comgdi:waypoint x=\"181\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"290\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"216\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"305\" y=\"209\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17bn2hx\" id=\"TextAnnotation_17bn2hx_di\"\u003e\u003comgdc:Bounds height=\"137\" width=\"176\" x=\"91\" y=\"-15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14jwjkk\" id=\"Association_14jwjkk_di\"\u003e\u003comgdi:waypoint x=\"381\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"179\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0so7w7l\" id=\"TextAnnotation_0so7w7l_di\"\u003e\u003comgdc:Bounds height=\"145\" width=\"181\" x=\"608\" y=\"-19\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1wzfeh6\" id=\"Association_1wzfeh6_di\"\u003e\u003comgdi:waypoint x=\"481\" xsi:type=\"omgdc:Point\" y=\"198\"/\u003e\u003comgdi:waypoint x=\"674\" xsi:type=\"omgdc:Point\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1cot0pb\" id=\"TextAnnotation_1cot0pb_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"150\" x=\"624\" y=\"325\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1nzxqcp\" id=\"Association_1nzxqcp_di\"\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"234\"/\u003e\u003comgdi:waypoint x=\"699\" xsi:type=\"omgdc:Point\" y=\"325\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 18,
      "description": "Example workflow to create a MS Group",
      "export_key": "incident_create_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638831614,
      "name": "Incident: Create a Microsoft Group",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_microsoft_group",
      "tags": [],
      "uuid": "36c20e30-8577-4109-b019-2e8e280f5798",
      "workflow_id": 86
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "task_enable_microsoft_team_for_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_enable_microsoft_team_for_group\" isExecutable=\"true\" name=\"Task: Enable Microsoft Team for Group\"\u003e\u003cdocumentation\u003eExample workflow to enable a MS Team for a Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Enable Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0e597a9e-7ce0-4580-86fa-11204e2f1caf\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Could not enable Teams for this MS Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams functionality has now been enabled for this Group.\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_group_id:\\n  inputs.ms_group_id = rule.properties.ms_group_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_group_name:\\n  inputs.ms_group_name = rule.properties.ms_group_name\\nelse:\\n  helper.fail(\\\"No input was provided.\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ve9164\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group_id\n-\u003e group_mailbox\n-\u003e group_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1o0m6ub\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0ve9164\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16ec5ou\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\n-\u003e Confirmation message\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14aa4yb\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_16ec5ou\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"148\" x=\"106\" y=\"300\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"300\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"382\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"535\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"245\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"130\" x=\"631\" y=\"301\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"301\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ve9164\" id=\"TextAnnotation_0ve9164_di\"\u003e\u003comgdc:Bounds height=\"109\" width=\"183\" x=\"88\" y=\"-11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1o0m6ub\" id=\"Association_1o0m6ub_di\"\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16ec5ou\" id=\"TextAnnotation_16ec5ou_di\"\u003e\u003comgdc:Bounds height=\"177\" width=\"167\" x=\"612\" y=\"-72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14aa4yb\" id=\"Association_14aa4yb_di\"\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Example workflow to enable a MS Team for a Group",
      "export_key": "task_enable_microsoft_team_for_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1675435447145,
      "name": "Task: Enable Microsoft Team for Group",
      "object_type": "task",
      "programmatic_name": "task_enable_microsoft_team_for_group",
      "tags": [],
      "uuid": "cb62b115-3cf1-40f0-9076-84ddd206b375",
      "workflow_id": 87
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "incident_delete_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_delete_a_microsoft_group\" isExecutable=\"true\" name=\"Incident: Delete a Microsoft Group\"\u003e\u003cdocumentation\u003eExample workflow to delete a MS Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_07l5bga\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1tk0xvp\" name=\"MS Teams: Delete Group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c710fb72-c934-45ce-9205-e36794fee376\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text = u\\\"\u0026lt;b\u0026gt;Microsoft Groups:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(content.get(\\\"message\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_group_id:\\n    inputs.ms_group_id = rule.properties.ms_group_id\\n\\nelif rule.properties.ms_group_mail_nickname:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\\nelif rule.properties.ms_group_name:\\n    inputs.ms_group_name = rule.properties.ms_group_name\\n\\nelse:\\n    helper.fail(\\\"Atleast one option must be specified to delete a group\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_07l5bga\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1q6a4wt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1eb2hkm\"\u003e\u003cincoming\u003eSequenceFlow_1q6a4wt\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1q6a4wt\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"EndEvent_1eb2hkm\"/\u003e\u003csequenceFlow id=\"SequenceFlow_07l5bga\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1tk0xvp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1se85ex\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1p7fhja\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_1se85ex\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10kzg48\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1m6api6\" sourceRef=\"EndEvent_1eb2hkm\" targetRef=\"TextAnnotation_10kzg48\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_142txyo\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nConfirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0lc1nip\" sourceRef=\"ServiceTask_1tk0xvp\" targetRef=\"TextAnnotation_142txyo\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"43\" width=\"169\" x=\"95\" y=\"312\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"174\" xsi:type=\"omgdc:Point\" y=\"312\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1tk0xvp\" id=\"ServiceTask_1tk0xvp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"363\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1eb2hkm\" id=\"EndEvent_1eb2hkm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"631\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"649\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1q6a4wt\" id=\"SequenceFlow_1q6a4wt_di\"\u003e\u003comgdi:waypoint x=\"463\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"502\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07l5bga\" id=\"SequenceFlow_07l5bga_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"235.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1se85ex\" id=\"TextAnnotation_1se85ex_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"144\" x=\"108\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1p7fhja\" id=\"Association_1p7fhja_di\"\u003e\u003comgdi:waypoint x=\"363\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"225\" xsi:type=\"omgdc:Point\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10kzg48\" id=\"TextAnnotation_10kzg48_di\"\u003e\u003comgdc:Bounds height=\"40\" width=\"143\" x=\"577\" y=\"314\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1m6api6\" id=\"Association_1m6api6_di\"\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"314\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_142txyo\" id=\"TextAnnotation_142txyo_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"143\" x=\"577\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0lc1nip\" id=\"Association_0lc1nip_di\"\u003e\u003comgdi:waypoint x=\"461\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"593\" xsi:type=\"omgdc:Point\" y=\"89\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to delete a MS Group",
      "export_key": "incident_delete_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638833486,
      "name": "Incident: Delete a Microsoft Group",
      "object_type": "incident",
      "programmatic_name": "incident_delete_a_microsoft_group",
      "tags": [],
      "uuid": "72deb741-c57f-454a-b304-63a72fb1c751",
      "workflow_id": 101
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "incident_delete_a_teams_channel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_delete_a_teams_channel\" isExecutable=\"true\" name=\"Incident: Delete a Teams Channel\"\u003e\u003cdocumentation\u003eExample workflow to delete a Teams Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Delete Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2ea7a99c-b4df-4e5d-860f-d2d4d841f3d9\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete Microsoft Channel\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channels:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(content.get(\\\"message\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ms_channel_name = rule.properties.ms_channel_name\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1s9nldw\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e channel_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1dknfp0\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_1s9nldw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eivlmh\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nConfirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hyb5g6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0eivlmh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"159\" x=\"100\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"129\" x=\"631\" y=\"303\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"303\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1s9nldw\" id=\"TextAnnotation_1s9nldw_di\"\u003e\u003comgdc:Bounds height=\"98\" width=\"152\" x=\"104\" y=\"-12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1dknfp0\" id=\"Association_1dknfp0_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"256\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eivlmh\" id=\"TextAnnotation_0eivlmh_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"165\" x=\"613\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hyb5g6\" id=\"Association_0hyb5g6_di\"\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"642\" xsi:type=\"omgdc:Point\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to delete a Teams Channel",
      "export_key": "incident_delete_a_teams_channel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832630,
      "name": "Incident: Delete a Teams Channel",
      "object_type": "incident",
      "programmatic_name": "incident_delete_a_teams_channel",
      "tags": [],
      "uuid": "621cb79d-1285-46d8-a65f-28f792be40d7",
      "workflow_id": 94
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "incident_create_a_teams_channel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_create_a_teams_channel\" isExecutable=\"true\" name=\"Incident: Create a Teams Channel\"\u003e\u003cdocumentation\u003eExample workflow to create a Channel for a Microsoft Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Create Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d89ac27e-9c8b-4383-a4da-3c5f901a74cb\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  url   = u\u0027\u0026lt;a href=\\\"{}\\\"\u0026gt;Click here\u0026lt;/a\u0026gt;\u0027.format(content.get(\\\"webUrl\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channel Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Web URL: {}\\\".format(url)\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(True)\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"email\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Membership Type: {}\\\".format(content.get(\\\"membershipType\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ms_channel_name = rule.properties.ms_channel_name if rule.properties.ms_channel_name else f\\\"Incident {incident.id} {incident.name}\\\"\\n\\n\\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0s3nxap\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e Channel name\n-\u003e Channel description\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0axmos6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0s3nxap\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xiuw92\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n---------\n-\u003e Name\n-\u003e Web URL\n-\u003e Description]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1a2o5wb\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0xiuw92\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"158\" x=\"101\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"131\" x=\"630\" y=\"301\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"301\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0s3nxap\" id=\"TextAnnotation_0s3nxap_di\"\u003e\u003comgdc:Bounds height=\"144\" width=\"146\" x=\"107\" y=\"-59\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0axmos6\" id=\"Association_0axmos6_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"85\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xiuw92\" id=\"TextAnnotation_0xiuw92_di\"\u003e\u003comgdc:Bounds height=\"132\" width=\"130\" x=\"631\" y=\"-53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1a2o5wb\" id=\"Association_1a2o5wb_di\"\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"64\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to create a Channel for a Microsoft Team",
      "export_key": "incident_create_a_teams_channel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832506,
      "name": "Incident: Create a Teams Channel",
      "object_type": "incident",
      "programmatic_name": "incident_create_a_teams_channel",
      "tags": [],
      "uuid": "1dfc6db1-c23a-4dc0-ac9b-1e436e2acc4e",
      "workflow_id": 93
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_delete_a_teams_channel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_delete_a_teams_channel\" isExecutable=\"true\" name=\"Task: Delete a Teams Channel\"\u003e\u003cdocumentation\u003eExample workflow to delete a Teams Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Delete Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"2ea7a99c-b4df-4e5d-860f-d2d4d841f3d9\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to delete Microsoft Channel\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channels:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;{}\\\".format(content.get(\\\"message\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ms_channel_name = rule.properties.ms_channel_name\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1s9nldw\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e channel_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1dknfp0\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_1s9nldw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eivlmh\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nConfirmation message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hyb5g6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0eivlmh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"159\" x=\"100\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"129\" x=\"631\" y=\"303\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"303\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1s9nldw\" id=\"TextAnnotation_1s9nldw_di\"\u003e\u003comgdc:Bounds height=\"98\" width=\"152\" x=\"104\" y=\"-12\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1dknfp0\" id=\"Association_1dknfp0_di\"\u003e\u003comgdi:waypoint x=\"390\" xsi:type=\"omgdc:Point\" y=\"174\"/\u003e\u003comgdi:waypoint x=\"256\" xsi:type=\"omgdc:Point\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eivlmh\" id=\"TextAnnotation_0eivlmh_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"165\" x=\"613\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hyb5g6\" id=\"Association_0hyb5g6_di\"\u003e\u003comgdi:waypoint x=\"487\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"642\" xsi:type=\"omgdc:Point\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to delete a Teams Channel",
      "export_key": "task_delete_a_teams_channel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832003,
      "name": "Task: Delete a Teams Channel",
      "object_type": "task",
      "programmatic_name": "task_delete_a_teams_channel",
      "tags": [],
      "uuid": "44f144ed-b2d0-43d9-b80e-d9b720c40ed5",
      "workflow_id": 89
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "incident_read_a_channels_messages",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_read_a_channels_messages\" isExecutable=\"true\" name=\"Incident: Read a Channel Messages\"\u003e\u003cdocumentation\u003eExample workflow to read messages from a MS Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Read Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"789a5606-7fcf-407e-a218-d96aabf5e543\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to read messages from Microsoft Channel\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channels:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"Successfully retrieved \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt; messages \u0026lt;br /\u0026gt;\u0026lt;br /\u0026gt;\\\".format(len(content))\\n  \\n  for message in content:\\n    url   = u\u0027\u0026lt;a href=\\\"{}\\\"\u0026gt;Click here\u0026lt;/a\u0026gt;\u0027.format(message.get(\\\"webUrl\\\"))\\n    text += \\\"Message Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"id\\\"))\\n    text += \\\"Channel Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"channelIdentity\\\").get(\\\"channelId\\\"))\\n    text += \\\"Team Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"channelIdentity\\\").get(\\\"teamId\\\"))\\n  \\n    if message.get(\\\"from\\\"):\\n      user_messages = message.get(\\\"from\\\").get(\\\"user\\\")\\n      if user_messages:\\n        text += \\\"From User : {} \u0026lt;br /\u0026gt;\\\".format(user_messages.get(\\\"displayName\\\"))\\n      else:\\n        text += \\\"From Application : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"from\\\").get(\\\"application\\\").get(\\\"displayName\\\"))\\n  \\n    text += \\\"Body Content : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"body\\\").get(\\\"content\\\"))\\n    text += \\\"Content Type : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"body\\\").get(\\\"contentType\\\"))\\n    text += \\\"Created Time : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"createdDateTime\\\"))\\n    text += \\\"Web URL : {} \u0026lt;br /\u0026gt;\\\".format(url)\\n    text += \\\"\u0026lt;br /\u0026gt;\\\"\\n    \\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_message_id:\\n  inputs.ms_message_id = rule.properties.ms_message_id\\nif rule.properties.ms_channel_id:\\n  inputs.ms_channel_id = rule.properties.ms_channel_id\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nif rule.properties.ms_channel_name:\\n  inputs.ms_channel_name = rule.properties.ms_channel_name\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1s9nldw\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e message_id\n-\u003e channel_id\n-\u003e channel_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1dknfp0\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_1s9nldw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eivlmh\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nAll messages from a channel or replies to a message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hyb5g6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0eivlmh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"159\" x=\"100\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"129\" x=\"631\" y=\"303\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"303\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1s9nldw\" id=\"TextAnnotation_1s9nldw_di\"\u003e\u003comgdc:Bounds height=\"139\" width=\"165\" x=\"91\" y=\"-53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1dknfp0\" id=\"Association_1dknfp0_di\"\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"256\" xsi:type=\"omgdc:Point\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eivlmh\" id=\"TextAnnotation_0eivlmh_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"210\" x=\"591\" y=\"-20\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hyb5g6\" id=\"Association_0hyb5g6_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"54\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Example workflow to read messages from a MS Channel",
      "export_key": "incident_read_a_channels_messages",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1675434162987,
      "name": "Incident: Read a Channel Messages",
      "object_type": "incident",
      "programmatic_name": "incident_read_a_channels_messages",
      "tags": [],
      "uuid": "5a29aa94-a52b-4c99-82a2-9490aede58bc",
      "workflow_id": 97
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_archive_unarchive_a_microsoft_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_archive_unarchive_a_microsoft_team\" isExecutable=\"true\" name=\"Task: Archive Unarchive a Microsoft Team\"\u003e\u003cdocumentation\u003eExample workflow to Archive or unarchive an existing MS Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mmyyd8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1e5tmyy\" name=\"MS Teams: Archive Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"553efbec-00dc-4205-8845-fbda91742028\"\u003e{\"inputs\":{\"5bc4e7ce-8aa4-42b9-af61-7a9a1c51de1f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"11cbdf5e-aa22-4b99-85d3-98790f9de82e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to archive the Microsoft Team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;The Team associated with this Group has now been {}.\u0026lt;br /\u0026gt;\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.archive_operation:\\n  inputs.archive_operation = rule.properties.archive_operation\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\n\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\n\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mmyyd8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tq2ksy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_02twd8l\"\u003e\u003cincoming\u003eSequenceFlow_1tq2ksy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tq2ksy\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"EndEvent_02twd8l\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1mmyyd8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1e5tmyy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0rb46or\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03q7rfn\" sourceRef=\"EndEvent_02twd8l\" targetRef=\"TextAnnotation_0rb46or\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10m8olk\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e team_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_084hb1e\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"TextAnnotation_10m8olk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00uwll4\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15ha2pz\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"TextAnnotation_00uwll4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"175\" x=\"92\" y=\"283\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"283\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1e5tmyy\" id=\"ServiceTask_1e5tmyy_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"354\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02twd8l\" id=\"EndEvent_02twd8l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"645.0007824726134\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"663.0007824726134\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tq2ksy\" id=\"SequenceFlow_1tq2ksy_di\"\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"550\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"550\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"645\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"520\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mmyyd8\" id=\"SequenceFlow_1mmyyd8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"246\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0rb46or\" id=\"TextAnnotation_0rb46or_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"134\" x=\"596\" y=\"290\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03q7rfn\" id=\"Association_03q7rfn_di\"\u003e\u003comgdi:waypoint x=\"663\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"664\" xsi:type=\"omgdc:Point\" y=\"290\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10m8olk\" id=\"TextAnnotation_10m8olk_di\"\u003e\u003comgdc:Bounds height=\"123\" width=\"147\" x=\"106\" y=\"-36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_084hb1e\" id=\"Association_084hb1e_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"84\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00uwll4\" id=\"TextAnnotation_00uwll4_di\"\u003e\u003comgdc:Bounds height=\"167\" width=\"173\" x=\"576\" y=\"-58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15ha2pz\" id=\"Association_15ha2pz_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"576\" xsi:type=\"omgdc:Point\" y=\"87\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to Archive or unarchive an existing MS Team",
      "export_key": "task_archive_unarchive_a_microsoft_team",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638833596,
      "name": "Task: Archive Unarchive a Microsoft Team",
      "object_type": "task",
      "programmatic_name": "task_archive_unarchive_a_microsoft_team",
      "tags": [],
      "uuid": "e5e8b36d-ee76-489d-b890-f78945f82f06",
      "workflow_id": 102
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "incident_post_message_to_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_post_message_to_teams\" isExecutable=\"true\" name=\"Incident: Post message to Teams\"\u003e\u003cdocumentation\u003eExample workflow to post SOAR Incident data to a MS Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tqeuuk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0nrnlka\" name=\"MS Teams: Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"resilient\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to Post message\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n  text = helper.createRichText(text)\\n  incident.addNote(text)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\n\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"SOAR Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code\\n   )\\n\\ninputs.teams_payload = payload\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tqeuuk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14r6yw4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tqeuuk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nrnlka\"/\u003e\u003cendEvent id=\"EndEvent_1cx5ym9\"\u003e\u003cincoming\u003eSequenceFlow_14r6yw4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_14r6yw4\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"EndEvent_1cx5ym9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ing8rr\"\u003e\u003ctext\u003e\u003c![CDATA[Format teams_payload as a json object. See pre-processor script for format.\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cgzb03\" sourceRef=\"ServiceTask_0nrnlka\" targetRef=\"TextAnnotation_0ing8rr\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0aa196j\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ns09fl\" sourceRef=\"EndEvent_1cx5ym9\" targetRef=\"TextAnnotation_0aa196j\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"148\" x=\"102\" y=\"290\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"287\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nrnlka\" id=\"ServiceTask_0nrnlka_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"278\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tqeuuk\" id=\"SequenceFlow_1tqeuuk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"278\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"238\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1cx5ym9\" id=\"EndEvent_1cx5ym9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"457\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"475\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14r6yw4\" id=\"SequenceFlow_14r6yw4_di\"\u003e\u003comgdi:waypoint x=\"378\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"417.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ing8rr\" id=\"TextAnnotation_0ing8rr_di\"\u003e\u003comgdc:Bounds height=\"82\" width=\"207\" x=\"76\" y=\"32\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cgzb03\" id=\"Association_1cgzb03_di\"\u003e\u003comgdi:waypoint x=\"286\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"226\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0aa196j\" id=\"TextAnnotation_0aa196j_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"123\" x=\"413\" y=\"291\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ns09fl\" id=\"Association_0ns09fl_di\"\u003e\u003comgdi:waypoint x=\"475\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"475\" xsi:type=\"omgdc:Point\" y=\"291\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "description": "Example workflow to post SOAR Incident data to a MS Channel",
      "export_key": "incident_post_message_to_teams",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832756,
      "name": "Incident: Post message to Teams",
      "object_type": "incident",
      "programmatic_name": "incident_post_message_to_teams",
      "tags": [],
      "uuid": "abecd789-c436-4006-be07-4d2db698252c",
      "workflow_id": 95
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "incident_archive_unarchive_a_microsoft_team",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_archive_unarchive_a_microsoft_team\" isExecutable=\"true\" name=\"Incident: Archive Unarchive A Microsoft Team\"\u003e\u003cdocumentation\u003eExample workflow to Archive or unarchive an existing MS Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1mmyyd8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1e5tmyy\" name=\"MS Teams: Archive Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"553efbec-00dc-4205-8845-fbda91742028\"\u003e{\"inputs\":{\"5bc4e7ce-8aa4-42b9-af61-7a9a1c51de1f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"11cbdf5e-aa22-4b99-85d3-98790f9de82e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to archive the Microsoft Team\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Team Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;The Team associated with this Group has now been {}.\u0026lt;br /\u0026gt;\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.archive_operation:\\n  inputs.archive_operation = rule.properties.archive_operation\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\n\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\n\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1mmyyd8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tq2ksy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_02twd8l\"\u003e\u003cincoming\u003eSequenceFlow_1tq2ksy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1tq2ksy\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"EndEvent_02twd8l\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1mmyyd8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1e5tmyy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0rb46or\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03q7rfn\" sourceRef=\"EndEvent_02twd8l\" targetRef=\"TextAnnotation_0rb46or\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_10m8olk\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e team_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_084hb1e\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"TextAnnotation_10m8olk\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00uwll4\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_15ha2pz\" sourceRef=\"ServiceTask_1e5tmyy\" targetRef=\"TextAnnotation_00uwll4\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"175\" x=\"92\" y=\"283\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"283\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1e5tmyy\" id=\"ServiceTask_1e5tmyy_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"354\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_02twd8l\" id=\"EndEvent_02twd8l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"645.0007824726134\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"663.0007824726134\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tq2ksy\" id=\"SequenceFlow_1tq2ksy_di\"\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"550\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"550\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"645\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"520\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mmyyd8\" id=\"SequenceFlow_1mmyyd8_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"276\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"354\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"246\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0rb46or\" id=\"TextAnnotation_0rb46or_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"134\" x=\"596\" y=\"290\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03q7rfn\" id=\"Association_03q7rfn_di\"\u003e\u003comgdi:waypoint x=\"663\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"664\" xsi:type=\"omgdc:Point\" y=\"290\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_10m8olk\" id=\"TextAnnotation_10m8olk_di\"\u003e\u003comgdc:Bounds height=\"123\" width=\"147\" x=\"106\" y=\"-36\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_084hb1e\" id=\"Association_084hb1e_di\"\u003e\u003comgdi:waypoint x=\"360\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"253\" xsi:type=\"omgdc:Point\" y=\"84\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00uwll4\" id=\"TextAnnotation_00uwll4_di\"\u003e\u003comgdc:Bounds height=\"167\" width=\"173\" x=\"576\" y=\"-58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_15ha2pz\" id=\"Association_15ha2pz_di\"\u003e\u003comgdi:waypoint x=\"451\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"576\" xsi:type=\"omgdc:Point\" y=\"87\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to Archive or unarchive an existing MS Team",
      "export_key": "incident_archive_unarchive_a_microsoft_team",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638831874,
      "name": "Incident: Archive Unarchive A Microsoft Team",
      "object_type": "incident",
      "programmatic_name": "incident_archive_unarchive_a_microsoft_team",
      "tags": [],
      "uuid": "dd0c9d90-5578-48db-aa10-89c27c1ff54d",
      "workflow_id": 88
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "incident_enable_microsoft_team_for_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"incident_enable_microsoft_team_for_group\" isExecutable=\"true\" name=\"Incident: Enable Microsoft Team for Group\"\u003e\u003cdocumentation\u003eExample workflow to enable a MS Team for a Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Enable Team\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0e597a9e-7ce0-4580-86fa-11204e2f1caf\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Could not enable Teams for this MS Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams functionality has now been enabled for this Group.\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_group_id:\\n  inputs.ms_group_id = rule.properties.ms_group_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_group_name:\\n  inputs.ms_group_name = rule.properties.ms_group_name\\nelse:\\n  helper.fail(\\\"No input was provided.\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ve9164\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group_id\n-\u003e group_mailbox\n-\u003e group_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1o0m6ub\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0ve9164\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16ec5ou\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\n-\u003e Confirmation message\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14aa4yb\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_16ec5ou\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"148\" x=\"106\" y=\"300\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"300\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"382\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"535\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"245\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"130\" x=\"631\" y=\"301\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"301\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ve9164\" id=\"TextAnnotation_0ve9164_di\"\u003e\u003comgdc:Bounds height=\"109\" width=\"183\" x=\"88\" y=\"-11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1o0m6ub\" id=\"Association_1o0m6ub_di\"\u003e\u003comgdi:waypoint x=\"382\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"180\" xsi:type=\"omgdc:Point\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16ec5ou\" id=\"TextAnnotation_16ec5ou_di\"\u003e\u003comgdc:Bounds height=\"177\" width=\"167\" x=\"612\" y=\"-72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14aa4yb\" id=\"Association_14aa4yb_di\"\u003e\u003comgdi:waypoint x=\"482\" xsi:type=\"omgdc:Point\" y=\"187\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Example workflow to enable a MS Team for a Group",
      "export_key": "incident_enable_microsoft_team_for_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1675435346666,
      "name": "Incident: Enable Microsoft Team for Group",
      "object_type": "incident",
      "programmatic_name": "incident_enable_microsoft_team_for_group",
      "tags": [],
      "uuid": "170d6a95-bcdd-4fdf-960e-88dcf2bef892",
      "workflow_id": 96
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "task_create_a_microsoft_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_microsoft_group\" isExecutable=\"true\" name=\"Task: Create a Microsoft Group\"\u003e\u003cdocumentation\u003eExample workflow to create a MS Group\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1uejmnm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q75ylm\" name=\"MS Teams: Create group\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"120d2055-a0de-413b-b5d7-444d289dd469\"\u003e{\"inputs\":{\"b246d664-7c89-47a7-bdce-e7bb6cf47321\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"9602467c-8872-4fe0-9992-20498e6b076e\"}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Group Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(content.get(\\\"teamsEnabled\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"mail\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Visibility: {}\\\".format(content.get(\\\"visibility\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Group Types: {}\\\".format(content.get(\\\"groupTypes\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Created date and time: {}\\\".format(content.get(\\\"createdDateTime\\\"))\\n  if content.get(\\\"unfoundUsers\\\"):\\n    text += u\\\"\u0026lt;br /\u0026gt;*Note the following users were unable to be added to the group: {}\\\".format(content.get(\\\"unfoundUsers\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if task:\\n    inputs.task_id = task.id\\n  \\ninputs.incident_id = str(incident.id)\\ninputs.ms_group_name = \\\"Incident {}: {}\\\".format(str(incident.id),  incident.name) if rule.properties.ms_group_name is None else rule.properties.ms_group_name\\n\\nif rule.properties.ms_owners_list is not None:\\n    inputs.ms_owners_list = rule.properties.ms_owners_list\\n    \\nif rule.properties.add_members_task is not None:\\n  _value = rule.properties.add_members_task.lower().strip()\\n  if _value == \\\"all incident members\\\":\\n    inputs.add_members_from = \\\"Incident\\\"\\n  elif _value == \\\"all task members\\\":\\n    inputs.add_members_from = \\\"Task\\\"\\n  else:\\n    inputs.add_members_from = \\\"None\\\"\\n    \\nif rule.properties.additional_members.content is not None:\\n    inputs.additional_members = rule.properties.additional_members.content\\n    \\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\\n  \\nif rule.properties.ms_group_mail_nickname is not None:\\n    inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1uejmnm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1avwvjy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0g889x3\"\u003e\u003cincoming\u003eSequenceFlow_1avwvjy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1avwvjy\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"EndEvent_0g889x3\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1uejmnm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q75ylm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0j0q9b4\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_19zhmo7\" sourceRef=\"EndEvent_0g889x3\" targetRef=\"TextAnnotation_0j0q9b4\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0jkumgn\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e group_name\n-\u003e group_mailNickname\n-\u003e owners_list\n-\u003e members_list\n-\u003e group_description\n-\u003e additional_members]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1g7juie\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"TextAnnotation_0jkumgn\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1fg0k49\"\u003e\u003ctext\u003e\u003c![CDATA[Outpus:\n----------\n-\u003e Confirmation message\n-\u003e Name\n-\u003e Description\n-\u003e Team Enabled\n-\u003e ID\n-\u003e Mail\n-\u003e Visibility\n-\u003e Group Type\n-\u003e Created Datetime]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_16nskn7\" sourceRef=\"ServiceTask_0q75ylm\" targetRef=\"TextAnnotation_1fg0k49\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"172\" x=\"91\" y=\"327\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"327\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q75ylm\" id=\"ServiceTask_0q75ylm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0g889x3\" id=\"EndEvent_0g889x3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"605.3485838779957\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"623.3485838779957\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1avwvjy\" id=\"SequenceFlow_1avwvjy_di\"\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"605\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"485\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uejmnm\" id=\"SequenceFlow_1uejmnm_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"231.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0j0q9b4\" id=\"TextAnnotation_0j0q9b4_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"132\" x=\"557\" y=\"327\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_19zhmo7\" id=\"Association_19zhmo7_di\"\u003e\u003comgdi:waypoint x=\"623\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"623\" xsi:type=\"omgdc:Point\" y=\"327\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0jkumgn\" id=\"TextAnnotation_0jkumgn_di\"\u003e\u003comgdc:Bounds height=\"133\" width=\"175\" x=\"92\" y=\"-15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1g7juie\" id=\"Association_1g7juie_di\"\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"189\"/\u003e\u003comgdi:waypoint x=\"171\" xsi:type=\"omgdc:Point\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1fg0k49\" id=\"TextAnnotation_1fg0k49_di\"\u003e\u003comgdc:Bounds height=\"169\" width=\"210\" x=\"550\" y=\"-46\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_16nskn7\" id=\"Association_16nskn7_di\"\u003e\u003comgdi:waypoint x=\"455\" xsi:type=\"omgdc:Point\" y=\"188\"/\u003e\u003comgdi:waypoint x=\"629\" xsi:type=\"omgdc:Point\" y=\"127\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "description": "Example workflow to create a MS Group",
      "export_key": "task_create_a_microsoft_group",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638832132,
      "name": "Task: Create a Microsoft Group",
      "object_type": "task",
      "programmatic_name": "task_create_a_microsoft_group",
      "tags": [],
      "uuid": "1a53cc12-68ce-4824-a7ab-c3ddd814f642",
      "workflow_id": 90
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "task_create_a_teams_channel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_create_a_teams_channel\" isExecutable=\"true\" name=\"task: Create a Teams Channel\"\u003e\u003cdocumentation\u003eExample workflow to create a Channel for a Microsoft Team\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Create Channel\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d89ac27e-9c8b-4383-a4da-3c5f901a74cb\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to create Microsoft Group\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  url   = u\u0027\u0026lt;a href=\\\"{}\\\"\u0026gt;Click here\u0026lt;/a\u0026gt;\u0027.format(content.get(\\\"webUrl\\\"))\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channel Details:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"\u0026lt;br /\u0026gt;Name: {}\\\".format(content.get(\\\"displayName\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Web URL: {}\\\".format(url)\\n  text += u\\\"\u0026lt;br /\u0026gt;Description: {}\\\".format(content.get(\\\"description\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Teams Enabled: {}\\\".format(True)\\n  text += u\\\"\u0026lt;br /\u0026gt;ID: {}\\\".format(content.get(\\\"id\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Mail: {}\\\".format(content.get(\\\"email\\\"))\\n  text += u\\\"\u0026lt;br /\u0026gt;Membership Type: {}\\\".format(content.get(\\\"membershipType\\\"))\\n\\nnote = helper.createRichText(text)\\ntask.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.ms_channel_name = rule.properties.ms_channel_name if rule.properties.ms_channel_name else f\\\"Incident {incident.id} {incident.name}\\\"\\n\\n\\nif rule.properties.ms_description is not None:\\n    inputs.ms_description = rule.properties.ms_description\\nelse:\\n    description = incident.description.content if incident.description else \\\"\\\"\\n    inputs.ms_description = f\\\"Incident {incident.id}: {incident.name} {description}\\\"\\n\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nelif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nelif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\nelse:\\n  helper.fail(\\\"No input was provided\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0s3nxap\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e Channel name\n-\u003e Channel description\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0axmos6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0s3nxap\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xiuw92\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n---------\n-\u003e Name\n-\u003e Web URL\n-\u003e Description]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1a2o5wb\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0xiuw92\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"33\" width=\"158\" x=\"101\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"35\" width=\"131\" x=\"630\" y=\"301\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"301\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0s3nxap\" id=\"TextAnnotation_0s3nxap_di\"\u003e\u003comgdc:Bounds height=\"144\" width=\"146\" x=\"107\" y=\"-59\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0axmos6\" id=\"Association_0axmos6_di\"\u003e\u003comgdi:waypoint x=\"389\" xsi:type=\"omgdc:Point\" y=\"175\"/\u003e\u003comgdi:waypoint x=\"252\" xsi:type=\"omgdc:Point\" y=\"85\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xiuw92\" id=\"TextAnnotation_0xiuw92_di\"\u003e\u003comgdc:Bounds height=\"132\" width=\"130\" x=\"631\" y=\"-53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1a2o5wb\" id=\"Association_1a2o5wb_di\"\u003e\u003comgdi:waypoint x=\"484\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"631\" xsi:type=\"omgdc:Point\" y=\"64\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "Example workflow to create a Channel for a Microsoft Team",
      "export_key": "task_create_a_teams_channel",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638833245,
      "name": "task: Create a Teams Channel",
      "object_type": "task",
      "programmatic_name": "task_create_a_teams_channel",
      "tags": [],
      "uuid": "12c2ac34-55d9-428c-99e6-39f48ed776b6",
      "workflow_id": 99
    },
    {
      "actions": [],
      "content": {
        "version": 14,
        "workflow_id": "task_post_message_to_teams",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_post_message_to_teams\" isExecutable=\"true\" name=\"Task: Post message to Teams\"\u003e\u003cdocumentation\u003eExample workflow to post a SOAR Task information to a MS Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0q5lshb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_17n68bf\" name=\"MS Teams: Post Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0c8e4497-c131-4d5d-bdf3-3153d30b9bbc\"\u003e{\"inputs\":{\"76023ce3-fc17-41d1-9002-2392283ce315\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"resilient\"}},\"fa64a099-f3d4-4caa-bd64-72ffdb46414f\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to Post message\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n  text = helper.createRichText(text)\\n  task.addNote(str(text))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"from java.util import Date\\n\\ninputs.incident_id = incident.id\\ninputs.task_id = task.id\\n\\\"\\\"\\\"\\nformat of a payload. * = optional\\n{ \\\"title\\\"*: xx, \\n  \\\"summary\\\": xx, \\n  \\\"sections\\\": [{ \\\"title\\\"*: yy, \\\"text\\\"*: yy, \\n                        \\\"facts\\\"*: [{\\\"name\\\": zz, \\\"value\\\": zz}]\\n              }]\\n}\\n\\\"\\\"\\\"\\n\\npayload = u\\\"\\\"\\\"{{ \\\"summary\\\": \\\"SOAR Incident\\\", \\\"sections\\\": [ \\n  {{ \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Name\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Description\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Id\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Types\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"NIST Attack Vectors\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Create Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Date Occurred\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Discovered Date\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Confirmed\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Severity\\\", \\\"value\\\": \\\"{}\\\" }} \\n   ]\\n  }},\\n  {{ \\\"text\\\": \\\"Task\\\", \\\"facts\\\": [ \\n    {{ \\\"name\\\": \\\"Task\\\", \\\"value\\\": \\\"{}\\\" }}, \\n    {{ \\\"name\\\": \\\"Owner\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Instructions\\\", \\\"value\\\": \\\"{}\\\" }},\\n    {{ \\\"name\\\": \\\"Due Date\\\", \\\"value\\\": \\\"{}\\\" }}\\n    ]\\n  }}\\n ] \\n}} \\n\\\"\\\"\\\".format(incident.name, incident.description.content.replace(\u0027\\\"\u0027, \u0027\\\\\\\\\\\"\u0027) if incident.description else \\\"-\\\", incident.id,\\n   incident.owner_id if incident.owner_id else \\\"-\\\",\\n   \\\", \\\".join(str(x) for x in incident.incident_type_ids), \\\", \\\".join(str(x) for x in incident.nist_attack_vectors),\\n   Date(incident.create_date), Date(incident.start_date) if incident.start_date else \\\"-\\\", Date(incident.discovered_date),\\n   \\\"True\\\" if incident.confirmed else \\\"False\\\",\\n   \\\"-\\\" if not incident.severity_code else incident.severity_code,\\n   task.name, task.owner_id if task.owner_id else \\\"-\\\", task.instructions.content.replace(\u0027\\\"\u0027, \\\"\u0027\\\") if task.instructions else \\\"-\\\", Date(task.due_date) if task.due_date else \\\"-\\\"\\n   )\\n\\ninputs.teams_payload = payload\",\"pre_processing_script_language\":\"python\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0q5lshb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1j9da45\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0q5lshb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_17n68bf\"/\u003e\u003cendEvent id=\"EndEvent_1d26c7r\"\u003e\u003cincoming\u003eSequenceFlow_1j9da45\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1j9da45\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"EndEvent_1d26c7r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1q8nu40\"\u003e\u003ctext\u003eFormat teams_payload as a json object. See pre-processor script for format.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1925sdu\" sourceRef=\"ServiceTask_17n68bf\" targetRef=\"TextAnnotation_1q8nu40\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17n68bf\" id=\"ServiceTask_17n68bf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"251\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q5lshb\" id=\"SequenceFlow_0q5lshb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"251\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1d26c7r\" id=\"EndEvent_1d26c7r_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"415\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"433\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1j9da45\" id=\"SequenceFlow_1j9da45_di\"\u003e\u003comgdi:waypoint x=\"351\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"415\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"383\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1q8nu40\" id=\"TextAnnotation_1q8nu40_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"185\" x=\"130\" y=\"68\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1925sdu\" id=\"Association_1925sdu_di\"\u003e\u003comgdi:waypoint x=\"271\" xsi:type=\"omgdc:Point\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"249\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 14,
      "description": "Example workflow to post a SOAR Task information to a MS Channel",
      "export_key": "task_post_message_to_teams",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1674638831423,
      "name": "Task: Post message to Teams",
      "object_type": "task",
      "programmatic_name": "task_post_message_to_teams",
      "tags": [],
      "uuid": "2500846e-793a-4f40-8945-004fd7a736b6",
      "workflow_id": 85
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "task_read_a_channels_messages",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"task_read_a_channels_messages\" isExecutable=\"true\" name=\"Task: Read a Channel Messages\"\u003e\u003cdocumentation\u003eExample workflow to read messages from a MS Channel\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_16uh319\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1022ens\" name=\"MS Teams: Read Message\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"789a5606-7fcf-407e-a218-d96aabf5e543\"\u003e{\"inputs\":{},\"post_processing_script\":\"content = results.get(\\\"content\\\")\\n\\nif not results.success:\\n  text = u\\\"Unable to read messages from Microsoft Channel\\\"\\n  fail_reason = results.reason\\n  if fail_reason:\\n    text = u\\\"{0}:\\\\n\\\\tFailure reason: {1}\\\".format(text, fail_reason)\\n    \\nelse:\\n  text  = u\\\"\u0026lt;b\u0026gt;Microsoft Channels:\u0026lt;/b\u0026gt;\u0026lt;br /\u0026gt;\\\"\\n  text += u\\\"Successfully retrieved \u0026lt;b\u0026gt;{}\u0026lt;/b\u0026gt; messages \u0026lt;br /\u0026gt;\u0026lt;br /\u0026gt;\\\".format(len(content))\\n  \\n  for message in content:\\n    url   = u\u0027\u0026lt;a href=\\\"{}\\\"\u0026gt;Click here\u0026lt;/a\u0026gt;\u0027.format(message.get(\\\"webUrl\\\"))\\n    text += \\\"Message Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"id\\\"))\\n    text += \\\"Channel Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"channelIdentity\\\").get(\\\"channelId\\\"))\\n    text += \\\"Team Id : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"channelIdentity\\\").get(\\\"teamId\\\"))\\n  \\n    if message.get(\\\"from\\\"):\\n      user_messages = message.get(\\\"from\\\").get(\\\"user\\\")\\n      if user_messages:\\n        text += \\\"From User : {} \u0026lt;br /\u0026gt;\\\".format(user_messages.get(\\\"displayName\\\"))\\n      else:\\n        text += \\\"From Application : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"from\\\").get(\\\"application\\\").get(\\\"displayName\\\"))\\n  \\n    text += \\\"Body Content : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"body\\\").get(\\\"content\\\"))\\n    text += \\\"Content Type : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"body\\\").get(\\\"contentType\\\"))\\n    text += \\\"Created Time : {} \u0026lt;br /\u0026gt;\\\".format(message.get(\\\"createdDateTime\\\"))\\n    text += \\\"Web URL : {} \u0026lt;br /\u0026gt;\\\".format(url)\\n    text += \\\"\u0026lt;br /\u0026gt;\\\"\\n    \\nnote = helper.createRichText(text)\\nincident.addNote(note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if rule.properties.ms_message_id:\\n  inputs.ms_message_id = rule.properties.ms_message_id\\nif rule.properties.ms_channel_id:\\n  inputs.ms_channel_id = rule.properties.ms_channel_id\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nif rule.properties.ms_channel_name:\\n  inputs.ms_channel_name = rule.properties.ms_channel_name\\nif rule.properties.ms_groupteam_id:\\n  inputs.ms_groupteam_id = rule.properties.ms_groupteam_id\\nif rule.properties.ms_group_mail_nickname:\\n  inputs.ms_group_mail_nickname = rule.properties.ms_group_mail_nickname\\nif rule.properties.ms_groupteam_name:\\n  inputs.ms_groupteam_name = rule.properties.ms_groupteam_name\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_16uh319\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_109ugi5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_07fzmrb\"\u003e\u003cincoming\u003eSequenceFlow_109ugi5\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_109ugi5\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"EndEvent_07fzmrb\"/\u003e\u003csequenceFlow id=\"SequenceFlow_16uh319\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1022ens\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_083j983\"\u003e\u003ctext\u003e\u003c![CDATA[\nWorkflow ends here\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_023kete\" sourceRef=\"EndEvent_07fzmrb\" targetRef=\"TextAnnotation_083j983\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1s9nldw\"\u003e\u003ctext\u003e\u003c![CDATA[Inputs:\n---------\n-\u003e message_id\n-\u003e channel_id\n-\u003e channel_name\n-\u003e group/team_id\n-\u003e group_mailbox\n-\u003e group/team_name]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1dknfp0\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_1s9nldw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0eivlmh\"\u003e\u003ctext\u003e\u003c![CDATA[Outputs:\n----------\nAll messages from a channel or replies to a message\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hyb5g6\" sourceRef=\"ServiceTask_1022ens\" targetRef=\"TextAnnotation_0eivlmh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"31\" width=\"159\" x=\"100\" y=\"302\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"176\" xsi:type=\"omgdc:Point\" y=\"223\"/\u003e\u003comgdi:waypoint x=\"175\" xsi:type=\"omgdc:Point\" y=\"302\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1022ens\" id=\"ServiceTask_1022ens_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"388\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_07fzmrb\" id=\"EndEvent_07fzmrb_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"678\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"696\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_109ugi5\" id=\"SequenceFlow_109ugi5_di\"\u003e\u003comgdi:waypoint x=\"488\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"678\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"538\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16uh319\" id=\"SequenceFlow_16uh319_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"388\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"248\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_083j983\" id=\"TextAnnotation_083j983_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"129\" x=\"631\" y=\"303\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_023kete\" id=\"Association_023kete_di\"\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"224\"/\u003e\u003comgdi:waypoint x=\"696\" xsi:type=\"omgdc:Point\" y=\"303\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1s9nldw\" id=\"TextAnnotation_1s9nldw_di\"\u003e\u003comgdc:Bounds height=\"139\" width=\"165\" x=\"91\" y=\"-53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1dknfp0\" id=\"Association_1dknfp0_di\"\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"256\" xsi:type=\"omgdc:Point\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0eivlmh\" id=\"TextAnnotation_0eivlmh_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"210\" x=\"591\" y=\"-20\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hyb5g6\" id=\"Association_0hyb5g6_di\"\u003e\u003comgdi:waypoint x=\"485\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"649\" xsi:type=\"omgdc:Point\" y=\"54\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example workflow to read messages from a MS Channel",
      "export_key": "task_read_a_channels_messages",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1675435576834,
      "name": "Task: Read a Channel Messages",
      "object_type": "task",
      "programmatic_name": "task_read_a_channels_messages",
      "tags": [],
      "uuid": "eacb5553-d133-4fd7-ac28-90c19a39d401",
      "workflow_id": 92
    }
  ],
  "workspaces": []
}
